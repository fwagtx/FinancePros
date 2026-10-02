# Fact-check: 2026-11-21-explainer (lease guarantors), posts Nov 21, 2026

Checked Oct 2, 2026. Math was recomputed in Python.

## Claims verified
- **NYC 40x tenant / 80x guarantor rule.** Confirmed as common practice, not law. StreetEasy ("What Is a Guarantor") says a guarantor needs to make 80 times the rent, double the 40x asked of renters. Panda Guarantee and Edge Realty say the same. Both multiples mean annual income compared with monthly rent.
- **Harvard JCHS, State of the Nation's Housing 2026 (released June 17, 2026).** Cost-burdened renter households hit a record 22.7 million (49%) in 2024. Confirmed by JCHS and NLIHC.
- **Apartment List national median rent.** September 2026 was $1,388 (-0.1%, the first decline since January). The chart points match the values as first reported: Feb $1,357, Mar $1,363, Apr $1,370, Jun $1,385, Jul $1,388, Aug $1,390, Sep $1,388. Jan and May are missing. This is acceptable because the x-axis uses month numbers and the title "(month)" explains them. Note that Apartment List revises past months, so the current series may differ by a few dollars.
- **Insurent fee.** Insurent's own site says the fee for U.S. parties is about 70%-90% of one month's rent for a one-year lease guaranty. This is a company-stated figure.
- **3x monthly-rent screen.** Widely described as a common guideline that is not mandatory, which matches how the script attributes it.
- **Guarantor liability.** A guarantor can be liable for unpaid rent, damages and attorney fees, depending on the guaranty's terms. "Often legal fees" is fair.
- **Math.** 2,000 x 40 = 80,000. 2,000 x 80 = 160,000. 2,000 x 3 x 12 = 72,000. 70%/90% of 2,000 = 1,400/1,800. All correct.

## Required fixes
1. **Hook (line 1) is ambiguous.** "Eighty times the rent" does not say monthly rent. Change it to: spoken "New York City landlords often want guarantors earning eighty times monthly rent." (12 words). On-screen: "NYC landlords often want guarantors earning 80 times monthly rent."
2. **Line 2: "the tenant's bar" is undefined, and it is not said that 80x is annual income.** Change it to: "That's yearly income, double the tenant's 40x, because the guarantor pays if the tenant doesn't." (spoken: "forty times").
3. **Line 3: say "monthly".** Change it to "On a hypothetical two thousand dollar monthly rent, ..." and add "monthly" to the on-screen text. Also make the right value "$160,000" so it matches the "$80,000" format on the left.
4. **Line 8 takes one company's figure and applies it to an industry ("Companies like Insurent charge...").** Attribute it instead: "Insurent says its fee is about 70% to 90% of one month's rent for a one-year lease." Change the sub to "of 1 month's rent, per firm" (27 characters). Make the same change in yt_desc.
5. **Line 9.** Change it to "On $2,000 a month, that's $1,400 to $1,800." (spoken: "On two thousand a month, that's fourteen hundred to eighteen hundred dollars.").
6. **Cover title "Why Your Guarantor Needs 80x Rent" overgeneralizes an NYC practice.** Change it to "Why NYC Guarantors Need 80x Rent".

## Other notes (not blocking)
- **Dating.** The hook describes an ongoing practice rather than news. The on-screen "NYC 2026" tag gives enough of a date, and the Sept 2026 rent figure is dated both in speech and on screen. No time words will be wrong on Nov 21.
- **IG post.** Clarified as "with yearly income of 80x the monthly rent".
- **Limits.** All label limits pass: hook title 21, compare subs 8, board lines 26 or fewer, list items 18 or fewer. The script has no keep:true. Spoken and on-screen values match. There is no advice or price prediction, and the tone is neutral.

VERDICT: FAIL

## Round 2: applied
All six required fixes have been applied to the raw.json. check.py output: "OK: 10 lines, 150 spoken words (~50s at 180 wpm)". The hook is 12 spoken words.

VERDICT: PASS
