#!/bin/bash
# Masterizacao de voz gravada em sala (palestra, entrevista): ruido, eco, equalizacao, dinamica e volume do Instagram.
# Uso: master_voz.sh entrada saida.wav [inicio] [duracao] [pad_total]
# Cadeia: RNNoise (modelo cb, GregorR/rnnoise-models) tira ruido e parte do eco; afftdn limpa o chiado que sobra;
# agate corta a cauda do eco nas pausas; EQ tira o embolado da sala (220 e 480 Hz), devolve corpo (120 Hz),
# presenca (3,2 kHz) e ar (9 kHz); de-esser; dois compressores (nivelar e segurar picos); limiter; loudnorm -14 LUFS.
IN="$1"; OUT="$2"; SS=${3:+-ss $3}; T=${4:+-t $4}; PAD=${5:+,apad=whole_dur=$5}
M=$(cd "$(dirname "$0")" && pwd)/rnnoise-cb.rnnn
ffmpeg -loglevel error -y $SS $T -i "$IN" -vn -af "aresample=48000,highpass=f=80,arnndn=m=$M:mix=0.9,afftdn=nf=-32:tn=1,\
agate=threshold=0.015:ratio=4:attack=3:release=70:range=0.08:knee=4,\
equalizer=f=220:t=q:w=1.0:g=-5,equalizer=f=480:t=q:w=1.4:g=-2.5,equalizer=f=120:t=q:w=0.8:g=2,\
equalizer=f=3200:t=q:w=1.2:g=4,highshelf=f=9000:g=3,deesser=i=0.5,\
acompressor=threshold=-22dB:ratio=3:attack=8:release=120:makeup=4dB,acompressor=threshold=-12dB:ratio=6:attack=2:release=60:makeup=2dB,\
alimiter=limit=0.9,loudnorm=I=-14:TP=-1:LRA=6,aresample=48000,aformat=channel_layouts=stereo$PAD" "$OUT"
