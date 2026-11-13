# Fact-check: 2027-01-12 Explainer (rent renewal leverage)
Checked Nov 13, 2026 for posting Tue Jan 12, 2027. Fixes are applied in 2027-01-12-explainer.raw.json. check.py: OK (10 lines, 134 spoken words, hook 12 words).

## Claims verified
- MAA Q3 2026 (release Oct 28, 2026): effective new lease rate -6.0%, renewal +5.3% (up 80 bp YoY), blended +0.4%. Confirmed (finviz/PR Newswire release, Zacks, Benzinga transcript). MAA's Q4 call is early Feb 2027, so Q3 2026 is still its latest quarter on Jan 12, 2027.
- Census HVS Q3 rental vacancy: 2020 6.4, 2021 5.8 (CB21-166), 2022 6.0 (Q3 2022 release), 2023 6.6, 2024 6.9, 2025 7.1, 2026 7.6 (7.3 in Q2 2026). Confirmed via Census releases, FRED RRVRUSQ156N, mpamag, TrendForce. Not seasonally adjusted. Next release Feb 2, 2027, after posting, so Q3 2026 stays the latest.
- Census median asking rent, vacant-for-rent units, Q3 2026: $1,541 (Q3 2025: $1,534). Confirmed (mpamag summary of the release).
- Zillow 39.8% of rental listings offered a concession: the April 2026 rental report (May 27, 2026 release); +5 pts YoY. "April 2026" is correct. (Zillow also reported 39.8% for July 2026; 39.7% June 2026.)
- Apartment List: the median vacant unit took 34 days to lease in September 2026 (October 2026 recap). Confirmed.

## Our math (recomputed)
- 1,541 x 0.053 x 12 = $980.08, so "about $980" is OK.
- 1,541 x 12 / 365 = $50.66 a day; x 34 = $1,722.54 (board's rounded 50.66 x 34 = $1,722.44), so "$1,722" is OK. Spoken "about seventeen hundred" is OK.
- "One empty month costs more than a year of your raise": 34 days is $1,722, and a 30-day month is about $1,520. Both are more than $980. OK.

## Issues fixed
1. Line 0 (hook): stated MAA's numbers as if they applied to all renters. Replaced with:
   - text: "One big landlord: renewals up 5.3%. New leases? Down 6%."
   - say: "One big landlord: renewals up over five percent. New leases? Down six." (12 words)
2. Line 1: the narration "landlord M A A in Q three twenty twenty-six" was awkward. Replaced with:
   - text: "That's MAA, Q3 2026, versus each unit's last lease."
   - say: "That's M A A, third quarter twenty twenty-six, versus each unit's last lease."
3. Line 2 say: "in Q three twenty twenty-six" is now "that same quarter". The on-screen text keeps "Q3 2026", so the claim is still dated.
4. Line 4: "a fifteen forty-one rent" was awkward. Changed to:
   - text: "...a 5.3% raise on $1,541 a month is about $980 a year."
   - say: "...on fifteen forty-one a month is about nine eighty a year."
5. post.title: it said the figures applied to renters generally. It is now "Why MAA renewers paid 5.3% more as new leases fell 6%".
6. post.tiktok: the figures were general and undated. It is now "At one big landlord (MAA, Q3 2026), renewals rose 5.3% and new leases fell 6%. Where rent leverage comes from. Not financial advice. #rent #moneytok" (148 chars).

## Checked, no change needed
- The ig and yt_desc captions are accurate, attributed and dated.
- Cover "Renewal Markup?" (-6% / +5.3%): the video delivers on it.
- The script gives no advice or predictions and includes the "landlord can still say no" caveat.
- The script has no time words that would be stale on Jan 12, 2027.

VERDICT: PASS

## Round 2 (editor)
Hook now attributes MAA; narration smoothed. check.py OK.
VERDICT: PASS
