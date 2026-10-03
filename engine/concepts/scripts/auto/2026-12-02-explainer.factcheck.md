# Fact-check: 2026-12-02 Explainer (financial infidelity)

Checked: 2026-10-03, for posting Wednesday 2026-12-02. Source read: `2026-12-02-explainer.raw.json` only (research.md not read).
Searches: WebSearch (bankrate.com fetches are blocked, so verification relies on search excerpts of Bankrate's own pages and press-release PDFs plus secondary coverage: Newsweek, CPA Practice Advisor, Fox 2 Detroit, Money Under 30, Moneywise, Kiplinger).

## Claims verified

| Line | Claim | Result | Source |
|---|---|---|---|
| 0, cover | 67% of Gen Z (ages 18-28) in live-in relationships committed financial infidelity, Jan 2025 | **Verified.** Bankrate says "about two-thirds (67%) of Gen Zers (ages 18-28) in live-in romantic relationships have committed or are currently committing financial infidelity" | Bankrate 2025 survey / press release PDF; Newsweek |
| 1 | 40% overall, Bankrate Jan 2025 survey | **Verified.** "40 percent of U.S. adults in committed relationships (married, in a civil partnership or living with a romantic partner)". Published Jan 27, 2025, conducted by YouGov | Bankrate 2025; Moneywise; InvestigateTV |
| 2 | Boomers 30%, ages 61-79; Gen Z ages 18-28 | **Verified** (millennials 54%, ages 29-44; Gen X 33%, ages 45-60, not used). 30% is less than half of 67% (33.5%): **correct** | Bankrate 2025 press release |
| 3 | Overspending 33%, secret debt 23%, secret card 17%, secret savings 15% | **Verified** (secret checking 13% omitted, which is fine). Note: these are shares of **all** partnered adults, not of Gen Z | Bankrate 2025 |
| 4 | Bankrate average card APR 19.63% as of Sept 30, 2026 | **Verified.** Bankrate shows 19.63% on Sept 30, 2026 (down from the 20.79% record of Aug 14, 2024). Other trackers differ (Experian 19.25%, WalletHub 22.19%, LendingTree 23.82%), so the Bankrate attribution and the date are both needed, and both are present | Bankrate current-rates page (search excerpt) |
| 4 | $3,000 x 19.63% = $588.90 a year, before compounding | **Math correct** (python: 588.90). "Before compounding" is accurate: this is simple interest on a flat balance. Daily compounding would give about $650 | python |
| 5 | Jan 2026: 43% say money secrets are at least as bad as physical cheating (38% equal, 5% worse) | **Verified.** Base is all U.S. adults, so "43% of adults" is correct. Published Jan 29, 2026 | Bankrate 2026 press release; CPA Practice Advisor (Feb 5, 2026) |
| 6 | Rossman: "As long as you agree upon the parameters, maintaining separate accounts doesn't constitute financial infidelity." | **Verified word for word.** The top match for the exact phrase is the 2025 press release PDF, so "Jan 2025" is consistent | Bankrate 2025 press release (search excerpt) |

**Is the data stale?** The Jan 2026 Bankrate survey did not repeat the prevalence question. It asked about "at least as bad as cheating" and "don't know everything about partner's finances" instead. That leaves Jan 2025 as Bankrate's latest generational prevalence data, and the script labels it "Jan 2025" everywhere. Bankrate has released this survey in late January (Jan 27, 2025; Jan 29, 2026), so a newer one is not expected before Dec 2, 2026. If posting slips past about Jan 25, 2027, re-check.

**Time words:** No "this year", "recently" or "now". All dates are absolute and will still be correct on Dec 2, 2026. The APR is clearly dated Sept 30, 2026, so it stays accurate even after the weekly rate moves.

**Advice, predictions, politics:** None. The tone is neutral. The Rossman line is attributed as a quote, not an instruction. The CTA is fine.

**Hook (line 0):** True and specific. "Gen Z partners" is a fair shorthand for Gen Zers in live-in relationships, and line 1 states the base right away. The hook has no time word, and the on-screen "Jan 2025" label dates it. It runs 9 words, 15 syllables, about 3 to 3.5 s. That is borderline but acceptable, and the cover and post promise "what's hidden", which line 3 pays off. An optional tighter version is below. The hook passes.

**On-screen vs spoken:** All values match. Line 3 drops "percent" after the first item, which is natural.

## Issues

1. **REQUIRED, layout.** Line 6 `scene.source` "Ted Rossman, Bankrate, Jan 2025" is 31 characters, over the 28 caption limit.
   Fix: `"source": "Ted Rossman, Bankrate, 2025"` (27). No word-count change.
2. **REQUIRED, misattribution.** `post.title` "67% of Gen Z partners kept money secrets. What they hide": "they" points the hidden-items list at Gen Z. The 33/23/17/15% figures are for all partnered adults.
   Fix: `"title": "67% of Gen Z partners kept money secrets. What's hidden"` (55 ≤60). This matches the tiktok wording, "Here's what's hidden".
3. **Minor, on-screen vs spoken date phrasing.** Line 4: the text says "as of Sept. 30, 2026" but the narration says "in late September twenty twenty-six".
   Fix, same word count: `say`: "Say a secret card holds three thousand dollars at nineteen point six three percent, Bankrate's average A P R on September thirtieth, twenty twenty-six. That's five hundred eighty-eight dollars and ninety cents a year, before compounding." (36 words, unchanged)
4. **Minor, read-aloud.** Line 1 "Overall, it's forty percent of people…": "it's" has no clear referent when spoken.
   Fix, same word count (16): `text`: "Overall, 40% of people living with a partner did, in Bankrate's January 2025 survey." `say`: "Overall, forty percent of people living with a partner did, in Bankrate's January twenty twenty-five survey."
5. **Optional, hook.** To shorten it under 3 s, use `say` "Sixty-seven percent of Gen Z partners hid money secrets." That saves no words. Better to keep it as is. Do not swap in "Two in three", which would make the spoken value differ from the on-screen 67%.

Word count after the fixes: 138 (unchanged; fixes 3 and 4 swap equal word counts). All other fields are within limits: hook title 22 (with brackets), labels ≤28 (line 5 label is exactly 28), subs ≤18, compare values 3, list items ≤16, board lines ≤22, prop label 8, tiktok 148.

## Sources
- [Bankrate 2025 financial infidelity survey](https://www.bankrate.com/credit-cards/news/financial-infidelity-survey-2025)
- [Bankrate 2025 press release PDF](https://www.bankrate.com/f/102997/x/a6625b1769/financial-infidelity-survey-press-release-2025.pdf)
- [Bankrate 2026 survey](https://www.bankrate.com/credit-cards/news/financial-infidelity-survey/)
- [Bankrate 2026 press release PDF](https://www.bankrate.com/f/102997/x/92d3a45036/financial-infidelity-press-release-2026.pdf)
- [CPA Practice Advisor, Feb 5, 2026](https://www.cpapracticeadvisor.com/2026/02/05/more-than-2-in-5-americans-believe-financial-secrets-are-at-least-as-bad-as-cheating-bankrate-survey-says/177578/)
- [Newsweek: Gen Z most likely to commit financial infidelity](https://www.newsweek.com/study-gen-z-financial-infidelity-boomers-2021915)
- [Bankrate current credit card interest rates](https://www.bankrate.com/credit-cards/advice/current-interest-rates/)
- [Moneywise / Yahoo coverage](https://moneywise.com/life/lifestyle/sethi-on-financial-infidelity)

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-4. VERDICT: PASS
