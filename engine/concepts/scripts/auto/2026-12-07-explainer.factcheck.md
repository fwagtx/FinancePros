# Fact-check: 2026-12-07-explainer (Present bias: future you pays)

Checked Thu Oct 8 2026 for posting Mon Dec 7 2026 (evergreen). Line indexes are 0-based. Every number was checked against web sources independently, and all math was recomputed in Python. Note: the caller pointed me to the research brief and I opened it, but every claim below was verified separately through search.

## Verified claims

- **Thaler (1981), Economics Letters 8(3):201-207.** Respondents were asked how much they would need at a later date to be indifferent to $15 now. The median answers were $20 at 1 month, $50 at 1 year and $100 at 10 years. The implied annual rates are 345%, 120% and 19%. Recomputed as continuously compounded rates: 12·ln(20/15)=3.452, ln(50/15)=1.204, ln(100/15)/10=0.190. All match. (Sources: MIT OCW 14.13 lecture 16 and UniTS "discounted values" slides.) For context, the same premium compounded annually would be about 3,057%. Continuous compounding (345%) is the paper's own convention, so it is fine to use.
- **Laibson (1997), "Golden Eggs and Hyperbolic Discounting," QJE 112(2):443-477.** This paper uses the quasi-hyperbolic weights 1, βδ, βδ², … The present gets full weight and every later period gets an extra β<1 discount. The functional form comes from Phelps & Pollak (1968). The script's wording "modeled it: now gets full value, later gets an extra discount" is accurate. It does not claim Laibson invented the model, which is correct.
- **Hershfield et al. (2011), JMR 48(SPL):S23-S37.** In Study 1, about 50 college students used immersive VR. Those who met an age-progressed avatar of themselves allocated about $172 of a hypothetical $1,000 windfall to retirement, against about $80 for the current-self group. That is 2.15x, so "about twice as much" is fair. The money was hypothetical, and the script says so ("pretend thousand dollars" / "hypothetical $1,000"). Caveat: the DOL CLEAR review says this Study 1 difference was not statistically significant at conventional levels. Later studies, including one using aged photos with adults aged 18-35, found smaller but significant effects (about 33% more of a hypothetical paycheck). The claim is acceptable as worded because it is labeled as one study with hypothetical money. The wording fixes below are about VR vs photo and "saved".
- **Thaler & Benartzi (2004), JPE 112(S1):S164-S187.** SMarT participants at one company raised their average savings rate from 3.5% to 13.6% over 40 months, which was after the 4th pay raise. This is confirmed by the paper's abstract and the Chicago Booth page. Separately, the company-wide average rose from 4.4% to 10.6%. DOL CLEAR rates the causal evidence "low" because people chose whether to join. The script's wording "at one company, joiners went from…" is appropriately narrow.
  - **Chart point 9.4% at 14 months:** supported. Thaler's Senate JEC testimony (Mar 10 2004) says that within 14 months, enrollees went from 3.5% to 9.4%, and "after two more years" they were saving 13.6%.
  - **Chart point 11.6% at 28 months:** supported. Chicago Booth Review and the University of Rochester Review both say the rate went "from 3.5 percent to 11.6 percent over the course of 28 months." This was the earlier report on the same site.
  - The three points come from different reports of the same plan rather than from a single table in the JPE paper. I could not retrieve the JPE table to confirm the exact month spacing. Both points have specific sources and agree with each other, so I recommend **keeping them**. If the producer wants zero exposure, the safe fallback is `[[0,3.5],[40,13.6]]`.
- **Renderer limits.** All pass:
  - compare values are $15 and $20 (≤7), and the subs are within 18;
  - stat value "~2x" is within 9, and its sub "Hershfield, 2011" is 16 (≤18);
  - board lines are all ≤26, the longest being "Make the cost land later" at 24;
  - split titles have 9 and 10 characters, and split items are ≤16;
  - chart end "13.6%" is within 6;
  - spoken words total 137 (range 115-138) and the hook is 12 words.
- **Other checks.** There are no keep:true flags. Nothing is time-sensitive, so the Dec 7 posting date is fine. There is no political content and no price predictions. The cover ("Why Future You Pays", $15 / 345%) is paid off by lines 0-4.

## Issues and exact fixes

