/* FinancePros TV doodle player: hand-drawn explainer look (white paper, black marker lines that
   "boil" like hand animation, flat colors, red annotations). Scenes are data: each line adds or
   updates items; lines that share a scene "group" keep everything on screen. */
var W, H, LAND, EP, TL, SCENES = [];
var INK = '#111', RED = '#E0241B', GREEN = '#3E9B4F', BLUE = '#1432E6';
var K = 'stroke="' + INK + '" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" vector-effect="non-scaling-stroke"';

function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }
function prog(t, s, d) { return clamp((t - s) / d, 0, 1); }
function ease(p) { return 1 - Math.pow(1 - p, 3); }
function back(p) { var c = 1.9; p = clamp(p, 0, 1); return 1 + (c + 1) * Math.pow(p - 1, 3) + c * Math.pow(p - 1, 2); }
function rng(seed) { var s = (seed * 9301 + 49297) % 233280; return function () { s = (s * 9301 + 49297) % 233280; return s / 233280; }; }
function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
function f1(n) { return Math.round(n * 10) / 10; }

/* ---------- drawing primitives ---------- */
function drawPath(d, p, extra) {   // stroke draws on as p goes 0 -> 1
  if (p <= 0) return '';
  return '<path d="' + d + '" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="' + f1(1 - p) + '" fill="none" ' + (extra || K) + '/>';
}
function roughLoop(cx, cy, rx, ry, seed, turns) {   // marker circle that overshoots its start, like a real annotation
  var r = rng(seed), n = 46, pts = [], a0 = -0.6 + r() * 0.4;
  for (var i = 0; i <= n; i++) {
    var a = a0 + (i / n) * Math.PI * 2 * (turns || 1.12), j = 1 + (r() - 0.5) * 0.05 + (i / n) * 0.06;
    pts.push(f1(cx + Math.cos(a) * rx * j) + ',' + f1(cy + Math.sin(a) * ry * j));
  }
  return 'M' + pts.join(' L');
}
function text(x, y, s, o) {
  o = o || {};
  var fam = { hand: 'Patrick Hand', serif: 'Baskerville', marker: 'Marker', chalk: 'Patrick Hand', kalam: 'Kalam' }[o.font || 'hand'];
  var lines = String(s).split('\n'), out = '';
  if (o.maxW) {   // shrink to fit, measured with the real font
    var cv = text._cv || (text._cv = document.createElement('canvas').getContext('2d')), sz = o.size || 60;
    cv.font = (o.weight || 400) + ' ' + sz + 'px "' + fam + '"';
    var wmax = Math.max.apply(null, lines.map(function (l) { return cv.measureText(l.replace(/[\[\]]/g, '')).width; }));
    if (wmax > o.maxW) o = Object.assign({}, o, { size: Math.floor(sz * o.maxW / wmax) });
  }
  var lh = (o.size || 60) * (o.lh || 1.05);
  lines.forEach(function (ln, i) {
    out += '<text x="' + x + '" y="' + f1(y + i * lh) + '" font-family="' + fam + '" font-size="' + (o.size || 60) + '"' +
      (o.weight ? ' font-weight="' + o.weight + '"' : '') + ' fill="' + (o.color || INK) + '" text-anchor="' + (o.anchor || 'middle') + '"' +
      (o.rot ? ' transform="rotate(' + o.rot + ' ' + x + ' ' + y + ')"' : '') + '>' +
      esc(ln).replace(/\[([^\]]+)\]/g, '<tspan fill="' + (o.hl || RED) + '">$1</tspan>') + '</text>';
  });
  return out;
}
function arrowD(x1, y1, x2, y2, bend) {
  var mx = (x1 + x2) / 2 - (y2 - y1) * (bend || 0.2), my = (y1 + y2) / 2 + (x2 - x1) * (bend || 0.2);
  return { d: 'M' + x1 + ',' + y1 + ' Q' + f1(mx) + ',' + f1(my) + ' ' + x2 + ',' + y2, mx: mx, my: my };
}

/* ---------- characters ---------- */
function ticker(o, lt) {   // Ticker as a doodle: TV head, stick body
  var talk = o._talk || 0, g = '';
  var A = {
    idle: 'M0,-262 L-62,-175 M0,-262 L62,-175', point: 'M0,-262 L-60,-178 M0,-262 L150,-305',
    pointdown: 'M0,-262 L-60,-178 M0,-262 L145,-200', pointleft: 'M0,-262 L-150,-305 M0,-262 L60,-178',
    wave: 'M0,-262 L-60,-178 M0,-262 L72,-330 L98,-398', shrug: 'M0,-262 L-72,-232 L-112,-292 M0,-262 L72,-232 L112,-292',
    cheer: 'M0,-262 L-86,-345 M0,-262 L86,-345', think: 'M0,-262 L-58,-182 M0,-262 L58,-212 L28,-300',
    hold: 'M0,-262 L-60,-178 M0,-262 L80,-205 L135,-232', hips: 'M0,-262 L-55,-215 L-8,-175 M0,-262 L55,-215 L8,-175'
  };
  g += '<path d="M0,-150 L-50,0 M0,-150 L50,0 M0,-292 L0,-150 ' + (A[o.pose || 'idle'] || A.idle) + '" fill="none" ' + K + '/>';
  if (o.stick) g += '<path d="M' + (o.pose === 'pointleft' ? -150 : 150) + ',-305 L' + o.stick[0] + ',' + o.stick[1] + '" stroke="#7B4B24" stroke-width="9" stroke-linecap="round"/>';
  g += '<path d="M-26,-423 L-62,-482 M26,-423 L56,-487" fill="none" ' + K + '/><circle cx="-62" cy="-484" r="9" fill="' + INK + '"/>' +
       '<circle cx="56" cy="-489" r="11" fill="' + RED + '" stroke="' + INK + '" stroke-width="5"/>';
  g += '<rect x="-98" y="-428" width="196" height="142" rx="30" fill="#F3EFE6" stroke="' + INK + '" stroke-width="7"/>' +
       '<rect x="-78" y="-411" width="156" height="106" rx="18" fill="' + BLUE + '" stroke="' + INK + '" stroke-width="5"/>' +
       '<circle cx="62" cy="-298" r="4" fill="' + INK + '"/><circle cx="48" cy="-298" r="4" fill="' + INK + '"/>';
  var m = o.mood || 'happy', blink = ((lt + (o.x || 0) / 97) % 3.7) < 0.12, E = '';
  if (m === 'up') E = '<path d="M-44,-358 L-30,-378 L-16,-358 M16,-358 L30,-378 L44,-358" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>';
  else if (m === 'shock') E = '<circle cx="-30" cy="-368" r="15" fill="#fff"/><circle cx="30" cy="-368" r="15" fill="#fff"/><circle cx="-30" cy="-368" r="6" fill="' + INK + '"/><circle cx="30" cy="-368" r="6" fill="' + INK + '"/>';
  else if (blink) E = '<path d="M-40,-368 L-20,-368 M20,-368 L40,-368" stroke="#fff" stroke-width="6" stroke-linecap="round"/>';
  else E = '<circle cx="-30" cy="-368" r="10" fill="#fff"/><circle cx="30" cy="-368" r="10" fill="#fff"/>';
  if (m === 'worried' || m === 'sad') E += '<path d="M-46,-384 L-18,-395 M18,-395 L46,-384" stroke="#fff" stroke-width="6" stroke-linecap="round"/>';
  if (m === 'angry') E += '<path d="M-46,-388 L-18,-378 M18,-378 L46,-388" stroke="#fff" stroke-width="6" stroke-linecap="round"/>';
  var M;
  if (talk > 0.12) M = '<ellipse cx="0" cy="-332" rx="17" ry="' + f1(4 + talk * 15) + '" fill="#fff"/>';
  else if (m === 'sad' || m === 'worried') M = '<path d="M-20,-322 Q0,-338 20,-322" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>';
  else if (m === 'shock') M = '<ellipse cx="0" cy="-330" rx="12" ry="14" fill="#fff"/>';
  else M = '<path d="M-24,-340 Q0,-318 24,-340" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>';
  g += E + M;
  if (o.sweat) g += '<path d="M112,-420 q10,18 0,26 q-10,-8 0,-26z" fill="#7EC8F2" stroke="' + INK + '" stroke-width="4"/>';
  return '<g transform="translate(' + o.x + ',' + o.y + ') scale(' + (o.s || 1) * (o.flip ? -1 : 1) + ',' + (o.s || 1) + ')">' + g + '</g>';
}

