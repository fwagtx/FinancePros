# Fact-check: 2026-12-21-lf-explained ("How to build wealth on a normal salary: the math")

Checked: Thursday, Oct 22, 2026. Posts: Monday, Dec 21, 2026. Line numbers are **0-based indices into `lines`**.
Script: 93 lines, 1791 spoken words (allowed range 1550-1800).

## 1. Worked-example math (all recomputed in Python, FV = P((1+r)^n - 1)/r, r = 0.07)

| Line(s) | Claim | Recomputed | OK |
|---|---|---|---|
| 1, 2, 34, 35, cover | Saver A, $6k/yr ages 25-35 then held to 65 | 82,898.69 x 1.07^30 = **$631,046** | yes |
| 1, 2, 17, 29, 30, 34 | $6k/yr x 30 yrs | **$566,765** ($567K) | yes |
| 17, 18, 86 | $9k/yr x 30 yrs; difference | **$850,147**; diff **$283,382** | yes |
| 19 | Extra deposits 30 x $3,000 | $90,000 | yes |
| 29, 30 | $6k/yr x 40 yrs | **$1,197,811** ($1.2M); "more than double" = 2.11x | yes |
| 31 | Extra deposits | $240k - $180k = $60,000 | yes |
| 90 | $9k/yr x 40 yrs | **$1,796,716** ($1.8M) | yes |
| 5 | $1,251 x 52 | $65,052 | yes |
| 25, 26 | 1.07^10; 72/7 | 1.967; 10.3 | yes |
| 27 | 1.07^30; 1.07^40 | 7.612; 14.974 | yes |
| 36 | "30 extra years = about 3 doublings" | 1.07^30 = 7.6 = 2.9 doublings | yes |
| 42 | 50% match on 6% of $60k | $3,600 in, $1,800 match | yes |
| 44 | $1,800/yr x 30 | **$170,029** | yes |
| 45 | $7,800/yr x 30 | **$736,794** | yes |
| 49, 50, 88 | $9k/yr x 30 at 6.95% vs 6.00% | **$842,537** vs **$711,524**; gap **$131,014** | yes |
| 59 | $5,000 x 22.36% | **$1,118.00** | yes |
| 65 | 3% of $60k | $1,800; $61,800 | yes |
| 66 | $900/yr x 30 | **$85,015** | yes |
| 68 | Half of each of five compounding 3% raises saved | salary $69,556, saved $10,778, so **15.50%** | yes |
| 81 | 2000-2009 compound annual rate from the chart's own points | **-0.95%** | yes |

**Fee convention (lines 49-50):** the script subtracts the fee from the return (7% - 1% = 6%; 7% - 0.05% = 6.95%) and shows that on screen ("Grows 6% a year" / "Grows 6.95% a year"), so the convention is stated. This is the usual simplification. A strict multiplicative drag (1.07 x (1 - fee) - 1) gives $702,818 vs $842,008, a gap of about $139K. "About $131,000" is defensible as stated. No change needed.

**Assumptions stated:** 7% is called an assumed return after inflation, "not a promise", at lines 2, 15, 16, 44, 66, 77, 82 and 90, and in the description. The match (42), fee (49) and raise (65-68) examples all give their inputs. Every example is hypothetical and labeled ("Our example", "Example:"). OK.

## 2. Facts verified

| Line | Claim | Source check | Status |
|---|---|---|---|
| 4 | Median full-time weekly pay was $1,251 in Q2 2026 | BLS Usual Weekly Earnings release, July 21, 2026: $1,251, not seasonally adjusted | OK |
| 11 | Saving rate was 4.1% in Aug 2026 | BEA Personal Income and Outlays, August 2026 (released Sept 30, 2026): 4.1% | OK, but see staleness |
| 12 | Vanguard: average deferral 7.6%, total 12.1% in 2025 | How America Saves 2026: average deferral 7.6%, average total rate 12.1% | OK |
| 40 | 96% of Vanguard plans made an employer contribution in 2025 | HAS 2026 table: 96% for 2024, and 96%* for 2025 (*the 2025 figure is an estimate) | OK; optional fix below |
| 54-55 | Fed SHED 2025: 63% would cover $400 with cash or equivalent | SHED 2025 (released May 2026): 63%, unchanged | OK |
| 58, 60 | Card accounts assessed interest averaged 22.36% in Aug 2026 (G.19) | G.19 released Oct 7, 2026 for Aug 2026: 22.36%. Next quarterly reading (Nov) comes out in early Jan 2027, so this is still the latest on Dec 21 | OK |
| 72-73 | 2026 limits: 401(k) $24,500, IRA $7,500, 50+ catch-up $8,000 | IRS IR-2025-111 / Notice 2025-67 (Nov 13, 2025) | OK |
| 74 | Limits are adjusted for inflation; 2027 limits | **The IRS has NOT announced 2027 limits as of Oct 22, 2026.** Only projections exist (Milliman: $25,500 401(k), $8,500 catch-up). An announcement is expected around early to mid-November, before air date | See fix |
| 51 | ICI: average equity mutual fund expense ratio 0.40% in 2024, down sharply since the 1990s | ICI Trends in Expenses and Fees 2024 (Mar 2025): 0.40% asset-weighted, down 62% since 1996 | OK |
| 78 | S&P 500 1928-2025 returned ~10% a year nominal, ~7% real (Damodaran) | Damodaran compound average ~9.9-10% nominal, ~6.9-7% real. The arithmetic average is higher (~11.8%), so these are compound figures | OK; optional wording |
| 79-80 | Chart of yearly total returns 2000-2025 | Spot-checked 2000 -9.10, 2002 -22.10, 2008 -37.00, 2009 26.46, 2013 32.39, 2018 -4.38, 2022 -18.11, 2024 25.02 and 2025 17.88 (YCharts/S&P). All match the standard Damodaran/S&P series | OK |
| 80 | 2008 -37%; 2022 about -18%; 2025 about +18% | Matches | OK |
| 81 | 2000-2009 averaged about -1% (lost decade) | Dimensional "A Tale of Two Decades": -0.95% annualized. Recomputed from the chart points: -0.95% | OK |

