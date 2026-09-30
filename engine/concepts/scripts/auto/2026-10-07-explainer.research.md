# Research brief: Compound interest, the snowball of acorns (posts Wed Oct 7, 2026)

Angle: evergreen. No single news hook needed; the timely tie-in is the latest Fed data on credit card rates (Q2 2026), showing compounding working against borrowers.

## Definition
- Compound interest: interest (or growth) is earned on the original amount AND on past interest. Formula (annual compounding): A = P x (1 + r)^t.
- Simple interest, for contrast: A = P x (1 + r x t).
- Rule of 72: years to double is roughly 72 / rate. At 7%: 72/7 = 10.3 years (exact: ln2/ln1.07 = 10.24 years).

## Worked example (hypothetical 7% a year, annual compounding, one-time $10,000, no additions, no taxes/fees)
Computed in Python:
- Year 1: 10,000 x 1.07 = $10,700 (adds $700)
- Year 10: $19,671.51
- Year 20: $38,696.84
- Year 30: $76,122.55
- Year 40: $149,744.58
- Growth in year 40 alone: 10,000 x 1.07^39 x 0.07 = $9,796.37
- Simple interest at 7% for 40 years, for contrast: 10,000 x (1 + 0.07 x 40) = $38,000
- Start at 25 (40 years to 65): $149,745. Start at 35 (30 years to 65): $76,123. The later start ends with 50.8% as much, i.e. about half (49.2% less).
- Surprising fact: the last 10 years (30 -> 40) add $73,622, about 49% of the final pile.

Chart series (same example, every 5 years, rounded to $):
| Year | Value |
|---|---|
| 0 | 10,000 |
| 5 | 14,026 |
| 10 | 19,672 |
| 15 | 27,590 |
| 20 | 38,697 |
| 25 | 54,274 |
| 30 | 76,123 |
| 35 | 106,766 |
| 40 | 149,745 |

## Real data
- US stocks long-run: the S&P 500 with dividends reinvested returned about 10% a year compounded from 1928 through 2025 (Aswath Damodaran, NYU Stern historical returns dataset; compilations cite 10.0% for 1928-2025, other cites range 9.8%-10.3% depending on end year). Includes deep down years (e.g., 1931, 2008). Past returns do not predict future returns.
- Inflation-adjusted: roughly 7% a year, 1928-2025 (per independent fact-check of Damodaran data). Past returns are not a promise.
- S&P 500 total return in 2025: 17.72% (price +16.39%, dividends 1.34%) per Damodaran, Data Update 2 for 2026 (January 2026).
- $100 invested in the S&P 500 in 1928 grew to roughly $1.16 million by end of 2025 (compilations of Damodaran data; not used on screen).
- Credit cards (compounding in reverse): Federal Reserve G.19, average interest rate on credit card accounts assessed interest: 22.15% in Q2 2026 (up from 21.52% in Q1 2026). All accounts: 20.94% in Q2 2026. Latest quarterly figure as of Sept 30, 2026 (G.19 released Sept 8, 2026; next quarterly rate update covers Q3).

## Surprising fact
In a steady-rate example, roughly half of a 40-year pile arrives in the final 10 years, so a 10-year-later start ends with about half.

SOURCES:
- Federal Reserve, G.19 Consumer Credit (Sept 8, 2026 release; Q2 2026 credit card rates): https://www.federalreserve.gov/releases/g19/ ; FRED TERMCBCCACINS/TERMCBCCALLNS; cross-check The Money Overview "Credit card accounts that were charged interest paid an average 22.15% rate in the second quarter"; tradingeconomics.
- Aswath Damodaran, NYU Stern, Historical Returns on Stocks, Bonds and Bills: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histretSP.html ; Data Update 2 for 2026 (Jan 2026): https://aswathdamodaran.substack.com/p/data-update-2-for-2026-a-testing ; FinanceWonk historical returns compilation: https://www.financewonk.com/references/historical-returns
- Worked example math: own calculation (Python), formula A = P(1+r)^t.
