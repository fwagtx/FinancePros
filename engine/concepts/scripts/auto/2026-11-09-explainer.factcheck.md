# Fact-check: 2026-11-09-explainer ("What happens in a stock market crash")

Checked on Oct 1, 2026, for posting Nov 9, 2026. I used only the script JSON. I checked claims with web search and redid all the math in Python.

## Verified claims

| Claim | Result | Source |
|---|---|---|
| S&P 500 close Feb 19, 2020: 3,386.15 (record) | Correct | Wikipedia S&P closing milestones; Fortune/NPR Aug 18, 2020 |
| Mar 16, 2020 close: 2,386.13 | Correct (-12%, worst day since 1987) | CNN live, Mar 16, 2020 |
| Mar 23, 2020 close: 2,237.40 (trough) | Correct | Wikipedia 2020 crash; NPR |
| Mar 31, 2020 close: 2,584.59 | Correct (StatMuse/FT Portfolios). One AP-style story printed 2,584.47, probably an early print. 2,584.59 is the standard figure. | StatMuse; Nasdaq/AP |
| Apr 30, 2020 close: 2,912.43 | No source shows the exact number, but it fits: 2,912.43 / 2,584.59 = +12.68%, which matches the reported April gain of 12.68% (best month since Jan 1987). I accept it as a derived value. | CNN, CNBC Apr 30, 2020 |
| Aug 18, 2020 close: 3,389.78 (record) | Correct | NPR, CBS, Fortune, Aug 18, 2020 |
| "34% in 33 days" | 3,386.15 to 2,237.40 = -33.92%, which rounds to 34%. Feb 19 to Mar 23 is 33 calendar days (23 trading days). Both correct. | Python |
| "51% climb to get even" | 3,386.15 / 2,237.40 - 1 = +51.34%. Also 1/0.66 - 1 = 51.5%. Correct. | Python |
| Chart x-values 0/26/33/41/71/181 | All match the calendar-day count from Feb 19, 2020 | Python |
| Circuit breakers 7%/13%/20% vs prior S&P 500 close; 15-min halt only before 3:25 pm ET; 20% closes the day | Correct | SEC Investor.gov glossary; NYSE |
| Halted 4 times in March 2020 (Mar 9, 12, 16, 18, all Level 1) | Correct. These were the first market-wide halts since Oct 27, 1997, under the old Dow-point system. | NYSE/SEC MWCB Working Group report |
| Reg T 50% initial / FINRA 4210 25% maintenance | Correct. The FINRA 4210 amendments effective June 4, 2026 replaced the pattern-day-trader rules but did not change the 25% maintenance minimum for long equity. | FINRA; WilmerHale Apr 2026 |
| Margin example: $10k, $5k borrowed, -34% gives $6,600; equity $1,600 = 24.24% (< 25%) | Math correct. It is labeled as an example. The 50% borrowed matches Reg T. | Python |

## Issues and fixes

1. **Chart title too long (lines 8-9, scene.title).** "S&P 500 close, days after Feb 19, 2020" is 38 characters, over the 28-character limit, and it squeezes the units into the title. Fix: change the title to **"S&P 500 after Feb 19, 2020"** (26 chars). If the template supports an axis label, add one such as "Days after the Feb 19 peak" (26). The chart itself is honest: x is proportional to calendar days, every plotted point is a real close, and the +51% note sits at the trough. The straight line from day 71 to day 181 hides the swings in between, which is fine for a short video.
2. **Stat label slightly over 28 chars (line 5).** "Market-wide halts, March 2020" is 29 characters. Fix: "Market-wide halts, Mar 2020" (27). All other sub-labels are 28 characters or fewer.
3. **Unclear "it" (line 8).** After two lines about the margin example, "it closed at a record again" doesn't say what "it" is. Fix: "Then buyers returned. On August 18, 2020, the S&P 500 closed at a record again." Update both text and say.
4. **Hook length (line 1), minor.** The hook is true, specific and pays off the cover, but spoken it runs about 3.5 seconds. Optional tighter version: "Stocks lost 34% in just 33 days." Keep 2020 on screen. Also optional: "stocks" means the S&P 500, and the scene labels it, so this is fine.
5. **Margin nuance (line 7), minor.** Many brokers set house maintenance requirements above 25%, so a margin call can come sooner. Optional: "Under 25%, the FINRA minimum, that's a margin call..." The current wording is not wrong.
6. **Circuit-breaker caption (line 4), minor.** The caption leaves out "before 3:25 pm ET". The word "can" covers this, and the post text includes it. No change required.

Other checks:
- No advice, predictions or political opinion. The post includes "Past recoveries don't predict future ones" and "not financial advice."
- No stale time words for Nov 9.
- On-screen and spoken numbers match on every line. The caption says "about 24%" and the stat shows 24.2%, which agree.
- No quotes in the script. Nothing is generalized from a single company.
- The cover ("34% Gone in 33 Days") is paid off by the video.

VERDICT: PASS

## Round 2 (orchestrator)
- Chart title "S&P 500 after Feb 19, 2020"; stat label "Market-wide halts, Mar 2020"; L8 names the S&P 500.

VERDICT: PASS
