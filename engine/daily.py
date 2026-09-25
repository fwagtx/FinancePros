"""One scheduled run: research -> script -> fact-check -> render -> commit video -> schedule on all four platforms.

usage: python daily.py --show morning|midday|close|flash
The show only runs inside its Eastern-time window, so cron can fire at both DST offsets safely.
"""
import argparse, datetime as dt, json, os, subprocess, sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ET = ZoneInfo("America/New_York")
# show -> (build window start hour ET, post time ET)
SLOTS = {"morning": (7, "07:30"), "midday": (12, "12:30"), "close": (16, "16:30"), "flash": (None, None)}
REPO = os.environ.get("GITHUB_REPOSITORY", "fwagtx/FinancePros")
BRANCH = os.environ.get("GITHUB_REF_NAME", "claude/dazzling-newton-1ex2s0")


def sh(*cmd, **kw):
    print("+", " ".join(cmd)); return subprocess.run(cmd, check=True, **kw)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--show", required=True, choices=list(SLOTS)); ap.add_argument("--force", action="store_true")
    a = ap.parse_args(); now = dt.datetime.now(ET)
    hour, post_at = SLOTS[a.show]
    if a.show != "flash" and not a.force and (now.weekday() > 4 or now.hour != hour):
        print(f"Outside the {a.show} window ({now:%a %H:%M} ET); skipping."); return
    if a.show == "flash" and not a.force and (now.weekday() > 4 or not (9 <= now.hour < 17)):
        print("Flash checks run on weekdays 9 AM-5 PM ET only."); return
    date = now.strftime("%Y-%m-%d")
    r = subprocess.run([sys.executable, os.path.join(HERE, "news.py"), "--show", a.show, "--date", date], capture_output=True, text=True)
    print(r.stdout, r.stderr)
    if r.returncode in (3, 4):   # 3: no qualifying Flash, 4: failed fact-check -> post nothing
        return
    r.check_returncode()
    ep_path = r.stdout.strip().splitlines()[-1]; ep = json.load(open(ep_path))
    video = subprocess.run([sys.executable, os.path.join(HERE, "build.py"), ep_path], check=True, capture_output=True, text=True).stdout.strip().splitlines()[-1]
    rel = f"videos/daily/{date}/{ep['id']}.mp4"; os.makedirs(os.path.dirname(os.path.join(ROOT, rel)), exist_ok=True)
    sh("cp", video, os.path.join(ROOT, rel))
    sh("git", "-C", ROOT, "add", rel, os.path.relpath(os.path.dirname(ep_path), ROOT))
    sh("git", "-C", ROOT, "commit", "-m", f"Daily video: {ep['id']}")
    sh("git", "-C", ROOT, "push", "origin", f"HEAD:{BRANCH}")
    url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{rel}"
    if post_at:
        when = dt.datetime.combine(now.date(), dt.time.fromisoformat(post_at), ET)
        if when < now + dt.timedelta(minutes=4): when = now + dt.timedelta(minutes=4)
    else:
        when = now + dt.timedelta(minutes=4)
    sys.path.insert(0, HERE); import publish
    publish.schedule(url, ep, when.strftime("%Y-%m-%dT%H:%M:00"), "America/New_York")


if __name__ == "__main__":
    main()
