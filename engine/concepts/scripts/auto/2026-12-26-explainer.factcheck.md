# Fact-check: 2026-12-26-explainer (LLC vs sole proprietor)

Checked Oct 27, 2026, for a Saturday Dec 26, 2026 post (evergreen buffer). Line indexes below count from 0 (`lines[0]` is the hook).

## Verified claims
- **Disregarded entity / Schedule C (line 1):** Correct. By default the IRS treats a single-member LLC as a disregarded entity, so the owner reports on Schedule C and pays SE tax on Schedule SE, the same as a sole proprietor (IRS Pub 3402, Topic 554). Line 1 already says "one-owner".
- **Default for multi-member LLCs:** By default these are taxed as partnerships (Form 1065, K-1). There is still no entity-level federal tax, so "$0 cut by default" is literally true for them too. But the video compares an LLC with a *sole proprietor*, which only makes sense for one owner. The hook should say so (Fix 1).
- **Worked example (line 2):** $50,000 x 0.9235 x 0.153 = $7,064.775, which rounds to **$7,065**. Correct, and the spoken and on-screen values match. It is labeled "Example:" but not "hypothetical" (Fix 3).
- **SSA wage base chart (line 3):** $137,700 (2020), $142,800 (2021), $147,000 (2022), $160,200 (2023), $168,600 (2024), $176,100 (2025), $184,500 (2026) and $192,300 (2027) are all correct.
  - SSA announced the 2027 base of $192,300 on Oct 14, 2026, alongside a 3.6% COLA (Journal of Accountancy, The Tax Adviser). It came in above the $190,200 projection.
  - The 2026 base is confirmed on SSA's OACT cbb page.
  - The end label "$192K" is consistent, and the spoken numbers match the caption.
- **Is the chart relevant?** Yes, as context. The 12.4% Social Security part of SE tax only applies up to the wage base, so "its Social Security part caps out" is accurate and follows from the line before. It doesn't change the $50K example, and the narration doesn't claim it does.
  - Timing: "$192,300 in 2027" is correct on a Dec 26, 2026 post, since it is already announced and applies to 2027 earnings.
- **CA $800 (line 6):** Correct. The FTB annual LLC tax is $800, paid with Form 3522 (2026 instructions). It applies to single-member LLCs too. The 2021–2023 first-year exemption has expired, so there is no caveat needed.
- **Liability shield (lines 4–5):** Phrased correctly with "generally". It notes that the shield doesn't cover the owner's own negligence or personal guarantees, and that courts can pierce the veil when funds are commingled. Accurate and hedged.
- **S corp / Form 2553 (line 7):** Neutral, and the election is described as optional. Fine.
- **Advice and politics:** None. The post text carries the "not financial advice" disclaimer and cites sources.

## Issues and fixes (exact replacement text)
1. **Hook, line 0: possibly misleading without "one-owner"** (priority). "An LLC" covers multi-member LLCs, which default to partnership treatment. Narrow it, which also matches the sole-prop comparison:
   - `text`: `By default, a one-owner LLC cuts your federal taxes by $0.`
   - `say`: `By default, a one-owner LLC cuts your federal taxes by zero dollars.` (12 words, within the limit; the total becomes 136)
   - The scene title can stay `LLC tax cut: [$0]`.
2. **Post copy: match the hook.**
   - `post.title`: `Does a one-owner LLC cut your taxes? By default, $0.` (52 chars)
   - `post.tiktok`: `By default, a one-owner LLC cuts your federal taxes by $0. Here's what changes. Not financial advice. #moneytok #personalfinance #llc #financeprostv` (149 chars, under the 150 limit, so there is no slack)
   - First line of `post.ig`: `By default, a one-owner LLC cuts your federal taxes by $0.`
3. **Line 2: label the example as hypothetical.** In both `left.sub` and `right.sub`, replace `$50K profit` with `Hypothetical $50K` (17 chars). Optionally:
   - `text`: `Hypothetical: $50,000 of profit means about $7,065 of self-employment tax either way.`
   - `say`: `Hypothetical: fifty thousand dollars of profit means about seven thousand sixty-five dollars of self-employment tax either way.`
   - Word count stays the same.
4. **Line 7 (minor): instruction-style item.** In `scene.items[2]`, replace `Ask a tax pro` with `Tax pro topic` (13 chars).
5. **Line 3 (minor nit, optional): long and number-heavy.** At 30 spoken words it's dense, but it reads correctly. No change required.

## Mechanical checks
- Spoken words: 135. After Fix 1 it becomes 136, inside the 115–138 range.
- Every `text` matches its `say`.
- All field lengths are within limits:
  - Compare values `$7,065` are 6 chars.
  - Board lines are at most 15 chars.
  - Split and list items are at most 14 chars.
  - Split titles are at most 6 chars.
  - Chart end label is 5 chars.
  - Stat label is 17 chars and its sub is 15.
  - Hook title is 17 chars.
  - Cover title is 16 chars and the cover value is 2.
  - Prop label is 3 chars and the tag is 3.
- There are no `keep:true` flags.
- There are no time words that will be wrong on Dec 26, 2026.

Sources: journalofaccountancy.com/news/2026/oct/social-security-wage-base-and-cola-announced-for-2027; thetaxadviser.com (same story); ssa.gov/OACT/COLA/cbb.html; ftb.ca.gov/forms/2026/2026-3522.pdf; IRS Pub 3402 / Topic 554.

All facts and math check out. Fix 1 is strongly recommended but is a precision fix, not a factual error.

VERDICT: PASS

## Round 2 (editor)
Applied fixes 1-4.
VERDICT: PASS
