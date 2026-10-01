"""One scheduled run: make and schedule every video the weekly plan says is due.

GitHub Actions runs this every hour (runs never overlap). Times are US Central, the brand's time zone in Metricool, and come from
Metricool's best-time-to-post data for these accounts (Sep 2026): TikTok, Instagram, Facebook and YouTube all peak at
10 AM, 12, 2, 4 and 6 PM, and YouTube's single best hour is 4 PM on weekdays (weekdays score about twice the weekend).
  5 shorts a day (TikTok, Instagram Reels, Facebook Reels, YouTube Shorts, Threads): 10:00, 12:00, 14:00, 16:00, 18:00
  5 long-form YouTube videos a week: Monday-Friday 16:00

A slot starts building a few hours before it posts, so a delayed or dropped hourly run is caught up by the next one. Every slot is
recorded in concepts/scripts/auto/<date>.state.json, so nothing is made or posted twice.

usage: python daily.py                  # scheduled run: make everything that is due now
       python daily.py --due            # prints due=yes|no (lets the workflow skip installing when nothing is due)
       python daily.py --show business  # make one show now (manual test): posts at its slot time today, or in 10 minutes
       python daily.py --check          # check the API keys and settings; posts nothing
       python daily.py --plan [--now 2026-10-05T08:30]   # print what would be made (no API calls)
"""
import argparse, datetime as dt, json, os, shutil, subprocess, sys, time, traceback
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); CON = os.path.join(HERE, "concepts")
sys.path.insert(0, HERE); sys.path.insert(0, CON)
TZ = ZoneInfo("America/Chicago")
SHORTS = [("morning", "10:00"), ("explainer", "12:00"), ("business", "14:00"), ("bigstory", "16:00"), ("hot", "18:00")]
LONG_DAYS = {0: "lf-explained", 1: "lf-business", 2: "lf-guide", 3: "lf-world", 4: "lf-big"}   # Monday-Friday
LONG_AT = "16:00"
LONG = set(LONG_DAYS.values())
LEAD = {"short": dt.timedelta(hours=2, minutes=30), "long": dt.timedelta(hours=8)}   # how early a slot may start building
GRACE = dt.timedelta(minutes=90)     # a slot that missed its time still goes out (right away) within this window
TRIES = 3                            # attempts per slot per day (API errors, failed renders)
FALLBACK = {"morning": "hot", "bigstory": "explainer", "lf-big": "lf-explained"}   # news slot with no confirmed story -> evergreen
# Hand-made episodes cover the days before this date; the plan runs from it. Override with the AUTO_START variable (YYYY-MM-DD).
AUTO_START = dt.date.fromisoformat(os.environ.get("AUTO_START") or "2026-10-03")
# Long-form videos run from this date (the hand-made ones all went out on Sep 29, so the weekday long-forms start Sep 30).
LONG_START = dt.date.fromisoformat(os.environ.get("LONG_START") or "2026-09-30")
FIRST_DAY = min(AUTO_START, LONG_START)
REPO = os.environ.get("GITHUB_REPOSITORY", "fwagtx/FinancePros")
BRANCH = os.environ.get("GITHUB_REF_NAME", "claude/dazzling-newton-1ex2s0")
MEDIA = os.environ.get("MEDIA_BRANCH", "media")      # videos live on their own branch, trimmed to the last week
KEEP_DAYS = 7                                         # Metricool copies each file when the post is scheduled
AUTO = os.path.join(CON, "scripts", "auto")


def sh(*cmd, check=True, **kw):
    print("+", " ".join(cmd), flush=True); return subprocess.run(cmd, check=check, **kw)


def slots(day):
    """[(show, post time)] for one day, in posting order."""
    plan = (list(SHORTS) if day >= AUTO_START else []) + \
           ([(LONG_DAYS[day.weekday()], LONG_AT)] if day.weekday() in LONG_DAYS and day >= LONG_START else [])
    return sorted(((s, dt.datetime.combine(day, dt.time.fromisoformat(t), TZ)) for s, t in plan), key=lambda x: (x[1], x[0] in LONG))


def kind(show): return "long" if show in LONG else "short"


# ---------------- state: what each slot did today ----------------
def state_path(date): return os.path.join(AUTO, f"{date}.state.json")


def load_state(date):
    p = state_path(date)
    return json.load(open(p)) if os.path.exists(p) else {}


