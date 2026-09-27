"""Scene templates -> positioned doodle items.

Scripts (hand-written or from Claude) describe each line's picture with a small set of templates instead of
coordinates. This module lays them out for 9:16 shorts (1080x1920, inside the platform safe zone) and
16:9 long-form (1920x1080), so every automated episode is drawn cleanly with no manual placement.

Line format:  {"who": "ticker"|"nutty", "text": "...", "say": "...", "scene": {"t": "<template>", ...fields}}
A line with "keep": true continues the previous line's picture (reveals the next list item, adds a chart note, ...).
"""
import re

RED, GREEN = "#E0241B", "#2E9A45"
COUNTRY_COLOR = {"us": "#3E9B4F", "china": "#E4572E", "japan": "#F07C7C", "uk": "#3B5BA5", "germany": "#E8C547",
                 "mexico": "#F2A541", "canada": "#C94C4C"}
PROPS = ("bill", "card", "house", "car", "bag", "coins", "fed", "store", "customs", "chart-up", "chart-down", "fire", "acorns",
         "box", "tag", "mattress", "pot", "paper", "none")
TEMPLATES = ("hook", "board", "chart", "compare", "list", "stat", "money", "countries", "building", "news", "quote",
             "timeline", "split", "squirrel", "chapter", "cta")


def plain(s): return re.sub(r"[\[\]]", "", str(s))


def wrap(text, max_w, size, k=0.5):
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if len(plain(t)) * size * k > max_w and cur: lines.append(cur); cur = w
        else: cur = t
    if cur: lines.append(cur)
    # keep [highlight] spans from breaking across lines
    out, open_ = [], False
    for ln in lines:
        if open_: ln = "[" + ln
        open_ = ln.count("[") > ln.count("]")
        out.append(ln + ("]" if open_ else ""))
    return out


def fit(text, max_w, max_lines, size, min_size=40, k=0.5):
    while size > min_size:
        ls = wrap(text, max_w, size, k)
        if len(ls) <= max_lines: return ls, size
        size -= 4
    return wrap(text, max_w, size, k), size


def T(x, y, t, size, **k): return dict(k="text", x=round(x), y=round(y), text=t, size=size, **k)


class Frame:
    """Geometry for one format. Coordinates for vertical are in the drawing space the player maps into the safe zone."""
    def __init__(self, fmt, host):
        self.v = fmt != "landscape"; self.host = host
        if self.v:
            self.W, self.H = 1080, 1920
            self.box = (90, 520, 760, 1250) if host else (90, 520, 990, 1300)
            self.hostpos = dict(x=880, y=1340, s=0.9) if host == "ticker" else dict(x=875, y=1345, s=0.6)
        else:
            self.W, self.H = 1920, 1080
            self.box = (120, 130, 1320, 960) if host else (120, 130, 1800, 960)
            self.hostpos = dict(x=1600, y=1000, s=1.05) if host == "ticker" else dict(x=1600, y=1005, s=0.78)

    @property
    def cx(self): return (self.box[0] + self.box[2]) / 2
    @property
    def w(self): return self.box[2] - self.box[0]
    @property
    def h(self): return self.box[3] - self.box[1]

    def host_item(self, mood="happy", pose="idle", **k):
        if not self.host: return []
        d = dict(k=self.host, id="host", mood=mood, pose=pose, **self.hostpos, **k)
        if self.host == "nutty": d["who"] = "nutty"
        return [d]

    def title(self, text, y=None, size=None, max_lines=3, k=0.52, **kw):
        size = size or (96 if self.v else 96)
        ls, sz = fit(text, self.w, max_lines, size, 44, k)
        y = y if y is not None else self.box[1] + sz
        return [T(self.cx, y + i * sz * 1.12, ln, sz, font="serif", weight=700, **kw) for i, ln in enumerate(ls)], y + len(ls) * sz * 1.12


