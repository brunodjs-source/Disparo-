import asyncio, json, ssl, edge_tts, edge_tts.communicate as ec
ec._SSL_CTX=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
SEG=[
"Sua live lotou e ninguém comprou.",
"Já assisti centenas de eventos de lançamento.",
"Os que não vendem têm um erro em comum: ensinam demais.",
"Evento que vende segue três passos.",
"Primeiro, mostra o problema e o custo de continuar nele.",
"Depois, mostra que existe outro caminho e que outras pessoas já fizeram.",
"Por último, apresenta o seu método como esse caminho.",
"O conteúdo serve pra provar que você sabe, não pra entregar tudo.",
"Quem aprende tudo de graça não sente que precisa de você.",
"Comenta EVENTO que eu te mando o roteiro.",
]
async def main():
    out=[]
    for i,s in enumerate(SEG):
        c=edge_tts.Communicate(s,"pt-BR-AntonioNeural",rate="+6%",pitch="-2Hz",boundary="WordBoundary")
        words=[]
        with open(f"s{i}.mp3","wb") as f:
            async for ch in c.stream():
                if ch["type"]=="audio": f.write(ch["data"])
                elif ch["type"]=="WordBoundary": words.append((ch["offset"]/1e7,ch["text"]))
        out.append({"text":s,"words":words})
    json.dump(out,open("segs.json","w"),ensure_ascii=False)
asyncio.run(main())
