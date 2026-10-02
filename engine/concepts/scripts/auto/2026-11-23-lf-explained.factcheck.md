# Fact-check: 2026-11-23-lf-explained ("How the stock market actually works")

Checked October 2, 2026, for posting November 23, 2026, 4 PM CT. The script JSON and house rules were read. The research brief was not read.

## Mechanical checks (python)
- 91 lines; 1,767 spoken words. Both are inside the 90-120 line and 1,550-1,800 word limits, and the fixes below keep them at 91 lines and 1,767 words.
- The file validates against `2026-11-23-lf-explained.schema.json`.
- keep:true chains: every keep:true line comes directly after a line with the same scene template (lines 4, 23, 33, 42, 43, 57, 62, 65, 66, 76, 79, 80, 85-87). No chains are broken.
- All compare values are 7 characters or fewer (longest: "$49.98", "$50.02", "9:30-4").
- Math, recomputed:
  - 1,000,000 x $50 = $50M; at $51, $51M (+$1M).
  - Spread: 50.02 - 49.98 = $0.04.
  - 100 x 50.02 = $5,002; 100 x 49.98 = $4,998; round trip $4 = 0.08% of $5,000.
  - $4,000B / $20B = 200.
  - SIFMA: $68.9T / 0.437 = $157.7T world total, which matches SIFMA's $157.8T.
  - Year-over-year from the chart: 2016 +9.5%, 2017 +19.4%, 2018 -6.2%, 2019 +28.9%, 2020 +16.3%, 2021 +26.9%, 2022 -19.4%, 2023 +24.2%, 2024 +23.3%, 2025 +16.4%.
  - All are correct.

## Verified correct
- **Fed SCF stock ownership:** 58.0% in 2022 (a record), up from 52.6% in 2019. 2013 was 48.8%, and 2007 and 2016 match the Fed bulletins.
- **2025 IPOs (Renaissance Capital):** 202 US IPOs raised $44.0B, a four-year high. Medline raised $6.3B, the largest since 2021.
- **SIFMA 2026 Fact Book:** the US was $68.9T, or 43.7% of global equity market cap, and 4.4 times the size of China, the next largest.
- **Market history:**
  - Buttonwood Agreement: May 17, 1792, 24 brokers.
  - Nasdaq: opened February 8, 1971, the first electronic stock market.
  - Nvidia: 10-for-1 split in June 2024.
- **2026 trading calendar:** NYSE is closed November 26, 2026 (Thanksgiving) and closes early at 1 p.m. on November 27.
- **23-hour trading:**
  - The SEC approved Nasdaq's 23x5 plan on April 10, 2026.
  - Nasdaq and NYSE Arca plan an overnight session from 9 p.m. to 4 a.m. ET, starting December 6, 2026 (Jones Day, September 2026).
  - The start still depends on approvals, the SIPs and DTCC readiness, so line 30's caveat is accurate.
- **S&P 500 entry rules:**
  - Minimum market cap of $22.7B, effective July 1, 2025 (up from $20.5B).
  - US domicile and listing required.
  - GAAP earnings must be positive in the latest quarter and over the trailing four quarters combined.
  - The index launched in 1957.
- **Index concentration:**
  - Top 10 at about 40% by mid-2026 (sources give 38-40%).
  - Dot-com peak about 26% (Vanguard/S&P figure; some outlets say 27%).
- **S&P 500 year-end closes:**
  - 2015-2024 match the historical closes: 2,043.94; 2,238.83; 2,673.61; 2,506.85; 3,230.78; 3,756.07; 4,766.18; 3,839.50; 4,769.83; 5,881.63.
  - 2025 closed at 6,845.50, up 16.39% (CNBC), after a sell-off in April.
  - 2022 was down 19.4%.
  - A long-run average of about 10% with dividends is reasonable.
- **SEC:** created by the Securities Exchange Act of 1934. The mission quote is word-for-word: "to protect investors; maintain fair, orderly, and efficient markets; and facilitate capital formation."
- **FINRA:** formed July 30, 2007 from NASD plus NYSE Member Regulation, and overseen by the SEC.
- **Settlement:** T+1 since May 28, 2024; T+2 before that.
- **Circuit breakers:**
  - Levels are 7%, 13% and 20% from the prior close.
  - The 7% and 13% halts last 15 minutes and apply only before 3:25 p.m. ET; a 20% drop closes trading for the day.
  - Level 1 halts fired on March 9, 12, 16 and 18, 2020.
  - Before that, the only market-wide halt was October 27, 1997, under the old rules tied to the Dow.

