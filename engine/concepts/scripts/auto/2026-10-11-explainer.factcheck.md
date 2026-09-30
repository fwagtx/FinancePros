# Fact-check: 2026-10-11-explainer (posts Oct 11, 2026)

## Verified facts (Experian State of the Automotive Finance Market, Q2 2026)
- Average new-car loan $43,610: CONFIRMED (Experian Ask Experian blogs, search excerpts).
- Average new-car rate 6.35%: CONFIRMED.
- Rates by credit tier: super prime (781-850) 4.41%, subprime (501-600) 13.52%: CONFIRMED. (Full table: 4.41 / 6.15 / 9.71 / 13.52 / 16.11.) Labels "Score 781+" and "Score 501-600" match.
- New-car loans over 72 months: 35.55% in Q2 2026 (up from 30.83% in Q2 2025), so ">35% ran past six years" is CORRECT. Note: Experian's press headline says "nearly one-third" for ALL loans; the script correctly says new-car loans.
- Experian's actual average new-car monthly payment was $765. The script's $730 is a labeled hypothetical (72 months), not a claim about the average payment, so it's OK.

## Math (standard amortization, fixed rate, no fees; recomputed in python)
- $43,610 at 6.35%, 72 mo: $729.97/mo, $8,947.87 interest -> $730 / $8,948 CORRECT.
- 84 mo: $644.42/mo, $10,521.42 interest -> $644 / $10,521 CORRECT.
- Difference: $1,573.54 -> "about $1,600" is acceptable rounding. "About $1,570" would be more precise (optional).
- 4.41%, 72 mo: $6,103 interest -> "about $6,100" CORRECT.
- 13.52%, 72 mo: $20,286 interest -> "about $20,300" CORRECT.
- Hook "almost $9,000": $8,948, CORRECT.

## Other checks
- On-screen and spoken values match on every line.
- Line 4: the caption says "Example:" but the narration drops it. Minor. Fix: start the narration with "For example, over seventy-two months..."
- Line 8: the caption says "Same loan, 72 months" but the narration drops it, so a listener could take $6,100/$20,300 as general figures. Fix: "Credit matters too. Same loan, same term: four point four one percent costs about sixty-one hundred..."
- Hook (line 1): true and specific, and the cover ($9,000) pays it off. Read aloud it runs about 3.5 s, a bit over the 3-second target. Optional trim: "A normal car loan can cost nine grand in interest." Also, the $9,000 depends on the 72-month assumption, which the next lines disclose. Acceptable.
- Time words: "In Q2 2026" / "That quarter": these are fixed dates and stay correct on Oct 11. The Q2 report is still the latest Experian release at posting (the Q3 report usually comes out in December). Not stale.
- No advice or price predictions. Line 9 is descriptive, not an instruction. No political content. No quotes. Both the post text and the description say "not financial advice" and state the math assumptions.

## Issues summary
1. (Minor) Line 8 narration omits "same loan, 72 months". Add "Same loan, same term".
2. (Minor) Line 4 narration omits "Example". Add "For example".
3. (Minor) Line 6: $1,574 rounds to "about $1,600". Acceptable; "about $1,570" is optional.
4. (Minor) The hook runs slightly over 3 s. Optional trim.

VERDICT: PASS
