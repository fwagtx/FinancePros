# Fact-check: 2026-10-12-lf-explained (posts Oct 12, 2026)

Checked Sept 30, 2026. Script JSON only; 12 searches; math recomputed in python.

## Verified OK
- M2 Aug 2026 = $23,342.8B SA (H.6, Sept 22, 2026), a record; +5.7% y/y. L3, L21 OK.
- M2 chart (Dec, SA): 2020 19.13, 2021 21.47, 2022 21.27, 2023 20.70, 2024 21.49, 2025 22.36, Aug 2026 23.34. All chart points round correctly (L15, L52, L90).
- Early 2020 ~$15T, early 2022 ~$21.7T (L16) OK.
- 26.9% y/y M2 growth Feb 2021 (St. Louis Fed, "The Rise and Fall of M2", May 2023) OK (L17).
- 2023: first y/y M2 decline of 2%+ since the Great Depression (widely reported, e.g. Motley Fool, from 1870+ data) OK (L19).
- Reserve requirements cut to 0% effective March 26, 2020, still 0% (L29).
- FOMC Sept 16, 2026: +25bp to 3.75%-4.00%, first hike since 2023; IORB raised to 3.90% effective Sept 17 (L65-67). Next FOMC is Oct 27-28, so this is still current on Oct 12.
- Reserve balances ~$2.93T (H.4.1, Sept 2026) (L45) OK.
- Loans and leases, all commercial banks ~$14.06T (H.8, Sept 2026) (L70) OK.
- CET1 minimum 4.5% + stress capital buffer floor 2.5% = at least 7% (L61-62) OK.
- The Bank of England quote in L42 matches the 2014 Q1 Bulletin word for word ("Whenever a bank makes a loan, it simultaneously creates a matching deposit in the borrower's bank account, thereby creating new money.").
- SVB: about $42B in withdrawal requests on Mar 9, 2023; closed by the California DFPI and FDIC on Mar 10; the second-largest US bank failure at the time (L81-82).
- FDIC $250,000 per depositor, per bank, per ownership category; FDIC created in 1933; Fed created in 1913; gold convertibility suspended in 1971; about 9,000 bank failures in the Depression. All OK.
- Loan math: payment = $594.036, which rounds to $594.04 (OK). Month-1 interest is $175.00 and principal is $419.04 (OK).
- Multiplier chain 1000/0.10 = $10,000 OK.

## Issues
1. **WRONG FIGURE, and it is the hook: L1, L4, L94, cover, all post text (89%, $2.48T, 11 cents).** The $2.48T is currency in circulation, a Fed balance-sheet and monetary-base measure that includes bank vault cash. It is not the currency that is part of M2. The M2 currency component (currency component of M1, H.6) for Aug 2026 was **$2,389.7B**. That is 2,389.7 / 23,342.8 = **10.2%**, so about **90%** isn't cash (89.8%). The on-screen "$20.9T" in L4 is also inconsistent with the script's own numbers: 23.3 - 2.48 = 20.82. With the correct component it is 20.95, about $21.0T.
   - Fix: L1 and the cover become "About 90% of America's money isn't cash." L4 becomes "Paper cash and coins were only about $2.39 trillion of that. About 10 cents of every dollar." In the scene, set left = $2.39T "about 10%" and right = "$21.0T" "about 90%". Update L94, the cover value, the post title, ig, tiktok and yt_desc ($2.39 trillion, 90%) to match.
2. **Misattribution: L57 "The Bank of England lists three brakes. First, profit."**, followed by capital rules and the central bank. The BoE's three constraints are: (i) banks themselves (profitability, risk, regulation); (ii) the behaviour of households and firms, for example repaying debt; (iii) monetary policy, which is the ultimate limit. Capital rules are part of (i), not a separate item on the BoE's list.
   - Fix: "Economists point to three big brakes. First, profit." Or keep the BoE attribution but list its three constraints correctly.
3. **Math consistency: L53 and L88 ($5,642.16).** $5,642.16 only works with an unrounded payment. With the stated $594.04 x 60, total interest is $5,642.40. A real amortization schedule with the final payment adjusted gives about $5,642.12. Viewers who multiply will get a different number.
   - Fix: use "about $5,642" everywhere. Drop the cents from the L53 text, the spoken line and the scene sub (e.g. "about $5,642: $30K, 7%, 60 months").
4. **L30 "One divided by zero is infinity."** This is mathematically wrong: division by zero is undefined, and the scene itself says "does not compute."
   - Fix: "Plug zero into the formula and it breaks. The multiplier would be infinite."
5. **L81 "customers pulled $42 billion in one day."** The DFPI and Fed OIG describe roughly $42B of withdrawal *requests* on March 9.
   - Fix: "customers tried to pull about $42 billion in a single day." Minor.
6. **L67 on-screen/spoken mismatch:** the text says "almost no risk" but the narration says "basically no risk." Make them match ("almost no risk"). Minor.
7. **L49 awkward:** "here's the answer from chapter one" (L20 said the answer comes in chapter three).
   - Fix: "And here's the answer to chapter one's question." Minor.
8. **L51 text/say differ in wording.** The meaning is the same, so this is acceptable. Optional: align them.
9. **L63 scene "Loans $100 / Capital $7":** the 7% applies to risk-weighted assets, not to loans. The sub says "risk-weighted," which is acceptable. Optional: change the label to "Risk-weighted loans."

## Other checks
- Opening: "About 89% of America's money isn't cash." is short (under 3s), specific and creates curiosity. It is strong once the number is corrected to 90%.
- Time words: "September 2026", "mid-September 2026" and "August 2026" are all dated explicitly. The next M2 release (~Oct 27) and the next FOMC (Oct 27-28) both come after the Oct 12 posting, so nothing goes stale.
- No advice, price predictions or political opinion. The worked example is clearly labeled ("Assume", "example"). The cover and title are paid off. The quote is exact. The BoE's UK statement is attributed to the BoE, and the QE caveat is included.

VERDICT: FAIL

---

## Round 2 (re-check of the revised file, Oct 1, 2026)

Reviewed the full revised JSON and the git diff. 0 new searches were needed: all changed values were already verified in Round 1.

**All Round 1 issues are resolved:**
1. Hook and currency share. L1, L4, L94, the cover, title, ig, tiktok and yt_desc now say 90% and $2.39T. M2 currency component $2,389.7B / M2 $23,342.8B = 10.2%. The rest is 23,342.8 - 2,389.7 = $20,953B, which rounds to $21.0T. On-screen and spoken values match. No stray "89", "2.48" or "eleven cents" remains.
2. L57 now reads "Economists point to three big brakes." The misattribution to the Bank of England is gone.
3. L53 and L88 now say "about $5,642" in the text, the spoken line and the scene. This is consistent with both $5,642.16 (unrounded payment) and roughly $5,642.12–$5,642.40 (rounded payment).
4. L30 now says "the formula breaks; the multiplier would be infinite." This is accurate.
5. L81 now says "tried to pull about $42 billion." This is accurate.
6. L67: text and spoken line both say "almost no risk." L49 and L51 are fixed. The L63 label is now "Risk-wtd loans."

The rest of the script is unchanged: dates, Fed decision, quote, chart and loan math are all verified in Round 1.

**Remaining issue (minor, optional):**
- L81 scene label "Withdrawn from Silicon Valley Bank, Mar 9, 2023" is slightly stronger than the corrected narration ("tried to pull"). Optional fix: "Withdrawal requests, Silicon Valley Bank, Mar 9, 2023". This is a style nit and does not block the slot.

VERDICT: PASS
