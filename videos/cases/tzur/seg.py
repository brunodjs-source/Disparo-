import sys, subprocess, numpy as np, time
from rembg import new_session, remove
from PIL import Image
s = new_session("u2net_human_seg")
W,H=360,640
p = subprocess.Popen(["ffmpeg","-v","error","-i",sys.argv[1],"-vf",f"scale={W}:{H}","-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
o = subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","gray","-s",f"{W}x{H}","-r","30","-i","-","-c:v","libx264","-crf","12","-pix_fmt","yuv420p",sys.argv[2]],stdin=subprocess.PIPE)
n=int(sys.argv[3]) if len(sys.argv)>3 else 10**9; k=0; t=time.time(); prev=None
while k<n:
    b=p.stdout.read(W*H*3)
    if len(b)<W*H*3: break
    m=np.array(remove(Image.frombytes("RGB",(W,H),b),session=s,only_mask=True),np.float32)
    if prev is not None: m=0.6*m+0.4*prev
    prev=m; o.stdin.write(m.astype(np.uint8).tobytes()); k+=1
o.stdin.close(); o.wait(); print(k,"quadros",round(time.time()-t,1),"s")
