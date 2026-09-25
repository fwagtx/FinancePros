/* FinancePros TV scene player. render(t) draws the exact frame for time t (seconds). */
var EP = null, TL = null, SCENES = [], FPS = 30;
var $ = function (id) { return document.getElementById(id) };
function clamp(x, a, b) { return Math.max(a, Math.min(b, x)) }
function prog(t, start, dur) { return clamp((t - start) / dur, 0, 1) }
function easeOut(p) { return 1 - Math.pow(1 - p, 3) }
function easeBack(p) { var c = 1.6; return 1 + (c + 1) * Math.pow(p - 1, 3) + c * Math.pow(p - 1, 2) }
function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;') }
// "text with [highlight]" -> html
function hlt(s) { return esc(s).replace(/\[(.+?)\]/g, '<span class="hl">$1</span>') }

/* LED text that lights up column by column (p = 0..1) */
function ledP(text, pitch, color, p, off) {
  var cols = ledCols(text), n = cols.length, lit = Math.floor(clamp(p, 0, 1) * (n + 0.999)), r = pitch * 0.38, on = '', offs = '';
  cols.forEach(function (c, x) { c.forEach(function (v, y) {
    var cx = (x + .5) * pitch, cy = (y + .5) * pitch;
    if (v && x < lit) on += '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '"/>';
    else if (off) offs += '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '"/>';
  }) });
  var w = n * pitch, h = 7 * pitch;
  return '<svg width="' + w + '" height="' + h + '" viewBox="0 0 ' + w + ' ' + h + '" style="display:block;overflow:visible">' +
    '<defs><filter id="lg' + pitch + '" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="' + pitch * 0.2 + '" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>' +
    (off ? '<g fill="#fff" opacity="' + off + '">' + offs + '</g>' : '') + '<g fill="' + color + '" filter="url(#lg' + pitch + ')">' + on + '</g></svg>';
}
function ledFit(text, maxW, maxPitch) { return Math.min(maxPitch, Math.floor(maxW / (ledCols(text).length))) }
function money(v, d) { return '$' + Number(v).toLocaleString('en-US', { minimumFractionDigits: d || 0, maximumFractionDigits: d || 0 }) }

/* ---------- scene renderers: (def, lt = seconds since scene start, step info) -> html ---------- */
var R = {};

R.title = function (d, lt) {
  // words animate in one by one; a [bracketed phrase] sits inside ONE continuous highlight box
  var words = d.headline.split(' '), html = '', group = null;
  words.forEach(function (w, i) {
    var p = easeBack(prog(lt, 0.05 + i * 0.07, 0.32)), open = w.indexOf('[') === 0, close = /\][,.!?:;]*$/.test(w);
    var txt = esc(w.replace(/[\[\]]/g, ''));
    var span = '<span style="display:inline-block;opacity:' + clamp(p * 1.4, 0, 1) + ';transform:translateY(' + (1 - p) * 40 + 'px) scale(' + (0.86 + 0.14 * p) + ')">' + txt + '</span>';
    if (open) { group = []; }
    if (group) { group.push(span); if (close) { var gp = clamp((lt - (0.05 + (i - group.length + 1) * 0.07)) / 0.25, 0, 1);
        html += '<span class="hl" style="opacity:' + gp + '">' + group.join(' ') + '</span> '; group = null } }
    else html += span + ' ';
  });
  var sp = prog(lt, 0.45, 0.4);
  return '<div class="abs" style="left:70px;top:' + (d.top || 290) + 'px;width:' + (d.width || 920) + 'px">' +
    '<div class="hd" style="font-size:' + (d.size || 112) + 'px;line-height:1.12">' + html + '</div>' +
    (d.sub ? '<div class="mono" style="margin-top:30px;font-size:32px;color:#C9D4FF;opacity:' + sp + '">' + esc(d.sub) + '</div>' : '') + '</div>';
};

