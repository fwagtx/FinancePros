# Fact-check: 2027-01-11-lf-explained (Buy now, pay later: the business model)
Checked 2026-11-12 for posting Mon Jan 11, 2027. Sources: web search excerpts, plus two Firecrawl reads (Fed SHED 2025 Credit page, CRS R48858). Direct fetches of sec.gov, federalreserve.gov, everycrsreport.com and investors.affirm.com were blocked.

## Verified (OK)
- Fed SHED 2025 (Credit page, read directly): 16% of adults used BNPL; 10% in 2021; 26% of users paid late ("slightly more than one-fourth"); 11% had an overdraft/NSF fee. 2022 = 12%, 2023 = 14% (2023 SHED); 2024 = 15%; 2023 paid-late = 18% (American Banker on the Fed data). Lines 5, 6, 73, 74, 75: OK.
- CFPB Sept 2022 report (Atlanta Fed summary): merchant discount fee 3.39% (2019), 2.91% (2020), 2.49% (2021). Lines 22, 23: OK.
- Affirm FY2026 (to June 30, 2026): revenue $4.26B, GMV $50.2B (Business Wire / Crowdfund Insider); interest income ~$2,047M (48.1%), merchant network ~$1,150M (27.0%) (beancount 10-K breakdown). Lines 3, 34, 35, 36, 38-41: OK.
- Affirm fiscal Q1 2027 (to Sept 30, 2026): GMV $14.4B (+34%), revenue ~$1.26B (+35%), interest income ~$658.1M (= 52%). Lines 53, 54: OK.
- Affirm GMV FY2019-2025 (2.6, 4.6, 8.3, 15.5, 20.2, 26.6, 36.7) match Affirm filings as known; FY2026 50.2 confirmed. 19x by our math (50.2/2.62 = 19.2). Lines 49-52: OK.
- Affirm APR 0-36%: OK (multiple reviewers). "Affirm says it doesn't charge [late fees]": OK as attributed (Affirm's marketing; most reviewers agree).
- CFPB Dec 2025 report: 4.1% of BNPL loans assessed a late fee in 2023. Line 58: OK.
- Klarna: IPO priced $40 (above $35-37 range), NYSE trading Sept 10, 2025, ~$15.1B; $45.6B (2021), $6.7B (2022). FY2025 GMV $127.9B, revenue $3.5B, net loss $273M; interest income $937M (~27%), transaction & service ~$2.5B (~71%). Q2 2026 revenue $1.042B (+27%). Lines 62-70: OK.
- CRS R48858 (Feb 18, 2026, read directly): $63.3B pay-in-4 in 2025; furnishing "inconsistent"; "only one major firm universally furnishes Pay in 4 data" (firm not named in excerpt). Richmond Fed EB 26-05: card purchase volume likely exceeded $6.3T in 2025. Lines 16, 17, 80: OK.
- Richmond Fed EB 25-03 quote verified verbatim. Lines 31, 32: OK.
- CFPB interpretive rule May 2024 (89 FR 47068); withdrawn May 2025 (90 FR 20084) with other guidance; June 2025 status report: will not reissue, procedurally defective / should go through rulemaking. Lines 84-88: OK.
- FICO Score 10 BNPL / 10 T BNPL announced June 23, 2025. Line 82: OK. New York BNPL Act (2025) requires licensing. Line 89: OK.
- LendingTree (fielded March 17-23, 2026): 47% paid late in past year; ~72% of late payers no more than about a week late. Line 76: OK.
- Our math recomputed: $400 x 2.49% = $9.96; $390.04; $9.96/$300 = 3.32%; $400 x 6% = $24.00; $1,150M/$50.2B = 2.29%; $1,000 at 15% APR, 12 mo: $90.26/mo, interest $83.10 (exact amortization). OK.
- Neutrality: no buy/avoid advice; rule debate presented both sides. OK.

## Fixes (applied to raw.json)
- Line 0 (hook): "Pay later is zero interest." is untrue for monthly BNPL loans (0-36% APR). FIX -> text/say: "Pay in four is zero interest. So who's paying for it?" (11 words). Same fix in post.tiktok; post.title -> "Pay in four is 0% interest. So how do Affirm and Klarna make billions?"
- Line 2: "the biggest US name" not confirmable (Klarna's volume is larger globally). FIX -> "And for one of the biggest US names in this business, store fees aren't even the main money."
- Lines 14/15: "3 months to about 4 years" / sub "3-48 months" is wrong; Affirm terms run up to 60 months. FIX line 14 -> "There's a second kind, too: longer monthly loans that can stretch for months or even years."; scene right.sub -> "Up to 5 years" (lines 14 and 15).
- Line 24: Consumer Reports "6 to 7% vs 1 to 3%" could not be found in the CR white paper. FIX -> text: "Other estimates run higher. A 2026 report from the advocacy group Protect Borrowers says many lenders charge stores up to 6%, plus about 30 cents." (say spelled out); scene -> stat "BNPL store fee" / "Up to 6%" / "Advocacy est. 2026". yt_desc source "Consumer Reports (Nov 2022)" replaced with "Protect Borrowers BNPL report (2026); Affirm/Experian credit reporting release (March 2025)".
- Lines 43/44: exact FY2026 mix 70/14/16 not confirmable; an Affirm investor deck shows 71/13/16 as illustrative (FQ3'26). FIX line 43 -> "In fiscal 2026, about 70% of Affirm's volume was interest-bearing monthly loans." (value "~70%"); line 44 -> "The rest, about 30%, was zero-percent monthly plans and classic pay in four, which Affirm calls Pay in X." scene -> stat "0% plans" / "~30%" / "0% mo. + Pay in X".
- Line 59: "$9.70 charged / $5.70 collected" not found; secondary summaries of the CFPB Dec 2025 report give an average late fee of $9.99 in 2023. FIX -> "The lenders in that data charged about $136 million in late fees that year, but collected only about $80 million." (American Banker on CFPB data); scene compare "Late fees, 2023": Charged $136M / Collected $80M, sub "CFPB data".
- Line 60: late fee value $9.70 -> "about $10". FIX text: "Notice something? One average late fee, about $10, is about the same as the whole store fee on our $400 order."; scene left.value "~$10".
- Line 77: "the share has climbed for years" conflicts with the Fed (2025 late share "essentially unchanged from the prior year"). FIX -> "Most of those were no more than about a week late. But in both surveys, the share is up from two years earlier." (Fed 18%->26%, LendingTree 34%->47%); board ["Most: ~1 week late", "up over 2 years"].
- Line 81: CRS does not name Affirm in the verified text. FIX -> "The report says only one major firm reports all of them. Affirm says it now reports all its loans to Experian." (Affirm/Experian release, March 2025, loans from April 1, 2025); board ["Affirm: reports", "to Experian"].
- Line 93: "$9.70" -> FIX "Pipe three: late fees, where lenders charge them, about $10 on average in the CFPB's 2023 data."

check.py: OK: 98 lines, 1800 spoken words (~600s at 180 wpm).

VERDICT: FIX

## Round 2 (editor)
- Checker applied all fixes; check.py OK (1800 words).
VERDICT: PASS
