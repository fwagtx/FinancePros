# Fact-check: 2026-10-06-lf-business ("How casinos are designed to always win")

Checked on 2026-09-30 for posting on 2026-10-06. The .research.md brief and gen_*.py were not read.

## Verification limits (read this first)
Independent web checking was **not possible** in this run:
- The WebSearch budget for the session was already used up (200/200). Every query came back "search not performed".
- Firecrawl returned 402 (out of credits).
- The proxy blocked WebFetch and curl to every source tried: Wikipedia, gaming.nv.gov, sec.gov, americangaming.org, wizardofodds.com, UNLV, LVCVA, AP, Reuters, Review-Journal, Nevada Independent, casino.org, Google News, DuckDuckGo and Bing.

So every figure below is marked **VERIFIED-MATH** (recomputed with python), **CONSISTENT-WITH-KNOWLEDGE** (matches what I knew before my June 2026 cutoff, but not re-checked on the web this run) or **UNVERIFIED** (could not be checked, usually because it came out after my cutoff). None of the priority 2025/2026 figures could be confirmed against a live source. They need a second pass once search budget is available.

## Math recomputed (python)
| Line | Claim | Result |
|---|---|---|
| 24-27, 88 | $2/$38 = 5.26% American roulette | 5.263% OK |
| 28 | European 2.70%; "nearly doubles" | 1/37 = 2.703%; 5.26/2.70 = 1.95x OK |
| 35-36 | 3:2 on $10 = $15; 6:5 = $12 | OK |
| 37 | Blackjack 4.75% of hands (6 decks) | 2*(24/312)*(96/311) = 4.749% OK |
| 38, 41 | 6:5 adds 1.39 pts; baccarat 1.06 / 1.24 / 14.36% | Match standard Wizard of Odds values (CONSISTENT-WITH-KNOWLEDGE) |
| 52-54, 89, 92 | $1,000 x 7.1% = $71; $100 becomes $29; 71% of bankroll | Arithmetic OK (see caveat, issue 9) |
| 58 | $2.3B / $24.6B = 9.4% | 9.35% from the rounded inputs; OK only if unrounded 10-K values give 9.4% |
| 59, 61 | $1.54B / $6.13B = 25.2% | **25.12%** from the displayed inputs (rounds to 25.1%). Small; confirm from the 10-K (see issue 12) |
| 77 | 0.8 pt x $6.13B = $49M | $49.0M OK |
| 66-67 | 26.1% of $21.1B = $5.5B; rest "nearly three-quarters" | $5.51B; 73.9% OK. Rooms $7.1B = 33.6% |
| 81 | Interest $2.2B = "10.6% of revenue" | 2.2/21.1 = **10.4%**. 10.6% needs about $2.24B; show "$2.24B" or change the sub to 10.4% |
| 81-82 | $154.2M on $21.1B = "less than a penny per dollar" | 0.73 cents OK. -81% implies prior year about $812M (UNVERIFIED) |
| 16 | $50.94B + $16.96B + $10.74B vs $78.72B | Sums to $78.64B; about $0.08B not accounted for (AGA total may include other items). Fine because it is spoken as "about" |
| 43 | Slots $944.7M of $1.27B statewide, Aug 2026 | 74% of win, so "over 2/3" holds for August |
| 3 | 1.27 / 1.0314 | implies Aug 2025 about $1.231B (UNVERIFIED) |

## Claim status
- L1-2, cover, post: Nevada 2025 win $15.8B, "fifth straight record". The 2021-2024 run of records (about $13.4B, $14.8B, $15.5B, $15.6B) is CONSISTENT-WITH-KNOWLEDGE. The **2025 $15.8B total is UNVERIFIED**. The yt_desc says "nearly $15.8 billion" while the video says "$15.8 billion". Pick one wording.
- L3, L43: August 2026 figures ($1.27B, +3.14%, slots $944.7M) are **UNVERIFIED** (after my cutoff). Timing is plausible: NGCB releases August data in late September, and September data won't be out until late October, so "latest" is still true on Oct 6.
- L4, L78: LVCVA 2025 visitation of 38.5M, down 7.5%. CONSISTENT-WITH-KNOWLEDGE but UNVERIFIED.
- L9, L11, L85: March 19, 1931 (AB 98 signed), the 1955 Gaming Control Board and 1962 *Beat the Dealer* are CONSISTENT-WITH-KNOWLEDGE.
- L13-15 chart (AGA): 2019 $43.65B, 2020 about $30.0B ($29.98B), 2021 $53.0B, 2022 $60.42B and 2023 $66.5B are CONSISTENT-WITH-KNOWLEDGE. **2024 is shown as $72.04B**, but AGA's original release said **$71.92B**. It may have been revised later; confirm. The 2025 figures ($78.72B, $50.94B, $16.96B, $10.74B, $18.09B tax) and the growth rates (iGaming +27.6%, sports +22.8%) are UNVERIFIED. Checked against the originally reported 2024 bases ($8.41B, $13.78B), the growth works out to about +27.7% and +23.1%. Close, so the script probably uses revised bases.
- L44: Reg. 14.040's 75% minimum payback is CONSISTENT-WITH-KNOWLEDGE.
- L46: Statewide 2025 slot hold of 7.1% and the UNLV "tighter over the past decade" finding are UNVERIFIED.
- **L47: the UNLV quote is UNVERIFIED word for word.** Quotes must match exactly. The on-screen source says "2025 slot hold report", but the yt_desc cites the "UNLV ... slot hold report (2026)". That is an inconsistency.
- L48: "State regulators have said any tightening stays within legal limits" is attributed to regulators but not sourced. UNVERIFIED.
- L56-61, L76, L79: MGM 2025 10-K figures are **all UNVERIFIED**: $24.6B handle, $2.3B slot win, 9.4%, $6.13B drop, $1.54B win, 25.2% vs 24.4% (2024), and Strip revenue -4%, casino +3%, rooms -9%.
- L65-68, L81: FY2025 Nevada Gaming Abstract Strip figures are **all UNVERIFIED**: 51 casinos, $21.1B revenue, gaming 26.1%, rooms $7.1B, ADR $250.72, occupancy 89.06%, interest $2.2B, net income $154.2M (-81%).

