# Plano da cadeira A · CRO e landing page · Reel do dentista · Agência Reunida Modo GOD · 21/10/2026

Cliente: O Estrategista (@o_estrategista.com.br).

| Campo | Conteúdo |
|---|---|
| Persona | Especialista em conversão de página e oferta. Trato o reel como uma página: a dobra é o que o espectador mediano vê antes de sair (6,2 s), o botão é o comentário, o pós-clique é a resposta do Bruno e o Tabuleiro |
| OTIMIZA PARA | Oferta, prova, fricção e velocidade, nesta ordem |
| PONTO CEGO (assumido) | Achar que a página resolve falta de demanda. Uma edição perfeita com alcance de 53 continua gerando perto de zero conversa. Compensação, por escrito: (1) toda previsão de conversão desta cadeira vem limitada pelo alcance, com conta; (2) o esforço de render fica proporcional ao alcance esperado (A primeiro, B e C só depois do áudio aprovado); (3) a seção "antes do clique" tem ações de distribuição sem verba; (4) nenhuma métrica de conversão com N = 1 decide formato |
| PERGUNTA CONTRÁRIA | E se o problema estiver antes do clique? Resposta curta: provavelmente está. Ver seção 2.15 |

Etiquetas: [FATO] com fonte · [ESTIMATIVA] com conta ou premissa · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, nível 4, nunca fecha objeção sozinho.

Medições novas feitas por esta cadeira em 21/10/2026 (somente leitura, nada gravado fora desta pasta; um script auxiliar foi criado e apagado no scratchpad, registrado aqui por transparência):
- M1 [FATO] Codificar voz_master.wav em AAC 128k (por pipe, sem arquivo) sobe o true peak de -0,5 para -0,3 dBTP e mantém -14,2 LUFS (ffmpeg ebur128 peak=true).
- M2 [FATO] voz_master.wav com limitador em 0,82 (cerca de -1,7 dBFS) a 192 kHz e depois AAC 128k mede -14,5 LUFS e true peak -1,4 dBTP. Logo o alvo da D1 cabe com folga se o limite for aplicado antes da codificação.
- M3 [FATO] Energia em janelas de 40 ms do voz_master: o silêncio real fica entre -53 e -63 dBFS (19,84 a 20,12 s; 13,36 a 13,48 s; 13,76 a 13,88 s), ou seja 39 a 49 dB abaixo da fala (-14,1 dBFS). Percentil 5 de todo o arquivo: -53,4 dBFS.
- M4 [FATO] As "pausas" que reprovam o critério de 40 dB em DR02 têm som em nível de fala dentro da janela do alinhamento: 13,56 a 13,64 s a -13 e -14 dBFS (palavra, estalo ou respiração, só o ouvido diz); 31,58 a 31,78 s a -11 a -18 dBFS (cauda de "produto.", o alinhamento cortou cedo); 19,64 a 19,80 s a -22 a -26 dBFS (respiração provável); 5,38 a 5,50 s a -29 a -35 dBFS (respiração provável). Um gate (agate threshold 0,02) não mudou essas janelas, o que confirma que não é ruído de fundo.
- M5 [FATO] Página de destino `estrategistadelancamento.com.br/tabuleiro/?o=ig-dentista` (GET, 21/10/2026): HTTP 200, 20,9 KB de HTML, servidor Vercel com cache HIT, uma leitura com 1,15 s até o primeiro byte a partir deste contêiner (amostra única, não representa celular). 12 perguntas com 3 opções (36 rádios), nenhum campo de e-mail ("Nada de e-mail, nada de cadastro"), resultado que abre o WhatsApp com mensagem pré-preenchida. Nenhuma ocorrência de location.search ou URLSearchParams no HTML, em main.js e em tabuleiro.js; nenhuma de gtag, fbq ou dataLayer. Ou seja, o parâmetro `o=ig-dentista` previsto no 06-plano-final.md seção 9.2 não chega à mensagem do WhatsApp nem a uma ferramenta de análise no navegador. Logs do servidor: sem dado. A página não cita dentista; as perguntas pressupõem produto e evento já existentes ("O evento já tem data", "A oferta está fechada: preço...").

---

## 1. Veredito (até 12 linhas)

1. Produzir os 3 modelos com a MESMA camada de conversão (título fixo legível no frame 0, nota de fonte do CFO, rótulo da oferta a partir de 22,70 s, CTA visual "Comenta a sua profissão: DENTISTA"), para que o júri compare forma e não porta.
2. Publicar em 29/10 o Modelo A enxuto (Tzur v2 sem manifesto, sem confete, 5 letreiros atrás, legenda palavra a palavra): rosto em 98,6% do tempo, zoom máximo 1,12x, pipeline já rodado.
3. B = tela dividida que explica a fala (stokebuilder-356793 + twoclipping-551116 + twoclipping-000267 + modelo.html da Série 2). C = tipografia arquitetônica com órbita atrás da cabeça (twoclipping-041659 + gdgtify-929495 + alex-prompter-997524 + techhalla-498547). B fica de variante (trial reel se a conta tiver o recurso, B23).
4. Áudio: remasterizar a partir do voz_master.wav, limitador antes do AAC (M2 prova que fecha -14 LUFS e -1,4 dBTP), medir no MP4 final. O "ruído nas pausas" de DR02 é respiração e cauda de palavra (M4), não ruído: o silêncio real já está 39 a 49 dB abaixo da fala (M3).
5. Legenda corrige "em Brasil" para "no Brasil" e "forna que a gente" para "formar quem", depois de ouvir (B02). Palavras de 0,04 s indicam erro do alinhamento, não da fala.
6. Tzur fora da tela: não foi dito e a autorização não está confirmada.
7. O maior risco está antes do clique: com alcance de 106, a conta prevê de 0 a 7 comentários. A peça não salva o mês sozinha; a bio antiga e a origem perdida no WhatsApp (M5) vazam o pouco que chegar.

---

## 2. Respostas às 14 perguntas

### 2.1 Qual modelo a cadeira defende e quais prompts entram

Defendo **publicar o Modelo A enxuto com a camada de conversão** e produzir B e C como pedido pelo Bruno.

Motivo pela ordem da cadeira:
- Oferta: a oferta falada ("Eu desenho seu lançamento") começa em 22,70 s [FATO, words-raw.json], 3,7 vezes o tempo mediano assistido de 6,2 s [FATO, F12; ESTIMATIVA 22,70/6,2]. Sem texto de oferta acima da dobra, o espectador mediano nunca vê a oferta. Isso vale para os 3 modelos, por isso a camada é comum.
- Prova: o único número verificado é o do CFO [FATO, F68]. Não há prova do Bruno dita nesta tomada [FATO, F10].
- Fricção: o CTA falado ("comenta a sua profissão") pede que a pessoa adivinhe a palavra. Na tela vira "Comenta a sua profissão: DENTISTA".
- Velocidade: A é o único com pipeline já rodado ponta a ponta (Tzur v2, F25) e com máscara pronta (F27).

O único fator medido na conta é o Bruno em cena (2,4x a 5,8x a mediana) [FATO, F13]. Entre os três, A mantém o rosto em tela cheia por mais tempo.

