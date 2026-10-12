// Uso: node build.js [slug ...]   (sem argumentos gera todos)
const path = require('path');
const { chromium } = require('/opt/node-tools/node_modules/playwright');

const SRC = __dirname;
const OUT = path.resolve(SRC, '..');
const ALL = ['checklist', 'pesquisa', 'oferta', 'captacao', 'aquecimento', 'evento', 'carrinho', 'recuperacao', 'perpetuo'];

(async () => {
  const slugs = process.argv.slice(2).length ? process.argv.slice(2) : ALL;
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium',
    args: ['--allow-file-access-from-files'],
  });
  const page = await browser.newPage();
  let problems = 0;
  for (const slug of slugs) {
    await page.goto('file://' + path.join(SRC, slug + '.html'), { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const report = await page.evaluate(() => {
      const out = [];
      document.querySelectorAll('.page').forEach((pg, i) => {
        const inner = pg.querySelector('.inner');
        if (!inner) return;
        const over = inner.scrollHeight - inner.clientHeight;
        let lastBottom = 0;
        inner.querySelectorAll(':scope > *').forEach((el) => {
          const r = el.getBoundingClientRect();
          lastBottom = Math.max(lastBottom, r.bottom);
        });
        const ib = inner.getBoundingClientRect();
        out.push({ page: i + 1, over, free: Math.round(ib.bottom - lastBottom) });
      });
      return { n: document.querySelectorAll('.page').length, pages: out };
    });
    const bad = report.pages.filter((p) => p.over > 1);
    problems += bad.length;
    console.log(`${slug}: ${report.n} paginas`);
    report.pages.forEach((p) =>
      console.log(`   p${p.page}: ${p.over > 1 ? 'OVERFLOW ' + p.over + 'px' : 'ok'}  livre=${p.free}px`)
    );
    await page.pdf({
      path: path.join(OUT, slug + '.pdf'),
      format: 'A4',
      printBackground: true,
      preferCSSPageSize: true,
      margin: { top: 0, right: 0, bottom: 0, left: 0 },
    });
  }
  await browser.close();
  if (problems) console.log(`\n${problems} pagina(s) com overflow`);
})();
