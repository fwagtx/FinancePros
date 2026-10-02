# Fact-check: 2026-11-26-explainer (Acorn Economics, "What the S&P 500 actually is")

Checked against the script JSON only. I did not read the research brief. Posts Thursday, November 26, 2026 (Thanksgiving). Checked on October 2, 2026.

## Verified claims

| Claim | Script | Finding | Status |
|---|---|---|---|
| Top-10 share of the index, Sept 2026 | "about 40%" | Sept-2026 weight trackers (westmountfundamentals, chartrow, macromicro) put the top 10 at about 40%. Listed weights: NVDA 8.10, AAPL 7.34, MSFT 5.60, AMZN 3.78, GOOGL 2.99, AVGO 2.62, GOOG 2.39, META 2.17, MU 1.69, plus TSLA, about 38-41% in total. RBC and Tema say the top 10 was "more than two-fifths" at the end of 2025. Note: the top-10 *holdings* include two Alphabet share classes, so they cover 9 companies. The top-10 *companies* weigh slightly more, so "about 40%" still holds. | OK |
| Kept since 1957 | 1957 | The index expanded to 500 companies and took the S&P 500 name on March 4, 1957 (Wikipedia, S&P Global, CNBC "turns 60" in 2017). | OK |
| Weighting | "weight follows its market value" | The index is weighted by float-adjusted market cap. The script's "market value" simplification is acceptable. | OK (simplified) |
| Eligibility | "generally… US-based, profitable, and big enough. A committee decides." | S&P DJI methodology requires US domicile, positive GAAP earnings (latest quarter and trailing four quarters), a market-cap minimum (about $22.7B since July 2025), float and liquidity tests, and committee selection. The "generally" hedge fits. | OK |
| Year-end closes | 2019 3,230.78; 2020 3,756.07; 2021 4,766.18; 2022 3,839.50; 2023 4,769.83; 2024 5,881.63; 2025 6,845.50 | All seven match published closes (FRED/YCharts/Wikipedia). The 2025 close of 6,845.50 on 12/31/2025 matches CNBC and Reuters (+16.39% for 2025). | OK |
| Hypothetical math | $60T basket: $3T is 5%; $30B is 0.05% | 3/60 = 5.00%. 0.03/60 = 0.05%. It is clearly labeled hypothetical ("Say…", "(example)"). The total market cap of about $61.1T at the end of 2025 makes $60T reasonable. A $30B company is above the about $22.7B minimum, so it is plausible. | OK |

## Other checks
- **Dating and time words:** "Sept 2026" is explicitly dated, so it stays accurate on Nov 26. There are no "today/this week/now" words. OK.
- **Advice / predictions:** None. Line 8 ("Index funds copy the basket") describes what index funds do without recommending them. The post carries "not financial advice". OK.
- **Political opinion:** None.
- **Cover/title payoff:** "10 Trees, 40% Of The Basket?" is paid off by the hook and by lines 4-5. The header is paid off. OK.
- **keep:true:** None used. OK.
- **Layout:** Compare values "5%" and "0.05%" are 7 characters or fewer. List has 3 items with reveal 3. Chart has 7 points, and the end label matches the last point. OK.
- **CTA:** The squirrel CTA is correct for acorn episodes.
- **Spoken word count:** 149 now, and 148 after the fixes below. Both are within 100-150.

## Issues and fixes (all minor)

1. **Line 1: the hook runs over 3 s.** It has 12 spoken words, about 4 s. The claim itself is true and specific.
   - text (keep): `In Sept 2026, 10 companies made up about 40% of the S&P 500.`
   - say → `Ten companies, about forty percent of the S and P.` (10 words, -2)
   - scene: unchanged (the title "10 firms: [~40%]" and the label "Sept 2026" carry the date and the full name).

2. **Lines 3 and 6: TTS may read "US" as the word "us".**
   - Line 3 say → `Picture one basket holding acorns from five hundred big U.S. trees. That basket is the S and P five hundred, an index kept since nineteen fifty-seven.`
   - Line 6 say → `To join, a company generally must be U.S.-based, profitable, and big enough. A committee decides.`
   - text and scene unchanged.

3. **Line 5: the spoken amount has no unit.** The narration says "sixty trillion" with no currency.
   - say → `Say the basket is worth sixty trillion dollars. A three trillion dollar company is five percent of it. A thirty billion dollar company is zero point zero five percent.` (+1)
   - text and scene unchanged.

4. **Line 7: the on-screen numbers are exact but the spoken ones are rounded.** The narration says "about thirty-eight forty" and "about sixty-eight forty-six". Make the caption match the speech:
   - text → `The basket's value moves every trading day. It ended 2022 near 3,840 and 2025 near 6,846.`
   - say: unchanged.
   - scene: unchanged (the chart's exact points and the end label "6,845.50" are fine as chart data).

5. **Line 4 (optional precision):** the weighting is float-adjusted.
   - scene.lines → `["Weight = company size", "(value of tradable shares)"]`
   - text and say unchanged.

6. **Post (optional):** the "index weight trackers" source is vague. Name one, e.g. `Sources: S&P Dow Jones Indices; RBC Wealth Management; Slickcharts/index weight trackers (Sept 2026).`

No wrong facts, no advice or predictions, no math errors, and no material number mismatches.

VERDICT: PASS