R.number = function (d, lt) {
  var pitch = ledFit(d.value, 900, d.pitch || 30), p = easeOut(prog(lt, 0.15, 0.7)), np = prog(lt, 0.6, 0.35);
  var color = d.color === 'up' ? '#2BD98A' : d.color === 'down' ? '#FF4D5E' : '#FFFFFF';
  return '<div class="abs mono" style="left:74px;top:320px;font-size:32px;color:#C9D4FF;opacity:' + prog(lt, 0, .3) + '">' + esc(d.label || '') + '</div>' +
    '<div class="abs card" style="left:60px;top:380px;padding:34px 30px">' + ledP(d.value, pitch, color, p, 0.09) + '</div>' +
    (d.note ? '<div class="abs hd" style="left:70px;top:' + (430 + pitch * 7 + 40) + 'px;width:900px;font-size:60px;text-transform:none;letter-spacing:-.025em;opacity:' + np + ';transform:translateY(' + (1 - np) * 20 + 'px)">' + hlt(d.note) + '</div>' : '');
};

R.growth = function (d, lt) {
  var W = 860, H = 380, n = d.balance.length - 1, max = d.max || Math.max.apply(null, d.balance);
  var p = easeOut(prog(lt, 0.3, d.drawTime || 3.2)), k = p * n;
  function pt(arr, i) { return [(i / n) * W, H - (arr[i] / max) * H] }
  function path(arr, upto) {
    var s = '', i; for (i = 0; i <= Math.floor(upto); i++) { var q = pt(arr, i); s += (i ? 'L' : 'M') + q[0].toFixed(1) + ',' + q[1].toFixed(1) }
    var f = upto - Math.floor(upto); if (f > 0 && Math.floor(upto) < n) { var a = pt(arr, Math.floor(upto)), b = pt(arr, Math.floor(upto) + 1); s += 'L' + (a[0] + (b[0] - a[0]) * f).toFixed(1) + ',' + (a[1] + (b[1] - a[1]) * f).toFixed(1) }
    return s }
  function area(arr, upto) { var s = path(arr, upto); var xe = (upto / n) * W; return s + 'L' + xe.toFixed(1) + ',' + H + 'L0,' + H + 'Z' }
  var i0 = Math.floor(k), f = k - i0, bal = d.balance[i0] + (i0 < n ? (d.balance[i0 + 1] - d.balance[i0]) * f : 0);
  var con = d.contrib[i0] + (i0 < n ? (d.contrib[i0 + 1] - d.contrib[i0]) * f : 0);
  var end = pt(d.balance, 0); if (k > 0) { var a = pt(d.balance, i0), b = pt(d.balance, Math.min(n, i0 + 1)); end = [a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f] }
  var grid = ''; [0.25, 0.5, 0.75, 1].forEach(function (g) { grid += '<line x1="0" x2="' + W + '" y1="' + (H - g * H) + '" y2="' + (H - g * H) + '" stroke="rgba(255,255,255,.12)" stroke-width="2" stroke-dasharray="2 10" stroke-linecap="round"/>' });
  var yr = Math.floor(k * (d.years / n) + 1e-6);
  return '<div class="abs card" style="left:60px;top:300px;width:960px;height:700px;padding:34px 40px">' +
    '<div style="display:flex;justify-content:space-between;align-items:flex-start">' +
    '<div><div class="mono" style="font-size:26px;color:#C9D4FF">' + esc(d.label) + '</div>' +
    '<div class="hd" style="font-size:88px;margin-top:10px;font-variant-numeric:tabular-nums;letter-spacing:-.03em">' + money(bal) + '</div></div>' +
    '<div class="mono" style="font-size:30px;background:#fff;color:#1432E6;border-radius:999px;padding:12px 18px 10px;margin-top:4px">Year ' + yr + '</div></div>' +
    '<svg width="' + W + '" height="' + (H + 10) + '" viewBox="0 -5 ' + W + ' ' + (H + 10) + '" style="margin-top:26px;overflow:visible">' + grid +
    '<path d="' + area(d.balance, k) + '" fill="rgba(43,217,138,.22)"/>' +
    '<path d="' + area(d.contrib, k) + '" fill="rgba(157,180,255,.55)"/>' +
    '<path d="' + path(d.balance, k) + '" fill="none" stroke="#2BD98A" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>' +
    '<circle cx="' + end[0] + '" cy="' + end[1] + '" r="13" fill="#2BD98A" stroke="#fff" stroke-width="4"/></svg>' +
    '<div style="display:flex;gap:14px;margin-top:22px">' +
    '<span class="chip" style="background:rgba(157,180,255,.28);color:#fff"><i style="width:18px;height:18px;border-radius:50%;background:#9DB4FF;display:inline-block"></i>You put in ' + money(con) + '</span>' +
    '<span class="chip" style="background:rgba(43,217,138,.2);color:#fff"><i style="width:18px;height:18px;border-radius:50%;background:#2BD98A;display:inline-block"></i>Growth ' + money(Math.max(0, bal - con)) + '</span></div></div>';
};

