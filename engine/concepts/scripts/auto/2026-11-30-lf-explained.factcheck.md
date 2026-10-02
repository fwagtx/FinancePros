# Fact-check: 2026-11-30-lf-explained ("Index funds: how a boring idea took over Wall Street")

Checker: independent. Checked on Oct 2, 2026, for posting on Nov 30, 2026. I read only the raw.json and the checker rules, not the research.md.
Scope: all 92 lines (text, say, scene), the cover, the header, and the post (title, ig, tiktok, yt_desc, tags).
Spoken words: 1,791 now. With the fixes below it is 1,790, which stays inside the 1550-1800 target.

## Math (recomputed in Python)
- $10,000 x 1.0695^30 = **$75,062.61**. $10,000 x 1.0636^30 = **$63,584.29**. With no fee, 1.07^30 gives **$76,122.55**. The script's figures match.
- The gap is $11,478.32, which is 15.3% of the low-fee result. The cost against no fee is $12,538.26 at 0.64% and $1,059.94 at 0.05%. All match.
- First-year fees on $10,000 are $5 and $64. 0.64/0.05 = 12.8x, so "nearly 13 times" is right. The fall from 0.27% to 0.05% is -81.5%, so "more than 80%" is right.
- Buffett bet: $100 becomes $225.80 or $136.30. Correct.
- The example is labeled hypothetical, the 7% is labeled an assumption, and the script says "not a prediction". Good.

## Verified (no change needed)
| Claim | Finding |
|---|---|
| SPIVA YE2025: 79% trailed in 2025 | Confirmed: 79%, up from 65% in 2024 |
| SPIVA YE2025 10-yr ">80%", 15-yr "~90%" | Confirmed: **84.34%** (10-yr) and **89.50%** (15-yr). The wording is fine. |
| SPIVA H1 2026: 67% | Confirmed: SPIVA U.S. Mid-Year 2026 reports 67% of large-cap funds trailed |
| Morningstar barometer: ~25% survived and beat over 10 yrs to June 2026 | Confirmed |
| Vanguard 500 Index Fund ">$1.6T" (all classes) | True but understated. Vanguard lists **$1.8T total net assets across all share classes (including the ETF class, VOO) as of Aug 31, 2026**. Admiral shares alone are $693B, so the fund-level figure is the right one to use. An optional upgrade is ">$1.7T"; ">$1.6T" is still accurate. |
| ICI fee points 1996 0.27, 2016 0.09, 2019 0.07, 2020 0.06, 2022 0.05, 2025 0.05; active 1.08 to 0.64 | Confirmed (ICI Trends reports; 2025 edition released March 2026) |
| SPY >$800B late Sept 2026 | Confirmed: about $805-809B (State Street, Sept 30, 2026) |
| SPY launched Jan 1993, first US ETF | Confirmed (Jan 22, 1993; first traded Jan 29, 1993) |
| Wells Fargo 1971, $6M Samsonite pension, equal-weighted NYSE, later switched to S&P 500 | Confirmed |
| First Index Investment Trust, Aug 31, 1976, $11.3M, 280 stocks, "Bogle's Folly", "un-American", Bogle called it a "complete flop" | Confirmed. One note: some sources put the target as "$50-150 million". "$150M goal" is the common shorthand and is acceptable. |
| Passive share: 1995 3%, 2005 14%, Mar 2020 41% | Confirmed: Fed/Boston Fed paper (Anadu et al.) using Morningstar data on US MF+ETF assets |
| End-2023 crossover $13.25T vs $13.24T; 2024 53%; end-2025 >55% | Confirmed (Morningstar: $13.252T passive vs $13.244T active; 53% to 55%+ in 2025) |
| Comparability of chart series | All points rest on Morningstar US mutual fund plus ETF data, so they are broadly comparable. The 2020 point is March 2020, not year-end; the narration says "by March 2020", which is acceptable. |
| BlackRock $15.3T at June 30, 2026 | Confirmed: $15.34T, a record (Q2 2026 results) |
| Buffett bet 2008-2017, Protégé, five funds of funds, +125.8% vs +36.3%, ~$2.2M to Girls Inc. of Omaha | Confirmed (2017 letter) |
| Buffett statue quote, 2016 letter | Word-for-word match |
| Bebchuk & Hirst: 13.5% (2008) to 20.5% (2017); ~25% of votes (25.4%) | Confirmed |
| Azar, Schmalz & Tecu (JF 2018) vs Dennis, Gerardi & Schenone (JF 2022) | Confirmed. The 2022 paper finds the fare link is spurious, and the original authors have published a rebuttal, so "debate continues" is accurate. |
| Cover "Wall Street Laughed At This." (bag prop, 1976 / $11.3M) | Paid off in lines 1, 21 and 70. The prop is not 'paper'. |
| yt_desc | Keeps the bare "CHAPTERS" line. The fee and example figures match the script. |

