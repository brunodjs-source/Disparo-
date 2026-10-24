# Plano da cadeira M · Pessimista de risco · Cronograma de 25/10 a 22/11/2026 · @o_estrategista.com.br

**Persona:** guardião de caixa no papel de CFO. Olho unit economics, CAC, payback e corte de desperdício. Neste cliente o caixa tem quatro moedas: minuto do Bruno (a mais escassa), hora da agência, capital de relação com terceiros (Mirna, TV Câmara, Tzur) e dinheiro (verba zero até 18/11, decisão D4 de 21/10 [FATO, 10-decision-brief.md, linhas 139 a 144]).

**OTIMIZA PARA:** preservar caixa e cortar desperdício.

**PONTO CEGO, assumido por escrito:** o custo de não agir. Um CFO enxerga o gasto que aparece na planilha e esquece a receita que deixou de acontecer. Compensação adotada neste plano: (1) cada corte vem com a conta do que ele deixa de render (seção 1.3); (2) três gastos ficam blindados contra corte: o bloco 1 de gravação, os 4 números de segunda do Bruno e as 6 ações de seguro de menos de 30 min; (3) o portão ganha uma linha "custo de não agir" com as vagas vazias e o alcance de referência que elas não geraram.

**PERGUNTA CONTRÁRIA:** quanto custa não fazer nada? Resposta na seção 1.3, com números.

Rodada de sábado, 24/10/2026, escrita entre 18h00 e 19h30 (horário de São Paulo). Trabalho isolado: não li os planos das outras cadeiras. Só leitura em todas as ferramentas; nada foi publicado, agendado, alterado ou enviado.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha uma objeção sozinho. Métrica que falta: "sem dado".

---

## 0. Conferências próprias desta cadeira (depois do livro de fatos das 15h50)

| # | O que conferi (só leitura) | Hora (SP) | Resultado |
|---|---|---|---|
| C1 | PostZen `listPosts`, conta j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 03h UTC a 01/12 03h UTC | 18h03 | [FATO] 48 itens: 6 stories publicados hoje (14h00, 14h03, 15h00, 15h01, 16h30, 18h00) e 42 agendados: stories de hoje às 19h30 e 20h30, Dentista B 21h, **28 stories de 25 a 31/10**, story pf01, 9 reels (tl01, pb01, ci01, po01, pb02, tl02, tl03, tl04, tl05) e car01. De dom 01/11 a sex 06/11: nada. Legendas de pb01, car01, ci01, po01 e pb02 iguais às da leitura das 15h46 (sem data, sem @) |
| C2 | `conteudo/stories-objecoes/06-agenda-postzen.md` (commit eeb4f21, 17h06) | 18h00 | [FATO] 28 stories sem sticker agendados de 25 a 31/10; story pf01 trocado pela versão "em dois meses" (`pf01-dentista-story-v2.mp4`, confirmado no C1). Chamadas que dependem do feed: 26/10 20h30, 28/10 20h30, 29/10 17h30 e 20h30, 30/10 20h30 |
| C3 | `conteudo/stories-objecoes/05-manuais-bruno.md` (commit 2b3a7d8, 17h00) | 18h00 | [FATO] 27 stories à mão de 25 a 31/10 e 4 provisórios em 01 e 02/11. O de dom 25/10 09h02 ainda pede "Votou SIM? Responde este story." (a ETAPAS só dispara com "etapa" ou "etapas" [FATO, livro de fatos, fato 118]) |
| C4 | `ffprobe` e `stat` dos renders em `scratchpad/tv/render/` | 18h05 | [FATO] ob01 17,9 s (render às 16h33), ob02 28,37 s (15h54), ob03 15,1 s (17h00). O "render final: sem dado" do fato 97 do livro caiu: os três existem. pf01 refeito às 16h26 (24,0 s) |
| C5 | Quadros aos 0, 1,5 e 2,9 s de ob01, ob02 e ob03 | 18h06 | [FATO] Nos três, o Bruno está em cena desde o quadro 0, de perfil, atrás de um monitor que ocupa boa parte da metade de baixo da imagem; nunca olha para a câmera. Cartão "OBJEÇÃO · VOCÊ DIZ" desde o quadro 0. Folha em `scratchpad/cadeiraM/folha_ob.png` |
| C6 | `videos/tv-camara/cortes/mc04.spec.json` (15h29) e transcrição | 18h08 | [FATO] mc04 = 1700,967 a 1705,567 s (4,6 s), manchete "Eu construí patrimônio, eu construí família."; fim no vale de energia depois de "família," (a voz cai em 1705,40 s e "eu construí tudo" volta em 1705,62 s). "estrategista digital" (1709,18 a 1710,18 s) fica fora |
| C7 | `date` para os dias da semana | 18h00 | [FATO] dom 25/10, qua 28/10, qui 29/10, dom 01/11, seg 02/11, qui 05/11, dom 08/11, qua 11/11, qui 12/11, dom 15/11, qua 18/11, qui 19/11, sex 20/11, dom 22/11, seg 23/11, qua 23/12/2026, sex 22/01/2027 |

Correções que este plano já incorpora (do pedido desta rodada e do livro de fatos): saídas de seguidores de 12 a 21/10 são 6 (líquido de -5) e não 7; máximo de views das edições no site da TV é 1.400 e não 124; a promessa do tl01 já é "o mais votado eu solto inteiro depois que a entrevista for ao ar"; a base de story de 7 dias é 982 até 14h11 e 1.041 às 15h30; o Módulo 7 de 21/10 tem 3 decisões não executadas (e 1 em parte) em 8; a leitura parcial de diagnóstico do brief é em 04/11; o piso de seguidores do brief é ganho líquido de 12 em 14 dias depois de 27/10; o saldo de seguidores até 08/11 só fecha numa leitura de 11/11 [FATO, livro de fatos, fatos 175 a 182 e derivação 5].

---

## 1. Veredito, o caixa e a pergunta contrária

### 1.1 Veredito (9 linhas)

1. A agenda da S1 já está quase certa e a S2 a S4 está vazia onde importa: mexer pouco agora, encher depois com portão.
2. Uma peça só muda de lugar: o ci01 sai de qua 28/10 e vai para seg 02/11 às 21h. A S1 cai de 6 para 5 reels, o dia da exibição ganha peça sem produção nova e a peça com mais voz e rosto da Mirna sai de antes da exibição. pb01, car01, po01, pb02 e tl02 ficam.
3. Gasto que não corto: bloco 1 de gravação até qua 28/10 23h59 (consórcio, nutricionista e vídeo de 02/11, 31 a 49 min [ESTIMATIVA, F5]). Sem ele a conferência de 11/11 fica "não testado" e a semana da TV roda só com corte de perfil, formato nunca medido.
4. Corto o que não tem retorno medido: 8 dos 27 stories à mão da S1, o 6º reel, o 2º carrossel da S1 feito às pressas, R2 e R3 antes do resultado do R1, cortes do banco antes de a família da TV passar no portão, Case Tzur e qualquer anúncio.
5. Compro seguro barato até seg 26/10 20h59: print e @ da Mirna, 6 automações de conta toda desligadas, bio para /tabuleiro/?o=ig-bio e 4 números do funil toda segunda. Soma de 30 a 40 min do Bruno [PRIOR].
6. Régua única por 4 semanas: alcance em 48 h sobre 53 (27, 42, 106, 150; pulo 60% e 75%); PARAR só com n de 2; com n de 1 a peça "pausa" e volta ao banco.
7. 5 reels e 2 carrosséis por semana é teto. Vaga sem peça aprovada fica vazia, com motivo escrito; nunca animação com voz sintética, nunca carrossel só de texto.
8. Teto de minutos do Bruno: de 112 a 180 na S1 e de 57 a 147 por semana depois [ESTIMATIVA com PRIOR], contra 170 a 327 da F5. A diferença vem das respostas: a F5 orçou 105 a 210 min por semana e o volume medido é de 5 interações em 7 dias.
9. A chance de cumprir os critérios do enquadramento é baixa em todas as decisões (0,08 a 0,25). A meta de 10 diagnósticos por mês não fecha pela bio nem pelo teto de comentários: este plano protege o caixa e compra informação; não promete funil.

### 1.2 O caixa e a conta de unidade

**Quanto custa cada tipo de peça e quanto ela devolve (o que existe medido)**

| Peça | Minuto do Bruno | Hora da agência | Retorno medido | Contas alcançadas por minuto do Bruno |
|---|---|---|---|---|
| Reel do Bruno para a câmera (nicho) | 12 a 18 de gravação [ESTIMATIVA, F5] + 2 a 3 de resposta [PRIOR] | até 1h51 com motor do zero; com motor pronto, sem dado [ESTIMATIVA, F5] | alcance mediano 167,5, pulo 48,1%, 0,65 comentário por 100 contas (n 4) [FATO, F1 e F8] | 8 a 12 [ESTIMATIVA: 167,5 / 14 a 21] |
| Corte da TV (pb, ci, po, ob, pf reel) | 1 a 2 de marcação da Mirna [PRIOR] | já feito; cerca de 6 min de calendário por corte com ficha [ESTIMATIVA, F5] | sem dado: formato de perfil em 3/4, nunca medido na conta [FATO, quadros, fato 88 e C5] | sem dado |
| Timelapse | 1 a 2 de marcação [PRIOR] | já feito (cerca de 52 min cada) [ESTIMATIVA, F5] | sem dado; montagem mede 0,69x em contas de 1 a 5 mil [FATO, playbook, fato 146] | sem dado |
| Carrossel com foto do Bruno na capa | 0 a 5 de aprovação [PRIOR] | cerca de 36 min [ESTIMATIVA, F5] | feed com foto do Bruno: mediana 111 e 23 visitas ao perfil somadas (n 7) [FATO, fato 51] | 22 ou mais [ESTIMATIVA: 111 / 5] |
| Carrossel ou estático só de texto | 0 a 5 | cerca de 36 min | mediana 34,5 e 1 visita (n 6), já em PARAR [FATO, fato 51 e F7] | baixo |
| Story agendado | 0 | minutos de render | 7 a 31 contas por story na pilha de hoje (provisório) [FATO, fato 58] | infinito (não usa o Bruno) |
| Story à mão | 1 a 2 [PRIOR, F5] | 0 | o mesmo alcance de um agendado; o que ele acrescenta é o sticker (voto, toque, resposta), que só o Bruno lê no app [FATO, fato 67] | o valor está no número do sticker, não no alcance |
| Trial Reel de remake (R1 a R3) | 0 pelo PostZen, se a conta for elegível; 3 a 5 pelo app [PRIOR] | 1 a 2 h por remake [PRIOR, F5] | 21% das vezes bate o alcance usual em conta pequena; 35% com original de 5x ou mais; 15% de 2 a 5x [FATO, playbook, fatos 150 e 151] | sem dado |
| Dentista C | 0 | 0 (pronto) | sem dado; 3ª edição da mesma fala [FATO, fato 101] | sem dado |

**Funil medido e o que falta para calcular CAC e payback**

| Etapa | 30 dias | 7 dias, sem anúncio | Fonte |
|---|---|---|---|
| Contas alcançadas | 3.216 (1.907 de anúncio) | 571 | [FATO, `ig_account_stats`, fatos 10 e 15] |
| Visitas ao perfil | 447 | 74 (10,6 por dia) | [FATO]; [ESTIMATIVA: 74 / 7] |
| Cliques no site | 7 (1,57% das visitas) | 0 | [FATO, fato 14] |
| Comentários | 14 | 2 | [FATO] |
| Respostas de story | 7 | 3 | [FATO] |
| Mensagens no WhatsApp, testes concluídos, diagnósticos agendados e realizados | sem dado (só o Bruno vê) | sem dado | [FATO, fato 143] |
| Vendas | 0 | 0 | [FATO, fato 8] |

- **CAC em minutos do Bruno por diagnóstico:** sem dado. Nenhum diagnóstico tem registro; sem os 4 números de segunda, continua sem dado nas 4 semanas.
- **Payback:** sem dado. O preço do serviço não aparece em nenhuma fonte lida (a O6 diz "parte variável do contrato: conferir com o Bruno" [FATO, F6]).
- **Conta de ponto de equilíbrio da meta:** 10 diagnósticos por mês só pela bio, com 1,57% de clique e 100% de conversão depois do clique (piso impossível), pedem 637 visitas por mês; o ritmo orgânico é de 317 [ESTIMATIVA, F8: 10 / 0,0157 e 74 / 7 x 30]. Falta o dobro das visitas mesmo no cenário perfeito. Pelo comentário, o teto até 22/11 com 5 posts de TABULEIRO no nível do Dentista A é de 3,7 a 5,5 comentários de qualquer tipo [ESTIMATIVA, F8].
- **Leitura de CFO:** o topo do funil existe (visitas), o meio não é medido (do clique ao WhatsApp e à agenda) e o fundo é zero. Gastar mais minuto no topo antes de medir o meio é comprar estoque sem saber se ele vende. Por isso os 4 números de segunda entram como gasto blindado.

