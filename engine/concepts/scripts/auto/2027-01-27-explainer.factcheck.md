# Fact-check: 2027-01-27-explainer (store card discount vs interest)

Posting date: January 27, 2027, 12 PM Central. Checked on 2026-11-28 with web search.

## Claims verified
- Bankrate 2025 retail card study: 30.14% average APR across 110 cards (surveyed July 21, 2025), down from 30.45% in 2024, the second-highest since tracking began in 2008. The all-card average was 20.12%. Sources: bankrate.com/credit-cards/news/retail-store-credit-card-survey/, Bankrate 2025 press release PDF, PaymentsJournal, Chain Store Age. VERIFIED.
- Newer study check: I found no Bankrate retail card study from 2026 (searched bankrate.com and the wider web). One blog (Debt Discipline) labels the 2025 figures "July 2026", but its numbers are the same as the 2025 study's, so that label looks like an error. WalletHub's October/November 2026 store-card figure (about 33.1%) uses a different method, so it is not comparable and is not used. The 2025 study is still the newest; the chart stays 2021-2025. If Bankrate publishes before Jan 27, 2027, re-run this check.
- Yearly series: 2021 24.35%, 2022 26.72% (record at the time), 2023 28.93% (record), 2024 30.45% (record high), 2025 30.14%. Sources: Bankrate 2023 and 2024 press releases (28.93% record, 30.45% record), Bankrate 2024 survey page (lists 26.72% for 2022 and 24.35% for 2021), CreditCards.com Nov 2022 study, CBS News. VERIFIED. Note: the 2022 figure first appeared in a study by CreditCards.com, Bankrate's sister site, and Bankrate reuses it in its own series. Attributing it to Bankrate is acceptable.
- CFPB, "Issue Spotlight: The High Cost of Retail Credit Cards" (Dec 18, 2024): 90% of retail cards reported a maximum APR above 30%, vs 38% of general-purpose cards. Sources: consumerfinance.gov, Orrick InfoBytes, NBC News. VERIFIED. The headline "Store cards cost more" is a fair paraphrase of the report title.
- Experian: putting $200 on a store card with a $400 limit gives 50% utilization ($200 / $400). Applying typically triggers a hard inquiry that can lower a score by a few points for a short time. Sources: Experian "What to Know Before You Apply for a Store Credit Card", FICO (myfico.com). VERIFIED.
- Math: 20% x $500 = $100. $400 x 30.14% = $120.56, which rounds to about $121 for one year (simple interest, labeled "about" and "approx."). CORRECT.

## Issues found and fixes applied (in raw JSON)
1. Line 0 (hook): the hook is true but vague. "Checkout discount" does not say it is a store card offer. Fixed. Text: "That 20% store card discount can cost more than it saves." Say: "That twenty percent store card discount can cost more than it saves." (12 words, under 3 seconds.)
2. Line 2 (chart): the 2024 record (30.45%) is on screen but was never spoken, and "climbed ... to 30.14% in 2025" hides the 2024 peak. Fixed. Text: "It peaked at 30.45% in 2024, up from 24.35% in 2021." Say: "It peaked at thirty point four five percent in twenty twenty-four, up from twenty-four point three five in twenty twenty-one." (20 words.) The chart end value 30.14% is spoken in line 1.
3. Line 3: "in 2024" read as though the data year were 2024, and "agrees" was loose wording. It now names the report date, which matches the on-screen source "CFPB, Dec 2024". Text: "A December 2024 CFPB report: 90% of retail cards had max APRs over 30%." Say: "A December twenty twenty-four C F P B report: ninety percent of retail cards had max A P Rs over thirty percent."
4. Line 5: trimmed to fit the word budget. Text: "Small limits hurt: per Experian, $200 on a $400 limit is 50% utilization." Say: "Small limits hurt: per Experian, two hundred on a four hundred dollar limit is fifty percent utilization."
5. Line 6: "interest repeats every month" was inaccurate without the condition of carrying a balance. Fixed. Text and say: "Plus a hard inquiry. Discount: once. Interest: every month you carry a balance." The board ("Discount: once" / "Interest: monthly") is unchanged and matches.
6. Post captions: the IG caption and YouTube description now include the 2024 record, the Dec 2024 CFPB date, the hard inquiry, and "if/when you carry a balance". The TikTok caption adds "if you carry a balance".

## Other checks
- Stale news / time words: none that will be wrong on Jan 27, 2027. Every year is stated explicitly. The 2025 study is still the newest.
- Advice / price predictions / political opinion: none. The CTA tagline is "Education, not advice".
- Cover "20% Off, Or Not?" with value 30.14%: the video pays it off, and 30.14% is spoken.
- On-screen vs spoken values: all match ($100, $121, 50%, $200/$400, 30.14%, 20.12%, 30.45%, 24.35%, 90%, 30%).
- Last line unchanged. check.py: OK, 8 lines, 140 spoken words.

VERDICT: PASS

## Round 2 (editor)
Reviewed applied fixes (hook wording, 2024 peak spoken, CFPB date, carry-a-balance accuracy); limits pass.
VERDICT: PASS
