# Research brief: How mortgage interest works in the first years
Prepared Wednesday, September 30, 2026. Posts Monday, October 5, 2026 (evergreen wording; every number dated).

## Timely angle
- Freddie Mac PMMS, week of September 24, 2026: the 30-year fixed averaged **7.03%**, up from 6.95% the week before; a year earlier it averaged 6.30%. The 15-year fixed averaged 6.42% (6.26% prior week; 5.49% a year earlier). (Freddie Mac release "Mortgage Rates Average 7.03%", Sept 24, 2026)
- First time the 30-year average passed 7% since January 2025 (about 20 months). (Fox Business, NPR, Sept 24, 2026; Freddie Mac PMMS Jan 16, 2025 was 7.04%)
- Note: Freddie Mac publishes a new weekly number on Thursday, October 1, 2026, before posting. Always say "as of September 24, 2026" / "in late September 2026".

## Chartable real data series: Freddie Mac PMMS 30-year fixed, weekly (2026)
| Week of | Rate |
|---|---|
| Aug 27, 2026 | 6.66% |
| Sep 3, 2026 | 6.71% |
| Sep 10, 2026 | 6.76% |
| Sep 17, 2026 | 6.95% |
| Sep 24, 2026 | 7.03% |
Sources: Freddie Mac releases "Mortgage Rates Average 6.71%" (Sep 3, 2026: prior week 6.66%), "6.95%" (Sep 17: prior week 6.76%), "7.03%" (Sep 24).

## How it works (definitions, stable)
- A fixed-rate mortgage has the same monthly principal-and-interest payment for the whole term (amortizing loan).
- Each month's interest = remaining balance x (annual rate / 12). Whatever is left of the payment pays down principal. (CFPB, "How does paying down a mortgage work?"; standard amortization formula)
- Early on the balance is highest, so interest takes most of the payment; as the balance falls, the principal share rises. The monthly payment does not change.
- Payment formula: M = P x i / (1 - (1+i)^-n), i = monthly rate, n = number of months.
- Extra principal payments lower the balance that future interest is charged on (CFPB). Education only; not advice.

## Worked example (exact math, hypothetical)
Loan $400,000, 30 years (360 payments), 7.03% fixed (the Sept 24, 2026 PMMS average). Principal and interest only (no taxes/insurance).
- i = 0.0703 / 12 = 0.0058583
- M = 400,000 x 0.0058583 / (1 - 1.0058583^-360) = **$2,669.27/month**
- Payment 1: interest = 400,000 x 0.0703 / 12 = **$2,343.33**; principal = 2,669.27 - 2,343.33 = **$325.94**. Interest share = **87.8%**.
- Year 1: paid 12 x 2,669.27 = **$32,031**; interest **$27,991**; principal **$4,040**; balance **$395,960**.
- After 5 years: interest paid $136,803; principal $23,353; balance **$376,647**.
- After 10 years: interest $263,804; principal $56,509; balance $343,491.
- Principal first exceeds interest in payment **#243** (year 21).
- Total interest over 30 years: **$560,939** (more than the $400,000 borrowed).
- Extra $100/month toward principal from month 1: loan ends in 321 months (39 months sooner), total interest $487,518, **saves about $73,421**.

Interest share of the payment, first payment of each year (computed, same loan):
Y1 87.8, Y2 86.9, Y3 86.0, Y4 84.9, Y5 83.8, Y6 82.7, Y7 81.4, Y8 80.1, Y9 78.6, Y10 77.1, Y11 75.4, Y12 73.6, Y13 71.7, Y14 69.6, Y15 67.4, Y16 65.1, Y17 62.5, Y18 59.8, Y19 56.9, Y20 53.7, Y21 50.4, Y22 46.8, Y23 42.9, Y24 38.8, Y25 34.3, Y26 29.6, Y27 24.5, Y28 19.0, Y29 13.1, Y30 6.8

## The surprising fact
At 7.03%, about 88% of the first payment is interest. After a full year of $32,031 in payments, the balance drops only about $4,040. Principal doesn't overtake interest until year 21.

SOURCES:
- Freddie Mac, Primary Mortgage Market Survey release "Mortgage Rates Average 7.03%", Sept 24, 2026 (freddiemac.gcs-web.com; also GlobeNewswire / Yahoo Finance)
- Freddie Mac PMMS releases "Mortgage Rates Average 6.95%" (Sept 17, 2026) and "Mortgage Rates Average 6.71%" (Sept 3, 2026)
- Fox Business, "Mortgage rates rise to 7.03%: Freddie Mac", Sept 24, 2026; NPR, "Mortgage rates have just surpassed 7% for the first time in well over a year", Sept 24, 2026
- CFPB, "How does paying down a mortgage work?" (consumerfinance.gov/ask-cfpb/how-does-paying-down-a-mortgage-work-en-1943/): early on most of the payment goes to interest because the balance is high; over time more goes to principal. Also notes some loans carry prepayment penalties (limited to the first 3 years where allowed).
- Worked example: standard amortization formula, computed in Python (values above)