**Orçamento de minutos do Bruno** [ESTIMATIVA com PRIOR por item; minutos reais: sem dado até a linha "feito" da S1]

| Item | S1 (25 a 31/10) | Por semana, S2 a S4 | Base |
|---|---|---|---|
| Gravação | 31 a 49 (bloco 1) | 12 a 36 (piso 1, meta 2 roteiros) | [ESTIMATIVA, F5] |
| Stories à mão | 19 x 1 a 2 = 19 a 38 | 14 a 19 x 1 a 2 = 14 a 38 | contagem deste plano; minuto [PRIOR, F5] |
| Marcação da Mirna | 6 peças x 1 a 2 = 6 a 12 | 1 a 4 peças = 1 a 8 | fichas [FATO, fato 90]; minuto [PRIOR] |
| Respostas a comentário e story | 10 a 30 | 10 a 30 | 5 interações em 7 dias [FATO, fato 15] x 2 a 3 min [PRIOR], até o dobro com a série |
| Uma vez: Mirna, automações, bio, edições no PostZen | 36 a 41 | 0 | [PRIOR] |
| Lista da rodada e agendamento | 0 | 10 a 20 | [PRIOR] |
| 4 números de segunda | 10 | 10 | [PRIOR] |
| Trial Reel pelo app, se preciso | 0 | 0 a 5 | [PRIOR] |
| **Soma** | **112 a 180** | **57 a 147** | contra 170 a 327 da F5 |

Teto declarado para S2 a S4: 90 min por semana [PRIOR], corrigido pela linha "feito" da S1. Se estourar, corta nesta ordem: (1) compartilhamento do reel à mão, salvo as 3 menções à Mirna; (2) link do diagnóstico diário vira 3 por semana; (3) marcação da Mirna em peça em que ela só aparece em plano aberto (tl); (4) enquete diária vira 3 por semana; (5) Trial Reel pelo app. Nunca se corta: piso de gravação, resposta a comentário dentro de 7 dias, 4 números de segunda.

### 1.3 Pergunta contrária: quanto custa não fazer nada?

Respondo item a item, porque "não fazer nada" tem custos de tamanhos muito diferentes.

| Se não fizer | Custo de não fazer | Custo de fazer | Leitura |
|---|---|---|---|
| Encher as vagas de S2 a S4 (11 vagas de reel neste plano, 12 na conta da F5) | alcance bruto não gerado de 462 a 1.843 contas-post [ESTIMATIVA: 11 x 42, piso da régua, e 11 x 167,5, mediana do Bruno para a câmera; contas se repetem entre posts, então é teto, não soma]. Em comentários: de 1,6 a 12 [ESTIMATIVA: x 0,35 e x 0,65 por 100]. Isso é o tamanho inteiro do teto de comentários da TABULEIRO | gravação de 12 a 36 min por semana e agência para editar | **O maior custo de não agir do plano.** Vaga vazia sai barata no caixa e cara no topo do funil |
| Gravar o bloco 1 até qua 28/10 | a conferência de nicho de 11/11 fica "não testado (n de 1)": só o Dentista A conta; a decisão D1 de 21/10 atrasa pelo menos até 25/11 [ESTIMATIVA: 2 semanas até a próxima janela com 3 reels lidos em 48 h]; o único formato medido acima de 1x (5,2x o da animação [FATO, fato 21 derivado]) fica fora do feed por 4 semanas, salvo 3 remakes em 720p | 31 a 49 min do Bruno [ESTIMATIVA, F5] | Gasto blindado. É o custo de não agir que meu ponto cego esconderia |
| Pedir o print e o @ da Mirna | risco de cauda: 10 peças de feed e cerca de 20 stories com imagem ou voz dela no ar com liberação só verbal; se a produção pedir retirada, a série inteira sai e o que foi visto não volta [FATO, fato 90 e item 2 do pecas-e-calendario]. Probabilidade: sem dado | 1 mensagem (5 a 10 min [PRIOR]) | Seguro barato: comprar até seg 26/10 20h59 |
| Desligar as 5 automações de conta toda e a ETAPAS de story | comentário de parabéns com "caso" ou "estrategista" recebe direct de diagnóstico ou de PDF e gasta a única resposta privada daquele comentário [FATO sobre a regra, fato 120; HIPÓTESE sobre a frequência, palpite 46] | 6 min [PRIOR] | Seguro barato |
| Trocar o link da bio | semana da TV com 0,5 a 1 clique pela bio [ESTIMATIVA, F8: 32 a 63 visitas x 1,57%]; a porta de quem vem da TV não leva ao teste nem cita a TV | 5 min [PRIOR] | Seguro barato; efeito sem dado |
| Informar os 4 números de segunda | a regra de abandono de 18/11 ("0 diagnóstico agendado, troca-se a porta") não roda; mais um mês de conteúdo sem saber se o funil converte | 10 min por semana [PRIOR] | Gasto blindado |
| Mexer na agenda do PostZen (opção "não mexer") | S1 com 6 reels contra a regra de 5; dia da exibição sem peça no feed; ci01 com a voz e o rosto da Mirna 5 dias antes da exibição. O 6º reel em si não tem custo medido (5 a 7 reels por semana: 7,0% de estouro; 3 a 5: 6,0% [FATO, fato 152]) | 1 edição de reel, 1 story apagado, 3 itens manuais cortados | Não fazer nada é aceitável para pb01, car01, po01, pb02 e tl02; para o ci01 não |
| Cortar 8 stories à mão | 8 a 16 min por semana do Bruno [PRIOR] gastos em compartilhamentos cujo número nenhuma ferramenta lê | 0 | Corte sem custo de informação |

**Resposta curta:** não fazer nada custa pouco no caixa e muito na informação. Os três custos grandes são o feed vazio de S2 a S4, a gravação que não vem e o funil que não é contado. Os outros (Mirna, automações, bio) são seguros de minutos que um CFO compra no mesmo dia.

---

## 2. Respostas às 22 perguntas

**P1. Quais decisões o plano move, qual número muda, com que fonte e em que segunda é lido?**

| Decisão | O que muda | Número que muda | Fonte | Leitura |
|---|---|---|---|---|
| D1 | ci01 de qua 28/10 para seg 02/11 21h; o resto fica | reels na S1: de 6 para 5; reels prontos na S2: de 1 (tl03) para 2 | `listPosts` [FATO, C1] | família da TV com n de 3 em dom 01/11 21h05 (decide se o ci01 sai); Módulo 7 de seg 02/11 19h; visitas por dia de 02 a 04/11 lidas em qui 05/11 e sex 06/11 (atraso de até 48 h [FATO, fato 140]); saldo de seguidores até 08/11 em qua 11/11 |
| D2 | bloco 1 obrigatório (2 roteiros + vídeo de 02/11); depois piso de 1 e meta de 2 roteiros, ligados à conferência de 11/11; R1 como Trial Reel primeiro | n de nicho em 11/11: de 1 (Dentista A) para 3 | `ig_post_stats` | qua 11/11 21h05 |
| D3 | 5 reels e 2 carrosséis como teto; vaga vazia permitida; nenhum 6º reel | S1 = 5 reels e 1 carrossel; S2 a S4 até 5 e 2 | `ig_posts`, `ig_post_stats` | seg 09/11 e seg 23/11, 19h |
| D4 | stories à mão da S1 de 27 para 19; depois 2 obrigatórios por dia e 1 opcional; ob no feed só com a família da TV fora de PARAR | views de story em 7 dias (piso 982); respostas | `ig_account_stats` | toda segunda 19h |
| D5 | régua de 53; "pausar" com n de 1; no máximo 3 ações do Bruno por rodada; coluna de custo e de "custo de não agir" | decisões executadas sobre o total (base de 21/10: 4 de 8 com sim [FATO, fato 125]) | arquivos de semana | seg 26/10 21h05; ter 27/10 18h35; dom 01/11 21h05; seg 02/11, 09/11, 16/11 e 23/11 às 19h |
| D6 | 6 automações desligadas; TABULEIRO de conta toda com texto genérico a partir de dom 01/11; bio; 4 números | disparos de terceiros; diagnósticos de 30 min | `listCommentAutomationLogs`; número do Bruno | parcial em qua 04/11 (brief) e seg 09/11; conferência em qua 18/11 |

**P2. Qual régua, quais limites, a mesma do começo ao fim?**
Alcance em 48 h sobre a mediana fixa de 53 (00-SISTEMA, 17 reels de 21/09 a 21/10 [FATO, fato 24]). Limites [ESTIMATIVA, derivação 2]: 27 (0,5x), 42 (0,8x), 106 (2x), 150 (palavra-chave, CLAUDE.md); pulo de 60% e 75%. A mesma régua de 25/10 a 23/11. A mediana de 37,5 do Buzzfy e o normal de 57 views entram só como colunas de referência no arquivo da semana, nunca como régua. Motivo de caixa: a régua móvel mudaria a decisão no meio das 4 semanas sem nenhum reel mudar (a base de 37,5 tem 12 de 20 reels de animação [FATO, F7]); trocar de régua no meio quebra a comparação S4 contra S1 do D5.

**P3. Grade dia a dia e hora a hora, dias conferidos, feriados?**
Está na seção 3, com o dia da semana conferido por `date` [FATO, C7]. Feriados: seg 02/11 (Finados e exibição): só 3 stories à mão do Bruno, o resto agendado; Módulo 7 lido pelos agentes, lista do Bruno vence ter 03/11 11h. Dom 15/11 (Proclamação): carrossel 12h agendado, stories só agendados, sem bloco à mão. Sex 20/11 (Consciência Negra): reel das 21h agendado se houver peça aprovada, stories só agendados. Leitura de peça publicada em feriado entra na mediana e não fecha PARAR sozinha [FATO, regra da F7]. Alcance em feriado com reel do Bruno: sem dado (o único feriado medido, 12/10, é de animação, 3 pares [FATO, fato 41]).

**P4. Antes, no dia e depois de 02/11?**
- **Antes (25/10 a 01/11):** tl01, pb01, car01, po01, pb02 e tl02 no feed, todos já agendados; 28 stories agendados com "NA TV · SEG, 02/11" ou "VAI AO AR SEG, 02/11" no texto (contagem pelo texto, custo zero); bastidor no bloco das 09h00; mc02 (dom 25/10) e mc03 (seg 26/10) já agendados; mc04 dom 01/11 09h. Sem sticker de contagem, salvo horário confirmado até dom 25/10 (custo: +4 stories à mão [ESTIMATIVA, derivação 17]).
- **No dia (seg 02/11):** 09h00 estático agendado sem hora ("SEG · 02/11 · NA TV CÂMARA CAMPINAS", programa, repórter, canais e site [FATO, fato 135]); assim que o horário vier, story à mão com a hora, menção à Mirna e link para tvcamaracampinas.com.br/ao-vivo; se às 12h00 o horário seguir sem dado, story à mão com link para /programacao ("Horários na programação"); 20h30 chamada agendada; 21h00 ci01; 21h05 compartilhamento do ci01 com menção. Se a hora não vier até a noite, o dia fica só com o estático das 09h00, a chamada e o ci01, e nenhuma peça diz "foi ao ar".
- **Depois (03/11 a 21/11):** o "o que eu disse na TV" sai em stories (trechos de 10 a 15 s no bloco das 09h00) e no feed por ob01 a ob03, tl03 a tl05 e o "mais votado" se tiver 5 votos ou mais; link da edição exibida quando subir no site ou no YouTube. Nada de recortar ou filmar a edição exibida [FATO, termos da TV, fato 137].

**P5. pb01, car01, ci01, po01 e pb02, um por um**