def commit(paths, msg):
    """Commit files to the main branch and push (retrying on a race with another push)."""
    paths = [p for p in paths if os.path.exists(p)]
    if not paths: return
    sh("git", "-C", ROOT, "add", *paths)
    if sh("git", "-C", ROOT, "diff", "--cached", "--quiet", check=False).returncode == 0: return
    sh("git", "-C", ROOT, "commit", "-q", "-m", msg)
    for i in range(4):
        if sh("git", "-C", ROOT, "pull", "-q", "--rebase", "--autostash", "origin", BRANCH, check=False).returncode == 0 and \
           sh("git", "-C", ROOT, "push", "-q", "origin", f"HEAD:{BRANCH}", check=False).returncode == 0: return
        time.sleep(2 ** (i + 1))
    print("WARNING: could not push", msg)


def save(date, st, msg, extra=()):
    os.makedirs(AUTO, exist_ok=True)
    json.dump(st, open(state_path(date), "w"), indent=1)
    logs = [os.path.join(AUTO, f) for f in os.listdir(AUTO) if f.startswith(date)]
    commit([state_path(date), os.path.join(CON, "topics_state.json"), *logs, *extra], msg)


def pull():
    sh("git", "-C", ROOT, "pull", "-q", "--rebase", "--autostash", "origin", BRANCH, check=False)


def due(now, st):
    """Slots that may be built now, earliest post first."""
    out = []
    for show, when in slots(now.date()):
        rec = st.get(show, {})
        if rec.get("status") in ("posted", "skipped", "missed"): continue
        if rec.get("tries", 0) >= TRIES: continue
        if now < when - LEAD[kind(show)] or now > when + GRACE: continue
        out.append((when, show))
    return out


# ---------------- making one slot ----------------
def studio(content, slot_id, attempt):
    """Run the studio (topic -> research -> script -> fact-check). Returns the script path, or None when nothing qualified."""
    r = subprocess.run([sys.executable, os.path.join(CON, "studio.py"), "--show", content, "--id", slot_id, "--attempt", str(attempt)],
                       capture_output=True, text=True)
    print(r.stdout[-3000:], r.stderr[-3000:], flush=True)
    if r.returncode in (3, 4): return None          # 3 = no confirmed news worth a video, 4 = failed the fact-check
    r.check_returncode()                            # anything else is a crash (API error...): the slot is retried next hour
    return r.stdout.strip().splitlines()[-1]


def script_for(show, slot_id, tries):
    """News slots fall back to an evergreen show; a failed fact-check on an evergreen topic tries a second topic."""
    for content in [show] + ([FALLBACK[show]] if show in FALLBACK else []):
        evergreen = content not in ("morning", "bigstory", "lf-big")
        for k in range(2 if evergreen else 1):
            path = studio(content, slot_id, tries * 10 + k)
            if path: return path, content
    return None, None


FP_R2_ACCOUNT = "231999c96851bc148ac14dfa00c54bae"   # the Cloudflare account that owns the financepros-media bucket (an identifier, not a secret)
# FinancePros has its own R2 bucket and keys (FP_R2_*). The generic R2_* / AWS_* variables in a shared environment may belong to
# another brand, so they are never used here.
def r2_cfg():
    e = os.environ.get
    return {"account": e("FP_R2_ACCOUNT_ID") or FP_R2_ACCOUNT, "key": e("FP_R2_ACCESS_KEY_ID"), "secret": e("FP_R2_SECRET_ACCESS_KEY"),
            "bucket": e("FP_R2_BUCKET") or "financepros-media", "public": (e("FP_R2_PUBLIC_URL") or "").rstrip("/")}


def r2_ready():
    c = r2_cfg(); return all(c.values()) and c["bucket"].startswith("financepros")


def host_r2(files, date):
    """Upload files to the FinancePros R2 bucket and return their public URLs. The bucket's lifecycle rule deletes them
    after 7 days; Metricool keeps its own copy once a post is scheduled."""
    import boto3, mimetypes
    c = r2_cfg()
    s3 = boto3.client("s3", endpoint_url=f"https://{c['account']}.r2.cloudflarestorage.com", aws_access_key_id=c["key"],
                      aws_secret_access_key=c["secret"], region_name="auto")
    urls = []
    for f in files:
        key = f"{date}/{os.path.basename(f)}"
        s3.upload_file(f, c["bucket"], key, ExtraArgs={"ContentType": mimetypes.guess_type(f)[0] or "application/octet-stream"})
        urls.append(f"{c['public']}/{key}")
    return urls


