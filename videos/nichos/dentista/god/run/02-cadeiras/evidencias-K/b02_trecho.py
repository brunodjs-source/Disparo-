# Segunda transcricao do trecho 24,5 a 29,6 s em raw.wav e voz_master.wav (B02). Leitura apenas.
import sys, subprocess, numpy as np
S='/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad'
sys.path.insert(0, S+'/fw')
from faster_whisper import WhisperModel
m = WhisperModel('small', device='cpu', compute_type='int8', download_root=S+'/fwmodels')
for f in ['raw.wav','voz_master.wav']:
    raw = subprocess.run(['ffmpeg','-v','error','-ss','24.5','-t','5.1','-i',S+'/dent/'+f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True,check=True).stdout
    a = np.frombuffer(raw,np.float32)
    for beam,temp in [(5,0.0),(10,0.0)]:
        segs,_ = m.transcribe(a, language='pt', word_timestamps=True, vad_filter=False, beam_size=beam, temperature=temp, condition_on_previous_text=False)
        ws=[(w.word.strip(), round(24.5+w.start,2), round(24.5+w.end,2), round(w.probability,2)) for s in segs for w in s.words]
        print(f, 'beam', beam, '|', ' '.join(w[0] for w in ws))
        print('   ', ws)
