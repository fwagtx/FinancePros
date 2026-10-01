"""Session mode: the daily shows made by scheduled Claude Code sessions (Routines) on the account's Claude plan.

No API keys: Claude in the session does the research, writing and fact-checking, and schedules the posts through the
Metricool connector. This script does everything else: the plan, topic picks, rendering, hosting and the state files.
The routine prompts are in ROUTINES.md.

Evergreen videos are kept BUFFER days ahead: fully made and scheduled in Metricool, so a missed run never leaves a gap.
News slots (morning, bigstory, lf-big) are only made on their own day.

  python engine/session.py setup                        # install ffmpeg, Python and Node packages, the voice model
  python engine/session.py next [--until 14:00] [--ahead 60] [--start 0]   # claim the next slot; prints its task file (or DONE)
                                                        # --start/--ahead let parallel sessions fill separate day ranges
  python engine/session.py fallback <slot>              # a news slot had no confirmed story: switch it to its evergreen show
  python engine/session.py build <slot> <script.json>   # sanitize, render, quality report, host; prints the Metricool posts
  python engine/session.py record <slot> scheduled|skipped|failed [--note ...] [--ids ...]
  python engine/session.py rehost <slot>                # re-upload a slot's files under new names (Metricool "Failed to normalize media")
  python engine/session.py status                       # today's slots and the buffer
A <slot> is "YYYY-MM-DD-show", e.g. 2026-10-05-explainer.

Slots, times and the state files (concepts/scripts/auto/<date>.state.json) are shared with daily.py.
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
BUFFER = 60                                  # days of evergreen videos kept made and scheduled ahead (about 2 months)
DONE_STATES = ("scheduled", "posted", "skipped", "missed", "failed")
LENGTH = {"short": (30, 62), "long": (480, 660)}   # seconds a finished video must fall inside


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


def split_slot(sid): return sid[:10], sid[11:]


def slot_time(date, show):
    return next(w for s, w in slots(dt.date.fromisoformat(date)) if s == show)


def task_text(show, content, topic, now, when, sid):
    """Everything the session needs to research, write, check and publish one video."""
    import studio
    k = studio.SHOWS[content][0]
    schema = os.path.join(AUTO, f"{sid}.schema.json"); json.dump(studio.SCRIPT, open(schema, "w"), indent=1)
    news = content in NEWS
    ahead = when.date() > now.date()
    lo, hi = LENGTH[k]
    return f"""# {sid}: {content} ({'long-form YouTube video' if k == 'long' else 'vertical short'}), posts {when:%A %B %d, %Y at %I:%M %p} Central

You are making one FinancePros TV video. Quality matters more than speed: take the time each step needs, and do not skip any.
{"This video is made ahead of time: it posts on " + f"{when:%A, %B %d}" + ". Keep it evergreen: no 'today', 'this week', 'yesterday' or 'just announced'; give every number with its date or period (for example 'in 2025' or 'as of August 2026')." if ahead else ""}

## 1. Research
{studio.BRAND}

{studio.research_prompt(content, now, topic)}

Use web search. Save the brief (facts, numbers with dates, a chartable data series, SOURCES) to:
  {os.path.join(AUTO, sid + '.research.md')}
{"If nothing is confirmed and important, run: python engine/session.py fallback " + sid + "  and follow the new task it prints." if news else ""}

## 2. Script
{studio.write_prompt(content, "(the brief you saved in step 1)", now, topic)}

Narration must sound like one smart friend talking, not a list being read:
- Read every `say` line in order as if out loud. Each one is a complete, natural spoken sentence (contractions, varied length),
  and each line leads into the next one; no fragments, no stacked labels, no repeated openers.
