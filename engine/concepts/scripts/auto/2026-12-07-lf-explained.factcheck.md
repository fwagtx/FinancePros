# Fact-check: 2026-12-07-lf-explained (Inflation explained, long-form)

Checked Thu Oct 8 2026 for posting Mon Dec 7 2026. Line numbers are 0-based indexes into `lines`. Spoken word count: 1,787 now, 1,781 after the fixes below. The hook stays at 11 words.

## Verified (no change needed)

- **Aug 2026 CPI (lines 14, 16, 17, 53).** 3.4% y/y (unchanged from July), core 2.4%, gasoline +27.4% y/y. Source: BLS CPI release, Sep 11 2026 (Trading Economics and others report the same figures). "Most of that gap is gasoline" holds up: gasoline weighs about 3%, so +27.4% adds roughly 0.8-0.9 pt.
- **Real hourly earnings -0.3% over the 12 months to Aug 2026 (lines 1, 21).** Confirmed by BLS Real Earnings, Sep 11 2026. Exact math: 1.031/1.034 - 1 = -0.29%.
- **Average hourly earnings +3.1% y/y in Aug 2026, slowest since May 2021 (line 70).** Confirmed by the BLS jobs report of Sep 4. The September figure, 3.0%, has since replaced it. Line 70 gives the date, so it can stay.
- **Fed 2% goal, Jan 2012 (line 18).** Correct.
- **Sep 16 2026 hike of 25 bp to 3.75-4.00%, first hike since 2023 (line 38).** Confirmed: the vote was 12-0 and the last hike was July 2023.
- **Mar 2022 to Jul 2023 hiking cycle, top of range 0.25% to 5.5% over 16 months (line 51).** Correct, with a minor precision note in issue 8.
- **June 2022 (lines 28, 50).** CPI 9.1%, "largest since the period ending Nov 1981", energy +41.6%. All correct.
- **CPI-U annual averages (lines 41, 42, 46, 48, 49, 52).** The 1970-85 series (5.7 ... 13.5 in 1980 ... 3.2 in 1983 ... 3.6) matches BLS annual averages. So does 2015-25 (0.1, 1.3, 2.1, 2.4, 1.8, 1.2, 4.7, 8.0, 4.1, 2.9, 2.6). For 2025, the annual-average index is 321.943, up 2.6%.
- **Purchasing power (lines 4, 5).** The 1970 annual-average CPI is 38.8. 321.943 / 38.8 = 8.30, and 38.8 / 321.943 = $0.12. Correct.
- **Volcker (lines 43, 44, 45).** He became Fed chair in Aug 1979. The fed funds target range was raised to 19-20% on Dec 5 1980, a record, so "about 20% in late 1980" is fine. Unemployment was 10.8% in Nov 1982. Correct.
- **M2 grew about 25% in 2020 (line 25).** Confirmed as the largest one-year growth in records going back to 1980. I could not reach the Atlanta Fed page itself, but secondary sources agree.
- **Oil above $100 in Sep 2026 (line 30).** Brent topped $100 on Sep 9 and settled at $104.61 on Sep 11. WTI closed at $100.05, the first time both closed above $100 in nearly four months. Other outlets confirm this, but reuters.com blocks the search tool, so I could not open the Reuters article. Plausible, low risk.
- **Friedman quote (line 32).** The wording is exact. It is the opening clause of a sentence in *Inflation: Causes and Consequences* (1963), and nothing is changed.
- **I bonds (lines 76, 77, 79).** Treasury's May 1 2026 release gives a 4.26% composite: 0.90% fixed plus 3.34% annualized inflation. Recomputed: 0.009 + 0.0334 + 0.009 x 0.0167 = 4.255%, which Treasury rounds to 4.26%. The rules on line 79 are correct: $10,000 a year, a 1-year lock, and a 3-month interest penalty if redeemed before 5 years.
- **TIPS (lines 80-85).** The 5/10/30-year terms, interest paid every six months on the adjusted principal, and "greater of adjusted or original at maturity" are all correct.
- **Social Security COLA (lines 54, 87).** 8.7% for 2023 and 2.8% for 2026 (announced Oct 24 2025) are correct. So is the Q3 CPI-W method.
- **FDIC national savings rate 0.38%, Aug 2026 (line 59).** Correct. The FRED SNDR series shows 0.38% from April through July, and the Aug 17 figure is 0.38%.
- **Math.** $10,000 x 1.0038 = $10,038. $10,038 / 1.034 = $9,707.93. $10,400 / 1.034 = $10,058.03. That gives -$292.07 and +$58.03. 72/2 = 36, 72/3 = 24, 72/9.1 = 7.91. Real return: 0.38 - 3.4 = -3.02, and the exact figure is -2.92%, so "about -3%" holds. $1,500 / 1.034^10 = $1,073.71. 2% x $10,300 = $206. All correct.
- **Renderer limits.** Every stat, compare, list, split, board and chart value is within its limit.
- **Advice and politics.** No "you should" and no product recommendations. Line 72 has a disclaimer. Politics are neutral.

## Issues and fixes

