# Fact-check: 2026-11-17-lf-business (How Walmart beat everyone on price)

Checked Oct 2, 2026 for posting Nov 17, 2026. "Line N" = entry N (1-based) in `lines[]`; "file L" = line in the raw JSON file.

## Required fixes

1. **Line 67 (file 1199-1200, scene file 1203-1215): Walmart Connect +41% was the Q4 FY2026 figure, not full-year.** Walmart's Q4 FY26 release and coverage (ppc.land, Talk Business) say Walmart Connect U.S. grew 41% *in the fourth quarter* (excl. Vizio). The scene title "Ad growth, fiscal 2026" sets it beside the full-year +46%.
   - text: `That figure includes Vizio, the TV maker Walmart bought in December 2024. In the fourth quarter alone, Walmart Connect in the U.S. grew 41%.`
   - say: `That figure includes Vizio, the TV maker Walmart bought in December twenty twenty-four. In the fourth quarter alone, Walmart Connect in the U S grew forty-one percent.`
   - scene: title `"Ad growth, FY2026"` (unchanged meaning). Right side: label `"WMT Connect US"`, value `"+41%"`, sub `"Q4 only, U.S."` (13 chars). Left sub stays `"incl. Vizio"`, and its label can become `"Global ads, FY"`.

2. **Line 12 (file 213-214), plus the timeline events in lines 9, 10, 12 and 16 (file 151, 182, 227, 311): the first distribution center date.** Walmart did go public in 1970 (first shares Oct. 1970 at $16.50; NYSE listing 1972). But Walmart's own corporate history page dates its first distribution center and Home Office in Bentonville to **1971**. Some secondary sources say 1970. Use the company's date.
   - text: `In 1970, Walmart went public. By 1971, it had opened its first distribution center, in Bentonville.`
   - say: `In nineteen seventy, Walmart went public. And by nineteen seventy-one, it had opened its first distribution center, back in Bentonville.`
   - timeline events (all four scenes): `{"when": "1971", "what": "Distribution hub"}`

## Recommended (not blocking)

3. **Line 79 (file 1385-1386): Supreme Court wording.** The current wording is accurate and neutral. Learning Resources v. Trump was decided Feb. 20, 2026, 6-3: IEEPA (1977) does not authorize the tariffs. A more precise version:
   - text: `On Feb. 20, 2026, the Supreme Court ruled that a 1977 emergency powers law, IEEPA, did not authorize certain tariffs.`
   - say: `Background: on February twentieth, twenty twenty-six, the Supreme Court ruled that a nineteen seventy-seven emergency powers law, known as I E E P A, did not authorize certain tariffs.`
4. **Line 80 (file 1397-1398): refund amount.** The CFO said Walmart was eligible for about $2.9B and had "just under $100 million" still to receive. CBS, NBC and Fortune report it received nearly $2.9-3B, recorded as a reduction of cost of sales. "About $2.9 billion" is defensible. A safer version:
   - text: `Walmart said it got nearly $2.9 billion in refunds in that quarter, and recorded them as lower cost of sales.`
   - say: `Walmart said it got nearly two point nine billion dollars in refunds in that quarter, and recorded them as a reduction in its cost of sales.`
5. **Line 58 (file 1054-1055): Sam's Club fees.** The new $60 and $120 prices apply to new members from May 1, 2026. Existing members pay them at their first renewal after that date. Suggested text: `Start with Sam's Club. Since May 1, 2026, new and renewing members pay $60 a year for a basic membership, and $120 for Plus.` (Change the say line to match.)
6. **Hook fairness (lines 1-2, 34, 89).** $22.3B is *consolidated* net income, which includes noncontrolling interests. Net income attributable to Walmart was $21.9B. Both work out to about 3.1¢ per dollar (3.12¢ vs 3.07¢), and line 2 says "consolidated" out loud, so the hook is fair. No change needed.

## Verified (no change)
- FY2026 (ended Jan 31, 2026): total revenues $713.163B (+4.7%); net sales $706.413B; consolidated net income $22.270B (3.12¢/$); operating income $29.825B (4.18% of revenue); gross profit rate 24.2% (24.1% prior year); opex $147.943B = 20.94% of net sales (20.7% prior year); cost of sales $535.395B.
- Inventories $56.4B and $58.9B; average about $57.6-57.7B; turns 9.28x (rounds to 9.3x); 365/9.28 = 39.3 days. All labeled "our math".
- Revenue series: FY20 524.0, FY21 559.2, FY22 572.8, FY23 611.3, FY24 648.1, FY25 681.0, FY26 713.2. +36.1% over six years.
- 10,955 retail units in 19 countries; Walmart U.S. 4,611 units and $483.0B; about 280M weekly customers (company figure); about 2.1M associates.
- Sam's Club U.S.: membership and other income $2.525B vs operating income $2.442B. Companywide membership and other income $6.75B. Sam's Club fees went from $50/$110 (set in 2022) to $60/$120 effective May 1, 2026.
- Advertising: up 46% to nearly $6.4B including Vizio (deal closed Dec 2024); $6.4B is 21% of operating income. eCommerce sales $150.4B. eCommerce was first profitable in Q1 FY26, reported May 15, 2025.
- Q2 FY27 (released Aug 20, 2026): revenue $187.9B (+5.9%); operating income +28.8% (about $9.4B); eCommerce +23%; advertising +38%; membership fee revenue +17%; more than 11,000 U.S. rollbacks (company-stated).
- History: Walton's 5&10 (Ben Franklin franchise), Bentonville, 1950. First Walmart in Rogers, Jul 2, 1962; Walton was born Mar 29, 1918, so he was 44. First Sam's Club in Midwest City, Apr 7, 1983. First Supercenter in Washington, MO, 1988. Retail Link in the early 1990s.
- Quote: "If we work together, we'll lower the cost of living for everyone..." Mar 17, 1992. It matches word for word (the rest of the sentence is truncated correctly).
- Hypotheticals are labeled. 10k/90k = 11.1% and 10k/40k = 25%. 1,000 x $60 = $60,000.
- Line 7 discloses that Q3 FY2027 results are not included.
- No advice or price predictions. Critics vs supporters are framed as views. No stale "now/latest" time words: the "now" uses in lines 26, 62 and 94 are conversational.
- Layout: no limits exceeded (hook titles, titles/labels/subs, compare subs, headlines, timeline when/what, board lines). No countries scenes. No captions over 130 characters. yt_desc has the literal "CHAPTERS" line. 1,761 spoken words, within 1550-1800.

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-2 and recommended 3-5 verbatim (timeline hub -> 1971 in all four timelines). VERDICT: PASS
