# Fact-check: 2026-11-20-explainer ("50% up to 6%" decoded)

Checked Oct 2, 2026 (posts Nov 20, 2026). Math recomputed in python.

## Verified
- Vanguard How America Saves 2026: "50% on the first 6% of pay" is still the single most common match formula (about 12% of plans offering a match; it is less dominant than before). HAS 2026 describes plan-year 2025 data; "Vanguard, 2026" names the report, so it is acceptable. The hook "the most common match maxes out at 3%" is fair: 50% x 6% = 3% of pay, and lines 2 and 9 make clear the 3% is of pay. Hook is 12 spoken words and on-screen matches spoken.
- Fidelity Q2 2026 Retirement Analysis (quarter ending June 30, 2026): average employer contribution 4.8%, employee 9.6%, total 14.4%. Correct. It is attributed to Fidelity, not generalized to all plans.
- IRS basic safe harbor match: 100% of the first 3% + 50% of the next 2% = 4% of pay max. Correct.
- Vesting: employee deferrals are always 100% vested. Non-safe-harbor matches can use at most a 3-year cliff or a 6-year graded schedule. Traditional safe harbor matches are 100% vested immediately (QACA: up to 2 years).
- Math: 6% of $60,000 = $3,600, so the match is $1,800. At 3% the match is $900, and the gap is $900. 50% x 6% = 3%. Post text math matches.
- Label limits: all titles, labels, subs, board lines, list items and the hook title ("\"50% up to 6%\" = [3%]", 22 characters) are within limits. The keep:true on line 5 follows a compare scene with identical data, so it is valid.
- No time words go stale by the posting date. There are no price predictions and no political content. The cover/title is paid off by line 9.

## Required fixes
1. Line 3 (hypothetical label missing from the narration). On screen it says "Hypothetical", but the narration says "Take a sixty thousand dollar salary".
   - text: "On a hypothetical $60,000 salary, 6% is $3,600, and the employer adds half: $1,800."
   - say: "On a hypothetical sixty thousand dollar salary, six percent is thirty-six hundred, and the employer adds half, eighteen hundred."
2. Line 5 (wording that reads like a nudge). "never collected" implies money the viewer is failing to take. Replace it with neutral description.
   - text: "That's $900 a year unmatched."
   - say: "That's nine hundred dollars a year unmatched."
3. Line 8 (vesting is overgeneralized). "other matches can take up to 3 years" wrongly includes safe harbor matches, which must vest immediately. It also reads awkwardly out loud.
   - text: "The catch is vesting. Workers' own money is always theirs; a regular match can take up to 3 years, or 6 if graded."
   - say: "The catch is vesting. Workers' own money is always theirs; a regular match can take up to three years, or six if graded."
4. Line 9 (word budget). Drop the leading "So" to keep the script at 150 spoken words or fewer after fixes 1 to 3.
   - text: "The real number is rate times cap: 50% times 6% is 3%."
   - say: "The real number is rate times cap: fifty percent times six percent is three percent."

Optional: the post says "regular matches" for vesting, which is consistent with fix 3. No "you should" or "free money" language was found.

VERDICT: FAIL

## Round 2: applied
Fixes 1 to 4 were applied to the raw.json. check.py: "OK: 10 lines, 149 spoken words (~50s at 180 wpm)". The hook is 12 words.

VERDICT: PASS
