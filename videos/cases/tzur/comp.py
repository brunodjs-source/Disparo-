# Junta: vídeo base (P&B até 4,28 s) + letreiros atrás da pessoa (máscara) + camada da frente; áudio com aplausos.
import subprocess, numpy as np
from PIL import Image
N=int(54.2*30)+1; W,H=1080,1920
b=subprocess.Popen(["ffmpeg","-v","error","-i","base.mov","-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
m=subprocess.Popen(["ffmpeg","-v","error","-i","mask.mp4","-vf",f"scale={W}:{H}","-f","rawvideo","-pix_fmt","gray","-"],stdout=subprocess.PIPE)
o=subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r","30","-i","-","-i","base.mov","-i","aplausos.wav",
 "-filter_complex","[2:a]adelay=4280|4280,volume=0.5[ap];[1:a]aformat=channel_layouts=stereo[va];[va][ap]amix=inputs=2:duration=first:normalize=0[a]",
 "-map","0:v","-map","[a]","-c:v","libx264","-crf","18","-preset","medium","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-shortest","case_v2_sem_trilha.mp4"],stdin=subprocess.PIPE)
for f in range(N):
    rb=b.stdout.read(W*H*3); rm=m.stdout.read(W*H)
    if len(rb)<W*H*3: break
    img=np.frombuffer(rb,np.uint8).reshape(H,W,3).astype(np.float32)
    if f/30<4.28: img[:]=img.mean(2,keepdims=True)
    else: g=img.mean(2,keepdims=True); img=np.clip(g+(img-g)*1.15,0,255)
    mk=np.frombuffer(rm,np.uint8).reshape(H,W).astype(np.float32) if len(rm)==W*H else np.zeros((H,W),np.float32)
    mk=np.clip((mk-70)/110,0,1); mk[:470]=0; mk=mk[...,None]
    try:
        bk=np.asarray(Image.open(f"ov2_back/{f:05d}.png").convert("RGBA"),np.float32)/255
        a=bk[...,3:]*(1-mk); img=img*(1-a)+bk[...,:3]*255*a
    except FileNotFoundError: pass
    try:
        fr=np.asarray(Image.open(f"ov2_front/{f:05d}.png").convert("RGBA"),np.float32)/255
        img=img*(1-fr[...,3:])+fr[...,:3]*255*fr[...,3:]
    except FileNotFoundError: pass
    o.stdin.write(img.clip(0,255).astype(np.uint8).tobytes())
o.stdin.close(); o.wait(); print("comp ok", f)
