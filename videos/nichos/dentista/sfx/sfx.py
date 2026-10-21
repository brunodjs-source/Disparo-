# Biblioteca de efeitos sonoros sintetizados (sem licença de terceiros). 48 kHz mono.
import numpy as np, wave
SR=48000
def save(n,x):
    x=x/max(1e-9,np.abs(x).max())*0.9
    w=wave.open(n+'.wav','wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((x*32767).astype(np.int16).tobytes());w.close()
def t(d): return np.arange(int(d*SR))/SR
def lp(x,a):
    y=np.zeros_like(x);s=0
    for i,v in enumerate(x): s+=a*(v-s);y[i]=s
    return y
rng=np.random.default_rng(7)
# whoosh: ruido com filtro varrendo e envelope em sino
x=t(0.55);n=rng.standard_normal(len(x));env=np.sin(np.pi*x/x[-1])**2
a=0.02+0.25*np.sin(np.pi*x/x[-1]);y=np.zeros_like(n);s=0
for i,v in enumerate(n): s+=a[i]*(v-s);y[i]=s
save('whoosh',y*env)
# impact: boom grave + transiente
x=t(1.2);save('impact',np.sin(2*np.pi*(45+80*np.exp(-x*18))*x)*np.exp(-x*3.2)+0.3*rng.standard_normal(len(x))*np.exp(-x*40))
# pop: bolha curta
x=t(0.12);save('pop',np.sin(2*np.pi*(600+900*np.exp(-x*60))*x)*np.exp(-x*35))
# click/tick
x=t(0.04);save('tick',rng.standard_normal(len(x))*np.exp(-x*300))
# ding em Si (B5) com harmônicos
x=t(1.8);f=987.77;save('ding_si',(np.sin(2*np.pi*f*x)+0.3*np.sin(2*np.pi*2*f*x)*np.exp(-x*4))*np.minimum(x/0.004,1)*np.exp(-x*2.4))
# riser: ruido + senoide subindo
x=t(1.6);save('riser',(0.6*lp(rng.standard_normal(len(x)),0.15)+0.4*np.sin(2*np.pi*(200+900*(x/x[-1])**2)*x))*(x/x[-1])**2)
# swipe curto
x=t(0.25);save('swipe',lp(rng.standard_normal(len(x)),0.3)*np.sin(np.pi*x/x[-1]))
# shutter
x=t(0.18);s1=rng.standard_normal(len(x))*np.exp(-x*80);s2=np.roll(s1,int(0.07*SR))*0.7;save('shutter',s1+s2)
# cash/coin: dois tons metálicos
x=t(0.6);save('coin',(np.sin(2*np.pi*2093*x)+np.sin(2*np.pi*2637*x)*(x>0.06))*np.exp(-x*7))
# bass drop sub
x=t(0.9);save('sub',np.sin(2*np.pi*(38+30*np.exp(-x*6))*x)*np.exp(-x*2.5))
# typing: 6 cliques
x=np.zeros(int(0.6*SR))
for k in range(6):
    i=int((0.02+k*0.09+rng.uniform(0,0.02))*SR);c=rng.standard_normal(500)*np.exp(-np.arange(500)/60);x[i:i+500]+=c
save('typing',x)
print('ok')
