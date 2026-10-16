# Fact-check: 2026-12-15-lf-business ("How Starbucks makes money")

Checker: independent (did not read the .research.md). Checked on Oct 16, 2026; the video posts Tuesday Dec 15, 2026.
Script: 95 lines, 1,779 spoken words. Mechanical checks: no keep:true follows a different scene template; every compare value is 7 characters or fewer.
Method: web search excerpts of the SEC 10-K, the Q4 FY25 and Q3 FY26 releases, the Starbucks IR digital dashboards and press releases, plus Axios, NPR, NBC, Bloomberg and GeekWire. Direct fetches of sec.gov, q4cdn and businesswire were blocked by the proxy. All math was recomputed in Python.

## Claim-by-claim

| Line | Claim | Verdict | Source / note |
|---|---|---|---|
| 0 | The highest-margin business has no cafes | TRUE | Channel Development's 47.3% is the highest segment margin (NA 11.5%, Intl about 12.1%). It is a 10-word hook that fits in under 3 seconds. |
| 1-3, 45 | Channel Dev 47.3%, NA 11.5%; $47.30 vs $11.50 per $100 | TRUE | FY2025 10-K segment table: CD op income $885.1M on revenue of $1,871.7M; NA $3,156.7M. |
| 4, 12 | $37.2B revenue (+3%); 40,990 stores at Sept 28, 2025 | TRUE | Q4 FY25 release; 10-K store table. |
| 8-11 | 1971 Pike Place; Schultz 1987; June 1992 IPO at $17 on Nasdaq; Niccol Sept 2024 | TRUE | Starbucks history. (The first store was at 2000 Western Ave in the Pike Place Market area. Starbucks itself describes it as Pike Place Market, so this is acceptable.) |
| 13, 83 | 16,864 US + 8,011 China = about 61% | TRUE | 24,875 / 40,990 = 60.7%. |
| 14-15 | Revenue chart FY19-FY25: 26.5, 23.5, 29.1, 32.3, 36.0, 36.2, 37.2 | TRUE | Matches the 10-K figures (26,508.6; 23,518.0; 29,060.6; 32,250.3; 35,975.6; 36,176.2; 37,184.4). |
| 18-20 | NA $27.4B (74%), Intl $7.8B (21%), CD $1.9B (5%) | TRUE | 73.6% / 21.0% / 5.0%. |
| 22 | 21,514 company-operated / 19,476 licensed | TRUE | 10-K; the two add to 40,990. |
| 24 | Company-operated $30.7B = 83% | TRUE | 82.7%. |
| 27 | Licensed $4.4B = 12%; nearly half of stores | TRUE | 11.7%; 47.5% of stores. |
| 28 | Quote: "licensed stores generally have a lower gross margin and a higher operating margin than company-operated stores" | TRUE (verbatim) | The sentence appears in the Licensed Stores section of every 10-K from FY2016 to FY2025. |
| 30-31 | Beverages 73%, food 23%, other 4% | TRUE | FY2025 10-K. |
| 33 | Nestle paid about $7B in Aug 2018 | TRUE | About $7B (reported $7.15B); the deal closed Aug 2018. Scene source "Starbucks 10-K, Aug 2018" is slightly wrong because no 10-K is dated Aug 2018; see minor fix M1. |
| 36 | $7B / 40 = $175M | TRUE (math) | Labeled as simple division. |
| 37 | $176.5M booked "each year since fiscal 2021" | PARTLY UNVERIFIED | The FY2025 10-K confirms $176.5M in each of FY2023, FY2024 and FY2025. "Since FY2021" could not be confirmed. FIX 2. |
| 38 | "about $5.6 billion still waiting to be counted" | INACCURATE | $5.6B is only the long-term portion. The current portion of $177.0M also remains, so the total is about $5.78B, or about $5.8B. This also cross-checks with the math: $7B minus about 7 years at $176.5M is about $5.8B. FIX 3. |
| 40 | Nestle sales and royalties are most of CD revenue | TRUE | 10-K wording. |
| 42-44 | $885.1M / $4,991.8M = 17.7%; 5.0% of revenue | TRUE | 17.73% and 5.03%. Implied Intl op income is $950.0M, or 12.1% of $7,819.9M, which is consistent. |
| 47 | CD margin fell 5 pts, mostly from the PepsiCo venture | TRUE | 10-K: down 500 bps, of which about 350 bps came from lower NACP joint-venture income. |
| 49 | 34.2M 90-day active US members, Q4 FY25 | TRUE | Q4 FY25 Digital IR Dashboard. |
| 50 | 35.8M in the quarter to June 2026 | TRUE | Q3 FY26 Digital IR Dashboard (data as of June 28, 2026). Scene sub "Quarter to June 26" reads like the date June 26. FIX 4. |
| 52-53 | Mar 10, 2026 relaunch: Green / Gold at 500 / Reserve at 2,500; Green 1x, Reserve 1.7x | TRUE | Starbucks press release (Mar 10, 2026), NRN, Axios. |
| 54 | "The latest figure we found: Dec 2023, 31%" mobile order | STALE / FALSE "latest" | The Q2 and Q3 FY26 dashboards show mobile order at 33% of US company-operated transactions in the quarter to June 28, 2026. FIX 5. |
| 56 | $1.75B prepaid cards + Stars | TRUE | FY2025 10-K rollforward: $1,751.7M at Sept 28, 2025. |
| 57 | Breakage $222.4M | TRUE | $200.4M company-operated + $22.0M licensed = $222.4M (FY2025 10-K). |
| 61-62 | Op margin chart 16.8, 14.3, 16.3, 15.0, 7.9; op income $5.4B to $2.9B | TRUE | Recomputed from the 10-Ks. Q4 FY25 release: GAAP margin down 710 bps to 7.9%. |
| 63 | NA 19.8% to 11.5% | TRUE | FY2025 annual report: down 830 bps. |
| 64 | NA restructuring $653.2M | TRUE | 10-K NA segment table (2.4% of segment revenue). |
| 65 | Quote "We're getting back to Starbucks." from the Sept 10, 2024 open letter | TRUE (verbatim) | Axios quotes the letter: "Today, I'm making a commitment: We're getting back to Starbucks." |
| 66 | Started Sept 9, 2024 | TRUE | Baking Business / Starbucks. |
| 67 | Non-dairy upcharge dropped Nov 2024 at US and Canada company-operated stores | TRUE | Announced Oct 30, effective Nov 7, 2024 (NBC, Axios, TODAY). |
| 68-69 | Jan 2025: cut about 30% of menu by late 2025; condiment bars return | TRUE | NPR, Jan 28, 2025. |
| 70 | Sept 2025: about $1B plan, about 900 corporate jobs, closures | TRUE | AP, Al Jazeera, CNN, Sept 25, 2025 ("non-retail" roles). |
| 71 | 627 closed in Q4 FY25, 584 in NA | TRUE | The Q4 FY25 release says 627 closures, "over 90%" in North America. The release footnote gives 584 Q4 closures (584/627 = 93%). |
| 72 | "Niccol said the savings would go toward more baristas and new store designs, with a goal of about four-minute waits" | ATTRIBUTION NOT SUPPORTED | The four-minute target comes from the broader Back to Starbucks plan (Green Apron service and order-sequencing software). I found no source in which Niccol says the restructuring savings fund it. FIX 6. |
| 73-75 | Boyu: 60/40, closed by April 2026, about 8,000 stores move to licensed | TRUE | Starbucks release (Apr 2, 2026); the 10-Q says the deal closed Mar 30, 2026. Starbucks keeps 40% and licenses the brand. |
| 76 | Q3 FY26 (ended June 28, 2026) global comps +7.9% | TRUE | Q3 FY26 release (Jul 29, 2026): transactions +4.2%, ticket +3.5%. Correctly dated. |
| 77 | "Operating margin that quarter was 14.4%, up about 4.3 points" | MISLEADING | 14.4% (+430 bps) is the NON-GAAP margin. The GAAP margin was 10.5% (+60 bps). The script's 7.9% and 15.0% chart figures are GAAP, so viewers will compare a non-GAAP 14.4% with a GAAP 7.9%. FIX 7. |
| 78 | Revenue -1% to $9.3B, attributed to the China deal | TRUE | Release headline: "Down 1% to $9.3 billion, Reflecting the Starbucks China Transaction." |
| 81 | Arabica record of about $4.38/lb on Oct 23, 2025 | TRUE | Bloomberg (Oct 23, 2025): intraday all-time high of $4.3795. No credible higher 2026 record found; 2026 coverage shows arabica falling. |
| 86 | "nearly half of US customers who paid to modify drinks would save 10% or more" | IMPRECISE | Starbucks said the change would cut prices by more than 10% for nearly half of US customers who modify drinks with non-dairy milk, not customers who modify drinks in general. FIX 8. |
| 87 (scene) | "Extra Star Days" | MOSTLY TRUE | The official term is Double Star Days (at least 4 extra per year for Gold). Minor fix M2. |
| 89 | "Starbucks didn't brew it" | AWKWARD / IMPRECISE | Starbucks roasts and sells much of that coffee to Nestle, and nobody "brews" a bag. FIX 9. |
| 91-92 | Recap in present tense: "own cafes bring in 83%", "keeps 47.3%" | TIME-WORD RISK | These are FY2025 shares. The China stores moved to licensed in FY2026, so the company-operated share is lower now, and FY2026 results will be public by Dec 15. FIX 10. |
| 6 | "Every number comes from Starbucks' own filings." | FALSE | The arabica price (Bloomberg), the Niccol quote (open letter, Axios), the NPR menu plan and other figures do not come from filings. FIX 1. |

