import asyncio, json, ssl, edge_tts, edge_tts.communicate as ec
ec._SSL_CTX=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
SEG=[
"Fechou o carrinho e você aceitou que acabou.",
"Quem não comprou no seu lançamento é o público mais valioso que você tem.",
"Já levantou a mão e só não fechou.",
"Antes de baixar o preço, reabra o carrinho por pouco tempo pra quem pediu.",
"Depois, pergunte pra quem não comprou o motivo.",
"Se foi dinheiro, ofereça uma versão menor.",
"Se foi tempo, mostre uma versão mais curta.",
"Só depois disso venha o desconto.",
"A ordem é reabertura, versão menor e, por último, preço.",
"Comenta RECUPERAÇÃO que eu te mando o passo a passo.",
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
