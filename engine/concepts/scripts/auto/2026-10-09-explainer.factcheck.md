# Fact-check: 2026-10-09-explainer ("What the Fed actually does")

Checked 2026-09-30 for posting on 2026-10-09. 6 web searches were run. Math was recomputed in Python.

## Claims verified

| Line | Claim | Status | Source |
|---|---|---|---|
| 1 | 12 people vote (FOMC) | TRUE. There are 12 voting members, and the Sept 2026 vote was 12-0. | Schwab "Fed Hikes in 12-0 Vote"; CNBC 2026-09-16 |
| 2 | Two jobs: maximum employment and stable prices | TRUE. This is the dual mandate. The statute also lists moderate long-term rates, which is usually folded in. | Fed |
| 3 | 2% goal; Aug 2026 CPI up 3.4% year over year | TRUE. BLS Aug 2026 CPI-U was +3.4% over 12 months, the same as July. Core was 2.4%. | BLS CPI release 2026 M08; CNBC 2026-09-11 |
| 4 | Main tool is the overnight interbank rate | TRUE, though loosely worded. The Fed sets a *target range* for the fed funds rate. | Fed |
| 5 | On Sept 16, 2026 the Fed raised to 3.75%-4.00%, its first hike since 2023 | TRUE. It was a 25 bp hike that ended a five-meeting pause. The last hike was July 2023. | CNBC, CNN, Schwab 2026-09-16 |
| 6 | Peak of 5.5% in 2023, then cuts | TRUE. The peak was 5.25-5.50 (Jul 2023). Cuts came in 2024-25. | Fed history |
| 6 chart | 2022 4.5, 2023 5.5, 2024 4.5, 2025 3.75, 2026 4.0 | TRUE. The year-end top of the range was 4.50 in Dec 2022, 5.50 in Dec 2023, 4.50 in Dec 2024 and 3.75 in Dec 2025 (cut on Dec 10, 2025). The 2026 point is 4.00 as of Sept. | CNBC 2025-12-10; MarketPulse |
| 7 | Prime rate rose to 7% from 6.75% on Sept 17, 2026 | TRUE. JPM, BofA, Citi, Wells and others moved, effective Sept 17. The math checks: 3.75 + 3 = 6.75. | Wells Fargo/BusinessWire; City National; Star-Advertiser 2026-09-17 |
| 7 | Most credit cards charge prime plus a markup | TRUE for variable-rate cards, which are the large majority. | General |
| 8 | $5,000 x 0.25% = $12.50 a year | Math is CORRECT: 5000 x 0.0025 = 12.50. It assumes the balance stays at $5,000 all year. | Python |
| 9 | Fed never lends to you; its rate moves borrowing costs | TRUE. | General |

## Staleness and time words
- No future-dated claims will be wrong on Oct 9.
- The Sept 2026 CPI release is on **Oct 14, 2026**, after the post goes up, so August is still the latest CPI on Oct 9.
- The next FOMC decision is **Oct 28, 2026**, also after the post, so 3.75%-4.00% will still be current.
- All dates are explicit, and there are no "this week" or "yesterday" words. The hike will be about 3 weeks old on the posting date. That is acceptable for an explainer.

## Issues (minor, none blocking)
1. **Line 1, hook length is borderline and the claim is slightly loose.** "Twelve people vote on one number that moves your credit card rate" is 12 words, about 3.3 s spoken, so it runs a little over 3 s. The FOMC also votes on a target *range*, not one number.
   - Stronger, true alternative (8 words, under 3 s, uses the news): "Twelve people just voted to raise your credit card rate." The vote was 12-0, and card APRs follow prime.
   - Also acceptable: "Twelve people just made your credit card pricier."
2. **Line 8, the example is idealized.** "$12.50 a year" assumes a constant $5,000 balance and a card APR that moves a full 0.25 points.
   - Fix: "adds about $12.50 a year", or add the on-screen sub-label "if the balance stays put".
3. **Line 6 chart, mixed time bases.** Four points are year-end values and the last is Sept 2026. The "4% Sep '26" end label already discloses this, so no change is needed. Optionally, title it "Fed target, top end (year-end)".
4. **Line 2 nit.** The law also names "moderate long-term interest rates". The common "dual mandate" framing is fine for this format.
5. **Line 4 nit.** "Its main tool is the rate…" could be read as the Fed charging that rate. Optional rewording: "Its main tool is a target for the rate banks charge each other overnight."

## Other checks
- **Caption vs spoken:** all values match: 12, 2%, 3.4%, 3.75%-4.00%, 2023, 5.5%, 7.00%/7%, $5,000, $12.50.
- **Advice or price predictions:** none. The disclaimer is present in the post text.
- **Political opinion:** none.
- **Cover and title payoff:** "What Does the Fed Actually Do?" and "12 votes" are paid off by the dual mandate, the policy-rate tool, the hike, and the prime and card chain.
- **Post text:** consistent with the script. The sources are listed correctly.
- **Read-aloud:** line 5's say reads "On September sixteenth, twenty twenty-six, it raised that target to three point seven five to four percent". That is long but workable. Optional: "…to a range of three point seven five to four percent."

VERDICT: PASS
