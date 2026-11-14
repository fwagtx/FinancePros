# Fact-check: 2027-01-13-explainer (Acorn Economics: what an IPO is)
Checked Nov 14, 2026 for posting Wed Jan 13, 2027 noon CT. Evergreen; every number is tied to calendar 2025 or labeled "our math".

## Verified claims
| Claim | Source | Status |
|---|---|---|
| 2025: 90 IPOs, 29.3% avg (equal-weighted) first-day return, $13.11B money left on the table | Ritter, "Initial Public Offerings: Updated Statistics," UF, Nov 5, 2026 (Table 1 dated July 13, 2026); PDF read via a cached Firecrawl copy; secondary sources (WebSearch) agree on 90 / 29.3% / $13.11B | OK |
| 24.4% of 2025 IPOs closed day one below offer (negative, excludes 2.2% flat) | Ritter Table 1a, same PDF | OK. Only one machine-read extract; it also listed 24.4% for 2021, so the 2025 row could not be re-quoted verbatim (Firecrawl credits ran out). Consistent with the brief and with 2023 = 53.7% |
| IPO counts 2015-2025: 118, 75, 107, 134, 113, 165, 311, 38, 54, 73, 90 | Ritter Table 1 (Nov 2026 ed.) | OK. Older editions show 117 (2015) and 74 (2016); the current edition has 118/75, which is what we chart |
| Ritter's count = operating companies, offer price >= $5, excludes SPACs/ADRs/units/REITs/banks/penny stocks | Ritter definitions; Renaissance Capital counts 202 for 2025 | OK, now labeled (see fixes) |
| ~7% gross spread on moderate-size deals | Ritter Table 10 "Gross Spreads Continue to Remain at 7% on Moderate-Size Deals, 2001-2025"; Chen & Ritter (2000); SEC 2018 appendix (96.6% of moderate IPOs at exactly 7%) | OK ("usually" for moderate-size deals; large deals pay less) |
| Lockup ~180 days, "usually" | Investor.gov glossary: "most prevent insiders from selling their shares for 180 days"; SEC lockup Q&A | OK |
| Money left on the table = (first-day close - offer) x shares; gain goes to buyers at the offer price, not the company | Ritter definition | OK, now explained in line 5 and the captions |

## Our math (recomputed)
- 2,000,000 x $20 = $40,000,000 (on screen "$40M") OK
- $40M x (1 - 0.07) = $37,200,000 ("$37.2M") OK
- ($26 - $20) x 2,000,000 = $12,000,000; pop = 6/20 = 30% ("+30%") OK

## Issues found and fixes applied to raw.json
1. Line 0 (hook): "IPOs" with no market was too broad (Ritter's $13.11B is US-listed IPOs only); "I-P-Os" hyphenation doesn't match earlier episodes, which use "I P O(s)" with spaces, and the spaced form would push the hook past 12 words. Fix: text "In 2025, US IPOs left about $13 billion on the table." / say "In twenty twenty-five, US IPOs left about thirteen billion on the table." (12 words; literally true).
2. Lines 6, 9: "I-P-Os" in say. Fix: "IPOs" (line 2's "I P O" matches past episodes and stays).
3. Line 5: "extra goes to first buyers" didn't tie back to "money left on the table". Fix: text "Our math: if slices close at $26, not $20, that's $12 million left on the table for first buyers." / say "Our math: if slices close at twenty-six, not twenty, that's twelve million left on the table for first buyers."
4. Line 6 chart: title "US IPOs per year" could be contradicted by broader trackers (Renaissance: 202 in 2025). Fix: title "US IPOs (Ritter)". The chart template has no sub field. Also "And the window swings" became "The window swings" to save a word.
5. Line 8: the 24.4% was not dated in speech, right after a 2021/2022 chart. Fix: text "But pops aren't promised: in 2025, about 1 in 4 closed day one below offer." / say "...in twenty twenty-five, about one in four closed day one below offer."
6. Line 7 (word budget): "That's the lockup." became ": the lockup." (text "Insiders usually can't sell for about 180 days: the lockup.").
7. Post: ig now defines money left on the table (it goes to first buyers, not the companies), labels the 311/38/90 counts as Ritter's operating-company count excluding SPACs and penny stocks, and dates the source as Nov 2026. tiktok now says "US IPOs" (143 chars). yt_desc gives the Ritter count definition and the money-left-on-the-table explanation.

## Other checks
- No stock tips, predictions or political content. "Not financial advice" is in all captions.
- Cover "What's an IPO?" / $13.1B is paid off by the hook and line 2. On-screen values match speech (13.1B rounds to "about thirteen billion"; 29.3% vs "about twenty-nine percent"; 24.4% vs "about one in four").
- check.py: OK, 10 lines, 140 spoken words (at the upper limit), hook 12 words.

Sources: https://site.warrington.ufl.edu/ritter/files/IPO-Statistics.pdf ; https://www.investor.gov/introduction-investing/investing-basics/glossary/initial-public-offerings-lockup-agreements ; https://www.sec.gov/answers/lockup.htm ; https://SEC.gov/news/speech/2018/ipo-data-appendix.pdf ; https://site.warrington.ufl.edu/ritter/files/2016/01/The-Seven-Percent-Solution-2000-06.pdf

VERDICT: PASS

## Round 2 (editor)
Hook says US IPOs; chart labeled Ritter count. check.py OK.
VERDICT: PASS
