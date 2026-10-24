// uso: node cap.js  -> story-frase-1.png ... story-frase-9.png (7 a 9: entrevista, sem imagem nem voz da repórter)
const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } }); p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + __dirname + '/s.html'); await p.evaluate(() => document.fonts.ready);
  for (let i = 0; i < 9; i++) { await p.evaluate(i => render(i), i); await p.waitForTimeout(250); await p.screenshot({ path: `${__dirname}/story-frase-${i + 1}.png` }); }
  await b.close(); console.log('ok');
})();
