> **Conselho de instâncias do mesmo modelo é autocrítica estruturada, não verificação independente. Concordância unânime pode refletir viés comum. Este documento reduz risco e explicita premissas; não garante resultado.**

# Plano final · Cronograma de 25/10 a 22/11/2026 · O Estrategista (@o_estrategista.com.br)

Presidente do conselho Agência Reunida. Sábado, 24/10/2026, escrito a partir das 19h45 (São Paulo). 14 cadeiras (A a N), 5 juízes (J1 a J5), 1 debate (D4). O presidente só vê letras e não sabe quem é cada cadeira.

**Pedido do Bruno nesta rodada (literal):** "Vai pro ar segunda dia 2" e "pode seguir pois as postagens vou marcar ela" [FATO 1, mensagem de 24/10, 14h40].

**Leituras próprias do presidente, só leitura, às 19h42:** PostZen `listPosts` da conta j97772ycndetk3f1wcdbh14p898g4b8w (24/10 a 01/12, 48 itens) e `listCommentAutomations` (17 automações); Buzzfy `ig_account_stats` (7 dias). Também: `git log` e `git diff` do repositório, a folha de quadros do vídeo do case de 6 para 20 e a visibilidade do repositório no GitHub (REST, só leitura). Nada foi publicado, agendado, alterado ou enviado. A única escrita é este arquivo.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha uma objeção sozinho. Métrica que falta: "sem dado". Números como "fato 77" apontam para `run/01-fatos.md`.

**Pesos fixos da matriz (enquadramento, seção 7):** impacto 25, probabilidade 20, evidência 20, custo e reversibilidade 15, tempo até o primeiro sinal 10, risco 10. Cada opção recebe nota de 1 a 5 por critério (5 é melhor; em risco, 5 é risco baixo; em custo, 5 é barato e reversível). Total = soma de (nota x peso) / 5, numa escala de 0 a 100. As notas são julgamento do presidente sobre a evidência do conselho, não medida. Uma nota a mais ou a menos muda o total em 5 pontos (impacto), 4 (probabilidade ou evidência), 3 (custo) ou 2 (tempo ou risco).

**Como ler as previsões:** valor central; faixa em que espero o número com cerca de 80% de chance; "chance" = probabilidade de a métrica bater o limiar escrito; data de conferência. A força da evidência vem descrita em cada decisão. Este documento não traz rótulo final de confiança: ele é calculado por regra depois.

---

## 0. Quatro fatos que chegaram depois dos planos e dos juízes

Os 14 planos foram escritos entre 16h17 e 18h20 e os 5 julgamentos entre 18h28 e 18h44 [FATO, hora de modificação dos arquivos em `02-cadeiras` e `03-julgamento`, em UTC menos 3 h]. Só o debate do D4 (19h23 a 19h40) leu o primeiro fato abaixo. Os outros três são leituras deste presidente.

1. **A TV está pausada.** Às 18h45 o Bruno pediu "pausar todos da TV até segunda ordem" [FATO, nota em `stories-objecoes/06-agenda-postzen.md`, `05-manuais-bruno.md` e `entrevista-tv-camara/pecas-e-calendario.md`; commit 6a17563]. Às 19h42: tl01 a tl05, pb01, car01, ci01, po01, pb02, o story pf01 e os stories com conteúdo da TV estão em **rascunho**; seguem agendados só o Dentista B (hoje 21h), a chamada dele (hoje 20h30) e 11 stories de 26 a 31/10 (6 A VIRADA, CRITÉRIO, MÉTODO XEQUE-MATE, ALINHAMENTO, DIAGNÓSTICO 30 MIN e O QUE EU MAIS OUÇO). Não há nada agendado no dom 25/10 nem de dom 01/11 em diante [FATO, `listPosts` 19h42]. O pedido do Bruno repassado a este conselho ("pode seguir") é das 14h40, anterior à pausa. Este plano não trata o "pode seguir" como fim da pausa: levantar a pausa é decisão do Bruno, por escrito.
2. **O story das 19h30 "Nem tudo que vemos é ouro", com o rótulo "NA TV · SEGUNDA, 02/11", não saiu.** Está em rascunho [FATO, `listPosts` 19h42]. A F4 e a maioria das cadeiras usaram "a frase do ci01 já foi anunciada com a data" como motivo para o ci01 sair em 02/11; esse motivo caiu. Saíram hoje 6 stories pelo PostZen (14h00, 14h03, 15h00, 15h01, 16h30, 18h00) e 1 à mão (09h33) [FATO, `listPosts` 19h42; fato 60]. O vídeo de bastidor das 14h00 termina em "AMANHÃ, 18H30, NO FEED" [fato 63] e o tl01 está em rascunho.
3. **Reel do case de 6 para 20 no dom 25/10, 21h, por decisão do Bruno.** Nota ainda não commitada em `06-agenda-postzen.md`: "Decisão do Bruno (24/10): o vídeo do case vai ao ar como está, como reel. Ainda não está no PostZen." Legenda final com "Se o seu negócio travou, comenta ESTRATEGISTA que eu te respondo." [FATO, `git diff` às 19h50]. Na folha de quadros (`scratchpad/tv/ig/case-6-20-folha.jpg`, 54,3 s): o Bruno aparece de frente desde 0,5 s; o nome e o logo da empresa do cliente aparecem no cenário e no cartão do responsável de marketing; aos 50 s há uma interface recriada com "COMENTA ESTRATEGISTA", "1.282 comentários" e perfis de exemplo [FATO, folha vista pelo presidente]. A própria nota registra: nome da empresa no cartão e no áudio, "6 MESES", duas frases "não é X, é Y" faladas e o CTA falado "comenta estrategista" [FATO, nota]. Nenhum plano nem juiz conhecia esse reel.
4. **O repositório é público** [FATO, `gh api repos/brunodjs-source/Disparo-` às 19h50: visibility public]. O debate do D4 mandou copiar ob01 a ob03 "para o repositório". Não fazer: os renders têm imagem e voz da Mirna e conteúdo da emissora, cujos termos vetam republicar conteúdo integral sem autorização [fato 137]. A cópia vai para o Drive do Bruno, em pasta restrita.

**Conta às 19h42, janela de 7 dias, sem anúncio** [FATO, `ig_account_stats`]: 577 contas alcançadas (216 seguidores, 362 não seguidores); 2.254 views; story com 343 contas e 1.354 views; reel 198 contas; 77 visitas ao perfil (11,0 por dia [ESTIMATIVA: 77 / 7]); 0 clique no site; 0 toque em link; 2 comentários; 3 respostas; 1.618 seguidores. Automações: 17 ativas, 1 disparo somado (CHECKLIST) [FATO, `listCommentAutomations` 19h42].

---

## 1. Resumo executivo

**O que muda o plano inteiro.** Com a pausa, o feed das 4 semanas tem, fora da TV, só o reel do case (domingo), 3 remakes de arquivo (R1, R2, R3) e o Dentista C. A gravação semanal do Bruno deixou de ser alavanca de alcance e virou condição para existir grade. O formato que mede bem nesta conta é o Bruno falando de frente para a câmera: mediana de 167,5 de alcance contra 32,5 da animação com voz sintética, pulo de 48,1% contra 83,9% [FATO 25 e 27; n de 4 contra 12, período confundido]. Nenhuma peça da entrevista mostra o Bruno de frente [fato 88 e 97].

**As 6 decisões, em uma linha cada:**

| Decisão | Recomendação | Opção | Previsão principal (chance de bater o limiar) |
|---|---|---|---|
| D1 Série da TV | Dividir (antes, dia, depois) por uma porta ligada à pausa: nada da TV volta sem ordem escrita do Bruno; o mapa de datas diz onde cada peça entra conforme a hora da ordem. ci01 em seg 02/11 21h só com horário confirmado antes das 21h, senão ter 03/11 21h; po01 em qua 04/11 21h; teto de 3 reels da TV por semana a partir da S2 | (c) | média de alcance em 48 h da série até 07/11: 50 (25 a 110); chance de 42 ou mais com pulo até 75%: 0,35 |
| D2 Gravação | 1 bloco por semana até quarta 23h59 com 2 roteiros (24 a 36 min); bloco 1 até qua 28/10 com consórcio, nutricionista, vídeo de 02/11 e 3 a 6 aberturas de frente; piso de 5 min de aberturas; ordem fixa sem gravação; Dentista C só com o portão G1; remakes escalonados | (a) | mediana dos reels de nicho em 11/11: 95 (45 a 170); chance de 53 ou mais com pulo até 75% e n de 3: 0,40 |
| D3 Grade | 5 reels e 2 carrosséis como teto, piso de 3 reels; hora fixa (reels seg, qua, qui, sex 21h e sáb 18h30; carrosséis dom e ter 12h; Trial Reel ter 14h fora da conta); nenhum 6º reel até 23/11; 1 ok semanal na sexta 18h; teto de 2 itens à mão por dia | (a) com o piso de (d) | ganho líquido de seguidores de 28/10 a 10/11: 6 (-4 a 22); chance de 12 ou mais: 0,25 |
| D4 Stories | A decisão do debate: linha sobre o que a pausa deixou; balão de objeção pelo PostZen com "Responde este story" 1 vez por dia útil; link do diagnóstico à mão 1 vez por dia; autoridade por 4 pilares; ob01 e ob03 sem data até 3 condições; ob02 no banco; base de medida em contas (342) | decisão do moderador | respostas de story em 14 dias até 09/11: 7 (3 a 14); chance de 12 ou mais: 0,15 |
| D5 Portão | Régua única de alcance em 48 h sobre 53 (27, 42, 106, 150; pulo de 60% e 75%) até 23/11; PARAR só com n de 2; n de 1 só pausa; feriado não fecha PARAR sozinho; no máximo 3 ações novas do Bruno por rodada; modo metade automático abaixo de 50% de execução em 2 rodadas | (a) | fração de ações executadas até a segunda seguinte: 60% (35% a 85%); chance de 100% em todas as rodadas: 0,10 |
| D6 TABULEIRO | Desligar as 16 automações que não são TABULEIRO em 2 passos (6 até dom 25/10, 10 até sáb 31/10), com a ESTRATEGISTA trocada por uma ligada só ao reel do case; TABULEIRO por post, com origem e profissão no link, no máximo 1 post por semana, só no próximo da mesma linha de um post com 150 em 48 h, nunca em peça da TV, nunca em 02/11, nunca em story; bio para /tabuleiro/?o=ig-bio até dom 01/11 12h | (c) | disparos de terceiros até 22/11: 1 (0 a 4); chance de 3 ou mais: 0,06 |

**As 8 ações das próximas 48 horas:**

1. Sáb 24/10, até 21h, opcional: corrigir o direct da TABULEIRO do Dentista B (promete "4 etapas"; a página entrega um dos 5 Lances) e pôr &p=dentista no botão [fato 117 e 129]. Bruno, ou a agência com ok dele. Cerca de 5 min.
2. Dom 25/10, antes das 09h02: o Bruno desliga a ETAPAS de resposta de story e dá o ok das frases 3 e 4 e do caso das 09h02 até 08h30 (D4).
3. Dom 25/10, até 16h: mensagem única do Bruno, por escrito: a pausa cai ou fica (com data e hora); print da liberação da Mirna; @ dela; horário da exibição, se souber.
4. Dom 25/10, até 18h29: o Bruno desliga CASE, ETAPAS de comentário, FUNIL, CAIXA e a ESTRATEGISTA de conta toda; antes das 21h, uma ESTRATEGISTA ligada só ao reel do case (D6).
5. Dom 25/10, até 20h: o Bruno decide 3 pontos do reel do case (seção 7, item 2). Sem resposta, vale a decisão dele de publicar como está.
6. Dom 25/10, 21h: rótulo das 6 frases de objeção e ok dos balões (D4).
7. Seg 26/10, até 12h: dia e hora do bloco 1 de gravação, que vence qua 28/10 23h59 (D2).
8. Seg 26/10, 21h05: primeira rodada do Módulo 7 com a régua escrita (Dentista B com 48 h; abre ou não o Dentista C e a TABULEIRO da linha de nicho).

