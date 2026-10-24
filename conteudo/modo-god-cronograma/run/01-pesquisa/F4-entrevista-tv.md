# F4 · Entrevista à TV Câmara · ordem da série, tl02 a tl05, mc02 a mc04 e data de exibição

Frente F4 da pesquisa do conselho Agência Reunida para @o_estrategista.com.br. Rodada de sábado, 24/10/2026, escrita às 14h (São Paulo). Somente leitura: nada foi publicado, agendado ou alterado no Instagram, no Buzzfy ou no PostZen. Toda mudança abaixo é uma ação para o Bruno executar.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha objeção sozinho. Métrica que falta: "sem dado".

**Base declarada (a mesma no arquivo inteiro):** alcance, mediana de 53 (escolha do 00-enquadramento até o Módulo 7 de 26/10). Limites: 0,5x = 27; 0,8x = 42; 1x = 53; 2x = 106; 3x = 159; TABULEIRO = 150. Pulo: corte em 75% (catálogo, seção 8). O Buzzfy calcula o próprio múltiplo sobre outra base (alcance 37,5 e views 57, 20 reels) [FATO, `ig_post_stats` baseline e `ig_reel_checkup`, 13h50]: o vs_median_x da ferramenta não é o múltiplo deste arquivo. O único critério que uso direto da ferramenta é a marca de hot streak do `ig_reel_checkup` (3x o normal dela).

---

## 0. Resposta curta

1. **Manter as 16 publicações de 24/10 a 30/10.** Não há métrica medida que mande trocar. Uma correção tem prazo: a legenda do tl01 promete "O mais votado sai no próximo sábado", e 5 dos 7 assuntos do índice saem antes de sábado (4 em reel, 1 em story). Trocar a frase no PostZen antes de dom 25/10, 18h30 (seção 5).
2. **tl02 a tl05 não são o mesmo formato.** tl01 e tl02 têm de 39% a 49% do tempo em plano aberto acelerado, com as cabeças pequenas, e só 34% a 41% de voz real. tl03, tl04 e tl05 têm de 61% a 68% de voz real e de 18% a 24% de acelerado [FATO, conta sobre as fichas `cortes/tl0X.spec.json`]. O risco medido da conta (animação sem rosto de 0,15x a 0,8x) pesa no tl01 e no tl02, bem menos nos outros três.
3. **Ordem proposta:** tl02 só se o tl01 passar no portão de ter 27/10, 18h30; depois, um por sábado, escolhido pelo desempenho da peça já publicada que trata do mesmo assunto ("peça-mãe"): tl04 depende do pb01, tl03 do car01, tl05 do ci01. Ordem padrão com tudo verde: tl02 (31/10), tl04 (07/11), tl03 (14/11), tl05 (21/11). A ordem do pecas-e-calendario (tl03 antes do tl04) troca de lugar porque o tl04 é o único com assunto que nenhuma peça da semana cobre (a origem e o pai) e o tl03 repete o assunto do mc01 de hoje e da capa do car01.
4. **tl02 tem um defeito de ficha:** 10,4 s seguidos sem voz real (de 16,55 s a 26,95 s), acima do teto de 8 s do catálogo (F5). Corrigir antes de agendar.
5. **mc04 está diferente do que o plano de stories diz:** o render termina em "como estrategista digital" (1709,18 a 1710,18 s), e o 03-plano-7-dias afirma que foi cortado antes [FATO, `mc04.spec.json` seg 1700,6 a 1710,15; transcrição; folha `mc04-folha.jpg`]. Recortar em 1707,82 s. E o mc04 não pode sair antes do tl02 no mesmo dia: a frase dele é o laço que o tl02 só paga aos 27 s.
6. **Data de exibição: sem dado.** O programa existe (Ser Empreendedor, TV Câmara Campinas) e a grade de 19/10 a 25/10 só traz outra edição; os vídeos das edições recentes no site têm de 27 a 124 views [FATO, tvcamaracampinas.com.br, 13h55]. Quando a data chegar, mudam a legenda ("foi ao ar" só depois de ir ao ar), o link nos stories, a conferência dos minutos e a trava de Mirna e produção (seção 8).

---

## 1. Fontes conferidas nesta rodada

