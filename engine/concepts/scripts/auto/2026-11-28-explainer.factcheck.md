# Fact-check: 2026-11-28-explainer (Tipflation), checked Oct 2, 2026 for the Nov 28, 2026 post

## Verified claims
- **Square Smart Tip Amounts** (Square help center "Set up and customize tipping" / "Settle payments and manage tips"; NerdWallet): under $10 the options are No Tip, $1, $2 or $3. At $10 or more they are 15%, 20% or 25%. This is a setting the seller chooses: it sits under Settings > Checkout > Tipping, next to "Set Percentage Amounts", and tipping has to be toggled on. It is not universal, so the hook must not read as if every $6 coffee shows a 50% button.
- **Math**: 1/6 = 16.67%, 2/6 = 33.33%, 3/6 = 50.0%. The board values and the spoken "about seventeen, thirty-three or fifty" match within the allowed rounding.
- **Pew**: 72% of US adults say tipping is expected in more places than five years ago. The survey ran Aug 7-27, 2023 (11,945 adults) and was published Nov 9, 2023. The sub "Pew survey, Aug 2023" is correct (fieldwork date).
- **Toast quick-service average tip, Q1**: 2021 16.9, 2022 17.0 (Toast Q1 2022 report, May 2022), 2023 16.0, 2024 16.0, 2025 15.8 and 2026 15.8 (Toast blog: "flat at 15.8% for six consecutive quarters"). All chart points check out. The figures are labeled as Toast's, not generalized to the industry.
- **Bankrate 2025 tipping survey**: 27% tip less or not at all when shown a pre-entered tip screen, and 11% tip more. Bankrate press release and The Hill, June 2025. Correct.
- **FLSA**: $2.13/hr minimum cash wage, $7.25 federal minimum and a $5.12 maximum tip credit (DOL Fact Sheet #15, DOL tipped-wage table). Correct.
- **Spoken vs on-screen values**: all match (17.0% is spoken as "seventeen percent", which is fine).
- **Spoken word count**: 150 (allowed range 100-150).
- No advice, no price predictions and no political opinion. The time words ("2023", "2025 survey", "early 2026") stay correct on Nov 28, 2026.

## Issues
1. **Line 1 (hook): too long, overclaims, misdated.**
   - At 12 spoken words it runs about 4 seconds, over the 3-second limit.
   - "On a $6 coffee, one tip button means a 50% tip" reads as universal, but it only happens when a seller uses Square's optional Smart Tip setting.
   - The scene title "2026: a [50%] coffee tip" suggests something new in 2026. Smart Tip Amounts is a long-standing Square setting, not a 2026 change.
   - Fix (8 words, about 2.7 s):
     - text: `A $6 coffee. A 50% tip button.`
     - say: `A six-dollar coffee. A fifty percent tip button.`
     - scene.title: `Square: a [50%] coffee tip` (keep t hook, prop tag, label "$6", value "+$3", mood shock)
2. **Line 2: missing qualifier and awkward narration.** Add "optional" so the setting isn't presented as universal. "On sales under ten. On six," reads awkwardly out loud.
   - text: `Square's optional Smart tip screen offers $1, $2 or $3 on sales under $10. On $6, that's about 17%, 33% or 50%.` (110 chars)
   - say: `Square's optional Smart tip screen offers one, two or three dollars on sales under ten dollars. On six dollars, that's about seventeen, thirty-three or fifty percent.` (26 words, +3)
   - scene unchanged.
3. **Line 8: non-sequitur.** "So the tip screen isn't a law" doesn't follow from the FLSA line.
   - text: `Tip screens aren't required by law. They're a store setting with presets.`
   - say: `Tip screens aren't required by law. They're a store setting with presets.` (13 words, unchanged count)
   - scene unchanged.
4. **Post text: keep it consistent with the qualified hook.**
   - ig first line: `A $6 coffee. A 50% tip button.`
   - ig second line: `Square's optional Smart tip setting shows $1, $2 or $3 on sales under $10; on $6 that's about 17%, 33% or 50%.`
   - yt_desc first sentence: `Square's optional Smart tip setting offers $1, $2 or $3 on sales under $10, so on a $6 coffee the $3 button is a 50% tip.`
5. **Minor, no change needed:**
   - The cover and header say "every screen". It's hyperbole, but line 4 pays it off.
   - Toast has published Q2 2026 and may publish Q3 2026 before posting. The chart compares Q1 to Q1, so it stays valid.
   - No 2026 Bankrate tipping survey turned up in search. Re-check before posting; if one has come out, swap in its figures.

Word count after fixes: 150 - 4 (line 1) + 3 (line 2) + 0 (line 8) = **149**.

Sources: squareup.com/help/us/en/article/8631-set-up-and-customize-tipping; squareup.com/help/gb/en/article/5069; nerdwallet.com/article/finance/dont-let-technology-bully-tipping; pewresearch.org/2023/11/09/tipping-culture-in-america-public-sees-a-changed-landscape/; pos.toasttab.com/blog/on-the-line/what-is-the-average-tip-percentage; pos.toasttab.com/news/toast-restaurant-q1-trends-report-dine-in-growth-surges-while-takeout-and-delivery-decline; pos.toasttab.com/blog/on-the-line/tipping-in-america; bankrate.com/press-releases/63-of-americans-have-a-negative-view-about-tipping-with-41-saying-tipping-culture-has-gotten-out-of-control/; thehill.com/business/5332326; dol.gov/agencies/whd/state/minimum-wage/tipped; DOL Fact Sheet #15.

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-4. Two changes from the suggested wording:
- Hook title is "Square: a [50%] tip", shortened from the suggested version to fit the 22-character limit.
- Stat label is "Tips expected in more places" (28 characters).
Re-check before posting: whether Bankrate has published a 2026 tipping survey. VERDICT: PASS
