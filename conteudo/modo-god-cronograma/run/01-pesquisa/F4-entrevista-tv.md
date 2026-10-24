# F4 · Entrevista à TV Câmara · a série em três tempos em torno de seg 02/11

Frente F4 da pesquisa do conselho Agência Reunida para @o_estrategista.com.br. Rodada de sábado, 24/10/2026, escrita às 15h15 (São Paulo), depois do fato novo: a entrevista vai ao ar na **segunda-feira, 02/11/2026** (mensagem do Bruno: "Vai pro ar segunda dia 2" e "pode seguir pois as postagens vou marcar ela"). Substitui a versão das 14h deste arquivo, escrita quando a data era sem dado (histórico no git, commit 88433c7).

Somente leitura: nada foi publicado, agendado ou alterado no Instagram, no Buzzfy ou no PostZen, e nenhuma mensagem foi enviada. Toda mudança abaixo é uma ação para o Bruno executar, com prazo.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha objeção sozinho. Métrica que falta: "sem dado".

**Régua (uma só no arquivo):** alcance em 48 h contra a mediana de 53 do enquadramento. Limites [ESTIMATIVA, conta sobre 53]: 0,5x = 27; 0,8x = 42; 2x = 106; TABULEIRO = 150. Pulo: corte em 75% (catálogo, seção 8). Hot streak: a marca do próprio `ig_reel_checkup` (3x o normal dele, 57 views), lida como está, sem converter para alcance.

---

## 0. Resposta curta

1. **Três tempos.** ANTES (sáb 24/10 a dom 01/11): bastidor e quem é o Bruno, com "SEG, 02/11" no texto de cada peça. NO DIA (seg 02/11, Finados): chamada para assistir só nos stories, com o horário quando houver fonte, e um reel só, o ci01, às 21h. DEPOIS (ter 03/11 a sáb 21/11): "o que eu disse na TV", com po01, tl03, tl04, tl05 e o link da edição exibida.
2. **Ficam na data:** tl01 (dom 25/10, 18h30), pb01 (seg 26/10, 21h), car01 (ter 27/10, 12h), pf01 em story (ter 27/10, 16h), pb02 (sex 30/10, 21h) e tl02 (sáb 31/10, 18h30). **Mudam:** ci01 de qua 28/10 para **seg 02/11, 21h**; po01 de qui 29/10 para **qua 04/11, 21h**, com uma condição de volta (seção 8). tl03, tl04 e tl05 ficam nos sábados 07, 14 e 21/11, todos depois da exibição.
3. **Por que esses dois mudam:** o ci01 é a peça com mais da Mirna (voz em 2 trechos e o rosto em 10,7 s) e a frase dele já foi anunciada hoje com a data: o story das 19h30 é "Nem tudo que vemos é ouro" com o rótulo "NA TV · SEGUNDA, 02/11" [FATO, `listPosts`]. O po01 é o método, a peça mais perto do diagnóstico, e ganha com a prova de que foi ao ar. Os dois são os assuntos 5 e 7 do índice do tl01, cuja legenda promete "O mais votado eu solto inteiro depois que a entrevista for ao ar" [FATO, `listPosts`]. E a semana da exibição está vazia no PostZen [FATO]: os dois são peças prontas para ela.
4. **Ritmo:** a S1 (25 a 31/10) tem hoje 6 reels agendados, acima da regra de 5 [FATO, `listPosts`; CLAUDE.md]. Com as duas mudanças fica com 4 reels da TV e 1 vaga (qui 29/10, 21h) para a cadeira de nicho. A S2 (01 a 07/11), hoje com 1 reel (tl03), passa a 3 reels prontos da TV e 2 vagas.
5. **Exceção medida:** se o `ig_reel_checkup` marcar hot streak no tl01 ou no pb01 até ter 27/10, 21h, o ci01 volta para qua 28/10, 21h como sequência (protocolo de 48 h do playbook) e o po01 assume seg 02/11, 21h. Dado vence plano.
6. **Mirna:** marcação na mídia à mão pelo Bruno no app; @ dela no texto da legenda pelo PostZen; menção com sticker em 3 stories feitos à mão; 1 convite de colaboração, no ci01, só com o @ e com o ok dela antes. O PostZen aceita até 3 colaboradores em reel, carrossel e foto, e não em story; marcação de pessoa pela API só em foto única [FATO, esquema de `createPost`/`updatePost` do PostZen lido nesta rodada, sem chamar]. @ da Mirna: sem dado.
7. **Achado novo, com consequência no "depois":** os termos de uso da TV Câmara liberam compartilhar link e citar trecho com a emissora como fonte, e vetam republicar conteúdo integral sem autorização e usar o conteúdo da emissora para fins comerciais [FATO, tvcamaracampinas.com.br/termos, atualizados em 24/05/2026, lido às 15h06]. Depois de 02/11: nada de recortar a edição exibida nem filmar a tela da TV. O "depois" usa a gravação do celular do Bruno (fonte de todas as peças) e o link da edição.
8. **Horário de 02/11: sem dado.** A grade de 02/11 não está publicada: o site redireciona qualquer data depois de 25/10 para 24/10 [FATO, 15h03]. Nesta semana o Ser Empreendedor passa 4 vezes por dia (01h, 06h, 13h, 18h) [FATO, grade de 24/10]. 9 das 17 edições com data calculável foram publicadas no site numa segunda (data de publicação, que não é necessariamente a de estreia) [FATO, conta sobre a página do programa]. Pedir o horário à Mirna é a única fonte antes do dia.

---

## 1. Fontes conferidas nesta rodada