| # | Fonte | Consulta (somente leitura) | Hora (SP) | Resultado |
|---|---|---|---|---|
| 1 | `contexto.md`, `00-enquadramento.md` | leitura | 13h40 | lidos |
| 2 | `entrevista-tv-camara/pecas-e-calendario.md` e `catalogo-formatos.md` (seções 1 a 8) | leitura | 13h40 | lidos |
| 3 | `stories-objecoes/03-plano-7-dias.md`, `01-objecoes.md`, `02-provas.md` (trechos) | leitura e busca | 13h45 | lidos |
| 4 | `videos/tv-camara/cortes/*.spec.json` (tl01 a tl05, mc01 a mc04, st01, pb01, pb02, ci01, po01, pf01), `engine/ENGINE.md`, `dados/transcricao.json`, `dados/correcoes.json` | leitura e conta em Python | 13h45 a 13h55 | ok |
| 5 | Renders no scratchpad desta sessão (`scratchpad/tv/render/`): folhas de tl02, tl03, tl04 e mc04; `ffprobe` de duração; 2 recortes de quadro dos mc (apagados logo depois) | leitura | 13h45 | ok |
| 6 | Processos em execução (`ps`) | leitura | 13h47 | `render.sh cortes/tl05.spec.json` rodando desde 13h41 |
| 7 | PostZen `listPosts`, conta j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 a 30/11 | leitura | 13h50 | 16 publicações, todas "scheduled"; nada depois de sex 30/10 |
| 8 | PostZen `listCommentAutomations`, mesma conta | leitura | 13h50 | 17 automações ativas; só CHECKLIST com disparo (1 enviado) |
| 9 | Cabeçalho HTTP das mídias do PostZen (tl01, st01, mc01) | `curl -I` | 13h52 | tamanhos iguais aos renders locais (seção 3) |
| 10 | Buzzfy `ig_posts` (reels e posts desde 12/10; stories ativos) | leitura | 13h50 | último reel: Dentista A (21/10, 21h); 1 story ativo (09h33) |
| 11 | Buzzfy `ig_reel_checkup` (12 últimos) | leitura | 13h50 | normal 57 views, pulo 70,9% (20 reels); janela de hot streak fechada |
| 12 | Buzzfy `ig_post_stats` (story de 09h33 e Dentista A) | leitura | 13h51 | ok; story traz alcance, respostas e toques |
| 13 | Buzzfy `buzzfy_playbook` (formats, hot_streaks) | leitura | 13h56 | ok |
| 14 | tvcamaracampinas.com.br: grade de 19/10 a 25/10 e página do programa Ser Empreendedor | `curl` de leitura | 13h53 a 13h57 | ok |
| 15 | campinas.sp.leg.br (portal da Câmara) | `WebFetch` e `curl` | 13h50 | **erro**: WebFetch estourou 60 s; 1ª tentativa de curl "Connection reset by peer"; 2ª tentativa ok (links da TV Câmara) |
| 16 | Busca na web "Ser Empreendedor TV Câmara Campinas" (2 consultas) | WebSearch | 13h49 | **sem resultado útil** (registrado como erro de busca, não como "programa não existe") |
| 17 | PostZen `listCommentAutomationLogs` | não rodado | | a frente não depende de log; os totais das 17 automações vieram do item 8 |

---

## 2. O que está agendado e o que falta agendar

[FATO, PostZen `listPosts`, 13h50] 16 publicações de sáb 24/10 a sex 30/10. Da série da TV: 4 stories hoje (14h00 st01, 14h03 estático, 15h00 "A pergunta da TV", 15h01 mc01), tl01 dom 25/10 18h30, pb01 seg 26/10 21h, car01 ter 27/10 12h, pf01 (story) ter 27/10 16h, ci01 qua 28/10 21h, po01 qui 29/10 21h, pb02 sex 30/10 21h. Mais o reel Dentista B hoje às 21h com TABULEIRO.

Não agendado: tl02 a tl05 e mc02 a mc04 [FATO, mesma consulta]. O 03-plano-7-dias já encaixa mc02 em dom 25/10 09h01, mc03 em seg 26/10 17h30 e mc04 em sáb 31/10 11h00, com o tl02 no sáb 31/10 18h30 [FATO, `03-plano-7-dias.md`]. O pecas-e-calendario propõe tl02 31/10, tl03 07/11, tl04 14/11 e tl05 21/11, sempre 18h30, cada um com portão [FATO].

Às 13h58 nada da série tinha saído: o único story ativo é de 09h33, fora do PostZen [FATO, `ig_posts` stories].

---

## 3. O que cada peça é de fato

### 3.1 Timelapses (contas sobre as fichas e as folhas de render)