R.split3 = function (d, lt, st) {
  var reveal = d.reveal || 0, html = '', x = 0;
  var bar = '<div style="display:flex;height:150px;border-radius:26px;overflow:hidden;background:rgba(10,15,46,.45)">';
  d.parts.forEach(function (p, i) {
    var ts = st.revealAt[i + 1]; var g = i < reveal ? easeOut(prog(lt, ts == null ? 0 : ts, 0.55)) : 0;
    bar += '<div style="width:' + (p.pct * g) + '%;background:' + p.color + ';display:flex;align-items:center;justify-content:center;overflow:hidden">' +
      '<span class="hd" style="font-size:64px;color:' + (p.ink || '#0A0F2E') + ';opacity:' + g + '">' + p.pct + '%</span></div>';
  });
  bar += '</div>';
  var rows = '';
  d.parts.forEach(function (p, i) {
    var ts = st.revealAt[i + 1]; var g = i < reveal ? easeOut(prog(lt, (ts == null ? 0 : ts) + 0.15, 0.4)) : 0;
    rows += '<div style="display:flex;align-items:center;gap:22px;opacity:' + g + ';transform:translateX(' + (1 - g) * -30 + 'px)">' +
      '<i style="width:30px;height:30px;border-radius:9px;background:' + p.color + ';flex:none"></i>' +
      '<span class="hd" style="font-size:54px;text-transform:none;letter-spacing:-.02em;flex:1">' + esc(p.name) + '</span>' +
      '<span class="hd" style="font-size:54px;font-variant-numeric:tabular-nums">' + esc(p.amt) + '</span></div>' +
      '<div style="font:600 30px/1.3 Red Hat Display;color:#C9D4FF;margin:-8px 0 8px 52px;opacity:' + g + '">' + esc(p.ex) + '</div>';
  });
  return '<div class="abs" style="left:70px;top:290px;width:900px">' +
    '<div class="mono" style="font-size:30px;color:#C9D4FF;margin-bottom:18px;opacity:' + prog(lt, 0, .3) + '">' + esc(d.label) + '</div>' + bar +
    '<div style="display:grid;gap:22px;margin-top:40px">' + rows + '</div></div>';
};

R.list = function (d, lt, st) {
  var reveal = d.reveal == null ? d.items.length : d.reveal, html = '';
  d.items.forEach(function (it, i) {
    var ts = st.revealAt[i + 1]; var g = i < reveal ? easeBack(prog(lt, ts == null ? i * 0.15 : ts, 0.45)) : 0;
    html += '<div class="card" style="display:flex;gap:28px;align-items:center;padding:30px 34px;opacity:' + clamp(g * 1.3, 0, 1) + ';transform:translateY(' + (1 - g) * 40 + 'px)">' +
      '<div style="flex:none;background:' + (it.color || '#fff') + ';border-radius:22px;padding:16px 18px">' + ledP(String(i + 1), 11, '#1432E6', 1, 0) + '</div>' +
      '<div><div class="hd" style="font-size:54px;text-transform:none;letter-spacing:-.025em">' + hlt(it.h) + '</div>' +
      (it.d ? '<div style="font:600 32px/1.3 Red Hat Display;color:#C9D4FF;margin-top:6px">' + esc(it.d) + '</div>' : '') + '</div></div>';
  });
  return (d.title ? '<div class="abs hd" style="left:70px;top:290px;width:900px;font-size:64px;text-transform:none;letter-spacing:-.03em">' + hlt(d.title) + '</div>' : '') +
    '<div class="abs" style="left:60px;top:' + (d.title ? 400 : 300) + 'px;width:960px;display:grid;gap:20px">' + html + '</div>';
};

