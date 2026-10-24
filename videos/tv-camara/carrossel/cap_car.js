// uso: node cap_car.js car01.html PASTA_COM_FUNDOS  -> lamina-1.png ... lamina-6.png (1080x1350) na pasta
const { chromium } = require('/opt/node-tools/node_modules/playwright'); const fs = require('fs'), path = require('path');
(async () => {
  const [html, dir] = process.argv.slice(2); const dst = path.join(dir, path.basename(html)); fs.copyFileSync(html, dst);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 6480, height: 1350 } }); p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + dst); await p.waitForSelector('body[data-pronto]'); await p.waitForTimeout(400);
  for (let i = 0; i < 6; i++) await p.screenshot({ path: path.join(dir, `lamina-${i + 1}.png`), clip: { x: i * 1080, y: 0, width: 1080, height: 1350 } });
  await b.close(); console.log('ok');
})();
