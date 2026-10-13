# Monta voz.wav e timeline.json a partir de s0.wav ... s7.wav (voz clonada).
# Para cada trecho: filtra, corta o silêncio e o ruído do começo e do fim pela energia,
# encurta pausas internas longas, iguala o volume, salva p{i}.wav e mede de novo o tempo de cada
# palavra com o Whisper no áudio já ajustado (assim a legenda cai exatamente na fala).
# uso: python3 build_clone.py
import json, re, subprocess, sys, unicodedata, wave
import numpy as np

SP = "/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad"
sys.path.append(SP + "/fw")
from faster_whisper import WhisperModel

SEGS = json.load(open("script.json"))["segs"]
GAPS = [0.15, 0.3, 0.3, 0.3, 0.3, 0.35, 0.3, 0.3]
HOLD, SR, HOP = 1.5, 48000, 480  # quadros de 10 ms
TEMPO = 1.12  # fala 12% mais rápida, sem mudar o tom: ritmo de anúncio e o vídeo cabe em 40 s
PAUSA_MAX, PAUSA_NOVA = 0.32, 0.26


def carrega(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-af", f"highpass=f=70,lowpass=f=12000,atempo={TEMPO}",
                          "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32)


def ajusta(a):
    n = len(a) // HOP
    db = np.array([20 * np.log10(np.sqrt(np.mean(a[k * HOP:(k + 1) * HOP] ** 2)) / 32768 + 1e-9) for k in range(n)])
    top = np.percentile(db, 95)
    m10 = np.convolve(db, np.ones(10) / 10, mode="same")  # média de 100 ms: ignora estalos e ruído curto
    m5 = np.convolve(db, np.ones(5) / 5, mode="same")
    fala = np.where(m10 > top - 26)[0]
    forte = np.where(m10 > top - 20)[0]  # o fim exige energia de fala de verdade (corta o rabicho de ruído)
    ini = max(0, fala[0] - 8)
    fim = min(n, forte[-1] + 16)
    # pausas internas longas viram pausas curtas
    quieto = m5 < top - 28
    pedacos, k = [], ini
    while k < fim:
        if quieto[k]:
            j = k
            while j < fim and quieto[j]:
                j += 1
            run = j - k
            if run * 0.01 > PAUSA_MAX and k > ini and j < fim:
                keep = int(PAUSA_NOVA / 0.01)
                pedacos.append(a[k * HOP:(k + keep // 2) * HOP])
                pedacos.append(a[(j - keep // 2) * HOP:j * HOP])
            else:
                pedacos.append(a[k * HOP:j * HOP])
            k = j
        else:
            j = k
            while j < fim and not quieto[j]:
                j += 1
            pedacos.append(a[k * HOP:j * HOP])
            k = j
    b = np.concatenate(pedacos)
    fade = int(0.04 * SR)
    b[-fade:] *= np.linspace(1, 0, fade)
    b *= (0.2 * 32768 / 2.2) / (np.sqrt(np.mean(b ** 2)) + 1e-9)
    return np.clip(b, -32000, 32000)


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.findall(r"[a-z0-9]+", t.replace("30", "trinta"))


asr = WhisperModel("small", device="cpu", compute_type="int8", download_root=SP + "/fwmodels")


def tempos(b, texto):
    a16 = subprocess.run(["ffmpeg", "-v", "error", "-f", "s16le", "-ar", str(SR), "-ac", "1", "-i", "-",
                          "-ar", "16000", "-f", "f32le", "-"], input=b.astype(np.int16).tobytes(),
                         capture_output=True, check=True).stdout
    segs, _ = asr.transcribe(np.frombuffer(a16, np.float32), language="pt", word_timestamps=True, beam_size=5)
    ws = [(w.start, w.word.strip()) for s in segs for w in s.words]
    out, k = [], 0
    for tok in texto.split(" "):
        n = norm(tok)
        if not n:
            continue
        t0 = None
        for j in range(k, min(k + 4, len(ws))):
            m = norm(ws[j][1])
            if m and m[0] == n[0]:
                t0, k = ws[j][0], j + 1
                break
        if t0 is None:
            t0 = (out[-1] + 0.25) if out else 0.0
        out.append(round(t0, 3))
    return out, " ".join(w for _, w in ws)


SO = [int(x) for x in sys.argv[1:]]  # com argumentos: só ajusta esses trechos (para ouvir amostra)
t, faixas, saida = 0.0, [], []
for i, texto in enumerate(SEGS):
    if SO and i not in SO:
        continue
    b = ajusta(carrega(f"s{i}.wav"))
    with wave.open(f"p{i}.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(b.astype(np.int16).tobytes())
    wt, ouvido = tempos(b, texto)
    t += GAPS[i]
    faixas.append((t, b))
    saida.append({"start": t, "end": t + len(b) / SR, "text": texto, "wt": [t + x for x in wt]})
    print(f"{i}: {len(b) / SR:.2f}s | {ouvido}")
    t += len(b) / SR
if SO:
    sys.exit(0)
total = t + HOLD
mix = np.zeros(int(total * SR) + 1, np.float32)
for st, b in faixas:
    mix[int(st * SR):int(st * SR) + len(b)] += b
with wave.open("voz.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(np.clip(mix, -32767, 32767).astype(np.int16).tobytes())
json.dump({"total": total, "segs": saida}, open("timeline.json", "w"), ensure_ascii=False)
print("total", round(total, 2))
