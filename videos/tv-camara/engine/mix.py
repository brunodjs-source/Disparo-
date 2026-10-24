# uso: python3 mix.py corte.json SAIDA.wav
# Voz do trecho (voz_trat.wav), efeitos sonoros alinhados pelo pico, trilha com ducking e quietudes; master -14 LUFS / TP -1,5.
import sys, json, subprocess, os
C = json.load(open(sys.argv[1])); OUT = sys.argv[2]
SRC = C.get("voz", "/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/entrevista/voz_trat.wav")
SFX = "/home/user/Disparo-/videos/nichos/dentista/sfx"
MUS = "/home/user/Disparo-/videos/musicas"
PICO = {"whoosh": .2685, "riser": 1.5966, "swipe": .1371, "typing": .3022, "impact": .02, "sub": .03, "pop": .01, "tick": 0, "ding_si": .004, "shutter": .0, "coin": .0}
ini, dur = C["seg"]; dur = C["dur"]
voz_vol = C.get("voz_vol", 1.0)
inp = ["-ss", f"{ini:.3f}", "-t", f"{dur:.3f}", "-i", SRC]; fc = []; lab = []
# velocidade da voz (timelapse usa voz cortada em trechos; aqui só volume)
fc.append(f"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={voz_vol},asplit=2[voz][sc]")
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
fc.append("[pre]loudnorm=I=-14:TP=-1.5:LRA=9,aresample=48000[a]")
subprocess.run(["ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", ";".join(fc), "-map", "[a]", "-t", f"{dur:.3f}", OUT], check=True)
print("mix ok", C.get("id"))
