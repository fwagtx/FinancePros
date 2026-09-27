"""Writes the concept episodes (scripts + drawings) as JSON. Facts are hand-checked:
- CPI-U annual averages (BLS): 1970 38.8 ... 2024 313.7 -> $100 of 1970 goods ~ $808 in 2024; $1 lost ~88% of its buying power.
- CPI peak: 9.1% year over year in June 2022, the highest since 1981 (~40 years). Fed inflation target: 2%.
- $100/month at 7%/yr compounded monthly for 30 years ~ $121,997 ($36,000 contributed).
- A U.S. tariff is paid by the U.S. importer to U.S. Customs and Border Protection; studies of the 2018-19 tariffs
  (Amiti-Redding-Weinstein 2019, Fajgelbaum et al. 2020) found near-complete pass-through to U.S. buyers.
"""
import json, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "episodes"); os.makedirs(OUT, exist_ok=True)

def L(text, group, items=(), who="ticker", say=None, cam=None):
    d = {"who": who, "text": text, "scene": {"group": group, "items": list(items)}}
    if say: d["say"] = say
    if cam: d["scene"]["cam"] = cam
    return d

def T(x, y, t, size=60, **k): return dict(k="text", x=x, y=y, text=t, size=size, **k)

# ---------------- CPI data: price of a 1970 $100 basket ----------------
CPI = [(1970, 38.8), (1975, 53.8), (1980, 82.4), (1985, 107.6), (1990, 130.7), (1995, 152.4), (2000, 172.2), (2005, 195.3),
       (2010, 218.1), (2015, 237.0), (2020, 258.8), (2021, 271.0), (2022, 292.7), (2023, 304.7), (2024, 313.7)]
BASKET = [[y, round(v / 38.8 * 100)] for y, v in CPI]            # 100 ... 808

def pt(chart, year):   # screen position of a data point (mirrors chart() in doodle.js)
    d = chart["data"]; mx = chart["max"]; x0, x1 = d[0][0], d[-1][0]
    v = dict((a, b) for a, b in d)[year]
    return chart["x"] + (year - x0) / (x1 - x0) * chart["w"], chart["y"] + chart["h"] - v / mx * chart["h"]

# ======================= A1: Paper Ticker (vertical short) =======================
ch = dict(k="chart", id="c", x=150, y=620, w=560, h=560, data=BASKET, numeric=True, max=900, title="Same stuff, priced over time", titleSize=44,
          xl=[[1970, "1970"], [1995, "1995"], [2024, "2024"]], yl=[[100, "$100"], [400, "$400"], [800, "$800"]], end="$808", endDx=30, endDy=10, endAnchor="start", draw=2.6)