## Issues and exact fixes

### 1. WRONG FACT and STALE NEWS: "51.8% in January 2025" (lines 0, 1, 31, 85, 89, cover, post)
- Bloomberg's 51.8% was a mid-month projection: the off-exchange share was "on course to account for a record 51.8%" in January.
- MEMX's full-month figure, which the yt_desc itself cites, is **51.6%** for January 2025.
- The headline number is also a January 2025 stat in a video posting in late November 2026.
- A fresher, final figure exists: Cboe's 2025 U.S. Equities Year in Review says the TRF (off-exchange) share was **50.6% of total consolidated volume for full-year 2025**, the first year above half.
- Fix: use the 2025 full-year figure everywhere.

### 2. WEAK OPENING (line 0)
- The current line opens with a date ("In January twenty twenty-five...").
- It runs 12 words, about 3.5-4 seconds, and the stat is about 22 months old.
- Fix: lead with the surprising claim in present tense, in 9 words (about 2.7 s). It is true for full-year 2025.

### 3. WRONG / OVERSTATED: "more concentrated in 2026 than at any point on record" (lines 61-62)
- Vanguard/S&P data puts current concentration as the highest since about 1965, so the mid-1960s were comparable.
- The top-10 weight also hit 40.7% in 2025, so "~40% in mid-2026" is not clearly a record.
- The claim of being far above the dot-com peak (about 26%) is solid.

### 4. ON-SCREEN vs SPOKEN mismatch (line 64; chart end values on lines 64-66)
- On screen it says "2,043.94" and "6,845.50"; the narration says "about two thousand forty-four" and "about six thousand eight hundred forty-six."
- Fix: round the on-screen values to match the narration.

### 5. MISLEADING against the script's own chart (line 68)
- "The index rarely returns anything close to 10% in a single year" is contradicted by the chart viewers are looking at: 2016 was +9.5% in price terms.
- Fix: soften the wording.

### 6. AWKWARD NARRATION (line 46)
- "...before any fees, and nothing even happened" is vague when read aloud.

### 7. Minor (optional, not FAIL-worthy)
- **Line 3/4 chart:** it skips the 2010 SCF survey (49.9%), so the 2007-to-2013 gap is drawn as one step. Adding `[2010, 49.9]` makes the series complete.
- **Lines 27-30:** this is a time-sensitive pre-launch plan. The "As of September 2026" stamp keeps the lines accurate.
  - The editor should re-check the week of November 16 that December 6 has not slipped.
  - If it is confirmed, line 28's text could read "...planned a new overnight session... set to start Dec. 6, 2026."
- **yt_desc:** "CHAPTERS" has no timestamps. Fill them in before posting, or confirm the pipeline adds them.
- **Line 90:** "Follow for more" is a YouTube long-form CTA; "Subscribe for more" fits the platform better.

## Exact replacement text (0-based line index)

**Line 0**
- text: `Most U.S. stock trading never touches a stock exchange.`
- say: `Most US stock trading never touches a stock exchange.`
- scene: `{"t": "hook", "title": "Off the [exchange]", "prop": "tag", "label": "2025", "value": "50.6%", "mood": "shock"}`

**Line 1**
- text: `In 2025, 50.6% of share volume traded away from exchanges like the NYSE and Nasdaq. A first, per Cboe.`
- say: `In twenty twenty-five, fifty point six percent of share volume traded away from exchanges like the N Y S E and Nasdaq. That's a first, according to Cboe.`
- scene: `{"t": "stat", "label": "Off-exchange share of volume", "value": "50.6%", "tone": "neutral", "sub": "2025, Cboe: first year over half"}`

**Line 31** (text and say unchanged)
- scene: `{"t": "hook", "title": "Where does it [go]?", "prop": "box", "label": "2025", "value": "50.6%", "mood": "think"}`

**Line 46**
- text: `That round trip cost $4, or 0.08% of $5,000, before any fees, even though the price never moved.`
- say: `That round trip cost four dollars, or zero point zero eight percent of five thousand, before any fees, even though the price never moved.`
- scene: unchanged.

**Line 61** (text and say unchanged)
- scene: `{"t": "compare", "title": "Top 10 weight", "left": {"label": "2000 peak", "value": "~26%", "tone": "neutral", "sub": "Dot-com era"}, "right": {"label": "Mid-2026", "value": "~40%", "tone": "up", "sub": "Far above 2000"}}`

