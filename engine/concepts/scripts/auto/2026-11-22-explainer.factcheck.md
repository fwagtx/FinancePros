# Fact-check: 2026-11-22-explainer (posts Nov 22, 2026; checked Oct 2, 2026)

## Verified
- **Loan math (recomputed in Python, standard amortization, monthly rate = APR/12):** $35,000 at 7%: 60 mo = $693.04/mo, interest $6,582.52 (rounds to $6,583); 84 mo = $528.24/mo, interest $9,372.48 (rounds to $9,372). Payment drop $164.80 (so "about $165" is right). Extra interest $2,789.96, so $2,790 is right. $1,500 at 7% over 84 mo = $22.64/mo ($1,901.68 repaid in total). All worked numbers are correct.
- **7% APR is realistic:** Edmunds says the average new-vehicle APR "held steady at 7%" in Q3 2026 (release dated Oct 1, 2026).
- **FTC "payment packing":** The FTC really uses this term. Its 2024 complaint against three Asbury/McDavid dealerships in Texas alleged add-ons were charged without consent (Asbury disputes this). The script names no company, so nothing needs to be framed as an allegation.
- **Total of payments:** Regulation Z 12 CFR 1026.18(h) requires closed-end credit disclosures to list the "total of payments." The claim is correct.
- **Edmunds history (from the Q1 2025 release):** Q1 2019 13.4%, Q1 2024 15.8%, Q1 2025 19.8% (that release's wording was "84-month loans"). The Q1 2026 release gives 22.9% for 84+ months, a record at the time.
- No advice, no price predictions, no political opinion. "In 2026" is still true on Nov 22, 2026. The cover and title ("Lower Payment, $2,790 More?") are paid off. All compare values are 7 characters or fewer. There are no keep:true flags.

## Issues (line numbers count `lines` from 1)

### 1. STALE NEWS and mixed data series, line 7 (must fix)
Edmunds put out Q3 2026 data on Oct 1, 2026. Loans of 84 months or more were a **record 25.5%** of financed new-vehicle purchases, up from 23.9% in Q2 2026 and 21.8% in Q3 2025. The video leads with the older Q1 figure (22.9%), even though the IG caption and YT description already cite 25.5%.

The chart also mixes two series. Edmunds' Q1 2026 release gives **21.2%** for Q1 2025 (84 months or longer), but the chart uses **19.8%** from the 2025 release ("84-month loans"). The same kind of revision shows up for Q3 2024: the original release said 18.1%, and a later snippet says 18.5%. Points from different releases and definitions should not sit on one line.

Replace line 7 with:
- text: `Long loans are spreading: 84-month-plus loans hit a record 25.5% of new-car financing in Q3 2026, up from 21.8% a year earlier (Edmunds).`
- say: `Long loans are spreading. Per Edmunds, a record twenty-five and a half percent of new-car loans ran eighty-four months or more in the third quarter.`
- scene: `{"t": "chart", "title": "84+ month loans (Q3)", "points": [[2025, 21.8], [2026, 25.5]], "suffix": "%", "end": "25.5%", "color": "up", "mood": "worried"}`
  - If a two-point chart looks too thin, use this instead: `{"t": "stat", "label": "84+ month loans, Q3 2026", "value": "25.5%", "tone": "down", "sub": "Record; 21.8% a year earlier (Edmunds)", "mood": "worried"}`

### 2. Weak, mismatched hook, line 1 (must fix)
At about 12 words, the spoken line runs over 3 seconds. "In twenty twenty-six" uses up the first beat without adding anything. "twenty-seven ninety" can be heard as $27.90. The spoken line also drops "you", so it doesn't match the caption, and the label "2026: 7% APR" suggests the example is real data when it is hypothetical.
- text: `This lower car payment costs $2,790 more.`
- say: `This lower car payment costs twenty-seven hundred ninety dollars more.`
- scene: `{"t": "hook", "title": "Pay less, [owe more]", "prop": "tag", "label": "Hypothetical, 7% APR", "value": "+$2,790", "mood": "shock"}`

### 3. On-screen subtraction doesn't match its result, line 4 (must fix)
The sub says "$9,372 - $6,583", which works out to $2,789, while the big number says +$2,790 (the exact difference is $2,789.96). The spoken "one sixty-five" and "twenty-seven ninety" are also hard to follow out loud.
- text: `The payment drops about $165, but interest rises $2,790.`
- say: `The payment drops about a hundred sixty-five dollars, but interest rises twenty-seven hundred ninety.`
- scene: `{"t": "stat", "label": "Extra interest, 84 vs 60", "value": "+$2,790", "tone": "down", "sub": "Unrounded math, hypothetical loan", "mood": "shock"}`

### 4. Rate assumption missing for the add-on, line 5 (should fix)
$22.64 only works at 7% APR, and the screen doesn't say so.
- text: `The payment can hide add-ons, too: at 7% APR, a $1,500 add-on over 84 months adds just $22.64 a month.`
- say: `The payment can hide add-ons, too. At seven percent, a fifteen hundred dollar add-on over eighty-four months adds just twenty-two dollars sixty-four a month.`
- scene: `{"t": "money", "from": {"label": "Add-on", "value": "$1,500"}, "to": {"label": "Per month, 84 mo, 7%", "value": "$22.64"}, "mood": "worried"}`

### 5. Awkward narration, line 6 (should fix)
"calls packing add-ons into a payment, payment packing" sounds clumsy read aloud.
- text: `The FTC calls that 'payment packing.'`
- say: `The F T C calls that payment packing.`
- scene: unchanged.

### 6. Line 3: label the example out loud (minor)
- text: unchanged.
- say: `Hypothetically, borrow thirty-five thousand dollars at seven percent. Over sixty months, it's about six ninety-three a month. Over eighty-four, about five twenty-eight.`
- scene: unchanged. The values ($693.04 and $528.24, 7 characters each) are correct.

### 7. Line 8: tighter wording (minor)
- text: `By law, the contract also lists the total of payments: everything paid over the loan.`
- say: `By law, the contract also lists the total of payments: everything paid over the loan.`
- scene: unchanged.

### 8. Post captions (must fix, so they match the new line 7)
- ig: change the Edmunds sentence to: `Edmunds: loans of 84+ months hit a record 25.5% of new-car financing in Q3 2026, up from 21.8% in Q3 2025.` Change the sources line to `Sources: Edmunds (Q3 2026); FTC; CFPB Regulation Z.` Change the first line to `This lower car payment costs $2,790 more.`
- yt_desc and tiktok: accurate; no change needed.

## Spoken word count
The original has 148 words. With all the replacements above it has 144, under the 150 limit.

## Sources
- Edmunds Q3 2026 release (Oct 1, 2026), via search snippets: 25.5% record, 23.9% Q2 2026, 21.8% Q3 2025, APR 7%: https://www.financialcontent.com/article/gnwcq-2026-10-1-new-car-financing-records-pile-up-in-q3-as-buyers-borrow-more-and-stretch-loans-longer-according-to-edmunds
- Edmunds Q1 2026 (22.9%, 21.2% Q1 2025): https://www.edmunds.com/car-news/edmunds-insights-q1-2026-report.html and https://www.autoremarketing.com/autofinjournal/records-set-in-edmunds-q1-data-reinforce-thought-of-cliff-connected-to-84-month-contracts/
- Edmunds Q1 2025 (19.8%, 15.8%, 13.4%): https://www.edmunds.com/industry/press/1-in-5-new-car-shoppers-committed-to-an-84-month-loan-in-q1-2025-according-to-edmunds-experts.html
- Edmunds Q3 2024 (18.1%): https://www.autonews.com/finance-insurance/18-q3-new-car-loans-have-84-month-terms-edmunds-says/
- FTC payment packing: https://www.autofinancenews.net/allposts/compliance/ftc-cracks-down-on-dealers-engaged-in-payment-packing/
- Reg Z 1026.18: https://www.consumerfinance.gov/rules-policy/regulations/1026/18/

VERDICT: FAIL

## Round 2 (re-read of the revised raw.json, Oct 2, 2026)

### Fixes checked
- **Line 1 (hook):** text "This lower car payment costs $2,790 more." matches the spoken "twenty-seven hundred ninety dollars more." It is 10 words, about 3 seconds. The label "7% APR example" now marks it as hypothetical. Resolved.
- **Line 4:** the sub "unrounded math, hypothetical" no longer shows a $2,789 subtraction. The spoken "about a hundred sixty-five dollars" matches $164.80 rounded. Resolved.
- **Line 5:** the 7% rate is now stated in the text, the narration and the "Per month, 84 mo, 7%" label. $22.64 is correct. Resolved.
- **Line 6:** "The FTC calls that 'payment packing.'" now reads naturally. The text matches the spoken line. Resolved.
- **Line 7:** now uses a stat scene with 25.5% (record, Q3 2026) and the sub "record; 21.8% in Q3 2025". Both figures match the Edmunds Q3 2026 release of Oct 1, 2026. Saying "third quarter of twenty twenty-six" in full avoids any relative time word, so it stays correct on Nov 22. The mixed-release chart is gone. Resolved.
- **Line 8:** the text matches the spoken line. Resolved.
- **IG caption:** it now carries the Q3 2026 / Q3 2025 figures and the updated first line. It is consistent with the video.

### New checks
- **Word count:** spoken words total 147, within the 150 limit.
- **On-screen vs spoken values:** they agree on every line ($693.04/$528.24 are spoken as "about six ninety-three/five twenty-eight").
- **Compare values:** both are 7 characters or fewer. No keep:true flags.
- **Content:** no advice, predictions or political opinion. The cover and title are paid off. The tiktok and yt_desc numbers match the script.
- **Optional nit (not blocking):** the IG add-on sentence could add "at 7% APR". The rate is already clear from the line before it.

VERDICT: PASS
