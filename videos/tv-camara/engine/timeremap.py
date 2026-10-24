# uso: python3 timeremap.py corte.json SAIDA.mp4
# Monta a base dos TIMELAPSES em sequência, a partir dos proxies (1080x1920, 30 qps):
# rt:      {"tipo":"rt", "fonte":F, "src":s, "dur":d}                       tempo real
# rapido:  {"tipo":"rapido", "fonte":F, "src0":a, "src1":b, "dur":d}        acelerado (setpts e tmix 1 2 1, rastro leve)
# amostra: {"tipo":"amostra", "fonte":F, "src0":a, "src1":b, "dur":d}       quadros soltos de a até b (pode voltar: rebobinar)
# congela: {"tipo":"congela", "fonte":F, "src":s, "dur":d}                  quadro parado
# duplo:   {"tipo":"duplo", "dur":d, "cima":{segmento}, "baixo":{segmento}} tela dividida (cada metade 1080x960, recorte central)
# Fontes F: full (plano aberto), zoom (Z2), cb (Bruno), cm (Mirna).
# Opções de qualquer segmento: "lento": 2 (câmera lenta com interpolação), "vf": "filtro ffmpeg extra" (ex.: zoompan, eq).
import sys, json, subprocess, os
C = json.load(open(sys.argv[1])); OUT = sys.argv[2]
SRC = C.get("src_dir", "/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/entrevista/src")
RECORTE = {"cb": "crop=771:1371:309:250,scale=1080:1920:flags=bicubic,", "cm": "crop=771:1371:0:250,scale=1080:1920:flags=bicubic,"}
def arquivo(f): return f"{SRC}/entrevista-{'1080p' if f == 'full' else 'zoom'}.mp4"
def faz(s, o, alt=1920):
    """renderiza um segmento simples em o (1080 x alt)."""
    arq = arquivo(s["fonte"]); n = int(round(s["dur"] * 30)); rec = RECORTE.get(s["fonte"], "")
    extra = (s.get("vf", "") + ",") if s.get("vf") else ""
    fim = f"crop=1080:{alt}:0:(ih-{alt})/2," if alt != 1920 else ""
    lento = s.get("lento", 1)
    if s["tipo"] == "amostra" or s["tipo"] == "congela":
        fs = o + "_q"; os.makedirs(fs, exist_ok=True)
        m = 1 if s["tipo"] == "congela" else n
        for q in range(m):
            ts = s["src"] if s["tipo"] == "congela" else s["src0"] + (s["src1"] - s["src0"]) * q / max(1, n - 1)
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{ts:.3f}", "-i", arq, "-frames:v", "1", f"{fs}/{q:04d}.png"], check=True)
        if s["tipo"] == "congela":
            cmd = ["-loop", "1", "-framerate", "30", "-i", f"{fs}/0000.png", "-vf", f"{rec}{extra}{fim}setsar=1"]
        else:
            cmd = ["-framerate", "30", "-i", f"{fs}/%04d.png", "-vf", f"{rec}{extra}tmix=frames=3:weights='1 2 1',{fim}setsar=1"]
    elif s["tipo"] == "rt":
        lent = f"minterpolate=fps={30 * lento}:mi_mode=mci:mc_mode=aobmc:vsbmc=1,setpts={lento}*PTS," if lento != 1 else ""
        cmd = ["-ss", f"{s['src']:.3f}", "-t", f"{s['dur'] / lento + .2:.3f}", "-i", arq, "-vf", f"{rec}{lent}fps=30,{extra}{fim}setsar=1"]
    else:
        v = (s["src1"] - s["src0"]) / s["dur"]
        cmd = ["-ss", f"{s['src0']:.3f}", "-t", f"{s['src1'] - s['src0']:.3f}", "-i", arq,
               "-vf", f"{rec}setpts=PTS/{v:.4f},fps=30,tmix=frames=3:weights='1 2 1',{extra}{fim}setsar=1"]
    subprocess.run(["ffmpeg", "-v", "error", "-y", *cmd, "-frames:v", str(n), "-an", "-c:v", "libx264", "-crf", "14", "-preset", "fast", "-pix_fmt", "yuv420p", o], check=True)
tmp = os.path.abspath(OUT) + ".partes"; os.makedirs(tmp, exist_ok=True); lista = []
for i, s in enumerate(C["segmentos"]):
    o = f"{tmp}/{i:02d}.mp4"
    if s["tipo"] == "duplo":
        for lado in ("cima", "baixo"):
            faz({**s[lado], "dur": s["dur"]}, f"{tmp}/{i:02d}_{lado}.mp4", alt=960)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{tmp}/{i:02d}_cima.mp4", "-i", f"{tmp}/{i:02d}_baixo.mp4", "-filter_complex", "vstack=2,setsar=1",
                        "-c:v", "libx264", "-crf", "14", "-preset", "fast", "-pix_fmt", "yuv420p", o], check=True)
    else:
        faz(s, o)
    n = int(round(s["dur"] * 30))
    lista.append(f"file '{o}'"); print("parte", i, s["tipo"], n, "quadros", flush=True)
open(f"{tmp}/lista.txt", "w").write("\n".join(lista))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{tmp}/lista.txt", "-c", "copy", OUT], check=True)
print("base ok", OUT)