cx, cy = pt(ch, 2022)
A1 = {"id": "A1-paper-ticker-inflation", "format": "vertical", "music": "lofi", "header": "Your dollar is quietly\nshrinking.", "lines": [
    L("This dollar has lost about 88 cents of its buying power since 1970. Nobody stole it.", "g1", [
        dict(k="bill", x=440, y=820, w=600, rot=-5),
        dict(k="text", x=330, y=1130, text="-88¢", size=150, font="marker", color="#E0241B", at=1.6),
        T(330, 1210, "since 1970", 60, at=2.2),
        dict(k="ticker", id="tk", x=850, y=1330, s=1.0, pose="pointleft", mood="shock", at=0.3)],
      say="This dollar has lost about eighty-eight cents of its buying power since nineteen seventy. Nobody stole it."),
    L("The thief has a name. Inflation.", "g2", [
        dict(k="board", x=80, y=560, w=700, h=420, lines=[{"t": "INFLATION", "size": 118}, {"t": "= prices creeping up", "size": 64}], write=3.4),
        dict(k="ticker", id="tk", x=880, y=1340, s=0.95, pose="pointleft", stick=[-300, -470], mood="happy")]),
    L("Prices across the whole economy creep up a little, almost every year.", "g2"),
    L("Here's the same basket of stuff that cost 100 dollars in 1970. Today it costs about 808.", "g3", [
        ch, dict(k="ticker", id="tk", x=930, y=1340, s=0.78, pose="pointleft", mood="worried", at=0.5)],
      say="Here's the same basket of stuff that cost a hundred dollars in nineteen seventy. Today, it costs about eight hundred and eight."),
    L("And in June 2022, prices were up 9.1% from a year before. The most in about 40 years.", "g3", [
        dict(k="circle", x=round(cx), y=round(cy), rx=70, ry=60, seed=4, at=0.6),
        dict(k="text", x=round(cx) - 230, y=round(cy) + 30, text="9.1% in\na year!", size=60, color="#E0241B", at=1.2),
        dict(k="ticker", id="tk", mood="shock")],
      say="And in June twenty twenty-two, prices were up nine point one percent from a year before. The most in about forty years."),
    L("Some of this is on purpose. The Federal Reserve aims for about 2% inflation a year.", "g4", [
        dict(k="fed", x=440, y=1200, s=1.2),
        dict(k="tag", x=470, y=580, s=1.2, label="Target: 2%", rot=-6, at=1.2),
        dict(k="ticker", id="tk", x=900, y=1340, s=0.85, pose="shrug", mood="happy")],
      say="Some of this is on purpose. The Federal Reserve aims for about two percent inflation a year."),
    L("So cash sitting still slowly loses value. Money that earns more than inflation keeps up.", "g5", [
        dict(k="mattress", x=270, y=1080, s=0.95), dict(k="bill", x=270, y=950, w=300, rot=8, at=0.2),
        dict(k="arrow", x1=270, y1=640, x2=270, y2=860, bend=0.15, at=0.6),
        T(270, 1200, "cash sitting still", 50, at=0.3),
        dict(k="pot", x=800, y=1110, s=1.2, at=1.8), dict(k="arrow", x1=800, y1=660, x2=800, y2=470, bend=-0.15, color="#2E9A45", at=2.4),
        T(800, 1200, "earning more than\ninflation", 50, at=2.0)]),
    L("That's the money. Follow for more.", "end", [
        dict(k="logo", x=540, y=620, s=1.0), T(540, 720, "money news + money basics, drawn simply", 44, at=0.4),
        dict(k="ticker", id="tk", x=540, y=1340, s=1.05, pose="wave", mood="up", at=0.2)]),
]}

# ======================= A2: Paper Ticker (16:9 long-form cold open) =======================
ch2 = dict(k="chart", x=170, y=260, w=900, h=560, data=BASKET, numeric=True, max=900, title="The same basket of stuff, 1970 to 2024", titleSize=46,
           xl=[[1970, "1970"], [1980, "1980"], [1990, "1990"], [2000, "2000"], [2010, "2010"], [2024, "2024"]], yl=[[100, "$100"], [400, "$400"], [800, "$800"]], end="$808", endDx=24, endDy=40, endAnchor="start", draw=3.0)
