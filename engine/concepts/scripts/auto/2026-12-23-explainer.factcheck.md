# Fact-check: 2026-12-23-explainer (pre-qualified vs pre-approved)

Checked October 24, 2026 for posting Wednesday, December 23, 2026, 12 PM Central. Line indexes below are **0-based**. Spoken word count is 138. None of the fixes adds words.

## Verified claims
- **Line 1, CFPB.** The CFPB says: "Lenders use the terms 'prequalification' and 'preapproval' differently." It also says both letters "are not guaranteed loan offers." The script paraphrases this accurately.
- **Line 2, soft vs hard / self-reported vs verified.** The CFPB says *some* lenders base prequalification on unverified, self-reported information and preapproval on verified information. It also says lenders may check credit for either letter. The split title "Often..." correctly frames this as typical, not a rule. The spoken line does not say "often", but it does not claim a rule either, so this is OK.
- **Line 3, myFICO.** For most people, one additional inquiry takes less than five points off their FICO Scores. Experian repeats this, citing FICO. "<5 pts" on screen matches "under five points" in the narration. OK.
- **Line 4, rate-shopping window.** myFICO says the window is any 14-day span on older FICO versions and any 45-day span on the newest versions. This applies to mortgage, auto and student loan inquiries. OK.
- **Line 5, worked example.** 3 mortgage pulls in 14 days count as 1 inquiry. This falls inside both windows and is labeled "Example"/"Say". The math is correct. On-screen 3 → 1 matches the narration.
- **Line 6, FTC v. Credit Karma (announced Sept 6, 2022).** The $3 million figure is correct. The FTC press release says that "for many offers, almost a third of consumers who applied were in fact denied." Credit Karma neither admitted nor denied the allegations and publicly disagreed with them. The headline "FTC: $3M settlement" (19 chars) matches the narration.
- **Line 7, OptOutPrescreen.com.** The FTC confirms a 5-year opt-out online or by phone. The permanent opt-out needs a signed, mailed form. The phone number in the IG caption, 1-888-5-OPT-OUT (1-888-567-8688), is correct.
- **Hook (line 0).** "That pre-approved letter isn't a loan. Neither is pre-qualified." This is true, specific and 10 words (≤12), and the CFPB backs it up. Hook title is fine (≤22). Prop label "PRE" is fine.
- **Cover.** "<5 pts" fits (≤9) and the video pays it off in line 3. The title "Pre-Approved Isn't Approved?" is paid off in lines 0–2 and 6.
- **Limits.** Every limit passes:
  - stat label 14, sub 15
  - compare values "14 days"/"45 days" = 7 each, subs 16
  - news headline 19
  - board lines ≤20 ("5 years or permanent" = 20, "Words vary by lender" = 20)
  - split titles ≤11 ("Pre-approve" = 11), items ≤13
  - list items fine
  - post.title 48
  - tiktok exactly 150 (at the limit, OK)
- **Content rules.** No keep:true lines. No advice, price predictions or politics. No time words that will be stale on Dec 23. The 2022 case is explicitly dated.

## Issues
1. **Line 6: allegation framing and an unclear "It" (should fix).** "the FTC said" is softer than "alleged". "It disagreed but paid" could be read as the FTC disagreeing. Also, the FTC said "almost a third" applied to *many* offers, not to all of them. The "nearly a third" paraphrase is acceptable, but use "alleged".
   - Replace `say` with (same word count):
     `For cards, in twenty twenty-two the F T C alleged nearly a third of applicants for Credit Karma's pre-approved offers were denied. Credit Karma disagreed; settled for three million.`
   - Replace `text` with:
     `For cards, in 2022 the FTC alleged nearly a third of applicants for Credit Karma's "pre-approved" offers were denied. Credit Karma disagreed; settled for $3 million.`
2. **Line 7: "stops it" is slightly absolute (minor, optional).** The FTC says the opt-out covers only offers built from credit-bureau lists, and it can take weeks to take effect. Optional same-word-count swap: change "stops it" to "cuts it" in both `text` and `say`.
3. **Line 1: wording (no change needed).** "use both words differently" matches the CFPB's own phrasing.

## Sources
CFPB Ask CFPB, "What's the difference between a prequalification letter and a preapproval letter?"; myFICO Credit Inquiries page and myFICO rate-shop blog; Experian on inquiry impact; FTC press release, Sept 6, 2022, and NPR, American Banker coverage of FTC v. Credit Karma; FTC consumer page "What To Know About Prescreened Offers".

VERDICT: PASS

## Round 2 (editor)
Applied fixes 1-2.
VERDICT: PASS
