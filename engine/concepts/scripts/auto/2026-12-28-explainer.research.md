# Research brief: Penalty APR - how one late payment can raise your rate
Slot 2026-12-28-explainer (posts Mon Dec 28, 2026, evergreen). Researched Oct 29, 2026. Note: direct fetch of consumerfinance.gov, ecfr.gov, law.cornell.edu and issuer sites is blocked in this session; rules below are confirmed via search results quoting the regulation, CFPB materials, issuer pricing tables and law-firm/credit-union summaries (cross-checked).

## No news hook
Evergreen. No timely event used. (Background only: CFPB $8 late-fee rule vacated April 15, 2025.)

## Core rules (CARD Act 2009, 15 U.S.C. 1666i-1; Regulation Z 12 CFR 1026.55, 1026.9(g), 1026.59)
- Penalty APR = a higher interest rate an issuer may apply after a late payment (missed minimum by due date) or a returned payment. Triggers listed in e.g. Chase cardmember agreement rate table ("fail to make a Minimum Payment by the date and time that it is due; or make a payment to us that is returned unpaid").
- New transactions: issuer may raise the rate on NEW transactions after a late payment, but must give 45 days' advance written notice (12 CFR 1026.9(g)); the higher rate can apply to transactions made more than 14 days after the notice is provided (1026.55(b)(3)).
- Existing balance: the penalty rate can reach the balance you already owe only if the required minimum payment is more than 60 days late (1026.55(b)(4)), still with the 45-day notice.
- Cure: when the 60-day exception is used, the issuer must reduce the rate back for those balances if it receives six consecutive required minimum periodic payments on or before the due date, starting with the first payment due after the increase takes effect (1026.55(b)(4)(ii); 15 U.S.C. 1666i-1). The notice must say so.
- Review: under 1026.59, issuers that raise a rate must review the account at least once every six months and reduce the rate if factors warrant. (New purchases made after the increase may stay at the penalty rate after cure - issuer dependent.)
- Some issuers reverse sooner as policy; some cards have no penalty APR at all (e.g. LendingTree listings show Capital One Platinum / Venture Rewards Penalty APR "None"; NerdWallet: Wells Fargo Active Cash had none as of Sept 2025).

## Typical penalty APR levels (attributed)
- Chase pricing pages (2026; Prime 6.75% as of 3/24/2026 and 5/5/2026): Penalty APR "Up to 29.99%" = Prime + up to 26.99%, max 29.99%. One Chase version: Penalty APR "could potentially remain in effect indefinitely" (for new transactions).
- Citi pricing tables: penalty APR up to 29.99% (variable with Prime). Late fee up to $41 (some versions $39). Dates not confirmed.
- Amex Gold terms (search snippet): penalty APR 29.99%, at least six months. Weakly sourced (search summary).
- NerdWallet: penalty APR on many cards is 29.99%. Note: there is NO general federal 29.99% legal cap (one secondary site claims so - wrong; do not use).

## Late fees
- CFPB's 2024 rule ($8 safe harbor for issuers with 1M+ accounts) was blocked by injunction May 2024 and VACATED April 15, 2025 by Judge Mark Pittman, U.S. District Court for the Northern District of Texas, on a joint consent-judgment motion by CFPB and plaintiffs (Orrick InfoBytes, Holland & Knight, Goodwin, ICBA, Kilpatrick). No reversal found as of Oct 2026.
- Prior Reg Z safe harbor applies again: base $30 first late / $41 repeat within the next six billing cycles (credit union summary), inflation-indexed; current 2026 CPI-adjusted figures NOT confirmed - do not put on screen.
- Issuer examples: Chase "Up to $40" late fee (2026 pages); Amex Gold agreement July 2024: $29 first, $40 if again within next 6 billing periods.

## Chartable data series (real)
Fed G.19 / FRED TERMCBCCINTNS - commercial bank interest rate on credit card plans, accounts assessed interest:
- Aug 2024: 23.37% (series high); Aug 2025: 22.83%; Feb 2026: 21.52%; May 2026: 22.15%; Aug 2026: 22.36% (third-party tracker citing G.19; verify). Not used in script (overlaps Oct 9 Fed episode).

## Worked example (OUR OWN MATH; hypothetical)
Assumptions: $6,000 balance held flat, regular APR 21%, penalty APR 29.99%, simple monthly interest = balance x APR / 12, no new purchases, no compounding.
- Regular: 6,000 x 0.21 / 12 = $105.00 per month
- Penalty: 6,000 x 0.2999 / 12 = $149.95 per month
- Difference: 149.95 - 105.00 = $44.95 per month
- Six months (minimum time before the six-payment cure can kick in): 44.95 x 6 = $269.70
(This applies to the existing balance only if the payment was more than 60 days late.)

## Surprising fact
A payment that's a little late can't raise the rate on what you already owe - that takes more than 60 days late. And the law makes the issuer drop the rate on that balance after six on-time minimum payments in a row.

## Overlap check
Avoid: Fed/rate-votes (Oct 9), paying off debt (Oct 7), carrying a balance (Oct 6). This episode focuses only on the penalty trigger rules, the cost math and the cure.

SOURCES:
- 12 CFR 1026.55 (b)(3), (b)(4); 1026.9(g); 1026.59 (Regulation Z) via govinfo/eCFR summaries and NAFCU compliance blog (nafcu.org/node/23685)
- 15 U.S.C. 1666i-1 (Credit CARD Act of 2009)
- Chase pricing and terms pages, e.g. https://www.chase.com/content/dam/pricingandterms/LGC64842.html (2026)
- Citi pricing tables, e.g. https://www.citi.com/CRD/PDF/CMA/pricingTables/PIT_PID410.pdf
- NerdWallet, Credit Card Penalty APR: https://www.nerdwallet.com/article/credit-cards/penalty-apr-what-it-is-how-to-avoid-it
- Orrick InfoBytes, Apr 25, 2025: https://infobytes.orrick.com/2025-04-25/cfpb-gets-its-credit-card-late-fee-rule-tossed/
- Holland & Knight, Apr 2025: https://www.hklaw.com/en/insights/publications/2025/04/cfpb-credit-card-late-fees-rule-vacated-by-texas-district-court
- Kilpatrick Townsend, May 2025; Goodwin, May 2025; ICBA
- American Express Gold Card Cardmember Agreement (July 25, 2024)
- FRED TERMCBCCINTNS (Federal Reserve G.19)
