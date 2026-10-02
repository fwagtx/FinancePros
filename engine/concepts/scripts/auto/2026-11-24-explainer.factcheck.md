# Fact-check: 2026-11-24-explainer (Exempt vs non-exempt: who gets overtime)

Checked October 2, 2026, for posting on November 24, 2026. I worked from the script JSON and web searches only. I did not read the research brief.

## Verified claims (correct)
- **Overtime rule.** Under the FLSA, non-exempt workers get 1.5x their regular rate after 40 hours in a workweek, whether they are paid hourly or by salary. Correct.
- **Current salary floor.** The EAP salary floor is $684/week, and 684 x 52 = $35,568/yr. This is current as of 2026. The DOL rescission on May 13-14, 2026 reinstated the 2019 levels: $684/week and an HCE threshold of $107,432. (Sources: Ogletree, Foley Hoag, National Law Review, Butzel.)
- **History.** The floor was $455/week in 2004 ($23,660/yr). The 2019 final rule set $684, effective January 1, 2020. Correct.
- **2024 rule.** It was vacated nationwide by the E.D. Texas on November 15, 2024. The Fifth Circuit dismissed the appeal on May 5, 2026, and DOL rescinded the rule in May 2026. "Struck down that November and rescinded in May 2026" is accurate.
- **Overtime deduction (OBBBA).** It covers tax years 2025-2028. The cap is $12,500, or $25,000 on a joint return. Only the premium half of FLSA-required overtime counts. It phases out above $150k MAGI ($300k joint) at $100 per $1,000. The IRS FAQ was updated August 6, 2026 (FS-2026-13). The 2026 W-2 has separate reporting. Correct.
- **Math (recomputed).**
  - Straight time: 50 x $20 = $1,000.
  - With overtime: 40 x $20 + 10 x $30 = $1,100.
  - Deductible premium: 10 x $10 = $100.
- **Later changes.** I found nothing after September 2026 that changes these facts. DOL has said it may review the threshold in future rulemaking, but nothing has been proposed, so nothing should be stale on Nov 24.
- **"In 2026".** This is still true on the posting date.
- **Layout and other checks.**
  - The compare values "$1,000" and "$1,100" are 6 characters each, within the 7-character limit.
  - No keep:true flags are present.
  - The cover "Do You Get Overtime?" is answered by the video.
  - There is no advice and no political opinion. The tax law is not named in narration, and the "no tax on overtime" tag is the common descriptive name.
  - The hypothetical is labeled ("Hypothetical" / "Say").
- **Spoken words.** The script has 147 now and would have 149 with the fixes below. Both are within 100-150.

## Issues and fixes

### 1. Line 2: spoken value differs from on-screen value (must fix)
The text and board show "$35,568 a year", but narration says "about thirty-five thousand six hundred". The narration also skips the "$684 a week" that the caption shows.
- text: `That's the federal salary floor for most exempt white-collar jobs, which also need exempt duties: $35,568 a year.`
- say: `That's the federal salary floor for most exempt white-collar jobs, which also need exempt duties: thirty-five thousand five hundred sixty-eight dollars a year.`
- scene: unchanged (board "Exempt salary floor:" / "$684 a week" / "= $35,568 a year"). The $684 a week was already spoken in the hook.

### 2. Line 1 (hook): slightly overstated, and slow to say
"Usually means overtime pay" suggests the money is automatic. In fact a non-exempt salaried worker is paid overtime only for hours past 40. Some workers are also exempt with no salary test at all:
- teachers
- licensed doctors and lawyers
- outside sales
- computer employees paid at least $27.63/hr
- other FLSA §13 exemptions

"Usually" is a fair hedge only if it is framed as being *owed overtime* past 40 hours. The current 12-word hook runs about 3.5 seconds, and "In 2026" spends the opening on a date.
- text: `Paid under $684 a week? You're usually owed overtime.`
- say: `Paid under six eighty-four a week? You're usually owed overtime.` (10 words, about 3 seconds)
- scene: unchanged (title "Under [$684] a week", tag "2026 floor" / "$35,568", mood shock).

