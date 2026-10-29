# Fact-check: 2026-12-28-lf-explained (What causes a recession)

Checked Oct 29, 2026 for a Dec 28, 2026 post. Spoken words now: 1784. With all required fixes below: about 1790, which is inside 1550-1800.

Limits on sources: nber.org, federalreservehistory.org, fred.stlouisfed.org and the BLS API could not be reached from this session. For those, I relied on search-result excerpts of the official pages and on reputable secondary sources. I did not use the writer's research notes as evidence.

## Priority 1: "As of October 2026, NBER hadn't announced a recession" (lines 64, 67)

- **Is it true today?** Yes. No NBER announcement of a business-cycle peak after the April 2020 trough turned up anywhere. Secondary trackers dated Oct 2, 2026 agree, and the ALFRED recession-indicator release from Sept 2026 shows no new recession.
- **Is it safe for Dec 28?** Not fully. The sentence is still literally true on Dec 28, but it pins the video to a date two months before it posts. NBER could announce a peak in November or December, and the line would then mislead. Viewers will also read "As of October" as stale news.
- **Fix:** frame it as the time of production, using the line 64 and line 67 replacements below.

## Required fixes

### lines[4]: "as first reported" does not match the on-screen values
- **Problem:** The first reports were Q1 -1.4% (advance, Apr 2022) and Q2 -0.9% (advance, Jul 28, 2022). The values shown, -1.6% and -0.6%, come from the third estimate of Sept 29, 2022. The YT description cites that release too.
- **Replacement:**
  - text: "Here's a twist: in 2022, the economy shrank two quarters in a row, as reported at the time, and it still wasn't officially a recession."
  - say: "Here's a twist. In twenty twenty-two, the economy shrank two quarters in a row, as reported at the time, and it still wasn't officially a recession."
  - scene: change both `sub` values from "annual rate, BEA" to "BEA, Sept 2022".
- **Description:** in yt_desc, change "like those first reported in 2022" to "like those reported in 2022".

### lines[64]: "after 27 months" is wrong, and "As of October 2026" will be stale
- **Problem:** The 10-year minus 3-month spread went negative on Oct 25, 2022 and turned positive around Dec 13, 2024. That is about 25.6 months, not 27. The 27-month figure seems to belong to the 2-year/10-year spread.
- **Note:** The spread also dipped below zero briefly in Feb-Mar 2025. The replacement does not claim it stayed positive, so it remains accurate.
- **Replacement:**
  - text: "The gap turned positive in December 2024, after about 25 months. When we made this video, NBER hadn't announced a recession after it."
  - say: "The gap turned positive in December twenty twenty-four, after about twenty-five months. When we made this video, N B E R hadn't announced a recession after it."

### lines[67]: "as of October 2026" will be stale by posting
- **Fact checked:** The Sahm rule tripping with the July 2024 report at 4.3% is correct.
- **Replacement:**
  - text: "It went off with the July 2024 jobs report, when unemployment hit 4.3%. Again, when we made this video, NBER hadn't announced a recession."
  - say: "It went off with the July twenty twenty-four jobs report, when unemployment hit four point three percent. Again, when we made this video, N B E R hadn't announced a recession."

### lines[68]: the September 2026 rate will be two reports out of date
- **Fact checked:** 4.2% for September 2026 is correct. BLS released it Oct 2, 2026; the rate was up from 4.1% in August.
- **Problem:** By Dec 28, the October and November 2026 reports will both be out, so this will not be the latest reading. Label it as the latest at production time.
- **Replacement:**
  - text: "For reference, unemployment was 4.2% in September 2026, the latest BLS reading as we made this. That's a data point, not a forecast."
  - say: "For reference, unemployment was four point two percent in September twenty twenty-six, the latest B L S reading as we made this. That's a data point, not a forecast."
  - scene: no change.

## Recommended (not required)

- **lines[21]:** The embargo began in October 1973 and lasted until March 1974, so the recession that started in November 1973 began during it, not after it ended. Suggested replacement:
  - text: "...: 16 months, right after the Arab oil embargo began."
  - say: "November nineteen seventy-three to March nineteen seventy-five lasted sixteen months, right after the Arab oil embargo began."
  - This adds one word.
- **lines[44]:** The on-screen sub "NBC, citing Lehman" is easy to confuse with Lehman's 2008 bankruptcy in line 52. Suggest changing it to "NBC News". The figures, about $14 in 1978 and above $30 by 1980, are consistent with Fed History's 1979 shock account, which says oil more than doubled to $39.50.
- **lines[63]:** 68.2% for April 2023, the highest since late 1982, is confirmed by Benzinga coverage of the NY Fed model. The model went higher still in May 2023, at 70.85%. The wording "In April 2023" stays accurate.