**Line 62**
- text: `So in 2026, the scoreboard was far more concentrated than even at the dot-com peak.`
- say: `So in twenty twenty-six, the scoreboard was far more concentrated than even at the dot-com peak.`
- scene: `{"t": "compare", "keep": true, "winner": "right", "title": "Top 10 weight", "left": {"label": "2000 peak", "value": "~26%", "tone": "neutral", "sub": "Dot-com era"}, "right": {"label": "Mid-2026", "value": "~40%", "tone": "up", "sub": "Far above 2000"}}`

**Line 64**
- text: `The scoreboard at each year's end: about 2,044 in 2015, and about 6,846 in 2025.`
- say: unchanged.
- scene: same as now, but `"end": "6,846"`.

**Lines 65 and 66**
- scene: same as now, but `"end": "6,846"`. This keeps the keep chain identical.

**Line 68**
- text: `But the average hides a lot. Single years often land far from 10%. It's booms and busts, averaged.`
- say: `But the average hides a lot. Single years often land far from ten percent. It's booms and busts, averaged out.`
- scene: unchanged.

**Line 85**
- text: `Two: trades happen in many places. In 2025, 50.6% of volume ran off the exchanges, mostly through wholesalers.`
- say: `Two. Trades happen in many places. In twenty twenty-five, fifty point six percent of volume ran off the exchanges, mostly through wholesalers.`
- scene: unchanged.

**Line 89** (text and say unchanged)
- scene: `{"t": "hook", "title": "Not one [place]", "prop": "box", "label": "2025", "value": "50.6%", "mood": "happy"}`

**Optional, lines 3 and 4**
- points: `[[2007, 53.2], [2010, 49.9], [2013, 48.8], [2016, 51.9], [2019, 52.6], [2022, 58.0]]`

**Cover**
- `{"title": "Where Do Stock Trades Go?", "prop": "tag", "label": "2025", "value": "50.6%"}`

**Post**
- title: `50.6% of US stock trading skipped the exchanges in 2025. How the market really works`
- ig: `In 2025, for the first time, more than half of US stock trading (50.6%) happened off the exchanges. Here's where it went, and how prices really get set.`
- tiktok: `In 2025, most US stock trading skipped the exchanges. Here's how the stock market actually works.`
- yt_desc, first replacement:
  - Replace: `(in January 2025, 51.8% of US stock volume ran off the exchanges, through wholesalers and dark pools)`
  - With: `(in 2025, 50.6% of US stock volume ran off the exchanges, mostly through wholesalers and dark pools)`
- yt_desc, second replacement:
  - Replace: `Bloomberg data on off-exchange volume (January 2025); MEMX (February 2025);`
  - With: `Cboe, 2025 U.S. Equities Year in Review;`
- yt_desc: also add timestamps under CHAPTERS.

After these edits: 91 lines and 1,767 spoken words, both within limits. The opening line is 9 words, about 2.7 seconds.

## Other checks (no issues)
- **Advice:** none. Line 7 disclaims it, lines 52 and 69 avoid prediction, and the market vs limit order section is a neutral trade-off.
- **Political opinion:** none. The tariffs are not mentioned, and "rough spring" is neutral.
- **Cover/title payoff:** the title and cover question is answered by lines 31-35.
- **Hypotheticals:** the made-up company and the example quote are labeled as examples.
- **Quotes:** word-for-word.

## Sources
- Bloomberg Law, "Wall Street Enters Darker Age With Most Stock Trading Hidden" (Jan 2025; 51.8% "on course")
- MEMX, "Strong Volume in January..." (51.6% full month)
- Cboe, "2025 U.S. Equities Year in Review" (TRF 50.6% for 2025)
- Federal Reserve SCF 2019-2022 bulletin (via Axios and search excerpts)
- Renaissance Capital, US IPO Market 2025 Annual Review
- SIFMA, "10 Key Findings from SIFMA's 2026 Capital Markets Fact Book"
- Troutman Pepper Locke and Simpson Thacher alerts (SEC approval April 10, 2026)
- Jones Day (September 2026; December 6, 2026 start)
- S&P DJI market cap guideline update (via Investing.com and GuruFocus)
- Motley Fool and Vanguard/S&P "Partner Perspectives" (since 1965; dot-com 26%)
- CNBC and ETF Trends (2025 close 6,845.50, +16.39%)
- SEC mission page (search excerpt)
- Reed Smith (FINRA July 30, 2007)
- Investor.gov and Cahill (T+1 May 28, 2024)
- NYSE MWCB working group report and NatLawReview (March 2020 halts; 1997)
- Nasdaq and Fidelity 2026 holiday calendars

VERDICT: FAIL