def host(files, date):
    """Host files publicly and return their URLs: Cloudflare R2 when configured, otherwise the repo's media branch
    (commit, raw URLs, old days dropped so the repo never grows without limit)."""
    if r2_ready(): return host_r2(files, date)
    wt = os.path.join(ROOT, ".media")
    if not os.path.exists(wt):
        if sh("git", "-C", ROOT, "fetch", "--depth", "1", "origin", f"{MEDIA}:{MEDIA}", check=False).returncode == 0:
            sh("git", "-C", ROOT, "worktree", "add", wt, MEDIA)
        else:
            sh("git", "-C", ROOT, "worktree", "add", "--detach", wt)
            sh("git", "-C", wt, "checkout", "--orphan", MEDIA); sh("git", "-C", wt, "rm", "-rf", "-q", ".", check=False)
    urls = []
    for f in files:
        rel = f"{date}/{os.path.basename(f)}"; os.makedirs(os.path.join(wt, date), exist_ok=True); shutil.copy(f, os.path.join(wt, rel))
        urls.append(f"https://raw.githubusercontent.com/{REPO}/{MEDIA}/{rel}")
    cutoff = (dt.date.fromisoformat(date) - dt.timedelta(days=KEEP_DAYS)).isoformat()
    old = [d for d in os.listdir(wt) if d[:4].isdigit() and d < cutoff]
    for d in old: shutil.rmtree(os.path.join(wt, d))
    sh("git", "-C", wt, "add", "-A"); sh("git", "-C", wt, "commit", "-q", "-m", f"media {date}")
    if old:   # squash history so dropped videos are really gone
        sh("git", "-C", wt, "checkout", "-q", "--orphan", "tmp-media"); sh("git", "-C", wt, "commit", "-q", "-m", f"media (last {KEEP_DAYS} days)")
        sh("git", "-C", wt, "branch", "-M", MEDIA); sh("git", "-C", wt, "push", "-q", "-f", "origin", MEDIA)
    else:
        for _ in range(4):
            if sh("git", "-C", wt, "push", "-q", "origin", f"HEAD:{MEDIA}", check=False).returncode == 0: break
            sh("git", "-C", wt, "pull", "-q", "--rebase", "origin", MEDIA, check=False)
    return urls


def chapters(sc, out_dir):
    """Real YouTube chapter timestamps from the rendered timeline."""
    tl = json.load(open(os.path.join(out_dir, "timeline.json")))
    rows = ["0:00 Intro"]
    for ln, t in zip(sc["lines"], tl["lines"]):
        if ln["scene"].get("t") == "chapter":
            s = int(t["s"]); rows.append(f"{s // 60}:{s % 60:02d} {ln['scene'].get('title', '')}")
    return "\n".join(rows)


def make_slot(show, when, date, st, key=None):
    """Make one slot end to end and record the outcome under key (default: the show). Returns True when it was posted."""
    key = key or show
    rec = st.setdefault(key, {}); rec["tries"] = rec.get("tries", 0) + 1; rec["status"] = "building"
    rec["started"] = dt.datetime.now(TZ).isoformat(timespec="minutes")
    save(date, st, f"{date} {key}: building (try {rec['tries']})")
    try:
        path, made_as = script_for(show, f"{date}-{key}", rec["tries"])
        if not path:
            rec.update(status="skipped", note="nothing passed the fact-check"); return False
        sc = json.load(open(path)); longform = kind(show) == "long"
        import run
        video, cover = run.make(path)
        if longform: sc["post"]["yt_desc"] = sc["post"]["yt_desc"].replace("CHAPTERS", chapters(sc, os.path.dirname(video)))
        import publish
        urls = host([video, cover] + ([] if longform else [publish.tiktok_video(video, cover)]), date)
        now = dt.datetime.now(TZ)
        at = max(when, now + dt.timedelta(minutes=10))
        import publish
        results = publish.schedule(urls[0], urls[1], sc["post"], at.strftime("%Y-%m-%dT%H:%M:00"), "America/Chicago", longform=longform,
                                   tt_video=urls[2] if len(urls) > 2 else None)
        rec.update(status="posted", made_as=made_as, title=sc["post"].get("title", ""), post_at=at.isoformat(timespec="minutes"),
                   video=urls[0], networks=results)
        if any(not r["ok"] for r in results): rec["note"] = "some networks failed; see networks"
        return all(r["ok"] or r.get("optional") for r in results)
    except Exception as e:
        traceback.print_exc()
        rec.update(status="failed", error=f"{type(e).__name__}: {e}"[:500]); return False
    finally:
        save(date, st, f"{date} {key}: {rec['status']}")