**Força da evidência, em uma frase:** forte para o formato (o Bruno de frente contra animação), fraca para a pergunta "antes ou depois de 02/11" (mercado com n de 3 por fase, conta com n de 0), fraca para a palavra-chave (3 comentários em 19 peças) e nula para o efeito da TV (audiência sem dado; mediana de 80,5 views por edição no site).

---

## 2. Decisões

### D1. Série da entrevista em torno de seg 02/11

**Recomendação.** Opção (c), dividir, executada por uma porta ligada à pausa. Nenhuma peça da TV volta ao PostZen sem ordem escrita do Bruno. Quando a ordem vier, cada peça entra na fase que o texto dela serve, pelo mapa abaixo. Peças que apresentam o Bruno e o bastidor (tl01, car01, pb01, pb02, tl02) ficam antes de 02/11 se couberem; a que entrega o método (po01) vai para depois; a de maior presença da Mirna e de posição (ci01) vai para o dia ou o dia seguinte. A Mirna é marcada à mão pelo Bruno em toda peça com imagem ou voz dela, como ele pediu.

**Mapa da porta (hora da ordem escrita do Bruno levantando a pausa):**

| Ordem chega | Feed antes de 02/11 | O que vai para depois |
|---|---|---|
| Até seg 26/10, 17h | seg 26/10 21h tl01; ter 27/10 12h car01; qua 28/10 21h pb01; sex 30/10 21h pb02; sáb 31/10 18h30 tl02, com o portão do tl01 em qua 28/10 21h. Com o case no domingo, a S1 fecha em 5 reels | po01 qua 04/11 21h; ci01 seg 02/11 ou ter 03/11 |
| Entre seg 17h e qua 28/10, 17h | qua 28/10 21h tl01; sex 30/10 21h pb01; sáb 31/10 18h30 tl02 com o portão do tl01 em sex 30/10 21h; car01 na próxima vaga de carrossel até dom 01/11 12h | pb02 e po01 |
| Entre qua 17h e sex 30/10, 17h | sáb 31/10 18h30 tl01 (no lugar do tl02); car01 dom 01/11 12h | pb01, pb02, po01; tl02 vai ao banco |
| Depois de sex 30/10, 17h, ou nenhuma até 02/11 | nada da TV antes da exibição | toda a série, com teto de 3 reels por semana, legendas revisadas (abaixo) |
| Nenhuma até seg 09/11, 19h | nada | a série sai do plano deste ciclo e volta à pauta na rodada de 23/11 |

Regras fixas do mapa: no máximo 1 reel por dia e 5 por semana; nenhum reel a menos de 6 h de outro, Trial Reel incluído [fato 152]; o tl01 não sai no domingo, porque o domingo já tem o case às 21h e os dois ficariam a 2h30 de distância; o tl02 só sai se o tl01 tiver 48 h lidas antes; peça que perder a fase de antes muda a legenda antes de voltar ao PostZen.

**Peça por peça (com a ordem chegando até seg 26/10, 17h):**

| Peça | Data e hora | Motivo | Cuidados antes de agendar |
|---|---|---|---|
| tl01 | seg 26/10 21h | abre a série e o índice dos 7 assuntos | marcar a Mirna (plano aberto, sem fala); a promessa "o mais votado eu solto inteiro depois que a entrevista for ao ar" fica [fato 77] |
| car01 | ter 27/10 12h | apresenta o Bruno ("um computador e um sonho") | um pedido só ("Comenta o número"); tirar "Me manda a data no direct"; os minutos são da gravação do celular, não da edição exibida [fato 81] |
| pb01 | qua 28/10 21h | trajetória (DJ por 20 anos), sem método | marcar a Mirna (Z2 de 0 a 8,75 s) [fato 90] |
| pb02 | sex 30/10 21h | caso do restaurante; fica antes porque a S1 precisa de 5 reels e nenhum dado favorece mover | a CASE de conta toda desligada antes (a legenda diz "Contei esse caso") [fato 79 e 114]; marcar a Mirna |
| tl02 | sáb 31/10 18h30 | parte 2 do bastidor | portão do tl01 pelas 4 faixas da F7 [F7]; tem 10,4 s sem voz real, acima do teto de 8 s [fato 92]: se o tl01 cair numa faixa ruim, o tl02 é o primeiro a ir ao banco |
| po01 | qua 04/11 21h | entrega o método, critério da opção (c) | legenda sem "Comenta a palavra." (não diz qual) [fato 80]; marcar a Mirna (Z2 o tempo todo) |
| ci01 | seg 02/11 21h se, até sex 30/10 18h, o horário da exibição tiver fonte e for antes das 21h; nos outros casos, ter 03/11 21h | peça de posição, com a maior presença da Mirna (10,7 s em Z2 e voz) [fato 90] | abertura com o rosto do Bruno (abertura gravada no bloco 1, ou recorte que abra num quadro com o rosto visível) e folha de quadros com nota 8 ou mais, porque hoje ele aparece de costas até 2,5 s [fato 88]; ouvir quem diz "Ainda. Sempre vai ser." [fato 91]; convite de colaboração só com o @ e o ok escrito da Mirna |
| tl03, tl04, tl05 | sáb 07/11, 14/11 e 21/11, 18h30 | ordem do PostZen | cada um com o portão do anterior; tl04 ("Uau!" recortado no rosto dela) mostrado à Mirna até qua 11/11 e tl05 (carimbo "AINDA?" e selo "REPÓRTER") até qua 18/11 [fato 90] |
| mc02, mc03, mc04 (stories) | mc02 09h01 e mc03 17h30 nos 2 primeiros dias depois da ordem; mc04 dom 01/11 09h | só o Bruno em cena | mc04 com o render de 4,60 s, corte em 1705,567 s, que termina em "família." e evita "estrategista digital" [fato 86 e 96; cadeiras A, B, C, F, G, I, L, M]; tirar o ticker "Uma profissão por 20 anos" [fato 100] |
| pf01 (story) | ter 27/10 16h | dentista, liga ao Dentista B | a versão no PostZen é a v2, "em dois meses" [FATO, `listPosts` 19h42]; o número do caso pede a frase "O número de um caso não se repete igual em outro negócio." num cartão às 16h01 [02-provas; cadeira A]; o link à mão passa para 16h02 |

**Antes, dia e depois.**

- **Antes (até dom 01/11), só com a pausa levantada:** contagem em texto no 1º story do dia, agendado pelo PostZen: "NA TV · SEG, 02/11 · FALTAM N DIAS" [derivar 26]. O sticker nativo de contagem fica de fora, porque pede o horário até dom 25/10 [F6] e o horário segue sem dado. Bastidor: tl01, tl02 e os stories em rascunho que a agência devolver ao PostZen, com teto de 2 itens à mão por dia.
- **Dia (seg 02/11, Finados):** tom sóbrio. 09h estático "NA TV CÂMARA CAMPINAS · SEG, 02/11" pelo PostZen, com a hora no texto se ela tiver fonte até sex 30/10 18h; sem fonte, sem hora. Story à mão com a hora e a menção à Mirna só quando houver fonte, com o link tvcamaracampinas.com.br/ao-vivo [fato 135]. 21h ci01 só nas condições acima. 21h10 pelo PostZen: "Chegou pela TV Câmara? Me manda um oi no direct e conta a sua área." (cadeiras D, H, I, K), a única atribuição da TV possível com as ferramentas de hoje [fato 128 e 130]. Nenhuma palavra-chave, nenhum pedido de venda.
- **Depois (03/11 a 21/11):** link da edição quando ela subir no site ou no YouTube (os agentes leem a página do programa às 09h de 02 a 09/11, cadeira E); destaque NA TV a partir de 03/11, sem logo, sem "vai ao ar" e só com o ok da Mirna para uso permanente [F6]; a promessa do tl01 se cumpre com o link da edição e o resultado da votação; corte longo do mais votado só com 5 votos ou mais [fato 170]; selfies "o que eu disse na TV" com o Bruno de frente, gravadas a partir do bloco 2 [cadeira L; fato 157: criador contando a entrevista, 0,90x, contra corte cru de TV, 0,0055x].
- **Teto:** no máximo 3 reels da TV por semana a partir da S2, timelapse incluído; sobe só com DOBRAR da família da TV no Módulo 7 (cadeiras B e C).
- **Texto depois de 02/11:** "foi ao ar" só com o horário confirmado e passado [fato 6]; minuto da edição só depois de o Bruno assistir; continuam vetados "ao vivo", "rede nacional", "a TV Câmara recomenda", "fui convidado pela TV", "entrevista exclusiva", "A TV me chamou de história de sucesso" [fato 6]; nunca recortar nem filmar a edição exibida [fato 137].

**Marcação da Mirna.** O PostZen não marca pessoa em reel, carrossel nem story; convida colaborador com o @ [fato 139]. Teste no primeiro reel da TV publicado: o app deixa marcar depois de publicado? [sem dado; a buscar 5]. Se deixar, o Bruno marca em até 10 min depois de cada publicação. Se não deixar, o Bruno publica as peças com a Mirna pelo app na hora da vaga (ou pelo agendador do próprio Instagram) e a agência tira essas peças do PostZen. Tudo que amplia o uso da imagem dela pede o ok escrito: convite de colaboração, destaque permanente, efeitos sobre o rosto (tl04 e tl05) e anúncio (cadeira A).

**Números.**
- Visitas ao perfil: 74 em 7 dias às 15h30 (10,6 por dia) [fato 15] e 77 às 19h42 (11,0 por dia) [FATO, `ig_account_stats`]. Meta do dia: 21 por dia de 02 a 04/11 [ESTIMATIVA: 2 x 10,6].
- Seguidores de 12 a 21/10: 1 entrada e 6 saídas, saldo de -5 [fato 17 e 175; o enquadramento dizia 7 saídas].
- Edições do programa no site: mediana de 80,5 views, máximo de 1.400, 4 de 20 com 150 ou mais [fato 136 e 178; o enquadramento dizia 124].
- Mercado (biblioteca do Buzzfy, n pequeno): antes 0,128x os seguidores (n de 3, convite ou bastidor), no dia 0,045x (n de 3), depois 0,066x (n de 7); corte cru de TV 0,0055x (n de 3) [fato 155 e 156].
- Grade da TV de 02/11: não publicada [fato 133]; nesta semana o programa passa às 01h, 06h, 13h e 18h [fato 134].

**Matriz de decisão.**

| Opção | Impacto (25) | Probabilidade (20) | Evidência (20) | Custo e reversibilidade (15) | Tempo até o sinal (10) | Risco (10) | Total |
|---|---|---|---|---|---|---|---|
| (a) Manter os 5 nas datas | 3 | 2 | 2 | 2 | 4 | 2 | 49 |
| (b) Mover os 5 para depois | 3 | 3 | 2 | 4 | 2 | 4 | 59 |
| (c) Dividir | 4 | 3 | 2 | 3 | 3 | 3 | 61 |
| (d) Não mexer, decidir em 26/10 | 2 | 3 | 1 | 3 | 3 | 2 | 45 |
| **Recomendada: (c) com a porta da pausa e as regras de data** | 4 | 3 | 2 | 4 | 3 | 4 | **66** |

**Por quê.** (a) perde pela pausa, que hoje torna as datas impossíveis, e pelo risco de a Mirna ou a produção pedirem para segurar peças já vistas (de 3% a 10% [PRIOR, cadeira A]). (d) perde porque decidir na segunda, com tudo em rascunho, deixa o domingo e a segunda sem peça e não resolve nada que a porta não resolva agora. (b) e (c) ficam próximas, e a recomendação junta as duas: se a ordem do Bruno vier depois de sex 30/10, o mapa transforma (c) em (b) sem nova reunião. O ganho de (c) sobre (b) está no antes: o mercado mostra que o antes que rende é convite e bastidor sem o miolo (0,128x, n de 3) [fato 155 e 156], e tl01, car01 e pb01 são isso. A evidência é fraca para os dois lados; o que pesa é custo e risco.

**Onde o conselho concorda e em que premissa.** Tirar o ci01 de qua 28/10 (12 de 14); fechar a S1 em 5 reels (14 de 14); a TV como prova e não como motor de alcance (7 cadeiras explícitas); nada de "foi ao ar" sem horário; link da edição sim, recorte da edição nunca. Premissas: que a série volte ao feed (os 14 planos são anteriores à pausa); que a S1 tinha 6 reels agendados (fato 76, hoje 0); e que o formato do Bruno de perfil à mesa não fique muito abaixo da média, o que tem n de 0 nesta conta.