| # | Fonte | Consulta (somente leitura) | Hora (SP) | Resultado |
|---|---|---|---|---|
| 1 | `contexto.md`, `00-enquadramento.md` (versão 14h45), `CLAUDE.md` | leitura | 15h00 | lidos |
| 2 | `entrevista-tv-camara/pecas-e-calendario.md` (versão 14h41) e `catalogo-formatos.md` (seções 1, 5, 6, 7 F1 a F3, 8) | leitura | 15h00 | lidos |
| 3 | `run/01-pesquisa/F1-auditoria-conta.md` e `F2-playbook-buzzfy.md` (versões desta rodada, 14h57 e 15h00) | leitura de trechos | 15h01 | lidos |
| 4 | `stories-objecoes/03-plano-7-dias.md` e `02-provas.md` (lista do que não pode ser dito) | busca e leitura | 15h08 | lidos |
| 5 | PostZen `listPosts`, conta j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 a 30/11 | leitura | 15h03 | 20 itens: 4 stories publicados hoje, 16 agendados |
| 6 | PostZen `listCommentAutomations`, mesma conta | leitura | 15h04 | 17 automações ativas; 1 disparo somado (CHECKLIST); TABULEIRO com 0 |
| 7 | Esquema das ferramentas PostZen `createPost` e `updatePost` | leitura da definição, sem chamar | 15h05 | campos de Instagram conferidos (seção 2) |
| 8 | Buzzfy `ig_posts` (stories ativos) | leitura | 15h03 | 5 stories ativos (09h33 fora do PostZen; 14h00, 14h03, 15h00, 15h01) |
| 9 | Buzzfy `ig_post_stats` (os 5 stories) | leitura | 15h04 | ok, todos provisórios |
| 10 | Buzzfy `buzzfy_playbook` (captions) | leitura | 15h12 | ok |
| 11 | tvcamaracampinas.com.br: início, /programacao/2026-11-02, /programacao/2026-10-26, /programas/ser-empreendedor, /ao-vivo, /programacao, /termos, /politica-editorial, /equipe | `curl` de leitura | 15h03 a 15h10 | sem www: 301 (redirecionamento, não erro); com www: 200 em todas. As duas datas futuras caem em /programacao/2026-10-24 |
| 12 | Fichas `videos/tv-camara/cortes/*.spec.json` (18) e `videos/tv-camara/dados/transcricao.json` | leitura e conta em Python | 15h08 a 15h14 | ok |
| 13 | Lâminas 1 e 2 do car01, baixadas da mídia do próprio post no PostZen | leitura e conferência visual | 15h12 | ok |

Erros de consulta: nenhum. O 301 do domínio sem www e o redirecionamento das datas futuras estão registrados como o que são (redirecionamento), não como "programa sem exibição".

---

## 2. O que mudou desde a versão das 14h

**PostZen** [FATO, `listPosts`, 15h03]
- tl02 a tl05 **estão agendados**: sáb 31/10, 07/11, 14/11 e 21/11, todos 18h30. O contexto.md (14h38) ainda diz "proposto e ainda não agendado": vale o PostZen.
- Legenda do tl01: "A entrevista vai ao ar na segunda, 02/11." e "O mais votado eu solto inteiro depois que a entrevista for ao ar." A promessa do sábado saiu. A legenda do tl02 também traz "A entrevista vai ao ar na segunda, 02/11."
- As legendas de pb01, car01, ci01, po01 e pb02 não citam a data. Três dizem "na TV" no passado: ci01 ("Na TV eu disse"), po01 ("do jeito que eu expliquei na TV") e pb02 ("Contei esse caso na TV Câmara Campinas").
- De dom 01/11 a sex 06/11 não há nada agendado. Depois de sex 30/10, o feed tem 1 reel por semana (os timelapses).
- Stories de 25/10 em diante: só o pf01 (ter 27/10, 16h). Os stories do 03-plano-7-dias ainda não estão no PostZen.

**PostZen, o que a API faz no Instagram** [FATO, esquema de `createPost`/`updatePost`, lido sem chamar]
- `collaborators`: até 3 usuários convidados como colaboradores, em foto, reel e carrossel. Story: não.
- `userTags` (marcar pessoa na mídia): só em foto única. Reel, carrossel e story: não. Confirma o contexto.md.
- `firstComment`: primeiro comentário depois de publicar, em foto, reel e carrossel.
- `trialParams`: Trial Reel com graduação MANUAL ou SS_PERFORMANCE, só em conta profissional que o Instagram tenha liberado; conta sem liberação falha na hora de publicar. Se esta conta está liberada: sem dado. (Insumo para a cadeira de remakes; o enquadramento dava "se o PostZen agenda Trial Reel" como sem dado.)

**TV Câmara Campinas** [FATO, site, 15h03 a 15h10]
- Onde assistir, nas palavras do site: "sinal aberto digital 11.3 UHF, NET canal 4, Vivo Fibra canal 9 e YouTube", mais o portal; a página /ao-vivo responde 200.
- Grade: só a semana corrente (19 a 25/10). Nela, a mesma edição de Ser Empreendedor ("Negócios para o público Infantil") passa às 01h, 06h, 13h e 18h. A grade de 26/10 em diante não está no ar.
- Página do programa: 20 edições listadas. Views de 27 a 1.400; mediana de 80,5; 4 das 20 com 150 ou mais [FATO, conta sobre a lista]. Das 17 com data calculável (15 com data e 2 com "há 2 dias" e "há 5 dias"), 9 caem numa segunda [FATO, `date`]. Os vídeos têm id de YouTube no endereço e o portal sincroniza o canal oficial pela API do YouTube [FATO, endereços e /termos].
- Instagram da emissora, como o próprio site linka: instagram.com/tvcamaracampinas [FATO].
- Termos de uso (seção 0, item 7). A página /equipe não cita a Mirna; o nome dela vem do contexto.md e da transcrição.

**Stories de hoje** [FATO, `ig_post_stats`, 15h04, provisórios]
| Hora | Peça | Vida | Alcance | Views | Respostas | Navegação |
|---|---|---|---|---|---|---|
| 09h33 | vídeo fora do PostZen | 5,5 h | 27 | 39 | 0 | 21 avanços, 6 deslizes, 3 saídas |
| 14h00 | st01, bastidor (vídeo) | 1 h | 12 | 23 | 0 | 8 avanços, 2 deslizes, 2 saídas |
| 14h03 | estático de bastidor | 1 h | 10 | 16 | 0 | 7 avanços, 1 saída |
| 15h00 | "A pergunta da TV" | menos de 1 h | 0 | 1 | 0 | abaixo de 5 viewers |
| 15h01 | mc01 (voz da Mirna) | menos de 1 h | 0 | 0 | 0 | abaixo de 5 viewers |

