# Fact-check: 2027-01-16-explainer ("GDP: what it measures and what it misses")
Posting: Sat Jan 16, 2027, noon CT. Checked: Nov 17, 2026. Independent verification; brief not trusted, research.md not read.

## Verified facts (all hold)
| Claim | Result | Source |
|---|---|---|
| US nominal GDP 2025 = $30.86T | TRUE: 30,861.292 bn (FRED vintage 2026-09-30, post annual update) | https://fred.stlouisfed.org/series/GDPA |
| US nominal GDP 2024 ~ $29.38T | TRUE: 29,380.991 bn | https://fred.stlouisfed.org/series/GDPA |
| Real GDP growth 2019-2025: 2.6, -2.1, 6.3, 2.4, 2.9, 3.0, 2.3 | TRUE, all 7 points match (vintage 2026-09-30) | https://fred.stlouisfed.org/series/A191RL1A225NBEA |
| BEA annual update released Sept 30, 2026 | TRUE | https://www.bea.gov/news/blog/2026-08-17/annual-update-gdp-industry-and-state-stats-publicly-available-starting-sept-30 |
| Nominal growth 2025 ~ 5.0% (our math) | TRUE: 30,861.292 / 29,380.991 = 1.0504 -> 5.0%. Implied price growth 1.0504/1.023 = 2.7%, i.e. ~54% of nominal growth, so "over half was higher prices" is correct | computed from FRED GDPA + A191RL1A225NBEA |
| 2020 is the only negative year in 2019-2025 | TRUE (within the chart window only; 2009 etc. were also negative, so "here" was added) | FRED A191RL1A225NBEA |
| BEA study: household production would raise 2010 GDP ~26% | TRUE: "raises the level of GDP 39 percent in 1965 and 25.7 percent in 2010" (Bridgman et al., SCB May 2012) | https://apps.bea.gov/scb/pdf/2012/05%20May/0512_household.pdf |
| Kuznets 1934: welfare can scarcely be inferred from national income | TRUE (1934 report to Congress, "National Income, 1929-1932") | https://ec.europa.eu/newsroom/env/items/33780/en ; https://theconversation.com/beyond-gdp-heres-a-better-way-to-measure-peoples-prosperity-168023 |

Note on staleness: 2025 remains the latest full annual figure on Jan 16, 2027 (2026 advance annual estimate comes later in Jan/Feb 2027; next annual revision Sept 2027). No relative time words ("this year", "last year", "now") used. No advice, price predictions or political opinion found.

## Issues found and fixes applied
1. **Line 0 hook too long (12 words, ~4s) and imprecise.** "GDP counts $0" for mowing your own lawn is overstated: your mower, gas and seed purchases do count; only your unpaid labor is valued at $0. "Pay someone, it counts" also adds length.
   - Fix: text "Mowing your own lawn? GDP values it at $0." / say "Mowing your own lawn? GDP values it at zero." (9 words, ~2.7s; true; open question pays off in line 6).
2. **Line 1 board "final goods & svcs"**: abbreviation reads poorly on screen.
   - Fix: board lines ["GDP = market value", "of final output"] (18 / 15 chars).
3. **Line 2 screen/spoken mismatch**: screen "$30.86T" and text "$30.86 trillion" vs spoken "about thirty point nine trillion".
   - Fix: text "In 2025, US GDP was about $30.9 trillion."; stat value "$30.9T" (spoken unchanged). Exact $30.86T kept in post copy.
4. **Line 4 "The only drop was 2020"**: true only for the chart window.
   - Fix: "The only drop here was 2020..." (text and say).
5. **Line 5 screen/spoken mismatch and awkward read**: screen "5.0%" vs spoken "about five percent"; "so much of that was higher prices" is vague.
   - Fix: compare left value "5%"; text "Before the inflation adjustment, our math says it grew about 5%, so over half was higher prices." / say "... about five percent, so over half was higher prices." (math verified: 2.7 of 5.0 points).
6. **Line 6 hook payoff weak / text-say mismatch** ("misses" vs "it misses"); hook's "pay someone" payoff not spoken.
   - Fix: text = say = "GDP counts paid work, like a hired lawn crew or crash repairs, but it misses unpaid chores, free time and pollution."
7. **Line 7 awkward narration and confusing sub**: "A B E A study" reads badly; sub "BEA study, 2010" mixes study year (2012) with data year (2010).
   - Fix: text "A government study found unpaid home work would have added about 26% to 2010 GDP." / say "... about twenty-six percent to twenty ten GDP."; stat label "2010 GDP boost", sub "BEA, 2012 study".
8. **Line 8 "its creator Simon Kuznets"**: overstated. Kuznets built the first US national income estimates (1934); his warning was about national income; GDP as the headline measure came later. Board mood "happy" also clashes with a warning.
   - Fix: text "National income pioneer Simon Kuznets warned in 1934: it measures size, not well-being." / say "... nineteen thirty-four ..."; mood "think".
9. **Post copy** aligned: IG/TikTok hook lines reworded to "values that work / values it at $0"; IG nominal growth "about 5%" with "over half was higher prices"; "2012 BEA study" in IG and YouTube description. TikTok kept <=150 chars.

Cover ("What GDP Misses", LAWN, $0) is paid off by lines 0, 6 and 7. Chart lines 3 and 4 have identical points. All spoken numbers now match on-screen values.

## Check
`python3 check.py 2027-01-16-explainer` -> OK: 10 lines, 138 spoken words, hook 9 words.

VERDICT: PASS

## Round 2 (editor)
Reviewed applied fixes: hook 9 words and accurate (labor valued at $0), screen values match speech, study year vs data year clarified, Kuznets wording softened.
VERDICT: PASS
