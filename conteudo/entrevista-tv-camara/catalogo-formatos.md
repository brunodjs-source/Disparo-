# Catálogo de formatos · Entrevista à TV Câmara Campinas

Decisão do presidente em 23/10/2026, fundindo os catálogos dos 2 juízes e conferindo cada formato contra o material real, o motor do dentista, o custo de render, o CLAUDE.md e o PDF de 42 efeitos.

- Material: bastidor gravado no celular (35 min 21 s) da entrevista do Bruno à repórter Mirna Abreu.
- Status: aguardando o passe de áudio, a transcrição palavra a palavra (Whisper) e o passe de vídeo. Nenhum trecho foi escolhido ainda: os critérios de trecho de cada ficha rodam sobre a transcrição.
- Regra de leitura: **fato** é o que foi medido ou visto no arquivo; **hipótese** é previsão. Métrica que falta está escrita como "sem dado".

---

## 1. Tabela-resumo (ordem de produção)

A ordem segue a data em que cada peça precisa estar pronta e, no empate, a nota. O kit comum (Nome e cargo, Legenda Gigante, Marca-texto, Punch-in, Look Cinemático, Title Card) é construído antes de todos, na semana 0.

| Ordem | Formato | Origem | Duração | Footage principal | Depende de | Qtd no ciclo | Nota | Primeira saída |
|---|---|---|---|---|---|---|---|---|
| 1 | REACT · O que eu não disse na TV | Extra (amplia o "react" pedido, com o rosto) | 30 a 38 s | selfie nova + Z2 ou CB | 20 min de selfie (6 reacts) | 3 | 9 | sáb 31/10, 18h30 |
| 2 | STORIES · Diário da entrevista | Extra | 3 a 4 telas por dia, até 15 s | todos | nada | 28 dias | 7 | ter 27/10 |
| 3 | CARROSSEL · O que eu disse na TV | Extra | 6 lâminas 1080x1350 | stills do 4K em P&B | transcrição | 4 | 6,5 | qua 28/10, 12h (se a transcrição fechar na seg 26) |
| 4 | MANCHETE · frase em loop | Extra | 7 a 10 s | CB | transcrição | 8 | 6,5 (story) | seg 02/11 (stories da manhã) |
| 5 | TIMELAPSE · 35 minutos em 35 segundos | **Pedido** | 34 a 36 s | ABERTO a cerca de 100x + Z2 + selfie opcional | passe de vídeo completo e capítulos | 1 | 6,5 | sáb 07/11, 18h30 |
| 6 | PB · Corte P&B "NA TV" | **Pedido** | 20 a 35 s | Z2 e CB em P&B (+1,5 s de selfie na versão A) | transcrição | 3 | 7,5 | dom 08/11, 18h30 (portão) ou sáb 14/11 |
| 7 | PERGUNTA · A TV perguntou | Extra | 25 a 40 s | Z2 + CB + CM | autorização da Mirna | 2 | 7,5 (6 sem autorização) | sáb 14/11, 18h30 |
| 8 | CINEMA · fonte de cinema, strobo e react | **Pedido** | 22 a 30 s | CB e Z2 + CM a 0,5x do 4K60 | autorização + trecho com reação | 2 | 7 (6 sem autorização) | dom 15/11, 18h30 (portão) |
| 9 | PONTOS · chuva de pontos escrevendo o assunto | **Pedido** | 25 a 32 s | Z2 com parede escurecida | trecho com 3 a 5 conceitos | 1 | 6 | dom 22/11, 18h30 (portão) |
| 10 | SALA · a parede da entrevista vira letreiro | Extra | 25 a 35 s | Z2 + CE | máscara de 2 pessoas; teste de 30 quadros | 1 | 6,5 | banco (semana 5 em diante) |
| 11 | PROFISSAO · o que eu disse na TV para o [profissional] | Extra | 20 a 28 s | Z2 + CB | trecho sobre profissão, sem trocar palavra | 2 | 6,5 | stories da tarde no dia do nicho; reel só com DOBRAR |
| 12 | MITO · verdade ou mito | Extra | 18 a 28 s | Z2 em P&B + CB em cor | crença dita e rebatida por ele | 1 | 6 | banco |

Saíram como formato próprio: o reel BASTIDOR ("fiquei atrás do monitor"), absorvido pelo REACT 01, pela abertura do TIMELAPSE e pelos stories de pré-estreia (era um segundo trailer, e o humor só funciona uma vez); o Feed de Reels recriado, o Mapa com pino e a Notificação (somam efeito sem somar retenção); o reel de votação (vira enquete nativa nos stories, porque a conta teve 12 comentários em 30 dias).

---

## 2. O que o material permite (verificado em 23/10)

**Arquivo (fato)**
- Fonte: HEVC Main 10, 10 bits, 3840x2160 com rotação (vertical 2160x3840), 59,94 fps, **HDR HLG** (bt2020, arib-std-b67), 2.121 s, cerca de 22 GB no Drive.
- Disco livre: 17 GB. A fonte não cabe: o passe de vídeo lê em fluxo (como o `puxar.sh` e o `converter.sh` fizeram) e grava só os proxies.
- Hoje existem só 9,6 s convertidos (`full.mp4`, `zoom.mp4`, `audio.wav`), no scratchpad, que some com a sessão. A conversão de teste não fez tonemap: HLG lido como SDR fica lavado.
- Velocidade medida na conversão de teste: 0,18x com 4 CPUs e 2 saídas. O passe completo leva cerca de 3 h 15 min, mais com o tonemap. É feito **uma vez**, em segundo plano.
- Áudio da amostra: média -37,8 dB, pico -22,6 dB. Transcrevível (a amostra já gerou `words.json`). Há 6 modelos arnndn (.rnnn) no scratchpad.
- faster-whisper não está instalado (há um wheel em `/tmp/fwtest`, também temporário). rembg 2.0.85 e librosa 0.11 estão no `cbenv` do scratchpad (temporário).

**Imagem (fato, quadro de 900 s)**
- Mirna à esquerda da mesa, de frente para a câmera (olhando para baixo nesse quadro). Bruno à direita, **em 3/4 olhando para a Mirna, com o rosto visível acima do monitor**; o corpo fica atrás do monitor e encosta na borda direita do quadro. O briefing fala em perfil e quase de costas: a folha de contato de 1 quadro por minuto decide em quais trechos o rosto aparece.
- Parede cinza clara livre acima das cabeças. Mesa branca em toda a metade de baixo. Sombra da cabeça na parede, entre os dois.
- Quadro PLANEJAMENTO MENSAL cortado na borda esquerda, com cerca de 400x410 px no 4K, fora do Z2.
- Câmera da TV cortada na borda esquerda, sem logo legível nesse quadro. Primeiro plano: laptop escuro à esquerda e o gravador à direita, com texto de marca nos botões. Monitor com etiqueta e marca no verso. Mirna com um broche ou microfone de lapela no peito.

**Ambiente de render (fato)**
- Fontes: Inter Display (todas as espessuras, inclusive Black), Cinzel e Playfair itálico (`videos/ads/a01-campinas/fonts`), Playfair TTF, DejaVu Sans Mono. Helvetica Neue não existe: o `dent.html` cai para a Liberation Sans. Os formatos novos declaram `font-family:"Inter Display"; font-weight:900`.
- SFX em `videos/nichos/dentista/sfx`: coin, ding_si, impact, pop, riser, shutter, sub, swipe, tick, typing, whoosh. O `PICO` do `mix.py` só mede 4 (whoosh, riser, swipe, typing).
- Trilhas em `videos/musicas`: close-up, complicated, deep-urban, hazy-after-hours, hip-hop-02, like-a-loop-machine, trap-electro-vibes, uplifting-bass.
- O `tv.html` já tem o path SVG da torre (o logo): serve de silhueta no fecho do TIMELAPSE e na lâmina final do CARROSSEL. Não precisa desenhar.

**Horários (fato, Buzzfy `ig_best_times`, 23/10, fuso de São Paulo)**
- Seguidores online: pico às 18h (428) e 19h (423); 21h com 416. Recomendação da ferramenta: postar entre 18h e 20h.
- Posts próprios por hora: 21h com média de 72 de alcance (5 posts), 12h com 65 (4), 18h com 49 (6). Por dia: quarta 102 (3 posts), domingo 70 (4). Melhor post do período: domingo às 18h29 (169). Sábado: sem dado.
- Mediana nos últimos 25 posts: 34. A mediana oficial do Módulo 1 é 53 (17 reels). O Módulo 7 de 02/11 atualiza a mediana, e o portão usa a atualizada.

---

## 3. Recortes fixos (câmera parada: medir uma vez num quadro)

| Nome | Região no 4K vertical (2160x3840) | Saída | O que mostra | Limite |
|---|---|---|---|---|
| ABERTO | quadro inteiro | 1080x1920 (0,5x) | sala, câmera da TV, quadro, gravador, os dois pequenos (cabeças com cerca de 90 px) | nunca em janela pequena; nunca abre reel |
| Z2 | x 1080 a 2160, y 1000 a 2920 | 1080x1920 nativo (1:1) | os dois; Bruno na borda direita (x 670 a 1080 do Z2), rosto perto de (760, 870); parede livre de y 100 a 850; mesa de y 1200 para baixo | punch-in até 1,12 |
| CB | dentro do Z2: x 309 a 1080, y 250 a 1621 (771x1371) | ampliado 1,4x | Bruno em 3/4, rosto a cerca de 45% da altura, respiro à esquerda; monitor cobre o peito | punch-in até 1,08 (teto de 1,5x sobre o 4K) |
| CM | dentro do Z2: x 0 a 771, mesma altura | ampliado 1,4x | Mirna a cerca de 32% da largura, olhando para a direita | só com autorização; no máximo 25% do tempo; nunca abre reel |
| CE | x 0 a 1080, y 900 a 2820 | 1080x1920 nativo | quadro de planejamento (cerca de 400x410 px), porta, lambri azul, câmera da TV | detalhe; nunca o quadro em tela cheia (seria 4,6x) |

CB e CM saem do proxy Z2, que já está em resolução nativa. Só a câmera lenta do CINEMA volta à fonte de 60 fps.

**Desfoque fixo (BLUR_RECTS no compositor):** marca nos botões do gravador, marca e etiqueta no verso do monitor, adesivo do laptop, broche ou microfone de lapela da Mirna (se tiver logo), qualquer logo da emissora na câmera ou no microfone. Conferir em 20 quadros espalhados. Conferir se o celular mexeu: correlação de fase do quadro 0 com 1 quadro a cada 5 min; se mexeu, um conjunto de retângulos por trecho.

---

## 4. Pipeline comum e custo de render

**Pré-requisitos que bloqueiam (fazer agora)**
1. Pedir hoje (sex 23/10) à Mirna, por escrito, a autorização de uso de imagem e voz e a data de exibição da entrevista. Prazo de resposta: qua 04/11. Sem autorização: CM, voz dela e PERGUNTA com voz saem; o ABERTO e o Z2 só com a região dela desfocada. Antes da data de exibição, publicar só com o ok da produção.
2. Copiar do scratchpad para `videos/tv-camara/engine/` os modelos arnndn e os scripts de conversão (o scratchpad some com a sessão).
3. Instalar faster-whisper no ambiente do repo.

