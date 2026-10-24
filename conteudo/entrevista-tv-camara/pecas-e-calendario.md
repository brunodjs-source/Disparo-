# Entrevista à TV Câmara Campinas · peças prontas, legendas e calendário

Rodada de 24/10/2026. Fonte: gravação de 35:21 (bastidor de 0:00 a 14:30, programa de 14:35 a 29:50, imagens do Bruno no computador depois). Transcrição medium conferida em 2 passes nos trechos usados. O "min" do rótulo conta a partir da abertura do programa.

## Antes de publicar qualquer peça
Atualização de 24/10: a Mirna liberou o uso ("pode seguir", dito ao Bruno) e o programa **vai ao ar na segunda-feira, 02/11/2026** (horário sem dado). O Bruno marca a Mirna nas postagens pelo app (o PostZen não marca pessoa em reel, carrossel nem story). Falta guardar a liberação por escrito (print da conversa).

1. **Autorização da Mirna Abreu por escrito**, de uso de imagem e voz nas redes do Bruno. Ela aparece no plano aberto da mesa (Z2) em quase todas as peças, e a voz dela entra em MANCHETE 01 e em CINEMA 01.
2. **Data de exibição do programa.** Antes dela, só com o ok da produção.
3. Sem autorização: as fichas trocam os planos para CB (só o Bruno) e cortam a voz dela. A troca é só no JSON da ficha (`planos` e `seg`), sem refazer o modelo.
4. Segurança: devolver o arquivo "Entrevista tv câmara.mov" do Drive para **Restrito** e apagar o rascunho de release `entrevista-tv-camara` do GitHub (o repositório é público). Os vídeos e a transcrição não vão para o git.

## Peças

| Id | Formato | Trecho (gravação) | Min do programa | Duração | O que tem |
|---|---|---|---|---|---|
| pb01 | P&B | 16:26 a 16:44 | 01:51 | 19,5 s | "Não foi uma aventura. Acabou sendo uma profissão por 20 anos." Frase acendendo, quietude e punch-in na virada, marca-texto em "profissão", cartão final |
| pb02 | P&B | 17:52 a 18:17 | 03:17 | 26,7 s | Restaurante de 45 mil para 250 mil. Marca-texto em "250 mil" |
| ci01 | CINEMA | 22:58 a 23:32 | 08:22 | 36,6 s | Strobo de fonte de cinema, "O MELHOR MARKETING", "OURO" cai na barra e a cor volta. Voz da Mirna em 2 perguntas curtas |
| po01 | PONTOS | 26:48 a 27:08 | 12:13 | 23,7 s | Método Xeque-Mate: GATILHOS, XEQUE-MATE, JOGADA, POSICIONAMENTO, MOMENTO formados em pontos no instante da fala, lista final |
| tl01 | TIMELAPSE | gravação inteira | | 36,5 s | 35 minutos em 35 segundos, relógio, 6 andares de assunto, o 5 escondido como laço até o pouso em "ouro", índice na torre |
| tl02 | TIMELAPSE 2 | gravação inteira | | 35,4 s | Empreender, cases só com nicho e valor e família no fim. Laço "eu construí patrimônio, eu construí..." pago em "família"; reacts reais: risada dos dois em câmera lenta e o "O que?" da Mirna; hip-hop-02 |
| tl03 | TIMELAPSE 3 · A pergunta da TV | 25:16 a 25:40 e bastidor | | 36 s | Pergunta "Você foi investir em equipamento?" fixa no topo, cronômetro contando para trás até a resposta; react: risada dos dois em tela dividida "ao mesmo tempo"; trap-electro-vibes |
| tl04 | TIMELAPSE 4 · De trás pra frente | gravação inteira ao contrário | | 34,4 s | Fita rebobinando do fim ao 00:00, paradas de 5 a 1 (ensinar empresários, realidade de hoje, quebrar a objeção, pai que estimulava, pai pioneiro); react: "Uau!" em replay; close-up |
| tl05 | TIMELAPSE 5 · A régua do tempo | 17:03 a 23:03 | | 35,3 s | Marketing de antes e de hoje numa régua de anos (antes, 2015, pandemia, hoje); react: "Ainda?" congelado com carimbo; CTA SIM ou NÃO; uplifting-bass |
| pf01 | PROFISSAO (dentista) | 20:28 a 20:49 | 05:52 | 24 s | Franquia odontológica, faixa "NA TV" que para na frase, CTA de envio |
| mc01 a mc04 | MANCHETE (stories) | vários | | 4,6 a 11,5 s | Loop com faixa "NA TV" e ticker de outras frases |
| car01 | CARROSSEL | 4 frases | 03:29, 08:33, 11:45, 13:45 | 6 lâminas 4:5 | Capa "Eu só tinha um computador e um sonho." com círculo na câmera da TV; vigas 250 MIL, OURO, PRODUTO, FAMÍLIA que atravessam a borda e passam atrás da cabeça; lista na torre |