# ---------------- checks ----------------
def check():
    """Verify secrets and API access without posting anything."""
    ok = True
    for k in ("ANTHROPIC_API_KEY", "METRICOOL_USER_TOKEN", "METRICOOL_USER_ID", "METRICOOL_BLOG_ID"):
        have = bool(os.environ.get(k)); ok &= have; print(f"{k:22} {'set' if have else 'MISSING'}")
    print("METRICOOL_DRAFT       ", os.environ.get("METRICOOL_DRAFT", "false"), "| AUTO_START", AUTO_START)
    try:
        import news
        r = news.client().messages.create(model=news.MODEL, max_tokens=64, messages=[{"role": "user", "content": "Reply with the single word OK."}])
        print("Claude API             OK:", r.model, "".join(b.text for b in r.content if b.type == "text")[:20])
    except Exception as e:
        ok = False; print("Claude API             FAILED:", type(e).__name__, str(e)[:300])
    try:
        import publish
        brands = publish.brands()
        mine = [b for b in brands if str(b.get("id")) == os.environ.get("METRICOOL_BLOG_ID")]
        print("Metricool API          OK:", f"{len(brands)} brand(s);", "brand found" if mine else "BRAND ID NOT FOUND")
        ok &= bool(mine)
    except Exception as e:
        ok = False; print("Metricool API          FAILED:", type(e).__name__, str(e)[:300])
    print("ALL GOOD" if ok else "SOMETHING IS MISSING (see above)")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--show"); ap.add_argument("--check", action="store_true"); ap.add_argument("--due", action="store_true")
    ap.add_argument("--plan", action="store_true"); ap.add_argument("--now")
    a = ap.parse_args()
    now = dt.datetime.fromisoformat(a.now).replace(tzinfo=TZ) if a.now else dt.datetime.now(TZ)
    date = now.strftime("%Y-%m-%d")
    if a.check: sys.exit(0 if check() else 1)
    if a.due or a.plan:
        d = due(now, load_state(date)) if now.date() >= FIRST_DAY else []
        if a.due: print("due=" + ("yes" if d else "no")); return
        print(f"{now:%a %Y-%m-%d %H:%M} CT, automation starts {AUTO_START}")
        for show, when in slots(now.date()):
            print(f"  {when:%H:%M} {show:13} {'<- due now' if (when, show) in d else ''}")
        return
    if a.show:   # manual run of one show; a draft test is recorded apart so it never blocks the real slot
        pull(); st = load_state(date)
        when = next((w for s, w in slots(now.date()) if s == a.show), now)
        draft = os.environ.get("METRICOOL_DRAFT", "false").lower() == "true"
        ok = make_slot(a.show, max(when, now), date, st, key=a.show + ("-draft" if draft else ""))
        sys.exit(0 if ok else 1)
    if now.date() < FIRST_DAY:
        print(f"Hand-made episodes cover {now:%a %b %d}; the automatic plan starts {FIRST_DAY}."); return
    t0 = time.monotonic(); failures = 0
    while time.monotonic() - t0 < 150 * 60:
        pull(); now = dt.datetime.now(TZ); st = load_state(date)
        missed = [s for s, w in slots(now.date()) if now > w + GRACE and st.get(s, {}).get("status") not in ("posted", "skipped", "missed")]
        if missed:
            for s in missed: st.setdefault(s, {})["status"] = "missed"
            save(date, st, f"{date}: missed {', '.join(missed)}")
        todo = due(now, st)
        if not todo: break
        when, show = todo[0]
        print(f"=== {show} (posts {when:%H:%M} CT) ===", flush=True)
        if not make_slot(show, when, date, st): failures += 1
    if failures: sys.exit(1)   # a red run in GitHub Actions; the state file says what failed


if __name__ == "__main__":
    main()