| Modelo | Ids do repositório | Aproveita | Descarta |
|---|---|---|---|
| A | nenhum obrigatório (é o nosso Tzur v2). Empresta só de twoclipping-000267 (SFX pelo pico, loudnorm) e de techhalla-498547 (punch-in até 1,08 a 1,12) | letreiro 3D atrás (ov2.html camada de trás), legenda palavra a palavra (cap2.js), P&B que volta à cor no número, bloco final com letterbox e granulação semeada | manifesto com confete e aplausos (partícula sem motivo e efeito sonoro que não combina com "colegas"), "1.287 comentários" e @ inventados (F32), glifos de texto de coração, check e X (viram SVG), RGB split e tremida |
| B | stokebuilder-356793, twoclipping-551116, twoclipping-000267, modelo.html da Série 2 | regra do PiP: sempre que há gráfico, o rosto fica na tela; não inventar número (stokebuilder). Stickers recortados com borda branca como reacts, letras subindo por máscara, P&B que vira cor (551116). Lista de banidos, SFX pelo pico, -14 LUFS (000267). Cenas count, cross, cta (Série 2) | gráfico em tela cheia com rosto pequeno (stokebuilder, rosto pequeno demais em 9:16); 8 subquadros de 551116 (fica 3, como 000267, só nas transições); 60 fps de 000267 (fonte tem 30 quadros reais) |
| C | twoclipping-041659, gdgtify-929495, alex-prompter-997524, techhalla-498547 | órbita com metade de trás atrás da cabeça e legenda presa à palavra; transição que atravessa a cabeça (041659). Palavras que viram arquitetura e quietude de 400 ms (gdgtify). Esqueleto de 5 cenas mapeado na fala (alex-prompter). Mola por letra com 125 ms de escalonamento, punch-in 1,0 a 1,08, pré-passe de 8 stills para QA (techhalla) | cena de "prova" do alex-prompter (não há prova autorizada nesta fala); RGB split, desalinhamento magenta e verde e paleta do techhalla |

### 2.2 Rosto, tempo de tela e zoom

| Modelo | Rosto de 0 a 3 s | Rosto visível no total | Rosto em tela cheia | Zoom máximo |
|---|---|---|---|---|
| A | sim, tela cheia desde o f0 | 98,6% [ESTIMATIVA: só o insert de 13,32 a 13,84 s esconde o rosto; (36,43 - 0,52)/36,43] | 98,6% | 1,12x (2,1x da fonte: 1,875 x 1,12) |
| B | sim, tela cheia de 0 a 5,83 s | 100% (na divisão o Bruno fica na janela de 1080x1120) | cerca de 32% [ESTIMATIVA: 0 a 5,83 + 19,50 a 20,64 + 31,58 a 36,43 = 11,8 s] | 1,08x |
| C | sim, tela cheia | 100% | 100% (a transição de 0,43 s atravessa a cabeça, o rosto segue na tela) | 1,08x |

Os três passam o corte de 80% [HIPÓTESE, P16]. Fico abaixo do limite de 1,25x porque 1,25x vira 2,34x da fonte (DR06) e o risco R1 de pele lavada cresce com a ampliação.

### 2.3 Lista de edição quadro a quadro

Convenções: 30 fps de saída, 1093 quadros (0 a 36,43 s), linha do tempo original sem cortar pausas (frames = round(t x 30), conferidos com words-raw.json). Faixas em 1080x1920: título fixo em y 236 a 366 (frente); letreiro 3D em y 330 a 600 (atrás, parte de baixo passa atrás do cabelo; topo da pessoa entre y 252 e 555, mediana 420, F29); reacts em x 60 a 280 ou x 800 a 1020 e y 1050 a 1300, nunca na faixa do rosto (x 300 a 780); legenda em y 1340 a 1460, 2 a 4 palavras por página, palavra ativa em #E8B36A. Zona segura de baixo respeitada até y 1470 (DR09, nível 3). SFX: início = quadro do evento menos o pico medido (F35); nível de -20 a -24 dB abaixo do pico da voz [PRIOR, P03].

#### Modelo A enxuto com camada de conversão (lista completa)

| # | Início s (f) | Fim s (f) | Palavra que dispara | Camada | Texto na tela | Animação | SFX (início) |
|---|---|---|---|---|---|---|---|
| A01 | 0,00 (0) | 36,43 (1093) | "Dentistas" | tela cheia | (vídeo base.mp4) | máscara com maior componente conexo, sem corte em y=470 (R5, R6) | trilha lounge da Série 2 com ducking, ver 2.7 |
| A02 | 0,00 (0) | 22,22 (667) | "Dentistas" | frente, título fixo | "Dentista: sua técnica pode virar um 2º produto?" | já visível no f0, sem entrada animada (F53: texto no frame 0) | nenhum |
| A03 | 0,00 (0) | 3,18 (95) | "Dentistas" | tela cheia | (sem texto extra) | P&B (saturação 0); volta à cor em 6 quadros, f95 a f101 | sub em 3,176 s (f95) |
| A04 | 0,00 (0) | 36,43 (1093) | todas | frente, legenda | fala palavra a palavra; correções em 2.4 e 2.5; "porque" vira "Por que" | página troca na primeira palavra; palavra ativa em ouro | nenhum |
| A05 | 2,08 (62) | 5,49 (165) | "474" | atrás | "474 MIL" | contagem 0 a 474 durante a extrusão; rotateX 55° para 0° em 0,55 s (f62 a f79); saída 0,35 s (f155 a f165) | impact em 2,629 s (f79) |
| A06 | 2,08 (62) | 5,16 (155) | "474" | frente, nota | "Dentistas ativos, soma dos CROs. Fonte: CFO, 21/10/2026" | fade 6 quadros, 26 px, segunda linha do título | nenhum |
| A07 | 3,80 (114) | 5,16 (155) | "colegas" | frente, react ombro direito | SVG de 3 silhuetas (sem jaleco com logotipo, sem dente) | traço que se desenha 0,30 s mais escala amortecida | pop em 3,797 s (f114) |
| A08 | 7,61 (228) | 9,36 (281) | "hora" | frente, react ombro esquerdo | SVG de relógio | entra 2 quadros antes da palavra; ponteiro gira 1 volta | tick em 7,664 s (f230) |
| A09 | 7,68 (230) | 9,36 (281) | "hora" | atrás | "HORA DE CADEIRA" | extrusão f230 a f247; saída f270 a f281 | impact em 8,229 s (f247) |
| A10 | 7,68 (230) | 9,67 (290) | "hora" | tela cheia | (zoom) | punch-in 1,00 a 1,08 em 0,25 s (f230 a f238); volta a 1,00 de f281 a f290 | nenhum |
| A11 | 10,24 (307) | 13,32 (400) | "perfil" | frente, react ombro direito | 3 cartões de post iguais (retângulos abstratos, sem boca, sem raio X) | um cartão em "perfil" (f307), cópia em "diagnóstico" (f341), cópia em "conclusão" (f380) | shutter em 10,231 s (f307) |
| A12 | 13,32 (400) | 13,84 (415) | pausa após "conclusão." | tela cheia, insert | grade 3x3 de posts iguais | entra por corte seco, congela; 0,52 s; o áudio segue intacto (há som em 13,56 a 13,64 s, M4) | whoosh em 13,065 s (f392); swipe em 13,696 s (f411) |
| A13 | 17,11 (513) | 19,50 (585) | "aprender" | frente, react ombro esquerdo | SVG de lousa | traço 0,35 s | pop em 17,164 s (f515) |
| A14 | 19,50 (585) | 20,10 (603) | pausa após "mercado." | tela cheia | (zoom) | empurrão lento 1,00 a 1,10 durante a pausa; trilha cai a zero de 19,84 a 20,10 s (silêncio real medido, M3) | nenhum |
| A15 | 20,10 (603) | 22,22 (667) | "Qual" | tela cheia | (zoom) | segura 1,10; volta a 1,00 de f667 a f681 | nenhum |
| A16 | 20,64 (619) | 22,58 (678) | "ensinar" | atrás | "ENSINAR" (grande) e "O SEU COLEGA" (menor, segunda linha) | extrusão f619 a f636; saída f667 a f678 | impact em 21,196 s (f636) |
| A17 | 22,70 (681) | 31,58 (947) | "Eu" | frente, título fixo | "Eu desenho o seu lançamento" | troca do título por máscara de baixo para cima em 8 quadros | nenhum |
| A18 | 22,70 (681) | 24,24 (727) | "desenho" | frente, react ombro direito | SVG de tabuleiro 4x4 sendo desenhado por traço | traço de f685 a f706 | swipe em 22,696 s (f681) |
| A19 | 24,94 (748) | 26,38 (791) | "deixa" | frente, cartão em y 1180 a 1300 | "disputar paciente" | aparece em "deixa"; risco desenhado no fim de "disputar," (f786) | tick em 26,197 s (f786) |
| A20 | 27,58 (827) | 29,04 (871) | "forna" (ver 2.4) | frente, mesmo cartão | "formar quem disputa" | troca do texto riscado por este, letras subindo por máscara | pop em 27,564 s (f827) |
| A21 | 29,76 (893) | 31,58 (947) | "vira" | frente, react ombro esquerdo | SVG de relógio (produto 1) e SVG de lousa (produto 2), lado a lado | relógio reaparece em "vira", lousa entra em "segundo" (f923) | nenhum |
| A22 | 30,78 (923) | 31,95 (958) | "segundo" | atrás | "2º PRODUTO" | extrusão f923 a f940; saída f947 a f958 | impact em 31,329 s (f940) |
| A23 | 32,00 (960) | 36,43 (1093) | "Dentista" | tela cheia, bloco final | (letterbox) | barras pretas de 96 px entram em 0,30 s; granulação com semente pelo índice do quadro (R9); empurrão 1,00 a 1,06 linear de f960 a f1078 | whoosh em 31,732 s (f952) |
| A24 | 32,00 (960) | 36,43 (1093) | "Dentista" | atrás | "DENTISTA" | extrusão f960 a f977; fica até o fim | sub em 32,563 s (f977) |
| A25 | 32,68 (980) | 36,43 (1093) | "comenta" | frente, cartão de CTA em y 1150 a 1310 | "Comenta a sua profissão:" e campo de comentário SVG | cartão sobe em 0,30 s com curva amortecida, sem quique | nenhum |
| A26 | 33,82 (1015) | 34,40 (1032) | "profissão" | frente, campo do CTA | "DENTISTA" digitado letra a letra | 8 letras em 17 quadros | typing em 33,806 s (f1014) |
| A27 | 35,36 (1061) | 36,43 (1093) | "respondo." | frente | "que eu te respondo" sob o campo | fade 6 quadros; quadro final segura o CTA por 0,51 s (f1078 a f1093) | ding_si em 35,360 s (f1061) |
| A28 | capa | | | capa do reel | quadro f100 (3,33 s): rosto em cor, "474 MIL" pousado, título fixo | | |

