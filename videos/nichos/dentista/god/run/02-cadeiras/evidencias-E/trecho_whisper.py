# Retranscreve o trecho 24,5 a 29,6 s (B02) com faster-whisper small, isolado, em raw.wav e voz_master.wav.
# Uso: python3 -I trecho_whisper.py  (somente leitura dos áudios; não escreve nada além do stdout)
import sys, subprocess, numpy as np
S='/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad'
sys.path.insert(0, S+'/fw')
from faster_whisper import WhisperModel
m = WhisperModel('small', device='cpu', compute_type='int8', download_root=S+'/fwmodels')
def load(f, a, b):
    raw = subprocess.run(['ffmpeg','-v','error','-ss',str(a),'-to',str(b),'-i',f,'-ac','1','-ar','16000','-f','f32le','-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)
for f in ['raw.wav','voz_master.wav']:
    for (a,b) in [(24.5,29.6),(26.8,29.6)]:
        au = load(S+'/dent/'+f, a, b)
        for prompt in [None, 'Você deixa de disputar paciente e passa a formar quem disputa.']:
            for beam in [1,5]:
                segs,_ = m.transcribe(au, language='pt', word_timestamps=True, vad_filter=False, beam_size=beam, initial_prompt=prompt, temperature=0.0, condition_on_previous_text=False)
                ws = [(w.word.strip(), round(w.start+a,2), round(w.probability,2)) for s in segs for w in s.words]
                print(f, a, b, 'beam', beam, 'prompt' if prompt else 'sem_prompt', '|', ' '.join(f'{w}({t};{p})' for w,t,p in ws))