Leitura: n de 1 por peça e menos de 2 h de vida. Serve para registrar que os stories da TV saíram e estão sendo vistos, não para comparar.

**Playbook** [FATO, `buzzfy_playbook` captions]: "an @mention or collab 1.13×"; "Tag who's in it: collaborators, places, brands"; pedidos: salvar 1,16x, seguir 1,12x, enviar 1,10x; "comenta aqui" e "link na bio" não somaram.

**Onde a Mirna aparece em cada peça** [FATO, campos `planos` e `falantes` das fichas; capa do car01 conferida a olho]

| Peça | Imagem dela | Voz dela |
|---|---|---|
| tl01 | plano aberto, os dois na mesa | nenhuma fala marcada |
| pb01 | Z2 (os dois na mesa) de 0 a 8,75 s | não |
| car01 | capa: os dois na mesa, Mirna de frente | não |
| pf01 (story) | Z2 de 0 a 6,45 s | não |
| ci01 | Z2 de 4,95 a 9,0 s e de 16,95 a 23,6 s (10,7 s) | 2,35 a 2,95 s ("Ainda?") e 4,95 a 8,8 s |
| po01 | Z2 o tempo todo (23,7 s) | não |
| pb02 | Z2 de 0 a 12,7 s | não |
| tl02 | plano aberto | 15,7 a 16,8 s ("O que?") |
| tl03 | plano aberto e tela dividida | a pergunta "você foi investindo em equipamento?" abre o reel (fonte 1518,68 a 1521,02 s, falante M na transcrição) |
| tl04 | plano aberto e "Uau!" com recorte no rosto | 2,2 a 4,5 s e 25,35 a 27,4 s |
| tl05 | rosto congelado com o carimbo "AINDA?" e o selo "REPÓRTER" (29,52 a 30,0 s) | 24,15 a 27,1 s e 29,5 a 30,15 s |
| mc02, mc03, mc04 | não (plano CB, só o Bruno) | não |
| mc01, st01 (já publicados) | mc01: CB; st01: bastidor | mc01: 3 trechos |

---

## 3. A série em três tempos

Horário de São Paulo. "PostZen" = já agendado; "mover" e "editar" = ação do Bruno no PostZen; "à mão" = postado pelo Bruno no app. Só a série da TV e o que encosta nela; o resto da grade é de outras cadeiras.

### 3.1 ANTES · sáb 24/10 a dom 01/11 · bastidor, quem é o Bruno, contagem

Objetivo: apresentar o Bruno e a entrevista sem pedir que ninguém assista ainda, com a data em todo texto. Nenhuma peça diz "foi ao ar", "assista" ou "ao vivo".

| Data | Hora | Peça | Tipo | Status | O que muda |
|---|---|---|---|---|---|
| sáb 24/10 | 14h00 a 15h01 | st01, bastidor, "A pergunta da TV", mc01 | story | publicados | nada |
| sáb 24/10 | 19h30 | "Nem tudo que vemos é ouro" · NA TV · SEGUNDA, 02/11 | story | PostZen | nada: vira a semente do ci01 de 02/11 |
| dom 25/10 | 09h01 | mc02 (CB, só o Bruno) | story | 03-plano, não agendado | trocar o rótulo para "NA TV · SEG, 02/11" ao agendar |
| dom 25/10 | 18h30 | **tl01** | reel | PostZen | legenda já certa; @ da Mirna na legenda se chegar antes |
| dom 25/10 | 18h35 | compartilhar o tl01 | story | à mão | **sticker de menção da Mirna** (1ª de 3) e primeiro teste de marcar pessoa no reel publicado |
| seg 26/10 | 17h30 | mc03 (CB, só o Bruno) | story | 03-plano | rótulo "NA TV · SEG, 02/11" |
| seg 26/10 | 21h00 | **pb01** | reel | PostZen | editar legenda (seção 5); marcar a Mirna depois de publicar |
| ter 27/10 | 12h00 | **car01** | carrossel | PostZen | editar legenda; marcar a Mirna na capa |
| ter 27/10 | 16h00 | pf01 | story | PostZen | nada (story agendado não leva menção) |
| qua 28/10 | 21h00 | sem reel da TV (o ci01 sai daqui) | | mover | chamada das 20h30 e compartilhamento das 21h05 do 03-plano vão para 02/11 |
| qui 29/10 | 21h00 | vaga para a cadeira de nicho (o po01 sai daqui) | | mover | chamada e compartilhamento do po01 vão para 04/11 |
| sex 30/10 | 21h00 | **pb02** | reel | PostZen | editar legenda; marcar a Mirna |
| sáb 31/10 | 18h30 | **tl02** | reel | PostZen | portão do tl01 (seção 8) e o trecho de 10,4 s sem voz real (seção 4) |
| dom 01/11 | 09h00 | mc04 recortado em 1707,82 s (7,2 s) com o rótulo "SEG · 02/11 · TV CÂMARA CAMPINAS" | story | agendar | é a véspera; sai depois do tl02, como manda a regra do laço |
| dom 01/11 | quando houver hora | contagem regressiva com o horário confirmado | story | à mão | só com o horário vindo da Mirna ou da grade; sem horário, não sai |

**Contagem sem story novo:** a contagem é o rótulo "NA TV · SEG, 02/11" nos estáticos de TV do 03-plano de 25/10 a 31/10 (e1, e2 e as manchetes), como o story de hoje às 19h30 já faz. Custo: reexportar imagem, sem gravação. O 03-plano já tem 27 stories à mão por semana [FATO, 03-plano]; esta frente só acrescenta stickers nos stories à mão que já existem e a contagem da véspera.

