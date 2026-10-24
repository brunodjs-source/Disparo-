#!/bin/bash
# uso: render.sh cortes/<id>.spec.json [quadros de teste...]
# ficha -> corte.json -> camadas (Playwright) -> composição -> mixagem -> mp4 final em $OUT/<id>.mp4
set -e
E=$(cd "$(dirname "$0")" && pwd); SPEC=$1; shift
OUT=${OUT:-/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/tv/render}
ID=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['id'])" "$SPEC"); W=$OUT/$ID; mkdir -p "$W"
python3 "$E/cortar.py" "$SPEC" "$W/corte.json" > "$W/frases.txt"
if python3 -c "import json,sys;sys.exit(0 if json.load(open(sys.argv[1])).get('segmentos') else 1)" "$W/corte.json"; then
  [ -f "$W/base.mp4" ] || python3 "$E/timeremap.py" "$W/corte.json" "$W/base.mp4"
  python3 - "$W/corte.json" "$W/base.mp4" <<'PY'
import json,sys; c=json.load(open(sys.argv[1])); c["base"]=sys.argv[2]; json.dump(c,open(sys.argv[1],"w"),ensure_ascii=False)
PY
fi
if [ $# -gt 0 ]; then rm -f "$W/cam/still_"*.jpg
  node "$E/cap.js" "$W/corte.json" "$W/cam" "$@" && python3 "$E/comp.py" "$W/corte.json" "$W/cam" "$W/x.mp4" "$@" 2>/dev/null
  ffmpeg -v error -y -pattern_type glob -i "$W/cam/still_*.jpg" -vf "scale=270:-1,tile=6x$(( ($# + 5) / 6 ))" -frames:v 1 "$W/teste.jpg"; echo "teste $W/teste.jpg"; exit 0
fi
rm -rf "$W/cam"; node "$E/cap.js" "$W/corte.json" "$W/cam"
python3 "$E/comp.py" "$W/corte.json" "$W/cam" "$W/video.mp4" 2>/dev/null
python3 "$E/mix.py" "$W/corte.json" "$W/audio.wav"
ffmpeg -v error -y -i "$W/video.mp4" -i "$W/audio.wav" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "$OUT/$ID.mp4"
# folha de revisão: 4 quadros por segundo
ffmpeg -v error -y -i "$OUT/$ID.mp4" -vf "fps=4,scale=180:-1,tile=12x$(python3 -c "import json,math;print(math.ceil(json.load(open('$W/corte.json'))['dur']*4/12))")" -frames:v 1 "$OUT/$ID-folha.jpg"
rm -rf "$W/cam"; echo "pronto $OUT/$ID.mp4"
