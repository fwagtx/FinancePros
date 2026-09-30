# Fact-check: 2026-10-13-lf-business ("It's Not the Store." / How Amazon makes money)

Checked Sept 30, 2026 against the posting date of Oct 13, 2026. I ran 19 web searches. Direct fetches of SEC and Amazon IR pages were blocked, so I relied on search excerpts from Amazon's releases and filings plus reputable outlets. I recomputed all the math in python.

## Verified (no change needed)
- **FY2025 (Q4 release Feb 5 2026, 10-K):**
  - Net sales were $716.9B. AWS sales were $128.7B (17.95%, shown as 18%).
  - Operating income was $80.0B. AWS operating income was $45.6B (57.0%).
  - North America operating income was $29.6B and International was $4.7B. Store side = $80.0B - $45.6B = $34.4B.
  - Store-side sales were $716.9B - $128.7B = $588.2B. 34.4/588.2 = 5.85% (shown as 5.8%, said as about 6%).
  - AWS margin was 45.6/128.7 = 35.4%. The ratio is 6.06x, so "roughly six times" holds.
- **FY2025 revenue by group (10-K):**
  - Online stores $269.287B
  - Third-party seller services $172.162B
  - Advertising $68.635B (up 22.1%)
  - Subscriptions $49.619B
  - Physical stores $22.561B
- **Ad revenue chart:** 2021-2024 values are 31.16 / 37.74 / 46.91 / 56.21. 68.64/31.16 = 2.20x, so "more than doubled" holds.
- **AWS operating income chart:** 2019-2024 values are 9.2 / 13.5 / 18.5 / 22.8 / 24.6 / 39.8. 2022 segments were NA -$2.85B, Intl -$7.75B, AWS +$22.84B, total $12.25B. "Cloud earned more than the whole company" holds.
- **Cash flow:**
  - Operating cash flow 2025 was $139.5B, up 20%.
  - FCF was $11.2B in 2025, down from $38.2B.
  - Gross cash purchases of property and equipment were $131.819B. Net of proceeds they were $128.3B, which is the figure Amazon uses for FCF. The "cash purchases" label is accurate.
- **TTM free cash flow through June 30 2026:** an outflow of $7.6B (Q2 2026 release). Correct as scripted (L75).
- **Q2 2026 (July 30 2026):**
  - Operating income was $27.5B. AWS operating income was $16.6B, and 16.6/27.5 = 60.4% (said as "about 60%").
  - AWS sales were $42.2B, up 36.7%, rounded to 37%.
  - Ads were $19.8B, up 26%.
  - The 2026 capex plan was raised to about $220B, up from about $200B.
- **Jassy quote (L72):** it matches the call word for word: "...we will still not have enough capacity to meet all the demand we have in 2026..." (full sentence continues "...and I believe this dynamic will also be true in 2027 too").
- **Synergy Q2 2026 cloud shares:** AWS 28%, Microsoft 20%, Google a record 15%.
- **Third-party share of paid units:** 61% in Q4 2025.
- **FTC trial:** the scheduling order by Judge Chun (W.D. Wash.) moved the trial from Feb 9 2027 to March 29, 2027. The script frames it as an allegation and includes Amazon's denial.
- **Prime settlement:** Sept 25 2025, $2.5B total ($1B civil penalty plus $1.5B refunds). Amazon neither admitted nor denied the allegations.
- **Oct 20 2025 AWS outage:** a DynamoDB DNS failure in US-EAST-1 caused about 15 hours of disruption. Snapchat, Reddit, Venmo, Fortnite and other apps went down. "For hours" is correct.
- **History:**
  - Amazon was founded July 1994, and the store opened July 1995.
  - IPO was May 1997 at $18.
  - Prime launched in Feb 2005 at $79 with two-day shipping.
  - S3 launched March 14 2006, and EC2 followed in Aug 2006.
  - Prime Video ads began Jan 29 2024, with a $2.99 ad-free add-on.
- **Prime price:** $139/yr or $14.99/mo as of Sept 2026, and no US increase has been announced. 14.99 x 12 = $179.88, which is $40.88 more than the annual fee. The $20 x 15% = $3.00 example is correct and is labeled as a hypothetical.
- **Hook (L1):** it is true, specific and short (about 2.5 s), and the cover and title pay it off (L2, L93). It is acceptable as is. An optional stronger version: "57% of Amazon's profit comes from something you've never bought."
- **Tone:** there is no advice, no price prediction and no political opinion. The takeaways (L84-L88) describe things rather than tell viewers what to do.

## Issues and fixes (all minor)
1. **L79 (FTC trial):** MLex reports that Amazon plans to ask for another postponement of the March 29 2027 trial. Fix: say "is currently scheduled for trial on March 29, 2027."
2. **L28 scene sub:** "$29.6B NA + $4.75B Intl." Amazon reports International as $4.7B. Fix: use "$29.6B NA + $4.7B Intl." or "$80.0B total - $45.6B AWS", so the on-screen parts match the published rounding.
3. **L23:** Q4 2025 (61%) is stale when Q2 2026 data exists. The Q2 2026 share was also 61%, down from 62% a year earlier. Fix: text "61% of paid units in mid-2026", say "in the April to June quarter of twenty twenty-six", and change the scene label to "Q2 2026".
4. **L42 "mostly Prime":** Amazon doesn't disclose how the subscriptions line splits. It covers Prime fees plus video, music, audiobooks and so on. Fix: "including Prime" or "largely Prime membership fees" (softer).
5. **L13:** "started renting its computing power" in March 2006 slightly conflicts with L14, which says compute (EC2) came in August. Fix: "started renting its computer infrastructure to other companies."
6. **Post yt_desc:** the "CHAPTERS" heading is empty. Fill in the timestamps or remove the heading.
7. **Risk to watch:** if Amazon announces a US Prime price increase before Oct 13, lines L43-L45 and L87 need updating. They are dated "as of September 2026", so they stay technically accurate.
8. **Visual nit (L50/L82):** the building uses kind "store" for "AWS DATA CENTER". Use a data-center or server visual if one is available.

I found no on-screen versus spoken number mismatches beyond acceptable rounding (5.8% shown vs "about 6%" said; 35.4% vs "about 35%"). No time words will be wrong on Oct 13, since Q3 2026 results come after the posting date.

## Sources (excerpts)
- Amazon Q4 2025 release: aboutamazon.com / businesswire (Feb 2026)
- Amazon 10-K FY2025 via sec-api.io
- Amazon Q2 2026 release: aboutamazon.com, TradingView, Yahoo Finance
- CNBC and Yahoo on the Jassy quote (July 30 2026)
- Synergy via tech-insider and 16IDC
- MLex articles 2422758 and 2526407
- CNBC, Axios and NBC on the Prime settlement
- ThousandEyes and Gremlin on the Oct 20 2025 outage
- AWS blog and Wikipedia on S3 and EC2
- DealNews (Prime cost, Sept 2026)
- Marketplace Pulse and ecomcrew (third-party unit share)

VERDICT: PASS
