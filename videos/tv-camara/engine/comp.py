# uso: python comp.py corte.json PASTA_CAMADAS SAIDA.mp4 [quadros de teste...]
# Compositor da entrevista: monta a base por plano (ABERTO, Z2, CB, CM) a partir dos proxies,
# aplica zoom, P&B, look (curva, grão, vinheta), desfoque fixo de marcas, letreiro atrás das pessoas
# (camada back recortada pela máscara) e camada front. Falha alto se faltar PNG.
import sys, json, subprocess, os, numpy as np
from PIL import Image, ImageFilter

C = json.load(open(sys.argv[1])); LAY = sys.argv[2]; OUT = sys.argv[3]
ONLY = [int(x) for x in sys.argv[4:]]
SRC = C.get("src_dir", "/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/entrevista/src")
W, H = C.get("w", 1080), C.get("h", 1920)
FPS = 30; N = int(round(C["dur"] * FPS))
cl = lambda x: max(0.0, min(1.0, x))
eio = lambda x: (4*cl(x)**3 if cl(x) < .5 else 1-(-2*cl(x)+2)**3/2)

# recortes fixos medidos no proxy Z2 (1080x1920, nativo do 4K) e no ABERTO (1080x1920, 0,5x)
PLANOS = {"Z2": ("zoom", (0, 0, 1080, 1920)), "CB": ("zoom", (309, 250, 771, 1371)),
          "CM": ("zoom", (0, 250, 771, 1371)), "ABERTO": ("full", (0, 0, 1080, 1920))}
BLUR = C.get("blur_rects", {})   # {"zoom": [[x,y,w,h],...], "full": [...]}

def keyval(lst, t, default):
    """lista de [t, valor] com interpolação suave; valor constante fora."""
    if not lst: return default
    if t <= lst[0][0]: return lst[0][1]
    for (a, va), (b, vb) in zip(lst, lst[1:]):
        if a <= t <= b: return va + (vb - va) * eio((t - a) / max(1e-6, b - a))
    return lst[-1][1]

def plano_em(t):
    for p in C.get("planos", []):
        if p["t0"] <= t < p["t1"]: return p
    return {"plano": "Z2"}

def em_intervalos(t, ivs):
    return any(a <= t < b for a, b in ivs)

def ler(nome):
    ini = C["seg"][0]
    return subprocess.Popen(["ffmpeg", "-v", "error", "-ss", f"{ini:.3f}", "-i", f"{SRC}/entrevista-{'zoom' if nome=='zoom' else '1080p'}.mp4",
        "-t", f"{C['dur']+0.2:.3f}", "-vf", "fps=30", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)

usa = {PLANOS[p.get("plano", "Z2")][0] for p in C.get("planos", [{"plano": "Z2"}])}
streams = {n: ler(n) for n in usa}
mask_p = None
if C.get("mascara"):
    mask_p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", C["mascara"], "-f", "rawvideo", "-pix_fmt", "gray", "-"], stdout=subprocess.PIPE)
o = None
if not ONLY:
    o = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", "30", "-i", "-",
        "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p", OUT], stdin=subprocess.PIPE)

rng = np.random.default_rng(11)
GRAO = [rng.normal(0, 1, (H // 2, W // 2)).astype(np.float32) for _ in range(8)]
yy, xx = np.mgrid[0:H, 0:W]; VIN = (((xx - W/2) / (W*0.62))**2 + ((yy - H/2) / (H*0.62))**2).astype(np.float32)
VIN = np.clip(1 - 0.55 * np.clip(VIN - 0.35, 0, 1), 0, 1)[..., None]

for f in range(N):
    frames = {}
    for n, s in streams.items():
        b = s.stdout.read(1080*1920*3)
        if len(b) < 1080*1920*3: raise SystemExit(f"fonte {n} acabou no quadro {f}")
        frames[n] = np.frombuffer(b, np.uint8).reshape(1920, 1080, 3)
    mk = None
    if mask_p:
        mb = mask_p.stdout.read(1080*1920)
        mk = np.frombuffer(mb, np.uint8).reshape(1920, 1080) if len(mb) == 1080*1920 else None
    if ONLY and f not in ONLY: continue
    t = f / FPS; p = plano_em(t); fonte, (cx, cy, cw, ch) = PLANOS[p["plano"]]
    img = frames[fonte].copy()
    for (x, y, w, h) in BLUR.get(fonte, []):
        reg = Image.fromarray(img[y:y+h, x:x+w]).filter(ImageFilter.GaussianBlur(14)); img[y:y+h, x:x+w] = np.asarray(reg)
    z = keyval(p.get("zoom"), t, 1.0)
    # recorte do plano com zoom extra centrado no ponto focal
    fx, fy = p.get("foco", [cw/2, ch*0.45])
    zw, zh = cw / z, ch / z
    x0 = min(max(cx + fx - zw/2, cx), cx + cw - zw); y0 = min(max(cy + fy - zh/2, cy), cy + ch - zh)
    pil = Image.fromarray(img).transform((W, H), Image.EXTENT, (x0, y0, x0 + zw, y0 + zh), resample=Image.BICUBIC)
    im = np.asarray(pil).astype(np.float32)
    msk = None
    if mk is not None:
        mpil = Image.fromarray(mk).transform((W, H), Image.EXTENT, (x0, y0, x0 + zw, y0 + zh), resample=Image.BILINEAR)
        msk = np.asarray(mpil.filter(ImageFilter.GaussianBlur(2)), np.float32)[..., None] / 255
    if em_intervalos(t, C.get("pb", [])):
        g = im @ np.array([0.30, 0.59, 0.11], np.float32); g = np.clip((g - 128) * 1.18 + 122, 0, 255); im = np.repeat(g[..., None], 3, 2)
    look = C.get("look", "natural")
    if look in ("cinema", "pb"):
        x = im / 255; sc = x * x * (3 - 2 * x); im = 255 * (x + (sc - x) * 0.55)   # curva em S
        im = np.clip(im, 0, 255) * VIN
        gr = np.asarray(Image.fromarray(GRAO[f % 8]).resize((W, H)), np.float32)[..., None]
        im = np.clip(im + gr * (9 if look == "pb" else 6), 0, 255)
    elif look == "natural":
        g = im.mean(2, keepdims=True); im = np.clip(g + (im - g) * 1.06, 0, 255)
    bkf = f"{LAY}/back/{f:05d}.png"
    if C.get("back") and os.path.exists(bkf):
        bk = np.asarray(Image.open(bkf).convert("RGBA"), np.float32) / 255
        a = bk[..., 3:] * (1 - msk if msk is not None else 1); im = im * (1 - a) + bk[..., :3] * 255 * a
    frf = f"{LAY}/front/{f:05d}.png"
    if not os.path.exists(frf): raise SystemExit(f"falta {frf}")
    fr = np.asarray(Image.open(frf).convert("RGBA"), np.float32) / 255
    if fr.shape[:2] != (H, W): raise SystemExit("front com tamanho errado")
    im = im * (1 - fr[..., 3:]) + fr[..., :3] * 255 * fr[..., 3:]
    fade_in, fade_out = C.get("fade", [0, 0.2])
    if fade_in and t < fade_in: im *= t / fade_in
    if t > C["dur"] - fade_out: im *= cl((C["dur"] - t) / fade_out)
    out = np.clip(im, 0, 255).astype(np.uint8)
    if ONLY: Image.fromarray(out).save(f"{LAY}/still_{f:05d}.jpg", quality=88)
    else: o.stdin.write(out.tobytes())
if o: o.stdin.close(); o.wait()
print("comp ok", C.get("id"), N, "quadros")
