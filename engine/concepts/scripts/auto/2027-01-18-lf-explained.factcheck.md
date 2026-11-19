# Fact-check: 2027-01-18-lf-explained ("How student debt got so big")

Checked Nov 19, 2026 for posting Mon Jan 18, 2027, 4 PM CT. Every claim was checked with web search. Primary .gov/.org pages (newyorkfed.org, collegeboard.org, FRED) could not be fetched from this session, so they were confirmed through search snippets of those pages and reputable outlets quoting them. All fixes below are applied in `2027-01-18-lf-explained.raw.json`. check.py result: OK, 91 lines, 1776 spoken words.

## Issues found and fixed

| Line | Problem | Fix applied |
|---|---|---|
| 2 | **False.** "Only mortgages are bigger." The NY Fed Q3 2026 report has auto loans at about $1.73T, which is more than student loans at $1.656T. | Changed to "Among household debts, only mortgages and auto loans are bigger." |
| 3, 4, 58 | **Stale.** 42.6M and $1.724T are FSA's March 2026 numbers. FSA's Sept 22, 2026 release gives June 30, 2026: 42.3M recipients and "more than $1.7 trillion". | Now 42.3M, as of June 2026. The average is now "over $40,000 each, on average" (our math: $1.7T / 42.3M = $40,190). Stat values are `42.3M` and `$40,000+`. |
| 11 | **Quote not exact.** The spoken line "a student should not be turned away..." was presented as "his own words", but it is a paraphrase. The verified transcript (American Presidency Project, Remarks at Southwest Texas State College, Nov 8, 1965) reads "...can apply to any college or any university in any of the 50 States and not be turned away because his family is poor." | The narration is now framed so that only the exact words are presented as his: "His goal: any high school senior could apply to college and, in his words, 'not be turned away because his family is poor.'" The on-screen fragment is unchanged and exact (11 words). |
| 13 | Mildly editorial wording ("pretty sweet setup"). | Changed to "a low-risk setup". |
| 20 | **Stale.** College Board's 2026 report (out in fall 2026) puts the 2026-27 public four-year in-state price at $12,290. The $11,950 figure is the 2025-26 number. | The lead stat is now 2026-27 at $12,290. |
| 22-23 | The 2005-06 chart point ($9,050) is the writer's own derived figure and could not be verified against any source. | Dropped the 2005 point. The chart is now 1995 $5,940, 2015 $12,810, 2025 $11,950. $5,940 and $11,950 come from College Board 2025. The $12,810 peak in 2015-16 (2025 dollars) matches NCAN's reading of the College Board chart and fits the report's 7% decline. The narration now says these figures come from College Board's 2025 report, in 2025 dollars. |
| 27-28 | The decline window was vague ("over the last decade"), and the 2026 report has newer data. | Now "fell 7% after inflation in the ten years through 2025-26", plus "Its newest report shows an 8% real drop in the ten years through 2026-27." |
| 31 | **Unverified.** "Student debt passed credit card debt for the first time in Q2 2010" could not be confirmed from any source. | Replaced with a verified claim: "By the end of 2012, the New York Fed said student loans had become the biggest household debt after mortgages" (NY Fed Q4 2012 report, $966B). The headline now reads "Loans now No. 2 debt". This also sets up the line 2 contrast (auto loans have since passed student loans). |
| 41-42 | **Stale.** G.19 "Dec 2025 $1.84T" has been superseded by Q2 2026 at $1,858.2B ($1.86T). "Early 2006" was vague. | Changed to "$481 billion in March 2006 versus $1.86 trillion by June 2026". The ratio went from 3.8x to 3.9x (1858/481 = 3.86). The labels are now `Mar 2006` and `June 2026`. |
| 59 | **Inaccurate.** Daily simple interest changes month-1 interest by dollars, not "a few cents" ($160.77 for 30 days vs $163.00 monthly). | Changed to "so real bills can differ a little from our math". The board now reads "Daily interest: / small differences". |
| 67 | **Stale or misleading.** It implied collections were active. ED paused wage garnishment and Treasury offset (tax refund seizure) on Jan 16, 2026, and reporting through late Oct 2026 says they are still paused. | Changed to "By law, refunds and wages can be taken. Collections restarted in May 2025, then paused again in January 2026." The label is now "Can take refunds" and the caption "Paused again Jan 2026". |
| 68 | Imprecise description of how SAVE ended. | On Mar 9, 2026 the 8th Circuit ordered the Dec 2025 ED-Missouri settlement entered as final judgment, and the district court did so. The line now reads "ended in March 2026, when a court made a settlement final." |
| 71 | "Short window" undersold the Grad PLUS interim exception, which covers students enrolled and borrowing before July 1, 2026. | Changed to "apart from a limited phase-out for students already enrolled and borrowing." |
| 85 | Narration did not match the screen ("1995-96 to 2025-26" vs "nineteen ninety-five to twenty twenty-five"). | Rewritten as "about doubled in thirty years" in both text and say. |
| post | Description cited only College Board 2025 and an unverified "2012 release". | Added the 2026-27 $12,290 figure, College Board 2026, and ED 2026, and removed the "2012 release" source. |

