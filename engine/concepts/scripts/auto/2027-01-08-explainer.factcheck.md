# Fact-check: 2027-01-08 explainer (credit score predicts repayment risk, not wealth)
Checked Nov 9, 2026 for posting Fri Jan 8, 2027, noon Central. Spoken words now 139 (115-140 OK); the fixes below keep it at 139. Hook (line 0) is 10 spoken words (OK).

## Verified (no change needed)
- Line 0 hook "A millionaire can have no credit score at all.": TRUE. A FICO Score needs at least one account open 6+ months and at least one account reported to a bureau in the past 6 months (and no deceased indicator). Savings, income and investments are not on credit reports. Source: myFICO "FICO score requirements" https://www.myfico.com/credit-education/faq/scores/fico-score-requirements ; Golden 1 CU help page; Bankrate "what credit score do you start with".
- Line 2 target definition: FICO bureau risk scores predict the likelihood of going 90+ days past due on a credit obligation in the next 24 months. Source: Equifax FICO Risk Score product page https://equifax.com/business/product/fico-risk-score ; myFICO "Understanding FICO Scores" booklet; American Banker (FICO scores rank borrowers by likelihood of default in the next 24 months, range 300-850).
- Line 3: 300-850, higher = lower predicted risk. Source: myFICO/FICO; American Banker.
- Average FICO, April readings (all confirmed): 2015 695 (FICO table, NGPF); 2016 699 (FICO blog "US Credit Quality Rising", CreditDonkey); 2017 700 (FICO blog "US Average FICO Score Hits 700"); 2018 704 (RISMedia Oct 2018, "704 in April"); 2019 706 (FICO/myFICO "Ticks Up to 706", April 2019 data); 2020 708 (FICO table; GOBankingRates, Self); 2021 716 (FICO blog "716 ... despite pandemic"); 2022 716 (FICO blog "Stays Steady at 716"); 2023 718 record (FICO blog "Average U.S. FICO Score at 718"; CNBC Oct 30, 2023); 2024 717 (FICO blog "stays at 717", as of April 2024); 2025 715 (FICO/BusinessWire Apr 16, 2025); Oct 2025 714 (FICO Score Credit Insights, BusinessWire Mar 24, 2026); **April 2026 714** (FICO Score Credit Insights Fall '26, BusinessWire Aug 25, 2026: "flat from October 2025 to April 2026, down one point year-over-year").
- Lines 6-7 our-math: Alex $1,000,000 - $0 = $1,000,000; Sam $60,000 - $95,000 = -$35,000. Correct, labeled hypothetical ("Our math"). Compare values "$1M" and "-$35K" are <=7 chars.
- Line 8: CFPB June 2025 technical correction: 2.7% of adults, about 7.0 million, credit invisible in Dec 2020; the 2015 report's 2010 estimate (26M / 11%) corrected to 13.5M (5.8%). Source: https://www.consumerfinance.gov/data-research/research-reports/technical-correction-and-update-to-the-cfpbs-credit-invisibles-estimate/ ; American Banker; Orrick InfoBytes Jun 27, 2025.
- No advice, no predictions, no politics. post.title 42 chars, tiktok 128 chars (OK).

## Issues

### 1. Line 4 + chart: stale latest reading (REQUIRED)
Problem: On Jan 8, 2027 the latest FICO national average is 714 (April 2026, FICO Fall '26 Credit Insights, released Aug 25, 2026; next reading not due until ~spring 2027). "then 715 in 2025" presents an outdated figure as the latest. Adding 2026 to the odd-year series would break even spacing, so switch the chart to the even-year April readings, all verified, ending at 714.
- Line 4 text: `The average FICO score was 699 in 2016, 714 in April 2026.`
- Line 4 say: `The average FICO score was six ninety-nine in twenty sixteen, seven fourteen in April twenty twenty-six.` (16 words, same as before)
- Line 4 scene: `{"t": "chart", "title": "Average FICO score", "points": [[2016, 699], [2018, 704], [2020, 708], [2022, 716], [2024, 717], [2026, 714]], "end": "714", "color": "up", "mood": "think"}`
Source: FICO blogs/BusinessWire as listed above (2016 699, 2018 704, 2020 708, 2022 716, 2024 717, Apr 2026 714).

### 2. Line 2 scene: stat value "24 mo" (REQUIRED)
Problem: the stat value is a time window, not an amount, and the label "Odds of 90+ late" does not read as a number paired with "24 mo"; viewers can't tell what is measured. Switch to a board. Also make the wording more exact: the target is reaching 90+ days past due, so "falling 90 days behind" fits better than "being 90 days late" (same word count).
- Line 2 text: `FICO builds it to predict your odds of falling 90 days behind on a debt within 24 months.`
- Line 2 say: `FICO builds it to predict your odds of falling ninety days behind on a debt within twenty-four months.`
- Line 2 scene: `{"t": "board", "lines": ["Predicts: 90+ days", "late in 24 months"], "mood": "think"}` (18 and 17 chars)
Source: Equifax FICO Risk Score page; myFICO "Understanding FICO Scores".

### 3. Line 6 scene: Sam sub overclaims (minor)
Problem: the right-hand sub "scores high" states as fact what the narration hedges ("can score high").
- Line 6 scene right.sub: `"can score high"` (14 chars). Text/say unchanged.

### 4. Line 8 scene: value differs from spoken (minor)
Problem: on-screen "7.0M" vs spoken "about seven million".
- Line 8 scene value: `"~7M"` (or `"7M"`). Text/say unchanged.

### 5. POST.ig and POST.yt_desc: stale average (REQUIRED, matches issue 1)
- POST.ig line replace `The average FICO score was 695 in 2015, a record 718 in 2023 and 715 in 2025 (FICO, April readings).` with `The average FICO score was 695 in 2015, a record 718 in 2023 and 714 in April 2026 (FICO, April readings).`
- POST.ig line replace `FICO scores (300 to 850) are built to predict the odds of being 90+ days late` with `FICO scores (300 to 850) are built to predict the odds of falling 90+ days behind` (optional, matches line 2).
- POST.yt_desc replace `The average FICO score was 718 in 2023 and 715 in 2025 (FICO)` with `The average FICO score hit a record 718 in 2023 and was 714 as of April 2026 (FICO)`.

## Notes
- Direct page fetches of fico.com / myfico.com / finviz.com were blocked by this session's network; figures were confirmed through multiple search results quoting FICO's releases and blogs.
- Once issues 1, 2 and 5 are applied (3 and 4 recommended), the script passes.

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-3 and minor fixes (chart even years to April 2026 = 714, line 2 board, can score high, ~7M, captions).
VERDICT: PASS
