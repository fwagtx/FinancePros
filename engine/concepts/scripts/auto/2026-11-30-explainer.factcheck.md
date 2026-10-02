# Fact-check: 2026-11-30 explainer (Acorn Economics: what a credit score measures)

Checked: 2026-10-02, for posting Monday, November 30, 2026. Reviewed only `2026-11-30-explainer.raw.json` (lines, scenes, cover, header, post text). The research brief was not read.

## Verified claims

| Claim | Status | Source |
|---|---|---|
| FICO weights: payment history 35, amounts owed 30, length of history 15, new credit 10, mix 10 | Verified | myFICO, "How are FICO Scores calculated?" |
| FICO range 300-850 | Verified for base FICO Scores. Industry-specific scores (Auto, Bankcard) run 250-900; acceptable for an explainer | myFICO |
| Income and employment not in FICO Scores | Verified: myFICO says scores do not use income, employment history or similar personal details. Savings balances are not in credit reports, so "savings" is also correct for standard FICO Scores | myFICO |
| VantageScore also excludes income | Verified (Chase, Credit Karma, Bankrate). The generic hook "your credit score counts your income at zero percent" is fair for both major models | Chase / Credit Karma |
| Avg US FICO (April): 2015 695, 2016 699, 2017 700, 2018 704, 2019 706 | Verified as April readings | FICO blog / Self.inc / NGPF summaries of FICO data |
| April 2020 708, April 2021 716, April 2022 716 | Verified | FICO / Business Wire (Aug 2022 "remains steady at 716") / Fortune |
| April 2023 718 (peak, spoken) | Verified: FICO blog "Average U.S. FICO Score at 718" gives April 2023 at 718, held in July 2023, then fell 1 point by Oct 2023. Record high | fico.com blog; CNBC; Money.com |
| April 2024 717 | Verified | FICO / Business Wire Oct 2024 |
| April 2025 715 | Verified ("Average U.S. FICO Score Drops to 715", Apr 16 2025) | Business Wire / investors.fico.com |
| April 2026 714 | Verified: Spring '26 Credit Insights (Mar 24 2026) put it at 714, flat Oct 2025 to Apr 2026, down 1 point year over year | Business Wire / fico.com newsroom |
| "714 in FICO's August 2026 report" (post) | Verified: Fall '26 report (Business Wire, Aug 25 2026) "Average FICO Score holds steady at 714" | Business Wire / Barchart |
| Math: $600 / $2,000 = 30%; 15+10+10 = 35% ("The other 35%"); 718-695 = +23; 714 vs 718 = -4 | Correct (recomputed in python) | |

All 12 chart points match FICO's April readings, so the title "Avg US FICO Score (April)" is accurate.

## Issues

1. **Line 1 hook, scene label "2026" (misleading date label, should fix).** Income has never been a FICO input, so putting "2026" on the 0% suggests a new 2026 change. The caption's "As of 2026" does the same. Neither is false on Nov 30, but both mislead. The hook itself is true and specific, and it is about 3 seconds spoken (9 words). It is fair beyond FICO because VantageScore also excludes income. It reads slightly stiffly ("counts your income at zero percent").
   - Fix: `scene.label`: `"FICO"` (was `"2026"`)
   - Fix: `text`: `"Your income counts for 0% of a FICO Score."`
   - Fix: `say`: `"Your income counts for zero percent of your credit score."` (10 words, +1)
   - Stronger optional variant (same word budget): `say`: `"A millionaire and a broke student can have the same credit score."` That version still needs the 0% beat to pay off the cover, so the 0% hook is recommended as above.

2. **Line 6 say, awkward narration.** "That includes credit in use." has no clear referent when spoken, because the 30% factor was two lines back.
   - Fix: `say`: `"Amounts owed tracks credit in use. Six hundred dollars on a two thousand dollar limit is thirty percent."` (18 words, +1)
   - `text` and `scene` unchanged. The example is labeled "(example)", which is good.

3. **Line 8 chart color "up" (should fix).** The narration ends on "then slipped to 714" and the end label is 714, below the 718 peak. A green "up" line ending on a decline contradicts the spoken point.
   - Fix: `scene.color`: `"down"`. Points, end "714" and title stay unchanged.

4. **Line 5, minor wording.** The caption says "length of credit history 15%" and the narration says "account age at fifteen percent". These are close enough (FICO's factor covers account ages). The numbers match. No change needed.

5. **Line 3, minor nuance.** 300-850 is the base FICO range. Industry-specific FICO scores use 250-900. Acceptable as is; no change needed.

6. **Stale news / time words.** "slipped to 714 by 2026" and the post's "FICO's August 2026 report" stay correct on Nov 30. FICO's fall report already came out (Aug 25 2026), and no newer FICO average is expected before posting. OK.

7. **Advice / predictions / politics.** None. There are no instruction-style takeaways, and the "not financial advice" disclaimer is present. OK.

8. **Cover/title payoff.** "Your Income Counts 0%?" is paid off by lines 1 and 7. The header "What a credit score actually measures" is paid off by lines 3-6. OK.

9. **On-screen vs spoken values.** All numbers match (0%, 300-850, 35/30, 15/10/10, $600/$2,000/30%, 695/718/714). OK.

10. **Layout.** Compare values "35%" and "30%" are 3 characters or fewer (limit 7). There are no keep:true flags. The Acorn style (short, funny squirrel sentences) is followed. OK.

11. **Runtime.** There are 136 spoken words now and 138 with the fixes above, which is inside 115-140.

## Summary of exact replacements

- `lines[0].text`: `Your income counts for 0% of a FICO Score.`
- `lines[0].say`: `Your income counts for zero percent of your credit score.`
- `lines[0].scene.label`: `FICO`
- `lines[5].say`: `Amounts owed tracks credit in use. Six hundred dollars on a two thousand dollar limit is thirty percent.`
- `lines[7].scene.color`: `down`

No factual errors were found. The fixes above are clarity and presentation fixes.

VERDICT: PASS

## Round 2 (editor)
Applied fixes 1-3. VERDICT: PASS
