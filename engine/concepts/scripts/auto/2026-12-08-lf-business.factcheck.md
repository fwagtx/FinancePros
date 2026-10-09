# Fact-check: 2026-12-08-lf-business ("How Berkshire Hathaway works")

Checked Oct 9, 2026 for a Dec 8, 2026 post. Line numbers are 0-based indexes into `lines`. Spoken words are currently 1,757; after the fixes below they come to about 1,759, still inside 1,550-1,800. Only the script JSON was used; I did not read the brief.

## Must fix

### 1. Lines 44, 45, 87: Alphabet's rank and weight are wrong
The script says the order was Apple, then AmEx at about 17%, then Coca-Cola at about 11%, then Alphabet at about 9%. Reuters, working from the filing, reports that Berkshire held about 106M Alphabet shares (Class A and Class C) worth about **$37.8B** at June 30, 2026. That made Alphabet the **third-largest** holding. $37.8B of the about $299.3B 13F total is about **12.6%**. Coca-Cola is about 10.9% (fourth) and BofA about 9.2% (fifth). The "9.4%" figure that some aggregators show counts only one share class.
- **Line 44**
  - text: "Behind Apple came American Express at about 17%, and Alphabet, Google's parent, at about 13%."
  - say: "Behind Apple came American Express, at about seventeen percent, and Alphabet, Google's parent, at about thirteen percent."
  - scene items: ["Apple", "American Express", "Alphabet", "Coca-Cola"], reveal 3
- **Line 45**
  - text: "Then Coca-Cola at about 11%, with Bank of America close behind."
  - say: "Then Coca-Cola, at about eleven percent, with Bank of America close behind."
  - scene: same items as line 44, reveal 4, keep true
- **Line 87**
  - text: "Three: big stock bets, led by Apple, American Express and Alphabet, as of June 2026."
  - say: "Three. Big stock bets, led by Apple, American Express, and Alphabet, as of June twenty twenty-six."

### 2. Line 38: the OxyChem price is wrong
Berkshire announced the OxyChem deal (Oct 2025) and its Jan 2, 2026 close at **$9.7B**, all cash. The Q1 2026 10-Q says "approximately $9.5 billion". I found no source for $9.4B.
- text: "And the buying continued in 2026: about $9.7 billion for OxyChem in January, then about $6.8 billion for homebuilder Taylor Morrison in July."
- say: "...About nine point seven billion dollars for OxyChem in January, then about six point eight billion for the homebuilder Taylor Morrison in July."

Taylor Morrison checks out. It is a real Berkshire acquisition: announced about June 1, 2026 at $72.50 a share, shareholders approved it July 22, and it **closed July 24, 2026**. That price is about $6.8B of equity, or about $8.5B including debt, so "about $6.8 billion ... in July" is fine. Optional: change the scene source from "Berkshire 10-Q, Aug. 2026" to "Berkshire, July 2026", because the closing was announced by press release.

### 3. Line 1: stat sub is over the renderer limit
"June 30, 2026, 10-Q" is 19 characters and the limit is 18. Replace with sub: "June 30, 2026 10-Q" (18).

## Should fix (risky or imprecise)

### 4. Line 23: GEICO figure
$994M is GEICO's **pre-tax** underwriting profit for Q2 2026, down 45.4% from $1,821M in Q2 2025. That is confirmed in Berkshire's 10-Q and by CollisionWeek. Coverager's article mislabels the period (it calls it the "second half"), so it is a weak source to show on screen.
- text: "But underwriting can swing. In the quarter ending June 2026, GEICO's pre-tax underwriting profit fell about 45%, to $994 million."
- say: "...GEICO's pre-tax underwriting profit fell about forty-five percent, to nine hundred ninety-four million dollars."
- scene: headline "GEICO Q2 profit falls to $994M", source "Berkshire 10-Q, Aug. 2026"

### 5. Line 67: Abel's pledge wording
Abel pledged his **after-tax salary**. In March 2026 he bought about $15M of Class A shares, which was the after-tax value of his $25M salary, and he told CNBC he would do this each year, ideally for 20 years. The pledge was not in the letter, and he did not say "for as long as he's CEO".
- text: "Abel also said he would put his entire after-tax salary into Berkshire stock each year."
- say: "Abel also said he would put his entire after-tax salary into Berkshire stock each year."
- board: ["Abel's pledge: salary", "goes into Berkshire stock"] (each line 26 characters or fewer)

### 6. Line 46: Alphabet purchase amount
Estimates of the Q2 purchase run from about $15.5B (Class A $7.9B plus Class C $7.6B) to about $17B (Reuters and others). "About $15 billion" is a little low. Suggested say: "...Berkshire bought more than fifteen billion dollars of it, based on estimates from its filing." Make the same change in the text.

### 7. Lines 0, 24, 89, cover, and post titles: the hook needs a recheck before posting
The hook says "over $177 billion" in the present tense, without a date. The Q3 2026 10-Q, due in early November, will report float at Sep 30. If that number is below $177B, the hook, cover and posts become false. Check it before Dec 8 and adjust "$177B+" if needed. Every other figure in the script is dated. The Q3 13F (about Nov 14) will replace the June portfolio, but the script labels the portfolio "June 2026" throughout, so that is acceptable.

