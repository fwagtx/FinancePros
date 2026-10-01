# Fact-check: 2026-11-10-lf-business (long-form, "How Apple Makes Money")

Checked Oct 1, 2026, for posting Nov 10, 2026. I used about 14 web searches. SEC and q4cdn would not load directly, so 10-K figures come from search excerpts of the 10-K plus reputable outlets. I recomputed all the math in python.

## Verified (no change needed)
- FY2025 10-K figures:
  - Net sales were $416.161B, up 6.4%.
  - iPhone $209.586B; Services $109.158B, up 13.5% (rounds to 14%); Wearables/Home/Accessories $35.686B, down 3.6%; Mac $33.708B, up 12.4%; iPad $28.023B.
  - Products gross margin was 36.8% ($112.9B). Services gross margin was 75.4%, up from 73.9%.
  - Net income $112.010B; R&D $34.55B, up 10%; buybacks of 402M shares for $89.3B; dividends $15.4B.
- Derived figures:
  - Services were 26.2% of sales and 42.2% of gross profit; devices 73.8% and 57.8%.
  - iPhone was 50.4% of sales. Hardware sales were $307.0B.
  - Services grew 2.36x from FY2019 ($46.291B), shown as "2.4x".
  - Cash returned was $104.7B, which is 93.5% of net income ("about 93%" is OK).
  - Services margin is 2.05x the products margin ("about twice").
- Services chart for FY2019–2025: 46.291, 53.768, 68.425, 78.129, 85.200, 96.169 and 109.158 all match the 10-Ks.
- 10-K wording:
  - The 10-K says Services growth was "primarily due to higher net sales from advertising, the App Store and cloud services".
  - The Services categories are advertising, AppleCare, cloud, digital content and payment services.
  - The 10-K says the Products margin decline was "primarily due to a different mix of products and tariff costs". So L24 and L83 are fair.
- Q3 FY2026 (quarter ended June 27, 2026; reported July 30, 2026): revenue was $109.4B, up 16%. Services set a June-quarter record of about $30.7B.
- On Apr 30, 2026, Apple announced an additional buyback program of up to $100B and raised its dividend 4% to $0.27.
- Installed base: "more than 2.5 billion" active devices (Jan 29, 2026 call), up from 2.35B in January 2025.
- Analysis Group study (released June 2026, paid for by Apple): over $1.4T in developer billings and sales in 2025. Developers paid no commission on more than 90% of it. Physical goods made up about $1.1T.
- Worked example: $10 at 30% splits $3/$7, and at 15% splits $1.50/$8.50. It is labeled "ignoring taxes".
- Epic case:
  - Contempt ruling by Judge Gonzalez Rogers on Apr 30, 2025, which covered the 27% commission.
  - The Ninth Circuit affirmed the contempt finding on Dec 11, 2025. It held Apple may charge a commission "based on the costs that are genuinely and reasonably necessary for its coordination of external links ... but no more" and sent that back to the trial court.
  - The Supreme Court granted cert on June 30, 2026.
- Google case:
  - Mehta's Aug 5, 2024 ruling said about $20B was paid to Apple in 2022.
  - The 36% figure came from Kevin Murphy, Google's own expert witness, on Nov 13, 2023 (Bloomberg). Pichai later confirmed it.
  - The remedies opinion was issued Sept 2, 2025.
  - Google filed its notice of appeal on Jan 16, 2026. The DOJ and the states cross-appealed in Feb 2026. The appeal is still pending in the D.C. Circuit and no argument date has been set.
- The 10-K quote text in L63 is word-for-word. Its framing is not (see issue 1).
- No advice, price predictions or political opinion. The Apple and Epic positions in L52 are balanced. The hypothetical in L44 is labeled.

## Issues (must fix)
1. **L63: the 10-K quote is put in the wrong context.**
   - In the FY2025 10-K, the "could materially adversely affect ..." sentence refers to the DOJ's *originally proposed* remedies, such as barring Google from offering Apple commercial terms. The 10-K says those could come back if the order were reversed on appeal.
   - The 10-K does not say this about the Sept 2025 remedies, which still allow payments. "Remedies like these", placed right after L60–62, misrepresents the filing.
   - Fix: "Apple's 10-K warns that if an appeal brought back tougher remedies the government first proposed, like barring Google from paying Apple, they 'could materially adversely affect' its ability to earn that revenue."
