# Fact-check: 2026-12-21-explainer (Acorn Economics: the $5,000 ask)

Checked: Oct 22, 2026, for posting Mon Dec 21, 2026, 12 PM CT (evergreen buffer). Source checked: `2026-12-21-explainer.raw.json` only.

## Math (recomputed in Python)

| Claim | Recomputed | Status |
|---|---|---|
| Year-30 gap $11,783 = 5000 x 1.03^29 | $11,783.27 | OK |
| Chart points (yr 1/5/9/13/17/21/25/30): 5000, 5628, 6334, 7129, 8024, 9031, 10164, 11783 | identical | OK |
| 30-year cumulative gap $237,877 = 5000 x (1.03^30 - 1)/0.03 | $237,877.08 | OK |
| 401(k): 10% of each year's gap (5% own + 5% match), 6%/yr, 30 yrs → ~$55,270 | $55,270.48 with **end-of-year deposits** (each year's deposit earns nothing in the year it is made). Start-of-year deposits would give $58,587 | OK, but the convention is the conservative one and is unstated. "About fifty-five thousand" is fine for both. |

Note on "$55,270 more": half of those deposits (about $11,894 of employee money over 30 years) comes out of the $237,877 pay gap, so "$55,270 more" on top of $237,877 reads like double counting. It is better framed as the 401(k) balance, not "more". See fix L7.

## Pew Research Center (short read, Apr 5, 2023, "When negotiating starting salaries, most U.S. women and men don't ask for higher pay")
- Sample: 5,775 U.S. adults, including 5,188 workers employed full or part time who are not self-employed. Question: what happened the last time they were hired.
- Men 32% vs women 28% asked for higher pay than first offered. **Matches L8.** "When last hired" matches Pew's wording.
- Among those who asked: 28% got what they asked for, 38% got more than the initial offer but less than they asked for, 35% got only the original offer. 28 + 38 = 66 is a valid sum of two exclusive groups, and the denominator ("of those who asked") is clear in the spoken line and the IG/YT text. Pew rounds each figure, and the three add to 101, so "about two-thirds" would be the most defensible wording. 66% is still accurate enough. On-screen sub "Pew 2023: 28%+38%" shows how it was built. **OK.**
- Possible confusion: Pew's topline also says roughly two-thirds of workers did *not* ask. The script never says that, so there is no conflict.

## Issues and fixes

1. **L1 hook / cover / post title: misleading "grow into" (FIX REQUIRED).** "A $5,000 ask can grow into about $238,000" sounds like $5,000 compounding into $238,000, as if invested. In fact it is 30 years of extra pay added up, before taxes, assuming the gap holds and both workers get the same 3% raises. Fixes keep the same word count:
   - L1 say: `A five-thousand-dollar ask can add up to two hundred thirty-eight thousand.` (11 words, same as now)
   - L1 text: `A $5,000 ask can add up to about $238,000 in pay.`
   - post.title (current "How a $5,000 raise ask can grow to $237,877" also wrongly says "raise ask"; this is a starting-salary ask): `How a $5,000 salary ask adds up to $237,877 over 30 years` (57 chars)
   - post.ig first line: `A $5,000 ask can add up to about $238,000 in pay.`
   - post.tiktok: `A $5K ask: $237,877 more pay over 30 years (example, 3% raises). Not financial advice. #moneytok #personalfinance #salary #careertok #financeprostv` (147 chars)
   - cover.title (optional): `One Ask, $237,877 More Pay`
   - Hook scene title "The $5K [ask]" is fine.

2. **L7: 6% unstated as an assumption, timing convention unstated, and "more" double counts (FIX REQUIRED, word count goes down by 1).**
   - L7 say: `Assuming six percent yearly growth, that's about fifty-five thousand.` (10 → 10 words. "At" becomes "Assuming", and "more" is dropped. Net 10, same as now.)
   - L7 text: `Assuming 6% yearly growth, that's about $55,270.`
   - L7 caption: `$55,270 by year 30` (18 chars)
   - post.ig and yt_desc already say "assumed 6%". Optionally add "(end-of-year deposits)" in yt_desc only.

3. **Example labeling / before taxes:** L2 "Made-up example", L3 board "Example assumptions", L4 chart "(example)", L5 "before taxes" + sub "example, pre-tax" are all good. The 401(k) figure is also pre-tax, which is implied by the 401(k). No change needed.

4. **Advice wording:** the script has no instructions to the viewer. Hashtag `#careeradvice` in post.ig conflicts with "not financial advice". Replace with `#careers`.

5. **On-screen vs spoken:** L4 "$11,800" ≈ $11,783 (labeled "about"). L5 $237,877 matches exactly. L7 spoken "about fifty-five thousand" vs screen $55,270 is acceptable rounding. L8/L9 match. OK.

6. **Template/limits:** compare values $60,000/$65,000/32%/28% are ≤7 chars. Stat labels/subs ≤18, values ≤9, board lines ≤20, chart end "$11.8K" = 6. No keep:true flags. OK.

7. **Time words:** "a 2023 Pew survey" is accurate on the posting date. No "this year/recently". OK. The data is 3.5 years old, but it is still the cited source and is labeled with its year.

8. **Spoken total:** 138 before fixes, 138 after fixes (L1 11→11, L7 10→10). Within 115–138.

9. **Readability:** L8 (22 words) is long but reads cleanly. No change needed.

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-3 (hook "add up to", post.title/tiktok/IG/cover, 401k assumption wording and caption, hashtag).
VERDICT: PASS