| | tl01 | tl02 | tl03 | tl04 | tl05 |
|---|---|---|---|---|---|
| Formato | timelapse | timelapse (igual ao tl01) | cronômetro e pergunta | fita de trás pra frente | régua do tempo |
| Duração | 36,5 s | 35,3 s | 36,0 s | 34,4 s | 35,3 s |
| Quadro 0 | Bruno de frente no computador (fonte 1965 s), 1,8 s | idem (1875 s), 1,6 s | idem (2032,5 s), 2,6 s, com a pergunta no topo | idem (2044 s), 1,7 s | idem (2066 s), 1,9 s |
| Voz real | 12,5 s (34%) | 14,6 s (41%) | 24,3 s (68%) | 21,1 s (61%) | 23,2 s (66%) |
| Plano aberto acelerado | 18,1 s (49%) | 13,8 s (39%) | 6,4 s (18%) | 8,3 s (24%) | 7,2 s (20%) |
| Maior trecho sem voz real | 7,1 s | **10,4 s** (16,55 a 26,95 s) | 4,4 s (no fim) | 7,0 s (no fim) | 3,4 s (no fim) |
| Mirna | nenhuma fala marcada | 1,1 s de voz ("O que?") | cerca de 4,7 s de voz [ESTIMATIVA pelos tempos da transcrição: 1518,64 a 1521,0 s duas vezes] e 2,2 s do rosto dela na tela dividida | 4,05 s de voz e o "Uau!" com recorte de 2,5x no rosto dela (432x768 do Z2) | 3,6 s de voz e 0,7 s de rosto congelado com o carimbo "AINDA?" |
| Assunto | índice dos 7 assuntos | empreender, cases, família (laço "eu construí patrimônio, eu construí..." pago aos 27 s) | "Você foi investir em equipamento?" e a resposta (min 10:01 a 11:00) | origem: pai pioneiro, pai que estimulava, quebrar objeção, realidade de hoje, ensinar empresários | marketing de antes e de hoje; fecha em "tête-à-tête" |
| Já sai na semana | | restaurante (pb02, sex), odontologia (pf01, ter), zero reais (mc01 hoje, capa do car01 ter) | o assunto do investimento (mc01 hoje, capa do car01) | nada (o assunto 1 do índice não tem peça) | "até hoje é o melhor marketing" (ci01 qua; enquete de story ter 14h32; cartão do ob03) |
| CTA | número | número | "Comenta o seu primeiro investimento." | número da parada | SIM ou NÃO |
| Render | 13h16, com desfoque; é o arquivo do PostZen | 13h24 | 13h34 | 13h41 | refazendo agora (o render de 11h42 é anterior à ficha com desfoque de 13h04) |

Fontes: fichas `videos/tv-camara/cortes/tl0X.spec.json` (segmentos, voz_trechos, falantes, vf), conta em Python nesta rodada; quadro 0 conferido nas folhas de tl02, tl03 e tl04 e, para tl01 e tl05, pela ficha e pela nota do `ENGINE.md` ("de 31:00 a TV grava o Bruno de frente no computador: ótimo para abrir reel"); horários dos arquivos convertidos de UTC para São Paulo; tl01 do PostZen com 19.980.328 bytes e última modificação às 13h19, igual ao render com desfoque [FATO, `curl -I` e `ls`].

O que isso diz:
- **Os timelapses são as únicas peças da série que abrem com o Bruno de frente.** pb01, pb02, po01 e pf01 abrem no Z2 (os dois na mesa, Bruno em 3/4 atrás do monitor) e ci01 abre no CB [FATO, `planos` das fichas]. A regra do CLAUDE.md (Bruno em cena nos 3 primeiros segundos) é cumprida pelas 5 fichas de timelapse.
- **tl01 e tl02 ficam na régua de montagem; tl03 a tl05 ficam mais perto de história com voz real.** O playbook do Buzzfy mede montagem a 0,69x o normal em contas de 1 a 5 mil seguidores e história a 1,28x [FATO, `buzzfy_playbook` formats]. Encaixar cada timelapse numa dessas classes é [HIPÓTESE]; o catálogo já diz que o miolo acelerado é "o mais parecido com a animação sem rosto" [FATO, catálogo F5].
- **O recorte de 2,5x no rosto da Mirna (tl04) passa do teto de 1,5x sobre o 4K** que o catálogo fixa para CB e CM (seção 3). Conferir nitidez na folha de 4 quadros por segundo e, mais importante, depende da autorização por escrito.

### 3.2 Manchetes (stories)

| | mc02 | mc03 | mc04 |
|---|---|---|---|
| Duração | 4,5 s | 11,0 s | 9,5 s |
| Frase (literal, transcrição) | "Até que hoje eu sou estrategista de marketing digital e lançamento de produto." (1199,50 a 1204,04 s; "produto" com probabilidade 0,11, conferido em 2 passes segundo o 02-provas) | "...tudo um fruto do nosso entendimento do produto de cada pessoa, de cada cliente. Cada cliente tem um produto específico e a gente vive esse produto." (1573,30 a 1583,98 s) | "Eu construí patrimônio, eu construí família, eu construí tudo através da profissão que hoje eu executo como estrategista digital" (1700,66 a 1710,18 s) |
| Palavra em ouro | lançamento | específico | família |
| Sticker (03-plano) | enquete "Você sabia?" | enquete "Concorda?" | caixa "Qual foi a sua virada?" |
| Problema | abaixo da faixa de 7 a 10 s do catálogo (F4) | nenhum | **termina em "como estrategista digital"**, termo que o 01-objecoes marca como contaminado; o 03-plano diz que foi cortado antes, e não foi |