## Verified as written (no change)

- **Hook (line 0):** "Americans owe more on student loans than on credit cards." It is true ($1.656T vs $1.285T), specific, and 10 words (under 3 seconds). It is acceptable. An optional stronger version: "Americans owe more on student loans than on all their credit cards."
- **NY Fed Q3 2026 (released Nov 10, 2026):** student loans $1.656T, credit cards $1.29T (a record), total household debt $19.1T, 10.9% of student balances 90+ days delinquent (up from 10.6%). Student loans are about 8.7% of total debt, so "about 9%" is fine. The Q4 2026 report is not due until Feb 2027, so these are still the latest numbers on Jan 18.
- **NY Fed year-end chart:** 2012 $966B, 2014 $1.16T, 2016 $1.31T, 2018 $1.46T, 2020 $1.56T, 2022 $1.60T, 2024 $1.62T. All confirmed. The +$594B rise from 2012 to 2020 rounds to "about $600 billion".
- **History:** NDEA 1958; HEA signed Nov 8, 1965 at Southwest Texas State; Guaranteed Student Loans; 1976 bankruptcy limit; time limit removed in 1998; 2005 BAPCPA extending the rule to private loans; Grad PLUS from 2006-07 with no fixed cap; direct lending only from July 1, 2010 (SAFRA).
- **College Board 2025:** $5,940 to $11,950 (2025 dollars), which is about double. The +$6,010 and -$860 math is correct.
- **2026-27 rates:** set from the May 12, 2026 10-year auction at 4.468%. Undergrad 6.52% (+2.05), grad 8.07% (+3.60), PLUS 9.07% (+4.60).
- **Worked example, recomputed:** 10 years: $340.95/month, $10,913.92 interest (≈$10,914), $40,914 total, +36%. Month 1: $163.00 interest and $177.95 principal. 20 years: $224.03/month, $23,766.08 interest (≈$23,766), which is 2.18x the 10-year interest ("more than double"). All correct.
- **Pause:** started March 2020 at 0% interest; interest returned Sept 1, 2023 and bills in Oct 2023 (about 3.5 years). Collections restarted May 5, 2025.
- **Defaults:** about 9.3M borrowers and about $234B as of June 30, 2026 (FSA data via Newsweek and The College Investor).
- **OBBBA (P.L. 119-21, July 4, 2025):** these took effect July 1, 2026. Grad $20,500 a year and $100K total; professional $50K and $200K; Parent PLUS $20K a year and $65K per student; lifetime limit $257,500 excluding Parent PLUS. Undergrad limits are unchanged (dependent aggregate $31,000). New loans get Tiered Standard or RAP (1-10% of AGI, $10 minimum, unpaid interest waived, forgiveness after 30 years). Legacy plans (ICR and PAYE) close by July 1, 2028, and IBR stays open for older loans.
- **Politics:** Supporter and critic views are paired (lines 40, 81), and no side is taken. There is no advice and no price prediction. The title and cover ("How It Got Huge.", $1.66T) are paid off by the video.

## Note for before upload (not a script error)

FSA usually posts updated quarterly data in December. By Jan 18 there may be Sept 30, 2026 figures for borrowers and defaults, and a Q3 2026 G.19 (due early Dec 2026). The current lines are dated ("as of June 2026"), so they stay accurate. A quick refresh before upload is optional.

## Sources

