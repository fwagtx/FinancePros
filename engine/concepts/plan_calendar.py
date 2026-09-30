"""Build the content calendar: a planned topic for every evergreen slot from the start date through the end date.

News slots (morning, bigstory, lf-big) are not planned: they cover whatever happened that day.
Order of precedence for each day: a seasonal money moment (seasonal.json), then the next topic from the show's pool
(topics.json), never repeating a topic that was already used; once a show's pool runs out, its oldest topics\nare re-run (at least a year after they first aired). Every video is still researched and fact-checked on the day
it is made, so the numbers are always current.

  python concepts/plan_calendar.py [--start 2026-10-03] [--end 2028-09-30]
writes concepts/calendar.json (read by studio.pick_topic) and concepts/calendar.csv (for reading in a spreadsheet).
"""
import argparse, csv, datetime as dt, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
TIME = {"explainer": "12:00", "business": "14:00", "hot": "18:00",
        "lf-explained": "16:00", "lf-business": "16:00", "lf-guide": "16:00", "lf-world": "16:00"}
LONG_DAY = {"lf-explained": 0, "lf-business": 1, "lf-guide": 2, "lf-world": 3}   # Monday-Thursday (Friday is the week's news)


def interleave(*pools):
    """Spread several pools evenly through one queue (keeps the mix varied day to day)."""
    total = sum(len(p) for p in pools); out = []; pos = [0] * len(pools)
    for i in range(total):
        # pick the pool that is furthest behind its fair share
        k = min(range(len(pools)), key=lambda j: (pos[j] + 1) / (len(pools[j]) + 1e-9) if pos[j] < len(pools[j]) else 9e9)
        out.append(pools[k][pos[k]]); pos[k] += 1
    return out


def queues(bank):
    s, l = bank["shorts"], bank["longform"]
    return {
        "explainer": interleave(s["explainer_ticker"], s["explainer_acorn"]),
        "business": interleave(s["business"], s.get("business_industry", [])),
        "hot": interleave(s["hot"], s.get("hot_scam", [])),
        "lf-explained": l["explained"], "lf-business": l["business"], "lf-guide": l["guide"], "lf-world": l["world"],
    }


def build(start, end, short_start):
    bank = json.load(open(os.path.join(HERE, "topics.json")))
    st = json.load(open(os.path.join(HERE, "topics_state.json")))
    anchors = json.load(open(os.path.join(HERE, "seasonal.json")))["anchors"]
    used = set(st.get("used", [])) | set(st.get("failed", []))
    q = {k: [t for t in v if t not in used] for k, v in queues(bank).items()}
    placed = set(); cal = {}

    history = {k: [] for k in q}   # (date, topic) per show, for re-runs

    def take(show, day):
        while q[show]:
            t = q[show].pop(0)
            if t not in placed: return t
        # every fresh topic is used: re-run the oldest one that aired at least a year ago (researched again, new numbers)
        for i, (d, t) in enumerate(history[show]):
            if (day - d).days >= 365:
                history[show].pop(i); return t
        return None

    day = start
    while day <= end:
        todays = {}
        for show in ("explainer", "business", "hot"):
            if day >= short_start: todays[show] = None
        for show, wd in LONG_DAY.items():
            if day.weekday() == wd: todays[show] = None
        for m, d, show, topic in anchors:
            if show not in todays or topic in placed: continue
            if show in LONG_DAY:   # long-form: the anchor lands on that show's weekday in the anchor's week
                a = dt.date(day.year, m, d); target = a - dt.timedelta(days=a.weekday()) + dt.timedelta(days=LONG_DAY[show])
                if target != day: continue
            elif (day.month, day.day) != (m, d): continue
            todays[show] = topic; placed.add(topic)
        for show in todays:
            if todays[show] is None: todays[show] = take(show, day)
            if todays[show]: placed.add(todays[show]); history[show].append((day, todays[show]))
        todays = {k: v for k, v in todays.items() if v}
        if todays: cal[day.isoformat()] = todays
        day += dt.timedelta(days=1)
    return cal, {k: len(v) for k, v in q.items()}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--start", default="2026-09-30"); ap.add_argument("--end", default="2029-09-30")
    ap.add_argument("--short-start", default="2026-10-03")
    a = ap.parse_args()
    cal, left = build(dt.date.fromisoformat(a.start), dt.date.fromisoformat(a.end), dt.date.fromisoformat(a.short_start))
    json.dump(cal, open(os.path.join(HERE, "calendar.json"), "w"), indent=1, ensure_ascii=False)
    with open(os.path.join(HERE, "calendar.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["date", "day", "time (CT)", "show", "topic"])
        for d, shows in cal.items():
            for show, topic in sorted(shows.items(), key=lambda x: TIME[x[0]]):
                w.writerow([d, dt.date.fromisoformat(d).strftime("%a"), TIME[show], show, topic])
    n = sum(len(v) for v in cal.values()); last = {}
    for d, shows in cal.items():
        for s in shows: last[s] = d
    print(f"{n} planned videos over {len(cal)} days; last planned day per show: {last}; topics left over: {left}")


if __name__ == "__main__":
    main()
