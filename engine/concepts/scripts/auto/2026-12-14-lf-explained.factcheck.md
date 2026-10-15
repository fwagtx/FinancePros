# Fact-check: 2026-12-14-lf-explained (How mortgages work)

Independent check of the raw.json only (97 lines, 1,719 spoken words). Posting date: Monday, December 14, 2026. The writer's .research.md was not used as a source. Math was recomputed in Python (script: /tmp/claude-0/-home-user-FinancePros/5ffba232-ed3e-5489-9dae-abbfd787fe50/scratchpad/m2.py).

## A. Worked-example math (own Python recomputation)

| Line(s) | Claim | Recomputed | Verdict |
|---|---|---|---|
| 2, 23, 28 | $400,000, 7.40%, 360 months: payment $2,769.52 | $2,769.519 | OK |
| 2, 24 | Month-1 interest $2,466.67 (about $2,467), 89% | $2,466.67 = 89.07% | OK |
| 2, 25 | Month-1 principal $302.85 (about $303), 11% | $302.85 = 10.93% | OK |
| 26 | Balance after payment 1: $399,697 | $399,697.15 | OK |
| 28 | Year 1: $29,474 interest, $3,760 principal | $29,474.17 / $3,760.06 | OK |
| 29 | Balance chart (in $K) 400/378/346/301/234/139/0 at years 0-30 | 400 / 378.09 / 346.41 / 300.60 / 234.35 / 138.54 / 0 | OK |
| 30 | After 10 yrs: about $332,000 paid, $346,411 owed | $332,342 paid; $346,410.90 owed | OK |
| 31 | $53,589 paid off | $53,589.10 | OK |
| 32 | Principal beats interest at payment 249, year 21 | Payment 249 (principal $1,391.15 vs interest $1,378.37); payments 241-252 = year 21 | OK |
| 4, 34 | Total interest $597,027; total paid about $997,000 | $597,026.91; $997,026.91 | OK |
| 36 | 15-yr at 6.73%: about $3,535/mo | $3,535.20 | OK |
| 37 | 15-yr interest about $236K, about $361K less | $236,336.71; difference $360,690 | OK |
| 14 | $8,000 fees, 7.40% rate -> APR about 7.61% | 7.606% (fees treated as prepaid finance charges, amount financed $392,000) | OK |
| 17 | 1 point on $400K = $4,000 | $4,000 | OK |
| 18 | At 7.15%: about $2,702; falls $67.89 | $2,701.63; difference $67.89 | OK |
| 19 | $4,000 / $67.89 = about 59 months, roughly 5 years | 58.9 months (4.9 years) | OK |
| 46 | Same loan at 2.96%: about $1,678 | $1,677.80 | OK |
| 45 | 2.96% to 6.81% "more than doubled" | x2.30 | OK |
| 60 | $500K x 0.9% = $4,500/yr = $375/mo | Same | OK |
| 62 | $2,424 / 12 = $202 | $202.00 | OK |
| 63 | PITI $2,769.52 + $375 + $202 = $3,346.52 | $3,346.52 | OK |
| 64 | About 21% more than P&I | 20.8% | OK (rounded) |
| 70 | 10% down: $450K loan; PMI $135-$315/mo at $30-$70 per $100K | 4.5 x 30 = 135; 4.5 x 70 = 315 | OK |
| 75 | $450K at 7.40%: balance hits 80% of $500K at payment 105, 78% at payment 120 (exactly 10 years) | Payment 104 balance $400,536, payment 105 $399,890; payment 119 $390,420, payment 120 $389,712 | OK |
| 88 | DTI on $12,000/mo: 27.9%; with $800 car loan, 34.6% | 27.89%; 34.55% (rounds to 34.6%) | OK |
| 85 | 2/1/5 caps from 6%: 8% max at first change, 11% lifetime | 6+2 = 8; 6+5 = 11 | OK |
| 21 | Formula M = L x r / (1 - (1+r)^-n) | Standard amortization formula | OK |

## B. Factual claims (web research)