Fontes: `mcXX.spec.json` (seg, chave), `transcricao.json` (tempos de palavra), `ffprobe` (duração), folha `mc04-folha.jpg` (últimos quadros mostram "executo como ESTRATEGISTA" e "DIGITAL").

Mais dois achados:
- **Ticker:** os 4 mc trazem "Uma profissão por 20 anos" no letreiro corrido, isolado, embaixo de "Bruno · Estrategista de Lançamento" [FATO, campo `ticker` das fichas]. O 01-objecoes manda usar essa frase "só como carreira na noite (DJ e casas noturnas). Nunca como 20 anos de marketing" [FATO, linha 301]. Ler como 20 anos de marketing é [HIPÓTESE], mas a regra escrita é clara. O mc01 de hoje às 15h01 já sai assim.
- **Gravador nos mc:** os mc usam o plano CB, que corta acima do gravador. Num quadro de cada mc não apareceu marca legível; a etiqueta do monitor fica atrás da faixa "NA TV" [FATO, recorte de 1 quadro por peça, apagado em seguida]. O catálogo pede conferir 20 quadros espalhados: só 1 foi conferido.

---

## 4. Julgamento da ordem agendada (24/10 a 30/10)

| Ponto | Fato | Veredito |
|---|---|---|
| tl01 abre a série no domingo | É o formato de maior risco (49% acelerado, 34% de voz real) e o catálogo o punha depois do REACT, "uma vez só" [FATO, catálogo F5 e seção 8]. Mas é o índice da série, foi pedido do Bruno e abre com ele de frente. Fim de semana: 1,10x o normal no playbook [FATO, `buzzfy_playbook` hot_streaks] | **Manter.** Não há métrica que mande trocar. Corrigir a legenda (seção 5) |
| pb01 (seg) e pb02 (sex) | Mesmo formato, assunto diferente | **Manter.** É o único par limpo da semana (muda uma coisa só) e dá n de 2 para o PB |
| ci01 (qua) e po01 (qui) | Cada um muda formato e assunto em relação ao anterior | **Manter**, sabendo que o Módulo 7 de 02/11 não separa efeito de formato e de assunto nessas duas |
| 5 reels da TV em 6 dias | O playbook pede 3 a 5 na mesma linha mudando uma coisa por vez [FATO, hot_streaks]. A TV é linha nova em relação ao Dentista A (F2 desta rodada) | **Manter.** Dá n de 5 para a linha. Risco: se a linha falhar, a semana inteira falha junto [HIPÓTESE] |
| Ordem dos assuntos | Seg assunto 2, ter 4 (story), qua 5, qui 7, sex 3 | Fora da ordem do índice. Efeito: sem dado; não justifica mexer [PRIOR] |
| Dentista B hoje 21h | Se o `ig_reel_checkup` marcar hot streak até dom 21h, o protocolo pede a sequência em 24 a 48 h [FATO, playbook] e a semana já está cheia de TV | Decisão da grade (outra cadeira). Registro aqui porque disputaria a vaga do pb01 de seg 21h |
| mc01 hoje 15h01 | Ticker com "Uma profissão por 20 anos" | Trocar a mídia não cabe no prazo sem novo render; aceitar hoje e corrigir nos próximos mc |
| tl02 no sáb 31/10 (pecas e 03-plano) | A S1 (25 a 31/10) já tem 5 reels e 1 carrossel [FATO, `listPosts`]. Com o tl02 seriam 6 reels e 1 carrossel: o mesmo volume de 7 posts de feed do ritmo 5 + 2, com a mistura trocada | **Condicional** ao portão do tl01 (seção 6), registrado como TESTAR com esse motivo escrito |

---

## 5. A promessa do tl01

**Problema** [FATO, legenda no PostZen]: "Comenta o número do assunto que você quer ver inteiro. O mais votado sai no próximo sábado." Até sábado já terão saído os assuntos 2 (pb01), 4 (pf01, story), 5 (ci01), 7 (po01) e 3 (pb02). Os assuntos 1 e 6 não têm corte próprio.

**Recomendação (ação do Bruno no PostZen, até dom 25/10, 18h30):** trocar a última frase por "Os cortes saem a partir de amanhã, um por dia." A frase é verdadeira (seg pb01, ter car01 e pf01, qua ci01, qui po01, sex pb02), mantém o pedido de número (que vira dado para ordenar tl03 e tl04) e solta o sábado da promessa.

**Se a legenda ficar como está**, o sábado cumpre assim:

| Voto | Assunto | O que sai no sábado 31/10 |
|---|---|---|
| 1 | Desde criancinha (min 00:47) | tl04 (paradas 1 e 2: "meu pai foi um dos pioneiros", min 01:16; "meu pai me estimulava a trabalhar", min 01:33), só com o print da Mirna. Alternativa: corte novo em PB de 923,7 a 958,0 s (cerca de 34 s), que não existe e pede render; antes, ouvir quem diz "Bruno, empreendedor nato" (922,1 a 924,2 s), pendência do enquadramento |
| 6 | Zero reais (min 10:30) | tl03 (a pergunta do investimento e a resposta, min 10:01 a 11:00); o "zero reais" em si passa acelerado em 0,8 s dentro do tl03 [FATO, ficha] |
| 2, 3, 4, 5 ou 7 | já saíram na semana | Story no sábado: repost do corte com "O mais pedido saiu [dia]. Está no perfil." O reel do sábado segue o portão da seção 6 |

**Contagem dos votos:** nenhuma ferramenta permitida nesta rodada lê o texto dos comentários (o `ig_post_stats` só traz o total). O Bruno conta à mão no app, até sex 30/10. Regra do catálogo: com menos de 5 votos somados (comentários e enquete), seguir a ordem da seção 6 e dizer isso nos stories, sem fingir votação [FATO, catálogo F5]. Menos de 5 votos é o caso provável: os 12 últimos reels tiveram 0 comentário cada e a conta teve 14 comentários em 30 dias [FATO, `ig_reel_checkup` e contexto.md] [HIPÓTESE sobre o tl01].

---

## 6. Ordem proposta de tl02 a tl05

### 6.1 Portão do tl01 (leitura com 48 h reais)

tl01 sai dom 25/10 18h30. Leitura parcial seg 26/10 18h30 (24 h, só para hot streak); leitura que decide: **ter 27/10, 18h30**, com `ig_post_stats` (alcance, pulo, tempo assistido, comentários) e `ig_reel_checkup` (marca de hot streak).

| Estado | Condição (base 53, pulo 75%) | O que acontece |
|---|---|---|
| QUENTE | `ig_reel_checkup` marca o tl01 em hot streak com 24 h | Protocolo do playbook: sequência em 24 a 48 h [FATO]. tl02 (já corrigido) na **ter 27/10, 18h30** (dia com car01 às 12h: 2 posts de feed, dentro da regra; nenhum reel no dia). Sábado 31/10 fica para o próximo pela regra 6.2 |
| VERDE | alcance de 42 ou mais e pulo abaixo de 75% | tl02 no **sáb 31/10, 18h30**, como TESTAR (motivo escrito: o timelapse precisa de n de 2 antes de PARAR ou MANTER, regra D6 do enquadramento; volume da S1 fica em 7 posts de feed) |
| AMARELO | alcance de 27 a 41, ou pulo de 75% ou mais | O acelerado não segura: tl02 fora do feed. Opção do F2 desta rodada: tl02 como trial reel no sábado, sem ocupar o feed [HIPÓTESE; se o PostZen sobe trial reel: sem dado; no app, a opção existe para conta profissional: PRIOR, conferir]. Próximo timelapse no feed só a partir de 07/11, pela regra 6.2, e só se a média de alcance de pb01 e pb02 for de 42 ou mais (o material em tempo real da TV funciona) |
| VERMELHO | alcance abaixo de 27 | A família inteira sai do feed (regra 2 e 5 do portão do catálogo). tl02 a tl05 viram trechos de 15 s nos stories e banco. Os sábados ficam com formato com rosto (PB, ob01 a ob03 ou REACT se houver selfie) |

Por que o tl02 vem logo depois do tl01 no VERDE: é o único próximo passo que muda uma coisa só (o assunto) [FATO, regra do playbook]. Por que sai no AMARELO: tem 39% de acelerado e o trecho de 10,4 s sem voz, justamente o que teria falhado.

### 6.2 Regra para os sábados de 07/11, 14/11 e 21/11

Cada candidato tem uma peça-mãe já publicada com o mesmo assunto. O sábado seguinte vai para o candidato cuja peça-mãe teve o maior alcance em 48 h, desde que: (a) o último timelapse publicado tenha ficado com 42 ou mais e pulo abaixo de 75%; (b) a peça-mãe tenha ficado com 42 ou mais; (c) exista o print da Mirna (obrigatório para tl03 e tl04, que têm mais voz e rosto dela). Empate: o de menor repetição de assunto primeiro (tl04, depois tl03, depois tl05).

