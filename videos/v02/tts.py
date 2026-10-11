import asyncio, json, ssl, edge_tts, edge_tts.communicate as ec
ec._SSL_CTX=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
SEG=[
"Seu produto é bom. A sua oferta é que não convence.",
"Quando um lançamento trava no carrinho, quase sempre o problema está em como a oferta foi montada.",
"Oferta forte tem cinco partes. Nessa ordem.",
"A oportunidade: por que agora.",
"A prova: quem já conseguiu.",
"A história: por que você.",
"A objeção, respondida antes de aparecer.",
"E só no final... o preço.",
"Quem mostra o preço primeiro, faz o cliente comparar valor com dinheiro antes de entender o que está levando.",
"Comenta OFERTA, que eu te mando a estrutura completa.",
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
