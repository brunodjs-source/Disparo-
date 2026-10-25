#!/bin/bash
# uso: tres.sh SAIDA.mp4 A B C [inicioA inicioB inicioC]
# Story 1080x1920 de 18 s: 3 faixas iguais (vídeo ou imagem) em momentos diferentes,
# fundo #141210, filetes ouro #E8B36A, assinatura discreta. Áudio da faixa A, baixo.
set -e
OUT=$1; A=$2; B=$3; C=$4; SA=${5:-0}; SB=${6:-15}; SC=${7:-30}; D=18
inp(){ case "$1" in *.jpg|*.jpeg|*.png|*.JPG|*.PNG) echo "-loop 1 -t $D -i $1";; *) echo "-ss $2 -t $D -i $1";; esac; }
F=$(fc-match -f '%{file}' 'DejaVu Sans:bold')
P='scale=1000:560:force_original_aspect_ratio=increase,crop=1000:560,setsar=1,fps=30'
ffmpeg -y -v error $(inp "$A" $SA) $(inp "$B" $SB) $(inp "$C" $SC) -f lavfi -i "color=c=0x141210:s=1080x1920:d=$D:r=30" -filter_complex "
[0:v]$P,zoompan=z='1+0.0006*on':d=1:s=1000x560:fps=30[a];
[1:v]$P,zoompan=z='1.06-0.0006*on':d=1:s=1000x560:fps=30[b];
[2:v]$P,zoompan=z='1+0.0006*on':d=1:s=1000x560:fps=30[c];
[3:v][a]overlay=40:230[x1];[x1][b]overlay=40:810[x2];[x2][c]overlay=40:1390,
drawbox=x=40:y=226:w=1000:h=2:c=0xE8B36A:t=fill,drawbox=x=40:y=1954:w=1000:h=2:c=0xE8B36A:t=fill,
drawtext=fontfile=$F:text='@o_estrategista.com.br':fontcolor=0xE8B36A@0.8:fontsize=30:x=(w-tw)/2:y=170,
fade=t=in:d=0.4,fade=t=out:st=$((D-1)):d=1[v]" -map "[v]" -map 0:a? -af "volume=0.6,afade=t=out:st=$((D-1)):d=1" -t $D -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart "$OUT"