### 3. Line 6: eligibility overstated, and "New" is stale by November 2026
"Non-exempt workers can deduct" ignores several limits:
- the income phase-out ($150k/$300k MAGI)
- the requirement that the overtime be FLSA-required
- the SSN requirement
- the exclusion for married filing separately

The deduction is also from federal income tax only, not payroll taxes. By late 2026 it is in its second year, so "New" no longer fits.
- text: `From 2025 through 2028, eligible workers can deduct that overtime premium from federal income tax, up to $12,500, or $25,000 filing jointly.`
- say: `From twenty twenty-five through twenty twenty-eight, eligible workers can deduct that overtime premium from federal income tax, up to twelve thousand five hundred, or twenty-five thousand filing jointly.`
- scene: change only the sub to `$25,000 joint, 2025-2028, income limits`. If that is too long for the layout, keep `$25,000 joint, 2025-2028`.

### 4. Post captions: carry the same fixes and add the exemptions caveat
- **IG first line:** `Paid under $684 a week? You're usually owed overtime past 40 hours.`
- **IG and YT deduction sentence:** replace "non-exempt workers can deduct" with `eligible workers can deduct the overtime premium from federal income tax (income limits apply)`.
- **IG and YT, add one sentence:** `Some jobs, like teachers, doctors, lawyers and outside sales, have no salary test, and some states set higher floors.`
- **TikTok:** `Paid under $684 a week? You're usually owed overtime past 40 hours. Exempt vs non-exempt, explained. Not financial advice. #moneytok #overtime #financeprostv`

### 5. Minor narration (optional)
- **Line 5:** the mix of "two thousand four" and "twenty twenty" reads unevenly but is acceptable. "Six eighty-four" without "dollars" is fine because the screen shows $684.
- **Line 7:** OK.
- **Line 8 (CTA):** OK.

## Summary
Every fact and number checks out against current sources. The script fails on one mismatched number: line 2 speaks "about $35,600" while the screen shows $35,568. Two framing fixes are also needed:
- the hook should say "owed overtime", not that a low salary automatically means overtime pay
- line 6 should say eligibility is limited (income caps, FLSA-required overtime only)

VERDICT: FAIL

## Round 2

I re-read the updated raw.json. No new web searches were needed because no new factual claims were added.

**Fixes 1-4 are applied and correct:**
- **Line 1 (hook):**
  - Text and narration now match.
  - "Usually owed overtime" is fair framing. The salary-test exceptions are now stated in the IG and YT captions.
  - At 10 spoken words, it runs about 3 seconds.
- **Line 2:**
  - The text, narration and board now all say $35,568, which is 684 x 52.
  - The board's "$684 a week" matches the hook.
- **Line 6:**
  - The text and narration now say "eligible workers", "federal income tax" and "From 2025 through 2028", and they match each other.
  - The stat value $12,500 and the sub "$25,000 joint, 2025-2028" match the narration.
  - Leaving "income limits" out of the sub is acceptable because the caption covers it.
- **Post captions:**
  - IG and YT carry the eligibility caveat and the exemptions/state caveat.
  - All figures in the captions are correct.
  - The TikTok caption is 134 characters, within 150. It matches the hook and includes the 40-hour condition.

**Re-checks:**
- Spoken words: 149, within 100-150.
- Compare values: "$1,000" and "$1,100", 6 characters each.
- keep:true: none present.
- Math, dates and the cover payoff are unchanged and correct.
- No advice and no political opinion.
- Nothing becomes stale by November 24, 2026.

**Optional nit (not blocking):** in line 6, "that overtime premium" has no direct antecedent, because line 5 is about the timeline. To fix it, change "that" to "the" in both text and say:
- text: `From 2025 through 2028, eligible workers can deduct the overtime premium from federal income tax, up to $12,500, or $25,000 filing jointly.`
- say: `From twenty twenty-five through twenty twenty-eight, eligible workers can deduct the overtime premium from federal income tax, up to twelve thousand five hundred, or twenty-five thousand filing jointly.`

VERDICT: PASS
