# Fact-check: 2026-12-27-explainer (credit vs debit fraud protection)

Checked: Wednesday, October 28, 2026. Posts: Sunday, December 27, 2026, 12 PM Central (evergreen).
Line indexes below are **0-based** (lines[0] = hook).

## Claims verified

| Line | Claim | Status |
|---|---|---|
| 0 | "Same fraud, two cards. Only one drains your checking account." | TRUE as a mechanism: debit fraud removes money from the linked checking account right away (provisional credit may come later); credit card fraud sits on the issuer's credit line. Specific, true, 10 words (well under 3 s). Fair hook. |
| 1 | Credit = bank's money, debit = yours | TRUE (simplified; "lender's money" is accurate). |
| 2 | TILA caps liability for unauthorized credit card use at $50 | TRUE: 15 U.S.C. 1643 / 12 CFR 1026.12(b) (Truth in Lending Act, as amended). |
| 3 | During a dispute, Regulation Z says you don't have to pay the charge | TRUE with nuance: 12 CFR 1026.13(d)(1) says the consumer need not pay the disputed amount (and related charges) while a billing-error claim is pending, and the issuer may not report it as delinquent (1026.13(d)(2)). Unauthorized charges count as a billing error (1026.13(a)(1)), but the 1026.13 protections need a written notice within 60 days of the statement. The $50 unauthorized-use cap (1026.12) applies separately and does not depend on that procedure. "Dispute" is acceptable shorthand; an optional tightening is given below. |
| 4 | Reg E: 10 business days to decide | TRUE: 12 CFR 1005.11(c)(1). Accounts open 30 days or less get 20 business days, which is an edge case covered by "generally". Acceptable. |
| 5 | Or provisionally credit and take up to 45 days, or 90 for some debit purchases | TRUE: 1005.11(c)(2) allows 45 calendar days if the bank provisionally credits within 10 business days. 1005.11(c)(3)(ii) extends that to 90 days for point-of-sale debit card transactions, foreign-initiated transfers and new accounts. POS debit card transactions are debit purchases, so "ninety for some debit purchases" is accurate, not overbroad. Timeline "45 d" / "90 d" match. |
| 6 | $2,500 − $2,000 = $500 | Math correct (python). Labeled "Example". OK. |
| 7 | Autopays can bounce; overdraft fees can pile up | General mechanism, hedged with "can", and not a statistic. OK. Some banks have dropped overdraft fees, and "can" covers that. |
| 8 | Card networks' zero-liability policies often cover debit too | FAIR: Visa and Mastercard Zero Liability cover branded debit cards in the U.S., with exclusions (some PIN/ATM transactions not processed on the network, commercial and unregistered prepaid cards, gross negligence, late reporting). "Often" is the right hedge. |

The only text/say differences are numerals versus spoken words (lines 2, 4, 5, 6). They match.

## Checks
- Spoken words: 138 (in the 115–138 range).
- Hook: title "Whose [money] is gone?" is 22 characters including brackets (OK), spoken 10 words, prop label "DEBIT" is 5. The value -$2,000 is paid off by the line-6 example.
- Cover: "Credit vs Debit" is 15 characters and value "-$2K" is 4, so "-$2K" is paired with "Credit vs Debit" as requested. The video pays off the cover through the $2K example.
- Compare values "Bank's"/"Yours" are 6 and 5 characters. Subs are 14 and 18. Stat label 15, value 3, sub 16. Board lines 13 and 16. List items are 12, 13 and 14. Split titles 6 and 5, items 9 to 13. Timeline "when" values are "Day 0", "10 BD", "45 d" and "90 d" (4–5 characters each, no duplicates).
- keep:true on line 5: the previous line is also a timeline. OK.
- post.title is 53 characters. The tiktok text is 145 characters (≤150).
- No product recommendation, no instruction-style takeaway, no price predictions, no politics, no time words that will be stale on the posting date.

## Optional fixes (not required for PASS)
1. **lines[3]** (billing-dispute nuance, +1 word):
   - text and say: `And in a billing dispute, Regulation Z says you don't have to pay the charge.`
   - Offset −1 word on **lines[7]**, text and say: `Rent autopays can bounce and overdraft fees can pile up.` (drop "Meanwhile,"). The total stays at 138.
2. No other changes are needed. The cover already shows "Credit vs Debit" with "-$2K".

## Sources
- 12 CFR 1005.11 (eCFR / Cornell LII); Federal Register, 63 FR 52115 (Sept 29, 1998) on the 90-day POS/foreign/new-account periods
- 12 CFR 1026.13 and the CFPB Official Interpretation (Interp-13); CFPB 2020 Reg Z error-resolution statement (1026.12 protections are separate from the 1026.13 notice rules)
- 12 CFR 1026.12(b) / 15 U.S.C. 1643 ($50 cap); FCBA secondary summaries
- Consumer Action Zero Liability FAQ; Mastercard Zero Liability pages

VERDICT: PASS

## Round 2 (editor)
Applied optional wording fixes.
VERDICT: PASS
