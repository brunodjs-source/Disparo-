// Captura u.html quadro a quadro. Uso: node capu.js pasta_frames pasta_mascaras saida dur [passo] [inicio]
const {chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs');
const [,,FR,MK,out,dur,step,start]=process.argv;
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+__dirname+'/u.html?fr='+encodeURIComponent('file://'+FR)+'&mk='+encodeURIComponent('file://'+MK));await p.evaluate(()=>document.fonts.ready);
fs.writeFileSync(out+'/events.json',JSON.stringify(await p.evaluate(()=>events())));
const n=Math.round(dur*30),st=+(step||1);for(let i=+(start||0);i<n;i+=st){await p.evaluate(t=>frame(t),i/30);await p.waitForTimeout(10);await p.screenshot({path:`${out}/${String(i).padStart(5,'0')}.jpg`,type:'jpeg',quality:95})}
await b.close()})();
