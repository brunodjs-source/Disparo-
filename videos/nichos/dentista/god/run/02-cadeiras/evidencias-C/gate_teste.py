# Cadeira C, 21/10/2026. Teste: expansor guiado pelos tempos do words-raw.json no voz_master.wav.
# Mede a distancia fala x pausa pelo mesmo metodo do DR02 (RMS das 79 palavras x RMS das pausas >= 0,3 s, -50 ms de cada borda).
import json, wave, sys, numpy as np
S='/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/dent/'
G='/home/user/Disparo-/videos/nichos/dentista/god/'
def rd(p):
    w=wave.open(p); n=w.getnframes(); sr=w.getframerate(); ch=w.getnchannels(); sw=w.getsampwidth()
    a=np.frombuffer(w.readframes(n),dtype={2:np.int16,4:np.int32}[sw]).astype(np.float64)
    a=a.reshape(-1,ch).mean(1)/ (32768.0 if sw==2 else 2147483648.0); return a,sr
words=json.load(open(G+'words-raw.json'))['voz_master.wav']
def db(x): return 20*np.log10(np.sqrt(np.mean(x**2))+1e-12)
def medir(a,sr):
    fala=np.concatenate([a[int(s*sr):int(e*sr)] for s,e,_ in words])
    pausas=[]
    for i in range(len(words)-1):
        s=words[i][1]; e=words[i+1][0]
        if e-s>=0.3: pausas.append((s+0.05,e-0.05))
    pd=[db(a[int(s*sr):int(e*sr)]) for s,e in pausas]
    return db(fala), pausas, pd
def gate(a,sr,att_db=-20,tail=0.08,pre=0.03,ramp=0.02):
    g=np.full(len(a),10**(att_db/20))
    for s,e,_ in words:
        i0=max(0,int((s-pre)*sr)); i1=min(len(a),int((e+tail)*sr)); g[i0:i1]=1.0
    k=int(ramp*sr); win=np.hanning(2*k+1); win/=win.sum()
    g=np.convolve(g,win,mode='same'); return a*g
for nome in ['raw.wav','rn_bd.wav','voz_master.wav']:
    a,sr=rd(S+nome); f,p,pd=medir(a,sr)
    print(nome,'sr',sr,'fala %.1f dBFS'%f,'pausas',['%.1f'%x for x in pd],'dif media %.1f dB'%(f-np.mean(pd)))
a,sr=rd(S+'voz_master.wav')
# o que ha nas pausas suspeitas (DR02/B03): RMS em passos de 40 ms
for s,e in [(13.32,13.84),(31.58,32.00),(19.50,20.10)]:
    seg=[('%.2f'%(s+i*0.04),'%.1f'%db(a[int((s+i*0.04)*sr):int((s+(i+1)*0.04)*sr)])) for i in range(int((e-s)/0.04))]
    print('pausa',s,e,seg)
for att in (-12,-20,-30):
    b=gate(a,sr,att); f,p,pd=medir(b,sr)
    print('gate',att,'fala %.1f'%f,'pausas',['%.1f'%x for x in pd],'dif media %.1f dB'%(f-np.mean(pd)),'pior %.1f'%(f-max(pd)))
    if att==-20:
        out=(np.clip(b,-1,1)*32767).astype(np.int16)
        w=wave.open(G+'run/02-cadeiras/evidencias-C/voz_gate20.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(out.tobytes()); w.close()
