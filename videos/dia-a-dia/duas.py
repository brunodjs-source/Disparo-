# uso: python3 duas.py SAIDA.mp4 FONTE[@inicio] FONTE[@inicio] ...
# Story 1080x1920, 18 s, 2 faixas iguais que trocam de cena a cada 3 s (alternadas),
# cada troca com flash branco e clique de câmera. Fundo #141210, filetes ouro, assinatura.
import sys, subprocess
SFX = '/home/user/Disparo-/videos/nichos/dentista/sfx/shutter.wav'
D, CENA, W, H = 18, 3.0, 1000, 760
Y = [230, 1010]
out, fontes = sys.argv[1], sys.argv[2:]
img = lambda f: f.lower().endswith(('.jpg', '.jpeg', '.png'))
src = []
for f in fontes:
    p, _, s = f.partition('@'); src.append((p, float(s or 0)))
font = subprocess.run(['fc-match', '-f', '%{file}', 'DejaVu Sans:bold'], capture_output=True, text=True).stdout
args, fc, n = ['ffmpeg', '-y', '-v', 'error'], [], 0
cenas = []  # (faixa, ini, dur, idx_input)
for faixa in (0, 1):
    off = 0 if faixa == 0 else CENA / 2
    t, k = 0.0, faixa
    marcos = [0.0] + [off + CENA * j for j in range(1, 20) if off + CENA * j < D] + [D]
    for a, b in zip(marcos, marcos[1:]):
        p, s0 = src[k % len(src)]
        if img(p): args += ['-loop', '1', '-t', f'{b-a:.3f}', '-i', p]
        else: args += ['-ss', f'{s0 + a + 7*faixa:.3f}', '-t', f'{b-a:.3f}', '-i', p]
        cenas.append((faixa, a, b - a, n)); n += 1; k += 1
args += ['-f', 'lavfi', '-i', f'color=c=0x141210:s=1080x1920:d={D}:r=30']; bg = n; n += 1
for faixa in (0, 1):
    seg = [c for c in cenas if c[0] == faixa]
    for j, (_, a, d, i) in enumerate(seg):
        z = "1+0.0008*on" if j % 2 == 0 else "1.08-0.0008*on"
        fc.append(f"[{i}:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},setsar=1,fps=30,"
                  f"zoompan=z='{z}':d=1:s={W}x{H}:fps=30,trim=duration={d:.3f},setpts=PTS-STARTPTS[f{faixa}_{j}]")
    fc.append(''.join(f'[f{faixa}_{j}]' for j in range(len(seg))) + f'concat=n={len(seg)}:v=1:a=0[p{faixa}]')
fc.append(f'[{bg}:v][p0]overlay=40:{Y[0]}[x];[x][p1]overlay=40:{Y[1]}[y]')
cortes = sorted({round(a, 3) for (_, a, _, _) in cenas if a > 0})
flash = ','.join(f"drawbox=x=40:y={Y[f]}:w={W}:h={H}:c=white@1:t=fill:enable='between(t,{a},{a+0.08})',"
                 f"drawbox=x=40:y={Y[f]}:w={W}:h={H}:c=white@0.5:t=fill:enable='between(t,{a+0.08},{a+0.16})'"
                 for (f, a, _, _) in cenas if a > 0)
fc.append(f"[y]{flash},drawbox=x=40:y={Y[0]-4}:w={W}:h=2:c=0xE8B36A:t=fill,drawbox=x=40:y={Y[1]+H+2}:w={W}:h=2:c=0xE8B36A:t=fill,"
          f"drawtext=fontfile={font}:text='@o_estrategista.com.br':fontcolor=0xE8B36A@0.8:fontsize=30:x=(w-tw)/2:y=170,"
          f"fade=t=in:d=0.3,fade=t=out:st={D-0.8}:d=0.8[v]")
args += ['-i', SFX]; s = n
fc.append(f"[{s}:a]asplit={len(cortes)}" + ''.join(f'[s{k}]' for k in range(len(cortes))))
fc += [f"[s{k}]adelay={int(c*1000)}|{int(c*1000)},volume=0.9[d{k}]" for k, c in enumerate(cortes)]
fc.append(''.join(f'[d{k}]' for k in range(len(cortes))) + f'amix=inputs={len(cortes)}:normalize=0,apad,atrim=duration={D}[a]')
args += ['-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]', '-t', str(D), '-c:v', 'libx264', '-crf', '20',
         '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out]
subprocess.run(args, check=True)
