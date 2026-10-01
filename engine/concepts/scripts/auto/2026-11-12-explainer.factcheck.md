# Fact-check: 2026-11-12-explainer (posts Nov 12, 2026; checked Oct 1, 2026)

Source read: `2026-11-12-explainer.raw.json` only. federalreserve.gov and jpmorganchase.com are blocked for direct fetch, so checks rely on search-result excerpts of the official pages. The math was recomputed in Python.

## Verified claims

| Line | Claim | Status |
|---|---|---|
| L1 / cover / post | 30% of US adults had income that varied in 2025 | Matches the Fed SHED 2025 report (May 2026): "30 percent of adults had income that varied at least occasionally," similar to 2024 and up from 28% in 2023. See the wording issue below. |
| L2 | 11% struggled to pay bills because income varied (2025) | Matches the Fed: "11 percent of adults reported they struggled to pay their bills in the prior 12 months because their income varied, similar to 2024." The denominator is all adults, not only those whose income varied. |
| Chart 2024 = 11 | Matches | 2024 report: 11%, "up slightly from 10 percent in 2023." |
| Chart 2023 = 10 | Matches | 2023 report: 10%, "similar to 2022." |
| Chart 2022 = 10 | Probably right | Implied only by "similar to 2022" in the 2023 report. I could not see the exact 2022 figure in excerpts. |
| Chart 2021 = 9 | Probably right | 2021 report: "Thirty percent of those who experienced varying monthly income, representing slightly less than 1 in 10 adults overall, said they struggled to pay their bills..." That is consistent with 9% of all adults, but no excerpt gave an exact integer. |
| L3 | JPMorgan Chase Institute, *Weathering Volatility 2.0*, Oct 2019, 36% | Matches: families at the median "experienced a 36 percent change in income month-to-month." The data covers more than 6 million Chase checking-account families, 2013–2018. "Typical family" is a fair plain-English version of "median." |
| L4–L7 math | $21,600 / 6 = $3,600; $5,000 − $2,600 = $2,400; 20% × $2,600 = $520; 20% × $5,000 = $1,000 | All correct. A six-month set with a $2,600 low, a $5,000 high and a $21,600 total is possible (the other four months would average $3,500). |
| Sub-labels ≤ 28 characters | All pass | Longest are "Struggled to pay bills (Fed)" at 28 and "Median monthly income swing" at 27. |
| Advice | None found | The methods are described with "One approach is…", "Some add…" and "Others use…". The post carries a not-advice disclaimer. No price predictions and no political content. |
| Staleness / time words | OK | "In 2025" is still correct on Nov 12, 2026. The 2025 SHED is the latest; the next comes about May 2027. |
| On-screen vs spoken | Match | All values agree. |

## Issues

1. **L8, factual error in the summary.** "All three treat the low month as the plan and the high months as extra" is not true of the percentage method. That method scales with each month's pay, and the list on the same screen says "Percent: scales with pay." The "smooth it out" buffer also plans around the average, not the low month. **Fix:** "All three are ways to keep a low month from breaking the budget." Or, if the claim should stay narrow: "Baseline and buffer both treat the low month as the plan."

2. **L1 / scene title / cover / post, hook drops "at least occasionally."** The Fed measure is income that varied at least occasionally, so it counts people who said "occasionally" as well as "often." "Had income that varied" is close enough. "Had uneven pay" (scene title, cover, post title, TikTok) goes further: it suggests regular swings in wages. **Fixes:**
   - Caption: "In 2025, 30% of US adults said their income varied at least sometimes."
   - Scene title: "[30%] had income vary" (21 characters).
   - Cover / post: "Income that varies? 3 ways people budget" and "30% of adults saw their income vary in 2025."

3. **L1, hook strength and length.** It is true and specific, but about 13 spoken words takes roughly 3.5–4 seconds, and it creates little tension. **Stronger option:** "Nearly 1 in 3 US adults had income that swung last year." Or lead with the tension: "1 in 9 adults struggled to pay bills just because their pay swung." That uses the 11% figure. Note that "last year" means 2025 only while posting in 2026, which holds for Nov 12.

