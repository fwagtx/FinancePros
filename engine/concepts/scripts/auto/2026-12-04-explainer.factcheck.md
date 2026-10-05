# Fact-check: 2026-12-04-explainer (Acorn Economics, SIPC vs FDIC)

Checked: 2026-10-05. Posting date: 2026-12-04. Source: 2026-12-04-explainer.raw.json only. Line numbers are 0-based indexes into `lines`.

## Verified claims
- **FDIC $250,000 per depositor, per insured bank, per ownership category (line 2, post, yt_desc):** correct. This is FDIC's standard wording.
- **FDIC doesn't cover stocks, bonds, mutual funds or crypto (line 5, yt_desc):** correct. The list is not complete (FDIC also excludes annuities, life insurance, municipal and Treasury securities, and safe deposit box contents), but the line does not claim to be complete.
- **"No depositor has lost a penny of FDIC-insured funds" since 1933 (line 7, post):** FDIC's own wording is "Since the FDIC was founded in 1933, no depositor has lost a penny of FDIC-insured funds" (for example, FDIC press release PR-32-2020). The script gives a close paraphrase without quote marks, which is fine. Some FDIC pages say "since the FDIC began operations in 1934"; both forms are official.
- **SIPC up to $500,000 including a $250,000 cash limit; applies when a member firm fails and customer assets are missing; does not protect against a decline in value (lines 2-3, post, yt_desc):** correct (sipc.org "What SIPC Protects"; Investor.gov).
- **Worked example (line 4):** $10,000 x 20% = $2,000 loss, leaving $8,000. The scene "to" value of $8,000 matches the spoken "$2,000 loss". SIPC covers $0 for a market decline, which is correct. The example is labeled "Example" / "Stocks (example)".
- **Bank-failure chart (line 6), 2001-2025:** 4, 11, 3, 4, 0, 0, 3, 25, 140, 157, 92, 51, 24, 18, 8, 5, 8, 0, 4, 4, 0, 0, 5, 2, 2. All values match FDIC failure counts.
  - 2001-2004 (4/11/3/4): matches FDIC statistics.
  - 2007 = 3: Metropolitan Savings, NetBank and Miami Valley.
  - 2017 = 8, 2019 = 4, 2020 = 4: confirmed.
  - 2023 = 5: SVB, Signature, First Republic, Heartland Tri-State, and Citizens Bank of Sac City, which was "fifth failure this year" on Nov 3, 2023.
  - 2024 = 2: Republic First and First National Bank of Lindsay.
  - 2025 = 2: Pulaski Savings Bank (Jan 17) and Santa Anna National Bank (Jun 27).
  - The peak of 157 in 2010 is correct. The data runs 25 years and totals 570 failures.
- **Pending legislation:** the Main Street Depositor Protection Act (S.4198, reintroduced Mar 25, 2026, with a House companion from Rep. Lucas) would let the FDIC raise coverage only for **noninterest-bearing transaction accounts**, to as much as $5M. As of early October 2026 it has only been referred to the Senate Banking Committee, and no floor vote has been found. Even if it passed, the standard $250,000 limit would stay the same. The risk that the limit changes by Dec 4 is low. Recheck the week before posting.
- **Structure checks:**
  - The keep:true on line 7 follows line 6, which uses the same "chart" template. OK.
  - Compare values "$250K" and "$500K" are both 7 characters or fewer. OK.
  - No advice, no price predictions and no political opinion.
  - The cover "Market Drop Pays $0?" is paid off by lines 0, 3 and 4.

## Issues
1. **Line 6 chart is stale for the posting date (medium).** At least 6 FDIC-insured banks failed in 2026 by late September:
   - Metropolitan Capital B&T (Jan 30)
   - Community Bank & Trust - West Georgia (May)
   - Tioga-Franklin Savings Bank (Aug 21, the 5th)
   - Nano Banc (late Sep, the 6th)

   A chart titled "US bank failures/year" that ends at "2" for 2025 will read as current on Dec 4, 2026, and it understates 2026. The data is not wrong, but the framing is.
   - **Fix:** retitle it "FDIC bank failures, 2001-2025". Better, add a final point labeled "2026 YTD" with the count re-verified before posting (6 as of Sep 30; check for more). Also say "FDIC-insured" in the title instead of "US".
2. **Line 3 ambiguous pronoun (low).** The spoken "It steps in when..." follows a sentence that ends on "two hundred fifty thousand cash", so "it" has nothing clear to refer to when heard.
   - **Fix:** say "S I P C steps in only when the firm fails and assets go missing." Adding "only" also strengthens the point.
3. **Hook, line 0 (low, judged acceptable).** "Brokerage protection: five hundred thousand dollars. Market drop? Zero." is true and specific: SIPC does pay $0 for market losses. It is about 9 words, roughly 3.3 seconds spoken, so slightly over the 3-second target. It is not misleading, but "brokerage protection" is vague. A viewer may not know it means SIPC, and might think it refers to a broker's own guarantee or excess insurance.
   - **Fix (stronger and shorter):** say "S I P C covers half a million. Market crash? Zero." Use the caption "SIPC: $500,000. Market drop? $0." Keep it consistent with the post title.
4. **Line 2 scene sub (nit).** "per depositor/bank" drops "per ownership category", which is spoken and in the caption.
   - **Optional fix:** "per owner/bank/category". Any change only needs to fit the sub field (the 7-character limit applies to the values).
5. **Line 2 tone (nit).** The left shield is "up" (green) and the right is "neutral", which slightly implies FDIC is "better". This is a design choice and does not need to change.

## Spoken vs on-screen
All numbers match: $500,000, $250,000, $10,000, 20%, $2,000, $0, 157 and 2010. The narration reads naturally aloud. "F D I C" and "S I P C" are spelled out for TTS, which is fine.

VERDICT: PASS

## Round 2 (editor)
- Line 6: chart retitled "FDIC bank failures, 2001-25", end label "2 in 2025" so it does not read as current-year data.
- Line 3: narration "Protection steps in only when..." (clear subject).
VERDICT: PASS