## Issues

1. **L69: Vanguard AUM is vague and likely understated (factual).** The line says "about $12T in 2026" with no date. Vanguard's 2026 Europe "in a nutshell" says USD 12T. Vanguard Australia reports AUD 19.30T at June 30, 2026, and other reporting gives about $13.3T by May/June 2026. "About $12T" for mid-2026 is too low, and a dated precise figure could not be confirmed from a primary US source. A safe floor is ">$12T".
   - text: `Vanguard: more than $12T in 2026.`
   - say: `Vanguard managed more than twelve trillion dollars in twenty twenty-six.`
   - scene: `{"t":"stat","label":"Vanguard assets managed","value":">$12T","tone":"up","sub":"Mid-2026"}`

2. **L79: stale ICI figure (stale news).** The 18% figure is for end-2024 and comes from the 2025 Fact Book. The **2026 Fact Book (April 2026) says index domestic equity mutual funds and ETFs held 19% of US stock value at year-end 2025.** L80's "under a fifth" still holds.
   - text: `Index stock funds held about 19% of US stocks at the end of 2025 (ICI).`
   - say: `Then again, index stock funds held only about nineteen percent of all US stock value at the end of twenty twenty-five, per the Investment Company Institute.`
   - scene: `{"t":"stat","label":"US stocks in index funds","value":"19%","tone":"neutral","sub":"End-2025, ICI"}`

3. **L82: BlackRock Voting Choice date is unverified and likely wrong (factual).** "$3.96T eligible" appears in BlackRock's **2026** Global Voting Spotlight and on its Voting Choice page, next to $8.79T of total index equity AUM. Search excerpts tie it to 2026, and one excerpt put Dec 31, 2025 at about $3.76T. The "Dec 2025" label cannot be confirmed. Attribute the figure to the report instead.
   - text: `BlackRock: $3.96T of index stock assets eligible for Voting Choice (2026).`
   - say: `In its twenty twenty-six voting report, BlackRock said three point nine six trillion dollars of its index stock assets were eligible for that choice.`
   - scene: `{"t":"stat","label":"BlackRock Voting Choice","value":"$3.96T","tone":"neutral","sub":"Eligible, 2026"}`

4. **L83: Vanguard Investor Choice is stale (stale news).** "12 funds, nearly 10 million investors" was the 2025 state. On **Feb 25, 2026**, Vanguard added 17 funds, including the Vanguard 500 Index Fund. That brought eligible investors to **about 22 million** and eligible assets to **over $3.6T**.
   - text: `Vanguard widened its program in Feb 2026: about 22 million investors eligible.`
   - say: `Vanguard widened its own program in February twenty twenty-six, to about twenty-two million eligible investors.`
   - scene: `{"t":"board","lines":["Vanguard, Feb 2026:","~22M investors eligible"]}`

5. **L59: layout limit broken.** The split item "Odds vary by year" is 17 characters, over the limit of 16.
   - scene.right.items: `["Some do win","Odds vary yearly"]` (16). text and say are unchanged.

6. **L26: the on-screen text overgeneralizes and does not match the spoken line.** The text says "An ETF is an index fund..." but the narration correctly says "a fund, often an index fund". Active ETFs exist.
   - text: `An ETF is a fund that trades all day like a stock.` (say and scene are unchanged; the scene is already correct)

7. **L3: narration reads awkwardly out loud.** "which is honestly kind of boring, went on to take over" is clunky.
   - say: `And the boring idea behind it went on to take over Wall Street.` (saves 5 words). text and scene are unchanged.