4. **L2 chart title is ambiguous.** "Struggled to pay bills (Fed)" can be read as all bill hardship, which the Fed measures separately (about 17–18% didn't pay all bills in full). **Fix:** "Bills hard: income varied" (25 characters). Optionally add "% of all adults" in the scene.

5. **L2, 2021 baseline is soft.** 9% is "slightly less than 1 in 10" in the source text. It is fine to keep, but the "up from 9%" claim rests on a rounded figure and a 2-point move. **Optional fix:** "…up from about 9% in 2021." If the generator has the SHED data appendix value, confirm the exact 2021 and 2022 figures.

6. **L3, sample caveat (minor).** The 36% comes from Chase checking customers, 2013–2018, and is now 7 years old. Consider a sub-label like "Chase data, 2013–18" or narration "…found the typical family in its data…". This is not required.

7. **L6, buffer math framing (minor).** "the extra $2,400" is extra over the $2,600 baseline, not over the $3,600 average (which would be $1,400). The list then calls the buffer "smooth it out," which suggests paying yourself the average. **Fix:** "In the $5,000 month, the $2,400 above the baseline goes to a holding account."

8. **Style nits.** "That's the money." reads oddly when spoken. The post title "How people budget it" is awkward; "How people budget for it" reads better.

VERDICT: FAIL

## Round 2 (re-check of the revised raw.json, Oct 1, 2026)

### Fixes confirmed

| Round 1 issue | What the revision does | Status |
|---|---|---|
| 1. L8 summary was false | Now reads "All three are ways to keep a low month from breaking the budget." That is true of all three methods. | Fixed |
| 2. Hook overstated | Caption keeps "had income that varied at least occasionally" and says "(30%)". Scene title is "[30%] had income vary". Cover is "Income Varies? 3 Ways People Budget". IG and YouTube text keep "at least occasionally". | Fixed |
| 3. Hook was weak and slow | Spoken hook is now "nearly one in three US adults saw income swing", about 12 words, roughly 3 seconds. "Nearly 1 in 3" is a fair rounding of 30%, and the caption shows 30%, so the spoken and on-screen values agree. | Fixed |
| 4. Chart title ambiguous | Now "Bills hard: income varied" (25 characters). The caption also says "11% of all adults", which states the denominator correctly. | Fixed |
| 5. 2021 baseline soft | Now "up from about 9% in 2021", matching the source's "slightly less than 1 in 10." | Fixed |
| 6. JPMC sample caveat | Narration now says "study of Chase data", the sub-label is "Chase data, 2013-18", and the post states the data range. "Typical family's income changed 36% month to month" fairly represents the median 36% figure. | Fixed |
| 7. Buffer framing | Now "the $2,400 above baseline", with the label "Above baseline". $5,000 − $2,600 = $2,400 is correct. | Fixed |
| 8. Style nit (post title) | Now "How people budget for it". | Fixed |

### Does "saw income swing" fairly represent "varied at least occasionally"?

Yes, with a caveat. "Swing" suggests somewhat bigger changes than "varied occasionally." It is spoken narration, though, and the on-screen caption at the same moment shows the exact Fed wording, "varied at least occasionally." I judge it acceptable, not misleading. If you want zero ambiguity, "saw their income vary" scans just as fast.

### New errors

None found. All values are unchanged and the math still holds:
- $21,600 / 6 = $3,600
- $5,000 − $2,600 = $2,400
- 20% of $2,600 = $520 and 20% of $5,000 = $1,000

### Remaining minor nits (no change needed)

- The post title "30% saw income vary in 2025" leaves out "of US adults". The IG, YouTube and TikTok text all include it.
- The list title "Uneven pay methods" and the header "your pay changes" still say "pay". These are topic labels, not stat claims, so they are fine.
- "That's the money." still reads a little oddly out loud. It is a house-style sign-off.

### Label lengths

All 28 characters or fewer. The longest are "Median monthly income swing" (27), "Bills hard: income varied" (25), "Percent: scales with pay" (24) and "plan on the lowest month" (24).

### Advice check

No advice: the methods are still described, not instructed.

VERDICT: PASS