**Passos**
1. **Áudio primeiro** (só demux, sem decodificar vídeo, limitado pela rede). Cadeia de voz: highpass 90 Hz, arnndn (testar std e cb), afftdn de 10 a 18 dB se ainda sobrar chiado, compressor 3:1, +3 dB em 3 kHz, dynaudnorm por turno. Ouvir em fone e aliviar se a voz ficar metálica: voz processada demais lembra a voz sintética que falhou. Master final pelo `mix.py` (-14 LUFS, TP -1,5).
2. **Whisper** large-v3 int8, tempo por palavra, português. Estimativa de cerca de 1 h em 4 CPUs (hipótese: medir). Revisão humana dos acentos nos trechos escolhidos.
3. **Passe único de vídeo** em segundo plano, lendo em fluxo: `zscale` linear, `tonemap=hable`, `zscale` bt709, e daí `split` em ABERTO 30 fps, Z2 30 fps e ABERTO 3 fps (timelapse). Comparar 1 quadro com o `nat900.jpg` antes de seguir. Proxies em disco no repo (estimativa de 4 a 6 GB, cabem nos 17 GB).
4. **Diarização:** F0 mediana por segmento do Whisper (librosa.pyin), conferida pelo "?" e por revisão humana.
5. **Folha de contato:** 1 quadro por minuto do Z2 (35 quadros), para marcar onde o rosto do Bruno aparece em 3/4.
6. **`pontuar.py`** (filtro de frase, abaixo) gera `capitulos.json` e `cortes.csv`.
7. **Motor** em `videos/tv-camara/engine/`, cópia generalizada do dentista: `cap.js` lê do `corte.json` o número de quadros, o viewport (1080x1920 ou 1080x1350) e as camadas, e pula a camada back nos quadros em que `render` volta vazio; `comp.py` escolhe a base por plano (ABERTO, Z2, CB, CM, CE), aplica P&B por intervalo, curva em S, grão, vinheta, dodge & burn, BLUR_RECTS, punch-in pelo centro medido e máscara dos **2** maiores componentes (hoje só o maior); `mix.py` lê eventos, duração, quietude e trilha do JSON, e o `PICO` passa a ter os 11 SFX medidos.
8. **Revisão em toda peça:** tabela de segundo, frase e efeito aprovada antes de construir (Prompt 2); folha com 4 quadros por segundo e nota por efeito, refazendo o que tirar menos de 8 (Prompt 5); as 6 conferências do "Antes de postar".

**Filtro de frase (`pontuar.py`, vale para todos)**
- Entra: frase do Bruno pela diarização, de 6 a 30 palavras.
- +3 número dito por ele; +3 profissão nomeada (médico, dentista, advogado, nutricionista, psicólogo, consórcio); +2 contradição ("mas", "só que", "na verdade", "o problema", "ninguém", "todo mundo acha"); +2 personagem (cliente, case Tzur); +1 até 14 palavras; +1 começa autônoma (sem "então", "isso", "aí", "ele", "como eu falei"); +1 probabilidade média do Whisper de 0,8 ou mais; +2 rosto em 3/4 na folha de contato; -2 de costas.
- -5 voz da Mirna por cima; -5 ruído alto depois do tratamento.
- Exclusão total: promessa de resultado ("garanto", "vai faturar", "com certeza vende"), os nomes proibidos do CLAUDE.md e frase contra o posicionamento (ensinar a lançar, fórmula pronta).
- Cada trecho vai a no máximo 2 peças (1 reel e stories ou carrossel).

**Custo de render** (fato: cerca de 0,3 s por quadro por camada em 1080x1920; o resto é estimativa)

| Formato | Camadas | Capturas | Captura | Extra |
|---|---|---|---|---|
| Passe de vídeo (uma vez) | | | | cerca de 3 h 15 min a 0,18x, mais com tonemap |
| REACT 35 s | front + back só no letreiro | cerca de 1.200 | 6 min | rembg na selfie só no trecho do letreiro (cerca de 150 quadros) |
| PB 30 s | front | 900 | 4,5 min | grão e dodge & burn no comp.py |
| PERGUNTA 35 s | front | 1.050 | 5,3 min | |
| CINEMA 25 s | front | 750 | 3,8 min | 1 a 2 trechos de 1 s lidos da fonte 4K60 por seek |
| TIMELAPSE 35 s | front | 1.050 | 5,3 min | remapeamento do proxy de 3 qps e tmix no ffmpeg; sem máscara |
| PONTOS 30 s | front (canvas) | 900 | 4,5 min | amostragem de cada palavra uma vez; testar 6 quadros antes |
| SALA 35 s | back + front | 2.100 | 10,5 min | rembg de 1.050 quadros a 360x640 (estimativa de 10 a 15 min) |
| MANCHETE 8 s | front | 240 por peça | 1,2 min por peça (8 peças: 10 min) | |
| CARROSSEL | 6 capturas 1080x1350 | 6 | segundos | |
| PROFISSAO e MITO 25 s | front | 750 | 3,8 min | |

O compositor soma cerca de 0,1 a 0,2 s por quadro (hipótese: medir no primeiro render).

---

## 5. Regras que valem para todos

- **Efeitos:** camadas de base (legenda, look, barra de progresso, selo fixo, rótulo de minuto) não contam. Todo o resto é efeito novo e fica a **2 s ou mais** do efeito anterior. Cada efeito começa na palavra que ilustra, pelo tempo do Whisper, nunca antes. Se duas ênfases caem na mesma palavra, fica uma.
- **Bruno em cena desde o quadro 0** em todo reel (CLAUDE.md): selfie, CB ou Z2. Nunca abrir na Mirna sozinha, no ABERTO ou num cartão sem ele.
- **Texto fiel:** só sai vício de fala ("né", "tipo"). Nada reescrito, nenhuma citação inventada. O minuto real aparece como prova.
- **Zona segura:** texto entre y 220 e 1450 e entre x 60 e 940. Nada sob os botões do app (x acima de 940, y de 1100 a 1750) nem no rodapé (y acima de 1600).
- **Contraste:** a parede é cinza clara e a mesa é branca. Texto branco só sobre caixa #141210 ou sobre parede escurecida por gradiente. Ouro só como marca-texto atrás de texto escuro ou sobre fundo escuro.
- **Fotossensibilidade:** no máximo 3 clarões por segundo, nenhum branco puro em tela cheia, nenhum vermelho saturado.
- **Banidos:** lens flare, neon, RGB split, tremida de câmera (exceto os 3 quadros do carimbo), brilho em volta de ponto, ouro com bisel, logo de terceiros, logo ou cores da TV Câmara, ícones ou marca do Instagram em interface recriada. A emissora aparece só em texto: "Entrevista à TV Câmara Campinas".
- **Copy (CLAUDE.md):** português do Brasil, sem travessão, sem emoji, sem promessa de resultado, sem os nomes proibidos, no máximo uma frase "não é X, é Y" por peça.
- **Palavra-chave:** TABULEIRO só em post que passou de 150 de alcance em 48 h, conferido no `ig_post_stats`, e só uma palavra-chave por mês.

---

## 6. Identidade fixa (6 efeitos em todas as peças)

É a combinação "Depoimento de cliente" do PDF (Nome e cargo, Legenda Gigante, Marca-texto na palavra, Look Cinemático, Title Card) mais o Punch-in do "Bastidor e rotina".

1. **Nome e cargo com a prova da TV.** Caixa #141210 a 88% com filete ouro #E8B36A que cresce antes do texto (o `lowerThird` do dent.html): "Bruno" em Inter Display Black, "Estrategista de Lançamento" em Playfair itálico ouro, "Entrevista à TV Câmara Campinas" em Inter SemiBold 24 px. Em x 56, entre y 1240 e 1400, sobre a mesa e sempre em caixa. Entra no primeiro intervalo livre de 2 s depois do gancho, até os 8 s. Só texto: sem logo, vinheta ou cores da emissora.
2. **Legenda Gigante** palavra a palavra pelo Whisper revisado. Grupos de 1 a 3 palavras em caixa #141210 de cantos levemente arredondados; palavra principal enorme em Inter Display Black, complemento em Playfair itálico; pop de 104% para 100% em 3 quadros; palavra ativa em #F5C46E. Fica no terço superior (y 230 a 700) o vídeo inteiro. Com áudio de celular captado de longe, é ela que faz o vídeo funcionar sem som. Exceções: no PB vira texto simples sobre a parede escurecida; no CINEMA vira legenda de cinema dentro da barra de baixo.
3. **Marca-texto na palavra.** Uma única palavra-chave por peça. Traço #E8B36A de borda irregular passa atrás dela em 0,3 s, no tempo exato da fala, com o texto em #141210 por cima. Assinatura sonora: um único ding_si por peça, nesse momento.
4. **Punch-in na virada** (entre 12 e 15 s). De 1,00 a 1,12 em 4 quadros no Z2, ou de 1,00 a 1,08 no CB, centrado na cabeça do Bruno (centro medido uma vez, câmera parada), voltando em 8 quadros. Mais um push contínuo de 1,00 a 1,04 em todo plano, para a câmera parada não parecer foto.
5. **Look Cinemático leve.** Tonemap do HLG antes de tudo; curva em S; grão novo a cada quadro (semente igual ao índice do quadro, amplitude de 6 a 8 em 255, crf 17); vinheta de 0,7; luzes quentes e sombras frias, pele natural. Barras pretas só no CINEMA.
6. **Title Card** (adaptado, sem a moldura de celular). O minuto real da entrevista em DejaVu Sans Mono ("min 14:22") em x 56, y 236, e um cartão final de 1,5 a 2,5 s "Entrevista à TV Câmara Campinas · Bruno · Estrategista de Lançamento" em Cinzel sobre #141210. Prova que a frase é literal e fecha toda peça do mesmo jeito.

Paleta: #141210, #E8B36A, #F5C46E, #F3EDE2, #8f877c, degradê ouro #F5D08F a #9A5F2A (o do tv.html). Fontes: Cinzel 900 (títulos), Inter Display Black (legenda e frases), Playfair itálico (cargo e citação), DejaVu Sans Mono (minuto e relógio).

---

## 7. Fichas

### F1 · REACT · O que eu não disse na TV

| Campo | Decisão |
|---|---|
| Objetivo | Alcance e conversão. É o único formato com o rosto do Bruno de frente nos 3 primeiros segundos, a variável que os dados mandam DOBRAR, somada à prova da TV. Abre a série. |
| Duração | 30 a 38 s; virada entre 12 e 15 s (Módulo 1) |
| Footage | Selfie nova vertical de frente, 30 fps, luz de janela de frente, celular a 40 cm na altura dos olhos, lapela se houver, mesmo enquadramento dos reels de nicho (para medir o `headtop.json`). O Bruno assiste a cada trecho pela primeira vez, sem ensaio: grava a reação muda e depois o complemento. São 20 min de gravação para 6 reacts, dos quais saem 3. Trecho da TV em Z2 ou CB, nunca no ABERTO. Tela dividida: entrevista em cima (y 0 a 860), selfie embaixo, filete ouro de 2 px (o `splitS` do modelo B). |
| Quantidade | 3 (31/10, 21/11 e banco) |
| Nota | 9 |

**Estrutura**

