"""Trilha de impacto estilo trailer, sincronizada com os cortes.
Uso: python3 trilha_impacto.py saida.wav duracao corte1 corte2 ...  (corte com sufixo r = retrocesso)"""
import sys, wave, numpy as np
SR = 48000
out, dur = sys.argv[1], float(sys.argv[2])
cuts = sys.argv[3:]
n = int(SR * dur) + SR
L = np.zeros(n); R = np.zeros(n)
rng = np.random.default_rng(7)
t_all = np.arange(n) / SR

def add(sig, at, pan=0.0, g=1.0):
    i = int(at * SR); j = min(n, i + len(sig)); s = sig[: j - i] * g
    L[i:j] += s * (1 - max(0, pan)); R[i:j] += s * (1 + min(0, pan))

def env(d, a=0.004, k=6.0):
    t = np.arange(int(d * SR)) / SR
    return np.minimum(1, t / a) * np.exp(-k * t), t

def boom(d=1.6):  # sub com queda de afinacao
    e, t = env(d, 0.002, 3.2)
    f = 38 + 70 * np.exp(-t * 18)
    return np.tanh(2.2 * np.sin(2 * np.pi * np.cumsum(f) / SR)) * e

def braam(d=1.4):  # metal grave distorcido
    e, t = env(d, 0.02, 2.4)
    s = sum(np.sin(2 * np.pi * f * t * (1 + 0.003 * np.sin(6 * t))) for f in (55, 55.4, 82.4, 110.2, 164.8))
    return np.tanh(1.8 * s / 3) * e

def hit():  # tambor de impacto
    e, t = env(0.5, 0.001, 9)
    return (np.sin(2 * np.pi * (60 + 120 * np.exp(-t * 40)) * t) + 0.5 * rng.standard_normal(len(t)) * np.exp(-t * 30)) * e

def tick():
    e, t = env(0.06, 0.0005, 60)
    return rng.standard_normal(len(t)) * e

# pulso de baixo 120 bpm em colcheias
beat = 0.5
for k in range(int(dur / (beat / 2)) + 1):
    at = k * beat / 2
    e, t = env(0.22, 0.003, 14)
    add(np.tanh(1.5 * np.sin(2 * np.pi * 55 * t)) * e, at, g=0.22)
    add(tick(), at, pan=0.4 if k % 2 else -0.4, g=0.05 if k % 2 else 0.035)
for k in range(int(dur / beat) + 1):
    add(hit(), k * beat, g=0.30 if k % 2 == 0 else 0.18)

# cama de tensao subindo
pad = sum(np.sin(2 * np.pi * f * t_all) for f in (110, 164.8, 220.5)) / 3
L += pad * 0.05 * (t_all / dur); R += pad * 0.05 * (t_all / dur)

for c in cuts:
    rev = c.endswith('r'); at = float(c.rstrip('r'))
    if rev:
        e, t = env(0.9, 0.3, 1.0)
        sw = np.sin(2 * np.pi * np.cumsum(900 * np.exp(-t * 3) + 120) / SR) * e
        add(sw, at, g=0.25)
        continue
    add(boom(), at, g=0.85); add(braam(), at, g=0.35)

# riser antes do fim e batida final
rd = 2.0; e = np.linspace(0, 1, int(rd * SR)) ** 2
add(rng.standard_normal(len(e)) * e * 0.18, dur - rd - 0.6)
add(boom(2.5), dur - 0.6, g=1.0); add(braam(2.5), dur - 0.6, g=0.5)

m = np.stack([L, R], 1)[: int(SR * dur)]
fade = np.ones(len(m)); fl = int(0.3 * SR); fade[-fl:] = np.linspace(1, 0, fl)
m = np.tanh(1.3 * m / (np.abs(m).max() + 1e-9)) * fade[:, None]
m = (m / np.abs(m).max() * 0.89 * 32767).astype(np.int16)
w = wave.open(out, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(m.tobytes()); w.close()