c2x, c2y = pt(ch2, 2022)
A2 = {"id": "A2-paper-ticker-longform", "format": "landscape", "music": "lofi", "captions": False, "lines": [
    L("Since 1970, prices in America have gone up about eight times.", "g1", [
        ch2, dict(k="ticker", id="tk", x=1520, y=1000, s=1.05, pose="pointleft", stick=[-330, -430], mood="happy", at=0.4)]),
    L("A basket of stuff that cost 100 dollars back then costs about 808 dollars today.", "g1", [
        dict(k="circle", x=1070, y=round(pt(ch2, 2024)[1]), rx=80, ry=60, seed=9, at=1.4), dict(k="ticker", id="tk", mood="shock")],
      say="A basket of stuff that cost a hundred dollars back then, costs about eight hundred and eight dollars today."),
    L("Which means a dollar from 1970 buys about 12 cents' worth of stuff now.", "g2", [
        dict(k="bill", x=560, y=520, w=640, rot=-4), T(560, 830, "1970 dollar", 64, at=0.3),
        dict(k="arrow", x1=920, y1=520, x2=1180, y2=520, bend=-0.2, at=0.9),
        dict(k="coin", x=1300, y=470, r=46, at=1.3), dict(k="coin", x=1360, y=540, r=36, at=1.45), dict(k="coin", x=1270, y=560, r=30, at=1.6),
        T(1320, 700, "about 12¢ today", 70, color="#E0241B", at=1.8),
        dict(k="country", name="us", x=1560, y=880, w=420, mood="worried", look=[-1, 0], at=2.2, talk=False)],
      say="Which means a dollar from nineteen seventy buys about twelve cents' worth of stuff now."),
    L("Some of that is on purpose. The Federal Reserve targets about 2% inflation a year.", "g3", [
        dict(k="fed", x=700, y=900, s=1.4), dict(k="tag", x=1320, y=420, s=1.4, label="Target: 2%", rot=-6, at=1.0),
        dict(k="ticker", id="tk", x=1560, y=1010, s=0.95, pose="shrug", mood="happy")],
      say="Some of that is on purpose. The Federal Reserve targets about two percent inflation a year."),
    L("But in June 2022, prices were 9.1% higher than a year before, and the whole country felt it.", "g4", [
        dict(k="country", name="us", x=780, y=560, w=900, mood="worried", sweat=True, look=[0.6, -0.4], talk=False),
        dict(k="tag", x=1440, y=330, s=1.1, label="+9.1%", rot=8, at=0.8), dict(k="tag", x=1480, y=560, s=0.9, label="groceries ↑", rot=-6, at=1.4),
        dict(k="tag", x=1400, y=760, s=0.9, label="rent ↑", rot=5, at=1.9)],
      say="But in June twenty twenty-two, prices were nine point one percent higher than a year before, and the whole country felt it."),
    L("So in this video, we'll cover where inflation comes from, why the Fed wants some, and how to protect your money.", "g5", [
        dict(k="board", x=200, y=170, w=1100, h=640, lines=[{"t": "1. Where inflation comes from", "size": 70}, {"t": "2. Why the Fed wants some", "size": 70}, {"t": "3. How to protect your money", "size": 70}], write=5.0),
        dict(k="ticker", id="tk", x=1580, y=1000, s=1.0, pose="pointleft", stick=[-420, -420], mood="happy")]),
    L("Let's start with the basics.", "g6", [
        dict(k="text", x=960, y=430, text="Chapter 1", size=70, font="hand", color="#E0241B"),
        dict(k="text", x=960, y=560, text="Where inflation comes from", size=110, font="serif", weight=700, at=0.3),
        dict(k="under", x1=420, x2=1500, y=600, at=0.9)]),
]}

# ======================= B1: Acorn Economics (vertical short) =======================
BAL = [0, 1239, 2568, 3993, 5521, 7159, 8916, 10800, 12820, 14986, 17308, 19799, 22469, 25333, 28404, 31696, 35227, 39013, 43072, 47425, 52093, 57098, 62465, 68219, 74390, 81007, 88102, 95711, 103869, 112617, 121997]
chB = dict(k="chart", x=150, y=620, w=680, h=520, data=[[i, v] for i, v in enumerate(BAL)], numeric=True, max=135000, color="#2E9A45",
           title="$100 a month at 7% a year", titleSize=46, xl=[[0, "year 0"], [15, "15"], [30, "30"]], yl=[[36000, "$36k"], [120000, "$120k"]], end="$122,000", endDx=-30, endDy=20, endSize=60, draw=3.0)
