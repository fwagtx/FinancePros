# Research brief: How car loans quietly cost thousands (2026-10-11 explainer)

Researched Wednesday, September 30, 2026. Note: direct fetches of experian.com, experianplc.com, bankrate.com, fred.stlouisfed.org and autoremarketing.com were blocked by the network proxy; figures below are confirmed through multiple search results quoting the official Experian report / Fed release.

## News angle
No single breaking event. Timely peg: Experian's State of the Automotive Finance Market, Q2 2026 (latest available; press release "New Experian Automotive report shows nearly one-third of automotive loan terms are longer than six years", 2026). Loans keep getting bigger and longer.

## Key facts (Experian, State of the Automotive Finance Market, Q2 2026)
- Average new-car loan amount: $43,610. Used: $27,852.
- Average rate: 6.35% new, 11.19% used.
- Average term: 69.5 months new, 67.9 months used.
- Average monthly payment: $765 new, $542 used.
- More than 35% of new-vehicle loans and 31% of used loans had terms longer than six years (press release headline: "nearly one-third of automotive loan terms are longer than six years").
- Average new-car rate by credit tier (Q2 2026): super prime (781-850) 4.41%; prime (661-780) 6.15%; near prime (601-660) 9.71%; subprime (501-600) 13.52%; deep subprime (300-500) 16.11%.
- Used by tier: 6.29% / 8.81% / 13.93% / 19.10% / 21.62%.

## Cross-check / context
- Edmunds: average new-car APR about 7% for July 2026; Q1 2026 average new amount financed $43,899 at 6.9% APR over 70 months, $773/month (Edmunds methodology differs from Experian; not used on screen).
- Federal Reserve G.19: 60-month new-car loan rate at commercial banks 7.52% (Jan and Feb 2026), 7.14% (Q2 2026 reading).

## Chartable data series (Experian, average new-vehicle monthly payment, Q2 of each year)
| Q2 year | Avg new payment |
|---|---|
| 2023 | $725 (one source says Q2 2022 was $625, another implies ~$650; 2023 figure itself reported consistently as $725) |
| 2024 | $734 (some sources round to $735) |
| 2025 | $749 |
| 2026 | $765 |
Source: Experian State of the Automotive Finance Market Q2 reports, via search results. Weakly sourced for 2023-2024 exact dollars; not used on screen in the script.

## Worked example (exact math, standard amortization)
Assumptions (labeled example): the Q2 2026 average new loan, $43,610, at the Q2 2026 average new rate 6.35%, fixed, no fees, payment = P*i/(1-(1+i)^-n), i = 6.35%/12.
- 72 months: payment $729.97 (~$730); total paid $52,557.87; interest $8,947.87 (~$8,948).
- 84 months: payment $644.42; total paid $54,131.42; interest $10,521.42 (~$10,521).
  - Payment drops $85.55 (~$86/month); interest rises $1,573.55 (~$1,600 more).
- 60 months: $850.22/month, interest $7,403.14. 48 months: $1,031.19/month, interest $5,887.35.
- Same $43,610 over 72 months by credit tier:
  - 4.41% (super prime): $690.46/month, interest $6,103.37 (~$6,100)
  - 13.52% (subprime): $887.45/month, interest $20,286.10 (~$20,300)
  - Gap: about $14,183.

## The surprising fact
Stretching the loan lowers the monthly payment but raises the total interest; and more than 35% of new-car loans in Q2 2026 were longer than six years. On the example loan, going from 72 to 84 months saves $86 a month but costs about $1,600 more in interest.

SOURCES:
- Experian, State of the Automotive Finance Market Q2 2026 (via Experian Ask Experian "Average Car Loan Interest Rates by Credit Score", "Average Car Payment in 2026", "Auto Loan Rates and Financing for 2026"): https://www.experian.com/blogs/ask-experian/average-car-loan-interest-rates-by-credit-score/ ; https://www.experian.com/blogs/ask-experian/average-car-payment/
- Experian press release (2026): "New Experian Automotive report shows nearly one-third of automotive loan terms are longer than six years": https://www.experianplc.com/newsroom/press-releases/2026/new-experian-automotive-report-shows-nearly-one-third-of-automot
- Auto Remarketing, "Experian sees refinancing continue to ripen in Q2": https://www.autoremarketing.com/subprime/experian-sees-refinancing-continue-to-ripen-in-q2
- Bankrate / Yahoo Finance, "Average auto loan interest rates by credit score in 2026" (quotes Experian Q2 2026)
- Edmunds (via Autoblog, briefglance): Q1 2026 new-vehicle financing figures
- Federal Reserve G.19 Consumer Credit, RIFLPBCIANM60NM (via FRED/ALFRED search results)
- Experian Q2 2024/Q2 2025 reports (payment history series), via search results
