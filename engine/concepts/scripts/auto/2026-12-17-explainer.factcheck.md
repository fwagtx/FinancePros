# Fact-check: 2026-12-17-explainer (Does paying rent build credit?)

Checked on Oct 18, 2026, for a Dec 17, 2026 post. I read only the raw.json, used 8 web searches and redid the math in Python.

## Verified claims

- **Line 2, TransUnion 13% (2025):** Correct. In TransUnion's 2025 Rent Payment Reporting study (released Sept 10, 2025), 13% of renters said their rent was reported, up from 11% in 2024. "Said their rent was reported" is the right framing for a survey.
- **Line 4 chart (27 / 36 / 48 / 44):** All four points are correct.
  - 2022: 27%.
  - 2023: 36% (June 2023 report).
  - 2024: 48% (Oct 2024 report).
  - 2025: 44% (Sept 2025 report). This is the first decline.
  - The wording "of property managers aware of rent reporting" matches TransUnion's definition. The 44% end label matches both the caption and the narration.
- **Line 3, rent isn't reported by default:** Correct. A landlord or a third-party furnisher has to send it, and many services charge a fee. "Some charge fees" is accurate.
- **Line 5, FICO 9 and VantageScore 4.0 count rent:** Correct. VantageScore 3.0 also counts rent, but the line doesn't claim to be a full list. FICO 8 being the most widely used FICO version is fine.
- **Line 6, FHFA timeline:** Correct.
  - Jul 2025: FHFA ordered Fannie and Freddie to accept VantageScore 4.0.
  - May 1, 2026: limited pilot began. Freddie announced it Apr 22.
  - Sept 9, 2026: Fannie Mae LL-2026-06 and Freddie Mac Bulletin 2026-H opened VantageScore 4.0 to all approved lenders without prior approval.
  - "Could use by September 2026" is accurate. One small caveat: manually underwritten loans still need Classic FICO. Leaving it out is acceptable at this length.
- **Post text:** The claim "Since September 2026, all approved Fannie Mae and Freddie Mac lenders can use VantageScore 4.0" will still be accurate on Dec 17. The cover title is answered by the final split.
- **Limits:** Every field is within its limit.
  - post.title: 57 characters.
  - tiktok: 143 characters.
  - Board lines: 17, 19 and 20 characters.
  - Split items: 15 characters at most.
  - Compare values: 6 and 7 characters. Compare subs: 18 and 14 characters.
  - Timeline "when" fields: 5 characters each. "What" fields: 5 words at most.
  - No line uses keep:true, so the template-mismatch check doesn't apply.
- **Advice and tone:** There is no instruction-style takeaway, no advice, no price prediction and no political opinion. The script is framed as news and education.

## Issues

### 1. Lines 5 and 7 and the post text overstate the FICO 8 claim (factual). Must fix.

Saying "FICO 8 ... doesn't" count rent is too absolute. Rent added through Experian Boost does count in FICO 8 when the score is calculated on the Experian file. Experian's own materials say Boost can raise FICO 8 using rent payments. Without the Boost exception, the statement is wrong.

**Line 5 text:**
> Even then, it depends on the score. FICO 9 and VantageScore 4.0 count rent; FICO 8, the one lenders use most, usually doesn't, except through Experian Boost.

**Line 5 say:**
> Even then, it depends on the score. FICO nine and VantageScore four point oh count rent; FICO eight, the one lenders use most, usually doesn't, except through Experian Boost.

**Line 5 scene.right:** set `"value": "Rarely"` (6 characters) and `"sub": "except Exp. Boost"` (17 characters).

**Line 7 scene.right.items[1]:** change "FICO 8 score" to:
> FICO 8 (mostly)

(15 characters.)

**post.ig:** replace
> FICO 9 and VantageScore 4.0 count reported rent; FICO 8, the version lenders use most, doesn't.

with
> FICO 9 and VantageScore 4.0 count reported rent; FICO 8, the version lenders use most, generally doesn't (Experian Boost is an exception).

**post.yt_desc:** replace
> while FICO 8, the version lenders use most, doesn't;

with
> while FICO 8, the version lenders use most, generally doesn't (Experian Boost is an exception);

### 2. Staleness risk for Dec 17 (check again before posting)

TransUnion has published this study every year: June 2023, Oct 2024 and Sept 10, 2025. As of Oct 18, 2026, I found no 2026 edition. If one comes out before Dec 17, the line "In a 2025 TransUnion survey, just 13%" would still be literally true but would be old news.

Check TransUnion's newsroom about a week before posting. If a 2026 report exists, update:
- line 2 (the stat value and sub "TransUnion, 2026"),
- the cover value,
- the line 4 chart (add a 2026 point and set the end label),
- the post text.

Nothing else in the script uses time words that break by Dec 17. "By September 2026" and "Since September 2026" are both safe.

### 3. Line 4 chart color (minor style point)

The chart ends on a drop (48 to 44, which is -8.3% relative) under the caption "Landlords lag too", but `"color"` is set to `"up"`. Consider `"color": "down"` so the color matches the story. Optional.

### 4. Opening hook (minor, passes)

"You pay rent every month. Your credit score probably never sees it." is true: about 87% of renters don't have their rent reported. It's specific and creates a question the viewer wants answered. At 12 words it runs about 3 seconds, which is right at the limit. To make it faster, use this optional tighter version:
> Your rent probably never reaches your credit score.

## Math

No worked examples. The chart's year-over-year changes match TransUnion's reported directions:
- 2022 to 2023: up.
- 2023 to 2024: up.
- 2024 to 2025: down 4 points.

On-screen values match the spoken values on every line (13%, 44%, 2025, September 2026).

## Sources (search excerpts)

- TransUnion 2025 Rent Payment Reporting release (Seeking Alpha / GlobeNewswire), TheMortgagePoint, NMP, DSNews
- TransUnion 2023 and 2024 releases (Multifamily Executive, CrowdfundInsider, Globe and Mail press release)
- Experian (Boost and FICO 8 rent, 2022 announcement; "What is Experian Boost"), Nasdaq/Esusu
- Fannie Mae LL-2026-06 and DU release of Sept 9, 2026; Freddie Mac (Apr 22, 2026 announcement; Bulletin 2026-H via HousingWire, The Mortgage Reports, Informative Research)

VERDICT: FAIL

## Round 2 (editor)
Applied fix 1 (Experian Boost exception on line 5, compare "Rarely"/"except Exp. Boost", split "FICO 8 (mostly)", posts), fix 3 (chart color down). 13% stays explicitly dated "2025 survey" (true on Dec 17 even if a 2026 edition appears); tiktok now dated.
VERDICT: PASS