Contagem de trocas de estímulo: 16 em 36,43 s, uma a cada 2,3 s [ESTIMATIVA], dentro da faixa de 1 a 3 s da Choppity (nível 3) e acima das 7 a 12 de DR12. SFX: 15 eventos; se o Bruno achar carregado, tirar primeiro A07, A13 e A20 (são reacts, não letreiros).

#### Modelo B · tela dividida que explica a fala (lista dos eventos que mudam em relação ao A)

| # | Início s (f) | Fim s (f) | Palavra | Camada | Texto | Animação | SFX |
|---|---|---|---|---|---|---|---|
| B01 | 0,00 (0) | 5,48 (164) | "Dentistas" | tela cheia | camada de conversão igual a A02, A05, A06 | igual ao A, sem P&B | igual ao A |
| B02 | 5,48 (164) | 5,83 (175) | "porque" | tela dividida | (entrada do painel) | painel opaco 1080x800 desce no topo, Bruno passa para a janela 1080x1120 embaixo, recorte segue o centro da máscara (média móvel de 9 quadros), deslocamento de 0,35 s com x(t) = 1 - (1 + wt)e^(-wt); linha de 4 px #E8B36A | whoosh em 5,565 s (f167) |
| B03 | 5,83 (175) | 9,36 (281) | "hora" | tela dividida, painel | "HORA DE CADEIRA" | relógio SVG grande, letras sobem por máscara em f230 | tick em 7,664 s (f230) |
| B04 | 9,36 (281) | 13,84 (415) | "perfil" | tela dividida, painel | grade 3x3 de posts iguais | cartões se duplicam em f307, f341, f380; na pausa (f400 a f415) o painel fica P&B | shutter em 10,231 s (f307) |
| B05 | 13,84 (415) | 19,50 (585) | "técnica", "mercado." | tela dividida, painel | "SUA TÉCNICA" e depois "UM MERCADO" | sticker de lousa com borda branca (551116) entra em "técnica" (f452); silhuetas de colegas entram em "dentistas" (f481) | pop em 15,077 s (f452) |
| B06 | 19,50 (585) | 20,64 (619) | pausa, "Qual é" | tela cheia | (sem painel) | painel sobe em 0,35 s; rosto em tela cheia; punch-in 1,00 a 1,08 em "Qual" | swipe em 19,363 s (f581) |
| B07 | 20,64 (619) | 22,22 (667) | "ensinar" | tela dividida, painel | "ENSINAR O SEU COLEGA" | painel volta; letras sobem por máscara | whoosh em 20,372 s (f611) |
| B08 | 22,70 (681) | 24,24 (727) | "desenho" | tela dividida, painel | "Eu desenho o seu lançamento" | tabuleiro 4x4 desenhado por traço | swipe em 22,696 s (f681) |
| B09 | 24,46 (734) | 29,04 (871) | "deixa", "forna" | tela dividida, painel | "disputar paciente" em P&B, depois "formar quem disputa" em cor | P&B que vira cor (551116) em f827 | tick em 26,197 s (f786) |
| B10 | 29,28 (878) | 31,58 (947) | "segundo" | tela dividida, painel | "2º PRODUTO" | relógio e lousa lado a lado, lousa acende em f923 | pop em 30,777 s (f923) |
| B11 | 31,58 (947) | 31,93 (958) | pausa | tela cheia | (saída do painel) | painel sobe em 0,35 s | swipe em 31,443 s (f943) |
| B12 | 32,00 (960) | 36,43 (1093) | "Dentista" | tela cheia | camada de conversão igual a A23 a A27 | igual ao A | igual ao A |

#### Modelo C · tipografia arquitetônica com órbita (lista dos eventos que mudam em relação ao A)

Mapa das 5 cenas do alex-prompter-997524 na fala: problema (0,00 a 13,32 s), o que existe (13,84 a 22,22 s), o que eu faço (22,70 a 24,24 s), virada no lugar da prova (24,46 a 31,58 s; não há prova autorizada nesta fala), nome e CTA (32,00 a 36,43 s).