**Opcional (cadeira de stories):** qui 29/10, caixa de perguntas "O que você perguntaria se fosse a repórter?" (pré-estreia do catálogo, F2). As respostas abastecem o "depois".

### 3.2 NO DIA · seg 02/11 (Finados) · chamada para assistir

| Hora | Peça | Tipo | Como | Condição |
|---|---|---|---|---|
| 09h00 | Estático com foto do Bruno (avatar com a torre): "SEG · 02/11 · NA TV CÂMARA CAMPINAS" / "Programa Ser Empreendedor, com a repórter Mirna Abreu" / "Canal 11.3 aberto, NET 4, Vivo Fibra 9 e tvcamaracampinas.com.br" | story | agendado | sem hora, sem "hoje", sem "ao vivo" (vetado no 02-provas) |
| assim que o horário for confirmado | "SEG · 02/11 · ÀS __H NA TV CÂMARA CAMPINAS" com **sticker de menção da Mirna** (2ª de 3) e sticker de link para tvcamaracampinas.com.br/ao-vivo (texto do link: "Assistir na TV Câmara") | story | à mão | se o horário já tiver passado de manhã (01h ou 06h), pular e ir para o "Foi ao ar" |
| 12h00, se a hora seguir sem dado | "A partir de hoje, 02/11, na TV Câmara Campinas." com link para tvcamaracampinas.com.br/programacao (texto: "Horários na programação") | story | à mão | a grade da semana deve aparecer no site na própria segunda [HIPÓTESE, pelo que se viu hoje: só a semana corrente fica no ar] |
| depois do horário confirmado | Selfie do Bruno, sem a tela da TV no quadro: "Foi ao ar." | story | à mão | só com o horário confirmado; nada de filmar a exibição (termos de uso; logo da emissora vetado no catálogo) |
| 18h30 | Módulo 7: o tl02 fecha 48 h e a S1 inteira está lida [F2, seção 9.1] | rodada | | registrar em `semanas/2026-11-02.md` |
| 20h30 | chamada "SEG · 21H · NO FEED" do ci01 | story | agendado | apagar às 21h05 |
| **21h00** | **ci01** (de qua 28/10) | reel | mover | legenda versão A agendada; versão B só depois do horário confirmado (seção 5); convite de colaboração se houver @ e ok |
| 21h05 | compartilhar o ci01 com **sticker de menção da Mirna** (3ª de 3) | story | à mão | |

Um reel só no dia. O ob02, que o 03-plano punha em seg 02/11 às 21h [FATO, 03-plano], vai para outro dia da S2 (decisão da cadeira de objeções): o ci01 está pronto e no PostZen; o render do ob02 é sem dado [FATO, 00-enquadramento, item 9].

Por que 21h: é depois do horário das 18h, se a grade de 02/11 repetir a desta semana [HIPÓTESE], e é o horário de reel dos dias úteis com média de 73 de alcance em 5 posts [FATO, contexto.md, `ig_best_times`; amostra pequena]. Alcance em feriado: sem dado.

### 3.3 DEPOIS · ter 03/11 a sáb 21/11 · o que eu disse na TV

| Data | Hora | Peça | Tipo | Status | Nota |
|---|---|---|---|---|---|
| ter 03/11 | 09h00 | repost do ci01 com enquete "Concorda com o que eu disse na TV?" | story | à mão (era qui 29/10 no 03-plano) | |
| ter 03/11 | quando a edição estiver no site ou no YouTube | "A entrevista inteira está aqui" com link da página do vídeo | story | à mão | compartilhar link é livre pelos termos; conferir antes em que minuto o Bruno aparece na edição exibida; vai para o destaque PROVA |
| ter 03/11 | | resultado da votação do tl01 | story | à mão | mapa na seção 7 |
| **qua 04/11** | **21h00** | **po01** (de qui 29/10) | reel | mover | legenda nova (seção 5); marcar a Mirna |
| sáb 07/11 | 18h30 | **tl03** "A pergunta da TV" | reel | PostZen | paga o story "A pergunta da TV" de hoje; 2º convite de colaboração só se ela aceitou o 1º |
| sáb 14/11 | 18h30 | **tl04** | reel | PostZen | portão; mostrar à Mirna o "Uau!" recortado antes de marcar |
| sáb 21/11 | 18h30 | **tl05** | reel | PostZen | portão; mostrar à Mirna o carimbo "AINDA?" no rosto dela antes de marcar |
| manhãs | | mc01 a mc04 e trechos de 10 a 15 s nos stories | story | 03-plano | |

Vagas da S2 que esta frente não preenche: 2 reels (cadeiras de objeção e de nicho: ob01 a ob03 se renderizados, pf01 como reel, nicho) e os 2 carrosséis (só o car01 está pronto; car02 não pede gravação). REACT 01 ("Fui ao ar na TV Câmara Campinas. Olha o que eu respondi...") só se o Bruno gravar os 20 min de selfie; entra no lugar de um sábado que falhar no portão.

Corte publicado antes de 02/11 (tl01, pb01, car01, pb02, tl02) não volta ao feed depois como "o que eu disse na TV", salvo como remake com 2 mudanças reais e como Trial Reel [FATO, `buzzfy_playbook` second_life, via F2].

---

## 4. Peça por peça: fica ou muda