## Verified as correct

- **Lines 0-2, cover and post:** The Great Recession ran Dec 2007 to Jun 2009, or 18 months. NBER announced it on Dec 1, 2008, about a year after it began.
- **Lines 8-13:** The NBER definition, the three tests (depth, diffusion and duration), the point that one extreme test can offset another, and that NBER does not use the two-quarter rule.
- **Line 14:** The 2001 recession had GDP declines in Q1 and Q3 but not two in a row (NBER FAQ).
- **Line 15:** 2022 unemployment averaged 3.6%.
- **Line 17:** The March 2001 peak was announced Nov 26, 2001, about 8 months later. The Feb 2020 peak was announced June 8, 2020, about 4 months later.
- **Lines 20-28:** Seven recessions since 1973, with dates and lengths that match NBER: 16, 6, 16, 8, 8, 18 and 2 months. The 2020 recession is the shortest on record; the 1980 recession, at 6 months, was the previous shortest.
- **Lines 29-31, chart:** Annual averages for 1990-2024 match the BLS CPS series. I spot-checked 1992 7.5, 2003 6.0, 2010 9.6, 2020 8.1, 2021 5.3 and 2024 4.0. For 2025, 4.3% is the 11-month average because the October 2025 household survey was not collected during the shutdown (EPI, Kentucky LMI, BLS LAUS release). Every hump lines up with a recession.
- **Lines 32-34:**
  - Unemployment was 10.8% in Nov-Dec 1982.
  - It was 14.8% in April 2020 (as revised; first reported as 14.7%), the highest since 1948.
  - Payrolls fell 20.5 million in April 2020, the largest drop on record.
- **Lines 36-37:** Unemployment peaked at 10.0% in Oct 2009 and at 6.3% in June 2003.
- **Line 42:** Oil went from $2.90 to $11.65 by Jan 1974 (Fed History).
- **Lines 45-47:** Fed History says the Fed let the funds rate approach 20 percent, that borrowing-reliant sectors were hit, and that by October 1982 inflation had fallen to 5 percent.
- **Line 49:** The Nasdaq fell about 78% from March 2000 to October 2002.
- **Line 51:** National home prices started falling after mid-2006.
- **Line 52:** Lehman went bankrupt in Sept 2008.
- **Line 60:** The 2023 claim that an inversion preceded each of the last eight recessions since about 1970 is consistent with reporting. I could not retrieve the CNBC article itself, so its exact wording is unconfirmed; the line paraphrases it rather than quoting it.
- **Line 62:** The spread inverted in late October 2022 (Oct 25).
- **Lines 65-66:** The Sahm rule definition, and that Sahm designed it to trigger automatic stimulus payments.
- **Line 73:** 2012 unemployment averaged 8.1%.
- **Line 74:** The Fed cut to near zero on Dec 16, 2008 and Mar 15, 2020.
- **Lines 77-78, 82:** The S&P 500 fell about 57% from Oct 2007 to Mar 2009 and about 34% from Feb to Mar 2020. It regained its 2007 peak on Mar 28, 2013.
- **Line 92:** The shortest gap between recessions was Jul 1980 to Jul 1981, about a year. Gaps of more than a decade were 1991-2001 and 2009-2020.
- **Math, labeled "our own" (recomputed):**
  - $10,000 at 4.5% earns $450 a year; at 0.5% it earns $50.
  - $10,000 after a 57% drop is $4,300. 10,000 / 4,300 = 2.3256, so a gain of about 133% is needed to recover.
  - $9,000 / $3,000 = 3 months; $18,000 / $3,000 = 6 months.
- **Advice and predictions:** There are none. Lines 6 and 86 are explicit disclaimers, and line 68 says "not a forecast."
- **Text vs say:** These match apart from small phrasing differences. In line 36, the spoken "October" is clear from context.
- **Opening (line 0):** True, specific and short.
- **Layout rules:**
  - Every `keep: true` line follows a line with the same scene template.
  - All compare values are 7 characters or fewer.

VERDICT: FAIL

## Round 2 (editor)
- lines[4]: "as reported at the time"; subs "BEA, Sept 2022"; yt_desc updated.
- lines[64]: "about 25 months"; "When we made this video" wording.
- lines[67], lines[68]: date-safe wording applied.
- lines[21]: "during the Arab oil embargo"; lines[44] sub "NBC News".
VERDICT: PASS
