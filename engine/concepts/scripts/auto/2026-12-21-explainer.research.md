# Research brief: Why negotiating your salary pays acorns for decades
Slot: 2026-12-21-explainer (Acorn Economics, posts Mon Dec 21, 2026, 12 PM CT). Evergreen; no timely news hook needed.

## Key facts (confirmed)
1. Pew Research Center survey, published April 5, 2023 (5,775 U.S. adults incl. 5,188 employed, not self-employed):
   - Most U.S. workers say they did NOT ask for higher pay than first offered the last time they were hired.
   - Asked for more: men 32%, women 28%.
   - Among those who asked: 28% got what they asked for; 38% got more than first offered but less than asked; 35% got only the original offer.
     => 66% of askers got more than the first offer (28 + 38; derived, consistent with Pew's numbers).
   - Of those who didn't ask: 39% satisfied with the offer; 38% didn't feel comfortable asking.
2. Fidelity Investments survey, 2022 (Engine Insights, March 8-14, 2022; 1,524 U.S. working adults 25-70): 85% of Americans who countered on salary and/or benefits got at least some of what they asked for (87% of ages 25-35). Reported by CNBC May 13, 2022. Covers pay OR benefits, "at least some". Dated (2022).
3. BLS (Current Population Survey, "Usual Weekly Earnings"): median weekly earnings of full-time wage and salary workers were $1,251 in Q2 2026 (not seasonally adjusted), up 4.6% from a year earlier vs. CPI-U up 3.9% (release July 21, 2026). Q3 2026 release expected around early Dec 2026 — say "Q2 2026" explicitly.

## Real chartable series: BLS median usual weekly earnings, full-time wage & salary workers, annual averages
| Year | Median weekly |
|---|---|
| 2019 | $917 |
| 2020 | $984 |
| 2023 | $1,117 |
| 2024 | $1,159 |
| 2025 | $1,204 (11-month avg; Oct 2025 not collected due to shutdown) |
| Q2 2026 | $1,251 (quarterly, NSA) |
(2021/2022 values not confirmed in this research; do not chart them.)

## Worked example (hypothetical, labeled as an example)
Assumptions: two identical workers; offer A $60,000, offer B $65,000 after negotiating (+$5,000); both get 3% raises every year; 30 years; pre-tax; no promotions/job changes.
- Salary in year n = start x 1.03^(n-1).
- Year 1: $60,000 vs $65,000 -> gap $5,000.
- Year 10: $78,286 vs $84,810 -> gap $6,524.
- Year 20: $105,210 vs $113,978 -> gap $8,768.
- Year 30: $141,394 vs $153,177 -> gap $11,783 (= 5,000 x 1.03^29 = 5,000 x 2.3566).
- Total 30-year gap = 5,000 x (1.03^30 - 1)/0.03 = 5,000 x 47.575 = **$237,877** (pre-tax).
- Retirement add-on (example): if 10% of each year's gap goes into a 401(k) (5% from the worker + 5% employer match) and grows 6% a year (assumption), the extra balance after 30 years = **about $55,270** (end-of-year contributions; computed in Python).
- Chartable example series (yearly gap, $): Y1 5,000; Y5 5,628; Y9 6,334; Y13 7,129; Y17 8,024; Y21 9,031; Y25 10,164; Y29 11,440; Y30 11,783.

## Surprising fact
A one-time $5,000 difference isn't $5,000 — with 3% raises it becomes about $11,783 a year by year 30 and about $237,877 in total, because every raise is a percentage of the bigger base. Yet most workers (Pew 2023) didn't ask, and two-thirds of those who did got more.

## Weakly sourced / not used
- Babcock & Laschever ("Women Don't Ask", 2003) "$500,000+ by age 60" — only secondary paraphrases of a hypothetical; exact calculation not confirmed. NOT used.
- Glassdoor/Fishbowl "54% didn't negotiate" — non-representative panel. NOT used.

SOURCES:
- Pew Research Center, "When negotiating starting salaries, most U.S. women and men don't ask for higher pay," April 5, 2023: https://www.pewresearch.org/short-reads/2023/04/05/when-negotiating-starting-salaries-most-us-women-and-men-dont-ask-for-higher-pay/
- CNBC, "85% of Americans who negotiated a job offer were successful," May 13, 2022 (Fidelity survey): https://www.cnbc.com/2022/05/13/85-percent-of-americans-who-negtiated-a-job-offer-were-successful.html
- Fidelity, "How to negotiate salary": https://fidelity.com/learning-center/smart-money/how-to-negotiate-salary
- BLS, Usual Weekly Earnings Q2 2026 (July 21, 2026): https://www.bls.gov/news.release/archives/wkyeng_07212026.htm
- BLS TED, "Median weekly earnings were $1,204 in 2025": https://www.bls.gov/opub/ted/2026/median-weekly-earnings-were-1204-in-2025.htm
- BLS annual averages tables (cpsaat54/55, 2019, 2020, 2023): https://www.bls.gov/cps/data/aa2023/cpsaat55.pdf ; https://www.bls.gov/cps/aa2019/cpsaat54.pdf
- BLS Usual Weekly Earnings Q4 2025 / annual 2024 (Jan 28, 2026): https://www.bls.gov/news.release/archives/wkyeng_01282026.htm
- Worked example: own calculation (Python), assumptions stated above.
