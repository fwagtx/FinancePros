# Fact-check: 2027-01-26 explainer (tax deduction vs tax credit)

Posting date: January 26, 2027 (filing season for tax year 2026 returns).

## Verified claims
- 2026 standard deduction: single $16,100, MFJ $32,200. Confirmed by NTU Foundation, U.S. Bank, Jackson Hewitt, and the IRS IRM 21.6.4 table.
- Child Tax Credit for 2026: up to $2,200 per child, with up to $1,700 refundable (ACTC). Confirmed by the IRS CTC page, NTU Foundation, Jackson Hewitt, and U.S. Bank.
- Chart points for the single standard deduction: 2022 $12,950, 2023 $13,850, 2024 $14,600, 2025 $15,750, 2026 $16,100. All five match the IRS IRM 21.6.4 table. The 2025 figure is the amount after the 2025 law raised it from the original $15,000; IRS "New and enhanced deductions" confirms $15,750. The years are evenly spaced, and there are 5 points.
- Math: $1,000 x 22% = $220. This is correct as a simplified example labeled "our math". It assumes the whole $1,000 falls in the 22% bracket. A credit cuts tax by $1,000 dollar for dollar, which is correct for a nonrefundable credit up to the tax owed.
- Refundable vs nonrefundable explanation: correct.

## Issues found and fixed (applied to the raw JSON)
1. Line 7: the voice did not match the screen. The caption and chart say $12,950, but the voice said "about thirteen thousand". New say: "...grew from twelve thousand nine hundred fifty in twenty twenty-two to sixteen thousand one hundred in twenty twenty-six."
2. Line 7 chart title: "Standard deduction, single" was 26 chars, too long. Changed to "Standard deduction" (18). The caption and voice still say "single".
3. Line 2 read awkwardly out loud: "...two hundred twenty, our math." Changed to "...two hundred twenty, by our math." in both text and say.
4. Line 6 time word: "In 2026" is ambiguous when posted in January 2027, because the viewer is filing tax year 2026. Changed to text "For tax year 2026, up to $1,700 per child is refundable." and say "For tax year twenty twenty-six, up to seventeen hundred per child is refundable." I dropped "per the IRS" to stay within the 140-word cap. The IRS is still credited in the post captions.
5. Cover: "$1K Off: Same?" was vague, and the video does not set up the "Off" framing. Changed to "$1K Isn't $1K" (13 chars). The hook and the deduction vs credit compare pay it off directly, and it echoes the post title "why $1,000 isn't $1,000". The cover value $220 is kept; it is spoken in the hook.

## Checked, no change needed
- Hook (line 0): 10 words, under 3 seconds. It is true and specific, and it creates a curiosity gap: why would $1,000 save only $220? The board in line 1 resolves it right away. The prop label "$1K" (3 chars) matches the spoken "thousand-dollar", so it is acceptable.
- Hook title "Deduction vs [Credit]" is 3 words. The value "$220" is spoken.
- No stale news or price predictions. No advice beyond the general framing "ask one question". No political opinion. The CTA tagline says "Education, not advice".
- Every on-screen value is spoken: $220, $1,000, $2,200, $1,700, $12,950, $16,100, and "$0" ("zero").
- Post captions (IG, TikTok, YT): figures are consistent and correct, sources are named, and the not-advice disclaimer is present. No edit needed.
- Last line is unchanged. The renderer check passes: 140 spoken words, OK.

VERDICT: PASS

## Round 2 (editor)
Reviewed applied fixes (caption/voice match, chart title, tax-year wording, cover); limits pass.
VERDICT: PASS
Editor: split left title 'Nonrefundable' overflowed its card; shortened to 'No refund'.
