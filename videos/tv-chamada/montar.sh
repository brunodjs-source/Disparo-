#!/bin/bash
# Chamada TV vertical: fundo desfocado + video tratado + overlay (o.html) + sfx.
# Uso: montar.sh video.mov pasta_overlay saida.mp4
set -e
IN="$1"; OV="$2"; OUT="$3"; R=$(cd "$(dirname "$0")/../.." && pwd); SFX=$R/videos/nichos/dentista/sfx
GR="hqdn3d=2:1.5:4:4,scale=1920:1080:flags=lanczos,eq=gamma=1.05:contrast=1.07:brightness=0.015:saturation=1.08,curves=preset=medium_contrast,unsharp=5:5:0.6:3:3:0"
ffmpeg -loglevel error -y -t 30.6 -i "$IN" -framerate 30 -i "$OV/%05d.png" -i $SFX/whoosh.wav -i $SFX/impact.wav -i $SFX/riser.wav -filter_complex "\
[0:v]fps=30,$GR,split[a][b];\
[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:3,eq=brightness=-0.34:saturation=0.7[bg];\
[b]scale=1080:608,vignette=PI/6[fg];\
[bg][fg]overlay=0:640,tpad=stop_mode=clone:stop_duration=6[base];\
[base][1:v]overlay=0:0:shortest=1,format=yuv420p[v];\
[0:a]afade=t=out:st=30.0:d=0.6,apad=whole_dur=36,highpass=f=80,acompressor=threshold=-18dB:ratio=3:makeup=3dB[voz];\
[2:a]adelay=1000|1000,volume=0.5[w];[4:a]adelay=29000|29000,volume=0.6[r];[3:a]adelay=31300|31300,volume=0.9[i];\
[voz][w][r][i]amix=inputs=4:normalize=0,alimiter=limit=0.89:level=false[au]" \
 -map "[v]" -map "[au]" -t 36 -c:v libx264 -preset slow -crf 16 -c:a aac -b:a 192k -movflags +faststart "$OUT"
