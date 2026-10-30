// Captura uma camada (back ou front) de j.html quadro a quadro.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
const [,,layer,out,dur,step]=process.argv;
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+__dirname+'/j.html?layer='+layer);await p.evaluate(()=>document.fonts.ready);
const n=Math.round(dur*30),st=+(step||1);for(let i=0;i<n;i+=st){await p.evaluate(t=>render(t),i/30);await p.screenshot({path:`${out}/${String(i).padStart(5,'0')}.png`,omitBackground:layer!=='back'})}
await b.close()})();
