# Repete o método DR02 do livro de fatos (RMS da fala nas janelas das 79 palavras contra RMS de pausas >= 0,3 s, 50 ms de borda)
# em voz_master.wav e em E_voz_final.wav, para comparar no mesmo método.
import json, subprocess, numpy as np
S='/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/dent/'
w=json.load(open('/home/user/Disparo-/videos/nichos/dentista/god/words-raw.json'))['voz_master.wav']
pz=[(w[i][1],w[i+1][0]) for i in range(len(w)-1) if w[i+1][0]-w[i][1]>=0.3]
for f in [S+'voz_master.wav','E_voz_final.wav']:
    x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','48000','-f','f32le','-'],capture_output=True,check=True).stdout,np.float32)
    seg=lambda a,b: x[int(a*48000):int(b*48000)]
    fala=np.concatenate([seg(a,b) for a,b,_ in w]); rf=20*np.log10(np.sqrt((fala**2).mean()))
    ps=[20*np.log10(np.sqrt((seg(a+0.05,b-0.05)**2).mean())+1e-9) for a,b in pz]
    print(f.split('/')[-1], 'fala %.1f dBFS'%rf, 'pausas', ' '.join('%.1f'%p for p in ps), '| media fala-pausa %.1f dB, melhor %.1f'%(rf-np.mean(ps), rf-min(ps)))
