// Captura o estatico e confere se algum texto passa da borda segura (40 px) ou estoura a caixa.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1920}});const pg=process.argv[2]||'estatico.html',outp=process.argv[3]||'estatico-dj-story.png';await p.goto('file://'+__dirname+'/'+pg);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const bad=await p.evaluate(()=>{const o=[];document.querySelectorAll('.hl,.q,.cap,.kick,.mh .n,.mh .d,.top .x').forEach(e=>{const r=document.createRange();r.selectNodeContents(e);for(const c of r.getClientRects())if(c.left<40||c.right>1040)o.push(e.textContent.slice(0,30)+' borda');if(e.scrollWidth>e.clientWidth+2)o.push(e.textContent.slice(0,30)+' estoura')});
 const pg=document.querySelector('.page').getBoundingClientRect(),q=document.querySelector('.q').getBoundingClientRect();if(q.bottom>pg.bottom-20)o.push('citacao passa da pagina');
 // carimbo e logo nao podem cobrir texto
 const txt=[...document.querySelectorAll('.hl,.q,.cap,.kick,.mh .n,.mh .d,.page>div:last-child')];
 for(const sel of ['.stamp','.globe']){const a=document.querySelector(sel).getBoundingClientRect();
  for(const e of txt){const r=document.createRange();r.selectNodeContents(e);for(const c of r.getClientRects())if(!(c.right<a.left||c.left>a.right||c.bottom<a.top||c.top>a.bottom))o.push(sel+' cobre '+e.textContent.slice(0,25))}}
 return [...new Set(o)]});
console.log(bad.length?bad.join('\n'):'auditoria ok');
await (await p.$('#story')).screenshot({path:__dirname+'/saidas/'+outp});await b.close()})();
