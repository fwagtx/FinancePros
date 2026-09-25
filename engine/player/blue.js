// ===== FinancePros TV blue LED system =====
var C={cobalt:'#1432E6',navy:'#0A0F2E',white:'#FFFFFF',sky:'#9DB4FF',paper:'#F4F6FF',up:'#2BD98A',down:'#FF4D5E',casing:'#F2F4FF',casing2:'#D3DAF6'};
var uid=0;

/* ---------- LED dot-matrix text ---------- */
var G={' ':'00000,00000,00000,00000,00000,00000,00000',
A:'01110,10001,10001,11111,10001,10001,10001',B:'11110,10001,10001,11110,10001,10001,11110',C:'01111,10000,10000,10000,10000,10000,01111',
D:'11110,10001,10001,10001,10001,10001,11110',E:'11111,10000,10000,11110,10000,10000,11111',F:'11111,10000,10000,11110,10000,10000,10000',
G:'01111,10000,10000,10111,10001,10001,01111',H:'10001,10001,10001,11111,10001,10001,10001',I:'11111,00100,00100,00100,00100,00100,11111',
K:'10001,10010,10100,11000,10100,10010,10001',L:'10000,10000,10000,10000,10000,10000,11111',M:'10001,11011,10101,10101,10001,10001,10001',
N:'10001,11001,10101,10011,10001,10001,10001',O:'01110,10001,10001,10001,10001,10001,01110',P:'11110,10001,10001,11110,10000,10000,10000',
R:'11110,10001,10001,11110,10100,10010,10001',S:'01111,10000,10000,01110,00001,00001,11110',T:'11111,00100,00100,00100,00100,00100,00100',
U:'10001,10001,10001,10001,10001,10001,01110',V:'10001,10001,10001,10001,01010,01010,00100',W:'10001,10001,10001,10101,10101,10101,01010',
Y:'10001,10001,01010,00100,00100,00100,00100',
'0':'01110,10001,10011,10101,11001,10001,01110','1':'00100,01100,00100,00100,00100,00100,01110','2':'01110,10001,00001,00010,00100,01000,11111',
'3':'11110,00001,00001,01110,00001,00001,11110','4':'00010,00110,01010,10010,11111,00010,00010','5':'11111,10000,11110,00001,00001,10001,01110',
'6':'00110,01000,10000,11110,10001,10001,01110','7':'11111,00001,00010,00100,01000,01000,01000','8':'01110,10001,10001,01110,10001,10001,01110',
'9':'01110,10001,10001,01111,00001,00010,01100','%':'11001,11010,00010,00100,01000,01011,10011','.':'00000,00000,00000,00000,00000,01100,01100',
'-':'00000,00000,00000,11111,00000,00000,00000','+':'00000,00100,00100,11111,00100,00100,00000','!':'00100,00100,00100,00100,00100,00000,00100',
':':'00000,01100,01100,00000,01100,01100,00000','$':'00100,01111,10100,01110,00101,11110,00100',',':'00000,00000,00000,00000,01100,00100,01000','?':'01110,10001,00001,00010,00100,00000,00100','^':'00100,00100,01110,01110,11111,11111,00000','v':'11111,11111,01110,01110,00100,00100,00000'};
function ledCols(text){var cols=[];for(var i=0;i<text.length;i++){var g=(G[text[i]]||G[' ']).split(',');for(var x=0;x<5;x++){var c=[];for(var y=0;y<7;y++)c.push(g[y][x]==='1');cols.push(c)}if(i<text.length-1)cols.push([0,0,0,0,0,0,0])}return cols}
// returns svg string sized to the text; p=pitch, color, off=unlit opacity, glow
function led(text,p,color,o){o=o||{};var cols=ledCols(text),w=cols.length*p,h=7*p,r=p*(o.r||0.38),id='lg'+(uid++),s='';
  var lit='',off='';cols.forEach(function(c,x){c.forEach(function(v,y){var cx=(x+.5)*p,cy=(y+.5)*p;if(v)lit+='<circle cx="'+cx+'" cy="'+cy+'" r="'+r+'"/>';else if(o.off)off+='<circle cx="'+cx+'" cy="'+cy+'" r="'+r+'"/>'})});
  s='<svg xmlns="http://www.w3.org/2000/svg" width="'+w+'" height="'+h+'" viewBox="0 0 '+w+' '+h+'" style="overflow:visible;display:block">'+
  (o.glow!==false?'<defs><filter id="'+id+'" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="'+(p*0.22)+'" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>':'')+
  (o.off?'<g fill="'+(o.offColor||'#fff')+'" opacity="'+o.off+'">'+off+'</g>':'')+
  '<g fill="'+color+'" '+(o.glow!==false?'filter="url(#'+id+')"':'')+'>'+lit+'</g></svg>';return s}