function nutty(o, lt) {   // the Acorn Economics squirrel: chunky marker drawing
  var talk = o._talk || 0, g = '', B = '#C27A3E', D = '#9E5A26', C = '#F4D9AE';
  var tap = o.tap ? Math.max(0, Math.sin(lt * 14)) * 10 : 0;
  g += '<path d="M40,-60 C170,-40 250,-160 205,-270 C178,-335 245,-385 212,-455 C170,-515 88,-482 108,-405 C122,-350 86,-300 106,-232 C120,-172 78,-118 30,-104 Z" fill="' + D + '" ' + K + '/>';
  g += '<path d="M168,-420 C188,-370 150,-318 170,-252" fill="none" stroke="#6E3A14" stroke-width="5" stroke-linecap="round"/>';
  g += '<ellipse cx="-45" cy="' + (-10 - tap) + '" rx="44" ry="17" fill="' + B + '" ' + K + '/><ellipse cx="42" cy="-10" rx="44" ry="17" fill="' + B + '" ' + K + '/>';
  g += '<ellipse cx="0" cy="-142" rx="88" ry="120" fill="' + B + '" ' + K + '/>';
  g += '<ellipse cx="-6" cy="-125" rx="52" ry="82" fill="' + C + '" stroke="' + INK + '" stroke-width="5"/>';
  g += '<path d="M-72,-340 L-86,-410 L-30,-358 Z M26,-360 L60,-418 L74,-338 Z" fill="' + B + '" ' + K + '/>';
  g += '<ellipse cx="-4" cy="-290" rx="92" ry="80" fill="' + B + '" ' + K + '/>';
  g += '<ellipse cx="-4" cy="-258" rx="46" ry="33" fill="' + C + '" stroke="' + INK + '" stroke-width="5"/>';
  g += '<ellipse cx="-4" cy="-280" rx="14" ry="10" fill="' + INK + '"/>';
  g += '<ellipse cx="-58" cy="-262" rx="15" ry="9" fill="#F29B9B" opacity=".8"/><ellipse cx="50" cy="-262" rx="15" ry="9" fill="#F29B9B" opacity=".8"/>';
  var blink = ((lt + 1.3) % 3.3) < 0.12;
  if (o.shades) g += '<path d="M-78,-326 L72,-326 L66,-296 Q36,-280 12,-300 L4,-312 L-12,-312 L-20,-300 Q-46,-280 -72,-296 Z" fill="' + INK + '"/><path d="M-60,-318 L-40,-318" stroke="#fff" stroke-width="4"/>';
  else if (blink) g += '<path d="M-52,-314 L-28,-314 M18,-314 L42,-314" stroke="' + INK + '" stroke-width="6" stroke-linecap="round"/>';
  else g += '<circle cx="-40" cy="-314" r="11" fill="' + INK + '"/><circle cx="30" cy="-314" r="11" fill="' + INK + '"/><circle cx="-36" cy="-318" r="3.5" fill="#fff"/><circle cx="34" cy="-318" r="3.5" fill="#fff"/>';
  if (o.mood === 'worried') g += '<path d="M-58,-332 L-28,-344 M20,-344 L50,-332" stroke="' + INK + '" stroke-width="6" stroke-linecap="round"/>';
  if (talk > 0.12) g += '<ellipse cx="-4" cy="-246" rx="16" ry="' + f1(4 + talk * 13) + '" fill="#5B1E1E" stroke="' + INK + '" stroke-width="4"/>';
  else g += '<path d="M-24,-252 Q-4,-240 16,-252" fill="none" stroke="' + INK + '" stroke-width="5" stroke-linecap="round"/>';
  g += '<rect x="-15" y="-246" width="11" height="15" rx="2" fill="#fff" stroke="' + INK + '" stroke-width="3.5"/><rect x="-4" y="-246" width="11" height="15" rx="2" fill="#fff" stroke="' + INK + '" stroke-width="3.5"/>';
  if (o.drool) g += '<path d="M10,-236 q4,24 -2,30 q-8,-6 2,-30z" fill="#9ED8F5" stroke="' + INK + '" stroke-width="3"/>';
  var arms = { idle: 'M-62,-200 Q-102,-160 -70,-128 M58,-200 Q98,-160 66,-128', hold: 'M-62,-205 Q-40,-160 -14,-170 M58,-205 Q36,-160 10,-170',
    up: 'M-62,-205 L-120,-300 M58,-205 L116,-300', point: 'M-62,-200 Q-102,-160 -70,-128 M58,-205 L150,-250', shrug: 'M-62,-205 L-110,-190 L-128,-240 M58,-205 L106,-190 L124,-240' };
  g += '<path d="' + (arms[o.pose || 'idle'] || arms.idle) + '" fill="none" stroke="' + INK + '" stroke-width="9" stroke-linecap="round"/>';
  if (o.item === 'acorn') g += acorn(0, -185, 0.8);
  if (o.item === 'coin') g += coin(0, -185, 32);
  return '<g transform="translate(' + o.x + ',' + o.y + ') scale(' + (o.s || 1) * (o.flip ? -1 : 1) + ',' + (o.s || 1) + ')">' + g + '</g>';
}

