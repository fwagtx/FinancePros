# Fact-check: How the 401(k) changed retirement in America (LF Explained, posts Mon Jan 4, 2027, 4 PM CT)
Checked Nov 5, 2026. Method: independent web searches (WebSearch). dol.gov / ici.org / bls.gov PDFs were not opened directly; checks rely on search snippets of the official pages plus trade press (PlanSponsor, PlanAdviser, InvestmentNews, 401k Specialist, EBRI, EPI, KPMG, IRS newsroom). Flagged where only partly confirmed.
Spoken word count as submitted: 1,752 (in range 1,550-1,800). The fixes below keep it roughly the same.

## Verified claims
- ICI: 401(k) plans held $10.8T at June 30, 2026 (ICI Q2 2026 release, Sept 17, 2026; 401k Specialist, PlanAdviser, InvestmentNews). CONFIRMED.
- ICI: $8.9T at end of 2024. PLAUSIBLE. I could not pull the ICI Q4 2024 release through search. It fits the ICI series ($8.0T Q2 2024, $9.3T Q2 2025, $10.1T end 2025), and as I recall ICI's Q4 2024 release gave $8.9T of $12.4T in DC plans. Re-check on ici.org if possible.
- Revenue Act of 1978 added Sec. 401(k), effective Jan 1, 1980. Ted Benna (The Johnson Companies) had the idea in 1980. IRS proposed regulations allowing pre-tax salary-reduction contributions came Nov 10, 1981. CONFIRMED (ASPPA, Workforce, Stacker/CNBC histories). Benna's own plan took effect Jan 1, 1981, and the script doesn't contradict that.
- DOL/EBSA active participants. DC: 1980 19M, 1990 35M (EPI Figure A from EBSA Table E7). 2000 50.9M (DOL 2000 abstract: 50,874k). 2020 85.3M (EBRI from the DOL 2020 bulletin). DB: 1980 30 (EPI rounds; 30.1 not seen in a snippet), 1990 26M, 2020 12.01M (EBRI). 401(k)-only active in 2020: 72.2M (EBRI). These are consistent: 72.2M is a subset of 85.3M. 2010 DC 73M was NOT directly confirmed by search (the abstract snippet showed no totals), but it fits the trend. Caveat on line 26 (eligible counts as "active") is correct.
- Pension math: 1.5% x 30 = 45%; 45% x $60,000 = $27,000. Correct. 5 yrs x 1.5% = 7.5%. Correct.
- 4% rule: Bengen, "Determining Withdrawal Rates Using Historical Data," Journal of Financial Planning, Oct 1994. $27,000 / 0.04 = $675,000. Correct.
- Tax example: $3,000 x 12% = $360; $3,000 - $360 = $2,640. Correct (federal income tax only; FICA still applies, as the script says).
- Match: 50% on first 6% of $50,000 = $3,000 in, $1,500 match. 3% = $1,500 in, $750 match, $750 difference. Correct.
- Vesting: employer match up to 3-yr cliff / 6-yr graded (IRS Issue Snapshot). Own deferrals always 100% vested. CONFIRMED.
- 2026 limits (IR-2025-111, Nov 13, 2025): $24,500 deferral, $8,000 catch-up for 50+, $11,250 for ages 60-63, $72,000 total. CONFIRMED.
- 2027 limits: NOT announced by the IRS as of Nov 5, 2026. Milliman projects $25,500 deferral / $8,500 catch-up, but that is a projection only. The IRS usually announces in Oct/Nov, so the official 2027 numbers will very likely be out before Jan 4.
- Vanguard How America Saves 2026 (2025 data): 6% hardship withdrawals (record) vs 1.7% in 2020; 61% of plans auto-enroll vs 10% in 2006; 94% vs 64% participation (participant-weighted); 7.6% avg deferral; 12.1% avg total with employer; $167,970 average, $44,115 median balance. ALL CONFIRMED.
- BLS, March 2025 (released Sept 25, 2025): 72% access, 53% participation, 70% DC access, 14% DB access. CONFIRMED, BUT SUPERSEDED. BLS released March 2026 data on Sept 25, 2026: 72% access, 52% participation, 14% DB access, 70% DC access. See Issue 1.
- PPA signed Aug 17, 2006, with an auto-enrollment safe harbor, preemption of state law, and default-investment (QDIA) protection. CONFIRMED.
- SECURE 2.0 (Dec 29, 2022), Sec. 101 / IRC 414A. New 401(k)/403(b) plans set up after Dec 29, 2022 must auto-enroll for plan years starting 2025. Default 3%-10%, rising 1 point a year to at least 10%, max 15%. Exempt: 10 or fewer employees, and businesses in existence under 3 years. CONFIRMED. (Final 414A regs cleared OIRA Oct 16, 2026 and may publish before air. Nothing in the script would change.)
- Saver's Match: 50% match on up to $2,000 (max $1,000), phased out by income, for tax years beginning after Dec 31, 2026. Deposits come after the 2027 return is filed, so 2028. IRS/Treasury Notice 2026-48 EXISTS (Aug 7, 2026; KPMG, IFEBP, Groom, WTW, IRS newsroom). CONFIRMED.
- PBGC insures private DB pensions up to legal limits. CONFIRMED.
- Cover "A 1978 Accident." with $10.8T, and the post title: the video pays both off (lines 0-13, 76).
- Advice / politics: no buy/sell or price predictions, and no political opinion. The Saver's Match notice is tied to the "TrumpIRA" executive order, but the script rightly leaves that out. Line 53 is mildly nudging (Issue 6).