B1 = {"id": "B1-acorn-economics-investing", "format": "vertical", "music": "bouncy", "pitch": 1.1, "header": "Investing, explained\nwith acorns", "lines": [
    L("Squirrel has ten acorns. Squirrel could eat all ten acorns today.", "g1", [
        dict(k="acorns", x=300, y=1230, w=360, h=160, n=10, seed=3, app="slide"),
        dict(k="nutty", id="n", x=720, y=1320, s=1.2, drool=True, who="nutty")], who="nutty"),
    L("Or. Squirrel plants one.", "g2", [
        dict(k="nutty", id="n", x=300, y=1320, s=1.05, pose="hold", item="acorn", who="nutty"),
        dict(k="sprout", x=760, y=1250, s=0.6, at=0.9)], who="nutty"),
    L("Nothing happens. One year later, still nothing.", "g2", [
        T(540, 620, "1 year later...", 80, font="marker", at=0.9), dict(k="nutty", id="n", pose="idle", item=None, tap=True, mood="worried")], who="nutty"),
    L("Thirty years later, squirrel has a whole oak tree, dropping acorns every single year. That's investing.", "g3", [
        T(540, 600, "30 years later", 80, font="marker"),
        dict(k="tree", x=660, y=1260, s=1.35, grow=True, growDur=2.0, acorns=[[-120, -300], [60, -350], [140, -260], [-40, -220]], app="none"),
        dict(k="acorns", x=660, y=1265, w=420, h=40, n=9, seed=8, at=2.0, app="fade"),
        dict(k="nutty", id="n", x=230, y=1330, s=0.8, shades=True, who="nutty", at=1.2)], who="nutty"),
    L("With money, same idea. 100 dollars a month at 7% a year can grow to about 122,000 dollars in thirty years.", "g4", [
        chB, T(560, 1235, "7% is an example, not a promise", 40, color="#666", at=2.5),
        dict(k="nutty", id="n", x=960, y=1340, s=0.5, pose="point", who="nutty", at=0.4)], who="nutty",
      say="With money, same idea. A hundred dollars a month at seven percent a year can grow to about a hundred and twenty-two thousand dollars in thirty years."),
    L("And squirrel doesn't bet on one tree. Squirrel buys a tiny piece of the whole forest. That's an index fund.", "g5", [
        dict(k="basket", x=500, y=1230, w=640, label="INDEX FUND", at=0.9),
        dict(k="tree", x=300, y=1010, s=0.42), dict(k="tree", x=500, y=990, s=0.48, at=0.15), dict(k="tree", x=700, y=1010, s=0.42, at=0.3),
        dict(k="nutty", id="n", x=920, y=1330, s=0.62, pose="up", who="nutty")], who="nutty"),
    L("One tree burns down? The forest keeps growing. Usually.", "g5", [
        dict(k="fire", x=300, y=960, s=0.9, at=0.2), dict(k="nutty", id="n", pose="shrug"),
        T(540, 1330, "investing can lose money", 42, color="#666", at=1.6)], who="nutty"),
    L("Squirrel explained investing. Squirrel would like one follow.", "end", [
        dict(k="logo", x=540, y=620, s=1.0), dict(k="nutty", id="n", x=540, y=1330, s=1.05, pose="up", who="nutty", at=0.2),
        dict(k="acorn", x=300, y=1150, s=1.0, at=0.6), dict(k="acorn", x=800, y=1160, s=1.0, at=0.7)], who="nutty"),
]}

