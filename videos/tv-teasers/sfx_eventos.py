"""Monta a trilha de efeitos a partir de events.json (maquina de escrever, trocas, carimbo).
Uso: python3 sfx_eventos.py events.json saida.wav duracao"""
import sys, json, subprocess, numpy as np, os
SR = 48000
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../sfx-mixkit')  # efeitos prontos do Mixkit
def load(n, a=0, b=None):
    cut = ['-ss', str(a)] + (['-to', str(b)] if b else [])
    raw = subprocess.run(['ffmpeg', '-v', 'error'] + cut + ['-i', f'{R}/{n}.mp3', '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2)
S = {'clic': (load('shutter', 0, 0.5), 0.9), 'k': (load('tecla', 0.10, 0.45), 0.7), 'k2': (load('tecla2', 0, 0.55), 0.35), 'swap': (load('whoosh', 0.1), 0.9),
     'stamp': (load('carimbo', 0.54, 1.6), 0.9), 'end': (load('impacto'), 0.9)}
ev, out, dur = json.load(open(sys.argv[1])), sys.argv[2], float(sys.argv[3])
mix = np.zeros((int(SR * dur) + SR, 2), np.float32)
for kind, t in ev:
    s, g = S[kind]; i = int(t * SR); j = min(len(mix), i + len(s))
    if i < len(mix): mix[i:j] += s[: j - i] * g
mix = np.clip(mix[: int(SR * dur)], -1, 1)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', '-', out], input=mix.tobytes(), check=True)
