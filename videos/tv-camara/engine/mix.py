# uso: python3 mix.py corte.json SAIDA.wav
# Voz do trecho (voz_trat.wav), efeitos sonoros alinhados pelo pico, trilha com ducking e quietudes; master -14 LUFS / TP -1,5.
import sys, json, subprocess, os
C = json.load(open(sys.argv[1])); OUT = sys.argv[2]
SRC = C.get("voz", "/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/entrevista/voz_mix.wav")
SFX = "/home/user/Disparo-/videos/nichos/dentista/sfx"
MUS = "/home/user/Disparo-/videos/musicas"
PICO = {"whoosh": .2685, "riser": 1.5966, "swipe": .1371, "typing": .3022, "impact": .02, "sub": .03, "pop": .01, "tick": 0, "ding_si": .004, "shutter": .0, "coin": .0}
ini = C["seg"][0]; dur = C["dur"]
voz_vol = C.get("voz_vol", 1.0)
fc = []; lab = []
if C.get("voz_trechos"):     # timelapse: pedaços de voz em tempo real colocados na linha do tempo [t_saida, src_ini, dur]
    inp = []; vs = []
    for j, (to, si, d) in enumerate(C["voz_trechos"]):
        inp += ["-ss", f"{si:.3f}", "-t", f"{d:.3f}", "-i", SRC]; ms = int(round(to * 1000))
        fc.append(f"[{j}:a]aformat=sample_rates=48000:channel_layouts=stereo,afade=t=in:d=0.04,afade=t=out:st={max(0, d - .06):.3f}:d=0.06,adelay={ms}|{ms}[v{j}]"); vs.append(f"[v{j}]")
    fc.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{dur}[sil]")
    fc.append(f"[sil]{''.join(vs)}amix=inputs={1 + len(vs)}:duration=first:normalize=0,volume={voz_vol},asplit=2[voz][sc]")
    k = len(C["voz_trechos"])
else:
    fala = min(dur, C["seg"][1] - C["seg"][0])   # a voz para no fim do trecho; o resto é cartão final
    inp = ["-ss", f"{ini:.3f}", "-t", f"{fala:.3f}", "-i", SRC]
    fc.append(f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,afade=t=out:st={max(0, fala - .08):.3f}:d=0.08,apad=whole_dur={dur:.3f},volume={voz_vol},asplit=2[voz][sc]")
    k = 1
if C.get("trilha"):
    inp += ["-i", f"{MUS}/{C['trilha']}.mp3"]; tv = C.get("trilha_vol", 0.09)
    q = "".join(f",volume=enable='between(t,{a},{b})':volume=0" for a, b in C.get("quietude", []))
    fc.append(f"[{k}:a]aformat=sample_rates=48000:channel_layouts=stereo,atrim=0:{dur},asetpts=PTS-STARTPTS,volume={tv}{q},afade=t=in:d=0.6,afade=t=out:st={max(0,dur-1.5)}:d=1.5[mus]")
    fc.append("[mus][sc]sidechaincompress=threshold=0.02:ratio=6:attack=15:release=300[duck]"); lab.append("[duck]"); k += 1
for n, t, v in C.get("sfx", []):
    inp += ["-i", f"{SFX}/{n}.wav"]; d = max(0, int(round((t - PICO.get(n, 0)) * 1000)))
    fc.append(f"[{k}:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay={d}|{d},volume={v}[s{k}]"); lab.append(f"[s{k}]"); k += 1
fc.append(f"[voz]{''.join(lab)}amix=inputs={1+len(lab)}:duration=first:normalize=0,alimiter=limit=0.9[pre]")
fc.append("[pre]aresample=48000[a]")
pre = OUT + ".pre.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", ";".join(fc), "-map", "[a]", "-t", f"{dur:.3f}", pre], check=True)
# master em 2 passes (o passe único ficava em -16 LUFS nas peças com muita trilha): mede e aplica loudnorm linear
import re
med = subprocess.run(["ffmpeg", "-hide_banner", "-i", pre, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
d = json.loads(re.search(r"\{[^{}]*\}", med[med.rfind("Parsed_loudnorm"):], re.S).group(0))
ln = f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={d['input_i']}:measured_TP={d['input_tp']}:measured_LRA={d['input_lra']}:measured_thresh={d['input_thresh']}:offset={d['target_offset']}:linear=true"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", pre, "-af", ln + ",aresample=48000", OUT], check=True); os.remove(pre)
print("mix ok", C.get("id"))
