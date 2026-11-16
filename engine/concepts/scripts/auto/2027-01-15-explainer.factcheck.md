# Fact-check: 2027-01-15-explainer (free trials / cancel flows)
Checked Mon Nov 16, 2026, for posting Fri Jan 15, 2027, 12:00 PM CT. Fixes applied directly to `2027-01-15-explainer.raw.json`. check.py prints OK: 11 lines, 140 spoken words (the upper limit), hook 10 words. TikTok caption is 136 characters.

## Verified claims
| Claim | Status | Sources |
|---|---|---|
| FTC complaint (June 2023) says Amazon internally called its Prime cancel flow "Iliad" | Confirmed. It is an FTC allegation and the script attributes it ("The FTC says") | Quartz, Gizmodo, Economic Liberties, Courthouse News, Bloomberg Law |
| Enrolling took 1-2 clicks; canceling was a "four-page, six-click, fifteen-option" process | Confirmed as the complaint's own wording. Bloomberg Law reported a different page count (5 desktop / 6 app). The split title "FTC complaint" keeps it attributed | same |
| Sept 25, 2025 settlement: $2.5B total = $1B civil penalty + $1.5B refunds, no admission | Confirmed. FTC calls the penalty the largest ever in a case involving an FTC rule violation | Axios, TheWrap, Claims Journal, TT News |
| 8th Circuit vacated click-to-cancel rule July 8, 2025 | Confirmed (Custom Communications v. FTC, procedural grounds, days before the July 14 compliance date) | Fenwick, Latham, Greenberg Traurig, AGG |
| FTC ANPRM March 11, 2026 (FR Mar 13; comments due Apr 13, 2026) | Confirmed. I found no NPRM as of Nov 2026, and the narrow old Negative Option Rule is still in effect. The brief's "Feb 2026 restoration" isn't used on screen, so I didn't rely on it | JD Supra, Covington, Kirkland, Kelley Drye, Sidley |
| California AB 2863 effective July 1, 2025 (click-to-cancel for online sign-ups, free-to-pay conversions covered) | Confirmed. Signed Sept 24, 2024 | DWT, JD Supra, Mondaq |
| C+R Research 2022: $86 guessed vs $219 itemized, per month | Confirmed (Apr 22 to May 2, 2022; n=1,000; gap $133) | NBC/CNBC, Motley Fool, C+R blog |
| CNET/YouGov 2026: $252/yr on unused subscriptions | Confirmed via syndicated coverage (WFSB, July 16, 2026). I couldn't reach cnet.com directly. The 2025 figure was $205 | WFSB, The Desk, Cord Cutters News |
| Prime annual fee: $79 (launch 2005; still $79 in 2006 and 2010), $99 (Mar 2014), $119 (May 2018), $139 (Feb 2022) | Confirmed. As of Nov 2026 there has been no US price change: $139/yr and $14.99/mo, and the $159 figure is only an analyst (J.P. Morgan) projection. The chart ending at 2022 at $139 is correct and doesn't need extending | Washington Post, NPR, dealnews (Nov 2026) |
| $14.99 x 12 = $179.88 | Correct ("about one eighty" spoken; labeled "By our math") | arithmetic |

## Issues found and fixes applied
1. **Line 2, overgeneralization.** "Free trials use the same trick" equated every free trial with the Prime cancel-flow allegation, and the trick it describes (auto-renewal) is a different one. Fixed:
   - Text: "Many free trials work like this: $0 now, card saved, auto-pay later."
   - Say: "Many free trials work like this: zero dollars now, card saved, auto-pay later."
2. **Line 3, survey numbers lacked their subject.** The line never said what the $86 and $219 were spent on, and it follows a line about free trials. Fixed:
   - Text: "A 2022 C+R survey: people guessed $86 a month on subscriptions. Itemized: $219."
   - Say: "A twenty twenty-two C plus R survey: people guessed eighty-six dollars a month on subscriptions. Itemized: two nineteen."
3. **Line 4, spoken value differed from the on-screen value.** The narration said "about two fifty" while the screen shows $252. Fixed the say to: "CNET, twenty twenty-six: two fifty-two a year on unused subscriptions."
4. **Line 7, implied causal link and no non-admission.** "Amazon still settled" implied the Amazon case depended on the voided rule. It didn't: the case was brought under ROSCA and the FTC Act. Fixed:
   - Text: "A court voided the FTC's click-to-cancel rule in July 2025. Amazon settled for $2.5 billion, admitting no wrongdoing."
   - Say: "A court voided the FTC's click-to-cancel rule in July twenty twenty-five. Amazon settled for two point five billion, admitting no wrongdoing."
5. **Line 8, overstated stage.** "The FTC is rewriting it" suggests rule text is being drafted, but the FTC is only at the ANPRM stage, with no proposed rule. Fixed:
   - Text: "As of November 2026, the FTC is reconsidering it. California requires click-to-cancel."
   - Say: "As of November twenty twenty-six, the FTC is reconsidering it. California requires click-to-cancel."
6. **Cover, value didn't pay off.** "FREE / $219" under "Free Trial Trap" implied a free trial costs $219. The figure is actually monthly subscription spending (C+R 2022). Fixed to label "SUBS", value "$219/m". The video pays it off on line 3 ("a month on subscriptions", compare sub "per month").
7. **IG caption.** Added "alleged it took" to the step counts, "no admission of wrongdoing" to the settlement, "no proposed rule as of Nov 2026", and "still $139 as of Nov 2026".
8. **TikTok caption.** Added "Amazon admits no wrongdoing." and dropped #personalfinance to stay at 136 characters.
   - Caption: `FTC: Amazon called its Prime cancel flow "Iliad." Amazon admits no wrongdoing. Not financial advice. #moneytok #freetrial #financeprostv`

## Notes
- **Hook.** It is literally true and attributed. It's a strong grabber: the name is specific, odd and verifiable, and line 1 pays it off at once.
- **Split and compare lines.** Line 1 has 13 spoken words and line 3 has 18, so both boxes appear. The chart has no chart_note.
- **Spoken words.** The count is now exactly 140, the upper limit. Any later addition needs an equal cut.
- **Line 1 timing.** It uses gerunds and no tense, and the "FTC complaint" title dates it. The FTC says Amazon changed the flow in 2023, which is acceptable for an explainer.
- **Prime price risk.** If Amazon raises Prime before Jan 15, 2027, line 5 ("$139 by 2022") stays true. Only the IG phrase "still $139 as of Nov 2026" is dated.
- **No advice, predictions or political opinion.** Line 9 ("alarm the end date, check statements") is a generic habit, not financial advice.

VERDICT: PASS

## Round 2 (editor)
Allegations attributed; cover relabeled $219/m subs. check.py OK.
VERDICT: PASS
