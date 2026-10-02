# Fact-check: 2026-11-23-explainer ("$100 Became $1 Million?")

Checked 2026-10-02 for a 2026-11-23 post. I read only the script JSON and the house rules, not the brief. I recomputed the math in python.

## Verified claims
| Claim | Script | Independent finding | Status |
|---|---|---|---|
| $100 in S&P 500 (dividends included), 1928-2025 | $1.16M / "past a million" | Damodaran (NYU Stern, Jan 2026 update): about $1,157,600 | OK |
| $100 in 3-month T-bills, 1928-2025 | $2,578 / "about $2,600" | Damodaran: about $2,578 | OK |
| Stock compound return | ~10% a year | Damodaran: 10.02% (python: (11,576)^(1/98)-1 = 10.02%) | OK |
| T-bill compound return | "~3.3%" on screen, "about three percent" spoken, "3.3%" in post | python: (25.78)^(1/98)-1 = **3.37%**, which rounds to **3.4%** | WRONG (rounding) |
| Worst year | 1931, -43.8% | Damodaran: -43.84% in 1931 | OK |
| Down years | 26 of 98 (1928-2025) | Damodaran: 72 up, 26 down; 1928-2025 = 98 years; 26/98 = 26.5%, which is "about 1 in 4" | OK |
| S&P 500 total returns 2018-2025 | -4.38, 31.49, 18.40, 28.71, -18.11, 26.29, 25.02, 17.88 | All match S&P DJI / Slickcharts / YCharts (2025: 17.88%, First Trust "17.9%") | OK |
| 2022 / 2023 | -18.1% / +26.3% | -18.11% / +26.29% | OK |
| Chart end label | +17.9% | 2025 = 17.88% | OK |

Layout checks: the compare values "$1.16M" and "$2,578" are 6 characters each, within the 7-character limit. The keep:true on line 5 follows a chart scene, which is the same template, so it is OK. Spoken word count is 125, within the 100-150 target, and stays at about 124 after the fixes below. I found no political opinion and no time words that will be stale on Nov 23, 2026: every figure is anchored to "1928-2025" or a named year. The cover "$100 Became $1 Million?" is paid off by lines 1-2.

## Issues and exact fixes

**1. Line 8 + post: T-bill rate is mis-rounded, and the spoken value differs from the on-screen value (MUST FIX).** $2,578 over 98 years works out to 3.37% a year, which should be shown as 3.4%. The current version shows "~3.3%" on screen and says "about three percent" aloud.
- text: `The safe bush barely sways, but it grew about 3.4% a year, versus about 10% for stocks.`
- say: `The safe bush barely sways, but it grew about three point four percent a year, versus about ten percent for stocks.`
- scene.right.items[0]: `"~3.4% a year"`
- post.ig: replace `T-bills about 3.3%.` with `T-bills about 3.4%.`

**2. Line 3: present-tense rule reads as a forward-looking claim or advice (advice risk, MUST FIX).** "The tall tree grows more" and the board text "More reward comes with bigger drops" state a general rule about the future. The video should only describe what happened.
- text: `That gap was the reward for taking risk. The tall tree grew more, but it swayed.`
- say: `That gap was the reward for taking risk. The tall tree grew more, but it swayed.`
- scene.lines: `["More growth", "came with", "bigger drops"]`

**3. Line 1: the hook is too long for 3 seconds.** The current spoken hook is 12 words, about 4 seconds at normal pace, and it front-loads "Since nineteen twenty-eight", which delays the payoff. It is true and specific, but it can be tighter.
- text: `Since 1928, US stocks turned $100 into over $1 million.`
- say: `Stocks turned a hundred dollars into over a million.` (9 words, about 2.7 seconds; the year stays on screen in the scene label "1928-2025")
- scene: unchanged.

**4. Line 2: the on-screen value differs from the spoken value.** The narration says "about twenty-six hundred", but the right side of the compare card shows "$2,578".
- scene.right.value: `"~$2,600"` (7 characters, within the limit). Alternatively, keep "$2,578" and change the say to `...grew to about twenty-five hundred seventy-eight dollars...`. The first option is preferred.

**5. Line 6: "S&P 500, 1931" label (minor accuracy point).** The S&P 500 itself launched in 1957. Damodaran's pre-1957 data uses its predecessor index.
- scene.label: `"US stocks, 1931"`
- text: `The worst year was 1931: a 43.8% loss.`
- say: `The worst year was nineteen thirty-one: a forty-three point eight percent loss.`

**6. Post, optional.** All figures are nominal, not adjusted for inflation. You could add "(before inflation)" after "$2,578 by the end of 2025" in post.ig. The existing disclaimers ("not financial advice", "past returns don't predict future returns") are good.

No quotes, allegations or hypothetical examples appear in the script.

## Sources
- Damodaran, Historical Returns on Stocks, Bonds and Bills (NYU Stern), https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histret.html (read through search excerpts; direct fetch is blocked)
- A Wealth of Common Sense, Historical Returns 2025: https://awealthofcommonsense.com/2026/01/historical-returns-for-stocks-bonds-cash-housing-gold-2025/ (search excerpt)
- Slickcharts S&P 500 total returns: https://www.slickcharts.com/sp500/returns
- YCharts S&P 500 Annual Total Return: https://ycharts.com/indicators/sp_500_total_return_annual
- First Trust, The S&P 500 Index 2025 Recap: https://www.ftportfolios.com/Commentary/EconomicResearch/2026/1/8/the-sp-500-index-2025-recap
- quantflowlab / westmountfundamentals (Damodaran-based 1928-2025 tables: 26 of 98 down years, 1931 -43.84%)

The verdict is FAIL because issues 1 (a wrong rounded figure, with spoken and on-screen values that disagree) and 2 (forward-looking, advice-like framing) must be fixed. After those edits the script should pass.

VERDICT: FAIL
