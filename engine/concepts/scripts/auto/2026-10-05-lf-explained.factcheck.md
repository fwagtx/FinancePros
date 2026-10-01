# Fact-check: 2026-10-05-lf-explained ("How the rich pay less tax", long-form)
Checked Oct 1, 2026 for posting on Oct 5, 2026. I used 14 web searches and recomputed all the math in Python. Line numbers are 1-based indexes into `lines`.

## Verified correct
- **Forbes 400, published Sept 15, 2026 (L3-4):** combined worth $8T, up from $6.6T in 2025. The cutoff is a record $4.4B. Source: the Forbes facts-and-figures page and the Forbes press release.
- **2026 tax numbers from Rev. Proc. 2025-32 (L25-28, 35, 78):**
  - Single-filer brackets: 10% to $12,400, 12% to $50,400, 22% to $105,700, 24% to $201,775, 32% to $256,225, 35% to $640,600, and 37% above that.
  - Standard deduction: $16,100.
  - Long-term gains rates: 0% up to $49,450 and 15% up to $545,500.
- **Taxes on top of the brackets (L29-32):**
  - The 3.8% NIIT starts at $200,000 for single filers, and that line isn't indexed for inflation.
  - The Additional Medicare Tax of 0.9% applies to wages over $200,000.
  - Employee payroll rates are 6.2% for Social Security and 1.45% for Medicare.
- **Social Security wage base for 2026 (L33):** $184,500.
- **Worked example, recomputed:**
  - At $100K: the worker owes $13,170 in income tax plus $7,650 in payroll tax, for $20,820 (20.8%). The investor owes $5,167.50 (5.2%). The investor's share of the worker's bill is 24.8%, so "about a quarter" holds.
  - At $1M: the worker owes $320,000.25 in income tax plus $33,139 in payroll tax, for $353,139.25 (35.3%). The investor owes $74,407.50 + $87,680 + $30,400 in NIIT (3.8% of $800K), for $192,487.50 (19.2%).
  - Top marginal rates: 37 + 1.45 + 0.9 = 39.35% on wages, and 20 + 3.8 = 23.8% on long-term gains.
  - Buy, borrow, die: $9M x 23.8% = $2,142,000. $900K x 23.8% = $214,200. $1M x 6% = $60,000. Gifts: 2 parents x 3 kids x $19,000 = $114,000.
- **History (L19-20):** the 1913 start date is correct. The Revenue Act of 1921 set a 12.5% rate for gains on assets held over two years, and it set the basis of inherited property at its value at death.
- **Moore v. United States, June 20, 2024 (L21, 90):** the Court expressly left open whether income has to be realized before it can be taxed.
- **Top-rate chart (L45-47):** every point matches the Tax Policy Center series: 70, 50, 38.5, 28, 31, 39.6, 39.1, 38.6, 35, 39.6, 37. The top gains rate was also 28% in 1988-90. The OBBBA was signed July 4, 2025 and made the 37% rate permanent.
- **JCT JCX-45-25 (L64):** the step-up costs $72.5B in FY2026 (CRFB rounds this to $73B).
- **Estate and gift (L68-71):** the exemption is $15M per person and $30M per couple, made permanent by the OBBBA and indexed after 2026. The annual gift exclusion is $19,000.
- **QSBS (L74-75):** for stock acquired after July 4, 2025, the excluded gain is capped at $15M or 10x basis, whichever is greater. The exclusion is tiered at 50%, 75% and 100% after 3, 4 and 5 years.
- **Retirement limits for 2026 (L77):** $24,500 for a 401(k) and $7,500 for an IRA. Source: IRS, Nov 13, 2025.
- **The two studies (L83, 85-86):**
  - White House CEA and OMB, Sept 23, 2021: 8.2% for the 400 wealthiest families over 2010-2018.
  - ProPublica, June 8, 2021: the 25 richest gained $401B in 2014-2018, paid $13.6B in federal income tax, a "true tax rate" of 3.4%.
- **The Tax Foundation critique (L87-88):** this is accurate. Erica York said the study "creates a new definition of income... but only applies that new measure of income to the top 400," and that it leaves out corporate income tax.

## Issues
1. **L98, on-screen value differs from spoken.** The right-hand value is "$5,168", but the narration says $5,167.50. L39, L40 and the YouTube description all use $5,167.50. Fix: set the scene value to "$5,167.50".
2. **L6 mischaracterizes ProPublica.** ProPublica did not count unsold gains as *income*. It divided tax paid by the *growth in wealth*, and it said outright that those gains aren't taxable income. Fix: "But both measure tax against gains nobody sold. Under the normal rules, those gains aren't income yet." Change the board in the same way: "Both studies count unsold gains. The tax code doesn't."
3. **L7 overclaims.** "That one difference is the whole story" is contradicted by L88, where the corporate tax that was left out is a second difference. Fix: "That difference drives most of the gap."
4. **Neutrality and balance in Ch. 5 (L84, L87-88).** Critics get the last word on both studies, and the studies' side never answers. Add one line, for example: "Supporters of the studies say unsold gains are real economic income, a definition many economists use." With that line, L84 also reads as the method rather than a rebuttal. L89-90 and L100 are balanced and neutral as written. L99 ("None of it is a secret loophole") is acceptable because it is factual.
5. **L44 and L95, minor.** "39.35%" is the employee's share only, since the employer pays another 1.45%. Consider changing the sub-label to "employee side: 37 + 1.45 + 0.9".
6. **L17, minor.** The on-screen list includes "No salary to speak of", but the narration never mentions salary. Fix: "If they take little salary, the company pays no dividend, and they don't sell, there's no income to tax."
7. **L1 hook, minor.** It is true and specific enough, but at 11 words it runs about 3.3 seconds, and "a stock fortune" is abstract. A stronger option: "Billionaires can get richer for decades and owe zero income tax." Optional.

## Other checks
- **Advice and predictions:** none.
- **Hypotheticals:** they are labeled ("made-up example", "assumed 6%").
- **Quotes and data:** quoted wording is accurate. No company's numbers are generalized to an industry.
- **Time words:** "September 2026" and the 2026 figures are all current on Oct 5. Nothing is stale.
- **Cover and title:** the "Zero Tax For Decades?" cover is paid off in L13-15 and L51-62.

Issue 1 is a mismatch between an on-screen number and the spoken one. That is a one-line fix, and I recommend fixing issues 2-4 at the same time.

VERDICT: FAIL