def prop_items(kind, x, y, scale=1.0, label=None, value=None):
    s = scale
    if kind == "bill": return [dict(k="bill", x=x, y=y, w=round(520 * s), rot=-5, label=label or "$1")]
    if kind == "card": return [dict(k="card", x=x, y=y, w=round(520 * s), rot=-6, label=label)]
    if kind == "house": return [dict(k="house", x=x, y=y + round(170 * s), s=s * 1.1, label=label)]
    if kind == "car": return [dict(k="car", x=x, y=y + round(100 * s), s=s * 1.2)]
    if kind == "bag": return [dict(k="bag", x=x, y=y + round(40 * s), s=s * 1.4, label=label or "$")]
    if kind == "coins": return [dict(k="coin", x=x - 70 * s, y=y + 20, r=round(55 * s)), dict(k="coin", x=x + 40 * s, y=y - 40, r=round(48 * s), at=0.15), dict(k="coin", x=x + 60 * s, y=y + 60, r=round(40 * s), at=0.3)]
    if kind == "fed": return [dict(k="fed", x=x, y=y + round(170 * s), s=s * 1.05)] + ([dict(k="tag", x=x, y=y - round(260 * s), s=s, label=label, rot=-6, at=0.8)] if label else [])
    if kind == "store": return [dict(k="store", x=x, y=y + round(170 * s), s=s * 0.95, label=label or "STORE")]
    if kind == "customs": return [dict(k="booth", x=x, y=y + round(170 * s), s=s, label=label or "U.S. CUSTOMS")]
    if kind in ("chart-up", "chart-down"):
        up = kind == "chart-up"; w, h = 460 * s, 300 * s; x0, y0 = x - w / 2, y - h / 2
        pts = [(0, .8), (.2, .7), (.35, .75), (.5, .5), (.65, .55), (.8, .3), (1, .1)] if up else [(0, .15), (.2, .25), (.35, .2), (.5, .45), (.65, .4), (.8, .7), (1, .9)]
        d = "M" + " L".join(f"{x0 + a * w:.0f},{y0 + b * h:.0f}" for a, b in pts)
        return [dict(k="path", x=x, y=y, d=f"M{x0:.0f},{y0:.0f} L{x0:.0f},{y0 + h:.0f} L{x0 + w:.0f},{y0 + h:.0f}"),
                dict(k="arrow", x1=round(x0), y1=round(y0 + pts[0][1] * h), x2=round(x0 + w), y2=round(y0 + pts[-1][1] * h), bend=0.05, color=GREEN if up else RED, at=0.2)]
    if kind == "fire": return [dict(k="fire", x=x, y=y + round(120 * s), s=s * 1.3)]
    if kind == "acorns": return [dict(k="acorns", x=x, y=y + round(80 * s), w=round(380 * s), h=round(150 * s), n=10, seed=3)]
    if kind == "box": return [dict(k="box", x=x, y=y, w=round(260 * s), label=label)]
    if kind == "tag": return [dict(k="tag", x=x, y=y, s=s * 1.2, label=label or "$", rot=-6)]
    if kind == "mattress": return [dict(k="mattress", x=x, y=y + round(60 * s), s=s), dict(k="bill", x=x, y=y - round(60 * s), w=round(300 * s), rot=8, at=0.2)]
    if kind == "pot": return [dict(k="pot", x=x, y=y + round(130 * s), s=s * 1.2)]
    if kind == "paper": return [dict(k="paper", x=x, y=y, w=round(600 * s), head=label or "BREAKING", sub=None)]
    return []