| Candidato | Peça-mãe e sinal extra | Leitura de 48 h da mãe | Se a mãe for fraca (abaixo de 42 com pulo de 75% ou mais) |
|---|---|---|---|
| tl04 | pb01 (trajetória e origem); votos no 1 | qua 28/10, 21h | stories de 15 s (paradas 1 e 2) e banco |
| tl03 | car01 (capa "computador e sonho": alcance contra a mediana de feed do Buzzfy, salvamentos e comentários); mc01 (respostas na caixa); votos no 6 | qui 29/10, 12h | stories de 15 s (pergunta e resposta) e banco |
| tl05 | ci01 (mesmo assunto); enquete de story de ter 27/10 14h32 ("O tête-à-tête ainda é o melhor marketing?") | sex 30/10, 21h | fica só nos stories |
| DOBRAR | ci01 com 106 ou mais: tl05 sobe para o primeiro sábado livre (mesmo assunto, formato novo: uma mudança só) | | |

**Ordem padrão, com tudo verde e o print guardado:** tl02 sáb 31/10 · tl04 sáb 07/11 · tl03 sáb 14/11 · tl05 sáb 21/11, todos às 18h30.

**Leituras de 48 h de cada timelapse** (decidem o sábado seguinte; agendar no PostZen até a quarta):

| Peça | Sai | 48 h | Decide |
|---|---|---|---|
| tl02 | sáb 31/10, 18h30 | seg 02/11 (Finados), 18h30 | sáb 07/11 |
| 2º sábado | sáb 07/11, 18h30 | seg 09/11, 18h30 | sáb 14/11 |
| 3º sábado | sáb 14/11, 18h30 | seg 16/11, 18h30 | sáb 21/11 |
| 4º sábado | sáb 21/11, 18h30 | seg 23/11, 18h30 | semana 5 |

O Módulo 7 de segunda lido de manhã pega o timelapse de sábado com cerca de 40 h: ou se lê depois das 18h30, ou a decisão do sábado fica para terça.

**PARAR, MANTER, DOBRAR para a família:**
- PARAR: 2 timelapses abaixo de 42 com pulo de 75% ou mais (n de 2, regra D6). Exceção: o tl01 sozinho já para o tl02 (mesmo mecanismo da animação sem rosto, que já tem n de 12 abaixo da mediana: 12 reels sintéticos com mediana de 32,5 de alcance e 83,8% de pulo [FATO, F1-auditoria-conta.md desta rodada, `ig_post_stats`]); não para tl03 a tl05, que são outro mecanismo [HIPÓTESE].
- MANTER: 42 a 105 com pulo abaixo de 75%: segue um por sábado.
- DOBRAR: 106 ou mais: o próximo timelapse fica garantido no sábado seguinte, sem vaga extra (ritmo de 5 + 2 por semana).
- TABULEIRO: só no timelapse seguinte a um que passou de 150 em 48 h e dentro da palavra do mês. Nos 4 timelapses o CTA é número ou SIM/NÃO, que não dispara nenhuma das 6 automações de conta toda (case, caso, estrategista, etapa, etapas, funil, caixa) [FATO, `listCommentAutomations`].

### 6.3 Correções antes de agendar (produção; nenhuma pede gravação)

1. **tl02:** quebrar o trecho de 16,55 a 26,95 s com um respiro de voz real de 2 a 2,5 s (regra F5: nunca mais de 8 s sem voz real). Render: cerca de 5 min de captura pela tabela de custo do catálogo [ESTIMATIVA do catálogo].
2. **tl05:** o render novo com desfoque estava rodando às 13h47; conferir a folha nova (gravador desfocado, quadro 0 com o Bruno) antes de subir.
3. **tl03:** a ficha troca "investindo" por "investir" na pergunta da Mirna (`correcoes` da ficha); a transcrição base lê "você foi investindo em equipamento?" (1516,6 a 1521,0 s). Ouvir e manter o que estiver no áudio (regra de texto fiel do catálogo).
4. **tl04:** conferir a nitidez do "Uau!" a 2,5x e manter só com o print da Mirna.
5. **Todos:** subir para o PostZen só a versão com desfoque, conferindo tamanho e hora do arquivo como foi feito com o tl01.

### 6.4 O que acontece com cada timelapse que não vai ao feed

- Vai para os stories em trechos de até 15 s, sem motor (corte direto do render), com o rótulo "NA TV" e a enquete ligada ao assunto, como o catálogo prevê no F2.
- Fica no banco para a semana 5 em diante, com a mesma regra da peça-mãe.
- Nunca vira reel sem passar pelo portão, e nunca com voz sintética.

---

## 7. Manchetes mc02 a mc04 nos stories

