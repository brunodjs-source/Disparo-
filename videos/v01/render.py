import json, math, wave, subprocess, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
BG = (5, 5, 5); TXT = (239, 230, 214); GOLD = (232, 179, 106); GOLD2 = (154, 95, 42); DIM = (120, 112, 100)
INTER = "/usr/share/fonts/opentype/inter/Inter-%s.otf"
def inter(w, s): return ImageFont.truetype(INTER % w, s)
def playfair(s, wght=700):
    f = ImageFont.truetype("fonts/Playfair.ttf", s)
    try: f.set_variation_by_axes([wght])
    except Exception: pass
    return f

segs = json.load(open("segs.json"))
HL = [{"ninguém", "comprou"}, {"três", "perguntas"}, {"maior", "problema"}, {"tentou", "funcionou"},
      {"investiria"}, {"segue", "lista"}, {"promessa", "formato", "preço", "adivinhar"}, {"pesquisa"}]
GAPS = [0.7, 0.8, 0.45, 0.45, 0.6, 0.55, 0.7, 0.75]  # pause BEFORE each segment
HOLD = 3.0

# ---- audio timeline
sr = 48000; tracks = []; t = 0.0; starts = []
for i in range(len(segs)):
    t += GAPS[i]
    with wave.open(f"t{i}.wav") as w:
        a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)
    starts.append(t); tracks.append((t, a)); t += len(a) / sr
TOTAL = t + HOLD
mix = np.zeros(int(TOTAL * sr) + 1, np.float32)
for st, a in tracks:
    i0 = int(st * sr); mix[i0:i0 + len(a)] += a