| # | Início s (f) | Fim s (f) | Palavra | Camada | Texto | Animação | SFX |
|---|---|---|---|---|---|---|---|
| C01 | 0,00 (0) | 2,08 (62) | "Dentistas" | atrás | "DENTISTAS" como fachada | letras sobem como colunas, mola por letra com 125 ms de escalonamento (techhalla); título fixo da camada de conversão já no f0 | nenhum |
| C02 | 2,08 (62) | 5,49 (165) | "474" | atrás e frente | "474 MIL COLEGAS ATIVOS" em anel | órbita em volta da cabeça na altura do cabelo (y 380 a 520): metade de trás na camada de trás, metade da frente na camada da frente (041659); nunca desce até os olhos (y 850 em diante); nota do CFO igual a A06 | impact em 2,629 s (f79) |
| C03 | 7,68 (230) | 13,32 (400) | "hora", "perfil" | atrás | "HORA DE CADEIRA" como prédio; depois cópias idênticas do prédio | blocos empilham por andar; em "perfil", "diagnóstico" e "conclusão" surgem prédios iguais ao lado | tick em 7,664 s; shutter em 10,231 s |
| C04 | 19,60 (588) | 20,00 (600) | pausa após "mercado." | todas | (nada se move) | quietude de 400 ms: tudo congela, trilha a zero, nenhum SFX (gdgtify); a voz não é tocada | nenhum |
| C05 | 20,10 (603) | 20,64 (619) | "Qual" | frente | "QUAL É?" | entra seco, único momento de impacto no centro superior, longe dos olhos | impact em 20,096 s (f603) |
| C06 | 20,64 (619) | 22,22 (667) | "ensinar" | atrás | "ENSINAR O SEU COLEGA" como ponte entre dois prédios | ponte se monta por letra | nenhum |
| C07 | 22,82 (685) | 24,24 (727) | "desenho" | atrás | planta do tabuleiro em linhas | traço de planta baixa desenhado atrás da cabeça | swipe em 22,696 s (f681) |
| C08 | 24,94 (748) | 29,04 (871) | "deixa", "forna" | atrás | "DISPUTAR PACIENTE" desce ao chão; "FORMAR QUEM DISPUTA" sobe | descida sem tremida (banido em 000267) | sub em 27,576 s (f827) |
| C09 | 30,78 (923) | 31,58 (947) | "segundo" | atrás | "2º PRODUTO" | segundo prédio acende ao lado do primeiro | pop em 30,777 s (f923) |
| C10 | 31,58 (947) | 32,01 (960) | pausa | frente e atrás | (transição) | wipe que atravessa a cabeça usando a máscara como matte (041659) | whoosh em 31,732 s (f952) |
| C11 | 32,00 (960) | 36,43 (1093) | "Dentista" | tela cheia | camada de conversão igual a A23 a A27 | igual ao A | igual ao A |

Motion blur em C: 3 subquadros em t - 1/120, t e t + 1/120 s só nas janelas de movimento de tipo, mistura em alfa pré-multiplicado (F4 4.3) [PRIOR para o obturador, P04].

### 2.4 Trecho de 24,94 a 29,04 s ("forna que a gente disputa")

Posição: **ouvir antes de decidir (B02, cerca de 10 min) e, salvo surpresa, legenda corrigida para "Você deixa de disputar paciente e passa a formar quem disputa."**
- [FATO] No alinhamento, "a" tem 0,06 s e "gente" tem 0,04 s (F08). [PRIOR] Uma sílaba falada raramente dura menos de 0,1 s; palavra de 0,04 s indica que o reconhecedor encaixou palavras que não estão lá. É sinal de erro de transcrição, não de fala.
- Se o ouvido confirmar "formar quem" ou algo próximo: legenda corrigida, tempos do alinhamento.
- Se o ouvido confirmar "forna que a gente": a legenda corrigida passa a mostrar palavra que não foi dita. Aí a ordem é: (1) legenda "formar quem disputa" assim mesmo, porque a diferença de leitura labial em 0,7 s é pequena [HIPÓTESE]; (2) se o Bruno discordar, regravar só a frase e cobrir 26,88 a 29,04 s com insert em tela cheia no A (rosto cai para 92,7% [ESTIMATIVA: (36,43 - 0,52 - 2,16)/36,43]). Cortar fala: nunca.

### 2.5 "em Brasil" (4,80 a 5,16 s)

Legenda corrigida para "no Brasil". Duas letras em 0,16 s não criam desalinho visível [HIPÓTESE], e a legenda é o que o espectador sem som lê. O erro de gramática na tela pesa mais que a diferença com a boca.

### 2.6 474 mil na tela

Com fonte. Letreiro "474 MIL" atrás e nota na frente: "Dentistas ativos, soma dos CROs. Fonte: CFO, 21/10/2026". Não escrevo "mais de" na tela: a soma pode contar duas vezes quem tem inscrição em mais de um CRO (lacuna B19), e a fala já diz "mais de". Número exato que conferimos: 474.659 [FATO, F68]; outra leitura do dia deu 474.640 (C2). Os dois arredondam para 474 mil, então o conflito não muda a tela.

### 2.7 Áudio

Cadeia, toda com filtros que já existem neste ffmpeg 6.1.1 (conferido: highpass, deesser, equalizer, agate, acompressor, sidechaincompress, alimiter, loudnorm, ebur128):
1. Base: voz_master.wav (-14,2 LUFS, TP -0,5 dBTP) [FATO, F04]. Não refazer do raw sem motivo: o silêncio real já está 39 a 49 dB abaixo da fala (M3). Refazer do raw só se o ouvido achar artefato de redução de ruído (B01).
2. highpass f=80; deesser leve; equalizer +2 dB em 3 kHz, Q 1 [PRIOR, P sem teste].
3. Respirações: abaixar 10 a 12 dB (não apagar) nas janelas de M4 que o ouvido confirmar como respiração (5,38 a 5,50; 19,64 a 19,80; talvez 13,56 a 13,64). Isso resolve a maior parte da distância de 40 dB que DR02 não achou.
4. Mistura em numpy a 48 kHz por índice de amostra (F4 4.4): trilha lounge sintetizada (som.py) com ducking por sidechaincompress (ratio 6, attack 20 ms, release 300 ms), mirando a voz pelo menos 15 dB acima da trilha nos trechos falados [PRIOR]; SFX de -20 a -24 dB abaixo do pico da voz, colocados pelo pico (lista 2.3).
5. loudnorm em duas passadas: I=-14, TP=-1,5, LRA=7, linear=true. Uso -1,5 antes da codificação porque o AAC sobe o pico em cerca de 0,2 dB (M1) e o teste com limitador mais AAC fechou em -1,4 dBTP (M2). Isso resolve o conflito C7: -1,5 no WAV, -1,0 como teto medido no MP4.
6. Medida que vale: ebur128 peak=true no MP4 final de cada modelo. Aceite: -15 a -13 LUFS e true peak até -1,0 dBTP. Distância fala e silêncio medida só em janelas de silêncio real (energia abaixo de -45 dBFS por 200 ms ou mais), não nas janelas do alinhamento.
7. Entrega para aprovação: um arquivo de 10 s antes e depois no mesmo loudness (bruto normalizado a -14 contra master), para o Bruno ouvir a diferença e não só o volume [HIPÓTESE: reduz pedido de refazer].

### 2.8 Ampliação de 576x1024 para 1080x1920

