# Research brief: How a tariff works - the acorn toll at the forest border
Slot 2026-12-29-explainer (Acorn Economics, posts Tue Dec 29, 2026, noon Central). Researched Fri Oct 30, 2026.
Evergreen: every number carries its year/period. No current tariff RATES are used (they changed repeatedly in 2025-26 and may change again before Dec 29).
Note: api.fiscaldata.treasury.gov, fred.stlouisfed.org and factually.co could not be fetched from this session (proxy/DNS block); figures confirmed via search results quoting official sources.

## Mechanics (who pays, legally)
- A tariff (customs duty) is a tax on imported goods, usually a percentage of the goods' customs value (ad valorem). Duty is calculated from value + tariff classification. (CBP "Entry Summary" page; 19 U.S.C. 1505)
- The IMPORTER OF RECORD (the US company bringing goods in) is legally liable and pays U.S. Customs and Border Protection (CBP). A customs broker may advance it, but the importer remains responsible. The foreign exporter/country does not pay CBP.
- Timing: entry summary filed and estimated duties deposited within 10 working days of release/entry (19 CFR 142.12; CBP entry summary page; statute 19 U.S.C. 1505 allows up to 12 working days; periodic monthly statement option exists). Script uses only "the importer pays US Customs" (no deadline, to stay safe).
- Then the importer decides how much to pass on: raise prices (shoppers pay), absorb it (thinner margins), or push suppliers to cut their price (foreign exporter bears part). Who ends up bearing it = "incidence", measured as "pass-through."

## Research on who bears it
- Amiti, Redding & Weinstein, "The Impact of the 2018 Tariffs on Prices and Welfare," Journal of Economic Perspectives 33(4), Fall 2019, pp. 187-210: full incidence of the 2018 tariffs fell on US consumers and importers (near-complete pass-through to tariff-inclusive import prices); ~$1.4B/month real income loss by end of 2018.
- Fajgelbaum, Goldberg, Kennedy & Khandelwal, "The Return to Protectionism," QJE 135(1), 2020: complete pass-through of 2018 tariffs to duty-inclusive import prices; ex-tariff prices of targeted imports did not fall.
- Cavallo, Gopinath, Neiman & Tang, "Tariff Passthrough at the Border and at the Store," AER: Insights 3(1), March 2021 (NBER w26396, 2019): tariffs on Chinese imports almost fully passed through to prices US importers paid; but at the store, retail price effects were much smaller -> retail margins fell (retailers absorbed part). Sector caveat: steel exporters cut prices.
- NY Fed Liberty Street Economics, "Who Is Paying for the 2025 U.S. Tariffs?" (Amiti, Flanagan, Heise, Weinstein), Feb 12, 2026: using import data through Nov 2025, nearly 90% of the tariffs' economic burden fell on US firms and consumers; Nov 2025 monthly estimate 86% pass-through; pass-through declined late in 2025. Average US tariff rate on imports rose from 2.6% to 13% over 2025 (per the post).
- Fajgelbaum & Khandelwal, Brookings Papers draft, March 2026: 2025 tariff pass-through to tariff-inclusive prices high but not complete (~80-90%+; secondary sources say ~90%). Not used on screen.

## Chartable series: US customs duties by fiscal year (Treasury)
| Fiscal year | Customs duties | Source |
|---|---|---|
| FY2022 | $99.9B | Reuters (record before FY2025); Treasury Combined Statement FY2023 implies $99.9B ($80.3B was -$19.6B) |
| FY2023 | $80.3B | Treasury Combined Statement FY2023 (receipts) |
| FY2024 | $77.0B | Treasury MTS, cited by USAFacts and others |
| FY2025 | $194.9B | USAFacts citing Treasury MTS |
- FY2026 (ended Sept 30, 2026): net customs is distorted by IEEPA refunds (~$134B of refunds booked May-Sept 2026 per secondary analysis; a tracker says ~$173B net) - NOT used; secondary and definition-dependent.
- Calendar-year alternative (BEA via FRED B235RC1A027NBEA, as of Feb 2026): 2017 38.5, 2018 53.3, 2019 77.8, 2020 68.6, 2021 89.1, 2022 102.3, 2023 81.6, 2024 83.6, 2025 265.1 ($B). Not used (calendar vs fiscal confusion).

## Worked example (OUR OWN MATH, labeled)
- Squirrel imports acorns with customs value $100. Tariff 10% (example rate, not a current rate).
- Duty = $100 x 10% = $10, paid by the importing squirrel to customs at the border. Landed cost = $110.
- Choice: charge shoppers $110 (shoppers bear it), keep price at $100 (squirrel's margin drops by $10), or split it (e.g. $105 price: shoppers $5, squirrel $5).

## Current legal status (context only; do NOT state amounts on screen)
- Feb 20, 2026: Supreme Court held 6-3 that IEEPA does not authorize tariffs; Section 232, Section 301, AD/CVD and normal tariffs remain.
- Refunds go to importers of record via CBP's CAPE process (Phase 3 launched Oct 6, 2026); amounts still changing. Section 122 temporary surcharge (Feb 24, 2026) reportedly expired July 24, 2026 and new Section 301 duties followed (single source). Status is fluid -> script avoids all of this. Our Oct 8 short already covered "$166B refunds."
- Overlap: avoid economies of scale (Dec 18 "Why the biggest squirrel pays 90% less per acorn").

## Surprising fact
The toll is legally paid by a US importer, not the foreign country, and research on 2018 and 2025 tariffs found ~90-100% of it shows up in what US buyers pay at the border; but stores often absorbed part at the shelf (Cavallo et al. 2021).

SOURCES:
- https://www.cbp.gov/trade/programs-administration/entry-summary
- https://www.law.cornell.edu/uscode/text/19/1505
- https://www.aeaweb.org/doi/10.1257/jep.33.4.187 (Amiti, Redding, Weinstein 2019)
- https://www.voxchina.org/show-3-194.html ; https://nber.org/papers/w26396 (Cavallo et al.)
- https://libertystreeteconomics.newyorkfed.org/2026/02/who-is-paying-for-the-2025-u-s-tariffs/
- https://www.brookings.edu/wp-content/uploads/2026/03/1_Fajgelbaum-Khandelwal_unembargoed.pdf
- https://fiscal.treasury.gov/files/reports-statements/combined-statement/cs2023/receipt.pdf
- https://usafacts.org/answers/how-much-revenue-does-the-federal-government-collect-from-tariffs/country/united-states/
- https://www.worldports.org/?p=597326 (Reuters: FY2022 record $99.9B)
- https://fred.stlouisfed.org/series/B235RC1A027NBEA
- https://www.millernash.com/firm-news/news/tariffs-in-flux-ieepa-and-section-122-struck-down-section-232-duties-expand
- https://www.cbh.com/insights/alerts/ieepa-tariff-refund-update-cape-phase-iii-set-for-october-6/