8. **L78: framing balance (minor).** The 2018 side is toned "down" and the 2022 side "neutral", which visually favors one study. Both should be neutral.
   - scene.left.tone: `"neutral"`

9. **L1: opening (minor, optional).** The line is true, specific, curiosity-driven and about 3 seconds long, so it passes. To make it hit harder and land inside 3 seconds, move the date to the screen (the label already shows 1976):
   - say (optional): `Wall Street laughed at this fund in nineteen seventy-six.` (same length, puts the hook first). Or, shorter: `Wall Street laughed at this fund.`

10. **L57/L58: redundancy (minor style).** L57 ("Buffett had already praised Bogle in his 2016 shareholder letter") and L58's on-screen text say the same thing back to back. This is optional to fix and not a cause for FAIL.

11. **L2/L70/tiktok (optional).** ">$1.6T" is true. Vanguard's own figure is $1.8T across all classes at Aug 31, 2026, so ">$1.7T" would be more current. Nothing has to change.

No advice, price predictions or political opinion found. The disclaimer is at L8 and L84 stays neutral. Time words are all dated ("late September 2026", "first half of 2026", "fifty years later", which is right for the Aug 2026 anniversary), so none will be wrong on Nov 30. All keep:true lines follow the same scene template. No other layout limits were exceeded. The cover title is 28 characters.

Word count after fixes: 1,791 -5 (L3) +1 (L69) +3 (L82) +0 (L79, L83) = **1,790**.

## Sources
- S&P DJI SPIVA U.S. Year-End 2025 and Mid-Year 2026: https://www.spglobal.com/spdji/en/spiva/ ; https://www.investmentnews.com/equities/active-managers-stumble-again-in-2025-as-large-caps-dominate/265541 ; https://www.tker.co/p/spiva-1h-2026-active-manager-vs-benchmark
- Morningstar Active/Passive Barometer mid-2026: https://www.morningstar.com/funds/active-fund-manager-success-rates-ticked-up-2026-passive-funds-still-hold-advantage
- Vanguard 500 Index Fund total net assets: https://workplace.vanguard.com/investments/product-details/fund/0540
- Vanguard AUM: https://www.ch.vanguard/content/dam/intl/europe/documents/en/vanguard-in-a-nutshell-eu-en.pdf ; https://fund-docs.vanguard.com/AU-Annual_report-Vanguard_Wholesale_International_Equities_Active_Funds_and_ETFs_Unhedged.pdf
- ICI fees: https://www.ici.org/files/2026/per32-01.pdf ; https://www.ici.org/system/files/2023-03/per29-03.pdf
- ICI Fact Books: https://www.icifactbook.org/pdf/2025-factbook.pdf ; https://icifactbook.org/pdf/2026-factbook-ch2.pdf
- SPY: https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-500-etf-trust-spy ; https://en.wikipedia.org/wiki/SPDR_S%26P_500_ETF_Trust
- Passive share: https://www.federalreserve.gov/econres/feds/files/2018060r1pap.pdf ; https://www.morningstar.com/funds/recovery-us-fund-flows-was-weak-2023 ; https://www.morningstar.com/funds/8-charts-us-fund-flows-2025-highest-net-inflows-since-2021
- History: https://workplace.vanguard.com/insights-and-research/perspective/50-years-50-facts-indexing-since-1976.html ; https://www.ifa.com/articles/fifty_years_bogle_folly ; https://en.wikipedia.org/wiki/Index_fund
- Buffett: https://money.cnn.com/2018/02/24/investing/warren-buffett-annual-letter-hedge-fund-bet/index.html ; https://www.bogleheads.org/forum/viewtopic.php?t=212099
- BlackRock: https://qz.com/blackrock-record-assets-q2-earnings-071526 ; https://www.blackrock.com/corporate/about-us/investment-stewardship/blackrock-voting-choice
- Vanguard Investor Choice: https://www.prnewswire.com/news-releases/vanguard-adds-17-new-funds-to-vanguard-investor-choice-302696127.html
- Bebchuk & Hirst: https://www.nber.org/system/files/working_papers/w25914/w25914.pdf
- Common ownership: https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.13176

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-8. The optional items were not applied. VERDICT: PASS
