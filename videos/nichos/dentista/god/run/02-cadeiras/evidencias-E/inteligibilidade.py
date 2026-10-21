# Proxy de inteligibilidade: faster-whisper small (int8, CPU) no arquivo inteiro de cada versão de áudio.
# Mede a probabilidade média por palavra e imprime o texto. Somente leitura dos áudios.
import sys, subprocess, numpy as np
S='/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad'
sys.path.insert(0, S+'/fw')
from faster_whisper import WhisperModel
m = WhisperModel('small', device='cpu', compute_type='int8', download_root=S+'/fwmodels')
for f in ['raw.wav','rn_std.wav','rn_sh.wav','rn_bd.wav','voz_master.wav']:
    raw = subprocess.run(['ffmpeg','-v','error','-i',S+'/dent/'+f,'-ac','1','-ar','16000','-f','f32le','-'], capture_output=True, check=True).stdout
    au = np.frombuffer(raw, np.float32)
    segs,_ = m.transcribe(au, language='pt', word_timestamps=True, vad_filter=False, beam_size=5, temperature=0.0, condition_on_previous_text=False)
    ws = [(w.word.strip(), w.probability) for s in segs for w in s.words]
    p = np.array([x[1] for x in ws])
    print(f'{f}: {len(ws)} palavras, prob media {p.mean():.3f}, mediana {np.median(p):.3f}, palavras com p<0,5: {(p<0.5).sum()}')
    print('   ', ' '.join(w for w,_ in ws))
