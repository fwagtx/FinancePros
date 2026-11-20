# Fact-check: 2027-01-19-explainer (marginal vs effective tax rate)
Checked 2026-11-20 for posting Tue 2027-01-19, 12:00 CT. Independent web verification. The research brief was not used.

## Verified facts
- 2026 single-filer brackets are 10% up to $12,400, 12% to $50,400, 22% to $105,700, 24% to $201,775, 32% to $256,225 and 35% to $640,600, with 37% above that. CONFIRMED by several sources that agree: the IRS release and Rev. Proc. 2025-32 summaries, PayBrackets, FinanceWonk and ustax.tools. The IRS release itself confirms the 37% rate above $640,600.
- The 2026 single standard deduction is $16,100, up from $15,750 in 2025. CONFIRMED by the IRS release (Oct 9, 2025) and AARP. One site (WealthVieu) lists $15,000, which is an older-year figure; I treated it as an outlier.
- The release number is IR-2025-103, per IRS.gov and KPMG. One newswire mirror labels it IR-2025-102. I kept IR-2025-103, which matches IRS.gov.
- Only search snippets were available: the fetches of kpmg.com and govdelivery.com were blocked by the network, and Firecrawl had no credits left.

## Math (all recomputed, all correct)
- Taxable income: 75,000 - 16,100 = 58,900.
- Tax by bracket: 10% x 12,400 = 1,240. 12% x 38,000 = 4,560. 22% x 8,500 = 1,870. Total 7,670.
- Effective rates: 7,670 / 58,900 = 13.02% of taxable income, and 7,670 / 75,000 = 10.23% of gross.
- Chart (effective rate on gross, single filer, standard deduction):
  - $25K: tax $890, rate 3.56%
  - $50K: tax $3,820, rate 7.64%
  - $75K: tax $7,670, rate 10.23%
  - $100K: tax $13,170, rate 13.17%
  - $125K: tax $18,734, rate 14.99%
- All five chart points match.

## Issues found and fixes applied
1. **Line 0, hook (weak and slow).** It ran 11 spoken words, about 3.7 seconds, which is over the 3-second target. Changed to text "22% bracket? You don't pay 22%." and say "Twenty-two percent bracket? You don't pay twenty-two percent." That is 8 words, about 2.7 seconds. It is true and specific, and it opens a question the viewer needs answered.
2. **Line 2, awkward narration.** "Our math, twenty twenty-six ... leaves fifty-eight nine hundred" read badly out loud. Changed the say to "Twenty twenty-six, single, seventy-five thousand. Minus the sixteen thousand one hundred standard deduction: fifty-eight thousand nine hundred taxable." The text now matches.
3. **Line 3, awkward narration.** "twelve forty" and "forty-five sixty" became "is twelve hundred forty" and "is forty-five hundred sixty". The text was updated to match.
4. **Line 4, awkward narration.** "eighteen seventy" became "eighteen hundred seventy".
5. **Line 5, awkward narration and missing scope.** "seventy-six seventy dollars" became "seventy-six hundred seventy dollars". The line now also says "Federal income tax only, no state or payroll tax", which makes the scope clear. The stat label changed from "2026 federal tax" to "Federal income tax" (18 characters).
6. **Line 6, trimmed for word budget.** "on the full" became "on all". The meaning is unchanged.
7. **Line 7, chart narration and axis labels.**
   - "our math climbs smoothly" was awkward. It now reads "Same math across incomes: about four percent at twenty-five thousand, rising to about fifteen percent at a hundred twenty-five thousand." That is 20 words.
   - The x values changed to the string labels "$25K", "$50K", "$75K", "$100K" and "$125K".
   - The end label changed from "14.99%" to "15.0%" so it matches the spoken "about fifteen percent". 15.0% is the correct rounding.
8. **Captions.** The IG and YT captions now say "payroll (FICA) tax". IG also gained the chart data points. All figures in the captions match the script.

## Other checks (no issue)
- **Time words:** "2026" is correct on Jan 19, 2027. That is the 2026 tax-year filing season, and the script uses no relative words like "this year" or "next year".
- **Stale news:** none. This is an evergreen explainer.
- **Advice, predictions or politics:** none. "Not financial advice" stays in the captions.
- **Cover ("22%? Not Really", 10.2%):** paid off by line 6 (10.2% of gross). Post title paid off as well.
- **Line 8 ("a raise into a higher bracket only taxes the extra dollars"):** accurate for the bracket mechanics shown.
- **On-screen vs spoken values:** they match. The on-screen 10.2% and 13.0% are spoken as "about ten" and "about thirteen percent", which is labelled rounding.
- **Checker:** reports OK with 10 lines and 140 spoken words. The hook is 8 words and the last line is unchanged.

## Sources
- IRS IR-2025-103: https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill
- KPMG on Rev. Proc. 2025-32: https://kpmg.com/us/en/taxnewsflash/news/2025/10/tnf-rev-proc-2025-32-inflation-adjustments-for-2026-individual-taxpayers.html
- Axios (Oct 9, 2025): https://www.axios.com/2025/10/09/irs-2026-tax-brackets-deductions-credits
- Tax Foundation: https://taxfoundation.org/data/all/federal/2026-tax-brackets/
- PayBrackets: https://paybrackets.com/2026-tax-brackets
- FinanceWonk: https://www.financewonk.com/references/federal-tax-brackets
- ustax.tools: https://ustax.tools/2026-federal-tax-brackets/
- AARP: https://www.aarp.org/money/taxes/income-tax-brackets-2025/

VERDICT: PASS

## Round 2 (editor)
Reviewed applied fixes: tighter hook, natural spoken numbers, federal-only scope stated, chart labels in $K.
VERDICT: PASS
