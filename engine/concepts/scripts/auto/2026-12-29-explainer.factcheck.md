# Fact-check: 2026-12-29-explainer (Acorn Economics: Who pays a tariff?)
Checked Oct 30, 2026 for a Dec 29, 2026 post. Only the factcheck file was written; raw.json was not edited.

## Verified claims (no change needed)
- **Mechanics (lines[1], lines[2]):** A tariff is a tax on imports. The importer of record is legally liable and pays CBP. Confirmed by CBP entry summary guidance and 19 U.S.C. 1505.
- **Worked example (lines[3], lines[4], post):** The script labels this "Our own math." Recomputed: $100 x 10% = $10, so the landed cost is $110. Correct.
- **lines[5]:** Amiti, Redding & Weinstein, JEP 33(4), 2019, found near-complete pass-through of the 2018 tariffs to US import prices. Fajgelbaum et al. (QJE 2020) agree. "~100%" is a fair summary.
- **lines[6]:** NY Fed Liberty Street Economics, "Who Is Paying for the 2025 U.S. Tariffs?" (Amiti, Flanagan, Heise, Weinstein), published Feb 12, 2026, used data through Nov 2025. It found "nearly 90 percent" of the tariffs' economic burden fell on US firms and consumers (94% in Jan-Aug, 86% by Nov). Confirmed by the post and coverage in The Fiscal Times, Fortune and WDEF.
- **lines[7]:** Cavallo, Gopinath, Neiman & Tang, AER: Insights 3(1), 2021, found near-full pass-through at the border but a much smaller effect on retail prices, so retail margins fell. Confirmed.
- **lines[8] chart values (net customs duties by fiscal year, Treasury):** FY2022 $99.9B, FY2023 $80.3B, FY2024 $77.0B, FY2025 $194.9B. All match Treasury-based trackers and USAFacts; CRFB gives "about $195B" for FY2025. These are net-of-refund figures. Other sources give other FY2024 numbers depending on method, but $77.0B is the widely cited Treasury MTS figure.
- **Timing and wording:**
  - No stale time words. Every number carries its year.
  - No current tariff rates or legal-status claims.
  - No advice or price predictions.
  - Compare values are 7 characters or fewer.
  - No keep:true flags.

## Issues
1. **cover and lines[0] (hook scene): "~90%" is unattributed and easy to misread.**
   - Problem: The label "TOLL" next to the value "~90%" reads as a 90% tariff rate. Nothing on the cover or hook says what the 90% is or who found it. The attribution first appears at lines[6].
   - Fix: In both cover and lines[0].scene, change `"label": "TOLL"` to `"label": "US SHARE"`.
   - Fix: In lines[0].scene, add `"sub": "NY Fed est., 2025 tariffs"` if the template supports it.
   - Fix: Change the cover title to `"Who Pays Tariffs?"`. Keep the value "~90%".
2. **lines[0] text/say: the hook overstates the claim.**
   - Problem: "The other country doesn't pay the tariff" is true legally, since the importer pays CBP. Economically, the video's own NY Fed figure implies foreign exporters bore about 10% in 2025. The flat claim also reads as a political rebuttal.
   - Fix (text and say): `"The other country doesn't pay the tariff bill at the border. So who does?"` A shorter option is `"Foreign countries don't pay the tariff bill. So who does?"`
3. **lines[8]: the on-screen number differs from the spoken one.**
   - Problem: The text says "$194.9 billion" but the narration says "about one hundred ninety-five billion".
   - Fix (text): `"Customs duties hit about $195 billion in fiscal 2025."` This matches the say line and the chart end label "$195B".
   - Optional fix: Set the chart title to `"US customs duties, fiscal years"` so the 2022-2025 points are clearly fiscal years and not calendar years.
4. **lines[6]: the noun is missing and the finding is stated as certain.**
   - Problem: "bore nearly 90%" doesn't say 90% of what. The finding is an estimate, and the White House publicly disputed it.
   - Fix (text): `"For 2025, the New York Fed estimated US firms and consumers bore nearly 90% of the tariff cost."`
   - Fix (say): `"For twenty twenty-five, the New York Fed estimated US firms and consumers bore nearly ninety percent of the tariff cost."`
5. **lines[5]: the narration is awkward and ambiguous.**
   - Problem: "nearly 100% hit US import prices" doesn't say what hit them.
   - Fix (text): `"Research on the 2018 tariffs found nearly all of the tariff showed up in US import prices."`
   - Fix (say): `"Research on the twenty eighteen tariffs found nearly all of the tariff showed up in US import prices."`
6. **lines[7]: "rose less" has no comparison point, and the study's subject is unclear.**
   - Problem: The line doesn't say less than what, or that the study covered the 2018 tariffs.
   - Fix (text): `"But a 2021 study of the 2018 tariffs found store prices rose less than import prices, as retailers ate some."`
   - Fix (say): `"But a twenty twenty-one study of the twenty eighteen tariffs found store prices rose less than import prices, as retailers ate some."`
7. **lines[4] scene (minor): the Squirrel side is unclear.**
   - Problem: "$100" under "Squirrel" can read as Squirrel paying $100.
   - Fix: `"right": {"label": "Squirrel", "value": "-$10", "tone": "neutral", "sub": "keeps $100 price"}`
8. **lines[2] (minor): "US company" isn't always accurate.**
   - Problem: The importer of record can be a non-resident or foreign entity.
   - Fix (text and say): `"The importer, usually the US company bringing the goods in, pays it to US Customs."`
9. **post.tiktok: "~90%" is vaguely attributed and "US buyers" is the wrong group.**
   - Problem: "research says ~90% lands on US buyers" doesn't name the source or the year. The finding covers US firms and consumers, not just buyers.
   - Fix: `"Who really pays a tariff? The importer pays Customs; a NY Fed study estimated US firms and consumers bore nearly 90% of 2025 tariff costs. Not financial advice. #moneytok #personalfinance #tariffs #financeprostv"`
10. **post.ig and post.yt_desc (minor): state the 90% as an estimate.**
    - Fix: Change "found US firms and consumers bore nearly 90%" to "estimated US firms and consumers bore nearly 90% of the economic burden of". This is for consistency with issue 4.

## Political neutrality
- The script stays neutral once issues 2, 4 and 9 are fixed: it attributes findings to studies, calls them estimates, and makes no evaluative claims about the policy.
- Posting-date risk: none. The script avoids IEEPA refunds, Supreme Court rulings and current rates.

VERDICT: FAIL

## Round 2 (editor)
- Hook reworded ("doesn't pay the border tariff"); hook/cover prop label "US" (5-char limit); cover title kept at 16 chars.
- lines[2] "usually a US company"; lines[4] Squirrel card "-$10 / keeps $100 price".
- lines[5] "nearly all of it hit US import prices"; lines[6] "estimated ... nearly 90% of the cost"; lines[7] "rose less than import prices".
- lines[8] caption "about $195 billion"; chart title "US customs, fiscal yrs".
- tiktok, ig, yt_desc: NY Fed attribution, "estimated".
VERDICT: PASS
