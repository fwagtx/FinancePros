# Fact-check: 2026-11-24-lf-business ("How McDonald's became a real estate empire")

Checked October 2, 2026 for posting November 24, 2026, 4 PM CT. I read only the script JSON and the house rules. All math was recomputed in Python.

Structure: 91 lines (target 90-120) and 1,724 spoken words (target 1550-1800). Every keep:true line follows a line with the same scene template, so no chains are broken. Every compare value is 7 characters or fewer. The countries scene (line 55) has no prop and no label.

## Verified claims (no change needed)

| Line(s) | Claim | Source / check |
|---|---|---|
| 1, 2, 26-31, cover, post | FY2025 rents $10,442M, royalties $6,018M, initial fees $88M, franchised revenues $16,548M, company-operated sales $9,690M, other $647M, total $26,885M | FY2025 10-K and Q4 2025 release, via search excerpts. Rent minus company sales = $752M. 10,442 + 6,018 + 88 = 16,548. 16,548 / 26,885 = 61.6% ("about 62%"). Rent 63.1% and royalties 36.4% of franchised revenues. Rent per $1 of royalties = $1.735, shown as $1.74. |
| 33-35 chart | Rent: 2019 7,500.2; 2020 6,844.7; 2021 8,381; 2022 9,046; 2023 9,840; 2024 10,017; 2025 10,442 ($M) | FY2020, FY2022, FY2024 and FY2025 10-K tables, via search excerpts. Every point matches after rounding. 10,442 / 7,500 = +39.2%. |
| 49-51, 87 | Franchised margin 84.2%, company-operated margin 14.7%, franchised share of margin dollars 90.7% | Franchised margins $13,930M and company-operated margins $1,422M (FY2025). 13,930 / 16,548 = 84.18%. 1,422 / 9,690 = 14.67%. 13,930 / 15,352 = 90.74%. |
| 23, 24 | 45,356 restaurants, about 95% franchised, systemwide sales above $139B | FY2025 10-K and company restaurant table give $139.4B. |
| 54 | About 56% of land and 80% of buildings owned, consolidated markets, Dec 31, 2025 | FY2025 10-K wording |
| 57-60 | PP&E at cost: land 8,169; buildings on owned land 22,202; buildings on leased land 15,506; equipment 2,954; other 459; total 49,290 | FY2025 10-K. Buildings 37,708 ($37.7B). Equipment plus other 3,413 ($3.4B). |
| 36, 62 | Rent is a percent of sales with minimums; typical franchise term is 20 years | 10-K revenue description and franchise-term description |
| 37, 38, 67 | Q2 2026: franchised revenues +4% to $4.39B; franchised margins +4.3% to $3.71B; US comps +0.8%; global comps +1.3% | Q2 2026 release (Aug 4, 2026), Zacks/Yahoo and TradingView coverage |
| 3, 68, 69, 73 | Sept 23, 2026 Investor Day: $8.5B of franchisee support through 2036 (rent relief plus capital support), about $5B of it by 2030, about $100K a year of added cash flow per average US restaurant, about 4-year payback | CNBC, Quartz, Restaurant Dive, CP24/AP, 24/7 Wall St |
| 75 | More than 46,000 restaurants | Fortune (Sept 24, 2026) |
| 41, 42 | 2024 US average sales for a traditional restaurant were $4,002,000; new US restaurants have paid a 5% royalty (up from 4%) since 2024 | 2025 FDD Item 19 via Franchise Chatter; Restaurant Dive |
| 7, 9, 10 | Kroc opened Des Plaines in 1955; franchisees paid 1.9%, with 0.5% to the brothers and 1.4% to Kroc; 15 cents x 1.4% = 0.21 cents | Multiple histories |
| 11-14, 85 | Sonneborn (former Tastee-Freez finance VP) joined in 1956; Franchise Realty Corp. formed in 1956; rent was a 40% markup or 5% of sales, whichever was greater | Sonneborn bio and histories. One source says FRC was "born" in 1957, but most give 1956, so this is acceptable. |
| 17 (1960 part), 18, 19 | 228 restaurants by 1960; 1961 buyout for $2.7M; Sonneborn president 1959-1967 (resigned June 8, 1967) | Histories and Sonneborn bio |
| 20 | Quote wording "We are not technically in the food business. We are in the real estate business." is attributed to Sonneborn in Love's *Behind the Arches* | Matches the standard published wording. The full quote continues "The only reason we sell fifteen-cent hamburgers...", and the script quotes the first two sentences exactly. |
| 78 | Delivery: the app takes a commission, but rent and royalty apply to the full sale | Restaurant Business ("McDonald's works to make delivery profitable for franchisees"). It is framed as a trade-press report, which is fine. |
| 44, 45, 47, 80 | Example math: $200K + $400K = $600K = 15% of $4M; $3.4M remains; at $4.4M of sales the take is $660K (+$60K) | Correct, and the example is labeled hypothetical with the 10% rent stated as an assumption |