- Write numbers, symbols and acronyms in `say` the way a person says them ("about twenty-two percent", "A P R", "four hundred
  thousand dollars"); keep exact figures on screen in `text`/scene values. Spoken and on-screen numbers must agree.
- No abbreviations the voice would stumble on (write "versus", "for example", "U S" becomes "US").
Write ONE JSON object that matches the JSON schema in {schema}
and save it to:  {os.path.join(AUTO, sid + '.raw.json')}

## 3. Fact-check (independent)
Launch a subagent (Agent tool) that has not seen your work. Give it the script's lines, on-screen values, cover and post text, and
this instruction: "Independently verify every factual claim, number and chart data point with web search (do not trust the brief).
Also flag: a weak opening (the first line must be a true, specific attention grabber spoken in under 3 seconds that makes a
viewer need the answer; say how to make it stronger if it is not), stale news, time words that will be wrong on the posting date ({when:%B %d, %Y}), advice or price predictions, political
opinion, a cover or title the video doesn't pay off, math errors in worked examples, any on-screen value that differs from the
spoken one, and narration that reads awkwardly out loud. List each issue. Finish with exactly one line: VERDICT: PASS or VERDICT: FAIL."
Fix every issue it lists and check again (at most 2 rounds). Save its last report to
  {os.path.join(AUTO, sid + '.factcheck.md')}
If it still fails: python engine/session.py record {sid} failed --note "fact-check"   and go to the next slot.

## 4. Build and quality check
  python engine/session.py build {sid} {os.path.join(AUTO, sid + '.raw.json')}
It renders the video and cover, uploads them, and prints a QUALITY report (length, preview frames, cover) and the Metricool posts.
Before scheduling:
- Length must be {lo // 60}:{lo % 60:02d} to {hi // 60}:{hi % 60:02d}. If it is outside, edit the script (add or trim real content, never filler)
  and run build again.
- Hook check: open the first preview frame and the cover. The opening line and visual must grab attention in the first 3 seconds
  (big bold text or number, no slow intro). If it would not stop you scrolling, sharpen line 1 and rebuild.
- Open every preview frame and the cover image it lists with the Read tool. Everything must be readable, nothing overlapping or cut
  off, the right scene for the words. Fix the script and rebuild if not (at most 2 rebuilds; if it still fails, record failed).

## 5. Schedule
Create each printed post with the Metricool createScheduledPost tool (blogId 7091438): pass "date" and "info" exactly as printed
(info as a JSON string). Then:
  python engine/session.py record {sid} scheduled --ids <uuid of each created post>
If a post marked optional (Threads) fails, still record scheduled and mention it in --note.
If a post fails with "Failed to normalize media", run  python engine/session.py rehost {sid}  and create that post again
from the rewritten posts file (Metricool sometimes refuses a URL but accepts the same file under a new name).
"""


def claim(date, show, content, topic, when, now, note=""):
    st = load_state(date); sid = slot_id(date, show)
    rec = st.setdefault(show, {})
    rec.update(status="building", content=content, topic=topic, started=now.isoformat(timespec="minutes"),
               post_at=when.isoformat(timespec="minutes"), tries=rec.get("tries", 0) + 1, **({"note": note} if note else {}))
    os.makedirs(AUTO, exist_ok=True)
    path = os.path.join(AUTO, f"{sid}.task.md"); open(path, "w").write(task_text(show, content, topic, now, when, sid))
    save(date, st, f"{date} {show}: building in a Claude session")
    return path


def pick(content, when, attempt):
    """The planned topic for the slot's own date (calendar.json), or the next bank topic."""
    import studio
    if studio.SHOWS[content][1] != "bank": return None
    _, topic = studio.pick_topic(content, when.astimezone(ET), attempt); return topic


def hosting_ok():
    """Videos are hosted on Cloudflare R2 when its env vars are set; otherwise Metricool fetches them from public
    raw.githubusercontent.com links, which only works while the repo is publicly visible."""
    import publish
    if daily.r2_ready(): return True
    return publish.wait_public(f"https://raw.githubusercontent.com/{daily.REPO}/{daily.MEDIA}/README.md", 2)


def open_slot(rec, now):
    """True when a slot still needs making (not done, not being made right now, tries left)."""
    if rec.get("status") in DONE_STATES: return False
    if rec.get("status") == "building" and now - dt.datetime.fromisoformat(rec["started"]) < STALE: return False
    return rec.get("tries", 0) < daily.TRIES


def nxt(until, ahead, start=0):
    pull(); now = dt.datetime.now(TZ); today = now.date()
    if not hosting_ok():
        print("DONE: video hosting is down (no FinancePros R2 settings and the GitHub repo is not public), so Metricool cannot "
              "fetch videos. Nothing was made; tell the user (see README: Video hosting)."); return
    # today's slots: mark the ones whose time has passed as missed, then make what is due
    date = today.isoformat(); st = load_state(date)
    missed = [s for s, w in slots(today) if now > w + daily.GRACE and st.get(s, {}).get("status") not in DONE_STATES]
    for s in missed: st.setdefault(s, {})["status"] = "missed"
    if missed: save(date, st, f"{date}: missed {', '.join(missed)}")
    cut = dt.datetime.combine(today, dt.time.fromisoformat(until), TZ) if until else None
    candidates = []
    for show, when in (slots(today) if start == 0 else []):
        if now > when + daily.GRACE: continue
        if cut and when > cut and kind(show) != "long": continue
        candidates.append((date, show, when))
    # the buffer: evergreen slots on the coming days
    for i in range(max(1, start), ahead + 1):
        day = today + dt.timedelta(days=i)
        for show, when in slots(day):
            if show not in NEWS: candidates.append((day.isoformat(), show, when))
    for d, show, when in candidates:
        rec = load_state(d).get(show, {})
        if rec.get("status") == "built":   # rendered and hosted, but the session ended before scheduling it
            print(f"SLOT {slot_id(d, show)} was built but not recorded as scheduled.\nPOSTS {os.path.join(AUTO, slot_id(d, show) + '.posts.json')}\n"
                  f"Check getScheduledPosts around {when:%Y-%m-%d %H:%M} CT, create only the posts that are missing, then record it."); return
        if not open_slot(rec, now): continue
        topic = pick(show, when, rec.get("tries", 0))
        path = claim(d, show, show, topic, when, now)
        print(f"SLOT {slot_id(d, show)} posts {max(when, now + MIN_LEAD):%a %b %d %H:%M} CT\nTASK {path}"); return
    print(f"DONE: nothing left to make in days {start}-{ahead}; evergreen videos are made through {today + dt.timedelta(days=ahead)}.")


def fallback(sid):
    pull(); now = dt.datetime.now(TZ); date, show = split_slot(sid); st = load_state(date)
    if show not in FALLBACK:
        rec = st.setdefault(show, {}); rec.update(status="skipped", note="no confirmed story"); save(date, st, f"{date} {show}: skipped"); print("DONE: skipped"); return
    content = FALLBACK[show]; when = slot_time(date, show)
    topic = pick(content, when, st.get(show, {}).get("tries", 0))
    st.get(show, {})["tries"] = max(0, st.get(show, {}).get("tries", 1) - 1); save(date, st, f"{date} {show}: switching to {content}")
    path = claim(date, show, content, topic, when, now, note=f"no confirmed story; made as {content}")
    print(f"SLOT {sid} (as {content})\nTASK {path}")


def posts_for(urls, sc, at, longform):
    import publish
    bodies = publish.long_post(urls[0], urls[1], sc["post"], at, "America/Chicago") if longform else \
        publish.short_posts(urls[0], urls[1], sc["post"], at, "America/Chicago", urls[2] if len(urls) > 2 else None)
    off = dt.datetime.fromisoformat(at).replace(tzinfo=TZ).strftime("%z"); off = off[:3] + ":" + off[3:]
    out = []
    for b in bodies:
        b = dict(b); optional = b.pop("optional", False); b.pop("saveExternalMediaFiles", None)
        out.append({"network": "+".join(p["network"] for p in b["providers"]), "optional": optional, "date": at + off, "info": b})
    return out


def quality(video, cover, sid, k):
    """Length and preview frames of the finished video, for the session to look at before scheduling."""
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video],
                               capture_output=True, text=True).stdout.strip() or 0)
    frames = []
    for n, f in enumerate((min(2.0, dur * 0.05) / max(dur, 1), 0.3, 0.55, 0.8)):   # frame 1 = the 2-second mark (the hook)
        out = os.path.join(AUTO, f"{sid}.frame{n + 1}.jpg")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{dur * f:.2f}", "-i", video, "-frames:v", "1", "-vf", "scale=720:-2", out])
        frames.append(out)
    lo, hi = LENGTH[k]; ok = lo <= dur <= hi
    print(f"QUALITY {sid}\n  length {int(dur) // 60}:{int(dur) % 60:02d} (target {lo // 60}:{lo % 60:02d}-{hi // 60}:{hi % 60:02d}) {'OK' if ok else 'OUT OF RANGE: fix the script and rebuild'}")
    print("  preview frames (open each with Read):\n    " + "\n    ".join(frames) + f"\n  cover (open with Read): {cover}")
    return dur, ok