var EYES = { us: [0.53, 0.36], china: [0.62, 0.52], mexico: [0.52, 0.45], canada: [0.44, 0.7], japan: [0.6, 0.4], uk: [0.62, 0.52], germany: [0.5, 0.45] };
var LEGY = { japan: 0.6, mexico: 0.72, uk: 0.9, us: 0.86 };
var BOX = { us: [1000, 620] };
function country(o, lt) {   // a country outline as a googly-eyed character
  var k = o.name, bw = (BOX[k] || [700, 700])[0], bh = (BOX[k] || [700, 700])[1], sc = o.w / bw, h = bh * sc, x0 = o.x - o.w / 2, y0 = o.y - h / 2, g = '';
  var talk = o._talk || 0, e = EYES[k] || [0.5, 0.45], ex = x0 + e[0] * o.w, ey = y0 + e[1] * h, r = Math.max(18, o.w * 0.045);
  if (o.legs !== false) {
    var ly = y0 + h * (o.legY || LEGY[k] || 0.86), lx = ex;
    g += '<path d="M' + (lx - r * 1.4) + ',' + ly + ' L' + (lx - r * 1.8) + ',' + (ly + r * 4.2) + ' l-' + r * 0.9 + ',0 M' + (lx + r * 1.4) + ',' + ly + ' L' + (lx + r * 1.8) + ',' + (ly + r * 4.2) + ' l' + r * 0.9 + ',0" fill="none" ' + K + '/>';
  }
  if (o.arms) g += '<path d="' + o.arms + '" fill="none" ' + K + '/>';
  g += '<g transform="translate(' + f1(x0) + ',' + f1(y0) + ') scale(' + sc + ')"><path d="' + GEO[k] + '" fill="' + (o.color || GREEN) + '" stroke="' + INK + '" stroke-width="7" stroke-linejoin="round" vector-effect="non-scaling-stroke"/></g>';
  var lk = o.look || [0, 0], blink = ((lt + o.x / 113) % 3.9) < 0.12;
  [-1, 1].forEach(function (sd) {
    var cx = ex + sd * r * 1.15;
    if (blink) g += '<path d="M' + (cx - r) + ',' + ey + ' L' + (cx + r) + ',' + ey + '" stroke="' + INK + '" stroke-width="6" stroke-linecap="round"/>';
    else g += '<ellipse cx="' + f1(cx) + '" cy="' + f1(ey) + '" rx="' + f1(r) + '" ry="' + f1(r * 1.2) + '" fill="#fff" stroke="' + INK + '" stroke-width="5"/>' +
      '<circle cx="' + f1(cx + lk[0] * r * 0.45) + '" cy="' + f1(ey + lk[1] * r * 0.5) + '" r="' + f1(r * 0.42) + '" fill="' + INK + '"/>';
  });
  if (o.mood === 'worried') g += '<path d="M' + (ex - r * 2.2) + ',' + (ey - r * 1.3) + ' L' + (ex - r * 0.4) + ',' + (ey - r * 1.9) + ' M' + (ex + r * 0.4) + ',' + (ey - r * 1.9) + ' L' + (ex + r * 2.2) + ',' + (ey - r * 1.3) + '" stroke="' + INK + '" stroke-width="6" stroke-linecap="round"/>';
  if (o.mood === 'angry') g += '<path d="M' + (ex - r * 2.2) + ',' + (ey - r * 1.9) + ' L' + (ex - r * 0.4) + ',' + (ey - r * 1.2) + ' M' + (ex + r * 0.4) + ',' + (ey - r * 1.2) + ' L' + (ex + r * 2.2) + ',' + (ey - r * 1.9) + '" stroke="' + INK + '" stroke-width="7" stroke-linecap="round"/>';
  var my = ey + r * 2.1;
  if (talk > 0.12) g += '<ellipse cx="' + f1(ex) + '" cy="' + f1(my) + '" rx="' + f1(r * 0.6) + '" ry="' + f1(r * (0.2 + talk * 0.6)) + '" fill="#5B1E1E" stroke="' + INK + '" stroke-width="4"/>';
  else if (o.mood === 'worried' || o.mood === 'sad') g += '<path d="M' + (ex - r * 0.8) + ',' + (my + 6) + ' Q' + ex + ',' + (my - 10) + ' ' + (ex + r * 0.8) + ',' + (my + 6) + '" fill="none" stroke="' + INK + '" stroke-width="5" stroke-linecap="round"/>';
  else if (o.mood !== 'none') g += '<path d="M' + (ex - r * 0.8) + ',' + (my - 4) + ' Q' + ex + ',' + (my + 12) + ' ' + (ex + r * 0.8) + ',' + (my - 4) + '" fill="none" stroke="' + INK + '" stroke-width="5" stroke-linecap="round"/>';
  if (o.sweat) g += '<path d="M' + (ex + r * 3) + ',' + (ey - r * 2) + ' q12,20 0,30 q-12,-10 0,-30z" fill="#7EC8F2" stroke="' + INK + '" stroke-width="4"/>';
  if (o.label) g += text(o.x, y0 - 20, o.label, { size: 48 });
  return g;
}

