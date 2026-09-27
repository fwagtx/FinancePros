# FinancePros TV engine

Fully automated, hand-drawn ("doodle") money videos: **4 shorts a day** on TikTok, Instagram Reels, Facebook Reels and YouTube Shorts,
plus **3 long-form YouTube videos a week**. Everything is free to run except the Claude API (writing and fact-checking) and a Metricool plan with API access.

## The look
White paper, black marker lines that "boil" like hand animation, flat colors, red annotations, real hand-drawn charts.
- **Paper Ticker**: Ticker, a stick figure with an old-TV head, explains news and money basics with a chalkboard, charts and props.
- **Acorn Economics**: a chunky squirrel explains investing with acorns (short, funny sentences).
- **World Money**: countries are googly-eyed characters (US, China, Japan, UK, Germany, Mexico, Canada).

## Weekly plan (Eastern time, set in `daily.py`)
| Slot | Every day | Format |
|---|---|---|
| 7:30 AM | **Morning Money**: the biggest money story this morning | short |
| 12:00 PM | **Explainer**: evergreen (Acorn Economics Mon/Wed/Fri/Sun, Paper Ticker Tue/Thu/Sat) | short |
| 4:30 PM | **The Big Story**: the day's most important money story (countries for world news) | short |
| 7:30 PM | **Hot Take**: money myth, scam alert, face-off, "why is X so expensive" | short |
| Mon 5 PM | **The Big Story, long-form**: the week's biggest story in depth | YouTube 16:9 |
| Wed 5 PM | **Explained**: a high-value evergreen topic, from zero | YouTube 16:9 |
| Sat 11 AM | **World Money**: a world-economy deep dive | YouTube 16:9 |

If no confirmed news qualifies for a news slot, that slot posts an evergreen video instead, so there are always 4 shorts a day.

## How a video is made (one GitHub Actions run)
1. **Topic**: news shows research today's stories and score them (reach, surprise, high-value category, visual, confirmed). Evergreen shows take
   the next topic from `concepts/topics.json` (weighted to investing, credit, taxes, housing, retirement, insurance); when a list runs low,
   Claude researches what people are searching for and adds 20 new topics.
2. **Research** with web search, then a **script** written as scene *templates* (hook, board, chart, compare, list, stat, money, countries,
   building, news, quote, timeline, split, squirrel, chapter, cta) in a strict JSON schema.
3. **Fact-check**: a separate Claude pass re-verifies every number and chart point on the web and must end in `VERDICT: PASS`.
4. **Layout** (`concepts/layout.py`) turns templates into drawings placed inside each platform's safe zone.
5. **Voice** (Kokoro, free), **music and sound effects** (generated, no licensing), **render** (Chromium frame by frame; long-form at 15 fps for the
   hand-drawn feel), loudness to -14 LUFS.
6. **Cover / thumbnail**: a 9:16 cover whose title sits in the square Instagram shows on the grid, or a 1280x720 YouTube thumbnail.
7. **Hosting**: the video and cover go to the `media` branch (only the last 21 days are kept, so the repo never balloons; Metricool copies each file).
8. **Publishing** (`publish.py`), formatted per platform:
   - Instagram Reel + Facebook Reel: caption with hashtags, custom cover
   - TikTok: short caption + hashtags, cover
   - YouTube Short: title with #Shorts, description, tags
   - Long-form: YouTube only, title, description with real chapter timestamps, tags, custom thumbnail

## Turn it on
GitHub → repo **Settings → Secrets and variables → Actions**:

| Name | Type | Value |
|---|---|---|
| `ANTHROPIC_API_KEY` | Secret | your Claude API key |
| `METRICOOL_USER_TOKEN` | Secret | Metricool → Account settings → API |
| `METRICOOL_USER_ID` | Variable | `5456294` |
| `METRICOOL_BLOG_ID` | Variable | `7091438` |
| `METRICOOL_DRAFT` | Variable (optional) | `true` = everything waits in Metricool for your approval |
| `AUTO_START` | Variable (optional) | first date the plan runs (default `2026-10-03`) |

Test any show by hand: **Actions → FinancePros TV daily shows → Run workflow** and pick the show.

## Make a video by hand
```bash
cd engine
pip install -r requirements.txt && npm install && npx playwright install chromium && ./setup_models.sh
python concepts/run.py concepts/scripts/rule-of-72.json            # -> concepts/out/<id>/<id>.mp4 + cover
python concepts/run.py concepts/scripts/rule-of-72.json --stills 3,9   # review frames only
```

## Files
- `daily.py`: one scheduled run (plan, fallbacks, hosting, chapters, publishing)
- `concepts/studio.py`: topic → research → template script → fact-check (Claude API)
- `concepts/topics.json` / `topics_state.json`: the evergreen topic bank and what's been used
- `concepts/layout.py`: scene templates → positioned drawings (9:16 and 16:9), covers and thumbnails
- `concepts/doodle.html`, `doodle.js`: the hand-drawn player (characters, props, charts, captions)
- `concepts/build.py`, `render.js`, `audio2.py`, `run.py`: voice, frames, music, mix
- `publish.py`: per-platform Metricool posts
- `voice.py`: free Kokoro voices (Ticker = am_adam; the squirrel is am_adam pitched up)
- Older blue "LED" engine files (`player/`, `build.py`, `news.py`) are kept for reference; `news.py` also holds the shared Claude call helper.
