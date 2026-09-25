# FinancePros TV video engine

Turns a script into a finished 1080×1920 video hosted by Ticker, and (in the daily workflow) turns the day's news into scripts.

## What's free and what isn't
| Part | Tool | Cost |
|---|---|---|
| Voices (Ticker, Dot) | Kokoro, Apache 2.0, runs on the CPU | Free |
| Animation, captions, lip-sync | Headless Chromium drawing `player/` frame by frame | Free |
| Music bed and sound effects | Generated from scratch in `audio.py` (no licensing) | Free |
| Mixing and encoding | ffmpeg, loudness −14 LUFS | Free |
| Running on a schedule | GitHub Actions (public repo) | Free |
| Hosting the video files | This public repo (raw GitHub URLs) | Free |
| Posting to IG, FB, TikTok, YouTube | Metricool REST API | Needs a Metricool plan with API access |
| Researching, writing and fact-checking the news | Claude API (`claude-opus-5`) with web search | Pay-per-use |

## Make a video by hand
```bash
cd engine
pip install -r requirements.txt && npm install && npx playwright install chromium && ./setup_models.sh
python build.py episodes/01-compound-interest.json            # -> out/<id>/<id>.mp4
python build.py episodes/01-compound-interest.json --stills 0,5,12   # review frames only
```

## Turn on the daily automation
Add these in GitHub → repo **Settings → Secrets and variables → Actions**:

| Name | Type | Value |
|---|---|---|
| `ANTHROPIC_API_KEY` | Secret | Your Claude API key |
| `METRICOOL_USER_TOKEN` | Secret | Metricool → Account settings → API → REST API access token |
| `METRICOOL_USER_ID` | Variable | `5456294` |
| `METRICOOL_BLOG_ID` | Variable | `7091438` (the financeprostv brand) |
| `METRICOOL_DRAFT` | Variable (optional) | `true` to save posts as drafts you approve in Metricool |

Then **Actions → FinancePros TV daily shows → Run workflow** once to test a show.

Schedule (Eastern time, weekdays): Morning Brief builds 7:00 and posts 7:30, Midday Pulse 12:00 → 12:30,
Closing Bell 4:05 → 4:30 PM, and an FP Flash check every hour from 9 AM to 5 PM.

## Quality gates (nothing posts unless all pass)
1. **Importance rules**: the research step scores stories; a Flash needs Tier 1 or a score of 18+/25.
2. **Only facts from the research brief** go into the script, with sources.
3. **Independent fact-check**: a separate Claude pass re-verifies every claim and number on the web and must end in `VERDICT: PASS`.
4. **Renderer guardrails**: anything the LED font can't draw falls back to a headline card; outro and disclaimer are always added.
5. **Audio**: every video is normalized to −14 LUFS with true peak below −1.5 dB.

Research and fact-check reports are saved with every run (`episodes/daily/*.md`) and uploaded as workflow artifacts.

## Files
- `voice.py`: script → narration (`voice.wav`) and timeline (line and word timings, lip-sync envelope)
- `audio.py`: original music bed and sound effects
- `player/`: the scene player (Ticker, Dot, LED text, charts, captions, transitions)
- `render.js`: renders frames with Chromium and pipes them into ffmpeg
- `build.py`: voice → audio → frames → final mix
- `news.py`: research → script → fact-check (Claude API)
- `daily.py`: one scheduled run, from news to scheduled post
- `publish.py`: schedules a video on all four networks through Metricool
- `episodes/`: hand-written evergreen episodes; `episodes/daily/` holds generated ones
