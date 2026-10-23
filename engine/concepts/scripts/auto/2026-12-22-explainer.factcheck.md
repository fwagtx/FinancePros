# Fact-check: 2026-12-22-explainer (FSA use-it-or-lose-it)
Checked Oct 23, 2026, for a post on Tue Dec 22, 2026, 12 PM CT. Line indexes are **0-based**.

## Verified claims
- **2026 health FSA limit $3,400**: confirmed (Rev. Proc. 2025-32, plan years beginning in 2026; up from $3,300).
- **Carryover max $680**: confirmed. Rev. Proc. 2025-32 / Newfront wording: the $680 cap applies to "carryover from a plan year starting in 2026 to a plan year beginning in 2027." The figure for 2025 money carried into 2026 was $660. So "$680 for 2026 plan years" (line 3, post) is correct for unused 2026 money. Employers may set a lower cap.
- **Carryover OR grace period, not both**: confirmed (IRS Notice 2013-71). The grace period is up to 2 1/2 months (Mar 15 for calendar-year plans).
- **Run-out period** (line 6): correct. Notice 2013-71 lets a carryover plan keep a run-out period for claims on prior-year expenses. The carryover is figured after run-out ends. A run-out period adds time to file claims, not to incur new expenses.
- **Example math**: $900 - $680 = $220 lost. With the full grace period, $0 is lost if eligible expenses are incurred by Mar 15. Correct, and it is labeled as an example. It assumes the plan allows the full $680 or the full 2.5 months and runs on a calendar year (see fixes).
- **EBRI $441 (2022)**: confirmed. EBRI says "Roughly half of FSA accountholders forfeited funds to their employer in 2022. The average forfeiture was $441" (3.2M+ accounts).
  - **Base:** EBRI's summary does not state the base. PlanSponsor reports "$441 or $1.4 billion... for all the accounts reviewed." $1.4B / 3.2M is about $437, so the $441 looks like an average across ALL accounts, not only forfeiters.
  - **Label:** The script's "average FSA forfeit" mirrors EBRI's own wording. It does not claim "among those who forfeited," so it is acceptable. Do NOT relabel it "among those who lost money."
- **"About half"**: matches EBRI's "roughly half." InvestmentNews reports 52%, but I could not confirm that number in EBRI's own text. Keep "about half" and do not add 52%.
- **HSA facts** (line 7, post): confirmed. Balances carry over year to year and the account is portable and nonforfeitable (Pub. 969, IRC 223).
- **Hook** (line 0): fair as written.
  - "For many workers" hedges correctly. Dec 31 is the end of the plan year only for calendar-year plans without carryover or a grace period.
  - The line is true and specific, at 10 spoken words (limit 12).
  - Optional idea, not required: a stronger hook would put the $441 up front. It is not changed here because of the word budget.
- **No advice**: wording stays neutral, and line 8 only says plan documents spell out the rules. No predictions or politics.
- **Time words**: nothing will be wrong on Dec 22. The 2027 limits will be out by then, but the video covers 2026 money, so it is not stale.
- **Numbers and limits**:
  - Spoken values match on-screen values.
  - Compare values are <=7 chars ("$0 lost" = 7).
  - No keep:true flags.
  - Spoken words = 136 (OK), tiktok = 147 (OK), post.title = 50 (OK).

## Issues and fixes (exact replacement text)
1. **[MUST FIX] Line 6, list items over the 14-char limit.** "File old claims" and "No new spending" are 15 chars each.
   - Replace `lines[6].scene.items` with `"items": ["Late claims OK", "No new costs"]` (14 and 12 chars).
2. **[Should fix] Line 3, right item "more to spend" is ambiguous.** It reads as more money, but a grace period adds more time.
   - Replace `lines[3].scene.right.items[1]` `"more to spend"` with `"time to spend"` (13 chars).
3. **[Should fix] Line 5, the Mar 15 date assumes a calendar-year plan.**
   - Replace `lines[5].text` with `"A carryover keeps $680 and loses $220; a full grace period loses $0 if spent by March 15 (calendar-year plan)."`
   - Leave the spoken line as is: adding words would push it past 138.
4. **[Should fix] Post ig, same calendar-year assumption.**
   - Replace `Full grace period: $0 lost if spent by March 15.` with `Full grace period: $0 lost if spent by March 15 (calendar-year plan).`
5. **[Optional] Line 4, add the plan's carryover cap to the example.** It assumes the plan allows the full $680.
   - Replace `lines[4].text` with `"Example: you put in the 2026 max, $3,400, and $900 is left (plan allows full carryover)."`
   - Optional; the caption already shows it is an example.

## Sources
- IRS Rev. Proc. 2025-32 (via Newfront, Mercer, Plante Moran, Hylant summaries)
- IRS Notice 2013-71 (via Pillsbury, Hunton, Smith Gambrell summaries)
- IRS Publication 969 / IRC 223
- EBRI, "Vital Statistics on Flexible Spending Accounts, 2022: Forfeitures on the Rise" and press release; PlanSponsor; InvestmentNews

Issue 1 is a hard layout-limit violation (15 > 14) and must be fixed before render. All facts and math check out.

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-5.
VERDICT: PASS