// dotted background as CSS
function dotsBg(pitch,op,col){col=col||'255,255,255';return 'background-image:radial-gradient(circle,rgba('+col+','+op+') '+(pitch*0.18)+'px,transparent '+(pitch*0.2+0.6)+'px);background-size:'+pitch+'px '+pitch+'px;'}

/* ---------- Ticker, the LED TV-head anchor ---------- */
var FW='#FFFFFF';
function eyesPill(dx,dy,h){h=h||38;return '<rect x="'+(144+dx)+'" y="'+(188+dy)+'" width="28" height="'+h+'" rx="12" fill="'+FW+'"/><rect x="'+(228+dx)+'" y="'+(188+dy)+'" width="28" height="'+h+'" rx="12" fill="'+FW+'"/>'}
function brows(l,r){return '<path d="M140,'+(174+l[0])+' L178,'+(174+l[1])+'" stroke="'+FW+'" stroke-width="10" stroke-linecap="round"/><path d="M222,'+(174+r[0])+' L260,'+(174+r[1])+'" stroke="'+FW+'" stroke-width="10" stroke-linecap="round"/>'}
var MOUTH={
  closed:'<path d="M176,258 Q200,266 224,258" fill="none" stroke="'+FW+'" stroke-width="10" stroke-linecap="round"/>',
  small:'<path d="M180,248 L220,248 Q218,270 200,270 Q182,270 180,248 Z" fill="'+FW+'"/>',
  talk:'<path d="M172,244 L228,244 Q226,282 200,282 Q174,282 172,244 Z" fill="'+FW+'"/>',
  wide:'<path d="M162,240 L238,240 Q234,292 200,292 Q166,292 162,240 Z" fill="'+FW+'"/>',
  o:'<ellipse cx="200" cy="264" rx="18" ry="22" fill="'+FW+'"/>',
  ee:'<path d="M166,248 L234,248 Q230,268 200,268 Q170,268 166,248 Z" fill="'+FW+'"/>',
  frown:'<path d="M176,272 Q200,252 224,272" fill="none" stroke="'+FW+'" stroke-width="10" stroke-linecap="round"/>',
  wavy:'<path d="M170,264 q10,-10 20,0 t20,0 t20,0" fill="none" stroke="'+FW+'" stroke-width="9" stroke-linecap="round"/>',
  smirk:'<path d="M182,262 Q206,268 226,250" fill="none" stroke="'+FW+'" stroke-width="10" stroke-linecap="round"/>'
};
function face(expr,mouth,blink){var e='',m=MOUTH[mouth||'talk'];
  if(expr==='neutral'){e=eyesPill(0,0)+brows([2,-2],[-2,2])}
  else if(expr==='up'){e='<path d="M158,184 L182,226 L134,226 Z" fill="'+C.up+'"/><path d="M242,184 L266,226 L218,226 Z" fill="'+C.up+'"/>'+brows([-8,-14],[-14,-8]);m=MOUTH[mouth||'wide']}
  else if(expr==='down'){e='<path d="M134,190 L182,190 L158,232 Z" fill="'+C.down+'"/><path d="M218,190 L266,190 L242,232 Z" fill="'+C.down+'"/>'+brows([8,-4],[-4,8]);m=MOUTH[mouth||'frown']}
  else if(expr==='worried'){e=eyesPill(0,6,32)+brows([6,-10],[-10,6]);m=MOUTH[mouth||'wavy']}
  else if(expr==='shock'){e='<circle cx="158" cy="206" r="22" fill="'+FW+'"/><circle cx="242" cy="206" r="22" fill="'+FW+'"/><circle cx="158" cy="206" r="8" fill="#000"/><circle cx="242" cy="206" r="8" fill="#000"/>'+brows([-18,-20],[-20,-18]);m=MOUTH[mouth||'o']}
  else if(expr==='think'){e=eyesPill(12,-10,32)+'<path d="M140,168 L178,164" stroke="'+FW+'" stroke-width="10" stroke-linecap="round"/><path d="M224,158 Q242,146 260,158" fill="none" stroke="'+FW+'" stroke-width="10" stroke-linecap="round"/>';m=MOUTH[mouth||'smirk']}
  else if(expr==='wink'){e='<path d="M140,212 Q158,192 176,212" fill="none" stroke="'+FW+'" stroke-width="11" stroke-linecap="round"/><rect x="228" y="188" width="28" height="38" rx="12" fill="'+FW+'"/>'+brows([0,-2],[-4,0]);m=MOUTH[mouth||'ee']}
  else if(expr==='dollar'){e='<text x="158" y="232" text-anchor="middle" font-family="Red Hat Display" font-weight="900" font-size="64" fill="'+C.up+'">$</text><text x="242" y="232" text-anchor="middle" font-family="Red Hat Display" font-weight="900" font-size="64" fill="'+C.up+'">$</text>';m=MOUTH[mouth||'wide']}
  if(blink&&/neutral|worried|think|wink/.test(expr)){e=e.replace(/<rect x="(\d+(?:\.\d+)?)" y="[\d.]+" width="28" height="\d+" rx="12"/g,function(_,x){return '<rect x="'+x+'" y="204" width="28" height="9" rx="4.5"'})}
  return e+m}
