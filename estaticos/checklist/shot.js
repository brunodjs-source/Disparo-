const { chromium } = require('/opt/node-tools/node_modules/playwright');
const fs=require('fs');
fs.writeFileSync('_b.html',fs.readFileSync('index.html','utf8').replace('__Q__',fs.readFileSync('q.json','utf8')));
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1350}});p.on('pageerror',e=>console.error(e.message));
await p.goto('file://'+process.cwd()+'/_b.html');await p.waitForTimeout(500);
for(let i=0;i<8;i++){await p.evaluate(i=>show(i),i);await p.waitForTimeout(150);await p.screenshot({path:`slide${i+1}.jpg`,type:'jpeg',quality:95});}
await b.close();fs.unlinkSync('_b.html')})();
