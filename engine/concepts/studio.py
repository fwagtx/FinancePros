"""FinancePros TV studio: picks the topic, researches it, writes a doodle-template script, fact-checks it.

Shows (see daily.py for the schedule; times are US Central):
  morning      Short 10 AM - the biggest money story this morning (news)
  explainer    Short 12 PM - evergreen explainer from the topic bank (Acorn Economics squirrel or Paper Ticker)
  business     Short  2 PM - "How they make money": the business model behind a company everyone knows
  bigstory     Short  4 PM - the day's most important / most talked-about money story (news; country characters for world stories)
  hot          Short  6 PM - high-engagement evergreen format: money myth, scam alert, face-off, "why is X so expensive"
  lf-explained Long  Mon 4 PM - a high-value money topic explained completely
  lf-business  Long  Tue 4 PM - how a famous company or industry really makes money
  lf-guide     Long  Wed 4 PM - a step-by-step money how-to
  lf-world     Long  Thu 4 PM - world-economy deep dive with country characters
  lf-big       Long  Fri 4 PM - the week's biggest money story in depth (news)

Three Claude calls per video: research (web search) -> script (structured output) -> independent fact-check (web search, must PASS).
usage: python concepts/studio.py --show morning [--date YYYY-MM-DD] [--id 2026-10-05-morning] [--attempt N]
-> prints the script path; exit 3 = nothing to post, 4 = fact-check failed
"""
import argparse, datetime as dt, json, os, random, re, sys
from zoneinfo import ZoneInfo
HERE = os.path.dirname(os.path.abspath(__file__)); ENG = os.path.dirname(HERE); sys.path.insert(0, ENG); sys.path.insert(0, HERE)
import layout
from news import call, WEB   # shared Claude helper (adaptive thinking, fallback, pause_turn handling)

ET = ZoneInfo("America/New_York")
TOPICS = os.path.join(HERE, "topics.json"); TSTATE = os.path.join(HERE, "topics_state.json")

BRAND = """You write for FinancePros TV: hand-drawn doodle explainer videos about money for people aged 18-40.
Look and voice: like a smart friend with a whiteboard. Plain words, short punchy sentences, a little dry humor, zero hype.
Hosts: Ticker, a stick figure with an old TV for a head (calm, curious), and on 'Acorn Economics' episodes a chunky squirrel who
explains money with acorns in short, funny sentences ("Squirrel plants one acorn. Nothing happens.").
Rules that never change:
- Education, never advice: never say buy, sell, hold, "you should invest in", and never predict prices.
- Only confirmed facts: an official source (Fed, BLS, BEA, Treasury, SEC filing, company release, central bank) or two reputable outlets.
- Neutral on politics: explain what a policy does to money; never take sides.
- Every number on screen must match the spoken number. Round when spoken ("about 4 percent"), exact on screen.
- The hook in the first 2 seconds must earn the click, and the video must pay it off. No clickbait.
- No emojis in scripts."""

SHOWS = {
    "morning": ("short", "news", "Morning Money (posts 10 AM Central). The single biggest money story this morning: overnight markets, an economic "
                "report, a big company, or a policy change, explained through what it does to a normal person's money."),
    "explainer": ("short", "bank", "Explainer (posts noon Central). One evergreen money idea explained so well people save it and share it."),
    "business": ("short", "bank", "How They Make Money (posts 2 PM Central). The surprising business model behind a company or industry everyone "
                 "knows, with the real numbers from its annual report (10-K) or official filings. Curious and neutral: never a stock tip."),
    "bigstory": ("short", "news", "The Big Story (posts 4 PM Central). The day's most important or most talked-about money story "
                 "(markets, jobs, prices, housing, AI and big tech, trade, world economy). If it's international, tell it with country characters."),
    "hot": ("short", "bank", "Hot Take (posts 6 PM Central). A high-engagement evergreen format: Money Myth (myth, then fact), Scam Alert, "
            "Face-off (A vs B), or 'Why is X so expensive'. Surprising, useful, shareable."),
    "lf-explained": ("long", "bank", "Explained (YouTube, 16:9, 8-10 minutes). One high-value money topic explained completely, from zero, "
                     "with real numbers, history, worked examples and a clear takeaway."),
    "lf-business": ("long", "bank", "How They Make Money (YouTube, 16:9, 8-10 minutes). How a famous company or a whole industry really makes "
                    "its money: the history, the business model with numbers from its filings, the clever parts, the risks, and what it "
                    "means for the customer. Curious and neutral: never a stock tip."),
    "lf-guide": ("long", "bank", "The Guide (YouTube, 16:9, 8-10 minutes). A practical, step-by-step money how-to for a beginner: every step "
                 "in order, the real rules and limits, worked examples with exact math, the common mistakes, and a one-screen checklist. "
                 "Education, not advice: explain the options and trade-offs, never tell the viewer what to buy."),
    "lf-world": ("long", "bank", "World Money (YouTube, 16:9, 8-10 minutes). A world-economy story told with country characters: "
                 "how it works, the history, and how it reaches an American's wallet."),
    "lf-big": ("long", "news", "The Big Story of the Week (YouTube, 16:9, 8-10 minutes). The week's most important money story in depth: "
               "what happened, the history that explains it, who wins and loses, what it means for your money, what to watch next."),
}
BANK = {"hot": ("shorts", "hot"), "business": ("shorts", "business"), "lf-explained": ("longform", "explained"),
        "lf-business": ("longform", "business"), "lf-guide": ("longform", "guide"), "lf-world": ("longform", "world")}

