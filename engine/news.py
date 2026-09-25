"""Live news -> Ticker episode, with a fact-check gate.

Three Claude calls per episode:
  1. research  - Claude searches today's news and picks the story that matters most (importance score).
  2. script    - Claude writes the episode JSON (structured output) from the research brief only.
  3. factcheck - a separate pass re-verifies every claim and number on the web. Anything that fails is not posted.

usage: python news.py --show morning|midday|close|flash [--date YYYY-MM-DD]
Writes engine/episodes/daily/<date>-<show>.json, or exits with code 3 when nothing qualifies.
"""
import argparse, datetime as dt, json, os, re, sys
from zoneinfo import ZoneInfo
import anthropic

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = "claude-opus-5"
ET = ZoneInfo("America/New_York")
_client = None


def client():
    global _client
    if _client is None:
        _client = anthropic.Anthropic()
    return _client

BRAND = """You write for FinancePros TV, an animated money-news channel for people aged 18-40 who don't read the financial pages.
Hosts: Ticker (a calm, quick, slightly dry TV-headed anchor) and Dot (a friendly glowing pixel who explains one money term).
Rules that never change:
- Education, never advice. Never say buy, sell, hold, "you should", or predict prices.
- Only confirmed facts: an official source (Fed, BLS, BEA, SEC filing, company release) or two independent reputable outlets. No rumors.
- Neutral on politics: say what a policy does to money, never take sides.
- Every episode ties the story to one money basic that Dot explains in plain words.
- Plain words for the ear: short sentences, contractions, round numbers when spoken ("about 4 percent"), exact figures only on screen.
- No hype words (mooning, insane, crashing unless it truly crashed). No emojis. No clickbait that the video doesn't pay off."""

SHOWS = {
    "morning": "Morning Brief (posts 7:30 AM ET). What moved overnight in Asia/Europe and U.S. futures, plus the one thing to watch today.",
    "midday": "Midday Pulse (posts 12:30 PM ET). One story explained through what it means for a normal person's wallet. Theme by weekday: Mon Money Myth Monday, Tue Pocketbook Tuesday (prices people pay), Wed Why Is This Moving? (one famous company), Thu World Money Thursday, Fri Friday Face-off (two things compared).",
    "close": "Closing Bell (posts 4:30 PM ET). How U.S. stocks closed today, the biggest winner or loser and why, and what reports after hours.",
    "flash": "FP Flash (breaking). Only if something important broke in the last 90 minutes.",
    "world": "World Money (short). The most important non-U.S. finance story today (central banks abroad, currencies, oil, trade, China, Europe, Japan) and how it reaches an American's wallet.",
    "recap": "Week in 60 (Saturday). The five stories that moved money this week, about 10 seconds each, U.S. and world.",
    "ahead": "Week Ahead (Sunday). The coming week's calendar: big earnings, economic data releases, Fed or central-bank meetings, with the day each lands and why it matters.",
    "lesson": "FP Money School lesson. Evergreen financial education on one topic (given below). No news hook needed; make it practical, with one worked example with real math.",
    "lf-world": "World Money Weekly (YouTube long-form, 16:9, 7-9 minutes). The week's biggest global finance stories explained in depth: markets in Asia, Europe and the U.S., currencies, commodities, central banks, trade. Chapters.",
    "lf-school": "Money School Deep Dive (YouTube long-form, 16:9, 8-10 minutes). One financial-basics topic (given below) explained completely, from zero, with worked examples. Chapters.",
    "lf-week": "This Week in Money (YouTube long-form, 16:9, 8-10 minutes). The full week recap, U.S. and world, and what's coming next week. Chapters.",
}
LONGFORM = {"lf-world", "lf-school", "lf-week"}
EVERGREEN = {"lesson", "lf-school"}

