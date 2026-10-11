import asyncio, json, ssl, edge_tts, edge_tts.communicate as ec
ec._SSL_CTX=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
SEG=[
"Todo lançamento seu começa do zero.",
"Lançamento não deveria ser um evento isolado.",
"Ele é o início de uma máquina de vendas.",
"Depois do lançamento, faça três coisas.",
"Reúna os depoimentos dos primeiros alunos nos primeiros sete dias.",
"Ofereça o próximo produto pra quem comprou, porque cliente satisfeito compra de novo.",
"E transforme o que mais converteu no lançamento em uma venda contínua:",
"anúncio, página e sequência rodando todo mês.",
"Assim o próximo lançamento já começa com prova e com caixa.",
"Comenta PERPÉTUO que eu te explico como montar.",
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
