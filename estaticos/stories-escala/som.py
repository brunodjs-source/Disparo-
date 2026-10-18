import numpy as np, wave
SR=48000; D=30.0; N=int(SR*D); t=np.arange(N)/SR
L=np.zeros(N); R=np.zeros(N)
def mf(n): return 440*2**((n-69)/12)
def add(sig,st,pan=0.0,g=1.0):
    i=int(st*SR)
    if i>=N: return
    e=min(N,i+len(sig)); s=sig[:e-i]*g
    L[i:e]+=s*(1-pan)/1.0; R[i:e]+=s*(1+pan)/1.0
def env(n,a,d):
    x=np.arange(n)/SR; return np.minimum(x/a,1)*np.exp(-x/d)
def rhodes(f,dur):
    n=int(dur*SR); x=np.arange(n)/SR
    mod=np.sin(2*np.pi*f*x)*1.2*np.exp(-x*3)
    s=np.sin(2*np.pi*f*x+mod)+0.25*np.sin(2*np.pi*2*f*x)*np.exp(-x*2)
    s*=1+0.15*np.sin(2*np.pi*4.5*x)
    return s*env(n,0.01,1.6)*(1-np.clip((x-dur+0.4)/0.4,0,1))
bpm=88; beat=60/bpm; bar=4*beat
# Emaj9, C#m9, Amaj9, B6/9 (midi)
ch=[[52,56,59,63,66],[49,52,56,59,63],[45,49,52,56,59],[47,51,54,56,61]]
bass=[40,37,33,35]
k=0; tt=0.0
while tt<D:
    c=ch[k%4]
    for j,nn in enumerate(c):
        add(rhodes(mf(nn+12),bar),tt+0.012*j,pan=(j-2)*0.15,g=0.07)
    add(rhodes(mf(nn+12+7) if False else mf(c[2]+24),beat*0.9),tt+beat*2.5,0.3,0.03)
    n=int(bar*SR); x=np.arange(n)/SR
    b=np.sin(2*np.pi*mf(bass[k%4])*x)*env(n,0.02,1.2)
    add(b,tt,0,0.22); add(b[:int(beat*SR)],tt+beat*2.5,0,0.12)
    for q in range(4):
        kn=int(0.3*SR); kx=np.arange(kn)/SR
        if q in (0,2): add(np.sin(2*np.pi*(50+60*np.exp(-kx*30))*kx)*np.exp(-kx*9),tt+q*beat,0,0.28)
        for h in (0,0.5):
            hn=int(0.08*SR); hs=np.random.randn(hn)*np.exp(-np.arange(hn)/SR*60)
            hs=np.diff(hs,prepend=0)
            add(hs,tt+(q+h)*beat,0.25,0.018 if h else 0.03)
        if q in (1,3):
            sn=int(0.25*SR); ss=np.random.randn(sn)*np.exp(-np.arange(sn)/SR*14)
            add(np.convolve(ss,np.ones(8)/8,'same'),tt+q*beat,-0.1,0.035)
    tt+=bar; k+=1
# pad
pad=sum(np.sin(2*np.pi*mf(n)*t*(1+0.002*i)) for i,n in enumerate([64,71,75]))*0.012
L+=pad;R+=pad
def rev(x,g=0.35):
    y=x.copy()
    for dl,gg in [(0.031,.5),(0.047,.45),(0.071,.4),(0.113,.33),(0.173,.25),(0.29,.18)]:
        d=int(dl*SR); z=np.zeros_like(x); z[d:]=x[:-d]*gg; y+=z*g
    return y
L=rev(L);R=rev(R)
fade=np.minimum(1,np.minimum(t/1.0,(D-t)/1.5)); L*=fade;R*=fade
np.save('mus.npy',np.stack([L,R]))
# FX: sino suave em Si (B5 + B6 cintilante)
def fx():
    n=int(2.2*SR); x=np.arange(n)/SR; f=mf(83)
    s=(np.sin(2*np.pi*f*x)+0.35*np.sin(2*np.pi*2*f*x)*np.exp(-x*4)+0.15*np.sin(2*np.pi*3.01*f*x)*np.exp(-x*7))
    s*=np.minimum(x/0.004,1)*np.exp(-x*2.2)
    sw=np.random.randn(n)*np.exp(-((x-0.05)/0.06)**2)*0.08
    return s*0.6+np.convolve(sw,np.ones(20)/20,'same')
F=fx()
def story(n,times):
    a=np.load('mus.npy')[:, int((n-1)*10*SR):int(n*10*SR)].copy()
    fl=np.zeros(a.shape[1]); 
    for tm in times:
        i=int(tm*SR); e=min(len(fl),i+len(F)); fl[i:e]+=F[:e-i]
    fl=rev(fl,0.5)*0.16
    a[0]+=fl; a[1]+=fl
    if n>1: a[:, :int(0.15*SR)]*=np.linspace(0.6,1,int(0.15*SR))
    a/=max(1e-9,np.abs(a).max())/0.8
    w=wave.open(f'som-{n}.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((a.T*32767).astype(np.int16).tobytes()); w.close()
for n,(cnt,st) in {1:(4,2.1),2:(5,1.6),3:(4,2.1)}.items():
    story(n,[0.6+i*st+0.03 for i in range(cnt)])
