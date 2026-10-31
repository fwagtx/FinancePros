# Fact-check: 2026-12-30-explainer (dental insurance annual maximums)
Checked Oct 31, 2026 for posting Wed Dec 30, 2026. Independent checker.

## Sources verified
- ADA News, "Dear ADA: Annual maximums" (Mary Beth Versaci, Dec 19, 2025), read in full: confirms "many still are promoting the long-standing $1,000 level that was established some 40 years ago"; NADP 32.8% / 48.2% / 17.2%; "a 2024 analysis by the ADA Health Policy Institute shows that only 3.4% of dental patients actually reach the typical annual maximum"; "the familiar design is 100% coverage for preventive, 80% for basic and 50% for major services". The "50 years" wording appears only in the member's question and the page description, not in the ADA's answer, so the hook's "40-year-old number" follows the ADA's own answer and is fair.
- BLS data.bls.gov CUUR0000SEMC02 (extracted Oct 31, 2026): every December value matches the brief exactly: 1985 116.8, 1990 159.9, 1995 210.4, 2000 262.2, 2005 329.6, 2010 402.386, 2015 455.459, 2020 514.957, 2025 628.951 (Oct 2025 missing due to the lapse; December unaffected).
- Chart math recomputed (1000 x index / 116.8): 1000, 1369.01, 1801.37, 2244.86, 2821.92, 3445.09, 3899.48, 4408.88, 5384.85. All chart points and "$5,385" correctly rounded.
- Waiting periods: Delta Dental (6-12 mo restorative, 12 mo often standard for major), Guardian (6 mo basic, 12 mo major example), Humana (6 or 12 mo major). "Some plans ... often 6 months for basic, 12 for major" is supported.
- Reset/rollover: Delta Dental of Arkansas (calendar-year benefit period, max resets; unused benefits typically do not roll over unless carryover feature) plus multiple dental sites agree. "Many plans reset on January 1" is accurate and correctly hedged.
- Worked example: 50% x $1,400 = $700 > $500 remaining, so plan pays $500; you pay $1,400 - $500 = $900. Correct, labeled "Our math" and "(example)".
- Hook, cover ("40-Year-Old Cap" / MAX $1,000) and header are paid off by line 2 and line 3. No advice, no predictions, no political opinion. No stale time words (all figures dated: Dec 2025, 2024, 1985-2025).

## Issues

1. lines[3] say: spoken value differs from on-screen value ("about fifty-four hundred" vs on-screen "$5,385").
   - Replace say with: "Our math: a thousand dollars of nineteen eighty-five dental care cost fifty-three hundred eighty-five dollars in twenty twenty-five."
   - text unchanged: "Our math: $1,000 of 1985 dental care cost $5,385 in 2025."

2. lines[7] say: spoken "about three percent" differs from on-screen "3.4%".
   - Replace say with: "Only three point four percent of patients reach the typical max, per an A D A analysis."
   - text unchanged: "Only 3.4% of patients reach the typical max, per an ADA analysis."

3. (Optional, minor) lines[0] scene: card reads "MAX / 40 yrs", which can look like a maximum of 40 years. Suggested: "label": "MAX SET", "value": "~40 yrs ago". text/say unchanged.

No other issues found in lines[1], [2], [4], [5], [6], [8], [9], cover, header, post.title, post.ig, post.tiktok, post.yt_desc or tags.

VERDICT: FAIL

## Round 2 (editor)
- lines[7] say: "three point four percent".
- lines[3]: kept "about fifty-four hundred" spoken with exact $5,385 on screen (house rule: round spoken numbers with "about").
- Hook prop label "SET" so "40 yrs" reads as age of the cap.
VERDICT: PASS
