# Fact-check: How Google makes money from free (posts Tue Jan 5, 2027, 4 PM CT; checked Nov 6, 2026)

## Verified (no change needed)
- FY2025 (Alphabet 10-K, filed Feb 5, 2026): total revenue $402.836B; Search & other $224.532B; YouTube ads $40.367B; Network $29.792B (2024 $30.359B, "decrease in AdSense revenues"); Google advertising $294.691B; paid clicks +6%, CPC +7%; Cloud $58.705B (2024 $43.229B, +35.8% = "about 36%"); subscriptions, platforms & devices $48.030B. YouTube ads + subs over $60B (Alphabet Q4 2025 call; Neowin/MediaPost Feb 2026).
- Revenue chart 2015-2025 (75.0, 90.3, 110.9, 136.8, 161.9, 182.5, 257.6, 282.8, 307.4, 350.0, 402.8): matches 10-Ks. 2021 +41.2%; 2015-2025 = 5.37x; first year above $400B: correct.
- Q3 2026 (10-Q for quarter ended Sept 30, 2026; release Oct 28, 2026): revenue $127.577B (+24.7%, "25%"); Search $63.350B (+12.0%); YouTube ads $11.207B (+9.2%); Google advertising $82.012B; TAC $16.366B (20.0% of ad revenue); Cloud $30.709B vs $15.157B (+102.6%, "103%"); Cloud op. income $11.121B vs $3.594B = 36.2% vs 23.7% margin; ads share 64.3%.
- Math: 294.691B/365 = $807.4M/day; /24 = $33.6M/hr; /31,536,000 s = $9,345/s; ads share 73.15% -> 73.2%; Ad Rank example 4x5=20, 3x8=24, 20/8+0.01 = $2.51, correctly labeled "simplified example, our math" and "Google doesn't publish its exact formula".
- Quality Score 1-10 per keyword with three components (Google Ads Help). AdWords 2000, IPO 2004, YouTube 2006, Alphabet 2015.
- Apple $20B in 2022 (court docs unsealed May 2024, Bloomberg); 36% Safari share (Google expert Kevin Murphy, Nov 2023 testimony, Bloomberg/CNBC).
- Mehta quote "Google is a monopolist, and it has acted as one to maintain its monopoly." (Aug 5, 2024) exact. Sept 2, 2025 remedies: no Chrome/Android sale, no exclusive contracts for Search/Chrome/Assistant/Gemini, payments allowed, data sharing with qualified competitors, technical committee. Final judgment entered Dec 5, 2025 (adds 1-year cap on default deals). Google appealed Jan 2026; DOJ and states appealed Feb 2026; "The appeals remain pending" (Alphabet Q3 2026 10-Q). No D.C. Circuit ruling found as of Nov 6, 2026; MacRumors/aggregators say decision not expected before 2027.
- AI Overviews 2B+ monthly users (Alphabet Q2 2025 call, July 2025).
- Spoken word count 1678 (in 1550-1800). Post title 50 chars, TikTok 117 chars. Cover/title paid off (lines 1, 45, 95). No advice, no price predictions; disclaimers at lines 5 and 89.

## Issues

1. Line 70 (scene + text) - REQUIRED. On-screen "Will appeal" is stale/wrong: Google already appealed (Jan 2026; line 68 says so). Also text says "Supporters" while the card says "Critics", and "supporters of the rules" is muddled because the DOJ is asking for tougher rules. Neutral replacement:
   - TEXT: The Justice Department says rivals need more room. Google says the rules hurt users. We'll leave that to the courts.
   - SAY: The Justice Department says rivals need more room. Google says the rules hurt users. We'll leave that to the courts.
   - SCENE: {"t": "split", "title": "Two views", "left": {"title": "DOJ", "items": ["More rivals", "Tougher rules"], "tone": "neutral"}, "right": {"title": "Google", "items": ["Hurts users", "Appealing"], "tone": "neutral"}}
   - Source: Alphabet Q3 2026 10-Q legal proceedings; MLex (DOJ/states seek harsher remedies, 2026).

2. Line 94 - REQUIRED. "ads made up a smaller share of revenue in 2026" claims a full-year 2026 result that won't be reported until Feb 2027; the script only supports the July-September quarter (64%).
   - TEXT: And it's growing Cloud fast, so ads were a smaller share of revenue by late 2026.
   - SAY: And it's growing Cloud fast, so ads were a smaller share of revenue by late twenty twenty-six.
   - Source: Alphabet Q3 2026 10-Q ($82.012B / $127.577B = 64%).

