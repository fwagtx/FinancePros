# Fact-check: 2026-11-29-explainer (cost of raising a kid)

Checker: independent, October 2, 2026. Posting date: Sunday, November 29, 2026. Sources: web search excerpts (USDA/CNPP press release and report, Brookings PDF and coverage, LendingTree study page and coverage, Child Care Aware of America (CCAoA) reports and releases). Math recomputed in Python.

## Verified claims

| Claim | Status | Source notes |
|---|---|---|
| USDA: child born 2015, middle-income married couple, $233,610 birth through age 17 | Verified | USDA/CNPP "Expenditures on Children by Families, 2015" (Jan 2017). It is in 2015 dollars; $284,570 with USDA's projected 2.2% inflation. "USDA, 2015 dollars" label is correct. |
| Shares: housing 29, food 18, childcare/education 16, transportation 15, health 9, misc 7, clothing 6 | Verified | USDA release and coverage. Total 100. |
| Housing + food + transportation = 62% | Verified | 29+18+15 = 62. |
| Brookings 2022: $310,605 | Verified | Brookings (Aug 2022): child born 2015, middle-income married couple with two kids, through age 17, assuming 4% inflation 2021-2032. Nominal (future) dollars, $26,011 above USDA's own inflation-projected $284,570. |
| $310,605 / 18 = $17,256 a year; about $1,438 a month | Verified | 17,255.83 and 1,437.99. Birth through age 17 = ages 0-17 = 18 years, correct. (Some news coverage says "more than $18,000 a year" by dividing by 17; the script's 18 is correct.) |
| LendingTree 2026 report: $303,418 over 18 years, mostly 2024 data | Verified | LendingTree study; up 1.9% from $297,674. |
| CCAoA national average price: 2022 $10,853; 2023 $11,582; 2024 $13,128; 2025 $13,184 | Verified as published | Each is CCAoA's headline figure (average of three methods). |
| 2025: 10% of median income for married couples, 33% for single parents | Verified | CCAoA 2025 Price & Supply (released May 2026). |

## Issues

1. **Hook, cover and post title are not framed as an average, and the video contradicts them (blocking).** "A kid's biggest cost? Housing, not daycare." is true only for the USDA average across all middle-income families, many of which pay nothing for childcare. For families who pay for daycare, it is usually the biggest cost. The script shows this itself: line 6's $13,184 a year in daycare is more than USDA's whole average yearly cost per child ($233,610 / 18 = about $12,978 in 2015 dollars) and about 3.5x USDA's housing share (about $3,764 a year). As written, the hook is a universal claim the video's own numbers disprove. Fix: frame lines 1 and 6, the cover and the post as the average.
2. **Line 4: the comparison is misleading (should fix).** "Brookings added higher inflation" puts $233,610 (2015 dollars) next to $310,605 (future nominal dollars at 4% inflation). Most of the gap comes from switching to future dollars, not from "higher" inflation alone; USDA's own inflated figure was $284,570. Say that Brookings counted in future dollars.
3. **Line 3: on-screen label differs from the spoken one (minor).** It says "childcare and school sixteen", but the screen shows "Childcare 16%". USDA's category is childcare and education.
4. **Line 8: awkward wording (minor).** "lands near" is followed by an exact figure ($303,418). Use "says".
5. **Line 6 chart: years are not strictly comparable (minor, not blocking).** All four years use CCAoA's three-method average, but the states covered change each year (for example, 49 states plus DC in 2024 and 47 states in 2025). Part of the 13% jump from 2023 to 2024 may come from that. Treat it as a series of headline figures, not a precise trend. Optional: note "state coverage varies by year" in the post.
6. **Stale news / time words:** none wrong on Nov 29, 2026. USDA's 2015-cohort report (2017) is old but is still USDA's latest, and the script dates it. CCAoA 2025 (released May 2026) and LendingTree 2026 are current. No "this year" or "now" wording.
7. **Advice, predictions, politics:** none. Post disclaimers are present.
8. **Layout:** compare values "10%" and "33%" are within 7 characters. There are no keep:true lines.
9. **Opening strength:** after the fix below it stays specific, true and about 2.7 s (8 words), and makes viewers want the answer.

## Exact replacements (spoken total stays 149 words)

**Line 1** (+1 word)
- text: `The average kid's biggest cost? Housing, not daycare.`
- say: `The average kid's biggest cost? Housing, not daycare.`
- scene: unchanged.

**Line 3** (0 words)
- scene.items[2]: `Childcare/ed 16%`

**Line 4** (+1 word)
- text: `Brookings' 2022 update, in future dollars with higher inflation: $310,605.`
- say: `Brookings' twenty twenty-two update, in future dollars with higher inflation: three hundred ten thousand, six hundred five dollars.`
- scene.to.label: `Brookings, future $`

**Line 5** (-2 words)
- text: `Over 18 years (birth to 17), that's $17,256 a year, about $1,438 a month.`
- say: `Over eighteen years, that's seventeen thousand, two hundred fifty-six dollars a year, about fourteen hundred thirty-eight a month.`
- scene.lines[0]: `$310,605 / 18 years (0-17)`

**Line 6** (+1 word)
- text: `Paying for daycare? It can top housing: $13,184, the 2025 national average.`
- say: `Paying for daycare? It can top housing: thirteen thousand, one hundred eighty-four dollars, the twenty twenty-five national average.`
- scene.title: `Avg US childcare (CCAoA)`

**Line 8** (-1 word)
- text: `LendingTree's 2026 report, with different math, says $303,418.`
- say: `LendingTree's twenty twenty-six report, with different math, says three hundred three thousand, four hundred eighteen dollars.`

**Cover**
- title: `Avg Kid's #1 Cost? Housing`

**Post**
- title: `On average, a kid's biggest cost is housing, not daycare (USDA data)`
- ig, first paragraph: `The average kid's biggest cost? Housing, not daycare. But if you pay for daycare, it can top housing.`
- ig, Brookings line: `Brookings (2022) redid it in future dollars with higher inflation: $310,605, or about $17,256 a year over 18 years.`
- tiktok: `On average, a kid's biggest cost is housing (29% per USDA), not daycare. Paying for daycare can change that. Not financial advice. #moneytok #personalfinance #parenting #childcare #financeprostv`
- yt_desc, first sentence: `USDA's 2017 report put a child born in 2015 at $233,610 through age 17 (2015 dollars), with housing the biggest average share at 29%.` Also change "Brookings' 2022 inflation update" to "Brookings' 2022 update in future dollars".

Word count after fixes: 149 (+1 +1 -2 +1 -1 = 0).

## Sources
- https://ktla.com/news/nationworld/it-costs-an-average-of-233610-to-raise-a-child-usda/
- https://content.govdelivery.com/accounts/USDAOC/bulletins/17f19c9
- https://www.fna.usda.gov/research/cnpp/expenditures-children-families
- https://www.brookings.edu/wp-content/uploads/2022/08/brookings_cost-to-raise-a-child_inflation-adjusted-2.pdf
- https://www.northernnewsnow.com/2022/08/24/310605-price-be-parent-age-inflation/
- https://www.lendingtree.com/debt-consolidation/raising-a-child-study/
- https://www.cbsnews.com/news/cost-to-raise-a-child-300000-us-state-by-state/
- https://info.childcareaware.org/media/child-care-prices-rival-major-household-expenses
- https://www.childcareaware.org/ccaoas-methodology-2025/
- https://www.childcareaware.org/price-landscape24/
- https://www.childcareaware.org/thechildcarestandstill/
- https://www.childcareaware.org/catalyzing-growth-using-data-to-change-child-care-2022/

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-6. The post title is shortened to 51 characters and the TikTok caption to 150 or fewer. The cover title is "Avg Kid's #1 Cost? Housing". VERDICT: PASS
Rebuild: the build ran 1:05, over the cap. Big numbers are now spoken rounded with 'about' (exact on screen), and the clothing sentence was cut. 138 words.
