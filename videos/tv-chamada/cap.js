// Captura o overlay quadro a quadro com fundo transparente.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
const [,,out,dur]=process.argv;
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+__dirname+'/o.html');await p.evaluate(()=>document.fonts.ready);
const n=Math.round(dur*30);for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/30);await p.screenshot({path:`${out}/${String(i).padStart(5,'0')}.png`,omitBackground:true})}
await b.close()})();