# ======================= C1: Country characters (vertical short) =======================
C1 = {"id": "C1-countries-tariffs", "format": "vertical", "music": "lofi", "header": "Who actually pays\na tariff?", "lines": [
    L("Say America puts a 25% tariff on a 100-dollar gadget from China.", "g1", [
        dict(k="country", id="us", name="us", x=320, y=820, w=520, look=[1, 0], talk=False),
        dict(k="country", id="cn", name="china", x=820, y=830, w=400, color="#E4572E", look=[-1, 0], talk=False, at=0.3),
        dict(k="box", x=790, y=1180, w=190, label="$100", at=0.9, move=[-460, 0], moveAt=1.3, moveDur=1.6),
        dict(k="tag", x=560, y=560, s=1.0, label="+25% tariff", at=2.6)],
      say="Say America puts a twenty-five percent tariff on a hundred-dollar gadget from China."),
    L("So who pays the 25 dollars? Not China.", "g1", [
        dict(k="bubble", x=820, y=540, w=300, h=150, text="not me!", size=56, tail=[800, 650], at=0.8),
        dict(k="country", id="us", mood="worried")], say="So who pays the twenty-five dollars? Not China."),
    L("The American company bringing it in pays U.S. Customs.", "g2", [
        dict(k="store", x=300, y=1240, s=0.9, label="U.S. IMPORTER"), dict(k="booth", x=820, y=1240, s=0.95, label="U.S. CUSTOMS", at=0.3),
        dict(k="bag", x=330, y=720, s=0.9, label="$25", at=0.8, move=[480, 0], moveAt=1.2, moveDur=1.4),
        dict(k="arrow", x1=380, y1=560, x2=760, y2=560, bend=-0.2, at=1.6)]),
    L("Then it can eat that cost, or raise the price on you.", "g3", [
        dict(k="tag", x=330, y=780, s=1.3, label="$100", rot=-8), dict(k="cross", x=330, y=780, w=260, h=150, at=1.0),
        dict(k="tag", x=380, y=1060, s=1.3, label="$125", rot=6, at=1.4),
        dict(k="ticker", id="tk", x=850, y=1330, s=0.85, pose="shrug", mood="worried", sweat=True)]),
    L("Studies of the 2018 and 2019 tariffs found most of the cost landed on American buyers.", "g4", [
        dict(k="paper", x=470, y=800, w=720, head="Most tariff costs\nlanded on U.S. buyers", sub="studies of the 2018-19 tariffs"),
        dict(k="country", id="us2", name="us", x=830, y=1250, w=340, mood="worried", sweat=True, look=[-0.5, -0.8], at=0.8, talk=False)],
      say="Studies of the twenty eighteen and twenty nineteen tariffs found most of the cost landed on American buyers."),
    L("That's the money. Follow for more.", "end", [
        dict(k="logo", x=540, y=640, s=1.0), dict(k="country", name="us", x=320, y=1150, w=380, look=[0.5, 0], talk=False, at=0.3),
        dict(k="country", name="china", x=780, y=1150, w=300, color="#E4572E", look=[-0.5, 0], talk=False, at=0.4)]),
]}

# ======================= D1: Scam alert (Paper Ticker) =======================
D1 = {"id": "D1-scam-alert-gift-cards", "format": "vertical", "music": "lofi", "header": "The payment only\nscammers ask for", "lines": [
    L("If anyone asks you to pay with a gift card, stop. It's a scam.", "g1", [
        dict(k="rect", x=120, y=640, w=480, h=300, fill="#FFD23F"), dict(k="text", x=360, y=770, text="GIFT CARD", size=70, font="marker"),
        dict(k="text", x=360, y=860, text="$500", size=64, font="serif", weight=700),
        dict(k="cross", x=360, y=790, w=420, h=260, at=2.0),
        dict(k="ticker", id="tk", x=850, y=1340, s=0.95, pose="pointleft", mood="shock", at=0.3)]),
    L("The Federal Trade Commission says it plainly. Anyone who demands payment by gift card is a scammer.", "g2", [
        dict(k="board", x=80, y=560, w=700, h=420, lines=[{"t": "Demands a gift card?", "size": 70}, {"t": "= SCAMMER", "size": 110}], write=3.2),
        dict(k="ticker", id="tk", x=880, y=1340, s=0.95, pose="pointleft", stick=[-300, -470], mood="angry")]),
    L("Watch for three red flags. One: pressure to pay right now.", "g3", [
        dict(k="text", x=110, y=600, text="3 red flags", size=90, font="serif", weight=700, anchor="start"),
        dict(k="text", x=110, y=760, text="1. \"Pay NOW or else!\"", size=64, anchor="start", color="#E0241B", at=2.2),
        dict(k="ticker", id="tk", x=880, y=1340, s=0.85, pose="think", mood="worried")]),
    L("Two: a strange way to pay, like gift cards, wire transfers or crypto.", "g3", [
        dict(k="text", x=110, y=890, text="2. Gift cards, wires, crypto", size=64, anchor="start", color="#E0241B", at=0.4)]),
    L("Three: being told to keep it secret.", "g3", [
        dict(k="text", x=110, y=1020, text="3. \"Don't tell anyone\"", size=64, anchor="start", color="#E0241B", at=0.3), dict(k="ticker", id="tk", mood="shock")]),
    L("So hang up, call back using a number you look up yourself, and report it at report fraud dot f t c dot gov.", "g4", [
        dict(k="bubble", x=360, y=690, w=440, h=200, text="*click*", size=72),
        dict(k="text", x=400, y=1000, text="Report it:", size=64, at=2.2), dict(k="text", x=400, y=1090, text="ReportFraud.ftc.gov", size=58, font="serif", weight=700, at=2.6),
        dict(k="under", x1=110, x2=690, y=1112, at=3.2),
        dict(k="ticker", id="tk", x=900, y=1340, s=0.8, pose="hips", mood="happy")]),
    L("Share this with someone who needs it.", "end", [
        dict(k="logo", x=540, y=620, s=1.0), T(540, 720, "money news + money basics, drawn simply", 44, at=0.4),
        dict(k="ticker", id="tk", x=540, y=1340, s=1.05, pose="wave", mood="up", at=0.2)]),
]}

