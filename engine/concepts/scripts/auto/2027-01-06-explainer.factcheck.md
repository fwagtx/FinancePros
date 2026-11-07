# Fact-check: 2027-01-06 explainer (Acorn Economics: why markets rise)
Checked Nov 7, 2026 for a Wed Jan 6, 2027 noon CT post. Spoken words: 131 as written; 133 after fixes below. Hook (line 0): 12 spoken words, true (nominal), at the limit.

## Verified OK
- Lines 0, 1 chart, COVER, POST: NYU Stern, Damodaran, histretSP ("Date: January 2026", "Updated: January 5, 2026"), column "Value of $100 invested at start of 1928 in S&P 500 (includes dividends)": 1975 $4,142.10; 1985 $15,516.60; 1995 $61,838.19; 2005 $146,077.85; 2015 $294,115.79; 2025 $1,157,598.95. All six chart points match after rounding; "$1.16M" correct. Convention is start of 1928 to end of 2025 (98 years); "$100 in 1928" is fair, ig correctly says "at the start of 1928". Source: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html
- Line 4 stat: (1,157,598.95 / 100)^(1/98) - 1 = 10.018% -> "10.02%" / "about 10%" correct (our math from the Damodaran series; Fool/Shiller gives 9.92%, consistent with "about 10%").
- Line 5: counted from Damodaran yearly S&P 500 total returns 1928-2025: 98 years, 72 positive, 26 negative (no zero years). Motley Fool (Shiller data, updated Sep 2026): "positive returns in 72 out of 98 years from 1928 through 2025". Correct.
- Line 6: S&P 500 closed Dec 31, 1999 at 1,469.25 (Yahoo Finance ^GSPC history; Macrotrends; SEC sp500 table) and Dec 31, 2012 at 1,426.19 (Wikipedia "Closing milestones of the S&P 500"; Macrotrends). 2012 close below 1999 close: correct. Text correctly says "index price" (with dividends the total return end-1999 to end-2012 was +23%, from Damodaran $156,658 -> $193,388, so price-only wording is required and is present).
- Line 7: 1,000 x 1.07^30 = 7,612.26 -> "$7,612" correct; labeled "Our math", hypothetical, not a forecast.
- Lines 2-3 drivers (earnings growth, dividends, economic growth, inflation): standard decomposition (Bogle: dividend yield + earnings growth + change in P/E; nominal earnings grow with real GDP and inflation). Accurate.
- "through 2025" on Jan 6, 2027: dated, so still correct. Damodaran's 2026 update typically lands in the first week of January (2025 data was posted Jan 5, 2026), so it may be out by post day; the claim stays true as dated. Optional: if posted before render, nothing must change.
- Advice/predictions: none. Line 8 has "Past results aren't a promise"; captions carry "not financial advice". Good.
- Field limits: post.title 60 chars (OK, at limit); tiktok 143; stat label "Yearly, compounded" 18, sub "S&P 500, 1928-2025" 18; compare values 2 chars; list items <=13. Text and say match on all lines.

## Issues

### 1. Line 1 (missing "before inflation"; hook reads as real wealth) - MUST FIX
Problem: $1.16M is nominal. Prices rose roughly 19x over 1928-2025 (Motley Fool/Shiller: nominal CAGR 9.92% vs real 6.64%), so in 1928 dollars the result is roughly $60K. The video even lists inflation as a driver, so without the caveat the hook overstates the payoff. Add it right after the hook. (+2 spoken words; total 133.)
Replacement:
- TEXT: That's the S&P 500 with dividends, before inflation, through 2025. Here's why.
- SAY: That's the S and P five hundred with dividends, before inflation, through twenty twenty-five. Here's why.
- SCENE: {"t": "chart", "title": "$100 from 1928, S&P 500", "points": [[1975, 4142], [1985, 15517], [1995, 61838], [2005, 146078], [2015, 294116], [2025, 1157599]], "prefix": "$", "end": "$1.16M", "color": "up", "mood": "think"} (unchanged)
Source: https://www.fool.com/research/sp-500-annual-returns/ ("The index's real, inflation-adjusted CAGR over the same time period was 6.64%").

### 2. POST.ig, POST.yt_desc, POST.tiktok (same caveat) - MUST FIX
- ig: replace "grew to about $1.16 million by the end of 2025, with dividends reinvested." with "grew to about $1.16 million by the end of 2025, with dividends reinvested, before inflation."
- yt_desc: replace "grew to about $1.16 million by the end of 2025, about 10% a year compounded" with "grew to about $1.16 million by the end of 2025 before inflation, about 10% a year compounded"
- tiktok (150 chars, drops #moneytok to fit): "$100 in 1928 became $1.16M by 2025 before inflation. Why markets rise, with acorns. Not financial advice. #personalfinance #stockmarket #financeprostv"

### 3. Line 6 (optional, readability) - OPTIONAL
"closed 2012 below its 1999 close" is a little clunky aloud. Optional same-length alternative:
- TEXT: Some stretches go nowhere: the index price ended 2012 below where it ended 1999.
- SAY: Some stretches go nowhere: the index price ended twenty twelve below where it ended nineteen ninety-nine.
(+1 word; total 134 if both fixes applied.) Scene unchanged.

### 4. Line 7 (optional, context) - OPTIONAL
7% appears right after "about 10%" with no reason given. It is a fair illustrative rate (close to the 6.64% real CAGR), and it is labeled "our math", so no change required.

VERDICT: FAIL

## Round 2 (editor)
Applied: line 1 "before inflation"; ig/yt_desc/tiktok caveat; line 6 smoother wording.
VERDICT: PASS
