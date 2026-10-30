# Fact-check: 2026-12-29-lf-business (How insurers make money: float)

Checked Oct 30, 2026 for a Dec 29, 2026 post. Claims were checked independently with web search (excerpts from Verisk/APCIA, AM Best/Business Wire, Howden, SEC/Progressive, Insurance Journal, Artemis, Captive.com and others). Direct fetches of verisk.com and nasdaq.com were blocked, so those checks rely on search excerpts. Math was recomputed in Python. Current spoken words: 1780. If every required and recommended fix below is applied: about 1793 (1787 without the optional line 92 change).

## REQUIRED FIXES

### 1. Hook/title mix two editions of the Verisk/APCIA 2023 numbers (lines[1], lines[2] scene, lines[36]/[37] chart, lines[49], post.title, post.ig, post.yt_desc)
- Verisk/APCIA's first 2023 full-year report (spring 2024) gives: underwriting loss **$21.1B**, combined ratio 101.6, net income after tax **$35.7B** (down 19% from $44B), and a revised 2022 loss of $24.8B at 102.4.
- Later reports revised 2023: the 2024 full-year report gives a **$21.8B** loss and **$40.9B** net income. The 2025 report rounds the 2023 loss to "$22 billion".
- So "lost about $22B ... still made $35.7B" pairs a revised loss with first-estimate net income. Each number has a source, but the pair never appears together in any single Verisk/APCIA report. Fix it by using one edition throughout. Option A below keeps $35.7B, so the cover, title value and most lines stay as they are.
  - **Option A (recommended): use the first 2023 report for both numbers ($21.1B loss, $35.7B net income).**
    - lines[1] text: "US property and casualty insurers lost about $21 billion on their policies in 2023, according to Verisk and the APCIA." / say: "US property and casualty insurers lost about twenty-one billion dollars on their policies in twenty twenty-three, according to Verisk and the A P C I A." / scene.left.value and lines[2] scene.left.value: "-$21B"
    - lines[36] and lines[37] scene.points: change [2023, -21.8] to [2023, -21.1]. This matches the 2022 point (-24.8), which comes from the same report.
    - lines[49] text: "That's how 2023 worked. Underwriting lost about $21 billion, but the float and the insurers' own capital kept earning." / say: "...Underwriting lost about twenty-one billion dollars, but..."
    - post.title: "Insurers lost $21B on policies in 2023 and still made $35.7B. Float, explained"
    - post.ig: "In 2023, US insurers lost about $21 billion on their policies and still earned $35.7 billion. The secret is float."
    - post.yt_desc first sentence: "In 2023, US property and casualty insurers lost about $21 billion on underwriting yet earned $35.7 billion in net income, according to Verisk and the APCIA's 2023 full-year report."
  - Option B: keep "$22B" and change net income to $40.9B in lines[1]/[2], the cover, post.title and post.ig. This needs more edits and changes the cover value.
- Word count: unchanged.

### 2. Camp Fire "$12.4 billion, per Verisk" could not be verified (lines[71])
- No Verisk/PCS source for $12.4B was found. Available figures: Munich Re about $12.5B insured; California Department of Insurance at least $11.4B; AIR (Verisk) $6-9B early estimate; PCS $13.8B for Camp and Woolsey combined.
- Replacement text: "The old wildfire record, the 2018 Camp Fire, cost insurers about $12.5 billion, per Munich Re." / say: "The old wildfire record, the twenty eighteen Camp Fire, cost insurers about twelve point five billion dollars, per Munich Re." / scene.left.value: "$12.5B" (+3 words)

## RECOMMENDED (accuracy and staleness)

### 3. lines[61]: name the Progressive investment-income measure
The $3.58B vs $2.83B figures (release, Zacks, Fintool) are **recurring** investment income. The 10-K also reports total investment income before expenses of about $4.3B (2025) vs $3.1B (2024). Without a label, a viewer who checks the 10-K could see a mismatch.
- text: "Its recurring investment income rose to about $3.6 billion in 2025, from about $2.8 billion in 2024." / say: "Its recurring investment income rose to about three point six billion dollars in twenty twenty-five, from about two point eight billion in twenty twenty-four." (+1 word)
- lines[64] and lines[65] scene.right.sub: "Recurring income". The "nearly three times" claim holds: 10.29/3.58 = 2.87x. Against the $4.3B total it would be about 2.4x, so the claim is safe only if the line names the recurring measure.

### 4. lines[45]: Fed sentence could read as stale by posting date
Trade coverage reports the Fed **raised** rates in Sept 2026 (to 3.75%-4.00%, held Oct 28, 2026), with markets pricing a possible December hike. This comes from secondary sources and was not checked against federalreserve.gov. Ending the rate story at "began cutting in Sept 2024" with no time anchor may look out of date on Dec 29, 2026. Anchor it to a year:
- text: "It began cutting in September 2024, but through 2025, rates stayed far above the near-zero years." / say: "It began cutting in September twenty twenty-four, but through twenty twenty-five, rates stayed far above the near-zero years." (+3 words)