INTEREST = """How to pick (score each candidate 1-5 on each, pick the highest total):
- Reach: does it touch anyone with a paycheck, rent, loan, savings, or a 401(k)?
- Surprise: is there a fact most people don't know or would argue about?
- Value: is it in a high-value money category (investing, retirement, credit, taxes, housing/mortgages, insurance, banking, income, AI economy)?
- Visual: can it be drawn simply (a chart, a comparison, countries, a before/after)?
- Confirmed: official source or two reputable outlets (a 1 here disqualifies it)."""

# ---------------- structured output schema (template scripts) ----------------
S = {"type": "string"}; N = {"type": "number"}; I = {"type": "integer"}
SIDE = {"type": "object", "additionalProperties": False, "properties": {"label": S, "value": S, "tone": {"type": "string", "enum": ["up", "down", "neutral"]}, "sub": S, "title": S, "items": {"type": "array", "items": S}}}
SCENE = {"type": "object", "additionalProperties": False, "required": ["t"], "properties": {
    "t": {"type": "string", "enum": list(layout.TEMPLATES)}, "keep": {"type": "boolean"},
    "mood": {"type": "string", "enum": ["happy", "up", "shock", "worried", "think", "angry", "sad"]},
    "title": S, "prop": {"type": "string", "enum": list(layout.PROPS)}, "label": S, "value": S, "sub": S, "tone": {"type": "string", "enum": ["up", "down", "neutral"]},
    "lines": {"type": "array", "items": S},
    "points": {"type": "array", "items": {"type": "array", "items": N}}, "prefix": S, "suffix": S, "end": S, "color": {"type": "string", "enum": ["up", "down"]},
    "chart_note": {"type": "object", "additionalProperties": False, "properties": {"x": N, "text": S}, "required": ["x", "text"]},
    "left": SIDE, "right": SIDE, "winner": {"type": "string", "enum": ["left", "right"]},
    "items": {"type": "array", "items": S}, "reveal": I,
    "from": {"type": "object", "additionalProperties": False, "properties": {"label": S, "value": S}, "required": ["label", "value"]},
    "to": {"type": "object", "additionalProperties": False, "properties": {"label": S, "value": S}, "required": ["label", "value"]},
    "cast": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["name"], "properties": {
        "name": {"type": "string", "enum": list(layout.COUNTRY_COLOR)}, "mood": {"type": "string", "enum": ["happy", "worried", "angry", "sad"]}, "says": S}}},
    "caption": S, "kind": S, "headline": S, "source": S, "text": S,
    "events": {"type": "array", "items": {"type": "object", "additionalProperties": False, "properties": {"when": S, "what": S}, "required": ["when", "what"]}},
    "n": I, "tagline": S, "note": S, "name": S}}
