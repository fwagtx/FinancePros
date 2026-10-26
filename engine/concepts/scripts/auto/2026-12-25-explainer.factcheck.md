# Fact-check: 2026-12-25-explainer (no-spend challenge)

Checked 2026-10-26 for posting Fri 2026-12-25, 12 PM CT. Line indexes are **0-based** and refer to the `lines` array.

## Verified claims
- **BLS CE food away from home, all consumer units (FRED CXUFOODAWAYLB0101M):** 2019 $3,526, 2020 $2,375, 2021 $3,030, 2022 $3,639, 2023 $3,933, 2024 $3,945. All six check out. 2021 and 2023 to 2024 came straight from FRED excerpts. 2020 was confirmed by FRED and Oberlo. 2019 matches the BLS-reported 32.6% drop in 2020 (2375/0.674 = $3,524, which rounds to ~$3,526). 2021 also matches the reported 27.6% rise (2375 x 1.276 = $3,030).
- **"Household" vs "consumer unit":** OK for narration. BLS's term is "consumer unit", which is close to a household. The post text already says "consumer unit". "Eating out" is a fair plain-English gloss of "food away from home".
- **C+R Research survey (2022, 1,000 US adults):** average quick guess $86/mo, itemized $219/mo, a $133 gap. 42% said they had forgotten they were still paying for a subscription they no longer use. The figures, the wording and the 2022 label are all correct. "Offhand estimate" is fair: respondents had 10 seconds to make the guess.
- **Worked example:** 3 x $15 = $45 a week, x 4 = $180. The math is correct and the line is labeled "Example".
- Every on-screen value matches the spoken one. text and say differ only in numerals.
- Limits: hook spoken 11 words; hook title 16 characters; prop label "$0" and "X-ray" OK; chart end "$3,945" is 6; compare values "$86"/"$219" OK; compare subs 16/18; stat label/sub OK; board lines <=18; split items 11/12; split titles OK; cover title 18; cover value "$0/mo" is 5; post.title 55; tiktok 144. Spoken total is 137.
- There is no advice, no price prediction and no political content. The `keep` flag is not used.

## Issues and fixes

1. **Prelec & Loewenstein attribution, line 5 (should fix).** The 1998 paper "The Red and the Black" (Marketing Science 17(1)) introduced the pain of paying. It also argues in theory that credit cards decouple payment from consumption. The direct card evidence, though, is Prelec & Simester (2001, Marketing Letters, "Always Leave Home Without It"), where card payers bid up to ~100% more. As written, the line reads as if the 1998 paper showed the card effect. The fix below is net +1 word, bringing the total to 138, which is within limits. It removes "researchers" and adds "later research found".
   - line 5 `text` -> `In 1998, Prelec and Loewenstein described the pain of paying; later research found cards can soften it.`
   - line 5 `say` -> `In nineteen ninety-eight, Prelec and Loewenstein described the pain of paying; later research found cards can soften it.`
   - post.ig, replace `Prelec and Loewenstein (1998) described the 'pain of paying,' which card payments can soften.` with `Prelec and Loewenstein (1998) described the 'pain of paying'; later research (Prelec & Simester, 2001) found card payments can soften it.`
   - post.ig sources, replace `Prelec & Loewenstein (Marketing Science, 1998).` with `Prelec & Loewenstein (Marketing Science, 1998), Prelec & Simester (Marketing Letters, 2001).`
   - post.yt_desc, replace `Prelec and Loewenstein (1998) described the 'pain of paying,' which card payments can soften.` with `Prelec and Loewenstein (1998) described the 'pain of paying'; later research found card payments can soften it.`

2. **Stale data before posting, lines 2 and post (must re-check before Dec 25).** BLS has scheduled the 2025 annual Consumer Expenditure data for **Oct 29, 2026**, so it will be out before this video posts. The 2024 statement stays true because it carries a year, but it will no longer be the latest figure. After Oct 29: add a `[2025, N]` point to the chart in line 2. Update line 2's text and say to "In 2025 ... $N", the chart `end`, and the 2024 references in the ig and yt_desc text. Note that BLS weight-adjusted the 2025 data to cover the Oct–Nov 2025 shutdown gap. If you would rather not touch it, the current wording is still accurate.

3. **Cover "$0/mo" (minor, optional).** It is sensible shorthand for "no-spend". Strictly, though, the script says rent, bills and groceries still get paid, so total spending is not $0. Acceptable as is. A possible swap is `$0 fun` (6 characters).

4. **Hook, line 0 (OK).** The claim is true as a framing, it is short (11 words, under 3 seconds), and lines 3–7 pay it off by showing what the month reveals (eating out, forgotten subscriptions, card spending). It is somewhat abstract. If you want it punchier, it would need a concrete number, which the 12-word limit makes hard. No change required.

5. **Line 7 (OK).** "Some people find..." is observational, not an instruction. It reads fine out loud.

## Sources
- FRED CXUFOODAWAYLB0101M (BLS CE): https://fred.stlouisfed.org/series/CXUFOODAWAYLB0101M
- BLS CE 2024 release: https://www.bls.gov/news.release/archives/cesan_12192025.pdf ; 2021 release (32.6% / 27.6% changes): https://www.bls.gov/news.release/archives/cesan_09082022.htm
- BLS 2025 data schedule notice: https://www.bls.gov/cex/notices/2026/2026-2-year-tables.htm
- C+R Research survey coverage: https://www.ktvu.com/news/many-underestimate-monthly-subscription-costs-133-survey-2022 ; https://www.nbcwashington.com/news/business/money-report/consumers-spend-an-average-133-more-each-month-on-subscriptions-than-they-realize-study-shows/3067565/
- Prelec & Loewenstein 1998: https://ideas.repec.org/a/inm/ormksc/v17y1998i1p4-28.html ; Prelec & Simester 2001 summaries: https://www.canr.msu.edu/news/beware_the_credit_card_premium

VERDICT: PASS

## Round 2 (editor)
Applied fix 1 (card attribution) and 3 (cover $0 fun). Item 2 noted for recheck after Oct 29 BLS release.
VERDICT: PASS
