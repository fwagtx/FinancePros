# Fact-check: 2026-12-12-explainer (401(k) vs IRA), posting Sat Dec 12, 2026

Checked: Oct 13, 2026. Script: `2026-12-12-explainer.raw.json`. Spoken total today: 137 words (limit 115-138).

## Verified claims

| Line | Claim | Status | Source |
|---|---|---|---|
| 1, post | 2026 401(k) limit $24,500; catch-up $8,000 (50+); $11,250 ages 60-63 | Correct | IRS IR-2025-111 / Notice 2025-67 (Nov 13, 2025) |
| 1, post | 2026 IRA limit $7,500; catch-up $1,100 | Correct | IRS IR-2025-111 |
| 0, cover, post | "Over 3x" | Correct: 24,500 / 7,500 = 3.27x (50+: 32,500 / 8,600 = 3.78x; 60-63: 35,750 / 8,600 = 4.16x) | python |
| 5, post | Roth IRA phase-out $153,000-$168,000 single (MFJ $242,000-$252,000, not stated in script) | Correct | IRS IR-2025-111 |
| 5 | Roth 401(k) has no income limit | Correct (the plan has to offer a Roth option) | multiple |
| 6 | 401(k) deferrals end Dec 31; 2026 IRA contributions due April 15, 2027 | Correct. April 15, 2027 is a Thursday, so the date does not shift. A filing extension does not extend the IRA deadline. | multiple |
| 7 | 401(k) limits: 2020 $19,500; 2021 $19,500; 2022 $20,500; 2023 $22,500; 2024 $23,000; 2025 $23,500; 2026 $24,500 | All 7 chart points correct | IRS / Fool / Nasdaq / DQYDJ |
| 3, post | 96% of plans made an employer contribution in 2025 | Correct, with a caveat. In the How America Saves 2026 (25th ed.) highlights table, "Plans providing an employer contribution" is 96%*. The asterisk means the 2025 figures are estimates, because the final data will not be available until Dec 2026. The figure covers Vanguard recordkeeping plans only. | Vanguard HAS 2026 |
| 4 | $60,000 x 6% = $3,600; 50% match up to 6% = $1,800 | Math correct; labeled "Example" | python |
| 2 | IRA you open yourself, with nearly any investment; 401(k) uses the plan's fund menu | Fair as a general contrast. IRAs cannot hold collectibles or life insurance, and the choice depends on the custodian. "Nearly any" is acceptable. | Vanguard, NerdWallet |
| 7 | You can have both | Correct. Script does NOT claim IRA contributions are deductible, so no fix needed. If a deduction is ever mentioned: for 2026 the traditional IRA deduction phases out at $81K-$91K single / $129K-$149K MFJ for people covered by a workplace plan. | IRS |

No wrong facts, no advice, no price predictions, no political content. Both posts include "Not financial advice". Tone is neutral.

## Issues and fixes (0-based line indexes)

1. **Hook is awkward (line 0, cover, post title, tiktok).** "takes over 3x what an IRA takes" says "takes" twice and is vague: takes what? Use this sharper and still true hook (11 words on screen, 14 spoken):
   - line 0 `text`: `A 401(k) lets you save over 3x what an IRA does.`
   - line 0 `say`: `A four-oh-one-k lets you save over three times what an I R A does.`
   - line 0 `scene.title`: `401(k) limit [3x+] IRA`. The current "401(k) holds [3x] more" reads as account balances, not yearly limits, and drops the "+".
   - `post.title` (55 chars): `A 401(k) lets you save over 3x what an IRA does in 2026`
   - `post.tiktok` (131 chars): `A 401(k) lets you save over 3x what an IRA does in 2026. Not financial advice. #moneytok #personalfinance #401k #ira #financeprostv`
   - post.ig first line: `A 401(k) lets you save over 3x what an IRA does.`
