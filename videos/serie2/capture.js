// uso: node capture.js r1-caixa [segundos para prints...]
const{chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs'),{spawn}=require('child_process');
const id=process.argv[2],dir=__dirname+'/'+id;
const html=fs.readFileSync(__dirname+'/modelo.html','utf8').replace('__TIMELINE__',fs.readFileSync(dir+'/timeline.json','utf8'));fs.writeFileSync(__dirname+'/_'+id+'.html',html);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.error('ERR',e.message));await p.goto('file://'+__dirname+'/_'+id+'.html');await p.evaluate(()=>document.fonts.ready);
const shots=process.argv.slice(3).map(Number),total=await p.evaluate(()=>TOTAL);
if(shots.length){for(const s of shots){await p.evaluate(t=>render(t),s);await p.screenshot({path:`${dir}/print_${s}.png`})}await b.close();return}
const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-i',dir+'/voz.wav','-c:v','libx264','-crf','19','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest',dir+'/sem-trilha.mp4'],{stdio:['pipe','inherit','inherit']});
for(let f=0;f<Math.floor(total*30);f++){await p.evaluate(t=>render(t),f/30);const buf=await p.screenshot({type:'jpeg',quality:92});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log(id,'ok')})();
