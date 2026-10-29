# Fact-check: 2026-12-28-explainer (Penalty APR)

Checked Oct 29, 2026, for posting Dec 28, 2026 (evergreen). Claims were checked against web search excerpts (Chase pricing pages, law-firm and news reports on the CFPB rule, CARD Act explainers) and the math was rerun in Python.

## Verified
- Chase pricing pages from 2026 (Prime 6.75% as of 3/24/2026 and 5/5/2026) list the Penalty APR as "Up to 29.99%" (Prime + up to 26.99%, max 29.99%). It can be triggered by a missed minimum payment or a returned payment. This is Chase's own pricing, not a legal cap. The script attributes it to Chase correctly.
- CARD Act / Reg Z: a higher rate on new transactions needs 45 days' notice (1026.9(g), 1026.55(b)(3)). A higher rate on the existing balance needs the minimum payment to be more than 60 days late (1026.55(b)(4)). Six consecutive on-time minimum payments after the increase require the issuer to bring that balance's rate back down. Several explainers agree (Credit Karma, WalletHub, credit.com, CardRatings). These rules cover consumer cards only.
- CFPB $8 late-fee rule: Judge Mark Pittman of the U.S. District Court for the Northern District of Texas vacated it on April 15, 2025, on a joint motion by the CFPB and the plaintiffs (Holland & Knight, American Banker, The Hill, Courthouse News). Correct.
- Math: 6,000 x 0.21 / 12 = $105.00. 6,000 x 0.2999 / 12 = $149.95. The difference is $44.95 a month, or $269.70 over 6 months. All correct.
- Compare values "$105" and "$149.95" are both 7 characters or fewer. No `keep:true` lines. On-screen numbers match the spoken numbers on every line.
- Hook (lines[0]) is true, specific and under about 3 seconds. Cover "One Late Payment / 29.99%" is paid off by the video.
- Some cards have no penalty APR: issuer listings on Credit Karma show "Penalty APR: None" for several Capital One cards. Acceptable as stated ("some cards").

## Issues

1. **lines[3] and lines[4]: the worked example contradicts the rule just explained (must fix).** The video opens with "one late payment" and then applies 29.99% to an existing $6,000 balance. Under 1026.55(b)(4), the existing balance can only get the penalty rate if the payment is more than 60 days late, so one slightly late payment would not do it. The example needs a clear condition.
   - lines[3] text → `Our math: if a $6,000 balance jumps from 21% to 29.99%, interest goes from $105 to $149.95 a month.`
   - lines[3] say → `Our math: if a six thousand dollar balance jumps from twenty-one percent to twenty-nine point nine nine, interest goes from a hundred five dollars to a hundred forty-nine ninety-five a month.`
   - lines[4] text → `That's $269.70 more over six months, if the balance stays flat.`
   - lines[4] say → `That's two hundred sixty-nine seventy more over six months, if the balance stays flat.`
   - lines[4] scene.sub `Our math, flat bal` → `Our math, flat balance` (if it fits the template; otherwise keep it).

2. **lines[7]: unsupported claim, and the list title is mislabeled (must fix).** "Many people autopay the minimum" has no source. "What people do" also doesn't fit the second item ("No penalty APR" is a card feature, not something people do). State neutral facts without instructions.
   - text → `Autopay can cover the minimum, and some cards have no penalty APR at all.`
   - say → `Autopay can cover the minimum, and some cards have no penalty A P R at all.`
   - scene.title `What people do` → `Worth knowing`; items → `["Autopay covers minimum", "Some: no penalty APR"]`

3. **lines[6] and the post fields: "$8 late fee cap" is imprecise (should fix).** The rule was an $8 safe-harbor amount for large issuers, not a hard cap, although some outlets did call it a cap.
   - lines[6] text → `And a court threw out the CFPB's $8 late fee rule in April 2025.`
   - lines[6] say → `And a court threw out the C F P B's eight dollar late fee rule in April twenty twenty-five.`
   - lines[6] scene.headline `Court voids $8 cap` → `Court voids $8 rule`
   - post.ig: `A court vacated the CFPB's $8 late fee cap in April 2025.` → `A court vacated the CFPB's $8 late fee rule in April 2025.`
   - post.yt_desc: `a court vacated the CFPB's $8 late fee cap in April 2025` → `a court vacated the CFPB's $8 late fee rule in April 2025`

4. **lines[1]: "2026" will date an evergreen video (minor, optional).** It is accurate on Dec 28, 2026, but it ages within days.
   - text → `Chase's card terms list this penalty APR at up to 29.99%.`
   - say → `Chase's card terms list this penalty A P R at up to twenty-nine point nine nine percent.`
   - scene.label `Penalty APR, 2026` → `Chase penalty APR`
   - The post's "(2026)" source citations can stay.

5. **lines[2]: small nuance (minor, optional).** Old debt also needs the 45-day notice, and the rate applies to purchases made more than 14 days after the notice. The current wording is acceptable as a simplification. A clearer version is:
   - text → `New buys: higher rate after a 45-day notice. Old debt: only if you're over 60 days late.`

6. **lines[5]: fine.** "Six on-time minimum payments in a row force a rate cut on that old balance" matches 1026.55(b)(4)(ii). Optional smoother read: `Then six on-time minimums in a row bring that old balance's rate back down.`

No advice, price predictions, political opinion or stale time words beyond item 4. The "Not financial advice" disclaimers are present in the post.

VERDICT: FAIL

## Round 2 (editor)
- lines[3]/[4]: example now conditional ("if a $6,000 balance jumps ... to the penalty rate"; "if the balance stays flat"); spoken values rounded (about $150 / about $270), exact on screen.
- lines[7]: neutral fact wording; list retitled "Worth knowing".
- lines[6], ig, yt_desc: "$8 late fee rule"; headline "Court voids $8 rule".
- lines[1]: removed "2026"; label "Chase penalty APR".
VERDICT: PASS
