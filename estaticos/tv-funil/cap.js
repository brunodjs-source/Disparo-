// uso: node cap.js [segundos de teste...]  (sem argumentos renderiza o loop inteiro em quadros/)
const{chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs');
(async()=>{const shots=process.argv.slice(2).map(Number);const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1920,height:1080}});p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file://'+__dirname+'/tv.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const fr=shots.length?shots.map(s=>Math.round(s*30)):[...Array(24*30).keys()];fs.mkdirSync(__dirname+'/quadros',{recursive:true});
for(const f of fr){await p.evaluate(t=>render(t),f/30);await p.screenshot({path:shots.length?`${__dirname}/teste_${f}.jpg`:`${__dirname}/quadros/${String(f).padStart(4,'0')}.jpg`,type:'jpeg',quality:94})}
await b.close();console.log('ok',fr.length)})();
