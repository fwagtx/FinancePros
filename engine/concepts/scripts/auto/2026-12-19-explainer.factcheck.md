# Fact-check: 2026-12-19-explainer (lease clauses)

Checked: October 20, 2026. Posting date: Saturday, December 19, 2026. Source read: `2026-12-19-explainer.raw.json` only. 11 web searches; math recomputed in python.

## Claims verified

| Line | Claim | Status | Source |
|---|---|---|---|
| L2 | 2024 US median gross rent $1,487 (ACS 1-year, B25064) | Confirmed. This is *gross* rent, which includes utilities the renter pays. | Discover; Walnut Invest (citing 2024 ACS 1-yr); StatRanker on B25064 |
| L2 | $1,487 x 2 = $2,974 | Math is correct | python |
| L2 | "Many lease-break fees equal 2 months' rent" | **Weak.** No named survey found. Guides give ranges of "1 to 2 months" (LeaseRunner, landlord blogs) or "2 to 4 months" (moving-company blog). The DC Bar tenant guide says "some leases ask for 2 months." "Some" is supportable; "many" is not. | lawhelp.org (DC); leaserunner.com; imoving.com |
| L4 | CA caps most deposits at 1 month since July 1, 2024 (AB 12, Civ. Code 1950.5) | Confirmed. Small landlords (natural person, all-natural-person LLC, or family trust owning no more than 2 properties with no more than 4 units) may charge 2 months, except when the tenant is a service member. "Most" covers this. | CBS Sacramento; Brownstein (bhfs.com); CAA |
| L5 | CA deposit refund deadline 21 days | Confirmed: 21 calendar days after the tenant vacates (1950.5(g)). | leginfo bill digest; secondary legal summaries |
| L5 | TX deposit refund deadline 30 days (Prop. Code 92.103) | Confirmed: on or before the 30th day after the tenant surrenders the premises. The landlord's duty depends on the tenant giving a written forwarding address (92.107). | Justia/Texas statute text; Texas State Law Library |
| L6 | NY late fee cap is the lesser of $50 or 5% of monthly rent (RPL 238-a) | Confirmed. A fee is allowed only once rent is more than 5 days late. | newyork.public.law 238-a; Beco v Ritter (3d Dept 2021) |
| L7 | Greystar $24M settlement with FTC and Colorado AG, Dec 2025, over alleged hidden fees | Confirmed. Announced Dec 2, 2025. $23M goes to the FTC for refunds and $1M to Colorado. Mandatory fees (pest control, valet trash, package concierge, utility admin) were left out of advertised rent. The script calls them "alleged," which is correct framing. I could not confirm no-admission/denial language in the search excerpts, so the script should not say Greystar "denied wrongdoing." It currently doesn't, and that is fine. | FTC; Multifamily Dive; ConsumerAffairs; Covington InsidePrivacy; Frankfurt Kurnit |
| L8 | FTC rental-fee rule "still in its earliest stage" as of Oct 2026 | Confirmed as of today. The FTC sent the ANPRM to OMB on Jan 30, 2026, published it on Mar 12, 2026 (FR Doc 2026-04907, Docket FTC-2026-0266), and comments **closed Apr 13, 2026**. A search on Oct 20, 2026 found no NPRM or later action. Context: the Dec 2024 fee rule (effective May 12, 2025) covers only live-event tickets and short-term lodging and excludes long-term rentals. | ftc.gov press releases (Jan and Mar 2026); Kirkland; NAA; Freshfields |

## Issues and fixes

1. **L2: "Many" overstates the evidence (labeling).** Sources say 1 to 2 months is typical. Two months is common but not shown to be "many." Change to "Some". On screen, the median is gross rent. That is optional but more accurate in the spoken line.
   - text: `Some lease-break fees equal 2 months' rent, and the 2024 US median gross rent was $1,487.`
   - say: `Some lease-break fees equal two months' rent, and the 2024 US median gross rent was one thousand four hundred eighty-seven dollars.` (21 words, net +1)
   - post.ig: replace `Many early-termination fees run about 2 months' rent;` with `Some early-termination fees equal 2 months' rent;`
   - The board stays as is. `Example: 2-month fee` (20 characters) already labels the example.

2. **post.ig / post.yt_desc: "still at the comment stage" is inaccurate.** The comment period closed April 13, 2026.
   - ig: replace `as of Oct 2026, an FTC rental-fee rule was still at the comment stage.` with `as of Oct 2026, an FTC rental-fee rule was still only an advance notice (comments closed April 2026).`
   - yt_desc: replace `as of October 2026 an FTC rental-fee rule was still at the comment stage.` with `as of October 2026 an FTC rental-fee rule was still only an advance notice; comments closed in April 2026.`

3. **L8: time word / staleness.** "As of October 2026" will be about 2 months old on Dec 19. It is true and dated, so it is acceptable. Re-verify the FTC docket (FTC-2026-0266) the week of posting. If an NPRM is published before Dec 19, this line becomes wrong. To make the date more precise (optional):
   - text: `As of mid-Oct. 2026, the FTC's rental-fee rule was still in its earliest stage.`
   - say: `As of mid-October 2026, the F T C's rental-fee rule was still in its earliest stage.` (16 words, unchanged)
   - board line 3: `As of mid-Oct 2026` (18 characters)

4. **L9: caption does not match narration.** Caption: "holds the real price". Spoken: "is where the real price lives." Make them match:
   - say: `So the lease, not the listing, holds the real price.` (10 words, net -2)

5. **L1: hook is a bit slow.** It is true and specific, but "two thousand nine hundred seventy-four dollars" takes about 4 seconds to say, and "Example:" up front softens it. Optional stronger version that is still labeled:
   - text: `One lease clause can cost $2,974. Example:`
   - Or keep the current line. The example label is required and is acceptable. Not a FAIL item.

6. **L5 (minor): Texas clock.** The 30 days also depends on the tenant giving a forwarding address in writing. "after move-out" is acceptable for a short. No change required.

7. **Header (minor): "Lease clauses to read before signing"** reads slightly like an instruction. Optional neutral version: `Lease clauses that\ncost renters money`.

8. **L3 auto-renewal:** a general description, not tied to a specific number. Acceptable. No advice phrasing.

## Other checks
- Advice, price predictions, political opinion: none. "Not financial advice" disclaimer is present.
- Quotes: none.
- Greystar's numbers are not generalized to the industry: OK.
- On-screen values match spoken values: yes on all numeric lines (L1, L2, L4, L5, L6, L7). The only mismatch is the L9 wording (issue 4).
- Limits: stat label/sub ("CA deposit cap" 14, "most since 7/2024" 17, "NY late fee cap" 15, "whichever is less" 17). Values "1 month" 7 and "$50 or 5%" 9. Compare values "21 days" and "30 days" are 7 each. Compare subs are 14. News headline "Greystar: $24M deal" is 19. Board lines are 20 or fewer. List items are 16 or fewer. Prop label "Lease" is 5. post.title is 50. tiktok is 148. All within limits.
- keep:true: none present.
- Cover/title payoff: "$2,974 lease clause" is paid off by L1-L2. "(and 3 more)" is paid off by auto-renewal, deposits and late fees.
- Spoken words: 137 now. With fixes 1 and 4: 137 + 1 - 2 = **136** (within 115-138).
- Nothing in the script is phrased as an instruction to the viewer.

VERDICT: FAIL

## Round 2 (editor)
Applied fixes 1-4 ("Some", median gross rent, FTC ANPRM wording "comments closed April 2026", "As of mid-October 2026", line 9 narration matched) and neutral header.
VERDICT: PASS