SCORING = """Importance score (out of 25). Reach x2 (up to 10: does it touch anyone with a loan, job, rent or savings?),
Size (up to 5), Surprise vs expectations (up to 5), Confirmed by an official source or two outlets (up to 5; 0 means not usable).
Tier 1 (always Flash): Fed rate decisions or emergency moves; jobs/CPI/GDP releases; S&P 500 moving 2%+ in a day or market-wide halts;
a major bank failing; shutdown/debt-ceiling outcomes or a tax/stimulus law signed; a world event that moves oil 5%+.
Tier 2 (Flash only if score >= 18): a top-10 company moving 5%+ on earnings; 1,000+ layoffs at a household name; $20B+ deals with known brands;
Bitcoin moving 8%+ in a day; mortgage rates or gas prices at multi-year highs/lows.
Never a Flash: analyst upgrades, small stocks, rumors, opinions, anything that sounds like a stock tip."""


def call(system, user, tools=None, fmt=None, max_tokens=16000):
    """One Claude request with adaptive thinking, server-side refusal fallback, and pause_turn continuation."""
    messages = [{"role": "user", "content": user}]
    output_config = {"effort": "high"}
    if fmt:
        output_config["format"] = {"type": "json_schema", "schema": fmt}
    for _ in range(6):
        kw = dict(model=MODEL, max_tokens=max_tokens, system=system, messages=messages,
                  thinking={"type": "adaptive"}, output_config=output_config,
                  betas=["server-side-fallback-2026-07-01"], fallbacks="default")
        if tools:
            kw["tools"] = tools
        with client().beta.messages.stream(**kw) as stream:
            resp = stream.get_final_message()
        if resp.stop_reason == "refusal":
            raise RuntimeError(f"Request declined: {resp.stop_details}")
        if resp.stop_reason == "pause_turn":          # server tool loop hit its step limit; continue the same turn
            messages = messages + [{"role": "assistant", "content": resp.content}]
            continue
        if resp.stop_reason == "max_tokens":
            raise RuntimeError("Response hit max_tokens")
        return "".join(b.text for b in resp.content if b.type == "text")
    raise RuntimeError("Too many pause_turn continuations")


WEB = [{"type": "web_search_20260209", "name": "web_search", "max_uses": 10}]


def research(show, now, topic=None):
    if show in EVERGREEN:
        q = (f"Today is {now:%B %d, %Y}. Show: {SHOWS[show]}\nTopic: {topic}\n\n"
             "Research this topic for a beginner audience. Use web search to confirm every rule, limit, number and definition that can change "
             "(for example contribution limits, legal protections, typical rates) and give the source for each. Write a research brief with: "
             "the plain-English explanation, the 3-5 key facts, one worked example with exact math (show the calculation), common mistakes, "
             "one short money term to define, and the sources. " + ("Plan 5-7 chapters. " if show in LONGFORM else "") + "End with a line 'SCORE: 25'.")
        return call(BRAND, q, tools=WEB)
    q = (f"Today is {now:%A, %B %d, %Y}, {now:%I:%M %p} Eastern Time.\n"
         f"Show: {SHOWS[show]}\n\n{SCORING}\n\n"
         "Search the web for today's finance and economy news for this show. Use only sources published today (or the last 90 minutes for a Flash). "
         "List up to 5 candidate stories with their importance score, then pick the single best story for this show. "
         "For the chosen story, write a research brief with: the facts, every number with its exact value and date, "
         "what it means for a normal person's money, one money-basics term it teaches, what to watch next, and the source URLs "
         "(at least one official source or two independent outlets). "
         + ("This is long-form: cover 4-6 stories in depth and plan chapters. " if show in LONGFORM else "")
         + ("For a Flash: if no story is Tier 1 or scores 18+, end your answer with the line NO_FLASH. " if show == "flash" else "")
         + "End with a line 'SCORE: <n>'.")
    return call(BRAND, q, tools=WEB)


