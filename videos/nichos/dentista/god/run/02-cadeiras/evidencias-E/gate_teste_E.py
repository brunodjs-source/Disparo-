# Gate (agate, range -24 dB, ratio 6) sobre arnndn sh mix 0,8: limiares 0,05 e 0,08 apos +15 dB. Mede se o gate come palavra.
# confiança do faster-whisper no arquivo inteiro e no trecho 'formar quem', e piso por percentil (p90-p5, janelas de 50 ms).
import sys, subprocess, numpy as np
S='/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad'
sys.path.insert(0, S+'/fw')
from faster_whisper import WhisperModel
m = WhisperModel('small', device='cpu', compute_type='int8', download_root=S+'/fwmodels')
fs = {'E_gate_0.05':'E_gate_0.05.wav','E_gate_0.08':'E_gate_0.08.wav'}
for k,f in fs.items():
    x48 = np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','48000','-f','f32le','-'],capture_output=True,check=True).stdout,np.float32)
    n=2400; kk=len(x48)//n; db=20*np.log10(np.sqrt((x48[:kk*n].reshape(kk,n)**2).mean(1))+1e-9)
    p90,p5=np.percentile(db,[90,5])
    au = np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True,check=True).stdout,np.float32)
    segs,_ = m.transcribe(au, language='pt', word_timestamps=True, vad_filter=False, beam_size=5, temperature=0.0, condition_on_previous_text=False)
    ws=[(w.word.strip(),w.start,w.probability) for s in segs for w in s.words]
    p=np.array([q for _,_,q in ws]); tre=' '.join(f'{w}({q:.2f})' for w,t,q in ws if 26.7<=t<=28.6)
    print(f'{k}: prob media {p.mean():.3f}, p<0,5: {(p<0.5).sum()}, p90-p5 {p90-p5:.1f} dB | trecho: {tre}')