| Peça | Decisão | Motivo | Data e hora | Até quando o Bruno mexe |
|---|---|---|---|---|
| pb01 | Fica | Apresenta o Bruno (DJ por 20 anos) sem entregar caso nem método; abre a dupla P&B; custo zero de execução | seg 26/10 21h | legenda com a data e o @ (se houver) até seg 26/10 20h59 (2 a 3 min) |
| car01 | Fica | Único carrossel pronto [FATO, F5]; capa com o Bruno e a Mirna; mover deixaria a S1 sem carrossel | ter 27/10 12h | legenda até ter 27/10 11h59: data, @, "na gravação" e um pedido só (o direct) |
| ci01 | **Move** | (1) resolve a regra de 5 reels da S1 sem produção; (2) enche o dia da exibição, hoje vazio [FATO, C1]; (3) é a peça com mais Mirna: voz em 2 trechos e rosto por 10,7 s [FATO, fato 90], e a liberação é verbal; (4) dá 5 dias para resolver a atribuição de "Ainda. Sempre vai ser." [FATO, fato 91] e a abertura de costas sem rosto até 2,5 s [FATO, fato 88]; (5) a frase já foi anunciada hoje com "NA TV · SEGUNDA, 02/11" [FATO, fato 77 e listPosts] | seg 02/11 21h (2026-11-03T00:00:00Z) | mover até qua 28/10 20h59; apagar o story "QUA · 21H · NO FEED" de 28/10 20h30 (m17fs6f2w0yyddqfw8p2vebqbd8gwcne) até qua 28/10 20h29; legenda versão A da F4 até dom 01/11 23h59 |
| po01 | Fica | Mover custa uma vaga na S1 sem peça com rosto para pôr no lugar (o bloco 1 vence qua 28/10 23h59 e a edição leva quinta e sexta); o ganho de mover ("ganha força com a prova de que foi ao ar") é hipótese sem fato perto [FATO, palpite 40 do livro]; a promessa do tl01 não pede o po01 depois (o "inteiro" se cumpre pelo link ou por corte longo). Menos edições: as 2 chamadas agendadas do dia 29/10 seguem valendo | qui 29/10 21h | legenda até qui 29/10 20h59: trocar "Comenta a palavra." por "Comenta qual delas." [FATO, F4] e pôr data e @ |
| pb02 | Fica | Fecha a dupla P&B com n de 2 antes da exibição; o pedido de direct funciona antes ou depois | sex 30/10 21h | legenda até sex 30/10 20h59 |

Condição de saída do ci01: se a família da TV (pb01, po01, pb02, todos com 48 h às 21h de dom 01/11) tiver mediana abaixo de 42 ou pulo mediano acima de 75%, o ci01 não vai ao feed em 02/11; vira trechos de story e banco, e a vaga das 21h recebe o nicho 1 se estiver pronto, senão fica vazia. Quem decide: agentes às 21h05 de dom 01/11; quem cancela: o Bruno até dom 01/11 23h59, para nada cair no feriado.

**P6. A promessa do tl01**
A legenda já não promete o sábado [FATO, fato 77 e C1]. Com o ci01 fora, a S1 fica com 5 reels sem precisar de motivo para um 6º. "O mais votado eu solto inteiro depois que a entrevista for ao ar" se cumpre assim, do mais barato ao mais caro: (1) story à mão com o link da edição exibida, quando ela subir no site ou no YouTube, com o resultado da votação no mesmo story (custo: 1 a 2 min do Bruno; compartilhar link é livre pelos termos [FATO, fato 137]); (2) se um assunto somar 5 votos ou mais, corte longo desse assunto como reel na seg 09/11 21h (custo: 1 corte de agência); (3) com menos de 5 votos somados, story dizendo que segue o plano, sem fingir votação [FATO, regra do catálogo, fato 170]. O Bruno conta os votos no app até seg 02/11 (nenhuma ferramenta permitida lê o texto dos comentários [FATO, fato 143]).

**P7. Ordem de tl02 a tl05, portão e destino**
Ordem como está no PostZen: tl02 sáb 31/10, tl03 sáb 07/11, tl04 sáb 14/11, tl05 sáb 21/11, sempre 18h30 [FATO, C1]. Portões:
- tl01 lido em ter 27/10 às 18h35 (48 h) decide o tl02: 42 ou mais com pulo até 75%, fica; só um critério ruim, o tl02 pausa (banco) e o tl03 vira a 2ª leitura; abaixo de 27, ou abaixo de 42 com pulo acima de 75%, tl02 pausa e tl03 a tl05 só voltam se outra leitura da família abrir. Com n de 1 a ação é pausar, nunca PARAR (D5).
- tl02 lido em seg 02/11 19h (48h30) decide o tl03; tl03 em seg 09/11 19h decide o tl04; tl04 em seg 16/11 19h decide o tl05, com a regra geral da família (mediana dos timelapses lidos, n de 2 ou mais).
- Cancelamento no PostZen até sex 23h59 anterior ao sábado.
- Timelapse que não vai ao feed vai para o banco, sem gasto novo de agência; trecho em story só se o bloco das 09h00 estiver sem peça. Trial Reel de timelapse: não (o espaço de Trial Reel é do R1).
- Condição extra de risco de relação: tl04 ("Uau!" recortado no rosto dela) e tl05 (carimbo "AINDA?" e selo "REPÓRTER" sobre o rosto congelado) [FATO, fato 90] só saem se a Mirna vir antes. Sem resposta até sex 13/11 12h (tl04) e qui 19/11 12h (tl05, porque sex 20/11 é feriado), o Bruno cancela.
- O tl02 tem 10,4 s sem voz real, acima do teto de 8 s [FATO, fato 92]: aceitar por escrito se o tl01 ficar em MANTER; consertar só se o conserto custar menos de 1 h de agência [PRIOR], senão pausa.

**P8. Ordem de mc02 a mc04 e recorte do mc04**
mc02 dom 25/10 09h01 (já agendado [FATO, C1]); mc03 seg 26/10 17h30 (já agendado [FATO, C1]); mc04 dom 01/11 09h00 (a agendar, 2026-11-01T12:00:00Z), depois do tl02, que traz "Eu construí família" no índice [FATO, fato 78]. Recorte: **1700,967 a 1705,567 s** (4,6 s), o que já está renderizado [FATO, C6], dentro da faixa de 1705,2 a 1705,7 s do 03-plano. Motivo de caixa: zero render novo, fim limpo no vale de energia, e "estrategista digital" fica fora. O corte em 1707,82 s (7,2 s) acrescentaria "eu construí tudo através da profissão" ao custo de um render novo e com "que hoje eu executo" colado na sequência.

**P9. Marcação da Mirna**
- Quem: o Bruno, no app. Quando: no mesmo momento em que compartilha o reel no story (até 15 min depois de publicar [PRIOR]). Onde: toda peça de feed com imagem ou voz dela: tl01, pb01, car01 (capa), po01, pb02, tl02, ci01, tl03, tl04, tl05 [FATO, fato 90]. Menção em story: só 3 vezes (dom 25/10 18h35, story do horário em 02/11, 02/11 21h05).
- Teste único: dom 25/10 18h35, no tl01 publicado. Se o app deixar marcar pessoa num reel já publicado, segue assim. Se não deixar, o @ entra no texto da legenda pelo PostZen antes da publicação de cada peça, nos mesmos prazos de legenda da P5 (custo: 0 minuto depois de publicar).
- Sem o @ até seg 26/10 20h59: as legendas saem sem @, a linha "marcada" do arquivo da semana registra "não feita: sem @", e a grade não muda. O plano não para por causa da marcação.
- Colaboração: nenhum convite antes do print, do @ e do ok dela; depois, só no ci01 (seg 02/11). Motivo: convite que falha na publicação ou é recusado custa relação, e o efeito medido mais perto é 1,13x entre contas [FATO, playbook, fato 148].
- Minutos: 1 a 2 por peça [PRIOR]; 6 a 12 na S1 e 2 a 8 por semana depois.

**P10. Copy depois de 02/11**
- "Foi ao ar" só depois do horário confirmado (legenda, story, capa) [FATO, fato 6]. Versão B do ci01 só se o Bruno trocar no app depois do horário; a versão A agendada já vale sem ele.
- Link da edição exibida: pode, com a TV Câmara como fonte [FATO, fato 137]. Minutos: os do car01 e do tl01 contam da gravação do celular [FATO, fato 81]; escrever "na gravação" e não citar minuto da edição exibida antes de conferir.
- tl03 a tl05: linha nova "A entrevista foi ao ar no dia 02/11, no programa Ser Empreendedor, da TV Câmara Campinas." só com horário confirmado [FATO, F4].
- Continua vetado: "ao vivo", "rede nacional", "a TV Câmara recomenda", "fui convidado pela TV", "entrevista exclusiva", "A TV me chamou de história de sucesso" [FATO, fato 6]; número de seguidores na tela [FATO, F6]; logo da emissora; recortar ou filmar a edição exibida; qualquer anúncio pago com conteúdo da TV sem autorização escrita [FATO, fato 137].

**P11. 5 reels e 2 carrosséis? Dias com 2 reels? Quem produz os carrosséis?**
- S1: 5 reels (tl01, pb01, po01, pb02, tl02) e 1 carrossel (car01). O 2º carrossel da S1 não é feito: dom 25/10 é amanhã e produzir às pressas para cumprir cota é gasto sem retorno medido. Motivo escrito no arquivo da semana.
- S2 a S4: até 5 reels e 2 carrosséis, com vaga vazia permitida. Nenhum dia com 2 reels. Carrossel só na terça e no domingo às 12h, dias sem reel de feed nesta grade: cada dia tem no máximo 1 post de feed. Trial Reel a 6 h ou mais de qualquer reel [FATO, playbook 0,92x, fato 152].
- Carrosséis: 6 da agência (car02 a car07), todos com foto do Bruno na capa (7 fotos de marca disponíveis [FATO, fato 113]), cerca de 36 min cada, 3 h 36 min no total [ESTIMATIVA, F5]. Prazos: car02 e car03 até sex 30/10 23h59; car04 e car05 até sex 06/11 23h59; car06 e car07 até sex 13/11 23h59. O Bruno aprova capa e texto (0 a 5 min cada [PRIOR]). Fontes sem material novo do Bruno [FATO, F5]: CARROSSEL 02 a 04 da TV, Os 5 Lances, Oferta em 5 pilares, Seguidor x comprador (versão nova).

**P12. Bruno em cena nos 3 primeiros segundos**

| Peça | Bruno de 0 a 3 s | Fonte |
|---|---|---|
| Dentista C | sim, selfie, "Dentistas," no quadro 0 | [FATO, fato 101] |
| tl01, tl02, tl03 | sim aos 0,6 e 2,5 s | [FATO, fato 89] |
| tl04, tl05 | pela ficha, plano CB no quadro 0; quadros não conferidos por esta cadeira | [FATO, ficha]; conferência visual: sem dado |
| ob01, ob02, ob03 | sim, de perfil atrás do monitor, desde o quadro 0 | [FATO, C5] |
| pb01, po01, pb02, pf01 | sim, de perfil em 3/4, desde o quadro 0 | [FATO, fato 88] |
| ci01 | em cena de costas, rosto não visível até 2,5 s | [FATO, fato 88]; cumpre a letra da regra, não o formato medido |
| Remakes R1 a R3 | sim, selfie com fala própria; o remake só corta | [FATO, fato 35] |
| Cortes do banco | de perfil ou de costas | [FATO, fato 107] |
| Nicho gravado | regra do bloco: quadro 0 com o Bruno de frente | regra deste plano |
Nenhuma peça da lista é animação com voz sintética.

**P13. Mínimo de gravação, próxima sessão, semana sem gravação**
- Bloco 1 (obrigatório, até qua 28/10 23h59): roteiro 1 consórcio (tomadas com e sem a linha da ABAC), roteiro 3 nutricionista (versões A e B) e vídeo curto de 02/11 com a data falada e sem horário: 31 a 49 min [ESTIMATIVA, F5]. Motivo: com o Dentista A, dá n de 3 para a conferência de 11/11 (o brief de 21/10 fala da mediana "dos 3": consórcio, dentista e nutricionista [FATO, 10-decision-brief, linha 123]), desde que os dois saiam até seg 09/11 21h.
- Blocos 2 a 4: piso de 1 roteiro (12 a 18 min) e meta de 2 (24 a 36 min) [ESTIMATIVA, F5]. Bloco 2 até qua 04/11 23h59 (psicólogo; advogado só com o provimento da OAB lido, senão consórcio 6 "Banco"). Bloco 3 até sex 13/11 23h59, pela conferência de 11/11. Bloco 4 até qua 18/11 23h59, para a S5.
- Depois de 11/11, financiamento por resultado: reel de nicho com 106 ou mais em 48 h "compra" o 2º roteiro da semana seguinte; abaixo de 42, a semana seguinte grava só o piso. Se 11/11 der abandono do nicho, o piso continua com 1 roteiro do Bruno para a câmera fora de nicho (Módulo 3), porque o formato segue sendo o único medido acima de 1x.
- Data da próxima sessão: sem dado (a sessão de seg 26/10 do brief não tem confirmação [FATO, F5]).
- Semana sem gravação, ordem fixa para cada vaga: (1) ob01 a ob03, se a família da TV não estiver em PARAR; (2) Dentista C, uma vez, se o Dentista B ficou em MANTER ou DOBRAR; (3) "mais votado inteiro", com 5 votos ou mais; (4) R1 no feed, se o Trial Reel fizer 106 ou mais; (5) cortes do banco, só com a família da TV em DOBRAR; (6) vaga vazia com motivo escrito. Nunca animação, nunca voz clonada, nunca carrossel só de texto.

