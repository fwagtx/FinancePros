# Fact-check: 2026-12-15-explainer ("Why rent is so much higher in some cities")

Checker: independent (did not read .research.md). Checked: Friday Oct 16, 2026. Posts: Tue Dec 15, 2026.
Note: checker-rules.md says "today is September 30, 2026"; the task file says October 16, 2026. I used October 16.
Tools: WebSearch only. Direct fetches of zumper.com, ktvu.com, kioncentralcoast.com, culturemap.com and fred.stlouisfed.org all failed (DNS/proxy), so verification relies on search excerpts of the official source plus outlets. Math recomputed in Python.

## Claims

| # | Claim (line) | Verdict | Source |
|---|---|---|---|
| 1 | SF median 1BR $4,400, Zumper September 2026 report (L1, L2, cover, post) | VERIFIED | KPIX/KION (Sep 29, 2026), KTVU, WLRN (Oct 6, 2026, Zumper Sept report: NYC $4,580, SF $4,400). One outlet (Latination, Oct 3) calls it the "October report"; most sources say September. Keep "Sept 2026". |
| 2 | SF 1BR +25.4% y/y, Zumper ties it to AI hiring (L4, post) | VERIFIED | KPIX/KION: "rents in San Francisco have jumped 25.4% for a one-bedroom"; Zumper statement attributes it to AI-sector hiring plus very little new supply (also cites return-to-office). |
| 3 | Houston median 1BR $1,050, Aug 2026, -14.6% y/y (L2, L7, post) | NOT CORROBORATED | Only CultureMap Houston (local) and a realtor blog repeating it. Zumper's own Houston pages in search show other numbers ($1,230 July 2026 city page; $1,219 rolling). Rent.com shows -5%. It does not meet the rule (official source or two reputable outlets). It is also a different month (Aug) from SF (Sept), and line 2's spoken text doesn't say the months. |
| 4 | "About four times" (hook, cover, titles) | MATH OK, BASIS FAILS | 4,400 / 1,050 = 4.19. With Zumper's own Houston page (~$1,230) it is about 3.6x. Because the ratio rests on claim 3, it has to change. |
| 5 | SF County permits 2020-2024: 2,004; 2,519; 2,044; 1,136; 770 (L5 chart) | VERIFIED | FRED BPPRIV006075 (Census BPS, annual, all structure types). 2021 to 2024 is -69%. |
| 6 | Houston metro permitted 65,075 homes in 2025 (L7, post) | VERIFIED | Census BPS 2025 annual highlights: Houston CBSA 65,075, second after Dallas 66,179. Secondary: InMyArea/Orion ">65,000". |
| 7 | Comparison fairness | NEEDS LABEL | SF is the county (~0.8M people, 2024); Houston is the whole metro (~7M+, 2025). The geography and year differ. The on-screen sub says "Metro", but the spoken words have to make it clear too (fix below). |
| 8 | Zoning / height limits / land cost (L6) | OK, NEUTRAL | It describes a mechanism and takes no side. |
| 9 | Advice / predictions | NONE | |
| 10 | Staleness by Dec 15 | OK if fixed | Every rent figure is dated (Sept 2026). No "today/this week". Newer Zumper reports (Oct, Nov) will be out by Dec 15; the dated labels keep the figures true. |
| 11 | Spoken vs on-screen | OK after fixes | Line 2's spoken words currently leave out the months that appear on screen. |
| 12 | Hook strength | OK | It is short and specific, and the video answers the "why" question. The replacement keeps that pattern. |
| 13 | compare values <= 7 chars; keep:true template check | OK | No keep:true lines. |

## Replacement data (corroborated)
Use Zumper's **national median 1BR, September 2026: $1,518**, from the same report and month as SF (WLRN Oct 6, 2026; Zumper national report page via search). 4,400 / 1,518 = **2.90**, so it is spoken as "nearly triple" with "2.9x" on screen. Houston stays in the video as the supply contrast (claim 6, Census-verified). Houston's rent figure is removed.

## Required fixes (line index is 0-based; the raw.json was not edited)

- **cover**: title -> `Why Is SF Rent Nearly 3x?`; value -> `2.9x` (label `1BR` unchanged).
- **L0**
  - text -> `San Francisco rent is nearly 3x the US median. Why?`
  - say -> `San Francisco rent is nearly triple the US median. Why?` (10 words)
  - scene.title -> `SF 1BR vs the [US]`; scene.value -> `2.9x`
- **L1**
  - text -> `Median one-bedroom rent, Sept 2026: $4,400 in SF vs $1,518 nationwide, per Zumper.`
  - say -> `In September twenty twenty-six, Zumper's median one-bedroom was four thousand four hundred dollars in San Francisco, versus fifteen hundred eighteen nationwide.` (21 words)
  - scene.right -> `{"label": "US median", "value": "$1,518", "tone": "neutral", "sub": "Zumper, Sept 2026"}`
- **L3**
  - text -> `Demand: SF one-bedroom rent rose 25.4% in a year. Zumper ties it to AI hiring.` (unchanged)
  - say -> `Demand first. San Francisco's one-bedroom rent rose twenty-five point four percent in a year, and Zumper ties that to AI hiring.` (21 words; fixes the dangling "San Francisco's rose")
- **L6**
  - text -> `Compare Houston: its whole metro area permitted 65,075 homes in 2025 (Census).`
  - say -> `Compare Houston, whose whole metro area permitted sixty-five thousand seventy-five homes in twenty twenty-five.` (14 words; removes the uncorroborated -14.6%)
  - scene.label -> `Houston metro permits`; scene.sub -> `Whole metro, 2025, Census`
- **post.title** -> `Why a San Francisco 1BR rents for nearly 3x the US median`
- **post.ig** -> replace lines 1-4 with:
  `Why does a San Francisco one-bedroom rent for nearly 3x the US median?`
  `Median 1BR rent, Sept 2026: $4,400 in San Francisco vs $1,518 nationwide, per Zumper.`
  `SF rent rose 25.4% in a year as AI hiring added demand. SF County permitted just 770 homes in 2024, down from 2,519 in 2021.`
  `Houston's whole metro area permitted 65,075 homes in 2025, second most in the US.`
  (The rest stays as is: sources line, disclaimer, follow line, hashtags.)
- **post.tiktok** -> `Why SF rent is nearly 3x the US median: jobs vs homes built. Not financial advice. #moneytok #personalfinance #rent #housing #financeprostv` (under 150 chars)
- **post.yt_desc** -> `A San Francisco one-bedroom had a median rent of $4,400 in September 2026, nearly three times the $1,518 national median (Zumper). The gap comes down to supply and demand: AI hiring added demand while San Francisco County permitted just 770 homes in 2024 (Census). Houston's whole metro area permitted 65,075 in 2025. News and education, not financial advice. #Shorts #rent #economics`
- **post.tags**: change `houston rent` -> `housing costs`.

Word count: currently 136. After the fixes: 136 - 11 + 10 - 18 + 21 - 19 + 21 - 21 + 14 = **133** (within 115-138). No trims needed.

Math check: 4,400 / 1,518 = 2.899, "nearly triple" and "2.9x". 2,519 -> 770 is -69.4%.

Optional, not required: line 7's split title "Same jobs, new homes?" is loose. "Jobs vs new homes" reads more cleanly.

VERDICT: FIX

## Round 2 (editor)
Applied all fixes: Houston rent replaced by Zumper US median $1,518 (Sept 2026); hook "nearly triple" (on-screen ~3x); Houston kept only as metro permits contrast; captions and tags updated; split title "Jobs vs new homes".
VERDICT: PASS
