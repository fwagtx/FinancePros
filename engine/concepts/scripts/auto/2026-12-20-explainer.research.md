# Research brief: Tax extensions: more time to file, not more time to pay
Slot 2026-12-20-explainer. Researched Oct 21, 2026; posts Sunday Dec 20, 2026. Evergreen; every figure dated.
Note: irs.gov blocks direct fetch from this environment; IRS rules confirmed via search results quoting IRS pages/news releases, cross-checked with secondary sources.

## Key dates (2026 tax year)
- 2026 individual federal returns (Form 1040) are due Thursday, April 15, 2027 (Reed Reports 2026-2027 due-date guide; National Taxpayer Advocate tax calendar). Verified calendar: Apr 15, 2027 is a Thursday, so no weekend shift.
- With an extension, the filing deadline is Friday, October 15, 2027 (Reed Reports; Taxpayer Advocate calendar: Oct 15 is the due date for individuals who requested an extension).
- Disaster-area and combat-zone relief can move deadlines (IRS).

## The core rule
- Form 4868 gives an automatic 6-month extension of time to FILE (April 15 -> October 15). IRS: "an extension to file is not an extension to pay taxes" (IRS news release/Tax Tip titles: "Taxpayers should know that an extension to file is not an extension to pay taxes"; "Taxpayers: Remember, an extension to file is not an extension to pay taxes", IR-2023-84, Tax Tips 2023-30 / 2024-30).
- Tax owed is still due by the original deadline; interest and the failure-to-pay penalty run on any unpaid balance from the original due date (IRS).
- Ways to request: file Form 4868 (paper or e-file, incl. IRS Free File), or make an electronic payment (IRS Direct Pay, EFTPS, debit/credit card) and select "extension"/Form 4868 as the payment type; the IRS then processes it as an extension automatically, no separate form needed (IRS news releases; NerdWallet 2026).
- Form 4868 requires a good-faith estimate of tax owed; an improper estimate can void the extension (secondary summaries of form instructions).

## Penalties (IRS "Failure to file penalty" and "Failure to pay penalty" pages)
- Failure-to-file: 5% of unpaid tax per month or part of a month the return is late, max 25%.
- Failure-to-pay: 0.5% of unpaid tax per month or part of a month, max 25%. Rises to 1%/month 10 days after a final notice of intent to levy; drops to 0.25%/month while an approved installment agreement is in effect (if return filed on time).
- When both apply in the same month: combined 5% per month (4.5% late filing + 0.5% late payment). Overall ceiling 47.5% (22.5% filing + 25% payment).
- IRS: "in most cases, the failure-to-file penalty is 10 times more than the failure-to-pay penalty" (5% vs 0.5%). IRS says if you can't pay in full, file and pay as much as you can.
- Minimum failure-to-file penalty for returns more than 60 days late: the smaller of $525 (for returns required to be filed in 2026) or 100% of the tax owed. The 2027 figure is inflation-adjusted and not confirmed; not used in script.
- Penalties/interest apply only to the unpaid amount (IRS; secondary).

## 90% rule (WEAKLY SOURCED - not used in script)
- Form 4868 instructions (1998 version; TurboTax community quoting current instructions): the late-payment penalty is generally not charged for the extension period if at least 90% of the actual tax was paid by the regular due date (withholding, estimates, or with 4868) and the rest is paid with the return by the extended date. Not confirmed from a current IRS page in this session.

## Interest
- IRS individual underpayment rate: federal short-term rate + 3 points, set quarterly, compounded daily.
- Q4 2026 (Oct 1-Dec 31, 2026): 7% (IR-2026-98, Aug 21, 2026; Rev. Rul. 2026-15). Q1 2027 rate not yet announced as of Oct 21, 2026 - so the script says "7% as of late 2026".

## Chartable data series: IRS individual underpayment interest rate, first quarter of each year
- Q1 2021: 3% (from knowledge; Manhattan Institute says 3% in 2022 era)
- Q1 2022: 3% (Manhattan Institute: "3% in 2022")
- Q1 2023: 7% (implied by Q4 2023 increase of 1 point to 8%; IR-2022-178 from knowledge; weakly confirmed)
- Q1 2024: 8% (IR-2023-219)
- Q1 2025: 7% (IR-2024-290)
- Q1 2026: 7% (IRS quarterly interest rates page)
- Also: Q2 2026 6%, Q3 2026 7%, Q4 2026 7% (IRS; IR-2026-98). 8% from Q4 2023 through Q4 2024.

## Worked example (hypothetical, labeled)
Assumptions: owes $4,000 for tax year 2026, pays nothing by April 15, 2027, files and pays everything exactly 5 months late (Sept 15, 2027). Interest (7% as of late 2026, rate can change) applies in both cases and is excluded.
- No extension: combined 5%/month x 5 months = 25% x $4,000 = $1,000 in penalties ($900 late-filing at 4.5% x 5 = 22.5%, + $100 late-payment at 0.5% x 5 = 2.5%). $900 exceeds the $525 minimum, so the minimum doesn't change it.
- Extension filed by April 15: no late-filing penalty (filed before Oct 15); late-payment only 0.5% x 5 = 2.5% x $4,000 = $100.
- Difference: $1,000 vs $100 = 10x. Same unpaid tax, same interest.

## The surprising fact
- The extension does nothing for the bill: interest and the 0.5%/month late-payment penalty start April 15 anyway. But skipping the extension costs far more: the late-filing penalty is 10x the late-payment penalty (IRS).
- You can get an extension just by paying: an online payment marked as an extension counts as the request.

## States
- State extension and payment rules differ; some states grant automatic extensions, many still require payment by the original date (e.g., California's automatic 6-month filing extension does not extend payment - CA taxes site). Described generally only.

SOURCES:
- IRS, Failure to File Penalty (irs.gov/payments/failure-to-file-penalty) - via search results quoting the page
- IRS, Failure to Pay Penalty (irs.gov/payments/failure-to-pay-penalty) - via search results
- IRS news: "Taxpayers should know that an extension to file is not an extension to pay taxes" (irs.gov/newsroom); IR-2023-84; Tax Tips 2023-30, 2024-30
- IRS IR-2026-98 (Aug 21, 2026), "Interest rates remain the same for the fourth quarter of 2026"; Rev. Rul. 2026-15; CPA Practice Advisor Aug 24, 2026
- IRS IR-2023-219 (Q1 2024 8%); IRS IR-2024-290 (Q1 2025 7%); IRS quarterly interest rates page (2025-2026 tables)
- Manhattan Institute economics newsletter (3% in 2022 -> 8% Q4 2023)
- Reed Reports 2026-2027 tax due dates; National Taxpayer Advocate tax calendar 2026
- NerdWallet, "How to File a Tax Extension Online in 2026"
- Form 4868 (1998) instructions; TurboTax community (90% rule - weak)
- taxes.ca.gov extension page (state example)
