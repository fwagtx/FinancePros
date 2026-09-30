# FinancePros TV engine

Fully automated, hand-drawn ("doodle") money videos: **5 shorts a day** on TikTok, Instagram Reels, Facebook Reels, YouTube Shorts and Threads,
plus **5 long-form YouTube videos a week**. Everything is free to run except the Claude API (writing and fact-checking) and a Metricool plan with API access.

## The look
White paper, black marker lines that "boil" like hand animation, flat colors, red annotations, real hand-drawn charts.
- **Paper Ticker**: Ticker, a stick figure with an old-TV head, explains news and money basics with a chalkboard, charts and props.
- **Acorn Economics**: a chunky squirrel explains investing with acorns (short, funny sentences).
- **World Money**: countries are googly-eyed characters (US, China, Japan, UK, Germany, Mexico, Canada).

## Weekly plan (US Central time, set in `daily.py`)
Post times come from Metricool's best-time-to-post data for these accounts: TikTok, Instagram, Facebook and YouTube all peak at
10 AM, 12, 2, 4 and 6 PM Central, and YouTube's single best hour is 4 PM on weekdays (weekdays score about twice the weekend).

| Time (CT) | Every day | Format |
|---|---|---|
| 10:00 AM | **Morning Money**: the biggest money story this morning | short |
| 12:00 PM | **Explainer**: evergreen (Acorn Economics Mon/Wed/Fri/Sun, Paper Ticker Tue/Thu/Sat) | short |
| 2:00 PM | **How They Make Money**: the business model behind a company everyone knows | short |
| 4:00 PM | **The Big Story**: the day's most important money story (countries for world news) | short |
| 6:00 PM | **Hot Take**: money myth, scam alert, face-off, "why is X so expensive" | short |

| Time (CT) | Long-form (YouTube, 16:9) |
|---|---|
| Mon 4 PM | **Explained**: a high-value money topic, from zero |
| Tue 4 PM | **How They Make Money**: a company or industry in depth |
| Wed 4 PM | **The Guide**: a step-by-step money how-to |
| Thu 4 PM | **World Money**: a world-economy story with country characters |
| Fri 4 PM | **The Big Story of the Week** |

If no confirmed news qualifies for a news slot, that slot posts an evergreen video instead, so every slot always posts.
`concepts/scripts/auto/<date>.state.json` records every slot, so nothing is made or posted twice.

## Content calendar
Every evergreen slot is planned through September 2029 in `concepts/calendar.json` (readable copy: `concepts/calendar.csv`), built by
`concepts/plan_calendar.py` from the topic banks in `concepts/topics.json` (about 2,500 edited topics) and the yearly money moments in
`concepts/seasonal.json` (tax season, open enrollment, Black Friday, back to school...). News slots (10 AM, 4 PM, Friday long-form)
always cover that day's news. Each video is researched and fact-checked the day it is made, so numbers are current; after a show's
fresh topics run out (spring 2028 for shorts), its oldest topics re-run at least a year after they first aired.
Re-plan after editing the banks: `python concepts/plan_calendar.py`.

## Video hosting
Rendered videos are uploaded to the Cloudflare R2 bucket `financepros-media` (public r2.dev URL; a lifecycle rule deletes files
after 7 days) and Metricool fetches them from there, keeping its own copy once the post is scheduled. It needs its own
environment variables (FinancePros-only names, so a shared environment never mixes brands): `FP_R2_ACCOUNT_ID` (or the shared
`R2_ACCOUNT_ID`), `FP_R2_ACCESS_KEY_ID`, `FP_R2_SECRET_ACCESS_KEY`, `FP_R2_BUCKET` (default `financepros-media`), `FP_R2_PUBLIC_URL`. Without them it falls back to the repo's `media` branch (public raw.githubusercontent.com links),
which only works while the GitHub repo is publicly visible; if neither works, `session.py next` stops before making anything.

## Who runs it
Two scheduled Claude Code sessions (Routines) on the Claude plan, every day at 5:50 AM and 12:40 PM Central; no API keys needed.
Claude researches, writes and fact-checks (with a separate subagent), `session.py` renders and hosts, and the posts are created
through the Metricool connector. Prompts and details: [ROUTINES.md](ROUTINES.md).

## How a video is made
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
7. **Hosting**: the video and cover go to the `media` branch (only the last 7 days are kept, so the repo never balloons; Metricool copies each file when the post is scheduled).
8. **Publishing** (`publish.py`), formatted per platform:
   - Instagram Reel + Facebook Reel: caption with hashtags, custom cover
   - TikTok: short caption + hashtags, cover
   - YouTube Short: title with #Shorts, description, tags
   - Threads: the Instagram caption fitted to 500 characters, one topic tag
   - Long-form: YouTube only, title, description with real chapter timestamps, tags, custom thumbnail

## GitHub Actions version (optional, needs API keys)
The same plan can also run in GitHub Actions (its hourly schedule is off). GitHub → repo **Settings → Secrets and variables → Actions**:

| Name | Type | Value |
|---|---|---|
| `ANTHROPIC_API_KEY` | Secret | your Claude API key |
| `METRICOOL_USER_TOKEN` | Secret | Metricool → Account settings → API |
| `METRICOOL_USER_ID` | Variable (optional) | `5456294` (already the default) |
| `METRICOOL_BLOG_ID` | Variable (optional) | `7091438` (already the default) |
| `METRICOOL_DRAFT` | Variable (optional) | `true` = everything waits in Metricool for your approval |
| `AUTO_START` | Variable (optional) | first date the plan runs (default `2026-10-03`) |

Check the keys: **Actions → FinancePros TV daily shows → Run workflow → show: check** (posts nothing; the log says ALL GOOD or what's missing).
Test one show end to end: pick the show and tick **draft**; the video lands in Metricool as a draft to review.

## Make a video by hand
```bash
cd engine
pip install -r requirements.txt && npm install && npx playwright install chromium && ./setup_models.sh
python concepts/run.py concepts/scripts/rule-of-72.json            # -> concepts/out/<id>/<id>.mp4 + cover
python concepts/run.py concepts/scripts/rule-of-72.json --stills 3,9   # review frames only
```

## Files
- `daily.py`: one scheduled run (plan, catch-up, state file, fallbacks, hosting, chapters, publishing, `--check`, `--plan`)
- `concepts/studio.py`: topic → research → template script → fact-check (Claude API)
- `concepts/topics.json` / `topics_state.json`: the evergreen topic bank and what's been used
- `concepts/layout.py`: scene templates → positioned drawings (9:16 and 16:9), covers and thumbnails
- `concepts/doodle.html`, `doodle.js`: the hand-drawn player (characters, props, charts, captions)
- `concepts/build.py`, `render.js`, `audio2.py`, `run.py`: voice, frames, music, mix
- `publish.py`: per-platform Metricool posts
- `voice.py`: free Kokoro voices (Ticker = am_adam; the squirrel is am_adam pitched up)
- Older blue "LED" engine files (`player/`, `build.py`, `news.py`) are kept for reference; `news.py` also holds the shared Claude call helper.
