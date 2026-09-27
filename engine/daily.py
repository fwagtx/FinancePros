"""One scheduled run: topic -> research -> script -> fact-check -> doodle render -> host -> schedule on every platform.

The GitHub Actions workflow runs this every hour; the weekly PLAN below (Eastern time) decides what is made.
4 shorts a day (TikTok, Instagram Reels, Facebook Reels, YouTube Shorts) + 3 long-form YouTube videos a week.

usage: python daily.py --show auto|morning|explainer|bigstory|hot|lf-big|lf-explained|lf-world [--force]
"""
import argparse, datetime as dt, glob, json, os, shutil, subprocess, sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); CON = os.path.join(HERE, "concepts")
sys.path.insert(0, HERE); sys.path.insert(0, CON)
ET = ZoneInfo("America/New_York")
SHORTS = [(6, "morning", "07:30"), (10, "explainer", "12:00"), (14, "bigstory", "16:30"), (17, "hot", "19:30")]
PLAN = {d: list(SHORTS) for d in range(7)}          # weekday (0=Mon) -> [(build hour ET, show, post time ET)]
PLAN[0].append((11, "lf-big", "17:00"))             # Monday: the week's big story, in depth
PLAN[2].append((11, "lf-explained", "17:00"))       # Wednesday: evergreen high-value explainer
PLAN[5].append((7, "lf-world", "11:00"))            # Saturday: world economy
LONG = {"lf-big", "lf-explained", "lf-world"}
FALLBACK = {"morning": "hot", "bigstory": "explainer"}   # if no confirmed news qualifies (or it fails fact-check), post an evergreen instead
# Hand-made episodes cover up to this date; planned shows start after it. Override with the AUTO_START variable (YYYY-MM-DD).
AUTO_START = dt.date.fromisoformat(os.environ.get("AUTO_START") or "2026-10-03")
REPO = os.environ.get("GITHUB_REPOSITORY", "fwagtx/FinancePros")
BRANCH = os.environ.get("GITHUB_REF_NAME", "claude/dazzling-newton-1ex2s0")
MEDIA = os.environ.get("MEDIA_BRANCH", "media")      # videos live on their own branch, trimmed to the last few weeks
KEEP_DAYS = 21


def sh(*cmd, check=True, **kw):
    print("+", " ".join(cmd)); return subprocess.run(cmd, check=check, **kw)


def host(files, date):
    """Commit files to the media branch and return their raw URLs. Old days are dropped so the repo never grows without limit
    (Metricool copies each file when the post is scheduled)."""
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
        sh("git", "-C", wt, "branch", "-M", MEDIA); sh("git", "-C", wt, "push", "-f", "origin", MEDIA)
    else:
        for _ in range(4):
            if sh("git", "-C", wt, "push", "origin", f"HEAD:{MEDIA}", check=False).returncode == 0: break
            sh("git", "-C", wt, "pull", "--rebase", "origin", MEDIA, check=False)
    return urls


def save_logs(date, show):
    """Keep scripts, research and fact-check reports (small text files) plus the topic state on the main branch."""
    paths = glob.glob(os.path.join(CON, "scripts", "auto", f"{date}-{show}*")) + [os.path.join(CON, "topics_state.json")]
    paths = [p for p in paths if os.path.exists(p)]
    if not paths: return
    sh("git", "-C", ROOT, "add", *paths)
    if sh("git", "-C", ROOT, "diff", "--cached", "--quiet", check=False).returncode == 0: return
    sh("git", "-C", ROOT, "commit", "-q", "-m", f"Script and fact-check: {date} {show}")
    for _ in range(4):
        if sh("git", "-C", ROOT, "pull", "--rebase", "origin", BRANCH, check=False).returncode == 0 and \
           sh("git", "-C", ROOT, "push", "origin", f"HEAD:{BRANCH}", check=False).returncode == 0: break


def chapters(sc, out_dir):
    """Real YouTube chapter timestamps from the rendered timeline."""
    tl = json.load(open(os.path.join(out_dir, "timeline.json")))
    rows = ["0:00 Intro"]
    for ln, t in zip(sc["lines"], tl["lines"]):
        if ln["scene"].get("t") == "chapter":
            s = int(t["s"]); rows.append(f"{s // 60}:{s % 60:02d} {ln['scene'].get('title', '')}")
    return "\n".join(rows)


def make(show, date):
    r = subprocess.run([sys.executable, os.path.join(CON, "studio.py"), "--show", show, "--date", date], capture_output=True, text=True)
    print(r.stdout[-3000:], r.stderr[-3000:])
    if r.returncode in (3, 4): return None
    r.check_returncode()
    return r.stdout.strip().splitlines()[-1]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--show", default="auto"); ap.add_argument("--force", action="store_true")
    a = ap.parse_args(); now = dt.datetime.now(ET); post_at = None
    if a.show == "auto":
        due = [x for x in PLAN[now.weekday()] if x[0] == now.hour]
        if not due: print(f"Nothing scheduled at {now:%a %H:00} ET."); return
        _, a.show, post_at = due[0]
        if now.date() < AUTO_START: print(f"{a.show}: hand-made episodes cover {now:%a %b %d}; automation starts {AUTO_START}."); return
    else:
        post_at = next((p for _, s, p in PLAN[now.weekday()] if s == a.show), None)
    date = now.strftime("%Y-%m-%d"); show = a.show
    path = make(show, date)
    if not path and show in FALLBACK:
        print(f"{show}: nothing qualified; making an evergreen '{FALLBACK[show]}' instead."); show = FALLBACK[show]; path = make(show, date)
    save_logs(date, a.show if show == a.show else f"{a.show}")
    if not path: print("Nothing to post this run."); return
    sc = json.load(open(path)); longform = show in LONG
    import run
    video, cover = run.make(path)
    if longform:
        sc["post"]["yt_desc"] = sc["post"]["yt_desc"].replace("CHAPTERS", chapters(sc, os.path.dirname(video)))
    urls = host([video, cover], date)
    when = dt.datetime.combine(now.date(), dt.time.fromisoformat(post_at), ET) if post_at else now + dt.timedelta(minutes=5)
    if when < now + dt.timedelta(minutes=5): when = now + dt.timedelta(minutes=5)
    import publish
    publish.schedule(urls[0], urls[1], sc["post"], when.strftime("%Y-%m-%dT%H:%M:00"), "America/New_York", longform=longform)
    save_logs(date, show)


if __name__ == "__main__":
    main()
