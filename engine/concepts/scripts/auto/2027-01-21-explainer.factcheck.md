# Fact-check: 2027-01-21-explainer (Acorn Economics, stock splits)

Checked Nov 22, 2026 for posting Thu Jan 21, 2027, noon Central. Every claim below was checked against web sources, not the brief.

## Claims verified
- **Nvidia 10-for-1 split.** It took effect after the close on Fri June 7, 2024 (record date June 6), and split-adjusted trading began Mon June 10, 2024. CONFIRMED.
- **Nvidia prices.** The June 7, 2024 close was $1,208.88, which is $120.88 split-adjusted. CONFIRMED. Fortune reported the shares rose about 1% on June 10, so no holder lost value because of the split.
- **Hook.** The per-share price did drop about 90% between the Friday close and Monday trading, which is a weekend. The claim is TRUE, and the video pays it off as a split in lines 1-5. The original said "stock price", which can be read as the company's value. Changed to "share price" (see issue 1).
- **Apple splits.** Apple went public Dec 12, 1980, then split 2-for-1 on June 16, 1987, June 21, 2000 and Feb 28, 2005, 7-for-1 on June 9, 2014, and 4-for-1 on Aug 31, 2020. That is 2 x 2 x 2 x 7 x 4 = 224. CONFIRMED.
- **Apple chart points.** The share counts below are CONFIRMED.

  | Year | Shares | Why |
  |---|---|---|
  | 1985 | 1 | No splits yet |
  | 1990 | 2 | After the 1987 split |
  | 1995 | 2 | No new splits |
  | 2000 | 4 | After the June 2000 split |
  | 2005 | 8 | After the Feb 2005 split |
  | 2010 | 8 | No new splits |
  | 2015 | 56 | After the 2014 split |
  | 2020 | 224 | After the Aug 2020 split |

- **Citigroup reverse split.** It was a 1-for-10 reverse split, effective 4:10 p.m. Fri May 6, 2011, with split-adjusted trading from May 9, 2011. Shares outstanding went from about 29 billion to about 2.9 billion. CONFIRMED.
- **Worked example.** 1 x $1,000 = $1,000 and 10 x $100 = $1,000. CORRECT.
- **Other checks.** I found no buy, sell or price-prediction advice and no political opinion. Line 8 ("doesn't bake a bigger one") states that a split does not create value. Anthropic is not mentioned.

## Issues found and fixed
1. **Line 0, hook.** "Stock price fell 90%" can be read as the company's value falling. Replaced with:
   - TEXT: "Nvidia's share price fell 90% in a weekend. Nobody lost anything."
   - SAY: "Nvidia's share price fell ninety percent in a weekend. Nobody lost anything."

   The hook is 12 spoken words. It is strong, specific, true, and makes the viewer need the answer.
2. **Line 2, narration and on-screen values.** There were two problems:
   - The spoken "about one twenty-one" is ambiguous out loud.
   - The right compare value showed "$120.88", but the narrator says "about $121".

   Replaced with:
   - TEXT: "Nvidia closed June 7, 2024 at about $1,209 a share. A 10-for-1 split made that about $121."
   - SAY: "...at about twelve hundred nine dollars a share. A ten-for-one split made that about a hundred twenty-one."

   The compare is now left "Before split" $1,209 (sub "$1,208.88 close") and right "After split" $121 (sub "$120.88 adjusted").
3. **Line 6, could go stale.** "Apple has split 5 times since its 1980 IPO" would become false if Apple splits before Jan 21, 2027. There was split speculation in July 2026, and I found no announcement. Reworded so the line stays true:
   - TEXT: "From its 1980 IPO to 2020, Apple split 5 times. One original share became 224 shares."
   - SAY: "From its nineteen eighty I P O to twenty twenty, Apple split five times. One original share became two hundred twenty-four shares."
4. **Post captions.** The IG, TikTok and YouTube captions were updated to match:
   - "share price"
   - the Apple wording bounded by 2020, with the split years listed in the IG caption
   - TikTok changed from "Nobody lost a cent" to the hook wording "Nobody lost anything", and shortened to 150 characters or fewer.

## Not changed
- The cover "Down 90%. Fine?" is paid off by the video.
- The hook title "Price cut, [no loss]" is fine.
- The Acorn Economics ending line is kept as written.
- There are no time words that will be wrong on Jan 21, 2027. "By 2020" and "May 2011" are fixed dates.

## Result after the fixes
- check.py: OK, with 10 lines and 139 spoken words.
- The JSON is valid.

## Sources
- Fortune: https://fortune.com/2024/06/10/nvidia-stock-split-10-for-1-rally-3-trillion-market-cap-ai-chips/
- Nasdaq: https://www.nasdaq.com/articles/nvidias-10-1-stock-split-has-arrived-heres-what-happens-next
- Yahoo Finance: https://ca.finance.yahoo.com/nvidia-stock-rises-after-10-for-1-stock-split-204412528.html
- StockInvest.us ($1,208.88 close): https://stockinvest.us/stock-news/nvidia-stock-price-ended-at-120888-on-friday-after-losing-00909-2024-06-07
- Yahoo Finance, Apple split history: https://finance.yahoo.com/news/apples-stock-split-history-everything-150100867.html
- Motley Fool, Apple split history: https://www.fool.com/investing/how-to-invest/stocks/stock-split/apple-history
- MacDailyNews (July 2026, speculation only, no split announced): https://macdailynews.com/2026/07/23/will-ternus-split-aapl-apple-stock-split-buzz-returns-near-record-highs/
- Citigroup 8-K press release (May 2011): https://www.sec.gov/Archives/edgar/data/0000831001/000119312511131957/dex991.htm
- Citigroup 8-K (March 2011 announcement): https://www.sec.gov/Archives/edgar/data/0000831001/000114420411016019/v215370_8k.htm

VERDICT: PASS

## Round 2 (editor)
Reviewed fixes; split framing is clear and evergreen; on-screen and spoken values agree.
VERDICT: PASS
