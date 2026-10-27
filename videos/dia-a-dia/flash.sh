#!/bin/bash
# Stories 9:16 em cortes rapidos: flash branco + click de camera a cada cena, 1 retrocesso.
# Musica de banco gratuito: MUSIC=arquivo.mp3 MUSIC_START=seg flash.sh ...
# Uso: flash.sh A.mov B.mov saida.mp4 "TITULO" "subtitulo"
set -e
A="$1"; B="$2"; OUT="$3"; T1="$4"; T2="$5"
R=$(cd "$(dirname "$0")/../.." && pwd)
PF="$R/videos/v02/fonts/Playfair.ttf"; IN=/usr/share/fonts/opentype/inter/Inter-Medium.otf
SH="$R/videos/nichos/dentista/sfx/shutter.wav"; SW="$R/videos/nichos/dentista/sfx/swipe.wav"
W=$(mktemp -d)
# fonte inicio dur centro_x reverso
SEGS=(
"B 0.0 2.0 560 0"
"A 0.3 1.8 470 0"
"B 3.0 1.9 560 0"
"A 6.4 2.0 590 0"
"A 6.4 2.0 590 1"
"A 9.0 1.9 440 0"
"B 6.0 1.9 380 0"
"B 9.2 2.6 520 0"
)
LIST=$W/list.txt; : > $LIST; i=0
for s in "${SEGS[@]}"; do
  read src st d cx rev <<< "$s"; f=$A; [ $src = B ] && f=$B
  x=$((cx-203)); [ $x -lt 0 ] && x=0
  base="crop=405:720:$x:0,scale=1080:1920:flags=lanczos,setsar=1,eq=contrast=1.06:saturation=1.08"
  if [ $rev = 1 ]; then
    vf="$base,reverse,setpts=PTS/2.5,rgbashift=rh=-8:bh=8,noise=alls=18:allf=t,fps=30"
    af="volume=0.25,areverse,atempo=2.0,atempo=1.25"
  else
    vf="$base,fps=30,fade=in:st=0:d=0.22:color=white"
    af="volume=0.35"
  fi
  ffmpeg -loglevel error -y -ss $st -t $d -i "$f" -vf "$vf" -af "$af,aformat=sample_rates=48000:channel_layouts=stereo" \
    -c:v libx264 -crf 17 -pix_fmt yuv420p -c:a aac $W/s$i.mp4
  echo "file '$W/s$i.mp4'" >> $LIST; i=$((i+1))
done
ffmpeg -loglevel error -y -f concat -safe 0 -i $LIST -c copy $W/cat.mp4
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $W/cat.mp4)
# tempos de corte para os sons
T=0; DL=""; n=0; CUTS=""
for f in $W/s*.mp4; do :; done
for k in $(seq 0 $((i-1))); do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $W/s$k.mp4)
  ms=$(python3 -c "print(int($T*1000))")
  if [ $k = 4 ]; then DL="$DL[2:a]adelay=$ms|$ms,volume=0.8[x$k];"; else DL="$DL[1:a]adelay=$ms|$ms,volume=0.9[x$k];"; fi
  if [ $k = 4 ]; then CUTS="$CUTS ${T}r"; else CUTS="$CUTS $T"; fi
  T=$(python3 -c "print($T+$d)")
done
if [ -n "$MUSIC" ]; then
  ffmpeg -loglevel error -y -ss ${MUSIC_START:-0} -i "$MUSIC" -t $D -af "afade=t=out:st=$(python3 -c "print($D-0.8)"):d=0.8" -ar 48000 -ac 2 $W/m.wav
else
  python3 "$R/videos/dia-a-dia/trilha_impacto.py" $W/m.wav $D $CUTS
fi
MIX=$(for k in $(seq 0 $((i-1))); do printf "[x$k]"; done)
GOLD=0xE8B36A
ffmpeg -loglevel error -y -i $W/cat.mp4 -i "$SH" -i "$SW" -i $W/m.wav -filter_complex "\
[0:v]drawbox=x=0:y=1250:w=iw:h=330:color=black@0.45:t=fill,\
drawtext=fontfile=$IN:text='BASTIDOR':fontsize=34:fontcolor=$GOLD:x=(w-tw)/2:y=1290:alpha='min(1,t/0.4)',\
drawtext=fontfile=$PF:text='$T1':fontsize=74:fontcolor=white:x=(w-tw)/2:y=1340:alpha='min(1,max(0,(t-0.15)/0.4))',\
drawtext=fontfile=$PF:text='$T2':fontsize=58:fontcolor=$GOLD:x=(w-tw)/2:y=1440:alpha='min(1,max(0,(t-0.3)/0.4))',\
drawtext=fontfile=$IN:text='REC':fontsize=30:fontcolor=0xFF3B30:x=110:y=270:enable='lt(mod(t,1),0.6)',\
drawtext=fontfile=$IN:text='%{eif\:t\:d\:2}s':fontsize=30:fontcolor=white:x=180:y=270[v];\
[0:a]volume=0.45[o];[3:a]volume=0.9[mu];$DL[o][mu]${MIX}amix=inputs=$((i+2)):normalize=0,apad=whole_dur=$D[a]" \
 -map "[v]" -map "[a]" -t $D -c:v libx264 -crf 17 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart $W/fin.mp4
ffmpeg -loglevel error -y -i $W/fin.mp4 -c:v copy -af "alimiter=limit=0.89:level=false" -c:a aac -b:a 192k -movflags +faststart "$OUT"
rm -rf $W
