# Gera a narração do anúncio com a voz do Bruno, clonada das gravações da pasta minhavoz.
# Modelo: Chatterbox Multilingual (Resemble AI, licença MIT), rodando local na CPU.
# Cada trecho é conferido com o Whisper; se o modelo errar ou pular palavra, o trecho é refeito
# com outra semente (até 4 tentativas) e fica a versão com menos erros.
#
# uso: python gerar_voz_clonada.py REFERENCIA.wav [trecho ...]
# saída: s0.wav ... s7.wav e segs.json (mesmo formato do tts.py: texto e tempo de cada palavra)
import json, re, subprocess, sys, unicodedata
import numpy as np
import torch, torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

SP = "/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad"
sys.path.append(SP + "/fw")
from faster_whisper import WhisperModel

REF = sys.argv[1]
SEGS = json.load(open("script.json"))["segs"]
ONLY = [int(x) for x in sys.argv[2:]] or list(range(len(SEGS)))
# o modelo lê melhor número por extenso; a legenda continua com o algarismo
FALA = {"30": "trinta"}


def falado(t):
    return " ".join(FALA.get(w, w) for w in t.split(" "))


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.findall(r"[a-z0-9]+", t.replace("30", "trinta"))


def erros(a, b):  # distância de edição entre listas de palavras
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, y in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (x != y))
    return d[-1]


tts = ChatterboxMultilingualTTS.from_pretrained(device="cpu")
asr = WhisperModel("small", device="cpu", compute_type="int8", download_root=SP + "/fwmodels")


def transcrever(wav, sr):
    a = ta.functional.resample(wav, sr, 16000).squeeze(0).numpy().astype(np.float32)
    segs, _ = asr.transcribe(a, language="pt", word_timestamps=True, beam_size=5)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in s.words]


try:
    saida = json.load(open("segs.json"))
except Exception:
    saida = [None] * len(SEGS)
saida += [None] * (len(SEGS) - len(saida))

for i in ONLY:
    alvo = norm(SEGS[i])
    melhor = None
    for tent in range(4):
        torch.manual_seed(1000 * i + tent)
        wav = tts.generate(falado(SEGS[i]), language_id="pt", audio_prompt_path=REF,
                           exaggeration=0.45, cfg_weight=0.5, temperature=0.7)
        ws = transcrever(wav, tts.sr)
        e = erros(alvo, norm(" ".join(w for _, _, w in ws)))
        print(f"trecho {i} tentativa {tent + 1}: {e} erro(s) | {' '.join(w for _, _, w in ws)}", flush=True)
        if melhor is None or e < melhor[0]:
            melhor = (e, wav, ws)
        if e == 0:
            break
    e, wav, ws = melhor
    ta.save(f"s{i}.wav", wav, tts.sr)
    # tempo de cada palavra do roteiro: casa as palavras do Whisper com as do texto, na ordem
    toks = SEGS[i].split(" ")
    tempos, k = [], 0
    for tok in toks:
        n = norm(tok)
        if not n:
            continue
        t0 = None
        for j in range(k, min(k + 4, len(ws))):
            if norm(ws[j][2]) and norm(ws[j][2])[0] == n[0]:
                t0, k = ws[j][0], j + 1
                break
        if t0 is None:  # palavra não achada: estima pelo vizinho
            t0 = (tempos[-1][0] + 0.25) if tempos else (ws[0][0] if ws else 0.0)
        tempos.append((round(t0, 3), tok))
    saida[i] = {"text": SEGS[i], "words": tempos, "erros": e}
    json.dump(saida, open("segs.json", "w"), ensure_ascii=False)
print("pronto")