- NY Fed Q3 2026 press release: https://www.newyorkfed.org/newsevents/news/research/2026/20261110 ; data: https://www.newyorkfed.org/medialibrary/interactives/householdcredit/data/pdf/HHDC_2026Q3 ; coverage: https://money.usnews.com/investing/news/articles/2026-11-10/ny-fed-finds-troubled-debt-levels-ticked-up-in-third-quarter , https://qz.com/credit-card-debt-record-new-york-fed-household-111026 , https://thecollegeinvestor.com/91905/student-loan-delinquency-hits-10-9-in-new-york-fed-q3-2026/
- NY Fed year-end: https://www.newyorkfed.org/newsevents/news/research/2015/rp150217.html , https://www.newyorkfed.org/newsevents/news/research/2019/20190212 , https://www.newyorkfed.org/newsevents/news/research/2021/20210217 , https://www.newyorkfed.org/newsevents/news/research/2023/20230216 , https://www.newyorkfed.org/newsevents/news/research/2025/20250213 ; Q4 2012 ($966B, No. 2 debt): https://www.scribd.com/doc/132232933/NY-debt-and-Credit-Report-Q42012 , https://www.ibtimes.com/student-loans-surpass-auto-loan-credit-cards-home-equity-become-second-largest-debt-1197937 ; Q4 2016: https://www.businessinsider.in/americans-have-12-58-trillion-of-debt-heres-what-it-looks-like/articleshow/57211308.cms
- FSA portfolio and defaults: https://fsapartners.ed.gov/knowledge-center/library/electronic-announcements/2026-09-22/federal-student-aid-posts-updated-reports-fsa-data-center , https://thecollegeinvestor.com/88850/9-3-million-federal-student-loan-borrowers-are-now-in-default/ , https://www.newsweek.com/student-loan-update-400000-more-borrowers-in-default-under-trump-admin-12485320
- LBJ remarks: https://www.presidency.ucsb.edu/documents/remarks-southwest-texas-state-college-san-marcos , https://www.lbjlibrary.org/news-and-press/media-kits/higher-education-act
- College Board: https://newsroom.collegeboard.org/trends-college-pricing-and-student-aid-report-published-tuition-prices-public-institutions-and , https://www.ncan.org/Web/News/College-Costs-Continue-to-Decline-According-to-Latest-College-Price-Report , https://newsroom.collegeboard.org/average-sticker-prices-public-colleges-rise-less-inflation-grant-aid-brings-average-net-tuition , https://www.insidehighered.com/node/223046
- G.19 and FRED: https://fred.stlouisfed.org/series/SLOASM , https://www.federalreserve.gov/releases/g19/20260807/ , https://eyeonhousing.org/2026/08/consumer-credit-slowed-in-q2/
- 2026-27 rates: https://thecollegeinvestor.com/80477/federal-student-loan-rates-set-to-rise-for-the-2026-27-school-year/ , https://www.collegehelpguide.com/blog/federal-loan-rates-confirmed-2026-27/
- Collections pause: https://marylandmatters.org/2026/01/16/repub/us-education-department-delays-plan-to-garnish-wages-of-student-borrowers-in-default/ , https://www.goodmorningamerica.com/news/story/education-department-delays-plan-garnish-wages-defaulted-student-129295202 , https://www.supermoney.com/student-loan-default-collections-november
- SAVE: https://thecollegeinvestor.com/76476/save-student-loan-plan-officially-ended-by-court-order/ , https://www.ed.gov/about/news/press-release/us-department-of-education-announces-agreement-missouri-end-biden-administrations-illegal-save-plan
- OBBBA: https://www.cbsnews.com/news/student-loan-changes-july-2026/ , https://financialaid.usc.edu/OBBBA , https://www.ed.gov/media/document/rise-final-rule-fact-sheet-113947.pdf , https://www.nasfaa.org/news-item/38809/ED_Publishes_Final_Regulations_Implementing_OBBBA_Federal_Student_Loan_Changes , https://www.opb.org/article/2026/06/10/guide-student-loan-options-change-july-1-what-you-need-to-know/

VERDICT: PASS

## Round 2 (editor)
Reviewed applied fixes. Replaced the 3-point unevenly spaced tuition chart with two stat scenes (same verified values). All other fixes accepted.
VERDICT: PASS