SCENE = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "type": {"type": "string", "enum": ["title", "number", "list", "vs", "term", "bars", "stats", "steps", "map", "chapter", "outro"]},
        "bars": {"type": "array", "items": {"type": "object", "additionalProperties": False,
                 "properties": {"label": {"type": "string"}, "value": {"type": "number"}, "display": {"type": "string"},
                                "tone": {"type": "string", "enum": ["up", "down", "neutral", "brand"]}}, "required": ["label", "value", "display", "tone"]}},
        "stats": {"type": "array", "items": {"type": "object", "additionalProperties": False,
                  "properties": {"k": {"type": "string"}, "v": {"type": "string"}, "tone": {"type": "string", "enum": ["up", "down", "neutral"]}}, "required": ["k", "v", "tone"]}},
        "region": {"type": "string", "enum": ["us", "europe", "uk", "china", "japan", "india", "middle-east", "latam", "canada", "africa", "australia", "world"]},
        "chapter": {"type": "integer"},
        "group": {"type": "string"},
        "headline": {"type": "string"}, "sub": {"type": "string"},
        "label": {"type": "string"}, "value": {"type": "string"},
        "color": {"type": "string", "enum": ["up", "down", "neutral"]}, "note": {"type": "string"},
        "term": {"type": "string"}, "def": {"type": "string"}, "example": {"type": "string"},
        "title": {"type": "string"},
        "items": {"type": "array", "items": {"type": "object", "additionalProperties": False,
                  "properties": {"h": {"type": "string"}, "d": {"type": "string"}}, "required": ["h", "d"]}},
        "reveal": {"type": "integer"},
        "left": {"type": "object", "additionalProperties": False, "properties": {"tag": {"type": "string"}, "name": {"type": "string"}, "rows": {"type": "array", "items": {"type": "string"}}}, "required": ["tag", "name", "rows"]},
        "right": {"type": "object", "additionalProperties": False, "properties": {"tag": {"type": "string"}, "name": {"type": "string"}, "rows": {"type": "array", "items": {"type": "string"}}}, "required": ["tag", "name", "rows"]},
        "expr": {"type": "string", "enum": ["neutral", "up", "down", "worried", "shock", "think", "wink", "dollar"]},
        "pose": {"type": "string", "enum": ["none", "point", "present", "think", "thumb", "shrug"]},
        "tk": {"type": "string", "enum": ["dock", "big", "off"]},
    },
    "required": ["type", "expr", "tk"],
}
EPISODE = {
    "type": "object", "additionalProperties": False,
    "properties": {
        "tag": {"type": "string"}, "title": {"type": "string"}, "caption": {"type": "string"}, "yt_title": {"type": "string"},
        "lines": {"type": "array", "items": {"type": "object", "additionalProperties": False,
                  "properties": {"who": {"type": "string", "enum": ["ticker", "dot"]}, "text": {"type": "string"},
                                 "say": {"type": "string"}, "scene": SCENE},
                  "required": ["who", "text", "say", "scene"]}},
    },
    "required": ["tag", "title", "caption", "yt_title", "lines"],
}

