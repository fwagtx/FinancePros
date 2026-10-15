# Fact-check: 2026-12-14-explainer (posts Mon Dec 14, 2026)

Independent check of every line, scene value, cover and post field in `2026-12-14-explainer.raw.json`, done with my own web research. I did not use the writer's research brief. Math was recomputed in python. Spoken words: 135 now, 137 after the fixes below (the limit is 115-138).

## Claims

| # | Claim (line / field) | Verdict | Source |
|---|---|---|---|
| 1 | Texas motor vehicle sales tax is 6.25% (L1, post) | TRUE | Texas Comptroller Motor Vehicle Tax Guide (comptroller.texas.gov/taxes/publications/96-254/mv-sales.php); Tarrant County Tax Office title-fees page |
| 2 | $32,000 x 6.25% = $2,000 (L1, L5, L6) | TRUE (math checked) | python |
| 3 | Texas taxes price minus trade-in, so $8,000 trade -> tax on $24,000 = $1,500; $500 less (L5, L6) | TRUE | Comptroller guide: for dealer sales the taxable value is the sales price minus the trade-in allowance (its example is $42,000 - $15,000 = $27,000). This applies to dealer sales, which is the scenario shown. |
| 4 | Is the doc fee taxed? | Texas does NOT tax a separately stated doc fee | Comptroller "Total Consideration" page (96-254/total-consideration.php): taxable total consideration is the sale price less trade-in and "does not include documentary fees, inspection fees, finance charges or the title and registration fees". Taxing only the $32,000 price is therefore correct, and no change is needed. |
| 5 | Title fee $33 (L2, post) | TRUE, but it needs a label | Tarrant County Tax Office: the title fee is $28 or $33 depending on the county, and $33 applies in emissions counties (Tarrant and its neighbors). TxDMV new-to-Texas page: "$28.00 or $33.00 (varies by county)". |
| 6 | $50.75 base registration (L2, post) | TRUE | TxDMV fee chart FeeChart_1C.pdf, "Texas Registration Fees effective January 1, 2026, expires December 31, 2026": passenger vehicles 6,000 lbs or less are $50.75 plus local fees. It is still current on Dec 14, 2026. |
| 7 | "$2,308.75 extra, before county fees" (L3, post, cover tie-in) | MATH TRUE (2000+33+50.75+225), WORDING INACCURATE | Besides county fees, the total also leaves out state fees: the $1 TexasSure fee (TxDMV says the registration line shows $51.75), the $4.75 processing and handling fee, and the state inspection program replacement fee ($7.50, or $16.75 for a new vehicle on a two-year registration; TxDMV, effective Jan 1, 2025). "Before county fees" suggests that only county fees are missing. |
| 8 | $225 doc fee; Texas dealers must file to charge more (L2, L4, post) | TRUE; it is correctly not called a cap | OCCC 7 TAC 84.205 (amended effective July 2024; OCCC filing instructions rev. 7/2/24): a fee of $225 or less needs no filing and is presumed reasonable. Above $225 the dealer must give the OCCC written notice and a cost analysis. A May 2026 OCCC pre-comment draft would revise the cost-analysis rules above $225 but leaves the $225 threshold alone. |
| 9 | California caps doc fees at $85 (L4, post) | TRUE | CalMatters, Oct 2025: Newsom vetoed SB 791, which would have raised the $85 cap to 1% of the price, up to $260. The $85 cap applies to dealers in the DMV's electronic programs and $70 to the others, so "caps at $85" is correct as the maximum. I found no 2026 law that changes it before Dec 14, 2026. |
| 10 | Chart FY2022 6.45, FY2023 6.82, FY2024 6.84, FY2025 7.08, FY2026 7.45 ($B), motor vehicle sales and rental taxes (L7) | ALL TRUE | Comptroller fiscal-year releases: FY2022 $6.45B (Sept 1, 2022); FY2023 $6.82B, +5.8% (Sept 1, 2023); FY2024 $6.84B, +0.2% (Sept 3, 2024); FY2025 $7.08B, +3.7% (Sept 3, 2025); FY2026 $7.45B, +5.2% (Huffines release Sept 2026; monthly table total 7,450,837K). |
| 11 | Fiscal 2026 = Sept 2025 to Aug 2026 (L7 text) | TRUE | The Texas state fiscal year runs Sept 1 to Aug 31. |
| 12 | Spoken numbers = on-screen numbers | TRUE | Every value matches. Minor: L1 `text` says "2026 Texas example" and `say` says "twenty twenty-six example" (it drops "Texas"). Not a number problem. |
| 13 | Staleness on Dec 14, 2026 | OK | The fee chart is valid through Dec 31, 2026. FY2026 is closed. The Texas Legislature is not in session until Jan 2027. |
| 14 | Advice / politics / predictions | None | Neutral, explanatory language only. |
| 15 | Hook (L0): 11 words, true, specific, paid off by L3 | PASS | |
| 16 | Template rules: keep:true on L6 follows the compare on L5; compare values are 7 characters or fewer | PASS | |

## Required fixes

1. **L3 (index 3) `text`**: replace with `That's $2,308.75 extra, before county and other fees.`
2. **L3 (index 3) `say`**: replace with `That's two thousand three hundred eight dollars and seventy-five cents extra, before county and other fees.` This adds 2 words, so the total goes from 135 to 137, which stays within 115-138. No trims are needed.
3. **L3 (index 3) `scene.sub`**: replace `TX example, 2026` with `Emissions-county example`. This labels the $33 title as the emissions-county rate.
4. **post.ig**, second line: replace with `Example at 2026 Texas rates: 6.25% sales tax on the vehicle price = $2,000, plus a $33 title (emissions counties; $28 elsewhere), $50.75 base registration and a $225 doc fee = $2,308.75 extra, before county and other fees.`
5. **post.yt_desc**, first sentence: replace with `Example at 2026 Texas rates: a $32,000 car adds $2,000 in sales tax (6.25% of the vehicle price), a $33 title (emissions counties; $28 elsewhere), $50.75 base registration and a $225 doc fee, $2,308.75 before county and other fees.`
6. **post.tiktok**: replace `A $32,000 car in Texas costs $2,308.75 more.` with `A $32,000 car in Texas costs over $2,308.75 more.` The total becomes 148 characters, within the 150 limit.

Optional, not required: L1 `say` could add "Texas" ("In this twenty twenty-six Texas example, ...", +1 word, 138 total) so it matches the caption word for word.

VERDICT: FIX

## Round 2 (editor)
Applied fixes 1-6 ("before county and other fees", emissions-county label shortened to "TX emissions cty" for layout, captions updated).
VERDICT: PASS
