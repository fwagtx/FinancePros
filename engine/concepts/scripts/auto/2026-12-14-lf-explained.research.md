# Research brief: How mortgages work: every number explained (2026-12-14-lf-explained)
Researched Thu Oct 15, 2026. Posts Mon Dec 14, 2026 (evergreen). Every number carries its date. Education only; no rate predictions.
Not repeating as main angle: Nov 29 "5% vs 20% down on $429,100 home"; Nov 16 Fed explainer.

## Key facts (dated, sourced)
1. **Freddie Mac PMMS, Oct 8, 2026:** 30-year fixed averaged **7.40%** (prior week Oct 1: 7.28%; year earlier ~6.30%). 15-year fixed **6.73%** (prior week 6.60%). Highest since November 2023. (Freddie Mac release "Mortgage Rates Average 7.40%", GlobeNewswire Oct 8, 2026; wrenews, Bridgepoint, Nadlan coverage.) The Oct 15 release was not yet indexed at research time. PMMS = conventional, conforming, fully amortizing purchase loans, 20% down, excellent credit (Freddie Mac).
   - Earlier 2026 readings: Feb 26 5.98% (first below 6% in ~3.5 years); Sep 24 7.03%; Oct 1 7.28%.
2. **Record extremes (PMMS since April 1971):** high **18.63%** week of Oct 9, 1981 (Marketplace / FRED; Freddie Mac); record low **2.65%** on Jan 7, 2021 (Freddie Mac).
3. **NAR median existing-home price, September 2026: $417,500**, up 1.3% from a year earlier; 39th straight month of annual gains; highest on record for a September. Sales 3.99M SAAR (+1.5% m/m). (NAR release Oct 13, 2026 via GlobeNewswire; Inman, HousingWire, RealEstateNews Oct 13, 2026.) August 2026 was first reported at $429,100.
4. **FHFA 2026 conforming loan limit: $832,750** (one-unit, most of US), up $26,250 from 2025; high-cost ceiling $1,249,125. Set yearly from FHFA house price index (+3.26%). (FHFA release Nov 25, 2025; Scotsman Guide; Consumer Finance Monitor.) Note: FHFA normally announces the 2027 limit in late November 2026, before posting; say "the 2026 limit" and that it is reset every year.
5. **Interest rate vs APR (CFPB):** interest rate = yearly cost of borrowing, no fees. APR = interest rate plus points, broker fees and other charges, as a yearly rate; usually higher than the rate. CFPB warns comparing fixed vs ARM APRs is tricky. (CFPB Ask CFPB "What is the difference between a mortgage interest rate and an APR?")
6. **Points (CFPB):** one point = 1% of the loan amount (on $100,000, $1,000). Points lower the rate in exchange for paying more at closing; lender credits do the reverse. How much a point lowers the rate varies by lender. (CFPB "What are discount points and lender credits")
7. **Property taxes (ATTOM 2025 property tax analysis, Apr 9, 2026):** average single-family effective tax rate **0.9%** in 2025 (0.86% in 2024); average bill **$4,427** on average value $494,231. Highest: Illinois 1.84%, New Jersey 1.58%.
8. **Homeowners insurance (Bankrate, 2026):** national average **$2,424 a year** for $300,000 dwelling coverage; other trackers $2,090-$2,870. Varies hugely by state (~$1,000 to $6,000+).
9. **PMI and the Homeowners Protection Act of 1998 (CFPB, Federal Reserve, FDIC exam manual):** borrower may REQUEST cancellation when balance reaches **80%** of original value (scheduled or actual; good payment history needed); servicer must cancel AUTOMATICALLY when balance is scheduled to reach **78%** of original value (if current). Final termination at the loan's midpoint (month after payment 180 on a 30-year). HPA does not cover FHA, VA or USDA insurance. Freddie Mac: PMI typically $30-$70 a month per $100,000 borrowed.
10. **Escrow (RESPA, Regulation X 12 CFR 1024.17):** servicer collects 1/12 of yearly taxes and insurance each month plus a cushion of no more than **1/6 of the yearly total (about two months)**; must do an annual escrow analysis and statement.
11. **Closing costs:** typically **2% to 5% of the purchase price** (Freddie Mac, widely cited; Freddie page not directly fetched). **Loan Estimate** within 3 business days of application; **Closing Disclosure** at least 3 business days before closing (CFPB TRID).
12. **ARMs:** modern conforming ARMs like the 5/6 are fixed for 5 years, then adjust every 6 months; index usually 30-day average SOFR plus a margin (~2.25%-3%); common caps 2/1/5 (first adjustment max 2 points, later adjustments 1 point, lifetime 5 points above start). Still 30-year term. (Lender program disclosures: Towne Mortgage 5/6 SOFR 2/1/5; NewRez bulletin; Enact.)
13. **DTI:** monthly debt payments / gross monthly income. Fannie Mae Selling Guide B3-6-02: manual underwriting max 36% (up to 45% with credit score/reserves); Desktop Underwriter up to 50%. (Fannie Mae Selling Guide / Eligibility Matrix Apr 2026, via homebuyer.com mirror and Lower.)