| Tempo | Imagem | Texto e efeito | Som |
|---|---|---|---|
| 0,0 a 2,5 s | Selfie em tela cheia; o Bruno fala o gancho: "Dei uma entrevista pra TV Câmara Campinas. Olha o que eu respondi quando ela perguntou [pergunta curta]." (ou um hook aprovado do Módulo 4 que case com o trecho) | **Efeito 1:** Connect Hook no topo (y 260), palavra-chave em ouro. Legenda Gigante na fala (base). | voz da selfie |
| 2,5 a 2,8 s (fim do gancho) | Tela dividida em 0,27 s: trecho em cima, selfie embaixo | **Efeito 2:** Tela dividida. Selo fixo no painel de cima: "Entrevista à TV Câmara Campinas · min 14:22" (base daí em diante). | swipe pelo pico; close-up a 0,06 só nas transições |
| cerca de 5 s | Painel de cima | **Efeito 3** (só no ep. 1): Círculo à mão em volta do Bruno, com "esse atrás do monitor sou eu" em Playfair itálico. Nos outros episódios, entra aqui o Nome e cargo. | pop |
| cerca de 7,5 s | | **Efeito 4** (ep. 1): Nome e cargo. | |
| 9 a 11 s | Painel de cima | **Efeito 5:** Marca-texto na palavra-chave do trecho. Punch-in de 1,00 a 1,08 no painel de baixo só se ele reagir de verdade (riso, aceno), a 2 s ou mais do Marca-texto. | ding_si no Marca-texto |
| 12 a 15 s (virada) | O painel de cima congela com um ícone de pausa de 2 barras; a divisão se desfaz em 0,27 s; a selfie volta em tela cheia | **Efeito 6:** Punch-in de 1,00 a 1,10 na selfie, na primeira palavra de "O que eu não tive tempo de dizer na TV:". | tick na pausa; riser terminando aqui; trilha a zero 0,4 s antes |
| virada + 2 a 3 s | Selfie | **Efeito 7:** letreiro 3D atrás da cabeça com a palavra-chave do complemento (`letter()` com o `headtop.json` da selfie, o efeito validado no dentista). | sub baixo |
| até 3 s do fim | Selfie: de 8 a 12 s com 1 exemplo concreto, 1 erro ou o Lance do método em que aquilo entra; informação nova, nunca repetição do trecho | Legenda Gigante, palavra principal em ouro | voz da selfie |
| últimos 3 s | Selfie | **Efeito 8:** CTA de Comentário: caixa genérica (avatar redondo, sem ícone de app) digitando, com o CTA também falado. | typing |

- **Efeitos do PDF:** Connect Hook, Tela dividida com print, Círculo à mão, Nome e cargo, Marca-texto na palavra, Punch-in, Legenda Gigante, CTA de Comentário.
- **Áudio:** a selfie limpa é a voz principal, baixada 2 dB, com reverb curto bem leve; o trecho da TV passa pela cadeia comum e sobe 3 dB, para os dois ambientes se aproximarem. Trilha close-up ou hip-hop-02 a 0,06 só nas transições, com ducking. SFX pelo pico.
- **CTA:** REACT 01: "Comenta a sua profissão que eu te digo qual parte disso vale pra você." (o mesmo CTA dos reels de nicho). REACT 02: "Vai lançar nos próximos 90 dias? Me manda a data no direct." No direct entram as perguntas de qualificação do Módulo 6. TABULEIRO só se o REACT anterior passou de 150 de alcance em 48 h.
- **Critério de trecho:** os 6 trechos de maior nota no filtro que tenham uma pergunta da Mirna antes (permite "olha o que eu respondi quando...") e deixem uma ideia incompleta que o Bruno completa hoje em uma frase. Trecho da TV de 10 a 18 s, nota 7 ou mais, de preferência com o rosto em 3/4. O complemento nunca repete o que já foi dito.
- **Gatilho:** rosto de frente nos 3 primeiros segundos (fato: reels com o Bruno falando ficaram de 2,4x a 5,8x a mediana; o reel do dentista teve 32% de pulo contra 70% de média) somado à prova da TV. A autoironia do "atrás do monitor" assume o defeito do material. "O que eu não tive tempo de dizer" paga quem fica até a virada.
- **Paleta e tipografia:** letreiro em Cinzel 900 atrás da cabeça; legenda da selfie em Inter Display Black com palavra principal em #F5C46E; legenda do trecho da TV em Inter itálico branco a 90% numa caixa (um estilo por voz); filete ouro na divisão.
- **Referências:** `videos/nichos/dentista/engine/dent.html` (modelo B: `splitS`, `panelScene`, `letter()` com `headtop.json`, `cta()`); `videos/nichos/dentista/engine/comp.py` (`split(t)`); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/sab8a-475686.md` (talking head); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/stokebuilder-356793.md` (quem fala sempre visível, texto fiel).
- **Por que (fusão e correções):** os 2 juízes deram 9 e fundiram as mesmas propostas. Corrigi a densidade: os dois tinham 3 efeitos novos nos 3 primeiros segundos (Connect Hook, letreiro e Nome e cargo); agora são 8 efeitos com 2 s ou mais entre eles, e o letreiro foi para depois da virada. O "de costas" virou "atrás do monitor", que é o que o quadro mostra. A virada ficou entre 12 e 15 s, como manda o Módulo 1. O humor do BASTIDOR entrou aqui. Perde 1 ponto porque depende de gravação nova; sem a selfie o formato não existe, e ela nunca é trocada por voz sintética.

---

### F2 · STORIES · Diário da entrevista

| Campo | Decisão |
|---|---|
| Objetivo | Relacionamento e conversa no direct. Resposta de story abre a janela do direct (Módulo 6) sem depender de palavra-chave, e os stories absorvem os cortes que não cabem no feed. |
| Duração | 3 a 4 telas por dia, até 15 s cada |
| Footage | Still do ABERTO em P&B, 5 s do timelapse (ffmpeg direto no proxy de 3 qps, sem motor), versões de 10 a 15 s dos cortes (MANCHETE, PB, PONTOS, PROFISSAO). |
| Quantidade | 28 dias (ter 27/10 a seg 23/11) |
| Nota | 7 (hipótese: respostas por dia sem dado) |

**Pré-estreia**

| Dia | Tela |
|---|---|
| ter 27/10 | Bastidor anotado: still do ABERTO em P&B, com 3 círculos à mão em ouro desenhados um por vez, com 2 s entre eles: "a câmera da TV", "o gravador", "eu, atrás do monitor". Texto: "O celular que gravou isso ficou com a pior vaga da sala." |
| qua 28/10 | 5 s do timelapse com "35 minutos de entrevista. O primeiro corte sai sábado." e repost do CARROSSEL 01, se tiver saído. |
| qui 29/10 | Caixa de perguntas nativa: "O que você perguntaria se fosse a repórter?" (alimenta a fase 2 do PERGUNTA). |
| sex 30/10 | Enquete nativa "Qual assunto primeiro?" com 2 temas reais e sticker de contagem para sáb 31/10, 18h30. |

**Durante a série (todo dia)**
- Manhã: MANCHETE em loop, ou o PB ou o PONTOS em 10 a 15 s.
- Tarde: sticker nativo ligado ao corte do dia (enquete, quiz, caixa de perguntas ou controle deslizante), com o texto de apoio em Máquina de escrever. No dia de nicho com trecho da entrevista sobre aquela profissão, o PROFISSAO entra à tarde e aponta para o reel das 21h.
- Noite: repost do reel do dia (o de nicho às 21h nos dias úteis; o da entrevista às 18h30 no fim de semana), com "Corte 0X" e a contagem para o próximo.
- Domingo: enquete de 4 temas, que escolhe o carrossel de quarta e o PERGUNTA de sábado.
- Terça e sexta: Checklist marcando com as 3 perguntas de qualificação ("Já tem audiência?", "Já vende algo on-line?", "Vai lançar em até 90 dias?") e "Marcou as 3? Me responde aqui."
- Depois de um reel que passar de 150 de alcance em 48 h: story com o link do TABULEIRO.
- Tudo o que for prova vai para o destaque PROVA.

- **Efeitos do PDF:** Círculo à mão, Máquina de escrever, Checklist marcando, Faixa de notícia (via MANCHETE), Legenda Gigante, Nome e cargo. Nas telas animadas também vale 1 efeito novo a cada 2 s.
- **Áudio:** voz tratada nos trechos com trilha a 0,06; telas de sticker sem áudio ou com a música do app.
- **CTA:** "Marcou as 3? Me responde aqui.", "Me manda a data do seu próximo lançamento." e "Responde com a sua área que eu te digo qual corte é para você." Quem responde recebe "Obrigado por responder! Qual é a sua área e quantos seguidores você tem hoje?" e segue o roteiro do Módulo 6 (+1, +4 e +10 dias), com resposta em até 2 h.
- **Critério de trecho:** de 10 a 15 s com ideia completa, bons demais para ficar de fora e curtos demais para reel. A pergunta do sticker sai da própria frase do trecho. Bastidor: só o que o celular viu de verdade. Resposta de terceiros só aparece com autorização.
- **Gatilho:** sticker nativo tem atrito zero; responder story abre o direct com um toque; o checklist filtra quem tem audiência e data.
- **Paleta e tipografia:** kit da série; círculos e setas em #F5C46E com traço irregular; anotações em Playfair itálico (não há fonte manuscrita instalada).
- **Referências:** `videos/stories` (s01 a s08: frase entrando com FX em Si, MANTER no Módulo 7); `estaticos/tv-funil/tv.html` (fundo com poeira); `conteudo/sistema-instagram/00-SISTEMA.md` (Módulos 6 e 7).
- **Por que:** os 2 juízes concordam no papel dos stories. Fundi o calendário dia a dia da pré-estreia (juiz 2) com o rodízio de qualificação (juiz 1), e o reel BASTIDOR virou a tela de terça, onde o humor custa pouco. Nota 7 porque é a maior alavanca de conversa (1 disparo de automação em 30 dias mostra que palavra-chave não converte hoje), mas o volume de respostas é sem dado: medir no `ig_inbox` e escrever "sem dado" até completar 7 dias.

---

### F3 · CARROSSEL · O que eu disse na TV

| Campo | Decisão |
|---|---|
| Objetivo | Salvamento e autoridade. É o segundo carrossel da semana (o primeiro é o de fim de semana do plano de nichos) e mantém a série viva entre os sábados. |
| Duração | 6 lâminas de 1080x1350 (nunca mais de 7: os carrosséis longos tiveram 0% de salvamento) |
| Footage | Quadros parados em P&B com grão, tirados no segundo exato de cada frase e escolhidos pela maior variância do Laplaciano no recorte (sem borrão de movimento). Capa: recorte 4:5 do ABERTO (câmera da TV, quadro, os dois, gravador) com os desfoques fixos. Lâminas internas: CB, CM se autorizado, detalhe do gravador, detalhe do quadro. Render no mesmo motor: `render(lâmina)` e captura de 1080x1350 no `cap.js`. |
| Quantidade | 4 (qua 28/10 se a transcrição fechar até seg 26, qua 04/11, 11/11, 18/11) |
| Nota | 6,5 |