/* ---------- props ---------- */
function acorn(x, y, s) {
  return '<g transform="translate(' + x + ',' + y + ') scale(' + s + ')"><path d="M-34,-6 Q-36,44 0,60 Q36,44 34,-6 Z" fill="#C98B45" ' + K + '/>' +
    '<path d="M-44,-4 Q-42,-38 0,-40 Q42,-38 44,-4 Q0,8 -44,-4 Z" fill="#7A4A22" ' + K + '/><path d="M0,-40 Q4,-56 14,-60" fill="none" ' + K + '/>' +
    '<path d="M-26,-20 L-18,-10 M-8,-26 L0,-14 M12,-24 L18,-12 M28,-18 L32,-8" stroke="#4A2A10" stroke-width="4" stroke-linecap="round"/></g>';
}
function coin(x, y, r) {
  return '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="#F2C230" ' + K + '/>' + text(x, y + r * 0.42, '$', { size: r * 1.25, font: 'serif', weight: 700, color: '#8A6508' });
}
function bill(x, y, w, rot, label) {
  var h = w * 0.45;
  return '<g transform="translate(' + x + ',' + y + ') rotate(' + (rot || 0) + ')"><rect x="' + (-w / 2) + '" y="' + (-h / 2) + '" width="' + w + '" height="' + h + '" rx="10" fill="#CFE6BF" ' + K + '/>' +
    '<rect x="' + (-w / 2 + 16) + '" y="' + (-h / 2 + 14) + '" width="' + (w - 32) + '" height="' + (h - 28) + '" rx="6" fill="none" stroke="#5E8C4E" stroke-width="4"/>' +
    '<ellipse cx="0" cy="0" rx="' + h * 0.34 + '" ry="' + h * 0.38 + '" fill="#A9CF95" stroke="#5E8C4E" stroke-width="4"/>' +
    text(0, h * 0.16, label || '$1', { size: h * 0.42, font: 'serif', weight: 700, color: '#2F5A22' }) +
    text(-w / 2 + 44, -h / 2 + 52, '1', { size: h * 0.26, font: 'serif', weight: 700, color: '#2F5A22' }) + text(w / 2 - 44, h / 2 - 22, '1', { size: h * 0.26, font: 'serif', weight: 700, color: '#2F5A22' }) + '</g>';
}
function bubble(x, y, w, h, s, tail, o) {
  o = o || {};
  var t = tail || [x - w * 0.2, y + h * 0.9];
  return '<path d="M' + (x - w * 0.18) + ',' + (y + h * 0.42) + ' L' + t[0] + ',' + t[1] + ' L' + (x + w * 0.02) + ',' + (y + h * 0.46) + '" fill="#fff" ' + K + '/>' +
    '<ellipse cx="' + x + '" cy="' + y + '" rx="' + w / 2 + '" ry="' + h / 2 + '" fill="#fff" ' + K + '/>' +
    '<path d="M' + (x - w * 0.16) + ',' + (y + h * 0.45) + ' L' + (x + w * 0.0) + ',' + (y + h * 0.46) + '" stroke="#fff" stroke-width="9"/>' +
    text(x, y + (o.size || 44) * 0.35 - (String(s).split('\n').length - 1) * (o.size || 44) * 0.5, s, { size: o.size || 44 });
}
function fed(x, y, s, label) {
  var g = '<path d="M-230,-250 L0,-360 L230,-250 Z" fill="#EDE6D3" ' + K + '/><rect x="-230" y="-250" width="460" height="38" fill="#EDE6D3" ' + K + '/>';
  for (var i = 0; i < 5; i++) g += '<rect x="' + (-200 + i * 90) + '" y="-212" width="40" height="170" fill="#F7F2E4" ' + K + '/>';
  g += '<rect x="-250" y="-42" width="500" height="22" fill="#EDE6D3" ' + K + '/><rect x="-275" y="-20" width="550" height="22" fill="#EDE6D3" ' + K + '/>';
  g += text(0, -222, label || 'FEDERAL RESERVE', { size: 28, font: 'serif', weight: 700 });
  return '<g transform="translate(' + x + ',' + y + ') scale(' + s + ')">' + g + '</g>';
}
function board(x, y, w, h, lines, p, o) {   // chalkboard; lines write on in order
  o = o || {};
  var g = '<rect x="' + (x - 14) + '" y="' + (y - 14) + '" width="' + (w + 28) + '" height="' + (h + 28) + '" rx="6" fill="#7B4B24" ' + K + '/>' +
    '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" fill="#2E6B3F" stroke="' + INK + '" stroke-width="5"/>';
  var n = lines.length, id = 'bc' + Math.round(x + y);
  lines.forEach(function (ln, i) {
    var pp = clamp(p * n - i, 0, 1); if (pp <= 0) return;
    var sz = ln.size || o.size || 88, ty = y + (ln.y != null ? ln.y : (h / (n + 1)) * (i + 1) + sz * 0.33);
    g += '<clipPath id="' + id + i + '"><rect x="' + x + '" y="' + (ty - sz) + '" width="' + f1(w * ease(pp)) + '" height="' + sz * 1.5 + '"/></clipPath>' +
      '<g clip-path="url(#' + id + i + ')">' + text(x + w / 2, ty, ln.t || ln, { size: sz, color: '#F4F4EC', font: 'chalk' }) + '</g>';
  });
  return g;
}
function tree(x, y, s, grow, acorns) {
  var g = '<path d="M-28,0 L-20,-190 Q-60,-230 -80,-260 M-20,-190 L-18,-150 M28,0 L22,-190 Q60,-230 76,-256" fill="#8A5A2B" ' + K + '/>' +
    '<path d="M-30,0 L-22,-200 L22,-200 L30,0 Z" fill="#8A5A2B" ' + K + '/>';
  g += '<path d="M-190,-230 C-260,-260 -230,-380 -150,-380 C-160,-470 -40,-500 0,-440 C40,-510 170,-470 150,-380 C240,-380 250,-250 170,-230 C170,-160 60,-150 20,-190 C-30,-150 -170,-150 -190,-230 Z" fill="#4FA64F" ' + K + '/>';
  (acorns || []).forEach(function (a) { g += acorn(a[0], a[1], 0.42); });
  return '<g transform="translate(' + x + ',' + y + ') scale(' + (s * (0.15 + 0.85 * grow)) + ')">' + g + '</g>';
}
function sprout(x, y, s) {
  return '<g transform="translate(' + x + ',' + y + ') scale(' + s + ')"><ellipse cx="0" cy="4" rx="120" ry="30" fill="#8B5A2B" ' + K + '/>' +
    '<path d="M0,-4 L0,-70" fill="none" stroke="' + INK + '" stroke-width="7" stroke-linecap="round"/><path d="M0,-50 Q-40,-80 -60,-60 Q-40,-40 0,-50 Z M0,-62 Q40,-96 62,-74 Q38,-50 0,-62 Z" fill="#6CC04A" ' + K + '/></g>';
}
function basket(x, y, w, label) {
  var h = w * 0.5, g = '<path d="M' + (-w / 2) + ',' + (-h) + ' L' + (w / 2) + ',' + (-h) + ' L' + (w * 0.4) + ',0 L' + (-w * 0.4) + ',0 Z" fill="#D9A55B" ' + K + '/>';
  for (var i = 1; i < 6; i++) g += '<path d="M' + (-w / 2 + i * w / 6) + ',' + (-h) + ' L' + (-w * 0.4 + i * w * 0.8 / 6) + ',0" stroke="#9C6A2A" stroke-width="5"/>';
  g += '<path d="M' + (-w * 0.46) + ',' + (-h * 0.5) + ' L' + (w * 0.46) + ',' + (-h * 0.5) + '" stroke="#9C6A2A" stroke-width="5"/>';
  if (label) g += '<rect x="' + (-w * 0.3) + '" y="' + (-h * 0.72) + '" width="' + (w * 0.6) + '" height="' + (h * 0.42) + '" rx="8" fill="#fff" ' + K + '/>' + text(0, -h * 0.41, label, { size: h * 0.22, font: 'marker' });
  return '<g transform="translate(' + x + ',' + y + ')">' + g + '</g>';
}
function box(x, y, w, label) {
  var h = w * 0.75;
  return '<g transform="translate(' + x + ',' + y + ')"><path d="M' + (-w / 2) + ',' + (-h / 2) + ' L' + (w / 2) + ',' + (-h / 2) + ' L' + (w / 2) + ',' + (h / 2) + ' L' + (-w / 2) + ',' + (h / 2) + ' Z" fill="#D9A86C" ' + K + '/>' +
    '<path d="M' + (-w * 0.1) + ',' + (-h / 2) + ' L' + (-w * 0.1) + ',' + (h * 0.05) + ' L' + (w * 0.1) + ',' + (h * 0.05) + ' L' + (w * 0.1) + ',' + (-h / 2) + '" fill="#E8C792" stroke="' + INK + '" stroke-width="5"/>' +
    (label ? text(0, h * 0.36, label, { size: w * 0.24, font: 'marker' }) : '') + '</g>';
}
function store(x, y, s, label) {
  var g = '<rect x="-190" y="-230" width="380" height="230" fill="#F3EFE6" ' + K + '/>';
  for (var i = 0; i < 6; i++) g += '<path d="M' + (-210 + i * 70) + ',-300 L' + (-140 + i * 70) + ',-300 L' + (-140 + i * 70) + ',-240 Q' + (-175 + i * 70) + ',-215 ' + (-210 + i * 70) + ',-240 Z" fill="' + (i % 2 ? '#fff' : RED) + '" ' + K + '/>';
  g += '<rect x="-60" y="-150" width="120" height="150" fill="#6BA8D8" ' + K + '/><rect x="-170" y="-170" width="90" height="80" fill="#BFE0F5" ' + K + '/><rect x="80" y="-170" width="90" height="80" fill="#BFE0F5" ' + K + '/>';
  g += '<rect x="-150" y="-370" width="300" height="64" rx="8" fill="#fff" ' + K + '/>' + text(0, -324, label || 'STORE', { size: 40, font: 'marker' });
  return '<g transform="translate(' + x + ',' + y + ') scale(' + s + ')">' + g + '</g>';
}
function booth(x, y, s, label) {
  var g = '<rect x="-120" y="-220" width="240" height="220" fill="#DCE6F2" ' + K + '/><path d="M-150,-220 L0,-300 L150,-220 Z" fill="#2B4C8C" ' + K + '/>' +
    '<rect x="-80" y="-180" width="160" height="80" fill="#BFE0F5" ' + K + '/><rect x="-140" y="-120" width="280" height="30" fill="#8FA9C8" ' + K + '/>' +
    '<rect x="-130" y="-360" width="260" height="56" rx="8" fill="#fff" ' + K + '/>' + text(0, -320, label || 'U.S. CUSTOMS', { size: 34, font: 'marker' });
  return '<g transform="translate(' + x + ',' + y + ') scale(' + s + ')">' + g + '</g>';
}
function tag(x, y, s, label, rot) {
  var w = Math.max(210, String(label).length * 34 + 70), a = -w / 2, b = w / 2 - 50;
  return '<g transform="translate(' + x + ',' + y + ') rotate(' + (rot || -8) + ') scale(' + s + ')"><path d="M' + a + ',-50 L' + b + ',-50 L' + (b + 50) + ',0 L' + b + ',50 L' + a + ',50 Z" fill="#FFF3B0" ' + K + '/><circle cx="' + (b + 12) + '" cy="0" r="10" fill="#fff" ' + K + '/>' +
    text((a + b) / 2, 22, label, { size: 60, font: 'marker' }) + '</g>';
}
function bag(x, y, s, label) {
  return '<g transform="translate(' + x + ',' + y + ') scale(' + s + ')"><path d="M-40,-150 L40,-150 L20,-115 Q110,-60 95,20 Q80,70 0,70 Q-80,70 -95,20 Q-110,-60 -20,-115 Z" fill="#CDB38A" ' + K + '/>' +
    '<path d="M-30,-118 L30,-118" ' + K + '/>' + text(0, 30, label || '$', { size: label && label.length > 2 ? 46 : 90, font: 'serif', weight: 700, color: '#3B6E2A' }) + '</g>';
}
function mattress(x, y, s) {
  var g = '<rect x="-230" y="-80" width="460" height="80" rx="18" fill="#E9F0FA" ' + K + '/>';
  for (var i = 1; i < 8; i++) g += '<path d="M' + (-230 + i * 57) + ',-80 L' + (-230 + i * 57) + ',0" stroke="#9DB7DA" stroke-width="5"/>';
  g += '<rect x="-205" y="-122" width="130" height="50" rx="20" fill="#fff" ' + K + '/>';
  return '<g transform="translate(' + x + ',' + y + ') scale(' + s + ')">' + g + '</g>';
}
function pot(x, y, s) {
  var g = '<path d="M-80,-100 L80,-100 L60,0 L-60,0 Z" fill="#C9683A" ' + K + '/><path d="M0,-100 L0,-230" ' + K + '/>' +
    '<path d="M0,-170 Q-60,-210 -90,-180 Q-60,-150 0,-170 Z M0,-200 Q60,-250 95,-215 Q60,-180 0,-200 Z" fill="#6CC04A" ' + K + '/>' + coin(0, -260, 38);
  return '<g transform="translate(' + x + ',' + y + ') scale(' + s + ')">' + g + '</g>';
}
function fire(x, y, s, lt) {
  var w = Math.sin(lt * 18) * 6;
  return '<g transform="translate(' + x + ',' + y + ') scale(' + s + ')"><path d="M-70,0 Q-100,-80 -50,-130 Q-40,-80 -20,-90 Q-30,-170 20,-210 Q' + (10 + w) + ',-140 50,-120 Q60,-160 80,-170 Q120,-80 70,0 Z" fill="#F28C28" ' + K + '/>' +
    '<path d="M-35,0 Q-50,-50 -20,-80 Q-10,-50 10,-60 Q' + (5 - w) + ',-110 35,-130 Q60,-60 40,0 Z" fill="#FFD23F" stroke="' + INK + '" stroke-width="5"/></g>';
}
function newspaper(x, y, w, head, sub) {
  var h = w * 0.72;
  var g = '<rect x="' + (-w / 2) + '" y="' + (-h / 2) + '" width="' + w + '" height="' + h + '" fill="#F7F4EC" ' + K + '/>' + text(0, -h / 2 + 62, 'THE DAILY MONEY', { size: 40, font: 'serif', weight: 700 }) +
    '<path d="M' + (-w / 2 + 20) + ',' + (-h / 2 + 84) + ' L' + (w / 2 - 20) + ',' + (-h / 2 + 84) + '" stroke="' + INK + '" stroke-width="4"/>' + text(0, -h / 2 + 150, head, { size: 50, font: 'serif', weight: 700, lh: 1.1 });
  for (var i = 0; i < 5; i++) g += '<path d="M' + (-w / 2 + 30) + ',' + (h * 0.05 + i * 34) + ' L' + (w / 2 - 30 - (i % 2) * 60) + ',' + (h * 0.05 + i * 34) + '" stroke="#999" stroke-width="5" stroke-linecap="round"/>';
  if (sub) g += text(0, h / 2 - 22, sub, { size: 30, color: '#555' });
  return '<g transform="translate(' + x + ',' + y + ')">' + g + '</g>';
}

