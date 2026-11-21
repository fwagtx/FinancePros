# Fact-check: 2027-01-20-explainer (posts Wed Jan 20, 2027, noon CT)

Checked Nov 21, 2026. I verified every claim independently with web search (irs.gov snippets and calendar sources). I did not read research.md.

## Claims verified
| Line | Claim | Result | Source |
|---|---|---|---|
| 0 | Employers have until Feb 1, 2027 to furnish W-2s | TRUE. Jan 31, 2027 is a Sunday, so the IRC 7503 weekend rule moves it to Mon Feb 1 (Feb 1, 2027 is a Monday). | https://www.irs.gov/instructions/i1099gi ; https://dupple.com/learn/when-are-1099s-due |
| 1 | Jan 31, 2027 is a Sunday; the deadline moves to Monday | TRUE | calendar check (Feb 1, 2027 = Monday) |
| 2 | Most 1099s are due the same day (bank interest, freelance pay) | TRUE. Recipient copies of 1099-NEC, -INT, -DIV and -MISC (except boxes 8/10) are due Feb 1, 2027. | https://www.irs.gov/publications/p1099 ; https://www.taxbandits.com/1099-forms/1099-reporting-requirements/ |
| 3 | Brokerage 1099-Bs are due Feb 16 because of Presidents' Day | TRUE. The normal date is Feb 15; Presidents' Day (Washington's Birthday) is Mon Feb 15, 2027, so it moves to Tue Feb 16. | https://www.officeholidays.com/countries/usa/presidents_day.php ; https://www.calendardate.com/presidents_day_2027.htm ; https://irs.gov/pub/irs-pdf/i1099gi.pdf |
| 4 | The 2026 season opened Jan 26 (announced in IR-2026-02) | TRUE. IR-2026-02 (Jan 8) announced the date; IR-2026-12 (Jan 26) opened the season. The original line was STALE, see issue 1. | https://www.irs.gov/newsroom/irs-announces-first-day-of-2026-filing-season-online-tools-and-resources-help-with-tax-filing ; https://content.govdelivery.com/accounts/USIRS/bulletins/40619f4 |
| 5 | Most e-filed, direct-deposit refunds arrive within 21 days | TRUE (IRS: "less than 21 days") | https://www.irs.gov/newsroom/tax-time-guide-use-wheres-my-refund-tool-to-track-refund-status ; https://irs.gov/newsroom/reasons-why-some-tax-refunds-filed-electronically-take-longer-than-21-days |
| 6 | Claiming the EITC or ACTC means, by law, the whole refund waits until mid-February | TRUE. Under the PATH Act the IRS cannot issue these refunds before mid-February, and it holds the entire refund, including the part not tied to EITC/ACTC. | https://webarchive.library.unt.edu/web/20201218003553/https://www.irs.gov/individuals/refund-timing ; https://www.irs.gov/for-tax-pros/new-federal-tax-law-may-affect-some-refunds-filed-in-early-2017 |
| 7 | In 2026 the IRS expected most EITC/ACTC refunds by March 2 | TRUE (IR-2026-12, for direct deposit with no other issues) | https://www.irs.gov/node/154686 |
| 8 | Average refund $3,275 in 2026 by Tax Day week | TRUE (week ending Apr 17, 2026) | https://www.irs.gov/newsroom/filing-season-statistics-for-week-ending-april-17-2026 |

## Chart points
Each point is the cumulative average refund from the IRS weekly report for the week that contains Tax Day.

| Year | Value | Week ending | Tax Day | Source |
|---|---|---|---|---|
| 2022 | $3,012 | Apr 22, 2022 | Apr 18 | https://www.irs.gov/newsroom/filing-season-statistics-for-week-ending-april-22-2022 |
| 2023 | $2,753 | Apr 21, 2023 | Apr 18 | https://www.irs.gov/newsroom/filing-season-statistics-for-week-ending-april-21-2023 |
| 2024 | $2,850 | Apr 19, 2024 | Apr 15 | https://www.irs.gov/node/134006 |
| 2025 | $2,942 | Apr 18, 2025 | Apr 15 | https://www.irs.gov/newsroom/filing-season-statistics-for-week-ending-april-18-2025 (also the comparison column in the Apr 17, 2026 report) |
| 2026 | $3,275 | Apr 17, 2026 | Apr 15 | https://www.irs.gov/newsroom/filing-season-statistics-for-week-ending-april-17-2026 |

All five values are confirmed and comparable: same metric, same report week relative to Tax Day. The $3,012 (2022) and $2,753 (2023) values are not from the "mid-April" weeks. The Apr 15, 2022 and Apr 14, 2023 reports show $3,103 and $2,840. That is why the "mid-Apr" title was inaccurate (issue 2).

## Issues found and fixed
1. **Stale (line 4).** "The IRS hasn't named a 2027 opening day" will almost certainly be false by Jan 20, 2027, because the IRS normally announces the date in early January.
   - Replaced with TEXT "The IRS usually opens filing in late January. In 2026, it opened January 26." and SAY "The IRS usually opens filing in late January. In twenty twenty-six, it opened January twenty-sixth."
   - The new wording is true: the season opened Jan 24, 2022; Jan 23, 2023; Jan 29, 2024; Jan 27, 2025; and Jan 26, 2026.
2. **Chart title (line 8).** "Avg refund, mid-Apr" was inaccurate: the 2022 and 2023 points come from Apr 22 and Apr 21 reports. Changed it to "Avg refund, Tax Day wk" to match the spoken "By Tax Day week".
3. **Stale caption (post.ig).** "The IRS hasn't announced the 2027 opening day yet" was replaced with "The IRS usually opens filing season in late January; the 2026 season opened Jan. 26, 2026." I also changed the chart caption to name the exact report weeks.
4. **Wrong source attribution (post.yt_desc).** The $3,275 average was credited to IR-2026-02, a release that has nothing to do with refund amounts. It now reads "IRS filing season statistics, week ending Apr. 17, 2026".

## Other checks (no change needed)
- **Hook:** "Your employer doesn't have to send your W-2 until February first." It is 12 spoken words, under 3 seconds, true and specific, and it makes viewers want to know why. Acceptable. (It could be stronger as "Your W-2 isn't late yet: the deadline is February first.", but the current line passes.)
- **Cover and title:** "When W-2s Arrive" / Feb 1, and "When your W-2, 1099s and tax refund actually arrive". The video pays off both.
- **On-screen vs spoken values:** they match (Feb 1, Feb 16, Jan 26, 21 days, mid-Feb, Mar 2, $3,275).
- **Math:** no worked examples.
- **Advice, predictions, politics:** no advice, price predictions or political opinion. "Not financial advice" is in the captions.
- **Time words:** "In 2026" references are past tense and labelled, so they are fine on the posting date. Feb 1 and Feb 16, 2027 are still in the future on Jan 20, 2027.
- **Narration:** reads naturally aloud.
- **Last line:** still exactly "That's the money. Follow for more."
- **check.py:** OK, 134 spoken words, hook 12 words.

VERDICT: PASS

## Round 2 (editor)
Reviewed fixes; evergreen wording holds on Jan 20, 2027; on-screen and spoken values agree.
VERDICT: PASS
