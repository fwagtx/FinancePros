# Fact-check: 2027-01-03 explainer (Acorn Economics: "Interest is rent")
Checked 2026-11-04 for posting Sun 2027-01-03, 12:00 CT. Data pulled live from FRED (via Firecrawl FRED connector, vintage 2026-11-04) plus web search. federalreserve.gov, fdic.gov and fred.stlouisfed.org are blocked in this session's network, so primary pages were reached through the FRED API instead.

## Verified claims
| Line | Claim | Source check | Result |
|---|---|---|---|
| 6 chart | 30-yr annual avgs 2016-2025: 3.65, 3.99, 4.54, 3.94, 3.11, 2.96, 5.34, 6.81, 6.72, 6.6 | FRED MORTGAGE30US, annual avg: 3.65, 3.99, 4.54, 3.94, 3.11, 2.96, 5.34, 6.81, 6.72, 6.60. Freddie Mac's Dec 11 2025 YTD average of 6.62% and the late-Dec readings of about 6.2% agree with this | All 10 points correct |
| 5 | Savings 0.38%, Oct 2026 (FDIC) | FRED SNDR: Oct 2026 = 0.38 (Sep 0.37, May-Aug 0.38) | Correct |
| 5 | Cards 22.36%, Aug 2026 (Fed G.19) | FRED TERMCBCCINTNS (commercial banks, accounts assessed interest): Aug 2026 = 22.36. All-accounts rate TERMCBCCALLNS = 21.19 | Number correct; the "Card APR" label is loose (see issue 4) |
| 7 | Fed target 3.75-4.00% as of Oct 2026 | FRED DFEDTARL/DFEDTARU Oct 2026 = 3.75/4.00. The Sept 2026 hike set this range, and the Oct 27-28 FOMC held it, 10-2 | Correct, and dated |
| 4 | 100 at 5% for 1 yr = 105 | 100 x 1.05 = 105 | Correct |
| 2-3 | Rent pays for waiting, inflation, risk | Standard textbook breakdown: time preference / real rate, expected inflation, default-risk premium | Fair simple explanation |

Data still current on Jan 3, 2027: the Nov 2026 G.19 rate (quarterly) comes out around Jan 8, 2027, so August stays the latest card figure. FDIC will publish Nov and Dec national rates before posting, but the line is dated, so it stays true. The Dec 8-9 2026 FOMC happens before posting, and some reports say markets are pricing a December hike. Line 7 is past tense and dated "as of October 2026", so it stays true either way. Keep that date.

## Issues

1. **Line 0 (hook): the point of view clashes with line 1, and the hook runs slightly long.** The hook has the squirrel lending ("wants 105 back"). Line 1 then says "You're paying to use someone else's acorns", which makes the viewer the borrower. At 12 words it is at the word cap and takes about 4 seconds to say, over the 3-second target. "a hundred five" also reads awkwardly out loud. Fix: speak from the viewer's side. That matches line 1 and makes the question personal.
   - text: `Borrow 100 acorns, owe 105. Why?`
   - say: `Borrow a hundred acorns, owe a hundred and five. Why?` (10 words, about 3 s)
   - scene.title: `Borrow 100, owe [105]` (label 100, value 105 unchanged)

2. **Line 5: spoken values differ from on-screen values.** The screen shows 0.38% and 22.36%, but the narration says "about zero point four" and "about twenty-two". The screen also shows "August 2026" while the narration says "August". The line is 22 words and clunky.
   - text: `Banks rent both ways. In 2026, savings paid 0.38%; cards charged 22.36%.`
   - say: `Banks rent both ways. In twenty twenty-six, savings paid zero point three eight percent; cards charged twenty-two point three six percent.`
   - The months stay in the compare subs (`FDIC, Oct 2026` / `Fed, Aug 2026`).

3. **Line 6: spoken value differs from on-screen value.** The narration says "about three percent" but the screen shows 2.96%, and "six point six" has no "percent".
   - text: `Mortgage rent moves too: 2.96% in 2021, 6.6% in 2025.` (unchanged)
   - say: `Mortgage rent moves too: two point nine six percent in twenty twenty-one, six point six percent in twenty twenty-five.`

4. **Line 5 compare label "Card APR" is imprecise.** 22.36% is the G.19 rate for accounts assessed interest, meaning finance charges on balances that carry interest. The G.19 average APR across all accounts is 21.19%. Change the right label to `Card rate` (or `Card interest`). In the POST tags, `credit card APR` can stay as a search term. The ig and yt text already says "card balances were charged 22.36%", which is accurate.

5. **Line 3: the chipmunk is never introduced, and "him" is unclear.** The chipmunk first appears here with no setup, so viewers can't tell he is the borrower.
   - text: `And risk: the chipmunk borrower might never pay back.`
   - say: `And risk: the chipmunk borrower might never pay back.`

6. **Line 4 board: "100 + 5% = 105" is sloppy notation.** Taken literally, 100 + 5% is not 105, and math-literate viewers will comment on it.
   - lines: `["Our math:", "100 x 1.05 = 105"]` (or `["5% of 100 = 5", "100 + 5 = 105"]`)
   - say (smoother aloud): `Our math: a hundred acorns at five percent for a year makes a hundred and five.`

7. **Line 7 (optional):** the on-screen building label `3.75-4%` has no date, but the narration says "as of October 2026". Suggested caption: `Base rent, Oct 2026`. The spoken line is fine as is.

## Not issues
- Cover "Why 105 Acorns?" and the post title are paid off by lines 1-4.
- There is no advice, price prediction or political opinion. Line 8 ("lend, collect; borrow, pay") describes how interest works and is not advice.
- There are no undated time words that would be wrong on Jan 3, 2027.
- Calling the fed funds target "base rent" is a fair simplification.

## Word count after fixes
Per line 10/11/13/9/16/21/19/17/11/11 = **138** (within 115-140). Hook 10 words. Board lines, list items and compare values are all within their limits.

VERDICT: FAIL

## Round 2 (editor)
Fixed: hook "Borrow 100 acorns, owe 105. Why?"; line 3 "the chipmunk borrower might never pay back"; board "100 x 1.05 = 105"; line 5 exact 0.38% and 22.36% spoken, label "Card rate"; line 6 "two point nine six percent"; Fed caption "Base rent, Oct 2026". 138 spoken words.
VERDICT: PASS