3. Line 69 (text/say + timeline scenes on lines 61, 63, 68, 69) - RECOMMENDED. Cross-appeal was filed in February 2026; make it specific and the timeline consistent. Keep the dated "As of November 2026" wording (true on Jan 5, 2027) but re-check for a D.C. Circuit ruling the week of posting.
   - TEXT: The Justice Department and states cross-appealed in February 2026, asking for tougher remedies. As of November 2026, the appeals court hadn't ruled.
   - SAY: The Justice Department and states cross-appealed in February twenty twenty-six, asking for tougher remedies. As of November twenty twenty-six, the appeals court hadn't ruled.
   - SCENE (all four timeline scenes): change {"when": "2026", "what": "DOJ cross-appeal"} to {"when": "2/26", "what": "DOJ cross-appeal"}.
   - Source: Alphabet Q3 2026 10-Q ("In February 2026, the DOJ and state Attorneys General also appealed. The appeals remain pending.").

4. Line 28 SAY - RECOMMENDED (awkward aloud). "That's two fifty-one" reads like a time/number, not money.
   - TEXT unchanged: And Ben doesn't pay his full $3. He pays just enough to beat Ann: 20 divided by 8, plus a penny. That's $2.51.
   - SAY: And Ben doesn't pay his full three dollars. He pays just enough to beat Ann: twenty divided by eight, plus a penny. That's two dollars and fifty-one cents.

5. Line 47 - RECOMMENDED (awkward aloud). "from somebody's" dangles.
   - TEXT: By the time you finish one search, Google's ads have made thousands of dollars.
   - SAY: By the time you finish one search, Google's ads have made thousands of dollars.
   - Source: $9,345 per second (our math, 10-K).

6. Line 0 (hook) - RECOMMENDED. True and specific (Alphabet made ~$1.1B/day overall; ads alone $807M/day), but 11 words runs ~3.5 s, "It made" is vague about ads, and SAY drops "dollars" vs "$" on screen. Tighter, still true, 9 spoken words, matches scene "$800M+":
   - TEXT: Google's free. Its ads made over $800 million a day.
   - SAY: Google's free. Its ads made over eight hundred million a day.
   - Then line 1 to avoid repeating "ads alone":
     - TEXT: That's 2025: $294.7 billion in ads, or about $807 million a day, by our math.
     - SAY: That's twenty twenty-five: two hundred ninety-four point seven billion dollars in ads, or about eight hundred seven million a day, by our math.
   - Source: Alphabet FY2025 10-K.

7. Line 63 - OPTIONAL accuracy note. "In September 2025 came the remedies" is fine (Sept 2, 2025 decision), but the final judgment was entered Dec 5, 2025 and the appeal targets it. No change required; if desired:
   - TEXT: In September 2025 the judge laid out the remedies. Google was not forced to sell Chrome or Android.
   - SAY: In September twenty twenty-five the judge laid out the remedies. Google was not forced to sell Chrome or Android.
   - Source: Bloomberg Law, Dec 5, 2025; Alphabet Q3 2026 10-Q.

## Pre-post re-check (Jan 4-5, 2027)
- Search for any D.C. Circuit ruling or argument in US v. Google (search) before posting; line 69/93 wording assumes none.

## Sources
- Alphabet Form 10-K FY2025: sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm
- Alphabet Form 10-Q Q3 2026: sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm
- Neowin, "Alphabet hits $400B annual revenue milestone" (Feb 2026); NewsBytes / AI Weekly Q3 2026 coverage (Oct 2026)
- Bloomberg / Bloomberg Law, "Google Must Limit Default Contracts to One Year" (Dec 5, 2025); MLex DOJ cross-appeal brief (2026); MediaPost Google appeal brief (May 2026)
- Bloomberg via Gulf News / Yahoo, $20B to Apple (May 2024); Bloomberg/CNBC, Murphy 36% testimony (Nov 2023)
- Google Ads Help: Quality Score, actual CPC

VERDICT: FAIL

## Round 2 (editor)
Applied: hook "Google's free. Its ads made over $800 million a day." + line 1; line 28 say; line 47; line 69 February 2026 + timeline 2/26; line 70 DOJ vs Google, "Appealing"; line 94 "by the third quarter of 2026".
VERDICT: PASS
