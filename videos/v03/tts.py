import asyncio, json, ssl, edge_tts, edge_tts.communicate as ec
ec._SSL_CTX=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
SEG=[
"Seu lead está barato, e mesmo assim ninguém compra.",
"Já vi lançamento com custo por lead lindo, e prejuízo no final.",
"Lead barato costuma ser lead errado.",
"O número que importa é quanto custa cada cliente, não cada lead.",
"Pra melhorar, mexa em três coisas.",
"O anúncio precisa falar com quem tem o problema.",
"A página precisa carregar rápido e prometer uma coisa só.",
"E a captação precisa durar de 14 a 21 dias.",
"Menos que isso, você não aquece. Mais que isso, esfria.",
"Comenta CAPTAÇÃO, que eu te mando o checklist.",
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
