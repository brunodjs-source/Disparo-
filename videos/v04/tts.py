import asyncio, json, ssl, edge_tts, edge_tts.communicate as ec
ec._SSL_CTX=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
SEG=[
"O lead se inscreveu no seu evento e esqueceu de você no dia seguinte.",
"A maior parte dos lançamentos perde a audiência entre a inscrição e o evento.",
"Esse intervalo é onde eu mais trabalho.",
"Entre a captação e o evento, o lead precisa receber três coisas.",
"Um motivo pra aparecer: o que ele vai sair sabendo.",
"Um lembrete em cada canal: e-mail, WhatsApp e stories.",
"E uma pequena tarefa antes do evento, como responder uma pergunta.",
"Quem se compromete com algo pequeno antes, aparece no grande.",
"Comenta AQUECIMENTO, que eu te mando a sequência.",
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
