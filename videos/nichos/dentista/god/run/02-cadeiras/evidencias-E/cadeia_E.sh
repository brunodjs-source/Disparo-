#!/bin/bash
# Cadeia de voz proposta pela cadeira E (rascunho medido, 21/10/2026). Entrada: raw.wav. Saída: E_voz_final.wav e .m4a
# 1 highpass 80 Hz + arnndn sh com mix 0,8 (inteligibilidade)  2 +15 dB e gate suave (limiar 0,08, range -24 dB)
# 3 EQ -2 dB em 250 Hz, +2 dB em 3,2 kHz, de-esser, compressor 3:1  4 loudnorm em 2 passadas, -14 LUFS, TP -1,5 (margem para o AAC)
S=/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad
ffmpeg -v error -y -i $S/dent/raw.wav -af "highpass=f=80,arnndn=m=$S/arnndn/sh.rnnn:mix=0.8,volume=15dB,agate=threshold=0.08:ratio=6:range=0.063:attack=3:release=200:knee=2,equalizer=f=250:t=q:w=1:g=-2,equalizer=f=3200:t=q:w=1.2:g=2,deesser=i=0.3,acompressor=threshold=0.1:ratio=3:attack=10:release=120:makeup=1" -ar 48000 -ac 1 E_pre.wav
J=$(ffmpeg -nostats -hide_banner -i E_pre.wav -af loudnorm=I=-14:TP=-1.5:LRA=7:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
g(){ echo "$J" | python3 -I -c "import json,sys;print(json.load(sys.stdin)['$1'])"; }
ffmpeg -v error -y -i E_pre.wav -af "loudnorm=I=-14:TP=-1.5:LRA=7:measured_I=$(g input_i):measured_TP=$(g input_tp):measured_LRA=$(g input_lra):measured_thresh=$(g input_thresh):offset=$(g target_offset):linear=true,aresample=48000" E_voz_final.wav
ffmpeg -v error -y -i E_voz_final.wav -c:a aac -b:a 192k E_voz_final.m4a
