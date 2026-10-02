# Research brief: ACH vs wire vs instant transfer: speed and cost
Researched October 2, 2026. Posts November 27, 2026 (evergreen; every number dated).

## Angle / hook
Same $1,000 can move for $0 (standard ACH or standard app transfer), $17.50 (Venmo instant, 1.75%) or $30 (Bank of America outgoing domestic wire, fee schedule effective Aug 7, 2026). The difference is the payment rail, not the money.
No single-week news hook; nearest timely items: Nacha membership approved raising the Same Day ACH per-payment limit from $1M to $10M (announced April 27, 2026; effective Sept 17, 2027). FedNow Q2 2026 volume up 83.2% quarter over quarter.

## Key facts (with dates)
### ACH (Nacha)
- 2025: 35.2 billion ACH payments, up about 4.9% from 2024; value $93 trillion (+7.9%); about 141 million payments a day. (Nacha, Jan 2026 release + FY25 infographic)
- Same Day ACH 2025: 1.4 billion payments, $3.9 trillion; volume +16.7%, value +21.4%. (Nacha)
- Same Day ACH per-payment limit: $1 million (since March 2022); rising to $10 million on Sept 17, 2027 after Nacha membership approval announced April 27, 2026. (Nacha / BusinessWire Apr 2026)
- Same Day ACH has three daily settlement windows: 1:00 p.m., 5:00 p.m., 6:00 p.m. ET (submission deadlines 10:30 a.m., 2:45 p.m., 4:45 p.m. ET). Receiving bank must make same-day credits available by 5:00 p.m. local time. (Nacha Same Day ACH rules; secondary guides)
- Standard ACH credits typically settle in 1-2 business days. (Nacha rules allow next-day/1-2 day settlement; secondary sources)
- ACH runs on business days only.

### Wires (Fedwire)
- Fedwire Funds Service operates 9:00 p.m. ET prior calendar day to 7:00 p.m. ET, Monday-Friday business days, excluding holidays (as of 2026; Fed has approved future expansion). Regulation J: processed same business day received; final and irrevocable. (Federal Reserve; Federal Register 2024/2025)
- Fees (bank fee schedules, outgoing domestic):
  - Bank of America: $30, Personal Schedule of Fees effective Aug 7, 2026.
  - Chase: $25 online / $35 with a banker (Chase Additional Banking Services and Fees, 2026).
  - Wells Fargo: $30 digital / $40 branch (secondary, 2026 comparison sites).
  - NerdWallet (2026): typical outgoing domestic wire $25-$35.

### Instant rails
- RTP (The Clearing House): launched Nov 2017; 24/7/365; per-payment limit $10 million since Feb 9, 2025 (was $1M since April 2022). 2024: 343 million payments, $246 billion. Q2 2025: $481 billion. (TCH)
- FedNow (Federal Reserve): launched July 20, 2023; 24/7/365; network limit raised from $1 million to $10 million in November 2025 (banks may set lower limits). (FRB Services, Sept 5 2025 release and Nov 12 2025 notice)
  - NOTE: the assignment brief said FedNow's limit was "raised to $1M in Nov 2025"; that is wrong. Nov 2025 raised it from $1M to $10M.
- FedNow Q2 2026: 4,997,811 settled payments, $274.7 billion; volume +83.2% vs Q1 2026; average $54,957 per payment. (FRB Services quarterly stats)

### Consumer app instant fee (worked example basis)
- Venmo instant transfer to bank/debit card: 1.75% fee, minimum $0.25, maximum $25; typically within 30 minutes. Standard transfer: free, 1-3 business days. (Venmo Help Center, as of 2026)

## Chartable data series: ACH Network annual volume (billions of payments), Nacha
| Year | Payments (billions) |
|---|---|
| 2020 | 26.8 |
| 2021 | 29.1 |
| 2022 | 30.0 |
| 2023 | 31.5 |
| 2024 | 33.6 |
| 2025 | 35.2 |
Source: Nacha annual ACH Network volume releases/infographics (2020-2025).

