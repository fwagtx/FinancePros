# Fact-check: 2026-10-12-explainer ("Interest on Your Interest?")
Checked 2026-09-30 against the script JSON only (web search, 6 queries; math recomputed in python).

## Verified
- 2026-27 undergrad Direct Loan rate 6.52% fixed, for loans first disbursed July 1, 2026 to June 30, 2027 (ED/FSA rate notice; NerdWallet, College Investor, AccessLex).
- Chart points (award years): 2016 3.76, 2017 4.45, 2018 5.05, 2019 4.53, 2020 2.75, 2021 3.73, 2022 4.99, 2023 5.50, 2024 6.53, 2025 6.39, 2026 6.52. All correct (finaid.org, College Investor, MOHELA).
- Math: 10,000 x 6.52% x 4 = $2,608. 10,000 x 6.52% = $652. 12,608 x 6.52% = $822.04. Difference = $170.04, so "about $170" is right. On-screen and spoken numbers match.
- Nov 1, 2022 final rule (in effect July 1, 2023) removed every capitalization event not required by statute: first entry into repayment (end of grace), leaving forbearance, leaving PAYE, ICR or REPAYE/SAVE, and loss of PAYE partial financial hardship. Events that still capitalize by statute: leaving IBR (and the IBR hardship loss), the end of deferment on unsubsidized loans, and consolidation. The split-screen lists are correct.
- Cover and title ("Interest on Your Interest?", $10,000, +$170/yr) are paid off in lines 4 to 6.
- Opening: true, specific and short (about 3 seconds). It works as a hook.
- No price predictions, no political opinion, and no quotes. The "not financial advice" disclaimer is present.

## Issues
1. **Lines 4-6 and the cover: the worked example is misleading under current rules (main issue).** The example is a 2026 loan at 6.52% that goes unpaid through school. Line 5 then says "If that capitalizes...". The script itself later says (line 7) that since July 2023 this interest no longer capitalizes when you start repaying. So, by default, the $2,608 would **not** be added to principal, and the +$170/yr on the cover and hook would not happen. It would happen only through a trigger such as consolidation or a deferment ending. Also, a loan first disbursed after July 1, 2026 cannot use IBR, PAYE or ICR (under the OBBBA, new loans get RAP or the Tiered Standard plan), so the "Leaving IBR" and "Leaving PAYE or ICR" items do not apply to the loan in the example. As written, viewers will think the $170/yr is automatic.
   **Fix:** name the trigger in line 5: "If that capitalizes, say when you consolidate, yearly interest jumps from $652 to about $822." Add "(if capitalized)" to the stat sub in line 6 and on the cover ("+$170/yr if capitalized"). Optionally add to line 8: "IBR, PAYE and ICR rules apply to older loans; new loans since July 2026 use RAP or Tiered Standard."
2. **Line 4: the hypothetical is unrealistic and its assumptions are not labeled.** A single $10,000 unsubsidized undergrad loan disbursed on day one of freshman year is above the first-year limit ($5,500 dependent, $9,500 independent). The calculation also ignores the 6-month grace period and assumes simple interest over a full 4 years on the whole amount.
   **Fix:** label the assumption on screen, e.g. "Hypothetical: $10,000 balance, 6.52%, 4 years of simple interest, no payments."
3. **Line 3, text vs spoken:** the caption says "2.75% in 2020-21", but the narration says "two point seven five in twenty twenty" and drops both "percent" and the school year.
   **Fix:** say "versus two point seven five percent in the twenty twenty to twenty-one school year", or change the caption to "2020".
4. **Line 7, minor precision:** the 2023 rule applies to federal Direct Loans (ED-held). "Federal loans" is acceptable shorthand; "Direct Loans" is more precise if there is room.
5. **Line 9: fine.** "Interest paid before it capitalizes never earns interest" is a statement of fact, not an instruction.
6. **Time words:** "since July 2026" and "since July 2023" will still be correct on 2026-10-12. Nothing is stale.
7. **Narration:** the lines read naturally out loud. "I B R" is spelled out correctly for TTS.

## Suggested stronger hook (optional)
The current hook passes. If you change it, keep it true under current rules: "Your student loan can still charge interest on its own interest."

VERDICT: FAIL

## Round 2 (revised script, re-checked 2026-09-30)
No new factual claims were added, so no new searches were needed. Math re-verified: $2,608, $652 to $822.04, +$170.04.

Resolved:
- Issue 1: line 5 now names consolidation as the trigger. The line 5 and 6 scenes say "If capitalized". Line 8 and the split screen limit IBR to older loans. The hook now says "can still", which is true.
- Issue 2: line 4 is labeled "Hypothetical", and the caption, narration and scene state the assumptions (no payments, 4 years, simple interest).
- Issue 3: the line 3 caption ("2.75% in 2020") now matches the narration, which says "percent".
- Issue 4: "Direct Loans" is now used throughout.
- The post, IG and YouTube text match the revised script.

Remaining (minor, not blocking):
- Cover and line 1 hook scene: "+$170/yr" still has no "if capitalized". The video pays it off right away as conditional, so this is a style nit. Suggested label: "+$170/yr if capitalized".

VERDICT: PASS
