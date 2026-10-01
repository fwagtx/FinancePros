# Research brief: Why timing the market is so hard, explained with acorns
Slot: 2026-10-19-explainer (posts Monday, October 19, 2026). Researched September 30, 2026. Evergreen; no news hook needed.

## Core facts (latest edition: J.P. Morgan Asset Management, Guide to Retirement 2026)
- Study: $10,000 in the S&P 500 Total Return Index, January 2, 2006 to December 31, 2025 (20 years).
- Fully invested: grew to $80,619, or 11.0% a year.
- Missed only the 10 best days: $35,866, or 6.6% a year.
- Missed the 40 best days (out of roughly 5,000 trading days): $9,462, about -0.3% a year, less than the $10,000 put in.
- Six of the 10 best days fell within two weeks of the 10 worst days (2006-2025); five of those six came after the worst days.
- J.P. Morgan's note: the second-worst day of 2020 (March 12) was immediately followed by the second-best day of 2020.
- Older edition for context (2025 Guide, 2005-2024): $71,750 fully invested vs $32,871 missing 10 best days; 7 of 10 best days within two weeks of a worst day. NOT used in script (superseded).
- WEAKLY SOURCED (one search summary only, not used): missing 20 best days = 3.6% a year; missing 30 = 1.4% a year.
- Note: an independent replication (cash earning 0%) gets 10.91% vs 6.51%; J.P. Morgan's published figures are 11.0% / 6.6%. Script uses J.P. Morgan's figures and names J.P. Morgan.

## Worked example (exact math)
- Gap: $80,619 - $35,866 = $44,753.
- Share lost vs staying in: 1 - 35,866 / 80,619 = 0.5551 -> about 56% less.
- Days missed as a share of trading days: 10 / ~5,000 = 0.2% of trading days.
- Sanity check of J.P. Morgan's rates: $10,000 x 1.11^20 = $80,623 (matches $80,619 at 11.0% rounded); $10,000 x 1.066^20 = $35,904 (matches $35,866 at 6.6% rounded).
- 40-day case: (9,462 / 10,000)^(1/20) - 1 = -0.28% a year -> "-0.3%".

## Chartable data series: S&P 500 daily closes, March 2020 (COVID crash)
| Date (2020) | Close | Daily change |
|---|---|---|
| Mar 6 | 2,972.37 | (base) |
| Mar 9 | 2,746.56 | -7.6% |
| Mar 10 | 2,882.23 | +4.9% |
| Mar 11 | 2,741.38 | -4.9% |
| Mar 12 | 2,480.64 | -9.5% |
| Mar 13 | 2,711.02 | +9.3% (+9.29%) |
| Mar 16 | 2,386.13 | -12.0% |
| Mar 17 | 2,529.19 | +6.0% |
Chart x = day of March 2020 (9,10,11,12,13,16,17), y = close.
- March 12, 2020: S&P 500 fell 9.5%, worst day since October 19, 1987 at the time (CNBC, March 12, 2020).
- March 13, 2020: S&P 500 rose 9.29%, best day since 2008 (Yahoo Finance / Zacks, March 13, 2020).

## The surprising fact
The best days and worst days cluster together: six of the 10 best days in 2006-2025 came within two weeks of the 10 worst. Selling after a scary drop often means missing the rebound. March 12-13, 2020 is the textbook case: -9.5% then +9.3% the next day.

## Squirrel framing
Squirrel buries acorns. Scary storm (big drop), squirrel runs off. Comes back after the bounce already happened. The good days hide right next to the bad ones.

## Neutrality / compliance
Education only: describe what happened and the math; no instructions, no predictions. Caveat: the study assumes the missed days earn nothing (cash at 0%); real timers also miss some worst days.

SOURCES:
- J.P. Morgan Asset Management, Guide to Retirement 2026, "Impact of being out of the market" ($10,000, Jan 2, 2006-Dec 31, 2025): https://am.jpmorgan.com/content/dam/jpm-am-aem/global/en/insights/retirement-insights/guide-to-retirement-us.pdf (figures confirmed via multiple search summaries quoting it; direct fetch blocked)
- J.P. Morgan Asset Management, Principles for a successful retirement 2026: https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/insights/retirement-insights/principles-for-a-successful-retirement.pdf
- CNBC, April 1, 2026, "Stock market is in for 'choppy, bumpy ride' in 2026 ... Why it pays to stay invested" (cites J.P. Morgan 2006-2025: 11% vs 6.6%): https://www.cnbc.com/2026/04/01/investors-stock-market-volatility.html
- CNBC, April 7, 2025 (prior-edition figures, context only): https://www.cnbc.com/2025/04/07/selling-out-during-the-markets-worst-days-can-hurt-you-research.html
- S&P 500 closes March 2020: Wikipedia, Closing milestones of the S&P 500 / StatMuse S&P 500 daily returns March 2020: https://www.statmuse.com/money/ask/s-and-p-500-daily-returns-for-march-2020
- CNBC, March 12, 2020, S&P 500 down 9.5%: https://www.cnbc.com/2020/03/12/stock-market-today-live.html
- Yahoo Finance, Stock Market News for Mar 13, 2020 (S&P 500 +9.29%): https://finance.yahoo.com/news/stock-market-news-mar-13-143302476.html
