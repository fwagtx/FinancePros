# Research brief: Why mortgage rates move with the 10-year Treasury (2026-10-10-explainer)

Researched Wednesday, September 30, 2026. Posts Saturday, October 10, 2026. Oct 5 video covers amortization, so this one focuses on the 10-year Treasury link and the spread.

NOTE on the Oct 1 PMMS: the next Freddie Mac survey is released Thursday, October 1, 2026, after this research date, so it could NOT be checked. The script labels every rate with its date (September 24, 2026), so it stays true after Oct 1. The build/fact-check step should look at the Oct 1 (and Oct 8) PMMS; if the 30-year moved a lot, consider mentioning it, but the dated figures remain accurate either way.

## Timely angle
- Freddie Mac PMMS, Sept 24, 2026: 30-year fixed averaged **7.03%**, up from 6.95% the week before (Sept 17); a year earlier (Sept 25, 2025) it was 6.30%. First time above 7% since January 2025. 15-year: 6.42% (prior week 6.26%; year ago 5.49%). [Freddie Mac release "Mortgage Rates Average 7.03%" via GlobeNewswire/Yahoo Finance; Fox Business; NPR, Sept 24, 2026]
- September 2026 weekly 30-year PMMS: Sept 3 6.71%, Sept 10 6.76%, Sept 17 6.95%, Sept 24 7.03%. [Freddie Mac releases]
- 10-year Treasury yield: **5.18% on September 24, 2026** (Treasury daily par yield curve per search results; also MacroRadar). 5.17% on Sept 25 (Advisor Perspectives). CNBC (Sept 26, 2026): 10-year at its highest in nearly two decades; reached about 5.23%, highest since 2007.
- Same-day gap, Sept 24, 2026: 7.03 - 5.18 = **1.85 percentage points**.
- The Fed raised the federal funds target range 0.25 point to 3.75%-4% on September 16, 2026, first increase since 2023. [CNBC, Advisor Perspectives, Sept 16, 2026] The Fed sets a short-term overnight rate; it does not set mortgage rates.

## Why the 10-year (mechanism)
- Most 30-year mortgages are pooled into mortgage-backed securities (MBS) and sold to investors; MBS compete with Treasurys for investor money. Treasurys are government-backed; MBS carry default and prepayment risk, so investors demand more yield. [Fannie Mae, "What Determines the Rate on a 30-Year Mortgage?"; Chase, "How Bonds Affect Mortgage Rates"]
- Mortgages are benchmarked to the 10-year because although the term is 30 years, many borrowers move or refinance well before then (commonly cited 7 to 10 years), so the expected life is closer to 10 years. [Chase; Brevitas; Kiplinger]
- Spread components (Fannie Mae): primary-secondary spread (lender costs and margins) + secondary spread (extra risk of MBS vs the 10-year).

## Chartable series: annual average spread, 30-yr mortgage (Freddie Mac PMMS) minus 10-yr Treasury, percentage points
| Year | Spread |
|---|---|
| 2021 | 1.52 |
| 2022 | 2.43 |
| 2023 | 2.85 (peak) |
| 2024 | 2.53 |
| 2025 | 2.29 |
| 2026 (year to date, ~Sept) | 1.98 |
Source: HousingWire / MarketXLS spread data (computed from Freddie Mac PMMS and Treasury yields); 2023 and 2025 values cross-checked in a second search (Understanding Mortgage Spreads, Ameris Bank; businessmodelanalyst). Cross-check with annual averages: 2021 PMMS 2.96% - 10-yr 1.45% = 1.51; 2023 6.81% - 3.96% = 2.85.
- Long-run average spread: about 1.7 points (1990-2021 ~170 basis points, per MBA/First American); ~1.76 since records began (marketxls). Wolf Street (Sept 3, 2026): spread "stuck" around 2 points.

## Worked example (hypothetical, same 10-year yield, different spread)
Assumptions: $300,000 loan, 30-year fixed, monthly payment of principal and interest only.
Formula: M = L x r / (1 - (1 + r)^-360), r = annual rate / 12.
- At 7.03% (10-yr 5.18% + 1.85 spread): r = 0.0058583; M = **$2,001.96** (about $2,002).
- At 8.03% (same 10-yr + 2.85 spread, the 2023 average): r = 0.0066917; M = **$2,207.57** (about $2,208).
- Difference: $205.62 a month.

## Surprising fact
A 30-year mortgage is priced off the 10-year Treasury, not the 30-year Treasury and not the Fed's rate, because most mortgages end early when people move or refinance.

## Weakly sourced
- 10-year 5.18% on Sept 24 comes from search-result summaries of Treasury/aggregator pages (direct fetch blocked); 5.17% on Sept 25 and ~5.15% "roughly" corroborate.
- The annual spread series comes from aggregators (HousingWire/MarketXLS); 2023 and 2025 values double-confirmed; my own arithmetic from known annual averages matches 2021 and 2023. The 2026 YTD cut-off date is not exact.
- "7 to 10 years" mortgage life is from lender/educational sources, not an official statistic; the script avoids an exact figure.

SOURCES:
- Freddie Mac PMMS release "Mortgage Rates Average 7.03%" (Sept 24, 2026): https://freddiemac.gcs-web.com/news-releases/news-release-details/mortgage-rates-average-703 ; https://www.globenewswire.com/news-release/2026/09/24/3368592/0/en/mortgage-rates-average-7-03.html ; https://finance.yahoo.com/real-estate/articles/mortgage-rates-average-7-03-160000686.html
- Fox Business, "Mortgage rates rise to 7.03%": https://www.foxbusiness.com/economy/mortgage-rates-9-24-2026
- NPR, Sept 24, 2026: https://www.npr.org/2026/09/24/nx-s1-5977796/mortgage-rates-freddie-mac-homebuying
- Freddie Mac PMMS: https://www.freddiemac.com/pmms
- US Treasury daily par yield curve / FRED DGS10: https://fred.stlouisfed.org/series/dgs10
- MacroRadar 10-year (5.18%, Sep 2026): https://www.macroradar.io/10-year-treasury-yield
- Advisor Perspectives Treasury Yields Snapshot Sept 25, 2026: https://www.advisorperspectives.com/dshort/updates/2026/09/25/treasury-yields-snapshot-september-25-2026
- CNBC, "The 10-year Treasury yield is at its highest in nearly two decades" (Sept 26, 2026): https://www.cnbc.com/amp/2026/09/26/10-year-treasury-yield-is-at-its-highest-in-19-years-how-we-got-here.html
- CNBC, Fed rate decision Sept 16, 2026: https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html
- Fannie Mae, What Determines the Rate on a 30-Year Mortgage?: https://www.fanniemae.com/research-and-insights/publications/housing-insights/rate-30-year-mortgage
- Chase, How Bonds Affect Mortgage Rates: https://www.chase.com/personal/mortgage/education/financing-a-home/how-bonds-affect-mortgage-rates
- HousingWire spread: https://www.housingwire.com/30-year-mortgage-vs-10-year-treasury-spread/
- MarketXLS spread chart: https://marketxls.com/indicators/mortgage-treasury-spread
- Wolf Street, Sept 3, 2026: https://wolfstreet.com/2026/09/03/the-spread-between-10-year-treasury-yield-30-year-mortgage-rate-has-been-stuck-at-2-percentage-points-despite-fannie-freddie-mbs-buybacks-some-thoughts/
- First American, Mind the Gap: https://blog.firstam.com/economics/mind-the-gap-between-mortgage-rates-and-the-10-year-treasury-yield