SCRIPT = {"type": "object", "additionalProperties": False, "required": ["series", "header", "cover", "lines", "post"], "properties": {
    "series": {"type": "string", "enum": ["ticker", "acorn"]},
    "header": S,
    "cover": {"type": "object", "additionalProperties": False, "required": ["title"], "properties": {
        "title": S, "prop": {"type": "string", "enum": list(layout.PROPS)}, "label": S, "value": S, "countries": {"type": "array", "items": S}}},
    "lines": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["who", "text", "say", "scene"], "properties": {
        "who": {"type": "string", "enum": ["ticker", "nutty"]}, "text": S, "say": S, "scene": SCENE}}},
    "post": {"type": "object", "additionalProperties": False, "required": ["title", "ig", "tiktok", "yt_desc"], "properties": {
        "title": S, "ig": S, "tiktok": S, "yt_desc": S, "tags": {"type": "array", "items": S}}}}}

TEMPLATE_GUIDE = """Draw every line with ONE template in scene.t (the renderer lays it out; you never give coordinates):
- hook: title (<=7 words, wrap ONE key word in [brackets] to color it red), prop (bill|card|house|car|bag|coins|fed|store|customs|chart-up|chart-down|fire|acorns|box|tag|mattress|pot|paper|none), label (text on the prop, e.g. "$1,000"), value (big red marker text, <=8 chars, e.g. "-88¢", "x2").
- board: chalkboard, lines (1-3 lines, <=26 chars each). Good for a definition or a formula.
- chart: title, points [[x, y], ...] (4-40 real data points, x numeric like a year or month), prefix ("$") / suffix ("%"), end (label at the last point, e.g. "$808"), color up|down.
  Next line with keep:true and chart_note {x, text} circles a point in red with a short note ("9.1% in a year!").
- compare: title, left/right {label, value (<=7 chars), tone up|down|neutral, sub}. Next line keep:true + winner left|right circles the winner.
- list: title, items (2-4, <=5 words each), reveal (how many show on this line). Following lines keep:true reveal the next item.
- stat: label (what the number is), value (big, <=9 chars), tone, sub (small source/context line).
- money: from {label, value} -> to {label, value}, e.g. a 1970 dollar -> "about 12¢".
- countries: cast (1-3 of us|china|japan|uk|germany|mexico|canada, each with mood and optional says <=18 chars), prop {kind: box|bag|tag, label}, caption (short red line). Countries are the characters; no host.
- building: kind fed|store|customs, label (a tag on it, e.g. "rate: 4.5%"), caption, name (the sign on the building; the fed building says
  FEDERAL RESERVE unless you set name, so ALWAYS set name for any other central bank, e.g. "BANK OF JAPAN", "EUROPEAN CENTRAL BANK").
- news: headline (<=10 words, factual), source (outlet or agency and date).
- quote: text (a real, exact quote <=30 words), source (who said it and when).
- timeline: events [{when, what (<=6 words)}] (3-5), reveal; keep:true lines reveal the next event.
- split: title, left {title, items (2-4 short), tone}, right {same}. Good vs bad, winners vs losers.
- squirrel (Acorn Economics only): kind pile|plant|wait|tree|basket|fire|think|bank, caption (big marker text like "30 years later"), value (big red number for think), label.
- chapter (long-form only): n, title (<=6 words).
- cta: last line only. tagline optional.
Every line may set mood (happy|up|shock|worried|think|angry|sad) for the host. Change the picture every 1-2 lines; use at least 5 different
templates in a short and many more in a long-form. Prefer a real chart, stat, compare, or countries whenever there is a number or a place."""

SHORT_GUIDE = """Write a vertical short (TikTok, Reels, YouTube Shorts): 35-55 seconds, 100-150 spoken words, 7-11 lines.
Structure: hook line (the surprising fact or question) -> the key number -> why it matters to your money -> one simple takeaway -> final line
"That's the money. Follow for more." with t = cta. (Acorn Economics ends with "Squirrel explained <topic>. Squirrel would like one follow.")
header: the on-screen title at the top of the video, 2 short lines separated by \\n (<= 22 chars per line), handwritten style, no brackets.
cover: the 9:16 cover: title (<=6 words, Title Case, can be a question), a prop, and a big red value or label; or countries (1-2) for world stories.
post.title: <= 60 chars, specific, curiosity without clickbait.
post.ig: Instagram/Facebook caption: 1 hook line, 2-4 short lines of the key facts with numbers, a sources line, "News and education, not financial advice.",
"Follow @financeprostv for money explained simply.", then 5 hashtags (lowercase) ending with #financeprostv.
post.tiktok: <= 150 chars incl. 4-5 hashtags (#moneytok, #personalfinance, topic tags, #financeprostv) and "Not financial advice."
post.yt_desc: 2-4 sentence YouTube Shorts description with the facts and sources, "News and education, not financial advice.", then "#Shorts" + 2 hashtags.
post.tags: 5 YouTube tags."""

