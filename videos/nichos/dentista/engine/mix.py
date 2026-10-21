# uso: python3 mix.py MODELO VOZ.wav SAIDA.wav
# Voz + SFX (atraso calculado pelo pico de cada som) + trilha hazy-after-hours com ducking pela voz,
# trilha a zero na quietude de 19,50 a 20,10 s, master final -14 LUFS / TP -1,5.
import sys, subprocess
M, VOZ, OUT = sys.argv[1:4]
SFX = "/home/user/Disparo-/videos/nichos/dentista/sfx"
MUS = "/home/user/Disparo-/videos/musicas/hazy-after-hours.mp3"
PICO = {"whoosh": 0.2685, "riser": 1.5966, "swipe": 0.1371, "typing": 0.3022}
EV = {  # (arquivo, tempo do evento em s, volume)
 "A": [("riser",2.08,.5),("tick",3.18,.6),("pop",7.68,.5),("swipe",10.24,.45),("whoosh",10.24,.5),("tick",12.66,.6),("pop",15.08,.5),
       ("tick",19.12,.6),("whoosh",20.64,.5),("ding_si",22.82,.35),("pop",27.24,.5),("pop",30.78,.5),("typing",32.0,.45)],
 "B": [("riser",2.08,.5),("swipe",3.18,.45),("tick",7.68,.6),("pop",11.38,.45),("pop",12.66,.45),("pop",15.08,.5),("tick",19.12,.6),
       ("whoosh",20.64,.5),("swipe",22.70,.45),("pop",27.24,.5),("pop",30.78,.5),("swipe",32.0,.4),("typing",32.1,.45)],
 "C": [("riser",2.08,.5),("pop",7.68,.5),("tick",11.14,.6),("tick",12.3,.6),("pop",15.08,.5),("pop",18.90,.5),("whoosh",20.64,.5),
       ("ding_si",22.82,.35),("pop",27.24,.5),("pop",30.78,.55),("typing",32.0,.45)],
}[M]
for _, t, _v in EV: assert not (19.5 <= t <= 20.1), "SFX na quietude"
inp = ["-i", VOZ, "-i", MUS]; fc = []; lab = []
for k, (n, t, v) in enumerate(EV):
    inp += ["-i", f"{SFX}/{n}.wav"]; d = max(0, int(round((t - PICO.get(n, 0))*1000)))
    fc.append(f"[{k+2}:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay={d}|{d},volume={v}[s{k}]"); lab.append(f"[s{k}]")
fc.append("[0:a]aformat=sample_rates=48000:channel_layouts=stereo,asplit=2[voz][sc]")
fc.append("[1:a]aformat=sample_rates=48000:channel_layouts=stereo,atrim=0:36.43,asetpts=PTS-STARTPTS,volume=0.11,"
          "volume=enable='between(t,19.5,20.1)':volume=0,afade=t=in:d=0.6,afade=t=out:st=34.9:d=1.5[mus]")
fc.append("[mus][sc]sidechaincompress=threshold=0.02:ratio=5:attack=20:release=350[duck]")
fc.append(f"[voz][duck]{''.join(lab)}amix=inputs={2+len(lab)}:duration=first:normalize=0,alimiter=limit=0.9[pre]")
fc.append("[pre]loudnorm=I=-14:TP=-1.5:LRA=9,aresample=48000[a]")
subprocess.run(["ffmpeg","-v","error","-y",*inp,"-filter_complex",";".join(fc),"-map","[a]","-t","36.43",OUT], check=True)
print("mix ok", M, len(EV), "SFX")
