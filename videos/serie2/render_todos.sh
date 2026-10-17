#!/bin/bash
# Renderiza os 5 Reels e coloca a trilha (uma diferente em cada).
set -e
cd "$(dirname "$0")"
declare -A M=([r1-caixa]=deep-urban [r2-marqueteiro]=hazy-after-hours [r3-funil]=uplifting-bass [r4-case]=trap-electro-vibes [r5-escala]=like-a-loop-machine)
for id in r1-caixa r2-marqueteiro r3-funil r4-case r5-escala; do
  node capture.js $id
  ../add_music.sh $id/sem-trilha.mp4 ../musicas/${M[$id]}.mp3 $id/$id-9x16.mp4 2
  echo "$id $(ffprobe -v error -show_entries format=duration -of csv=p=0 $id/$id-9x16.mp4)s $(du -h $id/$id-9x16.mp4 | cut -f1)"
done
