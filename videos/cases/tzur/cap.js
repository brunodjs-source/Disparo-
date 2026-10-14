const{chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs');
(async()=>{const html=fs.readFileSync('ov.html','utf8').replace('__EDIT__',fs.readFileSync('edit.json','utf8'));fs.writeFileSync('_ov.html',html);
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('ERR',e.message));await p.goto('file://'+process.cwd()+'/_ov.html');await p.evaluate(()=>document.fonts.ready);
const shots=process.argv.slice(2).map(Number);fs.mkdirSync('ov',{recursive:true});
if(shots.length){for(const s of shots){await p.evaluate(t=>render(t),s);await p.screenshot({path:`sh_${s}.png`,omitBackground:true})}await b.close();return}
const N=Math.ceil(54.2*30);for(let f=0;f<N;f++){await p.evaluate(t=>render(t),f/30);await p.screenshot({path:`ov/${String(f).padStart(5,'0')}.png`,omitBackground:true})}await b.close()})();
