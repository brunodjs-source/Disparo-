import json, math, wave, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
BG = (250, 249, 246); TXT = (22, 21, 19); GOLD = (196, 140, 52); GOLD_D = (120, 78, 24); DIM = (140, 134, 124)
INTER = "/usr/share/fonts/opentype/inter/Inter-%s.otf"
def inter(w, s): return ImageFont.truetype(INTER % w, s)
def playfair(s, wght=800):
    f = ImageFont.truetype("fonts/Playfair.ttf", s)
    try: f.set_variation_by_axes([wght])
    except Exception: pass
    return f
EMO = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", 109)

segs = json.load(open("segs.json"))
HL = [{"ninguém", "comprou"}, {"três", "perguntas"}, {"maior", "problema"}, {"tentou", "funcionou"},
      {"investiria"}, {"segue", "lista"}, {"promessa", "formato", "preço", "adivinhar"}, {"pesquisa"}]
ICONS = ["📉", "🎯", "❓", "🔁", "💰", "📣", "✅", "💬"]
GAPS = [0.7, 0.8, 0.45, 0.45, 0.6, 0.55, 0.7, 0.75]
HOLD = 3.0; TR = 0.45  # transition length

# ---------- audio
sr = 48000; tracks = []; t = 0.0; starts = []
for i in range(len(segs)):
    t += GAPS[i]
    with wave.open(f"t{i}.wav") as w:
        a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)
    starts.append(t); tracks.append((t, a)); t += len(a) / sr