**Onde diverge e o que resolveria.**
- po01 fica em qui 29/10 (B, C, G, I, K, L, M, N) ou vai para depois (A, D, E, F, H; J para ter 03/11). O reel do case no domingo, que nenhum plano conhecia, faria a S1 passar de 5 reels com o po01 dentro. Resolve: a regra de 5 do CLAUDE.md e o critério da opção (c) (método vai para depois).
- ci01 em seg 02/11 (maioria) ou ter 03/11 (C). Resolve: o horário da exibição com fonte até sex 30/10 18h.
- Decidir o ci01 agora ou no portão de dom 01/11 21h05 com n de 3 (B, M). Resolve: o portão de dom 01/11 só vale se pb01, pb02 e tl01 tiverem saído; ele entra como freio (PARAR da família tira o ci01 do feed), não como data.
- Recorte do mc04: 4,60 s pronto (8 cadeiras) contra 7,2 s (6 cadeiras). Resolve: o recorte de 7,2 s termina em "profissão", a 1,36 s de "estrategista digital" [fato 96]; o de 4,60 s já está renderizado e não chega perto do termo.

**Minoria vencedora.** Sim, em dois pontos. (1) po01 para qua 04/11 (A, D, E, F, H): com o case no domingo, manter o po01 em 29/10 obrigaria a S1 a 6 reels ou a tirar outra peça de apresentação; o po01 é a peça que entrega o método, exatamente o que a opção (c) manda para depois. (2) ci01 em ter 03/11 quando o horário não tiver fonte (B e C): o motivo da maioria para o dia 02/11 era a frase já anunciada no story das 19h30, e esse story não saiu; com o horário sem dado, publicar no feriado às 21h pode cair antes da exibição, e a leitura de 48 h cairia na quarta seguinte ao feriado sem ganho medido.

**Primeira ação.** O Bruno responde, numa mensagem única até dom 25/10 16h: a pausa cai ou fica (com data e hora); print da liberação da Mirna; @ dela; horário da exibição, se souber. Dono: Bruno. Prazo: 1 dia. Custo: cerca de 10 min [PRIOR].

**Dado que mudaria a decisão.** A hora da ordem escrita sobre a pausa; o horário da exibição; um pedido da produção para segurar peças; a família da TV com n de 2 ou mais abaixo de 42 ou com pulo acima de 75%; o teste de marcação no primeiro reel publicado.

**Critério de abandono.** Se na rodada de seg 09/11 19h a família da TV tiver n de 2 ou mais com mediana de alcance em 48 h abaixo de 42 ou pulo médio acima de 75%, ela sai do feed (fica link da edição, destaque e stories) e as vagas vão para nicho e remakes. Se a pausa não cair até seg 09/11 19h, a série sai do plano deste ciclo.

**Previsão.** Média de alcance em 48 h dos reels da série publicados de 25/10 a 07/11 (`ig_post_stats`), lida em seg 09/11 19h: valor 50; faixa de 25 a 110; chance de 42 ou mais com pulo médio até 75%: 0,35 (inclui a chance de a pausa deixar n abaixo de 2, que conta como não cumprido). Chance de cumprir o critério inteiro do D1 (alcance por fase, 21 visitas por dia de 02 a 04/11 e saldo de seguidores positivo de 25/10 a 08/11, lido em 11/11): 0,10.

**Teste mais barato.** A mensagem do Bruno até dom 16h (10 min, R$ 0) e a leitura da grade de 02/11 no site da TV pelos agentes, todo dia às 09h de 26/10 a 02/11 (2 min por dia).

**Força da evidência.** Fraca na pergunta antes ou depois: mercado com n de 3 por fase, classificado pela F3 a partir de resumos; conta sem nenhuma peça da série medida. Forte no estado da agenda (4 leituras de `listPosts` entre 19h08 e 19h42 com o mesmo quadro). Média nas regras de texto (termos da emissora lidos, nível 2).

---

### D2. Reels de nicho, gravação mínima, o que entra sem gravação, Dentista C e remakes

**Recomendação.** Opção (a): 1 bloco de gravação por semana, entregue até quarta 23h59, com 2 roteiros de nicho e 2 tomadas do gancho (de 24 a 36 min [ESTIMATIVA, F5]).

- **Bloco 1, até qua 28/10 23h59** (de 36 a 54 min [ESTIMATIVA: 31 a 49 da F5 mais 5 das aberturas]): consórcio na versão sem a linha da ABAC; nutricionista na versão sem linha travada (a vigência da CFN 856 segue sem dado [fato 103]); o vídeo de 02/11 com a data falada e sem hora; 3 a 6 aberturas de frente de 2 a 3 s ("Isso eu disse na entrevista à TV Câmara Campinas."), para a agência colar antes do ci01, do ob01 e do ob03 (cadeiras D, G, K).
- **Bloco 2, até qua 04/11:** psicólogo; advogado só com o provimento da OAB lido, senão consórcio 6; com a pausa levantada, a selfie do REACT (20 min [catálogo]) e uma selfie "o que eu disse na TV".
- **Bloco 3, até qua 11/11:** definido pela conferência de nicho de 11/11. **Bloco 4, até qua 18/11.**
- **Piso:** 1 roteiro (12 a 18 min [ESTIMATIVA, F5]); piso absoluto de 5 min só de aberturas de frente em lote (cadeira K).
- **Norma antes de gravar:** cada nicho só grava com a norma do conselho lida e registrada (cadeira A): fonte da ABAC, CFN 856, CFP, provimento da OAB, Res. CFO 196/2019.

**Ordem fixa para fechar as vagas de reel (numa semana sem gravação, a linha "nicho gravado" fica vazia e vale o resto; nunca voz sintética, nunca reel sem o Bruno nos 3 primeiros segundos):**

| # | Com a pausa mantida | Com a pausa levantada |
|---|---|---|
| 1 | Nicho gravado; remake da vez no feed só se o Trial Reel não estiver disponível (com Trial, ele sai na terça 14h e não ocupa vaga); R1, depois R2, depois R3, cada um só se o anterior fez 42 ou mais em 48 h (cadeira M) | Nicho gravado; peças da TV dentro do teto de 3 por semana; ob01 e ob03 só com as 3 condições do D4 |
| 2 | Dentista C, uma vez, só com o portão G1 (abaixo) | Remake da vez |
| 3 | Vaga vazia com motivo escrito | Mais votado só com 5 votos ou mais; corte do banco com folha de quadros e rosto nos 3 s |
| 4 | | pf01 como reel só com DOBRAR de profissão nomeada [fato 173]; Dentista C pelo portão G1 |
| 5 | | Vaga vazia com motivo escrito |

**Dentista C.** Fora do feed por padrão. Entra no feed uma vez, como sequência do Dentista B, só com o portão G1: na rodada de seg 26/10 21h05, o B com 106 ou mais de alcance em 48 h e pulo abaixo de 60%, a Res. CFO 196/2019 lida pela agência e o ok escrito do Bruno (cadeiras N, J e L). Sem G1, o C vai para o direct 1 a 1, como resposta à mão a dentistas que comentarem no A ou no B (cadeiras B, D, F, K). O uso em anúncio depois de 18/11 pede uma exceção escrita do Bruno ao portão de 300 de alcance orgânico do próprio brief, que uma peça nunca publicada não cumpre (achado da cadeira I).

**Remakes.** R1 "Ele nunca fez um anúncio" (10,14x, pulo 53,2%), R2 "90%" (4,42x) e R3 "Problema de equipe" (3,61x), todos em selfie, arquivos em 720p com HTTP 200 [fato 35 e 37]. Repost bate o alcance usual em 35% das vezes com original de 5x ou mais e em 15% com 2 a 5x [fato 150], por isso o R1 vai primeiro. Duas mudanças reais em cada: legenda queimada e texto no quadro 0, mantendo o preâmbulo (a hipótese 18 diz que cortar o preâmbulo pode subir o pulo); legenda de post nova, sem a promessa "saga de 7 dias" [fato 37]. R1 como Trial Reel na ter 27/10 14h, postado pelo Bruno no app, que serve de teste de elegibilidade. Se a opção de Trial Reel não aparecer, o R1 vai ao feed como reel normal na próxima vaga livre, marcado TESTAR. R2 na ter 03/11 14h e R3 na ter 10/11 14h, cada um só se o anterior fez 42 ou mais.

**Case de 6 para 20.** Decisão já tomada pelo Bruno: reel no dom 25/10 21h, como está. Entra na S1 como o reel do domingo. O conselho registra as quebras de regra que o Bruno aceitou (nome do cliente, "6 MESES", duas "não é X, é Y", segunda palavra-chave do mês) e recomenda três ajustes na seção 7, item 2.

**Números.** Última gravação: 21/10 13h12, 36,4 s, uma tomada [fato 104]; plano de 21/10 de 90 min por semana não cumprido [fato 105]. Fila: 19 roteiros de nicho e 21 do Módulo 3 [fato 106]. O Bruno de frente: 167,5 de alcance (n de 4) [fato 25]. Dentista A: 169 de alcance, pulo 46,6% [fato 30].

**Matriz de decisão.**

| Opção | Impacto (25) | Probabilidade (20) | Evidência (20) | Custo e reversibilidade (15) | Tempo até o sinal (10) | Risco (10) | Total |
|---|---|---|---|---|---|---|---|
| (a) 1 bloco semanal de 24 a 36 min | 4 | 3 | 4 | 4 | 3 | 4 | 74 |
| (b) 1 sessão de 60 a 90 min | 5 | 1 | 4 | 3 | 3 | 3 | 66 |
| (c) Sessão quinzenal | 4 | 2 | 3 | 3 | 1 | 3 | 57 |
| (d) Zero gravação | 1 | 5 | 3 | 5 | 3 | 1 | 60 |
| **Recomendada: (a) com piso de aberturas, ordem fixa, C pelo G1 e remakes escalonados** | 4 | 3 | 4 | 4 | 4 | 4 | **76** |

**Por quê.** (b) já foi tentada e não saiu: 36 s gravados desde o plano de 90 min [fato 104 e 105]. (d) é barata, mas com a pausa deixaria o feed com 3 remakes e o case. (a) pede pouco e mantém o único formato que mede bem. O piso de 5 min de aberturas é o que tira o Bruno de costas e de perfil do primeiro segundo das peças da TV, mesmo numa semana sem roteiro.

**Onde o conselho concorda e em que premissa.** 1 bloco semanal com 2 roteiros até quarta, bloco 1 até qua 28/10 (14 de 14); nunca voz sintética; Dentista C fora do feed por padrão (11 de 14). Premissas: que o efeito do Bruno de frente vale para nicho e não é do período (hipótese 16, n de 4 com período confundido); que o Bruno tem de 24 a 36 min por semana (sem dado).

**Onde diverge e o que resolveria.** Dentista C no feed condicional (J, L, N), no direct (B, D, F, K) ou em anúncio depois de 18/11 (maioria): resolve a leitura do B em seg 26/10 21h05. Remakes: quando e quantos (de 1 a 3, de 27/10 a 17/11): resolve a elegibilidade de Trial Reel no app e o alcance do R1 em 48 h. Piso: 1 roteiro, 10 min de selfie ou 5 min de aberturas: resolve o cronômetro do bloco 1.

**Minoria vencedora.** Sim, no Dentista C. A maioria o guardava para anúncio depois de 18/11, mas o próprio brief exige 300 de alcance orgânico para impulsionar (cadeira I), e a pausa tirou do feed quase todo o estoque com o Bruno. Com isso, o argumento de J, L e N (feed só se o B abrir a linha) fica melhor: usa a sequência que o playbook mede (1,81x depois de estouro, medido depois de 5x [fato 149]) sem gastar a mesma fala às cegas.

**Primeira ação.** O Bruno escreve, até seg 26/10 12h, dia e hora do bloco 1. A agência deixa no teleprompter, até seg 26/10 18h, consórcio sem a linha da ABAC, nutricionista na versão sem linha travada, o vídeo de 02/11 e as aberturas. Dono: Bruno. Prazo: 2 dias.

