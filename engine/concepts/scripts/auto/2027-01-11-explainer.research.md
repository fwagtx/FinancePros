# Research brief: The true hourly cost of a purchase (posts Mon Jan 11, 2027)

Evergreen explainer. No timely news hook needed; the latest wage figure is dated (October 2026) so it stays true on the posting date.
Note: the December 2026 jobs report is scheduled for Fri Jan 8, 2027, so by posting day a newer monthly figure will exist. Always say "in October 2026", never "latest" or "now".

## Key facts (confirmed)

1. **Average hourly earnings, all employees, total private (BLS CES, seasonally adjusted): $38.00 in October 2026.**
   BLS Employment Situation, October 2026: "In October, average hourly earnings for all employees on private nonfarm payrolls increased by 14 cents, or 0.4 percent, to $38.00."
   Source: https://www.bls.gov/news.release/empsit.nr0.htm (Employment Situation - October 2026). Earlier: September 2026 $37.81 (archive empsit_10022026).

2. **Chartable series: annual averages of average hourly earnings, all employees, total private (BLS series CEU0500000003, not seasonally adjusted, period M13 "Annual")**
   Retrieved from the BLS public API (via Firecrawl Alexandria bls-gov provider); series page https://data.bls.gov/timeseries/CEU0500000003

   | Year | Annual avg ($/hr) |
   |------|------|
   | 2016 | 25.64 |
   | 2017 | 26.32 |
   | 2018 | 27.11 |
   | 2019 | 27.99 |
   | 2020 | 29.35 |
   | 2021 | 30.60 |
   | 2022 | 32.26 |
   | 2023 | 33.72 |
   | 2024 | 35.06 |
   | 2025 | 36.45 |

   2016 to 2025: +42.2% nominal (our math: 36.45/25.64 - 1). Nominal, not inflation-adjusted.

3. **Mean travel time to work: 26.4 minutes (one way), US workers age 16+, ACS 5-year 2020-2024.**
   Source: US Census Bureau QuickFacts, https://www.census.gov/quickfacts/fact/table/US/LFE305224
   (Secondary reports cite 27.2 min for the 2024 1-year ACS; not confirmed on census.gov, so we use 26.4 from QuickFacts.)

4. **Surprising fact / attribution:** The "real hourly wage" idea comes from *Your Money or Your Life* by Vicki Robin and Joe Dominguez, first published 1992 (revised 2008 and 2018). They frame money as "life energy": subtract job-related costs from pay and add job-related hours (commuting, etc.), then divide, to see what an hour of your life really earns; then convert purchases into hours of life energy.
   Sources: Motley Fool (2018) https://www.fool.com/investing/2018/05/01/25-years-later-this-duo-is-still-inspiring-young-p.aspx ; Quartz https://qz.com/1738721/the-fire-movement-bible-that-wants-to-help-people-to-retire-early ; Get Rich Slowly https://www.getrichslowly.org/blog/2008/10/20/how-to-compute-your-real-hourly-wage/ ; Publishers Weekly listing https://www.publishersweekly.com/9780670843312

## Worked example (OUR MATH, illustrative assumptions)

Assumptions (stated on screen as "our math"):
- Pay: BLS average private hourly earnings, $38.00 (October 2026).
- Taxes: an illustrative flat 25% of gross for all taxes combined (income + payroll). This is NOT anyone's actual rate; real rates vary widely by income, state and filing status.
- Workday: 8 paid hours.
- Commute: 26.4 min each way (Census) = 52.8 min = 0.88 hour unpaid per workday.
- Purchase: $1,200 phone (round illustrative price, no brand).

Steps:
1. Sticker hours: $1,200 / $38.00 = 31.58 hours (about 32).
2. After tax: $38.00 x 0.75 = $28.50 per hour kept. $1,200 / $28.50 = 42.11 hours (about 42).
3. Add commute time: daily take-home = $28.50 x 8 = $228.00; daily time = 8 + 0.88 = 8.88 hours; real hourly wage = $228 / 8.88 = $25.68.
   $1,200 / $25.68 = 46.74 hours (about 47). More than a 40-hour work week.

Not included (could push it further, unsourced here): commuting money costs, work clothes, meals, childcare.

## Framing
- A tool for seeing prices in hours, not advice on whether to buy anything.
- Avoid claiming anyone's exact tax rate.

SOURCES:
- BLS, The Employment Situation - October 2026: https://www.bls.gov/news.release/empsit.nr0.htm
- BLS series CEU0500000003 (annual averages 2016-2025), BLS Public Data API: https://data.bls.gov/timeseries/CEU0500000003
- US Census Bureau QuickFacts, mean travel time to work 2020-2024: https://www.census.gov/quickfacts/fact/table/US/LFE305224
- Motley Fool on Your Money or Your Life (1992, Robin and Dominguez): https://www.fool.com/investing/2018/05/01/25-years-later-this-duo-is-still-inspiring-young-p.aspx
- Quartz: https://qz.com/1738721/the-fire-movement-bible-that-wants-to-help-people-to-retire-early
- Get Rich Slowly, real hourly wage: https://www.getrichslowly.org/blog/2008/10/20/how-to-compute-your-real-hourly-wage/