- base.mp4 já existe em 1080x1920 e 30 fps com os mesmos 1093 quadros [FATO, F02]. Método da ampliação: sem dado (B17). Se precisar refazer: scale=1080:1920:flags=lanczos e depois unsharp leve só no luma [PRIOR, P18].
- Rosto: com zoom de 1,12x a ampliação total é 2,1x da fonte [ESTIMATIVA: 1,875 x 1,12]. Abaixo dos 2,34x do limite de 1,25x.
- Recorte rembg: a máscara sai de 320x320 (F31), cerca de 6 px por ponto na vertical em 1920. Halo no cabelo é certo onde o letreiro passa atrás. Mitigação: encolher a máscara 2 px, desfocar a borda (sigma 2), letreiro em ouro claro com extrusão escura para o halo não virar faixa colorida, e manter só o maior componente conexo (P22) para os 44 quadros com gente ao fundo (F30).

### 2.9 Pipeline e tempo de render

Só o que existe: Playwright e Chromium, ffmpeg, numpy, rembg (máscara já pronta), faster-whisper (só se for realinhar o trecho de B02), HTML, Canvas e SVG. Nada instalado.

| Modelo | Etapas | Tempo [ESTIMATIVA, F4 2.1] |
|---|---|---|
| A | ov2.html adaptado (camadas de trás e da frente) > cap2.js > comp.py corrigido (sem corte em y=470, maior componente, falha se faltar PNG) > mistura de áudio | cerca de 951 s (16 min); cerca de 8 min se a composição for por filtros do ffmpeg (B15, não testado) |
| B | painel por JPEG em pipe (capture.js) + legenda PNG + composição | cerca de 887 s (15 min) |
| C | overlay com 3 subquadros nas janelas de movimento + composição | 1008 a 1319 s (17 a 22 min); custo do glifo deformado sem dado (B14) |

Em série, nunca em paralelo (F28: 2 a 5 vezes mais lento). Ordem: áudio, A, envio ao Bruno, B, C. Antes de cada render cheio, render cronometrado de 300 quadros (B13).

### 2.10 CTA

- Falado: "Dentista, comenta a sua profissão aqui que eu te respondo" (32,00 a 35,92 s) [FATO, F11].
- Tela: "Comenta a sua profissão:" mais campo digitando "DENTISTA" e, embaixo, "que eu te respondo". Isso tira a adivinhação da palavra.
- TABULEIRO: fora da tela. Só no comentário fixado, e só se o reel passar de 150 de alcance em 48 h [FATO, regra do CLAUDE.md e 06-plano-final.md linha 181].
- Legenda do post (primeiras linhas, sem emoji e sem travessão): "Dentista: a sua técnica pode virar um segundo produto? Ensinar colega é um mercado. Eu desenho o lançamento. Comenta DENTISTA que eu te respondo. Número de dentistas ativos: soma dos CROs, CFO, 21/10/2026."
- Resposta: em até 2 h nas primeiras 48 h [PRIOR; o plano pede 24 h], com o roteiro de DM já aprovado (06-plano-final.md seção 8.4).

### 2.11 Conformidade com publicidade odontológica

A Res. CFO 196/2019 foi lida no texto oficial pela frente F3 [FATO, F72]; a pergunta diz "não lida", o livro de fatos já fechou isso. Na tela: nenhuma boca, dente real, raio X, instrumental, cadeira odontológica desenhada (P11: ícone de equipamento é zona cinza, então troco por relógio e lousa), antes e depois, preço, "grátis", sorteio, promessa de faturamento ou de agenda, "melhor técnica", caso de terceiro. O título é pergunta ("pode virar um 2º produto?"), não promessa. A nota do CFO dá fonte ao único número. O art. 45 do Código de Ética (responsabilidade de quem concorre para a publicidade) recai sobre o dentista que comenta ou reposta, não muda o vídeo [FATO, F73; aplicação ao Bruno: HIPÓTESE P13].

### 2.12 Prova e o case Tzur

Fora da tela nos 3 modelos.
1. Não foi dito [FATO, F10]: texto de prova sem fala parece colado.
2. Autorização não confirmada (B24).
3. "6 para 20 milhões" ao lado de "dentista" pode ser lido como promessa de resultado (regra de texto do CLAUDE.md).

Prova que entra: o número do CFO (prova de mercado) e a especificidade do método (tabuleiro desenhado, que é ativo próprio do Bruno). Se a autorização chegar, o case vai para a resposta da DM, não para a tela deste reel.

### 2.13 Métrica, fonte, data e critério de parar

| Métrica | Fonte | Leitura | Critério |
|---|---|---|---|
| Alcance em 48 h | ig_post_stats (Buzzfy), só leitura | sáb 31/10/2026 | abaixo de 53: o próximo nicho não usa o modelo publicado. 150 ou mais: liga TABULEIRO no comentário fixado |
| Alcance, views, tempo médio assistido e pulo em 7 dias | ig_post_stats | qui 05/11/2026 | PARAR o título com a oferta se o pulo passar de 68% (mediana); DOBRAR se ficar abaixo de 60% (corte do plano). Assim os dois cortes do conflito C1 têm papel diferente |
| Comentários com "dentista" | ig_comments (Buzzfy) ou listInboxPostComments (PostZen), só leitura | 31/10 e 05/11 | contagem bruta e quantos são de dentista de fato |
| Conversas qualificadas (definição da seção 8.5 do plano) | planilha de leads | 12/11/2026 | 0 com alcance de 106 ou mais: mexer na porta (CTA e resposta), não no nicho (06-plano-final.md linha 182) |
| Diagnósticos agendados vindos do nicho | planilha de leads e WhatsApp | 18/11/2026 | decisão do plano dos 5 nichos |

Registrar em `conteudo/sistema-instagram/semanas/` na rodada do Módulo 7.

### 2.14 Regras de texto

Textos de tela conferidos: português do Brasil, sem travessão, sem emoji (reacts em SVG), sem os três nomes vetados. A única construção de contraste é a falada ("deixa de disputar paciente e passa a formar quem disputa"); nenhum texto de tela cria outra frase "não é X, é Y".

### 2.15 Resposta à pergunta contrária: e se o problema estiver antes do clique?

Provavelmente está, e a edição não resolve isso.
- Mediana da conta: 53 de alcance, 74 views, 6,2 s assistidos [FATO, F12]. 30 dias: 448 visitas ao perfil, 7 cliques no link, 1 disparo de automação, 0 venda [FATO, 00-SISTEMA.md].
- Comentários por view nos 30 dias: 12/12.779 = 0,09% [ESTIMATIVA]. Com alcance de 106, cerca de 148 views (106 x 74/53) [ESTIMATIVA]. Com 0,09% a 4,8% de comentário por view (piso da conta, teto de @clinicavolpe com palavra-chave, F56), dá 0,1 a 7 comentários [ESTIMATIVA]. Com conversão de comentário para conversa qualificada desconhecida, o número esperado de conversas é perto de 1.
- Teto do nicho: reels de negócio falando com dentista tiveram no máximo 764 views na busca (F58).
- Vazamentos depois do clique que a edição não conserta: (1) a bio ainda era a antiga em 21/10 (00-SISTEMA.md, Módulo 1, prioridade 1) e converte 1,6% das visitas em clique; (2) o `o=ig-dentista` não chega ao WhatsApp nem a uma ferramenta de análise (M5), então a origem do lead some se a pessoa não disser; (3) as perguntas do Tabuleiro pressupõem lançamento em andamento, e o dentista do reel ainda não tem produto [HIPÓTESE: nota baixa pode desanimar].
- O que faço com isso: render proporcional (A primeiro), ações de distribuição sem verba (ideias 41 a 52), e nenhuma conclusão sobre formato com N = 1.

