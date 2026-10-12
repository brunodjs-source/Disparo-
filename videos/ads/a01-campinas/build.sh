#!/bin/bash
# corta cada trecho da voz no início da primeira palavra (com 40 ms de folga) e tira só o silêncio do fim
set -e
N=$(python3 -c "import json;print(len(json.load(open('segs.json'))))")
for ((i=0;i<N;i++)); do
  W0=$(python3 -c "import json;s=json.load(open('segs.json'))[$i];print(max(0,s['words'][0][0]-0.04))")
  ffmpeg -v error -y -ss "$W0" -i s$i.mp3 -af "areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.08,areverse" -ar 48000 -ac 1 -c:a pcm_s16le t$i.wav
done
python3 build.py
