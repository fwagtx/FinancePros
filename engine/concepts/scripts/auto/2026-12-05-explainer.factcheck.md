# Fact-check: 2026-12-05-explainer (Severance pay: what's negotiable)

Checked Oct 6, 2026 against the raw script JSON only. Line numbers are 0-based indexes into `lines`.

## Verified claims
- **Line 0/1, no federal severance law / "matter of agreement":** DOL Severance Pay page and FLSA FAQ say severance is "a matter of agreement between an employer and an employee" and that the FLSA does not require it. Correct.
- **Line 2, WARN Act:** employers with 100+ workers must give 60 days' notice of plant closings and mass layoffs. If they don't, they owe back pay and benefits for the violation period, up to 60 days (DOL employer guide). The numbers are right, but the wording needs work (see Issues 1 and 2).
- **Line 3, Challenger annual announced job cuts:** 2019 592,556 (593K); 2020 2,304,755 (2,305K); 2021 321,970 (322K); 2022 363,824 (364K, correct rounding; the brief's 363,832 is slightly off but rounds the same); 2023 721,677 (722K); 2024 761,358 (761K); 2025 1,206,374 (1,206K, "1.2M"). Every chart point checks out. The caption says 1,206,374 and the narration says "about one point two million", which agree.
- **Line 4, math:** $60,000 / 52 x 10 = $11,538.46, which rounds to $11,538. Correct. The assumption is 52 paid weeks a year, which is reasonable.
- **Line 5, withholding:** 22% x $11,538.46 = $2,538.46, which rounds to $2,538. Correct. Pub 15 (2026) keeps the 22% flat rate (37% on supplemental wages above $1M), because P.L. 119-21 made the TCJA rates permanent.
- **Line 7, OWBPA/ADEA:** 21 days to consider, 45 for a group exit or termination program, and 7 days to revoke (EEOC). Correct. "Group layoffs" is an acceptable simplification.
- **Line 8, unemployment:** the effect of severance on unemployment benefits varies by state. Correct.
- **Line 6, negotiable items:** amount, COBRA premium subsidies, equity vesting and non-compete terms are commonly negotiated. The line describes what people do and doesn't tell anyone what to do. OK.
- **Compare values:** "$11,538" and "-$2,538" are both 7 characters. OK.
- **keep:true:** no line uses it.
- **Spoken vs on-screen values:** they match on every line.

## Issues
1. **Line 2, "The exception" partly contradicts the hook (moderate).** WARN does not require severance. It requires notice, and back pay is the penalty for skipping it. Calling it "the exception" right after "no federal law requires severance" suggests there is a federal severance mandate after all.
   - Fix the caption to: "One related rule (WARN Act): firms with 100+ workers must give 60 days' notice of mass layoffs, or owe up to 60 days' back pay."
   - Fix the narration to: "One related rule: firms with a hundred-plus workers must give sixty days' notice of mass layoffs, or owe up to sixty days of back pay."
2. **Line 2, the back pay needs "up to" (minor).** "Owe ... back pay" reads like an open-ended amount. Add "up to 60 days". Leaving out plant closings and the 50+/33% layoff thresholds is an acceptable simplification.
3. **Cover and line 0 scene, "0 laws" is false as written (wrong fact, on screen).** Next to "Is Severance Required?", "0 laws" says no law anywhere requires severance. That is wrong: New Jersey's amended WARN law (2023) requires 1 week of severance per year of service in covered mass layoffs. Fix the value to "0 federal" or "No fed law". Better still, add a short caveat to line 8 or 1, such as "Some states, like New Jersey, require it in mass layoffs."
4. **Line 5, "taxed" vs "withheld" (moderate).** The caption and compare panel correctly say withholding. The narration's "It's taxed as supplemental wages, so twenty-two percent ... takes" sounds like the final tax. 22% is an optional flat withholding method: the employer may use the aggregate method instead, the actual tax is settled at filing, and FICA and state withholding come on top.
   - Fix the narration to: "It counts as supplemental wages, so employers can withhold a flat twenty-two percent federal, about two thousand five hundred thirty-eight. Your real tax is settled at filing."
   - In `post.tiktok`, change "the 22% tax" to "22% withholding".
5. **Line 4, awkward narration (nit).** "About" before an exact figure ("about eleven thousand five hundred thirty-eight dollars") reads oddly. Fix: "That's ten weeks, or eleven thousand five hundred thirty-eight dollars."
6. **Hook, line 0 (nit).** It is true, specific and about 2.5 seconds long. "Your job" is awkward. A stronger version: "No federal law says your employer owes you severance." It is not contradicted, as long as Issues 1 and 3 are fixed.
7. **Disclaimers (nit).** The post text says "not financial advice", while the CTA says "not legal advice". Use "Education, not legal or financial advice" in both. Nothing in the script says sign or don't sign, and there are no instruction-style takeaways. No predictions or political content.
8. **Time words:** "in 2025" will still be right on Dec 5, 2026. The chart uses full years only, so nothing is stale.

VERDICT: FAIL

## Round 2 (editor)
- Line 2: "One related rule" (WARN = notice, back pay as penalty), not "the exception".
- Cover/line 0: value "US: none" (federal), and New Jersey's mass-layoff severance rule noted on line 8 caption and in IG.
- Line 5: "employers can withhold a flat 22% federal ... Real tax is settled at filing"; TikTok says "22% withholding".
- Line 4: dropped "about" before the exact figure.
VERDICT: PASS