**P14. Dentista C e remakes**
- Dentista C: fica como reserva de custo zero. Entra no feed só como item (2) da ordem sem gravação, a partir de sex 06/11, e só se o Dentista B fizer 42 ou mais com pulo até 75% em 48 h (leitura de seg 26/10 21h05). Anúncio: não antes de 18/11 (verba zero, D4 de 21/10 [FATO, fato 169]); depois disso, a decisão é do Bruno com teto escrito e com a Res. CFO 196/2019 conferida [FATO, fato 101]. Direct: não (não há fluxo que mande vídeo por direct).
- Remakes: só o R1 primeiro ("Ele nunca fez um anúncio", 10,14x, faixa de 35% do playbook [FATO, fatos 35 e 150]), como Trial Reel em ter 03/11 14h00, pelo PostZen com `trialParams` (0 minuto do Bruno) se a conta for elegível; se falhar na publicação, o Bruno posta pelo app uma vez (3 a 5 min [PRIOR]). Mudanças: abertura nova, legenda queimada, corte para 45 a 60 s, sem a promessa da "saga de 7 dias" [FATO, F2, fato 37]. R2 em ter 10/11 14h e R3 em ter 17/11 14h só se o anterior fizer 42 ou mais em 48 h. Custo poupado se o R1 falhar: 2 a 4 h de agência [PRIOR].

**P15. Stories por dia, horários, tipos, PostZen ou mão, fonte da frase**
- S1: o que já está agendado (28 stories [FATO, C1]) mais 19 à mão (lista da seção 3.1), cerca de 7 por dia.
- S2 a S4, molde de dia útil: 09h00 bastidor ou trecho "O QUE EU DISSE NA TV" com o Bruno em cena (agendado); 12h00 objeção do dia com enquete (à mão); 12h01 virada (agendado); 12h02 prova de autoridade (agendado); 12h03 link do diagnóstico (à mão); 17h30 frase de efeito (agendado); 20h30 chamada do reel em dia de reel (agendado); 21h05 compartilhar o reel (à mão, opcional, obrigatório só nos 3 momentos de menção à Mirna). Sábado com reel às 18h30: chamada 17h30 e compartilhamento 18h35; caixa de pergunta no lugar da enquete. Total: 6 a 8 por dia, 2 obrigatórios à mão.
- Fontes: frase de efeito do banco de 14 frases com fonte da F6 (estáticos 3 e 4 prontos, hooks com nota do Módulo 4, literais da transcrição com tempo); virada do `01-objecoes.md`; prova do `02-provas.md` com tempo da transcrição; trechos da gravação do celular do Bruno (nunca da edição exibida).
- Feriados (02/11, 15/11, 20/11): só agendados, mais os 3 à mão de 02/11.

**P16. ob01 a ob03**
Renders existem [FATO, C4]; a voz do trecho do ob01 está conferida na ficha ("quem fala é o Bruno" [FATO, fato 98]). Falta, até sex 30/10 23h59: folha de 4 quadros por segundo com nota por efeito e correção do que ficar abaixo de 8 (CLAUDE.md); se a folha já existir, registrar. Lugar: ob01 qui 05/11 21h; ob03 sex 06/11 21h, se o nicho 2 não estiver pronto; ob02 qua 11/11 21h. Todos só com a família da TV fora de PARAR na leitura de dom 01/11 21h05. ob02 tem 82% do áudio do pf01 [ESTIMATIVA, F2]: como o pf01 só sai em story (ter 27/10), a repetição no feed não existe; se o pf01 virar reel por DOBRAR, o ob02 sai do feed. Substituto se a família parar: nicho gravado, Dentista C, vaga vazia.

**P17. PARAR, MANTER, DOBRAR e TESTAR**

| Formato | PARAR (n de 2 ou mais) | MANTER | DOBRAR | TESTAR e pausar |
|---|---|---|---|---|
| Reel (por família: Bruno para a câmera; família da TV; timelapse) | mediana de alcance em 48 h abaixo de 42 ou pulo mediano acima de 75% | 42 a 105 e pulo até 75% | 106 ou mais e pulo abaixo de 60% | n de 1: TESTAR, no máximo 1 vaga por semana; n de 1 abaixo de 27 ou com pulo acima de 75%: pausar (banco, reversível) |
| Carrossel | abaixo de 42 em 2 | 42 a 105 | 106 ou mais e 2 visitas ao perfil ou mais | n de 1: TESTAR |
| Story (semana) | views de 7 dias abaixo de 982 por 2 semanas seguidas: volume volta a 5 por dia | 982 ou mais | 4 respostas ou mais: o tipo que respondeu ganha 1 quadro | tipo manual com 0 voto ou 0 toque por 2 semanas cai à metade |
| Trial Reel | abaixo de 42 em 48 h: o próximo remake não sai | 42 a 105 | 106 ou mais: vai ao feed e ganha 2ª versão | sempre n de 1 |

Datas: seg 26/10 21h05 (Dentista B com 48 h); ter 27/10 18h35 (tl01); dom 01/11 21h05 (família da TV com n de 3, decide o ci01); seg 02/11 19h (S1 inteira; agentes leem no feriado, a lista do Bruno vence ter 03/11 11h); seg 09/11, 16/11 e 23/11 às 19h; qua 11/11 21h05 (nicho); qua 18/11 (seguidores e diagnóstico, regras do brief). Leitura de feriado entra na mediana e não fecha PARAR sozinha. No máximo 3 ações do Bruno por rodada, em ordem.

**P18. TABULEIRO**
- Até dom 25/10 18h30 (antes do tl01), o Bruno desliga CASE, ESTRATEGISTA, ETAPAS (comentário), FUNIL, CAIXA e ETAPAS de story [FATO sobre a colisão de "caso" e "estrategista" com a série, fato 114]. As 10 presas a posts antigos ficam (0 comentário, 0 custo; mexer nelas é minuto do Bruno sem retorno).
- Novembro: uma TABULEIRO de conta toda com o texto genérico da F8 (seção 8), criada pelo Bruno até sáb 31/10 e ligada a partir de dom 01/11, com a do Dentista B desligada no mesmo momento. O pedido "Comenta TABULEIRO" só entra em post cujo anterior do mesmo formato fez 150 ou mais em 48 h, no máximo 1 por semana, nunca em 02/11, nunca em story.
- Leituras que abrem o pedido: Dentista B (seg 26/10 21h, abre o próximo de nicho); pb01 (qua 28/10 21h, abre o pb02, troca de legenda até sex 30/10 20h59); tl02 (seg 02/11, abre o tl03); tl03 (seg 09/11, abre o tl04); cada reel de nicho em 48 h.
- Pedidos de direct nas legendas: um pedido por legenda. pb02 fica com "Me manda a data no direct."; car01 fica só com o direct; po01 com "Comenta qual delas."; ob com o pedido da ficha.
- Contagem por etapa: (1) alcance e pulo do anterior em 48 h (`ig_post_stats`); (2) comentários do post; (3) disparos de TABULEIRO pela diferença do total do log entre segundas, sem perfis do Bruno; (4) visitas ao perfil e cliques no site (`ig_account_stats`); (5) a (8) com o Bruno: `tabuleiro_complete` e `generate_lead` no GA4, mensagens que começam com "Fiz O Tabuleiro no site" e com "Quero agendar o Primeiro Lance", directs que citam a TV, diagnósticos de 30 min agendados e realizados. "Diagnóstico" conta só a conversa de 30 min; o teste de 12 casas conta como "teste" [FATO, fato 131].

**P19. O que muda em cada post contra o anterior da mesma linha**
P&B: pb01 para pb02 muda o assunto (carreira para caso). Timelapse: tl01 a tl05 mudam o assunto (índices diferentes), mesmo formato. Família da TV: po01 para ci01 muda formato (pontos para cinema) e assunto; por isso o ci01 conta como TESTAR dentro da família. ob01 para ob02 para ob03: muda o assunto (objeção), mesmo formato. Nicho: Dentista A para B mudou o formato; consórcio e nutricionista mudam o assunto (profissão) e mantêm o modelo do A. Dentista C contra B: muda o formato (prédio de palavras), mesmo assunto. R1 contra o original: 2 ou 3 mudanças reais pela regra de segunda vida (regra diferente, de remake). Carrosséis: muda o assunto, mesma capa com foto do Bruno.

**P20. Regras de texto**
Este arquivo e todas as copys propostas: sem travessão, sem emoji, sem promessa de resultado, sem os nomes vetados, no máximo uma "não é X, é Y" por peça (a frase "Fila de espera não é sucesso. É teto." já gasta a dela), sem as frases vetadas do 02-provas.md, sem logo de terceiro, número de caso só como fato do caso com a ressalva "O número de um caso não se repete igual em outro negócio." [FATO, legenda do pb02].

**P21. O que depende só do Bruno (com prazo e minutos [PRIOR])**

| Até | Ação | Min |
|---|---|---|
| hoje, sáb 24/10, depois das 21h | apagar a chamada das 20h30 depois que o Dentista B sair (pendente [FATO, F6]) | 1 |
| dom 25/10 18h30 | desligar as 6 automações (P18) | 6 |
| dom 25/10 18h35 | compartilhar o tl01 com menção e testar a marcação no reel publicado | 3 |
| seg 26/10 | dizer se bruno26111982 é perfil dele | 1 |
| seg 26/10 20h59 | conversa com a Mirna: print da liberação, @, horário de 02/11, ok para publicar antes de 02/11, ok para destaque e para ver tl04 e tl05 | 10 |
| seg 26/10 20h59 | legenda do pb01 | 3 |
| ter 27/10 11h59 | legenda do car01 | 3 |
| qua 28/10 20h29 | apagar o story de 28/10 20h30 | 1 |
| qua 28/10 20h59 | mover o ci01 para seg 02/11 21h | 2 |
| qua 28/10 23h59 | **bloco 1 de gravação** e envio do arquivo original (documento ou Drive) | 31 a 49 |
| qui 29/10 20h59 | legenda do po01 | 3 |
| sex 30/10 20h59 | legenda do pb02 (e TABULEIRO se o pb01 passar de 150) | 3 |
| sáb 31/10 | criar a TABULEIRO de conta toda; trocar a bio para /tabuleiro/?o=ig-bio | 15 |
| dom 01/11 23h59 | cancelar o ci01 só se a família da TV estiver em PARAR | 2 |
| seg 02/11 | 3 stories à mão (horário, "Chegou pela TV?", compartilhar ci01) | 6 |
| toda segunda | 4 números (GA4, WhatsApp, diagnósticos agendados e realizados) | 10 |
| ter 11h de cada semana | executar a lista da rodada (até 3 ações) | 10 a 20 |
| o quanto antes | cópia no Drive de mc02 a mc04, ob01 a ob03 e da fonte da entrevista (958 MB) [FATO, fato 110] | 10 |
| sex 13/11 12h e qui 19/11 12h | ok da Mirna para tl04 e tl05 | 5 |

**P22. Etiquetas**
Todo número deste arquivo leva [FATO] com fonte, [ESTIMATIVA] com a conta, [HIPÓTESE] ou [PRIOR]. O que falta está escrito "sem dado": horário da exibição, @ da Mirna, audiência da TV, alcance em feriado, elegibilidade de Trial Reel, minutos reais do Bruno, números do GA4 e do WhatsApp, preço do serviço, diagnósticos.

---

## 3. Grade de dom 25/10 a dom 22/11

Legenda: **PZ** = já agendado no PostZen [FATO, C1]; **PZ novo** = a agendar no PostZen (pelo Bruno ou pela agência com o ok escrito dele; os agentes do conselho não agendam); **mão** = o Bruno posta no app; **corta** = sai da lista à mão de `05-manuais-bruno.md`; **agentes** = leitura só de leitura.

### 3.1 S1 · dom 25/10 a sáb 31/10 (antes da exibição) · 5 reels e 1 carrossel

