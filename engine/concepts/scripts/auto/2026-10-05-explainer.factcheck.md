# Fact-check: 2026-10-05-explainer ("Why Your Loan Barely Shrinks")

Checked on September 30, 2026 for posting on October 05, 2026. I checked every claim independently and did not use the research brief.

## Claims checked

| Line | Claim | Result | Source |
|---|---|---|---|
| 26-31 | Freddie Mac PMMS 30-year average hit 7.03% on Sept 24, 2026 | CORRECT. The rate was 7.03%, up from 6.95% the week before. This is the first reading above 7% since January 2025. | Freddie Mac release "Mortgage Rates Average 7.03%" (freddiemac.gcs-web.com, GlobeNewswire 2026-09-24); Fox Business, NPR 2026-09-24 |
| 37-42 | $400K, 30 years, 7.03% costs $2,669 a month | CORRECT. My python run gives $2,669.27. | Standard amortization |
| 49-55 | Month-1 interest: $400,000 x 7.03% / 12 = $2,343 | CORRECT. Exact value is $2,343.33. | Math |
| 62-78 | Principal in month 1 is $326, and the split is 87.8% / 12.2% | CORRECT. Principal is $325.94 and the interest share is 87.79%. | Math |
| 13-20, cover | "First payment can be 88% interest" | CORRECT at this rate and term. 87.8% rounds to 88%. | Math |
| 83-93 | Year-1 payments total $32,031 and the balance falls $4,040 | CORRECT. Payments are $32,031.29 and principal paid is $4,039.81. | Math |
| 100, 239-241 | Principal doesn't win until year 21 | CORRECT. Principal first exceeds interest in payment #243, which is year 21, month 3. | Math |
| 104-229 | Chart points for years 1-30 | CORRECT for the method used. Every point matches the interest share of the first payment in each year: 87.8, 86.9, ... 13.1, 6.8. | Math |
| 248-254 | An extra $100 a month saves $73,421 in interest and pays the loan off 39 months sooner | CORRECT. Savings are $73,420.83 and the loan pays off in 321 months instead of 360. | Math |

## Issues

1. **Line 104 (chart title): the label is ambiguous. This is a minor issue.** The points show the interest share of the first payment of each year, not the share across the whole year. The full-year shares are lower: year 1 is 87.4%, year 21 is 48.8% and year 30 is 3.7%. Fix: change the title to "Interest share of each year's first payment", or keep the title and replace the points with the full-year shares. If you swap in the full-year shares, set `end` to "3.7%".
2. **Line 26 (the news peg will be one week old on the posting date).** Freddie Mac publishes the next PMMS on Thursday, Oct 1, 2026, four days before this posts. "Late September" and "hit 7.03%" will still be true, but the figure will no longer be the latest. Fix: check the Oct 1 PMMS before posting.
   - If the rate moved, change the line to "In late September, the average 30-year rate topped 7% for the first time since January 2025 (7.03%, Freddie Mac)". That keeps the sentence accurate.
   - Alternatively, switch to the Oct 1 number and recompute all the math.
3. **Line 50 (spoken narration is awkward).** "four hundred thousand times seven point oh three percent, over twelve. About twenty-three forty-three." is clunky to say, and the dangling "About twenty-three forty-three" has no unit. Fix: "Why? Interest is charged on what you still owe. Four hundred thousand times seven point oh three percent, divided by twelve, is about two thousand three hundred forty-three dollars."
4. **Line 38 (small spoken/on-screen mismatch).** The narration says "about twenty-six sixty-nine a month" with no unit, while the screen shows $2,669. Also, "about" is unnecessary because the figure is exact. Fix: "the payment is twenty-six sixty-nine dollars a month."
5. **Line 84 (small spoken/on-screen mismatch).** The narration says "about thirty-two thousand dollars" while the screen shows $32,031. The two are consistent because of "about", so this is acceptable. Optional fix: say "thirty-two thousand and thirty-one dollars" to match the screen exactly.
6. **Line 234 (logic and wording).** "That's why, early on..." does not follow from the line before it, because the chart explains why principal is slow, not why extra payments help. The line is also close to prescriptive, although it describes a mechanism and gives no instruction. Fix: "Which means any extra principal paid early cuts the balance that all future interest is charged on."
7. **Post text (ig and yt_desc) cites CFPB as a source, but no claim in the script relies on CFPB.** This is minor. Fix: drop CFPB, or cite the CFPB amortization explainer by name.
8. **Hook (line 13).** The hook is true and specific. It takes about 2.8 seconds to say, so it fits the 3-second limit, and it creates a need to know why. It passes. Optional way to make it stronger and more concrete: "On a $400K mortgage, your first payment is 88% interest."

## Other checks
- **Advice or price predictions:** none. The extra-$100 line is framed as "in this example", and the post text carries "not financial advice".
- **Political opinion:** none.
- **Cover and title payoff:** the video pays off both "Why Your Loan Barely Shrinks" and the "88%" label.
- **Other time words:** no "this week", "today" or "yesterday" anywhere. "Late September 2026" will still be accurate on Oct 5.
- **Math errors:** none. All worked-example numbers reproduce to the dollar.

VERDICT: PASS
