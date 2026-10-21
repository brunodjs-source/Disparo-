# Fracao da largura ocupada pela pessoa em faixas de altura (1 a cada 3 quadros). Leitura apenas.
import subprocess, numpy as np, sys
M=sys.argv[1]; W,H=1080,1920
raw=subprocess.run(['ffmpeg','-v','error','-i',M,'-vf','select=not(mod(n\\,3)),scale=1080:1920','-vsync','0','-f','rawvideo','-pix_fmt','gray','-'],capture_output=True,check=True).stdout
fr=np.frombuffer(raw,np.uint8).reshape(-1,H,W)>127
print('quadros lidos',len(fr))
for y0,y1 in [(120,220),(220,300),(300,400),(400,500),(500,600),(600,700),(700,800)]:
    occ=fr[:,y0:y1,:].mean(axis=(1,2))
    print(f"faixa y {y0}-{y1}: pessoa ocupa mediana {np.median(occ)*100:.1f}% da area, p90 {np.percentile(occ,90)*100:.1f}%, max {occ.max()*100:.1f}%")