| Peça | Quando | Por quê | Correção antes |
|---|---|---|---|
| mc02 | dom 25/10, 09h01 (como no 03-plano) | Autoridade antes do tl01; não toca no laço de nenhum timelapse | Trocar o item "Uma profissão por 20 anos" do ticker por outra frase literal que não seja a da própria manchete (ex.: "Cada cliente tem um produto específico"); cerca de 1,2 min de captura por peça [ESTIMATIVA do catálogo] |
| mc03 | seg 26/10, 17h30 (como no 03-plano) | Quebra "meu nicho é diferente" no dia do pb01 | mesma troca do ticker, com outra frase (ex.: "Eu só tinha um computador e um sonho") |
| mc04 | **depois do tl02**: dom 01/11, 09h, se o tl02 sair no sáb 31/10; sáb 31/10, 11h (como no 03-plano) só se o tl02 não for ao feed | A frase do mc04 é o laço do tl02 ("eu construí patrimônio, eu construí...", pago em "família" aos 27 s). Mostrar a frase inteira 7 h antes entrega o fim do reel para quem segue o perfil [HIPÓTESE] | Recortar em 1707,82 s ("...eu construí tudo através da profissão", 7,2 s, dentro da faixa de 7 a 10 s). Corrigir também a nota do 03-plano, que diz que o corte já existe |

**Medição de cada mc** (o 00-enquadramento dava a leitura por story como sem dado; agora existe):
- [FATO, `ig_post_stats` do story de 09h33, 13h51] O Buzzfy lê story ativo com alcance, views, respostas, toques para avançar, deslizes e saídas, só enquanto o story está no ar (24 h) e com 5 viewers ou mais. Exemplo de hoje, com 4,3 h: alcance 21, views 26, 14 toques para avançar, 6 deslizes, 3 saídas, 0 resposta. É n de 1 e, segundo o F1 desta rodada, uma cena sem o Bruno na capa: serve de régua grosseira, não de mediana.
- Votos de enquete e respostas de caixa não aparecem no `ig_post_stats`: o Bruno anota à mão no app antes de expirar.
- Ler cada mc entre 20 h e 23 h depois de publicado.

**O que fazer com cada mc conforme o resultado** (entre mc01 a mc04):
- A frase com mais respostas somadas (enquete, caixa e direct) vira a capa ou a lâmina 2 do próximo carrossel (CARROSSEL 02, F3), que é peça sem gravação.
- Reel de manchete só se: a peça tiver o maior número de respostas entre as 4, o Módulo 7 abrir vaga de DOBRAR, e a manchete virar a abertura de um REACT gravado. Sozinha, a manchete no CB mostra o Bruno de lado e de costas para a câmera (folha do mc04) e o catálogo dá nota 6 como reel [FATO, catálogo F4].
- Zero resposta nas 4: as manchetes saem do rodízio de stories da manhã depois do mc04 e a vaga vai para os estáticos de objeção do plano de 7 dias.

---

## 8. Quando a data de exibição chegar

### 8.1 O que se sabe hoje

- [FATO, tvcamaracampinas.com.br/programas/ser-empreendedor, 13h57] O programa existe, com 374 edições no acervo. Edições recentes: "Negócios para o público Infantil" (há 2 e 5 dias, 27 e 47 views), "Confeitaria" (semana passada, 124), "Empreendedorismo de Impacto Social" (há 2 semanas, 49), "Campinas Innovation 2026" (há 3 semanas, 65; 20/09, 109). Duração de 30 a 47 min.
- [FATO, grade em tvcamaracampinas.com.br/programacao/2026-10-19 a 2026-10-25, 13h55] A grade da semana traz a mesma edição de Ser Empreendedor todos os dias; no sábado 24/10 ela passa à 01h, 06h, 13h e 18h. A edição do Bruno não está na grade até dom 25/10.
- [FATO, 02-provas.md, linha 138] A Mirna fecha a entrevista com "mais uma história de sucesso no próximo bloco": a entrevista do Bruno é um bloco de um programa mais longo [HIPÓTESE sobre a montagem final].
- Data de exibição: **sem dado**. Liberação da Mirna: verbal ("pode seguir"), print por escrito pendente. Se ela cobre publicar antes de ir ao ar: sem dado [FATO, contexto.md e 02-provas.md].
- [HIPÓTESE] Pelo padrão da grade, quando a edição do Bruno entrar, deve reprisar várias vezes por dia durante cerca de uma semana. Audiência na TV: sem dado. No site, as edições recentes ficam entre 27 e 124 views [FATO]: a exibição sozinha não deve trazer tráfego grande [HIPÓTESE].

### 8.2 O que muda