| Line(s) | Claim | Verdict | Source |
|---|---|---|---|
| 1, 35, 40, 46, 49 | Freddie Mac PMMS Oct 8, 2026: 30-yr 7.40%, 15-yr 6.73% | Confirmed | Freddie Mac release "Mortgage Rates Average 7.40%" (GlobeNewswire, Oct 8, 2026); Freddie Mac PMMS archive (15-yr 6.73%). The prior week (Oct 1) was 7.28%. |
| 49 | 5.98% in late February 2026 | Confirmed | Freddie Mac PMMS, Feb 26, 2026: 30-yr 5.98% (first time below 6% in about 3.5 years) |
| 47 | Record high 18.63%, October 1981 | Confirmed | Freddie Mac PMMS (week of Oct 9, 1981), reported by multiple outlets |
| 48 | Record low 2.65%, January 2021 | Confirmed | Freddie Mac release, week ending Jan 7, 2021 (RISMedia) |
| 43 chart | Annual averages: 2016 3.65, 2017 3.99, 2018 4.54, 2019 3.94, 2020 3.11, 2021 2.96, 2022 5.34, 2023 6.81, 2024 6.72, 2025 6.6 | Confirmed / consistent | 2016 3.65% confirmed by a Freddie Mac release. 2017-2024 match Freddie Mac PMMS annual averages. 2025: Freddie Mac cited a 6.62% YTD average in mid-December 2025, and Realtor.com reported "rates averaged 6.6%" for 2025. Because the 2025 figure is rounded to one decimal, "about 6.6%" (as spoken) is correct. |
| 44, 45 | 2021 avg 2.96% (low point of the series); 2023 6.81% | Confirmed | Freddie Mac PMMS annual averages |
| 41, 42 | PMMS is weekly and covers conventional loans for borrowers with 20% down and excellent credit | Confirmed | Freddie Mac PMMS methodology ("conventional, conforming, fully amortizing home purchase loans for borrowers who put 20% down and have excellent credit") |
| 50 | New number every Thursday | Essentially correct | Freddie Mac publishes on Thursdays (shifted to Wednesday in some holiday weeks). Minor nit; optional fix below. |
| 52, 53 | 2026 conforming limit $832,750, one unit, most areas; Fannie/Freddie buy up to it; jumbo above; FHFA resets yearly | Confirmed | FHFA release, Nov 25, 2025 (+3.26%, up $26,250; high-cost ceiling $1,249,125). The wording says "2026" on screen and "For twenty twenty-six" in the narration, so it stays accurate after FHFA announces the 2027 limit in late November 2026. |
| 54 | NAR: September 2026 median existing-home price $417,500 | Confirmed | NAR Existing-Home Sales release, Oct 13, 2026 ($417,500, +1.3% y/y from $412,300; sales 3.99M SAAR). Dated "Sep 2026", so it is fine on Dec 14. |
| 13 | CFPB: APR includes the rate plus points, broker fees and other charges, as a yearly rate | Confirmed | CFPB "What is the difference between a mortgage interest rate and an APR?" |
| 16 | One point = 1% of the loan amount | Confirmed | CFPB, discount points |
| 80 | Loan Estimate within 3 business days of application; Closing Disclosure at least 3 business days before closing | Confirmed | CFPB TRID rule (Reg Z 1026.19(e), (f)) |
| 58, 59 | ATTOM 2025: average effective property tax rate on single-family homes 0.9%; Illinois 1.84%, New Jersey 1.58% | Confirmed | ATTOM 2025 Property Tax Analysis (April 2026; MBA Newslink Apr 13, 2026) |
| 61 | Bankrate national average homeowners policy $2,424/yr for $300,000 dwelling coverage | Confirmed | Bankrate homeowners insurance cost page (2026; Quadrant data). Bankrate's earlier August 2025 figure was $2,470, so the 2026 figure is the right one to use. |
| 65-67 | Escrow; federal cushion cap of 1/6 of annual disbursements (about 2 months); annual escrow analysis | Confirmed | RESPA / Regulation X, 12 CFR 1024.17 |
| 68, 69 | PMI usually applies with under 20% down on conventional loans; Freddie Mac: $30-$70/mo per $100K borrowed | Confirmed | Freddie Mac My Home, "What Is Private Mortgage Insurance?" |
| 71-74, 94 | Homeowners Protection Act (1998): borrower can request cancellation at 80% of original value with good payment history; automatic at 78% on the original schedule if current; final termination at the midpoint if current | Confirmed | HPA, 12 USC 4901 et seq. (enacted July 29, 1998; covers loans closed on or after July 29, 1999); CFPB PMI cancellation guidance; Massachusetts state summary |
| 76 | FHA, VA and USDA loans are not covered by this law | Confirmed | HPA covers private mortgage insurance on conventional loans. Government-backed loans use their own mortgage insurance or guarantee fee rules (CFPB). |
| 78, 79 | Closing costs typically 2%-5% of the purchase price | Confirmed (widely cited) | Freddie Mac / Fannie Mae consumer guidance; CFPB |
| 82-84 | 5/6 ARM (fixed 5 years, then adjusts every 6 months); index (usually SOFR) plus margin; common 2/1/5 caps | Confirmed | Fannie Mae / Freddie Mac SOFR ARM plan specifications (5/6 SOFR ARM with 2/1/5 caps) |
| 89 | Fannie Mae max DTI: 50% through DU; 36% manual, up to 45% with credit score and reserves | Confirmed | Fannie Mae Selling Guide B3-6-02 |
| 11 | 30 years is the US standard term | Confirmed | Most common US mortgage term |

