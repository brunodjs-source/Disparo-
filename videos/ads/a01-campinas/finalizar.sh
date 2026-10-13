#!/bin/bash
# Renderiza o anúncio, põe a trilha com grave e gera as versões 9:16 (Reels/Stories) e 4:5 (Feed).
# uso: ./finalizar.sh   (precisa de voz.wav e timeline.json prontos)
set -e
node capture.js
# trilha: hazy-after-hours, com a entrada do grave (15,05 s na música) caindo no começo do trecho da autoridade.
# Se esse trecho começa depois de 15,05 s, a introdução ganha compassos repetidos (1,985 s cada) no começo.
DROP=15.05; BAR=1.985
S4=$(python3 -c "import json;print(json.load(open('timeline.json'))['segs'][4]['start'])")
read K SS <<< "$(python3 -c "import math;k=max(0,math.ceil(($S4-$DROP)/$BAR));print(k, round($DROP+k*$BAR-$S4,3))")"
MUS=../../musicas/hazy-after-hours.mp3
if [ "$K" -gt 0 ]; then
  ffmpeg -v error -y -i "$MUS" -filter_complex "[0:a]asplit=2[a][b];[a]atrim=0:$(python3 -c "print($K*$BAR)"),asetpts=PTS-STARTPTS[i];[i][b]concat=n=2:v=0:a=1[m]" -map "[m]" -c:a pcm_s16le _musica.wav
  MUS=_musica.wav
fi
echo "trilha: $K compasso(s) a mais, começa em ${SS}s"
../../add_music.sh anuncio.mp4 "$MUS" anuncio-campinas-9x16.mp4 "$SS"
ffmpeg -v error -y -i anuncio-campinas-9x16.mp4 -vf "crop=1080:1350:0:285" -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a copy -movflags +faststart anuncio-campinas-4x5.mp4
for f in anuncio-campinas-9x16.mp4 anuncio-campinas-4x5.mp4; do
  echo "$f $(ffprobe -v error -show_entries format=duration -of csv=p=0 $f)s $(du -h $f | cut -f1)"
done
