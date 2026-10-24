# uso: python3 cortar.py spec.json corte.json
# Monta o corte.json de uma peça a partir da ficha (spec) e da transcrição revisada (dados/transcricao.json).
# A ficha traz: id, fmt, seg [ini, fim] em segundos da gravação, planos, chave {palavra, perto}, correcoes {errado: certo}
# e os campos livres do formato. Aqui entram: dur, words, frases (até 2 linhas), legendas, rótulo com o minuto real.
import sys, json, re, os
D = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(sys.argv[1])); OUT = sys.argv[2]
T = json.load(open(S.get("transcricao", os.path.join(D, "..", "dados", "transcricao.json"))))
INICIO_PROGRAMA = S.get("inicio_programa", 875.0)   # 14:35 da gravação = 00:00 do programa (abertura da Mirna)
ini, fim = S["seg"]; dur = round(fim - ini + S.get("extra", 0), 3)   # extra: segundos de imagem depois da última fala (cartão final)
VICIOS = {"né", "né?", "né,", "tipo,"}
cor = S.get("correcoes", {})
ws = []
for s in T:
    for w in s["palavras"]:
        if ini - 0.05 <= w[0] < fim and w[2]:
            txt = cor.get(w[2], w[2])
            if txt.lower() in VICIOS: continue
            ws.append([round(w[0] - ini, 3), round(w[1] - ini, 3), txt, w[4] if len(w) > 4 else s.get("falante", "B")])
def blocos(ws, maxc, pausa=.9):
    """frases inteiras (ponto, troca de falante ou pausa longa); a que passa de maxc caracteres é dividida
    no ponto mais equilibrado, de preferência depois de vírgula."""
    sent, cur = [], []
    for i, w in enumerate(ws):
        cur.append(w); nx = ws[i + 1] if i + 1 < len(ws) else None
        if nx is None or re.search(r"[.!?]$", w[2]) or nx[3] != w[3] or nx[0] - w[1] > pausa:
            sent.append(cur); cur = []
    out = []
    def divide(b):
        txt = " ".join(x[2] for x in b)
        if len(txt) <= maxc or len(b) < 2: out.append(b); return
        n = -(-len(txt) // maxc); alvo = len(txt) / n; melhor, nota = 1, 1e9; acum = 0
        for j in range(1, len(b)):
            acum += len(b[j - 1][2]) + 1
            pena = abs(acum - alvo) - (12 if re.search(r"[,;:]$", b[j - 1][2]) else 0) - (5 if b[j][2].lower() in ("e", "mas", "porque", "que", "então") else 0)
            if pena < nota: melhor, nota = j, pena
        divide(b[:melhor]); divide(b[melhor:])
    for b in sent: divide(b)
    return out
for i in range(1, len(ws)):                  # "musicais, E aí" -> "musicais, e aí"
    if ws[i - 1][2].endswith(",") and ws[i][2] in ("E", "Mas", "Então", "Na", "Porque", "Que", "Aí"): ws[i][2] = ws[i][2].lower()
fr = blocos(ws, S.get("max_chars", 40))
frases = []
for i, b in enumerate(fr):
    a = b[0][0]; nxt = fr[i + 1][0][0] if i + 1 < len(fr) else dur
    frases.append({"a": round(a, 3), "b": round(min(nxt, b[-1][1] + 1.2), 3), "ws": [[x[0], x[2]] for x in b], "falante": b[0][3]})
C = {k: v for k, v in S.items() if k not in ("correcoes", "transcricao")}
C["dur"] = dur
C["words"] = [[w[0], w[2], w[3]] for w in ws]
C.setdefault("frases", frases)
C.setdefault("legendas", [{"a": f["a"], "b": f["b"], "txt": " ".join(x[1] for x in f["ws"])} for f in frases])
m = max(0, ini - INICIO_PROGRAMA); C.setdefault("rotulo", f"NA TV · {S.get('serie', 'CORTE')} · min {int(m // 60):02d}:{int(m % 60):02d}")
# palavra-chave: a ocorrência mais perto do tempo indicado
if "chave" in S and "t" not in S["chave"]:
    k = S["chave"]; alvo = k["palavra"].lower().strip(".,!?"); perto = k.get("perto", 0)
    cands = [w for w in ws if w[2].lower().strip(".,!?") == alvo]
    if not cands: raise SystemExit(f"palavra-chave '{alvo}' não está no trecho")
    w = min(cands, key=lambda w: abs(w[0] - perto)); C["chave"] = {**k, "t": w[0], "palavra": k.get("mostrar", w[2].strip(".,!?"))}
for a in C.get("assuntos", []):           # PONTOS: tempo de cada palavra-assunto
    if "t" in a: continue
    alvo = a.get("dita", a["palavra"]).lower().strip(".,!?"); perto = a.get("perto", 0)
    cands = [w for w in ws if w[2].lower().strip(".,!?") == alvo]
    if not cands: raise SystemExit(f"assunto '{alvo}' não está no trecho")
    a["t"] = min(cands, key=lambda w: abs(w[0] - perto))[0]
# marcadores de tempo nos efeitos sonoros: "chave", "final", "virada"
ref = {"chave": C.get("chave", {}).get("t"), "final": C.get("final", {}).get("a"), "virada": C.get("virada", {}).get("t") if isinstance(C.get("virada"), dict) else None}
C["sfx"] = [[n, (ref[t] if isinstance(t, str) else t) + (d[0] if d else 0), v] for n, t, v, *d in C.get("sfx", [])]
if isinstance(C.get("virada"), dict) and "t" not in C["virada"]:
    v = C["virada"]; alvo = v["palavra"].lower(); cands = [w for w in ws if w[2].lower().strip(".,!?") == alvo]
    C["virada"]["t"] = min(cands, key=lambda w: abs(w[0] - v.get("perto", 0)))[0]
json.dump(C, open(OUT, "w"), ensure_ascii=False, indent=1)
print("corte", C["id"], "dur", dur, "palavras", len(ws), "frases", len(frases))
for f in frases: print(f"  {f['a']:6.2f} {f['falante']} {' '.join(x[1] for x in f['ws'])}")
