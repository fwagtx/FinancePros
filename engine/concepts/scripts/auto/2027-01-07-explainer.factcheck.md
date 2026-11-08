# Fact-check: 2027-01-07 Explainer, rent-to-own and the real price of weekly payments
Checked Nov 8, 2026 for posting Thu Jan 7, 2027, 12:00 CT. I verified everything independently; I used the writer's brief only for leads.

## What checks out
- **Hook realism.** Real listings match the example almost exactly. A Rent-A-Center ad for a Hisense 65" TV lists $19.99/week for 65 weeks: $1,299.35 total of payments against a $584.71 max cash price. RentMart shows a TCL 65" at $1,299.35 total against $699 retail. So $20 x 65 = $1,300 on a $600 TV is fair. (milled.com Rent-A-Center email; rentmart.com listings)
- **Math.** $20 x 65 = $1,300, which is 2.17x $600 ("more than double" is correct). For the card: $600 at 22.36% APR, 15 equal monthly payments, gives r = 0.018633/month, a payment of $46.22 and a total of $693.29. "About $693" is correct.
- **22.36% rate.** The Fed G.19 release of Oct 7, 2026 shows credit card plans, accounts assessed interest, at 22.36 for Aug 2026 (the Q3 quarterly reading; Q2 was 22.15). The next quarterly reading (Nov data) comes out around Jan 8, 2027, after the post date. (federalreserve.gov/releases/g19/20261007/)
- **TILA/Reg Z exemption.** A lease the consumer can end at any time without penalty is not a "credit sale" under Reg Z (12 CFR 1026.2(a)(16)). TILA APR disclosures therefore don't apply federally (In re Hanley, 1990; Ortiz v. Rental Mgmt, 3d Cir. 1995). This is federal only: states regulate rent-to-own separately, and New Jersey caps the rate at 30%.
- **NerdWallet/Raycom, Oct 2017.** Implied APRs at Rent-A-Center ran from 43% to 468%, except NJ (30% cap). The figure is specific to Rent-A-Center, so it needs that attribution (see line 5). (Fox Business; Texas Tribune; Scripps "Don't Waste Your Money")
- **State caps.** California Civ. Code 1812.644(c) caps the total of payments at 2.25x the max cash price. Vermont 9 V.S.A. 41b caps total cost at 2x the max cash price (from the 2016 act, S.73). Both are confirmed. (law.justia.com; legislature.vermont.gov)
- **"Return it in week 64, you keep nothing."** Fair. Returned items don't come with refunds of rent paid. Reinstatement rights vary by state (windows run from 30 days to the remaining term), but they only let you resume payments; you get nothing back. Early purchase options exist and at least 38 states require them to be disclosed, so line 3's "until the final payment" is softened (see below). (APRO statutes explainer; NH RSA 358-P:8; RI statute)
- **Limits.** post.title is 52 characters (<=60), tiktok is 136 (<=150), and all scene strings are within their limits.

## Issues (all must be fixed)

### Line 4: on-screen text and narration don't match (REQUIRED)
- **Problem:** The text says "22.36% APR" but the narration says "about twenty-two percent A P R." They must match. Saying the full "twenty-two point three six" would add 2 words and push past 140, so round the text instead. The $693 figure stays "our math" at 22.36%, which still rounds to about 22%.
- **TEXT:** `The same $600 on a card at about 22% APR, over 15 months, is about $693. Our math.`
- **SAY:** (unchanged) `The same six hundred on a card at about twenty-two percent A P R, over fifteen months, is about six ninety-three. Our math.`
- **SCENE:** `{"t": "compare", "title": "Total for a $600 TV", "left": {"label": "Card 22% APR", "value": "$693", "tone": "up", "sub": "15 months"}, "right": {"label": "Rent-to-own", "value": "$1,300", "tone": "down", "sub": "65 weeks"}, "mood": "think"}`
- **Source:** Fed G.19, Oct 7, 2026 release (Aug 2026 = 22.36).

### Line 5: APR claim overstated and the 468% figure not attributed (REQUIRED)
- **Problem:** "No APR is required" is true only under federal law, since states regulate rent-to-own and NJ caps the rate at 30%. The 468% figure was the top of NerdWallet/Raycom's range for Rent-A-Center specifically, not for rent-to-own in general, so the current wording misattributes it.
- **TEXT:** `It's a lease, so federal law requires no APR. NerdWallet estimated Rent-A-Center's implied APRs up to 468% in 2017.`
- **SAY:** `It's a lease, so federal law requires no A P R. NerdWallet estimated Rent-A-Center's implied A P Rs up to four hundred sixty-eight percent in twenty seventeen.` (27 words, +5)
- **SCENE:** `{"t": "stat", "label": "Rent-A-Center max", "value": "468%", "tone": "down", "sub": "NerdWallet, 2017", "mood": "shock"}` (label 17 characters, sub 16)
- **Source:** 12 CFR 1026.2(a)(16); In re Hanley 135 B.R. 311; NerdWallet/Raycom via Fox Business, Oct 2017.

### Line 6: trim to stay within the word limit after the line 5 fix (REQUIRED to keep words <=140)
- **TEXT:** `Some states cap the total: California at 2.25 times the cash price, Vermont at 2.`
- **SAY:** `Some states cap the total: California at two point two five times the cash price, Vermont at two.` (18 words, -2)
- **SCENE:** unchanged (`["CA: 2.25x", "VT: 2x"]`).
- **Source:** Cal. Civ. Code 1812.644(c); 9 V.S.A. 41b.

### Line 0: the hook implies a specific real TV (recommended)
- **Problem:** "This $600 TV" reads like a particular real product, but the figures are a hypothetical example (only line 2 says "for example"). "A" keeps the hook honest, keeps it at 10 words, and real listings back it up.
- **TEXT:** `A $600 TV can cost you $1,300.`
- **SAY:** `A six hundred dollar TV can cost you thirteen hundred.` (10 words)
- **SCENE:** unchanged. Also change post.ig line 1 to `A $600 TV can cost you $1,300.`

### Line 3: early purchase options exist (recommended)
- **Problem:** Most states require an early purchase option, so ownership can come before the final scheduled payment.
- **TEXT:** `It's not yours until it's paid off. Return it in week 64, you keep nothing.`
- **SAY:** `It's not yours until it's paid off. Return it in week sixty-four, you keep nothing.` (15 words, unchanged count)
- **SCENE:** unchanged.

### post.yt_desc: the NerdWallet attribution is missing here too (REQUIRED)
- Replace `A 2017 NerdWallet study estimated implied APRs up to 468%` with `A 2017 NerdWallet study estimated Rent-A-Center's implied APRs up to 468%`.

## Word count after fixes
137 + 0 (line 0) + 0 (line 3) + 0 (line 4) + 5 (line 5) - 2 (line 6) = **140**, which is within 115-140. The hook is 10 words (<=12).

## Notes
- The script gives no advice and no price predictions. "Our math" labels are present. There are no time-sensitive words (the rate is in the post copy dated "Fed, Q3 2026").
- The card comparison assumes the viewer qualifies for a card. That's fine as "our math", and it's stated nowhere as a recommendation.

VERDICT: FAIL

## Round 2 (editor)
Applied required fixes 1-4 and recommended hook/line 3 wording.
VERDICT: PASS