**Variante A (frases)**
- Lâmina 1: ABERTO em P&B, teto escurecido; frase-gancho em Cinzel 900 (até 3 linhas, 88 px) com a palavra-chave em ouro; "O que eu disse na TV sobre [tema]"; "Entrevista à TV Câmara Campinas" em 24 px; Círculo à mão na câmera da TV; "1/6" em mono.
- Lâminas 2 a 5: uma frase literal por lâmina (8 a 20 palavras) em Playfair itálico 54 px, apoiada numa palavra-estrutura em Cinzel 900 de 260 a 300 px que atravessa a borda direita e continua na lâmina seguinte (puxa o deslize); Marca-texto na palavra-chave; "min 17:42" em mono. Ordem: da frase mais concreta (com número) para a tese.
- Lâmina 6: as 4 palavras-estrutura empilhadas dentro da silhueta da torre (path do tv.html); "Qual dessas trava o seu lançamento? Comenta o número." e "Salva para reler antes de lançar."; "@o_estrategista.com.br".

**Variante B (quiz "Responde antes de arrastar")**, só se houver material: capa com a pergunta literal da Mirna; lâmina 2 com A, B e C (a certa resumida com palavras do Bruno e 2 crenças que o próprio Bruno citou e rebateu na entrevista; nunca respostas de mercado inventadas); lâmina 3 "Comenta a sua letra antes de passar."; lâmina 4 a resposta literal com check e o minuto; lâmina 5 o porquê em 3 linhas dele; lâmina 6 "O vídeo dessa resposta está no perfil."

- **Efeitos do PDF:** Title Card (capa e minuto real), Marca-texto na palavra, Lista numerada, Círculo à mão, Checklist marcando (variante B).
- **Áudio:** nenhum; se usar música, a do app, baixa. A lâmina 2 nos stories pode levar 6 s da voz real.
- **CTA:** A: "Comenta o número" e "Salva para reler antes de lançar." B: "Comenta a sua letra" e "Respondo quem acertou e quem errou." Legenda: "Vai lançar nos próximos 90 dias? Me manda a data no direct." Sem palavra-chave.
- **Critério de trecho:** 4 frases do mesmo capítulo (o mais votado na enquete de domingo), nota 7 ou mais, legíveis sem áudio e sem contexto, que reforcem o posicionamento (comandar, ordem, agenda cheia, preparo antes do anúncio), com uma palavra-estrutura de até 8 letras dita por ele, e que não tenham virado reel na mesma semana. Vício de fala sai marcado com reticências. No máximo uma frase "não é X, é Y" no carrossel inteiro.
- **Gatilho:** frase literal com o minuto real é citável e boa de mandar no direct; a viga cortada na borda puxa o deslize; no quiz, o pedido de comentário vem antes da resposta.
- **Paleta e tipografia:** fundo #141210; foto P&B com curva em S; vigas em Cinzel 900 #F3EDE2 com a palavra-chave em #F5C46E; frases em Playfair itálico; minuto em DejaVu Sans Mono #8f877c.
- **Referências:** `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/gdgtify-929495.md` (palavra com papel de viga); `videos/nichos/dentista/engine/cap.js` (viewport 1080x1350); `estaticos/tv-funil/tv.html` (path da torre); `conteudo/sistema-instagram/00-SISTEMA.md` (Módulo 1).
- **Por que:** os 2 juízes fundiram as mesmas propostas. Fiquei com a viga e o minuto real dos dois, com a variante B corrigida pelo juiz 2 (opções erradas só de crenças que o Bruno rebateu) e com a quarta-feira (fato: melhor dia da conta, média de 102 em 3 posts; 12h com média de 65). A torre da lâmina final usa o path que já existe no tv.html. Nota 6,5: nesta conta o carrossel é motor de salvamento, não de alcance.

---

### F4 · MANCHETE · frase em loop

| Campo | Decisão |
|---|---|
| Objetivo | Replays e prova social nos stories da manhã. As 2 com mais respostas podem virar reel curto. |
| Duração | 7 a 10 s |
| Footage | CB com push periódico de 1,00 a 1,06 e volta, com período igual à duração; cor natural, dodge & burn leve. |
| Quantidade | 8 |
| Nota | 6,5 como story (6 como reel) |

**Estrutura**
- 0,0 s: tudo já na tela. Faixa de notícia da marca entre y 1150 e 1330: tarja #141210 com filete ouro, rótulo "NA TV" em Cinzel ouro à esquerda (nunca URGENTE nem AO VIVO) e, numa segunda linha, um ticker com 4 outras frases curtas da entrevista correndo da direita para a esquerda, com o texto terminando antes de x 900. Acima da tarja: "Bruno · Estrategista de Lançamento · Entrevista à TV Câmara Campinas". Legenda Gigante palavra a palavra entre y 300 e 650 (base).
- Do início ao fim: voz real só da frase.
- Palavra-chave (a 2 s ou mais do início): Marca-texto ouro. 6 quadros depois do fim da frase, corte seco para o quadro 0. O push e o ticker são periódicos, então só a voz recomeça; não há salto de câmera.

- **Efeitos do PDF:** Faixa de notícia (adaptada: NA TV, preto e ouro), Legenda Gigante, Marca-texto na palavra, Nome e cargo.
- **Áudio:** voz tratada e um pad a -30 dB que emenda no loop. Sem SFX: o corte seco é o ritmo.
- **CTA:** no vídeo, nenhum. No story: enquete "Concorda?" ou caixa "Me pergunta sobre isso". Se for ao feed: "Qual frase da entrevista você colocaria na manchete?"
- **Critério de trecho:** frases autônomas de 5 a 10 s, nota 8 ou mais, sem pronome que dependa do contexto ("isso", "ele", "aquilo"), com número, contradição ou profissão, probabilidade média de 0,85 ou mais. Ticker: 4 frases de nota 7 ou mais cortadas em até 6 palavras. Conferir no trecho inteiro que a frase isolada não muda o sentido.
- **Gatilho:** com mediana de 6,2 s assistidos na conta, 8 s podem ser vistos inteiros e recomeçar: conclusão e replays. O ticker avisa que há mais frases e leva ao perfil.
- **Paleta e tipografia:** tarja #141210 com filete #E8B36A; rótulo em Cinzel 30 px ouro; ticker em Inter Bold 30 px #F3EDE2; legenda em Inter Display Black com palavra ativa #F5C46E. Sem vermelho de telejornal.
- **Referências:** `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/twoclipping-551116.md` (push lento, último quadro igual ao primeiro); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/gdgtify-929495.md` (linha do tempo periódica); `videos/nichos/dentista/engine/dent.html` (`caption`, `lowerThird`).
- **Por que:** os 2 juízes concordam (nota 6,5). Corrigi a promessa de "emenda sem pulo": a voz recomeça, então o loop é um corte seco desenhado, com push e ticker periódicos. É o formato mais barato (8 peças em cerca de 10 min de captura) e o de uso diário.

---

### F5 · TIMELAPSE · 35 minutos em 35 segundos (pedido do Bruno)

| Campo | Decisão |
|---|---|
| Objetivo | Alcance e pauta. Mostra a entrevista inteira, abre um laço que só fecha aos 27 s e termina no índice da série, pedindo o número do assunto que a pessoa quer ver inteiro. |
| Duração | 34 a 36 s |
| Footage | Abertura e pouso em tempo real (selfie de 1,8 s se gravada; senão Z2 desde o quadro 0). Miolo: ABERTO a cerca de 100x, lido em sequência do proxy de 3 qps por uma função de tempo com rampa suave (`timeremap.py`, sem seek), com `tmix` de 3 quadros (pesos 1 2 1) para dar rastro leve. Começa em P&B e ganha cor até a volta ao tempo real. Teto escurecido 45% por gradiente para dar contraste aos andares. Sem máscara: as cabeças têm cerca de 90 px no ABERTO e os andares ficam na parede acima delas, multiplicados pela luminância local da parede (a sombra real passa por cima). |
| Quantidade | 1 |
| Nota | 6,5 |

**Fato que limita o formato:** câmera parada e duas pessoas sentadas. Acelerado, quase nada se move na sala; quem anda é o relógio e o texto. Por isso os respiros de voz real são obrigatórios.

**Estrutura**

| Tempo | Imagem | Texto e efeito | Som |
|---|---|---|---|
| 0,0 a 1,8 s | Selfie de frente (ou Z2 com o Bruno) | **Efeito 1:** Connect Hook "35 MINUTOS EM 35 SEGUNDOS", com "35 SEGUNDOS" em ouro, e a linha fina "Entrevista à TV Câmara Campinas". | voz da selfie: "Foram 35 minutos de entrevista pra TV. Cabem em 35 segundos." |
| 1,8 a 4,2 s | Z2 em tempo real, cor | Voz real: a primeira metade da frase de maior nota, cortada uma palavra antes da virada (laço aberto). **Efeito 2** (a 2 s ou mais do efeito 1, na palavra mais próxima): Círculo à mão em volta do Bruno, "eu, atrás do monitor". | pop |
| 4,2 a 4,8 s | Congela, passa a P&B em 6 quadros, corte para o ABERTO; rampa eio de 1x para cerca de 100x | **Efeito 3:** relógio em DejaVu Sans Mono no canto superior esquerdo dispara de 00:00 (Title Card de tempo real). Barra de progresso de 3 px no topo, com uma marca por capítulo (base). | whoosh pelo pico; like-a-loop-machine ou deep-urban a 0,14 |
| 4,8 a 26 s | Timelapse do ABERTO | 7 capítulos, um a cada 2,5 a 3 s, no tempo forte da trilha: quando o relógio passa pelo minuto da frase, a frase-título (2 a 6 palavras literais) entra na parede acima das cabeças em Cinzel 900 #F3EDE2, com o número em #F5C46E, como um andar; os anteriores sobem e escurecem para #8f877c, e só 3 ficam à vista. Cada andar é um efeito novo. | tick a 0,35 em cada andar |
| perto de 11 s e de 19 s | Rampa para 1x em 0,4 s, Z2 em P&B | Respiro: 2 a 2,5 s da voz real com a palavra-chave daquele capítulo, Legenda Gigante. O andar do capítulo entra quando a rampa volta. Nunca mais de 8 s sem voz real. | trilha a 0,05 por sidechain |
| 26 a 27 s | O relógio rebobina até o minuto da frase de abertura; a cor volta a 100% | **Efeito:** rebobinar. | whoosh invertido; riser com pico na volta |
| 27 a 32 s | Z2 e depois CB, tempo real | A frase da abertura recomeça 1 s antes do corte e agora termina. **Efeito:** Marca-texto na palavra de virada. **Efeito**, 2 s depois: Nome e cargo. | ding_si no Marca-texto |
| 32 a 35 s | ABERTO escurecido | **Efeito:** Lista numerada com os 7 capítulos dentro da silhueta da torre (path do tv.html) e o CTA em 2 linhas. O último quadro é a capa. | |

- **Efeitos do PDF:** Connect Hook, Círculo à mão, Title Card (relógio do tempo real), Barra de progresso, Lista numerada, Legenda Gigante, Marca-texto na palavra, Nome e cargo.
- **Áudio:** grade de batida medida em numpy, com cada andar no tempo forte; nos respiros e no pouso a trilha desce por sidechain. A voz nunca é acelerada.
- **CTA:** na tela: "Comenta o número do assunto que você quer ver inteiro." Na legenda: os capítulos com o minuto de cada um e "O mais votado sai no próximo sábado." A mesma votação roda em enquete nos stories. Com menos de 5 votos somados, seguir a ordem da nota e dizer isso nos stories, sem fingir votação.
- **Critério de trecho:** a entrevista inteira. Cada pergunta da Mirna abre um capítulo; capítulos com menos de 90 s se juntam ao seguinte até sobrarem 7. Frase-título: de 2 a 6 palavras literais do Bruno no capítulo (cortar, nunca reescrever), com prioridade para número, profissão nomeada ou contradição, e palavra-chave de até 10 letras. Frase de abertura e pouso: a de maior nota geral, de 5 a 9 s, com a palavra de virada depois da metade e probabilidade média de 0,85 ou mais. Respiros: as 2 frases seguintes de maior nota, com 4 a 9 palavras e áudio limpo.
- **Gatilho:** compressão de tempo com número específico (35 em 35), relógio correndo e laço aberto; a câmera da TV no plano aberto prova que não é encenação; a lista final dá pausa, print e um comentário de um caractere.
- **Paleta e tipografia:** andares em Cinzel 900 #F3EDE2 com número #F5C46E, antigos em #8f877c; relógio em DejaVu Sans Mono; Connect Hook em Inter Display Black; teto escurecido para #070605.
- **Referências:** `videos/nichos/dentista/engine/dent.html` (`backC`, o prédio de palavras, e `letter()` com ajuste de tamanho); `estaticos/tv-funil/tv.html` (`rnd` semeado, render determinístico, path da torre); `videos/nichos/dentista/engine/mix.py`; `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/gdgtify-929495.md` (palavras como arquitetura; o fecho construído pelo que veio antes); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/twoclipping-000267.md` (grade de batida, SFX pelo pico).
- **Por que:** fusão do laço aberto e dos respiros de voz (juízes 1 e 2), do índice com votação (juiz 1) e da torre (juiz 2), agora com o path que já existe no tv.html (o juiz 2 achou que não havia SVG). Cortes de custo: sem máscara rembg (as cabeças são pequenas e o texto fica acima delas) e andares na camada front, o que derruba a captura de cerca de 10,5 min para cerca de 5 min. Abre com o Bruno (selfie ou Z2), como manda o CLAUDE.md. Nota 6,5: é pedido explícito e não depende de gravação, mas o miolo é o mais parecido com a animação sem rosto que ficou de 0,15x a 0,8x da mediana. Entra depois do REACT 01, uma vez só. Abaixo de 0,8x da mediana com pulo acima de 75%, não se repete.