## Issues

1. **Weak opening (L1).** The spoken hook is 12 words, "In twenty twenty-five, Nevada casinos won fifteen point eight billion dollars." That is about 4 to 4.5 seconds at normal pace, so over the 3-second target. It is also a bare statistic with no open question. The tension ("fewer visitors, yet a record") doesn't arrive until L4-5. **Fix:** put the paradox first, for example "Vegas lost three million visitors last year, and casinos still won a record." 7.5% of about 41.7M is about 3.1M, and "last year" is correct on Oct 6, 2026. Then give the $15.8B in L2.
2. **Caption and narration say different things (L10).** The caption reads "a casino tax looked a lot easier than mining"; the narration says "legal casinos meant license fees and taxes flowing in". The "easier than mining" claim is also unsupported. **Fix:** use the spoken version for both.
3. **Caption and narration say different things (L94).** The caption reads "It just needs you to keep playing"; the narration says "It just needs the games to keep going". **Fix:** make them the same (the spoken version is safer).
4. **Caption and narration differ in meaning (L17).** The caption says taxes came "on top of it", which suggests taxes are added to the $78.7B. The narration correctly says "from all of it". **Fix:** caption "…in gaming taxes from that revenue."
5. **Framing of "rooms out-earn gambling" (L6, L64-67, L90, yt_desc).** The Abstract's Strip gaming revenue (about $5.5B) is counted net of comps and promotional allowances under ASC 606. It is far below the Strip's monthly-report gaming *win*, which was roughly $8.5-9B a year in recent years (not re-verified). Comp value is moved into rooms and F&B. A viewer who knows the Strip "wins" about $8-9B will see a contradiction with $5.5B. **Fix:** add one clause, for example "Counted the way casinos report it, after comps and free play, gaming was only 26 percent…", or label the chart "Gaming (net of comps)".
6. **Unverified quote (L47).** It must be checked word for word against the UNLV report. If it can't be confirmed, paraphrase it without quote marks or the "quote" scene. Also make the report year match between L47 ("2025 slot hold report") and yt_desc ("(2026)").
7. **L81 on-screen sub "10.6% of revenue"** doesn't match $2.2B / $21.1B = 10.4%. Show $2.24B or change the sub to 10.4%.
8. **L42 "more than two-thirds of Nevada's gaming win".** On a calendar-year basis Nevada slots have run close to exactly two-thirds (about 66-68%), so "more than" is borderline. **Fix:** "about two-thirds", or tie it to August ("about three-quarters of August's win").
9. **Churn example (L52-54, L89, tiktok).** Expected loss = edge x amount *actually* wagered. With a $100 bankroll and $1 spins, many players bust before reaching $1,000 in bets, so the true average loss is at most $71. **Fix:** "If you cycle through $1,000 in bets, the average loss is $71." Softer wording such as "can eat" is acceptable, but L54's "on average, you walk out with $29" overstates it slightly.
10. **Causal overreach (L5).** "Fewer people, more money won. That's not luck. That's design." A record despite fewer visitors can also come from higher spend per visitor, baccarat hold, or locals casinos. **Fix:** "Fewer people, more money won. Luck doesn't explain that. The design does."
11. **AGA 2024 value (L13-14 chart).** $72.04B vs AGA's originally published $71.92B. Confirm the revision or use $71.92B.
12. **L59 25.2%** vs 25.12% from the displayed $1.54B / $6.13B. Confirm from the 10-K; if the 10-K says 25.2%, keep it.
13. **"$15.8 billion" vs "nearly $15.8 billion"** (video vs yt_desc). Use one consistent wording once the exact figure is confirmed.
14. **Minor caption/voice rounding** is fine: L29 "Five cents" vs "About five cents", L38 1.39 vs "one point four", L77 $6.13B vs "six point one billion". Not errors.
15. **Awkward to read aloud:**
    - L77 "zero point eight point swing" is clumsy. Say "That swing of less than one point, on six point one billion dollars of drop…"
    - L46's caption is very long for one screen. Split it across two lines or two captions.
    - L12's caption "Most of our numbers today come from it" isn't true: AGA, MGM and LVCVA supply many of them. Say "many of the numbers."
16. **Time words:** "today", "now", "latest" and "In August 2026" are all fine on Oct 6, 2026, and no stale news was found. The August data is the latest release until late October.
17. **Advice, predictions, politics:** none found. The 1-800-GAMBLER line and the education disclaimer are present and good.
18. **Cover and title payoff:** "The Math Always Wins." and "Designed to Always Win" are paid off in chapters 2-3. Chapter 5 ("not always on the books") qualifies them, which is honest. No change needed.

## Verdict rationale
The game math is right: roulette, blackjack and baccarat edges and the churn and variance arithmetic all check. The script still can't pass as-is. None of the priority 2025/2026 data could be verified this run: Nevada 2025 total, August 2026 figures, AGA 2025, MGM 10-K, Abstract FY2025, UNLV 7.1% and the UNLV quote. On top of that there are real caption/narration mismatches (L10, L94, L17), an on-screen percentage that doesn't match its own inputs (L81), and the ASC 606 framing gap behind the "rooms beat gambling" headline claim. Fix issues 2-7, then re-run verification with search budget available.

VERDICT: FAIL
