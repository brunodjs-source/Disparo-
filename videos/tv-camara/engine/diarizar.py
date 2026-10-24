# uso: python diarizar.py voz.wav transcricao_bruta.json transcricao.json
# Separa Bruno (voz grave) e Mirna (voz aguda) pela frequência fundamental mediana de cada segmento.
import sys, json, numpy as np, subprocess
import librosa
aud, entra, sai = sys.argv[1:4]
SR = 16000
a = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", aud, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout, np.float32)
segs = json.load(open(entra))
f0s = []
for s in segs:
    x = a[int(s["ini"] * SR):int(s["fim"] * SR)]
    if len(x) < SR * 0.3: f0s.append(None); continue
    f0, vf, _ = librosa.pyin(x, fmin=70, fmax=400, sr=SR, frame_length=1024)
    v = f0[vf] if vf is not None else []
    f0s.append(float(np.median(v)) if len(v) > 5 else None)
val = np.array([f for f in f0s if f])
# limiar entre as duas vozes: vale do histograma (log) entre os dois picos
lg = np.log(val); h, e = np.histogram(lg, bins=40)
p1 = np.argmax(h[:20]); p2 = 20 + np.argmax(h[20:])
lim = float(np.exp(e[p1 + np.argmin(h[p1:p2+1])])) if p2 > p1 else 165.0
lim = min(max(lim, 140), 200)
for s, f in zip(segs, f0s):
    s["f0"] = round(f, 1) if f else None
    s["falante"] = "B" if (f and f < lim) else ("M" if f else "?")
    for w in s["palavras"]: w.append(s["falante"]) if len(w) == 4 else None
json.dump(segs, open(sai, "w"), ensure_ascii=False)
from collections import Counter
print("limiar", round(lim, 1), "Hz", Counter(s["falante"] for s in segs))
