# 2026-12-13-explainer research brief: How a traditional (pre-tax) 401(k) works, paycheck mechanics
Researched October 14, 2026. Evergreen; no news hook needed. Angle: pre-tax money leaves the paycheck before income tax, so take-home falls by less than the amount saved; FICA still applies; taxed later on withdrawal; 10% early-withdrawal additional tax before 59 1/2.
Avoided (already covered): match math, auto-enrollment rates, target-date funds, contribution-limit history, Roth IRA how-to, 401(k) vs IRA limits.

## Core rules (IRS)
- Traditional (pre-tax) 401(k) elective deferrals are NOT treated as current income for federal income tax, but ARE included as wages for Social Security, Medicare and FUTA. (IRS 401(k) Plan Overview; IRS Retirement Plan FAQ on withholding: pre-tax deferrals = FICA/Medicare yes, federal income tax withholding no; W-2: excluded from Box 1, included in Boxes 3 and 5.)
- Roth 401(k) deferrals are subject to both income tax and FICA (same IRS FAQ). Employer match is subject to neither when contributed.
- Pre-tax deferrals and earnings are taxed as ordinary income when withdrawn (IRS 401(k) Plan Overview / distributions pages).
- Early distributions before age 59 1/2: 10% additional tax on the taxable portion, on top of regular income tax, unless an exception applies (IRS Topic 558; Retirement Topics - Exceptions to Tax on Early Distributions; Pub 5036).
  - Main plan exceptions: death, disability, substantially equal periodic payments (after separation), separation from service in or after the year you turn 55 (50 for qualified public safety workers), certain medical expenses; SECURE 2.0 added optional emergency personal expense and domestic abuse victim distributions (Journal of Accountancy, Jun 2024).

## 2026 numbers
- 2026 federal brackets, single (IRS Rev. Proc. 2025-32, announced Oct 9, 2025; KPMG, Journal of Accountancy): 10% to $12,400; 12% to $50,400; 22% $50,400-$105,700; 24% to $201,775; 32% to $256,225; 35% to $640,600; 37% above. Standard deduction single $16,100.
- FICA employee rates 2026: Social Security 6.2% up to $184,500 wage base (SSA, Oct 2025); Medicare 1.45% no cap; +0.9% Additional Medicare over $200,000 single. Combined 7.65% below the wage base.

## Worked example (EXAMPLE, assumptions stated)
Assumptions: single filer whose taxable income stays inside the 22% federal bracket (2026: $50,400-$105,700 taxable), paid every two weeks (26 paychecks), wages below the SS wage base, state/local income tax ignored, traditional pre-tax 401(k).
- Save $100 pre-tax per paycheck: federal income tax falls by 22% x $100 = $22. Take-home falls by $100 - $22 = $78.
- FICA still applies to that $100: 7.65% x $100 = $7.65 (6.20 SS + 1.45 Medicare). It is owed whether or not you contribute, so it does not change the $78 figure.
- Same $100 saved after tax (e.g., to a Roth 401(k) or savings): take-home falls the full $100.
- Per year: 26 x $100 = $2,600 contributed; 26 x $78 = $2,028 less take-home; 26 x $22 = $572 less federal income tax for 2026.
- Later: withdrawals are taxed as ordinary income at whatever rate applies then. Before 59 1/2, generally +10% additional tax unless an exception applies.

### Take-home drop per $100 pre-tax, by 2026 federal bracket (derived from IRS rates; chartable)
x = federal bracket %, y = take-home drop in $: [10, 90], [12, 88], [22, 78], [24, 76], [32, 68], [35, 65], [37, 63]  (ignores state tax; FICA unchanged)

## Chartable real data series (Vanguard How America Saves)
- Average employee deferral rate: 2023 7.4% (HAS 2024); 2025 7.6% (HAS 2026, June 2026; median 6.6%; 2025 figures are Vanguard estimates). 2024 roughly 7.6-7.7% (sources conflict; not used on screen). 2021 7.3%.
- Total (employee + employer) average contribution rate 2025: 12.1% (median 11.6%).
- Average balance Dec 31, 2025: about $167,970 (sources differ by $10).
Not used in the script because the year-by-year series is incomplete/conflicting.

## The surprising fact
Putting $100 into a traditional 401(k) doesn't cost $100 of take-home pay: in the 22% bracket it costs $78, because the income tax on it is deferred. But Social Security and Medicare tax are still taken on it.

SOURCES:
- IRS, 401(k) Plan Overview: https://www.irs.gov/retirement-plans/plan-participant-employee/401k-resource-guide-plan-participants-401k-plan-overview
- IRS, Retirement plan FAQs: are contributions subject to FICA/Medicare/federal income tax withholding: https://www.irs.gov/retirement-plans/retirement-plan-faqs-regarding-contributions-are-retirement-plan-contributions-subject-to-withholding-for-fica-medicare-or-federal-income-tax
- IRS Topic 558, Additional tax on early distributions from retirement plans other than IRAs: https://www.irs.gov/taxtopics/tc558
- IRS, Retirement Topics - Exceptions to Tax on Early Distributions: https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-exceptions-to-tax-on-early-distributions
- IRS Pub 5036 (Form 5329 exception table): https://www.irs.gov/pub/irs-pdf/p5036.pdf
- Journal of Accountancy, Jun 2024, early-distribution exceptions: https://www.journalofaccountancy.com/news/2024/jun/exceptions-to-penalty-on-early-retirement-plan-distributions-outlined/
- IRS Rev. Proc. 2025-32 via KPMG: https://kpmg.com/us/en/taxnewsflash/news/2025/10/tnf-rev-proc-2025-32-inflation-adjustments-for-2026-individual-taxpayers.html and Journal of Accountancy Oct 2025: https://www.journalofaccountancy.com/news/2025/oct/annual-inflation-adjustments-announced-for-tax-year-2026/
- SSA 2026 wage base $184,500 via WICPA/TSCPA: https://www.wicpa.org/news/articles/2845:social-security-wage-base-cola-announced-for-2026
- Vanguard How America Saves 2026 via NAPA (Jun 2026): https://www.napa-net.org/news/2026/6/plan-design-drives-record-retirement-participation-better-outcomes-vanguard/ and PLANSPONSOR
