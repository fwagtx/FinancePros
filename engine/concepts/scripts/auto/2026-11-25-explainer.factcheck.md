# Fact-check: 2026-11-25-explainer (Acorn Economics, "What money actually is")

Checked October 2, 2026, for posting on November 25, 2026. I did not read the research brief. federalreserve.gov, FRED, macroradar and economicgreenfield were blocked by the proxy, so the figures below come from search-result excerpts of the Fed H.6 release, FRED/ALFRED, YCharts and TradingEconomics.

## Verified facts
| Claim | Finding | Status |
|---|---|---|
| M2, Aug 2026 = $23.3T | H.6 released Sept 22, 2026: M2 (seasonally adjusted) = $23,342.8B | OK |
| M2 at Dec 2025 = $22.36T | $22,355.3B | OK |
| M2 at Dec 2024 = $21.49T | YCharts $21.49T | OK |
| M2 at Dec 2023 = $20.7T | YCharts $20.70T | OK |
| M2 at Dec 2022 = $21.27T | YCharts says 21.27. An H.6 excerpt (Mar 2024 vintage) says $21,294.0B, so 21.29 | Minor (possible vintage difference, not visible on the chart) |
| Cash = $2.5T, 10.6% of M2 | **Wrong measure.** 2,475.6 / 23,342.8 = 10.6%, but $2,475.6B is the *monetary base* currency in circulation (MBCURRCIR). That figure includes cash sitting in bank vaults, and bank vault cash is **not** part of M2. The cash inside M2 is the **currency component of M1**, which was $2,390.5B in Aug 2026 (CURRNS; Feb 2026 seasonally adjusted was $2,356.2B). 2,390.5 / 23,342.8 = **10.2%** | **ERROR** |
| "About $20.9T lives in accounts" | M2 minus the currency in M2 = 23,342.8 − 2,390.5 = **$20,952B ≈ $21.0T**. The $20.9T figure comes from subtracting the wrong cash number | **ERROR** |
| Three functions of money | Medium of exchange, unit of account, store of value (St. Louis Fed) | OK |
| 1933: "Americans had to turn in most gold coins" | EO 6102 (Apr 5, 1933) required people to deliver gold coin, bullion and certificates to the Fed by May 1, 1933. People could keep up to $100 in gold and rare collector coins. "Most gold coins" is fair | OK. The on-screen "Gold coins recalled" is loose; see fix |
| 1971: "the US stopped swapping dollars for gold with other governments" | Nixon, Aug 15, 1971, suspended dollar-gold convertibility for foreign governments and central banks ("gold window") | OK |
| yt_desc: "since 1971 the dollar hasn't been convertible to gold" | True. Ordinary citizens lost convertibility in 1933–34 | OK |

## Newer data before the posting date
The H.6 is released on the fourth Tuesday of each month. The **Oct 27, 2026** release will carry September data and the **Nov 24, 2026** release (the day before posting) will carry October data. Every number in the script is explicitly dated "Aug 2026" or "by August 2026", so the claims stay true on Nov 25. The August values could be revised slightly, but they will still round to $23.3T. You can keep the August dating. Updating to the Nov 24 release is optional. The spoken hook uses the past tense ("had"), so it does not go stale.

## Math (recomputed in Python)
- 2,475.6 / 23,342.8 = 10.61% (the script's figure, built on the wrong cash measure)
- 2,390.5 / 23,342.8 = 10.24% (the correct cash share of M2, about 10%)
- 23,342.8 − 2,390.5 = 20,952.3 (about $21.0T held in accounts)
- Spoken words now: 148. After the fixes below: 149 (within the 100–150 range).

## Issues and exact fixes

### 1. Line 1 (hook): wrong cash share; spoken and on-screen values differ — ERROR
The 10.6% share uses a cash measure that is not part of M2. Also, the screen says "Only 10.6%" while the narration says "Barely a tenth". The hook opens with a true, specific number and is spoken in about 2.8 s, so it is strong once the share is fixed.
- text: `In Aug 2026, Americans had $23.3 trillion in money. Only about 10% was cash.`
- say: `Americans had twenty-three trillion dollars in money. Only about a tenth was cash.`
- scene: `"title": "Cash: just [~10%]"`, `"value": "~10%"` (keep `"label": "Aug 2026"`)

### 2. Line 9 (compare): wrong cash and account values — ERROR
- text: `Only about $2.4 trillion is paper and coin. About $21 trillion sits in accounts.`
- say: `Only about two point four trillion is paper and coin. About twenty-one trillion sits in accounts.`
- scene: `"left": {"label": "Cash", "value": "$2.4T", ...}`, `"right": {"label": "Accounts", "value": "$21.0T", ...}` (5 and 6 characters, within the 7-character compare limit)

### 3. Cover — ERROR (same figure)
- cover `"value": "~10%"` (keep `"label": "Aug 2026"`). The title "Why Do Acorns Have Value?" is answered by line 6 ("Value = shared trust"), so it is acceptable.

### 4. Post captions — ERROR (same figures)
- title: `$23.3 trillion of US money, and only about 10% was cash`
- ig, first paragraph: `In Aug 2026, Americans had $23.3 trillion in money (M2). Only about 10% was cash.`
- ig, M2 sentence: `M2 dipped to $20.7T at end-2023 and reached $23.3T in Aug 2026; cash was about $2.4T of it.`
- tiktok: `$23.3 trillion of US money in Aug 2026, and only about 10% was cash. Squirrel explains. Not financial advice. #moneytok #economics #financeprostv`
- yt_desc: change "only $2.5 trillion was paper and coin" to `only about $2.4 trillion was paper and coin`

### 5. Line 8: "M two" is never explained — minor (clarity)
Viewers first hear "M two" with no definition.
- say: `M two, broad money, dipped to twenty point seven trillion at the end of twenty twenty-three, then hit twenty-three point three trillion by August twenty twenty-six.`
- text: `M2, broad money, dipped to $20.7 trillion at the end of 2023, then hit $23.3 trillion by August 2026 (Federal Reserve).`
- Optional: change chart point `[2022, 21.27]` to `[2022, 21.29]` if the current FRED M2SL vintage shows 21,294. It makes no visible difference on the chart.

### 6. Line 7 timeline label — minor
EO 6102 covered gold bullion and gold certificates as well as coins, and it was not a "recall". Change the 1933 event `"what": "Gold coins recalled"` to `"what": "Gold turned in"`.

## Other checks
- keep:true: line 4 follows line 3 (list to list) and line 5 follows line 4 (list to list). Both are valid.
- Compare values: within 7 characters before and after the fixes.
- CTA: "Squirrel explained money. Squirrel would like one follow." is the correct acorn CTA.
- Advice, price predictions, political opinion: none. The 1933 and 1971 history is stated neutrally. "Not financial advice" appears in the captions.
- Time words: everything is explicitly dated, so nothing will be wrong on Nov 25.
- Narration: reads well. "Squirrel swaps acorns for berries" and "Berries rot" are fine.
- Spoken and on-screen numbers otherwise match: line 8 and the chart agree ($20.7T, $23.3T), and the timeline shows $23.3T.

## Summary
The history, the three functions of money and the M2 totals are correct. The cash figures are wrong: the 10.6% share, $2.5T of cash and $20.9T in accounts (hook, compare scene, cover, all captions) use monetary-base currency, which includes bank vault cash that is not part of M2. The correct figures are about 10% (10.2%), $2.4T and $21.0T. Apply fixes 1–4.

VERDICT: FAIL
