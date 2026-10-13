# Gera a narração do anúncio com a voz Antonio (Microsoft) no SEU computador.
# Serve para quando o servidor da sessão estiver bloqueado pela Microsoft.
#
# Como usar (Windows, Mac ou Linux, com Python 3 instalado):
#   1. pip install edge-tts
#   2. python gerar_voz_no_pc.py
#   3. Envie o arquivo voz-anuncio.zip que aparecer na mesma pasta.
import asyncio, json, os, zipfile
import edge_tts

TRECHOS = [
    "Em Campinas, você perde cliente no mesmo lugar.",
    "Ele pede o preço, diz que vai pensar e some.",
    "Seguidor. Curtida. Indicação. Nenhum deles diz quem vai fechar.",
    "Nutricionista, consórcio, dentista, advogado: vocês vendem uma decisão que o cliente adia.",
    "Treze anos de marketing me mostraram: a venda não morre no preço. Morre no intervalo.",
    "Lançamento encurta esse intervalo: pesquisa, oferta na ordem certa, aquecimento e prazo real.",
    "Por isso todo especialista precisa de um estrategista: você atende, e eu desenho e comando.",
    "Me manda sua profissão. Em 30 minutos eu te mostro onde o seu cliente escapa.",
]
PASTA = "voz-anuncio"


async def main():
    os.makedirs(PASTA, exist_ok=True)
    saida = []
    for i, texto in enumerate(TRECHOS):
        com = edge_tts.Communicate(texto, "pt-BR-AntonioNeural", rate="+8%", pitch="-2Hz", boundary="WordBoundary")
        palavras = []
        with open(os.path.join(PASTA, f"s{i}.mp3"), "wb") as f:
            async for parte in com.stream():
                if parte["type"] == "audio":
                    f.write(parte["data"])
                elif parte["type"] == "WordBoundary":
                    palavras.append((parte["offset"] / 1e7, parte["text"]))
        saida.append({"text": texto, "words": palavras})
        print(f"trecho {i + 1} de {len(TRECHOS)} ok")
    with open(os.path.join(PASTA, "segs.json"), "w", encoding="utf-8") as f:
        json.dump(saida, f, ensure_ascii=False)
    with zipfile.ZipFile("voz-anuncio.zip", "w") as z:
        for nome in sorted(os.listdir(PASTA)):
            z.write(os.path.join(PASTA, nome), nome)
    print("Pronto: envie o arquivo voz-anuncio.zip na sessão.")


asyncio.run(main())
