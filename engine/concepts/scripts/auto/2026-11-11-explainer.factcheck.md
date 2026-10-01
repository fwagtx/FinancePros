# Fact-check: 2026-11-11-explainer (posts Nov 11, 2026; checked Oct 1, 2026)

Method: read only the raw script JSON; verified with web search excerpts. ici.org, ssga.com, morningstar.com and prnewswire.com were blocked for direct fetch, and Firecrawl had no credits, so I relied on search-result excerpts of the official sources. Math recomputed in python.

## Verified claims
- **ICI year-end US ETF total net assets** (L2 chart, post): 2020 $5.4T, 2021 $7.2T, 2022 $6.5T, 2023 $8.1T, 2024 $10.3T, 2025 $13.4T. All six points match ICI's Fact Book headline ETF series: 2021/2022/2024/2025 Fact Books, ICI 2022 takeaways and the 2026 Fact Book (4,495 ETFs, $13.4T, Dec 2025). That series includes ETFs not registered under the 1940 Act (commodity ETFs) every year, so the points are comparable. 2022 ($6.5T) is now confirmed. Year-over-year changes: +33%, -10%, +25%, +27%, +30%. 2020 to 2025 is about 2.5x.
- **First US ETF, January 1993** (L2, post): SPY began operations Jan 22, 1993 and first traded on the AMEX Jan 29, 1993. Correct.
- **7% of ETFs vs 52% of mutual funds paid capital gains in 2025** (L6, post): this is State Street Global Advisors' figure from "Tax efficiency is structural...". SSGA's long-term average since 2016 is 9% vs 53%. Morningstar's numbers point the same way: about 6% of roughly 1,600 ETFs from 15 large providers estimated a 2025 distribution, and another Morningstar excerpt says about 72% of US equity mutual funds paid one. The Morningstar figures use different universes (projections, and equity-only mutual funds), so do not mix them with State Street's. Keep State Street as the source.
- **ICI 2025 asset-weighted average expense ratios** (L7-L8, post): index equity ETFs 0.14%, actively managed equity mutual funds 0.64%, index equity mutual funds 0.05% (ICI "Trends in the Expenses and Fees of Funds, 2025," March 2026). Correct.
- **$10,000 example math**: 0.14% = $14 and 0.64% = $64, both correct. It is labeled as an example ("Example: $10,000, 1 year").
- Spoken and on-screen values match on every line.
- Sub-labels are all 28 characters or fewer. The longest is "Avg index stock MF fee, 2025" at exactly 28.
- There is no advice, no fund recommendation, no price prediction and no political content. The post carries "not financial advice." "End of 2025" will still be correct on Nov 11, 2026.

## Issues and fixes
1. **L1 hook, minor.** "One share can hold 500 companies. That's an ETF." The word "can" keeps it true: an S&P 500 ETF holds about 503 stocks. But a mutual fund share can hold 500 companies too, so "That's an ETF" overstates how unique this is. The opener is still strong. Optional tighter version: "One S&P 500 ETF share holds about 500 companies." Or keep "can" as it is.
2. **L6, attribution in narration.** Only the on-screen subs credit State Street, and State Street is an ETF sponsor with an interest in this result. Fix the spoken line: "In 2025, State Street found seven percent of E T Fs paid capital gains. Mutual funds? Fifty-two percent." Optionally change the subs to "Source: State Street" (20). Post: "(State Street, an ETF provider)".
3. **L5, in-kind explanation slightly oversimplified.** "Big traders swap shares for stocks, not cash, so the fund rarely sells." In-kind redemptions mean the fund doesn't have to sell stocks to pay redeeming investors. The fund still trades for index changes, and some ETFs (many bond ETFs, for example) use cash. Fix: "...so the fund rarely has to sell to pay them out." The board line "Fewer sales, fewer gains" is fine.
4. **L7, "MF" abbreviation.** Casual viewers may not know "MF". Use "active stock mutual funds" (25 chars) for the L7 sub. The L8 label "Avg index stock MF fee, 2025" is already at 28 chars, so use "Index stock mutual funds" (24) as the label and "Avg fee, 2025, ICI" in the sub.
5. **L7, "keeper's yearly fee".** The "keeper" metaphor is never introduced, so it reads awkwardly out loud. Fix: "The fund's yearly fee is the expense ratio."
6. **L4, "1x/day"**: clear enough with "price after close" under it. The optional spoken shorthand "once a day" is already in the narration. OK.
7. **L2, staleness note (informational).** ICI's monthly data for 2026 will show higher ETF assets than $13.4T by November. Saying "end of 2025" keeps the claim accurate, so no change is needed.

None of these are wrong facts. Issues 2 and 3 are recommended before posting.

VERDICT: PASS

## Round 2 (orchestrator)
- Applied fixes 1-5: State Street attributed in narration and post (an ETF provider); "rarely has to sell to pay them out"; hook "One ETF share can hold 500 companies"; MF spelled out; "The fund's yearly fee".

VERDICT: PASS