---

## 3. Decisões

### D1 · Áudio masterizado

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. voz_master.wav como está | zero trabalho | reprova o true peak (-0,5 e -0,3 depois do AAC, M1); somar trilha e SFX piora |
| 2. Remasterizar a partir do voz_master (cadeia 2.7) | fecha -14 LUFS e TP até -1,0 no MP4 (M2 mostra que cabe) | mesma voz nos 3 modelos; diferença só na mistura, o que limpa a comparação |
| 3. Refazer do raw comparando rn_std, rn_sh, rn_bd | controla a cadeia (B01) | horas de escuta; os três têm distância média de 14,3 a 16,3 dB contra 16,0 do master (DR02), sem ganho claro |
| 4. Regravar o trecho de 24,94 a 29,04 s | resolve a frase se estiver errada | timbre e sala diferentes; quebra a sincronia com a boca, exige insert de 2,16 s |
| 5. Fora do óbvio: trocar o critério de 40 dB por "silêncio real" e entregar o par antes e depois no mesmo loudness para aprovação | o critério passa a medir ruído e não respiração (M3, M4) | aprovação mais rápida e menos subjetiva; risco de parecer que mudamos a régua para passar |

- Premissas: o ouvido do Bruno aceita respiração atenuada; o AAC do Instagram se comporta como o nosso (sem dado); a mistura não passa a voz para trás da trilha.
- **Posição: 2 + 5**, com 4 só se B02 mostrar erro que muda o sentido.
- Probabilidade de cumprir o critério da D1 (3 de 3 no loudness, TP, voz acima da trilha e zero pedido de refazer): **0,60, faixa [0,40; 0,80]**. Loudness e TP sozinhos: 0,95 (M2). O que puxa para baixo é "zero pedido de refazer" e o critério de 40 dB se ficar medido pelo método antigo.
- Confiança: **0,55**.

### D2 · Modelo A

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. Tzur v2 fiel (manifesto P&B, confete, aplausos, bloco final) | máximo de "o que já fazemos" | confete e aplausos sem motivo; o bloco final do Tzur tem prova inventada (F32), que precisa sair de qualquer jeito |
| 2. Tzur v2 enxuto (4 letreiros, sem manifesto) | menos ruído visual | perde a virada de cor do começo, que é a troca de estímulo mais barata antes de 3 s |
| 3. Tzur v2 fiel com legenda palavra a palavra | legenda no frame 0 (F53) | tela carregada nos primeiros 5 s |
| 4. Fora do óbvio: A enxuto com camada de conversão (título fixo com a tese, nota do CFO, rótulo da oferta, CTA digitado, capa escolhida) | a oferta aparece acima da dobra de 6,2 s | o título revela a resposta antes da fala: pode baixar a curiosidade e subir o pulo [HIPÓTESE]; ganha clareza para quem fica |

- Premissas: título fixo com a tese segura a abertura (P06, F55, N = 10); o letreiro atrás continua legível com a cabeça cobrindo o centro (sem dado, testar com 1 quadro por letreiro); o Bruno publica em 29/10.
- **Posição: 4** (enxuto com P&B que volta à cor em "mil", 5 letreiros, legenda, camada de conversão).
- Probabilidade pelo critério do enquadramento (produção ok e, publicado, alcance de 106 ou mais e pulo abaixo de 68% em 7 dias): **0,38, faixa [0,18; 0,58]**. Produção sozinha: 0,85. Desempenho: os 3 melhores reels com o Bruno tiveram 126 a 307 de alcance e 46% a 53% de pulo [FATO, 00-SISTEMA.md], mas quantos reels com o Bruno ficaram abaixo de 106 é sem dado, e o nicho estreito puxa para baixo (F58). O plano marcou 0,40 como PRIOR (P21).
- Confiança: **0,30**.

### D3 · Modelos B e C

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. B = sab8a + gdgtify (punchy com tipo arquitetônico); C = alex-prompter + máscara de tipo de 000267 | dois formatos de tipografia | B e C ficam parecidos entre si; ninguém atende "dividindo com reacts" |
| 2. B = tela dividida com reacts e animação; C = tipografia arquitetônica | cobre os dois itens literais do Bruno ("dividindo" e "letreiro") | B baixa o rosto em tela cheia para cerca de 32% |
| 3. Só B agora, C depois do primeiro resultado | menos render | descumpre "faça outros 2" |
| 4. Não fazer B e C | zero custo | descumpre o pedido |
| 5. Fora do óbvio: C = A com outra camada de conversão (título de identificação "Dentista, você só vende hora de cadeira?") | único teste que isola a porta | não é formato novo; não atende o pedido sozinho. Fica como variante de capa e título, não como modelo |

- Premissas: o júri cego de 3 cadeiras tem protocolo (B25 não existe ainda); as cenas SVG cabem no custo estimado; o Bruno aceita rosto em janela por 68% do tempo em B.
- **Posição: 2**, com a minha mistura: B = stokebuilder-356793 + twoclipping-551116 + twoclipping-000267 + Série 2; C = twoclipping-041659 + gdgtify-929495 + alex-prompter-997524 + techhalla-498547. Camada de conversão igual nos 3. Publicação: A principal; B como trial reel se o recurso existir (B23), senão guardado para outro nicho.
- Probabilidade pelo critério (júri dá a B e a C nota igual ou maior que A, cada modelo com ids, rosto de 0 a 3 s, sem banidos sem motivo, 1080x1920, nenhuma palavra cortada, lista quadro a quadro): **0,45, faixa [0,25; 0,65]**. Partes de produção: 0,85. Júri: incerto, porque A é a referência de acabamento já feita. Desempenho publicado: exploratório, N = 1.
- Confiança: **0,30**.

---

## 4. Ideias e hipóteses numeradas

Confiança: alta, média ou baixa. Evidência ao lado.

**Oferta (o que a pessoa entende que ganha)**
1. Título fixo com a tese no frame 0 nos 3 modelos. Média. F53 (10 de 10 com texto no frame 0), F55.
2. Título em forma de pergunta para não virar promessa de resultado. Alta. CLAUDE.md; F72.
3. Rótulo "Eu desenho o seu lançamento" fixo de 22,70 a 31,58 s, para quem chega no meio. Média. A oferta falada está em 22,70 s (words-raw.json).
4. A oferta precisa estar legível antes de 6,2 s, a dobra do espectador mediano. Média. F12.
5. Capa escolhida no f100 com rosto, "474 MIL" e título; a capa é o anúncio na grade do perfil. Média. 448 visitas ao perfil em 30 dias (00-SISTEMA.md).
6. Legenda do post repete a pergunta do título na primeira linha. Média. PRIOR de leitura na prévia.
7. Não mostrar "diagnóstico gratuito" na tela; a oferta do vídeo é o desenho do lançamento, o diagnóstico vem na DM. Alta. F3 (sem "grátis" na tela); 06-plano-final.md 8.4.
8. "2º PRODUTO" é a palavra que fecha a oferta; letreiro atrás e react de duas peças (relógio e lousa) para fixar a imagem. Média. Fala de 29,28 a 31,58 s.
9. Reutilizar os ícones do começo (relógio = hora de cadeira) no fim (relógio e lousa) para a oferta fechar o arco visual. Média. PRIOR de design.
10. Testar, em outra peça, título de identificação ("você só vende hora de cadeira?") contra título de oferta. Baixa. P06, sem teste na conta.