## Issues and exact fixes

### 1. Line 17: the "31 restaurants at end of 1957" figure is unverified and conflicts with sources (FACT, must fix)
Sources I could reach say "by 1957 there were 40 McDonald's" (TIME 2015 per search excerpt, TheStreet). None supports 31. Only the 228-by-1960 figure is confirmed.
- **text:** `And it worked. By 1960, there were 228 McDonald's restaurants.`
- **say:** `And it worked. By nineteen sixty, there were two hundred twenty-eight McDonald's restaurants.`
- **scene:** `{"t": "stat", "label": "McDonald's restaurants, 1960", "value": "228", "tone": "up", "sub": "From one Kroc store in 1955"}`

### 2. Line 70 (and the line 69 list item): the $800K cost is for a traditional US drive-thru, not "per US restaurant" (FACT, must fix)
Coverage says the NEXT upgrade costs about $800,000 for "a traditional U.S. drive-thru restaurant."
- **text:** `The goal: help pay for new equipment and tech that the company puts at about $800,000 for a traditional U.S. drive-thru.`
- **say:** `The goal is to help pay for new equipment and technology that the company puts at about eight hundred thousand dollars for a traditional US drive-thru restaurant.`
- **scene** (lines 69 and 70, both list items arrays): replace `"$800K per US store"` with `"~$800K per drive-thru"`. Make the same change on line 69 so the keep chain stays consistent.

### 3. Lines 75-76: the 2027 unit-growth target is reported inconsistently ("over", "about", "nearly" 4.5%) (FACT, should fix)
TipRanks/The Fly say "about 4.5%", another summary says "nearly 4.5%", and others say "over 4.5%". Use wording that holds under every version.
- Line 75 **text:** `The system keeps growing, too: more than 46,000 restaurants by September 2026. McDonald's also targeted net restaurant growth of about 4.5% in 2027.`
- Line 75 **say:** `The system keeps growing, too: more than forty-six thousand restaurants by September twenty twenty-six. McDonald's also targeted net restaurant growth of about four and a half percent in twenty twenty-seven.`
- Line 75 **scene.sub:** `"2027 goal: ~4.5% net growth"`
- Line 76 **scene.value:** `"~4.5%"` (was `"4.5%+"`)

### 4. Q3 2026 results will be out before the post (STALENESS, should fix)
McDonald's Q3 2026 report is expected October 22, 2026 (one calendar shows November 4). Either date falls before November 24, so by posting day Q2 will no longer be the latest quarter. As written, line 67's "U.S. sales growth slowed in 2026" could be contradicted if Q3 US comps reaccelerate. Change the wording so each Q2 figure is tied to its quarter.
- Line 37 **text:** `That held into 2026. In the April-to-June quarter of 2026, franchised revenues rose 4%, to $4.39 billion.`
- Line 37 **say:** `That held into twenty twenty-six. In the April-to-June quarter of twenty twenty-six, franchised revenues rose four percent, to four point three nine billion dollars.`
- Line 67 **text:** `And U.S. sales growth was slow in spring 2026. In the April-to-June quarter, U.S. comparable sales rose just 0.8%.`
- Line 67 **say:** `And US sales growth was slow in the spring of twenty twenty-six. In the April-to-June quarter, US comparable sales rose just zero point eight percent.`
- Editor note: when the Q3 release comes out, check whether US comps or franchised revenues moved sharply. If they did, think about adding the Q3 figures. The wording above stays true either way.

