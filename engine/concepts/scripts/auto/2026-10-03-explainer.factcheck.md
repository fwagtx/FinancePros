# Fact-check: 2026-10-03-explainer ("Zero Interest. Who Pays?", BNPL)

Line numbers refer to /home/user/FinancePros/engine/concepts/scripts/auto/2026-10-03-explainer.raw.json.

## Verified claims

| Line(s) | Claim | Result | Source |
|---|---|---|---|
| 26-27, 30-33 | 16% of US adults used BNPL in 2025 (Fed SHED) | CORRECT. The 2025 SHED, published May 2026, says BNPL use rose 1 point to 16% of all adults. | Fed, Economic Well-Being of US Households in 2025, Credit section (federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-credit.htm), via search excerpts; Capitol Hill Reader summary |
| 39-40 | Up from 10% in 2021, the first year the Fed asked | CORRECT. The SHED first asked about BNPL in 2021, when 10% of adults said they used it. | Fed SHED 2024 report, Banking and Credit ("up from ... 10 percent in 2021, when the survey first asked about BNPL") |
| 44-65 | Chart: 2021 10, 2022 12, 2023 14, 2024 15, 2025 16 | CORRECT. Every point matches the SHED reports for 2021 through 2025. | Fed SHED 2022 report (12%, up from 10%), SHED 2024 report (15%, up from 14% in 2023), SHED 2025 report (16%) |
| 73-80 | $200 purchase = $50 at checkout, then 3 x $50 every 2 weeks over 6 weeks, 0% | CORRECT. This is the standard pay-in-4 structure, and the math works: 4 x $50 = $200, with the last payment at week 6. | CFPB BNPL market report (Dec 2025) |
| 87-94 | Stores pay the lender a fee on each sale | CORRECT. Merchant fees (the merchant discount) are the main revenue source for pay-in-4 lenders. | CFPB, "The Buy Now, Pay Later Market" (Dec 2025) |
| 99-106 | 26% of BNPL users paid late in 2025 | CORRECT. 26% of users paid late in the prior year, per the 2025 SHED. Context: 64% of those who paid late were charged extra, which is 17% of all users. | Fed SHED 2025 (May 2026) |
| 112, 122 | Average late fee $9.99 in 2023; $50 + $9.99 = $59.99; about 20% of $50 | CORRECT. The CFPB's Dec 2025 report gives an average late fee of $9.99 in 2023. The math checks: 9.99 / 50 = 19.98%, which rounds to 20%. | CFPB BNPL market report, Dec 2025 (files.consumerfinance.gov/f/documents/cfpb_bnpl-market-report_2025-12.pdf); American Banker; ABA Banking Journal |
| 128-133 | FICO built scores that count BNPL loans (June 23, 2025) | CORRECT. On June 23, 2025, FICO announced FICO Score 10 BNPL and FICO Score 10 T BNPL, expected to be available in fall 2025. | FICO investor news release, June 23, 2025; Washington Post, July 7, 2025 |
| 138-158 | Zero interest holds if all payments are on time; $200 total | CORRECT for standard pay-in-4 plans. "Credit hit risk" is correctly worded as a risk, not a certainty. | CFPB, "Do BNPL loans have fees?" |

No math errors were found. There is no political opinion, and there are no price predictions or advice. The post text includes a "not financial advice" line. The cover and title ("Zero Interest. Who Pays?") are paid off: the video names two payers, stores through merchant fees and late payers through late fees.

## Issues (all minor, none factual)

1. **Line 112 vs 113: the on-screen number differs from the spoken one.** The caption and scene say "$9.99" and "$59.99", but the narration says "about ten dollars". The meaning is the same, but the value shown and the value spoken do not match exactly. Fix: change `say` to "The average late fee in twenty twenty-three was nine ninety-nine, about twenty percent of one fifty dollar payment." Source: CFPB, Dec 2025, $9.99.
2. **Line 26 vs 27: the caption and narration say different things.** The caption says "so it's worth knowing" and the narration says "so the answer matters". Fix: pick one. For example, set both to "so the answer matters."
3. **Lines 128-133: the FICO news is not new.** The announcement is from June 23, 2025, more than 15 months before posting, and the news card could make it look recent. The date on the card keeps it honest. Optional fix: change the headline to "FICO has offered BNPL-inclusive scores since 2025", or change the narration to "Since 2025, FICO has offered credit scores that count these loans...". The claim also stays accurate only because it says "could follow you": lenders have been slow to adopt these scores, so keep "could".
4. **Line 112: the data is somewhat old.** The late-fee figure is for 2023. It is the latest the CFPB has published (in its Dec 2025 report), and the script labels the year correctly, so no change is required.
5. **Lines 13-14: the hook works but could be tighter.** "Pay in four charges zero interest. So who's paying for it?" is true and creates a clear question, but at 11 words it runs about 3 to 3.5 seconds, which is borderline. Fix: shorten the narration to "Pay in four is zero interest. So who pays?" (9 words, under 3 seconds, and it matches the cover). Alternatively, make it more specific: "Pay in four is zero percent. Somebody's still paying. Who?"
6. **Line 100: optional context.** "Anyone who slips" implies that every late payer pays a fee, but only 64% of late payers were charged extra (17% of all users). This does not need a change. Optionally add it to the post text for accuracy.

## Time words
The script has no "this year", "last year", "today" or "recently" phrasing. Every figure is tied to an explicit year (2021 to 2025) and will read correctly on October 03, 2026.

## Sources
- Federal Reserve, Economic Well-Being of US Households in 2025 (May 2026), Credit: https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-credit.htm
- Federal Reserve, SHED 2024 Banking and Credit: https://www.federalreserve.gov/publications/2025-economic-well-being-of-us-households-in-2024-banking-and-credit.htm
- Federal Reserve, SHED 2022 Banking and Credit: https://www.federalreserve.gov/publications/2023-economic-well-being-of-us-households-in-2022-banking-credit.htm
- CFPB, The Buy Now, Pay Later Market (Dec 2025): https://files.consumerfinance.gov/f/documents/cfpb_bnpl-market-report_2025-12.pdf
- American Banker on the CFPB report: https://www.americanbanker.com/payments/news/cfpb-report-finds-pay-in-4-bnpl-loans-growing
- FICO release (June 23, 2025): https://investors.fico.com/news-releases/news-release-details/fico-unveils-groundbreaking-credit-scores-incorporate-buy-now/

VERDICT: PASS
