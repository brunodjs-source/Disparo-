#!/bin/bash
# Chamada TV estilo recorte de jornal: camada de tras (j.html?layer=back) + 2 paineis de video + camada da frente.
# Uso: montar2.sh video.mov pasta_back pasta_front musica.mp3 saida.mp4
set -e
IN="$1"; TB="$2"; TF="$3"; MU="$4"; OUT="$5"; R=$(cd "$(dirname "$0")/../.." && pwd); SFX=$R/videos/nichos/dentista/sfx
# lente: limpa ruido, sobe resolucao, look de filme quente (sombras frias, altas quentes, preto levantado, grao)
GR="hqdn3d=2:1.5:4:4,scale=1920:1080:flags=lanczos,eq=gamma=1.04:contrast=1.06:saturation=0.96,colorbalance=rs=-0.04:bs=0.05:rh=0.06:gh=0.02:bh=-0.05,curves=all='0/0.04 0.5/0.52 1/0.97',unsharp=5:5:0.7:3:3:0,noise=alls=5:allf=t"
S="(1-exp(-6*clip((t-0.5)/0.9,0,1))*cos(8*clip((t-0.5)/0.9,0,1)))"
ffmpeg -loglevel error -y -t 30.6 -i "$IN" -framerate 30 -i "$TB/%05d.png" -framerate 30 -i "$TF/%05d.png" -i "$MU" -i $SFX/whoosh.wav -i $SFX/impact.wav -filter_complex "\
[0:v]fps=30,$GR,split[a][b];\
[a]scale=920:518,tpad=stop_mode=clone:stop_duration=6[top];\
[b]crop=iw/1.7:ih/1.7:(iw-ow)/2:ih*0.06,scale=920:518,tpad=stop_mode=clone:stop_duration=6[bot];\
[1:v][top]overlay=x=80:y='442+(230-442)*$S':eval=frame[s1];\
[s1][bot]overlay=x=80:y='960+170*$S':eval=frame[s2];\
[s2][2:v]overlay=0:0,format=yuv420p[v];\
[0:a]afade=t=out:st=30.0:d=0.6,apad=whole_dur=36,highpass=f=80,acompressor=threshold=-18dB:ratio=3:makeup=3dB[voz];\
[3:a]atrim=0.8:36.8,asetpts=PTS-STARTPTS,volume=0.22,afade=t=out:st=34.5:d=1.5[m];\
[4:a]adelay=450|450,volume=0.6[w];[5:a]adelay=30500|30500,volume=0.9[i];\
[voz][m][w][i]amix=inputs=4:normalize=0,alimiter=limit=0.89:level=false[au]" \
 -map "[v]" -map "[au]" -t 36 -c:v libx264 -preset slow -crf 16 -c:a aac -b:a 192k -movflags +faststart "$OUT"
