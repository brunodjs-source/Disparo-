# Monta voz.wav e timeline.json a partir de s0.wav ... s7.wav (voz clonada) e segs.json.
# Corta o silêncio do começo e do fim de cada trecho pela energia do áudio (não pela marcação do
# Whisper, que às vezes chega atrasada), iguala o volume dos trechos e desloca os tempos das palavras.
import json, subprocess, wave
import numpy as np

segs = json.load(open("segs.json"))
GAPS = [0.25, 0.35, 0.35, 0.35, 0.3, 0.4, 0.35, 0.35]
HOLD, SR = 1.8, 48000


def carrega(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-af", "highpass=f=70,lowpass=f=12000",
                          "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32)


def limites(a):
    hop = int(SR * 0.01)
    rms = np.array([np.sqrt(np.mean(a[k:k + hop] ** 2) + 1e-9) for k in range(0, len(a) - hop, hop)])
    db = 20 * np.log10(rms / 32768)
    on = np.where(db > max(db.max() - 38, -50))[0]
    ini = max(0, on[0] * hop - int(0.05 * SR))
    fim = min(len(a), (on[-1] + 1) * hop + int(0.12 * SR))
    return ini, fim


t, starts, faixas = 0.0, [], []
for i, s in enumerate(segs):
    a = carrega(f"s{i}.wav")
    ini, fim = limites(a)
    a = a[ini:fim]
    a *= (0.2 * 32768) / (np.sqrt(np.mean(a ** 2)) + 1e-9) / 2.2  # nível parecido entre trechos
    a = np.clip(a, -32000, 32000)
    t += GAPS[i]
    starts.append((t, ini / SR))
    faixas.append((t, a))
    t += len(a) / SR
total = t + HOLD
mix = np.zeros(int(total * SR) + 1, np.float32)
for st, a in faixas:
    mix[int(st * SR):int(st * SR) + len(a)] += a
with wave.open("voz.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(np.clip(mix, -32767, 32767).astype(np.int16).tobytes())
out = []
for i, s in enumerate(segs):
    st, corte = starts[i]
    dur = len(faixas[i][1]) / SR
    wt = [max(st, st + o - corte) for o, _ in s["words"]]
    out.append({"start": st, "end": st + dur, "text": s["text"], "wt": wt})
json.dump({"total": total, "segs": out}, open("timeline.json", "w"), ensure_ascii=False)
print(round(total, 2))
