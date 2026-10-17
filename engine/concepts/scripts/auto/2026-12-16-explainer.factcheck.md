# Fact-check: 2026-12-16-explainer (Passive income myths with acorns)

Checked on: Saturday, October 17, 2026. Posts: Wednesday, December 16, 2026.
Source checked: 2026-12-16-explainer.raw.json only (no research brief or generator read).
Direct fetches of multpl.com, fdic.gov and ycharts.com failed (DNS), so figures were checked through search-result excerpts of those sites plus FRED, U.S. News, Forbes, NerdWallet and Experian.

## Math (recomputed in python)
- $12,000 / 4% = $300,000. Correct.
- $12,000 / 1.15% = $1,043,478, so "$1.04M" is correct.
- $12,000 / 0.38% = $3,157,895, so "$3.16M" is correct.
- For reference: at 0.37% (Sept 2026 FDIC) it is $3,243,243. At any rate under 0.40% it is over $3,000,000.
- On-screen values match the spoken ones on every line.
- Compare values "$300K" (5 characters) and "$3.16M" (6) are within the 7-character limit.
- There are no keep:true lines, so the keep/template rule doesn't apply.

## Claims verified
- **Line 3 and chart: S&P 500 dividend yield.** multpl's by-year table, which lists year-end values, gives Dec 31 2024 = 1.24%, 2023 = 1.50%, 2022 = 1.71%, matching the chart. A second site, us500.com, has the same three values. Dec 31 2025 = 1.15% is confirmed by YCharts (S&P data). The 2016-2021 points match multpl's series. YCharts shows slightly different numbers (2021 1.27%, 2020 1.55%) because it calculates the yield another way, but the script cites multpl, so the chart is consistent with its source. The chart is OK.
- **Line 6: rentals are passive even if you work on them.** IRS Topic 425 says rental activities are generally passive even if you materially participate. The exception is a qualifying real estate professional who materially participates. As written ("calls them passive even if you work on them"), the line is slightly too absolute (minor, fix below).
- **Line 7: 15.3% self-employment tax.** Correct per IRS Topic 554: 12.4% Social Security plus 2.9% Medicare. It applies to 92.35% of net earnings, and the Social Security part stops at the wage base, so "on most profit" is a fair simplification.
- **Line 5: FDIC national average savings rate of 0.38% in July 2026.** Plausible: several sources give 0.38% for May through August 2026. But it is stale (Issue 1).

## Issues

### 1. Stale data on the posting date: FDIC savings rate (line 5, compare scene, post ig and yt_desc). Must fix.
FRED, U.S. News, Forbes, NerdWallet and Experian already report the FDIC national savings rate as **0.37% for September 2026**. The FDIC updates the rate monthly, and the October and November figures will be out before December 16. "July 2026, 0.38%, $3.16 million" would be presented as current when it is about five months old and no longer the latest rate. The robust fix is wording that stays true at any rate under 0.40%:
- line 5 text: `In savings at the FDIC's national average, under 0.4%, it's over $3 million.`
- line 5 say: `In a savings account at the FDIC's national average, under point four percent, it's over three million.`
- compare.right: label `Savings <0.4%`, value `$3M+` (4 characters), sub `FDIC national avg`
- post.ig sentence: `At the FDIC national average savings rate (under 0.4%), it's over $3 million.`
- post.yt_desc clause: `at the FDIC national average savings rate (under 0.4%), over $3 million.`

Alternative: just before posting, update to the newest FDIC month (for example Sept 2026 = 0.37%, which gives $3.24M) in text, say, scene and post together.

### 2. Line 6 is slightly overstated (minor accuracy).
Real estate professionals who materially participate are an exception. Fix:
- text and say: `Rentals? The IRS usually calls them passive even if you work on them. It's a tax label, not a day off.`
- board line 1: `Rentals = passive` becomes `Rentals = usually passive`. Or keep the board and change line 3 to `on them (IRS, usually)`.
- post.ig / yt_desc: "The IRS calls rentals passive" becomes "The IRS usually treats rentals as passive".

### 3. Line 3 relies on an aging data point (minor, no change needed).
"Ended 2025 at 1.15%" is a true historical statement on December 16, 2026, and the year label keeps it honest. The live multpl yield is already about 1.06%, so the year-end 2025 figure is conservative rather than misleading. It can stay as is.

### 4. Hook (line 1) works but could be stronger (style, not a failure).
It is true, specific, about 2.5 seconds spoken, and matches the cover. However, the $300K comes from the hypothetical 4% case, and the real payoff is that it can take $1M to $3M or more. A stronger option that keeps the cover question paid off:
- text: `$1,000 a month in passive income? It can take $300,000, or $3 million.`
- say: `A thousand a month in passive income can take three hundred thousand. Or three million.`

## Other checks
- Advice or price predictions: none. The post says "not financial advice", and there are no instruction-style takeaways. "Passive income needs a big acorn pile first" is an observation, not a directive.
- Political opinion, quotes, allegations: none.
- Hypothetical labeling: the 4% case is labeled "Example" and "hypothetical". OK.
- Generalizing one company's numbers to an industry: not applicable.
- Cover and title payoff: the cover asks "$1,000 a Month Needs $300K?" and the video answers it ($300K at 4%, and much more at real yields). OK.
- Read-aloud: the say lines flow naturally. "S and P five hundred's dividend yield ended twenty twenty-five" is a bit of a mouthful but acceptable.
- Time words: "July 2026" is the only time-sensitive date (Issue 1).

VERDICT: FAIL

## Round 2 (editor)
Applied fix 1 (FDIC rate now "under 0.4%" / "over $3 million" on screen, voice, compare and posts) and fix 2 ("usually" passive on line, board and posts). Item 3 kept as dated. Hook unchanged (optional).
VERDICT: PASS
