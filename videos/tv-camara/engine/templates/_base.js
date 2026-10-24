// Biblioteca comum dos formatos da entrevista (injetada em cada template).
// Tudo é função do tempo t (render determinístico, sem relógio, sem aleatório sem semente).
const C = __DATA__;                         // dados do corte (palavras, tempos, textos)
const W = C.w || 1080, H = C.h || 1920;
const cl = x => Math.max(0, Math.min(1, x));
const eo = x => 1 - Math.pow(1 - cl(x), 3);
const eio = x => { x = cl(x); return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
const back = x => { x = cl(x); const c = 1.4; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); };
const mola = x => { x = cl(x); return 1 - Math.exp(-6 * x) * Math.cos(9 * x); };       // mola amortecida
const vis = (t, a, b, fi = .25, fo = .25) => cl((t - a) / fi) * (1 - cl((t - b) / fo));
let _s = 7; const rnd = () => { _s = (_s * 16807) % 2147483647; return _s / 2147483647; };
const OURO = '#E8B36A', OURO2 = '#F5C46E', CREME = '#F3EDE2', ESC = '#141210';
const FONTS = `@font-face{font-family:Cinzel;src:url(/home/user/Disparo-/videos/ads/a01-campinas/fonts/cinzel-latin.woff2)}
@font-face{font-family:Pf;src:url(/home/user/Disparo-/videos/ads/a01-campinas/fonts/playfair-italic-latin.woff2);font-style:italic}`;
document.head.insertAdjacentHTML('beforeend', `<style>${FONTS}
html,body{margin:0;background:transparent;width:${W}px;height:${H}px;overflow:hidden;font-family:"Inter Display","Inter",sans-serif}
#back,#front{position:absolute;inset:0}
.cap{position:absolute;left:70px;right:110px;text-align:center;line-height:1.05}
.cap .bx{display:inline-block;padding:14px 26px 18px;border-radius:18px;background:rgba(20,18,16,.82)}
.cap .big{display:block;font-weight:900;font-size:86px;color:#fff;letter-spacing:-.01em;text-transform:uppercase}
.cap .sm{display:block;font-family:Pf;font-style:italic;font-size:46px;color:${OURO2};margin-top:4px}
.L{position:absolute;left:0;right:0;text-align:center;font-family:Cinzel;font-weight:900;letter-spacing:.02em;line-height:.92;perspective:1000px}
.L span{display:inline-block;transform-origin:50% 100%;position:relative}
.pill{position:absolute;left:0;right:0;text-align:center}
.pill div{display:inline-block;background:rgba(20,18,16,.86);border:2px solid rgba(232,179,106,.55);color:${CREME};border-radius:22px;padding:16px 30px;font-weight:800;font-size:40px;line-height:1.15}
.lt{position:absolute;left:60px;background:rgba(20,18,16,.9);border-left:8px solid ${OURO};padding:16px 28px;border-radius:14px;color:${CREME}}
.lt b{display:block;font-size:42px;font-weight:900}.lt i{font-family:Pf;font-size:32px;color:${OURO}}
</style>`);
document.body.innerHTML = '<div id="back"></div><div id="front"></div>';

// palavras do corte: [t_rel, texto, falante('B'|'M')]
const WD = (C.words || []);
const PRINC = new Set((C.destaques || []).map(x => x.toLowerCase()));
// grupos de 1 a 3 palavras para a Legenda Gigante; a palavra principal é a mais longa (ou um destaque)
const GRUPOS = (() => { const g = []; let cur = [];
  WD.forEach((w, i) => { cur.push(i); const nx = WD[i + 1];
    if (cur.length >= 3 || /[.,!?;:]$/.test(w[1]) || (nx && nx[0] - w[0] > .7) || (nx && nx[2] !== w[2])) { g.push(cur); cur = []; } });
  if (cur.length) g.push(cur); return g; })();
