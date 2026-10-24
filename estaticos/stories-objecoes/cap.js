// uso: node cap.js [id ...]  -> png/ID.png para cada item de conteudo/stories-objecoes/04-estaticos.json, depois folha-1.jpg, folha-2.jpg ...
// (6 por linha, 3 linhas por folha, id embaixo de cada miniatura). Com ids na linha de comando, renderiza só esses e não refaz as folhas.
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs = require('fs'), path = require('path');
const MANIFESTO = path.join(__dirname, '../../conteudo/stories-objecoes/04-estaticos.json');
const PNG = path.join(__dirname, 'png');
(async () => {
  const itens = JSON.parse(fs.readFileSync(MANIFESTO, 'utf8')).itens;
  const so = process.argv.slice(2), lista = so.length ? itens.filter(i => so.includes(i.id)) : itens;
  fs.mkdirSync(PNG, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } }); p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + __dirname + '/so.html'); await p.evaluate(() => document.fonts.ready);
  const rel = [];
  for (const it of lista) {
    const r = await p.evaluate(it => render(it), it);
    await p.waitForTimeout(120);
    await p.screenshot({ path: `${PNG}/${it.id}.png` });
    rel.push(r);
    console.log(`${it.id} ${it.variante.padEnd(5)} ${r.px}px ${r.checagem.linhas_fr} linhas fio=${r.fio} bloco=${r.checagem.bloco} ${r.checagem.ok ? 'OK' : 'ERRO ' + r.checagem.erros.join(' | ')} ${r.ajuste}`);
  }
  if (process.env.REL) fs.writeFileSync(process.env.REL, JSON.stringify(rel, null, 1));
  if (!so.length) {
    // folhas de contato: 6 x 3 por folha
    const POR = 18, W = 270, H = 480;
    for (let f = 0; f * POR < itens.length; f++) {
      const grupo = itens.slice(f * POR, (f + 1) * POR);
      const cel = grupo.map(it => `<div class=c><img src="file://${PNG}/${it.id}.png"><div class=id>${it.id}</div><div class=ds>${it.variante === 'balao' ? 'balão' : it.foto.replace('.jpg', '')}${it.zona_sticker ? ' · zona sticker' : ''}</div></div>`).join('');
      const linhas = Math.ceil(grupo.length / 6);   // a última folha só tem as linhas usadas
      await p.setViewportSize({ width: 6 * W + 7 * 20, height: linhas * (H + 76) + (linhas + 1) * 20 });
      await p.setContent(`<html><body style="margin:0;background:#0b0a09"><style>
        .g{display:grid;grid-template-columns:repeat(6,${W}px);gap:20px;padding:20px}
        .c img{width:${W}px;height:${H}px;display:block;outline:1px solid #3a332b}
        .id{font:700 24px 'DejaVu Sans Mono',monospace;color:#E8B36A;text-align:center;height:32px;line-height:32px;margin-top:8px;white-space:nowrap}
        .ds{font:400 17px 'DejaVu Sans Mono',monospace;color:#8f877b;text-align:center;height:24px;line-height:24px;white-space:nowrap}
        </style><div class=g>${cel}</div></body></html>`, { waitUntil: 'load' });
      await p.screenshot({ path: path.join(__dirname, `folha-${f + 1}.jpg`), type: 'jpeg', quality: 88 });
      console.log('folha', f + 1, grupo.length);
    }
  }
  const erros = rel.filter(r => !r.checagem.ok), ajustes = rel.filter(r => r.ajuste);
  console.log(`checagem: ${rel.length - erros.length}/${rel.length} sem erro; ${ajustes.length} com frase reduzida`);
  await b.close(); console.log('ok', lista.length);
})();
