# Research brief: Diversification, why squirrel never hides all acorns in one tree (posts Oct 14, 2026)

Note: the Oct 17, 2026 explainer covers stocks vs bonds (2008/2022). This episode stays on single-company concentration vs owning many companies, to avoid overlap.

## Definition
- Diversification: spreading money across many investments (many companies, sectors, asset types) so a loss in any one has a limited effect on the whole. It reduces company-specific risk; it does NOT prevent losses when the whole market falls (SEC Investor.gov "Diversification" / "Asset allocation" guidance).

## The surprising fact (latest data: Bessembinder, "One Hundred Years in the U.S. Stock Markets", SSRN, March 2026)
- Sample: 29,754 US common stocks, 1926-2025.
- Median lifetime buy-and-hold return: -6.9% (the typical stock lost money). Mean: over 30,000%.
- Only 48.22% of stocks had a positive lifetime buy-and-hold return (so about 52% lost money outright).
- Only 41.17% beat one-month Treasury bills over the months they were listed; investors in nearly 60% of stocks saw wealth reductions.
- Net wealth creation over the century: about $91 trillion. Just 46 firms account for half of it.
- Concentration rising: in the 1926-2016 study, about 89-90 firms accounted for half; now 46.
- Value-weighted portfolio of all US common stocks: $1 (1926) -> $15,401 (end 2025). $1 in Treasury bills -> $25.34.
- Sources agree: SSRN abstract (6438198); CNBC, May 8, 2026 ("46 firms accounted for half the wealth..."); Evidence Investor; Hedge Fund Alpha (2026 MIC); Mauboussin quoting the abstract ("$91 trillion... nearly 60% of stocks").
- Earlier version (2018, 1926-2016, 25,967 stocks): 4.3% of stocks (1,092) accounted for all net wealth creation vs T-bills; 57.4% had lifetime returns below T-bills (Journal of Financial Economics / SSRN 2900447).

## One-tree case study: Enron (historical)
- As of Dec 31, 2000, 62% of the assets in Enron's 401(k) plan were Enron stock (Congressional Research Service, "The Enron Bankruptcy and Employer Stock in Retirement Plans"; Senate Governmental Affairs testimony, Prof. Susan Stabile, Feb 5, 2002). About 89% of that stock was bought by employees; the rest was company match.
- Share price: high of $90.75 on Aug 23, 2000 -> $0.26 close on Nov 30, 2001 (KHOU "From $90 to 26 cents", Wikipedia Enron scandal). Bankruptcy filed Dec 2, 2001.
- Drop: 1 - 0.26/90.75 = 99.71%.
- Employees were blocked from selling Enron shares in the 401(k) during a late Oct-Nov 2001 plan administrator change (lockdown) (EPI; Senate hearings).

## Chartable data series (Enron share price, key closes)
| Date | Price | Source |
|---|---|---|
| Dec 31, 1999 | $44.38 (44 3/8) | Enron 1999 Annual Report |
| Aug 23, 2000 | $90.75 (all-time high) | Wikipedia / KHOU |
| Dec 29, 2000 | $83.13 | Enron 2000 Annual Report |
| Jan 26, 2001 | $82.56 | Shortform / CNN timeline |
| Nov 30, 2001 | $0.26 | KHOU / Wikipedia |
(Irregular dates, so the script uses a money from->to scene instead of a chart.)

## Worked example (hypothetical; assumes the other 9 stocks don't move)
- $1,000 all in one stock that falls like Enron ($90.75 -> $0.26):
  1000 / 90.75 = 11.0193 shares x $0.26 = $2.87.
- $1,000 split equally across 10 stocks ($100 each); one falls the same way, other nine flat:
  9 x $100 = $900 + ($100 / 90.75 x 0.26 = $0.29) = $900.29.
- Loss: $997.13 vs $99.71.

## Caveat (keep in script)
- Owning many stocks doesn't avoid market-wide drops; it limits damage from any single company.

SOURCES:
- Hendrik Bessembinder, "One Hundred Years in the U.S. Stock Markets," SSRN abstract 6438198 (March 2026): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6438198
- CNBC, May 8, 2026: https://www.cnbc.com/2026/05/08/what-investors-can-learn-from-100-years-of-stock-market-returns.html
- Evidence Investor, "100 years, 29,000 stocks, 46 winners": https://www.evidenceinvestor.com/post/the-case-for-indexing-just-got-stronger
- Hedge Fund Alpha, 2026 MIC Bessembinder: https://hedgefundalpha.com/conferences/2026-mic-bessembinder-100-year-stocks-dont-beat-cash/
- Bessembinder, "Do Stocks Outperform Treasury Bills?" (2018), SSRN 2900447
- CRS, "The Enron Bankruptcy and Employer Stock in Retirement Plans": https://www.policyarchive.org/download/3557
- Senate Governmental Affairs hearing, Feb 5, 2002 (Stabile testimony): https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/stabile.pdf
- KHOU, "From $90 to 26 cents: Enron's stock value tanked before bankruptcy": https://www.khou.com/article/news/local/20-years-ago-today-enron-filed-bankruptcy/285-1d164a35-8e2f-4cb5-8cb6-f0e2f9235031
- Wikipedia, Enron scandal (price high $90.75, $0.26 on Nov 30, 2001)
- Enron Annual Reports 1999 and 2000 (year-end closes)
- SEC Investor.gov, diversification / asset allocation
