// uso: node cap.js corte.json PASTA_CAMADAS [quadros de teste...]
// Renderiza as camadas back (atrás das pessoas) e front quadro a quadro em PNG com alfa.
// O template vem de templates/<fmt>.html e recebe os dados do corte em __DATA__.
const { chromium } = require('/opt/node-tools/node_modules/playwright'); const fs = require('fs'), path = require('path');
(async () => {
  const [CJ, OUT, ...shots] = process.argv.slice(2); const D = __dirname; const C = JSON.parse(fs.readFileSync(CJ, 'utf8'));
  const tpl = fs.readFileSync(path.join(D, 'templates', C.fmt + '.html'), 'utf8')
    .replace('/*__BASE__*/', () => fs.readFileSync(path.join(D, 'templates', '_base.js'), 'utf8'))
    .replace('__DATA__', () => JSON.stringify(C));
  const tmp = path.join(D, `_${C.id}.html`); fs.writeFileSync(tmp, tpl);
  fs.mkdirSync(OUT + '/back', { recursive: true }); fs.mkdirSync(OUT + '/front', { recursive: true });
  const W = C.w || 1080, H = C.h || 1920, N = Math.round(C.dur * 30);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: W, height: H } });
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + tmp); await p.evaluate(() => document.fonts.ready);
  const fr = shots.length ? shots.map(Number) : [...Array(N).keys()]; const t0 = Date.now();
  for (const f of fr) for (const L of (C.back ? ['back', 'front'] : ['front'])) {
    const vazio = await p.evaluate(([t, l]) => render(t, l), [f / 30, L]);
    await p.screenshot({ path: `${OUT}/${L}/${String(f).padStart(5, '0')}.png`, omitBackground: true });
  }
  await b.close(); fs.unlinkSync(tmp); console.log('ok', C.id, fr.length, 'quadros', ((Date.now() - t0) / 1000).toFixed(1), 's');
})();