## Chartable data series: Freddie Mac PMMS 30-year fixed, annual average (%)
| Year | Avg |
|---|---|
| 2016 | 3.65 (lowest annual average on record at the time; Freddie Mac Dec 29, 2016 release) |
| 2017 | 3.99 |
| 2018 | 4.54 |
| 2019 | 3.94 |
| 2020 | 3.11 |
| 2021 | 2.96 |
| 2022 | 5.34 |
| 2023 | 6.81 |
| 2024 | 6.72 |
| 2025 | 6.60 (about; Freddie Mac cited year-to-date average 6.62% on Dec 11, 2025; last weeks ~6.15-6.21% -> ~6.59-6.60) |
Source: Freddie Mac PMMS annual averages (freddiemac.com/pmms; FRED MORTGAGE30US). 2019-2024 values used in earlier fact-checked briefs. 2017/2018 from Freddie Mac annual table (not re-confirmed by search this time; 2018 4.54% cited by HousingWire Sept 2019). Note: Freddie Mac changed PMMS methodology Nov 17, 2022.
2026 weekly backup: Feb 26 5.98, Sep 24 7.03, Oct 1 7.28, Oct 8 7.40.

## Worked example (hypothetical, exact math)
Assumptions: $500,000 home, 20% down ($100,000), **$400,000 loan**, 30-year fixed at **7.40%** (Freddie Mac average, Oct 8, 2026). Monthly payments; principal & interest first.
Formula: M = L x r / (1 - (1 + r)^-n), r = 0.074 / 12 = 0.0061667, n = 360.
- (1 + r)^360 = 9.1... -> **M = $2,769.52**
- **Payment 1:** interest = $400,000 x 0.074 / 12 = **$2,466.67** (89.1% of the payment); principal = $2,769.52 - $2,466.67 = **$302.85**. New balance $399,697.15.
- Year 1 totals: interest $29,474.18, principal $3,760.06.
- Principal first exceeds interest at **payment 249** (year 21): interest $1,378.37, principal $1,391.15.
- After 10 years (120 payments): paid $332,342.40; balance still **$346,410.76** -> only $53,589.24 of principal repaid; interest $278,753.16.
- Balances: yr5 $378,091.86; yr10 $346,410.76; yr15 $300,596.96; yr20 $234,346.03; yr25 $138,541.21; yr30 $0.
- **Total paid over 30 years: $997,026.91; total interest $597,026.91** (more than the $400,000 borrowed).
- **15-year at 6.73%** (Freddie Mac 15-year avg, Oct 8, 2026): M = **$3,535.20**; total interest **$236,336.71**. Costs $765.68 more a month; saves **$360,690.20** in interest.
- **APR example:** same loan with $8,000 of lender fees/points financed into the cost -> APR ~ **7.61%** (solve rate where $2,769.52 x 360 has PV $392,000: 7.606%).
- **Points example (assumption: 1 point cuts the rate 0.25 pt, varies by lender):** 1 point = $4,000; 7.15% -> $2,701.63/mo; saves $67.89/mo; break-even ~59 months (~5 years).
- **PITI example:** taxes 0.9% x $500,000 = $4,500/yr = **$375/mo** (ATTOM 2025 avg rate); insurance $2,424/yr = **$202/mo** (Bankrate 2026 avg); P&I $2,769.52 -> **PITI $3,346.52/mo** (no PMI at 20% down).
- **PMI example:** same $500,000 home, 10% down, $450,000 loan at 7.40% -> P&I $3,115.71. 80% of original value = $400,000, reached on schedule at **payment 105** (8 years 9 months); 78% = $390,000 at **payment 120** (10 years). Extra principal payments can get to 80% sooner (request); 78% automatic is based on the original schedule. PMI at Freddie's $30-$70 per $100K = $135-$315/mo.
- **DTI example:** gross income $12,000/mo ($144,000/yr). Housing $3,346.52 -> 27.9%. Plus $800 of other debts -> $4,146.52 -> 34.6%.
- **Closing costs example:** 2%-5% of $500,000 = $10,000-$25,000.
- **ARM caps example (hypothetical):** 5/6 ARM starting at 6%, caps 2/1/5 -> max 8% at first adjustment, then up to 1 point per 6 months, never above 11%.

## The surprise
On the example loan, 89% of the first payment is interest ($2,466.67 of $2,769.52), principal doesn't win until year 21, and after 10 years of payments ($332,342) the balance has fallen only $53,589.

