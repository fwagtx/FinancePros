# Fact-check: 2026-12-01-lf-business ("How airlines make money from credit cards, not flights")

Checker: independent. Checked on Oct 2, 2026 for posting on Tue Dec 1, 2026. I checked all 98 lines (0-96 plus the CTA), the cover, the header and the post. I did not read the research.md. Line numbers are 0-based indexes into `lines[]`.

## Verified (no change needed)
- **Amex payments to Delta.** 2018 $3.4B (CNBC/Bloomberg, Apr 2, 2019). 2020 $2.9B, down 30%. 2021 $4.0B, which was "98% restored" vs 2019, so 2019 was about $4.1B (Delta Q4 2021 release). 2022 about $5.5B and 2023 $6.8B (+22%) (Delta Q4 2023 release). 2024 $7.4B. 2025 $8.2B (+11%) (Delta FY2025 release, Jan 13, 2026). All chart points are correct.
- **Q2 2026 payment:** $2.4B, +16% (Delta, July 10, 2026). **$10B long-term goal:** correct.
- **Partnership dates:** started in 1996. An 11-year renewal was announced Apr 2, 2019 and runs "through the end of 2029". The Amex FY2025 10-K still says the end of 2029, so there has been **no extension since**.
- **Amex FY2025 10-K:** Delta cards were about 13% of worldwide billed business and about 21% of worldwide Card Member loans at Dec 31, 2025. Worldwide billed business was $1,670B. Delta is Amex's largest partner.
- **Delta net income is GAAP throughout.** 2021 $280M, 2022 $1,318M, 2023 $4,609M, 2024 $3,457M, 2025 $5,005M. 2025 GAAP operating revenue was $63.4B. More than 1M new card acquisitions in 2025, the fourth year in a row.
- **United MileagePlus (June 15, 2020 8-K and investor deck):** $5.3B of 2019 sales, about 71% from third-party partners (Chase is the main one). 2019 EBITDA about $1.8B, times 12 gives about $21.9B. The $6.8B financing ($3.8B notes plus a $3.0B term loan) closed July 2, 2020. A market value of "roughly $10B" in mid-2020 is plausible, and "on paper" hedges the comparison.
- **American AAdvantage:** $10B raised in March 2021. A third-party appraisal put the program at $19.5-31.5B (CNBC, Mar 8, 2021). Part of the money prepaid the Treasury CARES loan. 2025: $6.2B cash from co-brand and other partners, and $111M net income (AA, Jan 27, 2026). Citi deal: announced Dec 2024, 10 years, Citi becomes the sole US issuer from 2026. Expected growth is about 10% a year. As payments "approach $10 billion per year", pre-tax income is projected to be about $1.5B above 2024.
- **CFPB/DOT:** joint hearing on May 9, 2024. More than 1,200 rewards complaints in 2023, up more than 70% from pre-pandemic. The four complaint themes match the CFPB spotlight. DOT sent letters to AA, DL, WN and UA on Sept 5, 2024.
- **Buttigieg quote (line 78)** matches the original word for word as an excerpt: "But unlike a traditional savings account, these rewards are controlled by a company that can unilaterally change their value." Line 79 is also correct: he said "These programs bring real value to consumers".
- **Credit Card Competition Act:** reintroduced Jan 13, 2026 by Marshall and Durbin, and Trump endorsed it on Truth Social the same morning. It applies to issuers with more than $100B in assets and requires at least two unaffiliated networks. As of Sept 30, 2026 (Washington Times) it had still not passed.
- **IATA June 2026:** 2026 forecast of $23.0B, a 2.0% margin, $4.50 per passenger. The 2025 figure of $9.10 per passenger is correct. The reasons given (Middle East disruptions, high fuel prices) are correct.
- **Layout:** cover title 27 characters, no 'paper' prop, bare CHAPTERS line present, all keep:true lines share their previous line's template, compare values ≤7, news headlines ≤34, board lines ≤26, timeline fields fit, hook titles ≤22.