function legendaGigante(t, top, opts = {}) {
  let gi = -1; for (let k = 0; k < GRUPOS.length; k++) if (WD[GRUPOS[k][0]][0] - .03 <= t) gi = k;
  if (gi < 0) return '';
  const gr = GRUPOS[gi], last = WD[gr[gr.length - 1]], nx = GRUPOS[gi + 1];
  if (t > last[0] + .9 && (!nx || t < WD[nx[0]][0] - .03)) return '';
  const pal = gr.map(i => WD[i]); const limpa = s => s.replace(/[.,!?;:]/g, '');
  let pi = pal.reduce((b, w, k) => (PRINC.has(limpa(w[1]).toLowerCase()) ? k : b), -1);
  if (pi < 0) pi = pal.reduce((b, w, k) => limpa(w[1]).length > limpa(pal[b][1]).length ? k : b, 0);
  const t0 = pal[0][0], p = cl((t - t0) / .1), sc = 1.04 - .04 * p;
  const outras = pal.filter((_, k) => k !== pi).map(w => w[1]).join(' ');
  const quem = pal[0][2] === 'M' ? `<span style="display:block;font-size:22px;letter-spacing:.2em;color:#cfc6b6;margin-bottom:6px">REPÓRTER</span>` : '';
  return `<div class=cap style="top:${top}px;transform:scale(${sc})"><span class=bx style="${opts.bx || ''}">${quem}<span class=big style="${opts.big || ''}">${limpa(pal[pi][1])}</span>${outras ? `<span class=sm>${outras}</span>` : ''}</span></div>`;
}
// Connect Hook: texto entrando palavra por palavra no topo, palavra-chave em ouro
function connectHook(t, a, texto, chave, top = 220, linha = '') {
  const ws = texto.split(' '); if (t < a - .05) return '';
  const fora = 1 - cl((t - (a + ws.length * .15 + 2.2)) / .3);
  return `<div style="position:absolute;left:80px;right:120px;top:${top}px;text-align:center;opacity:${fora}">${linha ? `<div style="font-size:26px;letter-spacing:.18em;color:#d8cfc0;margin-bottom:10px;opacity:${cl((t - a) / .2)}">${linha}</div>` : ''}` +
    ws.map((w, i) => { const p = mola((t - a - i * .15) / .45); const k = w.replace(/[.,!?]/g, '').toLowerCase() === (chave || '').toLowerCase();
      return `<span style="display:inline-block;margin:0 9px;font-weight:900;font-size:70px;color:${k ? OURO2 : '#fff'};text-shadow:0 4px 18px rgba(0,0,0,.7);opacity:${cl(p * 3)};transform:translateY(${(1 - p) * 40}px) scale(${.8 + .2 * p})">${w}</span>`; }).join('') + '</div>';
}
// letreiro 3D atrás das pessoas (camada back); base em y (px)
const ext = (n, c) => [...Array(n)].map((_, k) => `${k * 1.2}px ${k * 1.8}px 0 ${c}`).join(',');
function letreiro(t, l) {   // l={a,b,txt,col,size,y}
  if (t < l.a - .02 || t > l.b + .45) return '';
  const p = back((t - l.a) / .55), out = eio((t - l.b) / .4);
  return `<div class=L style="top:${l.y}px;font-size:${l.size}px;color:${l.col || '#fff'};transform:translateY(-100%)"><span style="transform:translateY(${(1 - p) * 300 + out * 320}px) rotateX(${(1 - p) * 55 - out * 30}deg) scale(${.86 + .14 * p});text-shadow:${ext(14, 'rgba(60,40,15,.9)')},0 30px 60px rgba(0,0,0,.55)">${l.txt}</span></div>`;
}
// Nome e cargo: traço cresce antes do texto
function nomeCargo(t, a, b, top, nome = 'Bruno', cargo = 'Estrategista de Lançamento') {
  const o = vis(t, a, b, .3, .3); if (!o) return '';
  const tr = eo((t - a) / .35), tx = eo((t - a - .2) / .4);
  return `<div style="position:absolute;left:60px;top:${top}px;opacity:${o}"><div style="height:6px;width:${tr * 340}px;background:${OURO};border-radius:3px;margin-bottom:10px"></div><div style="opacity:${tx};transform:translateX(${(1 - tx) * -30}px);color:#fff;text-shadow:0 3px 12px rgba(0,0,0,.8)"><b style="display:block;font-size:46px;font-weight:900">${nome}</b><i style="font-family:Pf;font-size:34px;color:${OURO2}">${cargo}</i></div></div>`;
}
// selo fixo "Entrevista à TV Câmara Campinas" (texto, sem logo da emissora)
function seloTV(t, a, top = 130, extra = '') {
  const o = cl((t - a) / .3); if (!o) return '';
  return `<div class=pill style="top:${top}px;opacity:${o}"><div style="font-size:28px;letter-spacing:.06em;padding:10px 22px">Entrevista à TV Câmara Campinas${extra}</div></div>`;
}
// CTA de Comentário: caixa genérica digitando, botão acende no fim
function ctaComentario(t, a, texto, linha1 = 'Comenta aqui', linha2 = '', top = 1180) {
  if (t < a) return '';
  const p = back((t - a) / .45), n = Math.floor(cl((t - a - .3) / (texto.length / 16)) * texto.length), on = n >= texto.length;
  const cur = Math.floor(t * 2.5) % 2 ? '|' : '&nbsp;';
  return `<div style="position:absolute;left:80px;right:120px;top:${top}px;transform:scale(${.85 + .15 * p});opacity:${cl(p * 2)}"><div style="display:flex;align-items:center;gap:20px;background:#fff;border-radius:40px;padding:18px 22px;box-shadow:0 18px 40px rgba(0,0,0,.35)"><i style="width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,${OURO2},#9A5F2A);flex:none"></i><span style="flex:1;font-size:40px;font-weight:800;color:${ESC}">${texto.slice(0, n)}<span style="color:#C48C34">${on ? '' : cur}</span></span><i style="width:60px;height:60px;border-radius:50%;background:${on ? OURO : '#ddd'};flex:none;transform:translateY(${on ? 2 : 0}px)"></i></div>
  <div style="text-align:center;margin-top:18px;color:#fff;font-size:34px;font-weight:700;text-shadow:0 3px 12px #000;opacity:${cl((t - a - 1) / .3)}">${linha1}${linha2 ? `<br><span style="font-family:Pf;font-style:italic;color:${OURO2};font-weight:400">${linha2}</span>` : ''}</div></div>`;
}
// Marca-texto atrás de uma palavra (usado dentro de textos próprios)
const marca = (t, a, palavra, cor = OURO) => `<span style="position:relative;display:inline-block"><i style="position:absolute;left:-6px;bottom:6%;height:42%;width:${eo((t - a) / .3) * 104}%;background:${cor};opacity:.85;border-radius:6px;z-index:-1"></i>${palavra}</span>`;
// barra de progresso fina no topo
const progresso = (t, cor = OURO) => `<div style="position:absolute;left:0;top:0;height:6px;width:${cl(t / C.dur) * W}px;background:${cor}"></div>`;
