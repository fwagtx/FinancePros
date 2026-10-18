# Research brief: Does paying rent build credit? How rent reporting works
Slot: 2026-12-17-explainer (posts Thu Dec 17, 2026). Researched Oct 18, 2026. Evergreen phrasing: every figure carries its year/date.

## Core idea
Paying rent on time does not automatically build credit. Rent shows up on a credit report only if someone furnishes it to a bureau (landlord/property manager, or a third-party rent reporting service, often paid), and then it only matters for score models that use it.

## Facts (with dates and sources)
1. Not reported by default. No federal law requires landlords to report rent to credit bureaus; many don't, and historically landlords mostly reported only negatives (collections). (Experian "Is my rental history on my credit report?"; Privacy Rights Clearinghouse; WA Senate bill report 2024; VantageScore)
2. Share of renters with rent reported: TransUnion's 4th annual Rent Payment Reporting analysis (released Sept 10, 2025): share of consumers whose rent payments are reported to credit bureaus rose to 13% in 2025, from 11% in 2024 (survey-based). VantageScore separately estimates about 13% of renters benefit from positive rent reporting. Fannie Mae said in 2021 that fewer than 5% of renters had rent reported. (TransUnion release via Seeking Alpha/GlobeNewswire, HousingWire, PYMNTS; VantageScore; Mortgage News Daily Aug 2021)
3. CHARTABLE SERIES - Property managers (aware of the practice) who report rent payments, TransUnion annual surveys:
   - 2022: 27% (as stated in coverage of TransUnion's 2025 report; 2023 release implies ~26%)
   - 2023: 36% (TransUnion release, June 8, 2023: +37% vs 2022)
   - 2024: 48% (TransUnion release, Oct 17, 2024: +33% vs 2023)
   - 2025: 44% (TransUnion release, Sept 10, 2025: first decline in four years)
   TransUnion suggests renters are increasingly self-reporting via third-party data furnishers. No 2026 edition found as of Oct 18, 2026.
4. How rent gets on a file: landlord/property manager furnishes via a vendor (e.g., TransUnion TruVision Resident Credit, Experian RentBureau), or renter enrolls in a third-party service. Some are paid: e.g., RentReporters $94.95 sign-up + $9.95/month (reports to Equifax and TransUnion); RentRedi $3.99-$5.99/month; PaymentReport $49 per lease (per Bankrate/aggregator summaries - verify on provider sites; weak). Experian Boost is free and adds eligible rent to the Experian file only (Experian 2022 release).
5. California AB 2747 (Civil Code 1954.07): since April 1, 2025, landlords of buildings with 16+ units (and some corporate-owned smaller ones) must offer tenants the option of positive rent reporting to at least one bureau; landlords may charge the lesser of actual cost or $10 per month; offer repeated annually. (California Apartment Association, AAGLA summaries)
6. Which scores count rent:
   - FICO 9 (introduced 2015): counts rent payments when they're reported to bureaus. (Experian "What is FICO Score 9"; Credit Karma; FICO/HUD/PERC study)
   - FICO 8: rent has no impact (Experian FICO 8 vs 9 table). Exception: Experian Boost data, which Experian says can raise FICO Score 8 (Experian 2022 release; 62% of Boost users saw an increase, avg 13 pts - Experian's own figure).
   - FICO 8 is "the most widely used" base FICO version by lenders (myFICO "FICO Score versions").
   - VantageScore 4.0: uses reported rent payments (VantageScore; Experian mortgage page). FICO 10T also uses rent/alternative data (secondary sources). VantageScore 3.0 rent treatment: only a HUD research study used it with rent data - NOT independently confirmed from VantageScore docs; not used in script.
   - Classic FICO (versions 2, 4, 5), long used for mortgages, generally does not count rent (secondary sources: CapCenter, MoneyTalksNews).
7. Mortgages / FHFA / GSEs:
   - Fannie Mae Desktop Underwriter has, since Sept 18, 2021, used positive rent payment history found in bank-statement (VOA) data for first-time buyers who opt in; Fannie estimated 17% of first-time-buyer applicants who did not get Approve/Eligible could have with rent history. (Fannie Mae newsroom Aug 2021; Mortgage News Daily)
   - Fannie Mae multifamily Positive Rent Payment pilot (launched Sept 2022): as of Sept 2023, 435,000+ units enrolled; ~58% of participants saw score increases. Program status: Fannie page says ended June 30, 2025 (FHFA filing had said extended through year-end 2025) - status conflicting, not used in script.
   - July 2025: FHFA Director Bill Pulte announced lenders may use VantageScore 4.0 for loans sold to Fannie Mae and Freddie Mac, keeping tri-merge; lenders pick Classic FICO or VantageScore 4.0. (HousingWire; Brownstein; FHFA)
   - May 1, 2026: limited pilot (about 50 lenders); VantageScore 4.0 used on more than 9% of mortgages Fannie and Freddie securitized May 1-Aug 31, 2026.
   - Sept 9, 2026: Fannie Mae Lender Letter LL-2026-06 and Freddie Mac Bulletin 2026-H opened VantageScore 4.0 to all approved lenders (directive announced Sept 3; LL updated Sept 30, 2026). Manually underwritten loans still Classic FICO only. FICO 10T not yet eligible for delivery. (Fannie Mae LL-2026-06; HousingWire; The Mortgage Reports)

## Worked example (exact math)
California cap example (hypothetical renter at the max allowed fee): $10/month x 12 months = $120 a year for positive rent reporting. RentReporters example (aggregator pricing): $94.95 + 12 x $9.95 = $94.95 + $119.40 = $214.35 first year.

## Surprising fact
Even when rent IS reported, FICO 8 - the FICO version lenders use most - doesn't count it (Experian Boost aside). Only about 13% of renters had rent reported in 2025 (TransUnion).

## Weakly sourced / caution
- 2022 = 27% property-manager figure comes from secondary summaries of TransUnion's 2025 report.
- Third-party service prices are from aggregators; change often.
- VantageScore 3.0 rent treatment not confirmed; Classic FICO rent claim is secondary.
- CFPB: no consumer page retrieved; CFPB's Jan 2025 rental payment data report (CCIP) confirms rental payment data are sold by consumer reporting companies, ~240,000 consumers in its sample.

SOURCES:
- TransUnion Rent Payment Reporting analysis, Sept 10, 2025 (GlobeNewswire/Seeking Alpha): https://seekingalpha.com/pr/20227654-transunion-report-finds-more-consumers-likely-self-reporting-rent-payments-in-2025
- HousingWire, consumers increasingly self-reporting rent: https://www.housingwire.com/articles/consumers-are-increasingly-self-reporting-rent-payments-transunion-says/
- The Mortgage Point summary: https://themortgagepoint.com/?p=18001
- TransUnion June 8, 2023 release: https://www.crowdfundinsider.com/2023/06/208540-transunion-report-37-increase-in-number-of-property-managers-reporting-rent-payments-in-past-year/
- TransUnion Oct 17, 2024 release: https://www.tipranks.com/news/press-releases/transunion-report-finds-33-increase-in-number-of-property-managers-reporting-rent-payments-since-last-year
- Experian, What is FICO Score 9: https://www.experian.com/blogs/ask-experian/what-is-fico-score-9/
- Experian, rental history on credit report: https://www.experian.com/blogs/ask-experian/do-apartments-report-your-monthly-payments-to-credit-bureaus/
- Experian Boost rent release (2022): https://www.experianplc.com/media/latest-news/2022/experian-helps-consumers-use-positive-rent-payments-to-build-credit/
- myFICO, FICO Score versions: https://myfico.com/legal/fico-score-versions
- VantageScore on rent and VantageScore 4.0: https://vantagescore.com/resources/knowledge-center/press-releases/new-analysis-finds-millions-of-renters-become-mortgage-eligible-when-on-time-rent-payments-are-included-in-vantagescore-4-0-credit-score
- Experian VantageScore 4.0 mortgage: https://www.experian.com/mortgage/vantagescore-4
- Fannie Mae newsroom, DU rent payment history (2021): https://www.fanniemae.com/newsroom/fannie-mae-news/fannie-mae-introduces-new-underwriting-innovation-help-more-renters-become-homeowners
- Mortgage News Daily, Aug 12, 2021: https://www.mortgagenewsdaily.com/news/08122021-loan-underwriting
- Fannie Mae Lender Letter LL-2026-06: https://singlefamily.fanniemae.com/media/document/pdf/lender-letter-ll-2026-06-vantagescore-40-broad-lender-availability
- HousingWire, GSEs broaden VantageScore 4.0 access: https://www.housingwire.com/articles/gses-broaden-vantagescore-4-0-access-rocket-uwm-dominate-volume/
- The Mortgage Reports: https://themortgagereports.com/134153/vantagescore-fannie-freddie-all-lenders
- Brownstein, FHFA reverses course on bi-merge (July 2025): https://www.bhfs.com/insight/fhfa-reverses-course-on-bi-merge-opens-door-to-vantagescore-4-0/
- Fannie Mae multifamily Positive Rent Payment impact: https://multifamily.fanniemae.com/positive-rent-payment-impact
- California Apartment Association, AB 2747: https://caanet.org/april-1-is-fast-approaching-get-ready-for-new-rent-reporting-and-security-deposit-photo-requirements/
- AAGLA FAQ AB 2747: https://members.aagla.org/news/faqs-on-assembly-bill-2747--positive-rent-reporting
- Bankrate, how to report rent: https://www.bankrate.com/personal-finance/credit/how-to-report-rent-payments-to-credit-bureaus
- CFPB rental payment data report (Jan 2025): https://files.consumerfinance.gov/f/documents/cfpb-report-rental-housing-data_2025-01.pdf
- Kansas City Fed Economic Review 2026, Building Credit with Rent Data: https://www.kansascityfed.org/research/economic-review/building-credit-with-rent-data-the-potential-effects-of-rent-reporting-on-the-credit-scores-of-us-renters/