| Peça | Hoje no PostZen | Decisão | Motivo | Prazo para mexer |
|---|---|---|---|---|
| tl01 | dom 25/10, 18h30 | **Fica** | Bastidor é conteúdo de "antes" por natureza; legenda já avisa 02/11 e já tirou a promessa do sábado [FATO]; abre com o Bruno de frente | nenhum (só o @ dela na legenda, se chegar até dom 18h30) |
| pb01 | seg 26/10, 21h | **Fica** | Trajetória (DJ por 20 anos): apresenta o Bruno, não entrega caso nem método; abre a dupla PB que o Módulo 7 de 02/11 lê com n de 2 (regra de n mínimo do enquadramento) | legenda até seg 26/10, 20h59 |
| car01 | ter 27/10, 12h | **Fica** | (1) Único carrossel pronto: a S1 fica com 1, sem ele com 0. (2) A capa repete a frase do mc01 de hoje ("Eu só tinha um computador e um sonho"): 3 dias depois, o tema continua; em 04/11 ficaria a 3 dias do tl03, que paga o mesmo tema ("um bom computador"). (3) Os minutos das lâminas contam da gravação do celular (lâmina 2: "min 03:29") e não devem bater com a edição exibida, que é um bloco de um programa de 30 a 47 min [FATO, catálogo; HIPÓTESE sobre o descompasso]; antes de 02/11 ninguém compara. Ressalva: a capa já diz "O que eu disse na TV sobre começar" [FATO, lâmina 1]; vale como literal (ele disse à TV), sem "foi ao ar" | legenda até ter 27/10, 11h59 |
| pf01 (story) | ter 27/10, 16h | **Fica** | Story da tarde do dia do nicho dentista; expira em 24 h; liga com a linha do Dentista B. Não leva menção (story agendado) | nenhum |
| ci01 | qua 28/10, 21h | **Muda para seg 02/11, 21h** | (1) A frase dele já foi anunciada hoje com "NA TV · SEGUNDA, 02/11". (2) É a peça com mais Mirna (voz e rosto): é a candidata natural ao convite de colaboração, e o convite faz mais sentido no dia em que o trabalho dela vai ao ar [HIPÓTESE]. (3) Reduz a exposição dela antes da exibição enquanto o ok da produção é só verbal [FATO, pecas-e-calendario item 2; enquadramento]. (4) É o assunto 5 do índice do tl01: sai "depois que for ao ar", como a legenda promete | **decidir até ter 27/10, 21h** (leitura de hot streak); mover no PostZen até qua 28/10, 20h59, para 2026-11-03T00:00:00Z |
| po01 | qui 29/10, 21h | **Muda para qua 04/11, 21h** (com condição) | (1) Método Xeque-Mate: a peça mais perto do diagnóstico, na semana em que a exibição soma prova [HIPÓTESE]. (2) Assunto 7 do índice: cumpre a promessa do tl01. (3) A Mirna está no quadro o tempo todo: marcação depois da exibição. (4) A S2 está vazia. Condição: se a vaga de qui 29/10, 21h, não tiver peça aprovada pela cadeira de nicho até qua 28/10, 12h, o po01 fica onde está (regra de 5 reels e de vaga não vazia vence a preferência desta frente) | decidir até qua 28/10, 12h; mover até qui 29/10, 20h59, para 2026-11-05T00:00:00Z |
| pb02 | sex 30/10, 21h | **Fica** | (1) Fecha a dupla PB (pb01 e pb02 mudam só o assunto) com n de 2 antes do Módulo 7 de 02/11: o portão decide com 2 posts se o material da mesa em 3/4 segura no feed antes de pôr ci01 e po01 na S2. (2) Mantém a S1 com volume. (3) O pedido de direct funciona antes ou depois | legenda até sex 30/10, 20h59 |
| tl02 | sáb 31/10, 18h30 | **Fica** (com portão) | Último reel antes da exibição; legenda já avisa 02/11 [FATO]. Ficha com 41% de voz real e o maior trecho sem voz real de 10,4 s (16,55 a 26,95 s), acima do teto de 8 s do catálogo [FATO, conta sobre `voz_trechos`] | portão do tl01 em ter 27/10, 18h30 (seção 8); arquivo corrigido até sex 30/10 ou aceitar o risco por escrito |
| tl03 | sáb 07/11, 18h30 | **Fica** | Depois da exibição: "A pergunta da TV" vira o que a TV perguntou de fato. Paga o story "A pergunta da TV" de hoje | portão de seg 02/11 |
| tl04 | sáb 14/11, 18h30 | **Fica** | Origem (pai pioneiro) é o assunto 1 do índice, sem outra peça | portão de seg 09/11; Mirna ver o recorte antes |
| tl05 | sáb 21/11, 18h30 | **Fica** | Fecha a série com o mesmo assunto do ci01 em outro formato (muda uma coisa) | portão de seg 16/11; Mirna ver o carimbo antes |
| mc02 | 03-plano: dom 25/10, 09h01 | **Fica** | Só o Bruno no quadro e na voz: zero exposição de terceiro antes da exibição | agendar até sáb 24/10 |
| mc03 | 03-plano: seg 26/10, 17h30 | **Fica** | idem | agendar até dom 25/10 |
| mc04 | 03-plano: sáb 31/10, 11h (trocado pelo estático e1) | **Muda para dom 01/11, 09h**, recortado | Véspera da exibição; depois do tl02, que paga a frase. Recorte em 1707,82 s ("eu construí tudo através da profissão"), 7,2 s, dentro da faixa de 7 a 10 s do catálogo e antes de "que hoje eu executo como estrategista digital" (1707,82 a 1710,18 s) [FATO, transcrição]. O 03-plano propõe cortar entre 1705,2 e 1705,7 s, o que dá cerca de 5 s; a cadeira de stories escolhe ouvindo | render e agendamento até sáb 31/10 |
| st01, mc01 | publicados hoje | | | |

Contagem da S1 depois das mudanças: tl01, pb01, pb02, tl02 e 1 vaga = 5 reels; car01 = 1 carrossel. S2: ci01, po01, tl03 e 2 vagas = 5 reels.

**Correções de ficha que seguem valendo** (nenhuma pede gravação): o ticker dos 4 mc traz "Uma profissão por 20 anos" isolado, que o 01-objecoes manda usar só como carreira na noite [FATO, campo `ticker` e 01-objecoes, linha 301]; no ci01, a ficha marca "Ainda. Sempre vai ser." como fala do Bruno (2,95 a 4,8 s) e a transcrição marca como da Mirna (1380,8 a 1382,38 s) [FATO]: ouvir antes de convidar a Mirna, porque ela vai ver a peça e a legenda usa um estilo por voz.

---

## 5. Legendas ajustadas (prontas para colar)