mix = np.clip(mix * 1.05, -32767, 32767).astype(np.int16)
with wave.open("voz.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(mix.tobytes())
ends = [starts[i] + len(tracks[i][1]) / sr for i in range(len(segs))]

# word times (relative to trimmed audio: subtract first word offset)
for i, s in enumerate(segs):
    w0 = s["words"][0][0]
    s["wt"] = [starts[i] + max(0, o - w0) for o, _ in s["words"]]

# ---- layout text for each segment
CAP = inter("Bold", 72); LH = 92; MAXW = W - 2 * 90
def tokens(s):
    toks = s["text"].replace("...", "…").split()
    # map each token to a word time by sequential matching
    times, wi = [], 0
    for tok in toks:
        clean = tok.strip(".,:?…!").lower()
        if clean and wi < len(s["wt"]):
            times.append(s["wt"][wi]); wi += 1
        else:
            times.append(times[-1] if times else s["wt"][0])
    return toks, times
d0 = ImageDraw.Draw(Image.new("RGB", (10, 10)))
layouts = []
for i, s in enumerate(segs):
    toks, times = tokens(s)
    lines, cur, cw = [], [], 0
    sp = d0.textlength(" ", font=CAP)
    for k, tok in enumerate(toks):
        tw = d0.textlength(tok, font=CAP)
        if cur and cw + sp + tw > MAXW: lines.append(cur); cur, cw = [], 0
        cur.append((tok, times[k], tw)); cw += (sp if len(cur) > 1 else 0) + tw
    if cur: lines.append(cur)
    items = []
    y0 = 790
    for li, line in enumerate(lines):
        lw = sum(x[2] for x in line) + sp * (len(line) - 1); x = (W - lw) / 2
        for tok, tm, tw in line:
            items.append((tok, tm, x, y0 + li * LH)); x += tw + sp
    layouts.append(items)

# ---- background assets
def glow(r, color):
    im = Image.new("RGBA", (r * 2, r * 2), (0, 0, 0, 0))
    ImageDraw.Draw(im).ellipse((r * 0.3, r * 0.3, r * 1.7, r * 1.7), fill=color + (90,))
    return im.filter(ImageFilter.GaussianBlur(r * 0.35))
G1, G2 = glow(520, GOLD), glow(460, GOLD2)
vig = Image.new("L", (W, H), 0)
vd = ImageDraw.Draw(vig)
for k in range(60):
    vd.rectangle((k * 9, k * 15, W - k * 9, H - k * 15), outline=int(255 * (1 - k / 60) ** 2.2))
vig = vig.filter(ImageFilter.GaussianBlur(60))
VIG = Image.new("RGBA", (W, H), (0, 0, 0, 255)); VIG.putalpha(vig.point(lambda v: int(v * 0.85)))
rng = np.random.default_rng(1)
GRAIN = [Image.fromarray((rng.normal(0, 1, (H // 2, W // 2)) * 9 + 128).clip(0, 255).astype(np.uint8)).resize((W, H)).convert("RGBA") for _ in range(4)]
for g in GRAIN: g.putalpha(14)

def ease(x): x = min(max(x, 0), 1); return 1 - (1 - x) ** 4
def seg_at(t):
    cur = 0
    for i, st in enumerate(starts):
        if t >= st - 0.25: cur = i
    return cur

LABEL = inter("SemiBold", 34); BIG = playfair(150); MID = playfair(96); ITEM = inter("SemiBold", 50); SMALL = inter("Medium", 40)

def spaced(d, xy, text, font, fill, track=8, anchor_center=True):
    widths = [d.textlength(c, font=font) for c in text]; tw = sum(widths) + track * (len(text) - 1)
    x = xy[0] - tw / 2 if anchor_center else xy[0]
    for c, cw in zip(text, widths):
        d.text((x, xy[1]), c, font=font, fill=fill); x += cw + track

def alpha(c, a, base=BG): return tuple(int(base[j] + (c[j] - base[j]) * a) for j in range(3))

def visual(img, d, t, i):
    """Upper visual element per scene (y 330..680)."""
    a = ease((t - (starts[i] - 0.25)) / 0.5)
    if i == 0:  # zero sales counter
        n = max(0, int(round(47 * (1 - ease((t - starts[0]) / 2.6)))))
        s = f"{n}"
        d.text((W / 2, 520), s, font=playfair(230), fill=alpha(GOLD, a), anchor="mm")
        spaced(d, (W / 2, 660), "VENDAS", LABEL, alpha(DIM, a), 10)
    elif i == 1:
        d.text((W / 2, 510), "3", font=playfair(260), fill=alpha(GOLD, a), anchor="mm")
        spaced(d, (W / 2, 670), "PERGUNTAS ANTES DO PRODUTO", LABEL, alpha(DIM, a), 8)
    elif i in (2, 3, 4):
        qs = ["Qual o maior problema?", "O que já tentou?", "Quanto investiria?"]
        for k in range(3):
            if k > i - 2: continue
            ak = ease((t - (starts[k + 2] - 0.25)) / 0.45) if k == i - 2 else 1
            y = 420 + k * 110; x = 130 - (1 - ak) * 60
            on = k == i - 2
            d.rounded_rectangle((x, y, x + 820, y + 88), 22, outline=alpha(GOLD if on else GOLD2, ak), width=3,
                                fill=alpha((22, 18, 12) if on else (12, 11, 9), ak))
            d.text((x + 50, y + 44), str(k + 1), font=inter("Bold", 44), fill=alpha(GOLD, ak), anchor="mm")
            d.text((x + 100, y + 44), qs[k], font=ITEM, fill=alpha(TXT if on else DIM, ak), anchor="lm")
    elif i == 5:
        chips = ["Seguidores", "Clientes", "Lista"]
        for k, c in enumerate(chips):
            ak = ease((t - (starts[5] + k * 0.55)) / 0.4)
            y = 400 + k * 105
            cw = d.textlength(c, font=ITEM) + 120; x = (W - cw) / 2
            d.rounded_rectangle((x, y + (1 - ak) * 30, x + cw, y + 84 + (1 - ak) * 30), 42,
                                outline=alpha(GOLD, ak), width=3)
            d.text((W / 2, y + 42 + (1 - ak) * 30), c, font=ITEM, fill=alpha(TXT, ak), anchor="mm")
    elif i == 6:
        outs = ["PROMESSA", "FORMATO", "PREÇO"]
        for k, c in enumerate(outs):
            ak = ease((t - (starts[6] + 1.0 + k * 0.45)) / 0.4)
            x = 205 + k * 335
            d.ellipse((x - 120, 420, x + 120, 660), outline=alpha(GOLD, ak), width=3)
            d.text((x, 540), c, font=inter("Bold", 38), fill=alpha(GOLD if k == 2 else TXT, ak), anchor="mm")

COMMENT = inter("Medium", 44)
def cta(img, d, t):
    i = 7; a = ease((t - starts[i] + 0.2) / 0.6)
    sc = 0.85 + 0.15 * a
    f = playfair(int(170 * sc))
    d.text((W / 2, 560), "PESQUISA", font=f, fill=alpha(GOLD, a), anchor="mm")
    # shine sweep
    sx = (t - starts[i] - 0.6) / 1.2
    if 0 < sx < 1:
        band = Image.new("L", (W, H), 0); bd = ImageDraw.Draw(band)
        cx = -200 + sx * (W + 400)
        bd.polygon([(cx - 60, 400), (cx + 40, 400), (cx - 60, 720), (cx - 160, 720)], fill=110)
        band = band.filter(ImageFilter.GaussianBlur(25))
        mask = Image.new("L", (W, H), 0); ImageDraw.Draw(mask).text((W / 2, 560), "PESQUISA", font=f, fill=255, anchor="mm")
        img.paste((255, 240, 210), (0, 0), Image.fromarray(np.minimum(np.array(band), np.array(mask))))
    # comment box typing
    tb = t - (starts[i] + 1.0)
    if tb > 0:
        ab = ease(tb / 0.4)
        d.rounded_rectangle((110, 740, W - 110, 840), 50, fill=alpha((24, 22, 19), ab), outline=alpha((70, 62, 50), ab), width=2)
        word = "PESQUISA"; n = min(len(word), int(tb * 9))
        txt = word[:n] if n else "Adicione um comentário…"
        d.text((170, 790), txt, font=COMMENT, fill=alpha(TXT if n else DIM, ab), anchor="lm")
        if n and int(t * 2.5) % 2 == 0:
            cx = 170 + d.textlength(txt, font=COMMENT) + 6
            d.line((cx, 765, cx, 815), fill=GOLD, width=3)
        # send arrow
        d.ellipse((W - 200, 755, W - 130, 825), fill=alpha(GOLD, ab))
        d.text((W - 165, 790), "↑", font=inter("Bold", 42), fill=alpha(BG, ab, GOLD) if False else BG, anchor="mm")

def frame(fi):
    t = fi / FPS
    img = Image.new("RGBA", (W, H), BG + (255,))
    img.alpha_composite(G1, (int(-300 + 140 * math.sin(t * 0.35)), int(150 + 120 * math.cos(t * 0.27))))
    img.alpha_composite(G2, (int(520 + 120 * math.cos(t * 0.3)), int(1150 + 140 * math.sin(t * 0.22))))
    d = ImageDraw.Draw(img)
    i = seg_at(t)
    # top label
    spaced(d, (W / 2, 290), "ETAPA 1  ·  PESQUISA", LABEL, GOLD2, 9)
    d.line((W / 2 - 40, 345, W / 2 + 40, 345), fill=GOLD2, width=2)
    if i < 7:
        visual(img, d, t, i)
        # captions
        for tok, tm, x, y in layouts[i]:
            a = ease((t - tm + 0.05) / 0.28)
            if a <= 0: continue
            clean = tok.strip(".,:?…!").lower()
            col = GOLD if clean in HL[i] else TXT
            d.text((x, y + (1 - a) * 22), tok, font=CAP, fill=alpha(col, a))
    else:
        cta(img, d, t)
        for tok, tm, x, y in layouts[i]:
            a = ease((t - tm + 0.05) / 0.28)
            if a <= 0: continue
            clean = tok.strip(".,:?…!").lower()
            d.text((x, y + 180 + (1 - a) * 22), tok, font=inter("Bold", 70) if False else CAP, fill=alpha(GOLD if clean in HL[i] else TXT, a))
    # scene-change flash
    for st in starts[1:]:
        dt = t - (st - 0.25)
        if 0 <= dt < 0.3:
            fl = Image.new("RGBA", (W, H), GOLD + (int(40 * (1 - dt / 0.3)),)); img.alpha_composite(fl)
    # slow camera push-in
    z = 1 + 0.02 * ((t % 12) / 12)
    if z > 1.001:
        zw, zh = int(W * z), int(H * z)
        img = img.resize((zw, zh), Image.BILINEAR).crop(((zw - W) // 2, (zh - H) // 2, (zw - W) // 2 + W, (zh - H) // 2 + H))
    img.alpha_composite(GRAIN[fi % 4]); img.alpha_composite(VIG)
    return img.convert("RGB")

N = int(TOTAL * FPS)
p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                      "-i", "voz.wav", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
                      "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", "video01-pesquisa.mp4"], stdin=subprocess.PIPE)
for fi in range(N):
    p.stdin.write(frame(fi).tobytes())
p.stdin.close(); p.wait()
print("dur", TOTAL, "frames", N)