def build(sid, raw):
    import studio, run, publish
    now = dt.datetime.now(TZ); date, show = split_slot(sid); st = load_state(date); rec = st.setdefault(show, {})
    content = rec.get("content", show)
    sc = studio.sanitize(json.load(open(raw)), content, date); sc["id"] = sid
    path = os.path.join(AUTO, f"{sid}.json"); json.dump(sc, open(path, "w"), indent=1, ensure_ascii=False)
    video, cover = run.make(path)
    longform = kind(show) == "long"
    dur, ok = quality(video, cover, sid, "long" if longform else "short")
    if longform: sc["post"]["yt_desc"] = sc["post"]["yt_desc"].replace("CHAPTERS", chapters(sc, os.path.dirname(video)))
    urls = host([video, cover] + ([] if longform else [publish.tiktok_video(video, cover)]), date)
    for u in urls:
        if not publish.wait_public(u, 30): raise SystemExit(f"not reachable yet: {u}")
    at = max(slot_time(date, show), dt.datetime.now(TZ) + MIN_LEAD).strftime("%Y-%m-%dT%H:%M:00")
    posts = posts_for(urls, sc, at, longform)
    pp = os.path.join(AUTO, f"{sid}.posts.json"); json.dump(posts, open(pp, "w"), indent=1, ensure_ascii=False)
    rec.update(status="built", video=urls[0], post_at=at, title=sc["post"].get("title", ""), length=round(dur))
    save(date, st, f"{date} {show}: built")
    if not ok: print("NOT READY: the length is out of range. Fix the script and run build again; do not schedule this version.")
    print(f"Create these {len(posts)} Metricool posts (file: {pp}) after the quality check passes:")
    print(json.dumps(posts, indent=1, ensure_ascii=False))