# ======================= E1: Myth, checking your score =======================
E1 = {"id": "E1-myth-checking-score", "format": "vertical", "music": "lofi", "header": "Does checking your credit\nscore hurt it?", "lines": [
    L("Myth: checking your own credit score lowers it.", "g1", [
        dict(k="rect", x=160, y=620, w=520, h=330, fill="#fff"), T(420, 700, "your credit score", 48),
        dict(k="text", x=420, y=880, text="742", size=170, font="serif", weight=700, color="#2E9A45"),
        dict(k="text", x=460, y=1110, text="MYTH", size=120, font="marker", color="#E0241B", rot=-8, at=1.0),
        dict(k="ticker", id="tk", x=880, y=1340, s=0.9, pose="pointleft", mood="worried")]),
    L("Fact: checking your own score is a soft inquiry. It has zero effect.", "g1", [
        dict(k="cross", x=460, y=1080, w=360, h=150, at=0.3), dict(k="text", x=440, y=1250, text="soft check = no effect", size=62, color="#2E9A45", at=1.0),
        dict(k="ticker", id="tk", mood="up")]),
    L("What can dip it a little is a hard inquiry. That's when you apply for a new card or a loan.", "g2", [
        dict(k="rect", x=90, y=600, w=420, h=560, fill="#EAF6EC"), T(300, 690, "You check", 60), T(300, 760, "your own score", 48),
        dict(k="text", x=300, y=980, text="0", size=200, font="serif", weight=700, color="#2E9A45"), T(300, 1100, "no effect", 52),
        dict(k="rect", x=570, y=600, w=420, h=560, fill="#FDECEA", at=1.4), dict(k="text", x=780, y=690, text="You apply", size=60, at=1.5), dict(k="text", x=780, y=760, text="for new credit", size=48, at=1.5),
        dict(k="arrow", x1=780, y1=840, x2=780, y2=1010, bend=0.1, at=2.0), dict(k="text", x=780, y=1100, text="small dip", size=52, color="#E0241B", at=2.4)]),
    L("And you can see your credit reports from all three bureaus, free, every week, at annual credit report dot com.", "g3", [
        dict(k="board", x=80, y=560, w=700, h=420, lines=[{"t": "Free reports,", "size": 80}, {"t": "every week", "size": 80}, {"t": "AnnualCreditReport.com", "size": 58}], write=4.0),
        dict(k="ticker", id="tk", x=880, y=1340, s=0.95, pose="pointleft", stick=[-300, -470], mood="happy")]),
    L("Check often. Catching a mistake early is how you protect your score.", "g4", [
        dict(k="text", x=540, y=760, text="Check often.", size=110, font="serif", weight=700), dict(k="under", x1=220, x2=860, y=800, at=0.8),
        dict(k="ticker", id="tk", x=540, y=1340, s=1.05, pose="cheer", mood="up")]),
    L("That's the money. Follow for more.", "end", [
        dict(k="logo", x=540, y=620, s=1.0), T(540, 720, "money news + money basics, drawn simply", 44, at=0.4),
        dict(k="ticker", id="tk", x=540, y=1340, s=1.05, pose="wave", mood="up", at=0.2)]),
]}

