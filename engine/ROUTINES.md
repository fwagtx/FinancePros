# FinancePros TV routines (Claude Code on the web)

The daily shows are made by two scheduled Routines that wake the "FinancePros production" Claude Code session on claude.ai
(it has the Metricool connector and the FinancePros R2 settings) and run on the account's Claude plan.
They need no API keys: Claude does the research, writing and fact-checking itself and schedules the posts through the
Metricool connector. `engine/session.py` does the rest (plan, topics, rendering, hosting on Cloudflare R2, state).

| Routine | When (US Central) | Makes |
|---|---|---|
| FinancePros morning run | every day 5:50 AM | the 10 AM, 12 PM and 2 PM shorts, plus the weekday 4 PM long-form |
| FinancePros afternoon run | every day 12:40 PM | the 4 PM and 6 PM shorts (fresher news), and retries anything unfinished |
| FinancePros buffer run | every day 8:40 PM | no news; keeps filling the evergreen buffer |

Every run first makes what is due today, then keeps the **evergreen buffer** full: every non-news video for the next 60 days
(about 2 months) is made, quality-checked and scheduled in Metricool ahead of time, so a missed run never leaves a gap.
News slots (10 AM and 4 PM shorts, Friday long-form) are always made on their own day.

Each slot is claimed in `concepts/scripts/auto/<date>.state.json` before it is made, so the two runs never make the same video.
The GitHub Actions workflow (`daily-shows.yml`) is the API-key version of the same plan; its hourly schedule is off.

## Routine prompt

Both routines use this prompt; the morning one says `--until 14:00`, the afternoon one says `--until 23:59`.

```
You are the FinancePros TV production run for the repository fwagtx/FinancePros. This is fully automated: nobody will
answer questions, so never ask; decide and continue.

1. In the repository: git checkout claude/dazzling-newton-1ex2s0 && git pull. Commit and push only to that branch
   (engine/session.py also pushes rendered videos to the media branch; that is expected).
2. python engine/session.py setup
3. Repeat until it prints DONE:
     python engine/session.py next --until <UNTIL>
   It prints the slot and a TASK file. Read the whole task file and follow it step by step: research with web search,
   write the script JSON, have a separate subagent fact-check it, build, then schedule every printed post with the
   Metricool createScheduledPost tool (load it with ToolSearch "metricool"; blogId 7091438) and record the result.
   If a step fails, record the slot as failed with a short --note and move on to the next slot.
4. Finish with python engine/session.py status and a short summary of what was scheduled.
```