---

### F6 · PB · Corte P&B "NA TV" (pedido do Bruno)

| Campo | Decisão |
|---|---|
| Objetivo | Autoridade e compartilhamento. Série numerada com o texto simples do que foi dito em cada momento: é a assinatura visual da entrevista. |
| Duração | 20 a 35 s (o trecho decide; nunca esticar) |
| Footage | Tempo real em P&B: curva em S antes de tirar a cor, pretos em #0e0d0b, grão por quadro, vinheta. Topo escurecido por gradiente (-1,3 EV no topo, 0 na altura das cabeças) para o texto branco ler sobre a parede clara. Dodge & burn pela máscara: Bruno +0,2 EV, fundo e Mirna -0,6 EV. Alterna Z2 e CB só em troca de frase (mínimo 3 s por plano); CM de até 1,5 s se ela acenar (com autorização). Push contínuo. Versão A: 1,5 s de selfie em cor ("Isso eu falei na TV.") e corte seco para o P&B. Versão B: abre direto no P&B. |
| Quantidade | 3 (PB 01 versão A, PB 02 versão B para fechar o A/B, PB 03) |
| Nota | 7,5 |

**Estrutura**

| Tempo | Imagem | Texto e efeito | Som |
|---|---|---|---|
| 0,0 a 1,5 s (só versão A) | Selfie em cor | Legenda Gigante | voz da selfie; corte seco |
| 0,0 s do trecho (começa 0,1 s antes da primeira palavra) | Z2 ou CB em P&B | A frase inteira já na tela, texto simples sem caixa, Inter Display Black 68 px, até 2 linhas quebradas à mão, entre y 300 e 760; palavras não ditas a 35%, cada uma acende para branco em 0,2 s no tempo do Whisper (base). Rótulo "NA TV · CORTE 01 · min 14:22" em DejaVu Sans Mono 24 px (base). | voz tratada, som da sala baixo; pad a -30 dB ou close-up a 0,05 com ducking |
| 2,0 a 4,5 s | | **Efeito:** Nome e cargo. | |
| frases seguintes | Troca seca de frase no início da frase seguinte, junto com o corte de câmera | | |
| virada (entre 8 e 15 s) | 0,4 s de quietude absoluta: a frase some, fica só o som da sala | A frase da virada entra a 84 px. **Efeito:** Punch-in na primeira palavra. **Efeito:** Marca-texto ouro na palavra-chave, se ela estiver a 2 s ou mais do Punch-in; senão, fica só o Marca-texto. É a única cor do vídeo; o texto sobre ela fica #141210. | trilha zerada 0,5 s antes; ding_si no Marca-texto |
| últimos 1,5 s | Freeze com o grão correndo | **Efeito:** Title Card final: a frase-chave entre aspas em Playfair itálico 66 px e "Bruno, na entrevista à TV Câmara Campinas". | shutter baixo |

