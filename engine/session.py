"""Session mode: the daily shows made by scheduled Claude Code sessions (Routines) on the account's Claude plan.

No API keys: Claude in the session does the research, writing and fact-checking, and schedules the posts through the
Metricool connector. This script does everything else: the plan, topic picks, rendering, hosting and the state file.
The routine prompts are in ROUTINES.md.

  python engine/session.py setup                 # install ffmpeg, Python and Node packages, the voice model (idempotent)
  python engine/session.py next [--until 14:00]  # claim the next slot to make; prints its task file (or DONE)
  python engine/session.py fallback <slot>       # a news slot had no confirmed story: switch it to its evergreen show
  python engine/session.py build <slot> <script.json>   # sanitize, render, host; prints the Metricool posts to create
  python engine/session.py record <slot> scheduled|skipped|failed [--note ...] [--ids ...]
  python engine/session.py status                # today's slots and their state

Slots, times, lead times and the state file are shared with daily.py (the GitHub Actions version of the same plan).
"""
import argparse, datetime as dt, json, os, shutil, subprocess, sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__)); CON = os.path.join(HERE, "concepts")
sys.path.insert(0, HERE); sys.path.insert(0, CON)
import daily
from daily import TZ, AUTO, slots, kind, load_state, save, pull, host, chapters, FALLBACK

ET = ZoneInfo("America/New_York")
MIN_LEAD = dt.timedelta(minutes=20)         # a slot still being made this close to its time posts a little late instead
STALE = dt.timedelta(hours=3)               # a "building" claim older than this is from a session that died
NEWS = ("morning", "bigstory", "lf-big")


def sh(*cmd, **kw):
    print("+", " ".join(cmd), flush=True); return subprocess.run(cmd, **kw)


def setup():
    if not shutil.which("ffmpeg"):
        sh("bash", "-c", "(sudo -n true 2>/dev/null && S=sudo || S=); $S apt-get update -qq && $S apt-get install -y -qq ffmpeg", check=True)
    sh(sys.executable, "-m", "pip", "install", "-q", "-r", os.path.join(HERE, "requirements.txt"), check=True)
    if not os.path.isdir(os.path.join(HERE, "node_modules", "playwright")):
        sh("npm", "install", "--silent", cwd=HERE, check=True)
    if not os.path.exists("/opt/pw-browsers/chromium"):
        sh("npx", "playwright", "install", "--with-deps", "chromium", cwd=HERE, check=True)
    sh("bash", os.path.join(HERE, "setup_models.sh"), check=True)
    print("SETUP OK")


def slot_id(date, show): return f"{date}-{show}"


def task_text(show, content, topic, now, sid):
    """Everything the session needs to research, write and check one video."""
    import studio
    k = studio.SHOWS[content][0]
    schema = os.path.join(AUTO, f"{sid}.schema.json"); json.dump(studio.SCRIPT, open(schema, "w"), indent=1)
    news = content in NEWS
    return f"""# {sid}: {content} ({'long-form YouTube video' if k == 'long' else 'vertical short'})

You are making one FinancePros TV video. Work in this order and do not skip the fact-check.

## 1. Research
{studio.BRAND}

{studio.research_prompt(content, now, topic)}

Use web search. Save the brief (facts, numbers with dates, a chartable data series, SOURCES) to:
  {os.path.join(AUTO, sid + '.research.md')}
{"If nothing is confirmed and important, run: python engine/session.py fallback " + show + "  and follow the new task it prints." if news else ""}

## 2. Script
{studio.write_prompt(content, "(the brief you saved in step 1)", now, topic)}

Write ONE JSON object that matches the JSON schema in {schema}
and save it to:  {os.path.join(AUTO, sid + '.raw.json')}

## 3. Fact-check (independent)
Launch a subagent (Agent tool) that has not seen your work. Give it the script's lines, on-screen values, cover and post text, and
this instruction: "Independently verify every factual claim, number and chart data point with web search (do not trust the brief).
Also flag: stale news, advice or price predictions, political opinion, a cover or title the video doesn't pay off, math errors in
worked examples, and any on-screen value that differs from the spoken one. List each issue. Finish with exactly one line:
VERDICT: PASS or VERDICT: FAIL." Fix every issue it lists and check again (at most 2 rounds). Save its last report to
  {os.path.join(AUTO, sid + '.factcheck.md')}
If it still fails: python engine/session.py record {show} failed --note "fact-check"   and go to the next slot.

## 4. Build and schedule
  python engine/session.py build {show} {os.path.join(AUTO, sid + '.raw.json')}
It renders the video, hosts it and prints the Metricool posts. Create each one with the Metricool createScheduledPost tool
(blogId 7091438): pass "date" and "info" exactly as printed (info as a JSON string). Then:
  python engine/session.py record {show} scheduled --ids <uuid of each created post>
If a post marked optional (Threads) fails, still record scheduled and mention it in --note.
"""