## Math (recomputed in Python)
- $8.2B/365 = $22.47M a day, so "about $22.5M" is right.
- $8.2B/8,760 = $936,073 an hour, so "~$936K" is right.
- 13% × $1.67T = $217.1B. $8.2B / $217.1B = 3.78¢ per dollar, so "about 3.8¢" is right. $1,000 of spending gives $37.79, so "~$38" is right. This is a rough estimate and is labeled as one.
- $8.2B / $63.4B = 12.9%, so "about 13%" is right.
- $8.2B − $5.0B = $3.2B. (4.1 − 2.9)/4.1 = 29%, so "30%" is right. 8.2/4.1 = 2.0, so "doubled" is right.
- Breakage hypothetical: 50,000 × $0.01 = $500. 10% of that is 5,000 miles, which is $50. Correct, and labeled as an assumption.
- $100 × 3.9% = $3.90. The arithmetic is right, but the 3.9% input is out of date (Issue 1).
- 2021-2025: Amex payments were above Delta's net income every year, so line 65 is true.
- 1.8 × 12 = 21.6, not 21.9. United's actual 2019 EBITDA was about $1.825B. See Issue 6.

## Issues

1. **(FACT, stale) Lines 58, 59, 95: IATA's 2025 margin of 3.9% has been superseded.** 3.9% ($39.5B, $7.90 per passenger) was IATA's December 2025 estimate. In June 2026 IATA raised its 2025 estimate to **$45B, a 4.2% margin, $9.10 per passenger**. Line 61 already uses the June 2026 figure of $9.10, so the script mixes two vintages. A 3.9% margin goes with $7.90 per passenger, not $9.10. Note that 3.9% was also the *pre-cut 2026 forecast*. Fixes:
   - **Line 58.** text: "IATA's latest estimate, from June 2026, puts the global airline net margin for 2025 at 4.2%." say: "The airline group I A T A's latest estimate, from June twenty twenty-six, puts the global net margin for twenty twenty-five at four point two percent." scene: `{"t":"stat","label":"Global airline net margin","value":"4.2%","tone":"down","sub":"2025, IATA est."}`
   - **Line 59.** text: "On a $100 ticket, that's about $4.20 of profit." say: "On a hundred-dollar ticket, that's about four dollars and twenty cents of profit." scene: `{"t":"board","lines":["$100 ticket x 4.2%","= $4.20 profit"]}`
   - **Line 60.** It says "In June 2026" again, which now repeats line 58. text: "In the same update, citing Middle East disruptions and high fuel prices, IATA cut its 2026 forecast to a 2.0% margin." say: "In the same update, citing Middle East disruptions and high fuel prices, I A T A cut its twenty twenty-six forecast to a two percent margin." The scene stays the same.
   - **Line 95.** text: "Four: flying is thin: about a 4.2% net margin in 2025, by IATA's estimate." say: "Four. Flying is thin: about a four point two percent net margin in twenty twenty-five, by I A T A's estimate." The scene stays the same.

2. **(CONTEXT / FACT) Lines 80-84: the CCCA exempts Amex cards like Delta's, and the script never says so.** The bill exempts three-party networks, where the issuer is also the network, as with Amex. Delta's co-brand is therefore outside the routing mandate. The risk falls mainly on Visa and Mastercard co-brands such as United/Chase and American/Citi. As written, viewers will assume the "$8.2B card deal" is directly threatened. Also, line 84's "$200 million" comes from Forbes (July 23, 2026) **citing Demand Progress, an advocacy group that supports the bill**. It is a cumulative total since 2023 that counts lobbying filings listing the CCCA among other issues. Presenting it unattributed as "spending about $200 million against it" is one-sided, and "As of July 2026" will be stale on Dec 1. Fixes:
   - **Line 84.** text: "Cards on Amex's own network, like Delta's, would be exempt. Visa and Mastercard co-brands, like United's and American's, would not. When this video was made, the bill had not passed." say: "Cards on Amex's own network, like Delta's, would be exempt. Visa and Mastercard co-brands, like United's and American's, would not. When this video was made, the bill had not passed." scene: `{"t":"board","lines":["Amex cards: exempt","Visa/MC co-brands: covered"]}`. Re-check the bill's status before posting.
   - If you want to keep the $200M figure, attribute it: "Forbes, citing the pro-bill group Demand Progress, said industry groups had spent about $200 million opposing it since 2023." Offset the extra words elsewhere.
   - **yt_desc sources:** replace "Forbes (July 23, 2026)" with "Kilpatrick Townsend on the CCCA of 2026 (Jan. 2026)", or keep Forbes only if the attribution above is used.

