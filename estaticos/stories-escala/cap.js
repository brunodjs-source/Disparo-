const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
const n=process.argv[2],fps=24,D=10;await p.goto('file://'+__dirname+'/s.html?n='+n);await p.waitForTimeout(500);
require('fs').mkdirSync('/tmp/fr'+n,{recursive:true});
for(let f=0;f<fps*D;f++){await p.evaluate(t=>render(t),f/fps);await p.screenshot({path:`/tmp/fr${n}/${String(f).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});}
await p.evaluate(()=>render(10));await p.screenshot({path:__dirname+`/story-${n}.png`});await b.close();})();
