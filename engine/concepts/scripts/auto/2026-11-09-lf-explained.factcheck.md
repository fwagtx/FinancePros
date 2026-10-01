# Fact-check: 2026-11-09-lf-explained (long-form, posts Nov 9, 2026)

Checked Oct 1, 2026. I read only the raw.json script. I used 26 web searches. Most official sites (bain.com, gao.gov, repec, skadden, pe-insights) blocked direct fetch, so many checks rely on search excerpts. I recomputed the math with python and ran a script to check every on-screen length limit.

## Must fix (factual / staleness)

1. **L64: Davis et al. job figures are from the old working paper, not the version the script cites.** The script says "down 13% … up 13%" and shows -13% / +13% on screen. Those are the 2019 NBER working-paper numbers. The published Management Science (Nov 2025, vol. 71(11)) abstract says employment "shrinks 12%" after public-to-private buyouts and "expands 15%" after buyouts of private firms. The +8% productivity (L63) and -1.7% earnings (L65) figures match the published version.
   - **Fix:** in text, say, and the compare values, change to "down about 12% … up about 15%" and show -12% / +15%.
2. **L53: Steward's state count is wrong.** The script says "31 hospitals in 10 states". Bankruptcy coverage (May 6, 2024) says 31 hospitals in **eight** states (AZ, AR, FL, LA, MA, OH, PA, TX).
   - **Fix:** say "31 hospitals in eight states", or drop the state count.
3. **L49-50 (and L90 recap): the housing section is stale for a November 2026 video.** Congress passed the 21st Century ROAD to Housing Act in June 2026, which restricts institutional investors' purchases of certain single-family homes. GAO covered it in a July 13, 2026 blog post and also issued a newer report, GAO-26-108675 (Mar 24, 2026). Citing only the May 2024 report with 2022 data, and leaving out the law, leaves viewers with an out-of-date picture.
   - **Fix:** add one neutral line, for example: "In 2026, Congress passed a housing law that restricts large investors from buying certain single-family homes." First confirm the enactment and signing date and the exact scope.
   - **Also:** consider citing GAO-26-108675 for the figures.
   - **Also:** these investors are largely REITs and other institutions, not only PE funds. At L49, say "large investors, some backed by private equity".
4. **L47: "made JAB sell some clinics before buying" is imprecise.** The FTC orders (June 13 and June 29, 2022) required divestitures as a **condition** of the acquisitions. They also imposed prior-approval and prior-notice requirements for future deals.
   - **Fix:** "…the FTC required PE firm JAB Consumer Partners to sell some clinics as a condition of buying two vet chains."
   - Verified: the $1.1B SAGE and $1.65B Ethos deal values, and the FTC calling it a "rollup".
5. **L13: unsourced generality plus an overclaiming hook graphic.** The line "Many public pension funds, including teachers' funds…" is unsourced, and the on-screen hook "Your [pension] is in" tells every viewer that their own pension is invested in PE. Many viewers have no pension.
   - **Fix:** attribute the claim, for example "Big public pension funds, such as California's teachers' fund CalSTRS, put part of their money into PE funds."
   - **Fix:** change the hook title to "[Pensions] are in".

## Should fix / clarify

6. **L40-41 chart (975/719/442/628/904): only partly confirmed against the 2026 report.**
   - Confirmed: $904B is from the 2026 report and is +44% excluding add-ons. That implies 2024 = $628B, and 904/628 = +43.9%. "Second-best year on record", behind 2021, is also confirmed.
   - Only seen in an aggregator excerpt: 975 / 719 / 442 for 2021-2023. I could not open the Bain PDF to confirm all five values come from the same 2026 exhibit. Bain revises past years; for example, its 2025 report put 2024 at about $602B.
   - **Desk check:** confirm all five points against the 2026 report's buyout deal value exhibit before air.
7. **L1-3: the PitchBook and Bain figures count different things.** PitchBook's ">9,000" US deals (and about $1.2T) counts all PE deals, including add-ons. 9,000/365 = 24.7, so "about 25 a day" holds. Bain's $904B counts global buyouts and **excludes** add-ons.
   - **Fix:** in yt_desc or a sub, say "9,000+ deals, including add-ons".
   - **Fix:** at L3, consider "…$904 billion of buyouts, not counting add-on deals."
8. **L69: the "no sign of higher death rates" finding needs its scope.** The Gao-Kim-Sevilir (JFE 2025) mortality finding covers heart-attack, heart-failure and pneumonia patients. The Annals paper's June 2026 correction now describes it that way.
   - **Fix:** "…with no sign of higher death or readmission rates for heart attack, heart failure and pneumonia patients."
   - Verified: patient satisfaction declined, admin job cuts, no significant inpatient price increase.
   - Optional context: satisfaction also fell, and fell more, at hospitals bought by non-PE buyers.
