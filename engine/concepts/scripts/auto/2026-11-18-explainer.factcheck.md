# Fact-check: 2026-11-18-explainer (price elasticity)

Checked Oct 2, 2026. eia.gov blocks direct fetch from here, so figures come from search excerpts quoting EIA pages and from reputable secondary sources. All math was recomputed in python.

## Verified
- EIA annual average US regular gasoline: 2021 $3.01, 2022 $3.95 (+31.2%, so "jumped 31%" is correct). 2023 $3.52, 2024 $3.30 (one EIA note implies $3.31; a rounding difference that is not spoken), 2025 $3.10 (EIA: "averaged $3.10/gal in 2025, $0.21 less than 2024"). Chart points and the "$3.10" end label are OK.
- EIA finished motor gasoline consumption: 2021 8.82M b/d (135.14B gal), 2022 8.78M b/d. Change -0.45% (-0.23% if the 2021 figure is the revised 8.80). "Fell less than 1%" and "barely bought less" are accurate.
- Cigarettes: NCI monographs, CDC and Tobacco Free Kids cite a 3-5% drop in *overall cigarettes consumed* per 10% price rise. The numbers are correct, but the wording should say consumption, not smoking (see fix 3).
- Hypothetical: +10% ($4.00 to $4.40), -1% (10 to 9.9 gal), elasticity -0.1, bill $40.00 to $43.56. All correct, and the example is clearly labeled hypothetical.
- Hook: true and specific. First sentence runs about 2.5s. Hook title "Gas [+31%] in 2022" = 16 chars (limit 22). Hook prop is car with label "2022" (OK). Cover is paid off.
- Spoken and on-screen values match. Neutral tone, no advice or predictions, no time words that will be wrong on Nov 18.

## Required fixes
1. **Line 2 chart title is 29 chars (limit 28).** Replace `"Regular gas, yearly avg (EIA)"` with `"Regular gas yearly avg (EIA)"` (28).
2. **Line 8 stat label is 31 chars (limit 28).** Replace `"Less smoking per 10% price rise"` with `"Fewer cigarettes smoked"` (23), and the sub `"Natl Cancer Institute, CDC"` with `"Per 10% price rise; NCI, CDC"` (28).
3. **Line 8 wording, consumption vs prevalence.** The research measures cigarettes consumed, not the number of people who smoke. Change text to `"Cigarettes too: a 10% price rise cuts cigarettes smoked only about 3 to 5%."` and say to `"Cigarettes too: a ten percent price rise cuts cigarettes smoked only about three to five percent."` Make the same change in the post: in ig change "cuts smoking about 3-5%" to "cuts cigarettes smoked about 3-5%", and in yt_desc change "cutting smoking about 3-5%" to "cutting cigarettes smoked about 3-5%".
4. **Lines 3-4 overclaim causation.** 2022 demand was also being pushed *up* by the post-COVID driving rebound, so the tiny drop is not a clean measure of elasticity. The real price response was probably somewhat larger and is hidden by the rebound. Hedge line 4: text `"Part of the answer is price elasticity: % change in amount bought ÷ % change in price."` and say `"Part of the answer is price elasticity: percent change in amount bought, divided by percent change in price."` (Leave the board lines unchanged.)

## Recommended (not blocking)
5. Line 3 compare: the right-side value `"<1%"` gives no direction next to "+31%". Consider `"-0.5%"` with sub `"8.82M to 8.78M b/d"` (18). Alternatively, set tone to "down" and keep "<1%".
6. Line 7: "and the seller earns more" could read as profit. "and sellers collect more" (revenue) is more precise.

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-4 and both optional notes verbatim. VERDICT: PASS
