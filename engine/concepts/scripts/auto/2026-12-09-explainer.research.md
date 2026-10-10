# Research brief: Stablecoins, how a crypto coin stays pegged to a dollar
Slot 2026-12-09-explainer (evergreen, posts Wed Dec 9 2026). Researched Sat Oct 10 2026.

## Mechanics (definitions)
- Fiat/reserve-backed stablecoins (USDT, USDC) hold reserves of cash and short-term US Treasury bills (plus repos / money market funds) meant to equal tokens outstanding.
- Mint/redeem at $1: an approved customer deposits $1 with the issuer and gets 1 new token; redeeming burns the token and returns $1. Access is mostly for institutions/exchanges (Tether: $100,000 minimum direct redemption; recent guides say fee is the greater of $1,000 or 0.1%; $150 verification fee). Retail trades on exchanges.
- Arbitrage keeps the market price near $1: below $1 -> buy cheap on market, redeem with issuer for $1 (supply shrinks); above $1 -> mint at $1, sell above $1 (supply grows). (Spark, Banxa, Eco explainers; Circle describes mint/burn.)
- Attestations: accounting firm checks reserve balances on ONE date; not a full audit. Tether Q2 2026 attestation by BDO, assurance limited to June 30 balances.
- Issuer keeps the interest on reserves; holders usually get none.
- Algorithmic (TerraUSD/UST): no cash/bond reserves; peg relied on swapping UST for sister token LUNA. Failed May 2022.

## Key numbers (dated)
- Total stablecoin market cap: ~$305.25B as of Sep 14, 2026 (DefiLlama via TechFlow); $303.82B Sep 2, 2026 (DefiLlama sum via Axis Intelligence); record ~$322-323B May 2026. USDT ~60%, USDC ~24% (Sep 2026).
- Tether Q2 2026 (attestation released Jul 31, 2026, BDO): ~$1.5B net operating profit; T-bills $114.96B; reverse repos $25.62B; assets $187.75B vs liabilities $183.64B (June 30, 2026); excess reserves $4.11B (down from $8.23B Mar 31). Also holds gold (146.2 t, $18.84B) and bitcoin ($5.8B).
- Circle Q2 2026 (release Aug 5, 2026): reserve income $668M (+5% y/y); reserve return rate 3.5%; avg USDC circulation $76.5B; period-end USDC $73.3B; total revenue + reserve income $701M; net income from continuing ops $48M.
- USDC reserves largely in Circle Reserve Fund (USDXX), SEC-registered gov't money market fund managed by BlackRock, custodied at BNY Mellon, plus bank cash.

## When backing is in doubt
- USDC, March 10-11, 2023: Circle disclosed $3.3B of reserves (~8% of ~$40B) at failed Silicon Valley Bank. USDC fell to ~$0.87 (Decrypt, Axios; The Block says $0.88 low). Circle said it would cover any shortfall; peg restored after the FDIC/Fed backstop of SVB deposits on Mar 12, 2023 (back near $1 within days).
- TerraUSD (UST), May 2022: algorithmic; ~$18B market cap before collapse; fell to $0.65 on May 9, 2022 (CoinDesk); ~$0.16 by May 14; about 1 cent by early June 2022. LUNA went from ~$80+ to near zero; ~$40-45B in combined value wiped out (estimates vary). Terraform Labs filed Chapter 11 Jan 2024.

## Worked example (exact math)
1. Arbitrage: trader buys 100,000 coins at $0.98 = $98,000; redeems with issuer for 100,000 x $1.00 = $100,000; gross gain $2,000 before fees (Tether fee could be $1,000 at that size). Buying pressure pushes the price back toward $1.
2. Issuer income: Circle avg circulation $76.5B x 3.5% annual rate / 4 quarters = $669M, matches reported $668M Q2 2026 reserve income.

## Surprising fact
Holders usually earn nothing on the dollars behind their coins; the issuer keeps the Treasury interest: Circle reported $668M of reserve income in a single quarter (Q2 2026), Tether ~$1.5B operating profit.

## Chartable series: total stablecoin market cap (approx, year-end, $B; trackers differ)
- 2021: ~150-167 (CoinLedger 149.7; Bursa 167)
- 2022: 138 (Bursa)
- 2023: 130 (Bursa)
- 2024: 204 (Bursa)
- 2025: ~308 (Transak; single source)
- Sep 2026: ~305 (DefiLlama via TechFlow)
Caution: mixed sources; used only for context, not in script.

## Law
GENIUS Act already covered in Dec 3 short; not used.

SOURCES:
- TechFlow (DefiLlama data), Sep 14 2026: https://techflowpost.com/en-US/newsletter/136066
- Axis Intelligence, Sep 2 2026 DefiLlama sum: https://axis-intelligence.com/?p=41582
- Spark stablecoin tracker: https://www.spark.money/tools/stablecoin-market-cap-tracker
- Circle Q2 2026 results, Aug 5 2026: https://www.circle.com/pressroom/circle-reports-second-quarter-2026-results ; https://s206.q4cdn.com/265218871/files/doc_news/2026/Aug/05/CIRCLE_Q2-2026.pdf
- Tether Q2 2026 attestation coverage: https://forklog.com/en/tethers-excess-reserves-halve-in-q2/ ; https://stablecoininsider.org/tether-q2-2026-reserve-buffer-halved/ ; https://ground.news/article/stablecoins-worlds-largest-stablecoin-reports-15-billion-in-profits-in-q2-2026
- USDC/SVB: https://www.axios.com/2023/03/11/circle-usdc-peg-svb ; https://kakapo.decrypt.co/123224/circle-to-stand-behind-usdc-cover-3-3-billion-shortfall-held-in-silicon-valley-bank ; https://www.theblock.co/post/218993/usdc-and-dai-remain-at-about-0-90-following-circles-disclosure-of-funds-at-svb ; https://abc17news.com/money/cnn-business-consumer/2023/03/11/stablecoin-usdc-breaks-dollar-peg-after-revealing-3-3-billion-silicon-valley-bank-exposure/
- Terra/UST: https://coindesk.com/business/2022/05/09/ust-stablecoin-falls-below-dollar-peg-for-second-time-in-48-hours ; https://corporatefinanceinstitute.com/resources/cryptocurrency/what-happened-to-terra ; https://mattrickard.com/stablecoin-depeg
- Peg mechanics: https://www.spark.money/research/stablecoin-peg-mechanisms-compared ; https://banxa.com/learn/stablecoins-and-payments/how-do-stablecoins-stay-pegged
- Tether redemption terms: https://www.spark.money/tools/stablecoin-redemption-comparison ; https://cryptoslate.com/you-can-redeem-tether-usdt-11-on-tether-to-but-theres-a-catch/
- Year-end series: https://www.bursa.ro/stablecoin-market-growing-rapidly-22502751 ; https://coinledger.io/research/stablecoin-market-share-and-transaction-volume ; https://transak.com/blog/stablecoin-market-cap-2026