2. **Word budget (line 1).** The hook adds 2 words (137 -> 139), so trim 1 word here:
   - line 1 `text`: `2026 limits: $24,500 vs $7,500. It's not the only gap.`
   - line 1 `say`: `Twenty twenty-six limits: twenty-four thousand five hundred versus seventy-five hundred. It's not the only gap.` (15 words)
   - New spoken total: **138**, which is within 115-138.
3. **The 96% figure is an estimate (line 3, minor).** HAS 2026 marks the 2025 figure as estimated.
   - line 3 `scene.sub`: `Vanguard 2025 est.` (18 chars)
   - Optional: in post.ig and yt_desc, change "96% of Vanguard plans added some in 2025" to "an estimated 96% of Vanguard-administered plans added some in 2025".
4. **Caption vs spoken mismatch (line 4, minor).** The caption says "a 50% match up to 6% adds $1,800". The spoken line and the board omit "up to 6%". Make the caption match (no change to spoken words):
   - line 4 `text`: `Example: $60,000 salary, 6% in = $3,600; a 50% match adds $1,800.`
5. **401(k) deadline wording (line 6, optional).** "401(k) money stops Dec 31" could suggest employer contributions stop too, but they can be deposited later. Precise swap with the same word count:
   - line 6 `text`: `401(k) deferrals stop Dec 31; 2026 IRA money runs to April 15, 2027.`
   - line 6 `say`: `Four-oh-one-k deferrals stop December thirty-first; twenty twenty-six I R A money runs to April fifteenth, twenty twenty-seven.`
6. **Line 1 compare sub (minor, no change required).** "+$8,000 if 50+" understates the ages 60-63 catch-up ($11,250). That catch-up is disclosed in post.ig, and a fuller sub would not fit in 18 chars. Acceptable.

## Time words for the Dec 12, 2026 post
- "2026 limits", "In 2026", "2026 IRA ... April 15, 2027", "in 2025" (Vanguard) are all correct on the posting date.
- The Dec 31 deadline is 19 days away and still in the future. The IRS 2027 limits will likely be out by then (usually announced in Oct/Nov), but the script is clearly framed around 2026, so it is not stale.

## Renderer limits (all pass, before and after fixes)
- Hook: 9 words now, 11 after fix (max 12).
- Compare values: $24,500 (7), $7,500, $153K, None. Compare subs are 18 chars or fewer.
- Stat label: "Add employer money" (18).
- Split items are 16 chars or fewer; split titles are fine.
- Board lines: 23 / 14 / 18 chars.
- Timeline `when`: 12/31 (5), 4/15 (4). `what`: 18 / 17 chars.
- Chart end: $24.5K (6).
- Props: hook tag label "401k" (4); cover prop label "401k" (4).
- post.title: 48 now, 55 after fix. tiktok: 124 now, 131 after fix.
- No keep:true lines.

## Sources
- https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500
- https://workplace.vanguard.com/content/dam/inst/iig-transformation/has/2026/pdf/HowAmericaSaves2026.pdf (highlights table; excerpts from search, direct fetch failed)
- https://www.thetaxadviser.com/news/2025/nov/inflation-adjustments-to-retirement-account-limits-issued-for-2026/
- https://www.nasdaq.com/articles/401k-contribution-limits-2025-are-bigger-ever ; https://dqydj.com/historical-401k-contribution-limit/
- https://investor.vanguard.com/ira/401k-vs-ira ; https://www.nerdwallet.com/article/investing/can-i-have-a-401k-and-an-ira
- https://www.pensionbee.com/us/guides/2025-ira-and-401-k-deadlines

All facts, numbers and chart points check out. The fixes above are for clarity and the hook; none corrects a wrong fact.

VERDICT: PASS

## Round 2 (editor)
Applied fixes 1-4 (clearer hook "lets you save over 3x what an IRA does", line 1 trim, Vanguard "2025 est.", example caption matches narration). Fix 5 skipped (optional; "deferrals" is jargon for viewers). Spoken total 138.
VERDICT: PASS
