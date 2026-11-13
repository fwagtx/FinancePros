# Fact-check: 2027-01-12-lf-business (How They Make Money: Ozempic/Wegovy vs Mounjaro/Zepbound)
Checked Nov 13, 2026 for posting Tue Jan 12, 2027. Primary filings were read through Firecrawl (Lilly 8-K Q3 2026, Novo 6-K Q3 2026) and search snippets/mirrors.

## Verified (no change needed)
- Hook (11 spoken words): Lilly Q3 2026 8-K shows Mounjaro $10,723M (+65% vs $6,515M) and Zepbound $5,352M (+49% vs $3,588M). Sum $16,075M, so "$16 billion in three months" is literally true. The call also says "more than $16 billion".
- Per day: 16,075 / 92 days = $174.7M, so "about $175M" is correct.
- Q3 2026 total revenue was $24,397M. Tirzepatide share is 16,075 / 24,397 = 65.9%, or "about 66%".
- Q3 2026 price/volume (8-K): US revenue +34%, with volume +41% and realized price -7%. Outside the US, volume +76% and price -29%, mainly from Mounjaro's NRDL listing in China. Worldwide, volume +53% and price -15%.
- Lilly revenue 2019-2025 ($B): 22.3, 24.5, 28.3, 28.5, 34.1, 45.0, 65.2 (65,179M vs 45,043M in the Q4 2025 release). 65.18 / 28.54 = 2.28x, so "about 2.3x" holds.
- Lilly 2025: Mounjaro $22,965M (+99% from $11,540M) and Zepbound $13,542M (+175% from $4,926M). Combined $36,507M / $65,179M = 56.0%.
- 2026 guidance raised to $91-92B on Oct 29, 2026. Novo's adjusted sales outlook is -2% to +2% at CER (6-K, Nov 4, 2026).
- Lilly was the first drugmaker to reach a $1T market value on Nov 21, 2025 (Reuters via Yahoo/BNN, Al Jazeera).
- Novo net sales (DKK B): 122.0, 126.9, 140.8, 177.0, 232.3, 290.4, 309.1. 2025 was 309,064M, +6% DKK and +10% CER.
- Novo obesity care: about DKK 6B (2019) to DKK 82B (2025, 82,347M), as Novo states. 82 / 6 = 13.7, so "roughly 14x" holds.
- Novo Q3 2026: Ozempic DKK 29.7B (-5% CER), Wegovy injection DKK 20.4B (-2%), Wegovy pill DKK 5,394M. At the 6-K implied ~6.47 DKK/USD that is about $0.83B, so "about $800M" holds. The 6-K also says the Wegovy franchise has ">50% share" of US branded-obesity new patient starts.
- Novo Holdings / Foundation holds 28.1% of capital and 77.3% of votes. A shares carry 10x the votes of B shares.
- Headcount 77,349 (2024) to 69,505 (2025), per the Annual Report five-year overview. About 9,000 job cuts were announced in Sep 2025.
- History: John Eng (Bronx VA) found exendin-4 in Gila monster venom in 1992. Exenatide (Byetta) was approved in April 2005 as the first GLP-1 drug. Ozempic was approved in 2017, Wegovy in 2021, Mounjaro in 2022 and Zepbound in 2023.
- STEP 1 (NEJM 2021): -14.9% vs -2.4% at 68 weeks. SURMOUNT-1 (NEJM 2022): top dose -20.9% at 72 weeks. STEP 1 extension (DOM 2022): about two-thirds of the lost weight was regained one year after stopping.
- Prices:
  - Wegovy list price $1,349.02. $1,349 x 12 = $16,188.
  - Novo's $675 list price for Wegovy and Ozempic from Jan 1, 2027 (announced Feb 24, 2026) is about 50% off Wegovy and about 35% off Ozempic.
  - CMS set a $274 maximum fair price for 2027.
  - Under the Nov 6, 2025 deals, Medicare/Medicaid pay $245 with a $50 Medicare copay.
  - Zepbound vials have cost $299/$399/$449 since Dec 1, 2025. $449 x 12 = $5,388, which is 33% of $16,188.
  - Novo's $199 introductory cash offer started Nov 17, 2025.
  - The Wegovy pill launched Jan 5, 2026. Foundayo was approved Apr 1, 2026 and starts at $149 self-pay.
- Yale-led estimate (Barber et al., JAMA Netw Open, Mar 2024): semaglutide could be made for $0.89-$4.73 a month, so "under $5" holds.
- FDA shortages: semaglutide listed 2022, ended Feb 21, 2025. Tirzepatide listed Dec 2022, ended Oct/Dec 2024.
- Patents:
  - Abroad in 2026: Canada lapsed (generics from May 2026), India expired Mar 20, 2026, China and Brazil ended Mar 2026.
  - US: semaglutide about 2031-32, tirzepatide 2036.
