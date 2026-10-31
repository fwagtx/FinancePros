# Research brief: Dental insurance annual maximums - why dental coverage feels thin
Slot 2026-12-30-explainer (Explainer, series ticker; posts Wed Dec 30, 2026, noon Central). Researched Sat Oct 31, 2026.
Evergreen: every number carries its date/period. Year-end angle OK (posts Dec 30): many plans reset Jan 1. No promises about any specific plan.
Note: fred.stlouisfed.org and api.bls.gov blocked by the session proxy; BLS data pulled from data.bls.gov via Firecrawl (extracted Oct 31, 2026).

## Core definition
- Annual maximum: the most a dental plan will pay toward covered care in a benefit year; once reached, the patient pays the rest. (Delta Dental of Washington / Humana / Delta Dental of Kansas explainers: e.g. with a $1,500 max the plan pays its share until it has paid $1,500 total.)

## Typical maximums
- ADA News, "Dear ADA: Annual maximums" (Mary Beth Versaci, Dec 19, 2025; answer by Dr. Bert Hughes, vice chair ADA Council on Dental Benefit Programs):
  - "many still are promoting the long-standing $1,000 level that was established some 40 years ago. These limits have not kept pace with inflation or the rising costs of materials, technology and overall dental care."
  - Question text and page description: "Many dental plans' annual maximums have not increased in 50 years." Caps "often unchanged for decades."
  - "some plans now feature higher annual maximums of $2,000 or more."
  - Citing NADP: 32.8% of in-network annual maximums are $1,000-$1,500; 48.2% are $1,500-$2,500; 17.2% are $2,500 to no maximum.
  - ADA policy adopted 2024: does not support annual or lifetime maximums.
- Consumer guides (1-800-INSURANCE 2026 guide; Delta Dental examples): typical maximums ~$1,000-$2,000; $1,500 widely used as the example.
- Dentistry Today citing DentalInsurance.com (2023): average maximums about $1,700-$2,000 across states surveyed (secondary; not used on screen).
- Script uses: "$1,000 set some 40 years ago" (ADA, Dec 2025) and $1,500 as an example max (labeled example).

## The surprising fact
- ADA Health Policy Institute 2024 analysis (via ADA News Dec 19, 2025): only 3.4% of dental patients reach the typical annual maximum; another 3.3% come within $100 of common maximums like $1,000 or $1,500.
- ADA (same article): as patients approach their limit, they pay a larger share through coinsurance; "the combination of low annual maximums and major procedures covered at only 50% or less" creates a steep burden.

## Coinsurance structure
- ADA News Dec 2025: "the familiar design is 100% coverage for preventive, 80% for basic and 50% for major services"; some plans move major coverage to 20%.
- Humana "What does dental insurance cover?": most plans use the 100/80/50 model. Variations (100/70/50, 100/80/60) exist (LegalClarity).
- Examples: preventive = cleanings/exams; basic = fillings; major = crowns, bridges (Guardian example).

## Waiting periods
- Delta Dental PPO example plans: no wait for preventive, 6 months for basic, 12 months for major (via search summary of Delta Dental page).
- Guardian Life example: preventive right away, 6-month wait for basic (fillings), 12-month wait for major (crowns).
- Anthem: basic 3-6 months, major 3 months to 1 year. Some plans have no waiting periods (Guardian, Freelancers Union). Script: "some plans ... often 6 months for basic, 12 for major."

## Reset / rollover
- Delta Dental of Arkansas, "Benefit Period" (Oct 14, 2024): calendar-year benefit period runs Jan 1-Dec 31; many plans follow it, so deductible and annual maximum reset Jan 1. Some plans use an anniversary date instead.
- Unused benefits typically do not roll over unless the plan has a rollover feature (Delta Dental rollover option; Univ. of Iowa plan carryover). Script: "Many plans reset on January 1; unused benefits usually don't roll over."

## Chartable series: BLS CPI-U Dental services (CUUR0000SEMC02, 1982-84=100, NSA), December values, every 5 years
| Dec of | Index | $1,000 of Dec-1985 dental care (OUR MATH: 1000 x index / 116.8) |
|---|---|---|
| 1985 | 116.8 | $1,000 |
| 1990 | 159.9 | $1,369 |
| 1995 | 210.4 | $1,801 |
| 2000 | 262.2 | $2,245 |
| 2005 | 329.6 | $2,822 |
| 2010 | 402.386 | $3,445 |
| 2015 | 455.459 | $3,899 |
| 2020 | 514.957 | $4,409 |
| 2025 | 628.951 | $5,385 |
- Source: BLS data.bls.gov timeseries CUUR0000SEMC02 (extracted Oct 31, 2026). Oct 2025 missing due to the 2025 appropriations lapse; December values used.
- Comparison (our math): CPI-U all items Dec 1985 109.3 -> Dec 2025 324.054 = x2.965 ($1,000 -> $2,965). Dental prices rose ~5.4x vs ~3.0x overall over the same 40 years.
- Base year 1985 chosen to match ADA's "some 40 years ago" for the $1,000 level (Dec 2025 article).

## Worked example (OUR OWN MATH, labeled; example prices, not averages)
- Plan: $1,500 annual max, 50% for major work. Earlier in the year $1,000 of the max already used -> $500 left.
- Crown example price $1,400. At 50%, plan's share = 0.5 x 1,400 = $700. But only $500 of max remains -> plan pays $500.
- Patient pays 1,400 - 500 = $900 (vs $700 if the max weren't hit).
- Crown price context: published ranges vary widely (~$500-$3,000 per tooth depending on material/region); $1,400 is used purely as an example, not an average.

## Not used / weak
- "$1,000 max dates to the 1960s/70s" and "$7,500 if inflation-adjusted": repeated by dentists in Becker's Dental and blogs, no primary data -> not used. ADA's own wording ("some 40 years ago"; "not increased in 50 years") used instead, attributed.
- NADP "most common max $1,500" attribution on an HR glossary site: unverified, not used.

SOURCES:
- ADA News, "Dear ADA: Annual maximums," Dec 19, 2025: https://adanews.ada.org/ada-news/2025/december/dear-ada-annual-maximums/
- BLS CPI-U Dental services CUUR0000SEMC02: https://data.bls.gov/timeseries/CUUR0000SEMC02
- BLS CPI-U All items CUUR0000SA0: https://data.bls.gov/timeseries/CUUR0000SA0
- Humana, What does dental insurance cover?: https://www.humana.com/dental-insurance/dental-resources/what-does-dental-insurance-cover
- Humana, Dental insurance waiting period: https://www.humana.com/dental-insurance/dental-resources/dental-insurance-waiting-period
- Guardian Life, Full coverage / no waiting period: https://www.guardianlife.com/dental-insurance/full-coverage-no-waiting-period
- Anthem, Dental insurance waiting periods: https://www.anthem.com/individual-and-family/insurance-basics/dental-vision-insurance/waiting-periods
- Delta Dental of Arkansas, Benefit Period (Oct 14, 2024): https://www.deltadentalar.com/resources/blog/blog-detail/delta-dental/2024/10/14/dental-insurance-terms-explained-benefit-period
- Delta Dental of Washington, What is an annual maximum: https://www.deltadentalwa.com/dental-insurance-101/what-is-a-dental-insurance-annual-maximum
- Delta Dental of Kansas, What is an annual maximum: https://deltadentalks.com/knowledge/what-is-an-annual-maximum
- 1-800-INSURANCE, Dental insurance 2026: https://www.1800insurance.com/guides/dental-insurance-2026
- Dentistry Today (DentalInsurance.com data): https://www.dentistrytoday.com/?p=108844
