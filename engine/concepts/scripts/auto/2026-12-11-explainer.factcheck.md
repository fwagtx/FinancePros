# Fact-check: 2026-12-11-explainer (Acorn Economics, "What's a dividend?")

Posting date: Friday, Dec 11, 2026. Checked Oct 12, 2026. About 15 web searches. Math recomputed in Python.

## Claims verified

| Line | Claim | Result |
|---|---|---|
| 0, cover, post | 409 S&P 500 companies pay a dividend | VERIFIED. S&P DJI release of Jan 7, 2026: "409 issues or 81.3% within the S&P 500 currently pay a dividend" (Q4 2025; up from 407 in Q3 2025). 409/503 = 81.3%. |
| 1 | "late-2025 count" | ACCURATE but aging (see Staleness). |
| 2 | Ex-dividend date now equals record date | VERIFIED. Under T+1 (effective May 28, 2024; the first same-day ex/record date was May 29, 2024), the ex-date is generally the same day as the record date. A buyer must buy before the ex-date, so "own the stock before the ex-dividend date" is correct. (Narrow exception: very large dividends of 25% or more use different ex-date rules, which is fine to omit.) |
| 3 | 100 x $0.50 = $50/qtr, $200/yr | MATH OK. Labeled "Example". |
| 4 | Yield $2 / $50 = 4% | MATH OK. |
| 5 | DPS 2021-2025: 60.40, 66.92, 70.30, 74.83, 78.92 (record) | VERIFIED. S&P DJI releases: 2022 $66.92 vs 2021 $60.40; 2023 $70.30 (Jan 3, 2024 release); 2025 record $78.92, up 5.5% from $74.83 (Jan 7, 2026 release). 78.92/74.83 = +5.47%. Bloomberg-based series differ slightly; S&P's series is used consistently. |
| 6 | Intel suspended its dividend starting late 2024 | VERIFIED. Intel's Q2 2024 earnings release (Aug 1, 2024) announced "suspending dividend starting in the fourth quarter of 2024". As of early Oct 2026 Intel has NOT reinstated it (Motley Fool, Oct 6, 2026). Check again the week of posting. |
| 7 | 1940-2024, dividends averaged 34% of S&P 500 total return | SUPPORTED. Hartford Funds' "The Power of Dividends" says dividend income's contribution to S&P 500 total return has averaged 34% since 1940 (the decade chart runs through 2024; Motley Fool, Dec 2025, restates this as "between 1940 and 2024... an average of 34%, per Morningstar and Hartford Funds"). Hartford's "Dividend Dilemma" page gives a related 34.46% figure. The wording "averaged 34%" matches the source. |

## Staleness (posting Dec 11, 2026)
- S&P DJI publishes a payer count every quarter (early Jan, Apr, Jul and Oct). I could NOT find Q1, Q2 or Q3 2026 releases through search (the press site is not reachable by direct fetch, and some spam mirror pages claim "402" for Q1 2026, which I could not verify). A newer official count almost certainly exists by December. Options: (a) before posting, pull the latest S&P DJI quarterly count and update lines 0, 1, the cover and the post; or (b) keep 409 but label it precisely as S&P's end-of-2025 count (fix below). "Late-2025 count" is not wrong, but by Dec 2026 it reads as a year old with no source, and the present-tense "pay" in the hook leans on it.
- "In 2025... record $78.92" stays correct on Dec 11, 2026, because 2025 is still the last complete year.
- Intel: confirm the dividend is still suspended before posting.

## Hook (line 0)
"Four hundred nine S and P five hundred companies pay owners cash." 12 words, about 3 seconds, specific, and literally true as of the latest verified count. The hook is acceptable. It is a bit flat because it states a fact without opening a question. Optional stronger version (12 words, same truth): text "409 S&P 500 companies pay owners cash. Just for owning." This would push the word count over, so I am not making it a required change.

## Advice / tips
No stock tips and no price predictions. Line 2 ("Own the stock before the ex-dividend date") describes a mechanic and is not a recommendation. The post says "not financial advice". Intel is used as a cautionary fact, not a tip. OK.

