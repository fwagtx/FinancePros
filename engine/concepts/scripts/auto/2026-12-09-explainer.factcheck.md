# Fact-check: 2026-12-09-explainer (How Stablecoins Stay at $1)
Checked Sat Oct 10 2026 by an independent checker. Video posts Wed Dec 9 2026 (evergreen). Line indexes are 0-based.

## Claims verified
- L1, $305B total stablecoin market cap, Sep 2026, DefiLlama: CONFIRMED. DefiLlama-based write-ups give $305.25B on Sep 14 2026 and $305.10B on Sep 21 2026 (USDT ~60%, USDC ~$74B). "About $305 billion ... as of September 2026" is correctly dated and will still be true as a dated figure on Dec 9.
- L2, reserves of cash + T-bills: TRUE IN SUBSTANCE, slightly overstated. USDC is backed by cash plus the Circle Reserve Fund (T-bills and repos). Tether's reserves are mostly T-bills and reverse repos, but they also include gold, bitcoin and secured loans. "Cash and Treasury bills" with no qualifier is too absolute for "big issuers" in general. Fix below.
- L3, arbitrage: the mechanism is CORRECT, but "traders" can't all redeem. Only approved or verified customers can mint or redeem with the issuer: Circle Mint is an institutional, KYB-gated account, and Tether's direct redemption has a $100k minimum. Retail users trade on exchanges. Fix below.
- L4, Circle Q2 2026 reserve income of $668M: CONFIRMED by the Circle 8-K / press release of Aug 5 2026 ($668M, +5% y/y; reserve return rate 3.5%; total revenue and reserve income $701M). The math checks out: $76.5B average circulation x 3.5% / 4 = $669M. One wording risk: "The issuer keeps the interest" is too strong. Circle pays a large share of reserve income to distribution partners (mainly Coinbase), and some platforms pass rewards to holders. "Earns" is accurate. Fix below.
- L5, attestation vs audit: ACCURATE. An attestation is a point-in-time check of the reserve assertion and is not a full financial-statement audit. Tether's BDO reports are explicitly limited to the reporting date.
- L6, USDC in March 2023: CONFIRMED. Circle disclosed on Mar 10 2023 that $3.3B (about 8% of ~$40B in reserves) was at SVB. USDC hit about $0.87 overnight on Mar 11 (some sources, e.g. The Block, say $0.88). "About 87 cents" is fine.
- L7, "USDC recovered in days": CONFIRMED. The Fed/FDIC/Treasury backstop came Mar 12 2023, and Circle's Mar 13 release says the de-peg closed.
- L7, TerraUSD: algorithmic, collapsed in May 2022 (about 16 cents by May 13), and traded around a penny later in 2022. "About a penny in 2022" is defensible. "With no cash backing" is FAIR: Luna Foundation Guard held about $3B in bitcoin, not cash, and spent it trying to defend the peg. The on-screen sub "algorithmic, 2022" is correct. Optional, safer wording: "sank to pennies in 2022".
- L8: correct summary. No advice.
- L9: CTA, fine.

## Issues (with exact fixes)
1. **L0 hook / cover / post titles: "exactly" is misleading (MUST FIX).** Stablecoins trade near $1 with small deviations, and this same video shows USDC at 87 cents. Saying "exactly" sets up a claim the video then contradicts.
   - L0 say: `Why does this crypto coin stay worth about one dollar?` (10 words; the total is unchanged)
   - L0 text: `Why does this crypto coin stay worth about $1?`
   - Hook title "Why always [$1]?" and cover title "Why Is This Coin Always $1?": acceptable as questions the video answers (and partly debunks). Safer: cover `Why Does This Coin Stay at $1?`
   - post.title: `How a crypto coin stays worth about $1`
   - post.ig first line: `Why does a stablecoin stay worth about $1?`
   - post.tiktok: `How a crypto coin stays worth about $1, and when it doesn't. Not financial advice. #moneytok #personalfinance #stablecoins #crypto #financeprostv`
2. **L1 renderer limit: stat sub "DefiLlama, Sep 2026" is 19 characters, over the 18 limit (MUST FIX).** Replace with `DefiLlama Sep 2026` (18).
3. **L2: "cash and Treasury bills" overgeneralizes (SHOULD FIX).** Tether also holds gold, bitcoin and loans.
   - say/text: `Big issuers back each coin mostly with cash and T-bills.` (10 words; unchanged)
   - board line 2: `mostly cash + T-bills` (21)
4. **L3: implies any trader can redeem (SHOULD FIX).**
   - say: `Under a dollar, approved traders buy and redeem for a dollar. Over a dollar, they mint and sell.` (18 words, +1)
   - text: `Under $1, approved traders buy and redeem for $1. Over $1, they mint and sell.`
   - With fixes 1 and 3 the spoken total is 138 (at the limit).
5. **L4: "keeps the interest" (SHOULD FIX).**
   - say: `The issuer earns the interest: Circle reported six hundred sixty-eight million in the second quarter of twenty twenty-six.`
   - text: `The issuer earns the interest: Circle reported $668 million in Q2 2026.`
   - post.ig: change "Issuers keep the interest" to `Issuers earn the interest`. post.yt_desc: change "issuers keep the interest" to `issuers earn the interest`.
   - post.ig line 3 also says "traders redeem coins under $1 and mint coins over $1". Make it `approved traders redeem coins under $1 and mint coins over $1`.
6. Minor / optional: L7 "about a penny" could be `pennies`. The value "~1¢" can stay.

## Other checks
- Opening: a strong, specific question, about 3 seconds at 10 words. It is true once "exactly" is changed to "about".
- Time words: everything is dated (Sep 2026, Q2 2026, Mar 2023, 2022). Nothing will go stale by Dec 9.
- No advice, no price predictions, no politics. "Not financial advice" is present in the posts.
- On-screen values match the spoken ones on every line ($305B, $668M, 87¢, $3.3B, ~1¢).
- One company's numbers are labeled as Circle's and not generalized to the industry. Line 2's generalization is addressed in fix 3.
- Renderer limits: everything is within limits except the L1 sub (fix 2). Compare values "~$1" and "~1¢" are 3 characters each. No keep:true lines.
- Spoken words: 137 now, 138 after the fixes (limit 115-138).
- Posts: otherwise accurate. yt_desc "USDC hit about 87 cents in March 2023 after SVB failed" is correct.

Sources: DefiLlama data via TechFlow (techflowpost.com/en-US/newsletter/136066); Circle 8-K, Aug 5 2026 (sec.gov ... augustepr-circle_q22026f.htm); circle.com/pressroom/3-3-billion-of-usdc-reserve-risk-removed-dollar-de-peg-closes; Decrypt / The Block on SVB; The Block and CoinDesk on LFG reserves; Spark / eco.com on attestations and Circle Mint.

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-5: "exactly" → "about" in L0/title/IG/TikTok; L1 sub "DefiLlama Sep 2026"; L2 "mostly with cash and T-bills"; L3 "approved traders"; L4 "earns". Cover kept (checker: OK as is; alternative exceeds 28-char title limit). Spoken total 138.
VERDICT: PASS
