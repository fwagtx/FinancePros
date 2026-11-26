# Fact-check: 2027-01-25-explainer (Acorn Economics: Margin calls), posts 2027-01-25

## Verified claims
- Reg T (Federal Reserve) initial margin: firms may lend up to 50% of the purchase price. Confirmed by FINRA ("Know What Triggers a Margin Call", Margin Regulation key topic) and 12 CFR 220 (eCFR).
- FINRA Rule 4210(c) maintenance: 25% of current market value for long equity. Confirmed by FINRA Regulatory Notices 11-15 / 11-16 and FINRA investor guidance. Houses often set 30% to 40% (FINRA investor insight).
- Broker can sell without notice or a margin call: FINRA investor insight and SEC (sec.gov/answers/marsell.htm).
- Math: $5,000 + $5,000 = $10,000. Call when (V - 5,000)/V = 0.25, so V = $6,666.67, a 33.3% drop. At -50%, the stock is worth $5,000 = the loan, so equity is 0 (-100% of the cash, before interest). All correct.
- FINRA year-end debit balances (via YCharts/FINRA series plus secondary reports): Dec 2022 $606.66B (607), Dec 2023 $700.77B (701), Dec 2024 $899.17B (899), Dec 2025 $1.226T / $1,225.6B (1226; Benzinga: $1.23T). Chart points are correct, evenly spaced, and "$1.2T" is fine as a rounded figure.

## Issues found and fixes applied
1. Line 0 (hook), accuracy and prop label. "Lender wants them back" is inaccurate: a margin call asks for more cash or collateral, not repayment of the whole loan. The prop label "LOAN" was also never spoken. Fix: text "Squirrel buys stock on a loan. It drops 33%. Broker calls." / say "Squirrel buys stock on a loan. It drops thirty-three percent. Broker calls." (12 words, about 3.5s). The new hook is true for the worked example and leaves an open question (why does the broker call?), which line 1 answers with "That's a margin call." The LOAN label is now spoken.
2. Cover, accuracy. "Pay Back. Now." suggests the whole loan must be repaid. Fix: "Pay Up. Now."
3. Line 3, clarity and spoken match. "your share" is ambiguous (it can mean stock shares). The voice said "thirty" while the screen showed "30%+". Fix: text "FINRA's floor: your equity must stay at least 25%. Many brokers want 30%." / say "...at least twenty-five percent. Many brokers want thirty percent." Stat sub changed to "Many brokers: 30%".
4. Line 4, on-screen value differed from the spoken one. The board showed "$6,666.67" while the voice said "around six thousand six hundred sixty-seven dollars"; "around" next to an exact cents figure also reads oddly. Fix: board ["Call at $6,667", "= 33% drop"], text "Our math: the call hits when stock falls to $6,667, down 33%.", say "Our math: the call hits when stock falls to six thousand six hundred sixty-seven dollars, down thirty-three percent." The exact $6,666.67 / 33.3% stays in the post captions.
5. Post IG first line updated to match the new hook.

## Notes (no change needed)
- Line 1: caption "Reg T" with voice "Regulation T" is a standard abbreviation, acceptable.
- Line 7, time words. "2025" is the latest full year-end data point and is clearly dated. Monthly data later hit a record of about $1.50T in June 2026 and were about $1.45T in October 2026. FINRA posts each month's data around the third week of the next month, so the Dec 2026 figure may come out around Jan 21, 2027, just before posting. The script stays accurate as dated history. Optional: before publishing, check whether Dec 2026 is out. If it is, add a 2026 point; otherwise keep the chart as is.
- No advice, no price predictions, no political opinion. The disclaimer is present in all captions. The cover and title are paid off by the worked math. The last line is unchanged.
- Limits: check.py OK, 10 lines, 140 spoken words (at the cap), hook 12 words, JSON valid.

VERDICT: PASS

## Round 2 (editor)
Reviewed applied fixes (hook accuracy, $6,667 board, equity wording, cover); limits pass.
VERDICT: PASS
Editor: fire scene label set to STOCK (was default INDEX FUND); line 5 says 'your stock'; trimmed 'Same speed.'