**Dado que mudaria a decisão.** O Dentista B com 48 h; o arquivo do bloco 1 até qua 28/10 23h59; a opção de Trial Reel no app; o cronômetro real do bloco 1; a leitura das normas.

**Critério de abandono.** Qua 11/11: mediana dos 3 primeiros reels de nicho com o Bruno falando (Dentista A e os 2 gravados; o Dentista B anotado à parte, por ser outro formato) abaixo de 53 ou pulo mediano acima de 75%: o nicho para (regra de 21/10) [fato 169]. Com n menor que 3: "não testado", nunca PARAR. Se nenhum bloco for gravado até qua 04/11 23h59, a S3 e a S4 entram no modo metade e o D2 volta à pauta em 09/11.

**Previsão.** Mediana de alcance em 48 h dos 3 primeiros reels de nicho com o Bruno falando, lida em qua 11/11: valor 95; faixa de 45 a 170; chance de 53 ou mais com pulo mediano até 75% e n de 3: 0,40. O valor 95 repete a previsão de 21/10 [fato 169]. Chance de cumprir o critério inteiro do D2 (2 reels de nicho por semana a partir da S2 e 1 com 106 ou mais até 23/11): 0,20.

**Teste mais barato.** O Bruno grava só as aberturas de frente (5 min) até qua 28/10: o ci01 e os ob ganham o rosto no quadro 0 e o bloco 1 vira medida de tempo real.

**Força da evidência.** Média a forte para o formato (n de 4 contra 12, 5,2x no alcance, 35,8 pontos de pulo [derivar 21]), com período confundido. Fraca para a capacidade do Bruno (uma gravação em 3 dias). Fraca para nicho (n de 1 com o Dentista A).

---

### D3. Grade semanal, horários, feriados, PostZen e o que é à mão

**Recomendação.** Opção (a) como teto, com o piso da opção (d):

- **Ritmo:** 5 reels e 2 carrosséis por semana (domingo a sábado) como teto; piso de 3 reels com o Bruno nos 3 primeiros segundos. Vaga sem peça aprovada fica vazia, com motivo escrito no arquivo da semana. Nenhum 6º reel até 23/11.
- **Hora fixa por formato:** reels seg, qua, qui e sex às 21h e sáb às 18h30; carrosséis dom e ter às 12h; Trial Reel ter às 14h, fora da conta dos 5 [hipótese 32, regra escrita aqui]. No máximo 1 reel e 2 posts de feed por dia; nenhum reel a menos de 6 h de outro.
- **Feriados:** seg 02/11, o que o D1 manda; dom 15/11, carrossel às 12h, normal; sex 20/11, reel às 21h, normal, sem usar a data. Reel de feriado não fecha PARAR sozinho (D5).
- **PostZen e mão:** a agência produz e agenda uma semana por vez, depois de 1 ok semanal do Bruno na sexta até 18h; o Bruno faz à mão só o que exige o celular dele: stickers, marcação da Mirna, Trial Reel, compartilhamento de post e respostas. Teto de 2 itens à mão por dia (D4). Lista diária com "feito" ou "não feito" no arquivo da semana.
- **Carrosséis (agência, cerca de 36 min cada [ESTIMATIVA, F5]; foto do Bruno na capa, porque feed com foto tem mediana de 111 de alcance contra 34,5 do texto [fato 51]):**

| Data | Carrossel | Fonte do texto |
|---|---|---|
| dom 25/10 12h | car02 "Prazer. Eu sou o Bruno." (com o ok até 10h; sem ok, vai para ter 27/10) | posicionamento do Módulo 2; os estáticos "Prazer" e bastidor somaram 34 das 48 visitas ao perfil vindas do feed [fato 53] |
| ter 27/10 12h | car01 com a pausa levantada; senão car03 "Você atende. Eu comando." | car01 pronto; car03 do Módulo 2 e da cadeira G |
| dom 01/11 12h | car04 "Os 5 Lances" (A Abertura, O Gambito, O Meio-Jogo, O Xeque-Mate, A Promoção) | `tabuleiro.js` [fato 129] |
| ter 03/11 12h | car05 "Os 30 minutos": o que acontece, para quem é, para quem não é, sem preço | cadeira F; resolve o "diagnóstico" com dois sentidos [fato 131] |
| dom 08/11 12h | car06 Saga, 2ª temporada, parte 1 | cadeira K; a semana da saga trouxe 13 seguidores [fato 44] |
| ter 10/11 12h | car07 "Curso, mentoria ou comando" | cadeira G |
| dom 15/11 12h | car08 Saga, parte 2 | cadeira K |
| ter 17/11 12h | car09 "Para quem é e para quem não é" | cadeira G |
| dom 22/11 12h | car10 (abre a S5), tema escolhido na rodada de 16/11 | |

**Grade das 4 semanas.** Ver a seção 3.

**Números.** 3 posts por dia não aumentaram seguidores [CLAUDE.md; fato 44]; ritmo de 5 a 7 reels por semana com 7,0% de estouro contra 7,7% em 7 ou mais [fato 152]; reel a menos de 6 h do anterior, 0,92x [fato 152]; hora não separou resultado dentro do formato [fato 40 e 41, só animação]; nenhum reel com o Bruno saiu entre 12h e 20h59 [fato 39]; seguidores online de 386 a 430 das 11h às 22h [fato 20].

**Matriz de decisão.**

| Opção | Impacto (25) | Probabilidade (20) | Evidência (20) | Custo e reversibilidade (15) | Tempo até o sinal (10) | Risco (10) | Total |
|---|---|---|---|---|---|---|---|
| (a) 5 e 2 fixos | 3 | 2 | 3 | 4 | 3 | 2 | 57 |
| (b) 6 reels na S1 | 2 | 2 | 1 | 3 | 3 | 2 | 41 |
| (c) 6 a 7 com portão | 3 | 1 | 2 | 2 | 3 | 1 | 41 |
| (d) 3 e 2 em semana sem peça | 2 | 4 | 3 | 4 | 3 | 4 | 64 |
| **Recomendada: (a) como teto, piso de 3 de (d), sem 6º reel** | 3 | 4 | 3 | 4 | 3 | 4 | **69** |

**Por quê.** (b) perdeu a razão de existir: a promessa do sábado saiu da legenda do tl01 [fato 77]. (c) troca 0,7 ponto de chance de estouro [fato 152] por carga que a execução medida não sustenta (3 "não" em 8 decisões [fato 125]). (a) pura empurra a encher vaga com formato reprovado numa semana sem peça, que é o cenário da pausa.

**Onde o conselho concorda e em que premissa.** 5 e 2 com hora fixa (reels 21h nos dias úteis e 18h30 no sábado; carrosséis ter e dom 12h) na maioria; 1 reel por dia; carrossel com foto do Bruno; Trial fora da conta (A, C, D, G, K, N). Premissas: que a hora pesa pouco e o formato pesa muito (n pequeno, só animação); que existe peça aprovada para 5 vagas (com a pausa, não existe).

**Onde diverge e o que resolveria.** 6º reel (K abre na S3; B, E e M fecham): resolveria um dado desta conta de que mais reels por semana sobem estouro, que não existe. Vaga vazia contra "0 vaga vazia" do enquadramento: resolve a linha "feito" e a mediana semanal. Quem agenda (agência com 1 ok semanal, B, C e K, ou só o Bruno): resolve o Bruno, na seção 7. Stories à mão de 15 a 27 por semana: fechado no D4 (teto de 2 por dia).

**Minoria vencedora.** Sim, no piso. B, C, M e N defendiam teto de 5 com piso de 3 e vaga vazia com motivo; o enquadramento e a maioria pediam 0 vaga vazia. Com a pausa e sem gravação desde 21/10, "0 vaga vazia" obriga a publicar o que não passa na regra dos 3 segundos ou repetir a mesma fala; o piso protege a regra do CLAUDE.md, que é anterior e medida.

**Primeira ação.** A agência entrega até dom 25/10 09h a grade da S1 nas duas versões (pausa mantida e pausa levantada), com o car02 e o remake do R1 em produção; o Bruno dá 1 ok até 10h. Dono: agência. Prazo: 1 dia.

**Dado que mudaria a decisão.** A linha "feito" da S1 (sáb 31/10); o alcance de feriado (02/11, 15/11, 20/11) [a buscar 35]; um reel do Bruno de frente fora das 21h.

**Critério de abandono.** Linha "feito" abaixo de 50% em 2 semanas seguidas (lidas em 02/11 e 09/11): a semana seguinte entra no modo metade (3 reels, 2 carrosséis, stories só agendados e 1 item à mão por dia) (cadeira C). Ganho líquido de seguidores de 28/10 a 10/11 abaixo de 12 (lido em sex 13/11; conferência do brief em qua 18/11 [fato 169 e 182]): a rodada de 16/11 revisa oferta e público, não a grade (cadeira N).

**Previsão.** Ganho líquido de seguidores de 28/10 a 10/11 (`ig_follower_growth` lido em sex 13/11): valor 6; faixa de -4 a 22; chance de 12 ou mais: 0,25. Base: 0 e -2 nas duas últimas semanas fechadas [fato 18]. Chance de cumprir o critério inteiro do D3 (mediana semanal de 42 ou mais nas 4 semanas, 106 ou mais em 2, 0 dia com 2 reels e o ganho de 12): 0,08.

**Teste mais barato.** A lista diária com "feito" ou "não feito" na S1, lida pelos agentes na seg 02/11 19h. Nenhum minuto a mais do Bruno além de marcar.

**Força da evidência.** Média para o ritmo (playbook entre 531.037 criadores, nível 2, e a série 2 desta conta [fato 32 e 44]); fraca para hora e feriado (n de 3 pares, só animação).

---

### D4. Linha diária de stories e ob01 a ob03

**Recomendação.** A decisão do moderador do debate (`run/05-debates/D4.md`, seção 5), que as 14 cadeiras votaram depois do debate:

- **S1:** a base são os 11 stories agendados de 26 a 31/10. Dom 25/10: frase 3 às 09h00 e frase 4 às 18h00 e o caso de 6 para 20 às 09h02 com "Responde este story" no PNG, pelo PostZen com o ok do Bruno até 08h30; sem ok, o caso vai à mão. Os 5 balões de seg a sex vão pelo PostZen com "Responde este story" com o ok até dom 21h; o de sexta sai sem o pedido, porque o pedido do dia é o DIAGNÓSTICO · 30 MIN das 17h31, já agendado. Com os oks, 28 stories (19 pelo PostZen e 9 à mão); sem oks, 26 (11 agendados e 15 à mão).
- **Acréscimo deste presidente para o domingo:** a chamada do case às 20h30 (`2510-2030.png`) e o compartilhamento do reel do case às 21h05 (à mão) [FATO, nota não commitada]. Com os oks, o domingo fica com 3 itens à mão (12h00, 12h30 e 21h05), exceção de um dia.
- **Rótulo:** até dom 21h, o Bruno marca as 6 frases (O2, O8, O3, O4, O6, O5) como "ouço com frequência" ou "não". "Sim" mantém O QUE EU MAIS OUÇO; "não" ou sem resposta troca para VOCÊ JÁ PENSOU ISSO?. O balão de sáb 31/10 12h00 (m17f11admffkxasz208m9wzv518gwd0v) já está agendado com o rótulo antigo [FATO, `listPosts` 19h42]: trocar a mídia pede o ok até sex 30/10 18h.
- **Pedidos:** cada story pede uma coisa só; por dia, no máximo 1 pedido de resposta e 1 de clique; o "único pedido" do enquadramento vira "único destino", o diagnóstico.
- **ETAPAS de story:** desligada antes de dom 09h02; o Bruno responde à mão, em até 24 h, cada resposta, que chega como direct comum [fato 120]. A agência corrige a nota "cai na automação ETAPAS" em `05-manuais-bruno.md`, `04-estaticos.json` e `03-plano-7-dias.md`.
- **S2 a S4:** 09h00 frase de efeito pelo PostZen (a agência escreve 7 por semana a partir do `01-objecoes.md` e do 00-SISTEMA; o Bruno aprova no ok de sexta); 12h00 balão e 12h01 virada com o sub fixo "Você atende. Eu comando." nos 13 dias úteis de 03/11 a 19/11; 17h30 pilar em rodízio (quem é, como trabalha, o que já fez, o que não faz); link à mão e compartilhamento do post do dia; no máximo 2 itens à mão por dia e 14 por semana. Enquanto a pausa durar, a prova vem dos pilares e do caso de 6 para 20; depois que ela cair, a TV aparece em no máximo 2 dias por semana. Objeções: O9 a O12 na S2; O7 com fonte conferida, O1 e repetições na S3; frases tiradas das respostas na S4.
- **ob01 a ob03:** nenhum tem data. O ob01 entra na primeira vaga sem gravação nova quando houver as 3 condições: ordem escrita do Bruno levantando a pausa; abertura de 3 s com o rosto dele com nota 8 ou mais na folha de quadros (hoje os 3 abrem com o Bruno de perfil atrás do monitor e um braço de camisa azul na borda [fato 97]); família da TV fora de PARAR com n de 2. O ob03 vem depois. O ob02 vai para o banco (usa os mesmos 21,4 s de fala do pf01 [fato 95]).
- **Correção deste presidente:** os renders de ob01 a ob03 (e de ci01, pb01, pb02, po01, tl01, mc02, mc04, pf01) estão só em `scratchpad/tv/ig/` [FATO, `ls` às 19h55]. Cópia para o Drive do Bruno, em pasta restrita; nunca para o repositório, que é público.

