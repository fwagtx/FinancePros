# Fact-check: 2027-01-10-explainer (tragedy of the commons / Northern cod)

Checked 2026-11-11 for posting Sun 2027-01-10. Note: page fetches to DFO, NAFO, publications.gc.ca and faculty.lsu.edu are blocked in this session (and the one allowed Firecrawl scrape of the Library of Parliament paper only returned an archive redirect). So this check relies on web-search results that cite several primary sources.

## Lines

**0 hook: FIX.** "Why would fishers wipe out..." puts the blame on fishers in general. Sources say the overfishing came mainly from offshore trawler fleets: foreign fleets took about 80% of the 1968 catch, and Canadian and US trawlers later replaced them. Inshore fishers warned for years that catches were falling, and managers ignored them (Heritage NL). "Fleets" is more accurate and keeps the hook.
- text/say -> `Why would fleets wipe out the fish that paid their bills?` (11 words)
- scene title "Why wipe out your [paycheck]?": OK.

**1 chart: FIX (1988 point only).**
- 1968 "topped 800,000 t": OK. DFO SAR 2018/038 says "over 800,000 t". The Library of Parliament (BP-313E) gives 800,000 t and the Canadian Encyclopedia gives 810,000.
- 1978 140,000 t: OK. DFO and the Baird et al. NAFO study give ~140,000. BP-313E gives 139,000.
- 1988 266,000 t: NOT CONFIRMED. The 266,000 t figure turns up as the projected F0.1 catch (advice) for 1988 in Baird et al., not as actual landings. NAFO SCR 92/018 gives ~242,000 t for 1988. DFO SAR 2018/038 says "about 240,000 t through much of the 1980s".
  - points (lines 1 and 2) -> `[[1968, 800], [1978, 140], [1988, 240], [1998, 5]]`
- 1998 ~5,000 t: OK (DFO SAR 2018/038 Table A1 = 5 thousand t).
- text/say: OK.

**2 "-99%, our math": OK.** (800 - 5) / 800 = 99.4%. Labelled as our math and refers to the catch, not the stock.

**3 1992 moratorium, ~30,000 NL jobs: OK.** Crosbie announced it on July 2, 1992. Heritage NL says about 30,000 in NL (about 12% of the labour force). The Canadian Encyclopedia says nearly 30,000 in NL out of about 40,000 overall.

**4 Hardin quote: OK.** "Freedom in a commons brings ruin to all." is the exact sentence, from Science 162:1243-1248, Dec 13 1968 (WSU and Stanford reproductions).

**5-6 squirrel math: OK.** It is internally consistent: +5 gain, a loss of 10 split 10 ways means -1 each, so the net is +4 and every squirrel has the same incentive. It is labelled "our math". Minor point: the script never says why taking 5 costs the tree 10 (the brief means lost future crop). That is acceptable for an illustration, and no change is needed.

**7 Ostrom: FIX (wording).** The 2009 economics prize, shared with Williamson "for her analysis of economic governance, especially the commons", is OK, and so are the boundaries, own rules and monitoring. Ostrom's principle is "graduated sanctions", which are not necessarily fines.
- text -> `But Elinor Ostrom won the 2009 economics Nobel showing communities can fix it: clear members, own rules, monitoring, rising penalties.`
- say -> `But Elinor Ostrom won the twenty oh nine economics Nobel showing communities can fix it: clear members, own rules, monitoring, rising penalties.`
- scene item "Rising fines" -> `Rising penalty` (14-character limit)

**8 recovery: FIX (overclaim).** The June 12, 2026 DFO decision put the 2026-27 TAC at 59,000 t (from 38,000 t, +55%), and the 2026 assessment put the stock in the "healthy zone" for the first time since 1992. That rating uses new benchmarks with about a 60-70% probability, and Oceana Canada and Oceans North say the recovery is fragile and not yet a return to abundance. "Came back" overstates it.
- text -> `With limits, cod partly recovered: in 2026, Canada's quota hit 59,000 tonnes.`
- say -> `With limits, cod partly recovered: in twenty twenty-six, Canada's quota hit fifty-nine thousand tonnes.`
- The stat scene (59,000 t, Fisheries Canada) is OK.

**9 CTA: OK.**

## Header, cover and post
- header, cover ("Who Ate the Cod?", -99%) and title: OK.
- ig: FIX. Replace the first line with the new hook. Change the quota line to `In 2026, Canada set a 59,000-tonne northern cod quota as the stock reached DFO's healthy zone; conservation groups say recovery is still fragile.`
- tiktok: FIX -> `Why fleets wiped out the cod that paid them. Not financial advice. #moneytok #personalfinance #economics #tragedyofthecommons #financeprostv`
- yt_desc and tags: OK.
- No advice, predictions or political opinion found. Time words are correct for Jan 2027.

Spoken words are unchanged at 140. check.py: OK.

VERDICT: FIX

## Round 2 (editor)
- Checker applied all fixes; check.py OK.
VERDICT: PASS
