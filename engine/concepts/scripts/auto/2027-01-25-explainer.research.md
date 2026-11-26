# Research brief: Margin calls (Acorn Economics) - posts Mon Jan 25, 2027, 12 PM Central (evergreen)

## Key rules (definitions that can change; confirmed Nov 26, 2026)
- Initial margin, Regulation T (Federal Reserve Board, 12 CFR 220): a broker can lend up to 50% of the purchase price of a stock for new purchases. Some firms require more than 50% down. (FINRA "Know What Triggers a Margin Call"; FINRA Margin Regulation page; SEC/Investor.gov margin pages)
- Maintenance margin, FINRA Rule 4210: equity in the account must not fall below 25% of the current market value of the securities. This is a floor; firms may set higher "house" requirements, e.g. 30% or 40%, and can raise them at any time without advance written notice. (FINRA Rule 4210; FINRA investor insight on margin calls)
- No warning required: firms don't have to issue a margin call before selling securities in a margin account, can choose which securities to sell, and may sell enough to pay off the whole loan. (FINRA investor insight; SEC "Margin: Borrowing Money to Pay for Stocks", sec.gov/answers/marsell.htm)
- Definition: a margin call is a demand from the broker to add cash or securities (or sell) when account equity falls below the maintenance requirement.

## Worked example (our math)
- Buy $10,000 of stock with $5,000 cash + $5,000 margin loan (50% Reg T initial margin).
- Equity = Value - Loan. Call at 25% maintenance when (V - 5,000) / V = 0.25 -> V - 5,000 = 0.25V -> 0.75V = 5,000 -> V = $6,666.67.
- Drop from $10,000 to $6,666.67 = 33.3% (about a third). Equity at that point = $1,666.67 = 25% of $6,666.67.
- With a 30% house requirement: 0.70V = 5,000 -> V = $7,142.86 (a 28.6% drop) -- call comes sooner.
- If the stock falls 50% (to $5,000): value $5,000 - loan $5,000 = $0 equity. Your $5,000 cash is 100% gone (2x leverage doubles the percent loss), before interest.

## Surprising fact
- The broker doesn't have to call you first. It can sell your shares without notice, pick which ones, and you still owe any shortfall.

## Chartable data series: FINRA debit balances in customers' securities margin accounts (year-end, $ billions)
| Date | Margin debt |
|---|---|
| Dec 31, 2022 | $606.66B (~$607B) |
| Dec 31, 2023 | $700.77B (~$701B) |
| Dec 31, 2024 | $899.17B (~$899B) |
| Dec 31, 2025 | $1,225.6B (FINRA table: 1,225,597 million) (~$1.2T) |
- 2022 -> 2025: about doubled (1,225.6 / 606.66 = 2.02x, our math).
- Context: June 2026 = $1,502,072 million (~$1.5T), series high per FINRA table/GuruFocus (not used on screen; avoid "recent").
- Sources: FINRA Margin Statistics table (Dec-25 1,225,597; Nov-25 1,214,321); YCharts FINRA Margin Debt series (I:FINRADBC) for each Dec value; Benzinga (Jan 2026) "$1.23 trillion" Dec 2025; convextrade archive $1,225.6B Dec 2025. Note finra.org could not be fetched directly in this session (network); values agree across the search snippets of FINRA's table and YCharts.

## Angle
Evergreen. No news hook needed; margin debt at record levels in 2025-2026 makes it relevant, but keep dated.
Education only; no advice; no predictions.

SOURCES:
- Federal Reserve Board, Regulation T (12 CFR Part 220) - 50% initial margin, via FINRA: https://www.finra.org/investors/insights/margin-calls
- FINRA Rule 4210 Margin Requirements: https://www.finra.org/rules-guidance/rulebooks/finra-rules/4210
- FINRA, Know What Triggers a Margin Call: https://www.finra.org/investors/insights/margin-calls
- SEC, Margin: Borrowing Money to Pay for Stocks: https://www.sec.gov/answers/marsell.htm
- FINRA Margin Statistics: https://www.finra.org/rules-guidance/key-topics/margin-accounts/margin-statistics
- YCharts FINRA Margin Debt: https://ycharts.com/indicators/finra_margin_debt
- Benzinga (Jan 2026) margin debt $1.23T: https://www.benzinga.com/markets/equities/26/01/50053598/trump-credit-card-investor-leverage
- Convextrade FINRA margin debt history: https://convextrade.com/metrics/finra-margin-debt/history
