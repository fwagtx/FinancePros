# Fact-check: 2026-11-05-explainer (posts Nov 5, 2026; checked Oct 1, 2026)

## Verified
- **L2 "2 in 3"**: Vanguard How America Saves 2026 says "nearly 2 of every 3 dollars contributed were invested in target-date funds" in 2025. The figure measures **contributions made during 2025**, not balances or assets. The L2 label "Contributions into target-date funds" and the sub "Vanguard HAS 2026, 2025 data" (28 chars) are correct.
- **L3 98%**: HAS 2026 says that among plans with a designated QDIA, 98% of the QDIAs were target-date funds and 2% were balanced funds. The claim is correct. A tighter wording would be "98% of Vanguard plans' default funds (among plans that chose one)", but this is optional.
- **L5/L6 glide path**: Vanguard holds 90% stocks until 25 years before the target date, falls to 50% at the target date, and reaches 30% seven years after it. Mapped to a retirement age of 65, that gives 25→90, 40→90, 65→50 and 72→30. All the chart points are correct.
- **L6 "through" fund**: This matches FINRA. A through fund reaches its most conservative allocation after the target date.
- **L7 FINRA quote**: The quote matches word for word: "A 'to retirement' target-date fund will reach its most conservative asset allocation on the date of the fund's name." The title "Save the Date: Target-Date Funds Explained" is correct. finra.org blocked direct fetch, so this was verified from search excerpts.
- **L8 fee series** (Morningstar's asset-weighted average expense ratio for target-date mutual funds):
  - 2021: 0.34% and 2022: 0.32%, both from the 2023 Target-Date Landscape.
  - 2023: 0.30%, from the 2024 Landscape.
  - 2024: 0.29% and 2025: 0.27%, from the 2026 Landscape. The 2025 Landscape also gives the 2024 figure.
  - All the chart points are correct.
- **Morningstar 2026 Landscape timing**: The 2026 edition is already out. Its PDF was posted around March 10, 2026, and it is the source of the 2025 figure of 0.27%. The next edition, which would report 2026 data, would normally come out around March 2027. No new figure should appear before Nov 5. Labeling the figure as "2025" is correct and will not go stale.
- **L9 math**: $10,000 × 0.27% = $27.00. The script labels it as an example. Correct.
- **Sub-labels**: All are 28 characters or fewer (28 and 27).
- **Advice and politics**: The script contains no fund recommendation, no "you should", no price prediction and no political content. The post carries a "not financial advice" disclaimer.
- **Cover and title**: "How the 401(k) Autopilot Works" is paid off by the video.
- **Spoken vs on-screen**: The spoken lines match the on-screen values in every line.

## Issues
1. **L1 hook / cover / post title: the claim is mislabeled (this must be fixed).**
   - "Nearly 2 in 3 dollars **saved** in Vanguard plans **ride** on autopilot" reads as 2 in 3 of the dollars sitting in the plans, meaning balances in the present tense.
   - The source statistic is 2 in 3 dollars **contributed in 2025**.
   - "On autopilot" also suggests all of that money was defaulted, but many participants choose TDFs themselves.
   - Fix: "Nearly 2 of every 3 dollars going into Vanguard 401(k)s last year bought one kind of fund." Shorter option: "Two of every three new 401(k) dollars at Vanguard buy one fund."
   - Make the same change to `post.title`, the IG and TikTok first lines, and keep the "2 in 3" cover value. The yt_desc wording ("contributed... in 2025") is already correct.
2. **L1 length**: The hook is 12 spoken words, which is about 3.5–4 s. The target is under 3 s. Either option from Issue 1 at about 10 words helps.
3. **L5: the age mapping is an assumption.** Vanguard defines its glide path by years to the target date, not by age. Fix: make the chart title "% stocks by age (retire at 65)", or say "for someone retiring at 65".
4. **L8 wording is imprecise.** "Morningstar's average target-date fee" leaves out that the figure is the asset-weighted average for **mutual funds**. CITs now hold more than half of TDF assets and are usually cheaper. Fix: "Fees too: the average target-date mutual fund fee was 0.27% in 2025, per Morningstar." The chart title "Avg TDF mutual fund fee" is already correct.
5. **Minor**: "Vanguard plans" means plans that Vanguard recordkeeps. "Vanguard-run plans" or "Vanguard 401(k)s" is clearer, but this is optional.

## Sources (search excerpts; official sites blocked direct fetch)
- Vanguard, How America Saves 2026, and the HAS 2026 preview (workplace.vanguard.com; 401kspecialistmag.com; napa-net.org)
- Vanguard TDF glide path page (workplace.vanguard.com/investment/strategies/tdf-glide-path.html)
- FINRA, Save the Date: Target-Date Funds Explained (finra.org)
- Morningstar Target-Date Landscape 2023, 2024 and 2026 (morningstar.com; plansponsor.com; nasdaq.com press release)

VERDICT: FAIL

## Round 2 (re-check of revised raw.json, Oct 1, 2026)

### Round 1 issues
1. **Hook mislabel: resolved in the narration.** The new L1 says "new ... dollars bought one fund type". L2 adds "In 2025" and the label "New 401(k) dollars into TDFs". Together they match HAS 2026: "nearly 2 of every 3 dollars contributed" in 2025.
   - **Still overclaims in two places, which drop the word "type":**
     - `post.title`: "Nearly 2 in 3 new Vanguard 401(k) dollars bought one fund". Readers will take this as a single fund, which is false. Fix: "...bought one fund type".
     - L1 `scene.title`: "One fund, [2 in 3]". Fix: "One fund type, [2 in 3]" or "[2 in 3] new dollars".
2. **Hook length: not fully resolved, but minor.** It is still 12 spoken words, about 3.5 s. "Two in three new Vanguard 401(k) dollars bought one fund type" (11 words) is slightly tighter. This alone does not fail the script.
3. **Retire-at-65 assumption: resolved.** The chart title "% stocks by age (retire at 65)" has 30 characters and the IG post says "assuming retirement at 65".
   - Nit: the L5 caption ends "(retire at 65)" but the narration does not say it. Either drop it from the caption, since the chart title carries it, or add "if you retire at 65" to the narration.
4. **Fee wording: resolved in L8 and IG.** The yt_desc still says "the 0.27% average fee in 2025 (Morningstar)". Fix: "the 0.27% average target-date mutual fund fee in 2025 (Morningstar)".
5. **"Vanguard 401(k)s": acceptable.** HAS covers all Vanguard-recordkept defined contribution plans, which are mostly 401(k)s. That makes "401(k)s" a mild simplification, not an error.

### Trims
- **L6** "Landing after the date makes it a 'through' fund." It is correct, but "the date" now has no clear antecedent. Fix: "after the target date" (10 words).
- **L10** "Same year, different ride inside." It is correct, and the list title and items still match.
- **L2, L3:** the facts are unchanged and correct. QDIA: 98% target-date, 2% balanced, from HAS 2026.

### Posts and cover
- **Cover "How the 401(k) Autopilot Works":** this is not an overclaim. The video explains the default fund (QDIA) and the automatic glide path. However, the word "autopilot" no longer appears anywhere in the narration. An optional fix is "In 2025, that was the target-date fund, the 401(k) autopilot, per Vanguard."
- **IG and TikTok:** these are accurate, include "fund type" and "in 2025", and have no advice framing.
- **yt_desc:** see item 4. **post.title:** see item 1.

### Sub-labels
- Both are within the limit: L2 "Vanguard HAS 2026, 2025 data" (28) and L3 "QDIAs, Vanguard 401(k), 2025" (28).

### Other checks
- Math is unchanged: $10,000 × 0.27% = $27.
- On-screen and spoken values match.
- The script contains no advice.

### Required to pass
- Restore "type" in `post.title`.
- Restore "type" in the L1 `scene.title`.

### Recommended
- Add "target-date mutual fund" to yt_desc.
- Change L6 to "after the target date".

VERDICT: FAIL

## Round 3 (orchestrator)
- post.title now "...one fund type"; L1 scene title "[2 in 3] new dollars".
- yt_desc says "average target-date mutual fund fee"; L6 "after the target date"; L5 caption retire-at-65 note left on chart title only.

VERDICT: PASS
