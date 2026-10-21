# Proxy de inteligibilidade: transcreve cada versao inteira e compara com o roteiro (contexto.md). Leitura apenas.
import sys, subprocess, numpy as np, re, unicodedata
S='/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad'
sys.path.insert(0, S+'/fw')
from faster_whisper import WhisperModel
ref = "Dentistas são mais de 474 mil colegas ativos no Brasil por que você ainda só vende hora de cadeira e quase todo perfil posta o mesmo diagnóstico e a mesma conclusão se você domina uma técnica que os dentistas querem aprender existe um mercado qual é ensinar o seu colega eu desenho seu lançamento você deixa de disputar paciente e passa a formar quem disputa sua técnica vira um segundo produto dentista comenta a sua profissão aqui que eu te respondo"
def norm(s):
    s=unicodedata.normalize('NFKD',s.lower()); s=''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9 ]',' ',s).split()
def wer(r,h):
    d=np.zeros((len(r)+1,len(h)+1),int); d[:,0]=range(len(r)+1); d[0,:]=range(len(h)+1)
    for i in range(1,len(r)+1):
        for j in range(1,len(h)+1):
            d[i,j]=min(d[i-1,j]+1,d[i,j-1]+1,d[i-1,j-1]+(r[i-1]!=h[j-1]))
    return d[-1,-1]/len(r)
m = WhisperModel('small', device='cpu', compute_type='int8', download_root=S+'/fwmodels')
R=norm(ref)
for f in ['raw.wav','rn_std.wav','rn_sh.wav','rn_bd.wav','voz_master.wav']:
    raw = subprocess.run(['ffmpeg','-v','error','-i',S+'/dent/'+f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True,check=True).stdout
    a=np.frombuffer(raw,np.float32)
    segs,_=m.transcribe(a,language='pt',word_timestamps=True,vad_filter=False,beam_size=5,condition_on_previous_text=False)
    ws=[w for s in segs for w in s.words]
    p=np.array([w.probability for w in ws])
    txt=' '.join(w.word.strip() for w in ws)
    print(f"{f:16s} palavras {len(ws):3d} prob_media {p.mean():.3f} prob<0,5: {(p<0.5).sum():2d} WER_vs_roteiro {wer(R,norm(txt)):.3f}")
    print('   ', txt)