## On-screen vs spoken
- All values match (409, $0.50, $50, $200, $2/$50/4%, $78.92, 34%, 1940-2024).
- Line 3 money scene: the screen shows $0.50/qtr -> $200 per year and skips the spoken $50/quarter step. That is acceptable.
- Line 2 timeline shows Ex and Rec as two separate steps while the narration says they are the same day, which could confuse viewers. Fix below.

## Renderer limits
- Spoken total: 137 (limit 115-138). OK, but at the edge.
- Hook: 12 words. OK.
- Stat label "Share of return" is 15 (<=18). Sub "S&P 500, 1940-2024" is 18 (<=18). OK.
- Board lines are 26 and 22 (<=26). OK, the first is at the limit.
- Timeline "when" values are 2-3 characters; "what" values are 18, 17 and 12 (<=18). OK.
- Chart end "$78.92" is 6 (<=6). OK.
- Squirrel captions are 11 and 13 (<=16). OK.
- Prop label "cash" is 4 (<=5). Cover value "409". OK.
- Money from.label "Example: 100 shares" is 19 characters, the longest text field. Money values must be short, so shorten it (fix below).
- post.title is 49 (<=60). post.tiktok is 147 (<=150). OK.
- No keep:true flags. No compare scenes.

## Awkward narration
- Line 1, "Squirrel owns part of the tree, so squirrel gets acorns": the repeated "squirrel" is a voice choice and is fine. "the late twenty twenty-five count" is a slightly clunky phrase to say aloud.

## Fixes (0-based line indexes; spoken total stays 137)

1. **Line 1** (required for staleness, keeps 18 words):
   - text: "That's S&P's end-2025 count. Owners of the tree get acorns: that's a dividend."
   - say: "That's S and P's end of twenty twenty-five count. Owners of the tree get acorns: that's a dividend."
   - Alternative: replace 409 everywhere (lines 0-1, cover.value, post title/ig/tiktok/yt_desc) with the newest S&P DJI quarterly count, and label it "S&P's [quarter] 2026 count".
2. **Line 2 scene.events** (clears up the ex/record overlap; the spoken line is unchanged):
   `[{"when":"Buy","what":"Day before ex"},{"when":"Ex","what":"Also record date"},{"when":"Pay","what":"Cash arrives"}]`
3. **Line 3 scene.from.label**: "Example: 100 shares" -> "100 shares" (10 characters). The text and say lines keep "Example:", so the scene is still labeled as hypothetical.
4. **Post ig/yt_desc** (optional): "as of Q4 2025" is already precise. If the count is updated, update it here too. In the Sources line, "FINRA" is fine, but "Nasdaq/NYSE T+1 rules" is the primary source for ex-date = record date.
5. **Pre-post check**: confirm Intel still has not reinstated its dividend.

## Sources
- S&P DJI, Jan 7, 2026 dividend release (409 issues, 81.3%; 2025 $78.92 vs $74.83): press.spglobal.com/2026-01-07-S-P-Dow-Jones-Indices-Reports-U-S-Common-Indicated-Dividend-Payments-Increase-of-13-1-Billion-in-Q4-2025-and-46-4-Billion-for-2025
- S&P DJI, Jan 3, 2024 (2023 $70.30 vs $66.92); Jan 4, 2023 release (2022 $66.92 vs 2021 $60.40)
- Intel Q2 2024 earnings release, SEC 8-K, Aug 1, 2024 (sec.gov/Archives/edgar/data/50863/000005086324000122/q224_earningsrelease.htm)
- Nasdaq/NYSE T+1 ex-date rule filings (SEC SR filings 34-99873/34-99874); DTCC Nasdaq T+1 corporate action issuer alert
- Hartford Funds, The Power of Dividends / The Dividend Dilemma; Motley Fool, Dec 28, 2025
- Motley Fool/Nasdaq, Oct 2026: Intel dividend not reinstated

No wrong facts, no advice and no mismatched numbers. The fixes above are improvements for freshness and clarity.

VERDICT: PASS

## Round 2 (editor)
Applied fixes 1-3 (end-2025 count label, timeline events matching narration, shorter example label).
VERDICT: PASS