## Issues and exact replacements

### Issue 1 (MUST FIX, stale data): BLS figures superseded by the March 2026 release (Sept 25, 2026)
- Line 80, TEXT: "Now the gap. In March 2026, the BLS found 72% of private-industry workers had access to a plan at work."
  SAY: "Now the gap. In March twenty twenty-six, the Bureau of Labor Statistics found seventy-two percent of private-industry workers had access to a plan at work."
  SCENE: {"t": "stat", "label": "Can join a plan", "value": "72%", "tone": "neutral", "sub": "BLS, March 2026"}
- Line 81, TEXT: "But only 52% actually took part. So only about half of private-sector workers were saving in a plan at work."
  SAY: "But only fifty-two percent actually took part. So only about half of private-sector workers were saving in a plan at work."
  SCENE: {"t": "compare", "title": "Private workers, 2026", "left": {"label": "Have access", "value": "72%", "tone": "neutral", "sub": "BLS"}, "right": {"label": "Take part", "value": "52%", "tone": "down", "sub": "BLS"}}
- Line 82: no change (100 - 72 = 28% still holds).
- Line 83, SCENE title: "Access, March 2026" (14% DB / 70% DC unchanged in 2026).
- post.yt_desc: replace "BLS, Employee Benefits in the United States, March 2025 (Sept 25, 2025)" with "BLS, Employee Benefits in the United States, March 2026 (Sept 25, 2026)".

### Issue 2 (MUST FIX, time words): "For 2026" limits written in present tense will read as current on Jan 4, 2027
The 2027 limits were not announced as of Nov 5, 2026. If the IRS announces them before lock, swap in the official 2027 figures and drop line 59's "check" line. If not, use past tense as below:
- Line 56, TEXT: "There are limits, too. For 2026, the IRS capped what you could put in from your own pay at $24,500."
  SAY: "There are limits, too. For twenty twenty-six, the I R S capped what you could put in from your own pay at twenty-four thousand five hundred dollars."
  SCENE: {"t": "stat", "label": "Worker cap, 2026", "value": "$24,500", "tone": "neutral", "sub": "IRS, Nov 2025"}
- Line 57, TEXT: "That year, workers 50 or older could add $8,000 more, and ages 60 to 63 could add $11,250 instead."
  SAY: "That year, workers fifty or older could add eight thousand dollars more, and ages sixty to sixty-three could add eleven thousand two hundred fifty instead."
