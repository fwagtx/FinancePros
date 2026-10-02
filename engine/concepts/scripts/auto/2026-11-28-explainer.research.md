# Research brief: Tipflation, why every screen asks for a tip (posts Sat Nov 28, 2026)

Evergreen angle (no single news peg this week): the tip prompt moved from the restaurant table to every counter because point-of-sale tablets ship with preset tip buttons. Surprise: on a small sale, the "dollar" buttons can be a huge percentage, and quick-service tip rates on Toast have actually drifted DOWN even as prompts spread.

## Key facts (with dates)
1. Pew Research Center (survey Aug 7-27, 2023, 11,945 US adults; published Nov 9, 2023):
   - 72% say tipping is expected in more places than five years ago.
   - Only about a third say it is extremely/very easy to know whether (34%) or how much (33%) to tip.
   - 40% oppose vs 24% favor businesses suggesting tip amounts (on the bill or a checkout screen).
   - 72% oppose automatic service charges/tips added to bills.
   - Only 12% always tip at fast-casual restaurants with no servers.
2. Square's tip screen (Square Help Center "Set up and customize tipping" + Square API docs; confirmed via two search sources): with "Smart tip amounts," a sale under $10 shows No Tip, $1, $2, $3; a sale of $10 or more shows No Tip, 15%, 20%, 25%. Default percentages are 15/20/25; merchants can customize. (Mechanism: the prompt is a software setting chosen by the merchant, not a legal requirement.)
3. Toast platform data (aggregated card/digital tips; ~171,000 locations as of Mar 31, 2026): average quick-service (QSR) tip 15.8% in Q1 2026, flat at 15.8% for six straight quarters (Q4 2024-Q1 2026). Full-service 19.3% in Q1 2026 (seven-year low of 19.1% in Q2 2025). Q2 2026 data not found in search as of Oct 2, 2026.
4. Bankrate annual Tipping Survey (released June 4, 2025; latest found, no 2026 edition located): 63% hold at least one negative view of tipping (59% a year earlier); 41% say tipping culture is out of control; 38% annoyed by pre-entered tip screens; 27% tip less or not at all when shown a pre-entered tip screen vs 11% who tip more; 18% always tip coffee shop baristas; 70% always tip sit-down servers.
5. Federal tipped minimum wage (FLSA, US Dept of Labor): employers may pay a cash wage as low as $2.13/hour and take a tip credit up to $5.12/hour, as long as tips bring pay to at least the $7.25 federal minimum; employer must make up any shortfall. Many states set higher floors.
6. "No tax on tips" (One Big Beautiful Bill Act, signed July 2025; IRS): federal income-tax deduction of up to $25,000 of qualified tips per year, tax years 2025-2028, for occupations that customarily and regularly receive tips; phases out above $150,000 MAGI (single) / $300,000 (joint). Tips are still reported as income; payroll (Social Security/Medicare) taxes still apply; states may still tax tips.

## Chartable series: Toast quick-service average tip %, Q1 of each year
| Quarter | QSR avg tip |
|---|---|
| Q1 2021 | 16.9% |
| Q1 2022 | 17.0% |
| Q1 2023 | 16.0% |
| Q1 2024 | 16.0% |
| Q1 2025 | 15.8% |
| Q1 2026 | 15.8% |
Other confirmed quarters: Q2 2022 16.9%; Q2 2023 16.1%; Q3 2023 16.1%; Q4 2023 16.0%; Q2 2024 15.9%; Q3 2024 15.9%; Q4 2024 15.8%.
Source: Toast Restaurant Trends reports (Q1 2022 report; Q4 2023/2024 reports; "Average Tip Percentage in America [2026 Toast Platform Data]").

## Worked example (Square smart-tip buttons on a $6 coffee)
- $1 / $6 = 0.1667 = 16.7%
- $2 / $6 = 0.3333 = 33.3%
- $3 / $6 = 0.50 = 50%
Compare percentage buttons on the same $6: 15% = $0.90, 20% = $1.20, 25% = $1.50.
(Labeled example: a $6 sale under Square's Smart tip amounts setting.)

## Surprise fact
The $3 button on a $6 coffee is a 50% tip. And despite prompts everywhere, Toast's average quick-service tip fell from 17.0% (Q1 2022) to 15.8% (Q1 2026).

SOURCES:
- Pew Research Center, "Tipping Culture in America: Public Sees a Changed Landscape," Nov 9, 2023: https://www.pewresearch.org/2023/11/09/tipping-culture-in-america-public-sees-a-changed-landscape/ (report PDF: https://www.pewresearch.org/wp-content/uploads/2023/11/SR_23.11.09_tipping-culture_report.pdf); Axios, Nov 9, 2023: https://www.axios.com/2023/11/09/tip-added-automatic-gratuity-charged
- Square Help Center, "Set up and customize tipping": https://squareup.com/help/us/en/article/8631-set-up-and-customize-tipping ; Square API TipSettings/CheckoutLocationSettingsTipping reference: https://developer.squareup.com/reference/square/objects/TipSettings
- Toast, "Average Tip Percentage in America [2026 Toast Platform Data]": https://pos.toasttab.com/blog/on-the-line/what-is-the-average-tip-percentage ; Toast "Restaurant Tipping Trends": https://pos.toasttab.com/blog/data/restaurant-tipping-trends ; Toast Q1 2022 trends report: https://pos.toasttab.com/news/toast-restaurant-q1-trends-report-dine-in-growth-surges-while-takeout-and-delivery-decline ; Fast Company 2026: https://www.fastcompany.com/91562922/how-much-tip-restaurants-fast-food-takeout-2026-toast-report
- Bankrate press release, June 4, 2025: https://www.bankrate.com/press-releases/63-of-americans-have-a-negative-view-about-tipping-with-41-saying-tipping-culture-has-gotten-out-of-control/ ; The Hill: https://thehill.com/business/5332326-bankrate-survey-attitude-tipping-culture/
- US Dept of Labor / FLSA tipped employees ($2.13 cash wage, $5.12 tip credit): https://www.dol.gov/agencies/whd/minimum-wage/tipped (confirmed via multiple payroll sources)
- IRS, "What the No Tax on Tips deduction means for you": https://www.irs.gov/newsroom/what-the-no-tax-on-tips-deduction-means-for-you ; Kiplinger; Fidelity