/* ---------- chart: hand-drawn, draws itself ---------- */
function chart(o, p, lt) {
  var x = o.x, y = o.y, w = o.w, h = o.h, d = o.data, n = d.length, mx = o.max || Math.max.apply(null, d.map(function (q) { return q[1]; })) * 1.12, mn = o.min || 0;
  var x0 = d[0][0], x1 = d[n - 1][0], X = function (i) { return o.numeric ? x + ((d[i][0] - x0) / (x1 - x0)) * w : x + (i / (n - 1)) * w; }, Y = function (v) { return y + h - ((v - mn) / (mx - mn)) * h; };
  var g = '';
  if (o.title) g += text(x - 10, y - 40, o.title, { size: o.titleSize || 40, anchor: 'start', font: 'serif', weight: 700 });
  for (var k = 1; k <= 3; k++) g += '<path d="M' + x + ',' + f1(y + h - k * h / 4) + ' L' + (x + w) + ',' + f1(y + h - k * h / 4) + '" stroke="#D5D5D5" stroke-width="3" stroke-dasharray="10 10"/>';
  g += drawPath('M' + x + ',' + y + ' L' + x + ',' + (y + h) + ' L' + (x + w) + ',' + (y + h), clamp(p * 3, 0, 1), 'stroke="' + INK + '" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"');
  (o.xl || []).forEach(function (l) { g += text(o.numeric ? x + ((l[0] - x0) / (x1 - x0)) * w : X(l[0]), y + h + 50, l[1], { size: o.lsize || 38 }); });
  (o.yl || []).forEach(function (l) { g += text(x - 18, Y(l[0]) + 12, l[1], { size: o.lsize || 34, anchor: 'end' }); });
  var pts = d.map(function (q, i) { return f1(X(i)) + ',' + f1(Y(q[1])); });
  var lp = clamp((p - 0.25) / 0.75, 0, 1);
  g += drawPath('M' + pts.join(' L'), lp, 'stroke="' + (o.color || RED) + '" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"');
  if (lp >= 1 && o.dot !== false) g += '<circle cx="' + f1(X(n - 1)) + '" cy="' + f1(Y(d[n - 1][1])) + '" r="12" fill="' + (o.color || RED) + '" ' + K.replace('7', '4') + '/>';
  (o.notes || []).forEach(function (nt) {
    var np = prog(lt, nt.at || 0, 0.8); if (np <= 0) return;
    var cx = X(nt.i), cy = Y(d[nt.i][1]);
    g += drawPath(roughLoop(cx, cy, nt.rx || 60, nt.ry || 50, nt.i + 3), np, 'stroke="' + RED + '" stroke-width="6" stroke-linecap="round" fill="none"');
    if (np > 0.6) g += text(cx + (nt.dx || 0), cy + (nt.dy || -80), nt.t, { size: nt.size || 44, color: RED, font: 'hand' });
  });
  if (o.end && lp >= 1) g += text(X(n - 1) + (o.endDx || 0), Y(d[n - 1][1]) + (o.endDy || -40), o.end, { size: o.endSize || 64, color: RED, font: 'serif', weight: 700, anchor: o.endAnchor || 'end' });
  return g;
}

