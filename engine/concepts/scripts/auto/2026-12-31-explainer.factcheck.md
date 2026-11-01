# Fact-check: FHA vs conventional (posts Thu Dec 31, 2026, 12:00 CT)
Checked Nov 1, 2026. Spoken words now: 136. After the fixes below: 133 (target 115-140).

## Verified claims
- **FHA 3.5% down with a 580+ score:** correct (HUD; 10% down for scores 500-579).
- **Conventional 3% down:** correct (Fannie Mae 97% LTV / HomeReady, Freddie Home Possible). Usually needs a 620+ score.
- **FHA upfront MIP of 1.75% of the base loan:** correct and unchanged in 2026. It is usually rolled into the loan.
- **FHA annual MIP of 0.55%:** correct for the example. HUD Mortgagee Letter 2023-05 cut it from 0.85% to 0.55% for loans endorsed on or after Mar 20, 2023. The example (30-year, 3.5% down, base loan up to $726,200) is in the 0.55% tier. Loans with at least 5% down pay 0.50%.
  - One site claims a cut to 0.30% in Jan 2026 (cksaksens.com). No other source supports it, so treat it as unreliable.
  - "About half a percent" is a fair rounding, but it differs from the 0.55% on screen (see issue 3).
- **MIP length:** with under 10% down, MIP lasts the life of the loan; with 10% or more down, it lasts 11 years (case numbers from June 3, 2013 on). Correct.
- **Homeowners Protection Act:** the borrower can ask to cancel PMI when the balance reaches 80% of the original value. PMI must end automatically when the balance is scheduled to reach 78% of the original value, if the borrower is current. "Ask at 20% / Auto at 22%" is correct (CFPB Compliance Bulletin 2015-03).
- **PMI costs 0.2%-2% a year:** matches Fannie Mae's homebuyer FAQ ("typically from 0.2% to 2% annually"). Fannie's PMI page also gives 0.58%-1.86% as the typical 2022 range. I confirmed the FAQ wording through search results only, because yourhome.fanniemae.com is blocked from this session.
- **Conforming loan limit chart (FHFA baseline, one unit):** all 10 points are correct: 2017 $424,100; 2018 $453,100; 2019 $484,350; 2020 $510,400; 2021 $548,250; 2022 $647,200; 2023 $726,200; 2024 $766,550; 2025 $806,500; 2026 $832,750 (announced Nov 25, 2025). "Nearly doubled" is correct (1.96x).
- **Worked example:**
  - Loan: $350,000 x 0.965 = $337,750.
  - Upfront MIP: x 1.75% = $5,910.63, which rounds to $5,911.
  - Monthly MIP: x 0.55% / 12 = $154.80, which rounds to $155.
  - HUD charges annual MIP on the average balance for the year, so year one is really about $153. "About $155" is acceptable.

## Issues (0-based line index)
1. **Line 0, hook (weak and slightly overstated).** It runs 12 spoken words, about 3.5-4 seconds, which is over the 3-second limit. "Never cancels" also clashes with line 5's "Refi to exit". The post text already says it correctly: "never cancels on its own".
   - Fix: text "Under 10% down, FHA's fee never ends." / say "Under ten percent down, F H A's fee never ends." (9 words, about 2.8 s). True and specific.
   - Optional stronger version: say "This F H A fee can last thirty years." (8 words). Change the text to match.
2. **Line 2, scene sub "HUD, 2026 rules" (also "HUD rules, 2026" in ig and "as of 2026" in yt_desc).** The year goes stale the next day, and the rule dates from 2023, not 2026.
   - Fix: sub "HUD, since 2023".
   - Post: "(HUD rules since March 2023)" and "(HUD rules since 2023)".
3. **Line 2, spoken value differs from the screen.** Screen says 0.55%; voice says "about half a percent". The voice also drops "on most loans".
   - Fix say (17 words, same length): "But F H A adds one point seven five percent upfront, then point five five percent yearly."
   - Keep the text as is.
4. **Line 3, screen differs from voice, and the narration is awkward.** Screen says $337,750; voice says "about three thirty-eight thousand". "Three-fifty thousand dollar home" reads badly out loud.
   - Fix text: "Our math: a $350,000 home means borrowing about $338,000."
   - Fix say (16 words): "Our math: a three hundred fifty thousand dollar home means borrowing about three hundred thirty-eight thousand."
   - Board: ["$350K, 3.5% down", "= ~$338K loan"]. The post can keep the exact $337,750.
5. **Line 4, screen differs from voice.** Screen says $5,911; voice says "fifty-nine hundred" ($5,900). "One fifty-five a month" can be heard as $1.55.
   - Fix say (13 words): "That's about fifty-nine eleven upfront, plus about a hundred fifty-five dollars a month."
   - Keep the text and scene as they are.