def chart_items(F, sc, top):
    pts = sc["points"]; n = len(pts)
    x0 = F.box[0] + (110 if F.v else 150); w = F.box[2] - x0 - (150 if F.v else 220)
    y0 = top + 60; h = F.box[3] - y0 - (100 if F.v else 90)
    vals = [p[1] for p in pts]; lo = min(0, min(vals)); hi = max(vals); mx = hi + (hi - lo) * 0.15; mn = lo
    pre, suf = sc.get("prefix", ""), sc.get("suffix", "")
    def fmt(v):
        a = abs(v); s = f"{a / 1e12:.1f}T" if a >= 1e12 else f"{a / 1e9:.1f}B" if a >= 1e9 else f"{a / 1e6:.1f}M" if a >= 1e6 else f"{a / 1e3:.0f}k" if a >= 1e4 else (f"{a:,.0f}" if a >= 100 else f"{a:g}")
        return ("-" if v < 0 else "") + pre + s + suf
    xs = [p[0] for p in pts]; numeric = all(isinstance(v, (int, float)) for v in xs)
    data = [[(xv if numeric else i), yv] for i, (xv, yv) in enumerate(pts)]
    xl = [[data[0][0], str(xs[0])], [data[n // 2][0], str(xs[n // 2])], [data[-1][0], str(xs[-1])]] if n > 2 else [[data[0][0], str(xs[0])], [data[-1][0], str(xs[-1])]]
    import math
    span = (mx - mn) / 3 or 1; mag = 10 ** math.floor(math.log10(span)); step = next(m * mag for m in (1, 2, 2.5, 5, 10) if m * mag >= span)
    ticks = [k * step for k in range(math.ceil(mn / step), math.floor(mx / step) + 1) if k * step != 0 or mn < 0][:4]
    trend = sc.get("color") or ("up" if vals[-1] >= vals[0] else "down")
    item = dict(k="chart", id="chart", x=round(x0), y=round(y0), w=round(w), h=round(h), data=data, numeric=True, max=mx, min=mn,
                title=None, xl=xl, yl=[[t, fmt(t)] for t in ticks], lsize=34 if F.v else 32,
                color=GREEN if trend == "up" else RED, end=sc.get("end") or fmt(vals[-1]), endDx=-10, endDy=-44, endSize=56, draw=2.6)
    def pos(xv):
        i = xs.index(xv) if xv in xs else min(range(n), key=lambda j: abs((xs[j] if numeric else j) - (xv if numeric else 0)))
        dx = (data[i][0] - data[0][0]) / ((data[-1][0] - data[0][0]) or 1)
        return x0 + dx * w, y0 + h - (data[i][1] - mn) / (mx - mn) * h
    return item, pos


def countries_items(F, cast, prop=None):
    n = len(cast); out = []
    if F.v:
        P = {1: [(540, 850, 660)], 2: [(330, 800, 470), (800, 820, 380)], 3: [(300, 760, 420), (790, 760, 360), (540, 1120, 400)]}[min(n, 3)]
    else:
        P = {1: [(760, 520, 760)], 2: [(520, 520, 620), (1200, 540, 480)], 3: [(420, 460, 520), (1000, 460, 440), (700, 820, 420)]}[min(n, 3)]
    for i, c in enumerate(cast[:3]):
        x, y, w = P[i]; nm = c.get("name", "us")
        w = w * (0.8 if nm in ("uk", "germany") else 1)
        look = [1, 0] if (n > 1 and i == 0) else ([-1, 0] if n > 1 else [0, 0.3])
        out.append(dict(k="country", id="c_" + nm, name=nm, x=x, y=y, w=round(w), color=COUNTRY_COLOR.get(nm, "#3E9B4F"), mood=c.get("mood", "happy"),
                        look=look, talk=False, sweat=c.get("mood") == "worried", at=0.25 * i))
        if c.get("says"):
            bw = max(260, len(c["says"]) * 26 + 60)
            out.append(dict(k="bubble", id="b_" + nm, x=x, y=y - w * 0.55, w=bw, h=140, text=c["says"], size=48, tail=[x - 10, y - w * 0.3], at=0.9 + 0.25 * i))
    if prop:
        px, py = (540, 1230) if F.v else (860, 900)
        if n == 1: px, py = (540, 1250) if F.v else (1450, 700)
        out += [dict(i, at=1.2) for i in prop_items(prop.get("kind", "box"), px, py, 0.7, prop.get("label"))]
    return out


def layout_line(F, sc, st, step):
    """Items for one line. st carries the running state of a multi-line (keep) scene."""
    t = sc.get("t", "hook"); items = []; mood = sc.get("mood")
    top = F.box[1]
    if t == "hook":
        ti, yb = F.title(sc.get("title", ""), size=sc.get("size"))
        items += ti
        cy = (yb + F.box[3]) / 2 + 20
        items += [dict(i, at=0.4) for i in prop_items(sc.get("prop", "none"), F.cx, cy, 1.25 if F.v else 1.3, sc.get("label"))]
        if sc.get("value"): items.append(dict(k="text", x=F.cx, y=min(F.box[3], cy + 330), text=sc["value"], size=130 if F.v else 150, font="marker", color=RED, at=1.4))
        items += F.host_item(mood or "shock", "pointleft")
    elif t == "board":
        bx, by = F.box[0] - 10, top + 40; bw = F.w + 10 - (0 if F.host else 0); bh = 440 if F.v else 560
        lines = sc.get("lines", [])[:3]
        L = [{"t": ln, "size": fit(ln, bw - 60, 1, 88 if F.v else 92, 46, 0.46)[1]} for ln in lines]
        items.append(dict(k="board", id="board", x=bx, y=by, w=bw, h=bh, lines=L, write=max(1.5, 1.2 * len(L))))
        items += F.host_item(mood or "happy", "pointleft", stick=[-300, -470] if F.v else [-380, -430])
        st["board_y"] = by + bh
    elif t == "chart":
        ti, yb = F.title(sc.get("title", ""), size=56 if F.v else 60, max_lines=2)
        items += ti
        ch, pos = chart_items(F, sc, yb - 20); items.append(ch); st["pos"] = pos
        items += F.host_item(mood or "happy", "pointleft")
    elif t == "compare":
        ti, yb = F.title(sc.get("title", ""), size=64 if F.v else 70, max_lines=2); items += ti
        L, R = sc.get("left", {}), sc.get("right", {})
        col = lambda tone: GREEN if tone == "up" else RED if tone == "down" else "#111"
        xl, xr = F.box[0] + F.w * 0.25, F.box[0] + F.w * 0.75; cy = (yb + F.box[3]) / 2 + 20
        for side, d, x, a in (("l", L, xl, 0.3), ("r", R, xr, 1.2)):
            items.append(dict(k="rect", id="card_" + side, x=round(x - F.w * 0.22), y=round(cy - 230), w=round(F.w * 0.44), h=460, fill="#fff", at=a))
            ls, sz = fit(d.get("label", ""), F.w * 0.4, 2, 50, 34, 0.45)
            for i, ln in enumerate(ls): items.append(T(x, cy - 170 + i * sz * 1.1, ln, sz, at=a))
            vs = fit(d.get("value", ""), F.w * 0.4, 1, 110, 50, 0.64)[1]
            items.append(T(x, cy + 90, d.get("value", ""), vs, font="serif", weight=700, color=col(d.get("tone")), at=a + 0.2))
            if d.get("sub"): items.append(T(x, cy + 170, d["sub"], 38, color="#555", at=a + 0.3))
        items.append(dict(k="text", x=round(F.cx), y=round(cy - 250), text="vs", size=70, font="marker", color=RED, at=0.9))
        st["compare"] = (xl, xr, cy)
        items += F.host_item(mood or "think", "shrug")
    elif t == "list":
        ti, yb = F.title(sc.get("title", ""), size=70 if F.v else 76, max_lines=2); items += ti
        its = sc.get("items", [])[:5]; st["list"] = (its, yb + 30); n = sc.get("reveal", 1)
        items += _list_rows(F, its, yb + 30, 0, n); st["shown"] = n
        items += F.host_item(mood or "think", "think")
    elif t == "stat":
        cy = (top + F.box[3]) / 2
        if sc.get("label"):
            ls, sz = fit(sc["label"], F.w, 2, 76, 40, 0.48)
            for i, ln in enumerate(ls): items.append(T(F.cx, top + 90 + i * sz * 1.15, ln, sz))
        vsz = fit(sc.get("value", ""), F.w, 1, 230 if F.v else 250, 90, 0.58)[1]
        items.append(dict(k="text", x=round(F.cx), y=round(cy + vsz * 0.3), text=sc.get("value", ""), size=vsz, font="serif", weight=700,
                          color=GREEN if sc.get("tone") == "up" else RED if sc.get("tone") == "down" else "#111", at=0.3))
        items.append(dict(k="circle", x=round(F.cx), y=round(cy), rx=round(min(F.w * 0.48, len(sc.get("value", "")) * vsz * 0.33 + 40)), ry=round(vsz * 0.7), seed=6, at=1.1))
        if sc.get("sub"): items.append(T(F.cx, cy + vsz * 0.95, sc["sub"], 46 if F.v else 50, color="#555", at=1.4))
        items += F.host_item(mood or "shock", "pointleft")
    elif t == "money":
        a, b = sc.get("from", {}), sc.get("to", {})
        if F.v:
            items += [dict(k="bill", x=F.cx - 40, y=top + 170, w=440, rot=-5, label=a.get("value", "$1")), T(F.cx - 40, top + 370, a.get("label", ""), 50, at=0.3),
                      dict(k="arrow", x1=round(F.cx - 40), y1=top + 420, x2=round(F.cx - 40), y2=top + 560, bend=0.12, at=0.9),
                      dict(k="text", x=round(F.cx - 40), y=top + 690, text=b.get("value", ""), size=120, font="marker", color=RED, at=1.3), T(F.cx - 40, top + 770, b.get("label", ""), 50, at=1.5)]
        else:
            items += [dict(k="bill", x=440, y=460, w=560, rot=-5, label=a.get("value", "$1")), T(440, 680, a.get("label", ""), 56, at=0.3),
                      dict(k="arrow", x1=760, y1=460, x2=1000, y2=460, bend=-0.2, at=0.9),
                      dict(k="text", x=1150, y=500, text=b.get("value", ""), size=140, font="marker", color=RED, at=1.3), T(1150, 600, b.get("label", ""), 56, at=1.5)]
        items += F.host_item(mood or "shock", "pointleft")
    elif t == "countries":
        items += countries_items(F, sc.get("cast", [{"name": "us"}]), sc.get("prop"))
        if sc.get("caption"): items.append(T(F.cx if not F.v else 540, 1330 if F.v else 1010, sc["caption"], 56 if F.v else 60, color=RED, at=1.6))
    elif t == "building":
        cy = (top + F.box[3]) / 2 + 60
        items += prop_items(sc.get("kind", "fed"), F.cx, cy, 1.15 if F.v else 1.35, sc.get("label"))
        if sc.get("caption"): items.append(T(F.cx, F.box[3] + (30 if F.v else 0), sc["caption"], 52, color=RED, at=1.2))
        items += F.host_item(mood or "happy", "shrug")
    elif t == "news":
        items.append(dict(k="paper", x=round(F.cx), y=round(top + (330 if F.v else 380)), w=round(min(F.w, 760)), head="\n".join(wrap(sc.get("headline", ""), min(F.w, 760) - 80, 50, 0.5)[:3]), sub=sc.get("source")))
        items += F.host_item(mood or "shock", "pointleft")
    elif t == "quote":
        qw = F.w; ls, sz = fit('"' + sc.get("text", "") + '"', qw - 140, 5, 56, 36, 0.5)
        qh = 200 + len(ls) * sz * 1.25 + 60
        items.append(dict(k="quote", x=F.box[0], y=round(top + 40), w=qw, h=round(qh), text="\n".join(ls), size=sz, source=sc.get("source")))
        items += F.host_item(mood or "think", "think")
    elif t == "timeline":
        ev = sc.get("events", [])[:5]; st["timeline"] = ev; n = sc.get("reveal", len(ev))
        items += _timeline(F, ev, 0, n); st["tshown"] = n
        items += F.host_item(mood or "think", "pointleft")
    elif t == "split":
        ti, yb = F.title(sc.get("title", ""), size=64, max_lines=2); items += ti
        for side, key, x0, a in (("l", "left", F.box[0], 0.3), ("r", "right", F.box[0] + F.w * 0.52, 1.3)):
            d = sc.get(key, {}); cw = F.w * 0.48; tone = d.get("tone"); rows = []
            for it in d.get("items", [])[:4]:
                ls, sz = fit(it, cw - 50, 2, 58 if F.v else 56, 36, 0.46); rows.append((ls, sz))
            ch = 150 + sum(len(ls) * sz * 1.15 + 26 for ls, sz in rows) + 30
            items.append(dict(k="rect", x=round(x0), y=round(yb + 20), w=round(cw), h=round(ch), fill="#EAF6EC" if tone == "up" else "#FDECEA" if tone == "down" else "#fff", at=a))
            items.append(T(x0 + cw / 2, yb + 105, d.get("title", ""), fit(d.get("title", ""), cw - 40, 1, 64, 36, 0.52)[1], font="serif", weight=700, at=a))
            y = yb + 200
            for ls, sz in rows:
                for ln in ls: items.append(T(x0 + cw / 2, y, ln, sz, at=a + 0.2)); y += sz * 1.15
                y += 26
        items += F.host_item(mood or "think", "shrug") if not F.v else []
    elif t == "squirrel":
        items += _squirrel(F, sc)
    elif t == "chapter":
        items += [T(F.cx if not F.v else 540, (F.H * 0.38), f"Chapter {sc.get('n', 1)}", 70, color=RED),
                  dict(k="text", x=round(F.W / 2), y=round(F.H * 0.38 + 130), text=sc.get("title", ""), size=fit(sc.get("title", ""), F.W - 300, 1, 110, 60, 0.52)[1], font="serif", weight=700, at=0.3),
                  dict(k="under", x1=round(F.W * 0.25), x2=round(F.W * 0.75), y=round(F.H * 0.38 + 170), at=0.9)]
    elif t == "cta":
        y0 = 640 if F.v else 360
        items += [dict(k="logo", x=540 if F.v else 960, y=y0, s=1.0), T(540 if F.v else 960, y0 + 100, sc.get("tagline", "money news + money basics, drawn simply"), 44, at=0.4)]
        if F.host == "nutty": items.append(dict(k="nutty", id="host", x=540 if F.v else 960, y=1330 if F.v else 1000, s=1.0 if F.v else 0.9, pose="up", who="nutty", at=0.2))
        else: items.append(dict(k="ticker", id="host", x=540 if F.v else 960, y=1340 if F.v else 1010, s=1.0 if F.v else 1.0, pose="wave", mood="up", at=0.2))
    return items


def _list_rows(F, its, y0, a, b):
    out = []; rh = 165 if F.v else 140; x = F.box[0]; w = F.w
    for i in range(a, min(b, len(its))):
        ls, sz = fit(f"[{i + 1}.] {its[i]}", w - 20, 2, 68 if F.v else 70, 40, 0.46)
        for j, ln in enumerate(ls):
            out.append(dict(k="text", id=f"li{i}_{j}", x=round(x + 10), y=round(y0 + 60 + i * rh + j * sz * 1.05), text=ln, size=sz, anchor="start", at=0.3 + (i - a) * 0.3))
    return out


def _timeline(F, ev, a, b):
    out = []
    if a == 0:
        if F.v: out.append(dict(k="path", x=200, y=900, d=f"M200,{F.box[1] + 40} L200,{F.box[3] - 20}"))
        else: out.append(dict(k="path", x=900, y=560, d=f"M{F.box[0]},560 L{F.box[2]},560"))
    n = max(1, len(ev))
    for i in range(a, min(b, len(ev))):
        yr, lab = ev[i]
        if F.v:
            y = F.box[1] + 80 + i * (F.h - 120) / n
            out += [dict(k="coin", x=200, y=round(y), r=26, at=0.2), T(250, y + 18, str(yr), 56, font="serif", weight=700, anchor="start", color=RED, at=0.3)]
            for j, ln in enumerate(wrap(lab, F.w - 220, 46, 0.46)[:2]): out.append(T(250, y + 80 + j * 50, ln, 46, anchor="start", at=0.4))
        else:
            x = F.box[0] + 60 + i * (F.w - 120) / max(1, n - 1)
            out += [dict(k="coin", x=round(x), y=560, r=30, at=0.2), T(x, 490, str(yr), 76, font="serif", weight=700, color=RED, at=0.3)]
            for j, ln in enumerate(wrap(lab, (F.w - 60) / n, 52, 0.46)[:3]): out.append(T(x, 650 + j * 58, ln, 52, at=0.4))
    return out


def _squirrel(F, sc):
    kind = sc.get("kind", "pile"); out = []; v = F.v
    nx, ny, ns = (720, 1320, 1.15) if v else (1450, 1000, 1.0)
    if sc.get("caption"): out.append(dict(k="text", x=540 if v else 800, y=610 if v else 200, text=sc["caption"], size=78 if v else 90, font="marker"))
    if kind == "pile":
        out += [dict(k="acorns", x=300 if v else 600, y=1230 if v else 900, w=360, h=160, n=10, seed=3, app="slide"),
                dict(k="nutty", id="host", x=nx, y=ny, s=ns, drool=True, who="nutty")]
    elif kind == "plant":
        out += [dict(k="nutty", id="host", x=300 if v else 600, y=ny, s=1.0, pose="hold", item="acorn", who="nutty"), dict(k="sprout", x=760 if v else 1200, y=1250 if v else 900, s=0.6, at=0.9)]
    elif kind == "wait":
        out += [dict(k="nutty", id="host", x=300 if v else 600, y=ny, s=1.0, tap=True, mood="worried", who="nutty"), dict(k="sprout", x=760 if v else 1200, y=1250 if v else 900, s=0.6)]
    elif kind == "tree":
        out += [dict(k="tree", x=660 if v else 1150, y=1260 if v else 960, s=1.3 if v else 1.5, grow=True, growDur=2.0, acorns=[[-120, -300], [60, -350], [140, -260]], app="none"),
                dict(k="nutty", id="host", x=230 if v else 500, y=ny, s=0.8, shades=True, who="nutty", at=1.2)]
    elif kind in ("basket", "fire"):
        bx = 480 if v else 800; by = 1230 if v else 930
        out += [dict(k="basket", x=bx, y=by, w=620, label=sc.get("label", "INDEX FUND")), dict(k="tree", x=bx - 200, y=by - 220, s=0.42), dict(k="tree", x=bx, y=by - 240, s=0.48, at=0.15), dict(k="tree", x=bx + 200, y=by - 220, s=0.42, at=0.3),
                dict(k="nutty", id="host", x=nx + (200 if v else 0), y=ny, s=0.62 if v else 0.8, pose="up" if kind == "basket" else "shrug", who="nutty")]
        if kind == "fire": out.append(dict(k="fire", x=bx - 200, y=by - 270, s=0.9, at=0.3))
    elif kind == "think":
        out += [dict(k="nutty", id="host", x=540 if v else 960, y=ny, s=1.2 if v else 1.0, pose="shrug", who="nutty")]
        if sc.get("value"): out.append(dict(k="text", x=540 if v else 960, y=800 if v else 330, text=sc["value"], size=130, font="marker", color=RED, at=0.6))
    elif kind == "bank":
        out += prop_items("fed", 400 if v else 700, 950 if v else 560, 0.95, sc.get("label")) + [dict(k="nutty", id="host", x=nx + 60, y=ny, s=0.7, pose="point", who="nutty")]
    return out


def _step(F, sc, st, prev):
    """A 'keep' line: continue the previous picture and add what this line needs."""
    t = prev.get("t"); items = []; mood = sc.get("mood")
    if mood or sc.get("pose"): items.append({"id": "host", **({"mood": mood} if mood else {}), **({"pose": sc["pose"]} if sc.get("pose") else {})})
    if t == "list" and "list" in st:
        its, y0 = st["list"]; a = st.get("shown", 1); b = sc.get("reveal", a + 1)
        items += _list_rows(F, its, y0, a, b); st["shown"] = b
    elif t == "timeline" and "timeline" in st:
        a = st.get("tshown", 1); b = sc.get("reveal", a + 1); items += _timeline(F, st["timeline"], a, b); st["tshown"] = b
    elif t == "chart" and sc.get("note") and "pos" in st:
        x, y = st["pos"](sc["note"].get("x")); tx = x - 200 if x > F.cx else x + 60
        ty = y - 90 if y > (F.box[1] + F.box[3]) / 2 else y + 120
        items += [dict(k="circle", x=round(x), y=round(y), rx=70, ry=60, seed=4, at=0.4),
                  dict(k="text", x=round(tx), y=round(ty), text=sc["note"].get("text", ""), size=50 if F.v else 56, color=RED, at=1.0)]
    elif t == "compare" and sc.get("winner") and "compare" in st:
        xl, xr, cy = st["compare"]; x = xl if sc["winner"] == "left" else xr
        items.append(dict(k="circle", x=round(x), y=round(cy), rx=round(F.w * 0.26), ry=270, seed=8, color=GREEN, at=0.3))
    elif t == "countries" and sc.get("cast"):
        for c in sc["cast"]:
            items.append({"id": "c_" + c.get("name", "us"), **({"mood": c["mood"], "sweat": c["mood"] == "worried"} if c.get("mood") else {})})
            if c.get("says"):
                items.append(dict(k="bubble", x=540 if F.v else 960, y=620 if F.v else 200, w=max(280, len(c["says"]) * 26 + 60), h=140, text=c["says"], size=48, at=0.3))
    elif t == "stat" and sc.get("sub"):
        items.append(T(F.cx, F.box[3] - 30, sc["sub"], 48, color=RED, at=0.3))
    if sc.get("note") and t not in ("chart",):
        items.append(T(F.cx, F.box[3] - (10 if F.v else 0), sc["note"], 52 if F.v else 56, color=RED, at=0.4))
    return items


def build_episode(script):
    """script: {"id","format","series","header","lines":[{who,text,say,scene{t,...,keep}}]} -> player episode JSON."""
    fmt = script.get("format", "vertical"); host = {"acorn": "nutty"}.get(script.get("series"), "ticker")
    lines, st, prev, g = [], {}, None, 0
    for i, ln in enumerate(script["lines"]):
        sc = dict(ln.get("scene") or {"t": "hook", "title": ln["text"][:60]})
        if sc.get("t") not in TEMPLATES: sc = {"t": "hook", "title": ln["text"][:60], "prop": "none"}
        who = ln.get("who") or ("nutty" if host == "nutty" else "ticker")
        H = None if sc["t"] in ("countries", "squirrel", "chapter", "split") or (sc["t"] == "compare" and fmt != "landscape") else host
        F = Frame(fmt, H)
        if sc.get("keep") and prev is not None:
            items = _step(Frame(fmt, st.get("host")), sc, st, prev)
        else:
            g += 1; st = {"host": H}; prev = sc
            items = layout_line(F, sc, st, 0)
        d = {"who": who, "text": ln["text"], "scene": {"group": f"g{g}", "items": items}}
        if ln.get("say"): d["say"] = ln["say"]
        if sc.get("t") == "chart" and not sc.get("keep"): d["scene"]["cam"] = [1, 1.02]
        lines.append(d)
    ep = {"id": script["id"], "format": fmt, "music": script.get("music", "bouncy" if host == "nutty" else "lofi"), "lines": lines}
    if host == "nutty": ep["pitch"] = 1.1
    if fmt != "landscape": ep["header"] = script.get("header", "")
    else: ep["captions"] = False; ep["renderFps"] = 15
    return ep


def cover(script, size=(1080, 1920)):
    """9:16 cover (IG grid shows the middle 1080x1350) or 16:9 thumbnail, from the script's 'cover' block."""
    c = script.get("cover", {}); W, H = size; v = H > W; items = []
    title = c.get("title") or plain(script.get("header", "")).replace("\n", " ")
    if v:
        ls, sz = fit(title, 900, 3, 104, 60, 0.52)
        for i, ln in enumerate(ls): items.append(T(540, 540 + i * sz * 1.14, ln, sz, font="serif", weight=700))
        vy = 540 + len(ls) * sz * 1.14 + 250
        if c.get("countries"):
            ci = countries_items(Frame("vertical", None), [{"name": n, "mood": "worried" if i == 0 else "happy"} for i, n in enumerate(c["countries"][:2])])
            items += [dict(it, at=0, y=it["y"] + (vy - 820)) for it in ci if it["k"] == "country"]
        else: items += prop_items(c.get("prop", "bill"), 470, vy, 0.95, c.get("label"))
        if c.get("value"): items.append(dict(k="text", x=540, y=1420, text=c["value"], size=150, font="marker", color=RED))
        if script.get("series") == "acorn": items.append(dict(k="nutty", x=860, y=1450, s=0.6, shades=True))
        elif not c.get("countries"): items.append(dict(k="ticker", x=880, y=1450, s=0.7, pose="pointleft", mood="shock"))
    else:
        ls, sz = fit(title, 620, 3, 92, 60, 0.52)
        for i, ln in enumerate(ls): items.append(T(60, 150 + i * sz * 1.12, ln, sz, font="serif", weight=700, anchor="start"))
        if c.get("countries"):
            for i, n in enumerate(c["countries"][:2]):
                items.append(dict(k="country", name=n, x=870 + i * 250, y=300 + i * 200, w=360 - i * 60, color=COUNTRY_COLOR.get(n, "#3E9B4F"), mood="worried" if i == 0 else "happy", look=[1 - 2 * i, 0], sweat=i == 0))
        else: items += prop_items(c.get("prop", "chart-up"), 960, 330, 0.95, c.get("label"))
        if c.get("value"): items.append(dict(k="text", x=320, y=600, text=c["value"], size=140, font="marker", color=RED))
        items.append(dict(k="nutty", x=1150, y=715, s=0.5, shades=True) if script.get("series") == "acorn" else dict(k="ticker", x=1170, y=715, s=0.5, pose="pointleft", mood="shock"))
    return {"id": script["id"] + ("-cover" if v else "-thumb"), "size": [W, H], "items": items}
