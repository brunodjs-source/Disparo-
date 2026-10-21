# uso: python comp.py MODELO PASTA_CAMADAS SAIDA.mp4 [quadros...]
# Compositor: vídeo base (zoom punch-in, P&B no A, tela dividida no B) + letreiro atrás da pessoa
# (camada back recortada pela máscara, só o maior componente) + camada front. Falha se faltar PNG.
import sys, json, subprocess, numpy as np
from PIL import Image
from scipy import ndimage
M, LAY, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
ONLY = [int(x) for x in sys.argv[4:]]
SP = "/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/dent"
W, H, N = 1080, 1920, 1093
cl = lambda x: max(0.0, min(1.0, x))
eio = lambda x: (4*cl(x)**3 if cl(x) < .5 else 1-(-2*cl(x)+2)**3/2)

# zoom por modelo: lista de (tempo, escala); interpolação suave entre pontos
Z = {
 'A': [(0,1.0),(2.08,1.04),(5.3,1.04),(5.6,1.0),(7.5,1.0),(7.9,1.08),(8.8,1.08),(9.3,1.0),(11.94,1.04),(13.3,1.04),(13.84,1.0),(17.9,1.06),(20.1,1.06),(20.4,1.0),(20.8,1.08),(22.2,1.08),(22.6,1.0),(29.28,1.0),(30.76,1.08),(31.6,1.08),(32.0,1.0),(37,1.0)],
 'B': [(0,1.0),(3.0,1.04),(3.18,1.0),(20.1,1.0),(20.8,1.08),(22.2,1.08),(22.6,1.0),(37,1.0)],
 'C': [(0,1.0),(3.8,1.03),(13.8,1.03),(19.5,1.05),(20.1,1.05),(20.8,1.08),(22.2,1.08),(22.6,1.0),(29.3,1.0),(30.8,1.06),(31.6,1.06),(32.0,1.0),(37,1.0)],
}[M]
def zoom(t):
    for (a, za), (b, zb) in zip(Z, Z[1:]):
        if a <= t <= b: return za + (zb-za)*eio((t-a)/max(1e-6, b-a))
    return 1.0
def split(t):
    for a, b in [(3.18, 19.5), (22.7, 32.0)]:
        if a-.27 <= t <= b: return eio((t-(a-.27))/.27)*(1-eio((t-(b-.27))/.27))
    return 0.0
CX, CY = 540, 900   # centro do zoom (rosto)
def zoomimg(a, z, interp):
    if abs(z-1) < 1e-3: return a
    im = Image.fromarray(a); w2, h2 = W/z, H/z; x0 = CX-CX/z; y0 = CY-CY/z
    return np.asarray(im.transform((W, H), Image.AFFINE, (1/z, 0, x0, 0, 1/z, y0), resample=interp))

fr = ONLY or list(range(N))
b = subprocess.Popen(["ffmpeg","-v","error","-i",f"{SP}/base.mp4","-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
m = subprocess.Popen(["ffmpeg","-v","error","-i",f"{SP}/mask.mp4","-f","rawvideo","-pix_fmt","gray","-"],stdout=subprocess.PIPE)
o = None
if not ONLY:
    o = subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r","30","-i","-",
        "-c:v","libx264","-crf","17","-preset","medium","-pix_fmt","yuv420p",OUT],stdin=subprocess.PIPE)
for f in range(N):
    rb = b.stdout.read(W*H*3); rm = m.stdout.read(360*640)
    if len(rb) < W*H*3: raise SystemExit(f"base acabou no quadro {f}")
    if ONLY and f not in ONLY: continue
    t = f/30
    img = np.frombuffer(rb, np.uint8).reshape(H, W, 3)
    mk = np.frombuffer(rm, np.uint8).reshape(640, 360) > 110
    lab, k = ndimage.label(mk)
    if k > 1:
        s = ndimage.sum(mk, lab, range(1, k+1)); mk = lab == (1+int(np.argmax(s)))
    mk = ndimage.binary_dilation(mk, iterations=1)
    mkf = np.asarray(Image.fromarray((mk*255).astype(np.uint8)).resize((W, H), Image.BILINEAR).filter(__import__('PIL.ImageFilter',fromlist=['x']).GaussianBlur(3)), np.float32)/255
    z = zoom(t)
    img = zoomimg(img, z, Image.BICUBIC).astype(np.float32)
    mkf = zoomimg((mkf*255).astype(np.uint8), z, Image.BILINEAR).astype(np.float32)/255
    if M == 'A':   # P&B até 2,08 s, cor volta em 6 quadros
        kc = cl((t-2.08)/0.2); g = img.mean(2, keepdims=True); img = g+(img-g)*(kc*1.12)
    else:
        g = img.mean(2, keepdims=True); img = g+(img-g)*1.08
    bk = np.asarray(Image.open(f"{LAY}/back/{f:05d}.png").convert("RGBA"), np.float32)/255
    a = bk[..., 3:]*(1-mkf[..., None]); img = img*(1-a)+bk[..., :3]*255*a
    s = split(t) if M == 'B' else 0
    if s > 0:   # janela do Bruno embaixo: desloca o quadro para baixo, o painel cobre o topo
        top = int(round(800*s)); src0 = int(round(400*s))
        out = np.zeros_like(img); out[top:] = img[src0:src0+H-top]; img = out
    fr_ = np.asarray(Image.open(f"{LAY}/front/{f:05d}.png").convert("RGBA"), np.float32)/255
    img = img*(1-fr_[..., 3:])+fr_[..., :3]*255*fr_[..., 3:]
    if t > 36.43-0.2: img *= cl((36.43-t)/0.2)
    out = img.clip(0, 255).astype(np.uint8)
    if ONLY: Image.fromarray(out).save(f"{LAY}/still_{M}_{f:05d}.jpg", quality=88)
    else: o.stdin.write(out.tobytes())
if o: o.stdin.close(); o.wait()
print("comp ok", M)
