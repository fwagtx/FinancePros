# Research brief: How Google makes money from free (posts Jan 5, 2027; researched Nov 6, 2026)

Show: How They Make Money (long-form). Education only, neutral, no stock talk.

## Timely angle
- Alphabet reported Q3 2026 (quarter ended Sept 30, 2026) on Oct 28, 2026: revenue $127.6B, up 25% year over year. (Alphabet Q3 2026 earnings release / 8-K Exhibit 99.1; coverage: 9to5Google, TheDesk, NewsBytes, Oct 28-29, 2026.) Evergreen framing: "in the July-September 2026 quarter".

## Core facts (Alphabet filings)
Annual revenue, Alphabet, fiscal years (10-Ks; $ billions):
2015 75.0 (74.989) | 2016 90.3 (90.272) | 2017 110.9 (110.855) | 2018 136.8 (136.819) | 2019 161.9 (161.857) | 2020 182.5 (182.527) | 2021 257.6 (257.637) | 2022 282.8 (282.836) | 2023 307.4 (307.394) | 2024 350.0 (350.018) | 2025 402.8 (402.836)
Sources: Alphabet 10-K FY2017 (2015-2017), FY2019, FY2025 10-K; Macrotrends series; FY2025 first year above $400B (TheWrap, Outlook Business, Feb 2026).

FY2025 revenue mix (FY2025 10-K, filed Feb 2026):
- Google Search & other: $224.532B (2024: $198.084B). Growth driven by paid clicks +6% and cost-per-click +7% (10-K).
- YouTube ads: $40.367B (2024: $36.147B). YouTube ads + subscriptions topped $60B in 2025 (Alphabet Q4 2025 call; MediaPost, Feb 2026).
- Google Network: $29.792B (2024: $30.359B), down on lower AdSense.
- Google advertising total: $294.691B = 73.2% of revenue (our math: 294.691 / 402.836).
- Google Cloud: about $58.7B (2025, +36%) (sum of quarters; beancount.io analysis; Q4 2025 Cloud $17.7B, +48%, Neowin).
- Subscriptions, platforms & devices: about $48B (2025) (analysis $48.1B; Q4 2025 $13.578B in release). Somewhat uncertain: say "about $48 billion".

Latest quarter, Q3 2026 (July-Sept 2026), reported Oct 28, 2026 (8-K Ex. 99.1, 10-Q):
- Total revenue $127.6B, +25%.
- Search & other $63.35B, +12% (neoteo, money365; consistent with Q3 2025 $56.57B).
- YouTube ads $11.2B, +9% (Cord Cutters News, TheDesk).
- Google Network $7.455B (Q3 2025 $7.354B).
- Google advertising total $82.012B (Q3 2025 $74.182B) = 64% of revenue (our math 82.012/127.6).
- Google Cloud $30.7B, +103% (Q3 2025 $15.16B); Cloud operating margin 36.2% vs 23.7% in Q3 2025.
- Subscriptions, platforms & devices $14.29B, +11%.
- Total TAC $16.366B (Q3 2025 $14.876B); TAC rate 20.0% of ad revenue (10-Q).
- Capex $51.4B; free cash flow about -$9.1B (single-source analyses; not used).

## How a search ad auction works (Google Ads Help + industry guides)
- Advertisers bid on keywords; ads are ranked by Ad Rank, which combines the bid with ad quality (expected clickthrough rate, ad relevance, landing page experience) plus context.
- Quality Score: a 1-10 diagnostic per keyword based on those three parts (Google Ads Help).
- Advertisers pay per click (CPC). Actual CPC is often less than the max bid: you pay about what's needed to beat the ad below you (Google Ads Help "actual CPC").
- Common simplified textbook formula (not Google's exact formula): Ad Rank = max bid x Quality Score; Actual CPC = (Ad Rank of the ad below / your Quality Score) + $0.01.

## Worked examples (our math)
0) 10-year growth: 402.836 / 74.989 = 5.37 -> about 5.4x (2015-2025).
1) Ads per day, 2025: $294.691B / 365 = $807.4M per day; / 24 = $33.6M per hour; / 31,536,000 seconds = $9,345 per second.
2) Simplified auction: Ann bids $4.00 with Quality Score 5 -> Ad Rank 20. Ben bids $3.00 with Quality Score 8 -> Ad Rank 24. Ben gets the top spot despite the lower bid. Ben pays 20 / 8 + $0.01 = $2.51 per click.
3) TAC share Q3 2026: $16.366B / $82.012B = 20.0% -> about $1 of every $5 of ad revenue paid to partners.

