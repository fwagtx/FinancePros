# Fact-check: 2026-10-10-explainer (posts Oct 10, 2026)
Checked Sept 30, 2026. Script JSON only.

## Verified
- L2/L3/cover: 10-yr Treasury 5.18% on Sept 24, 2026 is confirmed as the Treasury daily par yield curve close (+7 bp on the day; market close was about 5.16%, and the intraday high later ran to about 5.27%). "Highest since 2007" is confirmed by CNBC, Semafor and Yahoo, so "near a two-decade high" (19 years) holds up.
- L1 scene/L3: Freddie Mac PMMS 30-yr 7.03% for Sept 24, 2026 is confirmed (up from 6.95%; 15-yr 6.42%). The Freddie Mac release, GlobeNewswire and Fox Business all report it.
- L6 chart: the spread series matches HousingWire's annual averages: 2021 1.52, 2022 2.43, 2023 2.85, 2024 2.53, 2025 2.29, 2026 YTD 1.98. Other trackers show slightly different values (for example Wolf Street 2022 2.39, 2024 2.51, 2025 2.30, 2026 YTD 1.96). The differences come from method and are not errors, and the sources line cites HousingWire.
- L7 math (python): $300k, 360 months. 7.03% gives $2,001.96, which rounds to $2,002. 8.03% gives $2,207.57, which rounds to $2,208. Correct. The case is labeled "Example".
- yt_desc gap: 7.03 - 5.18 = 1.85. Correct.
- On-screen values match the spoken ones on every line.

## Issues
1. STALENESS (cover + L1 scene), should fix. The cover shows "10-yr 5.18%" and the hook scene shows "30-yr 7.03%" with no date. By Oct 10, the Oct 1 and Oct 8 PMMS releases will be out, and the 10-yr has already moved (5.27% intraday after Sept 24). Viewers would take these as today's numbers. Fix: add sub "Sept 24" to the cover and to the L1 scene, or refresh both with the Oct 8 PMMS and the Oct 8/9 10-yr close before posting. L2, L3 and the post text already carry the date, so the body is fine.
2. L3 "that day" (minor accuracy). PMMS is a weekly survey average released Sept 24, not a single-day rate. Fix: "Freddie Mac's average 30-year rate that week? 7.03%."
3. Post sources list "Fannie Mae", but no Fannie Mae figure appears. Fix: remove it.
4. Read-aloud (minor): L2 say "September twenty-fourth, twenty twenty-six" is clunky. Drop the year when speaking ("on September twenty-fourth"). L6 "two point eight five points" is fine but could be "almost three points".
5. Hook (L1): true, specific and short (about 3s). Acceptable. It could be sharper, e.g. "The Fed doesn't set your mortgage rate. This number does."

No advice, predictions, political opinion, quotes or allegations. No instruction-style takeaways. The title and cover are paid off by L2 and L8.

VERDICT: PASS