LONG_GUIDE = """Write a long-form YouTube video (16:9): 8-10 minutes, 1250-1550 spoken words, 75-110 lines (8+ minutes allows mid-roll ads).
Open with a 20-40 second cold open (the most surprising fact + the promise of the video), then chapters: a line with t = chapter before each of
4-6 chapters. Inside chapters use every template type that fits, with real charts and data. Close with a recap chapter and the cta line.
cover: the YouTube thumbnail: title (<= 5 words, Title Case, ends with a period or question mark, like 'Nobody Is Talking About This.'), a prop or
countries, and a big red value. post.title: <= 90 chars, specific and curious. post.yt_desc: 3-4 sentence summary, then the line CHAPTERS
(the system inserts real timestamps), then sources (outlet/agency + date), "News and education, not financial advice.", 3 hashtags.
post.ig and post.tiktok: a one-line teaser each (they are not posted for long-form). Chapter titles must be short."""


def load_state():
    st = json.load(open(TSTATE)) if os.path.exists(TSTATE) else {}
    st.setdefault("used", []); st.setdefault("added", {}); st.setdefault("failed", []); return st


def pick_topic(show, now, attempt=0):
    """Next unused bank topic for this slot. Rotates series for explainers; refills the bank with new researched topics when low.
    Topics that failed a fact-check are skipped; attempt varies the pick when a slot is retried."""
    bank = json.load(open(TOPICS)); st = load_state()
    if show == "explainer":
        sec, key = "shorts", ("explainer_acorn" if now.weekday() in (0, 2, 4, 6) else "explainer_ticker")
    else:
        sec, key = BANK.get(show, ("longform", "explained"))
    pool = bank[sec][key] + st["added"].get(key, [])
    bad = set(st["used"]) | set(st.get("failed", []))
    left = [t for t in pool if t not in bad]
    if len(left) < 3:
        new = [t for t in refill(key, pool, now) if t not in pool]
        st["added"].setdefault(key, []).extend(new); left += new
        json.dump(st, open(TSTATE, "w"), indent=1)
    if not left:   # everything used: start a fresh cycle
        st["used"] = [t for t in st["used"] if t not in pool]; st["failed"] = [t for t in st.get("failed", []) if t not in pool]
        json.dump(st, open(TSTATE, "w"), indent=1); left = pool
    random.seed(f"{now:%Y%m%d}{show}{attempt}")
    return key, random.choice(left[:6])


def mark_failed(topic):
    st = load_state(); st.setdefault("failed", []).append(topic); json.dump(st, open(TSTATE, "w"), indent=1)


def mark_used(topic):
    st = load_state(); st["used"].append(topic); json.dump(st, open(TSTATE, "w"), indent=1)


def refill(key, pool, now):
    q = (f"Today is {now:%B %d, %Y}. Suggest 20 NEW evergreen video topics for the FinancePros TV slot '{key}' that are not in this list:\n"
         + "\n".join("- " + p for p in pool) + f"\n\n{INTEREST}\nUse web search to see what money questions people are searching and talking about now. "
         "Return only a JSON array of 20 topic strings.")
    try: out = call(BRAND, q, tools=WEB)
    except Exception as e:   # no API key (session mode) or an API error: keep cycling the existing bank
        print("topic refill skipped:", type(e).__name__); return []
    m = re.search(r"\[.*\]", out, re.S)
    try: return [t for t in json.loads(m.group(0)) if isinstance(t, str)][:20] if m else []
    except Exception: return []


HINT = {
    "business": "Take every company number from its most recent annual report (10-K) or official investor materials and name the fiscal year. ",
    "lf-business": "Take every company number from its most recent annual report (10-K) or official investor materials and name the fiscal year. ",
    "lf-guide": "Confirm every rule, limit, fee and deadline that applies this year from the official source (IRS, CFPB, SEC, FINRA, FDIC, "
                "or the provider's own pages) and lay the steps out in order. ",
}


