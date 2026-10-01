# Fact-check: 2026-10-14-explainer (Diversification: never one tree)

Checked: 2026-10-01 (posts 2026-10-14). Source read: the .raw.json script only.

## Claims checked

| Line | Claim | Status | Source |
|---|---|---|---|
| 1 / cover | Median US stock lost money: -6.9% | VERIFIED. This is the median lifetime buy-and-hold return of 29,754 US common stocks, 1926-2025 (mean is over 30,000%). Only 48.22% of stocks had a positive lifetime return, so "lost money" holds in absolute terms. | Bessembinder, "One Hundred Years in the U.S. Stock Markets" (SSRN 6438198, March 2026); Morningstar, Evidence Investor, Larry Swedroe write-ups |
| 2 | Whole market turned $1 into $15,401 over the century | VERIFIED. A value-weighted portfolio of all common stocks returned $15,401 per $1 invested (T-bills: $25.34). | CNBC, May 8, 2026, citing Bessembinder |
| 3 | 46 companies produced half of the $91T in wealth, 1926-2025; "Bessembinder, March 2026" | VERIFIED. 46 firms account for half of the $91 trillion in net wealth creation. The paper was posted in March 2026. | SSRN abstract excerpts; Edward Conard; Mauboussin on X |
| 5 | 62% of Enron 401(k) plan was Enron stock at end of 2000; CRS | VERIFIED. As of Dec 31, 2000, 62% of the assets in the 401(k) plan were Enron stock. | CRS RS21135, "The Enron Collapse: An Overview of Financial Issues" |
| 6 | Shares fell from $90.75 (Aug 2000) to 26 cents (Nov 2001), about 15 months | VERIFIED. The peak was $90.75 on Aug 23, 2000, and the close on Nov 30, 2001 was $0.26. That is 464 days, about 15.2 months. | Wikipedia (Enron scandal), KHOU |
| 7 | $1,000 to $2.87; 1 of 10 with the other 9 flat gives $900.29 | MATH CORRECT. 1000 x 0.26/90.75 = 2.865, which rounds to $2.87. 900 + 100 x 0.26/90.75 = 900.287, which rounds to $900.29. It is labeled "Example", and the assumptions (other 9 flat) are stated. | python |

On-screen text and spoken narration match on every number (lines 1, 2, 3, 5, 6, 7).
Cover "The Typical Stock Lost Money?" is paid off by lines 1-3.
Stale news / time words: the paper (Mar 2026) and the CNBC piece (May 2026) are not called "new". No "today", "this week" or "this year" wording. Nothing will be wrong on Oct 14.
Quotes: none. Allegations: none (Enron facts are historical and adjudicated). No one company's numbers are generalized to an industry. Enron is shown as an illustration only.
Political opinion / price predictions: none.

## Advice check (diversification takeaway)

Lines 4 and 8 describe what the squirrel does ("squirrel hides acorns under lots of trees"). They also say what diversification does and does not do ("won't stop market-wide drops; stops one rotten tree from taking every acorn"). None of this is a "you should" instruction. It names no product, fund or allocation. The post text has "not financial advice". **PASS on advice.**

## Issues (non-blocking)

1. **Line 1 (hook): no timeframe, and line 2's "that same century" has nothing to refer back to.** Spoken, line 1 never says "century" or "lifetime". A viewer could read it as a recent-period claim, and "that same century" is left dangling. Fix: "Over a century, the typical US stock lost money. Minus six point nine percent." Or put "lifetime return" in the caption: "Typical US stock, lifetime: -6.9%". The hook is still true, specific and under 3 s.
2. **Line 5 (read-aloud):** "At the end of two thousand" can be heard as a quantity. Fix: say "At the end of the year two thousand" (caption can stay "end of 2000").
3. **Line 7 (hypothetical label):** the example assumes buying at the $90.75 peak. Optional: change the sub or title to "bought at peak" so the assumption is explicit.
4. **Line 8 nuance (optional):** "It stops one rotten tree from taking every acorn" is fine as a metaphor. "Limits" would be slightly more precise than "stops", but this is not required.

No wrong facts, no on-screen/spoken mismatches, no math errors, no advice.

VERDICT: PASS

## Round 2 (orchestrator)
Applied minor fixes: line 2 now states the timeframe (1926 to 2025); line 5 says 'the year two thousand'. No factual changes.
VERDICT: PASS
