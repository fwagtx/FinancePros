# Fact-check: 2026-10-07-explainer (Compound interest: the acorn snowball)

Checked 2026-09-30 for posting 2026-10-07. Research brief not read. Math recomputed in Python (10000 * 1.07^n).

## Math (all correct)
| Claim | Script | Recomputed |
|---|---|---|
| Year 1 gain | $700 | $700.00 |
| Chart points y0..y40 | 10000, 14026, 19672, 27590, 38697, 54274, 76123, 106766, 149745 | 10000, 14025.52, 19671.51, 27590.32, 38696.84, 54274.33, 76122.55, 106765.81, 149744.58 (all round correctly) |
| Year 40 alone adds | $9,796 | $9,796.37 |
| Last 10 yrs adds | $73,622 | $73,622.03 (49.2% of final pile, so "about half" is fair) |
| Start 35 vs 25 at 65 | $76,123 vs $149,745 | ratio 50.8%, so "cut in half" is fair |

## Facts
- Line 8 (JSON L147-154): S&P 500 1928-2025 about 10% a year, compounded with dividends, per NYU Stern (Damodaran). VERIFIED. Sources put the compound (geometric) rate at about 10.0% (10.02%). The arithmetic average is about 11.7%. The label "compounded" is right. The phrase "brutal down years" is fair: 26 of 97 years were negative, and the worst was 1931 at -43.8%.
- Line 9 (L159-167): the average card rate on accounts assessed interest was 22.15% in Q2 2026, per Federal Reserve G.19. VERIFIED. Q1 2026 was 21.52%. The all-accounts rate was 20.94%, and the script correctly specifies "charged interest". This is the latest quarterly figure: Q3 comes out in the November G.19, so it is not stale on Oct 7.
- federalreserve.gov was blocked by the proxy. The G.19 figure was confirmed from search excerpts of the G.19 release and The Money Overview / LendingTree coverage.

## Issues
1. Line 8 (L147-148), minor: "Is 7% realistic?" is followed only by "about 10%", so the question is never actually answered. It can also read as "7% is conservative", a soft forward-looking implication. Fix: add the real return. Text: "Is 7% realistic? From 1928 through 2025, US stocks averaged about 10% a year, roughly 7% after inflation, with brutal down years." Say it the same way. Optionally add "Past returns aren't a promise."
2. Line 5 (L61-62), minor on-screen/spoken mismatch: the caption says "$9,796" and the narration says "almost ten thousand". The meaning is consistent, but the rule asks for matching values. Fix: say "nine thousand, seven hundred ninety-six", or change the caption to "almost $10,000".
3. Line 9 (L159-160), minor on-screen/spoken mismatch: the caption and stat show "22.15%" and the narration says "about twenty-two percent". This is acceptable rounding. For an exact match, say "twenty-two point one five percent" or show "~22%" in the caption and keep 22.15% in the stat.
4. Hook, line 1 (L13-14): the line is true, fits in about 3 seconds and works. It could be stronger with concrete numbers, which also creates a "how?" gap. Suggested: "Same $10,000. One saver ends with $150K, the other $76K." (on screen: "Same $10K: $150K vs $76K"). Alternative: keep the current line and add a number: "Waiting ten years can cut your pile in half, even with the same money."
5. Post tags (L199): "rule of 72" is never mentioned in the video. Fix: drop the tag, or add one line such as "At 7%, money doubles about every 10 years (rule of 72)." That line would also explain the hook neatly: 72/7 = 10.3 years.
6. Line 7 narration (L127) is long but reads fine. Optional trim: "Start at twenty-five: about a hundred fifty thousand by sixty-five. Start at thirty-five: about seventy-six thousand."

## Other checks
- Cover and title ("Why Starting Later Costs Half", "10 years later / HALF"): paid off by lines 6-7. OK.
- Time words: none will be wrong on Oct 7, 2026. "Q2 2026" is explicit. OK.
- Advice or price predictions: none. The 7% is labeled as an example throughout, and the post carries "not financial advice". OK (see issue 1 for wording).
- Political opinion: none.
- The chart end label "$149,745" matches point 40, and the compare subs match the chart points.

VERDICT: PASS
