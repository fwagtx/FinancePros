# 2026-12-07-explainer research brief: Present bias, why future you always gets the bill

Evergreen (posts Mon Dec 7, 2026). No news hook needed; all facts are published academic studies whose results do not change.

## Definition
- Present bias: people give "right now" extra weight compared with any later time, so the same trade-off (wait a bit for more) looks different depending on whether the wait starts now or later. Result: preference reversals, plans made for "later" get broken when later becomes now.
- David Laibson, "Golden Eggs and Hyperbolic Discounting," Quarterly Journal of Economics 112(2):443-477 (1997). Popularized the quasi-hyperbolic "beta-delta" model in economics: today gets full weight, every future period gets an extra discount (beta < 1) on top of ordinary discounting (delta). Predicts people value commitment devices (illiquid savings) and that consumption tracks income. (Form dates back to Phelps & Pollak 1968; say "modeled/popularized", not "invented".)

## Key study 1 (the surprising number): Thaler 1981
- Richard Thaler, "Some Empirical Evidence on Dynamic Inconsistency," Economics Letters 8(3):201-207 (1981).
- Survey question: how much would you need in 1 month / 1 year / 10 years to be as good as $15 now?
- Median answers: $20 (1 month), $50 (1 year), $100 (10 years).
- Implied annual (continuously compounded) discount rates: about 345% (1 month), 120% (1 year), 19% (10 years).
- My check of the math: 12 x ln(20/15) = 3.45 -> 345%; ln(50/15) = 1.20 -> 120%; ln(100/15)/10 = 0.19 -> 19%. Matches.
- Simple math: $15 -> $20 is a 33% premium for waiting one month.
- Caveat: small hypothetical-money survey (University of Oregon students, from memory, not verified); report as "median answer in a 1981 survey".
- Surprising fact: the shorter the wait, the steeper the implied rate. Waiting is most "expensive" when it starts now.

## Key study 2: Hershfield et al. 2011 (future self)
- Hershfield, Goldstein, Sharpe, Fox, Yeykelis, Carstensen & Bailenson, "Increasing Saving Behavior Through Age-Progressed Renderings of the Future Self," Journal of Marketing Research 48(SPL):S23-S37 (2011).
- Method: participants saw digitally aged avatars of their own face (some in virtual reality) vs current-age avatars; then made hypothetical allocation decisions.
- Results (per NYU Stern summary): in one experiment, those who saw aged photos were willing to put about twice as much of a hypothetical $1,000 windfall into a long-term/retirement account; working-age adults (18-35, online) allocated about 33% more of a hypothetical paycheck to retirement.
- Caveats: hypothetical money; DOL CLEAR notes the first (undergrad) study's effect was not statistically significant. Exact dollar amounts ($170 vs $80) only from a blog, NOT used.

## Key study 3 (chartable series): Thaler & Benartzi 2004, Save More Tomorrow (SMarT)
- Thaler & Benartzi, "Save More Tomorrow: Using Behavioral Economics to Increase Employee Saving," Journal of Political Economy 112(S1):S164-S187 (2004).
- Design: employees at one unnamed mid-size US manufacturer pre-commit to raise 401(k) contribution rates at each future pay raise (cost lands later, not from today's pay).
- SMarT joiners' average savings rate (% of pay):
  - month 0 (start): 3.5%
  - about 14 months: 9.4% (Thaler, Senate JEC testimony, Mar 10 2004)
  - 28 months (after 3 raises): 11.6% (earlier report of same site)
  - 40 months (4th raise): 13.6% (JPE 2004 abstract)
- Firm-wide average rose 4.4% -> 10.6%.
- Caveat: DOL CLEAR rates causal evidence "low" (joiners vs non-joiners, self-selection). Describe as "at one company, joiners' savings rate went from 3.5% to 13.6% in 40 months". Led to auto-escalation in the Pension Protection Act of 2006 (Wharton BCFG).

## Worked example (labeled hypothetical, textbook illustration)
- $100 today vs $110 in one week: many pick $100 now. Same choice pushed out a year ($100 in 52 weeks vs $110 in 53 weeks): many pick $110. Same 7-day wait, same $10, opposite answer. That flip is present bias.
- Math: $10/$100 = 10% for one week.

## Chartable data series
SMarT joiners' savings rate by month: [[0,3.5],[14,9.4],[28,11.6],[40,13.6]] (%). Sources: Thaler & Benartzi 2004 JPE; Thaler JEC testimony 2004.

SOURCES:
- Thaler, R. (1981). Some empirical evidence on dynamic inconsistency. Economics Letters 8(3):201-207. Figures via lecture slides/summaries (moodle2.units.it "discounted values"; MIT OCW 14.13 lec16).
- Laibson, D. (1997). Golden Eggs and Hyperbolic Discounting. QJE 112(2):443-477. https://scholar.harvard.edu/sites/scholar.harvard.edu/files/laibson/files/golden_eggs_and_hyperbolic_discounting.pdf
- Thaler, R. & Benartzi, S. (2004). Save More Tomorrow. JPE 112(S1):S164-S187. https://www.chicagobooth.edu/research/rustandy/social-impact-research/research-papers/2004/save-more-tomorrow-using-behavioral-economics-to-increase-employee-saving
- Thaler testimony, US Senate Joint Economic Committee, Mar 10 2004. https://www.jec.senate.gov/archive/Documents/Hearings/thalertestimony10march2004.pdf
- DOL CLEAR reviews of Thaler & Benartzi 2004 and Hershfield et al. 2011. https://clear.dol.gov
- Hershfield et al. (2011). JMR 48(SPL):S23-S37. NYU Stern summary: https://www.stern.nyu.edu/experience-stern/faculty-research/hershfield-retirement-savings
- Wharton BCFG on SMarT and Pension Protection Act 2006. https://bcfg.wharton.upenn.edu/newsletter-may-2019/