# ======================= F1: APR =======================
bal, b = [], 1000.0
for m in range(83):
    bal.append([m, round(max(b, 0))]); b = b * 1.02 - 25
chF = dict(k="chart", x=150, y=620, w=640, h=520, data=bal, numeric=True, max=1100, title="$1,000 at 24% APR, paying $25 a month", titleSize=38,
           xl=[[0, "month 0"], [40, "40"], [82, "82"]], yl=[[1000, "$1,000"], [500, "$500"]], end="82 months", endDx=-70, endDy=-150, endSize=56, draw=3.0, dot=True)
F1 = {"id": "F1-apr-explained", "format": "vertical", "music": "lofi", "header": "APR: the 3 letters that\ncan double your debt", "lines": [
    L("Three letters on your credit card can almost double what you owe. A, P, R.", "g1", [
        dict(k="card", x=400, y=820, w=560, rot=-6, label="APR 24%"),
        dict(k="circle", x=460, y=720, rx=190, ry=80, seed=5, at=2.2),
        dict(k="ticker", id="tk", x=880, y=1340, s=0.9, pose="pointleft", mood="shock", at=0.3)],
      say="Three letters on your credit card can almost double what you owe. A. P. R."),
    L("APR is the yearly price of borrowing. 24% a year works out to about 2% every month.", "g2", [
        dict(k="board", x=80, y=560, w=700, h=420, lines=[{"t": "APR = yearly price", "size": 72}, {"t": "of borrowing", "size": 72}, {"t": "24%/yr ≈ 2%/month", "size": 72}], write=4.0),
        dict(k="ticker", id="tk", x=880, y=1340, s=0.95, pose="pointleft", stick=[-300, -470], mood="happy")],
      say="A P R is the yearly price of borrowing. Twenty-four percent a year works out to about two percent every month."),
    L("Owe a thousand dollars, and that's about 20 dollars of interest in one month.", "g3", [
        dict(k="bill", x=330, y=760, w=460, rot=-5, label="$1,000"), dict(k="arrow", x1=330, y1=920, x2=330, y2=1060, bend=0.1, at=1.0),
        dict(k="text", x=330, y=1170, text="≈ $20 a month", size=80, font="marker", color="#E0241B", at=1.5),
        dict(k="ticker", id="tk", x=860, y=1340, s=0.9, pose="shrug", mood="worried")],
      say="Owe a thousand dollars, and that's about twenty dollars of interest in one month."),
    L("Pay only 25 dollars a month, and it takes 82 months to clear. Almost seven years.", "g4", [
        chF, dict(k="ticker", id="tk", x=950, y=1340, s=0.7, pose="pointleft", mood="shock", at=0.5)],
      say="Pay only twenty-five dollars a month, and it takes eighty-two months to clear. Almost seven years."),
    L("You'd pay about 2,032 dollars in total. Over a thousand of that is interest.", "g5", [
        dict(k="bag", x=300, y=1000, s=1.1, label="$1,000"), T(300, 1140, "what you borrowed", 46),
        dict(k="bag", x=720, y=1000, s=1.35, label="$1,032", at=0.9), dict(k="text", x=720, y=1170, text="interest", size=56, color="#E0241B", at=1.1),
        dict(k="text", x=510, y=680, text="Total paid: $2,032", size=80, font="serif", weight=700, at=1.8)],
      say="You'd pay about two thousand and thirty-two dollars in total. Over a thousand of that is interest."),
    L("The fix: pay your full statement balance on time, and most cards charge no interest on purchases.", "g6", [
        dict(k="text", x=540, y=620, text="Pay in full,", size=96, font="serif", weight=700), dict(k="text", x=540, y=735, text="on time.", size=96, font="serif", weight=700, at=0.5),
        dict(k="text", x=540, y=840, text="no interest on purchases*", size=54, color="#2E9A45", at=2.0), T(540, 900, "*on most cards", 36, color="#666", at=2.2),
        dict(k="ticker", id="tk", x=540, y=1350, s=0.8, pose="cheer", mood="up")]),
    L("That's the money. Follow for more.", "end", [
        dict(k="logo", x=540, y=620, s=1.0), T(540, 720, "money news + money basics, drawn simply", 44, at=0.4),
        dict(k="ticker", id="tk", x=540, y=1340, s=1.05, pose="wave", mood="up", at=0.2)]),
]}

