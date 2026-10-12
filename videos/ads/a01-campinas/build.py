import json, wave, numpy as np
segs=json.load(open("segs.json"))
GAPS=[0.25,0.35,0.35,0.35,0.3,0.4,0.35,0.35,0.4]; HOLD=1.8; sr=48000
t=0; starts=[]; tr=[]
for i in range(len(segs)):
    t+=GAPS[i]
    with wave.open(f"t{i}.wav") as w: a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)
    starts.append(t); tr.append((t,a)); t+=len(a)/sr
total=t+HOLD; mix=np.zeros(int(total*sr)+1,np.float32)
for st,a in tr: mix[int(st*sr):int(st*sr)+len(a)]+=a
with wave.open("voz.wav","wb") as w: w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes(np.clip(mix,-32767,32767).astype(np.int16).tobytes())
out=[]
for i,s in enumerate(segs):
    w0=s["words"][0][0]
    out.append({"start":starts[i],"end":starts[i]+len(tr[i][1])/sr,"text":s["text"],"wt":[starts[i]+0.04+o-w0 for o,_ in s["words"]]})
json.dump({"total":total,"segs":out},open("timeline.json","w"),ensure_ascii=False)
print(round(total,2))