Other checks:
- **Advice and products:** no fund, ticker, provider or product is named or recommended. Line 7 has an "education, not financial advice" disclaimer. Lines 61 and 84 describe the math and give no instructions. OK.
- **Politics, allegations, quotes:** none.
- **keep:true:** lines 2, 18, 28, 30, 35, 50, 80 and 87-89 all follow a line with the same template. OK.
- **Field limits:** every stat label/sub/value, compare value/sub, board line, list/split item, chart end label (`+17.9%`), hook title, post.title (81 characters) and tiktok (96 characters) is within its limit. Compare value `22.36%` is 6 characters (limit 7). OK.
- **On-screen vs spoken:** line 58 shows 22.36% and says "about twenty-two percent". This is rounding, not a conflict. OK.

## 3. Issues and fixes (exact replacement text, 0-based line index)

### Issue A: the hook is misleading without the start-date condition (lines 0, cover, post). Must fix.
"Saving for ten years can beat saving for thirty years" is only true when the ten years come first (25-35 vs 35-65). Heard alone, it suggests saving less is better in general. The hook should carry the condition. The fix below is 12 spoken words, still under about 3 seconds, and stays specific.

- **Line 0 `say`:** `Ten years of saving at twenty-five can beat thirty years at thirty-five.` (12 words, replacing 10; total becomes **1793**, within range)
- **Line 0 `text`:** `10 years of saving at 25 can beat 30 years at 35.`
- Line 0 `scene.title` (`[10] years beats 30`) can stay: the label "25-35" is on screen.
- **cover.title:** `10 Early Years Beat 30.` (fits 22)
- **post.title:** `Saving for 10 years early can beat saving for 30 years later: the math on a normal salary` (89 characters, limit 90)
- **post.ig:** `Save for 10 years from 25 and you can beat 30 years from 35. Here's the math on a normal salary.`
- **post.tiktok:** `Save for 10 years from 25 and you can beat 30 years from 35. The real math of building wealth on a normal salary.` (113 characters, limit 150)
- **post.yt_desc** first sentence: `Saving for 10 years starting at 25 can beat saving for 30 years starting at 35, and this video shows the exact math.`

### Issue B: line 74 and 2027 IRS limits (staleness risk on Dec 21). Must re-check before air.
The 2027 limits are **not confirmed today**, so I cannot give confirmed numbers. They are expected in November, and by Dec 21 a video that calls 2027 "worth checking" will look out of date. The current line is also mildly instruction-style.
- **Now, safe either way (24 words, -1):**
  - `say`: `The I R S adjusts these limits for inflation most years, and it posts each new year's figures at I R S dot gov.`
  - `text`: `The IRS adjusts these limits for inflation most years, and posts each new year's figures at IRS.gov.`
- **Once the IRS notice is out (expected about mid-November), replace line 74** with the official numbers, using this template: `say`: `The I R S has already set the twenty twenty-seven limits: [N] for a 401(k), and [M] for an I R A.` / `text`: `For 2027, the IRS has set the 401(k) limit at $[N] and the IRA limit at $[M].` / board lines: `2027: $[N] 401(k)`, `$[M] IRA`. Only use this with the figures from the IRS release, not projections (Milliman projects $25,500 for the 401(k); IRA projections range from $7,500 to $8,000).

### Issue C (minor): line 11, BEA saving rate staleness
On Dec 21 the September and October 2026 saving rates will be out, since BEA's October report is due in late November or early December. The line is dated ("August 2026") and stays true, but it is no longer the latest figure. Optional: before air, replace 4.1% / "Aug 2026" in `text`, `say`, scene value and sub with the latest BEA month. Not required to pass.

### Issue D (optional precision): line 40
The Vanguard 2025 figure is an estimate. `text`: `In Vanguard's plans, about 96% made some kind of employer contribution in 2025.` `say`: add "about" before "ninety-six percent" (+1 word).

### Issue E (optional precision): line 78
`say`: change "returned about ten percent a year" to "grew about ten percent a year, compounded," (+1 word). This makes clear it is the compound rate and not the arithmetic average (~11.8%).

### Issue F (nit): line 73
Ages 60-63 have a higher $11,250 catch-up in 2026. The line is not wrong, so no change is needed.

### Issue G (nit): yt_desc
It contains an empty "CHAPTERS" heading. Make sure the pipeline fills it in before posting.

## 4. Spoken-word budget
Current 1791. With fix A (+2) and fix B-now (-1): **1792**. Adding optional D and E (+2): 1794. All within 1550-1800.

## Verdict
All math, data and chart points check out, and the assumptions are stated. The hook (Issue A) is misleading as written because it drops the "start earlier" condition, and it also appears in the cover and all post titles. Line 74 needs the safe wording now and a re-check for the official 2027 limits before Dec 21. With fixes A and B applied, this script passes.

VERDICT: FAIL

## Round 2 (editor)
Applied A (hook, cover, post copy), B-now (line 74 safe wording), D and E. Recheck 2027 IRS limits after the mid-November release.
VERDICT: PASS
