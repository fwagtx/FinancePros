# Fact-check: 2026-11-27-explainer (ACH vs wire vs instant)

Checked October 2, 2026 for a November 27, 2026 post. Sources: web search excerpts (Nacha, frbservices.org, The Clearing House/Payments Dive/ABA, help.venmo.com, bankofamerica.com fee schedule listing, Federal Register). bankofamerica.com blocked direct fetch, so the BofA fee is confirmed from search excerpts of the official schedule plus third-party fee sites. I redid all the math in python.

## Verified claims

| Claim | Status | Source |
|---|---|---|
| ACH 2020-2025: 26.8 / 29.1 / 30.0 / 31.5 / 33.6 / 35.2 B | Correct (each matches Nacha's annual release; 2025 = 35.2B, +4.9%) | nacha.org annual releases; FY25 infographic |
| "Usually 1-2 business days" for standard ACH | Fair. Under Nacha rules, ACH credits settle in 1-2 business days and debits by the next business day. Nacha says most settle in 1 day or less. Consumer apps often say 1-3 days. | nacha.org "majority settle in one business day or less" |
| "Often free" for standard ACH | Fair as a hedge. Most big banks and P2P apps do standard transfers for free. Some banks and businesses still charge per ACH, so "often" is the right word. | Venmo standard = free; general bank practice |
| Wires usually land the same business day | Correct if sent before the bank's cutoff. Fedwire does not run on weekends. The Fed's 22x6 expansion is not expected until 2028-29, so "business day" stays true. | frbservices / Federal Register 2025-19942 |
| BofA $30 outgoing domestic wire, schedule effective Aug 7, 2026 | Correct (incoming $15, international $45). Some sources say Premier tier gets the outgoing fee waived. | BofA Personal Schedule of Fees (eff. Aug 7, 2026) via search |
| RTP launched 2017 | Correct (Nov 2017) | TCH |
| FedNow launched July 2023 | Correct (July 20, 2023) | Federal Reserve |
| RTP limit $10M, Feb 2025 | Correct (effective Feb 9, 2025; was $1M from 2022) | Payments Dive, ABA Banking Journal, TCH |
| FedNow limit $10M, Nov 2025 | Correct (effective Nov 12, 2025; was $1M) | frbservices.org 11/12/25 notice |
| No change to either limit in 2026 | None found | search |
| Venmo instant 1.75%, min $0.25, max $25; standard free, 1-3 business days | Correct | help.venmo.com Instant / Standard transfer FAQs |
| Math: 1.75% x $1,000 = $17.50; 1.75% x $2,000 = $35, capped at $25 | Correct. The cap starts to apply at about $1,428.57. | python |

## Issues

1. **House rule broken: the hook is not dated on screen (line 1).** The hook has a fee that can change ($30), but the hook scene shows no date. This must be fixed.
2. **Hook timing and strength (line 1).** It is true and specific, but the 11 spoken words take about 4 seconds, which is over the 3-second target. Tighten it so the free-vs-$30 contrast lands by about 3 seconds.
3. **"Every transfer trades time for money" is false as an absolute (line 8).** Zelle and many bank RTP/FedNow sends are instant and free. Use "Most".
4. **The $10M limits are network maximums (line 5, IG post, YT description).** Banks and credit unions set lower per-customer limits, often far lower. FedNow's default participant limit is much lower too. As written, "both now take up to $10 million per payment" suggests any user can send $10M. Say "network limits".
5. **The TikTok caption makes one company's numbers sound like the whole industry.** "$30 by wire, $17.50 instant" turns BofA's wire fee and Venmo's instant fee into general prices. Name them.
6. **Minor: the BofA fee is not universal.** Premier-tier clients reportedly get the outgoing domestic fee waived. The current wording ("Bank of America charges $30 ... as of August 2026") is acceptable. Optional: "lists $30" (matches the post text). Re-check the fee schedule shortly before posting in case a new edition replaces the Aug 7, 2026 one.
7. **Minor: text and spoken words differ (line 6).** The caption starts with "Example:" but the narration drops it. No values differ, so this is fine.
8. **Minor: the "same day ach" tag** is not covered in the video. Optional swap: "venmo instant transfer fee".
9. **Checked with no problems found:**
   - Stale news: none.
   - Time words: "now" and "as of August 2026" are still correct on Nov 27, 2026.
   - Advice, price predictions or political opinion: none.
   - The cover and title ("Same $1,000: Free or $30?") are paid off.
   - On-screen values match the spoken ones.
   - Compare values ("$0", "$17.50") are within 7 characters.
   - No keep:true flags.

   Optional extra: the post date is the day after Thanksgiving, when ACH and Fedwire are closed but RTP/FedNow run. That could make a timely hook.

## Fixes (exact replacement fields)

**Line 1 (hook)**
- text: `Same $1,000. One transfer is free. Another costs $30.` (unchanged)
- say: `Same thousand dollars: one transfer's free, another costs thirty.` (9 words, was 11)
- scene.title: `2026: Free or [$30]?` (adds the on-screen date; other scene fields unchanged)

**Line 5**
- text: `Instant rails, RTP and FedNow, never close, and their network limits are now $10 million per payment.`
- say: `Instant rails, R T P and FedNow, never close, and their network limits are now ten million dollars per payment.` (20 words, same as before)
- scene: unchanged

**Line 8**
- text: `Most transfers trade time for money: slow and free, or fast and paid.`
- say: `Most transfers trade time for money: slow and free, or fast and paid.` (13 words, same)
- scene: unchanged

**Post**
- ig, sentence 3: `RTP (since 2017) and FedNow (since July 2023) settle in seconds, 24/7, with network limits up to $10M per payment.`
- yt_desc: change `with limits up to $10 million` to `with network limits up to $10 million`
- tiktok: `Same $1,000: free by standard ACH, $30 for a BofA wire, $17.50 for Venmo instant. Not financial advice. #moneytok #personalfinance #banking #ach #financeprostv`

Spoken word count after fixes: 148 (was 150), within 100-150.

VERDICT: FAIL

## Round 2 (editor)
Applied all fixes: the hook is dated "2026: Free or [$30]?" and spoken in 9 words; network limits are worded as network maximums; "Most transfers trade time for money"; the post captions are company-specific. The TikTok caption was trimmed to 145 characters ("free by ACH", 4 hashtags). VERDICT: PASS