def claim(show, content, topic, when, date, st, now, note=""):
    sid = slot_id(date, show)
    rec = st.setdefault(show, {}); rec.update(status="building", content=content, topic=topic, started=now.isoformat(timespec="minutes"),
                                              post_at=when.isoformat(timespec="minutes"), tries=rec.get("tries", 0) + 1, **({"note": note} if note else {}))
    os.makedirs(AUTO, exist_ok=True)
    path = os.path.join(AUTO, f"{sid}.task.md"); open(path, "w").write(task_text(show, content, topic, now, sid))
    save(date, st, f"{date} {show}: building in a Claude session")
    return path


def pick(content, now, attempt):
    import studio
    if studio.SHOWS[content][1] != "bank": return None
    _, topic = studio.pick_topic(content, now, attempt); return topic


def hosting_ok():
    """Videos are hosted on Cloudflare R2 when its env vars are set; otherwise Metricool fetches them from public
    raw.githubusercontent.com links, which only works while the repo is publicly visible."""
    import publish
    if daily.r2_ready(): return True
    return publish.wait_public(f"https://raw.githubusercontent.com/{daily.REPO}/{daily.MEDIA}/README.md", 2)


def nxt(until):
    pull(); now = dt.datetime.now(TZ); date = now.strftime("%Y-%m-%d"); st = load_state(date)
    if not hosting_ok():
        print("DONE: video hosting is down: the GitHub repo is not publicly visible, so Metricool cannot fetch videos. "
              "Nothing was made; tell the user (see README: Video hosting; Cloudflare R2 env vars fix it)."); return
    if now.date() < daily.FIRST_DAY:
        print(f"DONE: hand-made episodes cover {date}; the automatic plan starts {daily.FIRST_DAY}."); return
    missed = [s for s, w in slots(now.date()) if now > w + daily.GRACE and st.get(s, {}).get("status") not in ("scheduled", "posted", "skipped", "missed", "failed")]
    for s in missed: st.setdefault(s, {})["status"] = "missed"
    if missed: save(date, st, f"{date}: missed {', '.join(missed)}")
    cut = dt.datetime.combine(now.date(), dt.time.fromisoformat(until), TZ) if until else None
    for show, when in slots(now.date()):
        rec = st.get(show, {})
        if rec.get("status") in ("scheduled", "posted", "skipped", "missed", "failed"): continue
        if rec.get("status") == "building" and now - dt.datetime.fromisoformat(rec["started"]) < STALE: continue
        if rec.get("status") == "built":   # rendered and hosted, but the session ended before scheduling it
            print(f"SLOT {show} was built but not recorded as scheduled.\nPOSTS {os.path.join(AUTO, slot_id(date, show) + '.posts.json')}\n"
                  "Check getScheduledPosts around its time, create only the posts that are missing, then record it."); return
        if rec.get("tries", 0) >= daily.TRIES: continue
        if cut and when > cut and kind(show) != "long": continue
        if now > when + daily.GRACE: continue
        topic = pick(show, now.astimezone(ET), rec.get("tries", 0))
        path = claim(show, show, topic, when, date, st, now)
        print(f"SLOT {show} posts {max(when, now + MIN_LEAD):%H:%M} CT\nTASK {path}"); return
    print("DONE: nothing left to make in this run.")


