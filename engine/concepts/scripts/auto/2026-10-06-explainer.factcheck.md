# Fact-check: 2026-10-06-explainer ("Cheaper plan, bigger bill?")

Checked 2026-09-30 for posting 2026-10-06. Script: `2026-10-06-explainer.raw.json`. I did not read the research brief.

## Sources and access limits
- KFF 2025 Employer Health Benefits Survey (kff.org/health-costs/2025-employer-health-benefits-survey/ and its Summary of Findings PDF). Search excerpt of the official page: "Thirty-four percent of covered workers in 2025 are in a plan with a general annual deductible of $2,000 or more for single coverage" and "the average deductible among covered workers in a plan with a general annual deductible was $1,886 for single coverage."
- HealthCare.gov out-of-pocket maximum glossary: premiums do not count toward the out-of-pocket limit. The proxy blocked the page and the web search budget ran out, so this rests on well-established HealthCare.gov wording and was not re-fetched.
- The proxy blocked kff.org, files.kff.org and healthcare.gov. The session's web search budget (200) ran out partway through the check.

## Math (recomputed in Python)
Assumptions: all care goes toward the deductible first, then 20% coinsurance, capped at the out-of-pocket max. Annual premium is monthly × 12.

| Scenario | Plan A (120/mo, 1,000 ded, 4,000 max) | Plan B (40/mo, 3,000 ded, 7,000 max) |
|---|---|---|
| Annual premium | 1,440 | 480 |
| $500 of care | 500 → **1,940** | 500 → **980** |
| $20,000 bill | 1,000 + 0.2×19,000 = 4,800 → capped at 4,000 → **5,440** | 3,000 + 0.2×17,000 = 6,400 (under 7,000) → **6,880** |
| Difference in a big year | | 6,880 − 5,440 = **1,440** |

All worked numbers are correct, and every on-screen value matches the spoken value.

## Claim-by-claim
| Line | Claim | Status |
|---|---|---|
| 1 | Cheaper plan can cost $1,440 more | Correct inside the hypothetical example |
| 2 | Premium, deductible, out-of-pocket max | Correct, but simplified (see issue 2) |
| 3 | Plan values | Hypothetical; caption and narration match |
| 4 | $980 vs $1,940 | Correct |
| 5 | $5,440 vs $6,880; A hits its cap, B stays under its cap | Correct |
| 6 | $1,440 more | Correct |
| 7 | Premiums don't count toward the max; yearly cost = premium × 12 + your share of care | Correct |
| 8 | 34% of covered workers had a $2,000+ deductible (single coverage, 2025, KFF) | Verified against the KFF excerpt |
| Post | Average single deductible $1,886 | Verified. This average covers only workers in plans that have a deductible (see issue 8) |

## Issues
1. **Line 1 hook (minor).** The hook is true and specific. It is about 13 spoken words, so it runs about 3–3.5 s, slightly over the target. The spoken "fourteen hundred forty more" also drops "dollars". A tighter version: text "The cheaper health plan can cost you $1,440 more." / say "The cheaper health plan can cost you fourteen hundred forty dollars more."
2. **Line 2 simplification (minor).** "only one of three numbers you pay" leaves out coinsurance and copays, yet line 5 uses 20% coinsurance. Suggested fix: "Because the premium is only one of the numbers you pay. Three matter most:" or change the list title to "3 big numbers on every plan".
3. **Line 3 hypothetical not flagged in the video (minor).** Only the post text says the plans are hypothetical. Suggested fix: change the scene title to "Two example plans (hypothetical)". The line is also long, about 9–10 s. The spoken "a four-thousand max" reads awkwardly; "a four-thousand-dollar max" or "four-thousand-dollar out-of-pocket max" is smoother.
4. **Line 5 wording (minor, clarity).** "Plan A's cap kicks in: $5,440 total" could make viewers think the cap is $5,440, when it is $4,000 plus $1,440 in premiums. Suggested fix: "Plan A hits its $4,000 cap: $5,440 with premiums. Plan B: $6,880."
5. **Line 6 coincidence (nit).** The $1,440 gap is the same number as Plan A's annual premium (120 × 12), which viewers may confuse. The math is still right. Text drops the "So" that the narration has; this is harmless.
6. **Line 8 stale-data risk (watch).** KFF usually publishes each year's Employer Health Benefits Survey in October (the 2024 edition came out in October 2024 and the 2025 edition in late October 2025). The 2026 survey could come out near or after the posting date. "In 2025" stays accurate either way, but re-check on posting day and swap in 2026 figures if they are out. One search summary claimed the 2026 survey came out in August 2026, but it quoted 2024 figures, so I treated it as unreliable.
7. **Line 8 phrasing (minor).** The caption and narration say "had a deductible of $2,000 or more" without "for single coverage". The on-screen sub-caption covers it. For a tighter match with KFF, say "...a single-coverage deductible of two thousand dollars or more."
8. **Post IG text (minor).** "(average: $1,886)" should read "(average single deductible among plans with one: $1,886)", because KFF computes that average only over workers whose plan has a deductible.
9. **Line 9 split scene (nit).** "Low premium wins / Low max wins" is a generalization; it holds for this example. It is not advice.

## Other checks
- Time words: only "In 2025" appears, and it is correct on October 6, 2026. There is no "this week", "today" or "next year".
- Advice and price predictions: none. The "not financial advice" disclaimer is in the post.
- Political opinion: none.
- Cover and title payoff: "Cheaper Plan, Bigger Bill? +$1,440" is paid off in lines 5–6.
- On-screen vs spoken values: all match (1,440; 120/40; 1,000/3,000; 4,000/7,000; 980/1,940; 5,440/6,880; 20%; 34%; 2,000).
- Timeliness: the video fits open enrollment season.

VERDICT: PASS