Conferidas: sem travessão, sem emoji, sem promessa de resultado, sem nomes vetados, no máximo uma "não é X, é Y", nada da lista do 02-provas ("ao vivo", "entrevista exclusiva", "fui convidado pela TV", "a TV Câmara recomenda", "rede nacional"). A linha entre colchetes só entra com o @ real da Mirna; sem ele, sai inteira. Hashtags: as mesmas 5 de hoje.

**pb01** (seg 26/10, 21h)
> Fui DJ por 20 anos. Na entrevista à TV Câmara Campinas eu contei por que isso nunca foi uma aventura.
> A entrevista vai ao ar na segunda, 02/11, no programa Ser Empreendedor.
> Antes do digital, eu aprendi como funcionava a noite, as casas e as festas. Foi ali que comecei a fazer estratégia de divulgação, muito antes de chamar isso de lançamento.
> [Entrevista com @usuario_da_mirna.]
> Manda para um expert que vai lançar este ano.

**car01** (ter 27/10, 12h)
> Eu só tinha um computador e um sonho. Quatro frases que eu disse na entrevista à TV Câmara Campinas, com o minuto de cada uma na gravação.
> A entrevista vai ao ar na segunda, 02/11.
> [Entrevista com @usuario_da_mirna.]
> Qual delas pesa mais no seu próximo lançamento? Comenta o número.
> Vai lançar nos próximos 90 dias? Me manda a data no direct.

("na gravação" evita que alguém compare os minutos com a edição exibida. Os dois pedidos já estavam na legenda agendada; a cadeira de playbook decide se fica um só.)

**pb02** (sex 30/10, 21h)
> Um restaurante que vendia 45 mil. Colocamos ele para vender 250 mil com o marketing digital.
> Contei esse caso na entrevista à TV Câmara Campinas, que vai ao ar na segunda, 02/11. O número de um caso não se repete igual em outro negócio. O que se repete é a ordem: entender o produto antes de anunciar.
> [Entrevista com @usuario_da_mirna.]
> Vai lançar nos próximos 90 dias? Me manda a data no direct.

**ci01, versão A** (agendada para seg 02/11, 21h; vale com ou sem horário confirmado)
> Até hoje o melhor marketing é o olho no olho.
> Essa conversa com a repórter Mirna Abreu [@usuario_da_mirna] está na edição do programa Ser Empreendedor que a TV Câmara Campinas exibe a partir de hoje, 02/11.
> Na entrevista eu disse que nem tudo que vemos é ouro. Muita gente vende o que não consegue cumprir, e o cliente chega machucado. Por isso o encontro ainda decide a venda.
> Segue o perfil: os próximos trechos da entrevista saem aqui.

**ci01, versão B** (o Bruno troca a linha 2 no app só depois do horário confirmado)
> Essa conversa com a repórter Mirna Abreu [@usuario_da_mirna] foi ao ar hoje no programa Ser Empreendedor, da TV Câmara Campinas.

(Pedido de seguir de 02 a 04/11: regra de sequência do playbook, 1,12x, adaptada a quem chega pela TV [HIPÓTESE, F2 trava E3]. "Os próximos trechos saem aqui" é verdade: po01 em 04/11 e tl03 em 07/11 estão agendados. O vídeo termina com "Manda para quem precisa ouvir isso." [FATO, ficha]: são dois pedidos, um falado e um escrito.)

**po01** (qua 04/11, 21h)
> O Método Xeque-Mate do jeito que eu expliquei na entrevista à TV Câmara Campinas: os gatilhos corretos, cada jogada, cada posicionamento e o momento certo.
> [Entrevista com @usuario_da_mirna, no programa Ser Empreendedor.]
> Qual dessas peças falta no seu lançamento? Comenta qual delas.

("Comenta a palavra" não dizia qual palavra [FATO, F1]. O pedido de comentário casa com o que o vídeo já pede no fim [FATO, ficha: "Qual dessas peças falta no seu lançamento? Comenta."]. Nenhuma das peças (gatilho, jogada, posicionamento, momento) dispara automação [FATO, `listCommentAutomations`].)

**tl03, tl04, tl05** (linha nova, só depois do horário de 02/11 confirmado)
> A entrevista foi ao ar no dia 02/11, no programa Ser Empreendedor, da TV Câmara Campinas. [Com @usuario_da_mirna.]

---

## 6. Marcação da Mirna e convite de colaboração

### 6.1 O que cada caminho faz

| Caminho | Quem faz | Onde vale | O que se sabe |
|---|---|---|---|
| @ no texto da legenda | Bruno, no PostZen antes de publicar ou no app depois | reel, carrossel | Regra medida mais próxima: "@mention or collab" 1,13x [FATO, playbook]. Que o @ no texto vira link e avisa a pessoa quando o post sai pela API: [PRIOR] sim, conferir no tl01 |
| Marcar pessoa na mídia | Bruno, no app, depois de publicar | reel, carrossel (na capa) | O PostZen só marca em foto única [FATO, esquema]. Se o app deixa marcar num reel já publicado, editando: sem dado; [PRIOR] deixa. Teste: tl01, dom 25/10, 18h35 |
| Sticker de menção no story | Bruno, no app, na hora de postar | story à mão | Story agendado no PostZen não leva sticker, e story publicado não aceita sticker depois [FATO, 03-plano]. Que a pessoa mencionada recebe aviso e pode repostar no próprio story com um toque: [PRIOR] |
| Convite de colaboração | Bruno, no PostZen (campo `collaborators`, até 3) antes de publicar, ou no app | reel, carrossel, foto; story não | [FATO, esquema]. Se ela aceitar, o post aparece também no perfil dela e para quem a segue, com os mesmos números [PRIOR]. Se a conta dela precisa ser pública ou profissional para receber o convite pela API: sem dado; o convite pode falhar na publicação |

Tudo depende do @ dela, que é sem dado para os agentes. O Bruno disse que vai marcar: o primeiro passo é ele pôr o @ nas legendas agendadas e anotar no arquivo da semana em quais peças marcou.

