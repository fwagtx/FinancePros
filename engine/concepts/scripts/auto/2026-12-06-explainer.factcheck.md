# Fact-check: 2026-12-06-explainer (Ticker, scholarships vs grants vs work-study)

Checked Oct 7 2026 for posting Sun Dec 6 2026 (evergreen). Line indexes are 0-based. Spoken total: 131 words (115-138 OK). There are no keep:true lines and no compare scenes.

## Verified claims

- **L2, max Pell 2026-27 = $7,395: TRUE.** ED Dear Colleague Letter GEN-26-01 (Jan 30 2026) sets the maximum at $7,395 and the minimum at $740 for July 1 2026 to June 30 2027. FY26 full-year appropriations (H.R. 7148) kept the maximum at $7,395. The 2026-27 award year is already fixed, so the figure will still be correct on Dec 6.
- **L3, chart data: TRUE.** 2017-18 $5,920, 2018-19 $6,095, 2019-20 $6,195, 2020-21 $6,345 and 2021-22 $6,495 come from NASFAA/BestColleges. 2022-23 $6,895 (+$400, FY22 omnibus) and 2023-24 $7,395 (+$500, FY23 omnibus) are confirmed. 2024-25, 2025-26 and 2026-27 are each $7,395. NCAN describes FY26 as "Pell Max Set at $7,395 for Third Consecutive Year".
- **L3, "flat for four award years in a row": ACCEPTABLE, slightly loose.** The amount has been $7,395 in four award years (2023-24 through 2026-27). That is three straight years with no increase after the 2023-24 raise. Most viewers will read "flat at $7,395 for four award years" correctly. A precise alternative is below (optional).
- **L4, $12,080 grant aid per FTE undergrad in 2024-25 (College Board Trends in Student Aid 2025): TRUE.** The same report gives $16,810 in total aid per FTE.
- **L5, IRS Pub 970: TRUE.** A scholarship or grant is tax-free only when it pays for tuition, required fees, and books, supplies and equipment the courses require. Money used for room and board is taxable. The example math is right: $10,000 - $7,000 qualified = $3,000 taxable. It is clearly labeled as an example.
- **L6, work-study: TRUE.** FWS pays at least the current federal minimum wage. FWS earnings are left out of income in the FAFSA/SAI calculation. That still holds under the current (SAI-era) FAFSA, which asks for taxable earnings from need-based employment programs such as FWS so they can be subtracted. FWS pay is still subject to income tax; the script never says otherwise.
- **L7, early withdrawal: TRUE.** Under Return of Title IV funds rules, a student who withdraws before the 60% point may have to repay unearned grant aid (a grant overpayment, generally half of the unearned amount). "May owe back part of a federal grant" is accurate.
- **L1, "usually merit" / "usually need-based": OK.** This is the standard framing from studentaid.gov and financial-aid offices, and "usually" covers the exceptions.

## Issues and fixes

1. **L4, spoken "per full-time student" does not match on-screen "per FTE" (MUST FIX).** FTE (full-time-equivalent) weights part-time students. The College Board figure is not what an average full-time student gets, so the spoken simplification changes what the number means.
   - say: `In 2024 to 2025, undergrads averaged twelve thousand eighty dollars in grants per full-time-equivalent student, says the College Board.` (19 words, unchanged count)
   - The text, stat label and sub are already correct. Keep "sub": "College Board 2025" (18 chars).

2. **L5, "that three thousand is taxable" (SHOULD FIX).** It is taxable under Pub 970. But many students owe no tax on it because of the standard deduction, so "taxable income" is the precise and fair phrasing.
   - text: `Example: a $10,000 scholarship puts $3,000 toward housing. That $3,000 counts as taxable income (IRS Pub 970).`
   - say: `The catch: say a ten thousand dollar scholarship puts three thousand toward housing. Under IRS rules, that three thousand counts as taxable income.` (23 words)
   - Optionally change the to-label to `Taxable income (housing)`.

3. **L3, optional precision.**
   - text: `That max has held at $7,395 since 2023-24: four award years in a row.`
   - Or leave the text and change say only: `That max has been stuck at that level since 2023 to 2024.` (12 words)

4. **L1, board lines drop "usually" (minor).** The board shows "Scholarship = merit gift" and "Grant = need-based gift", which are absolute, while the caption and spoken line hedge. Suggested (all 26 chars or fewer):
   - `Scholarship: often merit` (24)
   - `Grant: often need-based` (23)
   - `Work-study: a paycheck` (22)

5. **L6, split item "No repayment" (minor).** It conflicts slightly with L7 (grants can be repaid after early withdrawal). Suggested item: `Rarely repaid` (13 chars). Other items are 16 chars or fewer and fine.

6. **L0, hook (minor).** It is true and specific, and the cover "Free Money, Taxed?" pays off at L5. At 11 words it runs about 3.5-4 s. A tighter option: `Your free college money can be taxable.` (7 words). Optional.

7. **Posts:**
   - ig: change `don't have to be repaid` to `generally don't have to be repaid`. Change `IRS rule: scholarship money used for housing is taxable.` to `IRS rule: scholarship money used for housing counts as taxable income.` The "flat for four award years in a row" wording is OK, or change it to `unchanged since 2023-24`.
   - yt_desc: change `scholarship money used for housing is taxable under IRS Publication 970` to `scholarship money used for housing counts as taxable income under IRS Publication 970`.
   - tiktok: fine.
   - No advice language, no price predictions, no politics. No stale time words: every year is explicit (2026-27, 2024-25). The disclaimers are present.

Running total after fixes 1-3: 131 + 2 (L5) + 0 (L4) + 0 (L3 say option, still 12 words) = 133. Within 115-138.

Passes once fixes 1 and 2 are applied; fixes 3-7 are recommended.

## Sources
- ED GEN-26-01: https://fsapartners.ed.gov/knowledge-center/library/dear-colleague-letters/2026-01-30/2026-27-federal-pell-grant-maximum-and-minimum-award-amounts
- NCAN FY26 Pell "third consecutive year": https://www.ncan.org/news/718626/House-and-Senate-Release-FY26-Appropriations-Bill-Pell-Max-Set-at-7395-for-Third-Consecutive-Year.htm
- 2023-24 +$500 to $7,395: https://nasfaa.org/news-item/29680/Congress_Unveils_Sprawling_Fiscal_Year_2023_Spending_Bill_With_500_Maximum_Pell_Grant_Boost
- 2022-23 $6,895: https://www.bestcolleges.com/news/2022/03/15/congress-increases-max-pell-grant/
- Pell history: https://bestcolleges.com/research/pell-grant-amount
- College Board highlights: https://research.collegeboard.org/trends/student-aid/highlights
- IRS Pub 970: https://www.irs.gov/publications/p970 (via TaxAct and Fox Business summaries)
- FWS / FAFSA exclusion: https://fsapartners.ed.gov/sites/default/files/2026-01/202627StandardSAIProcedures.pdf ; https://www.eou.edu/financial-aid/work-study/
- R2T4: https://www.pittstate.edu/financial-aid/return-of-title-iv-aid.html

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-5 and 7: line 4 says full-time-equivalent; line 5 "counts as taxable income"; line 3 "stuck at that level since 2023 to 2024"; board "often"; split "Rarely repaid"; ig/yt_desc wording. Hook kept (true, paid off at line 5).
VERDICT: PASS
