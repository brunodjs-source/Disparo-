# Gera voz.wav e timeline.json de cada Reels da série 2 (Kokoro pt-BR + conferência no Whisper).
# uso: python voz.py r1-caixa [r2-...]
import json, re, subprocess, sys, unicodedata, wave
import numpy as np
SP = "/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad"
sys.path.append(SP + "/fw")
from kokoro_onnx import Kokoro
from faster_whisper import WhisperModel
R = json.load(open("roteiros.json"))
kok = Kokoro(SP + "/kokoro/kokoro-v1.0.onnx", SP + "/kokoro/voices-v1.0.bin")
asr = WhisperModel("small", device="cpu", compute_type="int8", download_root=SP + "/fwmodels")
SR, TEMPO, GAP, HOLD = 48000, 1.06, 0.45, 1.6
def norm(t):
    t = unicodedata.normalize("NFD", t.lower()); t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.findall(r"[a-z0-9]+", t)
def dist(a, b):
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, y in enumerate(b, 1): p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (x != y))
    return d[-1]
def proc(s, sr):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-f", "f32le", "-ar", str(sr), "-ac", "1", "-i", "-", "-af",
        f"highpass=f=70,atempo={TEMPO},silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse",
        "-ar", str(SR), "-f", "f32le", "-"], input=s.astype(np.float32).tobytes(), capture_output=True, check=True).stdout
    b = np.frombuffer(raw, np.float32).copy(); return b / (np.sqrt(np.mean(b ** 2)) + 1e-9) * 0.09
def words(b, text):
    a16 = np.ascontiguousarray(subprocess.run(["ffmpeg","-v","error","-f","f32le","-ar",str(SR),"-ac","1","-i","-","-ar","16000","-f","f32le","-"],input=b.astype(np.float32).tobytes(),capture_output=True,check=True).stdout and np.frombuffer(subprocess.run(["ffmpeg","-v","error","-f","f32le","-ar",str(SR),"-ac","1","-i","-","-ar","16000","-f","f32le","-"],input=b.astype(np.float32).tobytes(),capture_output=True,check=True).stdout,np.float32))
    segs, _ = asr.transcribe(a16, language="pt", word_timestamps=True, beam_size=5)
    ws = [(w.start, w.word.strip()) for s in segs for w in s.words]
    out, k = [], 0
    for tok in text.split(" "):
        n = norm(tok)
        if not n: continue
        t0 = None
        for j in range(k, min(k + 4, len(ws))):
            m = norm(ws[j][1])
            if m and m[0] == n[0]: t0, k = ws[j][0], j + 1; break
        out.append(round(t0 if t0 is not None else ((out[-1] + .25) if out else 0), 3))
    return out, " ".join(w for _, w in ws)
for rid in sys.argv[1:]:
    r = R[rid]; t = 0.2; mix = []; segs = []
    for i, (text, label, vis, hl) in enumerate(r["segs"]):
        best = None
        for vel in (1.0, 0.95, 1.05):
            s, sr = kok.create(text, voice=r["voice"], speed=vel, lang="pt-br")
            b = proc(s, sr); wt, heard = words(b, text); e = dist(norm(text), norm(heard))
            if best is None or e < best[0]: best = (e, b, wt, heard)
            if e == 0: break
        e, b, wt, heard = best
        print(f"{rid} {i}: {e} erro(s) {len(b)/SR:.2f}s | {heard}", flush=True)
        mix.append((t, b)); segs.append({"start": t, "end": t + len(b) / SR, "text": text, "label": label, "vis": vis, "hl": hl, "wt": [t + x for x in wt]})
        t += len(b) / SR + GAP
    total = t - GAP + HOLD
    m = np.zeros(int(total * SR) + 1, np.float32)
    for st, b in mix: m[int(st * SR):int(st * SR) + len(b)] += b
    import os; os.makedirs(rid, exist_ok=True)
    with wave.open(f"{rid}/voz.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(m, -1, 1) * 32767).astype(np.int16).tobytes())
    json.dump({"total": total, "kw": r["kw"], "segs": segs}, open(f"{rid}/timeline.json", "w"), ensure_ascii=False)
    print(rid, "total", round(total, 2))