def research_prompt(show, now, topic=None):
    kind, src, desc = SHOWS[show]
    if src == "bank":
        q = (f"Today is {now:%A, %B %d, %Y}. Show: {desc}\nTopic: {topic}\n\n"
             "Research this topic. If there is a timely news angle this week, use it as the hook. Use web search to confirm every number, rule, "
             "limit and definition that can change, and give the source for each. Find at least one REAL data series that can be charted "
             "(with the actual values and the source), one worked example with exact math (show the calculation), and the one fact that "
             "surprises people. " + HINT.get(show, "") + ("Plan 5-7 chapters with the key points for each. " if kind == "long" else "")
             + "Finish with 'SOURCES:' and the list.")
    else:
        q = (f"Today is {now:%A, %B %d, %Y}, {now:%I:%M %p} Eastern.\nShow: {desc}\n\n{INTEREST}\n\n"
             "Search the web for money and economy news from the last 24 hours" + (" and this week" if kind == "long" else "") + ". "
             "List 5 candidates with their scores, pick the best one, then write a research brief: the facts, every number with its exact value "
             "and date, a REAL data series to chart if one exists (actual values + source), the history or context that explains it, what it means "
             "for a normal person's money, and what to watch next. " + ("Plan 4-6 chapters. " if kind == "long" else "")
             + "Finish with 'SOURCES:' and the URLs. If nothing is confirmed and important, answer only NOTHING_TODAY.")
    return q


def research(show, now, topic=None):
    return call(BRAND, research_prompt(show, now, topic), tools=WEB)


def write_prompt(show, brief, now, topic=None):
    kind, src, desc = SHOWS[show]
    series_hint = ("This is an Acorn Economics episode: series 'acorn', who 'nutty' on every line, use squirrel scenes plus charts/compare/lists. "
                   if topic and "acorn" in topic.lower() else "Series 'ticker': who 'ticker' on every line. ")
    q = (f"Date: {now:%A, %B %d, %Y}. Show: {desc}\n" + (f"Topic: {topic}\n" if topic else "") + series_hint +
         f"\nResearch brief (the ONLY facts you may use):\n{brief}\n\n{TEMPLATE_GUIDE}\n\n{LONG_GUIDE if kind == 'long' else SHORT_GUIDE}\n"
         "Each line: who, text (the caption, numerals allowed), say (the same sentence written for the voice: numbers, symbols and "
         "acronyms in words, like 'twenty-four percent' and 'A P R'), scene.")
    return q


def write_script(show, brief, now, topic=None):
    kind = SHOWS[show][0]; q = write_prompt(show, brief, now, topic)
    try:
        return json.loads(call(BRAND, q, fmt=SCRIPT, max_tokens=64000 if kind == "long" else 16000))
    except Exception as e:   # schema rejected or truncated: ask for plain JSON and parse it ourselves
        print("structured output failed, retrying as plain JSON:", e)
        out = call(BRAND, q + "\n\nReturn ONLY one JSON object matching this JSON schema, no prose:\n" + json.dumps(SCRIPT), max_tokens=64000 if kind == "long" else 16000)
        return json.loads(out[out.index("{"):out.rindex("}") + 1])


def factcheck_prompt(sc, brief, now):
    def shown(s): return json.dumps({k: v for k, v in s.items() if k not in ("t", "keep", "mood", "prop", "color", "tone", "n", "reveal")}, ensure_ascii=False)
    body = "\n".join(f"- {l['text']}  | on screen: {shown(l['scene'])}" for l in sc["lines"])
    q = (f"Today is {now:%A, %B %d, %Y}, {now:%I:%M %p} ET. Fact-check this FinancePros TV video before it is published.\n\n"
         f"Header: {sc['header']}\nCover: {json.dumps(sc['cover'])}\nScript:\n{body}\n\nPost text:\n{json.dumps(sc['post'], ensure_ascii=False)}\n\n"
         f"Research brief it was written from:\n{brief}\n\n"
         "Independently verify every factual claim, number and chart data point with web search (do not trust the brief). Also flag: stale news, "
         "advice or price predictions, political opinion, a cover or title the video doesn't pay off, math errors in worked examples, "
         "and any on-screen value that differs from the spoken one. List each issue. Finish with exactly one line: VERDICT: PASS or VERDICT: FAIL.")
    return q


