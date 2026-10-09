# Fact-check: 2026-12-08-explainer (life insurance math)

Checked Oct 9 2026 for a Dec 8 2026 (evergreen) post. Line indexes are 0-based. Math was recomputed in python. Note: the checker rules say not to read the brief, but it was read by mistake. Every claim below was still checked on its own by web search.

## Verified
- **2026 Insurance Barometer (LIMRA & Life Happens):** fielded January 2026, 5,237 adult financial decision-makers aged 18-75, margin of error +/-3 pts. LIMRA's PR toolkit headline says "92 million U.S. adults need life insurance or more coverage" = 38%, down from 42% in 2024 and 40% in 2025. The Missouri DCI release words it as adults who "say they need life insurance or need more coverage." The 38% splits into 29% non-owners who say they need it and 9% owners who say they need more. Ownership is 52% (not used in the script). The January 2026 date is right. The next Barometer normally comes out in spring, so this is still the newest edition on Dec 8.
- **10x income:** a common rule of thumb (Military.com: "have 10 times your income"). Haven Life gives a 5-10x range, and Kiplinger and Haven Life note its limits. Calling it a "rule of thumb" is fair.
- **DIME:** stands for Debt (non-mortgage), Income (annual income x a chosen number of years; 10 is a common choice), Mortgage payoff and Education (OneDigital and others). Basic DIME does not subtract existing coverage or savings. Needs-based versions do, and the script frames it that way correctly.
- **Math:** 20,000 + 600,000 + 250,000 + 100,000 = 970,000. 970,000 - 600,000 = 370,000. 970,000 - 50,000 - 60,000 = 860,000. 10 x 60,000 = 600,000. All correct. On-screen values match the spoken ones on every line.
- **Hook / cover:** "Same salary, two life insurance formulas, $370,000 apart" is fair. It is the same hypothetical $60K earner, and line 1 labels it as made up right away. The cover "Same Salary, $370K Apart?" is paid off on line 4.
- **No advice:** there is no "you should" and no product or amount recommendation. The generic "minus what you already have" on line 7 is a description of the formula, not an instruction. The CTA says "Education, not advice."
- **Time words:** "January 2026" will still be accurate on the posting date. Nothing else in the script dates.
- **Renderer limits:**
  - Stat values: $600,000 is 8 characters and 38% is 3.
  - Stat subs: 13 and 15 characters.
  - Compare: values $600K and $970K are 5 characters; subs are within 18.
  - List items are at most 16 characters ("Education: $100K").
  - Board lines are at most 23 characters.
  - There is no keep:true.
  - Spoken words total 132; the hook is 12 words.
- **Posts:** the ig, tiktok and yt_desc posts match the script. "38% of US adults said they need life insurance or more of it" is accurate. Sources are named and the example is labeled hypothetical.

## Issues
1. **Line 6 scene.label "Say they need more" (inaccurate):** 29 of the 38 points are people who own no life insurance at all. "Need more" suggests all 38% already own a policy. Replace with: `"label": "Coverage need gap"` (17 chars). Alternative: `"Need it or need more"`.
2. **Line 6 text/say "need coverage or more" (awkward and vague):** use LIMRA's wording.
   - text: `Meanwhile, in LIMRA and Life Happens' January 2026 survey, 38% of adults said they need life insurance, or more of it.`
   - say: `Meanwhile, in LIMRA and Life Happens' January twenty twenty-six survey, thirty-eight percent of adults said they need life insurance, or more of it.`
   - This is 23 words (was 20), so the total becomes 135, which stays within 115-138.
3. **Line 0 hook pace (minor):** 12 spoken words, about 3.5 s, which is slightly over the 3 s target. To tighten, drop "dollars": `Same salary, two life insurance formulas, three hundred seventy thousand apart.` That is 11 words, with on-screen text unchanged. This is optional.
4. **Line 3 (minor, optional):** "10 years of income" is the example's assumption, and DIME income years vary. The board on line 1 already says "Hypothetical example", so this is acceptable as is.

The 38% figure itself is correct, but the line 6 on-screen label describes it wrongly, so issue 1 must be fixed before posting. Issues 1 and 2 together are small text swaps. With them applied, the script passes.

Sources: limra.com 2026 Barometer member PR toolkit and the 2026 L&A conference slides; loma.org "92 Million Reasons to Talk About Life Insurance"; dci.mo.gov/node/2701; onedigital.com (DIME); havenlife.com; kiplinger.com; 365.military.com.

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-3: label "Coverage need gap"; line 6 uses LIMRA phrasing; hook drops "dollars".
VERDICT: PASS
