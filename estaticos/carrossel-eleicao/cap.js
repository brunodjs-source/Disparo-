const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto('file://'+__dirname+'/c.html');await p.evaluate(()=>document.fonts.ready);
for(let i=0;i<7;i++){await p.evaluate(i=>render(i),i);await p.waitForTimeout(150);await p.screenshot({path:`${__dirname}/lamina-${i+1}.png`})}await b.close()})();
