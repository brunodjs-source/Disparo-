// uso: node cap.js MODELO SAIDA [quadros de teste...]
// Renderiza as camadas back (letreiro atrás da pessoa) e front (legenda, painel, CTA) quadro a quadro em PNG com alfa.
const{chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs'),path=require('path');
(async()=>{const[M,OUT,...shots]=process.argv.slice(2);const D=__dirname;
const html=fs.readFileSync(D+'/dent.html','utf8').replace('__WORDS__',fs.readFileSync(D+'/../words.json','utf8')).replace('__HT__',fs.readFileSync(D+'/headtop.json','utf8'));
fs.writeFileSync(D+'/_dent.html',html);fs.mkdirSync(OUT+'/back',{recursive:true});fs.mkdirSync(OUT+'/front',{recursive:true});
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('ERR',e.message));await p.goto('file://'+D+'/_dent.html?m='+M);await p.evaluate(()=>document.fonts.ready);
const N=1093,fr=shots.length?shots.map(Number):[...Array(N).keys()];const t0=Date.now();
for(const f of fr)for(const L of['back','front']){await p.evaluate(([t,l])=>render(t,l),[f/30,L]);await p.screenshot({path:`${OUT}/${L}/${String(f).padStart(5,'0')}.png`,omitBackground:true})}
await b.close();console.log('ok',fr.length,'quadros',((Date.now()-t0)/1000).toFixed(1),'s')})();