6. **Line 5, legal precision.** The automatic end is based on the original value and the amortization schedule, not on market equity.
   - Suggested text: "Under 10% down, it lasts the whole loan. By law, conventional PMI ends at 22% equity."
   - Say: "Under ten percent down, it lasts the whole loan. By law, conventional P M I ends at twenty-two percent equity." (19 words)
   - Optional: add the scene sub "of original value".
7. **Line 7, stale risk and wrong term.** FHFA is expected to announce the 2027 limits around Nov 24-30, 2026, and several lenders already lend up to about $845K-$847K. By Dec 31, the endpoint "2026 / $832,750" will be the outgoing figure. The chart title says "Conforming", but the line says "Conventional".
   - Fix text: "Conforming limits nearly doubled since 2017."
   - Fix say (9 words): "Conforming loan limits have nearly doubled since twenty seventeen."
   - End label: "$832,750 (2026)".
   - Before posting, if FHFA has announced the 2027 limit, add [2027, X] as the last point and set the end label to "$X (2027)". The text still works.
8. **Line 8, clarity.** "FHA is easier to get into" right after "conventional needs only 3% down" sounds contradictory. FHA's real edge is easier credit and DTI.
   - Fix text: "The trade-off: FHA is easier to qualify for, conventional easier to get out of."
   - Fix say (16 words, same length): "The trade-off: F H A is easier to qualify for, conventional easier to get out of."
   - Board: ["FHA: easier credit", "Conv: easier exit"].
9. **News watch (no change needed today).** On Oct 22, 2026, an executive order directed FHFA to create a pilot that cancels mortgage insurance automatically on future Fannie and Freddie loans once borrowers have enough equity. It does not change FHA MIP or existing loans, and it has no launch date or threshold yet. A House bill on FHA MIP cancellation is also pending.
   - All script claims are still true today. Re-check before Dec 31 for FHFA pilot details or HUD MIP changes. If a pilot launches, "Auto at 22%" is still the legal floor.
   - Do not mention the order in the video, which keeps it free of politics.
10. **Cover and title:** "The Forever Fee" / $155 is paid off by lines 0, 4 and 5. OK. To match the "Refi to exit" accuracy, consider changing the post "title" and "tiktok" to "the fee that never cancels on its own".
11. **Advice, price predictions, politics:** none found. The disclaimers are present.

## Spoken word count after fixes
133 (line 0: -3; line 3: +1; line 4: +2; line 7: -1; line 5: +1; line 2 and line 8: no change). This is within 115-140.

## Sources
- HUD Mortgagee Letter 2023-05: https://archives.hud.gov/news/2024/2023-05hsgml.pdf ; https://www.ncsha.org/resource/fha-mortgagee-letter-2023-05-reduction-in-annual-single-family-mortgage-insurance-premium/
- FHFA 2026 conforming loan limits: https://www.fhfa.gov/news/news-release/fhfa-announces-conforming-loan-limit-values-for-2026 ; history: https://www.fhfa.gov/data/conforming-loan-limit
- Timing of the 2027 limits: https://nationalmortgageprofessional.com/news/three-competing-2027-conforming-loan-limits-and-none-official
- CFPB PMI bulletin: https://files-prod.consumerfinance.gov/f/documents/201508_cfpb_compliance-bulletin_private-mortgage-insurance-cancellation-and-te_jpbfQUl.pdf
- Fannie Mae FAQ: https://yourhome.fanniemae.com/frequently-asked-questions/homebuyer ; https://yourhome.fanniemae.com/buy/private-mortgage-insurance
- Oct 2026 executive order: https://www.gtlaw.com/ar/insights/2026/10/trump-executive-order-addresses-mortgage-insurance-title-insurance-costs ; https://www.housingwire.com/articles/trump-order-mortgage-insurance/

Note: yourhome.fanniemae.com, cnbc.com and housingwire.com could not be fetched from this session (network allowlist). I verified them through search results only.

VERDICT: FAIL

## Round 2 (editor)
All fixes applied: shorter hook ("Under 10% down, FHA's fee never ends."), sub "HUD, since 2023" and post wording, 0.55% spoken exactly, ~$338,000 loan on screen and voice, "fifty-nine eleven" and "a hundred fifty-five dollars", "By law, conventional PMI ends at 22% equity", evergreen "Conforming limits nearly doubled since 2017", "easier to qualify for" with board "FHA: easier credit / Conv: easier exit", TikTok "never cancels on its own". 140 spoken words.
VERDICT: PASS
