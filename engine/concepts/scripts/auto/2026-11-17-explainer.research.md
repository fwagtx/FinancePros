# Research: Market orders vs limit orders (speed vs price)

## Definitions (SEC Investor Bulletin "Understanding Order Types"; investor.gov glossary)
- Market order: buy/sell at the best available price; generally executes immediately; price NOT guaranteed; the last-traded price is not necessarily the execution price. Advantage: almost always executes. Disadvantage: price may differ from what you expected, especially in fast-moving markets.
- Limit order: buy/sell at a specific price or better. Buy limit executes only at the limit or lower; sell limit only at the limit or higher. Price control, but no guarantee it executes. Example (investor.gov): buy ABC for no more than $10.

## Real-world case: May 6, 2010 "Flash Crash" (SEC/CFTC joint report, Sept 30, 2010)
- Began ~2:32 p.m. ET, lasted ~36 minutes. Dow fell nearly 1,000 points (~9%) intraday and closed down 348.
- Accenture (ACN) fell from about $40 to $0.01 (one cent), then closed at $41.09.
- Over 20,000 trades in more than 300 securities executed 60% or more away from their 2:40 p.m. prices; many were retail customer orders. Exchanges and FINRA canceled ("broke") those trades as clearly erroneous.
- Market orders (and stop orders that became market orders) executed against "stub quotes" (placeholder bids like $0.01). Afterward: stub quotes banned (Dec 2010), single-stock circuit breakers, then Limit Up-Limit Down (2013).

## Data series (Accenture, May 6, 2010, sequence of prints per reports)
- quote before ~$39; trades $32.62, $5.34, $4.04, $1.84, $0.01; close $41.09. (Wikipedia/encyclopedia summaries of SEC-CFTC report) - not charted in video (prints are sequence, not time series).
- Dow: down nearly 1,000 points intraday; close -348 (CNBC).

## Worked example (hypothetical)
- Stock quoted $50.00 bid / $50.10 ask. Buy 100 shares.
- Market order in a calm market: fills near ask: 100 x $50.10 = $5,010.
- If price jumps to $51.00 before it fills: 100 x $51.00 = $5,100 -> $90 more.
- Buy limit at $50.10: pays at most $5,010, or doesn't fill at all.

## Surprising fact
- In the 2010 flash crash, a roughly $40 stock (Accenture) traded for one penny.

SOURCES:
- SEC Investor Bulletin, Understanding Order Types: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-14
- investor.gov, Market Order / Limit Orders glossary: https://www.investor.gov/introduction-investing/investing-basics/glossary/market-order
- SEC/CFTC, Findings Regarding the Market Events of May 6, 2010: https://www.sec.gov/files/marketevents-report.pdf
- SEC press release 2010-104 / speeches on erroneous trades
- CNBC (May 6, 2014), The lasting impact of the 2010 flash crash: https://www.cnbc.com/2014/05/06/the-lasting-impact-of-the-2010-flash-crash.html
