# Fact-check: 2026-10-08-explainer (Tax refund or owe? Withholding explained)

Checked: September 30, 2026. Posting date: October 08, 2026. Research brief not consulted. Math recomputed in python.

## Verified claims

| Line | Claim | Result | Source |
|---|---|---|---|
| 4 | $12,000 withheld - $9,000 tax = $3,000 refund | Correct | python |
| 5 | $9,000 - $8,000 = $1,000 owed | Correct | python |
| 6 / chart | 2026 avg refund by mid-April = $3,275 (week ending Apr 17, 2026) | Correct | IRS filing season stats wk ending Apr 17, 2026; CNBC Apr 24, 2026 (+11.3%) |
| chart | 2025 = $2,942 (wk ending Apr 18, 2025) | Correct (IRS 2026 release also uses $2,942 as the comparison) | IRS stats wk ending Apr 18, 2025 |
| chart | 2024 = $2,850 (wk ending Apr 19, 2024) | Correct | IRS stats wk ending Apr 19, 2024 |
| chart | 2023 = $2,753 (comparable week, 2023) | Correct (the comparison figure in the IRS Apr 19, 2024 release) | IRS stats wk ending Apr 19, 2024 |
| chart | Growth: +3.5%, +3.2%, +11.3% | Matches the IRS percentages | python |
| 7 | IRS left 2025 withholding tables unchanged after the new law | Correct. The IRS said Form W-4, the withholding tables and payroll forms would stay the same for TY2025, and the new provisions would go into the 2026 tables | IRS "How to update withholding..." page; payroll.org; Thomson Reuters |
| 8 | $3,275 / 12 = about $273 a month, interest-free | Correct ($272.92). The IRS pays interest on a refund only when it is issued more than 45 days late | python |
| 9 | $1,000+ owed, so a penalty can apply | Correct as a "can" statement. The penalty does not apply when the tax due after withholding and credits is under $1,000, or when a safe harbor is met (90% of this year's tax, or 100%/110% of last year's) | IRS Form 2210 rules; multiple tax outlets |
| 9 | 7% for Oct-Dec 2026 | Correct. The IRS announced that individual underpayment and overpayment rates stay at 7% for the quarter starting Oct 1, 2026 (federal short-term rate 4% + 3) | IRS newsroom "Interest rates remain the same for the fourth quarter of 2026"; CPA Practice Advisor Aug 24, 2026 |
| post | Up from $2,942 in 2025 | Correct | IRS |

The on-screen text and spoken numbers match in every line. Cover value $3,275 matches lines 6 and 8. No price predictions. No personal advice. The law is not named ("new tax breaks"), so the wording is politically neutral.

## Issues

1. **Weak opening, line 1 (medium).** "Your tax refund isn't a gift. It's your own money." is true but generic, a cliche viewers have heard before. It has no number or specific fact and no open loop. It is about 10 words, roughly 3.8 s at normal pace, so it runs over the 3-second target.
   Fix: open with the specific number, for example: "The average tax refund hit $3,275 this year. That's your money." This is about 9 words and can be read in under 3 s. Or: "$3,275. That's what the IRS held of your money, interest-free."

2. **Penalty vs interest rate wording, line 9 (medium, accuracy).** "a penalty can apply: 7% a year" conflates the underpayment penalty with the IRS interest rate. The 7% is the quarterly IRS underpayment interest rate. The estimated-tax penalty is computed like interest at that rate on the shortfall, per quarter, until paid. It is not a flat 7% fine. The line also leaves out the safe harbor, so it implies that owing $1,000 or more by itself triggers a penalty. The on-screen label ("IRS underpayment rate") is correct, but the spoken framing blurs the two ideas.
   Fix: say "Owe a thousand or more at filing and an underpayment penalty can apply. It's figured like interest, at seven percent a year right now." Optionally add in the post text: "Generally avoided if withholding covered 90% of this year's tax or 100% of last year's."

3. **Causal overreach, line 7 (low-medium).** "Why? The IRS left 2025 withholding tables unchanged..." presents this as the only reason. Refunds grew because the new deductions were retroactive to 2025 and were claimed at filing, while paychecks were still withheld under the old tables. The unchanged tables are the mechanism, not the whole cause. Outlets describe it as "partly." The yt_desc already says "partly because."
   Fix: "Why? New tax breaks applied to 2025, but withholding tables didn't change until 2026, so many workers overpaid."

4. **Long narration, line 9 (low, read-aloud).** At 26 words (about 10 s) it is by far the longest line, and the phrase "seven percent a year for October through December twenty twenty-six" is clunky to say. Shortening it as in fix 2 solves this.

5. **Staleness and timing (low).** The refund data is from April, about 6 months before posting. It is labeled "By mid-April 2026," so it stays accurate. The video has no hook for why it is posting in October. The Q4 2026 rate is current for the whole posting window, so no time words will be wrong on Oct 8. Optional: use the later IRS figure (through May 8, 2026: $3,276, +11.5%) or frame it as "this year's refund season."

6. **Minor (nit).** The chart_note "overpaid in 2025" sits on the x=2026 point, which is correct (2026 refunds are for 2025 overpayment) but may briefly confuse viewers. Consider "2025 overpayment". Line 4 says "got withheld" where the caption says "was withheld". This is fine.

## Items with no problems

- Cover and title ("Your Refund Isn't a Gift", $3,275): the video pays both off.
- Worked-example math: correct.
- The chart data points match IRS comparable-week figures for each year.
- Time words on Oct 8, 2026: "Oct-Dec 2026" is current. "By mid-April 2026" is correctly dated.
- Advice and predictions: none. "Not financial advice" is present in the post text.
- Political neutrality: OK. The law is referred to only as "new tax breaks."

VERDICT: FAIL