/* ---------- items ---------- */
var KINDS = {
  ticker: function (o, p, lt) { return ticker(o, lt); },
  nutty: function (o, p, lt) { return nutty(o, lt); },
  country: function (o, p, lt) { return country(o, lt); },
  text: function (o) { return text(o.x, o.y, o.text, o); },
  bill: function (o) { return bill(o.x, o.y, o.w || 520, o.rot, o.label); },
  coin: function (o) { return coin(o.x, o.y, o.r || 40); },
  acorn: function (o) { return acorn(o.x, o.y, o.s || 1); },
  acorns: function (o) { var g = '', r = rng(o.seed || 5); for (var i = 0; i < (o.n || 12); i++) g += acorn(o.x + (r() - 0.5) * (o.w || 300), o.y - Math.pow(r(), 1.4) * (o.h || 120), 0.55 + r() * 0.25); return g; },
  bubble: function (o) { return bubble(o.x, o.y, o.w || 360, o.h || 170, o.text, o.tail, o); },
  fed: function (o) { return fed(o.x, o.y, o.s || 1, o.label); },
  board: function (o, p) { return board(o.x, o.y, o.w, o.h, o.lines, o._wp, o); },
  tree: function (o, p, lt) { return tree(o.x, o.y, o.s || 1, o.grow == null ? 1 : o._grow, o.acorns); },
  sprout: function (o) { return sprout(o.x, o.y, o.s || 1); },
  basket: function (o) { return basket(o.x, o.y, o.w || 500, o.label); },
  box: function (o) { return box(o.x, o.y, o.w || 200, o.label); },
  store: function (o) { return store(o.x, o.y, o.s || 1, o.label); },
  booth: function (o) { return booth(o.x, o.y, o.s || 1, o.label); },
  tag: function (o) { return tag(o.x, o.y, o.s || 1, o.label, o.rot); },
  bag: function (o) { return bag(o.x, o.y, o.s || 1, o.label); },
  mattress: function (o) { return mattress(o.x, o.y, o.s || 1); },
  pot: function (o) { return pot(o.x, o.y, o.s || 1); },
  fire: function (o, p, lt) { return fire(o.x, o.y, o.s || 1, lt); },
  paper: function (o) { return newspaper(o.x, o.y, o.w || 600, o.head, o.sub); },
  chart: function (o, p, lt) { return chart(o, o._cp, lt); },
  circle: function (o, p) { return drawPath(roughLoop(o.x, o.y, o.rx || 90, o.ry || 70, o.seed || 7), p, 'stroke="' + (o.color || RED) + '" stroke-width="' + (o.sw || 7) + '" stroke-linecap="round" fill="none"'); },
  arrow: function (o, p) {
    var a = arrowD(o.x1, o.y1, o.x2, o.y2, o.bend), c = o.color || RED, g = drawPath(a.d, p, 'stroke="' + c + '" stroke-width="' + (o.sw || 8) + '" stroke-linecap="round" fill="none"');
    if (p >= 1) { var ang = Math.atan2(o.y2 - a.my, o.x2 - a.mx), L = 34;
      g += '<path d="M' + f1(o.x2 - L * Math.cos(ang - 0.5)) + ',' + f1(o.y2 - L * Math.sin(ang - 0.5)) + ' L' + o.x2 + ',' + o.y2 + ' L' + f1(o.x2 - L * Math.cos(ang + 0.5)) + ',' + f1(o.y2 - L * Math.sin(ang + 0.5)) + '" fill="none" stroke="' + c + '" stroke-width="' + (o.sw || 8) + '" stroke-linecap="round" stroke-linejoin="round"/>'; }
    return g;
  },
  cross: function (o, p) { return drawPath('M' + (o.x - o.w / 2) + ',' + (o.y - o.h / 2) + ' L' + (o.x + o.w / 2) + ',' + (o.y + o.h / 2), clamp(p * 2, 0, 1), 'stroke="' + RED + '" stroke-width="9" stroke-linecap="round"') +
    drawPath('M' + (o.x + o.w / 2) + ',' + (o.y - o.h / 2) + ' L' + (o.x - o.w / 2) + ',' + (o.y + o.h / 2), clamp(p * 2 - 1, 0, 1), 'stroke="' + RED + '" stroke-width="9" stroke-linecap="round"'); },
  under: function (o, p) { return drawPath('M' + o.x1 + ',' + o.y + ' Q' + ((o.x1 + o.x2) / 2) + ',' + (o.y + 14) + ' ' + o.x2 + ',' + (o.y - 6), p, 'stroke="' + (o.color || RED) + '" stroke-width="8" stroke-linecap="round" fill="none"'); },
  logo: function (o) {
    return '<g transform="translate(' + o.x + ',' + o.y + ') scale(' + (o.s || 1) + ')">' + text(-80, 0, 'FinancePros', { size: 110, font: 'serif', weight: 700 }) +
      '<rect x="300" y="-92" width="130" height="84" rx="16" fill="' + BLUE + '" ' + K + '/>' + text(365, -32, 'TV', { size: 56, font: 'marker', color: '#fff' }) + '</g>';
  },
  house: function (o) {
    var g = '<path d="M-200,-190 L0,-340 L200,-190 Z" fill="#C9683A" ' + K + '/><rect x="-170" y="-190" width="340" height="190" fill="#F3EFE6" ' + K + '/>' +
      '<rect x="-40" y="-110" width="80" height="110" fill="#6BA8D8" ' + K + '/><rect x="-140" y="-160" width="70" height="60" fill="#BFE0F5" ' + K + '/><rect x="70" y="-160" width="70" height="60" fill="#BFE0F5" ' + K + '/>' +
      '<rect x="100" y="-320" width="40" height="80" fill="#8A5A2B" ' + K + '/>';
    return '<g transform="translate(' + o.x + ',' + o.y + ') scale(' + (o.s || 1) + ')">' + g + '</g>' + (o.label ? tag(o.x + 120 * (o.s || 1), o.y - 360 * (o.s || 1), 0.9 * (o.s || 1), o.label, 6) : '');
  },
  car: function (o) {
    var g = '<path d="M-220,-60 L-200,-120 L-110,-130 L-60,-200 L90,-200 L150,-130 L220,-110 L230,-60 Z" fill="' + (o.fill || RED) + '" ' + K + '/>' +
      '<path d="M-40,-185 L-80,-130 L20,-130 L20,-185 Z M40,-185 L40,-130 L125,-130 L90,-185 Z" fill="#BFE0F5" ' + K + '/>' +
      '<circle cx="-130" cy="-50" r="42" fill="#333" ' + K + '/><circle cx="140" cy="-50" r="42" fill="#333" ' + K + '/><circle cx="-130" cy="-50" r="14" fill="#ccc"/><circle cx="140" cy="-50" r="14" fill="#ccc"/>';
    return '<g transform="translate(' + o.x + ',' + o.y + ') scale(' + (o.s || 1) + ')">' + g + '</g>';
  },
  quote: function (o) {
    return '<rect x="' + o.x + '" y="' + o.y + '" width="' + o.w + '" height="' + o.h + '" rx="18" fill="#F7F4EC" ' + K + '/>' +
      text(o.x + 50, o.y + 130, '\u201C', { size: 180, font: 'serif', weight: 700, color: RED, anchor: 'start' }) +
      text(o.x + o.w / 2, o.y + 150, o.text, { size: o.size || 52, font: 'serif', lh: 1.25 }) +
      (o.source ? text(o.x + o.w - 40, o.y + o.h - 40, '\u2014 ' + o.source, { size: 38, anchor: 'end', color: '#555' }) : '');
  },
  path: function (o) { return '<path d="' + o.d + '" fill="' + (o.fill || 'none') + '" ' + K + '/>'; },
  card: function (o) {
    var w = o.w || 520, h = w * 0.63, g = '<rect x="' + (-w / 2) + '" y="' + (-h / 2) + '" width="' + w + '" height="' + h + '" rx="' + w * 0.06 + '" fill="' + (o.fill || '#2B4C8C') + '" ' + K + '/>' +
      '<rect x="' + (-w * 0.38) + '" y="' + (-h * 0.18) + '" width="' + w * 0.16 + '" height="' + h * 0.24 + '" rx="8" fill="#F2C230" ' + K + '/>' +
      text(-w * 0.4, h * 0.3, o.num || '4000 1234 5678 9010', { size: w * 0.07, anchor: 'start', color: '#fff', font: 'kalam' }) +
      (o.label ? text(w * 0.1, -h * 0.25, o.label, { size: w * 0.1, color: '#fff', font: 'marker' }) : '');
    return '<g transform="translate(' + o.x + ',' + o.y + ') rotate(' + (o.rot || 0) + ')">' + g + '</g>';
  },
  row: function (o) {
    return '<rect x="' + o.x + '" y="' + o.y + '" width="' + o.w + '" height="' + (o.h || 110) + '" rx="14" fill="' + (o.fill || '#fff') + '" ' + K + '/>' +
      text(o.x + 30, o.y + (o.h || 110) * 0.64, o.a, { size: o.size || 50, anchor: 'start' }) + text(o.x + o.w - 30, o.y + (o.h || 110) * 0.64, o.b, { size: o.size || 50, anchor: 'end', font: 'marker', color: o.bc || INK });
  },
  rect: function (o) { return '<rect x="' + o.x + '" y="' + o.y + '" width="' + o.w + '" height="' + o.h + '" rx="' + (o.r || 14) + '" fill="' + (o.fill || '#fff') + '" ' + K + '/>'; }
};
var DRAWN = { circle: 1, arrow: 1, cross: 1, under: 1 };

