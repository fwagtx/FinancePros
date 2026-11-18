# Fact-check: 2027-01-17-explainer (Acorn Economics: good debt vs bad debt)

Posting date: Sun Jan 17, 2027, 12:00 CT. Checked Nov 18, 2026. Checked against primary data, not the brief.

## Verified claims

| Claim | Script | Verified | Source |
|---|---|---|---|
| Fed card rate, accounts assessed interest, latest quarter | 22.36% (Q3 2026) | 22.36% (2026-08-01 obs = Q3 2026). It is still the latest quarter on Jan 17, 2027, because Q4 2026 data comes out in the G.19 release in early Feb 2027. | https://fred.stlouisfed.org/graph/fredgraph.csv?id=TERMCBCCINTNS |
| Chart annual averages 2019-2025 | 16.98, 16.28, 16.45, 17.91, 22.15, **22.89**, 22.32 | 16.98, 16.28, 16.45, 17.91, 22.15, **22.90**, 22.32. 2024 = (22.63+22.78+23.37+22.80)/4 = 22.895, and FRED rounds that to 22.90. | https://fred.stlouisfed.org/graph/fredgraph.csv?id=TERMCBCCINTNS&fq=Annual&fam=avg |
| "about 16% in 2021 to about 22% by 2025" | spoken | Correct (16.45 to 22.32) | same |
| Direct Sub/Unsub undergraduate rate 2026-27 | 6.52% | 6.52%, fixed, for loans first disbursed 7/1/2026 to 6/30/2027 (10-yr high yield 4.47 + 2.05) | https://studentaid.gov/understand-aid/types/loans/interest-rates ; https://www.federalregister.gov/documents/2026/09/10/2026-18493/annual-notice-of-interest-rates-for-fixed-rate-federal-student-loans-made-under-the-william-d-ford |
| Freddie Mac PMMS 30-yr | "averaged 7.11% in November 2026" | 7.11% is the weekly figure for Nov 12, 2026. The week of Nov 5 was 7.18%, so "averaged in November" is inaccurate. | https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US&cosd=2026-09-01 (FRED mirror of Freddie Mac PMMS) |
| Math | $1,000 x 22.36% = $223.60; x 6.52% = $65.20; "under a third" | Correct. 65.20 / 223.60 = 0.292. This is one year of simple interest on a flat balance. Real card interest compounds monthly. Direct Loans use simple daily interest. The math is labelled as "our math" and as simple interest. | arithmetic |

## Issues found, with fixes applied

1. **Line 0, weak hook (fixed).** The old hook ran 12 spoken words (about 4 s) and had a soft, generic open. It now runs 10 words (about 3 s), keeps the squirrel's acorn voice, and is true (Fed average on accounts charged interest is 22.36%; the screen shows the exact figure and the spoken line says "about").
   - text: "Cards charge about 22%. Can borrowed acorns be smart?"
   - say: "Cards charge about twenty-two percent. Can borrowed acorns be smart?"
2. **Line 2, chart point (fixed).** The 2024 point changed from 22.89 to 22.90.
3. **Line 3, spoken value differs from screen (fixed).** The line said "six and a half percent" with no "about", while the screen shows 6.52%. It also said "the card's twenty-two percent" with no "about", while the screen shows 22.36%.
   - say: "Our math: a thousand dollars for a year at about twenty-two percent costs about two hundred twenty-four; at the six point five two percent student loan rate, about sixty-five."
   - text: "Our math: $1,000 for a year at 22.36% costs about $224; at the 6.52% student loan rate, about $65."
   - The compare subs changed to "22.36%, simple" and "6.52%, simple" to flag that this is simple interest.
4. **Line 5, awkward read-aloud (fixed).** "it hurts buying stuff that's gone" was a dangling participle and did not suit the squirrel's short-sentence voice. Split into two sentences: "Debt can work when a low rate buys something that earns more. It hurts when it buys stuff that's gone." Advice check: this is a general educational rule of thumb. It does not recommend any product or action, so it is not advice.
5. **Line 6, inaccurate time phrase (fixed).** "averaged 7.11% in November 2026" was wrong because 7.11% is a single week's figure.
   - text: "Even useful debt costs: 30-year mortgages averaged 7.11% the week of November 12, 2026."
   - say: "... averaged about seven point one percent in mid-November twenty twenty-six."
   - The stat sub changed to "Freddie, 11/12/26".
   - On Jan 17 the figure will be about 2 months old and newer PMMS weeks will exist. It is clearly dated, so this is acceptable for an evergreen explainer. If the line is refreshed before posting, swap in the latest PMMS week.
6. **Post captions (fixed).**
   - The IG/YT opener now matches the new hook.
   - The mortgage date now reads "for the week of Nov 12, 2026".
   - The sources line now reads "G.19 / FRED TERMCBCCINTNS (Q3 2026 data); Federal Student Aid and Federal Register (2026-27 rates); Freddie Mac PMMS (Nov 12, 2026)". The old "FSA (Jun 2026)" date could not be verified.
   - YT now says "(simple interest)".
   - The TikTok caption now says "on accounts charged interest".

## Checked, no issue

- **Time words:** "Q3 2026" will still be the latest quarter on Jan 17, 2027. "2026-27" student loan rates will still apply. There is no "this week" or "today".
- **Cover and title:** "Is Debt Smart?" is answered by line 7 ("smart only when they grow faster than they cost").
- **Content checks:** no political opinion and no price or rate predictions.
- **Final CTA line:** unchanged.
- **Labels:** the "APR" prop label is acceptable shorthand for the Fed's credit card plan interest rate.

## Limits check

`check.py` result: OK. 9 lines, 138 spoken words (about 46 s), hook is 10 words. who="nutty", series="acorn" and the final line are unchanged.

VERDICT: PASS

## Round 2 (editor)
Reviewed applied fixes: tighter hook in squirrel voice, 2024 chart point corrected, spoken/screen numbers aligned, mortgage figure dated to its week.
VERDICT: PASS
