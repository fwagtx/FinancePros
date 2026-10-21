# Fact-check: 2026-12-20-explainer (Tax extensions: more time to file, not more time to pay)

Checked 2026-10-21 for a post on Sun 2026-12-20, 12 PM CT. Source: the .raw.json only. Math rerun in Python.

## Verified claims
- **Deadlines (L2–L3, L10, post):** 2026 returns and payments are due Thu Apr 15, 2027, and the extended due date is Fri Oct 15, 2027. Both are weekdays, so no rollover. Correct.
- **Form 4868 extends filing, not payment (L1, L3, L10):** IRS says an extension "does not provide additional time to pay taxes owed." Correct. The hook is true and specific.
- **Payment marked as an extension (L9):** IRS says you don't need to file a Form 4868 when paying through Direct Pay, EFTPS or debit/credit card if you select "Form 4868"/extension as the payment type. Correct.
- **Penalty rates (L5–L6):** Failure-to-file is 5%/month, capped at 25%. Failure-to-pay is 0.5%/month, capped at 25%. Correct. For "usually 10 times bigger", an IRS Tax Tip says the FTF penalty is "usually much more" than the FTP penalty and "in most cases, it's 10 times more." The paraphrase is fair.
- **Worked example (L7–L8):** $4,000 owed, filed and paid 5 months late.
  - No extension: the coordination rule (IRC 6651(c)(1)) cuts FTF to 4.5% in each month both penalties apply. 4.5% x 5 = 22.5% = $900 FTF, and 0.5% x 5 = 2.5% = $100 FTP. Total **$1,000** (25%). Correct, and the sub "25% of $4,000" is correct.
  - The $900 FTF is above the >60-day minimum penalty (about $525 for 2026 returns, indexed), so the minimum doesn't change the result.
  - With an on-time extension: the return is filed Sept 15, inside the Oct 15 extension, so there is no FTF. FTP = 2.5% = **$100**. Correct.
  - Labeled as an example ("Say someone...") and "Interest extra" is on screen. Good.
- **Interest rate (L4):** 7% for individuals in Q4 2026 (IR-2026-98, Aug 21, 2026; Rev. Rul. 2026-15). Correct. "From April" is correct: interest runs from the original due date even with an extension.
- **Chart (L4), Q1 rates:**
  - 2022 Q1: 3% (IR-2021-234)
  - 2023 Q1: 7% (up from 6%)
  - 2024 Q1: 8%
  - 2025 Q1: 7% (IR-2024-290)
  - 2026 Q1: 7%

  All five points are correct. End label "7%" matches the Q4 2026 spoken rate.
- **Spoken vs on-screen values:** they match on every line.
- **Interest wording:** no line implies an extension avoids interest. L4, L7 ("Interest extra"), L10 and the post copy all keep interest separate. Good.
- **keep:true:** L3 (timeline after timeline) and L6 (compare after compare) are fine.
- **Limits:**
  - Compare values "0.5%/mo" = 7 chars, "$1,000" = 6, "$100" = 4. All OK.
  - Subs are all ≤18.
  - Board lines are ≤20 ("Paying: still Apr 15" = 20).
  - List items are ≤16.
  - Timeline when values are 5 chars.
  - post.title = 48, tiktok = 134.
  - Spoken words = 138.
- **Rules check:** no advice imperatives, price predictions, politics, or quotes.

## Issues (none blocking)
1. **L4 chart, unlabeled data basis (minor).** The x-axis shows years, but each point is the Q1 rate, and rates changed within some years (for example, 2022 went 3% to 6%). Optional fix: scene.title `"IRS interest rate"` -> `"IRS rate each Jan"`. No spoken change.
2. **L4 time word risk (minor).** The Q1 2027 rate will be announced around mid-November 2026, before the post date. "As of late 2026" stays literally true, but if Q1 2027 moves off 7%, viewers watching in 2027 get a stale rate. Recheck in late November. If the rate changes, keep the wording and leave the 7% end label as is, since it is still accurate "as of late 2026".
3. **L7 board vs narration (minor).** Board says "Paid 5 months late" but the narration says "files and pays." Fix: `"Paid 5 months late"` -> `"Filed+paid 5 mo late"` (20 chars).
4. **L8 compare title (minor clarity).** The right-side value "$100" without "penalties" on screen could read as the total cost. Fix: scene.title `"5 months late"` -> `"Penalties, 5 mo"` (15 chars). No spoken change.

No fix adds spoken words.

## Sources
- IRS, Q4 2026 interest rates: https://www.irs.gov/newsroom/interest-rates-remain-the-same-for-the-fourth-quarter-of-2026
- IRS Q1 rates: 2022 https://www.irs.gov/node/102611 ; 2023 https://www.irs.gov/node/116646 ; 2024 https://www.irs.gov/node/128371 ; 2025 https://www.irs.gov/newsroom/interest-rates-decrease-for-the-first-quarter-of-2025 ; 2026 https://www.irs.gov/node/152321
- IRS Tax Tip 2014-56 (10 times): https://www.irs.gov/node/9399
- IRS extension guidance: https://www.irs.gov/node/14407
- FTF/FTP coordination and minimum penalty: https://beancount.io/blog/2026/09/28/failure-to-file-vs-failure-to-pay-penalty-section-6651-guide

VERDICT: PASS

## Round 2 (editor)
Applied optional fixes 1, 3, 4. Recheck the Q1 2027 IRS rate in late November.
VERDICT: PASS