The "isn't its own" framing in the hook is fair. Float is policyholder money that Berkshire holds but owes back, and Buffett himself describes it as money "that doesn't belong to us" but that Berkshire gets to invest. The hook is 12 spoken words, true, specific and attention-grabbing, so it passes. It runs about 3.3 seconds, slightly over the target.

## Verified (no change needed)
- **Float.** $177.5B at June 30, 2026, up about $1.1B from year-end 2025 (Q2 release and 10-Q). Year-end 2025 is about $176.4B, so the chart's "$176B" is correct. Chart points 1970 $39M, 1980 $237M, 1990 $1,632M, 2000 $27,871M and 2010 $65,832M match the float table in the 2010 letter. 2015 at about $88B and 2024 at about $171B match those years' letters.
- **2025 operating earnings: $44,486M.** Insurance underwriting $7,258M; insurance investment income $12,513M; BNSF $5,476M (+8.8%); BHE $3,979M (+6.7%); manufacturing, service and retailing (MSR) $13,647M (+4.4%); other $1,613M. Insurance $7,258M + $12,513M = $19,771M, so "$19.77B" is correct, and all segments sum to $44,486M. Underwriting profit plus investment income makes "less than nothing" cost of float true for 2025.
- **BNSF revenue.** About flat in 2025 at about $23.4B (BNSF and Railway Age).
- **Q2 2026 operating earnings.** $12.98B vs $11.16B a year earlier, so "about $13.0B" and "$11.2B" are correct.
- **History.** Buffett took control in 1965. The two Omaha insurers (National Indemnity and National Fire & Marine) were bought in 1967 for about $8.6M, which is "under $9M". GEICO was fully acquired in 1996. BNSF: the 77.5% Berkshire didn't own was bought in 2010 for about $26.5B. The only dividend was 10 cents a share in 1967.
- **Employees.** About 387,800 at year-end 2025 (10-K).
- **13F at June 30, 2026.** Total about $299.3B. Apple: 227.9M shares worth $65.95B, 22.0%. AmEx 17.1%. Coca-Cola 10.9%. Berkshire was a net buyer of $19.8B ($23.5B bought, $3.7B sold), ending a 14-quarter run of net selling. BofA was trimmed (30.2M shares) for the fifth straight quarter. Apple was trimmed in Q4 2025 (about 10.3M shares) and in Q2 and Q3 2025.
- **Cash.** $359.2B in cash, equivalents and T-bills, net of payables, at June 30, 2026 (10-Q), vs $373.3B at year-end 2025 (10-K and Abel's letter). Both are dated correctly. T-bills were about $325B, so "most of it" sits in T-bills is correct.
- **Buybacks.** $4.8B in H1 2026, about $4.5B of it in Q2.
- **$30B floor.** Real. Berkshire won't repurchase if that would cut consolidated cash, equivalents and T-bills below $30B (10-Qs). The buyback rule (CEO, after consulting the chairman, judges the price below conservatively determined intrinsic value) is also described correctly.
- **Leadership.** Abel became CEO on Jan 1, 2026, and Buffett stays chairman. Abel has overseen the non-insurance businesses since 2018. His letter of Feb 28, 2026 says Buffett is in the office five days a week and kept the no-dividend policy. At the May 2, 2026 annual meeting, Abel took the stage and Buffett sat with the board. Buffett was born in 1930.
- **Line 77.** The letter called BNSF's performance gap with top rivals "too wide", so "needs to improve" is a fair paraphrase. PacifiCorp faces large wildfire claims and lawsuits, and they are framed as lawsuits, not as findings.
- **Line 78.** $8.26B write-down = Kraft Heinz $3.76B (Q2 2025) + Occidental $4.5B (Q4 2025).
- **Letter record.** The 1965-2025 compounded annual gains are 19.7% vs 10.5%, and the overall gains are 6,099,294% vs 46,061% (2025 letter, per Motley Fool and Coinpaper). Math check: $100 × 60,993.94 = $6,099,394 (about $6.1M), and $100 × 461.61 = $46,161. Lines 72-73 match the math. Note that the cumulative figures imply 19.8% and 10.6% a year over 61 years, but the letter prints 19.7% and 10.5%, so keep the letter's figures.
- **Line 74.** The S&P 500 10-year total return for 2016-2025 recomputes to 14.8% a year. I could not locate the exact Morningstar text for book value per share growing 12.4% a year, but it is consistent with book value per share rising from about $155.5K at end-2015 to about $500K at end-2025. It is low risk if the brief cites Morningstar directly.
- **Worked examples (lines 14-18, 60).** Labeled as made-up numbers, and the math is correct: $50 + $40 = $90, and -$20 + $40 = $20.
- **Advice and politics.** No advice, price predictions or political opinion. Line 7 is an "education, not advice" disclaimer. The tax point in line 61 is general and correct.
- **On-screen vs spoken.** Every spoken value matches its on-screen value. The keep:true lines all follow the same scene template. All other renderer limits are OK.

## Minor
- The "CHAPTERS" placeholder in yt_desc is empty. Make sure the pipeline fills it.

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-7: Alphabet #3 at ~13%, Coca-Cola ~11% (lines 44, 45, 87); OxyChem ~$9.7B; stat sub 18 chars; GEICO pre-tax + 10-Q source; Abel pledge "after-tax salary ... each year"; Alphabet "more than $15B"; float hook/cover/posts "about $177B" (dated in line 1); yt_desc empty CHAPTERS removed.
VERDICT: PASS