TOTAL = t + HOLD
mix = np.zeros(int(TOTAL * sr) + 1, np.float32)
for st, a in tracks: mix[int(st * sr):int(st * sr) + len(a)] += a
with wave.open("voz.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(np.clip(mix, -32767, 32767).astype(np.int16).tobytes())
for i, s in enumerate(segs):
    w0 = s["words"][0][0]; s["wt"] = [starts[i] + max(0, o - w0) for o, _ in s["words"]]
SC = [st - 0.3 for st in starts]  # scene switch times

# ---------- caption layout
CAP = inter("Bold", 72); LH = 92; MAXW = W - 180
d0 = ImageDraw.Draw(Image.new("RGB", (10, 10)))
def layout(i, y0):
    s = segs[i]; toks = s["text"].replace("...", "…").split(); times = []; wi = 0
    for tok in toks:
        if tok.strip(".,:?…!") and wi < len(s["wt"]): times.append(s["wt"][wi]); wi += 1
        else: times.append(times[-1] if times else s["wt"][0])
    sp = d0.textlength(" ", font=CAP); lines, cur, cw = [], [], 0
    for tok, tm in zip(toks, times):
        tw = d0.textlength(tok, font=CAP)
        if cur and cw + sp + tw > MAXW: lines.append(cur); cur, cw = [], 0
        cur.append((tok, tm, tw)); cw += (sp if len(cur) > 1 else 0) + tw
    lines.append(cur); out = []
    for li, line in enumerate(lines):
        x = (W - (sum(z[2] for z in line) + sp * (len(line) - 1))) / 2
        for tok, tm, tw in line: out.append((tok, tm, x, y0 + li * LH)); x += tw + sp
    return out
LAY = [layout(i, 790 if i < 7 else 960) for i in range(len(segs))]

# ---------- assets
def glow(r, color, a=70):
    im = Image.new("RGBA", (r * 2, r * 2), color + (0,))
    ImageDraw.Draw(im).ellipse((r * .3, r * .3, r * 1.7, r * 1.7), fill=color + (a,))
    return im.filter(ImageFilter.GaussianBlur(r * .35))
G1, G2 = glow(520, (240, 210, 160)), glow(460, (225, 228, 235), 90)
rng = np.random.default_rng(1)
GRAIN = []
for _ in range(3):
    g = Image.fromarray((rng.normal(0, 1, (H // 2, W // 2)) * 10 + 128).clip(0, 255).astype(np.uint8)).resize((W, H)).convert("RGBA"); g.putalpha(8); GRAIN.append(g)
def emoji(ch):
    im = Image.new("RGBA", (160, 160), (0, 0, 0, 0)); ImageDraw.Draw(im).text((80, 80), ch, font=EMO, embedded_color=True, anchor="mm"); return im
EMOJI = {c: emoji(c) for c in set(ICONS)}

def ease(x): x = min(max(x, 0), 1); return 1 - (1 - x) ** 4
def back(x):  # overshoot pop
    x = min(max(x, 0), 1); c = 1.7; return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2
def mixc(c, a): return tuple(int(BG[j] + (c[j] - BG[j]) * a) for j in range(3))

def text3d(img, xy, text, font, a, depth=14, face=GOLD, side=GOLD_D, tilt=0.0):
    """Extruded 3D lettering with soft floor shadow."""
    if a <= 0: return
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    x, y = xy
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((x + depth * 1.4, y + depth * 2.2), text, font=font, fill=(60, 40, 10, 70), anchor="mm")
    lay.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
    dx = 0.55 + tilt; dy = 1.0
    for k in range(depth, 0, -1):
        f = k / depth; col = tuple(int(side[j] * (1 - 0.25 * f)) for j in range(3))
        d.text((x + k * dx, y + k * dy), text, font=font, fill=col, anchor="mm")
    d.text((x, y), text, font=font, fill=face, anchor="mm")
    if a < 1: lay.putalpha(lay.getchannel("A").point(lambda v: int(v * a)))
    img.alpha_composite(lay)

def spin_icon(img, t, ch, cx, cy, size, t0, speed=1.6):
    a = ease((t - t0) / 0.5)
    if a <= 0: return
    e = EMOJI[ch].resize((size, size), Image.LANCZOS)
    sx = abs(math.cos((t - t0) * speed * math.pi))  # Y-axis spin
    w2 = max(4, int(size * (0.15 + 0.85 * sx))); bob = 10 * math.sin(t * 2.2)
    e = e.resize((w2, size), Image.LANCZOS)
    s = back((t - t0) / 0.6);
    if s <= 0.02: return
    e = e.resize((max(2, int(w2 * s)), max(2, int(size * s))), Image.LANCZOS)
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).ellipse((cx - w2 * .35, cy + size * .55, cx + w2 * .35, cy + size * .65), fill=(0, 0, 0, 40))
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(8)))
    if a < 1: e.putalpha(e.getchannel("A").point(lambda v: int(v * a)))
    img.alpha_composite(e, (int(cx - e.width / 2), int(cy - e.height / 2 + bob)))

LABEL = inter("SemiBold", 34); ITEM = inter("SemiBold", 50); COMMENT = inter("Medium", 44)
def spaced(d, xy, text, font, fill, track=8):
    ws = [d.textlength(c, font=font) for c in text]; x = xy[0] - (sum(ws) + track * (len(text) - 1)) / 2
    for c, cw in zip(text, ws): d.text((x, xy[1]), c, font=font, fill=fill); x += cw + track

def card(d, box, a, on):
    x0, y0, x1, y1 = box
    d.rounded_rectangle((x0 + 4, y0 + 8, x1 + 4, y1 + 8), 26, fill=mixc((225, 220, 210), a))
    d.rounded_rectangle(box, 26, fill=mixc((255, 255, 255), a), outline=mixc(GOLD if on else (225, 220, 210), a), width=3)

def scene(i, t):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    a = ease((t - SC[i]) / 0.5)
    if i == 0:
        n = max(0, int(round(47 * (1 - ease((t - starts[0]) / 2.6)))))
        text3d(img, (W / 2, 500), str(n), playfair(250), a, depth=16)
        spaced(d, (W / 2, 650), "VENDAS", LABEL, mixc(DIM, a), 10)
        spin_icon(img, t, ICONS[0], 860, 400, 130, SC[0] + 0.2)
    elif i == 1:
        s = back((t - SC[1]) / 0.6)
        text3d(img, (W / 2, 500), "3", playfair(max(10, int(280 * s))), a, depth=18)
        spaced(d, (W / 2, 670), "PERGUNTAS ANTES DO PRODUTO", LABEL, mixc(DIM, a), 8)
        spin_icon(img, t, ICONS[1], 250, 420, 120, SC[1] + 0.3)
    elif i in (2, 3, 4):
        qs = ["Qual o maior problema?", "O que já tentou?", "Quanto investiria?"]
        for k in range(i - 1):
            ak = ease((t - SC[k + 2]) / 0.5) if k == i - 2 else 1
            y = 400 + k * 115; x = 130 + (1 - ak) * 120; on = k == i - 2
            card(d, (x, y, x + 820, y + 92), ak, on)
            d.ellipse((x + 22, y + 18, x + 78, y + 74), fill=mixc(GOLD if on else (235, 228, 214), ak))
            d.text((x + 50, y + 46), str(k + 1), font=inter("Bold", 36), fill=mixc((255, 255, 255) if on else GOLD_D, ak), anchor="mm")
            d.text((x + 105, y + 46), qs[k], font=ITEM, fill=mixc(TXT if on else DIM, ak), anchor="lm")
        spin_icon(img, t, ICONS[i], 960, 330 + (i - 2) * 115 + 40, 90, SC[i] + 0.2)
    elif i == 5:
        for k, c in enumerate(["Seguidores", "Clientes", "Lista"]):
            ak = back((t - (starts[5] + k * 0.55)) / 0.5); al = ease((t - (starts[5] + k * 0.55)) / 0.3)
            if al <= 0: continue
            cw = d0.textlength(c, font=ITEM) + 120; x = (W - cw) / 2; y = 400 + k * 110
            card(d, (x, y + (1 - ak) * 40, x + cw, y + 86 + (1 - ak) * 40), al, k == 2)
            d.text((W / 2, y + 43 + (1 - ak) * 40), c, font=ITEM, fill=mixc(TXT, al), anchor="mm")
        spin_icon(img, t, ICONS[5], 190, 360, 110, SC[5] + 0.2)
    elif i == 6:
        for k, c in enumerate(["PROMESSA", "FORMATO", "PREÇO"]):
            tk = starts[6] + 1.0 + k * 0.45; ak = ease((t - tk) / 0.4); s = back((t - tk) / 0.5)
            if ak <= 0: continue
            x = 205 + k * 335; r = 120 * s
            d.ellipse((x - r + 5, 540 - r + 10, x + r + 5, 540 + r + 10), fill=mixc((228, 222, 210), ak))
            d.ellipse((x - r, 540 - r, x + r, 540 + r), fill=mixc((255, 255, 255), ak), outline=mixc(GOLD, ak), width=4)
            d.text((x, 540), c, font=inter("Bold", int(38 * max(s, .1))), fill=mixc(GOLD_D if k == 2 else TXT, ak), anchor="mm")
        spin_icon(img, t, ICONS[6], W / 2, 720, 80, starts[6] + 2.4)
    else:
        s = back((t - SC[7]) / 0.7); f = playfair(max(10, int(165 * s)))
        text3d(img, (W / 2, 560), "PESQUISA", f, a, depth=14)
        tb = t - (starts[7] + 1.0)
        if tb > 0:
            ab = ease(tb / 0.4)
            card(d, (110, 740, W - 110, 845), ab, True)
            word = "PESQUISA"; n = min(len(word), int(tb * 9)); txt = word[:n] if n else "Adicione um comentário…"
            d.text((170, 792), txt, font=COMMENT, fill=mixc(TXT if n else DIM, ab), anchor="lm")
            if n and int(t * 2.5) % 2 == 0:
                cx = 170 + d.textlength(txt, font=COMMENT) + 6; d.line((cx, 767, cx, 817), fill=GOLD, width=3)
            d.ellipse((W - 205, 757, W - 135, 827), fill=mixc(GOLD, ab))
            d.polygon([(W - 170, 773), (W - 154, 795), (W - 186, 795)], fill=(255, 255, 255)); d.rectangle((W - 173, 793, W - 167, 812), fill=(255, 255, 255))
        spin_icon(img, t, ICONS[7], 880, 380, 120, SC[7] + 0.5)
    # captions
    for tok, tm, x, y in LAY[i]:
        ak = ease((t - tm + 0.05) / 0.3)
        if ak <= 0: continue
        col = GOLD if tok.strip(".,:?…!").lower() in HL[i] else TXT
        d.text((x, y + (1 - ak) * 26), tok, font=CAP, fill=mixc(col, ak))
    return img

def frame(fi):
    t = fi / FPS
    img = Image.new("RGBA", (W, H), BG + (255,))
    img.alpha_composite(G1, (int(-300 + 140 * math.sin(t * .35)), int(150 + 120 * math.cos(t * .27))))
    img.alpha_composite(G2, (int(520 + 120 * math.cos(t * .3)), int(1150 + 140 * math.sin(t * .22))))
    d = ImageDraw.Draw(img)
    spaced(d, (W / 2, 290), "ETAPA 1  ·  PESQUISA", LABEL, GOLD, 9)
    d.line((W / 2 - 40, 345, W / 2 + 40, 345), fill=GOLD, width=2)
    i = max([k for k in range(len(SC)) if t >= SC[k]] or [0])
    cur = scene(i, t)
    p = (t - SC[i]) / TR
    if i > 0 and p < 1:  # smooth transition: old scene drifts up + blurs out, new rises in
        e = ease(p)
        old = scene(i - 1, SC[i] - 0.01).filter(ImageFilter.GaussianBlur(10 * e))
        old.putalpha(old.getchannel("A").point(lambda v: int(v * (1 - e))))
        img.alpha_composite(old, (0, int(-80 * e)))
        cur.putalpha(cur.getchannel("A").point(lambda v: int(v * e)))
        img.alpha_composite(cur, (0, int(60 * (1 - e))))
    else:
        img.alpha_composite(cur)
    z = 1 + 0.025 * ((t - SC[i]) / 8)  # slow continuous push-in per scene
    zw, zh = int(W * z), int(H * z)
    img = img.resize((zw, zh), Image.BILINEAR).crop(((zw - W) // 2, (zh - H) // 2, (zw - W) // 2 + W, (zh - H) // 2 + H))
    img.alpha_composite(GRAIN[fi % 3])
    return img.convert("RGB")

import sys
if len(sys.argv)>1:
    for tt in sys.argv[1:]: frame(int(float(tt)*FPS)).resize((360,640)).save(f'/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/g{tt}.png')
    sys.exit()
N = int(TOTAL * FPS)
p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                      "-i", "voz.wav", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
                      "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", "video01-pesquisa.mp4"], stdin=subprocess.PIPE)
for fi in range(N): p.stdin.write(frame(fi).tobytes())
p.stdin.close(); p.wait(); print("dur", TOTAL)