function arm(pose,JK){var sl='stroke="'+JK+'" stroke-width="50" stroke-linecap="round" stroke-linejoin="round" fill="none"';
  function glove(x,y,rot,kind){var g='<g transform="translate('+x+','+y+') rotate('+rot+')">';
    if(kind==='point')g+='<rect x="-72" y="-11" width="58" height="20" rx="10" fill="#fff"/><circle cx="0" cy="0" r="27" fill="#fff"/><rect x="-30" y="-34" width="30" height="16" rx="8" fill="#fff" transform="rotate(-20 -15 -26)"/><path d="M-18,6 q8,6 18,4 M-16,14 q8,6 18,4" stroke="#C5CBE0" stroke-width="3" fill="none" stroke-linecap="round"/>';
    else if(kind==='palm')g+='<circle cx="0" cy="0" r="27" fill="#fff"/><rect x="-26" y="-40" width="14" height="30" rx="7" fill="#fff"/><rect x="-10" y="-48" width="14" height="36" rx="7" fill="#fff"/><rect x="6" y="-44" width="14" height="32" rx="7" fill="#fff"/><rect x="20" y="-24" width="13" height="26" rx="6.5" fill="#fff" transform="rotate(30 26 -10)"/>';
    else if(kind==='thumb')g+='<rect x="-24" y="-18" width="48" height="44" rx="16" fill="#fff"/><rect x="-10" y="-58" width="20" height="46" rx="10" fill="#fff"/><path d="M-20,0 h40 M-20,12 h40" stroke="#C5CBE0" stroke-width="3"/>';
    else g+='<circle cx="0" cy="0" r="27" fill="#fff"/>';
    return g+'</g>'}
  if(pose==='point')return '<path d="M318,420 L382,340 L378,236" '+sl+'/>'+glove(378,224,28,'point');
  if(pose==='pointL')return '<path d="M82,420 L18,340 L22,236" '+sl+'/>'+glove(22,224,20,'point');
  if(pose==='present')return '<path d="M82,420 L30,372 L22,300" '+sl+'/>'+glove(22,290,-12,'palm');
  if(pose==='think')return '<path d="M312,430 L292,372 L262,346" '+sl+'/>'+glove(250,340,-30,'fist');
  if(pose==='thumb')return '<path d="M318,420 L380,360 L372,290" '+sl+'/>'+glove(372,280,0,'thumb');
  if(pose==='shrug')return '<path d="M82,420 L26,380 L10,320" '+sl+'/>'+glove(10,310,-30,'palm')+'<path d="M318,420 L374,380 L390,320" '+sl+'/>'+glove(390,310,30,'palm');
  return ''}