def fallback(show):
    pull(); now = dt.datetime.now(TZ); date = now.strftime("%Y-%m-%d"); st = load_state(date)
    if show not in FALLBACK:
        rec = st.setdefault(show, {}); rec.update(status="skipped", note="no confirmed story"); save(date, st, f"{date} {show}: skipped"); print("DONE: skipped"); return
    content = FALLBACK[show]; when = next(w for s, w in slots(now.date()) if s == show)
    topic = pick(content, now.astimezone(ET), st.get(show, {}).get("tries", 0))
    st.get(show, {})["tries"] = max(0, st.get(show, {}).get("tries", 1) - 1)   # the switch is not a failed try
    path = claim(show, content, topic, when, date, st, now, note=f"no confirmed story; made as {content}")
    print(f"SLOT {show} (as {content})\nTASK {path}")


def posts_for(urls, sc, at, longform):
    import publish
    bodies = publish.long_post(urls[0], urls[1], sc["post"], at, "America/Chicago") if longform else \
        publish.short_posts(urls[0], urls[1], sc["post"], at, "America/Chicago")
    off = dt.datetime.fromisoformat(at).replace(tzinfo=TZ).strftime("%z"); off = off[:3] + ":" + off[3:]
    out = []
    for b in bodies:
        b = dict(b); optional = b.pop("optional", False); b.pop("saveExternalMediaFiles", None)
        out.append({"network": "+".join(p["network"] for p in b["providers"]), "optional": optional, "date": at + off, "info": b})
    return out


def build(show, raw):
    import studio, run
    now = dt.datetime.now(TZ); date = now.strftime("%Y-%m-%d"); st = load_state(date); rec = st.setdefault(show, {})
    content = rec.get("content", show); sid = slot_id(date, show)
    sc = studio.sanitize(json.load(open(raw)), content, date); sc["id"] = sid
    path = os.path.join(AUTO, f"{sid}.json"); json.dump(sc, open(path, "w"), indent=1, ensure_ascii=False)
    video, cover = run.make(path)
    longform = kind(show) == "long"
    if longform: sc["post"]["yt_desc"] = sc["post"]["yt_desc"].replace("CHAPTERS", chapters(sc, os.path.dirname(video)))
    urls = host([video, cover], date)
    for u in urls:
        import publish
        if not publish.wait_public(u, 30): raise SystemExit(f"not reachable yet: {u}")
    when = next(w for s, w in slots(now.date()) if s == show)
    at = max(when, dt.datetime.now(TZ) + MIN_LEAD).strftime("%Y-%m-%dT%H:%M:00")
    posts = posts_for(urls, sc, at, longform)
    pp = os.path.join(AUTO, f"{sid}.posts.json"); json.dump(posts, open(pp, "w"), indent=1, ensure_ascii=False)
    rec.update(status="built", video=urls[0], post_at=at, title=sc["post"].get("title", ""))
    if rec.get("topic"): studio.mark_used(rec["topic"])
    save(date, st, f"{date} {show}: built")
    print(f"Create these {len(posts)} Metricool posts (file: {pp}):")
    print(json.dumps(posts, indent=1, ensure_ascii=False))


def record(show, status, note, ids):
    pull(); now = dt.datetime.now(TZ); date = now.strftime("%Y-%m-%d"); st = load_state(date); rec = st.setdefault(show, {})
    rec.update(status=status, finished=now.isoformat(timespec="minutes"))
    if note: rec["note"] = note
    if ids: rec["metricool"] = ids
    if status == "failed" and rec.get("topic"):
        import studio; studio.mark_failed(rec["topic"])
    save(date, st, f"{date} {show}: {status}")
    print("RECORDED", show, status)


def status():
    pull(); now = dt.datetime.now(TZ); st = load_state(now.strftime("%Y-%m-%d"))
    for show, when in slots(now.date()):
        r = st.get(show, {}); print(f"{when:%H:%M} {show:13} {r.get('status', '-'):10} {r.get('title', '')} {r.get('note', '')}")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd"); ap.add_argument("args", nargs="*")
    ap.add_argument("--until"); ap.add_argument("--note", default=""); ap.add_argument("--ids", nargs="*", default=[])
    a = ap.parse_args()
    if a.cmd == "setup": setup()
    elif a.cmd == "next": nxt(a.until)
    elif a.cmd == "fallback": fallback(a.args[0])
    elif a.cmd == "build": build(a.args[0], a.args[1])
    elif a.cmd == "record": record(a.args[0], a.args[1], a.note, a.ids)
    elif a.cmd == "status": status()
    else: ap.error("unknown command")


if __name__ == "__main__":
    main()