## Worked example (exact math, hypothetical)
Cashing out $1,000 from Venmo:
- Standard: $0 fee, 1-3 business days -> $1,000 arrives.
- Instant: 1.75% x $1,000 = $17.50 -> $982.50 arrives, usually within 30 minutes.
- Cap: on $2,000, 1.75% x $2,000 = $35.00, but the cap is $25 -> fee $25 (1.25%).
Compare: a $1,000 outgoing domestic wire at Bank of America costs $30 (Aug 2026 schedule) = 3% of $1,000.

## Surprise fact
Speed and cost are not tied the way people assume: the wire, the "serious" option, is often the priciest at ~$25-35, while the newest rails (RTP, FedNow) are instant 24/7, even on weekends when ACH and Fedwire are closed.

## Weakly sourced / caveats
- Standard ACH "1-2 business days" is from secondary guides consistent with Nacha rules, not a single Nacha number.
- Wells Fargo wire fee from comparison sites only (not used in script).
- Fees at each bank vary by account tier; waivers exist.

SOURCES:
- Nacha, "Same Day ACH and Business-to-Business Payments Propel ACH Network Volume Growth in 2025": https://www.nacha.org/news/same-day-ach-and-business-business-payments-propel-ach-network-volume-growth-2025
- Nacha FY25 infographic: https://www.nacha.org/sites/default/files/2026-01/FY25_Infographic-FINAL.pdf
- Nacha ACH volume statistics: https://www.nacha.org/content/ach-network-volume-and-value-statistics
- Nacha 2020 (26.8B): https://www.nacha.org/news/podcast-record-ach-payment-growth-2020-268-billion-payments
- Nacha 2021 (29.1B): https://www.nacha.org/news/ach-network-sees-291-billion-payments-2021-led-major-gains-b2b-and-same-day-ach
- Nacha 2022 infographic: https://www.nacha.org/sites/default/files/2023-02/FY22_ACH-Network-Infographic_FINAL+.pdf
- Nacha 2023: https://www.nacha.org/news/ach-network-records-strong-growth-2023-same-day-ach-surpasses-3-billion-payments-inception
- Nacha 2024: https://www.nacha.org/news/same-day-ach-passes-major-milestone-2024-ach-network-shows-higher-growth
- Same Day ACH limit to $10M (Apr 2026): https://www.businesswire.com/news/home/20260422048226/en/Same-Day-ACH-Per-Payment-Limit-to-Increase-to-$10-Million
- Nacha Same Day ACH: https://www.nacha.org/same-day-ach ; https://www.nacha.org/rules/same-day-ach-moving-payments-faster-phase-3
- FRB Services, FedNow limit to $10M: https://www.frbservices.org/news/press-releases/090525-fednow-transaction-limit-increase ; https://www.frbservices.org/news/communications/111225-fednow-transaction-limit-increase
- FedNow volume stats: https://www.frbservices.org/resources/financial-services/fednow/volume-value-stats
- Covington, FedNow launch July 20, 2023: https://www.cov.com/en/news-and-insights/insights/2023/07/the-federal-reserves-real-time-payments-fednow-service-launches-on-july-20-2023-potential-impacts-and-considerations
- TCH RTP $10M limit: https://www.theclearinghouse.org/payment-systems/Articles/2024/12/Higher_10_Million_RTP_Network_Transaction_Limit_Empowers_New_Uses_12-04-2024 ; Payments Dive: https://www.paymentsdive.com/news/real-time-payments-network-transacion-limit-increase/734710/
- TCH RTP 2024 records: https://www.theclearinghouse.org/payment-systems/Articles/2025/01/RTP_2024_Year_Records_01-08-2025
- Federal Reserve, Fedwire Funds Service: https://www.federalreserve.gov/paymentsystems/fedfunds_about.htm ; Federal Register 2025-19942
- Bank of America Personal Schedule of Fees (eff. Aug 7, 2026): https://www.bankofamerica.com/salesservices/deposits/resources/personal-schedule-fees/
- Chase Additional Banking Services and Fees: https://www.chase.com/content/dam/chase-ux/documents/personal/checking/ABSF-en.pdf
- NerdWallet wire fees: https://www.nerdwallet.com/banking/learn/wire-transfers-what-banks-charge
- Venmo Instant Bank Transfer FAQ: https://help.venmo.com/cs/articles/instant-bank-transfer-faq-vhel302 ; Bank Transfer Timeline: https://help.venmo.com/cs/articles/bank-transfer-timeline-vhel288
