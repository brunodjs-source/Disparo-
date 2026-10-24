# Entrevista à TV Câmara Campinas · peças prontas, legendas e calendário

Rodada de 24/10/2026. Fonte: gravação de 35:21 (bastidor de 0:00 a 14:30, programa de 14:35 a 29:50, imagens do Bruno no computador depois). Transcrição medium conferida em 2 passes nos trechos usados. O "min" do rótulo conta a partir da abertura do programa.

## Antes de publicar qualquer peça (bloqueia tudo)
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
> #estrategistadelancamento #lancamento #marketingdigital #empreendedorismo #campinas #carreira

**pb02**
> Um restaurante que vendia 45 mil. Colocamos ele para vender 250 mil com o marketing digital.
> Contei esse caso na TV Câmara Campinas. O número de um caso não se repete igual em outro negócio. O que se repete é a ordem: entender o produto antes de anunciar.
> Vai lançar nos próximos 90 dias? Me manda a data no direct.
> #estrategistadelancamento #marketingdigital #restaurante #empreendedorismo #campinas #estrategia

**ci01**
> Até hoje o melhor marketing é o olho no olho.
> Na TV eu disse que nem tudo que vemos é ouro. Muita gente vende o que não consegue cumprir, e o cliente chega machucado. Por isso o encontro ainda decide a venda.
> E você, o que teria respondido?
> #estrategistadelancamento #marketingdigital #vendas #confianca #empreendedorismo #campinas

**po01**
> O Método Xeque-Mate do jeito que eu expliquei na TV: os gatilhos corretos, cada jogada, cada posicionamento e o momento certo.
> Qual dessas peças falta no seu lançamento? Comenta a palavra.
> Salva para conferir antes do próximo lançamento.
> #metodoxequemate #estrategistadelancamento #lancamento #marketingdigital #estrategia #infoproduto

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
> #bastidores #estrategistadelancamento #entrevista #marketingdigital #campinas #empreendedorismo

**pf01** (stories da tarde na terça, dia do nicho dentista; reel só se o Módulo 7 mandar DOBRAR profissão nomeada)
> Dentista, esse case eu contei na TV: uma franquia odontológica muito famosa, um projeto com o diretor de marketing, e saímos de lá com um milhão e meio de faturamento em dois meses.
> Resultado de um caso não vale como promessa para outro. O que eu mostro é o caminho: estratégia antes do anúncio.
> Manda para um dentista que precisa ouvir isso.
> #dentista #odontologia #marketingodontologico #estrategistadelancamento #clinica #campinas

**car01** (quarta 28/10, 12h)
> Eu só tinha um computador e um sonho. Quatro frases que eu disse na entrevista à TV Câmara Campinas, com o minuto de cada uma.
> Qual delas pesa mais no seu próximo lançamento? Comenta o número.
> Vai lançar nos próximos 90 dias? Me manda a data no direct.
> #estrategistadelancamento #lancamento #marketingdigital #empreendedorismo #campinas #frases

**Manchetes nos stories** (sem legenda; sticker)
- mc01 "Eu só tinha um computador e um sonho": caixa "Me pergunta sobre isso" (tem a voz da Mirna).
- mc02 "Hoje eu sou estrategista de marketing digital e lançamento de produto": enquete "Você sabia?".
- mc03 "Cada cliente tem um produto específico e a gente vive esse produto": enquete "Concorda?".
- mc04 "Eu construí patrimônio, eu construí família": caixa "Qual foi a sua virada?".

## Calendário (encaixado no catálogo; nichos às 21h intocados)

| Data | Hora | Peça | Condição |
|---|---|---|---|
| ter 27/10 a sex 30/10 | manhã | stories: mc02, mc03, mc04 (um por dia) e 5 s do timelapse | data de exibição ou ok da produção |
| qua 28/10 | 12h | **car01** | idem (a capa mostra a Mirna) |
| sáb 31/10 | 18h30 | **pb01** (abre a série; o REACT espera a selfie) | autorização da Mirna; sem ela, versão CB |
| seg 02/11 | | Módulo 7 com 48 h do pb01 | |
| sáb 07/11 | 18h30 | **tl01** e enquete igual nos stories | autorização |
| dom 08/11 | 18h30 | **pb02** | só com o portão aberto |
| ter 10/11 | tarde | **pf01** nos stories (dia do nicho dentista) | |
| sáb 14/11 | 18h30 | PERGUNTA 01 (a fazer, depende da autorização) ou ci01 | |
| dom 15/11 | 18h30 | **ci01** | portão e autorização |
| dom 22/11 | 18h30 | **po01** | portão |
| stories da manhã | | mc01 quando houver autorização | |

Portão, medição e regras de PARAR / DOBRAR: seção 8 do `catalogo-formatos.md`.

## O que falta produzir
- REACT 01 a 03: precisa de 20 minutos de selfie (6 reacts e 12 aberturas "Isso eu falei na TV.").
- CARROSSEL 02 a 04 e PERGUNTA 01 e 02.
- Banco: MITO ("até hoje é o melhor marketing?"), pb03 ("eu construí tudo"), CINEMA 02.