2. **L60–L62: the one-year limit comes from the wrong ruling.**
   - The limit of one year per default deal comes from Mehta's final judgment of Dec 5, 2025, not the Sept 2, 2025 opinion. The title "Remedies, Sept. 2, 2025" is shown on all three items.
   - Fix L60: "In September 2025, the judge ruled on remedies, and a final judgment in December spelled them out." Retitle the list "Google remedies, 2025".
   - Optionally add "Dec 2025: final judgment" to the L64/65 timeline. Google appealed that judgment.
3. **L25, on screen "Half from iPhone": wrong.** iPhone is about 68% of the $307B hardware sales ($209.6B / $307.0B). It is half of *total* sales. Fix the item to "iPhone: $209.6B" or "About 2/3 from iPhone".
4. **Post title "$104.7B in Buybacks": wrong.** Buybacks were $89.3B; $104.7B is buybacks plus dividends. Fix: "...and $104.7B Returned to Shareholders".
5. **L82 overstates the Supreme Court case.** Cert was granted "limited to Question 1", which is the standard for a civil-contempt sanction. The Court is not reviewing Apple's commission or steering rules generally.
   - Fix L82: "Third, the App Store fights. The Supreme Court is reviewing the contempt ruling that limits Apple's fees on outside purchases."
   - Optionally make L49 more precise: "...agreed to hear Apple's appeal of the contempt ruling in its fight with Epic Games."
6. **L8 and yt_desc: wording will be stale or awkward on Nov 10.**
   - "Were due in late October 2026, after this video was made" reads oddly once the results are out. The yt_desc line "due in late October 2026, are not included" will be stale. The Oct 29 date is not yet confirmed.
   - Fix L8, both on screen and spoken: "We made this video before Apple's fiscal 2026 results came out, so they aren't included here." This is true whenever Apple reports.
   - yt_desc: "This video was made before Apple reported its fiscal 2026 results, so those are not included."

## Issues (should fix)
7. **L51: no date for the appeals ruling.** Make it: "In December 2025, an appeals court upheld the contempt finding, but said Apple may charge a commission based on its genuine costs for linked-out purchases. The exact amount is still being set, and Apple is still fighting it." The on-screen "Fee for real costs: OK" is fine.
8. **L57: attribution.** Say "Google's own expert witness testified in November 2023 that Apple gets 36%..." This is more precise and is how Bloomberg reported it.
9. **L6: spoken and on-screen don't match.** Five chapters are spoken, but the list shows four items; "Where the cash goes" is missing. Add it as a fifth item.
10. **L43: small business rule.** The program covers developers with *up to* $1M in proceeds in the prior calendar year, and they must enroll. Suggested wording: "...for small developers in Apple's program, with up to $1 million in proceeds the year before..."
11. **L66: status date.** "As of August 2026" is accurate but can be refreshed to "As of late September 2026, the appeal was still pending." That is verified, and no argument date has been set.
12. **L79: awkward to say aloud.** "Services can keep billing at about 75%" sounds like a price. Fix: "...and services can keep billing, at about a 75% margin."
13. **L11: "For three decades, computers were the story" is a simplification.** By 2006 the iPod was a large share of sales. Suggest "For most of three decades, computers were the core of the story."
14. **On-screen length.**
    - L25 is the longest caption at 163 characters and 34 spoken words. It likely breaks the caption limit, so split it into two lines.
    - L50 (142), L56 (139), L49 (136) and L52 (134) are also long.
    - The L63 quote is 104 characters. It is fine if the quote card allows it.
15. **L93: awkward phrasing.** "If this made Apple make more sense" is clunky aloud. Try "If Apple makes more sense now, subscribe..."
16. **Context (optional).** In Q3 FY2026, Apple's gross margin included about 2 points of *tariff refunds*. L83's tariff risk is still accurate as a FY2025 10-K statement, but the framing should stay dated as it is now.

## Opening
L1 is true, specific, about 10 words and under 3 seconds. It is a solid hook. It could be stronger with the contrast in the same breath: "Apple keeps about 75 cents of every Services dollar, double what it keeps on its devices." Do not say "iPhone", because iPhone-only margin isn't public. Consider folding L7 and L8 into a single line so the housekeeping doesn't slow the cold open.

VERDICT: FAIL
