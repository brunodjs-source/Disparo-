const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs = require('fs'), { spawn } = require('child_process');
const html = fs.readFileSync('index.html', 'utf8').replace('__TIMELINE__', fs.readFileSync('timeline.json', 'utf8'));
fs.writeFileSync('_built.html', html);
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => console.error('PAGEERR', e.message));
  await p.goto('file://' + process.cwd() + '/_built.html'); await p.waitForTimeout(800);
  const FPS = 30, total = await p.evaluate(() => TOTAL);
  const shots = process.argv.slice(2).map(Number);
  if (shots.length) { for (const s of shots) { await p.evaluate(t => render(t), s); await p.screenshot({ path: `${process.env.SP}/s04_${s}.png` }); } await b.close(); return; }
  const ff = spawn('ffmpeg', ['-v','error','-y','-f','image2pipe','-framerate',String(FPS),'-c:v','mjpeg','-i','-','-i','voz.wav','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart','story04-aquecimento.mp4'], { stdio: ['pipe','inherit','inherit'] });
  const N = Math.floor(total * FPS);
  for (let f = 0; f < N; f++) { await p.evaluate(t => render(t), f / FPS); const buf = await p.screenshot({ type: 'jpeg', quality: 92 }); if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r)); }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close(); console.log('frames', N);
})();
