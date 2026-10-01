# Fact-check: 2026-10-19-lf-explained ("Will Social Security Run Out?")

Checked Oct 1, 2026, for posting Oct 19, 2026. Only the .raw.json was read. Direct fetches of ssa.gov, congress.gov and crfb.org were blocked, so these sources were checked through search-result excerpts. About 13 searches were used. All math was recomputed in Python.

## Verified correct

**2026 Trustees Report (June 9, 2026)**
- OASI is depleted in Q4 2032, one quarter earlier than last year, with 78% payable after that (lines 1-3, 66-69, 90). The SSA press release and the SSA and CRS excerpts confirm this.
- Last year's report said 2033 with 77% payable (line 67).
- DI pays 100% through at least 2100 (line 70).
- Combined OASDI lasts to Q3 2034, then 83% payable (line 71).
- The actuarial deficit is 4.42% of payroll for 2026-2100, up from 3.82% (line 77).
- Closing the gap would take a payroll tax of 16.65%, a 25.2% cut to all benefits, or a 30.3% cut for people newly eligible in 2026 and later (lines 78-80).

**2025 operations (2026 Trustees Report)**
- Income was $1,449B: $1,323B payroll tax, $58B tax on benefits and $69B interest. Cost was $1,609B.
- Reserves fell by $160.2B, to $2,561B at the end of 2025.
- About 185M people paid in during 2025.
- 70M people got benefits in December 2025: 56M retirees and families, 8M disabled workers and families, 6M survivors.

**Reserves chart (line 57)**
- Year-end values from 2015 to 2024 match SSA data after rounding: 2812.5, 2847.7, 2891.8, 2894.9, 2897.4, 2908.3, 2852.0, 2829.9, 2788.5 and 2721.5.
- The peak was $2,908B in 2020. The drop from the peak to the end of 2025 is $347B.

**Workers per beneficiary**
- 5.1 in 1960, about 2.6 in 2025 and about 1.9 by 2075 (CRS IF13256). 185/70 = 2.64, which is consistent.

**Other report details**
- The fertility assumption was cut from 1.90 to 1.75.
- The 2025 tax law (OBBBA) added a temporary senior deduction for 2025-2028. The Trustees confirm it reduces income from the tax on benefits.

**2026 parameters**
- The COLA is 2.8%.
- The average retired worker's check went from $2,015 to $2,071.
- The taxable maximum is $184,500, up from $176,100.
- The bend points are $1,286 and $7,749.
- Full retirement age is 67 for people born 1960 or later. Benefits are 70% at 62 and 124% at 70.
- 40 credits are needed to qualify.

**History**
- The Act was signed Aug 14, 1935.
- The FDR quote is word for word. It is the first clause of a longer sentence that continues "but we have tried to frame a law...".
- Ida May Fuller of Ludlow, Vermont got the first check: $22.54 on Jan 31, 1940. She paid $24.75 in tax, collected $22,888.92 and died at 100 in 1975.
- Automatic COLAs began in 1975.
- In late 1982, OASI was projected to be depleted. It borrowed $17.5B from the DI and HI funds, which carried it to mid-1983.
- The 1983 amendments were based on the bipartisan Greenspan Commission, which mixed revenue increases with benefit changes.
- Reserves were about $2.9T in 2020.

## Math (recomputed)

| Line | Item | Result |
|---|---|---|
| 9-10 | Payroll tax on $60,000 | $3,720 each, $7,440 total |
| 12 | Maximum tax | $184,500 x 6.2% = $11,439 |
| 28-30 | Benefit formula | $1,157.40 + $1,188.48 = $2,345.88, rounded down to the dime = $2,345.80 |
| 31 | Replacement rate | 46.9%, so "about 47%" holds |
| 33 | Benefit at 62 | $1,642.06 |
| 35 | Benefit at 70 | $2,908.79 |
| 36 | Difference, 70 vs 62 | $1,266.73 |
| 73-74 | 78% of the benefit | $1,829.72; gap $516.08 (22%) |
| 81 | $60,000 at 16.65% | $9,990 |
| 55 | Income parts | Sum to $1,450B vs $1,449B total (rounding only) |

All on-screen values match the spoken ones.

## Issues

1. **Lines 38-39: stale after Oct 14 (should fix).** The 2027 COLA, taxable maximum and bend points are announced Oct 14, five days before this posts. "Checks rise with inflation each year: 2.8% for 2026" stays true. But viewers on Oct 19 will know the 2027 number, and the video never mentions it.
   - Fix: after the announcement, add "and [X]% for 2027, announced October 14". Or rephrase as "2.8% for 2026; the 2027 raise was announced October 14."
   - Lines 11-12 ($184,500 for 2026) and 24 (2026 bend points) are labeled with their year, so they stay accurate. Optionally add a note on the 2027 taxable maximum.
2. **Lines 30-36: rounding detail (minor).** SSA rounds the full-retirement-age amount down to the dime ($2,345.80), which the script does correctly. SSA also rounds the actual monthly payment and reduced benefits down. For example, 70% of $2,345.80 is paid as about $1,642, not $1,642.06.
   - Fix: none required, since the example is labeled hypothetical. Optionally add "roughly" or use whole dollars for the 62 and 70 figures.
3. **Line 50: imprecise wording (minor).** "Full retirement age is 67 today": people born in 1959 have a full retirement age of 66 and 10 months, and no one reaches 67 under the new rule until 2027.
   - Fix: "That's why full retirement age is 67 for anyone born in 1960 or later, instead of 65."
4. **Line 84: attribute the judgment (minor).** "Starting sooner just spreads the change thinner" is the Trustees' view, and it is stated here as fact.
   - Fix: "The Trustees note that acting sooner spreads the change thinner." The political framing is otherwise neutral, with no side taken.
5. **Line 1 hook (OK).** It is true, specific and gets to the stakes fast, at about 11 words (roughly 3.3 seconds). It could be trimmed slightly, for example "Social Security's retirement fund is projected to empty in 2032."
6. **Line 45 (OK).** "She lived to 100 and collected $22,888.92" is accurate. The scene's "1940-1975" range matches.

There is no advice, no price predictions, no unframed allegations and no instruction-style takeaways. Line 92 is a pointer to my Social Security, which is fine. The cover and title are paid off in lines 68-75 and 91.

VERDICT: PASS
