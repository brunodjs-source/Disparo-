# uso: python3 conferir.py ini-fim [ini-fim ...]  (segundo passe de transcrição: medium com áudio bruto e com filtro de voz)
import sys, numpy as np, subprocess
SP = "/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad"
sys.path.append(SP + "/fw")
from faster_whisper import WhisperModel
m = WhisperModel("medium", device="cpu", compute_type="int8", cpu_threads=4, download_root=SP + "/fwmodels")
aud = SP + "/entrevista/src/entrevista-audio.m4a"
for faixa in sys.argv[1:]:
    a0, a1 = map(float, faixa.split("-"))
    for nome, af in [("bruto", "anull"), ("voz", "highpass=f=120,lowpass=f=6000,afftdn=nr=18:nf=-38,loudnorm=I=-18")]:
        x = np.frombuffer(subprocess.run(["ffmpeg","-v","error","-ss",str(a0),"-t",str(a1-a0),"-i",aud,"-af",af,"-ac","1","-ar","16000","-f","f32le","-"],capture_output=True).stdout,np.float32)
        segs,_ = m.transcribe(x, language="pt", beam_size=8, best_of=5, vad_filter=False, condition_on_previous_text=True, temperature=0)
        print(f"== {faixa} {nome}: " + " ".join(s.text.strip() for s in segs), flush=True)
