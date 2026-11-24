# Fact-check: 2027-01-23-explainer (secured credit cards)
Checked 2026-11-24 for posting Sat Jan 23, 2027, 12:00 CT. Evergreen.

## Claims verified
- **CFPB: 7 million (2.7%) US adults had no credit record, December 2020.** Confirmed. The CFPB's "Technical Correction and Update to the CFPB's Credit Invisibles Estimate" (June 2025) gives 2.7 percent (7.0 million consumers) in December 2020. "No credit record" is the CFPB's own wording. It is attributed to the CFPB and dated on screen ("CFPB, Dec 2020"), so it is not stale news.
  - https://www.consumerfinance.gov/data-research/research-reports/technical-correction-and-update-to-the-cfpbs-credit-invisibles-estimate/
  - https://files.consumerfinance.gov/f/documents/cfpb_update-credit-invisibles-estimate_2025-06.pdf
  - https://www.acainternational.org/news/cfpb-revises-its-estimate-of-credit-invisibles/
- **The deposit usually equals the credit limit.** Confirmed as "usually". The Federal Reserve FEDS Note "An Overview of Credit-Building Products" (Dec 6, 2024) describes secured cards as requiring a cash deposit that usually matches the limit. Some issuers set a limit above the deposit.
  - https://www.federalreserve.gov/econres/notes/feds-notes/an-overview-of-credit-building-products-20241206.html
- **Payment history is 35% of a FICO Score.** Confirmed by myFICO. Amounts owed is 30%, which supports "amounts owed count toward your score". myFICO says these percentages are general approximations.
  - https://www.myfico.com/credit-education/whatsinyourscore.aspx
- **Utilization math.** $90 / $300 = 30% and $30 / $300 = 10%. Both are correct. The script frames this as "lower is generally better", not as a 10% rule.
- **FICO minimum scoring criteria.** Confirmed. FICO requires at least one account open six months or more and at least one account reported to the bureau in the past six months. A single account can meet both conditions.
  - https://www.myfico.com/credit-education/faq/scores/fico-score-requirements
  - https://marketplace.fico.com/blogs/fico-fact-does-ficos-minimum-scoring-criteria-limit-consumers-access-credit
- **The deposit is refunded on closing or upgrading in good standing.** True generally, but issuer terms and timing vary.
  - https://www.bankrate.com/credit-cards/building-credit/secured-card-deposit-refund
  - https://www.experian.com/blogs/ask-experian/how-to-upgrade-secured-credit-card-to-unsecured-card/
- **Not all secured cards report to all 3 bureaus, so check before applying.** Supported by credit bureau and issuer education pages. This is framed as something to check, not as product advice.
  - https://www.transunion.com/blog/credit-advice/what-is-a-secured-credit-card
  - https://www.experian.com/blogs/ask-experian/what-is-a-secured-credit-card/
  - https://www.chase.com/personal/credit-cards/education/build-credit/how-to-establish-credit-with-secured-credit-card

## Issues found (all fixed)
1. **Line 0, hook.** The hook was weak and slightly untrue. "How does $300 of your own cash build credit?" implies the cash itself builds credit; on-time payments that get reported do. It was also a generic question.
   - Text is now: "No credit? Your own $300 can become your limit."
   - Spoken is now: "No credit? Your own three hundred dollars can become your limit." (10 words; the checker counts 11)
   - Why it is stronger: it is true, specific, and short enough to say in under 3 seconds. It leaves an open question (how?) that line 2 answers. The cover, "Cash Into Credit", still pays off.
2. **Line 2, board.** The board read "deposit = limit", which is absolute. The spoken line says "usually".
   - Board is now: ["Deposit usually", "= your limit"].
   - The sentence was also tightened to: "With a secured card, the deposit usually becomes your limit."
3. **Line 3.** "It's reported like any card" was stated as universal, which contradicts line 8 ("Not all do").
   - Now: "It's often reported like any card, and payment history is 35% of FICO scores."
4. **Line 4, narration.** "and thirty is ten percent" was ambiguous when read aloud.
   - Spoken is now: "...and thirty dollars is ten percent." The on-screen text is unchanged.
5. **Line 5.** "Lower is generally better" did not say what should be lower.
   - Now: "Lower utilization is generally better, since amounts owed count toward FICO scores."
6. **Line 6.** "open at least 6 months, reported in the last 6" was imprecise. It read as if both conditions had to apply to one account, and the second "6" had no unit.
   - Now: "FICO needs an account open six months or more, and one reported in the last six."
   - Text and speech now match, with the number written as words.
7. **Line 7.** "In good standing, you get the deposit back" was absolute and gave no trigger for the refund.
   - Now: "Some issuers let you graduate. Close or upgrade in good standing, and the deposit's generally refunded."
8. **Line 8.** Shortened for the word budget.
   - Now: "Before applying, check it reports to all 3 bureaus. Not all do." Spoken with "three".
9. **Post captions (ig, yt_desc).** Updated to match the script:
   - "many issuers report" instead of "the issuer reports"
   - the precise FICO minimum criteria (at least one account each)
   - "lower utilization is generally better"
   - the refund caveat (issuer terms vary)
   - "Dec 2024" added to the yt_desc sources

## Other checks
- **Time words.** None will be wrong on Jan 23, 2027. Every date is explicit (Dec 2020, June 2025, Dec 2024).
- **Advice, predictions and politics.** No investment advice, price predictions or political opinion. No issuers are named.
- **On-screen vs spoken values.** All values match: 7 million, 35%, $300, $90 = 30%, $30 = 10%, 6 months, 3 bureaus.
- **Length.** 137 spoken words (target 115-140). check.py returns OK.
- **Closing line.** The last line is still exactly "That's the money. Follow for more."

VERDICT: PASS

## Round 2 (editor)
Reviewed fixes; hedged wording (usually/often/generally) where terms vary; on-screen and spoken values agree.
VERDICT: PASS