function ticker(o){o=o||{};var id='t'+(uid++),expr=o.expr||'neutral',JK=o.jacket||C.navy,LP='#060920';
  var body='<path d="M72,410 Q72,372 112,362 L162,346 L238,346 L288,362 Q328,372 328,410 L350,600 L50,600 Z" fill="'+JK+'"/>'+
  '<polygon points="162,346 238,346 200,446" fill="#fff"/>'+
  '<polygon points="189,350 211,350 215,370 185,370" fill="'+C.cobalt+'"/><polygon points="185,370 215,370 225,446 203,470 179,446" fill="'+C.cobalt+'"/>'+
  '<g fill="#fff" opacity=".85"><circle cx="196" cy="392" r="2.4"/><circle cx="206" cy="404" r="2.4"/><circle cx="196" cy="416" r="2.4"/><circle cx="206" cy="428" r="2.4"/><circle cx="198" cy="440" r="2.4"/></g>'+
  '<polygon points="162,346 200,446 176,478 138,372" fill="'+LP+'"/><polygon points="238,346 200,446 224,478 262,372" fill="'+LP+'"/>'+
  '<rect x="252" y="402" width="40" height="28" rx="5" fill="'+C.cobalt+'"/><text x="272" y="422" text-anchor="middle" font-family="Red Hat Mono" font-weight="600" font-size="16" fill="#fff">FP</text>'+
  '<circle cx="200" cy="520" r="6" fill="'+LP+'"/><circle cx="200" cy="560" r="6" fill="'+LP+'"/>';
  var s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="'+(o.vb||'-20 20 440 580')+'" '+(o.attrs||'')+'><defs>'+
  '<clipPath id="'+id+'c"><rect x="108" y="148" width="184" height="152" rx="22"/></clipPath>'+
  '<pattern id="'+id+'d" width="9" height="9" patternUnits="userSpaceOnUse" x="108" y="148"><circle cx="4.5" cy="4.5" r="3.3" fill="#fff"/></pattern>'+
  '<mask id="'+id+'m" maskUnits="userSpaceOnUse" x="100" y="140" width="200" height="170"><rect x="100" y="140" width="200" height="170" fill="url(#'+id+'d)"/></mask>'+
  '<filter id="'+id+'g" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2.6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'+
  (o.outline?'<filter id="'+id+'o" x="-10%" y="-10%" width="120%" height="120%"><feMorphology in="SourceAlpha" operator="dilate" radius="'+o.outline+'" result="d"/><feFlood flood-color="'+(o.outlineColor||'#fff')+'"/><feComposite in2="d" operator="in" result="ol"/><feMerge><feMergeNode in="ol"/><feMergeNode in="SourceGraphic"/></feMerge></filter>':'')+
  '</defs><g '+(o.outline?'filter="url(#'+id+'o)"':'')+'>'+body+
  '<rect x="186" y="318" width="28" height="36" fill="#C4CCEE"/>'+
  '<path d="M184,136 L140,70" stroke="'+C.casing+'" stroke-width="7" stroke-linecap="round"/><path d="M216,136 L268,60" stroke="'+C.casing+'" stroke-width="7" stroke-linecap="round"/>'+
  '<circle cx="140" cy="68" r="11" fill="'+C.casing+'"/><circle cx="268" cy="58" r="11" fill="'+(o.antenna||C.up)+'"/>'+
  '<path d="M170,136 Q200,108 230,136 Z" fill="'+C.casing2+'"/>'+
  '<g transform="rotate('+(o.tilt||0)+' 200 230)">'+
  '<rect x="88" y="130" width="224" height="204" rx="36" fill="'+C.casing+'"/>'+
  '<path d="M88,290 L312,290 L312,298 Q312,334 276,334 L124,334 Q88,334 88,298 Z" fill="'+C.casing2+'"/>'+
  '<text x="200" y="323" text-anchor="middle" font-family="Red Hat Mono" font-weight="600" font-size="19" fill="'+C.cobalt+'" letter-spacing="2">FP·TV</text>'+
  '<circle cx="288" cy="314" r="6" fill="'+(o.flash?C.down:C.up)+'"/><circle cx="112" cy="314" r="3" fill="#8C97C2"/><circle cx="124" cy="314" r="3" fill="#8C97C2"/>'+
  '<rect x="104" y="144" width="192" height="160" rx="26" fill="#B9C3EA"/>'+
  '<rect x="108" y="148" width="184" height="152" rx="22" fill="'+(o.screen||'#070B24')+'"/>'+
  '<g clip-path="url(#'+id+'c)"><rect x="108" y="148" width="184" height="152" fill="url(#'+id+'d)" opacity=".09"/>'+
  '<g mask="url(#'+id+'m)" filter="url(#'+id+'g)">'+face(expr,o.mouth,o.blink)+'</g>'+
  '<path d="M108,148 L210,148 L150,300 L108,300 Z" fill="#fff" opacity=".05"/></g>'+
  '</g>'+arm(o.pose,JK)+'</g></svg>';
  return s}

