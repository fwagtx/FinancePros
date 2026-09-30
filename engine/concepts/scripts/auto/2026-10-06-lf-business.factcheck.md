# Fact-check: 2026-10-06-lf-business ("How casinos are designed to always win")

Checked on 2026-09-30 for posting on 2026-10-06. I did not read the brief or the generators. I used 17 web searches. The official NGCB, cdcgaming, RJ and 8newsnow pages block direct fetch, so these checks rely on search excerpts. I recomputed all the math in python.

## Verified (no change needed)
- L1-2 / cover / post: Nevada 2025 gaming win of $15.80B (+1.2%) was the 5th straight record year (NGCB via Gaming Intelligence, casino.org, GGB). The Strip won $8.82B, flat.
- L3: August 2026 statewide win was $1,266,105,114, up 3.14% from $1,227,573,173 (NGCB release via Fox5/RJ/newsquawk).
- L4 / L78: LVCVA reports 38.5M visitors in 2025, down 7.5%.
- L6 / L65-68 / L81-82: Nevada Gaming Abstract FY2025 (51 Strip casinos). Total revenue was $21.1B (-3.7%). Gaming was $5.5B, 26.1% of the total. Rooms were $7.1B. ADR was $250.72 and occupancy about 89%. Interest expense was $2.2B ("over 10%" of revenue). Net income fell 81.2%, from $820.2M to $154.2M. The math checks out: 5.5/21.1 = 26.1%, non-gaming = 73.9% ("nearly three-quarters"), and 154.2/21,100 = 0.73 cents per dollar.
- L13-17 / L83-84: AGA reports 2025 GGR of $78.72B (+9.2%, a record). Traditional games were $50.94B, sports betting $16.96B (+22.8%), iGaming $10.74B (+27.6%) and taxes $18.09B. The chart points for 2019 ($43.65B), 2020 (~$30.0B), 2021 ($53.0B), 2022 ($60.42B) and 2023 ($66.5B) match AGA. For 2024, the chart shows 72.04. AGA first reported $71.92B, but 78.72/1.092 = 72.09, so a revised figure of about $72.0B is consistent.
- L9 / L11 / L85: History dates check out. AB 98 was signed March 19, 1931, during the Depression. The Gaming Control Board was created by the 1955 Legislature. Thorp's *Beat the Dealer* came out in 1962.
- L22-28 roulette: 2/38 = 5.263%, 1/37 = 2.703%, and the ratio is 1.95x ("nearly doubles"). The $38 bet returning $36 is correct.
- L35-38 blackjack: 3:2 on $10 pays $15 and 6:5 pays $12. The chance of a blackjack from 6 decks is 4.75% (1/0.0475 = 21 hands). Wizard of Odds lists 6:5 as costing 1.39 points of edge, and 4.75% x 0.3 = 1.43 before dealer-blackjack pushes, which is consistent.
- L41 baccarat: 1.06 / 1.24 / 14.36% are the standard 8-deck Wizard of Odds figures (tie paying 8:1).
- L44: Nevada Reg. 14.040 requires a theoretical payout of at least 75%. Correct.
- L46-47: UNLV reports 2025 statewide slot hold of 7.15% and says hold rose 26% over 10 years. The quote "Hold percentage — the portion of money gambled that the casino retains — has a huge impact on casino revenues" is word-for-word (RJ).
- L57-61 / L76-77 / L79: MGM 2025 10-K, Las Vegas Strip Resorts. Slot handle was $24,565M and slot win $2,306M (9.4%). Table drop was $6,127M and table win $1,541M, which is 25.2% (24.4% in 2024). Net revenue fell 4%, casino revenue rose 3% and rooms fell 9%. 0.8% x $6.13B = $49.0M.
- L53 / L89 / L92: 7.1% x $1,000 = $71, leaving $29.

## Issues

