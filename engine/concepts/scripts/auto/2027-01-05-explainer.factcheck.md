# Fact-check: 2027-01-05 explainer (25x retirement rule)
Checked Nov 6, 2026 for a Tue Jan 5, 2027 noon CT post. Spoken words: 139 as written; 139 after fixes below. Hook (line 0): 11 spoken words, true, OK.

## Verified OK
- Line 1: 1 / 0.04 = 25. Correct.
- Line 2: Bengen, "Determining Withdrawal Rates Using Historical Data," Journal of Financial Planning, Oct 1994; 30-year rolling retirements, US data from 1926, stock/bond mix; worst case (1968 start) about 4.15%, rounded to 4%. "4% survived them all" is a fair plain-English summary (no tested 30-year period ran out at 4%). Sources: Bankrate (bankrate.com/retirement/revised-4-percent-rule/), Retirement Researcher, Wikipedia "4% rule".
- Line 3: Trinity study, Cooley/Hubbard/Walz, AAII Journal, Feb 1998, data 1926-1995; 4% inflation-adjusted over 30 years succeeded in ~95-100% of periods for balanced/stock-heavy mixes. "Backed it up" is accurate. Source: Retirement Researcher, Wikipedia "Trinity study".
- Line 4 and chart: Morningstar's own series page states "In 2021 ... 3.3%", "In 2022 ... 3.8%", "In 2023 ... 4.0%", "In 2024 ... 3.7%", and the Dec 2025 report's base case is 3.9%. Publication-year labels (2021-2025, evenly spaced) match Morningstar's own wording, so they are defensible. Note: the 2021 and 2023 reports came out in November (ThinkAdvisor Nov 13, 2023), not December; the chart uses years only, so no change needed. Source: morningstar.com/retirement/morningstars-retirement-income-research-finding-your-safe-withdrawal-rate; ThinkAdvisor Dec 3, 2025.
- POST.ig: Bengen 4.7% in "A Richer Retirement" (Wiley, Aug 2025), a worst-case figure. Correct. Source: Advisor Perspectives Aug 29, 2025; Money.com.
- Line 7 caveats (taxes, fees, bad early years): accurate (Trinity excluded taxes/fees; sequence risk, 1966/1968 starts). Not advice.
- Field limits: all within limits (title 58 chars, tiktok 138 chars, stat label 18, list items <=13, board lines <=16, timeline when/what OK).

## Issues

### 1. Line 5 (stale Social Security figure) - MUST FIX
Problem: "$2,071 a month in January 2026" will be a year old on Jan 5, 2027. SSA announced the 2027 COLA (3.6%) on Oct 14, 2026; its fact sheet estimates the average retired-worker benefit rises from $2,095 to about $2,170 for January 2027 ($2,095 x 1.036 = $2,170). (Note: NAPA reported ~$2,163 and NBC Boston $2,107; $2,170 matches the arithmetic and most outlets. ssa.gov was not reachable from this session; confirm at ssa.gov/cola before render.)
Replacement:
- TEXT: Social Security helps: the average retirement check is projected at about $2,170 a month in January 2027.
- SAY: Social Security helps: the average retirement check is projected at about two thousand one hundred seventy dollars a month in January twenty twenty-seven.
- SCENE: {"t": "stat", "label": "Avg. retiree check", "value": "$2,170", "tone": "up", "sub": "SSA est., Jan 2027", "mood": "happy"}
Sources: Newsweek "Social Security COLA revealed: what 3.6% increase means for retirees"; NewsNation "Social Security COLA 2027"; PSCA/NAPA Oct 2026 "2027 Social Security COLA marks biggest increase in 5 years".

### 2. Line 6 (worked example must follow the new SS number) - MUST FIX
Problem: with $2,170 x 12 = $26,040/yr (about $26,000), the gap is $40,000 - $26,000 = $14,000; $14,000 x 25 = $350,000 (exact: $13,960 x 25 = $349,000). Also drops "first" to keep total at 139 words.
Replacement:
- TEXT: Our math: $40,000 a year times 25 is $1 million. Subtract about $26,000 of Social Security, and it's $350,000.
- SAY: Our math: forty thousand a year times twenty-five is one million. Subtract about twenty-six thousand of Social Security, and it's three hundred fifty thousand.
- SCENE: {"t": "compare", "title": "Our math: $40K/yr", "left": {"label": "No SS", "value": "$1M", "tone": "neutral", "sub": "$40K x 25"}, "right": {"label": "With SS", "value": "$350K", "tone": "up", "sub": "$14K x 25"}, "mood": "shock"}

### 3. POST.ig and POST.yt_desc (same stale figure/math) - MUST FIX
- ig, replace the line "Our math: $40,000/yr x 25 = $1,000,000. Subtract ~$25,000 of Social Security (avg $2,071/mo, Jan 2026) and it's $375,000." with: "Our math: $40,000/yr x 25 = $1,000,000. Subtract ~$26,000 of Social Security (avg ~$2,170/mo, SSA est. for Jan 2027) and it's $350,000."
- yt_desc, replace "Social Security (avg $2,071/month, Jan 2026) shrinks the target: in our math, $40,000/yr drops from $1,000,000 to $375,000." with: "Social Security (avg ~$2,170/month, SSA est. for Jan 2027) shrinks the target: in our math, $40,000/yr drops from $1,000,000 to $350,000."

### 4. Line 4 / chart (pre-post recheck, not a fix today)
Problem: Morningstar typically publishes its next estimate in late Nov/Dec. No 2026 report found as of Nov 6, 2026. If a December 2026 figure is out before Jan 5, 2027, "3.9% in December 2025" will read stale. Action: recheck in mid-December; if a new value X exists, use TEXT "Morningstar's forward-looking estimate runs lower: X% in [Month] 2026." / SAY to match, add point [2026, X] to the chart and set "end" to "X%" (drop 2021 to keep five points if needed), and update ig/yt_desc. If no new report, keep as is.

### 5. Line 2 (optional precision, no change required)
"found 4% survived them all" is acceptable. Optional tighter wording, same word count is not possible without lengthening; leave as is.

VERDICT: FAIL