/* ---------- scene timeline ---------- */
function setup(ep, tl) {
  EP = ep; TL = tl; LAND = ep.format === 'landscape'; W = LAND ? 1920 : 1080; H = LAND ? 1080 : 1920; if (ep.size) { W = ep.size[0]; H = ep.size[1]; LAND = true; }
  var st = document.getElementById('stage'); st.style.width = W + 'px'; st.style.height = H + 'px';
  document.body.style.width = W + 'px'; document.body.style.height = H + 'px';
  var art = document.getElementById('art'); art.setAttribute('width', W); art.setAttribute('height', H); art.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
  var hd = document.getElementById('head');
  if (!LAND && ep.header) { hd.style.cssText = 'left:60px;width:880px;top:' + (ep.headTop || 235) + 'px;font-size:' + (ep.headSize || 72) + 'px'; hd.innerHTML = esc(ep.header).replace(/\n/g, '<br>'); }
  var cap = document.getElementById('cap');
  cap.style.cssText = LAND ? 'left:260px;width:1400px;top:955px;font-size:46px' : 'left:60px;width:880px;top:' + (ep.capTop || 1290) + 'px;font-size:' + (ep.capSize || 62) + 'px';
  if (ep.captions === false) cap.style.display = 'none';
  SCENES = []; var cur = null;
  TL.lines.forEach(function (ln, i) {
    var s = (EP.lines[i] && EP.lines[i].scene) || ln.scene || {};
    if (!cur || !s.group || s.group !== cur.group) { cur = { group: s.group, start: i === 0 ? -5 : ln.s - 0.12, items: {}, order: [], cam: s.cam }; SCENES.push(cur); }
    if (s.cam) cur.cam = s.cam;
    (s.items || []).forEach(function (it, j) {
      var id = it.id || ('i' + i + '_' + j);
      if (!cur.items[id]) { if (!KINDS[it.k]) return; cur.items[id] = { base: it, t0: ln.s + (it.at || 0), ups: [] }; cur.order.push(id); }
      else cur.items[id].ups.push({ t: ln.s + (it.at || 0), v: it });
    });
  });
}