### 5. Spoken values that differ from on-screen values (MISMATCH, should fix)
- **Line 51:** the screen shows 90.7%, but the narration says "about ninety percent." 90.7 rounds to 91.
  **say:** `So franchised restaurants made about ninety-one percent of its restaurant margin dollars: thirteen point nine billion out of fifteen point four billion.`
  **text:** `So franchised restaurants made about 91% of its restaurant margin dollars: $13.9 billion of $15.4 billion.`
  Also note that the rounded $13.9B / $15.4B gives 90.3%, so a viewer checking the screen sees a slightly different number. Changing scene.value to `"91%"` makes everything consistent.
- **Line 2:** the screen shows $752 million, but the narration says "about seven hundred fifty million."
  **say:** `Rent won by seven hundred fifty-two million dollars. The world's best-known burger chain is also a giant landlord.`
- **Line 30:** the screen shows $16,548M, but the narration says "about sixteen and a half billion."
  **say:** `Add up rent, royalties and small initial fees, and franchisees sent McDonald's sixteen point five billion dollars in twenty twenty-five.`
  **text:** `Add rent, royalties and small initial fees, and franchisees sent McDonald's $16.5 billion in 2025.` (keep the board breakdown as is)
- Lines 31, 49, 50 and 87 round 63.1% to "about sixty-three", 36.4% to "about thirty-six", 84.2% to "about eighty-four" and 14.7% to "about fifteen". These round correctly, so they are acceptable. Optional: line 50 could say "fourteen point seven percent" to match the screen exactly.

### 6. Line 20: the "telling investors" context is unverified (QUOTE ATTRIBUTION, minor)
The wording matches the widely cited text from Love's book, but I could not confirm who Sonneborn was speaking to.
- **say:** `In John Love's nineteen eighty-six company history, Sonneborn is quoted saying: We are not technically in the food business. We are in the real estate business.`

### 7. Line 55: "the ones McDonald's runs directly" is loose (minor accuracy)
Consolidated markets are the US and the International Operated Markets. McDonald's is the franchisor there and owns or leases the sites, but most of those restaurants are still franchised.
- **text:** `Consolidated markets are ones where McDonald's itself is the franchisor, like the U.S. In licensed markets, local partners generally provide the real estate.`
- **say:** `Consolidated markets are the ones where McDonald's itself is the franchisor, like the US. In developmental licensed markets, local partners generally provide the real estate.`
- **scene:** the countries cast `says` for us: `"Franchisor here"`. No prop or label is needed.

### 8. Opening, line 0 (acceptable, optional upgrade)
"McDonald's made more from rent than from selling its own food." is true (2025: $10.44B of rent against $9.69B of company-operated sales) and specific. At 11 words it takes about 3 seconds to say. A slightly tighter version that dates itself:
- **text/say:** `McDonald's collected more rent than it sold in food.` (9 words). Leave the scene as it is, since it already shows 2025 and $10.4B.

### 9. Minor narration nit (optional)
- Line 38: "about three point seven one billion dollars" reads awkwardly. Better: `rose four point three percent, to three point seven one billion dollars that quarter.` (drop "about", because the screen shows $3.71B exactly).

## Other checks
- **Time words:** "September 2026", "Sept. 23, 2026" and "by September 2026" are all dated, so they stay true. No "this week", "today", "recently" or "next month" appears. The only staleness risk is the Q2 framing (issue 4).
- **Advice and price predictions:** none. Line 5 says it is education, not advice. Line 74 frames the $100K as the company's estimate. No stock price targets. The 24/7 Wall St note about the stock falling is not in the script, which is fine.
- **Political opinion:** none.
- **Generalization:** line 72 ("A franchisor that only collects royalties has no rent to cut") is true by definition, and McDonald's numbers are not extended to the whole industry.
- **Cover and title:** "Rent Beat The Burgers." / $10.4B (2025) is paid off in lines 1-2 and 86. The title "real estate empire" is paid off in chapter 4. The post, IG, TikTok and yt_desc numbers all match the verified figures ($10.4B, $9.7B, $26.9B, 84.2%, 14.7%, 56%/80%, $8.5B, Sept 23 2026). Optional: if line 17 changes, yt_desc needs no edit.
- **Hypothetical example:** labeled (lines 40, 43, 80) and its assumptions are reasonable (2024 average sales of $4.0M; 5% royalty, which applies to new US restaurants; 10% rent assumed).
- **Counts after the fixes:** still 91 lines. Spoken words go to about 1,722, which stays within 1550-1800.