## Traffic acquisition costs (TAC) and Apple
- TAC = payments to distribution partners (browsers like Safari, phone makers, carriers) and Network partners (sites showing Google ads).
- Google paid Apple $20 billion in 2022 to be Safari's default search engine (court documents unsealed May 2024 in US v. Google; Bloomberg, AppleInsider, 9to5Mac, May 1-2, 2024).
- Google shares 36% of Safari search ad revenue with Apple (testimony by Google's economics expert Kevin Murphy, Nov 2023; Bloomberg/CNBC/The Verge).

## Antitrust (strictly neutral)
- Aug 5, 2024: Judge Amit Mehta (US District Court, D.C.) ruled Google illegally maintained a monopoly in general search and search text ads. Quote: "Google is a monopolist, and it has acted as one to maintain its monopoly." (opinion, Aug 5, 2024; AP, CNBC).
- Sept 2, 2025 remedies: no forced sale of Chrome or Android; Google barred from exclusive distribution contracts for Search, Chrome, Assistant, Gemini; payments to partners for placement still allowed; Google must share certain search index and user-interaction data with qualified competitors, overseen by a technical committee (AP, The Hill, Digiday, Stanford Law, Sept 2025; Google's appeal challenges the data sharing and technical committee oversight, PYMNTS 2026).
- Appeals: Google filed notice of appeal Jan 16, 2026; DOJ and states cross-appealed seeking stronger remedies; briefing at D.C. Circuit through mid-2026 (PYMNTS May 2026, Bloomberg Government, MLex). No appeal decision found as of Nov 6, 2026.

## AI context (confirmed figures only)
- Q3 2025 call (Oct 2025): Gemini app over 650 million monthly active users (Alphabet).
- AI Overviews: over 2 billion monthly users (Alphabet Q2 2025 call, July 2025).
- Q3 2026: Alphabet said Search query growth hit a five-year high; ads expanding into AI Mode (call coverage, Oct 2026). Gemini "1 billion users" from transcript only: not used.

## History timeline
- 1998 Google founded; Oct 2000 AdWords launches; 2002 pay-per-click auction with quality; 2004 IPO; 2006 buys YouTube ($1.65B); 2015 Alphabet formed.

## Surprising fact
- In 2025, Google's ads brought in about $807 million a day (our math), and you never paid a cent directly.

## Chapters
1. The free trick (product is the ad slot; history)
2. Inside the ad auction (CPC, Quality Score, worked example)
3. The money machine in numbers (chart 2015-2025, 2025 mix)
4. Paying for the front door (TAC, Apple $20B, 36%)
5. The court case (2024 ruling, 2025 remedies, appeals)
6. Beyond ads (Cloud, subscriptions, Q3 2026, AI)
7. What it means + recap

SOURCES:
- Alphabet Form 10-K FY2025 (filed Feb 2026), FY2019, FY2017; Alphabet Q4 2025 earnings release (Feb 4, 2026)
- Alphabet Q3 2026 earnings release, 8-K Ex. 99.1 and 10-Q (Oct 28, 2026); coverage: 9to5Google, TheDesk, NewsBytes, Cord Cutters News, neoteo (Oct 28-29, 2026)
- Macrotrends Alphabet revenue series; TheWrap / Outlook Business (Feb 2026); Neowin / beancount.io Q4 2025 analysis (Feb 2026); MediaPost (Feb 2026)
- Google Ads Help: actual CPC, Quality Score
- Bloomberg via AppleInsider / 9to5Mac (May 1-2, 2024): $20B to Apple in 2022; Bloomberg/CNBC (Nov 2023): 36% share
- US v. Google, Mehta opinion Aug 5, 2024 (AP, CNBC); remedies decision Sept 2, 2025 (AP, The Hill, Digiday, Stanford Law)
- PYMNTS (May 2026), Bloomberg Government, MLex (2026): appeals
- Alphabet Q2 2025 and Q3 2025 earnings calls (July / Oct 2025): AI Overviews, Gemini users
