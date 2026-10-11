# Fact-check: 2026-12-10-explainer (Roth conversions, posts Thu Dec 10, 2026)

Checked: 2026-10-11. Script: 2026-12-10-explainer.raw.json. 11 web searches; math recomputed in python.

## Claims verified

| Claim | Status | Source |
|---|---|---|
| No income limit on Roth conversions since 2010 | TRUE. TIPRA (2006) repealed the $100,000 MAGI limit and the MFS bar, effective Jan 1, 2010. IRS Topic 309: you may convert "regardless of your adjusted gross income." | Journal of Accountancy (2010); IRS Topic 309 |
| Hook "This Roth move has had no income limit since 2010" | TRUE. "Move" = conversion. Direct Roth contributions still have income limits (2026 single phase-out $153,000-$168,000). The script never says anyone can contribute directly, so the hook is accurate. | Fox/IRS 2026 limits coverage; TIPRA coverage |
| Converted pre-tax amount is ordinary income in the conversion year | TRUE. Treas. Reg. 1.408A-4; Pub 590-A: included in gross income for the year converted. After-tax basis is excluded, and "pre-tax" covers that. | Reg. 1.408A-4; Pub 590-A (via TaxAct) |
| Must be done by Dec 31 to count for the tax year | TRUE. No April window, unlike contributions. Custodians often set earlier cutoffs. | NAPA; advisor sources citing Pub 590 / Form 8606 |
| No recharacterization (undo) since Jan 1, 2018 | TRUE. IRS FAQ: "A Roth IRA conversion made on or after January 1, 2018, cannot be recharacterized." (TCJA) | irs.gov IRA FAQs - Recharacterization |
| 5-year rule per conversion | TRUE in substance, but line 7 states it imprecisely (see Issue 1). Pub 590-B: a separate 5-year period applies to each conversion. It starts Jan 1 of the conversion's tax year. Under 59½, a distribution of the taxable converted amount inside that window may owe the 10% additional tax unless an exception applies. | Pub 590-B (quoted by forums and Marotta) |
| 2026 single brackets: 12% $12,400-$50,400; 22% $50,400-$105,700 | TRUE (Rev. Proc. 2025-32) | KPMG TaxNewsFlash; Accounting Today |
| $10,000 x 12% = $1,200; x 22% = $2,200 | MATH CORRECT. The assumption that the whole $10K stays in one bracket is missing (see Issue 2). | python |
| IRS SOI: 2010 conversions rose "over 800 percent, to $64.8 billion" | TRUE, IRS wording, SOI Bulletin Fall 2013. From the 2009 figure of $6.8B the rise is about 853%. | irs.gov SOI Bulletin Fall 2013; Accounting Today |

## Issues and fixes (0-based line indexes)

1. **Line 7: imprecise 5-year rule (factual).** "each conversion gets its own 5-year clock, or a 10% extra tax can apply" makes the clock and the tax sound like alternatives. It also never says the tax applies only when converted money is withdrawn early.
   - text: `Under 59½, withdrawing converted money within 5 years of that conversion can trigger a 10% extra tax.`
   - say: `Under fifty-nine and a half, withdrawing converted money within five years of that conversion can trigger a ten percent extra tax.`
   - The list item "5-yr clock each" (lines 6 and 7) can stay.

2. **Line 4: hypothetical not fully labeled.** The $1,200 and $2,200 figures hold only if the entire $10,000 falls inside one bracket. Add that assumption.
   - text: `Example: 2026, single, federal only, all in one bracket. Converting $10,000 costs $1,200 at 12%, $2,200 at 22%.`
   - say: `Example: twenty twenty-six, single, federal only, all in one bracket. Converting ten thousand costs twelve hundred at twelve percent, twenty-two hundred at twenty-two percent.`
   - scene.left.sub: `2026, single, fed` (17). scene.right.sub: `all in 1 bracket` (16). Values $1,200 and $2,200 are 6 characters each, so they are fine.

3. **Line 5: absolutes.** "paying now wins" and "it costs you" are stated as certain. Other factors also matter (where the tax money comes from, state tax, growth).
   - text: `It's a bet on your tax rate: higher later, paying now usually wins; lower later, it usually costs you.`
   - say: `It's a bet on your tax rate: higher later, paying now usually wins; lower later, it usually costs you.`
   - scene.left.items[0]: `Usually wins` (12). scene.right.items[0]: `Usually costs` (13).