- Side effects are attributed to the FDA labels. The pricing politics are framed neutrally ("supporters/critics"). There is no advice and no stock talk.

## Issues found and fixed in raw.json
1. cover.label "3 MONTHS" (8 chars) was over the 5-char limit. Changed to "3 MO".
2. L14: "The lizard's version... became Byetta" was imprecise, because Byetta is lab-made exenatide.
   - TEXT: "A lab-made copy, exenatide, lasted much longer than our own GLP-1. As Byetta, it became the first GLP-1 drug, approved in 2005 for diabetes."
3. L15: "its own long-lasting version" implied semaglutide derives from the lizard peptide, but it is based on human GLP-1.
   - TEXT: "Novo Nordisk engineered its own long-lasting version of the human hormone, semaglutide. As Ozempic, ..."
4. L17 and L20: the on-screen and spoken values differed ("14.9%" on screen, "about fifteen" spoken; "20.9%" on screen, "about twenty-one" spoken). The SAY lines now read "fourteen point nine", "two point four" and "twenty point nine".
5. L34: Lilly had sold vials directly before Dec 2025, so this line now dates the price, not the channel. It also names the pharmacy.
   - TEXT: "From December 2025, Lilly's own LillyDirect pharmacy sold Zepbound vials for $299 to $449 a month, depending on the dose."
6. L35: TEXT now says "about a third" to match SAY.
7. L36: the $199 offer applied only to new cash-pay patients as an introductory price.
   - TEXT: "Novo did the same through its own pharmacy. In late 2025, new cash-pay patients could start Wegovy at an introductory $199 a month."
8. L45: the on-screen "65.9%" did not match the spoken "about sixty-six percent". The value is now "66%".
9. L48: "$49 billion" used a year-end exchange rate. At the 2025 average of about 6.6 DKK/USD, DKK 309.1B is about $46.8B.
   - TEXT: "...to 309 billion, or roughly $47 billion."
10. L50: "the old leader was shrinking" was untrue, because Novo's Q3 2026 sales grew 4% at CER.
    - TEXT: "But by 2026 its biggest shots were slipping. In July to September, Ozempic sales fell 5% and Wegovy shots fell 2%, at constant currency."
11. L52: on the call, Lilly's "about 6 out of 10 total prescriptions" referred to US obesity incretin prescriptions. In diabetes it said ">60% share".
    - TEXT: "...about 6 of every 10 US prescriptions for obesity drugs like these were for its medicines."
12. L53: aligned with the 6-K wording, which reports share for the Wegovy brand on new patient starts.
    - TEXT: "Novo counters that the Wegovy brand wins over half of new US patients starting branded obesity drugs. ..."
13. L64 and L65: the tense was stale for a Jan 12, 2027 post, because the $675 list price is already in effect. They now read "Starting January 2027, Wegovy's US list price is $675 a month..." and "Ozempic's list price is $675 too, about 35% lower, Novo said."
14. L66: the $274 figure needed to be separated from the $245 deal price. The two are distinct mechanisms, and press reports the Medicare price as "muddled".
    - TEXT: "Separately, Medicare's own negotiation set a $274 monthly price for Ozempic and Wegovy, starting in 2027."
15. L69: the forecast is now dated and gives its basis.
    - TEXT: "Novo, meanwhile, said in November that its 2026 adjusted sales would land between down 2% and up 2%, at constant currency."
16. L74 scene: the countries said "Generics!", but no generic launch is confirmed in China. Both cast lines now say "Patent over".
17. post.yt_desc: added these sources: Novo Holdings, CMS 2027 negotiated prices (Nov 2025), Novo self-pay offer (Nov 17, 2025) and Wegovy pill launch (Jan 5, 2026). CHAPTERS remains a placeholder, as in earlier episodes.

## Checks
- The hook is 11 spoken words and literally true.
- The cover title "The $16B Shot." is 14 chars, the value "$16B" is 4 and the label "3 MO" is 4.
- check.py prints OK: 92 lines, 1713 spoken words.
- The JSON is valid, formatting is unchanged (indent 1), and the diff is limited to the edited fields.
- Residual notes (acceptable):
  - The $1,349 list price covers a 28-day pack, and "a month" follows Novo's own wording.
  - The $449 Zepbound tier requires a refill within 45 days.
  - The share figures from Lilly ("6 in 10") and Novo (">50% of starts") are each company's own claim, and the script attributes them.

VERDICT: PASS

## Round 2 (editor)
Reviewed 17 fixes (Novo growth wording, market-share scope, USD conversion, cover label). check.py OK.
VERDICT: PASS
