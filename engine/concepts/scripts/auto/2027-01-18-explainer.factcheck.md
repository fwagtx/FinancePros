# Fact-check: 2027-01-18 explainer (credit utilization, paid in full but score drops)

Checked 2026-11-19 for posting Mon Jan 18, 2027, 12:00 CT. Sources checked independently. The research brief was not read.

## Verified claims
- **Issuers usually report the statement balance (line 1).** VERIFIED. myFICO: "The total balance on your last statement is generally the amount that will show in your credit report... even if you pay your credit card balances in full each month, your account balance won't necessarily show on your credit report as $0." Experian: issuers "usually report... the current balance and credit limit... around the end of each statement period." Because that is before the due date, "before your payment is even due" holds.
- **Amounts owed = 30% of a FICO Score (line 2).** VERIFIED. myFICO: "Amounts owed on accounts determines 30% of a FICO Score."
- **Math (line 3).** VERIFIED. $2,000 / $2,500 = 0.80 = 80%. Board, text, say and cover "80%" all agree.
- **Experian March 2026 utilization by score band (line 4, compare chart).** VERIFIED. Experian "State of Credit Cards" page (updated Jul 27, 2026; table labelled March 2026): Poor (300-579) 76.8%, Fair 59.2%, Good 38.5%, Very good 14.6%, Exceptional (800-850) 6.4%. The screen shows 6.4% and 76.8%. The narration says "about six" and "about seventy-seven", which is allowed rounding. Note: Experian's older utilization explainer page still shows Q3 2024 figures (7.1% and 80.7%). The script correctly uses the newer March 2026 data. It is still the latest Experian release as of today. Re-check before posting in case Experian publishes newer data.
- **Classic scores have "no memory" (line 6).** SUPPORTED. FICO describes non-trended scores as using "the most recently reported month of data". myFICO forum moderators describe FICO utilization as having no memory. Experian says utilization updates each time the issuer reports, typically once per billing cycle.
- **FICO 10T looks back 24 months (line 6).** VERIFIED. The FICO marketplace blog says trended data covers "monthly account balances for the previous 24+ months". Experian says trended data covers card balances, minimum payments and amounts paid "going back 24 months".
- **Experian on the 30% level (line 7).** The original wording was INACCURATE and has been rewritten (see issue 3). Experian's actual wording: "there's no specific point when your utilization rate goes from good to bad, 30% is the point at which it starts to have a more pronounced negative effect." Another Experian page calls under 30% "a good rule of thumb". So "a guideline, not a rule" was not Experian's phrase and partly contradicts "rule of thumb".

## Issues found and fixes applied
1. **Line 0 hook (weak and untrue).** "You paid your card in full. Your score still dropped." states as fact something that only *can* happen, and the post title already says "can still drop". FIX: text/say -> "Paid your card in full? Your score can still drop." That is 10 words, true, and opens on a question the viewer needs answered. Hook title "Paid in [full]?" is kept.
2. **Line 4 (awkward narration, unit dropped).** "800-plus scorers ... poor scores about seventy-seven" drops "percent" and reads awkwardly out loud. FIX: text -> "Experian's March 2026 data: people scoring 800-plus used about 6% of their limits. Poor scores? About 77%." Say -> "...people scoring eight hundred plus used about six percent of their limits. Poor scores? About seventy-seven percent." The chart (6.4% and 76.8%, Mar 2026) is unchanged.
3. **Line 7 (misattributed wording).** "Experian calls it a guideline, not a rule" is not Experian's wording. FIX: text -> "And under 30%? Experian says there's no magic cutoff. Lower is better, and your statement balance counts." Say matches, with "thirty percent" spelled out. List item "30% = guide" -> "No magic 30%".
4. **Line 5 (overstated certainty).** "looks like the low-score crowd" -> "can look like the low-score crowd, even if paid off." This also trims words to stay within 115-140.
5. **Captions.** The IG first line repeated the untrue hook. It now reads "Paid your card in full? Your score can still drop. Here's why." The IG now names the Poor band (300-579), rewords the classic-score line ("Classic scores like FICO 8 use your latest reported balance..."), and adds Experian's no-magic-cutoff point. TikTok -> "Paid in full, score can still drop? ...". YouTube description adds the 76.8% figure for poor scores.

## Other checks (no issue)
- Stale news or time words: none. "March 2026 data" is a dated reference, not a relative time word, so it is still correct on Jan 18, 2027.
- Advice or price predictions: none. The script is educational, and the captions carry the "not financial advice" line.
- Political opinion: none.
- Cover "Paid Off. Why?" / 80% is paid off by lines 1-5. The post title is paid off.
- On-screen vs spoken values all match, with "about" rounding only.
- check.py: OK (9 lines, 139 spoken words, hook 10 words).

## Sources
- myFICO, Amounts owed: https://www.myfico.com/credit-education/credit-scores/amount-of-debt
- Experian, State of Credit Cards (updated Jul 27, 2026; March 2026 utilization table): https://www.experian.com/blogs/ask-experian/state-of-credit-cards/
- Experian, What Is a Credit Utilization Rate? (30% wording; reporting at end of statement period; Q3 2024 table): https://www.experian.com/blogs/ask-experian/credit-education/score-basics/credit-utilization-rate/
- Experian, How Much Available Credit Should I Have? ("good rule of thumb"): https://www.experian.com/blogs/ask-experian/how-much-available-credit-should-i-have/
- FICO marketplace blog, FICO Score 10 Suite (trended data 24+ months): https://marketplace.fico.com/blogs/fico-score-10-suite-available-all-three-credit-bureaus
- Experian, FICO 10 scores (trended data going back 24 months): https://www.experian.com/blogs/ask-experian/FICO-10-score-changes-what-it-means-to-your-credit
- myFICO forums, "Does utilization have a memory?": https://ficoforums.myfico.com/t5/Understanding-FICO-Scoring/Does-utilization-have-a-memory/m-p/6093149

VERDICT: PASS

## Round 2 (editor)
Reviewed applied fixes: hook says "can still drop", no false Experian quote, natural narration.
VERDICT: PASS