| Dia | Hora | Peça | Via | Nota |
|---|---|---|---|---|
| dom 25/10 | 09h00 | story BASTIDOR · SER EMPREENDEDOR | PZ | |
| | 09h01 | story mc02 (NA TV) | PZ | |
| | 09h02 | enquete "Quer saber o que mudou nesse caso?" com "Responde este story" | corta | depende da ETAPAS, que não dispara com "sim" |
| | 12h00 | compartilhar Dentista B + enquete "Você é dentista?" | mão | mede o público do nicho |
| | 12h30 | link do diagnóstico (/tabuleiro/?o=ig-stories) | mão | |
| | 17h30 | story DOM · 18H30 · NO FEED | PZ | |
| | 18h30 | **reel tl01** | PZ | 1º reel com a Mirna; @ na legenda se chegar antes |
| | 18h35 | compartilhar tl01 + menção à Mirna (1ª de 3) e teste de marcação | mão | |
| | 21h00 | Dentista B com 24 h | agentes | |
| seg 26/10 | 09h00 | compartilhar tl01 + enquete | corta | repete a exposição de ontem; o número não decide nada |
| | 12h00 | enquete "Você já pensou isso?" | mão | |
| | 12h01 | A VIRADA | PZ | |
| | 17h30 e 17h31 | mc03 e NA TV · A EQUIPE EXECUTA | PZ | |
| | 17h32 | link do diagnóstico | mão | |
| | 20h30 | SEG · 21H · NO FEED | PZ | |
| | 21h00 | **reel pb01** | PZ | legenda com a data até 20h59 |
| | 21h05 | compartilhar pb01; marcar a Mirna | mão | |
| | 21h05 | portão extra: Dentista B com 48 h | agentes | decide C, TABULEIRO no próximo de nicho, status da família Bruno para a câmera (n de 5) |
| ter 27/10 | 09h00 | compartilhar pb01 + enquete | corta | |
| | 12h00 | **carrossel car01** | PZ | legenda até 11h59; marcar a Mirna na capa |
| | 14h30 | enquete "O seu consultório vive de indicação?" | mão | |
| | 14h31 a 14h33 | NA TV · VAI AO AR SEG, 02/11; A VIRADA; CONTEI NA TV | PZ | |
| | 16h00 | story pf01 (versão "em dois meses") | PZ | |
| | 16h01 | link do diagnóstico | mão | |
| | 18h35 | portão do tl01 (48 h) | agentes | decide o tl02 (P7) |
| qua 28/10 | 09h00 | compartilhar car01 | corta | |
| | 12h00 | enquete "Já pagou por promessa que não veio?" | mão | |
| | 12h01 | A VIRADA | PZ | |
| | 17h30 a 17h32 | NA TV · TV CÂMARA CAMPINAS; NA TV; CRITÉRIO | PZ | |
| | 17h33 | link do diagnóstico | mão | |
| | 20h30 | QUA · 21H · NO FEED | **apagar** | o ci01 sai do dia |
| | 21h00 | sem reel | | ci01 movido para seg 02/11 até 20h59 |
| | 21h00 | pb01 com 48 h | agentes | 150 ou mais abre TABULEIRO no pb02 |
| | 21h05 | compartilhar ci01 | corta | |
| | 23h59 | **prazo do bloco 1 de gravação** | Bruno | |
| qui 29/10 | 09h00 | compartilhar ci01 + enquete | corta | a enquete "Concorda com o que eu disse na TV?" vai para ter 03/11 |
| | 12h00 | enquete "Já aconteceu com você?" | mão | |
| | 12h01 | A VIRADA | PZ | |
| | 17h30 e 17h31 | NA TV · VAI AO AR SEG, 02/11; MÉTODO XEQUE-MATE | PZ | |
| | 17h32 | link do diagnóstico | mão | |
| | 20h30 | QUI · 21H · NO FEED | PZ | |
| | 21h00 | **reel po01** | PZ | legenda "Comenta qual delas." até 20h59 |
| | 21h05 | compartilhar po01; marcar a Mirna | mão | |
| sex 30/10 | 09h00 | compartilhar po01 + enquete | corta | |
| | 12h00 | enquete "Já travou nessa pergunta?" | mão | |
| | 12h01 | A VIRADA | PZ | |
| | 12h02 | link do diagnóstico | mão | |
| | 17h30 e 17h31 | ALINHAMENTO; DIAGNÓSTICO · 30 MIN | PZ | |
| | 20h30 | SEX · 21H · NO FEED | PZ | |
| | 21h00 | **reel pb02** | PZ | legenda até 20h59 |
| | 21h05 | compartilhar pb02; marcar a Mirna | mão | |
| | 23h59 | S2 agendada; car02 e car03 prontos; folha dos ob com nota | agência e Bruno | prazo D3 |
| sáb 31/10 | 09h00 | compartilhar pb02 + enquete | corta | |
| | 11h00 a 12h02 | NA TV; O QUE EU MAIS OUÇO; A VIRADA; NA TV · TV CÂMARA CAMPINAS | PZ | |
| | 12h03 | link do diagnóstico | mão | |
| | 17h30 | SÁB · 18H30 · NO FEED | PZ | |
| | 18h30 | **reel tl02** | PZ | se o portão de 27/10 deixar |
| | 18h35 | compartilhar tl02; marcar a Mirna | mão | |
| | 19h30 | enquete TEMPO / MEDO DE ERRAR EM PÚBLICO | mão | |
| | 21h00 | po01 com 48 h | agentes | |

À mão na S1: 19 (3, 3, 2, 2, 3, 3, 3), contra 27 no `05-manuais-bruno.md` [FATO, C3]. Cortados: 8, todos compartilhamentos do dia anterior com enquete ou o compartilhamento de um reel que não sai.

### 3.2 S2 · dom 01/11 a sáb 07/11 (semana da exibição) · até 5 reels e 2 carrosséis

| Dia | Hora | Peça | Via | Nota |
|---|---|---|---|---|
| dom 01/11 | 09h00 | mc04 (4,6 s) | PZ novo | depois do tl02 |
| | 09h01 | vídeo curto de 02/11 (se gravado) ou estático "NA TV · SEG, 02/11 · FALTA 1 DIA" | PZ novo | |
| | 12h00 | **carrossel car02** (CARROSSEL 02 da TV, capa com o Bruno) | PZ novo | linha 2: "A entrevista vai ao ar amanhã, 02/11." |
| | 12h01 | enquete da O12 (vou fazer um curso) | mão | |
| | 12h02 e 12h03 | virada e prova da O12 | PZ novo | |
| | 12h04 | link do diagnóstico | mão | |
| | 17h30 | frase "Lançamento é xadrez. A maioria joga dama." (estático 3, pronto) | PZ novo | |
| | 21h00 | pb02 com 48 h | agentes | |
| | 21h05 | portão da família da TV (pb01, po01, pb02) | agentes | decide o ci01 |
| | 23h59 | cancelar o ci01 se a família estiver em PARAR | Bruno | |
| seg 02/11 Finados, exibição | 09h00 | estático "SEG · 02/11 · NA TV CÂMARA CAMPINAS" com programa, repórter e canais; vídeo curto se existir | PZ novo | sem hora, sem "ao vivo" |
| | ao confirmar o horário | story com a hora, menção à Mirna (2ª) e link para /ao-vivo | mão | se a hora já passou, pula |
| | 12h00 | se o horário seguir sem dado: link para /programacao | mão | exclusivo com o anterior |
| | 17h30 | frase "Eu sou estrategista de marketing digital e lançamento de um produto." (literal, M11) | PZ novo | |
| | depois do horário | "Chegou pela TV Câmara? Me manda um oi no direct e conta a sua área." | mão | única atribuição da TV |
| | 18h30 | tl02 com 48 h | agentes | |
| | 19h00 | Módulo 7 (S1) | agentes | `semanas/2026-11-02.md`; lista do Bruno até ter 03/11 11h |
| | 20h30 | SEG · 21H · NO FEED | PZ novo | |
| | 21h00 | **reel ci01** (versão A da legenda) | PZ (movido) | colaboração só com @ e ok |
| | 21h05 | compartilhar ci01 + menção (3ª) | mão | |
| ter 03/11 | 09h00 | trecho "O QUE EU DISSE NA TV" (10 a 15 s, Bruno em cena) | PZ novo | |
| | 11h00 | prazo da lista da rodada de 02/11 | Bruno | |
| | 12h00 | **carrossel car03** (Os 5 Lances) | PZ novo | |
| | 12h01 | enquete da O14 ("TV de Câmara não prova nada"); a enquete "Concorda com o que eu disse na TV?" fica de fora para não somar um pedido | mão | |
| | 12h02 e 12h03 | virada e prova da O14 | PZ novo | |
| | 14h00 | **R1 Trial Reel** | PZ novo com `trialParams`, ou mão | 17 h depois do ci01 |
| | 17h30 | frase "As pessoas me contratavam para resolver problemas nas empresas delas." | PZ novo | |
| | quando a edição subir | "A entrevista inteira está aqui" + link + resultado da votação do tl01 | mão | cumpre a promessa do tl01 |
| qua 04/11 | 09h00 | trecho da TV | PZ novo | |
| | 12h00 a 12h03 | O9 (meu problema é tráfego): enquete (mão), virada e prova (PZ novo), link (mão) | | |
| | 17h30 | frase "O lead que não comprou vale mais do que o que comprou." (estático 4) | PZ novo | |
| | 20h30 | chamada do reel | PZ novo | |
| | 21h00 | **reel: nicho 1 consórcio** se o bloco 1 chegou; senão ob01; senão vazio | PZ novo | |
| | durante o dia | leitura parcial de diagnóstico do brief | Bruno informa | |
| qui 05/11 | 09h00 | trecho da TV | PZ novo | |
| | 12h00 a 12h03 | O11 (não sei se compraria) | | |
| | 17h30 | frase "Os clientes chegam pra gente machucados." (M9) | PZ novo | |
| | 20h30 e 21h00 | chamada e **reel ob01** se a família da TV não estiver em PARAR; senão nicho 2; senão vazio | PZ novo | |
| | durante o dia | visitas ao perfil de 02 a 04/11 | agentes | atraso de até 48 h |
| sex 06/11 | 09h00 | trecho da TV | PZ novo | |
| | 12h00 a 12h03 | O13 (vendo serviço, não curso) | | |
| | 17h30 | frase "Saber convencer as pessoas quebrando a objeção delas." (M5) | PZ novo | |
| | 20h30 e 21h00 | chamada e **reel nicho 2 nutricionista**; senão ob03; senão Dentista C (se o B passou); senão vazio | PZ novo | |
| | 23h59 | car04 e car05 prontos | agência | |
| sáb 07/11 | 09h00 | trecho da TV | PZ novo | |
| | 12h00 | caixa "Qual a sua maior dúvida antes de chamar um estrategista?" | mão | |
| | 12h03 | link do diagnóstico | mão | |
| | 17h30 | SÁB · 18H30 · NO FEED | PZ novo | |
| | 18h30 | **reel tl03** | PZ | portão de 02/11; marcar a Mirna |
| | 18h35 | compartilhar tl03 | mão, opcional | |

### 3.3 S3 · dom 08/11 a sáb 14/11 · até 5 reels e 2 carrosséis

| Dia | Hora | Peça | Via | Nota |
|---|---|---|---|---|
| dom 08/11 | 09h00 | trecho da TV | PZ novo | |
| | 12h00 | **carrossel car04** (CARROSSEL 03 da TV) | PZ novo | |
| | 12h01 | enquete da O15 (meu público é local), só enquete | mão | sem virada até o Bruno dizer onde foram os casos |
| | 12h03 | link | mão | |
| | 17h30 | frase "Mais verba numa ordem errada só acelera o erro." | PZ novo | |
| seg 09/11 | 09h00 a 12h03 | trecho; objeção com mais SIM na S1 (rodízio) | PZ novo e mão | |
| | 17h30 | frase do nicho do dia (psicólogo: "Psicólogo com fila de espera tem um produto pronto e não percebeu.") | PZ novo | |
| | 19h00 | Módulo 7 (S2; tl03 com 48h30) | agentes | |
| | 20h30 e 21h00 | chamada e **reel: nicho 3 psicólogo** (bloco 2); senão "mais votado inteiro" com 5 votos ou mais; senão ob02; senão vazio | PZ novo | último reel que conta para 11/11 |
| ter 10/11 | 12h00 | **carrossel car05** (Oferta em 5 pilares) | PZ novo | |
| | 12h01 a 12h03 | O7 só se as resoluções dos conselhos estiverem lidas; senão rodízio | | |
| | 14h00 | R2 Trial Reel, só se o R1 fez 42 ou mais | PZ novo ou mão | |
| | 17h30 | frase "Curso te dá o mapa. A partida precisa de quem comande." | PZ novo | |
| qua 11/11 | 12h01 a 12h03 | O10 só se o Bruno confirmar cliente, ano e papel; senão rodízio | | |
| | 17h30 | frase "Cada cliente tem um produto específico e a gente vive esse produto." (M3) | PZ novo | |
| | 21h00 | **reel: ob02 ou ob03** (família da TV em MANTER ou DOBRAR); senão nicho; senão Dentista C; senão vazio | PZ novo | |
| | 21h05 | conferência de nicho (brief) | agentes | mediana dos 3 abaixo de 53 ou pulo mediano acima de 75%: o nicho para |
| | 21h05 | saldo de seguidores de 25/10 a 08/11 fecha | agentes | |
| qui 12/11 | 12h01 a 12h03 | 1ª objeção com mais SIM | | |
| | 21h00 | **reel: nicho 4** (se 11/11 aprovou); Bruno para a câmera fora de nicho (se reprovou); senão vazio | PZ novo | |
| sex 13/11 | 12h00 | prazo do ok da Mirna para o tl04 | Bruno | sem resposta: cancelar o tl04 até 23h59 |
| | 12h01 a 12h03 | 2ª objeção com mais SIM | | |
| | 21h00 | **reel: Dentista C** (uma vez, se o B passou) ou ob restante; senão vazio | PZ novo | |
| | durante o dia | ganho líquido de 28/10 a 10/11 fecha | agentes | piso do brief: 12 |
| | 23h59 | bloco 3 de gravação; car06 e car07 prontos | Bruno e agência | |
| sáb 14/11 | 12h00 | caixa de pergunta | mão | |
| | 18h30 | **reel tl04** | PZ | portão de 09/11 e ok da Mirna |

