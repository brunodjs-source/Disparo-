// Recaptura so os quadros que faltam. Uso: node capmiss.js pagina saida dur fr ct
const {chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs');
const [,,html,out,dur,FR,CT]=process.argv;
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+__dirname+'/'+html+'?fr='+encodeURIComponent('file://'+FR)+'&ct='+encodeURIComponent('file://'+CT));await p.evaluate(()=>document.fonts.ready);
const n=Math.round(dur*30);let k=0;for(let i=0;i<n;i++){const f=`${out}/${String(i).padStart(5,'0')}.jpg`;if(fs.existsSync(f))continue;await p.evaluate(t=>frame(t),i/30);await p.screenshot({path:f,type:'jpeg',quality:93});k++}
console.log('recapturados',k);await b.close()})();