9. **L36-38: EA deal size wording.** EA's release (Sept 29, 2025) says "approximately $55 billion", which is fine. Bain records the deal at $56.6B and calls it an all-time buyout record, not just 2025's biggest. The financing is confirmed: about $20B of debt arranged by JPMorgan and about $36B of equity.
   - Optional: say "the biggest buyout on record". Reports say the deal closed Aug 4, 2026, and "agreed … to be bought" is still accurate.
10. **L93: generic "Supporters…/Critics…" attribution.** Attribute both sides, for example: "The administration says it widens access and diversification. Critics, including some consumer advocates, point to higher fees and assets that are hard to sell."
    - The dates are correct: the executive order was Aug 7, 2025, and the DOL proposal was Mar 30, 2026. As of September 2026 the rule is still only proposed, with more than 47,000 comments filed. "Proposed" is correct, but check again before posting in case it is finalized.
11. **L31 / L89: say the multiple is before the GP's carry.** 2.75x is the deal multiple before carry. After the $14M carry, LPs get $96M on $40M, which is 2.4x.
    - Optional: add "before the GP's cut" to avoid confusion.
12. **L50: national share of single-family rentals.** GAO-24-106643 is quoted as "about 3%" nationally (some summaries say 3-5%) and about 25% in Atlanta. Keep "about".
13. **yt_desc:** the "CHAPTERS" heading is empty. Fill in timestamps or remove it.
14. **L36: news source string is 30 characters.** "Electronic Arts, Sept 29, 2025" is over 28 if that limit applies to sources. Use "EA release, Sept 29, 2025".

## Verified OK

- **PitchBook 2025 Annual US PE Breakdown:** more than 9,000 deals, $1.2T, second-highest total after 2021.
- **Bain 2026 report:**
  - Buyout fundraising down 16% to $395B in 2025.
  - 32,000 unsold companies worth $3.8T.
  - Healthcare: the press release says a record $190B (the report says an estimated $191B). This is from Bain's Global Healthcare PE Report, Jan 2026.
- **WSJ (Oct 12, 2024, PitchBook data):** nearly 800 HVAC, plumbing and electrical firms bought since 2022.
- **Dentists:**
  - ADA HPI: DSO affiliation rose from 7.2% (2015) to 16.1% (2024).
  - Health Affairs (Nasseh, LoSasso, Vujicic, Aug 2024): PE-affiliated dentists rose from 6.6% to 12.8%, 2015-21.
- **GAO-24-106643 (May 22, 2024):** 32 investors owned about 450,000 homes as of 2022; about 25% of single-family rentals in Atlanta.
- **Steward:**
  - Cerberus bought Caritas Christi in 2010 (it became Steward).
  - The 2016 sale-leaseback with MPT covered 9 hospitals for $1.25B.
  - Cerberus exited in 2020.
  - Chapter 11 filed May 6, 2024, with 31 hospitals.
  - More than $9B in liabilities, of which $6.6B was long-term lease liabilities owed to MPT.
  - The wording sticks to documented facts.
- **Sports:**
  - NFL vote 31-1 on Aug 27, 2024, allowing up to 10%, passive stakes only (CNBC).
  - Other leagues cap PE at 30% (reported). The NBA and NHL also cap a single fund at 20%; the "combined" wording is OK. MLB also allows it and could be added.
- **Studies:**
  - Harris, Jenkinson & Kaplan (Journal of Finance, Oct 2014): buyout funds beat the S&P 500 by 20-27% over a fund's life, more than 3% a year.
  - Gupta, Howell, Yannelis & Gupta (RFS 2024, 37(4)): +11% mortality; lower staffing and weaker compliance with care standards; about 11% higher taxpayer spending per episode.
  - Kannan, Bruch & Song (JAMA, Dec 26, 2023): +25.4% hospital-acquired conditions, including falls and central-line bloodstream infections.
  - Kannan et al. (Annals, Sept 23, 2025): -11.6% full-time employees, -16.6% salary spending, +13.4% ED mortality (7.0 more per 10,000 visits). The June 2026 correction changes only how the Gao study is described, not these numbers.
  - Phalippou (Journal of Investing, 2020): about 11% a year, matching stock indexes since 2006; about $230B in carry.
  - Bernstein & Sheen (RFS 2016), restaurant health violations: checked from known citation only, not searched (budget).
- **LBO math:**
  - Good case: 110/40 = 2.75x versus 150/100 = 1.5x for an all-cash buyer.
  - Carry: 70 × 20% = $14M to the GP, $56M to LPs.
  - Bad case: 20/40 = -50% versus 80/100 = -20%.
  - The example is labeled hypothetical and simplified (L25, L32, "Example" labels).
- **On-screen limits:** all titles, labels, subs, list items and board lines are 28 characters or fewer. Compare subs are 18 or fewer, headlines 34 or fewer, and timelines have 8 or fewer events.
- **Other checks:** no advice, no price predictions, and no "now/latest" wording. Balance is even (chapters for and against). Spoken and on-screen values match.
- **Opening:** "Private equity did over 9,000 US deals in 2025" is true and specific but about 3.5 seconds spoken. A stronger, shorter option: "Nine thousand private equity deals. In one year." The cover and title are paid off.

VERDICT: FAIL