**Prova**
11. Nota "soma dos CROs, CFO, 21/10/2026" em vez de "CFO, out/2026", para mostrar o método da soma. Alta. F68, B19.
12. Não escrever "mais de" na tela. Média. Possível dupla contagem (B19).
13. Tzur fora da tela deste reel. Alta. F10, B24.
14. Prova de método: tabuleiro desenhado como react em "desenho". Média. Ativo próprio (página do Tabuleiro, M5).
15. Se o Tzur for autorizado, usar na 2ª DM e não no reel. Média. 06-plano-final.md seção 7 item 5.
16. Nenhum contador de comentários ou @ na tela. Alta. F32.
17. Quando o reel tiver comentários reais de dentistas, um story com print (com permissão de quem comentou) vira prova social verdadeira. Baixa. PRIOR; F73 art. 45 recai sobre quem comenta.
18. Número exato 474.659 só em texto de legenda do post, com data e hora da leitura. Baixa. C2 mostra que muda no dia.

**Fricção**
19. CTA na tela escreve a palavra: "Comenta a sua profissão: DENTISTA". Alta. Fala ambígua (F11).
20. CTA digitado letra a letra imita o gesto que pedimos. Média. PRIOR.
21. CTA visível nos últimos 4,43 s e no quadro final segurado 0,51 s. Média. A fala termina em 35,92 s.
22. Nenhum outro pedido no vídeo (seguir, salvar, link). Alta. Uma porta só (06-plano-final.md D3).
23. TABULEIRO fora da tela, só no fixado com 150 ou mais em 48 h. Alta. CLAUDE.md.
24. Resposta pública ao comentário com o texto já aprovado, sem link, para não pedir outro clique. Média. 06-plano-final.md 8.4.
25. Pedir ao Bruno para ler as primeiras respostas em voz de "colega", sem perguntar faturamento na 1ª DM. Média. 06-plano-final.md 8.4 item 5.
26. Na página do Tabuleiro, levar a origem `o` para a mensagem do WhatsApp; é sugestão ao Bruno, a cadeira não edita o site. Alta. M5.
27. Na página do Tabuleiro, uma linha para quem ainda não tem produto ("ainda não lancei") evitaria nota zero sem leitura útil. Baixa. M5, perguntas pressupõem lançamento.
28. Comentário de dentista que não tem audiência recebe o caminho "segue o perfil" do roteiro, sem diagnóstico. Alta. 06-plano-final.md 8.4 item 4.

**Velocidade**
29. Responder comentário em até 2 h nas primeiras 48 h. Baixa. PRIOR.
30. Áudio primeiro, render de A logo depois, B e C só depois do OK do áudio. Alta. F28, B13.
31. Render de 300 quadros cronometrado antes de cada render cheio. Alta. B13.
32. Composição por filtros do ffmpeg testada em 300 quadros; se igualar o comp.py, A cai de 16 para cerca de 8 min. Média. F26, B15.
33. Não cortar pausas em A: ganho de 1,9 s antes da oferta não paga o salto de imagem em selfie de mão. Média. DR03; F07.
34. Em B, o painel entra em "porque" (5,48 s), logo depois da regra dos 3 s. Média. CLAUDE.md.
35. Enviar ao Bruno uma prévia leve (2,55 Mb/s) para aprovar pelo celular. Média. F25.

**Edição e forma**
36. 5 letreiros em A (474 MIL, HORA DE CADEIRA, ENSINAR, 2º PRODUTO, DENTISTA). Média. Opção enxuta da D2.
37. Letreiro na faixa y 330 a 600, com a parte de cima sempre acima do cabelo. Média. F29, DR10.
38. Teste de legibilidade com 1 quadro por letreiro antes do render. Alta. Sem dado de legibilidade.
39. P&B que volta à cor em "mil" mantém a troca de estímulo antes de 3,2 s sem esconder o rosto. Média. Tzur v2; F13.
40. Insert de 0,52 s na pausa após "conclusão." é o único momento sem rosto em A. Média. F07.
41. Quietude de 400 ms em C entre 19,60 e 20,00 s; o silêncio real medido vai de 19,84 a 20,12 s. Média. F47, M3.
42. Órbita de C na altura do cabelo, nunca na altura dos olhos. Alta. Critério da D2.
43. Halo da máscara tratado com erosão de 2 px e borda desfocada. Média. F31, R3.
44. Maior componente conexo da máscara para os 44 quadros com gente ao fundo. Alta. F30, P22.
45. Tirar o corte fixo em y=470 do comp.py. Alta. F29.
46. Reacts só em SVG, fora da faixa do rosto (x 300 a 780). Alta. F4 4.2.
47. Nenhum item banido (shockwave, partículas, RGB split, tremida, lens flare, neon) em B e C. Alta. F48.
48. Motion blur só nas janelas de movimento, em alfa pré-multiplicado. Média. F4 4.3.
49. Granulação com semente pelo índice do quadro. Alta. R9.
50. Letterbox no bloco final em vez de outro efeito: sinal de "cena final" sem custo de render. Baixa. PRIOR.

**Antes do clique (demanda, sem verba)**
51. Trocar a bio antes de 29/10 pela do Módulo 2; é a página que recebe quem gostou do reel. Alta. 00-SISTEMA.md Módulo 1 (13% e 1,6%).
52. Publicar no melhor horário lido no ig_best_times (só leitura). Média. 06-plano-final.md linha 558.
53. Story no dia com a caixa de perguntas do plano (9.5) apontando para o reel. Média. 06-plano-final.md 9.5.
54. Repostar o reel nos stories em D+1 e D+3 com outra frase do vídeo. Baixa. PRIOR.
55. B como trial reel para não seguidores, se a conta tiver o recurso. Média. B23 sem dado.
56. Pedir a 1 dentista conhecido do Bruno para comentar de verdade nas primeiras horas, sem roteiro. Baixa. PRIOR; art. 45 recai sobre ele, mas não há conteúdo clínico.
57. Collab com um dentista que já ensina colega, num próximo reel, não neste. Baixa. PRIOR; risco regulatório para o dentista (F73).
58. Não publicar os 3 modelos no mesmo dia nem na mesma semana. Média. P15.
59. Não impulsionar: verba zero até 18/11. Alta. F18.
60. Hashtag e texto alternativo com "dentista" para a busca do Instagram. Baixa. PRIOR.

**Áudio**
61. Limite de -1,5 dBTP antes do AAC. Alta. M1, M2.
62. Medir no MP4, não no WAV. Alta. M1.
63. Respiração atenuada 10 a 12 dB, nunca apagada. Média. M4.
64. Critério de ruído medido em silêncio real. Média. M3.
65. Trilha a zero na quietude de C e na pausa de A (19,84 a 20,10 s). Média. F47.
66. SFX alinhado pelo pico, com início calculado. Alta. F35, F48.
67. Se o Bruno achar SFX demais, cortar os de react primeiro, nunca os de letreiro. Baixa. C4.
68. Par antes e depois no mesmo loudness para aprovação. Média. PRIOR.