### 3.4 S4 · dom 15/11 a sáb 21/11 · até 5 reels e 2 carrosséis · e dom 22/11

| Dia | Hora | Peça | Via | Nota |
|---|---|---|---|---|
| dom 15/11 Proclamação | 09h00 | trecho da TV | PZ novo | sem bloco à mão (feriado) |
| | 12h00 | **carrossel car06** (CARROSSEL 04 da TV) | PZ novo | |
| | 17h30 | frase (rodízio das 3 com menor saída, 14 dias ou mais entre voltas [PRIOR, F6]) | PZ novo | |
| seg 16/11 | 12h00 a 12h03 | rodízio das 3 objeções com mais votos | mão e PZ novo | |
| | 19h00 | Módulo 7 (S3) | agentes | |
| | 21h00 | **reel: nicho 5** (bloco 3) ou Bruno fora de nicho; senão vazio | PZ novo | |
| ter 17/11 | 12h00 | **carrossel car07** (Seguidor x comprador, versão nova) | PZ novo | |
| | 14h00 | R3 Trial Reel, só se o R2 fez 42 ou mais | PZ novo ou mão | |
| qua 18/11 | 21h00 | **reel: nicho 6**; senão ob restante; senão vazio | PZ novo | |
| | durante o dia | conferências do brief: seguidores (12 em 14 dias depois de 27/10) e diagnóstico (0 agendado = troca a porta) | agentes e Bruno | |
| | 23h59 | bloco 4 de gravação (para a S5) | Bruno | |
| qui 19/11 | 12h00 | prazo do ok da Mirna para o tl05 | Bruno | sem resposta: cancelar o tl05 até 23h59 |
| | 21h00 | **reel** da ordem sem gravação ou nicho | PZ novo | |
| sex 20/11 Consciência Negra | 09h00 e 17h30 | trecho e frase | PZ novo | sem bloco à mão |
| | 21h00 | **reel** só se houver peça aprovada até qua 18/11 | PZ novo | |
| sáb 21/11 | 12h00 | caixa de pergunta | mão | |
| | 18h30 | **reel tl05** | PZ | portão de 16/11 e ok da Mirna |
| dom 22/11 | 09h00 e 17h30 | trecho e frase | PZ novo | sem feed: a S5 sai do portão de seg 23/11 19h |

---

## 4. Decisões

### D1. Série da entrevista em torno de 02/11

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) Manter os 5 nas datas | zero edição; S1 com 6 reels; 02/11 sem feed | semana da TV sem peça nova; ci01 com voz e rosto da Mirna no ar 5 dias antes da exibição, com ok verbal |
| (b) Mover os 5 para depois | 5 reels e 5 stories agendados a mexer (26/10 20h30, 28/10 20h30, 29/10 17h30 e 20h30, 30/10 20h30 [FATO, C2]) mais os manuais; S1 com 2 reels | S2 e S3 com 10 peças de um formato nunca medido em 2 semanas, acima de 5 por semana; a sobra empurra para a S4 |
| (c) Mover ci01 e po01 (F4) | 2 reels e 3 stories agendados a mexer; S1 com 4 reels e a vaga de qui 29/10 sem peça com rosto | a própria F4 prevê que o po01 fica se a vaga não tiver peça; na prática converge para (d) com mais edições |
| **(d) Mover só o ci01; decisão final dele em dom 01/11 21h05 pela família da TV com n de 3** | 1 reel movido, 1 story apagado, 3 manuais cortados; S1 = 5 | o "depois" fica com ci01, ob e nicho; o assunto 7 (po01) sai antes da exibição; o portão impede gastar ci01 e ob num formato que falhar |
| (e) Fora do óbvio: ci01 em ter 03/11 21h com "foi ao ar ontem" e 02/11 só em stories | nenhuma troca de legenda no feriado; o texto pode dizer "foi ao ar" se o horário vier | o dia da TV fica sem feed; terça com 2 posts de feed (car03 e ci01); quebra a grade de reel |

- **Premissas:** (1) o corte da TV de perfil em 3/4 nunca foi medido nesta conta [FATO, fato 88]; (2) a TV tende a trazer pouco tráfego: edições do programa no site com mediana de 80,5 views [FATO, fato 136]; audiência da TV sem dado; (3) cada edição no PostZen é uma chance de falha de execução, e a base de execução é fraca (3 de 8 decisões de 21/10 não executadas [FATO, fato 125]); (4) o Bruno autorizou publicar ("pode seguir pois as postagens vou marcar ela" [FATO, fato 1]); (5) a versão A da legenda do ci01 vale sem horário confirmado [FATO, F4].
- **Posição:** (d). A (e) perde para a (d) porque a versão A já tira o feriado do caminho e a (e) deixa o dia da exibição sem feed.
- **Probabilidade de sucesso pelo critério do enquadramento** (média de 42 ou mais com pulo até 75% em cada fase, 21 ou mais visitas por dia de 02 a 04/11, saldo de seguidores positivo de 25/10 a 08/11, mais as condições de texto e marcação): **0,10, faixa [0,04, 0,22]**. Peso maior no alvo de visitas, que é 2x a base de 10,6 [ESTIMATIVA] num feriado com TV de audiência sem dado. **Confiança: 0,4.**

### D2. Gravação, Dentista C e remakes

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 1 bloco por semana com 2 roteiros, o 1º com 3 e o REACT (F5) | 24 a 36 min por semana; 43 a 67 no 1º | REACT gasta 20 min num formato (TV) sem medida |
| (b) 1 sessão de 60 a 90 min com 5 roteiros | 5 reels de nicho por semana | o plano de 21/10 já previa isso e veio 1 fala de 36 s em 3 dias [FATO, fatos 104 e 105]: alto risco de não acontecer e de travar o resto |
| (c) Sessão quinzenal com 10 roteiros | 2 sessões no período | a 1ª sessão chega tarde para 11/11; 10 roteiros numa sessão ampliam a chance de cansaço na câmera [PRIOR] |
| (d) Zero gravação | 0 min | 11/11 "não testado"; feed só com perfil 3/4 e 3 remakes em 720p |
| **(e) Bloco 1 obrigatório (2 roteiros + vídeo de 02/11, 31 a 49 min); depois piso 1 e meta 2** | n de 3 em 11/11; S2 com 2 reels do formato medido | a conta de vagas fecha com estoque e não com pressa; o REACT só entra se a família da TV fizer DOBRAR |
| (f) Fora do óbvio: gravação financiada por resultado depois de 11/11 | reel de nicho com 106 ou mais compra o 2º roteiro da semana seguinte; abaixo de 42, só o piso | o minuto do Bruno segue o retorno medido, semana a semana |

- Dentista C: reserva de custo zero, uma vez, a partir de sex 06/11, só com o B em 42 ou mais e pulo até 75%. Remakes: R1 em ter 03/11 14h; R2 e R3 condicionados ao anterior.
- **Premissas:** (1) o formato do Bruno para a câmera mantém a vantagem com assunto novo [HIPÓTESE, palpites 15 e 16]; (2) 12 a 18 min por roteiro [ESTIMATIVA, F5; medida real sem dado]; (3) as travas de leitura (ABAC, CFN 856) não bloqueiam a gravação porque o bloco grava as duas versões [FATO, F5].
- **Posição:** (e), com (f) a partir de 11/11.
- **Probabilidade pelo critério** (2 reels de nicho por semana com gravação, mediana de 53 ou mais e pulo até 75% em 11/11 com n de 3, 0 animação, 0 reel sem o Bruno, C e remakes só com condição): **0,20, faixa [0,10, 0,35]**. A parte de desempenho é provável (o formato fez 128 a 308 [FATO, fato 25]); a parte de execução (2 por semana por 3 semanas) é a fraca. **Confiança: 0,45.**

### D3. Grade, ritmo e trabalho à mão

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 5 reels e 2 carrosséis fixos | vaga sempre cheia | vaga cheia com formato em PARAR quando faltar peça boa: o erro da série 2 (8 posts em 3 dias, 0 seguidor [FATO, fato 44]) |
| (b) 6 reels na S1 pela promessa | resolvido: a promessa mudou | sem motivo hoje |
| (c) 6 a 7 por semana com portão | +1 reel por semana | ganho medido do volume é de 1 ponto (7,0% contra 6,0% de estouro [FATO, fato 152]) e cada reel extra gasta estoque com rosto |
| (d) 3 reels e 2 carrosséis em semana sem gravação | menos carga | trava a grade antes de ver o portão |
| **(e) 5 e 2 como teto; vaga vazia com motivo; nenhum 6º reel; carrossel só com foto do Bruno; à mão no máximo 3 por dia** | S1 = 5 e 1; S2 a S4 conforme o portão | menos alcance bruto nas semanas fracas e menos atenção gasta em formato fraco; o custo de não agir vira linha do portão |
| (f) Fora do óbvio: grade por orçamento de minutos | toda sexta o Bruno declara os minutos da semana seguinte e a grade se ajusta | casa a grade com a capacidade real; pede disciplina de declarar |

- **Premissas:** (1) o volume não explica o resultado tanto quanto o formato (5,2x entre formatos [FATO, fato 21 derivado]); (2) hora fixa por formato, sem teste de hora (hora não separou nada dentro do formato [FATO, fato 40]); (3) carrossel com foto do Bruno segura (111 de mediana, n 7 [FATO, fato 51]).
- **Posição:** (e), com o orçamento de minutos de (f) como linha do arquivo da semana.
- **Probabilidade pelo critério** (0 vaga vazia, 0 dia com 2 reels, mediana semanal de 42 ou mais nas 4 semanas e de 106 ou mais em 2, ganho líquido de 12 ou mais): **0,08, faixa [0,03, 0,18]**. Minha posição aceita vaga vazia, então o critério "0 vaga vazia" falha por desenho se faltar peça aprovada; registro a discordância: esse critério gera desperdício. **Confiança: 0,5.**

### D4. Stories e ob01 a ob03

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 03-plano estendido (8 por dia, 27 à mão por semana) | máxima presença | 27 a 54 min por semana do Bruno [PRIOR] só em stories; as segundas enquetes do dia não decidem nada |
| (b) 3 a 5 por dia | menos carga | perde views de story, hoje 40,8% das views orgânicas de 30 dias [FATO, fato 57] |
| (c) 6 a 8 em 4 blocos (F6) | 20 à mão por semana | bom molde; ainda tem compartilhamentos sem número |
| **(e) agendado livre até 6 por dia; à mão só onde o sticker gera número usado numa decisão (enquete de objeção, link, caixa semanal, 3 menções); compartilhamento opcional; ob no feed só com a família da TV fora de PARAR** | S1: 19 à mão; depois cerca de 14 por semana | menos minuto, a mesma medição de objeção; views de story podem cair um pouco nos dias sem compartilhamento [HIPÓTESE] |
| (f) Fora do óbvio: destaque NA TV montado uma vez no lugar da contagem diária como ativo de prova | 1 montagem do Bruno (5 a 10 min [PRIOR]) | ativo permanente para quem chega pela TV; troca o texto com data em 03/11 |

- ob01 a ob03: renders existem [FATO, C4]; ob01 qui 05/11, ob03 sex 06/11 (se o nicho 2 não estiver pronto), ob02 qua 11/11.
- **Premissas:** (1) story agendado e story à mão alcançam o mesmo; a diferença é o sticker [FATO, fatos 58 e 66]; (2) a frequência de objeção é sem dado e a enquete é o único instrumento [FATO, F6]; (3) os ob são família da TV, formato sem medida [FATO, C5].
- **Posição:** (e) com (f) a partir de ter 03/11 (sem texto com data).
- **Probabilidade pelo critério** (982 views de story ou mais por semana, 6 respostas ou mais a cada 14 dias, ob com média de 42 ou mais e pulo até 75%): **0,20, faixa [0,10, 0,35]**. Views: provável (7 dias com 1.041 já na base [FATO, fato 56]); respostas: meio a meio; ob: sem dado. **Confiança: 0,4.**

