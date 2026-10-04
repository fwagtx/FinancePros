# Fact-check: 2026-12-03-explainer (lemon laws, vertical short, posts Dec 3, 2026)

Checked October 4, 2026. Line numbers are 0-based indexes into `lines`.

## Verified OK
- **All 50 states have a new-car lemon law** (DC does too). Correct.
- **CA presumption numbers (line 3):** Civ. Code 1793.22(b) applies within 18 months or 18,000 miles, whichever comes first. It is met by (1) 2 or more repairs of a defect likely to cause death or serious injury, plus direct notice to the maker; (2) 4 or more repairs of the same defect, plus direct notice to the maker; or (3) more than 30 cumulative calendar days out of service for repairs. "4" and "30+" are correct. The sub-label "total, any defect" is correct, because the days count across any nonconformities.
- **Usage offset (line 5):** Civ. Code 1793.2(d)(2)(C) uses the price paid × miles before the first delivery for repair of that defect ÷ 120,000. $50,000 × 6,000 / 120,000 = **$2,500**, recomputed in python. The example is labeled hypothetical, and the on-screen and spoken values match. AB 1755 / SB 26 (2025) did not change the formula.
- **CA attorney fees (line 7):** Civ. Code 1794(d) says a prevailing buyer "shall be allowed" costs and attorney fees "reasonably incurred". The fees are mandatory, so the line is accurate. (Magnuson-Moss fees are discretionary: "may".)
- **Magnuson-Moss (line 6):** The law covers written warranties on used cars too, and it gives consumers a federal right to sue with fee shifting. It does not require anyone to give a warranty.
- **Exclusions (line 4):** Accident damage, abuse or neglect, unauthorized modifications, and defects that don't substantially impair use, value or safety are standard exclusions. This is acceptable as a general list.
- **The 10-state list** (AZ, CT, HI, IL, MA, MN, NJ, NM, NY, RI) matches the CT Office of Legislative Research (2015-R-0285) and NCLC. Illinois's 15-day/500-mile powertrain warranty (815 ILCS 505/2L, from July 2017) is still in effect. New York's used-car law is confirmed by the NY AG (dealer warranty; refund after a reasonable number of tries).
- No time words go stale by Dec 3, 2026. No political content. No keep:true lines. The compare values on line 3 ("4", "30+") are ≤7 characters.

## Issues

1. **Wrong source attribution (line 1 scene.sub "J.D. Power list"; yt_desc "per J.D. Power and the New York Attorney General"). FACT ERROR.**
   J.D. Power's used-car lemon law guide says "only **seven** states": CT, **CA**, MA, MN, NJ, NM, NY. That is not about 10, and it includes California, which is not on the 10-state list. The NY AG page covers only New York's law and gives no national count. The "about 10" figure comes from the CT Office of Legislative Research / NCLC list.
   **Fix:** Change sub to "CT legislative research" or "NCLC count". In yt_desc write "only about 10 have one for used cars, per Connecticut's Office of Legislative Research", and drop the J.D. Power attribution or move it elsewhere. Replace "J.D. Power" in the IG Sources line too. Optional: add "counts vary" (sources say 7 to 10), e.g. sub "Counts vary: 7-10".

2. **Hook overstates (line 0, cover/hook value "NOPE"; post title).**
   "In most states, lemon laws don't cover used cars" is mostly right about used-car-specific laws. But in many states (for example WA, TX, VA), the new-car lemon law still covers a used car bought while it is within the original warranty or lemon-law period. California is the exception: Rodriguez v. FCA (2024) excludes used cars with leftover factory warranty, but CPO cars with a warranty issued at sale still count. The flat "NOPE" next to "USED" reads as a universal no, which contradicts "in most states" and this nuance.
   **Fix:** Change the hook and cover value "NOPE" to **"RARELY"** (6 chars). Keep the spoken hook, or tighten it to: "Bought a used car that's a lemon? In most states, the lemon law won't save you." The current hook is true and specific, but it is a flat statement. A second-person version creates more need-to-know and stays under 3 seconds.

3. **CA presumption simplified (line 3).**
   The 4-try route also needs at least one direct notice to the manufacturer (when the maker disclosed that requirement), and serious-safety defects need only 2 tries. As written it is not false, but it is incomplete.
   **Fix:** Caption: "California presumes a lemon within 18 months/18,000 miles: 4 repair tries (2 for safety defects), or 30+ days in the shop." Optionally add the compare sub "same defect, maker notified".

4. **Generalized remedy (line 2): "the maker refunds or replaces the car".**
   This is acceptable for a summary. Laws use "substantial" defect and a "reasonable number" of attempts, and in some states the maker, not the buyer, chooses the remedy. It is minor, but "serious" should be "substantial".
   **Fix:** "If a substantial defect isn't fixed after repeated tries, the maker must refund or replace the car."

5. **Line 6 wording "makes it enforceable".**
   Written warranties are already enforceable under state contract law. What Magnuson-Moss adds is a federal right to sue and recovery of attorney fees. The line also leaves out that "as is" cars with no written warranty get no Magnuson-Moss help.
   **Fix:** "Used car with a written warranty? Federal Magnuson-Moss law lets you sue if it's broken. Sold 'as is'? It doesn't help."

6. **Line 7 could read as a promise or legal advice.**
   "Winning buyers get attorney fees paid by the maker." The statute says fees "reasonably incurred", awarded by the court, and the defendant can be the seller as well as the maker. The meaning is fine, but soften the wording to explanation.
   **Fix:** "In California, buyers who win can recover reasonable attorney fees from the maker." Change sub to "CA, if buyer wins; court sets amount".

7. **Line 4 caption vs. narration.**
   The caption says "Not covered: ..." with "unauthorized mods". The narration says "What's not covered? ... unauthorized modifications". This matches and is fine. Note that the exclusions vary by state; adding "Typically" to the caption would help ("Typically not covered: ...").

8. **No instruction-style takeaways.** No price predictions. The disclaimer is present in the posts. The CTA is fine.

## Summary
The core law and math check out. However, the "About 10" stat is attributed to J.D. Power on screen and in the YouTube description, and J.D. Power actually says seven states, including California. That is a wrong-source fact error. The "NOPE" hook value is also more absolute than "in most states" supports. Fix items 1 and 2, and ideally 3 and 5.

Sources: jdpower.com/cars/shopping-guides/used-car-lemon-laws (search excerpt); cga.ct.gov/2015/rpt/2015-R-0285.htm; library.nclc.org "12 Ways to Recover..."; ag.ny.gov used-car lemon law fact sheet; illinoisattorneygeneral.gov 15-day/500-mile FAQ; Cal. Civ. Code 1793.22, 1793.2(d)(2)(C), 1794(d) (Justia/FindLaw); Rodriguez v. FCA US (Cal. 2024, Justia); FTC/Center for Auto Safety Magnuson-Moss overviews.

VERDICT: FAIL

## Round 2 (editor)
- Line 1 sub: "Counts vary: 7-10"; J.D. Power credit removed from yt_desc and IG (now CT Office of Legislative Research, counts vary).
- Line 0 / cover: hook now "Most states have no lemon law just for used cars." with value "RARELY" (no absolute "NOPE"); post title/IG/TikTok match.
- Line 3: adds "maker notified; 2 for safety defects" (caption, narration, compare sub).
- Line 2: "substantial defect ... isn't fixed after repeated tries, the maker must refund or replace it".
- Line 6: "lets you sue if it's broken. Sold 'as is'? It doesn't help."
- Line 7: "buyers who win can recover reasonable attorney fees from the maker."
- Line 4: "Typically not covered".
VERDICT: PASS
