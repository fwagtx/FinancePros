# Fact-check: 2027-01-25-lf-explained (Gold, explained)

Checked by an independent checker on Nov 26, 2026 for posting on Jan 25, 2027. I used WebSearch only; WebFetch to gold.org and visualcapitalist.com was blocked by the network. Fixes are applied in the raw JSON, and check.py passes: 92 lines, 1,753 spoken words, 12-word hook.

## Verified (two or more reputable sources, or an official source)
- 53 record highs in 2025 (WGC FY2025). Record about $5,590 in late Jan 2026 (CBS: $5,589.38 on Jan 28; Reuters: $5,594.82).
- Nov 18, 2026 low near $3,720 (Nation Thailand $3,719.55; Reuters intraday range about $3,667-$3,773, lowest since Sept 2025; Khaleej Times/NST: 14-month low on Fed hike bets). A drop of about a third: 1 - 3,720/5,590 = 33.5%.
- WGC: 675t Jan-Sep 2026; Q3 2026 321t, +42% y/y; 120t reported, so 201/321 = 63% unreported (WGC page, Kitco, Money Metals). Total demand 2025 5,002t worth $555bn; ETFs 801t; bars and coins 1,374t; jewelry $172bn record with volume at a five-year low of 1,542t; central banks 863t (2024 1,092.4t in the FY2025 table); 2010-2021 average 473t; 2020 255t (decade low); 2021 463t; 2022 1,082t (revised).
- China bars and coins +28%, India +17%; jewelry China -25%, India -24% (WGC FY2025 and JewelleryNet).
- WGC June 2026 survey: a record 45% plan to add gold (Kitco, WGC press release).
- 2025 average $3,431, +44% (LBMA, WGC). 2025 gain about 65%, best since 1979 (Trading Economics, ABC/AP). DXY -9.4% (Barchart 9.37%), worst since 2017 (Bloomberg, NPR). Three Fed cuts in 2025.
- Bloomberg, Sept 11, 2025: gold topped its inflation-adjusted 1980 peak of $850 (Jan 21, 1980 London fix). 24x = 850/35. It took about 28 years to regain $850 (Jan 2008).
- Chart annual averages (LBMA): 36, 161, 615, 317, 383, 384, 279, 444, 1,225, 1,160, 1,770, 3,431, all consistent. 2012 $1,669 to 2015 $1,160 = -30.5%. 2008 +25.4%, 2020 +27.1%.
- History: Gold Reserve Act 1934 ($20.67 to $35); Bretton Woods 1944; the Nixon quote of Aug 15, 1971 is exact; floating by 1973; Washington Agreement Sept 26, 1999 (400t a year cap); 2011 peak about $1,921 intraday.
- US 8,133t and Germany 3,350t (IMF/WGC). GLD 0.40% and GLDM 0.10% (State Street, Motley Fool).
- Fee math: 10,000 x (1 - 0.996^10) = $392.7, about $393; 10,000 x (1 - 0.999^10) = $99.6, about $100; gap $293.

## Issues found and fixed
1. Line 0, weak hook. It stated two facts and asked nothing. New version: "Gold pays zero. Why did central banks buy 863 tonnes?" It is 12 words, opens with the paradox as a question, and speaks the 0% and 863t on screen. Line 1 now reads "That was in 2025...".
2. Line 40, stale. The 14-month China streak "through December 2025" is out of date. The PBOC/SAFE data from Nov 7, 2026 show 24 straight months through October 2026 (China Daily HK, GKToday, BraveNewCoin). Label changed to "24 months".
3. Line 42, mixed vintage. China's 2,313t was a Q1 2026 figure placed next to end-2025 figures for the US and Germany. Changed to China reporting about 2,306t at the end of 2025 (WGC China update, PBOC). Caption changed to "Official gold, end-2025".
4. Lines 68-70 and 87, single-source 5.1% Eagle premium. Trackers disagree: the lowest-dealer average for Nov 2026 was 2.86%, and guides say 3-8%. Line 68 now says premiums vary, often about 3% to 8% (stat "3% to 8%"). The worked example is now a hypothetical 5%: $3,720 x 5% = $186, coin about $3,906, and a 5% rise to break even. The recap at line 87 says 5%.
5. Line 62, single-source "19-month dollar high". Softened to "a strong dollar added to the pressure."
6. Line 61, news source date. Changed to "Reuters, Nov 2026" because the exact Nov 16 Reuters item was not confirmed.
7. Line 25, date of the 1999 low. Sources put it in July 1999 ($252.80) or August 1999 ($251.70). Changed to "mid-1999", with sub "mid-1999, London".
8. Line 22, unverifiable superlative. "One of the longest slumps of any big asset" changed to "a slump that lasted about 20 years".
9. Lines 35-38, chart revision. WGC revised 2023 from 1,037t to 1,050.8t, so the point is now 1,051 (not spoken). Caveat: WGC revises this series often, and I could not open the full FY2025 table, so the 2020-2022 points come from earlier WGC vintages. They are close and all labeled as WGC data.
10. Lines 36 and 47, text did not match say. The text was missing "during the pandemic" and "to a five-year low". Text now matches say.
11. Line 39, time word. "Hasn't stopped" changed to "didn't stop", because the newest data is Q3 2026 and the Q4 2026 WGC report comes out after the posting date.
12. Post yt_desc sources. Replaced "dealer premium survey (Nov 3, 2026)" with the premium trackers and added the PBOC/SAFE data and the Nov 2026 Reuters-syndicated reports.

## Other checks
- Every latest price is dated (Nov 18, 2026 and Jan-Nov 2026), and nothing reads as a current price. The video makes no predictions and gives no buy/sell advice (lines 7 and 90 say so). It contains no political opinion.
- The cover "Zero Yield. Why?" and the title are paid off by chapters 3-4. On-screen values match the spoken ones. The last line is unchanged.
- Minor point, left as is: "$35 in 1971" is the official price, and the free-market price was a little higher.

VERDICT: PASS

## Round 2 (editor)
Reviewed applied fixes (hook question, dated prices, China streak/holdings, coin premium range); limits pass.
VERDICT: PASS
