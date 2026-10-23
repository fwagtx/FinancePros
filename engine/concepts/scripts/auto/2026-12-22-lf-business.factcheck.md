# Fact-check: 2026-12-22-lf-business ("How Disney makes money")

Checked: Oct 23, 2026. Posts: Tue Dec 22, 2026. Read only `2026-12-22-lf-business.raw.json`.
**Line numbers below are 0-based indexes into `lines[]`.** All math was recomputed in Python.

## Verified (no change needed)
- FY2025 (ended Sept 27, 2025) revenue $94.4B, up 3% (94.425 / 91.361 = +3.4%). Segment revenue Ent $42.5B / Sports $17.7B / Exp $36.2B; segment OI $4.674B / $2.882B / $9.995B (record for Experiences; Ent +19%; Sports +19.8%, so "Up 20%" on line 67 is OK). Source: Disney Q4 FY2025 release (Nov 13, 2025) and FY2025 10-K. The Sports full-year OI of $2.882B was not shown in a search excerpt, but it matches the +20% and the 10-K tables.
- Derived numbers: Exp share of revenue 38.3%, share of segment OI 56.9% (57%). Margins: Ent 11.0¢, Sports 16.3¢, Exp 27.6¢ (28¢). Ent+Sports = $7.556B (~$7.6B). All correct.
- Entertainment sub-lines for FY2025 (10-K): Linear Networks revenue $9,364M (-12%), OI $2,955M (-14%, ~$3.0B); DTC OI $1,327M (vs $143M); Content Sales/Licensing OI $392M. Lines 56-58 OK.
- DTC chart (lines 46-49): FY22 -$3.424B, FY23 -$2.496B, FY24 +$0.143B, FY25 +$1.327B. These are on the **restated Entertainment DTC basis** (excludes ESPN+). FY2022 as originally reported, including ESPN+, was about -$4.0B. The chart is internally consistent; the swing is $4.75B ("nearly $5 billion" is OK). Optional: change the chart title to "Ent. streaming op. inc." Not required.
- Q3 FY2026 (quarter ended June 27, 2026; reported Aug 5, 2026): Entertainment SVOD OI $712M vs $329M (restated); SVOD revenue $5.53B, so the margin is 12.9% (13%). Sports OI $858M (-17%). Experiences OI $3.02B (+20%), helped by a ~$100M tariff refund. Total segment OI ~$5.6B. Lines 54, 55, 71, 79, 80 OK.
- Disney+ Premium went from $18.99 to $21.49 effective Sept 23, 2026 (Bloomberg/Variety via TVLine, 9to5Google, Cleveland19). 12 x 21.49 = $257.88, which is more than one $209 ticket. Lines 51-52 OK.
- Subscriber reporting dropped starting FY2026, announced Aug 2025 (line 53) OK. Disney+ launched Nov 2019 OK. ESPN DTC at $29.99 in Aug 2025 OK. Epic Universe opened May 2025 OK. D'Amaro named Tue Feb 3, 2026, effective Mar 18, 2026 OK. AP, Sept 19, 2023: "$60 billion... nearly double what it spent in the prior 10-year period" OK.
- 2026 Magic Kingdom adult one-day ticket $139-$209; $209 falls on select late-Nov/Dec 2026 dates; kids 3-9 pay $5 less (TouringPlans, Theme Park Shark, planDisney). Math: 2x209 + 2x204 = $826; 2x139 + 2x134 = $546; difference $280. OK.
- 1971 $3.50 with rides extra, 1987 $28, June 2012 $89: supported by the AllEars ticket-increase guide and Spectrum News 13 (2014). This is fan-site and press history, not Disney filings, so it needs attribution (see fix).
- Disney Adventure: maiden voyage Mar 10, 2026 from Singapore; 8th DCL ship; ~6,700 guests is maximum capacity (4,222 at double occupancy).
- keep:true continuity: every keep:true line uses the same template as the line before it. Field limits: all within limits. Mid-video hook scenes (lines 38, 78, 90) speak 17/13/21 words. Treated the 12-word limit as applying to the opening hook only (line 0 = 12 words).

## Issues and fixes (exact replacement text, 0-based line index)

1. **Line 70: STALE / misleading (must fix).** The NFL-ESPN deal **closed around Jan 31, 2026** after DOJ review (AP, Feb 1, 2026; ESPN). The NFL now owns 10% of ESPN (Disney 72%, Hearst 18%). "Subject to approvals" is out of date.
   - text: `In early 2026, ESPN closed a deal giving the NFL a 10% stake in ESPN, in exchange for NFL Network and other media assets.`
   - say: `In early twenty twenty-six, ESPN closed a deal giving the NFL a ten percent stake in ESPN, in exchange for NFL Network and other media assets.`
   - scene.headline: `NFL now owns 10%`; scene.source: `AP, ESPN, Feb 2026`

2. **Line 0: hook framing (should fix).** "Earns more" is ambiguous. On *revenue* the claim is false (Exp $36.2B vs Ent+Sports $60.1B). It is true only for segment operating income. "Movies, streaming and ESPN" also leaves out TV networks, which are part of the $7.6B. The wording below is accurate, stronger, and 12 words:
   - text: `Disney's parks make more profit than movies, TV, streaming and ESPN combined.`
   - say: `Disney's parks make more profit than movies, TV, streaming and ESPN combined.`
   - Present tense: this was true in FY2025 ($10.0B vs $7.6B). It also held for 9M FY2026 per reported quarters: Exp ~$3.3B + $2.62B + $3.02B vs Ent+Sports ~$1.1B + $0.19B + $1.34B + $0.65B + $1.7B + $0.86B. The Q1 FY26 figures are approximate. Re-confirm after FY2026 results on Nov 17 (see item 6).