### 5. lines[78]: make the Howden metric precise
Howden Re's 14.7% is the **risk-adjusted global property-catastrophe** rate decrease. That figure and "largest since 2014" are both confirmed. Other brokers measured smaller or similar drops: Guy Carpenter about -12%, Gallagher Re about -15%.
- text: "Reinsurance has its own cycle. At the January 2026 renewals, Howden Re says risk-adjusted property catastrophe reinsurance rates fell 14.7%." / say: "Reinsurance has its own cycle. At the January twenty twenty-six renewals, Howden Re says risk-adjusted property catastrophe reinsurance rates fell fourteen point seven percent." (0 words)

### 6. lines[92] (optional): "lending an insurer money, interest-free" is inaccurate
A premium is not repaid like a loan, and regulators often count expected investment income when rates are set. Suggested change:
- text: "So next time you pay a premium, remember: you're not just buying protection. You're also handing an insurer money to invest until claims come due." / say: same (+6 words). Cover value "0%" could become "FLOAT" if changed; optional.

### 7. lines[49]/[50] scene order (minor)
lines[49] shows the "$73.9B, AM Best, record" stat while the narration is about the $21B loss. lines[50] then shows "Lose on policies, win on bonds" while the narration says $73.9B. Swap the two scenes so each value appears when it is spoken.

### 8. lines[62] (minor)
"The yield on its recurring income was 4.1%" reads oddly. Progressive's own term is the "pretax book yield" on its portfolio. Searches did not independently confirm 4.1%. The figure is plausible, but treat it as weakly sourced. Option: "Its portfolio's book yield was four point one percent." (0 words)

## VERIFIED (no change needed)
- Combined ratios 2020-2025 (Verisk/APCIA): 98.6 and 99.6 (2021 report); 102.4 and 101.6 (2023 report; the first 2022 estimate was 102.7); 96.6 and 92.9 (2025 report). The chart mixes report editions, but each value is a published Verisk/APCIA figure. OK.
- Underwriting results: 2020 +5.2, 2021 -3.8, 2022 -24.8 (revised; the first estimate was -26.9), 2024 +23 (2025 report; the 2024 report said +24.8), 2025 +63. OK. 2023: see fix 1.
- Net investment income: $54.3B in 2021, up from $51.7B (Verisk/APCIA). $73.9B record in 2023, tied to higher rates (AM Best, May 28, 2024). $91.4B in 2025, +9.1% (AM Best First Look, Mar 2026). Lines 47/48 already disclose the change of source ("different counters"). OK.
- AM Best 2025: underwriting income $60.9B, nearly triple $22.1B; catastrophes 7.6 points vs 8.8. OK. Note: AM Best's 2025 combined ratio is 92.2, but the script consistently uses Verisk's 92.9 and attributes it, and lines[58]'s "about 7 cents" matches Verisk. OK.
- "Best underwriting year in about a decade" (lines[18]): AM Best coverage describes 2025 as "decade-high performance". OK.
- H1 2026 (Verisk/APCIA, Sept 2, 2026): combined ratio 92.7 vs 96.5; net written premium growth 2.1% vs 5.2%. Khemka warning on underlying risk confirmed. OK.
- Fed: first hike March 2022; 5.25%-5.50% in July 2023; first cut Sept 2024. OK.
- Progressive FY2025: combined ratio 87.4 vs 88.8 (12.6% vs 11.2% margin, 10-K). Net premiums written up 12% (2024 base $74.4B, so about $83.2B). Portfolio $97.4B vs $80.3B (10-K). 38.6M policies, +10%. Net income about $11.3B (secondary sources). 96 goal. OK.
- LA fires: Verisk Jan 22, 2025, $28B-$35B insured. OK. 2017: 103.7, $23.2B loss (ISO/PCI). OK.
- Math: 1,900/2,000 = 95, so $100; 1,400 x 4% = $56, total $156; 2,040, ratio 102, -$40; 1,540 x 4% = $61.60, net +$21.60 ("about $22" OK); ratio 110 gives -$200 vs at most about $68 of float income; 12.6% x $81.7B = $10.29B; 10.29/3.58 = 2.87x ("nearly three times" OK). All hypothetical examples are labeled.
- No advice or predictions: lines 81-87 are neutral and line 87 says "That's not a forecast." OK. No political opinion.
- keep:true lines all follow a line with the same template. Compare values are all 7 characters or fewer. Text and say match throughout.
- Opening (lines[0]): true and intriguing. It runs about 13 spoken words (about 4 s), slightly over the 3-second target. Optional tighter version: "In 2023, insurers lost billions on policies, and still profited." (-3 words)

VERDICT: FAIL

## Round 2 (editor)
- Option A applied: 2023 loss "about $21 billion" / -$21B (chart point -21.1) everywhere, consistent with $35.7B net income.
- lines[71]: Camp Fire $12.5B per Munich Re.
- lines[61],[64],[65]: "recurring investment income"; lines[45] "through 2025"; lines[78] risk-adjusted wording.
- lines[49]/[50] scenes swapped; lines[92] reworded (no "interest-free loan").
VERDICT: PASS
