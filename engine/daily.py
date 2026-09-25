"""One scheduled run: research -> script -> fact-check -> render -> commit video -> schedule on all four platforms.

usage: python daily.py --show morning|midday|close|flash
The show only runs inside its Eastern-time window, so cron can fire at both DST offsets safely.
"""
import argparse, datetime as dt, json, os, subprocess, sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ET = ZoneInfo("America/New_York")
# The weekly plan (Eastern time). Each entry: weekday (0=Mon) -> [(build hour, show, post time)].
# About 3 short videos a day on all four platforms, plus 3 long-form YouTube videos a week (lf-*).
PLAN = {
    0: [(7, "morning", "07:30"), (11, "lesson", "12:30"), (16, "close", "16:30"), (14, "lf-world", "18:00")],
    1: [(7, "morning", "07:30"), (11, "lesson", "12:30"), (16, "close", "16:30")],
    2: [(7, "morning", "07:30"), (11, "lesson", "12:30"), (16, "close", "16:30"), (14, "lf-school", "18:00")],
    3: [(7, "morning", "07:30"), (11, "world", "12:30"), (16, "close", "16:30")],
    4: [(7, "morning", "07:30"), (11, "lesson", "12:30"), (16, "close", "16:30")],
    5: [(6, "lf-week", "09:00"), (9, "recap", "10:00"), (12, "lesson", "13:00"), (16, "world", "17:00")],
    6: [(10, "lesson", "11:00"), (13, "world", "14:00"), (17, "ahead", "18:00")],
}
LONGFORM = {"lf-world", "lf-school", "lf-week"}
REPO = os.environ.get("GITHUB_REPOSITORY", "fwagtx/FinancePros")
BRANCH = os.environ.get("GITHUB_REF_NAME", "claude/dazzling-newton-1ex2s0")


def sh(*cmd, **kw):
    print("+", " ".join(cmd)); return subprocess.run(cmd, check=True, **kw)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--show", default="auto"); ap.add_argument("--force", action="store_true")
    a = ap.parse_args(); now = dt.datetime.now(ET)
    if a.show == "auto":          # hourly cron: run whatever the plan says is due this hour (if anything)
        due = [x for x in PLAN[now.weekday()] if x[0] == now.hour]
        if not due:
            if now.weekday() < 5 and 9 <= now.hour < 17: a.show, post_at = "flash", None
            else: print(f"Nothing scheduled at {now:%a %H:00} ET."); return
        else:
            _, a.show, post_at = due[0]
    else:
        post_at = next((p for _, s, p in PLAN[now.weekday()] if s == a.show), None)
    date = now.strftime("%Y-%m-%d")
    r = subprocess.run([sys.executable, os.path.join(HERE, "news.py"), "--show", a.show, "--date", date], capture_output=True, text=True)
    if a.show == "lesson": subprocess.run(["git", "-C", ROOT, "add", os.path.join(HERE, "state.json")])
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
    for _ in range(4):   # another run may have pushed meanwhile
        if subprocess.run(["git", "-C", ROOT, "pull", "--rebase", "origin", BRANCH]).returncode == 0 and \
           subprocess.run(["git", "-C", ROOT, "push", "origin", f"HEAD:{BRANCH}"]).returncode == 0: break
    url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/{rel}"
    if post_at:
        when = dt.datetime.combine(now.date(), dt.time.fromisoformat(post_at), ET)
        if when < now + dt.timedelta(minutes=4): when = now + dt.timedelta(minutes=4)
    else:
        when = now + dt.timedelta(minutes=4)
    sys.path.insert(0, HERE); import publish
    publish.schedule(url, ep, when.strftime("%Y-%m-%dT%H:%M:00"), "America/New_York", longform=a.show in LONGFORM)


if __name__ == "__main__":
    main()