3. **Post copy: match the hook (should fix).**
   - post.title (<=90): `How Disney makes money: its parks out-profit movies, TV, streaming and ESPN combined` (84 chars)
   - post.ig: `Disney's parks division made $10.0 billion in operating income in fiscal 2025, more than movies, TV, streaming and ESPN combined.`
   - post.tiktok (<=150): `Disney's parks make more profit than its movies, TV, Disney+ and ESPN combined. Here's how Disney really makes money.` (117 chars)
   - yt_desc: change `ESPN and Fox Business (Aug 2025)` to `ESPN and Fox Business (Aug 2025); AP (Feb 1, 2026); AllEars ticket price history`.

4. **Line 40: unsupported attribution (must fix).** No source says Disney announced "five more ships by 2031" *at the Adventure launch*. Disney's standing plan (announced earlier) is a 13-ship fleet by 2031, which means 5 more after ship #8.
   - text: `Disney plans five more ships by 2031, for 13 in all.`
   - say: `Disney plans five more ships by twenty thirty-one, for thirteen in all.`
   - (scene unchanged: "Ships planned" / "+5" / "By 2031")

5. **Lines 27-28: weak sourcing on ticket history (should fix).** The figures match AllEars and Spectrum News, but "December 1987" is not supported (sources give only 1987). "Any Disney World park" in 2012 is looser than the sources, which list the Magic Kingdom price.
   - Line 27 text: `By 1987, after ride coupons ended, a one-day ticket was $28, according to fan site AllEars.`
   - Line 27 say: `By nineteen eighty-seven, after ride coupons ended, a one-day ticket was twenty-eight dollars, according to fan site AllEars.`
   - Line 28 text: `By June 2012, a one-day Magic Kingdom ticket was $89.`
   - Line 28 say: `By June twenty twelve, a one-day Magic Kingdom ticket was eighty-nine dollars.`

6. **Staleness: FY2026 full-year results arrive before posting (should fix / pre-post gate).** Disney has confirmed Q4 and full-year FY2026 results for **Tue Nov 17, 2026**, five weeks before this posts. The script always labels FY2025 and the June-2026 quarter explicitly, so nothing it says is false. Nothing calls FY2025 "latest" or "last year". But viewers will have FY2026 numbers by then. Minimum fix is to say upfront which data the video uses:
   - Line 6 text: `Numbers come mostly from Disney's fiscal 2025 filings and its mid-2026 reports. This is education, not advice.`
   - Line 6 say: `Numbers come mostly from Disney's fiscal twenty twenty-five filings and its mid twenty twenty-six reports. This is education, not advice.`
   - Strongly recommended: after Nov 17, re-check that FY2026 Experiences OI is still greater than Ent + Sports (hook, lines 0-3, post copy) and that nothing contradicts the FY2026 release. Updating to FY2026 is better if time allows.

7. **Line 39: capacity wording (minor).** 6,700 is the maximum capacity.
   - text: `In March 2026, the Disney Adventure began sailing from Singapore. It's the line's eighth and largest ship, for up to about 6,700 passengers.`
   - say: `In March twenty twenty-six, the Disney Adventure began sailing from Singapore. It's the line's eighth and largest ship, for up to about six thousand seven hundred passengers.`

8. **Line 30: minor precision (optional).** In Feb 2016, Disney World began seasonal pricing (value/regular/peak) for one-day tickets. Full date-based pricing for all tickets came in Oct 2018. Optional text/say: `That's date-based pricing, which Disney World started for one-day tickets in 2016. Busy days cost more, quiet days cost less.` (say: `...in twenty sixteen...`)

9. **Line 86 list item "Streaming: +$" (style nit).** It reads oddly. Suggest `Streaming: +` → `D+: profitable` (14 chars). Not required.

## Other checks
- No advice, no price predictions, no political opinion. Lines 84-85 disclaim and contain no buy/sell instruction. The "example family" is labeled as hypothetical with 2026 prices. The 1957 chart claim is fine.
- On-screen values match spoken values throughout.
- Spoken words: currently 1655. With fixes 1, 2, 4, 5, 6, 7 applied: **1666** (within 1550-1800). Fix 8 adds 3 more words (1669).

## Sources
Disney Q4 FY2025 release and FY2025 10-K (sec.gov, investors.thewaltdisneycompany.com); Q3 FY2026 coverage (Benzinga, GuruFocus, Beancount, MarketBeat, WDWInfo); Disney Q4 FY2026 date (Disney Oct 12, 2026 release; LaughingPlace; BlogMickey); TVLine / 9to5Google / Cleveland19 (Sept 23, 2026); AP / NBC News / ESPN (NFL deal closed, Feb 1, 2026); Wikipedia / TTG Asia / CruiseHive (Disney Adventure); Fox affiliates (D'Amaro, Feb 2026); AP (Sept 19, 2023, $60B); TouringPlans / Theme Park Shark / planDisney (2026 prices); AllEars ticket-increase guide, Spectrum News 13 (2014), Travelweek (price history).

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-9. Recheck hook vs FY2026 results after Nov 17, 2026.
VERDICT: PASS