### 6.2 Onde marcar

- **Marcar (legenda e mídia):** toda peça de feed com imagem ou voz dela: tl01, pb01, car01 (na capa), pb02, tl02, ci01, po01, tl03, tl04, tl05.
- **Não marcar:** mc02, mc03 e mc04 (só o Bruno no quadro) e ob01 a ob03 se a imagem dela não aparecer (no 03-plano a voz dela fica fora e a pergunta entra só como texto). Marcar onde ela não aparece é ruído para ela [HIPÓTESE].
- **tl04 e tl05:** mostrar a ela antes, por mensagem do Bruno, o "Uau!" recortado no rosto (tl04) e o carimbo "AINDA?" com o selo "REPÓRTER" sobre o rosto congelado (tl05) [FATO, fichas]. Marcar alguém num efeito sobre o rosto dela sem ela ter visto é risco de relação [HIPÓTESE].

### 6.3 Menção nos stories: 3 momentos, não toda hora

1. dom 25/10, 18h35: compartilhamento do tl01 (bastidor; primeira peça com ela no feed).
2. seg 02/11, story com o horário: é a chamada que ela tem motivo para repostar [HIPÓTESE].
3. seg 02/11, 21h05: compartilhamento do ci01.

Mais menções só se ela repostar alguma das três. Quantas menções ela aceita sem cansar: sem dado.

### 6.4 Convite de colaboração (só se o Bruno tiver o @ e ela disser que topa)

- **Pedir antes, junto com o resto:** o Bruno já precisa falar com a Mirna para guardar o print da liberação. Na mesma conversa: o @, o horário de 02/11, se publicar antes de 02/11 está ok para a produção e se ela aceita ser colaboradora em 1 reel. Agentes não mandam mensagem; quem pergunta é o Bruno.
- **1º convite: ci01, seg 02/11, 21h.** Ela fala nele e está no quadro 10,7 s; o post sai no dia em que o trabalho dela vai ao ar. Colocar o @ no campo de colaboradores do post m177cf21jjcv7fa2y1q1twc4n58gwe0n até seg 02/11, 20h59.
- **2º convite: tl03, sáb 07/11, 18h30**, só se ela aceitou o 1º. A pergunta dela abre o reel.
- **Sem convite** nas peças antes de 02/11 e em pb01, pb02 e po01 (ela está no quadro, mas não fala). A emissora (@tvcamaracampinas, linkado no site dela [FATO]) não recebe convite: é emissora pública do Legislativo, os termos vetam uso comercial do conteúdo dela, e um convite num perfil que vende diagnóstico tende a ser recusado [HIPÓTESE]. Citar o nome da emissora em texto continua valendo (catálogo, seção 5).
- **Se ela recusar ou não responder:** o post segue só no perfil do Bruno, sem mudança na grade. Não reenviar convite.

### 6.5 O que não fazer

- Não recortar, filmar ou republicar a edição exibida (termos de uso da TV Câmara). O link da edição pode.
- Não mostrar a tela da TV com a marca da emissora (catálogo, seção 5).
- Não usar "ao vivo" em nenhum texto (02-provas), nem na chamada; o endereço /ao-vivo vai só no link.
- Não usar peça da entrevista em anúncio pago sem autorização por escrito que cubra anúncio: a liberação da Mirna é verbal e fala de uso nas redes do Bruno [FATO, contexto.md]; os termos da emissora vetam uso comercial do conteúdo dela; se a gravação de bastidor do celular do Bruno conta como conteúdo da emissora: sem dado (não é parecer jurídico).
- Não escrever "foi ao ar" antes do horário confirmado (legenda, story ou capa).

### 6.6 Como medir

- O efeito da marcação não se separa por post: o Buzzfy não mostra de onde veio o alcance [FATO, F1, item 8]. Medir por semana: alcance de não seguidores no `ig_account_stats` antes e depois de 02/11.
- O Bruno anota: se ela repostou cada uma das 3 menções (sim ou não), se aceitou o convite (sim, não, sem resposta).
- ci01 com colaboração aceita contra a dupla PB sem colaboração: alcance em 48 h. n de 1, formato diferente (CINEMA contra PB): só indício.
- Semana da exibição: visitas ao perfil por dia de 02 a 04/11 contra 10,6 por dia [ESTIMATIVA do enquadramento: 74 / 7]; seguidores de 02 a 04/11 no `ig_follower_growth`; views da edição do Bruno no site da TV contra a mediana de 80,5 das 20 últimas [FATO, conta desta rodada].

---

## 7. A promessa do tl01 depois da exibição

Legenda: "Comenta o número do assunto que você quer ver inteiro. O mais votado eu solto inteiro depois que a entrevista for ao ar." [FATO, `listPosts`]. Contagem à mão pelo Bruno até seg 02/11 (nenhuma ferramenta desta rodada lê o texto dos comentários). Regra do catálogo: com menos de 5 votos somados, seguir o plano e dizer isso nos stories, sem fingir votação [FATO, catálogo F5]. Os 12 últimos reels tiveram 0 comentário cada e a conta teve 14 comentários em 30 dias [FATO, contexto.md e versão anterior desta frente]: menos de 5 votos é o mais provável [HIPÓTESE].

| Voto | Assunto | Como cumpre depois de 02/11 |
|---|---|---|
| 5 | Nem tudo que vemos é ouro | ci01, seg 02/11, 21h |
| 7 | Método Xeque-Mate | po01, qua 04/11, 21h |
| 6 | Zero reais | tl03, sáb 07/11 (a pergunta do investimento e a resposta) |
| 1 | Desde criancinha | tl04, sáb 14/11 (pai pioneiro e pai que estimulava); se for o mais votado com 5 votos ou mais, o tl04 troca de lugar com o tl03 e sai em 07/11 |
| 2, 3 ou 4 | 20 anos, restaurante, franquia odontológica | já saíram antes (pb01, pb02, pf01): story de ter 03/11 com o post e o link da edição exibida no minuto em que o assunto aparece, conferido na edição |

