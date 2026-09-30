# Fact-check: 2026-10-04-explainer (Index Funds vs Picking Stocks)

Checked on September 30, 2026 for posting on October 04, 2026. Line numbers are line numbers in `2026-10-04-explainer.raw.json`. I did not read the research brief.

## Verified claims (no change needed)

| JSON line(s) | Claim | Result | Source |
|---|---|---|---|
| 5-8, 13-20, 26-33 | 79% of active large-cap US funds trailed the S&P 500 in 2025 | TRUE. SPIVA says it was the 4th-worst year in 25 years of SPIVA data. | S&P DJI, SPIVA U.S. Year-End 2025 (spglobal.com/spdji/en/spiva/article/spiva-us); InvestmentNews, "Active managers stumble again in 2025" |
| 53-78 | Chart points: 2021 85%, 2022 51%, 2023 60%, 2024 65%, 2025 79% | TRUE. All five match SPIVA year-end scorecards. | SPIVA U.S. Year-End 2024 PDF; SPIVA U.S. Year-End 2025 |
| 50-51 | "Most pros lost every year from 2021 to 2025" | TRUE. Every value is above 50%. The 2022 value of 51% is only just a majority. | same |
| 85-90 | H1 2026: 67% trailed, while conditions favored pickers | TRUE. SPIVA Mid-Year 2026 reports 67%. It calls the conditions "about as favorable for stock pickers as they get": the highest dispersion since 2008, wider breadth, and the Mag 7 weight falling from 34.9% to 31.6%. The report came out in September 2026, so the news is not stale. | SPIVA U.S. Mid-Year 2026; ETF Trends; TKer |
| 96-111, 167 | 2025 average expense ratio: 0.64% active vs 0.05% index | TRUE (ICI, asset-weighted, equity mutual funds) | ICI, Trends in the Expenses and Fees of Funds, 2025 (ici.org/files/2026/per32-01.pdf); ICI news release, "Mutual Fund and ETF Fees Remained Near Historic Lows in 2025" |
| 96-111 | Math: $10,000 x 0.64% = $64; $10,000 x 0.05% = $5 | CORRECT | arithmetic |
| 165-167 | Post text numbers (79, 85/51/60/65/79, 67, $64 vs $5, 0.64% vs 0.05%) | All match the script and the sources | as above |

## Issues found

1. **Opening hook, line 14 (minor, optional):** "Seventy-nine percent of pro stock pickers lost to a lazy index." The line is true and specific, and it takes about 3 seconds to say, so it passes. It does not say when, which makes it a little weaker, and the year only arrives in line 27. Fix: "In 2025, seventy-nine percent of pro stock pickers lost to a lazy index." A stronger alternative adds a curiosity gap: "Seventy-nine percent of pro stock pickers just lost to a fund that doesn't even pick."

2. **Scope wording, lines 96-97 and 167 (minor accuracy nuance):** The ICI figures of 0.64% and 0.05% are for actively managed equity *mutual funds* and index equity *mutual funds*. They do not cover all active or index funds, and ETFs are excluded. Line 96 says "active funds" while line 97 says "active stock funds", so the caption and narration also differ slightly. Fix: set line 96 to "...about $64 for active stock funds versus $5 for index stock funds." Optionally change line 100 to "Yearly fee on $10,000 (2025, stock mutual funds)" and change `yt_desc` (line 167) to "active stock mutual funds averaged 0.64%... versus 0.05% for index stock mutual funds (ICI)". The numbers themselves are correct.

3. **Awkward narration, lines 118-119 (style nit):** "Squirrel pays the acorn guide..." reads as broken English out loud. That may be the character's voice, since line 154 uses the same pattern, but here the metaphor is also unclear. Fix: "The squirrel pays its acorn guide every year, whether the hunt works or not." Make the caption on line 118 match.

4. **Support for an extra claim, line 143 (minor):** The narration adds "and the odds aren't great". This is supported by SPIVA's U.S. Persistence Scorecard (Year-End 2025), which shows that few top-quartile funds stay top-quartile, so it can stay. Optionally put that source in the post text.

5. **Cover and title payoff, lines 5 and 164 (OK):** "Why 79% of Pros Lost" is paid off by lines 26, 96 and 142, which explain it through fees and how hard it is to pick winners ahead of time. No change needed.

## Other checks

- **On-screen vs spoken values:** all match: 79%, 85/51/60/65/79, 67%, $64/$5, 0.64%/0.05%.
- **Time words:** "2025", "first half of 2026" and "Early 2026" (line 89) will all still be correct on October 04, 2026. Nothing says "this week" or "yesterday".
- **Stale news:** none. Mid-Year 2026 is the latest SPIVA U.S. report.
- **Advice or price predictions:** none. The script tells no one to buy or sell anything, and the CTA carries the "Education, not financial advice." disclaimer.
- **Political opinion:** none.
- **Math errors:** none.

No wrong facts, no mismatched numbers and no advice. The issues above are optional polish.

VERDICT: PASS