- **Efeitos do PDF:** Legenda Gigante (versão texto simples), Marca-texto na palavra, Nome e cargo, Punch-in, Look Cinemático (grão e vinheta em P&B), Title Card.
- **Áudio:** voz protagonista, ambiente da sala baixo (dá verdade de bastidor). Sem riser nem impacto: é o formato sóbrio.
- **CTA:** alterna "Manda para um expert que vai lançar este ano." (compartilhamento) e "Vai lançar nos próximos 90 dias? Me manda a data no direct." (Módulo 6). TABULEIRO só se um PB anterior passou de 150 em 48 h.
- **Critério de trecho:** blocos de 20 a 35 s com uma ideia só, cuja primeira frase seja autônoma, tenha nota 7 ou mais e até 14 palavras com personagem, número ou contradição (Módulo 4); palavra de virada entre 8 e 15 s; probabilidade média de 0,75 ou mais no trecho inteiro (abaixo disso, a legenda do áudio distante erra); sem a voz da Mirna por cima. Resposta maior que 35 s: cortar respiros, nunca o meio de uma frase.
- **Gatilho:** P&B com uma única palavra em ouro interrompe o feed colorido; a frase inteira visível no quadro 1 faz o vídeo funcionar sem som; a numeração pede o próximo; o minuto real prova a citação; a quietude de 0,4 s quebra o padrão uma vez.
- **Paleta e tipografia:** P&B; texto #F3EDE2 com sombra 0 4px 18px; ouro #E8B36A só no marca-texto; Inter Display Black nas frases, Playfair itálico na citação final, DejaVu Sans Mono no rótulo.
- **Referências:** `videos/nichos/dentista/engine/comp.py` (P&B do modelo A, `zoomimg`); `videos/nichos/dentista/engine/dent.html` (`caption`, `lowerThird`); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/notdwd-998633.md` (legenda que acende de cinza para branco, grão por quadro, vinheta); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/gdgtify-929495.md` (400 ms de quietude); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/twoclipping-551116.md` (push lento).
- **Por que:** os 2 juízes chegaram ao mesmo desenho. Duas correções de viabilidade: o texto branco sobre a parede cinza clara não lia, então o topo é escurecido por gradiente; e o Marca-texto e o Punch-in caíam na mesma palavra, o que fere a regra de 1 efeito a cada 2 s. Só captura a camada front (cerca de 4,5 min por peça). Nota 7,5: melhor custo por autoridade e é o pedido literal do Bruno. O teto é o Bruno em 3/4: o A/B (PB 01 com selfie contra PB 02 sem) diz no Módulo 7 se a abertura com rosto vira regra da série.

---

### F7 · PERGUNTA · A TV perguntou

| Campo | Decisão |
|---|---|
| Objetivo | Comentários e autoridade. A TV pergunta e o estrategista responde: é a imagem de quem é consultado. A fase 2, "Você perguntou", leva o comentário para o direct. |
| Duração | 25 a 40 s |
| Footage | Z2 em cor na pergunta (os dois em quadro; o Bruno em 3/4 desde o quadro 0). CB na resposta, alternando com Z2 só em fim de frase. CM de até 1,5 s com a reação dela, com a voz do Bruno por cima; CM nunca passa de 25% do tempo. Sem autorização: a pergunta vai só em texto (sem a voz dela) e a imagem fica em CB. |
| Quantidade | 2 (sáb 14/11 e banco) |
| Nota | 7,5 com autorização; 6 sem |

**Estrutura**

| Tempo | Imagem | Texto e efeito | Som |
|---|---|---|---|
| 0,0 s | Z2 | **Efeito 1:** cartão #141210 a 88% com filete ouro no terço superior (y 230 a 640): "A PERGUNTA DA TV · Nº 01" em Cinzel 26 px ouro e a pergunta literal inteira em Playfair 58 px; as palavras acendem de cinza para papel no tempo da voz dela (o vídeo lê sem som). | voz da Mirna tratada; typing baixo; sem trilha |
| fim da pergunta (2 s ou mais depois) | Z2 segue andando, push lento, nunca congela | **Efeito 2:** um anel único de 1,2 s em volta de "Responde antes dele". No fim, o cartão sobe e vira selo fixo no topo: "PERGUNTA: [até 5 palavras dela]" (base). | tick no início e no fim do anel; 0,4 s de quietude |
| 1ª palavra da resposta | Corte para CB | **Efeito 3:** Punch-in de 1,00 a 1,08. | hazy-after-hours a 0,06 com ducking |
| +2 s | | **Efeito 4:** Nome e cargo. | |
| palavra que responde a pergunta | | **Efeito 5:** Marca-texto. | ding_si |
| virada (12 a 15 s) | Inserção de CM de até 1,5 s, voz do Bruno por cima | | |
| últimos 3 s | CB | **Efeito 6:** CTA de Comentário com caixa genérica digitando "eu responderia..." e "Próxima pergunta: sábado". | typing |

- **Variante B** (teste no nº 02): cold open de 2,4 s em CB com a frase mais forte da resposta antes do cartão. Medir qual tem menos pulo.
- **Fase 2, "Você perguntou"** (semana 5 em diante, só com material real): o cartão traz uma pergunta real que chegou nos comentários, no direct ou na caixa dos stories, com as iniciais e a autorização da pessoa, respondida por outro trecho da entrevista ou por selfie nova. Nunca pergunta inventada.
- **Efeitos do PDF:** Máquina de escrever (pergunta acendendo no tempo da voz), Contagem regressiva (um anel só), Punch-in, Nome e cargo, Legenda Gigante, Marca-texto na palavra, CTA de Comentário.
- **Áudio:** as duas vozes niveladas por turno (dynaudnorm por segmento). Sem trilha na pergunta.
- **CTA:** "Comenta como você responderia. Eu respondo cada um." O Bruno responde todo comentário em até 2 h com uma pergunta de volta; quem citar lançamento próximo recebe no direct a pergunta 1 do Módulo 6.
- **Critério de trecho:** par pergunta e resposta pela diarização. Pergunta da Mirna com até 20 palavras ou 6 s, de um tema que o expert se pergunta (lançamento, vender, agenda, curso, preço, erro, começar). +3 se começa com "como", "por que", "quanto", "quem" ou "vale a pena"; -3 se é sobre a TV, a cidade ou política local. Resposta do Bruno de 15 a 30 s, nota 6 ou mais, que já comece respondendo. Pergunta longa: o áudio é cortado no respiro e a tela mostra só palavras dela, sem reescrever. Ordem: a mais votada; sem votos, a de maior nota.
- **Gatilho:** pergunta aberta (quem leu fica para ouvir a resposta); o "responde antes dele" põe o espectador no jogo e gera comparação nos comentários; a numeração cria hábito.
- **Paleta e tipografia:** cartão #141210 a 88% com filete #E8B36A de 2 px; pergunta em Playfair (TTF do repo) #F3EDE2; selo em Cinzel 26 px ouro; caixa de comentário branca, sem logo, botão ouro.
- **Referências:** `videos/nichos/dentista/engine/dent.html` (`cta()` com cursor, `caption`, `lowerThird`); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/twoclipping-041659.md` (texto no tempo da voz); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/stokebuilder-356793.md` (texto fiel); `conteudo/sistema-instagram/00-SISTEMA.md` (Módulo 6).
- **Por que:** o juiz 1 abria com a pergunta no quadro 1; o juiz 2, com um cold open do Bruno. Fiquei com a pergunta no quadro 1, que é o próprio gancho e já tem o Bruno em cena no Z2, e o cold open virou o teste do nº 02. Ficaram o selo fixo, o anel curto sem congelar o vídeo e a fase 2 só com pergunta real. Saíram os balões de abertura e a Barra de Prompt (lê como chat de IA). Nota 7,5, que cai para 6 sem autorização da Mirna.

---

### F8 · CINEMA · fonte de cinema, strobo e react (pedido do Bruno)

| Campo | Decisão |
|---|---|
| Objetivo | Compartilhamento e emoção (a métrica mais fraca da conta: 11 compartilhamentos em 30 dias). A reação real da jornalista em câmera lenta é a prova social com emoção e entrega o rosto de frente que o Bruno não entrega. |
| Duração | 22 a 30 s |
| Footage | CB e Z2 cortados em fim de frase, no tempo forte da trilha, dentro de uma janela de 1080x1200 (y 300 a 1500), com barras pretas de 300 px em cima e 420 px embaixo desde o quadro 0, para os rostos não ficarem pequenos. Começa em P&B e a cor volta na frase-chave. React da Mirna em CM a 0,5x real: 1 s da fonte 4K60 lido por seek, com `setpts=2*PTS` e saída a 30 fps (2 s de tela), enquanto a voz do Bruno segue em tempo real. Sem autorização da Mirna: o react vira um freeze no Bruno em CB com push lento e 0,4 s de quietude. |
| Quantidade | 2 (dom 15/11 e banco; no máximo 1 a cada 2 semanas) |
| Nota | 7 com autorização; 6 sem |

**Estrutura**

| Tempo | Imagem | Texto e efeito | Som |
|---|---|---|---|
| 0,0 a 0,6 s | CB em P&B escurecido a 50% na janela; barras desde o quadro 0 (Look Cinemático, base) | **Efeito 1:** strobe tipográfico. As 3 a 5 palavras do gancho em Cinzel 900 ouro trocam a cada 4 quadros, sem quadro vazio entre elas (a luminância não alterna, então não há clarão); a imagem não pisca. | riser com pico em 0,6 s; a voz já começa |
| 0,6 a 2,0 s | Imagem volta a 100% (ainda P&B), push lento | O gancho assenta em Cinzel 72 px na barra de cima (y 200 a 290). | |
| 2,0 s | | **Efeito 2:** Nome e cargo dentro da janela, em caixa. | |
| 2 a 12 s | Cortes CB, Z2 e CB só em fim de frase | Legenda de cinema em Playfair itálico 46 px creme dentro da barra de baixo (y 1530 a 1630), uma frase por vez (base). Minuto real em mono no canto da janela (base). Opcional, um só: Círculo à mão em traço ouro sobre algo que ele cita e que está na tela. | deep-urban ou complicated a 0,10 com ducking |
| frase-chave (12 a 15 s) | A trilha zera 0,5 s antes | **Efeito:** na palavra-chave, a cor volta em 6 quadros e a palavra cai em Cinzel 150 px na barra de cima com Gravity Drop (2 quiques); fica até o fim da frase. | impact no pouso |
| +2 s | Corte para CM a 0,5x | **Efeito:** Punch-in lento de 1,00 a 1,08 no rosto dela, sem legenda e sem dizer o que ela sentiu. | sub; 0,4 s de quietude antes de voltar |
| payoff | CB em cor | Legenda de cinema | |
| últimos 2,5 s | A janela escurece | **Efeito:** Title Card "ENTREVISTA À TV CÂMARA CAMPINAS" em Cinzel 28 px com espaçamento de .3em e "Bruno · Estrategista de Lançamento"; as barras fecham para o centro na última sílaba. | whoosh |

- **Efeitos do PDF:** Look Cinemático, Nome e cargo, Gravity Drop, Punch-in, Title Card, Legenda Gigante (versão legenda de cinema), Círculo à mão (opcional).
- **Áudio:** cortes no tempo forte de uma grade medida em numpy. Medir os picos de impact, sub e shutter e incluir no `PICO`. Fotossensibilidade: no máximo 3 clarões por segundo, nenhum branco puro em tela cheia, nenhum vermelho.
- **CTA:** na tela: "Manda para quem precisa ouvir isso." Na legenda: 2 linhas de contexto e "E você, o que teria respondido?" Sem palavra-chave.
- **Critério de trecho:** frase de impacto do Bruno com nota 8 ou mais e emoção mensurável (pausa de 0,8 s ou mais antes de uma frase declarativa, pico de voz 6 dB acima da mediana do trecho, riso, ou história com personagem), mais uma reação visível da Mirna até 3 s depois. Achar a reação por código: no proxy a 360x640, energia de movimento por segundo na região do rosto dela (diferença absoluta entre quadros, numpy) acima do percentil 90, cruzada com picos de riso no áudio; conferir no olho numa folha de contato de CM com 1 quadro por segundo. A reação tem de ser consequência daquela fala, nunca colada de outro momento. Sem reação clara, o trecho vai para o PB.
- **Gatilho:** o strobe da palavra trava o polegar no primeiro meio segundo; a reação real em câmera lenta é emoção e validação de fora; a estética de trailer transforma o trecho em evento e pede envio por direct.
- **Paleta e tipografia:** pretos levantados #0E0D0B nas barras, creme #F3EDE2, ouro em degradê de #F5D08F a #9A5F2A nos títulos; Cinzel 900 é a fonte de cinema da marca; Playfair itálico na legenda; DejaVu Sans Mono no minuto.
- **Referências:** `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/notdwd-998633.md` (strobe, grão, halação, vinheta); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/twoclipping-000267.md` (banidos, cortes no tempo forte); `videos/cases/tzur/ov2.html` (fecho cinematográfico); `videos/nichos/dentista/engine/dent.html` (`#bars`); `estaticos/tv-funil/tv.html` (degradê ouro).
- **Por que:** fusão dos 2 juízes, com 4 correções. (1) O strobe virou troca de palavras sem quadro vazio, que atende ao pedido do strobo sem clarão (antes eram 15 piscadas por segundo). (2) Saíram o strobe de corte entre CB e CM e o pulso de tela cheia: eram 3 efeitos em 1 s e punham a Mirna em tela no primeiro segundo. (3) A legenda foi para dentro da barra de baixo, porque na janela ela cairia sobre a mesa branca. (4) A palavra que vira letreiro atrás das cabeças saiu (pedia máscara e camada back para 2 s de efeito). Nota 7: alto potencial de envio, com risco de soar pretensioso para o médico do Tier 1 e dependência da autorização.

---

### F9 · PONTOS · chuva de pontos escrevendo o assunto (pedido do Bruno)

| Campo | Decisão |
|---|---|
| Objetivo | Retenção por satisfação visual e salvamento pela lista final. A palavra se forma no instante em que o Bruno a diz. |
| Duração | 25 a 32 s |
| Footage | Z2 em cor nos 2 primeiros segundos; depois luminância a 50% e saturação a 40%, com a parede escurecida por gradiente para o ouro aparecer. Os pontos vivem só na parede acima das cabeças (y 220 a 820) e nunca entram na zona das cabeças: sem máscara, e o Bruno fica sempre visível. Versão A com 1,5 s de selfie ("Isso eu falei na TV."). |
| Quantidade | 1 (mais versões de 10 s nos stories) |
| Nota | 6 |

**Mecânica:** canvas único dentro do `render(t)`, função pura do tempo, sem física acumulada. Cada palavra-assunto (até 10 letras) é desenhada em Cinzel 900 a 200 px num canvas fora da tela e amostrada numa grade de 11 a 12 px (600 a 1.200 alvos, guardados por palavra). Cada ponto nasce acima da tela com x e atraso de semente fixa (o `rnd` do tv.html), cai por y = y0 + g·τ²/2 com g = 5200 px/s² e quica 1 vez, amortecido, no alvo; pousa da esquerda para a direita e passa de creme a ouro em 0,2 s.

**Estrutura**

| Tempo | Imagem | Texto e efeito | Som |
|---|---|---|---|
| 0,0 s do trecho | Z2 em cor | **Efeito 1:** a primeira palavra-assunto já formada em pontos e pontos extras ainda caindo (Gravity Drop em pontos); frase-gancho em Legenda Gigante (base). | uplifting-bass ou hazy-after-hours a 0,08 com ducking |
| 2,0 a 4,0 s | O Z2 escurece | **Efeito 2:** Nome e cargo. | |
| cada assunto novo (3 a 5, com 3 s ou mais entre eles) | | **Efeito:** a queda começa na primeira sílaba da palavra no Whisper, nunca antes. Os pontos da palavra antiga voam com mola para a nova, os que faltam caem do topo, os que sobram encolhem até sumir. Fecha em 0,6 a 0,8 s. Logo abaixo, a frase curta dele naquele assunto é digitada (Máquina de escrever) no ritmo da fala. | 5 a 8 ticks agrupados por palavra (nunca 1 por ponto); coin baixo quando a palavra fecha |
| número dito por ele | | **Efeito** (só se houver número e a 2 s de outro efeito): os pontos se reorganizam na quantidade (1 ponto = N, escala em 22 px) e o Contador sobe. | |
| últimos 3 s | | **Efeito:** as palavras encolhem e empilham como Lista numerada dos assuntos, que fica 1,5 s para print. | ding_si |