**Medida.** Respostas de story: meta de 12 em 14 dias, 2x a base de 3 em 7 dias [fato 56; correção de A, B, C, D, E, F e G: 6 em 14 é 1x]. Contagem oficial no `ig_account_stats` de 14 dias lido na seg 09/11 às 12h00 (janela de 26/10 12h a 09/11 12h); contagem por story no `ig_post_stats` antes de expirar, e story com menos de 5 espectadores conta "sem dado" [fato 67]. Faixas (Poisson de média 6, chance de cair na faixa sem efeito nenhum entre parênteses [ESTIMATIVA, debate]): 12 ou mais (2%) DOBRAR; 7 a 11 (37%) MANTER; 3 a 6 (54%) MANTER e trocar só o texto do pedido; 0 a 2 (6%) o pedido cai para 2 por semana. Alcance de story: base de 342 contas em 7 dias [FATO, 19h23; 343 às 19h42], lida toda segunda às 19h; views só anotadas, porque subiram 27% enquanto as contas subiram 1,5% entre 15h30 e 19h23 [ESTIMATIVA, debate].

**Matriz de decisão.**

| Opção | Impacto (25) | Probabilidade (20) | Evidência (20) | Custo e reversibilidade (15) | Tempo até o sinal (10) | Risco (10) | Total |
|---|---|---|---|---|---|---|---|
| (a) 03-plano estendido | 3 | 1 | 2 | 4 | 4 | 2 | 51 |
| (b) 3 a 5 por dia | 2 | 4 | 2 | 5 | 4 | 3 | 63 |
| (c) 6 a 8 em 4 blocos com enquete e TV | 3 | 2 | 2 | 4 | 4 | 3 | 57 |
| (d) ob01 a ob03 com data | 2 | 1 | 1 | 4 | 3 | 2 | 40 |
| **Recomendada: decisão do moderador** | 3 | 4 | 3 | 5 | 5 | 4 | **76** |

**Por quê.** Story pela API sai sem sticker [fato 66] e nenhuma ferramenta permitida lê voto de enquete [fato 143]: a objeção em enquete da opção (c) não gera número. O balão com "Responde este story" gera um número que o `ig_post_stats` lê, sai pelo PostZen e tira 5 itens da mão do Bruno. A TV como prova em 6 de 7 dias era ponto único de falha, e a pausa mostrou isso.

**Onde o conselho concorda e em que premissa.** Depois do debate, as 14 cadeiras votaram na decisão do moderador (13 grafias diferentes; a estatística marcou "rachada" por causa das grafias). Antes do debate, (c) liderava com 0,64. Premissas: que o Bruno dá os oks de dom 08h30 e 21h e responde em 24 h; que "Responde este story" gera resposta acima da base de 0,9% por conta (3 em 337) [ESTIMATIVA, debate].

**Onde diverge e o que resolveria.** Média de base da regra (6 ou 3,3, a de 30 dias [fato 57]): resolve a média de respostas por pedido de 26 a 30/10 (3 ou mais sobe a meta; abaixo de 1,3, a meta é revista em 09/11). Rótulo substituto: fechado (VOCÊ JÁ PENSOU ISSO?). Segundo horário da frase no domingo (17h30 ou 18h00): sem dado; vale 18h00.

**Minoria vencedora.** Não. A posição final saiu do debate com as 14 cadeiras, embora a autoridade por pilares tenha vindo de uma só cadeira (G) antes do debate.

**Primeira ação.** O Bruno desliga a ETAPAS de resposta de story antes de dom 25/10 09h02 e dá o ok das frases 3 e 4 e do caso até 08h30. Dono: Bruno. Prazo: 1 dia. Custo: cerca de 4 min [PRIOR].

**Dado que mudaria a decisão.** Média de respostas por pedido de 26 a 30/10; a pausa levantada; views e contas variando na mesma proporção; stories de pilar abaixo dos de TV na mesma posição da pilha.

**Critério de abandono.** Leitura de seg 09/11 12h com 0 a 2 respostas em 14 dias: o pedido cai para 2 por semana. Contas de story abaixo de 342 em 02/11 e 09/11: a agência acrescenta estáticos pelo PostZen, nunca item à mão.

**Previsão.** Respostas de story de 26/10 12h a 09/11 12h (`ig_account_stats`, 14 dias), lidas em seg 09/11 12h: valor 7; faixa de 3 a 14; chance de 12 ou mais: 0,15. Chance de cumprir o critério inteiro do D4 (respostas, contas de 342 ou mais nas segundas e ob01 a ob03 com média de 42 ou mais, este último "não testado" se não forem ao ar): 0,10.

**Teste mais barato.** Os agentes leem no `ig_post_stats`, antes de 24 h, as respostas de cada story de pedido de seg 26/10 a sex 30/10 (5 leituras de cerca de 2 min, 0 minuto do Bruno). Primeira resposta na sex 30/10.

**Força da evidência.** Alta no estado da agenda e na troca de views por contas (leituras repetidas de hoje); média no pedido diário (aritmética sobre base pequena); fraca nos pilares (n de 1 dia de stories de TV).

---

### D5. Portão semanal do Módulo 7

**Recomendação.** Opção (a), com as regras de (e) que a maioria somou:

- **Régua única até 23/11:** alcance em 48 h sobre a mediana de 53 [fato 24]: 27 (0,5x), 42 (0,8x), 106 (2x), 150 (2,8x); pulo de 60% e 75% [derivar 2]. Views equivalentes só como coluna de leitura (alcance x 1,52 [derivar 4]).
- **PARAR:** mediana do formato abaixo de 42 ou pulo mediano acima de 75%, com n de 2 ou mais. **MANTER:** de 42 a 105. **DOBRAR:** 106 ou mais e pulo abaixo de 60%, com n de 2 ou mais. **TESTAR:** n de 0 ou 1, no máximo 1 vaga nova por semana. Peça com n de 1 abaixo da régua vai para "pausa" e volta ao banco, sem PARAR o formato (cadeira M). Carrossel: DOBRAR pede também 2 visitas ao perfil [F7].
- **Formatos lidos separados (cadeira L):** Bruno de frente; TV de perfil; TV de costas; timelapse; remake; carrossel com foto; nicho em tela dividida.
- **Feriado:** reel de 02/11, 15/11 ou 20/11 não fecha PARAR sozinho.
- **Leitura:** tolerância de 1 h na leitura de 48 h; erro de consulta é erro, nunca zero (cadeira D); só orgânico, em janelas de 7 dias com hora fixa, porque cerca de 1.907 contas de anúncio saem da janela de 30 dias até meados de novembro (cadeira I) [fato 10].
- **Rodadas:** seg 26/10 21h05 (Dentista B com 48 h; portão G1); com a pausa levantada, portão do tl01 48 h depois de ele sair; dom 01/11 21h05, só se a família da TV tiver n de 2 ou mais (freio do ci01); seg 02/11 19h, lida pelos agentes no feriado, com a lista do Bruno vencendo ter 03/11 11h; seg 09/11, 16/11 e 23/11 às 19h (a de 23/11 decide a S5). Conferências: qua 04/11 (diagnóstico parcial [fato 181]), qua 11/11 (nicho; saldo de seguidores de 25/10 a 08/11 [derivar 5]), sex 13/11 (piso de seguidores de 28/10 a 10/11), qua 18/11 (diagnóstico e seguidores, brief).
- **Execução:** cada rodada registra "executado: sim ou não" por ação, a coluna de minutos do Bruno por peça (cadeira I) e uma linha de conformidade que trava DOBRAR em peça com regra quebrada (cadeira A). No máximo 3 ações novas do Bruno por rodada (cadeiras L e M). Execução abaixo de 50% em 2 rodadas seguidas: modo metade automático na semana seguinte (cadeira C).
- **Registro:** `conteudo/sistema-instagram/semanas/AAAA-MM-DD.md`, com a projeção do 00-SISTEMA atualizada e "sem dado" onde faltar. A rodada de 26/10 atualiza também as faixas do CLAUDE.md em "Aprendizados medidos", que estão desatualizadas: o Bruno de 3,41x a 8,21x em alcance sobre 37,5; sintéticos de 0,39x a 1,07x em views, com pulo de 69,4% a 89,7% [fato 183].

**Números.** Teste da régua na fase atual: 12 de 12 reels de animação em PARAR, 4 de 4 com o Bruno em DOBRAR, 3 sem rosto em MANTER [F7]. Semanas fechadas: medianas de 64, 128, 33,5 e 16 [fato 43]. Execução de 21/10: 3 sim, 1 em parte, 3 não, 1 sem dado, em 8 [fato 125; o enquadramento dizia 2 não executadas]. Mediana atual do Buzzfy: 37,5 de alcance; normal de 57 views [fato 23].

**Matriz de decisão.**

| Opção | Impacto (25) | Probabilidade (20) | Evidência (20) | Custo e reversibilidade (15) | Tempo até o sinal (10) | Risco (10) | Total |
|---|---|---|---|---|---|---|---|
| (a) Alcance em 48 h sobre 53 | 4 | 4 | 3 | 5 | 4 | 4 | 79 |
| (b) Views sobre 57 | 3 | 4 | 3 | 5 | 4 | 3 | 72 |
| (c) Mediana 37,5 | 3 | 4 | 3 | 5 | 4 | 2 | 70 |
| (d) Mediana refeita a cada rodada | 2 | 3 | 2 | 3 | 4 | 2 | 51 |
| **Recomendada: (a) com n de 2, pausa para n de 1, feriado, 3 ações e modo metade** | 4 | 4 | 3 | 5 | 4 | 5 | **81** |

**Por quê.** (c) deixaria a animação (32,5) em MANTER, porque 0,8 x 37,5 = 30 [ESTIMATIVA]; a régua de 53 separa os formatos como os dados separam. (d) quebra a comparação entre semanas, que é a medida do D5 (S4 contra S1). (b) mistura revisitas com contas. O acréscimo que mais pesa é o de execução: o gargalo medido é fazer, não decidir.

**Onde o conselho concorda e em que premissa.** Régua de 53 fixa com n de 2 para PARAR (14 de 14); rodada de 02/11 lida pelos agentes (maioria). Premissas: que 53 serve de referência embora o Buzzfy não a recalcule hoje e a base atual seja 37,5 [fato 23 e 24]; que alcance de feriado é comparável (sem dado).

**Onde diverge e o que resolveria.** Gatilho de sequência por 171 views em 24 h (G e K) contra régua só de alcance: fica como coluna de leitura, sem abrir vaga, porque o enquadramento pediu para não misturar alcance com views. Portão extra de dom 01/11: entra só como freio. Forma da regra de execução (B 60%, C 50%, M 3 ações, F 5 decisões): vale 50% e 3 ações; resolve a execução das rodadas de 26/10 e 02/11.

**Minoria vencedora.** Não. Os acréscimos de execução (C, M, L) somam à maioria sem contrariar a régua.