def factcheck(sc, brief, now):
    q = factcheck_prompt(sc, brief, now)
    out = call(BRAND, q, tools=WEB)
    v = re.findall(r"VERDICT:\s*(PASS|FAIL)", out)
    return (v[-1] == "PASS" if v else False), out


def sanitize(sc, show, date):
    """Keep the model inside what the renderer can draw; convert schema shapes to layout shapes."""
    kind = SHOWS[show][0]; acorn = sc.get("series") == "acorn"
    lines = []; prev_t = None
    for ln in sc["lines"]:
        s = dict(ln["scene"])
        if s.get("keep") and s.get("t") != prev_t:   # a "keep" line must continue the same template (e.g. not follow a chapter card)
            s = {"t": "hook", "title": ln["text"][:48], "prop": "none"}
        if s["t"] == "squirrel" and not acorn: s = {"t": "hook", "title": ln["text"][:50], "prop": "acorns"}
        if s["t"] == "chapter" and kind != "long": continue
        if s.get("chart_note"): s["note"] = s.pop("chart_note")
        if s["t"] == "timeline": s["events"] = [[e.get("when", ""), e.get("what", "")] for e in s.get("events", [])]
        if s["t"] == "chart" and not s.get("keep"):
            pts = [p for p in s.get("points", []) if isinstance(p, list) and len(p) == 2]
            if len(pts) < 3: s = {"t": "stat", "label": s.get("title", ""), "value": s.get("end", ""), "tone": "neutral"}
            else: s["points"] = pts
        if s["t"] == "building" and s.get("kind") not in ("fed", "store", "customs"): s["kind"] = "fed"
        if s["t"] == "countries" and not s.get("keep"): s["cast"] = [c for c in s.get("cast", []) if c.get("name") in layout.COUNTRY_COLOR][:3] or [{"name": "us"}]
        who = "nutty" if acorn else "ticker"
        lines.append({"who": who, "text": ln["text"], "say": ln.get("say") or ln["text"], "scene": s}); prev_t = s["t"]
    if not lines or lines[-1]["scene"]["t"] != "cta":
        lines.append({"who": "nutty" if acorn else "ticker", "text": "That's the money. Follow for more.", "say": "That's the money. Follow for more.", "scene": {"t": "cta"}})
    out = {"id": f"{date}-{show}", "format": "landscape" if kind == "long" else "vertical", "series": "acorn" if acorn else "ticker",
           "header": sc.get("header", "").replace("[", "").replace("]", ""), "cover": sc.get("cover", {}), "lines": lines, "post": sc["post"]}
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--show", required=True, choices=list(SHOWS)); ap.add_argument("--date"); ap.add_argument("--topic")
    ap.add_argument("--id", help="slot id used for file names, e.g. 2026-10-05-morning"); ap.add_argument("--attempt", type=int, default=0)
    a = ap.parse_args(); now = dt.datetime.now(ET); date = a.date or now.strftime("%Y-%m-%d"); sid = a.id or f"{date}-{a.show}"
    logdir = os.path.join(HERE, "scripts", "auto"); os.makedirs(logdir, exist_ok=True)
    log = lambda part: os.path.join(logdir, f"{sid}.{a.show}.{part}.md")
    topic = a.topic
    if SHOWS[a.show][1] == "bank" and not topic: _, topic = pick_topic(a.show, now, a.attempt)
    if topic: print("Topic:", topic)
    brief = research(a.show, now, topic)
    open(log("research"), "w").write(brief)
    if brief.strip().endswith("NOTHING_TODAY") and SHOWS[a.show][1] == "news":
        print("Nothing confirmed and important today."); sys.exit(3)
    sc = sanitize(write_script(a.show, brief, now, topic), a.show, date)
    sc["id"] = sid
    ok, report = factcheck(sc, brief, now)
    open(log("factcheck"), "w").write(report)
    if not ok:
        if topic: mark_failed(topic)
        print("Fact-check FAILED; nothing will be posted."); sys.exit(4)
    if topic: mark_used(topic)
    path = os.path.join(logdir, f"{sid}.json"); json.dump(sc, open(path, "w"), indent=1, ensure_ascii=False)
    print(path)


if __name__ == "__main__":
    main()
