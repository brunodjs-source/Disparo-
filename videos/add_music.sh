#!/bin/bash
# uso: add_music.sh video.mp4 musica.mp3 saida.mp4 [inicio_musica_s]
V=$1; M=$2; O=$3; SS=${4:-0}
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
FO=$(python3 -c "print(max(0,$D-2.5))")
ffmpeg -v error -y -i "$V" -ss "$SS" -i "$M" -filter_complex \
"[0:a]aformat=sample_rates=48000:channel_layouts=stereo,asplit=2[voz][sc];\
[1:a]aformat=sample_rates=48000:channel_layouts=stereo,atrim=0:$D,asetpts=PTS-STARTPTS,volume=0.085,bass=g=3:f=90,afade=t=in:d=0.6,afade=t=out:st=$FO:d=2.5[mus];\
[mus][sc]sidechaincompress=threshold=0.02:ratio=5:attack=20:release=350[duck];\
[voz][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=9,aresample=48000[a]" \
-map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -movflags +faststart "$O"