- **Efeitos do PDF:** Gravity Drop (em pontos), Máquina de escrever, Legenda Gigante, Nome e cargo, Contador de número (só com número dito), Lista numerada.
- **Áudio:** voz à frente; trilha leve; som dos pontos sintetizado em grupos, sem chiado.
- **CTA:** "Qual dessas palavras trava o seu lançamento? Comenta." (resposta de uma palavra) e "Salva a lista."
- **Critério de trecho:** 25 a 32 s, nota 6 ou mais, em que o Bruno nomeia de 3 a 5 conceitos curtos (etapas, "primeiro, segundo", pares de opostos) com 3 s ou mais entre eles; cada palavra dita por ele, com até 10 letras e probabilidade acima de 0,8. Prioridade para a enumeração de etapas, que mostra o método em ordem. Trecho com um conceito só é descartado.
- **Gatilho:** cada queda abre uma pergunta de 0,7 s que fecha quando ele diz a palavra, de 3 a 5 vezes por vídeo; a lista final dá motivo para salvar; é um visual que o nicho de lançamento não usa.
- **Paleta e tipografia:** pontos em #F5C46E, #E8B36A e #9A5F2A com centro creme (gradiente radial do tv.html), sem brilho em volta; frase digitada em Inter 800 #F3EDE2; lista com números em Cinzel ouro.
- **Referências:** `estaticos/tv-funil/tv.html` (`rnd`, `ballPos` com queda e quique analítico); `videos/nichos/dentista/engine/dent.html` (`dots()`); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/gdgtify-929495.md` (função pura do tempo); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/godsboy7777-150194.md` (gravidade crível); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/morse-369333.md` (molas em forma fechada).
- **Por que:** fusão dos 2 juízes. Os pontos não atravessam mais as pessoas (nem caindo para fora, nem quicando na mesa): isso dispensa a máscara rembg em 900 quadros e não esconde o Bruno. A troca de palavra usa a mola (juiz 2) em vez do chão que abre (juiz 1). Canvas, e não SVG com 1.200 círculos. Testar 6 quadros: se passar de 0,5 s por quadro, abrir a grade. Nota 6: é o pedido com mais cara de animação, o formato que ficou de 0,15x a 0,8x da mediana. Entra uma vez, no fim do ciclo, e só repete se passar de 0,8x com pulo abaixo de 75%.

---

### F10 · SALA · a parede da entrevista vira letreiro

| Campo | Decisão |
|---|---|
| Objetivo | Autoridade e reassistida. É a transposição mais direta do letreiro atrás da cabeça, validado no dentista, para este material: as palavras do Bruno mudam a sala da entrevista. |
| Duração | 25 a 35 s |
| Footage | Z2. Superfície principal: a parede cinza livre acima das cabeças, quase de frente para a câmera (não precisa de homografia). Letreiro na camada back, atrás das pessoas pela máscara dos 2 maiores componentes; a base das letras desce até y 950, atrás das cabeças, e nunca chega ao monitor (topo em y 1000), então não há máscara estática. A camada é multiplicada pela luminância local da parede (quadro desfocado 15 px dividido pela média): a sombra real escurece as letras. Insert opcional em CE quando ele enumera: o quadro tem cerca de 400x410 px no recorte nativo e está na parede lateral, então leva homografia de 4 cantos medida uma vez. |
| Quantidade | 1 (banco) |
| Nota | 6,5 |

**Estrutura**
- 0,0 s: Z2; a parede já mostra a primeira palavra-chave como letreiro em Cinzel 900 preto quente #141210 a 92%, com as pessoas na frente (**efeito 1**). Frase-gancho em Legenda Gigante (base).
- 2,0 a 4,5 s: **efeito:** Nome e cargo.
- Cada palavra-chave seguinte (no máximo 1 a cada 3 s): **efeito:** acende como projetor ligando (4 quadros com 1 oscilação de brilho) e a anterior apaga.
- Na palavra-chave principal da peça: **efeito:** Marca-texto ouro atrás das letras pretas.
- Se ele enumerar ("primeiro", "segundo", "etapa"): insert de 2 a 3 s no CE; **efeito:** cada item se escreve em traço de caneta ouro (texto em path, `stroke-dashoffset`) com o número em Cinzel, e um check aparece quando ele termina o item. Se ficar ilegível na folha de 4 quadros por segundo, a lista vai para a parede.
- Virada (12 a 15 s): **efeito:** Punch-in.
- Últimos 4 s: **efeito:** todas as palavras do corte acendem juntas na parede como um mural, com o CTA em caixa preta.

- **Efeitos do PDF:** Nome e cargo, Legenda Gigante, Marca-texto na palavra, Lista numerada, Checklist marcando, Punch-in.
- **Áudio:** voz tratada; trilha do banco a 0,07 com ducking; tick a 0,3 quando a palavra acende; typing curto no quadro; ding_si no Marca-texto.
- **CTA:** "Salva para montar o seu plano antes do próximo lançamento." Legenda: "Qual dessas etapas está vazia no seu plano? Comenta o número."
- **Critério de trecho:** 25 a 35 s, nota 6 ou mais, com 3 a 5 palavras-chave de até 9 letras ditas por ele (cabem na largura da parede) e, de preferência, uma enumeração. Conferir no vídeo inteiro se o quadro de planejamento mostra anotação de cliente; se mostrar, borrar antes de escrever por cima.
- **Gatilho:** as palavras do Bruno mudam a sala com profundidade real (letra atrás das pessoas, sombra real por cima), o que faz reassistir e gera o "como fez isso?"; o mural final é capa e print.
- **Paleta e tipografia:** letreiro preto quente #141210 com marca-texto ouro #E8B36A atrás (ouro direto sobre cinza claro não tem contraste); traço de caneta ouro; legenda em caixa #141210.
- **Referências:** `videos/nichos/dentista/engine/dent.html` (`letter()`, camadas back e front); `videos/nichos/dentista/engine/comp.py` (máscara, componente, dilatação, blur); `videos/cases/tzur/seg.py` (rembg u2net_human_seg); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/gdgtify-929495.md` (mural montado com o que já apareceu).
- **Por que:** os 2 juízes deram 7. Baixei para 6,5 depois de olhar o material: o quadro de planejamento está cortado, pequeno e fora do Z2 (o juiz 1 previa um insert em tela cheia, que seria uma ampliação de 4,6x), então a força do formato fica na parede. Cortes de custo: sem homografia na parede (ela está de frente) e sem máscara estática do monitor. É o formato mais caro (cerca de 10,5 min de captura mais rembg): render de teste de 30 quadros antes do completo. Reserva número 1 para a vaga de um formato que o Módulo 7 mandar PARAR.

---

### F11 · PROFISSAO · o que eu disse na TV para o [profissional]

| Campo | Decisão |
|---|---|
| Objetivo | Compartilhamento para um colega e ponte entre a série da entrevista e os reels de nicho das 21h (TESTAR do Módulo 7: profissão nomeada). |
| Duração | 20 a 28 s |
| Footage | Z2 desde o quadro 0, depois CB. Sem a abertura no ABERTO (o Bruno ficaria pequeno demais nos 3 primeiros segundos). |
| Quantidade | 2 (stories; reel só com DOBRAR) |
| Nota | 6,5 (condicional à existência do trecho) |

