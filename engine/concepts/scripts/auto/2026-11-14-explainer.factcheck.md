# Fact-check: 2026-11-14-explainer (Why gold rises when people panic)

Checked Oct 2, 2026 for posting Nov 14, 2026. Sources: WGC Gold Demand Trends FY2025 (gold.org); LBMA Precious Metals Market Report Q4/FY2025 and LBMA forecast survey ($3,431.54 2025 average); LBMA PM annual averages (NMA/metalcharts/ycharts excerpts); Bloomberg/NPR/Barchart on DXY; WGC Gold Market Commentary Dec 2025 (GRAM attribution).

## Verified
- 53 all-time highs in 2025 (LBMA PM): WGC FY2025. OK.
- 2025 average $3,431/oz, +44% y/y: WGC says $3,431 (+44%); LBMA itself reports $3,431.54. Recomputed 3431.54/2386.20 - 1 = +43.8%, so "44%" is fine. (A $3,435 figure was not found in any source. The chart title "(LBMA)" and the 2025 point agree, so the sources don't conflict.)
- Central banks bought 863 t in 2025: WGC FY2025. OK. (It was below the 1,000t+ of 2022-24, but "Even central banks bought" is still accurate.)
- Chart points (LBMA PM annual averages, rounded): 2007 695.39, 2008 871.96, 2009 972.35, 2010 1224.53, 2011 1571.52, 2012 1668.98, 2013 1411.23, 2014 1266.40, 2015 1160.60, 2016 1250.74 (to 1,251), 2017 1257.12, 2018 1268.49, 2019 1392.60, 2020 1769.64, 2021 1798.61, 2022 1800.09, 2023 1940.54, 2024 2386.20, 2025 3431.54. All 19 points match.
- 2008 +25%: 871.96/695.39 - 1 = +25.4%. OK.
- DXY 2025: Barchart -9.37% (rounds to -9.4%), other reports say -9.6% or "over 9%"; all call it the worst year since 2017. Supported.
- Fed: three cuts in 2025 to 3.50-3.75%. The script says only "scary times often bring rate cuts", which is consistent.
- Worked example math: $10,000 x 4% = $400; x 2% = $200. Correct.
- No price prediction, no advice, no political opinion. Disclaimers are in the post. Time words: everything is pinned to "2025" or "2008", so nothing goes stale by Nov 14.
- Spoken and on-screen numbers match on every line.
- Lengths: hook title "[53] record highs" 17 (<=22); list title 19; chart title 28 (at limit, OK); stat label 21, sub 21; compare subs 12/12; board lines <=20; building label "+863 t", caption 25; building kind fed with name "CENTRAL BANKS" set. All within limits.

## Required fixes

1. Line 1 (hook), overclaim of causation. WGC attributes 2025's gain to several roughly equal drivers: risk/geopolitical uncertainty, a weaker dollar and lower rates, momentum, and economic factors. Fear was not the only cause. Replace:
   - text: `In 2025, gold hit 53 record highs. Fear helped drive it.`
   - say: `In twenty twenty-five, gold hit fifty-three record highs. Fear helped drive it.`
   (11 words, dated, still a strong hook.)

2. Post text has the same overclaim. In `post.ig`, replace the first line `In 2025, gold hit 53 record highs. Fear did that.` with `In 2025, gold hit 53 record highs. Fear helped drive it.`

3. Line 6 (worked example), not labeled hypothetical, and the caption doesn't match the narration ("Example:" on screen, "Say" spoken). Replace:
   - text: `Second, scary times often bring rate cuts. Say $10,000 earns 4%: $400 a year. At 2%, $200. Gold's $0 looks less costly.`
   - scene.title: `Hypothetical: $10k, 1 yr` (24 chars)
   (Spoken line unchanged.)

Optional (not blocking): Line 9 board `Fear = demand` could read `Fear lifts demand` (17), which makes it a softer claim than an equation.

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-3 verbatim plus optional board text; hook prop changed chart-up -> tag so the 2025 label renders. VERDICT: PASS
