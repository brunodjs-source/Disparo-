import asyncio, json, ssl, edge_tts, edge_tts.communicate as ec
ec._SSL_CTX=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
SEG=[
"Você criou o produto, gravou as aulas... e ninguém comprou.",
"Em todo lançamento que eu desenho, o produto só nasce depois que a audiência responde três perguntas.",
"Primeira: qual é o maior problema que você quer resolver agora?",
"Segunda: o que você já tentou, e não funcionou?",
"Terceira: quanto você investiria pra resolver isso?",
"Manda pra quem te segue, pra quem já comprou de você, e pra sua lista.",
"A resposta te dá a promessa, o formato e o preço. Você para de adivinhar.",
"Comenta PESQUISA, que eu te mando o modelo das perguntas.",
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