| Momento | O que muda | Por quê |
|---|---|---|
| Até a data | Nenhuma peça diz "foi ao ar", "assista na TV" ou cita data. Peças com mais voz e rosto da Mirna (tl03, tl04) só com o print. Se o print não cobrir publicar antes da exibição, segurar tl03 e tl04 até a data e seguir com tl02 e tl05 | Regra do pecas-e-calendario: antes da exibição, só com o ok da produção. 02-provas veta "data de exibição" sem fonte |
| Quando a grade ou a página do programa mostrar a edição | Story na véspera com contagem regressiva; no dia, story antes de cada horário da grade daquele dia (conferir na grade, não supor 13h e 18h) | Fonte pública e conferível para a data |
| Dia da exibição | Nenhum reel extra (nunca 2 reels no dia). Se cair num sábado, o timelapse do dia ganha na legenda a linha "Foi ao ar hoje na TV Câmara Campinas" só depois do horário confirmado | Ritmo do CLAUDE.md |
| Depois que a edição estiver no site ou no YouTube | Link nos stories e no destaque PROVA: "Assista à entrevista inteira". Isso responde ao "quer ver inteiro" do tl01 sem cortar os assuntos 1 e 6 para o feed | A emissora aparece só em texto e link, sem logo nem cores (catálogo, seção 5) |
| Minutos citados | Os rótulos "min" contam da abertura do programa na gravação do celular (14:35). A edição exibida pode ter outros blocos e cortes: antes de citar minuto junto do link, conferir o minuto na versão exibida. As peças já renderizadas ficam como estão | Edições de 30 a 47 min contra cerca de 15 min de entrevista na gravação |
| Trava da produção | Sai a trava "antes da exibição, só com o ok da produção". Continua valendo a autorização de imagem e voz da Mirna | pecas-e-calendario, item 2 |
| REACT | A data é o melhor gancho para gravar o REACT 01 ("Fui ao ar na TV Câmara Campinas. Olha o que eu respondi..."): 20 min de selfie, a única peça da série com o rosto de frente o tempo todo [HIPÓTESE sobre o gancho; custo pelo catálogo] | Bruno falando para a câmera: 4 de 4 reels acima de 3,4x a mediana de alcance [FATO, F1-auditoria-conta.md, `ig_post_stats`] |
| Medição | Na semana da exibição: visitas ao perfil por dia contra a base de 14,9 [ESTIMATIVA: 447 / 30, contexto.md], seguidores no `ig_follower_growth` de D a D+2 e fatia de Campinas no `ig_audience`. Registrar no arquivo da semana do Módulo 7 | Separar efeito da TV do efeito dos reels |
| Se a data cair depois de 21/11 | A série inteira terá saído antes da exibição. A semana da exibição fica com stories, link e o REACT, se gravado; nada de repostar reel da série no feed, salvo o que chegar a 3x | A lista de remake do playbook começa em 3x o normal da conta [FATO, `ig_reel_checkup`, remake_candidates] |

---

## 9. Ações que só o Bruno executa (com prazo)

| Até | Ação | Ferramenta |
|---|---|---|
| hoje, antes das 15h01 | Guardar o print da liberação da Mirna; perguntar se cobre publicar antes de ir ao ar e qual é a data | conversa com a Mirna |
| dom 25/10, 18h30 | Trocar a última frase da legenda do tl01 (seção 5) | PostZen, editar post m171tvpw4z0c0rxz7fpak824bd8gx35v |
| dom 25/10 a sex 30/10 | Ler cada story da série antes de expirar e anotar votos e respostas de caixa | app e Buzzfy |
| ter 27/10, 18h30 | Ler o tl01 com 48 h e escolher o estado da seção 6.1 | Buzzfy `ig_post_stats` e `ig_reel_checkup` |
| qua 28/10 | Agendar o tl02 (corrigido) para sáb 31/10, se VERDE; mc04 recortado no dia seguinte | PostZen |
| toda quarta | Agendar o timelapse do sábado pela regra 6.2 | PostZen |
| quando sair a data | Seção 8.2 | grade da TV Câmara e app |

---

## 10. Lacunas

- Data de exibição: sem dado. A busca na web não achou a edição; o portal da Câmara deu erro de conexão na primeira tentativa e o WebFetch estourou o tempo (registrados como erro).
- Se a liberação verbal da Mirna cobre publicar antes da exibição e se ela fala pela produção: sem dado.
- Votos por número no tl01: nenhuma ferramenta permitida lê o texto dos comentários; contagem manual.
- Votos de enquete e respostas de caixa nos stories: fora do `ig_post_stats`; contagem manual.
- Quadro 0 do tl01 e do tl05 conferido pela ficha e pelo `ENGINE.md`, não pela folha (tl05 está sendo refeito).
- Marca do gravador e etiqueta do monitor nos mc: 1 quadro conferido por peça, não 20.
- Se o PostZen publica trial reel: sem dado.
- Audiência da TV Câmara: sem dado; só as views do site (27 a 124 nas edições recentes).
- Alcance em feriado (02/11, 15/11, 20/11): sem dado. A leitura de 48 h do tl02 cai em 02/11.
- O tl01 ainda não saiu: toda a seção 6 é árvore de decisão, nenhuma escolha está medida.
- Respiro novo do tl02 (qual fala entra): escolha de produção, não feita aqui.