Arquivos renderizados: `scratchpad/tv/render/<id>.mp4` e `scratchpad/tv/car01/lamina-N.png` desta sessão (temporário; já enviados no chat). Fichas para refazer: `videos/tv-camara/cortes/<id>.spec.json`; carrossel: `videos/tv-camara/carrossel/car01.html` com `cap_car.js`.

## Legendas (prontas para colar)

Regras do CLAUDE.md conferidas: sem travessão, sem emoji, sem promessa de resultado, no máximo uma frase "não é X, é Y".

**pb01**
> Fui DJ por 20 anos. Na entrevista à TV Câmara Campinas eu contei por que isso nunca foi uma aventura.
> Antes do digital, eu aprendi como funcionava a noite, as casas e as festas. Foi ali que comecei a fazer estratégia de divulgação, muito antes de chamar isso de lançamento.
> Manda para um expert que vai lançar este ano.
> #estrategistadelancamento #lancamento #marketingdigital #empreendedorismo #campinas

**pb02**
> Um restaurante que vendia 45 mil. Colocamos ele para vender 250 mil com o marketing digital.
> Contei esse caso na TV Câmara Campinas. O número de um caso não se repete igual em outro negócio. O que se repete é a ordem: entender o produto antes de anunciar.
> Vai lançar nos próximos 90 dias? Me manda a data no direct.
> #estrategistadelancamento #marketingdigital #restaurante #empreendedorismo #campinas

**ci01**
> Até hoje o melhor marketing é o olho no olho.
> Na TV eu disse que nem tudo que vemos é ouro. Muita gente vende o que não consegue cumprir, e o cliente chega machucado. Por isso o encontro ainda decide a venda.
> E você, o que teria respondido?
> #estrategistadelancamento #marketingdigital #vendas #empreendedorismo #campinas

**po01**
> O Método Xeque-Mate do jeito que eu expliquei na TV: os gatilhos corretos, cada jogada, cada posicionamento e o momento certo.
> Qual dessas peças falta no seu lançamento? Comenta a palavra.
> Salva para conferir antes do próximo lançamento.
> #metodoxequemate #estrategistadelancamento #lancamento #marketingdigital #estrategia

**tl01**
> 35 minutos de gravação em 35 segundos. Bastidor da minha entrevista à TV Câmara Campinas.
> 1 Desde criancinha (min 00:47)
> 2 Profissão por 20 anos (min 01:42)
> 3 45 mil para 250 mil (min 03:29)
> 4 Franquia odontológica (min 05:59)
> 5 Nem tudo que vemos é ouro (min 08:33)
> 6 Zero reais (min 10:30)
> 7 Método Xeque-Mate (min 12:17)
> Comenta o número do assunto que você quer ver inteiro. O mais votado sai no próximo sábado.
> #bastidores #estrategistadelancamento #entrevista #marketingdigital #campinas

**tl02**
> Parte 2 do bastidor da minha entrevista à TV Câmara Campinas: empreender, os cases e o que mais importa.
> 1 Com 9 anos de idade (min 00:57)
> 2 Restaurante · 250 mil (min 03:37)
> 3 Odontologia · 1,5 milhão (min 06:11)
> 4 Zero reais (min 10:33)
> 5 Eu construí família (min 13:49)
> 6 Ser empreendedor (min 14:16)
> 7 Famílias felizes (min 15:02)
> Comenta o número do assunto que você quer ver inteiro.
> #empreendedorismo #estrategistadelancamento #bastidores #familia #campinas

**tl03**
> Você foi investir em equipamento? A pergunta da TV e a minha resposta, com o cronômetro correndo.
> Comenta o seu primeiro investimento.
> #empreendedorismo #estrategistadelancamento #bastidores #marketingdigital #campinas

**tl04**
> A entrevista de trás pra frente: do fim da gravação até o 00:00, parando nos 5 momentos que explicam de onde eu vim.
> Comenta o número da parada que você quer ver inteira.
> #bastidores #estrategistadelancamento #entrevista #empreendedorismo #campinas

**tl05**
> O marketing de antes e o de hoje. Banners, outdoors, panfletos, a ascensão do digital desde 2015, a pandemia. E o que até hoje é o melhor marketing.
> Comenta SIM ou NÃO: o tête-à-tête ainda é o melhor marketing?
> #marketingdigital #estrategistadelancamento #vendas #empreendedorismo #campinas

**pf01** (stories da tarde na terça, dia do nicho dentista; reel só se o Módulo 7 mandar DOBRAR profissão nomeada)
> Dentista, esse case eu contei na TV: uma franquia odontológica muito famosa, um projeto com o diretor de marketing, e saímos de lá com um milhão e meio de faturamento em dois meses.
> Resultado de um caso não vale como promessa para outro. O que eu mostro é o caminho: estratégia antes do anúncio.
> Manda para um dentista que precisa ouvir isso.
> #dentista #odontologia #marketingodontologico #estrategistadelancamento #campinas