### 1. Line 0 hook and post text: "Paychecks rose 3.1%" is inaccurate (FACT)
The 3.1% is average *hourly* earnings. Weekly earnings, which are closer to "paychecks", rose faster because the workweek got longer: BLS real *weekly* earnings were **+0.3%** over the year. Saying paychecks lost to prices is therefore wrong. Fix the wording to say hourly pay.
- line 0 `say`: "Hourly pay rose three point one percent. Prices rose three point four." (11 words)
- line 0 `text`: "Hourly pay rose 3.1%. Prices rose 3.4%."
- `post.title`: "Hourly pay rose 3.1%. Prices rose 3.4%. Inflation explained, from the 1970s to I bonds."
- `post.ig`: "Hourly pay rose 3.1%. Prices rose 3.4%. Where inflation comes from and the tools people use against it."
- `post.tiktok`: "Hourly pay up 3.1%, prices up 3.4% (year to Aug 2026). Where inflation comes from and how I bonds and TIPS work."
- `yt_desc` already says "average hourly pay", so it is fine.

### 2. Line 39: wrong by the posting date (STALE)
"The Fed meets again in late October and December". The Oct 27-28 meeting will be over by Dec 7, and the December meeting is Dec 8-9.
- `say`: "The Fed meets about every six weeks, so the current rate may already be different." (15 words, same as now)
- `text`: "The Fed meets about every six weeks, so the current rate may differ."
- The scene is fine as it is.

### 3. Line 88: the 2027 COLA is written as already announced, but gives no number (STALE/RISK)
SSA has scheduled the 2027 COLA announcement for Oct 14 2026, so by December viewers will know it. Projections put it around 3.2-3.6%. The line implies the figure is known but leaves it out, and it would be wrong if the release were delayed (last year's slipped to Oct 24). Use wording that doesn't depend on the date:
- `say`: "Each year's raise is announced in the fall, and it first shows up in January checks." (16 words, -4)
- `text`: "Each year's COLA is announced in the fall and first shows up in January checks."
- `scene.lines`: ["COLA: set each fall", "Paid from January"]
- Alternative, if production updates after Oct 14: "The 2027 COLA, announced in October 2026, is X%, paid from January 2027." Use the official SSA figure.

### 4. Line 73: "the latest CPI" will be stale (STALE)
By December the September and October CPI will be out, so 3.4% will not be the latest figure.
- `say`: "Tool one is the simplest: the rate on your cash. Bank rates vary a lot, and many people compare theirs to inflation, like that zero point three eight versus three point four." (-2 words)
- `text`: "Tool one: the rate on your cash. Bank rates vary a lot; many people compare theirs to inflation, like 0.38% vs. 3.4% in August."

### 5. Lines 67-68: year 10 is 9 years after year 1 (MATH, minor)
Dividing by 1.034^10 is 10 years of inflation, but year 1 to year 10 covers only 9. With 9 years the result would be about $1,110.
- line 67 `say`: "Take a hypothetical fixed mortgage payment of fifteen hundred dollars a month. Ten years later, it's still fifteen hundred." (same word count)
- line 67 `text`: "Take a hypothetical fixed mortgage payment of $1,500. Ten years later, it's still $1,500."
- line 67 `scene.right.label`: "10 yrs later"
- Line 68 can stay as it is ("for those 10 years", $1,074). Optionally change "year-one dollars" to "today's dollars", in both `say` and `text` and on board line 2 ("≈ $1,074 in today's $").

### 6. keep:true after a different template (RENDER)
Lines 27, 31 and 34 have `keep: true`, but the line before each is a board or news scene. Line 80 follows a different list ("I bond rules"), and line 86 follows a split. Remove `"keep": true` from lines 27, 31, 34, 80 and 86 so each list re-enters correctly.

### 7. yt_desc has an empty "CHAPTERS" header (POST)
Fill in the timestamps for chapters 1-6, or remove the header before publishing.

### 8. Line 51: precision (optional, minor)
The top of the range was 0.25% *before* the Mar 16 2022 hike. That hike took it to 0.50%.
- `say`: "...from a quarter percent before March twenty twenty-two to five and a half percent by July twenty twenty-three." (+1 word)
- `text`: "The Fed raised the top of its range from 0.25% before March 2022 to 5.5% by July 2023."
- `left.label`: "Early 2022"

### 9. Line 78: optional freshness update (OK as written)
Line 78 is dated, so it can stay. Since the video posts after Nov 1, consider adding the Nov 2026 I bond composite once Treasury publishes it, to save the viewer a lookup. This is not required.

### 10. Line 30: attribution (low risk)
I could not open the Reuters piece because reuters.com blocks the tool. Other outlets confirm Brent above $100 on Sep 9-14 2026. If the Reuters link can't be confirmed in production, change `scene.source` to "Market data, Sep 2026" and the `say` to "It happened again in twenty twenty-six, when oil climbed back above a hundred dollars a barrel."

## Opening
The opening is strong: two specific, true numbers in under 3 seconds, and the -0.3% payoff comes on line 1. It stays strong after fix 1, which changes only "Paychecks" to "Hourly pay".

## Word count
1,787, minus 2 (fix 4), minus 4 (fix 3), plus 0 (fixes 1, 2 and 5) = **1,781**, within 1,550-1,800. If fix 8 is applied, the total is 1,782.

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-7: hook/posts/cover say "hourly pay"; line 39 meeting wording timeless; line 88 COLA generic; line 73 "compare to inflation ... in August"; lines 67-68 "Ten years later" / "today's dollars"; removed cross-template keep flags; yt_desc empty CHAPTERS removed. Optional: line 51 "early 2022"; line 30 source "Market data, Sep 2026".
VERDICT: PASS
