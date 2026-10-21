#!/bin/bash
cd /home/user/Disparo-/videos/nichos/dentista/engine
for M in A B C; do
  node cap.js $M /tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/dent/lay_$M && /tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/cbenv/bin/python comp.py $M /tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/dent/lay_$M /tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/dent/video_$M.mp4
done
echo FIM