4. **Line 2: word budget and clarity (needed to fit the fixes above).** "When that cap ended in 2010" becomes a plain date. The causal "when" stays implied, and the IRS does attribute the jump mainly to the expanded eligibility.
   - text: `In 2010, conversions jumped over 800%, to $64.8 billion.`
   - say: `In twenty ten, conversions jumped over eight hundred percent, to sixty-four point eight billion dollars.`
   - The stat scene is unchanged.

5. **Post text (minor).** In ig and yt_desc, "a 5-year clock per conversion if under 59½" / "each has its own 5-year clock if you are under 59½" should name what the clock governs:
   - ig: `...and under 59½, withdrawing converted money within 5 years of each conversion can trigger a 10% extra tax.`
   - yt_desc: `...cannot be undone since 2018, and under 59½, withdrawing converted money within 5 years of that conversion can trigger a 10% additional tax.`

## Other checks
- **Hook.** 11 words, literally true, specific, and makes viewers need the answer ("what move?"). OK. Optional: the ig could add "(direct Roth contributions still have income limits)" for clarity. It is not required, because the script never implies direct contributions are open to everyone.
- **Advice.** The script never says "should" or "convert now". Each post carries a "not financial advice" line. OK.
- **Time words on Dec 10, 2026.** "Done by Dec 31" is correct for tax year 2026, and the script does not count days left. "Since 2010" and "since 2018" are evergreen. OK.
- **On-screen vs spoken.** All values match ($64.8B / sixty-four point eight billion; $1,200/$2,200; 800%; 12%/22%; 10%; 59½). OK.
- **Narration.** It reads naturally. The proposed fixes are speakable.
- **Renderer limits after fixes.**
  - Spoken words: 11+16+15+11+24+19+15+21+6 = **138** (at the 138 limit).
  - Hook: 11 words.
  - Stat label "Converted in 2010" is 17; sub "over 800%, IRS SOI" is 18.
  - Compare values are 6 each.
  - List and split items are 16 or fewer.
  - Split titles "Higher later" and "Lower later" are 12 and 11.
  - Board lines are 26 or fewer (longest is 25).
  - Prop label "Roth" is 4.
  - post.title is 49; post.tiktok is 144.
- **keep:true on line 7.** The previous line (6) is also `list`, so this is OK.
- **Cover.** "No Income Limit Since 2010?" is paid off by lines 0-2. OK.
- **Political opinion, allegations, quotes.** None. The SOI "over 800 percent" wording is used accurately.

## Sources
- IRS SOI Bulletin Fall 2013: https://www.irs.gov/statistics/soi-tax-stats-soi-bulletin-fall-2013
- Accounting Today on SOI 2010 conversions: https://www.accountingtoday.com/news/tax-break-for-roth-ira-conversion-attracted-10-of-high-earners
- KPMG, Rev. Proc. 2025-32: https://kpmg.com/us/en/taxnewsflash/news/2025/10/tnf-rev-proc-2025-32-inflation-adjustments-for-2026-individual-taxpayers.html
- IRS Topic 309: https://www.irs.gov/taxtopics/tc309
- IRS recharacterization FAQ: https://www.irs.gov/retirement-plans/ira-faqs-recharacterization-of-ira-contributions
- Journal of Accountancy (TIPRA, 2010): https://www.journalofaccountancy.com/news/2010/apr/20102811/
- Treas. Reg. 1.408A-4: https://federal-regs.com/title/26/part-1/1.408A-4/
- Pub 590-B 5-year conversion rule (quoted): https://marottaonmoney.com/understanding-the-5-year-holding-period-roth-conversions-and-exceptions/
- 2026 Roth contribution phase-outs: https://www.fox26houston.com/news/irs-401k-ira-contribution-limits-2026
- Dec 31 deadline: https://www.napa-net.org/node/31092

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-5 (precise 5-year rule wording, one-bracket assumption, "usually" in the bet, trimmed line 2, post copy). Spoken total 138.
VERDICT: PASS