def rehost(sid):
    """Metricool sometimes rejects a URL for good ("Failed to normalize media") but takes the same file under a new name:
    re-upload this slot's video, cover and TikTok copy with a fresh suffix and point its posts file at them."""
    import publish, urllib.request
    date, show = split_slot(sid); pp = os.path.join(AUTO, f"{sid}.posts.json"); posts = json.load(open(pp))
    tag = dt.datetime.now(TZ).strftime("r%H%M%S"); new = {}
    for p in posts:
        for url in p["info"]["media"] + [p["info"].get("videoThumbnailUrl")]:
            if not url or url in new: continue
            base, ext = os.path.splitext(url.rsplit("/", 1)[1]); local = os.path.join(AUTO, f"{base}-{tag}{ext}")
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=120) as r:
                open(local, "wb").write(r.read())
            new[url] = host([local], date)[0]; os.remove(local)
            if not publish.wait_public(new[url], 30): raise SystemExit(f"not reachable yet: {new[url]}")
    for p in posts:
        p["info"]["media"] = [new[u] for u in p["info"]["media"]]
        if p["info"].get("videoThumbnailUrl"): p["info"]["videoThumbnailUrl"] = new[p["info"]["videoThumbnailUrl"]]
    json.dump(posts, open(pp, "w"), indent=1, ensure_ascii=False)
    print(f"REHOSTED {sid}: {pp} now uses fresh URLs; create (or update) the posts that failed with them.")


def record(sid, status, note, ids):
    pull(); now = dt.datetime.now(TZ); date, show = split_slot(sid); st = load_state(date); rec = st.setdefault(show, {})
    rec.update(status=status, finished=now.isoformat(timespec="minutes"))
    if note: rec["note"] = note
    if ids: rec["metricool"] = ids
    save(date, st, f"{date} {show}: {status}")
    print("RECORDED", sid, status)


def status():
    pull(); now = dt.datetime.now(TZ); today = now.date()
    st = load_state(today.isoformat())
    print(f"Today {today}:")
    for show, when in slots(today):
        r = st.get(show, {}); print(f"  {when:%H:%M} {show:13} {r.get('status', '-'):10} {r.get('title', '')} {r.get('note', '')}")
    ready = total = 0
    for i in range(1, BUFFER + 1):
        day = today + dt.timedelta(days=i); s = load_state(day.isoformat())
        for show, _ in slots(day):
            if show in NEWS: continue
            total += 1; ready += s.get(show, {}).get("status") in ("scheduled", "posted")
    print(f"Buffer (next {BUFFER} days, evergreen): {ready}/{total} made and scheduled")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("cmd"); ap.add_argument("args", nargs="*")
    ap.add_argument("--until"); ap.add_argument("--ahead", type=int, default=BUFFER)
    ap.add_argument("--start", type=int, default=0, help="first day offset to fill (parallel sessions split the buffer by range)")
    ap.add_argument("--note", default=""); ap.add_argument("--ids", nargs="*", default=[])
    a = ap.parse_args()
    if a.cmd == "setup": setup()
    elif a.cmd == "next": nxt(a.until, a.ahead, a.start)
    elif a.cmd == "fallback": fallback(a.args[0])
    elif a.cmd == "build": build(a.args[0], a.args[1])
    elif a.cmd == "rehost": rehost(a.args[0])
    elif a.cmd == "record": record(a.args[0], a.args[1], a.note, a.ids)
    elif a.cmd == "status": status()
    else: ap.error("unknown command")


if __name__ == "__main__":
    main()
