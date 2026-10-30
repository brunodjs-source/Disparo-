"""Monta a trilha de efeitos a partir de events.json (maquina de escrever, trocas, carimbo).
Uso: python3 sfx_eventos.py events.json saida.wav duracao"""
import sys, json, subprocess, numpy as np, os
SR = 48000
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../nichos/dentista/sfx')
def load(n):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', f'{R}/{n}.wav', '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2)
S = {'k': (load('tick'), 0.55), 'k2': (load('tick'), 0.25), 'swap': (load('whoosh'), 0.8), 'stamp': (load('impact'), 0.7), 'end': (load('impact'), 1.0)}
ev, out, dur = json.load(open(sys.argv[1])), sys.argv[2], float(sys.argv[3])
mix = np.zeros((int(SR * dur) + SR, 2), np.float32)
for kind, t in ev:
    s, g = S[kind]; i = int(t * SR); j = min(len(mix), i + len(s))
    if i < len(mix): mix[i:j] += s[: j - i] * g
mix = np.clip(mix[: int(SR * dur)], -1, 1)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', out], input=mix.tobytes(), check=True)