R.vs = function (d, lt, st) {
  var reveal = d.reveal || 0;
  function col(c, x, accent) {
    var rows = '';
    c.rows.forEach(function (r, i) {
      var ts = st.revealAt[i + 1]; var g = i < reveal ? easeOut(prog(lt, ts == null ? 0 : ts, 0.4)) : 0;
      rows += '<div style="font:700 34px/1.25 Red Hat Display;padding:18px 0;border-top:2px solid rgba(255,255,255,.14);opacity:' + g + ';transform:translateY(' + (1 - g) * 16 + 'px)">' + esc(r) + '</div>';
    });
    return '<div class="card" style="position:absolute;left:' + x + 'px;top:300px;width:450px;padding:30px 32px 16px">' +
      '<div class="chip" style="background:' + accent + ';color:#0A0F2E">' + esc(c.tag) + '</div>' +
      '<div class="hd" style="font-size:72px;margin:18px 0 14px">' + esc(c.name) + '</div>' + rows + '</div>';
  }
  var vp = easeBack(prog(lt, 0.1, 0.4));
  return col(d.left, 60, '#9DB4FF') + col(d.right, 570, '#2BD98A') +
    '<div class="abs" style="left:490px;top:370px;width:100px;height:100px;border-radius:50%;background:#fff;color:#1432E6;display:grid;place-items:center;transform:scale(' + vp + ');box-shadow:0 10px 30px rgba(6,10,40,.35)"><span class="hd" style="font-size:44px">VS</span></div>';
};

R.myth = function (d, lt, st) {
  var fact = d.phase === 'fact', ft = st.phaseAt || 0;
  var sp = fact ? easeOut(prog(lt, ft, 0.5)) : 0, fp = fact ? easeBack(prog(lt, ft + 0.35, 0.5)) : 0, mp = easeBack(prog(lt, 0.05, 0.4));
  return '<div class="abs card" style="left:60px;top:300px;width:960px;padding:36px 40px;opacity:' + (1 - sp * 0.45) + '">' +
    '<div class="chip" style="background:#FF4D5E;color:#fff;transform:scale(' + mp + ');transform-origin:left">Myth</div>' +
    '<div class="hd" style="position:relative;font-size:64px;text-transform:none;letter-spacing:-.03em;margin-top:18px">' + esc(d.myth) +
    '<i style="position:absolute;left:-6px;top:52%;height:9px;border-radius:9px;background:#FF4D5E;width:' + (sp * 102) + '%"></i></div></div>' +
    '<div class="abs" style="left:60px;top:650px;width:960px;background:#fff;color:#0A0F2E;border-radius:34px;padding:36px 40px;opacity:' + clamp(fp * 1.3, 0, 1) + ';transform:translateY(' + (1 - fp) * 50 + 'px)">' +
    '<div class="chip" style="background:#2BD98A;color:#0A0F2E">Fact</div>' +
    '<div class="hd" style="font-size:60px;text-transform:none;letter-spacing:-.03em;margin-top:18px">' + hlt(d.fact) + '</div></div>';
};

R.term = function (d, lt) {
  var pitch = ledFit(d.term, 620, 26), p = easeOut(prog(lt, 0.1, 0.6)), cp = easeOut(prog(lt, 0.45, 0.45)), ep = easeOut(prog(lt, d.exampleAt || 1.4, 0.45));
  return '<div class="abs chip" style="left:70px;top:300px;background:#2BD98A;color:#0A0F2E">Dot explains</div>' +
    '<div class="abs" style="left:70px;top:380px">' + ledP(d.term, pitch, '#fff', p, 0.1) + '</div>' +
    '<div class="abs" style="left:60px;top:' + (410 + pitch * 7 + 30) + 'px;width:960px;background:#fff;color:#0A0F2E;border-radius:34px;padding:34px 40px;opacity:' + cp + ';transform:translateY(' + (1 - cp) * 30 + 'px)">' +
    '<div class="hd" style="font-size:58px;text-transform:none;letter-spacing:-.03em">' + hlt(d.def) + '</div>' +
    (d.example ? '<div style="font:800 44px/1.3 Red Hat Display;color:#1432E6;margin-top:18px;opacity:' + ep + '">' + esc(d.example) + '</div>' : '') + '</div>';
};

