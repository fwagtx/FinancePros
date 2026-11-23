# Fact-check: 2027-01-22-explainer ("The pain of paying", cash vs card)

Checked Nov 23, 2026 for a Fri Jan 22, 2027 noon CT post. Every claim was checked against web search results, not the brief.
Limitation: direct page fetches to frbservices.org, frbsf.org, pewresearch.org and ocw.mit.edu were blocked by this session's network, and Firecrawl ran out of credits after two scrapes. Verification used search-result excerpts from those primary pages, one Firecrawl extraction of the Pew chart, and one Firecrawl read of the Fed's 2026 Diary PDF.

## Claims verified

| Claim | Status | Evidence |
|---|---|---|
| Prelec & Simester, Marketing Letters, 2001, sealed-bid auction for sold-out Celtics tickets; card bidders bid more than cash bidders | Confirmed | "Always Leave Home Without It: A Further Investigation of the Credit-Card Effect on Willingness to Pay," Marketing Letters 12(1), Feb 2001, DOI 10.1023/A:1008196717017. Subjects were MIT Sloan (MBA) students. |
| Cash mean $28.51 vs card mean $60.64 | Confirmed (secondary sources) | One source quotes these exact figures, and MIT course slides give rounded $29 and $61 (p<.01). Sample sizes were not confirmable, so the script does not state them. |
| 60.64 / 28.51 = about 2.1x | Correct | 2.127x, or +113%. "Double" in the hook is a fair rounding. |
| Knutson et al. 2007, Neuron: excessive prices activated the insula | Confirmed | Abstract: "excessive prices activated the insula and deactivated the mesial prefrontal cortex prior to the purchase decision." The insula is associated with anticipating loss or pain. |
| Fed Diary cash share by number: 2016 31% | Confirmed | 2018 Findings: 2017 was 30%, one point lower than 2016. Pew's chart of Atlanta Fed data also shows 31%. |
| 2017 30% | Confirmed | 2018 Findings: "30 percent of all transactions." |
| 2018 26% | Confirmed | 2019 Findings: cash 26%, debit 28%. |
| 2019 26% | Confirmed | 2020 Findings: "remains consistent at 26 percent." |
| 2020 19% | Confirmed | 2021 Findings: cash share fell 7 points in 2020. 2022 Findings: "up from 19 percent in 2020 and down from 26 percent in 2019." |
| 2021 19% | **Wrong per Fed** | The Fed's 2022 Findings say cash was **20%** in 2021 (the first rise in Diary history). Pew's chart shows 19, but the narration cites "the Fed's payment diary," so the Fed's figure is used. |
| 2022 17% | **Wrong per Fed** | The Fed's 2023 Findings say **18%** in 2022, and eMarketer also says 18%. Pew shows 17. The Fed figure is used. |
| 2023 16% | Confirmed | Fed's 2024 Diary: cash "decreased to 16%." |
| 2024 14% | Confirmed | Fed's 2025 Diary: cash was 14% of payments by number. |
| 2025 14% | Confirmed, already published | Fed's 2026 Diary (released May 2026): about 1 in 7 payments, roughly 14%. Pew (Sep 30, 2026) gives 14% for 2025. The next Diary normally comes out in May, so no newer data is expected before Jan 22, 2027, and the numbers are dated anyway. |
| "Biggest drop came in 2020, 26 to 19" | Confirmed | A 7-point drop. The next largest one-year drop was 4 points (2018). The chart_note "26>19" is 5 characters and matches the narration. |

## Issues found and fixes applied