**Primeira ação.** Os agentes rodam a rodada de seg 26/10 21h05 com a régua escrita, a linha "executado" e a linha de conformidade, registrada em `conteudo/sistema-instagram/semanas/2026-10-26.md`. Dono: agência (Módulo 7). Prazo: 2 dias. Custo: de 30 a 45 min de agente [PRIOR].

**Dado que mudaria a decisão.** A mediana de 53 recalculada pelo Buzzfy; um reel do Bruno de frente fora das 21h; execução abaixo de 50%.

**Critério de abandono.** Execução abaixo de 50% nas rodadas de 02/11 e 09/11: a rodada de 16/11 passa a no máximo 1 ação nova do Bruno e a semana entra no modo metade. A régua de 53 só muda na rodada de 23/11, com as 4 semanas de dado.

**Previsão.** Fração das ações do Bruno marcadas "executado: sim" até a segunda seguinte, nas rodadas de 26/10 a 16/11: valor 60%; faixa de 35% a 85%; chance de 100% em todas: 0,10. Chance de cumprir o critério inteiro do D5 (5 rodadas registradas até 23/11, tudo executado, nenhum PARAR com n de 1 e mediana da S4 acima da S1): 0,08.

**Teste mais barato.** Rodar a rodada de 26/10 com a régua sobre os reels que já têm 48 h e conferir se a classificação bate com o Módulo 7 de 21/10 (15 min de agente).

**Força da evidência.** Média: a régua separa os formatos da fase atual sem erro (12 de 12 e 4 de 4), mas a base de 53 vem de outra janela (17 reels de 21/09 a 21/10) e o n por formato é pequeno.

---

### D6. TABULEIRO, as outras automações e o caminho até o diagnóstico

**Recomendação.** Opção (c), com quatro pontos em que a minoria vence:

- **Automações, em 2 passos:** até dom 25/10 09h02, a ETAPAS de resposta de story; até dom 25/10 18h29, CASE ("case", "caso"), ESTRATEGISTA de conta toda, ETAPAS de comentário, FUNIL e CAIXA [fato 114]. Antes das 21h do domingo, uma ESTRATEGISTA nova ligada só ao reel do case, para servir o CTA falado do vídeo, com o botão para /tabuleiro/?o=ig-case e ativa até dom 01/11. Até sáb 31/10, as outras 10 ligadas a posts antigos (ETAPAS Escala 7x7, RECUPERAÇÃO, PERPÉTUO, CARRINHO, EVENTO, PESQUISA, AQUECIMENTO, CAPTAÇÃO, OFERTA, CHECKLIST), cumprindo a decisão de 21/10 de parar 12 palavras-chave, que não foi executada [fato 125] (cadeiras A, D, L, N).
- **TABULEIRO por post, nunca de conta toda:** uma automação por post, com o=ig-tab-AAMMDD e &p=profissão no botão, e linkTracking ligado (cadeiras A, E, H, L). No máximo 1 post por semana; só no próximo post da mesma linha (formato) de um post com 150 ou mais de alcance em 48 h [CLAUDE.md; fato 170 e 171]; nunca em peça com imagem ou voz da entrevista; nunca em 02/11; nunca em story. A condição extra de pulo abaixo de 60% sai da regra e fica como coluna de leitura (cadeira B: Dentista A e PESQUISA tiveram 169 de alcance, pulos de 46,6% e 86,9%, e 0 comentário os dois [fato 30 e 122]).
- **Candidatos em novembro, nesta ordem:** o próximo reel de nicho, se o Dentista B ou o primeiro nicho gravado passar de 150; o próximo remake, se o R1 passar; o próximo carrossel com foto, se o anterior passar.
- **Direct:** o texto passa a falar dos 5 Lances que a página entrega, e não de "4 etapas" [fato 117 e 129], sem tom de pressão [PRIOR 13].
- **Um pedido por peça.** Nas legendas da série da TV, só pergunta aberta ou "Manda para alguém"; o pedido privado fica nos stories (link) e na bio.
- **Bio e perfil até dom 01/11 12h:** texto do Módulo 2 sem "Estrategista Digital" (vetado no 02-provas) e sem emoji; "Estrategista de Lançamento" no campo Nome (cadeira K); link /tabuleiro/?o=ig-bio [fato 132]; 3 fixados com o Bruno de frente ou a foto dele: car02 "Prazer", o R1 original de 03/10 (10,14x) e o Dentista A (169).
- **Nomes:** "O Tabuleiro" é o teste de 12 casas; "O Primeiro Lance" é a conversa de 30 min; "diagnóstico" na meta de 10 por mês conta só a conversa realizada (cadeiras G, L, N) [fato 131].
- **Contagem toda segunda até 18h, antes do portão:** as 11 etapas da F8 mais "abriu com preço: sim ou não" (cadeira G) e a origem de cada conversa (cadeira N). Logs sem os perfis do Bruno; GA4 (tabuleiro_start, tabuleiro_complete, generate_lead), WhatsApp e agenda informados pelo Bruno; o que ele não informar fica "sem dado".
- **Teste de ponta a ponta até dom 01/11:** um perfil de terceiro comenta "tabuleiro" no Dentista B, recebe o direct, faz o teste e chega ao WhatsApp; o log é conferido no `listCommentAutomationLogs`.
- **Plano B em seg 09/11:** se o post com TABULEIRO tiver 0 comentário, todo comentário de pergunta aberta recebe resposta privada à mão, em até 2 h, com o link do teste (cadeiras D e E).

**Números.** 17 automações ativas, 15 palavras, 1 disparo somado (CHECKLIST, perfil que pode ser do Bruno) [FATO, `listCommentAutomations` 19h42; fato 116]. TABULEIRO: 0 log [fato 117]. 19 peças com palavra-chave renderam 3 comentários (0,39 por 100 contas); os 4 reels com o Bruno, 5 em 771 (0,65) [fato 122 e 123; derivar 12]. Mercado em português: palavra-chave a 0,043x os seguidores contra 0,081x dos outros pedidos; 0 de 9 estouros de contas até 6 mil seguidores usou palavra-chave [fato 164]. Teto de comentários de qualquer tipo em posts com TABULEIRO até 22/11: de 3,7 a 5,5 [derivar 13]. Funil da bio: 1,57% de clique; 10 conversas por mês pedem 637 visitas com 100% de conversão depois do clique, contra cerca de 317 orgânicas [derivar 14]. 7 dias: 0 clique em 77 visitas [FATO, 19h42]. A origem o= se perde: não entra no WhatsApp nem nos eventos do GA4 [fato 129 e 130].

**Matriz de decisão.**

| Opção | Impacto (25) | Probabilidade (20) | Evidência (20) | Custo e reversibilidade (15) | Tempo até o sinal (10) | Risco (10) | Total |
|---|---|---|---|---|---|---|---|
| (a) TABULEIRO em todo post com 150 | 2 | 2 | 1 | 4 | 3 | 2 | 44 |
| (b) Um único post por mês | 2 | 2 | 2 | 5 | 2 | 4 | 53 |
| (c) (a) ou (b) com revisão das automações | 3 | 2 | 2 | 4 | 3 | 4 | 57 |
| (d) Não ligar em novembro | 1 | 3 | 2 | 5 | 1 | 4 | 50 |
| **Recomendada: (c) por post, sem TV, 16 automações fora em 2 passos** | 3 | 2 | 2 | 4 | 3 | 5 | **59** |

**Por quê.** O gargalo está antes do comentário: 577 contas, 2 comentários e 0 clique em 7 dias. Nenhuma opção de D6 move muito; a recomendada é a que custa menos para errar e a única que deixa medir por peça. As automações de conta toda são risco concreto na volta da TV: um comentário de parabéns com "caso" ou "estrategista" receberia o direct de venda e gastaria a única resposta privada daquele comentário [fato 114 e 120; hipótese 46].

**Onde o conselho concorda e em que premissa.** Desligar as automações de conta toda antes do tl01 (13 de 14); TABULEIRO nunca em 02/11, no máximo 1 por semana e só depois de 150; bio para o teste. Premissas: que comentários com "caso" e "estrategista" vão aparecer quando a série voltar (hipótese, sem medida); que o gargalo é o topo do funil.

**Onde diverge e o que resolveria.** Conta toda (8) contra por post (4): resolveria saber qual automação responde quando duas têm a mesma palavra [a buscar 32]; sem esse dado, por post evita a colisão. TABULEIRO em peça da TV (A, C, D, I, N aceitam; B, E, H, L excluem): resolveria um parecer sobre os termos da emissora, que este conselho não dá. Quantas desligar já (6 contra 16): resolvido pelo escalonamento.

**Minoria vencedora.** Sim, em quatro pontos. (1) Por post (A, E, H, L; J1 e J2 inclinam para o mesmo lado): dá atribuição por peça, a única base para contar o funil com as ferramentas de hoje, e evita colisão de duas automações com a mesma palavra. (2) Fora de peça da TV (B, E, H, L): o ganho esperado é perto de zero (posts de 169 com 0 comentário) e o custo de errar recai sobre a relação com a Mirna e com a emissora, cujos termos vetam uso comercial do conteúdo [fato 137; leitura do conselho, não parecer jurídico]. (3) 16 fora, em 2 passos (A, D, L, N): a regra "uma por mês" é do CLAUDE.md e a decisão de 21/10 já mandava parar. (4) Sem o reforço de pulo (B): não há dado que o sustente, e ele só reduz os posts elegíveis numa meta que já está perto do teto.

**Primeira ação.** O Bruno desliga CASE, ETAPAS de comentário, FUNIL, CAIXA e a ESTRATEGISTA de conta toda até dom 25/10 18h29, e liga antes das 21h a ESTRATEGISTA só do reel do case. Dono: Bruno (ou a agência, se ele pedir por escrito). Prazo: 1 dia. Custo: de 10 a 15 min [PRIOR].

**Dado que mudaria a decisão.** Um disparo real de terceiro; a resposta do Bruno sobre o perfil do disparo da CHECKLIST [a buscar 13]; o teste de duas automações com a mesma palavra; a reação da Mirna ou da produção.

**Critério de abandono.** Até qua 18/11, 0 disparo de terceiros e 0 conversa de 30 min agendada: a TABULEIRO não liga em dezembro e o pedido passa a resposta privada à mão com o link do teste. Leitura parcial em qua 04/11 [fato 181].

**Previsão.** Disparos de TABULEIRO de perfis que não são do Bruno, somados de 24/10 a 22/11 (`listCommentAutomationLogs`), lidos em seg 23/11: valor 1; faixa de 0 a 4; chance de 3 ou mais: 0,06. Conversa de 30 min agendada até 18/11, pelo número do Bruno: chance de 1 ou mais, 0,15 (o brief de 21/10 dava 0,2 [fato 169]).

**Teste mais barato.** O teste de ponta a ponta com um perfil de terceiro até dom 01/11 (10 min do Bruno, R$ 0).

**Força da evidência.** Fraca para a palavra-chave (n pequeno, sempre perto de zero, na conta e no mercado). Forte para o estado das automações e para a regra de uma resposta privada por comentário (descrição da ferramenta, nível 2).

---

## 3. Grade das 4 semanas

Horário de São Paulo. "PZ" = PostZen, agendado pela agência depois do ok semanal. "Mão" = o Bruno no app. Stories de 26 a 31/10 seguem a tabela do D4 (`05-debates/D4.md`, seção 5.1). Vagas de reel de S2 a S4 seguem a ordem fixa do D2 e o teto de 3 reels da TV por semana.

### S1 · dom 25/10 a sáb 31/10 (antes da exibição)

