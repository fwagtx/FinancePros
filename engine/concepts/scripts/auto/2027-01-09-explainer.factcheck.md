# 2027-01-09-explainer fact-check: Keeping up with the Joneses

Checked 2026-11-10 for posting Sat Jan 9 2027. Independent web checks (WebSearch; philadelphiafed.org, fedinprint.org and
grammarphobia.com are blocked in this session, so the WP 18-16 wording was confirmed through search excerpts of the paper,
Bloomberg/BloombergQuint 2018, WEF 2016 and CBS coverage).

## Verified facts
- Agarwal, Mikhed & Scholnick, Philadelphia Fed WP 18-16 (2018), published RFS 33(1) 2020: a win equal to the sample's median
  annual income (C$29,229) raises neighbors' bankruptcies over three years by 0.03, "a 6.59% increase relative to the average
  bankruptcy rate of 0.455" in the event window. It is a RELATIVE rise on a small base (aggregate rate of neighbors in the same
  six-digit postal code), not a change in any one person's odds. Bloomberg rounds to 6.6%. CONFIRMED.
- Six-digit Canadian postal codes: median about 13 households. CONFIRMED.
- Visible vs less visible: "the magnitude of the neighbor's lottery win is related to the dollar value of more visible, but not
  less visible consumption assets, of neighboring bankruptcy filers" (house, car vs furniture). It is a win-size relationship,
  not a comparison of filers vs non-filers. CONFIRMED with framing fix (line 3).
- Kuhn, Kooreman, Soetevent & Kapteyn, AER 101(5) 2011, Dutch Postcode Lottery: nonparticipants next door to winners have
  "significantly higher levels of car consumption than other nonparticipants." No bankruptcy finding. CONFIRMED.
- Bankrate social media survey, fielded Aug 16-23 2023 (YouGov): those who impulse-bought from social media in the past 12 months
  spent an AVERAGE of $754 in that period. CONFIRMED (fix "spent ... a year" to "averaged ... in a year").
- $754 x 10 = $7,540, labelled "our math", no growth. Math CORRECT.
- Pop Momand's "Keeping Up with the Joneses" began March 31, 1913; OED's earliest cite is the 1913 strip title; the Joneses are
  mentioned but never shown (the McGinis family chase them). CONFIRMED. (One unverified claim of a Twain usage written 1901,
  published 1923; "coined" is the standard account, left OK.)

## Per line

0 HOOK - FIX (overgeneralizes: "your bankruptcy odds" implies an individual risk change; study measures a small relative rise
  in the bankruptcy rate of the winner's postal-code neighbors in Canada).
  TEXT: When a neighbor wins the lottery, nearby bankruptcies tick up.
  SAY: When a neighbor wins the lottery, nearby bankruptcies tick up.
  SCENE title: "Their win, nearby [debt]"  (value "+6.6%" OK, 5 chars)

1 OK. (~13 = median households per six-digit postal code.)

2 FIX (6.6% must read as a relative rise on a low base, not 6.6 percentage points / "your odds").
  TEXT: A win worth a year's median income lifted neighbors' already-low bankruptcy rate about 6.6% over three years.
  SAY: A win worth a year's median income lifted neighbors' already-low bankruptcy rate about six point six percent over three years.
  SCENE sub: "Relative rise"  (value "+6.6%" OK; stat.sub max 18 chars, source stays in post copy)

3 FIX (paper links WIN SIZE to filers' visible assets; it does not say filers had more visible stuff than non-filers).
  TEXT: Bigger wins meant bankrupt neighbors held more visible stuff, like houses and cars.
  SAY: Bigger wins meant bankrupt neighbors held more visible stuff, like houses and cars.
  SCENE title: "What grew with the win"; right.title: "Less visible" (left/right items unchanged).

4 OK. (AER 2011; "spent more on cars" = higher car consumption among next-door nonparticipants.)

5 FIX ($754 is an average over the 12 months before the survey, not a recurring annual figure).
  TEXT: Your feed does it too: in 2023, Bankrate found social media impulse buyers averaged $754 in a year.
  SAY: Your feed does it too: in twenty twenty-three, Bankrate found social media impulse buyers averaged seven hundred fifty-four dollars in a year.
  SCENE: OK ("$754", sub "Bankrate, Aug 2023").

6 OK. Math correct, labelled as our math, values $754 / $7,540 within 8 chars.

7 OK.

8 OK (rhetorical, no advice).

9 OK.

HEADER: OK. COVER: OK ("+6.6%" matches spoken/onscreen).

POST - FIX (carry the same framing fixes):
  title: "A neighbor's lottery win can mean more bankruptcies nearby"  (58 chars, post.title max 60)
  ig line 1: "When a neighbor wins the lottery, nearby bankruptcies tick up."
  ig line 2: "In Canadian data, a win equal to a year's median income (C$29,229) raised neighbors' bankruptcy rate 6.59% over three years, a relative rise on a low base (Philadelphia Fed working paper, 2018)."
  ig line 3: "The bigger the win, the more visible stuff, like houses and cars, the bankrupt neighbors held."
  ig Bankrate line: OK as written ("spent an average of $754 in a year").
  tiktok: "A neighbor's lottery win can mean more bankruptcies nearby. Not financial advice. #moneytok #personalfinance #keepingupwiththejoneses #financeprostv"
  yt_desc: "A Philadelphia Fed working paper (2018) found that a Canadian lottery win equal to a year's median income raised neighbors' bankruptcy rate 6.59% over three years (a relative rise on a low base), and bigger wins went with more visible assets, like houses and cars, among bankrupt neighbors. A 2011 Dutch Postcode Lottery study (American Economic Review) found winners' next-door neighbors spent more on cars, and a 2023 Bankrate survey found social media impulse buyers spent an average of $754 in a year. News and education, not financial advice. #Shorts #keepingupwiththejoneses #personalfinance"

## Limits
Hook 10 spoken words (max 12). Total spoken words after fixes: 140 (10/14/20/13/15/22/12/15/13/6), within 115-140.
Money/hook values: +6.6%, $754, $7,540 all at most 8 characters. No advice, no predictions, no stale time words.

Applied to raw.json on 2026-11-10; check.py: OK, 10 lines, 140 spoken words, hook 10 words.

VERDICT: FIX

## Round 2 (editor)
- All fixes applied by checker; check.py OK (140 words).
VERDICT: PASS