## Other checks
- Hook: true, specific and short, and the cover "47% Margin. No Cafes." and the post title are paid off in lines 1-3 and 42-47. PASS.
- Advice and predictions: none. Line 79 explicitly declines to predict. Chapter 6 describes effects on customers without telling viewers what to do. PASS.
- Politics: none.
- Spoken vs on-screen: all match, apart from the scene subs covered in the fixes.
- Worked examples: 17.7%, $175M, $11.50 and $47.30, and 61% are all correct and labeled.
- Staleness on Dec 15: FY2026 Q4 and full-year results (about late Oct 2026) will be out. Lines 76-78 are explicitly dated ("The latest quarter when this video was made ended June 28, 2026"), which is acceptable. Lines 54 and 91-92 need the fixes below.
- yt_desc: "CHAPTERS" is an empty heading. Confirm the build step fills it in, or remove it. If FIX 5 is applied, update the sources list as in FIX 11.

## Required fixes (line index = 0-based position in `lines`)

1. Line 6, `text`: `Most numbers come from Starbucks' own filings and releases. Education, not advice.`
   Line 6, `say`: `Most numbers come from Starbucks' own filings and releases. Education, not advice.`
   Line 6, `scene.lines`: `["Mostly Starbucks filings", "Education only"]`
2. Line 37, `text`: `The filings actually show about $176.5 million booked in each of fiscal 2023, 2024 and 2025.`
   Line 37, `say`: `The filings actually show about one hundred seventy-six point five million dollars booked in each of fiscal twenty twenty-three, twenty twenty-four and twenty twenty-five.`
   Line 37, `scene.sub`: `"FY2023-FY2025"`