3. **(LAYOUT) Split items over 16 characters.**
   - **Line 17**, left item "Booked on the trip" (18): change to "Booked when used" (16).
   - **Line 83**, right items "Less reward money" (17) and "Card deals at risk" (18): change to "Smaller rewards" (15) and "Card deals hit" (14).
   - **Line 83 say/text** (optional neutral tidy): "Supporters, including big retailers, say it would cut swipe fees. Opponents, including banks and airlines, say it could shrink the money that pays for rewards."

4. **(FRAMING / OPENING) Lines 0-2 compare gross card revenue to net profit with no caveat.** The $8.2B is revenue, and much of it covers miles, seats and perks that Delta still has to provide. It is not profit. The opening is true, specific, and under 3 seconds, so it passes the hook test. It could be stronger and plainer. Fixes:
   - **Line 0** (stronger, 9 words, about 2.7 seconds). text: "Amex paid Delta more than Delta earned all year." say: "Amex paid Delta more than Delta earned all year." The scene stays the same; label "2025" gives the year.
   - **Line 2** (adds the caveat). text: "That's revenue, not profit, so not apples to apples. But the gap is $3.2 billion, and it's not just Delta." say: "That's revenue, not profit, so not apples to apples. But the gap is three point two billion dollars, and it's not just Delta." The scene stays the same.

5. **(STALE / TIME WORDS) Line 68 uses future tense for something already done.** The Barclays-to-Citi move finished in April 2026. text: "As part of the switch, Barclays AAdvantage cardholders were moved over to Citi in April 2026." say: "As part of the switch, Barclays Advantage cardholders were moved over to Citi in April twenty twenty-six." scene: `{"t":"board","lines":["Barclays AA cards","moved to Citi, 2026"]}`

6. **(MATH ON SCREEN) Line 48.** The board shows "~$1.8B x 12 = $21.9B", but 1.8×12 = 21.6. The real figure was about $1.825B. Reading "E B I T D A" letter by letter is also awkward out loud. text: "United took the program's 2019 EBITDA, just over $1.8 billion, and multiplied it by 12." say: "United took the program's twenty nineteen earnings before interest, taxes and depreciation, just over one point eight billion dollars, and multiplied them by twelve." scene: `{"t":"board","lines":["EBITDA: just over $1.8B","x 12 = about $21.9B"]}`

7. **(UNSOURCED TIMING) Line 69.** American projects about 10% a year growth and pre-tax upside "as remuneration approaches $10 billion per year". The company did not commit to "by the end of the decade". text: "American expects its partner cash to grow about 10% a year, toward roughly $10 billion a year." say: "American expects its partner cash to grow about ten percent a year, toward roughly ten billion dollars a year." scene sub: "By decade's end" becomes "Company target".

8. **(STALE NEWS, minor) Line 40.** Q2 2026 ($2.4B, +16%) is correct, but Delta reports Q3 2026 around mid-October, before the posting date. By Dec 1 this will no longer be the latest quarter. Recommendation: refresh with the July-September 2026 figure once Delta releases it, and update the news source to "Delta Q3 2026 results, Oct. 2026". If you don't refresh it, the line is still accurate as written.

9. **(Minor) Line 53, sub "2021 filing".** The $19.5-31.5B appraisal was first disclosed in 2020 for the CARES loan and repeated in the 2021 offering. Suggest sub "Third-party est." on both sides. Not required.

10. **(Minor) Line 55.** The hook shows "2020 / $2.9B", which is Delta's Amex figure, in a section about United and American lenders. It could confuse viewers. Suggest label "Amex→Delta 2020" or keep it as is. Not required.

## Checks with no problems
- No advice, no price predictions, and AA's projection is labeled as one (line 70).
- The political framing is balanced, with the Trump endorsement stated as fact.
- Allegations are attributed (merchants argue, critics call it devaluation).
- No line generalizes one company's numbers to the whole industry.
- The cover, title and header are paid off by lines 1, 93 and the whole video.

## Word count
The original has 1,793 spoken words. Fixes 1-7 bring it to about 1,799, inside 1,550-1,800.

VERDICT: FAIL
