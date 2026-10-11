import asyncio, json, ssl, edge_tts, edge_tts.communicate as ec
ec._SSL_CTX=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
SEG=[
"Você abriu o carrinho e ficou esperando as vendas caírem.",
"Em lançamento, a abertura do carrinho é a largada, não a linha de chegada.",
"Nos dias de carrinho aberto, cada dia tem uma ação.",
"Dia um: bônus pra quem entrar primeiro.",
"Dia dois: depoimentos e prova.",
"Dia três: uma live respondendo objeções.",
"Último dia: lembrete de fechamento em todos os canais.",
"De hora em hora, nas últimas horas.",
"E alguém do seu time chamando no WhatsApp quem clicou e não comprou.",
"Comenta CARRINHO, que eu te mando o cronograma.",
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