## Sources (via search excerpts)
- McDonald's FY2025 10-K (sec.gov mcd-20251231): revenue table, margins, PP&E, land/building ownership, 45,356 restaurants, $139.4B systemwide sales
- McDonald's FY2020, FY2022 and FY2024 10-Ks: rent series
- McDonald's Q2 2026 release (Aug 4, 2026); Zacks/Yahoo; TradingView
- CNBC, Quartz, Restaurant Dive, CP24/AP and Fortune coverage of the Sept 23, 2026 Investor Day; TipRanks/The Fly and Quartr (unit growth)
- Franchise Chatter (2025 FDD Item 19); Restaurant Dive (5% royalty); Restaurant Business (delivery economics)
- Harry J. Sonneborn bio (Wikipedia, via excerpt); History of McDonald's; TIME (2015) and TheStreet excerpts (1957 and 1960 counts); Investing.com (Q3 2026 report date)

## Summary
The financial core of the script is accurate to the decimal. FAIL because of one unsupported historical number (line 17, the 31 restaurants in 1957), one misstated plan detail (line 70, $800K "per US restaurant"), an inconsistently reported growth target shown as "4.5%+", spoken and on-screen values that disagree (line 51, and to a lesser degree lines 2 and 30), and Q2-based lines that need dating before Q3 results come out ahead of the November 24 post. All fixes are listed above and are small.

VERDICT: FAIL

## Round 2

I re-read the full raw.json. It now has 91 lines and 1,723 spoken words, both within target.

**Fix verification**
- **Issue 1, line 17:** now a stat showing "228" restaurants in 1960, with the sub "From one Kroc store in 1955". The text and narration say "By 1960, there were 228". Verified. The 31-in-1957 claim is gone.
- **Issue 2, lines 69-70:** the list item is "$800K/drive-thru" (16 characters, within the 18-character limit). Line 70's text and narration say "for a traditional U.S. drive-thru (restaurant)", which matches the sourced wording. The items arrays on lines 69 and 70 are identical, so the keep chain holds. Verified.
- **Issue 3, lines 75-76:** the narration now says "about 4.5%". The sub reads "2027 goal: ~4.5% net growth" and the hook value is "~4.5%". These are consistent and hold whether the target is "over", "about" or "nearly" 4.5%.
- **Issue 4, lines 37 and 67:** now "April-to-June quarter of 2026" and "slow in spring 2026". Each Q2 2026 figure is tied to its quarter, so these lines stay true after Q3 results come out on Oct 22 (or Nov 4).
- **Issue 5:**
  - Line 51 shows "91%" and the narration says "about ninety-one percent". 13,930 / 15,352 = 90.7%, so verified.
  - Line 2's narration now says "seven hundred fifty-two million", matching $752 million.
  - Line 30's text and narration both say $16.5 billion, and the board keeps the exact breakdown summing to $16,548M.
- **Issue 6, line 20:** "Sonneborn is quoted saying:". The quote wording is unchanged and correct.
- **Issue 7, line 55:** reworded to "where McDonald's itself is the franchisor", and the US cast line says "Franchisor here". The countries scene still has no prop or label.
- **Issue 8:** line 38 drops "about", so "$3.71 billion" matches the screen. Line 0 is unchanged, which is acceptable as noted in round 1.

**New checks**
- **Keep chains:** every keep:true line follows a line with the same template. Line 17 changed from compare to stat, but no line after it uses keep (line 18 is a fresh timeline), so no chain breaks.
- **Layout:** all compare values are 7 characters or fewer, no list item is longer than 18 characters, and the countries scene has no prop or label.
- **yt_desc chapters:** the timestamps (0:35, 2:08, 3:56, 5:29, 6:48, 9:01) match each chapter's cumulative word position at a steady pace of about 180 words per minute. They are internally consistent and in order, and the yt_desc facts are unchanged and verified. Recheck them against the rendered audio if the voice pace differs.
- **Unchanged items:** cover, title and post text are as before and paid off. There are no new time words, advice, price predictions or political content.

There are no remaining issues.

VERDICT: PASS
