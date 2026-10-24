# uso: python3 timeremap.py corte.json SAIDA.mp4
# Monta a base do TIMELAPSE: trechos em tempo real (rt) e trechos acelerados (rapido) dos proxies, em sequência.
# rt:     {"tipo":"rt", "fonte":"zoom|full", "src":s, "dur":d}
# rapido: {"tipo":"rapido", "fonte":"full", "src0":a, "src1":b, "dur":d}  (setpts, tmix 1 2 1 para rastro leve)
import sys, json, subprocess, os
C = json.load(open(sys.argv[1])); OUT = sys.argv[2]
SRC = C.get("src_dir", "/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/entrevista/src")
tmp = OUT + ".partes"; os.makedirs(tmp, exist_ok=True); lista = []
for i, s in enumerate(C["segmentos"]):
    arq = f"{SRC}/entrevista-{'zoom' if s['fonte'] == 'zoom' else '1080p'}.mp4"; o = f"{tmp}/{i:02d}.mp4"
    n = int(round(s["dur"] * 30))
    if s["tipo"] == "rt":
        cmd = ["-ss", f"{s['src']:.3f}", "-i", arq, "-vf", "fps=30,setsar=1"]
    else:
        v = (s["src1"] - s["src0"]) / s["dur"]
        cmd = ["-ss", f"{s['src0']:.3f}", "-t", f"{s['src1'] - s['src0']:.3f}", "-i", arq,
               "-vf", f"setpts=PTS/{v:.4f},fps=30,tmix=frames=3:weights='1 2 1',setsar=1"]
    subprocess.run(["ffmpeg", "-v", "error", "-y", *cmd, "-frames:v", str(n), "-an", "-c:v", "libx264", "-crf", "14", "-preset", "fast", "-pix_fmt", "yuv420p", o], check=True)
    lista.append(f"file '{o}'"); print("parte", i, s["tipo"], n, "quadros", flush=True)
open(f"{tmp}/lista.txt", "w").write("\n".join(lista))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{tmp}/lista.txt", "-c", "copy", OUT], check=True)
print("base ok", OUT)