1. **L43: wrong number (FAIL).** On-screen "$944.7M" and spoken "about nine hundred forty-five million" do not match the reports. RJ/8newsnow reporting of the NGCB data says statewide slots won **$865.7 million in August 2026, +6.1%**. The check is consistent: 865.7/1,266.1 = 68.4%, which supports the "over 2/3" claim, while 944.7 would be 74.6%.
   **Fix:** Use "$865.7M" on screen. Say "about eight hundred sixty-six million dollars."
2. **L17: misleading on-screen text.** The caption says taxes were collected "on top of it", but the taxes come out of the $78.7B. The narration correctly says "from all of it."
   **Fix:** Change the caption to "...about $18 billion in gaming taxes from it."
3. **L10: on-screen text differs from narration and is unsourced.** The caption says "a casino tax looked a lot easier than mining", but the narration says "legal casinos meant license fees and taxes flowing in."
   **Fix:** Make the caption match the narration.
4. **L94: on-screen text differs from narration.** The caption reads "It just needs you to keep playing." The narration says "It just needs the games to keep going."
   **Fix:** Pick one wording for both. The narration's version is the safer one.
5. **L1: weak opening.** The line is true and specific, but the spoken line is 11 words, about 3.5 to 4 seconds. On its own it is a bare stat with no open question. The tension ("fewer visitors, still a record") does not arrive until L4.
   **Stronger version (under 3s):** "Vegas lost visitors in 2025, and casinos still won a record." Put the $15.8B figure in L2.
6. **L81: small mismatch.** The sub-label "10.6% of revenue" gives $2.2B / $21.1B = 10.4% when recomputed. The 10.6% only works with unrounded interest of about $2.24B, and the reports only say "over 10%."
   **Fix:** Use "over 10% of revenue" or "about 10%."
7. **L46 / L53 / L89 / L92: rounding.** UNLV's 2025 hold is 7.15%, which normally rounds to 7.2%, not 7.1%. The "about" wording keeps this defensible.
   **Optional fix:** Say "about 7%" in narration, or use 7.15% and recompute ($71.50, leaving $28.50).
8. **L54: worked-example caveat.** "On average you walk out with $29" assumes all 1,000 spins are played. With a $100 bankroll, some players go broke earlier, so the average amount wagered is under $1,000 and the average amount left is a bit above $29. Also, "hold" is realized win, not the machine's built-in edge.
   **Fix:** "If you play all 1,000 spins, the expected loss is $71."
9. **L48: loose paraphrase.** Regulators (Rusty LeBlanc and Jeremy Eberwein of the NGCB) said casinos cannot set machines beyond the legal hold limit or adjust individual machines unnoticed. They did not say that "any tightening stays within legal limits."
   **Fix:** "State regulators say machines can't be set outside legal limits, and they're audited."
10. **L77: awkward narration.** "Zero point eight point swing" is hard to say.
    **Fix:** "That swing of less than one percentage point, on six point one billion dollars of drop, is worth about forty-nine million dollars."
11. **L16: minor.** Under the title "Where the $78.72B came from", the three parts add up to $78.64B, not $78.72B. This is AGA rounding or other revenue, and is acceptable. Optionally, retitle it "Main sources of the $78.72B."
12. **L47 source label (minor):** The label says "2025 slot hold report", but yt_desc says "UNLV ... (2026)". Make them consistent, for example "UNLV Center for Gaming Research (data through 2025)".

## Other checks
- **Time words:** "latest numbers" (August 2026) stays accurate on October 6, because September data comes out in late October. There is no "this week" or "yesterday" wording.
- **Stale news:** none.
- **Advice or price predictions:** none. L92 frames the edge as a price of entertainment, which is educational. The 1-800-GAMBLER line and the disclaimer are present.
- **Political opinion:** none.
- **Cover and title payoff:** "The Math Always Wins" and "Designed to Always Win" are paid off in chapters 2 and 3. Chapter 5 adds nuance ("wins at the table, not always on the books") without undercutting the title.
- **yt_desc:** "nearly $15.8 billion" is fine (the actual figure is $15.80B). The CHAPTERS placeholder is ignored as instructed.

VERDICT: FAIL