1. **Line 0, hook.** It was true but presented one experiment as a general fact, without "in one experiment" as the brief requires. Changed to TEXT/SAY: "In one experiment, card payers bid double for the same Celtics tickets." That is 12 words, and the hook title "Card bids [double]" now matches the narration.
2. **Line 1.** "In a study published in 2001" repeated the hook's framing, and the spoken amounts "twenty-eight fifty-one" and "sixty sixty-four" were hard to follow by ear. Changed to TEXT: "In that 2001 study, cash bidders averaged $28.51; card bidders, $60.64." SAY: "In that two thousand one study, cash bidders averaged twenty-eight dollars fifty-one; card bidders, sixty dollars sixty-four." The on-screen values $28.51 and $60.64 are unchanged.
3. **Line 3, causal overclaim.** "Cash hurts because you watch it leave" stated a cause as fact. Changed to: "Researchers call it the pain of paying: handing over cash can sting, while a swipe may barely register." The split items became "Hand it over / It can sting" and "Just a swipe / Less felt".
4. **Line 4, inaccurate wording.** "Too-high prices lit up an area tied to expected loss" was loose. Changed to match the paper: "A 2007 brain-scan study found excessive prices activated the insula, a region linked to anticipating loss." It no longer implies the scan study compared cash and cards.
5. **Line 5, chart data.** The 2021 and 2022 points did not match the Fed's published figures. Changed points 2021 from 19 to **20** and 2022 from 17 to **18**. All 10 years stay evenly spaced (2016 to 2025). The narration now says "US consumer payments," which is what the Diary measures.
6. **Line 6.** Because 2021 rose to 20, "biggest drop" became "biggest one-year drop" so the claim is precise. The line was also lengthened to 17 spoken words to meet the 15+ minimum for chart lines: "The biggest one-year drop came in 2020, when it went from 26% to 19%."
7. **Line 7, advice.** "Before a big card purchase, ask if you'd pay that in cash" was a behavioral instruction. Changed to a neutral reflection: "Worth a thought: would you pay the same amount if it were cash?" The board "Would I pay this / in cash?" is kept and the mood is set to think.
8. **Post captions.** Updated to match the narration: post title "In one study, card bidders offered twice as much", plus matching IG, TikTok (150 characters) and YouTube text with the "one study" and "consumer payments" wording.

Checks with no issues:
- No stale news or time words: every figure is tied to a year, and there is no "this year" or "recently".
- No price predictions and no political opinion.
- The cover "Cash vs. Card" with x2 is paid off by the video.
- The worked math is correct.
- On-screen values match the spoken ones.
- Anthropic is not mentioned.
- The last line is unchanged.

check.py result: OK, 9 lines, 139 spoken words, hook 12 words.

## Sources
- Prelec & Simester 2001, Marketing Letters (DOI): https://doi.org/10.1023/A:1008196717017
- MIT OCW course slides (Celtics auction, about $29 vs $61): https://ocw.mit.edu/courses/15-821-listening-to-the-customer-fall-2002/5cc52570803b6e1bbea64585acdce779_redblack20copy.pdf
- Secondary source with the exact $28.51 / $60.64: https://insightcompass.substack.com/p/the-painless-purchase
- Knutson et al. 2007, Neuron, "Neural predictors of purchases": https://pubmed.ncbi.nlm.nih.gov/17196537/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC1876732
- Fed 2018 Findings (2017 data, 30%, down 1 point from 2016): https://www.frbservices.org/news/research/2018-findings-diary-consumer-payment-choice/
- Fed 2019 Findings (2018 data, 26%): https://www.frbservices.org/news/research/2019-findings-diary-consumer-payment-choice/
- Fed 2020 Findings (2019 data, 26%): https://frbservices.org/news/research/2020-findings-from-the-diary-of-consumer-payment-choice
- Fed 2021 Findings (2020 data, down 7 points): https://frbservices.org/news/research/2021-findings-from-the-diary-of-consumer-payment-choice/
- SF Fed press release on the 2022 Findings (2021 data, 20%; 19% in 2020; 26% in 2019): https://www.frbsf.org/news-and-media/news-articles/press-releases/2022/05/pandemic-continues-to-affect-consumer-payments/
- Fed 2023 Findings (2022 data, 18%): https://www.frbsf.org/wp-content/uploads/2023-Findings-from-the-Diary-of-Consumer-Payment-Choice.pdf
- Fed 2024 Diary (2023 data, 16%): https://www.frbservices.org/news/research/2024-diary-of-consumer-payment-choice/
- Fed 2025 Diary (2024 data, 14%): https://www.frbservices.org/news/research/2025-diary-of-consumer-payment-choice/
- Fed 2026 Diary (2025 data, about 1 in 7, roughly 14%): https://frbservices.org/news/research/2026-findings-diary-consumer-payment-choice ; https://www.frbservices.org/binaries/content/assets/crsocms/news/research/2026-diary-consumer-payments-choice.pdf
- Pew Research, Sep 30, 2026 (Atlanta Fed series, 14% in 2025): https://www.pewresearch.org/short-reads/2026/09/30/from-cash-to-credit-how-americans-payment-methods-have-changed-in-the-past-decade/

All issues above are fixed in 2027-01-22-explainer.raw.json.

VERDICT: PASS

## Round 2 (editor)
Reviewed fixes; experiment framed as one study; Fed diary values used; on-screen and spoken values agree.
VERDICT: PASS