**car01** (terça 27/10, 12h)
> Eu só tinha um computador e um sonho. Quatro frases que eu disse na entrevista à TV Câmara Campinas, com o minuto de cada uma.
> Qual delas pesa mais no seu próximo lançamento? Comenta o número.
> Vai lançar nos próximos 90 dias? Me manda a data no direct.
> #estrategistadelancamento #lancamento #marketingdigital #empreendedorismo #campinas

**Manchetes nos stories** (sem legenda; sticker)
- mc01 "Eu só tinha um computador e um sonho": caixa "Me pergunta sobre isso" (tem a voz da Mirna).
- mc02 "Hoje eu sou estrategista de marketing digital e lançamento de produto": enquete "Você sabia?".
- mc03 "Cada cliente tem um produto específico e a gente vive esse produto": enquete "Concorda?".
- mc04 "Eu construí patrimônio, eu construí família": caixa "Qual foi a sua virada?".

## Calendário agendado no PostZen (horário de São Paulo)

Hashtags cortadas para 5 em todas as legendas (o Buzzfy marcou 6 ou mais). Stories saem sem sticker pelo PostZen: enquete e caixa de pergunta entram à mão no app.

| Data | Hora | Peça | Tipo | Id no PostZen |
|---|---|---|---|---|
| sáb 24/10 | 14h00 | st01 bastidor (15 s, anuncia o timelapse de amanhã) | story | m1763qsxtry2ctpf67rj8y0bpd8gxdz4 |
| sáb 24/10 | 14h03 | estático de bastidor | story | m17akrbjzae47yr9qrg1btznf58gwwhz |
| sáb 24/10 | 15h00 | estático "A pergunta da TV" | story | m17fqwrdv5ztfhm5jcd328jcn98gx24w |
| sáb 24/10 | 15h01 | mc01 (a resposta) | story | m179np4c1txva7w5qe3pnyegm18gx0hm |
| dom 25/10 | 18h30 | **tl01** | reel | m171tvpw4z0c0rxz7fpak824bd8gx35v |
| seg 26/10 | 21h | **pb01** | reel | m17dqk63b0e1hk75xcevdwmc458gwmfn |
| ter 27/10 | 12h | **car01** (6 lâminas) | carrossel | m174q9y41reqfn4eqhqrm124f58gwzbr |
| ter 27/10 | 16h | **pf01** (dia do nicho dentista) | story | m17empvbrp604edk3wzpmxzmj58gw00w |
| qua 28/10 | 21h | **ci01** | reel | m177cf21jjcv7fa2y1q1twc4n58gwe0n |
| qui 29/10 | 21h | **po01** | reel | m17ersdnwmmsk5e7fyw4jqwfdx8gwcxt |
| sex 30/10 | 21h | **pb02** | reel | m1718n57yvmtpyb4xnf3zsw7fn8gwe7q |
| sáb 31/10 | 18h30 | **tl02** (legenda avisa a exibição de segunda) | reel | m171fp82kqkbcw5h3xggewpev18gwe2g |
| sáb 07/11 | 18h30 | **tl03** | reel | m17fbsgpqmam5e83vhtaxwcgsn8gwpjr |
| sáb 14/11 | 18h30 | **tl04** | reel | m17bwhfnzsvax8d8bsjtas6yed8gxkez |
| sáb 21/11 | 18h30 | **tl05** | reel | m175r38ys7zcrmnd1nzcfhkj458gw4fw |

Mudanças de 24/10 depois da data de exibição: o story das 19h30 de hoje ("Nem tudo que vemos é ouro") passou a ter o rótulo "NA TV · SEGUNDA, 02/11"; a legenda do tl01 avisa a exibição e troca "o mais votado sai no próximo sábado" por "o mais votado eu solto inteiro depois que a entrevista for ao ar". Os cortes de 26 a 30/10 estão antes da exibição: o conselho do modo GOD decide se ficam ou se vão para depois de 02/11.

Regra para tl03 a tl05: se o anterior ficar abaixo de 0,8x da mediana ou com pulo acima de 75%, o seguinte sai do sábado e volta para o banco (Módulo 7 decide).

| Quando | Peça |
|---|---|
| seg 02/11 | dia da exibição: chamada para assistir nos stories (a definir no conselho) |
| seg 02/11 | Módulo 7 com a semana inteira da série |
| stories da manhã | mc02, mc03, mc04 (um por dia) |

Portão, medição e regras de PARAR / DOBRAR: seção 8 do `catalogo-formatos.md`.

## O que falta produzir
- REACT 01 a 03: precisa de 20 minutos de selfie (6 reacts e 12 aberturas "Isso eu falei na TV.").
- CARROSSEL 02 a 04 e PERGUNTA 01 e 02.
- Banco: MITO ("até hoje é o melhor marketing?"), pb03 ("eu construí tudo"), CINEMA 02.