3. Line 38, `text`: `At the end of fiscal 2025, about $5.8 billion of it was still waiting to be counted.`
   Line 38, `say`: `At the end of fiscal twenty twenty-five, about five point eight billion dollars of it was still waiting to be counted.`
   Line 38, `scene.value`: `"$5.8B"`
4. Line 50, `scene.sub`: `"Qtr to June 2026"`
5. Line 54, `text`: `Ordering ahead matters too. In the quarter that ended in June 2026, 33% of transactions at US company-operated stores came through mobile order.`
   Line 54, `say`: `Ordering ahead matters too. In the quarter that ended in June twenty twenty-six, thirty-three percent of transactions at US company-operated stores came through mobile order.`
   Line 54, `scene.value`: `"33%"`; `scene.sub`: `"US, Qtr to June 2026"`
6. Line 72, `text`: `Alongside the cuts, Starbucks has been adding baristas and redesigning stores, with a goal of getting most orders out in about four minutes.`
   Line 72, `say`: the same sentence as the text.
   Line 72, `scene.lines`: `["More baristas", "New store designs", "4-minute goal"]`
7. Line 77, `text`: `Operating margin that quarter was 10.5%, or 14.4% leaving out restructuring and other items.`
   Line 77, `say`: `Operating margin that quarter was ten point five percent, or fourteen point four percent leaving out restructuring and other items.`
   Line 77, `scene`: `{"t": "compare", "title": "Op. margin, Q3 FY26", "left": {"label": "Reported", "value": "10.5%", "tone": "neutral", "sub": "GAAP"}, "right": {"label": "Adjusted", "value": "14.4%", "tone": "up", "sub": "Ex-restructuring"}}`. If you keep the stat template instead, use value "10.5%" and sub "GAAP; 14.4% adjusted".
8. Line 86, `text`: `The free non-dairy swap was a real price cut. Starbucks said nearly half of US customers who add non-dairy milk would see their drink price drop by more than 10%.`
   Line 86, `say`: `The free non-dairy swap was a real price cut. Starbucks said nearly half of US customers who add non-dairy milk would see their drink price drop by more than ten percent.`
   (Scene value "10%+" can stay. Sub: `"Non-dairy users, 2024"`.)
9. Line 89, `text` and `say`: `And that bag of Starbucks coffee at the grocery store? Starbucks doesn't sell it to you directly, but it still earns from it, through Nestle.`
10. Line 91, `text`: `In fiscal 2025, Starbucks' own cafes brought in 83% of revenue. Licensed stores brought in 12%, with fewer costs.`
    Line 91, `say`: `In fiscal twenty twenty-five, Starbucks' own cafes brought in eighty-three percent of revenue. Licensed stores brought in twelve percent, with fewer costs.`
    Line 92, `text`: `The grocery and Nestle business is small, but it kept 47.3% of its sales as operating profit.`
    Line 92, `say`: `The grocery and Nestle business is small, but it kept forty-seven point three percent of its sales as operating profit.`
11. post.yt_desc: replace `GeekWire (Jan 2024)` with `Starbucks Q3 FY2026 Digital IR Dashboard`, and change `results for the quarter ended June 28, 2026` to `results for the quarter ended June 28, 2026 (GAAP and adjusted margins)`. Fill in or remove the empty `CHAPTERS` heading.

Minor (recommended, not blocking):
- M1. Line 33, `scene.source`: `"Deal closed Aug 2018"`.
- M2. Line 87, `scene.right.items[1]`: `"Double Star Days"`.

After these fixes: 1,794 spoken words (within 1550-1800). The line count stays at 95 (within 90-120).

VERDICT: FIX

## Round 2 (editor)
Applied fixes 1-11 and M1-M2 (subs/board lines shortened for layout; bare CHAPTERS line kept, the engine fills it with timestamps).
VERDICT: PASS
