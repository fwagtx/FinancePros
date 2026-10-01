# Research brief: 2026-11-09-explainer — What happens in a stock market crash, explained with acorns
Researched October 1, 2026 (posts November 9, 2026). Evergreen mechanics explainer; crisis history (1929, 1987, 2008, Japan) is covered by the Oct 15 long-form, so history is limited to dated 2020 examples.

## Mechanics (definitions)
- A price is where a buyer and a seller agree. In a crash, many more holders want to sell than people want to buy at current prices, so sellers accept lower and lower prices until buyers step in. (Basic market mechanics; SEC Investor.gov.)
- A crash does not make money "disappear into the pockets" of buyers: every share sold has a buyer. Prices fall because the agreed price falls.

## Circuit breakers (current rule, NYSE/SEC; unchanged as of Oct 2026)
- Market-wide circuit breakers measure the S&P 500's drop vs the prior day's close: Level 1 = 7%, Level 2 = 13%, Level 3 = 20%. (NYSE MWCB FAQ; SEC Investor.gov glossary)
- Level 1 or 2 before 3:25 p.m. ET: all US stock trading halts for 15 minutes. At/after 3:25 p.m.: no halt for L1/L2. Level 3 at any time: trading halts for the rest of the day. (NYSE MWCB FAQ)
- March 2020: market-wide circuit breakers triggered four times — March 9, 12, 16 and 18, 2020 (Level 1, 7%, each time). Before that, the only market-wide halt was October 27, 1997. (NYSE MWCB Working Group report; Fidelity; multiple outlets)

## Margin calls (current rules)
- Regulation T: initial margin for stocks = 50% of purchase value (borrow up to half). (Federal Reserve Reg T; FINRA; SEC investor bulletin)
- FINRA Rule 4210: maintenance minimum = 25% of current market value of long margin securities; brokers often set higher "house" requirements. If equity falls below, the broker issues a margin call and can sell the securities. (FINRA Rule 4210; SEC Investor Bulletin "Understanding Margin Accounts")

## Worked example (hypothetical, labeled)
- Squirrel buys $10,000 of stock: $5,000 own money + $5,000 borrowed (Reg T 50%).
- Stock falls 34% (same size as the S&P 500's 2020 drop): $10,000 x 0.66 = $6,600.
- Loan still $5,000. Equity = $6,600 - $5,000 = $1,600. Equity % = 1,600 / 6,600 = 24.2% -> below the 25% FINRA minimum -> margin call.
- Squirrel's own money fell from $5,000 to $1,600 = -68% (twice the market's 34% drop). Forced selling adds more sellers.

## Recovery math (surprising fact)
- S&P 500 record close Feb 19, 2020: 3,386.15. Low close Mar 23, 2020: 2,237.40. Drop = 1 - 2237.40/3386.15 = 33.9% (about 34%).
- To get back: 3386.15 / 2237.40 = 1.513 -> needed a ~51% gain. NPR/AP: "furious 51.5% rally" (to Aug 18 close).
- New record close Aug 18, 2020: 3,389.78. Peak to bottom: 33 calendar days (Feb 19 -> Mar 23). Bottom to new record: about 5 months (Mar 23 -> Aug 18, 148 days); peak to new record ~6 months (181 days). "Quickest bear market on record." (NPR, CNN, Forbes, PBS, Aug 18, 2020)
- Worst single day: March 16, 2020, S&P 500 fell about 12% (11.98%) to 2,386.13, worst day since 1987. (CNBC, Time, CNN)
- Caveat: recovery times vary a lot; past recoveries do not predict future ones.

## Chartable series: S&P 500 closes, 2020 (x = calendar days after Feb 19, 2020)
| Date | Day | Close | Source |
|---|---|---|---|
| Feb 19, 2020 | 0 | 3,386.15 | NPR/Forbes |
| Mar 16, 2020 | 26 | 2,386.13 | CNN/CNBC |
| Mar 23, 2020 | 33 | 2,237.40 | St. Louis Fed / Wikipedia |
| Mar 31, 2020 | 41 | 2,584.59 | AP via news-journal / Fox Business |
| Apr 30, 2020 | 71 | 2,912.43 | (April +12.68%: 2584.59 x 1.1268 = 2912.3, consistent; CNBC) |
| Aug 18, 2020 | 181 | 3,389.78 | NPR/Forbes/CNN |

SOURCES:
- NYSE, Market-Wide Circuit Breakers FAQ: https://www.nyse.com/publicdocs/nyse/NYSE_MWCB_FAQ.pdf
- SEC Investor.gov, Stock Market Circuit Breakers: https://www.investor.gov/introduction-investing/investing-basics/glossary/stock-market-circuit-breakers
- NYSE, Report of the MWCB Working Group: https://www.nyse.com/publicdocs/nyse/markets/nyse/Report_of_the_Market-Wide_Circuit_Breaker_Working_Group.pdf
- Fidelity, Trading halts and circuit breakers: https://www.fidelity.com/learning-center/trading-investing/trading-halts
- FINRA Rule 4210: https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210
- SEC Investor Bulletin, Understanding Margin Accounts: https://www.sec.gov/investor/alerts/ib_marginaccounts.pdf
- NPR, S&P 500 closes at record high 6 months after coronavirus plunge (Aug 18, 2020): https://www.npr.org/sections/coronavirus-live-updates/2020/08/18/903252878/
- Forbes, S&P 500 closes at new record high (Aug 18, 2020): https://www.forbes.com/sites/sergeiklebnikov/2020/08/18/sp-500-closes-at-new-record-high/
- CNN, S&P 500 first record since pandemic (Aug 18, 2020): https://www.cnn.com/2020/08/18/investing/sp-500-stock-market-record
- St. Louis Fed, How COVID-19 has impacted stock performance: https://www.stlouisfed.org/on-the-economy/2021/march/covid19-impacted-stock-performance-industry
- CNBC, One year ago stocks dropped 12% in a single day (Mar 16, 2021): https://www.cnbc.com/2021/03/16/one-year-ago-stocks-dropped-12percent-in-a-single-day-what-investors-have-learned-since-then.html
- Fox Business / AP, Mar 31, 2020 close: https://www.foxbusiness.com/markets/us-stocks-march-31-2020
- CNBC, April 2020 best month since 1987: https://www.cnbc.com/2020/04/30/stock-market-live-today.html
