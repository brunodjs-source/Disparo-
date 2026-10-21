# Piso de ruido no miolo das pausas >= 0,40 s (corta 100 ms de cada borda), antes e depois do expansor
import json, wave, numpy as np
S='/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/dent/'
G='/home/user/Disparo-/videos/nichos/dentista/god/'
def rd(p):
    w=wave.open(p); a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(float)/32768; return a.reshape(-1,w.getnchannels()).mean(1),w.getframerate()
W=json.load(open(G+'words-raw.json'))['voz_master.wav']
def db(x): return 20*np.log10(np.sqrt(np.mean(x**2))+1e-12)
for p in [S+'voz_master.wav', G+'run/02-cadeiras/evidencias-C/voz_gate20.wav']:
    a,sr=rd(p); r=[]
    for i in range(len(W)-1):
        s,e=W[i][1],W[i+1][0]
        if e-s>=0.40: r.append(('%.2f-%.2f'%(s+.1,e-.1),'%.1f'%db(a[int((s+.1)*sr):int((e-.1)*sr)])))
    print(p.split('/')[-1],r)
