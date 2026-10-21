# Método alternativo ao DR02: RMS em janelas de 50 ms no arquivo inteiro; fala = percentil 90; piso = percentil 10.
# Distância fala-piso em dB. Não depende do alinhamento de palavras. Somente leitura.
import subprocess, numpy as np
S='/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/dent/'
for f in ['raw.wav','rn_std.wav','rn_sh.wav','rn_bd.wav','voz_master.wav']:
    x = np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',S+f,'-ac','1','-ar','48000','-f','f32le','-'],capture_output=True,check=True).stdout,np.float32)
    n=2400; k=len(x)//n
    r=np.sqrt((x[:k*n].reshape(k,n)**2).mean(1))+1e-9
    db=20*np.log10(r)
    p10,p50,p90=np.percentile(db,[10,50,90]); p5=np.percentile(db,5)
    print(f'{f}: p90 {p90:.1f} dBFS, p50 {p50:.1f}, p10 {p10:.1f}, p5 {p5:.1f}; p90-p10 = {p90-p10:.1f} dB; p90-p5 = {p90-p5:.1f} dB')