**Medição**
69. Pulo de 68% como linha de parar e 60% como linha de dobrar. Média. C1.
70. Leitura em 31/10 (48 h) e 05/11 (7 dias). Alta. 06-plano-final.md.
71. Contar comentário de dentista separado de comentário genérico. Alta. 06-plano-final.md 8.5.
72. Anotar na planilha a origem de cada lead à mão até o `o` funcionar. Alta. M5.
73. Comparar o reel do dentista com a mediana de reels com o Bruno, não com a mediana geral, quando houver a lista. Média. F12 mistura animação e Bruno.
74. Rodar ig_post_stats do Tzur v2 se foi publicado, antes de 29/10. Média. B06.
75. Nenhuma decisão de formato com N = 1; formato só muda com 3 peças ou mais. Alta. 00-enquadramento D4.
76. Registrar tempo real de render de cada modelo no arquivo da semana. Média. B13.

**Conformidade e texto**
77. Relógio e lousa no lugar de cadeira odontológica. Média. P11, F72.
78. Nenhum dente estilizado na tela. Média. P11 sem consulta ao CRO (B21).
79. "no Brasil" e "formar quem disputa" na legenda. Média. F08, F09.
80. "Por que" separado na legenda (pergunta). Alta. Norma da língua.
81. Rodar busca por travessão e emoji em todos os textos de tela antes do render. Alta. CLAUDE.md.
82. Uma só construção de contraste, a falada. Alta. CLAUDE.md.

---

## 5. Pre-mortem da cadeira: como este plano fracassa

1. A peça sai bonita e chega a 50 de alcance. A camada de conversão converte bem uma audiência que não existe. É o ponto cego, e é o fracasso mais provável [ESTIMATIVA, seção 2.15].
2. O título com a resposta mata a curiosidade: o pulo sobe acima de 68% porque a pessoa já leu a tese. Sinal: tempo médio assistido abaixo de 6,2 s.
3. Tela carregada: título, letreiro, legenda, react e nota juntos de 2 a 5 s ficam ilegíveis no celular. Sinal: o Bruno ou o júri não conseguem ler o "474 MIL" na primeira passada.
4. O letreiro atrás fica ilegível porque a cabeça cobre o centro em 71,6% dos quadros (F29).
5. A legenda corrigida não bate com o áudio, alguém comenta o erro e a credibilidade cai.
6. Os comentários vêm de quem não é dentista ou de robôs; a planilha conta errado.
7. O lead chega no WhatsApp sem origem (M5) e a rodada conclui que o reel não gerou nada quando gerou.
8. A bio antiga recebe a visita e não converte.
9. O render de 3 modelos atrasa e o reel sai depois de 29/10, empurrando o calendário dos 5 nichos.
10. A atenuação de respiração soa cortada e o Bruno pede para refazer o áudio.
11. O Bruno não gosta de ver a oferta escrita no começo ("parece anúncio") e veta a camada nos 3.
12. A comparação A, B e C vira debate de gosto, porque o júri mede acabamento e não conversão (P17).

---

## 6. Previsões numéricas com data de conferência

Todas [PRIOR] com a conta indicada; nenhuma fecha objeção sozinha.

| Métrica | Valor previsto (faixa) | Conferência | Base |
|---|---|---|---|
| Loudness e true peak dos 3 MP4 finais | -14,0 a -14,5 LUFS e -1,1 a -1,5 dBTP | 23/10/2026 | M2 |
| Alcance do reel do dentista em 7 dias (se publicado em 29/10) | 105 (45 a 260) | 05/11/2026 | F12, F13, F58 |
| Pulo em 7 dias | 60% (50% a 72%) | 05/11/2026 | 3 melhores com o Bruno: 46% a 53%; mediana 68% |
| Comentários com "dentista" em 7 dias | 2 (0 a 8) | 05/11/2026 | seção 2.15 |
| Conversas qualificadas de dentista (D+30) | 1 (0 a 3) | 20/11/2026 | seção 2.15 |
| Leads com origem "ig-dentista" registrada automaticamente (D+30) | 0, se o `o` não for levado ao WhatsApp | 20/11/2026 | M5 |
| Diagnósticos agendados vindos do nicho dentista (D+60) | 0 (0 a 2) | 20/12/2026 | conversa de 1 e conversão desconhecida |
| Venda vinda do nicho dentista (D+90) | 0 (0 a 1) | 19/01/2027 | 0 venda em 30 dias (00-SISTEMA.md) |
| Reels do nicho dentista acima de 150 em 48 h até D+90 | 1 (0 a 2) | 19/01/2027 | 3 de 17 reels passaram de 126 (00-SISTEMA.md) |

---

## 7. O que mudaria minha opinião

- Métricas do Tzur v2 publicadas (B06) com pulo acima de 75%: tiro o letreiro 3D do modelo publicado e passo C a principal.
- B02 mostrando que a frase falada perdeu o sentido: regravação com insert vira obrigatória.
- Trial reels disponíveis (B23): publico B como trial no mesmo dia, e a decisão de formato ganha um segundo ponto.
- Um teste de 1 quadro mostrando "474 MIL" ilegível atrás da cabeça: o letreiro desce para a frente da parede, ao lado da cabeça.
- A bio já trocada: a seção 2.15 perde um vazamento e a previsão de conversa sobe.
- O Bruno vetando texto de oferta no começo: troco o título por identificação ("Dentista, você só vende hora de cadeira?").
- Dados de edição dos 10 reels de referência (B08) mostrando que os de negócio não usam título fixo: rebaixo a ideia 1 para baixa.

## 8. Lacunas

- Não ouvi o áudio. M3 e M4 são medições de energia, não de conteúdo.
- Não renderizei nenhum quadro. Legibilidade do letreiro atrás e carga visual são hipóteses.
- Protocolo do júri cego: não existe (B25).
- Trial reels na conta: sem dado (B23).
- Bio atual da conta em 21/10: o 00-SISTEMA.md diz que é a antiga; se foi trocada depois, sem dado.
- Logs de acesso da página do Tabuleiro e qualquer analítica do lado do servidor: sem dado.
- Tempo real de render: sem dado (só estimativas de F4).
- Quantos reels com o Bruno ficaram abaixo de 106: sem dado.
- Especificação de áudio do Instagram e o que o reencode dele faz com o pico: sem dado (B05).

## 9. Fontes

- /home/user/Disparo-/videos/nichos/dentista/god/contexto.md
- /home/user/Disparo-/videos/nichos/dentista/god/run/00-enquadramento.md
- /home/user/Disparo-/videos/nichos/dentista/god/run/01-fatos.md (F01 a F76, C1 a C10, B01 a B25, DR01 a DR20, P01 a P22)
- /home/user/Disparo-/videos/nichos/dentista/god/run/01-pesquisa/F4-viabilidade-pipeline.md (seções 2.1, 3, 4, 5)
- /home/user/Disparo-/videos/nichos/dentista/god/words-raw.json e transcricao-tempos.txt
- /home/user/Disparo-/videos/nichos/dentista/god/frames-amostra.jpg
- /home/user/Disparo-/conteudo/sistema-instagram/00-SISTEMA.md (ficha de entrada, 3 melhores, Módulo 1)
- /home/user/Disparo-/conteudo/modo-god-nichos/run/06-plano-final.md (seções 2.2, 4, 8.4, 8.5, 9.1, 9.2, 9.5, linhas 179 a 186 e 586)
- /home/user/Disparo-/CLAUDE.md
- M1 a M4: ffmpeg ebur128 e numpy sobre scratchpad/dent/voz_master.wav, 21/10/2026, por pipe, sem arquivo gerado
- M5: GET em https://estrategistadelancamento.com.br/tabuleiro/?o=ig-dentista, /js/main.js e /js/tabuleiro.js, 21/10/2026, só leitura
- Lista de filtros: ffmpeg -filters, 21/10/2026