## C. Editorial checks

- **Opening:** Line 0 "The first mortgage payment can be 89% interest." is 9 words (under 3 seconds), true for the labeled example (89.07%), specific, and paid off by lines 1-3, 24-25 and 95. The hook visual is a big red 89%. Strong. Optional: "Your first mortgage payment can be 89% interest." is a little more direct.
- **Cover and title:** "89% Goes to Interest." and the post title are paid off by the video. OK.
- **Dating and evergreen wording:** The 7.40% rate is dated "Oct 8, 2026" every time it appears as a market rate (lines 1, 35, 46 sub, 49, and yt_desc). Elsewhere it is used as the example loan's rate. A December 14 viewer will not read it as the current rate. There are no "today", "this week" or "just announced" words. The conforming limit is labeled 2026. NAR, ATTOM and Bankrate figures are dated. OK.
- **Advice and predictions:** None. "Nobody knows which way it goes next" (line 50) and "nobody knows rates 5 years out" (line 86) explicitly avoid prediction. The points break-even (line 19) is descriptive math, not a recommendation. "That's a ceiling, not a budget" (line 89) is an observation, not an instruction. OK.
- **Politics:** None.
- **Hypotheticals labeled:** "Example", "our example" and "Hypothetical" are used throughout (lines 1, 9, 14, 18, 60, 70, 75, 85, 88), and yt_desc says "All examples are hypothetical and labeled." OK.
- **Spoken and on-screen numbers:** Checked every line. All match (rounding is spoken, exact figures are on screen).
- **Template limits:** All compare values are 7 characters or fewer (longest: "$29,474", "Pmt 105", "11% max"). All stat values are 9 characters or fewer. Every keep:true line follows a line with the same template (lines 3, 10, 11, 38, 48, 49, 57, 73, 74, 92-94). OK.
- **Length:** 1,719 spoken words and 97 lines, both within range.

## D. Optional polish (not required for PASS)

None of these is a factual error. If applied, word count stays within about +/-10 of 1,719 and the line count stays at 97.

1. **Line 50** (`text` and `say`): "A new number comes out every Thursday" -> "A new number comes out almost every Thursday". Holiday weeks move the release to Wednesday, and Thanksgiving week falls just before posting.
2. **Line 82** (`say`): "A five six ARM is fixed for five years" -> "A five-slash-six ARM is fixed for five years". This avoids the voice reading "five six" as a list.
3. **Line 84** (`say`): "Common two, one, five caps allow" -> "Common two-one-five caps allow".
4. **Line 4** (`scene.sub`): "On a $400K loan" -> "$400K at 7.40%". This ties the stat to its assumption.
5. **Line 61** (`scene.sub`): "Per year, Bankrate" -> "Per year, Bankrate 2026".
6. **post.tiktok:** "On a $400K loan at 7.40%, ..." -> "On a $400K loan at 7.40% (Oct 2026 rate), ...". This teaser is not posted for long-form.
7. **post.yt_desc:** "lender 5/6 SOFR ARM disclosures" -> "Fannie Mae and Freddie Mac SOFR ARM plan terms (5/6, 2/1/5 caps)". This is a more specific source.

No required fixes.

VERDICT: PASS

## Round 2 (editor)
Applied optional polish 1, 4, 5. No required fixes.
VERDICT: PASS
