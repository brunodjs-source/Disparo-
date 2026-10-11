import asyncio, json, ssl, edge_tts, edge_tts.communicate as ec
ec._SSL_CTX=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
SEG=["Seu produto é bom... mas a oferta não convence?",
"Acabou de sair um Reels novo, com as cinco partes de uma oferta que vende. Na ordem certa.",
"Toca aqui embaixo e assiste agora."]
async def main():
    out=[]
    for i,s in enumerate(SEG):
        c=edge_tts.Communicate(s,"pt-BR-FranciscaNeural",rate="+4%",boundary="WordBoundary")
        w=[]
        with open(f"s{i}.mp3","wb") as f:
            async for ch in c.stream():
                if ch["type"]=="audio": f.write(ch["data"])
                elif ch["type"]=="WordBoundary": w.append((ch["offset"]/1e7,ch["text"]))
        out.append({"text":s,"words":w})
    json.dump(out,open("segs.json","w"),ensure_ascii=False)
asyncio.run(main())
