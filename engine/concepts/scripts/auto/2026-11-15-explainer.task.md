# 2026-11-15-explainer: explainer (vertical short), posts Sunday November 15, 2026 at 12:00 PM Central

You are making one FinancePros TV video. Quality matters more than speed: take the time each step needs, and do not skip any.
This video is made ahead of time: it posts on Sunday, November 15. Keep it evergreen: no 'today', 'this week', 'yesterday' or 'just announced'; give every number with its date or period (for example 'in 2025' or 'as of August 2026').

## 1. Research
You write for FinancePros TV: hand-drawn doodle explainer videos about money for people aged 18-40.
Look and voice: like a smart friend with a whiteboard. Plain words, short punchy sentences, a little dry humor, zero hype.
Hosts: Ticker, a stick figure with an old TV for a head (calm, curious), and on 'Acorn Economics' episodes a chunky squirrel who
explains money with acorns in short, funny sentences ("Squirrel plants one acorn. Nothing happens.").
Rules that never change:
- Education, never advice: never say buy, sell, hold, "you should invest in", and never predict prices.
- Only confirmed facts: an official source (Fed, BLS, BEA, Treasury, SEC filing, company release, central bank) or two reputable outlets.
- Neutral on politics: explain what a policy does to money; never take sides.
- Every number on screen must match the spoken number. Round when spoken ("about 4 percent"), exact on screen.
- The attention grabber in the first 3 seconds must stop the scroll and earn the click, and the video must pay it off. No clickbait.
- No emojis in scripts.

Today is Wednesday, September 30, 2026. Show: Explainer (posts noon Central). One evergreen money idea explained so well people save it and share it.
Topic: How crypto is taxed: every trade can be a taxable event

Research this topic. If there is a timely news angle this week, use it as the hook. Use web search to confirm every number, rule, limit and definition that can change, and give the source for each. Find at least one REAL data series that can be charted (with the actual values and the source), one worked example with exact math (show the calculation), and the one fact that surprises people. Finish with 'SOURCES:' and the list.

Use web search. Save the brief (facts, numbers with dates, a chartable data series, SOURCES) to:
  /home/user/FinancePros/engine/concepts/scripts/auto/2026-11-15-explainer.research.md


## 2. Script
Date: Wednesday, September 30, 2026. Show: Explainer (posts noon Central). One evergreen money idea explained so well people save it and share it.
Topic: How crypto is taxed: every trade can be a taxable event
Series 'ticker': who 'ticker' on every line. 
Research brief (the ONLY facts you may use):
(the brief you saved in step 1)

Draw every line with ONE template in scene.t (the renderer lays it out; you never give coordinates):
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
templates in a short and many more in a long-form. Prefer a real chart, stat, compare, or countries whenever there is a number or a place.

THE FIRST 3 SECONDS DECIDE EVERYTHING. The first line is the attention grabber, and it must stop the scroll:
- Spoken in under 3 seconds (at most 12 words), and it lands on screen at the same moment with one big, bold visual (hook template,
  a huge red number or a dramatic prop). No greeting, no "hey guys", no channel name, no "in this video", no slow setup.
- Use one proven pattern: a shocking true number ("You pay $1,000 a year for this and never see it."), a myth called out
  ("Checking your credit score doesn't hurt it."), a direct challenge ("Your savings account is losing you money."), a "why"
  question the viewer can't answer ("Why is a movie ticket $15 but popcorn is $9?"), or a stakes line ("This one number decides
  your car loan.").
- It must be true, specific and paid off by the video (no clickbait), and it should create a question that only watching answers.
- Line 2 raises the stakes or promises the answer within the next 3 seconds, so the viewer stays past second 6.
- The cover/thumbnail and the post's first caption line echo the same hook.