### D5. Portão do Módulo 7

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) Régua de 53 de alcance | limites fixos 27, 42, 106, 150 | compara semanas |
| (b) 57 views | régua do Buzzfy | mistura views com alcance e o múltiplo anda com a base |
| (c) 37,5 de alcance | base atual | a base tem 12 de 20 reels de animação [FATO, F7]: sobe sozinha e muda a decisão no meio |
| (d) Mediana móvel | acompanha a conta | quebra S4 contra S1 |
| **(e) (a) + "pausar" com n de 1 + no máximo 3 ações do Bruno por rodada + colunas de custo e de custo de não agir** | 5 rodadas registradas e decisões que cabem no tempo do Bruno | adaptação mais lenta (fila de ações), execução maior [HIPÓTESE] |
| (f) Fora do óbvio: régua por minuto do Bruno | alcance em 48 h dividido pelos minutos gastos na peça | põe o caixa dentro do portão; minutos reais são sem dado até a S1 |

- **Premissas:** (1) a execução é o gargalo (base de 21/10: 4 sim, 1 em parte, 3 não, em 8 [FATO, fato 125]); (2) n de 2 por formato antes de PARAR [FATO, enquadramento]; (3) o Buzzfy revisa números com mais de 48 h [FATO, fato 33].
- **Posição:** (e), com (f) como coluna de referência.
- **Probabilidade pelo critério** (5 rodadas registradas, todas as decisões executadas até a segunda seguinte, nenhum PARAR com n de 1, mediana da S4 acima da S1): **0,25, faixa [0,12, 0,40]**. A parte "todas executadas" é a mais fraca. **Confiança: 0,5.**

### D6. TABULEIRO e caminho até o diagnóstico

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) TABULEIRO em todo post de novembro com 150 | mais pedidos | fere o "um por semana" do Módulo 1 [FATO, fato 171] |
| (b) Um post só no mês | leitura estrita | teto ainda menor que 3,7 a 5,5 comentários |
| (c) (a) ou (b) + revisão das 6 automações de conta toda + um pedido por peça | menos colisão | pede minutos do Bruno uma vez |
| (d) Não ligar até 1 disparo real e caminho testado | nada a medir em novembro | o mês passa sem disparo possível |
| **(e) (c) com uma TABULEIRO de conta toda genérica a partir de 01/11, no máximo 1 pedido por semana, mais bio /tabuleiro/?o=ig-bio e os 4 números** | 6 automações desligadas; bio que leva ao teste | dá para separar "Fiz O Tabuleiro" de "Quero agendar o Primeiro Lance" no WhatsApp; a origem por canal segue sem dado [FATO, fato 129] |
| (f) Fora do óbvio: pagar o fundo antes do topo | nenhuma palavra nova até o caminho bio, teste e WhatsApp ter 2 semanas de números do Bruno | mede a conversão antes de pedir mais comentário; adia a TABULEIRO de novembro para depois de 08/11 |

- **Premissas:** (1) o teto é de 3,7 a 5,5 comentários de qualquer tipo até 22/11 [ESTIMATIVA, F8]; (2) "tabuleiro" não aparece em comentário comum [HIPÓTESE, palpite 50]; (3) o Bruno informa os números (sem eles, "sem dado").
- **Posição:** (e). A (f) vira regra se o Bruno não informar os números das segundas 26/10 e 02/11: aí a TABULEIRO de conta toda não é criada e o minuto vai para a bio.
- **Probabilidade pelo critério** (3 disparos de terceiros até 22/11 e 1 diagnóstico agendado até 18/11): **0,10, faixa [0,03, 0,20]**. O brief de 21/10 dá 0,2 só para o diagnóstico [FATO, fato 169]; somado aos 3 disparos, cai. **Confiança: 0,5.**

---

## 5. Ideias e hipóteses numeradas (88)

| # | Ideia ou hipótese | Confiança | Evidência |
|---|---|---|---|
| 1 | Tratar o minuto do Bruno como o caixa do plano e escrever o orçamento semanal no arquivo da semana | alta | carga da F5 de 170 a 327 min [ESTIMATIVA com PRIOR]; 1 fala de 36 s em 3 dias [FATO, fato 104] |
| 2 | Reescrever a linha de respostas da F5 (105 a 210 min por semana) para 10 a 30 min | alta | 2 comentários e 3 respostas em 7 dias [FATO, fato 15]; minutos por resposta [PRIOR] |
| 3 | Mover só o ci01 resolve a regra de 5 reels da S1 e enche o dia da exibição com uma edição | alta | S1 com 6 reels e nada de 01 a 06/11 [FATO, C1] |
| 4 | Manter o po01 em 29/10: o ganho de mover é hipótese sem fato perto | média | palpite 40 do livro de fatos |
| 5 | Decidir o ci01 em dom 01/11 21h05, com a família da TV em n de 3, e não no feriado | alta | horas de 48 h de pb01, po01 e pb02 [FATO, derivação 7] |
| 6 | Toda ação do Bruno que cairia em 02/11 vai para dom 01/11 ou ter 03/11 | alta | 02/11 é Finados [FATO, fato 3]; disponibilidade do Bruno sem dado |
| 7 | Cortar os 8 compartilhamentos com enquete das 09h00 e os de reel que não sai | média | 05-manuais-bruno [FATO, C3]; o número do compartilhamento não é lido por nenhuma ferramenta [FATO, fato 67] |
| 8 | Uma enquete por dia, sempre no story de objeção | média | F6, seção 4.2 |
| 9 | Link do diagnóstico 1 por dia na S1 e S2; na S3, 3 por semana se a soma de toques for menor que 2 | baixa | toques sem dado [FATO, fato 67]; limite [PRIOR] |
| 10 | Story agendado não tem custo de Bruno: manter o volume agendado e cortar só o manual | alta | 28 agendados na S1 [FATO, C1] |
| 11 | Carrossel com foto do Bruno é o melhor retorno por minuto do Bruno no feed | média | mediana 111 e 23 visitas, n 7 [FATO, fato 51]; 0 min de gravação |
| 12 | Nenhum carrossel sem foto do Bruno na capa | alta | texto: 34,5 e 1 visita, n 6 [FATO, fato 51] |
| 13 | S1 fecha com 1 carrossel, com motivo escrito | média | só o car01 pronto [FATO, F5] |
| 14 | Bloco 1 é o único gasto de minuto que não se corta | alta | brief: mediana "dos 3" em 11/11 [FATO, 10-decision-brief linha 123] |
| 15 | Piso de 1 roteiro por semana depois do bloco 1 | média | 12 a 18 min por roteiro [ESTIMATIVA, F5] |
| 16 | Se o nicho for abandonado em 11/11, a gravação segue com 1 roteiro fora de nicho, sem zerar | média | Bruno para a câmera 5,2x a animação [FATO, fato 25 e 27] |
| 17 | Pedir o arquivo original como documento ou Drive | média | raw de 576x1024 [FATO, fato 104]; compressão [HIPÓTESE, palpite 52] |
| 18 | R1 primeiro; R2 e R3 só se o anterior fizer 42 ou mais | média | 35% contra 15% pelo playbook [FATO, fato 150] |
| 19 | R1 pelo PostZen com `trialParams`; se falhar, uma tentativa pelo app | média | `trialParams` existe e falha só na publicação [FATO, fato 139] |
| 20 | Dentista C como reserva de custo zero, usado uma vez, depois da leitura do B | média | pronto, selfie no quadro 0 [FATO, fato 101] |
| 21 | Case Tzur fora das 4 semanas | alta | autorização sem dado e CTA que dispara ESTRATEGISTA [FATO, fato 102] |
| 22 | pf01 segue só como story | média | regra de DOBRAR de profissão [FATO, fato 173] |
| 23 | ob02 no feed só enquanto o pf01 não virar reel | média | 82% do mesmo áudio [ESTIMATIVA, F2] |
| 24 | ob01 a ob03 entram só com a família da TV fora de PARAR | alta | renders prontos [FATO, C4] |
| 25 | Os ob são TESTAR da família da TV, não DOBRAR do Bruno | alta | Bruno de perfil atrás do monitor [FATO, C5] |
| 26 | Cumprir o "inteiro" do tl01 com o link da edição | média | compartilhar link é livre [FATO, fato 137] |
| 27 | Com menos de 5 votos, dizer nos stories que segue o plano | alta | regra do catálogo [FATO, fato 170] |
| 28 | Cancelar timelapse até sex 23h59 anterior | alta | F7, seção 5.3 |
| 29 | tl04 e tl05 só com a Mirna vendo antes os efeitos no rosto dela | média | fichas [FATO, fato 90]; risco de relação [HIPÓTESE, palpite 37] |
| 30 | Nenhum convite de colaboração antes do print e do @ | média | `collaborators` pede @ [FATO, fato 139] |
| 31 | Nada de destaque permanente com a Mirna antes do ok escrito | média | liberação verbal [FATO, fato 4] |
| 32 | Nenhum impulsionamento até 18/11; conteúdo da TV nunca em anúncio sem autorização escrita | alta | brief D4 [FATO, fato 169]; termos [FATO, fato 137] |
| 33 | Desligar as 5 automações de conta toda e a ETAPAS de story antes do tl01 | alta | colisão com "caso" e "estrategista" [FATO, fato 114] |
| 34 | Manter as 10 automações presas a posts antigos | média | 0 comentário nesses posts [FATO, F8] |
| 35 | Bio para /tabuleiro/?o=ig-bio antes de dom 01/11 | média | Módulo 2 aprovou e não foi aplicado [FATO, fato 132] |
| 36 | "Diagnóstico" conta só a conversa de 30 min | alta | duas coisas com o mesmo nome [FATO, fato 131] |
| 37 | Os 4 números de segunda são a única forma de calcular CAC | alta | nenhuma ferramenta lê GA4 nem WhatsApp [FATO, fato 143] |
| 38 | A meta de 10 diagnósticos não fecha pela bio | alta | 637 contra 317 visitas [ESTIMATIVA, F8] |
| 39 | Pedir ao Bruno o valor médio de um comando de lançamento, só para a conta interna de payback | média | preço sem dado [FATO, F6] |
| 40 | Régua de 53 fixa de 25/10 a 23/11 | alta | F7, seção 5.1 |
| 41 | Com n de 1, "pausar" e nunca PARAR | média | enquadramento D5 |
| 42 | No máximo 3 ações do Bruno por rodada | média | 3 de 8 não executadas [FATO, fato 125]; efeito [HIPÓTESE] |
| 43 | Coluna de custo (minutos e horas) em cada rodada | média | carga sem medida [FATO, F5] |
| 44 | Tarefa manual com saída zero por 2 semanas cai à metade | baixa | limite [PRIOR] |
| 45 | Leitura de feriado não fecha PARAR sozinha | alta | F7, seção 4.4 |
| 46 | Ouvir 1380,8 a 1382,38 s do ci01 antes de 02/11 | alta | ficha e transcrição divergem [FATO, fato 91] |
| 47 | Abertura do ci01: aceitar por escrito o Bruno de costas até 2,5 s, ou trocar o primeiro quadro se o render custar menos de 1 h | média | quadros [FATO, fato 88]; custo [PRIOR] |
| 48 | Apagar o story de 28/10 20h30 se o ci01 mover | alta | chamada agendada [FATO, C2] |
| 49 | Versão B do ci01 só depois do horário | alta | regra do "foi ao ar" [FATO, fato 6] |
| 50 | Sem horário até 12h de 02/11: link para /programacao | média | grade não publicada [FATO, fato 133] |
| 51 | Vídeo curto de 02/11 gravado no bloco 1 | média | 3 a 5 min [ESTIMATIVA, F5] |
| 52 | Um reel só em 02/11 | média | playbook não mede TV nem feriado [FATO, fato 144] |
| 53 | Nicho gravado vai na frente dos ob na S2 | média | formato medido contra formato sem medida |
| 54 | Nenhum dia com 2 reels; Trial Reel a 6 h | alta | 0,92x a menos de 6 h [FATO, fato 152] |
| 55 | Hora fixa por formato: reel 21h em dia útil, 18h30 no sábado, carrossel 12h ter e dom | média | hora não separa dentro do formato [FATO, fato 40] |
| 56 | Manter a hora nos feriados de 15/11 e 20/11 | baixa | 1 feriado medido, animação [FATO, fato 41] |
| 57 | Teste de marcação no tl01; plano B: @ no texto pelo PostZen | média | `userTags` só em foto [FATO, fato 139] |
| 58 | Sem @ até seg 26/10, a grade não para | média | o Bruno autorizou publicar [FATO, fato 1] |
| 59 | Menção à Mirna em story só 3 vezes | média | F4, seção 6.3 |
| 60 | Escrever "na gravação" ao lado de minuto | alta | minutos do celular [FATO, fato 81] |
| 61 | Lista de vetos mantida inteira depois de 02/11 | alta | 02-provas [FATO, fato 6] |
| 62 | Responder comentário em até 7 dias com link e &p= | média | regra de 7 dias [FATO, fato 120]; `p` aceito [FATO, fato 129] |
| 63 | po01 com "Comenta qual delas." | média | "a palavra" sem palavra [FATO, fato 80] |
| 64 | car01 com um pedido só (direct) | baixa | dois pedidos [FATO, fato 80]; regra S6 da F2 |
| 65 | Cópia no Drive do estoque que só existe na pasta temporária | alta | 958 MB de fonte, refazer custa 3 h 15 min [FATO, fatos 110 e 111] |
| 66 | Não renderizar variações sem vaga aberta (disco com 11 GB livres) | média | `df` [FATO, fato 110] |
| 67 | Consertar o trecho sem voz do tl02 só se custar menos de 1 h | média | 10,4 s sem voz [FATO, fato 92]; custo [PRIOR] |
| 68 | Nenhum 6º reel no período | média | 7,0% contra 6,0% [FATO, fato 152] |
| 69 | Ordem fixa sem gravação: ob, C, mais votado, R1 no feed, banco, vazio | média | estoque [FATO, F5 e C4] |
| 70 | Cortes do banco só com a família da TV em DOBRAR | média | sem ficha, custo de agência [FATO, fato 107] |
| 71 | Vaga vazia aceita quando o candidato está em PARAR | média | série 2: 8 posts, 206 de alcance somado, 0 seguidor [FATO, fato 44] |
| 72 | Pedido de seguir na legenda de 02 a 04/11 | média | 1,12x [FATO, fato 148]; chegada pela TV [HIPÓTESE, palpite 31] |
| 73 | Nenhuma palavra-chave em 02/11 | alta | Módulo 1 [FATO, fato 171] |
| 74 | Uma TABULEIRO de conta toda genérica a partir de 01/11 | média | texto atual de dentista [FATO, fato 117] |
| 75 | Pulo abaixo de 60% como reforço do portão da TABULEIRO fica registrado como hipótese | baixa | n de 1 de cada lado [FATO, fato 122] |
| 76 | Contar disparos pela diferença do log entre segundas | alta | log sem data [FATO, fato 119] |
| 77 | Confirmar se bruno26111982 é o Bruno | alta | único disparo [FATO, fato 116] |
| 78 | Ler visitas de 02 a 04/11 em 05 e 06/11 | média | atraso de até 48 h [FATO, fato 140] |
| 79 | Não declarar saldo de seguidores até 08/11 antes de 11/11 | alta | derivação 5 do livro |
| 80 | Critério secundário de views da edição: acima de 80,5, e não 124 | média | fatos 136 e 178 |
| 81 | Piso de seguidores: 12 em 28/10 a 10/11, lido em 13/11, decidido em 18/11 | alta | fato 182 |
| 82 | O pf01 do PostZen já é a versão "em dois meses": a dúvida de versão fechou | alta | `listPosts` 18h03 [FATO, C1] |
| 83 | mc04 de 4,6 s já renderizado é o recorte que vale | alta | mc04.spec.json [FATO, C6] |
| 84 | Linha "custo de não agir" em cada rodada | média | compensação do ponto cego |
| 85 | Nenhum agente agenda: toda mudança vira lista com prazo e minutos | alta | regra do cliente |
| 86 | Antes de gasto novo de agência, conferir se há vaga aberta pelo portão | média | regra de caixa |
| 87 | Não planejar a S2 como pico de tráfego | média | mediana de 80,5 views por edição [FATO, fato 136]; audiência sem dado |
| 88 | Destaque NA TV é o ativo de maior vida útil da série | média | destaque fica até ser removido [FATO, fato 68]; efeito [HIPÓTESE] |