## Chapters
1. The parts of a mortgage: principal, rate, term, APR, points.
2. Amortization: the payment, the split, the crossover, total interest; 15 vs 30.
3. Where the rate comes from: PMMS chart 2016-2025, 7.40% Oct 8, 2026, records, conforming limit $832,750, credit matters.
4. PITI: taxes, insurance, PMI and the 78/80 rule, escrow.
5. Getting the loan: closing costs, Loan Estimate/Closing Disclosure, fixed vs ARM, DTI.
6. Recap.

## Weakly sourced / notes
- 2017 (3.99%) and 2018 (4.54%) annual averages and 2025 (~6.60%) not directly confirmed in a primary page this session (fetch blocked); 2025 derived from Freddie's 6.62% YTD on Dec 11, 2025.
- Closing costs 2-5% attributed to Freddie Mac by many sites; original not fetched.
- Fannie DTI 50% DU cap via secondary mirrors of Selling Guide B3-6-02.
- Points rate reduction (0.25 per point) is an assumption, labeled as such.
- Insurance averages differ by source; Bankrate $2,424 used and named.
- PMMS will have newer weekly values by Dec 14, 2026; script dates the 7.40% to Oct 8, 2026.

SOURCES:
- Freddie Mac PMMS release "Mortgage Rates Average 7.40%", Oct 8, 2026: https://www.globenewswire.com/news-release/2026/10/08/3377537/0/en/mortgage-rates-average-7-40.html ; https://wrenews.com/freddie-mac-mortgage-rates-7-40-october-8-2026/
- Freddie Mac PMMS, Oct 1, 2026 (7.28%): https://www.foxbusiness.com/economy/mortgage-rates-10-1-2026
- Freddie Mac PMMS annual averages / FRED MORTGAGE30US: https://www.freddiemac.com/pmms ; https://fred.stlouisfed.org/series/MORTGAGE30US
- Freddie Mac year-end 2025 releases ("Mortgage Rates Remain Near 2025 Lows", Dec 11, 2025; Dec 31, 2025 6.15%): https://freddiemac.gcs-web.com/news-releases/news-release-details/rates-remain-near-2025-lows
- Marketplace, "When mortgages hit the roof" (18.63%, Oct 1981): https://www.marketplace.org/2018/10/12/highest-mortgage-rate
- NAR, "Existing-Home Sales Increased 1.5% in September", Oct 13, 2026: https://www.globenewswire.com/news-release/2026/10/13/3379853/0/en/existing-home-sales-increased-1-5-in-september-according-to-nar-report.html ; https://www.inman.com/2026/10/13/existing-home-sales-september-2026/
- FHFA, "FHFA Announces Conforming Loan Limit Values for 2026" (Nov 25, 2025): https://www.fhfa.gov/news/news-release/fhfa-announces-conforming-loan-limit-values-for-2026
- CFPB, interest rate vs APR: https://www.consumerfinance.gov/ask-cfpb/what-is-the-difference-between-a-mortgage-interest-rate-and-an-apr-en-135/
- CFPB, discount points and lender credits: https://www.consumerfinance.gov/ask-cfpb/what-are-discount-points-en-136/
- CFPB, When can I remove PMI: https://www.consumerfinance.gov/ask-cfpb/when-can-i-remove-private-mortgage-insurance-pmi-from-my-loan-en-202/ ; FDIC Compliance Manual V-5 HPA: https://www.fdic.gov/consumer-compliance-examination-manual/v-5-homeowners-protection-act
- Regulation X 12 CFR 1024.17 (escrow): https://www.consumerfinance.gov/rules-policy/regulations/1024/17/
- CFPB Know Before You Owe (Loan Estimate / Closing Disclosure): https://www.consumerfinance.gov/about-us/blog/know-before-you-owe-closing-disclosure/
- ATTOM 2025 property tax analysis (Apr 9, 2026): https://www.attomdata.com/news/market-trends/home-sales-prices/2025-annual-tax-report
- Bankrate homeowners insurance cost (2026): https://www.bankrate.com/insurance/homeowners-insurance/homeowners-insurance-cost/
- Fannie Mae Selling Guide B3-6-02 DTI: https://homebuyer.com/guidelines/fannie-mae/debt-to-income-ratios-b3-6-02
- 5/6 SOFR ARM 2/1/5 caps disclosure: https://tpo.townemortgage.com/pdf/5_6_SOFR_ARM_Program_Disclosure_(2_1_5_CAPS).pdf
- Freddie Mac My Home, PMI cost: https://myhome.freddiemac.com/buying/breaking-down-pmi
- Payment math: standard amortization formula, own calculation (Python, cent-rounded schedule).