/* ---------- Alternates ---------- */
function bullet(o){o=o||{};var id='b'+(uid++),expr=o.expr||'neutral',HEAD='#26305E',SN='#3A4580',HORN='#F2F4FF',JK=C.navy;
  var eyes=expr==='up'?'<path d="M150,214 L168,184 L186,214 Z" fill="'+C.up+'"/><path d="M214,214 L232,184 L250,214 Z" fill="'+C.up+'"/>':'<ellipse cx="166" cy="206" rx="16" ry="19" fill="#fff"/><ellipse cx="234" cy="206" rx="16" ry="19" fill="#fff"/><circle cx="169" cy="209" r="8" fill="#070B24"/><circle cx="237" cy="209" r="8" fill="#070B24"/>';
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="'+(o.vb||'-20 20 440 580')+'" '+(o.attrs||'')+'><defs><filter id="'+id+'o" x="-10%" y="-10%" width="120%" height="120%"><feMorphology in="SourceAlpha" operator="dilate" radius="'+(o.outline||0.01)+'" result="d"/><feFlood flood-color="#fff"/><feComposite in2="d" operator="in" result="ol"/><feMerge><feMergeNode in="ol"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><g filter="url(#'+id+'o)">'+
  '<path d="M72,410 Q72,372 112,362 L162,346 L238,346 L288,362 Q328,372 328,410 L350,600 L50,600 Z" fill="'+JK+'"/><polygon points="162,346 238,346 200,446" fill="#fff"/><polygon points="185,352 215,352 225,446 203,470 179,446" fill="'+C.cobalt+'"/><polygon points="162,346 200,446 176,478 138,372" fill="#060920"/><polygon points="238,346 200,446 224,478 262,372" fill="#060920"/>'+
  '<rect x="180" y="300" width="40" height="54" fill="'+HEAD+'"/>'+
  '<path d="M128,176 Q70,176 52,104 Q60,96 70,104 Q92,146 140,150 Z" fill="'+HORN+'"/><path d="M272,176 Q330,176 348,104 Q340,96 330,104 Q308,146 260,150 Z" fill="'+HORN+'"/>'+
  '<ellipse cx="104" cy="196" rx="30" ry="14" fill="'+HEAD+'" transform="rotate(-20 104 196)"/><ellipse cx="296" cy="196" rx="30" ry="14" fill="'+HEAD+'" transform="rotate(20 296 196)"/>'+
  '<path d="M128,150 Q200,128 272,150 Q296,210 282,262 Q270,300 200,300 Q130,300 118,262 Q104,210 128,150 Z" fill="'+HEAD+'"/>'+
  '<path d="M146,182 L184,188" stroke="#fff" stroke-width="6" stroke-linecap="round"/><path d="M216,188 L254,182" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'+eyes+
  '<ellipse cx="200" cy="280" rx="68" ry="46" fill="'+SN+'"/><ellipse cx="176" cy="276" rx="9" ry="13" fill="#070B24"/><ellipse cx="224" cy="276" rx="9" ry="13" fill="#070B24"/>'+
  '<path d="M170,302 Q200,320 230,302" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'+(o.pose?arm(o.pose,JK):'')+'</g></svg>'}
function dot(o){o=o||{};var id='d'+(uid++);
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" '+(o.attrs||'')+'><defs><radialGradient id="'+id+'r" cx=".38" cy=".32" r=".75"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".7" stop-color="#E4EAFF"/><stop offset="1" stop-color="#B9C6FF"/></radialGradient><filter id="'+id+'g" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="18"/></filter></defs>'+
  '<circle cx="200" cy="210" r="150" fill="#fff" opacity=".35" filter="url(#'+id+'g)"/>'+
  '<circle cx="200" cy="210" r="130" fill="url(#'+id+'r)"/>'+
  '<rect x="152" y="160" width="26" height="44" rx="13" fill="'+C.navy+'"/><rect x="222" y="160" width="26" height="44" rx="13" fill="'+C.navy+'"/><circle cx="160" cy="170" r="5" fill="#fff"/><circle cx="230" cy="170" r="5" fill="#fff"/>'+
  '<path d="M160,240 Q200,280 240,240" fill="none" stroke="'+C.navy+'" stroke-width="12" stroke-linecap="round"/>'+
  '<ellipse cx="128" cy="232" rx="16" ry="9" fill="#8FA6FF" opacity=".6"/><ellipse cx="272" cy="232" rx="16" ry="9" fill="#8FA6FF" opacity=".6"/>'+
  '<path d="M70,230 Q40,210 44,176" fill="none" stroke="#fff" stroke-width="18" stroke-linecap="round"/><path d="M330,230 Q364,214 360,180" fill="none" stroke="#fff" stroke-width="18" stroke-linecap="round"/>'+
  '<path d="M200,80 L200,52" stroke="#fff" stroke-width="8" stroke-linecap="round"/><circle cx="200" cy="44" r="12" fill="'+C.up+'"/></svg>'}
