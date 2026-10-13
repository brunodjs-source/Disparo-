#!/bin/bash
# Renderiza o anúncio, põe a trilha com grave e gera as versões 9:16 (Reels/Stories) e 4:5 (Feed).
# uso: ./finalizar.sh   (precisa de voz.wav e timeline.json prontos)
set -e
node capture.js
# trilha: hazy-after-hours, com a entrada do grave (15 s na música) caindo no trecho da autoridade
DROP=15.0
S4=$(python3 -c "import json;print(json.load(open('timeline.json'))['segs'][4]['start'])")
SS=$(python3 -c "print(max(0.0, $DROP-$S4))")
../../add_music.sh anuncio.mp4 ../../musicas/hazy-after-hours.mp3 anuncio-campinas-9x16.mp4 "$SS"
ffmpeg -v error -y -i anuncio-campinas-9x16.mp4 -vf "crop=1080:1350:0:285" -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a copy -movflags +faststart anuncio-campinas-4x5.mp4
for f in anuncio-campinas-9x16.mp4 anuncio-campinas-4x5.mp4; do
  echo "$f $(ffprobe -v error -show_entries format=duration -of csv=p=0 $f)s $(du -h $f | cut -f1)"
done
