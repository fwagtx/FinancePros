# Fact-check: 2026-12-18-explainer (economies of scale)

Checked on Mon Oct 19, 2026, for posting on Fri Dec 18, 2026. Source: `2026-12-18-explainer.raw.json` only. I used 8 web searches and recomputed the math in python.

## Verified claims

| Line | Claim | Status | Source |
|---|---|---|---|
| 6 | Costco FY2026 net sales were $297.2B (52 weeks ended Aug 30, 2026) | CORRECT. The figure is $297,247M, up 10.1% from $269.9B | Costco Q4/FY2026 release of Sep 24, 2026 (8-K Ex. 99.1); FY2026 10-K |
| 6 chart | FY2019 149.4, FY2020 163.2 | CORRECT. The figures are $149,351M and $163,220M | FY2020 10-K and release |
| 6 chart | FY2021 192.1, FY2022 222.7 | CORRECT. The figures are $192.05B and $222.73B | FY2022 release and annual report |
| 6 chart | FY2023 237.7, FY2024 249.6 | CORRECT. FY2023 was a 53-week year, which does not matter at this scale | FY2024 8-K and 10-K |
| 6 chart | FY2025 269.9 (the missing point) | CORRECT | FY2026 release ("from $269.9 billion last year") |
| 7 | Costco gross margin of 11.1% in FY2026 | CORRECT. The 10-K gives 11.09% of **net sales** ($32,968M / $297,247M = 11.09%). FY2025 was 11.12% | FY2026 10-K |
| 7 | Kroger gross margin of 22.9% in FY2025 | CORRECT. Kroger's release says "Gross margin was 22.9% of sales for 2025 compared to 22.3% last year" | Kroger Q4/FY2025 release of Mar 5, 2026 |
| 4-5 | Acorn math | CORRECT. 10 acorns: ($100 + $10) / 10 = $11.00. 1,000 acorns: ($100 + $1,000) / 1,000 = $1.10. 1.10 / 11 = 0.10, so the hook's "90% less" is right. The example is labeled "made up" on screen and in the narration | python |

### How the two companies define gross margin
- **Costco:** gross margin is net sales minus merchandise costs, as a percent of net sales. Membership fees ($5.907B in FY2026) are **not** in net sales. Measured against total revenue ($303.15B), the margin would be a different number. The script's 11.1% therefore uses Costco's own net-sales basis, which is correct.
- **Kroger:** gross margin is a percent of sales, and Kroger has no membership-fee revenue. Both figures are **sales-based ratios that exclude membership fees**, so the numbers are like-for-like. Two caveats remain:
  - The fiscal years differ. Kroger's FY2025 ended around Jan 31, 2026, and Costco's FY2026 ended Aug 30, 2026. The script labels both years.
  - The cost line items each company counts are not identical, and the product mix differs: Costco's sales include fuel and its ancillary businesses, Kroger's include pharmacy and fresh food.

  Neither caveat needs a script change.

### Kroger FY2026 Q3
Kroger is expected to report FY2026 Q3 in early December, before Dec 18. That is a quarterly figure. The full-year FY2025 figure of 22.9% stays the latest full-year number, so no change is needed. I did not check Kroger's FY2026 year-to-date margins.

## Issues

### 1. (Must fix) Line 7: crediting the thin margin to volume alone is misleading
The line "It says volume helps it run thin" implies scale alone lets Costco live on an 11.1% gross margin.
- In FY2026, membership fees were $5.907B (up 11%), about **50% of Costco's roughly $11.7B operating income**. The fees are the main reason Costco can price merchandise near cost.
- An economies-of-scale explainer that leaves this out overstates what scale explains.
- Separately, "It says" points at Costco's 10-K language: high sales volume and rapid inventory turnover let it operate at lower gross margins. I could not confirm the exact wording in a search excerpt, so the paraphrase is plausible but not verified word for word.

**Fixes (exact replacement text):**
- `text`: `Volume plus membership fees let it run thin: an 11.1% gross margin (FY2026), versus Kroger's 22.9% (FY2025).`
- `say`: `Volume plus membership fees let it run thin: an eleven point one percent gross margin, versus Kroger's twenty-two point nine.`
  - This is 20 words, one more than the current 19, so the spoken total goes from 137 to **138** (within the 115-138 limit).
- `scene.left.sub` (optional): `FY26, ex-member fees` is 20 characters, which is too long. Use `fiscal 2026` (unchanged) or `FY26 net sales` (14 characters).
- `post.ig`: replace `and it says volume helps it profit on an 11.1% gross margin (FY2026) vs. Kroger's 22.9% (FY2025).` with `and volume plus $5.9B in membership fees let it profit on an 11.1% gross margin (FY2026) vs. Kroger's 22.9% (FY2025).`
- `post.yt_desc`: replace `and it says volume helps it profit on an 11.1% gross margin (FY2026)` with `and volume plus $5.9 billion in membership fees let it profit on an 11.1% gross margin (FY2026)`.

### 2. (Minor) Line 7: spoken narration leaves out the fiscal years shown on screen
The fiscal years are shown in the compare subs, and the numbers match the spoken ones, so this is acceptable. No change is needed.

### 3. (Minor) Line 6: one company's figure, used as an illustration
This is fine. The script does not generalize Costco's figure to all warehouse clubs.

## Other checks
- **Hook:** it is true within the labeled example, specific, and about 2.5 seconds spoken. Fine.
- **Time words:** "fiscal 2026" will still be correct on Dec 18, since Costco's FY2027 Q1 is reported around Dec 10 and is only a quarter. There is no "this week" or "today".
- **Advice and predictions:** none. Nothing instructs viewers. The call to action asks only for a follow.
- **Politics and allegations:** none. There are no quotes in the script.
- **Character limits:**

  | Field | Value | Length | Limit | OK |
  |---|---|---|---|---|
  | Compare values | $11.00 / $1.10 / 11.1% / 22.9% | 6 / 5 / 5 / 5 | <=7 | Yes |
  | Compare subs | longest is "$1,100 / 1,000" | 14 | <=18 | Yes |
  | Board lines | longest is "Sack: $1 per acorn" | 18 | <=20 | Yes |
  | Split items | longest is "Same at any size" | 16 | <=16 | Yes |
  | List items | all | within | <=16 | Yes |
  | Chart end label | $297.2 | 6 | <=6 | Yes |
  | Prop label | $1.10 | 5 | <=5 | Yes |
  | post.title | | 48 | <=60 | Yes |
  | TikTok | | 148 | <=150 | Yes |

- **Spoken words:** 137 now, 138 after fix 1.
- **keep:true:** no lines use it.
- **Cover and title payoff:** "Why Bigger Costs Less" and "-90%" are paid off on lines 4-5.

VERDICT: FAIL
