# Fact-check: 2026-11-13-explainer (Net worth explained with acorns)

Checked Oct 1, 2026 for a Nov 13, 2026 post. Independent web search (Fed SCF bulletin excerpts, Fed 2025 SCF press release, NerdWallet, Yahoo Finance, CNBC Select). Math recomputed in python.

## Verified claims
- 2022 SCF median family net worth $192,900 and mean $1,063,700: confirmed (Fed, "Changes in U.S. Family Finances from 2019 to 2022", Oct 2023). Both are in 2022 dollars, so "In 2022 ... $192,900" is correctly stated with no inflation adjustment needed. Mean/median = 5.5x.
- "Average family's net worth topped $1 million": fair. $1,063,700 is the SCF mean across all US families, and coverage widely describes it as average US family net worth topping $1M. "$1.06M" on screen matches "topped a million dollars" spoken.
- Under-35 median $39,000: Fed bulletin table shows 39.0 thousand (2022 dollars); third parties using the SCF microdata/interactive chart list $39,040. "$39,000" is a fair rounding of the Fed's published figure. (Technically "families whose head is under 35"; "families under 35" is acceptable shorthand.)
- 2025 SCF: fielded Mar-Dec 2025; Fed said results would be published "in late 2026". No evidence of release as of Oct 1, 2026. Prior cadence: 2019 results Sept 2020, 2022 results Oct 18, 2023, so a release before Nov 13, 2026 is plausible.
- Net worth definition (own minus owe) correct; can be negative.
- Worked example: 8,000 + 12,000 = 20,000; 20,000 - 25,000 = -5,000. Correct. Labeled "Example" in text, say ("Here's an example"), and scene titles ("Example squirrel", "Example net worth"). Assumptions reasonable.
- Negative net worth early on: SCF-based coverage says at least about 1 in 10 under-35 households owe more than they own (25th percentile negative), mostly student loans. "Common" is defensible.
- Spoken vs on-screen: all match ($1.06M / a million+; $192.9K / $192,900; $20,000, $25,000, -$5,000; $39,000).
- Label lengths: hook title "Average: [$1M+]" 15 (<=22); compare titles 25/16, labels 7/4, subs max 15 (<=18); stat labels max 26 (<=28), subs max 17; board lines max 18 (<=26); captions max 25. All pass.
- No advice, instructions, price predictions, or political opinion. Line 8 is descriptive, not instruction. Cover "Average Family: $1 Million?" is paid off by lines 1-2. CTA is series standard.
- No time words that go stale ("this year", "latest", "new") - every number is dated "in 2022".

## Required fixes
1. Pre-post check (Nov 12-13, 2026): search for the Fed's 2025 SCF results. If released, the script stays true as written (all figures are dated 2022), but update the post text so it does not imply 2022 is current. Replace in `post.ig` the line
   `Sources: Federal Reserve, Changes in U.S. Family Finances from 2019 to 2022 (Oct 2023).`
   with
   `Source: Federal Reserve, Survey of Consumer Finances 2022 (published Oct 2023). Figures in 2022 dollars.`
   (Use this replacement now regardless; it also adds the 2022-dollars note.) Do NOT add "latest" or "most recent" anywhere.

## Recommended (non-blocking)
2. Line 7 logic: "That's common early on" (about being below zero) is followed by a positive $39,000 median, which reads like a contradiction. Replace:
   - text: `Starting low is common. In 2022, families under 35 had a median of $39,000.`
   - say: `Starting low is common. In twenty twenty-two, families under thirty-five had a median of thirty-nine thousand dollars.`
3. Hook speed: line 1 say is 12 words but "twenty twenty-two" pushes it to ~3.5 s and opens on the date instead of the surprise. Put the date last:
   - text: `The average family's net worth topped $1 million in 2022.`
   - say: `The average family's net worth topped a million dollars in twenty twenty-two.`

VERDICT: PASS