**Estrutura**
- 0,0 s: Z2; **efeito 1:** Connect Hook "[PROFISSÃO] COM AGENDA CHEIA", com a dor em ouro e a linha fina "o que eu disse na TV". Selo "Entrevista à TV Câmara Campinas" (base).
- 2,0 a 4,5 s: **efeito:** Nome e cargo.
- cerca de 5 s: **efeito:** Faixa de notícia da marca entre y 1150 e 1330 (tarja #141210, filete ouro, etiqueta "NA TV" em ouro), com a frase literal correndo a 120 px/s; quando ele diz a frase, a faixa para e fica 1,5 s inteira.
- Virada: **efeito:** Punch-in no CB.
- Últimos 2,5 s: "Manda para um [profissão] que precisa ouvir isso."

- **Efeitos do PDF:** Connect Hook, Nome e cargo, Faixa de notícia (NA TV, preto e ouro), Legenda Gigante, Punch-in.
- **Áudio:** complicated a 0,10 com ducking; swipe na entrada da faixa; tick quando ela para. Nada que lembre vinheta de emissora.
- **CTA:** "Manda para um [profissão]." A legenda começa pela profissão e fecha com "Você conhece alguém assim?". Nos stories, aponta para o reel de nicho das 21h da mesma profissão.
- **Critério de trecho:** só roda se a entrevista tiver trecho sobre profissional de agenda cheia, fila de espera, hora de atendimento ou uma das profissões dos nichos (consórcio, dentista, nutricionista, psicólogo, advogado) que valha para a profissão do cartão sem mudar uma palavra dele. Nunca forçar a profissão.
- **Gatilho:** profissão nomeada faz pensar em alguém e mandar (hipótese do Módulo 7: pelo menos 2x mais compartilhamento); a faixa empresta credibilidade de noticiário sem copiar a emissora.
- **Paleta e tipografia:** tarja #141210 com filete #E8B36A; etiqueta "NA TV" em Cinzel 900 #141210 sobre ouro; manchete em Inter 800 46 px #F3EDE2. Nunca as cores, a vinheta ou a tarja da TV Câmara; sem "URGENTE" e sem "AO VIVO".
- **Referências:** `videos/nichos/dentista/engine/dent.html` (`lowerThird`, `pill`); `conteudo/nichos-30-dias/roteiros-20-videos.md` (ordem dos nichos); `conteudo/sistema-instagram/00-SISTEMA.md` (Módulo 7).
- **Por que:** veio do juiz 1; o juiz 2 o tinha fundido na manchete. Mantive separado porque é a única ponte com os reels de nicho em formato médio, mas com duas correções: saíram a abertura no ABERTO e a Notificação, que punham 2 efeitos em 0,8 s e o Bruno pequeno no começo. Fica nos stories da tarde; vira reel de fim de semana só se o Módulo 7 mandar DOBRAR profissão nomeada.

---

### F12 · MITO · verdade ou mito

| Campo | Decisão |
|---|---|
| Objetivo | Comentário de menor atrito (V ou M) e retenção até a revelação. |
| Duração | 18 a 28 s |
| Footage | Z2 em P&B escurecido a 65% na afirmação e na contagem, com os dois à vista; CB em cor na resposta (a cor que volta marca a resposta, como no modelo A do dentista). |
| Quantidade | 1 (banco; condicional) |
| Nota | 6 |

**Estrutura**
- 0,0 a 2,5 s: "VERDADE OU MITO?" em Cinzel 40 px ouro no topo e a crença em Inter Display Black 66 px numa caixa #141210 a 88% (y 260 a 700), **dita pela voz real do Bruno** ("muita gente acha que..."), com cada palavra acendendo no tempo da fala (**efeito 1**). Há voz real desde o quadro 1.
- 2,5 a 4,5 s: **efeito:** Contagem regressiva 2, 1 com um anel que se fecha (`relogio()` do dent.html) e "Responde antes do zero". A imagem segue com push lento; são 2 s sem voz, só com o som da sala, o único buraco de voz permitido.
- 4,5 s: corte para CB em cor com a resposta. Na palavra que decide: **efeito:** o carimbo MITO ou VERDADE cai sobre a caixa (escala de 130% para 100% e tremida de 3 quadros); se for mito, um risco ouro atravessa a frase.
- Depois: Legenda Gigante; **efeito:** Punch-in na virada; Checklist marcando só se ele enumerou, cada check no tempo do item.
- Últimos 3 s: **efeito:** CTA de Comentário.

- **Efeitos do PDF:** Connect Hook, Contagem regressiva, Ícone com Impacto (carimbo e risco), Legenda Gigante, Punch-in, Checklist marcando, CTA de Comentário.
- **Áudio:** riser curto e tick por segundo na contagem, alinhados pelo pico; impact no carimbo; pop em cada check; trilha a 0,05 com ducking na resposta.
- **CTA:** "Comenta V ou M: o que você respondeu antes do zero?" e "Salva para lembrar antes do seu lançamento." No story do mesmo dia, quiz nativo com a mesma crença.
- **Critério de trecho:** só existe se o Bruno disse a crença e a correção. Marcadores: "muita gente acha", "todo mundo fala", "o pessoal pensa", "dizem que", seguidos em até 20 s de "mas", "na verdade", "não funciona" ou "ao contrário". Crença de até 3 s, resposta de 12 a 20 s, nota 7 ou mais. Só crenças sobre lançamento, nunca sobre a profissão do público. Sem trecho assim, o formato não roda.
- **Gatilho:** o quiz obriga a tomar posição em 2 s; V ou M é o comentário mais fácil de dar; o carimbo paga a curiosidade e a cor que volta é a recompensa.
- **Paleta e tipografia:** selo MITO #141210 com borda e texto #F5C46E; selo VERDADE #E8B36A com texto #141210; risco em ouro, nunca vermelho (o `strike` do dent.html é vermelho e muda aqui).
- **Referências:** `videos/nichos/dentista/engine/dent.html` (`relogio()`, `letter()` com strike); `videos/nichos/dentista/engine/comp.py` (P&B com cor voltando em 6 quadros); `/home/user/yihui-dev/awesome-opus5-5-videos/prompts/twoclipping-402193.md` (molas, check).
- **Por que:** fusão dos 2 juízes, com a voz real desde o quadro 1 (juiz 2), que resolve o pulo da contagem muda. Corrigi um furo: com o vídeo andando durante a contagem, a voz dele entregaria a resposta; agora a contagem tem 2 s de sala sem voz. Nota 6: participação alta, mas o carimbo pode simplificar o raciocínio do estrategista e a existência do trecho é incerta.

---

## 8. Calendário (4 semanas, dias e horários)

**Base (fato):** seguidores online no pico às 18h (428) e às 19h (423); melhor post do período num domingo às 18h29; posts às 21h com média de 72; quarta é o melhor dia (102 em 3 posts); sábado sem dado. Amostras pequenas e misturadas com formato: tratar como indício.

**Regra de ritmo**
- Os reels de nicho continuam intocados: 1 por dia útil às 21h (seg consórcio, ter dentista, qua nutricionista, qui psicólogo, sex advogado). O carrossel de fim de semana do plano de nichos também continua.
- A entrevista ocupa: 1 reel fixo no sábado às 18h30; 1 reel no domingo às 18h30 **só com o portão aberto**, a partir da semana 2; o segundo carrossel da semana na quarta às 12h; stories todo dia.
- Nunca 2 reels no mesmo dia, nunca mais de 2 posts no dia.
- Isso leva o ritmo aprovado (5 reels e 2 carrosséis) a 6 reels por semana, ou 7 com o portão aberto. É um TESTAR com portão, não uma regra nova.

**Semana 0 (sex 23/10 a seg 26/10, preparo)**
- Sex 23: pedir a autorização da Mirna e a data de exibição; copiar arnndn e scripts para o repo; instalar faster-whisper; disparar o passe de áudio.
- Sáb 24 a seg 26: Whisper, diarização, folha de contato, `pontuar.py`, `capitulos.json` e `cortes.csv`; passe de vídeo com tonemap em segundo plano (cerca de 3 h 15 min ou mais); desfoques fixos; generalização do motor.
- Até qui 29: selfie do REACT (20 min, qualquer dia, só o celular): 6 reacts, 12 aberturas "Isso eu falei na TV." e a abertura do TIMELAPSE.
- Antes de cada render: tabela do Prompt 2 aprovada, folha de 4 quadros por segundo com nota por efeito (refazer abaixo de 8), as 6 conferências.

**Semana 1 (26/10 a 01/11)**
- Seg a sex, 21h: nicho.
- Ter 27 a sex 30: stories de pré-estreia (bastidor anotado, 5 s de timelapse, caixa "o que você perguntaria", enquete do assunto e contagem).
- Qua 28/10, 12h: CARROSSEL 01 (A), se a transcrição fechar até seg 26; última lâmina: "O primeiro corte sai sábado, 18h30." Se não fechar, a semana fica só com o carrossel do plano de nichos.
- Sáb 31/10, 18h30: **REACT 01** (abre a série, com o círculo "esse atrás do monitor sou eu"). Se a selfie não existir até qui 29: PB 01 versão B.
- Dom 01/11: sem reel da entrevista.

**Semana 2 (02 a 08/11)**
- Seg 02/11 (Finados): Módulo 7 com 48 h do REACT 01 e os nichos da semana; atualiza a mediana; decide o portão de dom 08/11. Registrar em `conteudo/sistema-instagram/semanas/2026-11-02.md`.
- Seg a sex, 21h: nicho. Stories: MANCHETE de manhã, sticker à tarde, repost à noite, checklist na terça e na sexta.
- Qua 04/11, 12h: CARROSSEL 02 (B, quiz, se houver crença rebatida; senão A). Prazo da autorização da Mirna.
- Sáb 07/11, 18h30: **TIMELAPSE** (índice e votação; enquete igual nos stories).
- Dom 08/11, 18h30 (portão): **PB 01** (versão A, com selfie).

**Semana 3 (09 a 15/11)**
- Seg 09/11: Módulo 7 (`semanas/2026-11-09.md`).
- Seg a sex, 21h: nicho; PROFISSAO nos stories da tarde no dia do nicho correspondente, se houver trecho.
- Qua 11/11, 12h: CARROSSEL 03 (A, tema mais votado).
- Sáb 14/11, 18h30: **PERGUNTA 01** (a mais votada; sem votos, a de maior nota). Sem autorização: versão só texto, ou troca com o PB 01 se este não saiu no domingo.
- Dom 15/11 (feriado), 18h30 (portão): **CINEMA 01** (sem autorização, versão com freeze no Bruno). Alcance de feriado: sem dado.

**Semana 4 (16 a 22/11)**
- Seg 16/11: Módulo 7 (`semanas/2026-11-16.md`).
- Seg a sex, 21h: nicho (sex 20/11 é feriado; o nicho segue o próprio plano).
- Qua 18/11, 12h: CARROSSEL 04 (A ou B).
- Sáb 21/11, 18h30: **vaga do vencedor**: segundo episódio do formato da entrevista com maior vs_median_x até 16/11. Padrão: REACT 02. Se o PB 01 vencer, entra o PB 02 (versão B, sem selfie), que fecha o A/B.
- Dom 22/11, 18h30 (portão): **PONTOS 01**.
- Seg 23/11: Módulo 7 decide a semana 5.

**Se o portão fechar:** os domingos ficam vazios e os sábados seguem REACT 01, TIMELAPSE, PB 01 (versão A) e REACT 02. PERGUNTA, CINEMA e PONTOS vão aos stories em 15 s e ao banco.

**Portão (lido no Módulo 7 de cada segunda, com 48 h ou mais de cada reel)**
1. Média dos reels da entrevista da semana em 0,8x da mediana ou mais e pulo médio abaixo de 75%, e reels de nicho da mesma semana sem queda abaixo de 0,8x da semana anterior: o domingo seguinte abre.
2. Média abaixo de 0,5x, ou pulo médio acima de 75%: fica só o sábado, sempre com um formato com rosto (REACT ou PB versão A), e o resto vai para os stories.
3. Formato abaixo de 0,8x com pulo acima de 75%: PARAR. A vaga vai para o vencedor ou para SALA, PROFISSAO ou MITO do banco.
4. Formato em 2x ou mais: DOBRAR. O próximo episódio dele ganha a próxima vaga.
5. Dois formatos sem selfie seguidos abaixo de 0,5x: só REACT e PB versão A ficam no feed até haver dado novo.
6. Reel com 150 ou mais de alcance em 48 h: o próximo do mesmo formato pode usar TABULEIRO (comentário fixado e automação no PostZen), dentro da regra de uma palavra-chave por mês.
- Referência com a mediana oficial de 53: 0,8x = 42, 0,5x = 27, 2x = 106. Se o Módulo 7 atualizar a mediana, os limites mudam junto.

**Banco para a semana 5 em diante:** REACT 03, PB 02 e 03, PERGUNTA 02 (variante cold open) e fase 2 "Você perguntou", CINEMA 02, SALA, PROFISSAO como reel, MITO e as 2 MANCHETES com mais respostas.

**Medição:** por post, `ig_post_stats` (alcance, vs_median_x, pulo, tempo assistido, compartilhamentos, salvamentos); respostas de story e direct no `ig_inbox`; disparos no `listCommentAutomationLogs` do PostZen; diagnósticos vindos da série. Cada rodada em `conteudo/sistema-instagram/semanas/AAAA-MM-DD.md`. Métrica que faltar: "sem dado".

**Avisos**
- A tabela "Próximos 7 dias" do Módulo 7 no `00-SISTEMA.md` tem dias da semana trocados: 22/10/2026 foi quinta (está "Qua 22") e 27/10 é terça (está "Seg 27"). Conferir antes de agendar.
- O Módulo 1 deixou trial reels para depois: se TIMELAPSE ou PONTOS devem sair como trial é decisão do Módulo 7, não deste catálogo.

---

## 9. O que mudou em relação aos juízes (viabilidade)

1. **Fonte HDR HLG:** os 2 juízes trataram o material como SDR. Tonemap obrigatório no passe de vídeo.
2. **Disco e tempo:** a fonte de 22 GB não cabe nos 17 GB livres; só existem 9,6 s convertidos; o passe completo leva cerca de 3 h 15 min. Um passe único em fluxo gera ABERTO, Z2 e ABERTO a 3 qps. CB e CM saem do Z2, e só o CINEMA volta à fonte de 60 fps.
3. **Enquadramento:** no quadro de 900 s, o Bruno está em 3/4 com o rosto visível acima do monitor. "De costas" virou "atrás do monitor" em toda copy, e a folha de contato entrou no filtro de frase.
4. **Quadro de planejamento:** tem 400x410 px, está cortado e fica fora do Z2. Insert em tela cheia seria 4,6x: virou detalhe no recorte nativo CE, e a parede passou a ser a superfície principal.
5. **Contraste:** parede cinza clara e mesa branca. Texto branco só com caixa ou com a parede escurecida; ouro só atrás de texto escuro; a legenda do CINEMA foi para dentro da barra de baixo.
6. **Regra de 2 s:** REACT, CINEMA, PROFISSAO, PB e BASTIDOR tinham 2 ou 3 efeitos novos no mesmo segundo. Todas as estruturas foram reespaçadas.
7. **Strobo:** de 15 piscadas por segundo para troca de palavras sem quadro vazio; sem pulso de tela cheia.
8. **Custo:** TIMELAPSE e PONTOS sem máscara (texto e pontos nunca cruzam as pessoas); SALA sem homografia na parede e sem máscara do monitor; `cap.js` pula a camada back vazia. Só o SALA continua com 2 camadas o tempo todo.
9. **Ampliação:** CB a 1,4x e punch-in de 1,08 no CB, para não passar de 1,5x sobre o 4K.
10. **Torre:** o path SVG do logo já existe no tv.html.
11. **Formatos:** BASTIDOR absorvido (REACT 01, abertura do TIMELAPSE e stories de terça); 12 formatos no lugar de 13 e 11.
12. **Calendário:** sábado fixo às 18h30 (janela de 18h a 20h do Buzzfy) e domingo só com portão, em vez de 2 reels por semana desde o início (juiz 1) ou do domingo às 21h com portão de 48 h lido 24 h depois do sábado (juiz 2).
