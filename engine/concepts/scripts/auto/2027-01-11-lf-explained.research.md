# Research brief: Buy now, pay later: the business model (2027-01-11-lf-explained)
Show: Explained (long-form, 16:9, 8-10 min). Posts Mon Jan 11, 2027. Researched Thu Nov 12, 2026.
Evergreen: date every figure. Direct fetches of sec.gov, federalreserve.gov, consumerfinance.gov and most other hosts were blocked
in this session; figures were confirmed from search-result excerpts of filings/official pages plus reputable coverage, one Firecrawl
read of the Congressional Research Service report (Feb 18, 2026), and two earlier in-house briefs (2026-10-03-explainer,
2026-11-13-business) that had been fact-checked. Confidence notes are given where sources are thin.

## News angle (no "this week" language in the script)
- Affirm reported fiscal Q1 2027 (quarter ended Sept 30, 2026) on Nov 5, 2026: GMV $14.4B (+34%), revenue $1.262B (+35%).
- Klarna publishes Q3 2026 results on Nov 17, 2026 (after this brief). Script uses Q2 2026 and FY2025 only, each dated.
- No timely hook needed; the evergreen hook is "zero interest, so who pays?"

## 1. What BNPL "pay in four" is
- CFPB definition (Sept 2022 report): a four-installment, no-interest loan; typically 25% down at checkout, then three more payments
  every two weeks (six weeks total).
- Longer "monthly installment" BNPL loans exist and can charge interest (Affirm: APR 0% to 36%, terms roughly 3 to 48 months; Affirm
  disclosures as reported by US News / NerdWallet / LendingTree).
- Size: CRS (Feb 2026) estimates pay-in-4 originations at about $63.3B in 2025, about 1.0% of the $6.3T in US credit card purchase volume
  (Richmond Fed/Nilson calc). Including monthly installment loans (~$40B), about $103.3B, roughly 1.6%.
- Use: 16% of US adults used BNPL in the prior 12 months in 2025, up 1 point (Fed SHED 2025, published May 2026; Fed executive summary).
  History: 10% (2021), 12% (2022), 14% (2023), 15% (2024), 16% (2025).

## 2. Who pays: the store (merchant discount fee)
- CRS (Feb 2026): "The primary source of BNPL-related revenue for many firms comes directly from merchants. Merchants pay a fee ... for
  each related transaction"; such fees "are often higher than those charged by credit cards to merchants." Other revenue: interest on
  monthly installment loans, late fees, debit-card interchange, advertising, subscriptions.
- CFPB (Sept 2022 report, via Atlanta Fed summary): average merchant discount fee 3.39% (2019), 2.91% (2020), 2.49% (2021); falling
  as competition rose.
- Ranges quoted elsewhere (less official): Consumer Reports white paper (Nov 2022): 6-7% vs 1-3% for cards; advocacy group Protect
  Borrowers (2026): up to 6% plus ~30 cents. Third-party merchant guides list Klarna US pay-in-4 at 3.29%-5.99% + $0.30 (NOT from a filing;
  not used on screen).
- Affirm FY2026 (10-K, year ended June 30, 2026): merchant network revenue $1,149.9M on GMV $50.2B = 2.29% of GMV (our math). Affirm
  says larger merchant fees are generally earned on 0% APR products (10-K description, paraphrase).
- Why merchants pay: Richmond Fed Economic Brief 25-03 (2025): BNPL fees are often higher than card fees; "the fact that merchants are
  willing to pay such fees suggests that merchants benefit from accepting BNPL" (more sales / bigger orders).

## Worked example (our math; fee assumption = CFPB's 2021 average merchant discount, 2.49%)
- $400 order, pay in four: $400 / 4 = $100. $100 at checkout, then $100 at week 2, week 4, week 6. Shopper pays $400 total, $0 interest.
- Merchant fee: $400 x 2.49% = $9.96. Store receives $400 - $9.96 = $390.04.
- After the $100 down payment, the lender is owed $300 for up to six weeks and earns $9.96: $9.96 / $300 = 3.32% for six weeks.
- Hypothetical higher fee of 6% (top of quoted ranges): $400 x 6% = $24.00.
- Late fee comparison: CFPB data (as cited by CRS, Feb 2026): 4.1% of pay-in-4 loans were assessed a late fee; average $9.70 assessed,
  $5.70 collected per late fee. So one average late fee (~$9.70) is about the same as the whole merchant fee on this order, and 9.7% of
  one $100 payment.

## 3. The interest engine (Affirm)
- Affirm FY2026 (10-K): total revenue $4,261.1M (+~32%); interest income $2,047.5M = 48.05%; merchant network revenue $1,149.9M = 26.99%;
  other (card network $294.0M, gain on sales of loans $596.6M, servicing ~$173M) = ~25%. (Line items via in-house brief + beancount.io 10-K
  breakdown; totals confirmed by Crowdfund Insider.)