1. **Line 0, the hook. Wording overstates the finding (must fix).** Nobody "demanded" a rate. Respondents named a dollar amount, and the 345% is a rate implied by their answers. "Demanded" also makes it sound like a real-money negotiation, when this was a hypothetical survey. The hook is still a strong, specific opener; it only needs the right verb. Replace with (12 spoken words, so the total is unchanged):
   - text: `Wait one month? People's answers implied a 345% yearly rate.`
   - say: `Wait one month? People's answers implied a three hundred forty-five percent yearly rate.` (13 words). If the 12-word cap is strict, use instead:
   - text: `Wait one month? People implied a 345% yearly rate.` / say: `Wait one month? People implied a three hundred forty-five percent yearly rate.` (12 words)
   - Apply the same change to `post.title` and the first line of `post.ig`: `Wait one month? People's answers implied a 345% yearly rate.`
2. **Line 1. "wanted $20 next month over $15 now" implies they preferred $20, but $20 was the indifference point (optional, recommended).**
   - text: `Richard Thaler's 1981 survey: the median answer was $20 next month to match $15 now.`
   - say: `Richard Thaler's nineteen eighty-one survey: the median answer was twenty dollars next month to match fifteen now.` (17 words, which brings the total to 138, still within the cap. Skip this change if you use the 13-word hook.)
3. **Line 5. The ~2x result came from VR avatars, not photos, and nobody actually "saved" anything (must fix the stat label).**
   - scene.label: `Aged-avatar group put` → or, more simply, `To retirement, aged-avatar group`. Keep value `~2x` and sub `Hershfield, 2011`.
   - say (23 words, unchanged count): `In a twenty eleven study, students who met their aged avatars put about twice as much of a pretend thousand dollars toward retirement.`
   - text: `Hershfield et al., 2011: students who met their aged avatars in VR put ~2x as much of a hypothetical $1,000 toward retirement.`
4. **Line 7 board. Reads as instructions, which conflicts with the no-advice rule (should fix).** Change the scene lines from imperatives to descriptions:
   - `Future you feels real` / `The cost lands later`.
   - The spoken line ("Both work with the bias…") is descriptive and fine.
5. **Line 4 split. The item "Saves later" under Future you is confusing (minor).** It reads as if future-you is the one saving. Replace with `Pays it back` (12 characters).
6. **Line 2. Minor mismatch between screen and voice.** The caption says "about 19% a year" but the narration says "about nineteen percent". The value is the same, so this is acceptable. Optionally add "a year" to the narration, which adds 2 words. Only do this if the total stays ≤138.
7. **Posts.**
   - `post.ig` says "people shown an aged photo of themselves put about twice as much". The ~2x result was from the VR avatar study, so change this to `people who met an aged avatar of themselves put about twice as much of a hypothetical $1,000 toward retirement`.
   - In `yt_desc`, "aged-photo studies (Hershfield et al., 2011)" → `aged-avatar studies (Hershfield et al., 2011)`.
   - `yt_desc` correctly says "an implied 345% yearly rate".
   - `tiktok` is fine.
   - All source citations are correct: Economics Letters 1981, QJE 1997, JMR 2011 and JPE 2004. Every post carries the "not financial advice" disclaimer.
8. **Optional context.** The Thaler survey used hypothetical money with a small student sample. The script never generalizes beyond "people" in a survey, so this is acceptable.

## Sources
- MIT OCW 14.13 lec16: https://ocw.iti.hr/courses/economics/14-13-economics-and-psychology-spring-2004/lecture-notes/1413_lec16_tmdis.pdf
- UniTS slides: https://moodle2.units.it/pluginfile.php/199737/mod_resource/content/0/discounted%20values.pdf
- Laibson 1997: https://scholar.harvard.edu/sites/scholar.harvard.edu/files/laibson/files/golden_eggs_and_hyperbolic_discounting.pdf
- Hershfield et al. 2011: https://pmc.ncbi.nlm.nih.gov/articles/PMC3949005 ; DOL CLEAR review; NYU Stern summary https://www.stern.nyu.edu/experience-stern/faculty-research/hershfield-retirement-savings ; wealthmanagement.com / ispr.info coverage ($172 vs $80)
- Thaler & Benartzi 2004: https://www.chicagobooth.edu/research/rustandy/social-impact-research/research-papers/2004/save-more-tomorrow-using-behavioral-economics-to-increase-employee-saving ; Chicago Booth Review https://www.chicagobooth.edu/review/save-more-tomorrow ; Rochester Review https://www.rochester.edu/pr/Review/V66N2/feature5.html ; JEC testimony https://www.jec.senate.gov/archive/Documents/Hearings/thalertestimony10march2004.pdf

VERDICT: FAIL

## Round 2 (editor)
Applied: hook reworded to "One month's wait? Priced like 345% a year." (no "demanded"); line 1 "median answer ... to match"; line 5 avatars/students, label "Aged-avatar group put"; line 7 board descriptive; split "Pays it back"; posts updated. Chart points kept.
VERDICT: PASS
