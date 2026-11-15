# Fact-check: 2027-01-14-explainer (Broker fees: NYC FARE Act, Massachusetts)
Checked Nov 15, 2026 for posting Thu Jan 14, 2027 12:00 PM CT. All fixes below are already applied to 2027-01-14-explainer.raw.json; check.py prints OK (10 lines, 140 spoken words, hook 12 words).

## Verified claims
- FARE Act = Local Law 119 of 2024, passed by City Council Nov 13, 2024 (Inman), in effect June 11, 2025 (NYC DCWP FAQ/news). Landlord or landlord's agent cannot charge tenant a broker fee; whoever hires the broker pays; tenants who hire their own broker still pay; DCWP enforces. Federal court denied REBNY's injunction request. CONFIRMED.
- Pre-FARE typical NYC fee: one month's rent to 15% of annual rent (Dwell, ABC7, Council Member Abreu/THE CITY; some sources cite up to 20%). StreetEasy models 12%. CONFIRMED.
- StreetEasy upfront cost series, fee listings (Dec 9, 2024 report): 2024 = $12,951 "all-time high", up 29% since 2017 (consistent with $10,007). 2024 figure was published Nov/Dec 2024, so it is a partial year (year to date); now labeled "2024 YTD" in chart title and "by late 2024" in narration. Intermediate years (2018-2023) could not be fetched directly (streeteasy.com blocked from this session); they match the writer's transcription of the StreetEasy table, and secondary press (NY Post: $12,667 for 2023) agrees. PLAUSIBLE/CONFIRMED for endpoints.
- StreetEasy Dec 18, 2025 six-month review: ~1.1%, $38/mo (Nov 2025), $5,454 saved. CONFIRMED but SUPERSEDED.
- StreetEasy May 2026 report ("NYC rental market update one year after FARE Act"): renters pay ~$46/mo more in rent (~1.1% per CRE Daily); avoided average broker fee ~$5,862 in May 2026. No newer StreetEasy FARE Act estimate found (searched through Nov 2026). Script updated to the May 2026 figures with date.
- DCWP: 2,000+ complaints and inquiries in first year (The Real Deal, June 10, 2026; THE CITY/DCWP data). CONFIRMED.
- Massachusetts: statewide law in FY26 budget signed by Gov. Healey July 4, 2025; effective Aug 1, 2025; fee paid only by the party who engaged the broker (Mass.gov FAQ/press release, Boston.gov). CONFIRMED.
- Math: 12 x $3,500 = $42,000; x 12% = $5,040. CORRECT.

## Issues found and fixes applied
- Line 0 (hook): "Paying fifteen percent of a year's rent, just to sign a lease?" is present tense with no place; for a nationwide audience it implies a current, general practice. Fixed (12 words): text "Some New York renters paid 15% of a year's rent upfront." / say "Some New York renters paid fifteen percent of a year's rent upfront."
- Line 1: "New York renters often paid that" overstated (15% was the top of the range, not the common amount). Fixed: text "The norm: one month's rent to 15%, often paid even to the landlord's broker." / say "The norm: one month's rent to fifteen percent, often paid even to the landlord's broker." Board still dates it "NYC, pre-June 2025".
- Line 2: 2024 is partial year. Text "...at $12,951 upfront by late 2024." / say "...near thirteen thousand upfront by late twenty twenty-four." Chart title "NYC upfront cost, fee units (2024 YTD)".
- Line 3: "a 12% fee on $3,500 rent is $5,040" was wrong as worded (12% of $3,500 is $420; the fee is 12% of a year's rent). Fixed: text "By our math, 12% of a year at $3,500 a month is $5,040." / say "By our math, twelve percent of a year at thirty-five hundred a month is five thousand forty." Money "to" label "12% of a year".
- Line 4 (smoothness + clarity, "New York's" could read as state law): text "Then, on June 11, 2025, New York City's FARE Act made whoever hires the broker pay." / say "Then, on June eleventh, twenty twenty-five, New York City's FARE Act made whoever hires the broker pay."
- Line 6: Dec 2025 estimate superseded by StreetEasy May 2026. Text "The trade-off? As of May 2026, StreetEasy put rents up about $46 a month, against about $5,862 saved upfront." / say "...about forty-six dollars a month, against about fifty-nine hundred saved upfront." Compare values +$46 / $5,862 (sub "May 2026"); 22 spoken words, both boxes appear.
- Captions: post.title now "Why NYC renters paid 15% of a year's rent to a broker" (53 chars); IG and YouTube descriptions updated to May 2026 figures, 2024 YTD label, corrected "our math" wording, DCWP complaint stat dated. TikTok unchanged, 145 chars (<=150), accurate.

## Other checks
- Neutrality: presented as a rule change and a StreetEasy trade-off estimate; no position taken. Line 7 "Still" is factual framing. OK.
- Time words on post date (Jan 14, 2027): all dated ("year one" = first year to June 2026, dated in captions). No stale "new"/"this year". OK.
- Cover "The Broker Fee" / 15% is paid off by hook and line 1. OK.
- Line 8 tips are general, not financial advice. OK.
- Note: streeteasy.com and credaily.com could not be fetched directly from this session (network allowlist); StreetEasy figures verified via search snippets of StreetEasy pages and secondary press.

VERDICT: PASS

## Round 2 (editor)
Hook scoped to NYC renters; StreetEasy May 2026 figures; math fixed. check.py OK.
VERDICT: PASS