| Dia | Feed com a pausa mantida (estado das 19h42) | Feed com a ordem do Bruno até seg 26/10 17h | Stories e mão | Leitura |
|---|---|---|---|---|
| dom 25/10 | 12h car02 "Prazer" (ok até 10h); 21h reel do case de 6 para 20 (decisão do Bruno) | igual | 09h00 frase 3 (PZ); 09h02 caso (PZ com ok, senão mão); 12h00 Dentista B com enquete (mão); 12h30 link (mão); 18h00 frase 4 (PZ); 20h30 chamada do case (PZ); 21h05 compartilhar o case (mão) | 08h30 `listPosts`; 08h45 ETAPAS desligada; 21h Dentista B com 24 h |
| seg 26/10 | sem reel (vaga com motivo: pausa) | 21h tl01 | 12h00 balão O2 (PZ); 12h01 virada (PZ); 17h32 link (mão); com a ordem: contagem às 09h00 (PZ) | 12h05 balão saiu; 21h05 Módulo 7 e portão G1 |
| ter 27/10 | 12h car03 (ou car02, se não saiu no domingo); 14h R1 Trial Reel (mão) | 12h car01; 14h R1 Trial; 16h pf01 e 16h01 cartão do caso | 14h30 balão O8 (PZ); 14h32 virada (PZ); 16h01 link (mão; 16h02 com o pf01) | 21h case com 48 h |
| qua 28/10 | 21h Dentista C só com G1 | 21h pb01 | 12h00 balão O3 (PZ); 12h01 virada; 17h32 CRITÉRIO; 17h33 link (mão) | 21h tl01 com 48 h (portão do tl02) |
| qui 29/10 | 21h R1 no feed, como TESTAR, só se a opção de Trial Reel não apareceu na terça; senão sem reel | sem reel | 12h00 balão O4 (PZ); 12h01 virada; 17h31 MÉTODO XEQUE-MATE; 17h32 link (mão) | 14h R1 com 48 h |
| sex 30/10 | 21h nicho 1 se o bloco 1 saiu até qua 23h59 | 21h pb02 | 12h00 balão O6 sem pedido (PZ); 12h01 virada; 12h02 link (mão); 17h30 ALINHAMENTO; 17h31 DIAGNÓSTICO · 30 MIN | 18h ok semanal da S2 e prazo do horário da exibição |
| sáb 31/10 | 18h30 nicho 2 se gravado; senão vaga com motivo escrito | 18h30 tl02 com o portão do tl01 | 12h00 balão O5 (rótulo pela regra); 12h01 virada; 12h03 link (mão); 19h30 enquete TEMPO / MEDO (mão) | leitura de story |

Contagem da S1 com a pausa mantida: case mais 1 a 4 reels, conforme G1, bloco 1 e R1; abaixo de 3, motivo escrito. Com a ordem até seg 17h: case, tl01, pb01, pb02, tl02 = 5 reels; car01 e car02 = 2 carrosséis.

### S2 · dom 01/11 a sáb 07/11 (semana da exibição)

| Dia | Feed | Stories e mão | Leitura |
|---|---|---|---|
| dom 01/11 | 12h car04 "Os 5 Lances"; sem reel | 09h frase (PZ); com a pausa levantada, 09h mc04 (PZ); 17h30 pilar (PZ); link (mão) | bio, link e fixados prontos até 12h; teste de ponta a ponta até 23h59; 21h05 freio da família da TV (se n de 2 ou mais) |
| seg 02/11 (Finados, exibição) | 21h ci01 só com horário confirmado até sex 30/10 18h e exibição antes das 21h; senão sem reel | com a pausa levantada: 09h "NA TV CÂMARA CAMPINAS · SEG, 02/11" (PZ, hora só com fonte); story com a hora e a menção à Mirna (mão, só com fonte); 21h05 compartilhar o ci01 (mão); 21h10 "Chegou pela TV Câmara? Me manda um oi no direct e conta a sua área." (PZ). Com a pausa mantida: só a frase das 09h e o pilar | 19h Módulo 7 pelos agentes; lista do Bruno até ter 03/11 11h |
| ter 03/11 | 12h car05 "Os 30 minutos"; 14h R2 Trial (se o R1 fez 42 ou mais); 21h ci01 se não saiu em 02/11 | 12h00 balão O9 (PZ); 12h01 virada; 17h30 pilar; link (mão); destaque NA TV só com o ok | 09h agentes leem a página do programa (até 09/11) |
| qua 04/11 | 21h po01 (pausa levantada) ou vaga pela ordem fixa | balão O10; virada; pilar; link | diagnóstico parcial; bloco 2 até 23h59 |
| qui 05/11 | 21h vaga (nicho 1 ou Dentista C pelo G1) | balão O11; virada; pilar; link | |
| sex 06/11 | 21h vaga (nicho 2 ou remake) | balão O12; virada; pilar; link | 18h ok semanal da S3 |
| sáb 07/11 | 18h30 tl03 com o portão do tl02 (pausa levantada) ou vaga | frase; pilar; compartilhar (mão) | |

### S3 · dom 08/11 a sáb 14/11

| Dia | Feed | Leitura |
|---|---|---|
| dom 08/11 | 12h car06 Saga, parte 1 | |
| seg 09/11 | 21h vaga | 12h00 respostas de story em 14 dias; 19h Módulo 7; plano B do D6 |
| ter 10/11 | 12h car07 "Curso, mentoria ou comando"; 14h R3 Trial (se o R2 fez 42 ou mais) | |
| qua 11/11 | 21h vaga | conferência do nicho (n de 3); saldo de seguidores de 25/10 a 08/11; prazo da prévia do tl04 à Mirna; bloco 3 até 23h59 |
| qui 12/11 | 21h vaga | |
| sex 13/11 | 21h vaga | piso de seguidores de 28/10 a 10/11; 18h ok semanal da S4 |
| sáb 14/11 | 18h30 tl04 com o portão do tl03 e a prévia feita, ou vaga | |

Stories da S3 e da S4: molde do D4 (09h00 frase; 12h00 balão e 12h01 virada nos dias úteis; 17h30 pilar; link e compartilhamento à mão, no máximo 2 por dia).

### S4 · dom 15/11 a sáb 21/11, e dom 22/11

| Dia | Feed | Leitura |
|---|---|---|
| dom 15/11 (feriado) | 12h car08 Saga, parte 2 | reel e carrossel de feriado não fecham PARAR sozinhos |
| seg 16/11 | 21h vaga | 19h Módulo 7 |
| ter 17/11 | 12h car09 "Para quem é e para quem não é" | |
| qua 18/11 | 21h vaga | conferência de diagnóstico e de seguidores (brief de 21/10); prazo da prévia do tl05 à Mirna; bloco 4 até 23h59 |
| qui 19/11 | 21h vaga | último dia útil de balão do D4 |
| sex 20/11 (feriado) | 21h vaga, sem usar a data | |
| sáb 21/11 | 18h30 tl05 com o portão do tl04 e a prévia feita, ou vaga | |
| dom 22/11 | 12h car10 (abre a S5) | |
| seg 23/11 | | 18h30 tl05 com 48 h; 19h Módulo 7 decide a S5; contagem final da TABULEIRO |

---

## 4. Plano de execução com dono, prazo e custo

Mídia paga: R$ 0 até 18/11 [fato 169]; nenhum anúncio com conteúdo da TV [fato 137]. Minutos do Bruno: [ESTIMATIVA com PRIOR], de 130 a 200 na S1 e de 80 a 150 por semana depois, dos quais a gravação é de 36 a 54 na S1. Agência: horas de produção, sem custo de mídia.

| Quando | Dono | Ação | Custo |
|---|---|---|---|
| sáb 24/10, até 21h | Bruno ou agência com ok | Opcional: direct da TABULEIRO com os 5 Lances e &p=dentista no botão | 5 min |
| sáb 24/10, noite | agência | Render dos 5 balões com "Responde este story" (2 versões de rótulo) e do caso das 09h02; início do car02 e do remake R1 | de 2 a 3 h [ESTIMATIVA: 30 min, 36 min e 1 a 2 h] |
| sáb 24/10, noite | Bruno | Cópia dos renders da TV do scratchpad para o Drive, em pasta restrita (nunca no repositório público) | 15 min |
| dom 25/10, 08h30 | Bruno | Ok das frases 3 e 4 e do caso | 2 min |
| dom 25/10, 08h30 e 08h45 | agentes | `listPosts` (pausa) e `listCommentAutomations` (ETAPAS de story desligada) | 5 min |
| dom 25/10, antes de 09h02 | Bruno | Desligar a ETAPAS de resposta de story | 2 min |
| dom 25/10, 10h | Bruno | Ok da grade da S1 (duas versões) e do texto do car02 | 10 min |
| dom 25/10, 16h | Bruno | Mensagem única: pausa, print da Mirna, @, horário | 10 min |
| dom 25/10, 18h29 | Bruno | Desligar CASE, ETAPAS de comentário, FUNIL, CAIXA, ESTRATEGISTA de conta toda | 10 min |
| dom 25/10, 20h | Bruno | Respostas sobre o reel do case (seção 7, item 2) | 5 min |
| dom 25/10, até 20h30 | agência | Case no PostZen; ESTRATEGISTA ligada só a ele, com botão para /tabuleiro/?o=ig-case; chamada das 20h30 | 20 min |
| dom 25/10, 21h | Bruno | Rótulo das 6 frases e ok dos balões | 5 min |
| seg 26/10, 12h | Bruno | Dia e hora do bloco 1 | 2 min |
| seg 26/10, 18h | agência | Teleprompter do bloco 1 (consórcio sem ABAC, nutricionista, vídeo de 02/11, aberturas) | 30 min |
| seg 26/10, 21h05 | agentes | Módulo 7: Dentista B com 48 h, G1, régua escrita | de 30 a 45 min |
| ter 27/10, 14h | Bruno | R1 como Trial Reel pelo app (teste de elegibilidade) | 5 min |
| qua 28/10, 23h59 | Bruno | Bloco 1 de gravação | de 36 a 54 min |
| qui 29/10 | agência | Edição do nicho 1 e 2 e colagem das aberturas no ci01 e nos ob; folhas de quadros | de 3 a 6 h [ESTIMATIVA, fato 112] |
| sex 30/10, 18h | Bruno | Ok semanal da S2; horário da exibição, se tiver; troca do rótulo do balão de sáb, se for o caso | 15 min |
| sex 30/10 | Bruno | Política de privacidade do site corrigida (nega rastreamento enquanto o GA4 carrega), antes de qualquer anúncio (cadeira A) | sem dado |
| sáb 31/10 | Bruno | Desligar as outras 10 automações | 10 min |
| dom 01/11, 12h | Bruno | Bio do Módulo 2, Nome, link /tabuleiro/?o=ig-bio, 3 fixados | 15 min |
| dom 01/11, 23h59 | Bruno | Teste de ponta a ponta da TABULEIRO com perfil de terceiro | 10 min |
| seg 02/11, 19h | agentes | Módulo 7 do feriado; lista do Bruno até ter 03/11 11h | 45 min |
| toda segunda, 18h | Bruno | Números do funil (GA4, WhatsApp, conversas marcadas e feitas, "abriu com preço", origem) | 10 min |
| toda quarta, 23h59 | Bruno | Bloco de gravação | de 24 a 36 min |
| toda sexta, 18h | Bruno | Ok semanal; agência agenda a semana seguinte | 15 min |
| qua 11/11 e qua 18/11 | Bruno | Prévia do tl04 e do tl05 à Mirna (só com a pausa levantada) | 5 min cada |

---

## 5. Metas e critérios de parar ou escalar

| Métrica | Base | Meta | Leitura | Parar ou cair | Escalar |
|---|---|---|---|---|---|
| Alcance em 48 h por formato | régua sobre 53 [fato 24] | 42 ou mais | toda segunda, 19h | PARAR abaixo de 42 ou pulo acima de 75% com n de 2 | DOBRAR com 106 ou mais e pulo abaixo de 60%, n de 2 |
| Família da TV | sem dado (n de 0) | média de 42 ou mais | dom 01/11 21h05 e seg 09/11 | sai do feed (D1) | teto de 3 sobe com DOBRAR |
| Nicho, 3 primeiros reels | Dentista A 169 [fato 30] | mediana de 53 ou mais, pulo até 75% | qua 11/11 | nicho para; n menor que 3, "não testado" | 1 nicho com 106 ou mais abre a TABULEIRO da linha |
| Visitas ao perfil por dia, 02 a 04/11 | 10,6 a 11,0 [fato 15; leitura 19h42] | 21 ou mais | qua 04/11 | sem ação na grade; revisar bio | manter bio e fixados; ler cliques |
| Seguidores, saldo de 25/10 a 08/11 | -5 em 12 a 21/10 [fato 17] | positivo | qua 11/11 | registrar | registrar |
| Seguidores, ganho de 28/10 a 10/11 | 0 e -2 nas últimas semanas [fato 18] | 12 ou mais | sex 13/11; conferência em 18/11 | revisar oferta e público em 16/11 | manter |
| Respostas de story em 14 dias | 6 [fato 56] | 12 | seg 09/11 12h | 0 a 2: pedido cai para 2 por semana | 12 ou mais: DOBRAR o pedido |
| Contas de story em 7 dias | 342 [FATO 19h23] | 342 ou mais | toda segunda, 19h | 2 leituras abaixo: estáticos a mais pelo PostZen | manter |
| Disparos de TABULEIRO de terceiros | 0 [fato 117] | 3 ou mais até 22/11 | parcial 04/11; final 23/11 | 0 e 0 conversa em 18/11: sai em dezembro | 1 disparo real abre o 2º post da linha |
| Conversas de 30 min marcadas | sem dado; vendas 0 [fato 8] | 1 ou mais até 18/11 | 04/11 e 18/11 | 0 em 18/11: revisar oferta e público | registrar origem |
| Execução das ações do Bruno | 3 sim em 8 [fato 125] | 100% das até 3 ações por rodada | toda segunda | abaixo de 50% em 2 rodadas: modo metade | volta ao plano cheio na rodada seguinte |
| Views da edição no site | mediana 80,5; máximo 1.400 [fato 136] | 150 ou mais até 09/11 | 09/11 | informativo | informativo |