- Line 58, TEXT: "Counting the employer's money, the 2026 cap on total contributions was $72,000."
  SAY: "Counting the employer's money too, the twenty twenty-six cap on total contributions was seventy-two thousand dollars."
- Line 59, TEXT: "The IRS updates these limits each year, so check irs.gov for the 2027 numbers."
  SAY: "The I R S updates these limits each year, so check I R S dot gov for the twenty twenty-seven numbers."
- Line 87, TEXT: "Three: the engine is the tax break plus the match, within yearly IRS limits, like $24,500 of your own pay in 2026."
  SAY: "Three: the engine is the tax break plus the match, within yearly I R S limits, like twenty-four thousand five hundred dollars of your own pay in twenty twenty-six."

### Issue 3 (MUST FIX, unsupported causal claim): Line 66
"Same kind of workers, same kind of paychecks" is not supported. Vanguard compares different plans (auto-enroll plans skew larger), not matched workers.
- Line 66, TEXT: "These are different plans, so it's not a perfect test. But the gap shows how much the default does."
  SAY: "These are different plans, so it's not a perfect test. But the gap shows how much the default does."

### Issue 4 (on-screen vs spoken): Line 25
The screen shows "72.2M" but the narrator says "about seventy-two million".
- Line 25, SCENE value: "72M" (keep TEXT/SAY). Or keep 72.2M and SAY "about seventy-two point two million".

### Issue 5 (awkward read-aloud): Line 34
- SAY: "Our math: twenty-seven thousand divided by four percent is six hundred seventy-five thousand dollars. That's what you'd need saved on day one to match that pension."
- TEXT: "Our math: $27,000 divided by 4% is $675,000. That's what you'd need saved on day one to match that pension."

### Issue 6 (advice tone, minor): Line 53
"Leaves $750 a year on the table" reads as an implied instruction to contribute more.
- TEXT: "Put in only 3%, and the match is $750. Our math: that's $750 a year less from the employer."
  SAY: "Put in only three percent, and the match is seven hundred fifty. Our math: that's seven hundred fifty dollars a year less from the employer."

### Issue 7 (minor, clarity): Line 68/69/70 list item "+1% a year"
The narration says "one point a year" (a percentage point).
- items: ["Auto-enroll", "3% to 10%", "+1 pt a year", "Opt out OK"] (on lines 68, 69, 70).

### Issue 8 (watch item, freshness): Lines 0, 1, 76, cover, post
"$10.8T as of June 2026" is dated, so it stays accurate. But ICI usually releases Q3 data in mid/late December, so by Jan 4 there will likely be a Sept 30, 2026 figure. If it's out at lock, update to it (and "June 2026" -> "September 2026" in lines 1 and 76, the stat sub "ICI, Sept 2026", and yt_desc "Q3 2026"). Otherwise leave as is.

### Issue 9 (hook, optional): Line 0
It is true, specific, and creates a clear curiosity gap. But spoken it is 12 words (~4 s), over the 3-second target. Optional tighter version:
- TEXT: "A 1978 tax accident now holds $10.8 trillion."
  SAY: "One tax accident now holds ten point eight trillion dollars." (10 words, ~3 s; the year stays on screen in the hook title "A [1978] tax rule")

## Not issues (checked)
- Line 79 compare shows "$168K" for the average. That is a rounding of the $167,970 spoken in line 78 and needed for the 7-character compare limit. OK.
- Line 71 "kicks in with 2027 contributions" is correct on Jan 4, 2027.
- Lengths: all replacements stay within field limits (stat label "Worker cap, 2026" = 16; compare title "Private workers, 2026" is a title, not a value).

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-7: BLS updated to March 2026 (72% access, 52% participation, 14% vs 70%; yt_desc source updated); 2026 limits in past tense with "check irs.gov for 2027" (L56-59, L87); L66 rewritten ("different plans, not a perfect test"); L25 value 72M; L34 "divided by 4%"; L53 no "on the table"; list item "+1 pt a year". Fix 8 noted ($10.8T dated June 2026, stays accurate). Optional hook change not applied. 1,764 spoken words. No remaining issues.
VERDICT: PASS