# ======================= G1: Avalanche vs snowball =======================
MT = "M-230,0 L-60,-300 L0,-210 L90,-380 L260,0 Z"
G1 = {"id": "G1-avalanche-vs-snowball", "format": "vertical", "music": "lofi", "header": "Avalanche vs snowball:\nwhich kills debt faster?", "lines": [
    L("Two ways to crush debt. The avalanche, and the snowball.", "g1", [
        dict(k="path", x=300, y=1000, d="M70,1000 L240,700 L300,790 L390,620 L560,1000 Z", fill="#E8EEF6"),
        dict(k="path", x=300, y=700, d="M390,620 L340,720 L380,700 L420,740 L445,690 Z", fill="#fff"),
        T(310, 1090, "avalanche", 64),
        dict(k="circle", x=780, y=880, rx=130, ry=125, seed=2, color="#111", sw=7, at=0.9),
        dict(k="text", x=780, y=1090, text="snowball", size=64, at=1.1)]),
    L("Both start the same. Pay the minimum on every debt, then throw every extra dollar at one of them.", "g2", [
        dict(k="text", x=110, y=600, text="Your debts", size=80, font="serif", weight=700, anchor="start"),
        dict(k="row", x=110, y=660, w=820, a="Credit card: $2,000", b="24%", bc="#E0241B", at=0.3),
        dict(k="row", x=110, y=800, w=820, a="Store card: $500", b="18%", at=0.5),
        dict(k="row", x=110, y=940, w=820, a="Car loan: $6,000", b="7%", at=0.7),
        T(520, 1150, "(example numbers)", 40, color="#666", at=1.0)]),
    L("The avalanche goes after the highest interest rate first. It saves the most money.", "g2", [
        dict(k="circle", x=860, y=715, rx=80, ry=55, seed=3, at=0.3), dict(k="text", x=800, y=620, text="avalanche", size=52, color="#E0241B", at=0.8)]),
    L("The snowball goes after the smallest balance first. Quick wins keep you going.", "g2", [
        dict(k="circle", x=420, y=855, rx=90, ry=55, seed=4, color="#2E9A45", at=0.3), dict(k="text", x=420, y=1240, text="snowball: quick win", size=56, color="#2E9A45", at=0.8)]),
    L("The best one is the one you'll stick with. Both beat paying only the minimums.", "g3", [
        dict(k="text", x=540, y=640, text="Pick one.", size=110, font="serif", weight=700), dict(k="text", x=540, y=760, text="Stick with it.", size=96, font="serif", weight=700, at=0.6),
        dict(k="under", x1=250, x2=830, y=790, at=1.2),
        dict(k="ticker", id="tk", x=540, y=1350, s=0.8, pose="cheer", mood="up")]),
    L("That's the money. Follow for more.", "end", [
        dict(k="logo", x=540, y=620, s=1.0), T(540, 720, "money news + money basics, drawn simply", 44, at=0.4),
        dict(k="ticker", id="tk", x=540, y=1340, s=1.05, pose="wave", mood="up", at=0.2)]),
]}

for ep in (A1, A2, B1, C1, D1, E1, F1, G1):
    json.dump(ep, open(os.path.join(OUT, ep["id"] + ".json"), "w"), indent=1, ensure_ascii=False)
    print(ep["id"], len(ep["lines"]))