R.outro = function (d, lt) {
  var p = easeOut(prog(lt, 0.1, 0.9)), tp = easeOut(prog(lt, 0.7, 0.4));
  return '<div class="abs" style="left:70px;top:340px;display:flex;align-items:center;gap:18px">' + ledP('FINANCEPROS', 11, '#fff', p, 0.08) +
    '<div style="background:#fff;border-radius:14px;padding:9px 10px;opacity:' + p + '">' + ledP('TV', 7, '#1432E6', 1, 0) + '</div></div>' +
    '<div class="abs hd" style="left:70px;top:580px;font-size:84px;text-transform:none;letter-spacing:-.03em;opacity:' + tp + '">' + hlt(d.line || "That's the [money].") + '</div>' +
    '<div class="abs mono" style="left:74px;top:700px;font-size:30px;color:#C9D4FF;opacity:' + tp + '">' + esc(d.cta || 'Follow for the next bell') + '</div>' +
    '<div class="abs mono" style="left:74px;top:770px;font-size:22px;color:rgba(255,255,255,.6);opacity:' + tp + '">News and education, not financial advice.</div>';
};

/* ---------- timeline -> scenes ---------- */
function buildScenes() {
  SCENES = []; var cur = null;
  TL.lines.forEach(function (ln, i) {
    var s = ln.scene || {};
    var same = cur && s.type && cur.def.type === s.type && s.group && cur.def.group === s.group;
    if (s.type && !same) {
      cur = { start: i === 0 ? -5 : ln.s - 0.22, def: JSON.parse(JSON.stringify(s)), steps: [{ t: ln.s, def: s }], first: i === 0 };
      SCENES.push(cur);
    } else if (cur && s.type) { cur.steps.push({ t: ln.s, def: s }); }
    if (cur) cur.end = ln.e;
  });
  SCENES.forEach(function (sc, i) { sc.stop = i < SCENES.length - 1 ? SCENES[i + 1].start : 1e9 });
}
function sceneAt(t) { var s = SCENES[0]; SCENES.forEach(function (x) { if (t >= x.start) s = x }); return s }
function lineAt(t) { var l = null; TL.lines.forEach(function (x) { if (t >= x.s - 0.05 && t <= x.e + 0.28) l = x }); return l }

function mergedDef(sc, t) {
  var d = {}, st = { revealAt: {}, phaseAt: 0 };
  sc.steps.forEach(function (s, i) {
    if (i === 0 || t >= s.t - 0.05) {
      if (s.def.reveal != null && d.reveal !== s.def.reveal) st.revealAt[s.def.reveal] = s.t - sc.start;
      if (s.def.phase && d.phase !== s.def.phase) st.phaseAt = s.t - sc.start;
      Object.keys(s.def).forEach(function (k) { d[k] = s.def[k] });
    }
  });
  return { d: d, st: st };
}

/* ---------- captions ---------- */
function chunks(words) {
  var out = [], cur = [];
  words.forEach(function (w, i) {
    cur.push(w);
    var end = /[,.;:?!]$/.test(w.w) && cur.length >= 3;
    if (cur.length >= 6 || end || i === words.length - 1) { out.push(cur); cur = [] }
  });
  return out;
}
function captions(t) {
  var ln = lineAt(t); if (!ln || (ln.scene && ln.scene.nocap)) return '';
  var ch = chunks(ln.words), act = null, cc = ch[ch.length - 1];
  for (var i = 0; i < ch.length; i++) { var c = ch[i]; if (t < c[c.length - 1].e + 0.02) { cc = c; break } }
  cc.forEach(function (w) { if (t >= w.s && t < w.e + 0.02) act = w });
  var html = ln.who === 'dot' ? '<span class="who">Dot</span>' : '';
  cc.forEach(function (w) { html += '<span class="w' + (w === act ? ' on' : '') + '">' + esc(w.w) + '</span> ' });
  return html;
}

