# uso: python transcrever.py AUDIO SAIDA.json [modelo] [ini_s] [fim_s]
# Transcrição palavra a palavra (faster-whisper) com probabilidade por palavra.
# Teste de 21/10 no trecho 15:00-16:00: medium com tratamento leve (sem arnndn) acertou nomes e números;
# small e o áudio com arnndn erraram muito (microfone de sala, longe).
import sys, json, subprocess, numpy as np, time
SP = "/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad"
sys.path.append(SP + "/fw")
from faster_whisper import WhisperModel
aud, out = sys.argv[1], sys.argv[2]
modelo = sys.argv[3] if len(sys.argv) > 3 else "medium"
ini = float(sys.argv[4]) if len(sys.argv) > 4 else 0.0
fim = float(sys.argv[5]) if len(sys.argv) > 5 else None
LEVE = "highpass=f=90,lowpass=f=7500,afftdn=nr=10:nf=-40,dynaudnorm=f=150:g=15,loudnorm=I=-18"
m = WhisperModel(modelo, device="cpu", compute_type="int8", cpu_threads=4, download_root=SP + "/fwmodels")
cmd = ["ffmpeg", "-v", "error", "-ss", str(ini)] + (["-t", str(fim - ini)] if fim else []) + ["-i", aud, "-af", LEVE, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"]
a = np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, np.float32)
t0 = time.time()
segs, info = m.transcribe(a, language="pt", beam_size=5, word_timestamps=True, vad_filter=True,
                          vad_parameters=dict(min_silence_duration_ms=400), condition_on_previous_text=False)
# sem hotwords nem initial_prompt: os dois fizeram o modelo escrever a própria lista no lugar da fala (15:21)
res = []
r2 = lambda x: round(x + ini, 2)
for s in segs:
    res.append({"ini": r2(s.start), "fim": r2(s.end), "texto": s.text.strip(), "prob": round(float(np.exp(s.avg_logprob)), 3),
                "palavras": [[r2(w.start), r2(w.end), w.word.strip(), round(w.probability, 3)] for w in s.words]})
    if len(res) % 20 == 0:
        print(f"{s.end + ini:.0f}s em {time.time()-t0:.0f}s", flush=True)
        json.dump(res, open(out, "w"), ensure_ascii=False)
json.dump(res, open(out, "w"), ensure_ascii=False)
print("FIM", len(res), "segmentos", round(time.time() - t0), "s", flush=True)
