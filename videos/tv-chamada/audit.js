// Auditoria de texto: percorre o video a 4 quadros por segundo e lista o que vaza da tela.
const {chromium}=require('/opt/node-tools/node_modules/playwright');
const [,,FR,MK,dur]=process.argv;
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});
const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+__dirname+'/u.html?fr='+encodeURIComponent('file://'+FR)+'&mk='+encodeURIComponent('file://'+MK));await p.evaluate(()=>document.fonts.ready);
let n=0;for(let t=0;t<+dur;t+=0.25){const bad=await p.evaluate(t=>audit(t),t);for(const x of bad){console.log(t.toFixed(2)+'s  '+x);n++}}
console.log(n?`${n} problemas`:'auditoria ok: nenhum texto vazando');await b.close()})();
