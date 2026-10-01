# Fact-check: 2026-10-19-explainer ("Why Timing the Market Is So Hard")

Checked 2026-10-01 for posting 2026-10-19. Source checked: only `2026-10-19-explainer.raw.json`.
Access note: am.jpmorgan.com, FRED and StatMuse are blocked by the egress proxy and Firecrawl has no credits left, so these checks rely on search-result excerpts (J.P. Morgan Guide to Retirement 2026 PDF, CNBC, Yahoo Finance and others) plus python recomputation.

## Verified claims
| Claim | Status | Notes |
|---|---|---|
| $10,000 in the S&P 500, 2006-2025, left alone = $80,619 (11.0%/yr) | VERIFIED | JPM GTR 2026: S&P 500 **Total Return** Index, Jan 2, 2006 - Dec 31, 2025. Python: (80,619/10,000)^(1/20)-1 = 11.0% |
| Missed 10 best days = $35,866 (6.6%/yr) | VERIFIED | Python: 6.59% gives 6.6% |
| "56%" | VERIFIED as math | 1 - 35,866/80,619 = 55.5%, rounds to 56%. **The framing is wrong, though** (see issue 1) |
| 6 of the 10 best days within 2 weeks of the 10 worst | VERIFIED | JPM GTR 2026 says the same (5 of the 6 came after the worst days) |
| 10 of ~5,000 trading days = 0.2% | VERIFIED | About 252 x 20 = 5,040 days. 10/5,000 = 0.2% |
| Mar 12, 2020: S&P 500 -9.5% | VERIFIED | 2,480.64 vs 2,741.38 = -9.51% (CNBC: worst day since 1987) |
| Mar 13, 2020: +9.3% | VERIFIED | 2,711.02 vs 2,480.64 = +9.29%. It is one of the 10 best days of 2006-2025, so it fits the example |
| Chart closes Mar 9/10/11/12/13/16/17 2020: 2,746.56 / 2,882.23 / 2,741.38 / 2,480.64 / 2,711.02 / 2,386.13 / 2,529.19 | VERIFIED | Match the published closes. Daily changes: -7.60, +4.94, -4.89, -9.51, +9.29, -11.98, +6.00%. End label "2,529" matches |
| Not advice | PASS | The takeaway ("Squirrel runs from the storm. The acorn rain comes right after.") describes; it does not tell anyone what to do. The CTA says "Education, not financial advice." No price predictions and no political content |
| Time words / staleness | PASS | No "today/this week" wording. GTR 2026 is still the current edition on Oct 19 |
| On-screen vs spoken values | PASS | Every number matches between the text, say and scene fields |

## Issues
1. **Lines 1 (hook), cover, post.title, ig line 1, tiktok: misleading framing (substantive).** "Missing 10 days in 20 years shrank this pile by 56%" is wrong in two ways:
   - It leaves out the word **best**. Missing any 10 days would not do this.
   - The pile did not **shrink**. It still grew from $10,000 to $35,866. It ended 56% smaller than the stayed-in pile.
   The cover "Miss 10 Days, Lose 56%" and the TikTok "end with 56% less" have the same problem.
   Fixes:
   - Hook: "Missing the 10 best days in 20 years left this pile 56% smaller." Say: "Miss the ten best days in twenty years, and this pile ends up fifty-six percent smaller."
   - Cover: "Miss 10 Best Days: 56% Less".
   - Post title: "Missing the 10 Best Days in 20 Years Left 56% Less".
   - Do the same in ig line 1 and tiktok ("Miss the 10 best days in 20 years, end with 56% less").
2. **Line 1: weak opening (length).** At about 13 words the hook runs about 4 seconds out loud, and the 3-second budget is not met. A shorter version: "Ten best days. Missed. Fifty-six percent less money." Or: "Miss ten days, end up with half." (Only if you keep "best" in the caption.)
3. **Lines 2-3 and post: index basis.** J.P. Morgan used the S&P 500 **Total Return** Index (dividends reinvested). Add "with dividends" to the line 2 caption or the compare sub, e.g. "$10,000 in the S&P 500 (dividends reinvested), 2006-2025". Do the same in the ig and yt_desc. The March 2020 % moves are price-index moves, which is fine.
4. **Line 3: narration (minor).** "it's thirty-five thousand, eight hundred sixty-six" has no unit. Add "dollars".
5. **Line 6 chart (minor, optional).** The chart shows Mar 16 (-12.0%) as a bigger drop than the Mar 12 drop the caption names. That is accurate, but viewers may wonder. Optionally note "Mar 16: -12%", or end the chart at Mar 13.
6. **post.title (minor).** "Cost This Investor" suggests a real person. JPM's figure is a hypothetical backtest, so use the title in issue 1.

VERDICT: FAIL
