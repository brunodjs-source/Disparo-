# Narração com pronúncia de português do Brasil e o timbre do Bruno.
# 1) Kokoro (Apache 2.0) gera a fala com a voz brasileira pm_alex (fonemas pt-br do espeak).
# 2) ChatterboxVC (MIT) troca o timbre pelo do Bruno, usando a gravação de referência da pasta minhavoz.
# 3) Whisper confere cada trecho; se houver erro, tenta de novo com outra velocidade.
# uso: python gerar_voz_br.py REFERENCIA.wav [trecho ...]
# saída: s0.wav ... s7.wav (para o build_clone.py)
import json, re, sys, unicodedata
import numpy as np, soundfile as sf, torchaudio as ta, librosa
from kokoro_onnx import Kokoro
from chatterbox.vc import ChatterboxVC

SP = "/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad"
sys.path.append(SP + "/fw")
from faster_whisper import WhisperModel

REF = sys.argv[1]
SEGS = json.load(open("script.json"))["segs"]
ONLY = [int(x) for x in sys.argv[2:]] or list(range(len(SEGS)))
FALA = {"30": "trinta", "Eu": "Êu"}  # "Êu" força a tônica: sem ela o "eu" sai átono e soa "é o"
VELOCIDADES = [1.0, 0.95, 1.05, 0.9]
# trechos em que cada frase é gerada separada e emendada com pausa (o Kokoro junta listas curtas)
PICOTADO = {2: 0.2}


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.findall(r"[a-z0-9]+", t.replace("30", "trinta"))


def erros(a, b):
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, y in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (x != y))
    return d[-1]


kok = Kokoro(SP + "/kokoro/kokoro-v1.0.onnx", SP + "/kokoro/voices-v1.0.bin")
vc = ChatterboxVC.from_pretrained("cpu")
asr = WhisperModel("small", device="cpu", compute_type="int8", download_root=SP + "/fwmodels")

for i in ONLY:
    texto = " ".join(FALA.get(w, w) for w in SEGS[i].split(" "))
    alvo, melhor = norm(SEGS[i]), None
    for vel in VELOCIDADES:
        if i in PICOTADO:
            partes = [kok.create(f, voice="pm_alex", speed=vel, lang="pt-br") for f in re.split(r"(?<=[.:]) ", texto)]
            sr = partes[0][1]
            pausa = np.zeros(int(PICOTADO[i] * sr), np.float32)
            s = np.concatenate([x for a, _ in partes for x in (a, pausa)][:-1])
        else:
            s, sr = kok.create(texto, voice="pm_alex", speed=vel, lang="pt-br")
        sf.write("_src.wav", s, sr)
        wav = vc.generate(audio="_src.wav", target_voice_path=REF)
        a16 = librosa.resample(wav.squeeze(0).numpy(), orig_sr=vc.sr, target_sr=16000)
        segs, _ = asr.transcribe(a16.astype(np.float32), language="pt", beam_size=5)
        ouvido = " ".join(x.text.strip() for x in segs)
        e = erros(alvo, norm(ouvido))
        print(f"trecho {i} velocidade {vel}: {e} erro(s) | {ouvido}", flush=True)
        if melhor is None or e < melhor[0]:
            melhor = (e, wav)
        if e == 0:
            break
    ta.save(f"s{i}.wav", melhor[1], vc.sr)
print("pronto")