SCRIPT_GUIDE = """Write one 30-50 second episode (110-150 spoken words) as JSON.
Structure: hook (the news in one sentence, with the headline on screen) -> what happened (key number) -> why it matters to you ->
Dot explains one term (1-2 lines) -> what to watch next -> final line exactly "That's the money. See you at the next bell." with an outro scene.
Fields per line: who, text (caption text, numerals allowed), say (the same sentence written the way it should be spoken: numbers and symbols in words,
tickers and acronyms spaced out like "A P R"), scene.
Scenes:
- title: headline (max 7 words; wrap ONE key phrase in [square brackets] for the highlight), optional sub (short, plain).
- number: label (short), value (LED text, max 8 characters, ONLY A-Z 0-9 $ % . , - + and space; e.g. "$4.12", "-2.3%", "82 MONTHS"), color up|down|neutral, note (short, one [highlight] allowed).
- list: title, items [{h, d}] (max 3, h max 5 words), reveal = how many items are visible at this line. Consecutive list lines share the same group.
- vs: left/right {tag, name (one word), rows (3 short rows)}, reveal = rows visible. Same group for consecutive lines.
- term: term (LED, max 10 characters, same allowed characters), def (one sentence, one [highlight]), example (short). Use tk "off" for term scenes; Dot speaks them.
- bars: title + bars [{label, value (number used for bar length), display (text shown, e.g. "$1,500" or "4.1%"), tone}] (2-5 bars). Great for comparisons and before/after.
- stats: title + stats [{k (short label), v (short value, e.g. "4.3%"), tone}] (3-4 stats). For "the numbers at a glance".
- steps: title + items [{h, d}] (2-4) + reveal. For processes ("how a mortgage payment splits").
- map: region (us, europe, uk, china, japan, india, middle-east, latam, canada, africa, australia, world) + headline (max 6 words, one [highlight]) + label (short place/metric line). Use for world news.
- outro: final line only, tk "big", expr "wink", pose "present".
Variety matters: use at least 4 different scene types, change the visual every 1-2 lines, and prefer a chart, stat or map over a plain title whenever there is a number or a place.
expr must match the news: up = green arrow eyes on a real up move, down = red arrow eyes on a real down move, shock only for breaking news.
tag is the show label, e.g. "Morning Brief", "Closing Bell", "FP Flash", "Pocketbook Tuesday".
caption: 3-5 short lines for the post: the news in plain words, why it matters, "Money 101: <term>", "Sources: <names>", "News and education, not financial advice.", then 5 hashtags starting with #FinanceProsTV.
yt_title: max 80 characters, specific, no clickbait. Use only facts from the research brief."""


LONG_GUIDE = """This is a LONG-FORM YouTube video (16:9), 7-10 minutes, 1100-1500 spoken words, 60-100 lines.
Open with a 20-second cold open (the most interesting fact), then a 'chapter' scene before each chapter: chapter (number) and headline (chapter title).
Inside chapters use the same scene types with lots of variety (bars, stats, steps, map, number, vs, term). Dot explains 2-4 terms across the video.
Recap the key takeaways in the final chapter, then the outro line. Keep every sentence plain, specific and sourced from the brief.
yt_title: max 90 characters. caption: a YouTube description: 2-3 sentence summary, chapter list with approximate timestamps
(0:00 Intro, then estimate ~150 words per minute), sources, "News and education, not financial advice.", 5 hashtags."""


def write_script(show, brief, now, topic=None):
    guide = SCRIPT_GUIDE + ("\n\n" + LONG_GUIDE if show in LONGFORM else "")
    q = (f"Date: {now:%A, %B %d, %Y}. Show: {SHOWS[show]}\n" + (f"Topic: {topic}\n" if topic else "") +
         f"\nResearch brief (the ONLY facts you may use):\n{brief}\n\n{guide}")
    return json.loads(call(BRAND, q, fmt=EPISODE, max_tokens=64000 if show in LONGFORM else 16000))


def factcheck(ep, brief, now):
    claims = "\n".join(f"- [{l['who']}] {l['text']}" + (f" | on screen: {json.dumps({k: v for k, v in l['scene'].items() if k in ('headline','value','label','note','def','example','items','left','right','sub')})}" if l["scene"] else "") for l in ep["lines"])
    q = (f"Today is {now:%A, %B %d, %Y}, {now:%I:%M %p} ET. Fact-check this FinancePros TV script before it is published.\n\n"
         f"Script:\n{claims}\n\nCaption:\n{ep['caption']}\n\nResearch brief it was written from:\n{brief}\n\n"
         "Independently verify every factual claim and every number with web search (do not trust the brief). "
         "Also flag: anything stale (not today's news), advice or predictions, political opinion, misleading headlines, "
         "a Dot definition that is wrong or oversimplified to the point of being false, and any on-screen value that differs from the spoken one. "
         "List each issue. Finish with exactly one final line: VERDICT: PASS or VERDICT: FAIL.")
    out = call(BRAND, q, tools=WEB)
    verdict = re.findall(r"VERDICT:\s*(PASS|FAIL)", out)
    return (verdict[-1] == "PASS" if verdict else False), out