---

## 6. Pre-mortem da cadeira M: como este plano fracassa

| # | Como fracassa | Sinal cedo | O que fazer |
|---|---|---|---|
| 1 | O bloco 1 não chega até qua 28/10; a S2 roda com ob e vaga vazia; 11/11 vira "não testado"; o plano é lembrado como econômico demais | nenhum arquivo novo na pasta de trabalho até qui 29/10 09h | piso de 1 roteiro (12 a 18 min) até sex 30/10 23h59; o vídeo de 02/11 pode ser gravado sozinho em 3 a 5 min |
| 2 | Gating demais: S2 a S4 com 2 ou 3 reels por semana, alcance da conta cai abaixo de 571 contas em 7 dias, saldo de seguidores negativo | 2 vagas vazias seguidas | liberar o Dentista C e o R1 no feed antes de deixar a 3ª vaga vazia |
| 3 | O corte de stories à mão derruba as views de story abaixo de 982 por 2 semanas | `ig_account_stats` de 7 dias em 09/11 | devolver o compartilhamento do reel do dia |
| 4 | A família da TV fica em PARAR e o estoque pronto (ci01, ob) vira banco: o dinheiro já gasto em agência vira custo afundado | mediana de pb01, po01 e pb02 abaixo de 42 em dom 01/11 | aceitar o custo afundado; não gastar mais agência na família |
| 5 | A Mirna não responde e tl04 e tl05 caem; S3 e S4 perdem o sábado | sem resposta até seg 09/11 | sábado com o Bruno para a câmera, se houver bloco |
| 6 | Trial Reel não é elegível e o R1 não sai | falha na publicação de ter 03/11 | uma tentativa pelo app e fim; R2 e R3 não são feitos |
| 7 | Os 4 números não chegam e o CAC fica sem dado em 18/11 | segunda 26/10 sem número | aplicar a opção (f) da D6: nenhuma automação nova, minuto vai para a bio |
| 8 | Os minutos de PRIOR estão errados por 2x e o teto de 90 por semana estoura | linha "feito" da S1 abaixo de 60% | cortar na ordem: compartilhamento, link diário, marcação em plano aberto, enquete diária |
| 9 | A TV traz tráfego muito acima do esperado e a semana fica com pouca peça nova | visitas por dia de 02 a 04/11 acima de 21 | ob01 e ob03 sobem para qua e qui; R1 vai ao feed |
| 10 | Uma edição no PostZen esquecida publica chamada para reel que não existe (28/10 20h30) | story no ar sem reel | apagar no app; regra de conferir a lista toda terça 11h |

---

## 7. Previsões numéricas com data de conferência

D = sáb 24/10/2026. D+30 = seg 23/11/2026; D+60 = qua 23/12/2026; D+90 = sex 22/01/2027. Todas [ESTIMATIVA] com a premissa ao lado.

| Métrica | Valor e faixa | Conferência | Premissa |
|---|---|---|---|
| Seguidores (`ig_account_stats`) | 1.630 [1.600, 1.670] | D+30, 23/11 | base 1.618; -5 de 12 a 21/10 e +40 em 30 dias com anúncio [FATO, fatos 16 e 17]; só orgânico |
| Saldo de seguidores de 25/10 a 08/11 | +4 [-6, +18] | 11/11 | ritmo das 2 últimas semanas (-2 e 0) [FATO, fato 18] mais o formato do Bruno |
| Ganho líquido de 28/10 a 10/11 (piso do brief: 12) | 6 [-4, 20]; chance de 12 ou mais: 0,3 | 13/11 | brief previa 28 com 0,4 [FATO, fato 169]; sem anúncio |
| Mediana de alcance em 48 h dos reels de 25/10 a 21/11 | 60 [35, 110] | D+30 | mistura de família da TV (sem dado), timelapse e nicho |
| Mediana da família da TV (pb01, po01, pb02, ci01, ob) | 45 [25, 90] | 23/11 | perfil 3/4 entre sem rosto (58) e animação (32,5) [HIPÓTESE] |
| Reels de nicho gravados e publicados até 22/11 | 3 [0, 6] | D+30 | 1 fala em 3 dias [FATO, fato 104] |
| Disparos de TABULEIRO de terceiros até 22/11 | 1 [0, 4] | D+30 | teto de 3,7 a 5,5 comentários [ESTIMATIVA, F8] |
| Diagnósticos de 30 min agendados de 25/10 a 18/11 | 1 [0, 3]; "sem dado" se o Bruno não informar | 18/11 | brief: 1 com 0,2 [FATO, fato 169] |
| Visitas ao perfil em 30 dias | 320 [220, 470] | D+30 | ritmo orgânico de 317 [ESTIMATIVA, F8] |
| Cliques no site em 30 dias | 5 [1, 14] | D+30 | 1,57% das visitas [FATO, fato 14] |
| Views da edição do Bruno no site da TV | 110 [40, 600] | 09/11 | mediana 80,5, máximo 1.400 [FATO, fato 136] |
| Stories à mão feitos sobre os planejados na S1 | 60% [35%, 90%] | 02/11 | execução de 21/10 [FATO, fato 125] |
| Seguidores | 1.650 [1.600, 1.730] | D+60, 23/12 | mesmo ritmo, sem verba até 18/11 e teto escrito depois |
| Diagnósticos realizados desde 25/10 | 2 [0, 6] | D+60 | sem dado de conversão; base 0 |
| Vendas desde 25/10 | 0 [0, 1] | D+60 | base 0 [FATO, fato 8] |
| Seguidores | 1.675 [1.600, 1.800] | D+90, 22/01/2027 | idem |
| Vendas acumuladas desde 25/10 | 0 [0, 2] | D+90 | idem |
| Reels do Bruno para a câmera publicados desde 25/10 | 8 [2, 18] | D+90 | piso de 1 por semana com falhas |

---

## 8. O que mudaria minha opinião, lacunas e fontes

### 8.1 O que mudaria minha opinião
- Bloco 1 entregue até qua 28/10 com minutos cronometrados abaixo de 31: subo a meta para 2 roteiros fixos por semana.
- Família da TV com mediana de 106 ou mais e pulo abaixo de 60% em dom 01/11: abro os cortes do banco (gasto de agência) e aceito a família como DOBRAR.
- Família da TV abaixo de 27: o ci01 não vai ao feed em 02/11 e os ob ficam no banco.
- Dentista B com 150 ou mais em 48 h: TABULEIRO no próximo de nicho e o Dentista C vira sequência imediata.
- Visitas ao perfil acima de 21 por dia de 02 a 04/11: eu teria errado ao não pôr mais estoque na S2; a próxima exibição (se houver) ganha mais peças.
- R1 com 106 ou mais: R2 e R3 saem na semana seguinte, sem esperar.
- A Mirna pedir retirada: tiro tudo com imagem dela, aceito o custo das 10 peças e a S3 e S4 viram nicho e Bruno para a câmera.
- O Bruno informar minutos reais e os 4 números: refaço o CAC e o teto de minutos.
- Horário de 02/11 conhecido até dom 25/10: a contagem com sticker entra (+4 à mão na S1 [ESTIMATIVA, derivação 17]).

### 8.2 Lacunas (sem dado)
Horário da exibição e reprises; @ da Mirna, print e ok para destaque e efeitos no rosto; se o app marca pessoa em reel publicado; audiência da TV; alcance em feriado com reel do Bruno; elegibilidade de Trial Reel; minutos reais de gravação, de story à mão, de marcação e de resposta; números do GA4, do WhatsApp e da agenda; preço do serviço (payback); se bruno26111982 é o Bruno; votos do tl01; desempenho de qualquer corte da TV em perfil 3/4; folha de 4 quadros por segundo e notas dos ob; quadros de tl04 e tl05 conferidos a olho; cópia no Drive; status das leituras da OAB, CFN 856, ABAC, CFP e CFO 196/2019; autorização da Tzur.

### 8.3 Fontes
- Livro de fatos: `/home/user/Disparo-/conteudo/modo-god-cronograma/run/01-fatos.md` (15h50); enquadramento: `run/00-enquadramento.md`; contexto: `contexto.md`.
- Pesquisa: `run/01-pesquisa/F2-playbook-buzzfy.md` (seções 7 a 10), `F4-entrevista-tv.md`, `F5-capacidade-e-estoque.md`, `F6-stories-e-objecoes.md` (seções 3 a 11), `F7-horarios-e-portao.md` (seções 4 a 8), `F8-funil-diagnostico.md`.
- Repositório: `/home/user/Disparo-/CLAUDE.md`; `conteudo/modo-god-nichos/run/10-decision-brief.md` (linhas 115 a 150); `conteudo/sistema-instagram/semanas/2026-10-21.md`; `conteudo/entrevista-tv-camara/pecas-e-calendario.md` (item 2); `conteudo/stories-objecoes/05-manuais-bruno.md` e `06-agenda-postzen.md`; `videos/tv-camara/cortes/mc04.spec.json` e `mc02.spec.json`; `videos/tv-camara/dados/transcricao.json` (1692,8 a 1718,4 s); `git log` (commits 318e97d a eeb4f21).
- Ferramenta, só leitura: PostZen `listPosts`, conta j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 03h UTC a 01/12 03h UTC, ordenado por data, às 18h03 (48 itens).
- Arquivos locais: `ffprobe` e `stat` de `scratchpad/tv/render/` e `scratchpad/tv/ig/` (ob01 a ob03, pf01, mc02, mc03, mc04) às 18h05; folha de quadros em `/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/cadeiraM/folha_ob.png`.
- Nenhuma consulta deu erro. Nenhum agente publicou, agendou, alterou ou enviou nada.
