# Fact-check (re-check after revision): 2026-10-08-explainer

Checked: September 30, 2026. Posting date: October 08, 2026. I re-read the whole revised script. The research brief was not consulted. Math was recomputed in python. No new searches were needed: every figure in the revision is covered by sources already verified in the first pass (IRS filing season statistics, IRS Q4 2026 interest-rate release, IRS guidance on 2025 withholding and OBBBA, and tax outlets on Form 2210 and safe harbor rules).

## Verified claims

| Line | Claim | Result | Source |
|---|---|---|---|
| 1 | Average 2026 refund $3,275 | Correct. This is the figure through the week ending Apr 17, 2026, and line 6 gives the "by mid-April" date | IRS filing season stats, wk ending Apr 17, 2026; CNBC Apr 24, 2026 |
| 4 | $12,000 - $9,000 = $3,000 refund | Correct | python |
| 5 | $9,000 - $8,000 = $1,000 owed | Correct | python |
| 6 / chart | 2026 $3,275, up from $2,942 a year earlier; 2024 $2,850; 2023 $2,753 | All match the IRS figures for comparable mid-April weeks (+11.3%, +3.2%, +3.5%) | IRS stats, Apr 17 2026 / Apr 18 2025 / Apr 19 2024 |
| 7 | New tax breaks applied to 2025; withholding tables did not change until 2026 | Correct. The IRS kept the W-4 and withholding tables unchanged for tax year 2025 and built the new provisions into the 2026 tables | IRS "How to update withholding..." page; payroll.org |
| 8 | $3,275 / 12 is about $273 a month, interest-free | Correct ($272.92) | python |
| 9 | Owing $1,000+ at filing means a penalty can apply, figured like interest at 7% a year right now | Correct. 7% is the IRS individual underpayment rate for Q4 2026 (short-term rate 4% + 3), which is in effect on Oct 8. The Form 2210 penalty is computed as interest at this rate | IRS newsroom, "Interest rates remain the same for the fourth quarter of 2026" |
| posts | Safe harbor: 90% of this year's tax, or 100% of last year's (110% for high earners) | Correct | Form 2210 rules |

Other checks:
- The on-screen and spoken values match in every line.
- The cover ("Your Refund Was Your Money", $3,275) and the post titles are paid off by lines 1 and 6-8.
- The time words ("2026 refund season", "right now" = Q4 2026, "Oct-Dec 2026") are all correct on October 8.
- There is no advice and there are no price predictions. The "Not financial advice" line is present.
- The law is referred to only as "new tax breaks", so the script stays politically neutral.

## Remaining issues (all minor; none blocks)

1. **Line 1, hook length (nit).** The hook is now specific and grabs attention. Spoken, it is about 3-3.5 seconds, because "twenty twenty-six" takes time to say. It also says "Thirty-two seventy-five" without "dollars", which is fine because the $3,275 is on screen.
   Optional trim: "Average refund this year? Thirty-two seventy-five. Your own money."
2. **Lines 1 and 8, "your own money" / "lent to the IRS" (nit, nuance).** Part of the average refund comes from refundable credits such as the EITC and ACTC, not from overwithholding, so "your own money" is a slight simplification. This is acceptable for an explainer.
3. **Line 9, on-screen label (nit).** The label reads "IRS penalty rate", with the sub "Q4 2026, figured as interest". It is accurate as written. "IRS underpayment rate" would be more precise.
4. **Staleness (low).** The refund data is from April, but it is clearly dated, so this is acceptable.

VERDICT: PASS