"Inteiro", para qualquer assunto, também se cumpre pelo link da edição exibida, que é a entrevista inteira.

---

## 8. Portões e exceções (régua: alcance em 48 h, mediana 53)

| Quando | Leitura | Se | Então |
|---|---|---|---|
| ter 27/10, 18h30 a 21h | `ig_reel_checkup` (marca de hot streak) no tl01 (48 h) e no pb01 (24 h) | hot streak em qualquer um | **ci01 volta para qua 28/10, 21h** (sequência em 24 a 48 h do playbook; mesmo material, outro assunto: muda uma coisa). seg 02/11, 21h, fica com o po01; qua 04/11 vai para a grade (ob01 ou nicho) |
| ter 27/10, 18h30 | tl01 com 48 h (`ig_post_stats`) | alcance de 42 ou mais e pulo abaixo de 75% | tl02 fica no sáb 31/10 |
| | | alcance de 27 a 41, ou pulo de 75% ou mais | tl02 sai do feed (story em trechos de 15 s ou Trial Reel, se a conta for liberada); a vaga de sáb 31/10 vai para a grade |
| | | alcance abaixo de 27 | a família de timelapses sai do feed; tl03 a tl05 viram stories e banco; os sábados vão para formato com rosto |
| qua 28/10, 12h | grade da cadeira de nicho | qui 29/10, 21h sem peça aprovada | po01 fica em qui 29/10 (nenhuma mudança no PostZen) |
| seg 02/11, 18h30 | Módulo 7: pb01 e pb02 com 48 h | média abaixo de 27, ou pulo médio de 75% ou mais nos dois | ci01 e po01 saem do feed da S2 e vão para stories em 15 s; a vaga fica com formato de rosto de frente (Bruno falando para a câmera: mediana de 167,5 de alcance [FATO, F7 via enquadramento]) |
| seg 02/11, 09/11 e 16/11 | timelapse do sábado anterior | abaixo de 42 com pulo de 75% ou mais | o próximo timelapse sai do sábado e vai para o banco (regra do pecas-e-calendario) |

---

## 9. Ações que só o Bruno executa (com prazo)

| Até | Ação | Onde |
|---|---|---|
| assim que possível, antes de dom 25/10, 18h30 | Falar com a Mirna: print da liberação, @ dela, horário de 02/11, ok para publicar antes de 02/11, se aceita 1 convite de colaboração | conversa dele com ela |
| dom 25/10, 18h35 | Compartilhar o tl01 com menção à Mirna; testar se o app deixa marcar pessoa no reel publicado e anotar o resultado | app |
| seg 26/10, 20h59 | Legenda do pb01 (seção 5) | PostZen m17dqk63b0e1hk75xcevdwmc458gwmfn |
| ter 27/10, 11h59 | Legenda do car01 | PostZen m174q9y41reqfn4eqhqrm124f58gwzbr |
| ter 27/10, 21h | Ler hot streak de tl01 e pb01 e decidir o ci01 (seção 8) | Buzzfy |
| qua 28/10, 20h59 | Mover o ci01 para seg 02/11, 21h (2026-11-03T00:00:00Z) e trocar a legenda pela versão A | PostZen m177cf21jjcv7fa2y1q1twc4n58gwe0n |
| qui 29/10, 20h59 | Mover o po01 para qua 04/11, 21h (2026-11-05T00:00:00Z), salvo a condição da seção 8, e trocar a legenda | PostZen m17ersdnwmmsk5e7fyw4jqwfdx8gwcxt |
| sex 30/10, 20h59 | Legenda do pb02 | PostZen m1718n57yvmtpyb4xnf3zsw7fn8gwe7q |
| sáb 31/10 | Agendar mc04 recortado para dom 01/11, 09h | PostZen |
| dom 01/11 | Contagem da véspera, só com o horário confirmado | app |
| seg 02/11 | Stories do dia (seção 3.2), versão B do ci01 só depois do horário, convite de colaboração se combinado | app e PostZen |
| seg 02/11 a sex 06/11 | Procurar a edição na página do programa e no YouTube da emissora; postar o link quando sair | site da TV Câmara |
| depois de cada publicação com ela | Marcar a Mirna e anotar "marcada: sim ou não" no arquivo da semana | app |

---

## 10. Lacunas

- Horário de exibição em 02/11: sem dado. A grade de 02/11 não está publicada (redireciona para 24/10); o padrão de 4 horários por dia é desta semana e de outra edição.
- Se a edição do Bruno estreia em 02/11 e reprisa a semana toda: sem dado ([HIPÓTESE] pela grade desta semana).
- Quando a edição sobe no site e no YouTube: sem dado (9 de 17 edições com data numa segunda).
- Minuto em que o Bruno aparece na edição exibida: sem dado.
- @ da Mirna, tamanho e tipo da conta dela, se aceita marcação em série e colaboração: sem dado.
- Se o app deixa marcar pessoa em reel e carrossel já publicados: sem dado (teste no tl01).
- Se o @ no texto da legenda publicada pela API avisa a pessoa: [PRIOR] sim, sem fonte nesta rodada.
- Se a liberação verbal da Mirna vale como ok da produção para publicar antes de 02/11: sem dado; print pendente.
- Se a gravação de bastidor do celular conta como conteúdo da emissora para os termos de uso: sem dado.
- Audiência da TV: sem dado; só as views do site (mediana de 80,5 nas 20 últimas edições, máximo de 1.400).
- Alcance da conta em feriado (02/11, 15/11, 20/11): sem dado.
- Votos do tl01 e respostas de sticker: contagem manual.
- Quem diz "Ainda. Sempre vai ser." no ci01: ficha e transcrição divergem; ouvir.
- Se a conta está liberada para Trial Reel pela API: sem dado (falha na hora de publicar se não estiver).
- Efeito de publicar o miolo antes ou depois da exibição: sem dado na conta e no mercado; a divisão desta frente é decisão com motivo escrito, não medida.
