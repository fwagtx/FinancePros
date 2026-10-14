# Fact-check: 2026-12-13-explainer (posts Sunday December 13, 2026)

Checker: independent, did not read the .research.md brief. Checked against web research (IRS pages via search excerpts; irs.gov direct fetch fails DNS from this sandbox) and recomputed with python.

## Claims

| # | Line / field | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | L1 (say/text) | A traditional 401(k) takes money from the paycheck before (federal) income tax | TRUE | IRS 401(k) Plan Overview; IRS Topic 424 ("elective deferrals isn't subject to income tax withholding at the time of deferral", excluded from W-2 box 1) |
| 2 | L2, L0 hook, cover, compare | 22% bracket: $100 deferred cuts federal income tax $22, take-home drops $78 | TRUE (math: 100 x 0.78 = 78). Labeled "Example: 22% bracket" on L2; state tax excluded is labeled on L5 | Rev. Proc. 2025-32 (2026: 22% bracket = $50,401-$105,700 single, $100,801-$211,400 MFJ, per NerdWallet/Betterment/q3adv summaries of the Rev. Proc.) |
| 3 | L3 compare | Saving $100 after tax drops take-home the full $100 | TRUE | Arithmetic |
| 4 | L4 stat | Social Security and Medicare still apply: 7.65% = $7.65 per $100 | TRUE (6.2% + 1.45% = 7.65%; SS part only up to the $184,500 2026 wage base). WORDING ISSUE, see Fix 1 | IRS 401(k) Plan Overview ("included as wages subject to Social Security (FICA), Medicare..."); IRS Topic 424; 2026 wage base $184,500 (Mayer Brown, Venable 2026 COLA summaries) |
| 5 | L5 money | 26 paychecks: $2,600 in, take-home drops $2,028 (example, no state tax) | TRUE (26 x 100 = 2,600; 2,600 x 0.78 = 2,028). Well under the 2026 $24,500 deferral limit | Arithmetic; Venable (2026 limit $24,500) |
| 6 | L6 | Tax delayed, not skipped; income tax due on withdrawal | TRUE | IRS 401(k) Plan Overview; IRS Topic 558 |
| 7 | L7 stat | Before age 59 1/2, usually an extra 10% tax | TRUE ("usually" correctly hedges exceptions) | IRS Topic 558 (10% of the amount includible in income); IRC 72(t) |
| 8 | L8 list | Exceptions: disability, separation at 55+, death | TRUE. Rule of 55 = separation during or after the calendar year you turn 55, from that employer's plan only; "leaving the job at 55 or later" is an acceptable simplification. ISSUE: "Death" is on screen but not spoken, see Fix 2 | IRS Pub 5036 / IRC 72(t)(2)(A)(ii),(iii),(v); IRS Topic 558 |
| 9 | post.ig / yt_desc | "22% federal bracket in 2026", Rev. Proc. 2025-32, Topic 558, SSA (2026) | TRUE; still correct on Dec 13, 2026 (2027 tables will exist by then, but the year label keeps it accurate) | As above |

## Other checks
- Hook (L0): 10 spoken words, under 3 seconds, specific true number, creates a "how?" question that L1-L2 pay off. Strong. Cover "Save $100, Lose Only $78?" (5 words) and post title are paid off.
- Assumptions labeled: 22% bracket on L2 (spoken and on screen), "ex." on L3 compare, "example, no state tax" on L5 text. Adequate.
- Advice / predictions / politics: none. No instruction-style takeaway. CTA fine.
- Time words: none ("today", "this week" etc. absent). Every number is dated or generic. Not stale on Dec 13, 2026.
- On-screen vs spoken: all numbers match ($100/hundred, 22%, $22, $78, $7.65, $2,600, $2,028, 59 1/2, 10%, 55). Only mismatch is the non-numeric list item "Death" (Fix 2).
- Compare values <= 7 chars ("-$100", "-$78"): OK. No keep:true lines. Hook title <= 7 words with one bracketed word: OK. Board lines <= 26 chars: OK.
- Spoken word count: 137 now; 136 after fixes (limit 138).

## Required fixes

**Fix 1 (L4, index 4) - FICA line reads as an extra cost on top of the $78.** "Still take $7.65 of it" can make viewers add $7.65 to the $78 drop. FICA is paid on that $100 either way (pre-tax or after-tax), so the $78 vs $100 comparison stands; the line should say so.
- `say`: "One catch: Social Security and Medicare still tax that hundred, seven sixty-five, either way." (14 words, was 15)
- `text`: "One catch: Social Security and Medicare still tax that $100, $7.65, either way."
- `scene.sub`: "per $100 (7.65%), both ways" (optional; current "per $100 (7.65%)" is acceptable)

**Fix 2 (L8, index 8) - "Death" shown on screen but not spoken.**
- `say`: "Some exits skip that ten percent: disability, death, or leaving the job at fifty-five or later." (16 words, unchanged count)
- `text`: "Some exits skip that 10%: disability, death, or leaving the job at 55 or later."

Optional (not required): L1 could say "federal income tax" for precision (a few states, e.g. Pennsylvania, tax deferrals); not needed since L2 says "federal".

Sources:
- IRS, 401(k) Plan Overview: https://www.irs.gov/retirement-plans/plan-participant-employee/401k-resource-guide-plan-participants-401k-plan-overview
- IRS, Topic 424, 401(k) plans: https://www.irs.gov/taxtopics/tc424
- IRS, Topic 558: https://www.irs.gov/taxtopics/tc558
- IRS, Pub 5036 (exceptions table, age 55 separation): https://www.irs.gov/pub/irs-pdf/p5036.pdf
- 2026 brackets (Rev. Proc. 2025-32 summaries): https://www.betterment.com/help/federal-income-tax-brackets ; https://q3adv.com/?p=4105 ; https://paybrackets.com/2026-tax-brackets
- 2026 wage base $184,500 and 7.65%: https://www.mayerbrown.com/es/insights/publications/2025/12/irs-annual-limits-for-benefit-plans-2026-cost-of-living-adjustments
- 2026 deferral limit $24,500: https://www.venable.com/insights/publications/2025/11/2026-irs-dollar-limits-on-benefits-contributions

VERDICT: FIX

## Round 2 (editor)
Applied fix 1 (line 4: FICA taken on that $100 either way, $7.65 spoken in full) and fix 2 (line 8: death now spoken).
VERDICT: PASS
