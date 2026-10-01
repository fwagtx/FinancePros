# Fact-check: 2026-10-30-explainer ("Does a Higher Limit Hurt?")
Checked Oct 1, 2026, for posting Oct 30, 2026. Source: the script JSON only. Several official sites (newyorkfed.org, consumerfinance.gov, capitalone.com, wolfstreet.com) refused direct fetch, so the checks rely on search-result excerpts of those sources.

## Claim-by-claim
| Line | Claim | Status | Notes |
|---|---|---|---|
| 1 | Asking for a higher limit "can cost points. Or add them." | OK | This is true: a hard pull can lower a score, and a higher limit can lower utilization. It hedges ("can") and promises nothing. It works as a hook and takes under 3 seconds to say. It could be more specific, e.g. "One phone call to your card issuer can cost you points, or add them." It's acceptable as written. |
| 3 | CFPB: soft inquiries don't affect scores; hard ones can | OK | The CFPB "What is a credit inquiry?" page says soft inquiries "will not affect your credit scores" and hard inquiries can, because models look at how recently and how often you apply. The "Existing accounts" bullet under Soft matches the CFPB's own example (a lender checking an existing account). "Issuers differ" is the channel's words, not the CFPB's. The comma split makes that clear enough. |
| 4 | Capital One uses a soft inquiry for limit increases, whether you ask or it offers | OK | Capital One's Help Center and Learn & Grow pages say it "uses soft inquiries to review credit limit increases ... whether you request the increase or Capital One offers it." The scope is right: limit increases on existing Capital One cards. It is correctly presented as one issuer ("for one") and not as the industry norm. |
| 5 | Hard inquiry: most people lose fewer than 5 points (myFICO), counted 12 months | OK | myFICO says a hard inquiry takes fewer than five points off most people's FICO Scores. FICO counts inquiries from the last 12 months, and they stay on the report for 2 years. "Counted for 12 months" is accurate for FICO. This is FICO-specific, which the "myFICO" attribution covers. |
| 6-7 | $1,500/$5,000 = 30%; $1,500/$7,500 = 20% | OK | Recomputed in Python: 0.30 and 0.20. It is labeled "Hypothetical example". |
| 8 | Amounts owed = 30% of FICO | OK | myFICO's general-population weights: amounts owed 30%. |
| 8 | Utilization = 20% of VantageScore 4.0 | Minor | Credit Karma, Chase and others report 20%. VantageScore itself mostly ranks factors by influence ("highly influential") and gives the percentages as approximate. Suggested fix: "about twenty percent" in the voiceover and "about 20%" in the caption. |
| 9 | US card limits $5.56T in Q2 2026 (NY Fed) | OK (secondary) | Wolf Street (Aug 25, 2026), citing the NY Fed Household Debt and Credit / CCP data: aggregate limit +$324B YoY to a record $5.56T ($5.559T). |
| 9 chart | Q2 2023 $4.6T; Q2 2024 $4.92T; Q2 2025 $5.23T | OK (secondary) | Q2 2023 $4.6T (Wolf Street Aug 2023, NY Fed data). Q2 2024 $4.92T (Wolf Street Aug 2024). Q2 2025 $5.23T (Wolf Street Aug 2025). Internal check: 5.559 - 0.324 = 5.235, which matches $5.23T. YoY steps of 0.32 / 0.31 / 0.33 are consistent. Not checked against the primary NY Fed PDF (fetch blocked). Before posting, check the HHDC_2026Q2 PDF / data file. If you can't, credit it on screen as "NY Fed data via Wolf Street". |
| 9 timing | "Q2 2026" is the latest on Oct 30 | OK | The Q2 2026 report came out Aug 11, 2026. The Q3 2026 report is expected in early to mid November (past pattern: Nov 5, 2025; Nov 13, 2024), after the Oct 30 posting date. Nothing is stale, and no time words will be wrong on the posting date. |

## Other checks
- Advice: none. There is no "you should ask for an increase". Line 10 ("the effect hinges on...") explains rather than instructs, and the post includes "not financial advice". OK.
- Personalized advice or price predictions: none. Politics: none. Allegations: none. Quotes: all paraphrased and attributed, with no direct quotation marks.
- Text vs voiceover: all lines match. The only differences are numbers spelled out for the voiceover.
- Sub-labels are all 28 characters or fewer: 24, 25, 16, 16.
- Cover and title ("Does a Higher Limit Hurt?") are answered by the hard/soft and utilization content.
- Minor: line 9 (the aggregate card-limits chart) is loosely connected. "And" makes it a trivia aside that doesn't tie back to the viewer's score. Optional bridge: "Issuers have been raising limits: US card limits hit $5.56 trillion..."
- Minor: the post lists Experian as a source, but no on-screen claim is attributed to Experian. That's harmless.
- Reading aloud: "VantageScore four point oh" is fine. "Hard ones can; issuers differ." reads a little choppy. Optional: "Hard ones can, and issuers differ."

## Issues
1. Line 8: VantageScore 4.0 "20%" should be "about 20%" (minor).
2. Line 9 chart: the values come from a secondary source and are consistent but not checked against the primary NY Fed file. Verify against HHDC_2026Q2, or credit "via Wolf Street" (minor).
3. Line 9: weak tie-in. Add a bridge line (style).

VERDICT: PASS

## Round 2 (orchestrator)
- L8: "about 20%" for VantageScore. L3 wording smoothed. L9 drops "And". L2 shortened to keep <=150 words.
- Chart values consistent with NY Fed data as reported; title credits NY Fed.

VERDICT: PASS
