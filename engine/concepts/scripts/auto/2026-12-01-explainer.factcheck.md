# Fact-check: 2026-12-01-explainer (Holiday debt, BNPL and credit cards)
Checked 2026-10-02 for posting Tue 2026-12-01. I read only the raw.json and the checker rules, not the research.md. Spoken words now: 138. After fixes 1-7: 136.

## Verified claims
| Claim | Result | Source |
|---|---|---|
| 37% took on holiday debt, avg $1,223 (up from $1,181) | TRUE, but the survey date is wrong (see #1) | LendingTree "Holiday Debt Hits $1,223", survey of 2,032 adults, Dec 10-15 2025; covered by CNBC, Chain Store Age and Newsmax on Dec 23 2025 |
| 62% credit cards, 35% BNPL (of holiday debtors) | TRUE | LendingTree, same survey |
| Adobe: BNPL $20B online, Nov-Dec 2025 (+9.8%) | TRUE | Adobe press release, Jan 7 2026 |
| CFPB: 63% had multiple simultaneous BNPL loans, 2022 data | TRUE. The CFPB says "borrowers" (see #4) | CFPB BNPL report, Jan 2025 |
| NY Fed Q4 card balances: 0.86 / 0.986 / 1.13 / 1.21 / 1.28 $T | TRUE, all five | NY Fed HHDC 2021Q4-2025Q4 |
| Fed G.19 Q2 2026: 22.15% for accounts assessed interest | TRUE (Q1 was 21.52%) | Fed G.19, Aug 7 2026 |
| Pay in 4 = 4 payments over 6 weeks, 0% interest "if paid on time" | IMPRECISE (see #3) | Afterpay and Klarna run about 6 weeks; Affirm about 2 months. Missing a payment brings late fees, not interest |

## Math (recomputed in Python)
- $1,223 at 22.15% APR, minimum = interest + 1% with a $25 floor: **91 months, $1,186.94 interest**. Correct.
- 4 equal monthly payments: **$319.99** (last payment $319.97), **$56.94 interest** with interest rounded to the cent each month. Correct.
- On screen: $1,187, $57 and $320 a month all round correctly.

## Layout check
All fields are within limits except one: **cover.title "What Holiday Debt Really Costs" is 30 characters, over the 28 limit** (see #6). The other counts: hook title 18, post.title 53, tiktok 138, compare values 6 and 3, list items 16 and 14, longest board line 22, longest label 26, longest sub 18.

## Issues and fixes

### 1. FACT: The LendingTree survey is dated January 2026, but it came out in December 2025 (lines 1-2, cover, post)
The survey ran Dec 10-15, 2025 and was published Dec 23, 2025. On Dec 1, 2026 it is still the latest edition (the 2026 edition is expected in mid/late Dec 2026), so it is not stale. Only the date is wrong.
- L2 text: `In LendingTree's December 2025 survey, 37% took on holiday debt.`
- L2 say: `In LendingTree's December twenty twenty-five survey, thirty-seven percent took on holiday debt.` (12 words, no change)
- L2 scene.sub: `LendingTree 12/25` (17)
- cover.label: `Dec 2025`. L1 scene.label: `Dec 2025` (or `Avg debt, Dec 2025`, 18)
- post.ig: replace `(LendingTree, Jan 2026)` with `(LendingTree, Dec 2025)`
- post.yt_desc: replace `LendingTree's January 2026 survey` with `LendingTree's December 2025 survey`
- The header "the January math" can stay. It refers to when the bills arrive, not to the survey date.

### 2. WEAK OPENING and spoken/on-screen mismatch (line 1)
"About twelve hundred dollars" does not match the $1,223 on screen. The line also answers itself, so the viewer has no reason to keep watching. Stronger version (true at minimum payments, and line 9 pays it off):
- L1 text: `Average holiday debt could take 91 months to repay.`
- L1 say: `Average holiday debt could take ninety-one months to repay.` (9 words, +1)
- L1 scene.title: `Could take 91 [months]` (22). Keep value `$1,223`, label `Dec 2025`.
- If the writer keeps the current hook, at least fix the mismatch: say `The average holiday debt? Twelve twenty-three.` (7 words)

### 3. FACT/PRECISION: Pay in 4 (line 4)
"Zero interest if paid on time" suggests a late payment adds interest. In fact standard Pay in 4 charges no interest either way, and a missed payment brings late fees.
- L4 text: `Pay in 4: 4 payments over about 6 weeks, no interest, but late fees can bite.`
- L4 say: `Pay in four: four payments over about six weeks, no interest, but late fees can bite.` (16 words, +1)
- L4 scene.lines: `Pay in 4:` / `4 payments, ~6 weeks` (20) / `No interest; late fees` (22)

### 4. WORDING: The CFPB counts "borrowers", not "users" (line 6)
- L6 text: `The CFPB found 63% of BNPL borrowers stacked overlapping loans in 2022.`
- L6 say: `The CFPB found sixty-three percent of borrowers stacked overlapping loans in twenty twenty-two.` (13 words, no change)

### 5. STALENESS RISK: "record" $1.28T (line 7)
Q2 2026 is $1.26T. The NY Fed's Q3 2026 report (due about early Nov 2026) could top $1.28T before Dec 1, so this would no longer be the latest figure. Drop the word "record". The figure stays correct because it is dated.
- L7 text: `Card balances hit $1.28 trillion at the end of 2025, per the New York Fed.`
- L7 say: `Card balances hit one point two eight trillion dollars at the end of twenty twenty-five.` (15 words, -2)
- The chart is a Q4-only series, so do not add a 2026 point. Keep it as a dated Q4 series.

### 6. LAYOUT: cover.title is over the limit
- cover.title: `Holiday Debt's Real Cost` (24). The compare scene pays this off.

### 7. STALENESS RISK, MINOR: G.19 Q2 2026 rate (line 8)
The Fed's Q3 2026 G.19 (about early Nov 2026) will be the latest rate on Dec 1. "Q2 2026" stays accurate because it is dated, but before posting either update the rate (and recompute) or leave it dated as it is. The narration is also long (19 words) and rounds to "about twenty-two percent" while the screen shows 22.15%. Tightened version:
- L8 text: `Example: $1,223 at 22.15%, the Fed's Q2 2026 average for cards charging interest.` (unchanged)
- L8 say: `Take twelve twenty-three at twenty-two point one five percent, the Fed's second-quarter average for cards charging interest.` (17 words, -2)

### 8. MINOR (style only): line 9 "Paid off in four months" comes right after "Pay in 4" and could be confused with it
Optional say: `At minimums, that takes ninety-one months and eleven hundred eighty-seven dollars in interest. Paid off in four months instead: fifty-seven dollars.` (+1. If used, the total is 137, still within the limit.)

## Other checks
- Advice and predictions: none. The example is labeled hypothetical and its assumptions are stated on screen and in the post. The post carries the "not financial advice" disclaimer. No political opinion.
- Line 5 "it" (BNPL) refers back two lines. That is acceptable.
- No keep:true flags.
- Word count after fixes 1-7: 138 +1 +1 -2 -2 = **136**, within 115-138.

VERDICT: FAIL