LED_OK = set("ABCDEFGHIKLMNOPRSTUVWY0123456789$%.,-+ ")
CURRICULUM = os.path.join(HERE, "curriculum.json"); STATE = os.path.join(HERE, "state.json")


def next_lesson():
    """Next Money School topic in order, skipping ones already done. Returns (topic, lesson number)."""
    cur = json.load(open(CURRICULUM)); st = json.load(open(STATE)) if os.path.exists(STATE) else {"done": [], "number": 3}
    done = set(cur["done"]) | set(st["done"])
    for lv in cur["levels"]:
        for t in lv["lessons"]:
            if t not in done:
                return t, st["number"] + 1, lv["name"]
    return None, None, None


def mark_lesson(topic, number):
    st = json.load(open(STATE)) if os.path.exists(STATE) else {"done": [], "number": 3}
    st["done"].append(topic); st["number"] = number
    json.dump(st, open(STATE, "w"), indent=1)


def sanitize(ep, show, date):
    """Keep the model inside what the renderer can draw."""
    for l in ep["lines"]:
        sc = l["scene"]
        for k in ("value", "term"):
            if sc.get(k):
                v = sc[k].upper()
                if not set(v) <= LED_OK or len(v) > (8 if k == "value" else 10):
                    # the LED font can't draw it: fall back to a plain headline card
                    l["scene"] = {"type": "title", "headline": sc.get("note") or sc.get("def") or sc.get("label") or l["text"][:48],
                                  "expr": sc.get("expr", "neutral"), "tk": "dock"}
                    break
                sc[k] = v
        if sc.get("pose") == "none":
            sc.pop("pose")
        if sc.get("type") == "term":
            sc["dot"] = True
        if sc.get("type") == "chapter":
            sc["nocap"] = False
        if sc.get("type") in ("steps",) and sc.get("reveal") is None:
            sc["reveal"] = len(sc.get("items", []))
        if sc.get("type") == "outro":
            sc["nocap"] = True; sc.setdefault("cta", "Follow for the next bell")
    ep["id"] = f"{date}-{show}"
    return ep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--show", required=True, choices=list(SHOWS))
    ap.add_argument("--date"); ap.add_argument("--topic")
    a = ap.parse_args()
    now = dt.datetime.now(ET)
    date = a.date or now.strftime("%Y-%m-%d")
    logdir = os.path.join(HERE, "episodes", "daily"); os.makedirs(logdir, exist_ok=True)
    topic = number = None
    if a.show == "lesson":
        topic, number, level = next_lesson()
        if not topic: print("Curriculum finished."); sys.exit(3)
    elif a.show == "lf-school":
        topic = a.topic or "Credit scores, completely explained"
    brief = research(a.show, now, topic)
    open(os.path.join(logdir, f"{date}-{a.show}.research.md"), "w").write(brief)
    score = re.findall(r"SCORE:\s*(\d+)", brief)
    if a.show == "flash" and ("NO_FLASH" in brief or not score or int(score[-1]) < 18):
        print("No story qualifies for a Flash."); sys.exit(3)
    ep = sanitize(write_script(a.show, brief, now, topic), a.show, date)
    if a.show in LONGFORM: ep["format"] = "landscape"
    if a.show == "lesson": ep["tag"] = f"Money School · #{number}"
    ok, report = factcheck(ep, brief, now)
    open(os.path.join(logdir, f"{date}-{a.show}.factcheck.md"), "w").write(report)
    if not ok:
        print("Fact-check FAILED; nothing will be posted. See the factcheck report."); sys.exit(4)
    if a.show == "lesson": mark_lesson(topic, number)
    path = os.path.join(logdir, f"{date}-{a.show}.json")
    json.dump(ep, open(path, "w"), indent=1)
    print(path)


if __name__ == "__main__":
    main()