- Product mix FY2026 share of GMV (10-K): interest-bearing monthly installments 70%, 0% APR monthly 14%, Pay-in-X 16%.
- GMV FY2026 $50.2B; revenue / GMV = 8.49% (our math).
- Net income FY2026 $1.93B includes ~$1.5B tax benefit; pre-tax income ~ $493M (TIKR, beancount). Not used as profit claim.
- Latest quarter: fiscal Q1 2027 (to Sept 30, 2026): revenue $1,262M (+35%); GMV $14.4B (+34%); interest income $658.1M (+44.9%,
  Zacks) = 52% of revenue (our math; moderate confidence, single source). Affirm Card GMV $3.3B (+117%), 23% of GMV. FY2027 outlook:
  GMV above $65.25B (company guidance; not used as a prediction).
- Interest example (hypothetical, inside Affirm's 0-36% APR range): $1,000 over 12 months at 15% APR: payment $90.26/month,
  total $1,083.10, interest $83.10.
- Affirm says it charges no late fees (consumer disclosures as reported by reviewers).

## Chartable data series: Affirm GMV by fiscal year (years end June 30), $ billions
| FY | GMV | Source |
|---|---|---|
| 2019 | 2.6 (2.62) | S-1 / SEC CORRESP 2020 |
| 2020 | 4.6 (4.64) | S-1 (2020) |
| 2021 | 8.3 | FY2021 10-K / Q4 FY21 release |
| 2022 | 15.5 | FY2024 10-K / filings |
| 2023 | 20.2 | FY2024 10-K |
| 2024 | 26.6 | FY2024 10-K |
| 2025 | 36.7 | FY2025 10-K |
| 2026 | 50.2 | FY2026 results (Crowdfund Insider, Pulse2) |
50.2 / 2.62 = about 19x in seven years (our math).

## 4. Klarna
- IPO: priced Sept 9, 2025 at $40 (above $35-37 range); began trading on NYSE Sept 10, 2025 as KLAR; ~34.3M shares, ~$1.37B raised
  (Klarna itself got ~$222M); valuation ~$15.1B at IPO price. Closed day one at $45.82. Peak private valuation $45.6B (2021), $6.7B in 2022.
  (American Banker, IPO Scoop, The Star/Reuters, Crunchbase.)
- FY2025 (year to Dec 31, 2025; results Feb 26, 2026): revenue $3.51B (+25%); GMV $127.9B (+22%); 118M active consumers; net loss $273M;
  Q4 2025 first $1B+ revenue quarter. Revenue mix: transaction & service ~$2.5B = 71%; interest income $937M = 27% (moderate confidence).
- Q2 2026 (results Aug 2026): revenue $1.042B (+27%); GMV $36.6B (+18%). (FashionUnited, RTTNews.)
- Late fees (provider terms as reported by review sites, 2026): Klarna up to $7 per missed payment; Afterpay up to $8, both capped at 25%
  of order. Moderate confidence; used only in the brief, not on screen.
- Klarna is Swedish (Stockholm). No country scene (Sweden not in cast).

## 5. Risks and credit reporting
- Fed SHED 2025 (May 2026): 26% of BNPL users paid late at least once in 2025 (24% in 2024, 18% in 2023); 11% had a BNPL payment trigger an
  overdraft/NSF fee. (26% via secondary summaries of the Fed report; earlier in-house brief confirmed it from Fed page excerpts.)
- LendingTree survey (2,060 US consumers, March 17-23, 2026): 47% of BNPL users paid late in the past year (41% in 2025, 34% in 2024);
  most late payers were no more than about a week late.
- Credit reporting: CRS (Feb 2026): reporting to major bureaus is inconsistent; most providers (with the exception of Affirm) do not
  consistently furnish pay-in-4 data. FICO announced FICO Score 10 BNPL and 10 T BNPL on June 23, 2025 (FICO release, Business Wire),
  the first scores from a leading provider to include BNPL data; offered alongside existing scores; adoption by lenders unconfirmed.
- "Phantom debt": because many loans are not reported, other lenders may not see them (critics; Fed researchers' "blind spot").

## 6. Rules (neutral)
- May 2024: CFPB interpretive rule treated pay-in-4 lenders as card issuers under Regulation Z (Truth in Lending) subpart B: dispute rights,
  refunds, periodic statements. Effective July 30, 2024 (in-house knowledge; CRS confirms May 2024 issuance).
- Challenged in court by the Financial Technology Association (D.D.C.).
- May 12, 2025: CFPB withdrew it (90 Fed. Reg. 20084) along with other guidance; June 2025 status report: CFPB does not intend to reissue it
  (said changes should go through notice-and-comment); lawsuit dismissed. No federal reversal found as of Nov 2026.
- States: New York enacted a Buy Now Pay Later Act (2025) requiring licensing; NYDFS proposed implementing rules.

## The surprising fact
- The store usually pays for your "interest-free" loan (about $10 on a $400 order at the CFPB 2021 average fee), and the best-known US
  BNPL lender, Affirm, earned about 48% of its FY2026 revenue from interest, because 70% of its volume was interest-bearing loans.

## Chapter plan
1. What pay in four is (definition, size, who uses it)
2. The store pays (merchant fee, $400 example, why merchants accept)
3. The interest engine (Affirm mix, GMV chart, $1,000 example)
4. Late fees and Klarna (late fee data, Klarna IPO and results, revenue mix compare)
5. The risks (SHED, LendingTree, credit reporting, FICO)
6. The rules (CFPB 2024 rule, 2025 withdrawal, states), then recap

SOURCES:
- Congressional Research Service, R48858, "Buy Now, Pay Later: Policy Issues and Options for Congress," Feb 18, 2026: https://www.everycrsreport.com/files/2026-02-18_R48858_ff6a61f61022347480affb93afe0f3c6ca2be927.html
- CFPB, "Buy Now, Pay Later: Market Trends and Consumer Impacts," Sept 2022: https://files.consumerfinance.gov/f/documents/cfpb_buy-now-pay-later-market-trends-consumer-impacts_report_2022-09.pdf ; Atlanta Fed summary (merchant discount 3.39%/2.91%/2.49%): https://www.atlantafed.org/blogs/take-on-payments/2022/10/03/cfpb-releases-report-on-buy-now-pay-later
- CFPB, BNPL market data spotlight, Dec 2025: https://files.consumerfinance.gov/f/documents/cfpb_bnpl-market-report_2025-12.pdf
- CFPB withdrawal, 90 Federal Register 20084, May 12, 2025; Consumer Finance Monitor, "CFPB will not issue revised BNPL rule," June 20, 2025: https://www.consumerfinancemonitor.com/2025/06/20/cfpb-will-not-issue-revised-bnpl-rule/ ; Cooley, May 15, 2025: https://www.cooley.com/news/insight/2025/2025-05-15-cfpb-withdraws-guidance-documents-in-shift-from-nonbinding-policymaking
- Federal Reserve, Economic Well-Being of U.S. Households in 2025 (May 2026): https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-credit.htm ; executive summary https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-executive-summary.htm
- Richmond Fed Economic Brief 25-03 (2025): https://www.richmondfed.org/publications/research/economic_brief/2025/eb_25-03 ; EB 26-05 (Feb 2026): https://www.richmondfed.org/publications/research/economic_brief/2026/eb_26-05
- LendingTree BNPL statistics (March 2026 survey): https://www.lendingtree.com/personal/buy-now-pay-later-loan-statistics/
- FICO press release, June 23, 2025: https://www.businesswire.com/news/home/20250623623014/en/FICO-Unveils-Groundbreaking-Credit-Scores-That-Incorporate-Buy-Now-Pay-Later-Data
- Affirm Form 10-K FY2026: https://www.sec.gov/Archives/edgar/data/0001820953/000162828026059279/afrm-20260630.htm ; Crowdfund Insider (Aug 2026): https://www.crowdfundinsider.com/2026/08/302674-bnpl-fintech-affirm-beats-revenue-estimates-and-lifts-outlook-as-afrm-stock-surge-in-after-hours/ ; beancount.io 10-K breakdown: https://beancount.io/blog/2026/09/13/affirm-fy2026-q4-earnings-analysis ; TIKR: https://www.tikr.com/blog/affirms-1-9-billion-profit-has-a-1-5-billion-asterisk
- Affirm fiscal Q1 2027 (Nov 5, 2026): https://www.panabee.com/news/affirm-earnings-q1-2027 ; https://finviz.com/news/418183/affirm-beats-on-34-gmv-growth-and-a-43-take-rate-but-credit-upticks-and-a-light-gaap-margin-guide-muddy-the-story ; Zacks coverage (interest income $658.1M)
- Affirm GMV history: S-1 (2020) https://www.sec.gov/Archives/edgar/data/1820953/000110465920126927/tm2026663-4_s1.htm ; FY2021 results https://www.businesswire.com/news/home/20210909006033/en ; FY2024 10-K https://www.sec.gov/Archives/edgar/data/1820953/000182095324000035/afrm-20240630.htm ; FY2025 10-K https://www.sec.gov/Archives/edgar/data/1820953/000182095325000080/afrm-20250630.htm
- Klarna IPO: American Banker https://www.americanbanker.com/payments/news/klarna-debuts-on-the-new-york-stock-exchange ; IPO Scoop https://www.iposcoop.com/?p=36260 ; The Star (Sept 12, 2025) https://www.thestar.com.my/business/business-news/2025/09/12/klarna-valued-at-nearly-us20bil-as-shares-jump-in-nyse-debut
- Klarna FY2025 results (Feb 26, 2026): https://www.businesswire.com/news/home/20260226134670/en/Klarna-Group-plc-Publishes-Full-Year-2025-Results
- Klarna Q2 2026: https://fashionunited.com/news/business/klarna-achieves-18-percent-gmv-and-27-percent-revenue-growth-in-q2/2026081974145 ; https://www.rttnews.com/3681540/klarna-swings-to-q2-profit-revenue-rises-27-lowers-full-year-outlook-stock-down.aspx
- Consumer Reports BNPL white paper (Nov 2022): https://advocacy.consumerreports.org/wp-content/uploads/2022/11/FINAL-Buy-Now-Pay-Later_-Consumer-Protections-Needed-for-the-Popular-New-Way-To-Pay-White-Paper.pdf
