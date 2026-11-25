# Fact-check: 2027-01-24-explainer (states without income tax)

Checked Nov 25, 2026 for posting Sun Jan 24, 2027, 12:00 CT. Every claim was checked again against web sources. I did not use the brief.

## Claims verified
| # | Claim | Result | Source |
|---|---|---|---|
| 0 | 9 states don't tax wages | TRUE. AK, FL, NV, NH, SD, TN, TX and WY have no individual income tax. WA taxes only some capital gains. | taxfoundation.org/new-hampshire-become-ninth-income-tax-free-state/ |
| 1 | NH I&D tax repealed | TRUE. Applies to tax periods beginning on or after Jan 1, 2025 (HB 2, 2023). | https://revenue.nh.gov/taxes-glance/interest-dividends-tax ; https://www.nashuatelegraph.com/news/2025/01/25/repeal-of-nh-interest-and-dividends-tax-now-in-effect/ |
| 1 | WA taxes only some capital gains (as of 2026) | TRUE through the posting date. SB 6346 was signed Mar 30, 2026 and creates a 9.9% tax on income over $1M. It takes effect Jan 1, 2028. No other state enacted a new wage tax or a repeal that takes effect by Jan 2027. | https://www.axios.com/local/seattle/2026/03/30/bob-ferguson-washington-income-tax-millionaires-2028-law ; https://lawfilesext.leg.wa.gov/biennium/2025-26/Htm/Bill%20Reports/Senate/6346-S.E%20SBR%20FBR%2026.htm ; https://rsmus.com/insights/tax-alerts/2026/washington-state-enacts-millionaires-tax.html |
| 2 | TN average combined sales tax 9.61% (July 2026) | TRUE. The Tax Foundation shows 9.61% in January 2026. Its midyear 2026 page says no statewide rates changed from January to July 2026, and secondary coverage of the midyear data lists TN at 9.61%. I verified this from search snippets because taxfoundation.org was not fetched directly. | https://taxfoundation.org/data/all/state/2026-sales-tax-rates-midyear/ ; https://taxfoundation.org/data/all/state/2026-sales-tax-rates/ ; https://sales.tax/sales-tax-updates/2026-midyear-sales-tax-rates-rankings-state-by-state/ |
| 5 | US average 7.53% | TRUE. The Tax Foundation's 7.53% is a population-weighted average. The captions now say so. | https://taxfoundation.org/data/all/state/2026-sales-tax-rates-midyear/ |
| 3 | TX sales tax 58% of state tax collections, FY2025 | TRUE. The Comptroller's releases say 58%. FY2025 sales tax was $49.06B of $84.2B in total tax collections (about 58.3%). | https://comptroller.texas.gov/about/media-center/news/20250903-acting-texas-comptroller-kelly-hancock-announces-state-revenue-for-fiscal-2025-august-state-sales-tax-collections-1756843079560 |
| 4 | AK PFD 2021 $1,114 | TRUE | https://www.akleg.gov/basis/get_documents.asp?docid=2380 |
| 4 | AK PFD 2022 $3,284 | TRUE. Made up of a $2,622 dividend and $662 energy relief. | https://gov.alaska.gov/2022-permanent-fund-dividend-hits-a-record-3284-00/ |
| 4 | AK PFD 2023 $1,312 | TRUE | https://www.adn.com/alaska-news/2023/10/06/alaskans-got-a-1312-dividend-check-this-year-the-political-cost-of-the-benefit-is-high/ |
| 4 | AK PFD 2024 $1,702 | TRUE. Made up of a $1,403.83 dividend and $298.17 energy relief. | https://dor.alaska.gov/department-of-revenue/news-detail/2024/09/19/department-of-revenue-announces-2024-permanent-fund-dividend-amount-and-energy-relief |
| 4 | AK PFD 2025 $1,000 | TRUE | https://pfd.alaska.gov/Division-Info/summary-of-dividend-applications-payments |
| 4 | AK PFD 2026 $1,000 | **WRONG as a total payment.** The 2026 payment was $1,200: a $1,000 dividend plus $200 energy relief (HB 263). | https://pfd.alaska.gov/ ; https://www.alaskasnewssource.com/2026/09/30/permanent-fund-dividends-will-be-distributed-alaskans-starting-this-week/ |
| 4 | Alaska has no state sales tax and relies on oil and the Permanent Fund | TRUE. There is no statewide sales tax, although some local governments levy one. | general/state sources |
| 5 | Math: $40,000 x 9.61% = $3,844; x 7.53% = $3,012 | TRUE. Both results are exact. | arithmetic |

## Issues found and fixes applied
1. **Line 4 and chart, PFD 2026 (factual and inconsistent).** The script said residents were paid $1,000 in 2026, but the actual payment was $1,200. The chart was also inconsistent: it used totals including relief for 2022 and 2024 but the base dividend for 2026. Fix: every chart point is now the total payment, so 2026 = 1200, the end label is "$1,200", and the chart title is "PFD + relief". New text: "Alaska has no state sales tax either. It leans on oil and its Permanent Fund, which paid $1,200 in 2026, counting one-time relief." New say: "...which paid twelve hundred dollars in twenty twenty-six, counting one-time relief."
2. **Line 5, the worked example was not labeled as simplified, and the narration was awkward.** The spoken amounts had no unit ("costs three thousand eight hundred forty-four"). Fix: the line now opens "Rough math:" and says "...means three thousand eight hundred forty-four in sales tax at Tennessee's rate...". The compare title is now "Rough math". The captions add that the example is simplified because rates vary by city and some items, like groceries, are taxed differently.
3. **Captions: the US average was not labeled as population-weighted.** Fixed in the IG caption and the YouTube description.
4. **Context for Jan 2027: Washington's 2028 tax on income over $1 million.** The video stays accurate because the list is anchored "as of 2026" and the tax does not start until 2028. A neutral one-clause note was added to the IG caption and the YouTube description so viewers who have heard about the new law are not misled. No opinion is expressed.
5. **Word budget.** I removed "at all" from line 1 and "just" from line 6. The script now has 139 spoken words and the hook has 11.

## Other checks
- **Hook:** "Nine states don't tax your paycheck. So who pays the bills?" It is true and specific, about 3 seconds long, and opens a question the video answers. OK.
- **Stale news or time words:** None. Everything is anchored to a stated year (2026 or FY2025) and remains true on Jan 24, 2027.
- **Advice, predictions or politics:** None. There is no suggestion to move states.
- **Cover and title payoff:** "No Paycheck Tax" / 9 and "who pays the bills" are both paid off in the video. OK.
- **On-screen vs spoken values:** These now match. The 9.61%, 58%, $1,200, $3,844 and $3,012 shown on screen equal the spoken values.
- **check.py:** OK. 8 lines, 139 spoken words.
- **Last line:** Unchanged.

All issues have been fixed.

VERDICT: PASS

## Round 2 (editor)
Reviewed fixes; PFD series now consistent total payments incl. relief; 2026 corrected to $1,200; example labeled rough; on-screen and spoken values agree.
VERDICT: PASS
