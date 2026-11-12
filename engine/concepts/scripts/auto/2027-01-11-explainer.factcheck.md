# Fact-check: 2027-01-11 explainer (true hourly cost of a purchase)

Checked 2026-11-12 for posting Mon Jan 11 2027. bls.gov, census.gov and fred.stlouisfed.org were blocked for direct fetch. BLS figures were pulled from the BLS Public Data API (api.bls.gov, via Firecrawl's bls-gov provider). Census and book facts were checked by web search.

## Sources verified
- BLS CES0500000003 (SA), October 2026 = **38.00** (footnote "P: preliminary"). September 2026 was revised to 37.86. The research brief's 37.81 is not used in the script. Press summaries match: "rose 14 cents to $38.00 in October, up 3.1% y/y".
- BLS CEU0500000003 (NSA), annual averages (M13) for 2016-2025: 25.64, 26.32, 27.11, 27.99, 29.35, 30.60, 32.26, 33.72, 35.06, 36.45. **All 10 chart points match exactly.**
- Census QuickFacts LFE305224: mean travel time to work, workers 16+, 2020-2024 ACS 5-year = **26.4 min**. Confirmed.
- *Your Money or Your Life*, Vicki Robin & Joe Dominguez, 1992. The book's "real hourly wage" takes pay, subtracts job costs and adds job-related hours such as commuting. Confirmed (Get Rich Slowly, WRAL, book summaries).
- Our math (recomputed): 1200/38 = 31.58 h. 38 x 0.75 = 28.50, and 1200/28.50 = 42.11 h. A commute of 2 x 26.4 = 52.8 min = 0.88 h, so the day is 8.88 h, 228/8.88 = $25.676 (shown as $25.68), and 1200/25.676 = 46.74 h (46.7, about 47). 46.7 is more than 40 hours, so "more than a work week" holds. All correct.

## Per line
- **0 hook: FIX.** "can cost an average worker 47 hours" sounds like a measured fact. In fact the 47 rests on an illustrative 25% tax, an 8-hour day and the commute. The phrase "average worker" also overstates what the mean wage tells us.
  - TEXT: `By our math, a $1,200 phone costs about 47 work hours.`
  - SAY: `By our math, a twelve-hundred-dollar phone costs about forty-seven work hours.` (11 words)
  - The scene is OK.
- **1: OK.** $38.00 is clearly dated October 2026. This matters because the Dec 2026 report (Jan 8 2027) will be out by posting day. Do not say "now" or "latest".
- **2: OK.** The chart and endpoints are verified. The spoken "about twenty-six / thirty-six" is fine rounding.
- **3: OK.** 31.6 h is correct.
- **4: FIX.** The 25% must read as illustrative, not as a claim about anyone's tax rate.
  - TEXT: `Say an illustrative 25% goes to taxes, so you keep $28.50. Now it's 42.1 hours.`
  - SAY: `Say an illustrative quarter goes to taxes, so you keep twenty-eight fifty. Now it's about forty-two hours.`
  - The board is OK.
- **5: OK.** 26.4 min each way, Census ACS 2020-24.
- **6: FIX.** The $25.68 depends on an 8-hour day, and the script never stated that assumption.
  - TEXT: `Over an 8-hour day, that unpaid time drops the real wage to $25.68.`
  - SAY: `Over an eight-hour day, that unpaid time drops the real wage to about twenty-five seventy.`
- **7: OK.** The attribution and year are correct.
- **8: OK.** 46.7 h, more than a 40-h week. "A tool, not a rule" gives no buy/don't-buy advice.
- **9 CTA: OK.**
- **Header and cover: OK.** "Price in Hours?" and "47 hrs" are paid off.
- **post.title: FIX.** New title: `By our math, a $1,200 phone costs about 47 hours of work`
- **post.ig: FIX.**
  - First line becomes `By our math, a $1,200 phone costs about 47 hours of work at average pay.`
  - The commute line adds "to an 8-hour day".
- **post.yt_desc: FIX.** Add "(not anyone's real rate), an 8-hour day" to the assumptions.
- **post.tiktok: OK.** It already says "our math".

Applied to 2027-01-11-explainer.raw.json. check.py: `OK: 10 lines, 139 spoken words (~46s at 180 wpm)`; hook 11 words.

VERDICT: FIX

## Round 2 (editor)
- Checker applied all fixes; check.py OK.
VERDICT: PASS
