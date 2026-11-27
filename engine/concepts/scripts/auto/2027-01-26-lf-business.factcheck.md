# Fact-check: How Anheuser-Busch InBev makes money (posts Jan 26, 2027)

Sources checked: AB InBev FY2025 results release (Feb 12, 2026, via FinancialContent/Business Wire mirror), FY2017, FY2019, FY2023 results and 2Q23 release (SEC 6-K), FY2016 20-F, Bloomberg/Food Dive (Jan 6, 2026), CNN/ABC/Fox citing Circana (Sept 2025), ABC/Boston.com (June 2023).

## Verified (no change needed)
- FY2025: revenue $59.32B; volume 561.1M hl, -2.3% (beer -2.6%); normalized EBITDA $21.223B, +4.9% organic; margin 35.8%; revenue/hl +4.4%; above-core 35% of revenue; Corona outside Mexico +8.3%, double-digit volume growth in 30 markets; no-alcohol beer revenue +34% (global; the "high-twenties" figure is US-only, so +34% kept); Beyond Beer 3% of revenue; Brazil revenue/hl +5.4%; FCF $11.3B; $6B buyback announced Oct 30, 2025; FY25 dividend EUR 1.15 (0.15 interim + 1.00 final); net debt $60.9B; 20 billion-dollar brands; Corona and Budweiser #1/#2 (Kantar BrandZ).
- Per-can math: 56.11B L / 0.355 L = ~158B; $59.32B / 561.1M hl = $105.7/hl; /281.8 cans = 37.5c (~38c); EBITDA $37.8/hl = 13.4c (~13c). 1 hl = 281.8 cans (~282). Correct.
- Q4 2025 regions: Middle Americas $2,508M EBITDA / $4,927M revenue = 50.9%; North America $906M / $3,235M = 28.0%; South America $1,321M / $3,645M = 36.2%. Correct.
- History: 2015 net debt $42.2B -> $108.0B end 2016; SABMiller GBP 45/share, ~GBP 79B, closed Oct 2016; 2008 A-B deal $70/share, ~$52B; 2020 sale of 49.9% can-plant stake to Apollo-led group (~$3B), buyback announced Jan 6, 2026, closed Jan 30, 2026 (~$2.9B, "about $3 billion" OK); Constellation US Corona rights since 2013; 2018 dividend halved.
- Chart (net debt/EBITDA): 2015 2.51x, 2016 5.5x (amended basis), 2017 4.8x, 2018 4.6x, 2019 4.0x (PRO FORMA for the Australia sale), 2020 4.8x, 2021 3.96x, 2022 3.51x, 2023 3.38x, 2024 2.89x, 2025 2.87x. All points match; x-axis is annual and evenly spaced.
- 2023: Bud Light lost No.1 to Modelo in May 2023 sales data; FY23 US revenue -9.5%; 2Q23 US EBITDA -28.2%; FY23 group revenue +7.8% to $59.4B.
- Michelob Ultra No.1 by volume YTD (Circana, Sept 2025), Modelo still No.1 by dollars. US aluminum tariff raised to 50% on June 4, 2025.
- No buy/sell advice or price predictions; line 82 explicitly declines to predict. Bud Light segment stays neutral business framing. Last line unchanged.

## Issues found and fixed (applied to raw.json via build_abi.py)
1. Line 0 (hook) inaccurate: "pours about 158 billion cans" - AB InBev also sells bottles and kegs; 158B is a can-equivalent. Now TEXT "One brewer sells 158 billion cans' worth a year." / SAY "One brewer sells one hundred fifty-eight billion cans' worth a year." (11 words, ~3.5 s at normal pace). Hook is true, specific, and line 2 sets up the question it pays off. Post title changed to "...158 Billion Cans' Worth a Year".
2. Line 68 WRONG NUMBER: FY2023 US sales-to-retailers fell 11.9% (12.7% was sales-to-wholesalers). Now "dropped 11.9%" / "eleven point nine percent"; compare value "-11.9%".
3. Line 69: "-28%+" / "more than 28%" made exact: "fell 28.2%", value "-28.2%".
4. Line 70: "a record $59.4 billion" is out of date (FY2024 revenue $59.8B was higher). Now "$59.4 billion, a record at the time"; sub "Up 7.8%".
5. Line 42: list said "Five regions" but showed four items ("EMEA and Asia Pacific" combined) and narration named only some. Now five items, all spoken.
6. Line 46: Mexico "about 58%" share from 2016 20-F could not be pinned to the stated year (filing language refers to 2015) and is 10 years stale. Replaced with "In Mexico it's the biggest brewer by a wide margin, and that kind of scale pays."
7. Line 55: 2019 4.0x is pro forma for the pending Australia sale; added "counting a pending sale".
8. Line 59: "By our math, around $61 billion" - net debt is reported ($60.9B); now "on about $61 billion of net debt".
9. Line 61 (stale on posting date): "counting a proposed final payment" - the final dividend went to the April 29, 2026 AGM; clause removed.
10. Line 66: news source "Fortune, May 31, 2023" could not be found; changed to "ABC News, June 2023" (Bud Light/Modelo coverage dated June 14, 2023). Post sources updated likewise.
11. Line 75: "mid-2025" dated precisely as "June 2025" (text, say, sub).
12. Line 79: "Michelob Ultra Zero leads it in the US" unverified; release says it was a top-2 beer innovation of FY25. Now "in the US, Michelob Ultra Zero was a top new beer of 2025."
13. Post description: replaced unverified Fortune and no-longer-cited 2016 20-F with AB InBev 2Q23 results and 2023 annual report.

## Notes (no change)
- Line 4 "+4.9%" is organic growth (reported EBITDA +1.3%); the on-screen sub says "Organic growth", acceptable.
- "2025" as latest full year is still correct on Jan 26, 2027 (FY2026 results due ~Feb 2027).
- Line 89 "A good chunk of what you pay for a premium label is the label" is framing, not advice.
- check.py: OK, 91 lines, 1790 spoken words; all on-screen values spoken; JSON valid.

VERDICT: PASS

## Round 2 (editor)
Reviewed applied fixes (hook accuracy, corrected figures, dated wording); limits pass.
VERDICT: PASS
