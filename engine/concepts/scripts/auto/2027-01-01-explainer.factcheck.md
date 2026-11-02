# Fact-check: 2027-01-01 Explainer (Acorn Economics, fractional reserve banking)

Checked 2026-11-02 for posting Fri 2027-01-01 12:00 CT. Spoken words as written: 138 (budget 115-140).

## Verified claims

| Claim | Status | Source |
|---|---|---|
| Fed reserve requirement ratios cut to 0% effective March 26, 2020 (announced Mar 15, 2020) | TRUE, and still 0% for 2026 (Nov 24, 2025 Reg D indexation rule says requirements "will remain zero") | federalreserve.gov/monetarypolicy/reservereq.htm; 85 FR 16525 (Mar 24, 2020); 90 FR (Nov 24, 2025, doc 2025-20744) |
| Reserves held as vault cash or balances at the Fed | TRUE (these are the two ways reserve requirements were satisfied) | federalreserve.gov reserve requirements page |
| FRED WRESBAL annual averages 2016-2025 | TRUE, all ten points match after rounding: 2.306, 2.253, 1.983, 1.555, 2.649, 3.884, 3.396, 3.239, 3.367, 3.195 ($T) | FRED API, WRESBAL, frequency=a, avg, vintage 2026-11-02 |
| "About $3.2 trillion in 2025, on average" | TRUE ($3.195T) | same |
| BoE 2014 Q1 bulletin: loans create deposits | TRUE: McLeay, Radia & Thomas, "Money creation in the modern economy," BoE Quarterly Bulletin 2014 Q1 | bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy |
| FDIC $250,000 per depositor, per insured bank, per ownership category | TRUE, unchanged as of Nov 2026 (no enacted increase found) | fdic.gov deposit insurance FAQ |
| Math 100 deposit, keep 10, lend 90 | Correct arithmetic; 10% matches the old pre-2020 top reserve ratio | n/a |

Note: the 2026 year-to-date WRESBAL average is about $3.00T, so reserves fell in 2026. "2025" is the latest full year and is labelled, so this is not wrong, but it will be a year old on the posting date.

## Issues

1. **Line 0 (hook): accurate, but missing the actor, which can mislead.** "Your bank is required to keep 0%" is true only for the Fed's reserve requirement. Large banks still face the Liquidity Coverage Ratio and must hold high-quality liquid assets, and every bank keeps some cash in practice. Naming the Fed keeps it true and adds authority. As a grabber it is strong: about 2.8 s and surprising.
   - Replacement text: `The Fed requires your bank to keep 0% of your deposit.`
   - say: `The Fed requires your bank to keep zero percent of your deposit.` (12 words, about 3 s)
   - scene.title: `Fed requires: [0%]` (was "Required in vault: [0%]". The 0% also applied to Fed balances, not just the vault.)

2. **Lines 2-3: the textbook model is shown as fact, and the BoE line later contradicts it.** "Keeps 10 acorns and lends 90 to a chipmunk" plus "Keep a slice, lend the rest" is exactly the money-multiplier and intermediation picture that the BoE 2014 article calls a misconception. Line 7 then reverses it without labelling either one. Viewers end up with two conflicting models. Label line 2 as the textbook version so the line 7 twist pays off.
   - Line 2 text: `Textbook math: the bank keeps 10 acorns and lends 90 to a chipmunk.`
   - say: `Textbook math: the bank keeps ten acorns and lends ninety to a chipmunk.` (13 words, unchanged count)
   - Line 3 can stay as is. Board lines "Keep a slice," and "lend the rest" are 13 characters each, within the 18 limit.

3. **Line 5: no mention of liquidity rules (requested).** A short caveat stops the hook from implying banks have no liquidity rules.
   - text: `Since March 26, 2020, the Fed requires 0%. Big banks still face liquidity rules.`
   - say: `Since March twenty-sixth, twenty twenty, the Fed requires zero. Big banks still face liquidity rules.` (15 words, +2)
   - scene: label `Required reserve` (16), value `0%`, sub `Fed, Mar 26 2020` (unchanged).

4. **Line 6: "still" repeats once line 5 changes. The chart tone is also off.**
   - text: `Yet banks kept about $3.2 trillion at the Fed in 2025, on average.`
   - say: `Yet banks kept about three point two trillion dollars at the Fed in twenty twenty-five, on average.` (17 words, -1)
   - chart `color`: change "up" to `neutral`. 2025 ($3.20T) was below 2024 ($3.37T) and far below the 2021 peak, so an "up" color and mood misstate the trend. Data points are correct and need no change.

5. **Line 7: the twist is vague ("new loans create new deposits" does not say what happens to your acorns).** It also runs a bit long.
   - text: `Twist: the Bank of England (2014) says a new loan creates a brand-new deposit.`
   - say: `Twist: the Bank of England says a new loan creates a brand-new deposit.` (13 words, -2)
   - Board lines `New loan =` / `new deposit` (10 and 11 characters).

6. **Cover: "The Empty Vault" is not paid off and contradicts the video.** The video shows banks holding about $3.2T at the Fed plus vault cash, so the vault is not empty. Only the requirement is zero.
   - Cover title: `The 0% Rule` (keep prop acorns, label `FED RULE`, value `0%`).

7. **Line 8 (minor, optional):** "If a bank fails" is fine because the "per bank" phrasing implies insured banks. For precision, use "If an insured bank fails" (+1 word, which brings the total to 139 if used). The spoken line is long (23 words) but reads cleanly.

## Other checks
- Stale news / time words on Jan 1, 2027: none wrong. "Since March 26, 2020" and "in 2025" are dated explicitly and stay true. The 0% rule is confirmed for 2026, and no 2027 change has been announced.
- Advice or price predictions: none. The post includes "not financial advice."
- Political opinion: none.
- On-screen vs spoken: all values match (0%, 100, 90, $3.2T, $250,000, March 26 2020).
- Post text: accurate. The IG and YT descriptions are fine. Optionally prefix the example in yt_desc with "textbook" to match fix 2. TikTok "per Fed rules since 2020" is good.
- Awkward narration: "Our math:" reads stiffly out loud. Fix 2 removes it.
- Word count with fixes 1-5: 138 +1 +0 +2 -1 -2 = **138** (within 115-140). Hook is 12 words.

## Result
All facts and chart data are correct. FAIL is for the misleading cover and the unlabelled textbook model, plus the requested LCR caveat. All fixes are small text swaps.

VERDICT: FAIL

## Round 2 (editor)
Fixed: hook names the Fed ("The Fed requires your bank to keep 0% of your deposit", title "Fed requires: [0%]"); "Textbook math" label on the 10/90 example; line 5 adds "Big banks still face liquidity rules"; dropped repeated "still"; BoE twist "a new loan creates a brand-new deposit" with board "New loan = / new deposit"; "insured bank"; cover "The 0% Rule" (label FED); ig/tiktok reworded to match. Chart color kept (renderer supports only up/down). 140 spoken words.
VERDICT: PASS