---

## 6. Riscos e plano B

| Risco | Sinal | Chance | Plano B |
|---|---|---|---|
| A pausa não cai ou cai tarde | sem ordem escrita até sex 30/10 18h | sem dado (motivo da pausa sem dado) | o mapa do D1 leva a série para depois; sem ordem até 09/11, sai do ciclo; o feed roda pela ordem fixa do D2 |
| O Bruno não grava | nenhum arquivo até qua 28/10 23h59 | alta [PRIOR, fato 104 e 105] | piso de 5 min de aberturas; remakes escalonados; Dentista C pelo G1; vaga vazia com motivo; modo metade |
| Execução à mão fraca | linha "feito" abaixo de 50% | alta [PRIOR, fato 125] | teto de 2 à mão por dia; balões pelo PostZen; 3 ações por rodada; modo metade automático |
| Reação da Mirna ou da produção | pedido para segurar peças; incômodo com efeitos ou marcação | de 3% a 10% [PRIOR, cadeira A] | nada amplia o uso da imagem sem ok escrito; prévia do tl04 e do tl05; sem TABULEIRO nem anúncio em peça da TV; série volta para "depois" pelo mapa |
| O case de 6 para 20 como está | comentário apontando o "1.282 comentários" que a conta não tem; pedido do cliente para tirar o nome | sem dado | recomendações da seção 7, item 2; arquivar o reel é reversível |
| A TV traz pouca gente | visitas abaixo de 21 por dia de 02 a 04/11 | média [PRIOR; fato 136: mediana de 80,5 views] | a TV como prova (link, destaque, bio), não como motor; vagas voltam para nicho e remakes |
| Automação de conta toda disparando em comentário de parabéns | log de CASE ou ESTRATEGISTA em post da TV | alta se ficarem ligadas [hipótese 46] | desligar até dom 18h29; ESTRATEGISTA só do case |
| Perda do estoque do scratchpad | ambiente reciclado | sem dado | cópia no Drive restrito até sáb 24/10 à noite; refazer o passe de vídeo custa cerca de 3 h 15 min [fato 111] |
| Leitura enganosa | views sobem por volume de stories; anúncios saindo da janela de 30 dias; seguidores com 2 dias pendentes | alta, comprovada no dia [debate D4] | contas no lugar de views; só orgânico em 7 dias com hora fixa; saldo até 08/11 só em 11/11 |
| Trial Reel indisponível | opção ausente no app em ter 27/10 | sem dado [a buscar 7] | R1 vai ao feed como TESTAR na próxima vaga |
| Dentista C contra a norma | Res. CFO 196/2019 não lida | sem dado | C não sai sem a leitura e o ok escrito |

---

## 7. Decisões que dependem do cliente

Cada item tem prazo e o que vale se não houver resposta.

1. **Pausa da TV.** Levantar ou manter, por escrito, com data e hora. Prazo: dom 25/10 16h para o mapa cheio; a hora da resposta define o encaixe (D1). Sem resposta: pausa mantida e grade da coluna "pausa mantida".
2. **Reel do case de 6 para 20 (dom 25/10 21h).** A decisão de publicar é do Bruno e está mantida. O conselho recomenda, até dom 20h: (a) tirar do cartão final o número "1.282 comentários" e os perfis de exemplo, ou não usar o cartão, porque a conta não tem esses comentários e o comprador que conferir vai ver; (b) confirmar com o cliente, por escrito, o uso do nome da empresa (o 02-provas proíbe o nome nesta série); (c) trocar, na legenda, "comenta ESTRATEGISTA" por uma pergunta aberta, mantendo a ESTRATEGISTA ligada só a este reel para quem seguir o CTA falado. Sem resposta: vai como o Bruno decidiu, e a ESTRATEGISTA de conta toda vira a do reel, que é a proteção mínima.
3. **Mirna.** Print da liberação; @; se a liberação cobre publicar antes de 02/11, convite de colaboração, destaque permanente e prévia dos efeitos do tl04 e do tl05. Prazo: com a mensagem do item 1. Sem resposta: marcação só pelo app, sem convite, sem destaque, tl04 e tl05 fora do feed.
4. **Horário da exibição.** Prazo: sex 30/10 18h. Sem resposta: ci01 em ter 03/11 21h e chamada de 02/11 sem hora.
5. **Gravação.** Dia e hora do bloco 1 até seg 26/10 12h; minutos por semana. Sem resposta: piso de aberturas e ordem fixa.
6. **Automações.** 6 até dom 25/10 (ETAPAS de story até 09h02, as outras 5 até 18h29) e 10 até sáb 31/10; quem executa (o Bruno ou a agência com pedido escrito). Sem resposta: risco aberto e registrado na rodada de 26/10.
7. **Bio, Nome, link e fixados.** Até dom 01/11 12h.
8. **Stories.** Ok das 08h30 de domingo; rótulo das 6 frases e ok dos balões até dom 21h; ok semanal toda sexta 18h.
9. **Trial Reel.** Testar no app na ter 27/10 14h e escrever a regra de contagem (fora dos 5 reels).
10. **Dentista C.** Ok escrito, com a Res. CFO 196/2019 lida, para o portão G1.
11. **Definição de diagnóstico.** "O Primeiro Lance" é a conversa de 30 min e é o que conta na meta; "O Tabuleiro" é o teste. Prazo: dom 01/11, junto com a bio.
12. **Números de segunda até 18h.** GA4, WhatsApp, conversas marcadas e feitas, "abriu com preço", origem. Sem número: "sem dado".
13. **Feriado de 02/11.** Disponibilidade para o story com a hora e a menção à Mirna. Prazo: sex 30/10.
14. **Votos do tl01.** Contagem à mão até seg 02/11, se o tl01 sair.
15. **Política de privacidade.** Corrigir até sex 30/10, antes de qualquer anúncio.
16. **Cópia do estoque.** Drive restrito, hoje à noite.

---

## 8. Como o conselho chegou aqui

1. **Enquadramento** (14h45): 6 decisões, pesos fixos, 22 perguntas, checklist do pedido, gatilhos de escalada (4 de 5 presentes) e modo god.
2. **Pesquisa** (13h42 a 15h45, refeita depois da data de 02/11): 8 frentes (auditoria da conta, playbook do Buzzfy, nicho e TV no mercado, entrevista, capacidade e estoque, stories e objeções, horários e portão, funil). Só leitura.
3. **Livro de fatos** (15h50): 185 fatos com fonte e nível, 43 a buscar, 33 a derivar e 62 palpites de nível 4 (14 PRIOR e 48 hipóteses), mais 11 correções a números usados nas decisões.
4. **14 cadeiras isoladas** (16h17 a 18h20): A guardião de regras; B advogado do diabo; C executor; D automação e atendimento; E concorrência; F voz do comprador; G marca e posicionamento; H página e conversão; I mídia paga; J forasteiro; K otimista de crescimento; L primeiros princípios; M pessimista de risco; N comercial consultivo. Juntas, 1.215 ideias numeradas (A 90, B 86, C 85, D 89, E 87, F 84, G 88, H 85, I 83, J 87, K 85, L 90, M 88, N 88). O número é só contexto: volume não prova nada.
5. **5 juízes** (18h28 a 18h44), cada um com uma lente: J1 retorno e risco de verba; J2 comprador real; J3 execução rápida; J4 técnica e mensuração; J5 diferenciação. Posição média: D 4,6; H 5,0; I 5,4; M 6,0; N 6,2; G 6,4; B 7,2; C 7,4; L 7,6; E 7,8; F 8,0; K 9,4; A 10,0; J 14,0. J foi o último nos 5 juízes por premissas vencidas (promessa antiga do tl01 e agenda sem leitura do PostZen).
6. **Votos:**

| Decisão | Mais votada | Votos | Probabilidade agregada (faixa) |
|---|---|---|---|
| D1 | (c) | 11 de 14 (e, a e d com 1 cada) | 0,16 (0,04 a 0,38) |
| D2 | (a) | 12 de 14 (e com 2) | 0,26 (0,06 a 0,50) |
| D3 | (a) | 10 de 14 (e com 3, d com 1) | 0,13 (0,02 a 0,35) |
| D4 | decisão do moderador | 14 de 14 depois do debate, em 13 grafias; antes, (c) com 0,64 | 0,22 (0,08 a 0,40) |
| D5 | (a) | 12 de 14 (e com 2) | 0,16 (0,03 a 0,50) |
| D6 | (c) | 12 de 14 (e com 2) | 0,08 (0,01 a 0,30) |

7. **Debate** só no D4 (19h23 a 19h40), o primeiro a ler a pausa. 11 cadeiras mudaram de posição citando a pausa e o fato 143 (voto de enquete sem leitura).
8. **Falhas que os juízes apontaram e este plano corrige:** a meta do D4 chamava de 2x o que era 1x; a meta do D6 fica perto do teto (de 3,7 a 5,5 comentários de qualquer tipo); a base do D5 eram 3 decisões não executadas, e não 2; o critério do D1 citava a promessa antiga do tl01 e 124 como máximo de views; o saldo de seguidores até 08/11 só fecha em 11/11; o estoque pronto existe só no scratchpad; várias grades da S1 não casavam com os stories já agendados.
9. **O que este presidente acrescentou:** as leituras das 19h42; o mapa da porta da pausa; o reel do case e os riscos dele; o story das 19h30 que não saiu; o repositório público e o destino da cópia do estoque; o po01 para depois por causa do case; os fixados com peças que já estão no perfil.
10. **Limites:** as 14 cadeiras, os 5 juízes e o presidente são instâncias do mesmo modelo; todos os planos e julgamentos são anteriores à pausa; quase toda comparação da conta tem n de 1 a 4 e período confundido com formato; nenhuma ferramenta permitida lê enquete, WhatsApp, GA4, agenda ou comentário escrito; a audiência da TV é sem dado.

## Fontes

- `run/00-enquadramento.md`; `run/01-fatos.md`; `run/01-pesquisa/F1` a `F8`; `run/02-cadeiras/plano-A.md` a `plano-N.md` (resumos e posições); `run/03-julgamento/J1.md` a `J5.md` (resumos); `run/05-debates/D4.md`.
- `contexto.md`; `/home/user/Disparo-/CLAUDE.md`; `stories-objecoes/05-manuais-bruno.md`, `06-agenda-postzen.md` e `04-estaticos.json` (com as notas não commitadas lidas às 19h50); `entrevista-tv-camara/pecas-e-calendario.md`; commit 6a17563.
- PostZen `listPosts` e `listCommentAutomations`, conta j97772ycndetk3f1wcdbh14p898g4b8w, lidos às 19h42 de 24/10.
- Buzzfy `ig_account_stats` (7 dias), lido às 19h42 de 24/10.
- Folha de quadros `scratchpad/tv/ig/case-6-20-folha.jpg` e `ls` de `scratchpad/tv/ig/` (19h55); `ffprobe` do `case-6-20.mp4` (54,3 s, 1080x1920).
- GitHub REST `repos/brunodjs-source/Disparo-` (visibility public), 19h50.