function render(t) {
  var sc = SCENES[0];
  for (var i = 0; i < SCENES.length; i++) if (t >= SCENES[i].start) sc = SCENES[i];
  var lt = t - sc.start, fr = Math.round(t * TL.fps);
  var line = TL.lines[0]; TL.lines.forEach(function (l) { if (t >= l.s - 0.05) line = l; });
  var talk = TL.env[Math.min(TL.env.length - 1, fr)] || 0;
  if (!(t >= line.s && t <= line.e + 0.05)) talk = 0;
  document.getElementById('turb').setAttribute('seed', 1 + Math.floor(fr / 3) % 7);
  var out = '';
  sc.order.forEach(function (id) {
    var it = sc.items[id], o = {}, k;
    for (k in it.base) o[k] = it.base[k];
    var tUp = it.t0;
    it.ups.forEach(function (u) { if (t >= u.t) { for (var k2 in u.v) o[k2] = u.v[k2]; tUp = u.t; } });
    if (o.hide) { var hp = prog(t, tUp, 0.25); if (hp >= 1) return; o._fade = 1 - hp; }
    var p = prog(t, it.t0, o.dur || (DRAWN[o.k] ? 0.7 : 0.38));
    if (p <= 0) return;
    if ((o.k === 'ticker' || o.k === 'nutty' || o.k === 'country') && o.talk !== false && (o.who || 'ticker') === line.who) o._talk = talk;
    if (o.k === 'board') o._wp = prog(t, it.t0 + 0.2, o.write || 1.4);
    if (o.k === 'chart') o._cp = prog(t, it.t0, o.draw || 2.2);
    if (o.k === 'tree') o._grow = ease(prog(t, it.t0 + (o.growAt || 0), o.growDur || 1.4));
    var ilt = t - it.t0, inner = KINDS[o.k](o, p, ilt);
    var app = o.app || (DRAWN[o.k] || o.k === 'chart' || o.k === 'board' ? 'none' : 'pop');
    var cx = o.x != null ? o.x : W / 2, cy = o.y != null ? o.y : H / 2;
    if (o.k === 'ticker' || o.k === 'nutty') cy = o.y - 200 * (o.s || 1);
    if (o.bob) inner = '<g transform="translate(0,' + f1(Math.sin(ilt * 2.2 + cx) * o.bob) + ')">' + inner + '</g>';
    if (o.move) { var mp = ease(prog(t, it.t0 + (o.moveAt || 0), o.moveDur || 1.2)); inner = '<g transform="translate(' + f1(o.move[0] * mp) + ',' + f1(o.move[1] * mp) + ')">' + inner + '</g>'; }
    if (app === 'pop') { var s = back(p); inner = '<g transform="translate(' + cx + ',' + cy + ') scale(' + f1(s * 100) / 100 + ') translate(' + (-cx) + ',' + (-cy) + ')">' + inner + '</g>'; }
    else if (app === 'fade') inner = '<g opacity="' + f1(p) + '">' + inner + '</g>';
    else if (app === 'slide') inner = '<g transform="translate(0,' + f1((1 - ease(p)) * 160) + ')" opacity="' + f1(Math.min(1, p * 2)) + '">' + inner + '</g>';
    if (o._fade != null) inner = '<g opacity="' + f1(o._fade) + '">' + inner + '</g>';
    out += inner;
  });
  var cam = sc.cam || [1, 1.035], z = cam[0] + (cam[1] - cam[0]) * ease(clamp(lt / 6, 0, 1));
  var g = document.getElementById('g');
  // vertical: keep the drawing inside the TikTok / Reels / Shorts safe zone (clear of the top tabs, the right-hand buttons and the bottom caption)
  var safe = (!LAND && EP.safe !== false) ? 'translate(60,405) scale(0.9) translate(-60,-430) ' : '';
  g.setAttribute('transform', safe + 'translate(' + W / 2 + ',' + H * 0.45 + ') scale(' + z + ') translate(' + (-W / 2) + ',' + (-H * 0.45) + ')');
  g.innerHTML = out;
  // captions: short chunks, current word in red
  var cap = document.getElementById('cap'), html = '';
  if (t >= line.s - 0.05 && t <= line.e + 0.25 && EP.captions !== false) {
    var ws = line.words, chunks = [], c = [];
    ws.forEach(function (w, i) { c.push(i); if (c.length >= (LAND ? 7 : 4) || /[.,!?;:]$/.test(w.w)) { chunks.push(c); c = []; } });
    if (c.length) chunks.push(c);
    var cur = chunks[0];
    chunks.forEach(function (ch) { if (t >= ws[ch[0]].s - 0.05) cur = ch; });
    cur.forEach(function (i) { var on = t >= ws[i].s && t < ws[i].e + 0.02; html += '<span class="w' + (on ? ' on' : '') + '">' + esc(ws[i].w) + '</span>'; });
  }
  cap.innerHTML = html;
}
window.setup = setup; window.render = render;
