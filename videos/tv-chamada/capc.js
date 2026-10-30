const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+__dirname+'/c.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
for(const id of ['story','feed'])await (await p.$('#'+id)).screenshot({path:`${__dirname}/saidas/criativo-${id}.png`});await b.close()})();