Write a vertical short (TikTok, Reels, YouTube Shorts): 35-55 seconds, 100-150 spoken words, 7-11 lines.
Structure: attention-grabber hook (see the hook rules) -> the key number -> why it matters to your money -> one simple takeaway -> final line
"That's the money. Follow for more." with t = cta. (Acorn Economics ends with "Squirrel explained <topic>. Squirrel would like one follow.")
header: the on-screen title at the top of the video, 2 short lines separated by \n (<= 22 chars per line), handwritten style, no brackets.
cover: the 9:16 cover: title (<=6 words, Title Case, can be a question), a prop, and a big red value or label; or countries (1-2) for world stories.
post.title: <= 60 chars, specific, curiosity without clickbait.
post.ig: Instagram/Facebook caption: 1 hook line, 2-4 short lines of the key facts with numbers, a sources line, "News and education, not financial advice.",
"Follow @financeprostv for money explained simply.", then 5 hashtags (lowercase) ending with #financeprostv.
post.tiktok: <= 150 chars incl. 4-5 hashtags (#moneytok, #personalfinance, topic tags, #financeprostv) and "Not financial advice."
post.yt_desc: 2-4 sentence YouTube Shorts description with the facts and sources, "News and education, not financial advice.", then "#Shorts" + 2 hashtags.
post.tags: 5 YouTube tags.
Each line: who, text (the caption, numerals allowed), say (the same sentence written for the voice: numbers, symbols and acronyms in words, like 'twenty-four percent' and 'A P R'), scene.

Narration must sound like one smart friend talking, not a list being read:
- Read every `say` line in order as if out loud. Each one is a complete, natural spoken sentence (contractions, varied length),
  and each line leads into the next one; no fragments, no stacked labels, no repeated openers.
- Write numbers, symbols and acronyms in `say` the way a person says them ("about twenty-two percent", "A P R", "four hundred
  thousand dollars"); keep exact figures on screen in `text`/scene values. Spoken and on-screen numbers must agree.
- No abbreviations the voice would stumble on (write "versus", "for example", "U S" becomes "US").
Write ONE JSON object that matches the JSON schema in /home/user/FinancePros/engine/concepts/scripts/auto/2026-11-15-explainer.schema.json
and save it to:  /home/user/FinancePros/engine/concepts/scripts/auto/2026-11-15-explainer.raw.json

## 3. Fact-check (independent)
Launch a subagent (Agent tool) that has not seen your work. Give it the script's lines, on-screen values, cover and post text, and
this instruction: "Independently verify every factual claim, number and chart data point with web search (do not trust the brief).
Also flag: a weak opening (the first line must be a true, specific attention grabber spoken in under 3 seconds that makes a
viewer need the answer; say how to make it stronger if it is not), stale news, time words that will be wrong on the posting date (November 15, 2026), advice or price predictions, political
opinion, a cover or title the video doesn't pay off, math errors in worked examples, any on-screen value that differs from the
spoken one, and narration that reads awkwardly out loud. List each issue. Finish with exactly one line: VERDICT: PASS or VERDICT: FAIL."
Fix every issue it lists and check again (at most 2 rounds). Save its last report to
  /home/user/FinancePros/engine/concepts/scripts/auto/2026-11-15-explainer.factcheck.md
If it still fails: python engine/session.py record 2026-11-15-explainer failed --note "fact-check"   and go to the next slot.

## 4. Build and quality check
  python engine/session.py build 2026-11-15-explainer /home/user/FinancePros/engine/concepts/scripts/auto/2026-11-15-explainer.raw.json
It renders the video and cover, uploads them, and prints a QUALITY report (length, preview frames, cover) and the Metricool posts.
Before scheduling:
- Length must be 0:30 to 1:02. If it is outside, edit the script (add or trim real content, never filler)
  and run build again.
- Hook check: open the first preview frame and the cover. The opening line and visual must grab attention in the first 3 seconds
  (big bold text or number, no slow intro). If it would not stop you scrolling, sharpen line 1 and rebuild.
- Open every preview frame and the cover image it lists with the Read tool. Everything must be readable, nothing overlapping or cut
  off, the right scene for the words. Fix the script and rebuild if not (at most 2 rebuilds; if it still fails, record failed).

## 5. Schedule
Create each printed post with the Metricool createScheduledPost tool (blogId 7091438): pass "date" and "info" exactly as printed
(info as a JSON string). Then:
  python engine/session.py record 2026-11-15-explainer scheduled --ids <uuid of each created post>
If a post marked optional (Threads) fails, still record scheduled and mention it in --note.