/* ---------- characters ---------- */
function mouthFor(v) { return v < 0.07 ? 'closed' : v < 0.28 ? 'small' : v < 0.62 ? 'talk' : 'wide' }
function renderTicker(t, sc, d) {
  var mode = d.tk || 'dock', el = $('tk');
  if (mode === 'off') { el.innerHTML = ''; return }
  var ln = lineAt(t), f = Math.min(TL.env.length - 1, Math.floor(t * FPS));
  var talking = ln && ln.who === 'ticker' && t >= ln.s && t <= ln.e;
  var mouth = talking ? mouthFor(TL.env[f]) : 'closed';
  if (!talking && d.expr && /up|shock|dollar/.test(d.expr)) mouth = d.expr === 'shock' ? 'o' : 'ee';
  var blink = (t % 3.9) > 3.76;
  var bob = Math.sin(t * 2.1) * 6, lean = Math.sin(t * 1.3) * 1.2;
  var box = mode === 'big' ? { l: 250, t: 900, w: 660 } : mode === 'right' ? { l: 520, t: 1120, w: 480 } : { l: 260, t: 1090, w: 560 };
  var sp = sc.first ? 1 : easeBack(prog(t, sc.start + 0.05, 0.4));
  el.style.cssText = 'left:' + box.l + 'px;top:' + (box.t + bob + (1 - sp) * 120) + 'px;width:' + box.w + 'px;transform:rotate(' + lean + 'deg);transform-origin:50% 100%';
  el.innerHTML = ticker({ expr: d.expr || 'neutral', pose: d.pose, mouth: mouth, blink: blink && !/up|down|shock|dollar/.test(d.expr || ''), flash: d.expr === 'shock', outline: 7 });
}
function renderDot(t, d) {
  var ln = lineAt(t), el = $('dot'), show = d.dot || (ln && ln.who === 'dot');
  if (!show) { el.innerHTML = ''; return }
  var f = Math.min(TL.env.length - 1, Math.floor(t * FPS)), talk = ln && ln.who === 'dot' && t >= ln.s && t <= ln.e ? TL.env[f] : 0;
  var bob = Math.sin(t * 3) * 10, s = 1 + talk * 0.06;
  var big = d.type === 'term', w = big ? 380 : 230, L = big ? 350 : 720, T = big ? 1180 : 1150;
  el.style.cssText = 'left:' + L + 'px;top:' + (T + bob) + 'px;width:' + w + 'px;transform:scale(' + s + ');transform-origin:50% 60%';
  el.innerHTML = dot({ attrs: 'width="' + w + '"' });
}

/* ---------- main ---------- */
function setup(ep, tl) {
  EP = ep; TL = tl; FPS = tl.fps; buildScenes();
  $('top').innerHTML = '<span class="pill"' + (ep.pillColor ? ' style="background:' + ep.pillColor + ';color:#fff"' : '') + '>' + esc(ep.tag) + '</span>';
  $('bug').innerHTML = led('FP', 6, '#fff', { off: 0 });
}
function render(t) {
  var sc = sceneAt(t), md = mergedDef(sc, t), d = md.d, lt = sc.first ? 99 : t - sc.start;
  if (sc.first) { lt = t + 3 }            // frame 0 shows the finished title card (it is the cover image)
  $('bg').style.transform = 'translate(' + (-(t * 7) % 26) + 'px,' + (-(t * 4) % 26) + 'px)';
  $('bg').style.backgroundColor = d.bg === 'navy' ? '#0A0F2E' : '#1432E6';
  $('scene').innerHTML = (R[d.type] || R.title)(d, lt, md.st);
  $('cap').style.top = (d.capTop || 960) + 'px';
  $('cap').innerHTML = captions(t);
  renderTicker(t, sc, d); renderDot(t, d);
  // LED scan wipe into each new scene
  var w = $('wipe'); w.style.opacity = 0;
  SCENES.forEach(function (x) { if (x.first) return; var p = (t - (x.start - 0.18)) / 0.5;
    if (p > 0 && p < 1) { var c = -30 + p * 160; w.style.opacity = 1;
      w.style.webkitMaskImage = w.style.maskImage = 'linear-gradient(100deg,transparent ' + (c - 22) + '%,#000 ' + c + '%,transparent ' + (c + 22) + '%)' } });
}
window.setup = setup; window.render = render;
