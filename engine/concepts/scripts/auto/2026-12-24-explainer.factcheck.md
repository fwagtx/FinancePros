# Fact-check: 2026-12-24-explainer (529 plans)
Checked Oct 25, 2026 for posting Thu Dec 24, 2026, 12 PM CT. Line indexes are 0-based.

## Verified
- Line 1: Federal tax-free growth and tax-free qualified withdrawals are correct. "State perks vary" is fine.
- Line 2 chart: ICI year-end totals 2020 $425.2B, 2021 $480.4B, 2022 $411.3B, 2023 $471.2B, 2024 $525.1B, 2025 $602.9B all match ICI's Q4 statistical releases (ici.org/research/stats/529s/529s_XX_q4). Dec 2025 is confirmed: $602.9B, up 14.82% from year-end 2024 (ICI release dated March 2026; the page header shows a "2025" date typo). "About $603 billion" and end label "$603B" are fine. Year labels are correct. Note: ICI will probably have published June 2026 data by Dec 24, 2026, so this is not the newest figure. It is clearly dated "end of 2025", though, so it is accurate and not a blocker.
- Line 3: OBBBA (signed July 4, 2025) raised the K-12 cap from $10,000 to $20,000 per year starting in tax years after Dec 31, 2025. Correct. Broadened K-12 expenses (curriculum, books, tutoring, testing fees, dual enrollment, therapies) took effect at enactment. The script does not mention them, which is acceptable. Compare values and subs are within limits.
- Line 4: Recomputed $100/mo, 216 months, 6%/12 monthly, end-of-month deposits: FV = $38,735.32, so $38,735 is correct. Contributions = $21,600, correct. It is labeled "Example" and "assumed", not a prediction. On-screen and spoken values match.
- Line 5: Non-qualified withdrawals: earnings are subject to income tax plus a 10% additional tax. Exceptions (scholarship, death, disability, military academy, education credits) waive the 10% penalty only. Earnings are still taxed. See the fix below.
- Line 6: SECURE 2.0 529-to-Roth: account open 15+ years, $35,000 lifetime, subject to the annual IRA limit (2026: $7,500, per IRS Notice 2025-67), the beneficiary must have earned income, and contributions or earnings from the last 5 years are ineligible. "Within yearly limits" covers this enough for a short.
- Hook (line 0): true, specific, 12 spoken words, under 3 seconds. Lines 5-6 pay it off: the money can be used, at a cost, or rolled to a Roth IRA. Cover "Is 529 Money Stuck?" / "$35K" is paid off by line 6 and is the correct lifetime cap. It is not misleading.
- No advice, no price prediction, no political opinion. Using the bill's official name is neutral. No quotes. No time words that will be wrong on Dec 24, 2026.
- Limits: all within. Hook title 16, cover title 19, cover value 4, prop label 3, board lines <=17, compare values 7, subs <=16, stat label 13, value 4, sub 16, chart end 5, post.title 55, tiktok 143. Spoken total is 138 words (in range). Every line's text matches its say. No keep:true flags.

## Issues and fixes (recommended, not blocking)
1. Line 5 says the exceptions apply to the tax as well as the penalty, but scholarships and similar exceptions waive only the 10% penalty. Replace with the following (19 spoken words, same as now):
   - text: "Spend it elsewhere? The IRS taxes earnings plus a 10% penalty, waived for things like scholarships."
   - say: "Spend it elsewhere? The I R S taxes earnings plus a ten percent penalty, waived for things like scholarships."
2. Line 6: when spoken, "a fifteen-year-old account" sounds like a 15-year-old child, and "student's" is less precise than "beneficiary's". Replace with the following (25 spoken words, same as now, so the total stays 138):
   - text: "Under SECURE 2.0, after 15 years, up to $35,000 can roll to the beneficiary's Roth IRA, within yearly limits."
   - say: "Under SECURE two point oh, after fifteen years, up to thirty-five thousand dollars can roll to the beneficiary's Roth I R A, within yearly limits."
3. Optional: post.ig/yt_desc could add "2026 IRA limit $7,500; beneficiary needs earned income; last-5-year contributions excluded" for completeness.

Sources: ICI 529 statistical reports Q4 2020-2025 (ici.org); IRS Notice 2025-67 via Accounting Today / InvestmentNews; OBBBA 529 summaries (J.P. Morgan, Voya, Weaver).

VERDICT: PASS

## Round 2 (editor)
Applied suggested fixes 1-2 (penalty waiver wording, Roth rollover wording).
VERDICT: PASS
