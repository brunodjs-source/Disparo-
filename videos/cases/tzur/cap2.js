const{chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs');
(async()=>{fs.writeFileSync('_ov2.html',fs.readFileSync('ov2.html','utf8').replace('__EDIT__',fs.readFileSync('edit.json','utf8')));
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('ERR',e.message));await p.goto('file://'+process.cwd()+'/_ov2.html');await p.evaluate(()=>document.fonts.ready);
const shots=process.argv.slice(2).map(Number);
if(shots.length){for(const s of shots)for(const L of ['back','front']){await p.evaluate(([t,l])=>render(t,l),[s,L]);await p.screenshot({path:`sh2_${L}_${s}.png`,omitBackground:true})}await b.close();return}
for(const L of ['back','front']){fs.mkdirSync('ov2_'+L,{recursive:true});for(let f=0;f<Math.ceil(54.2*30);f++){await p.evaluate(([t,l])=>render(t,l),[f/30,L]);await p.screenshot({path:`ov2_${L}/${String(f).padStart(5,'0')}.png`,omitBackground:true})}}
await b.close();console.log('ok')})();
