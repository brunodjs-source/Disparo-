# F7 · Horários e portão semanal · @o_estrategista.com.br · rodada de 24/10/2026

Frente F7 da pesquisa do conselho Agência Reunida. Leituras ao vivo, somente leitura, feitas entre 14h10 e 14h19 de sábado 24/10/2026 (horário de São Paulo). Nada foi publicado, agendado ou alterado no Instagram, no Buzzfy ou no PostZen. Toda mudança abaixo é proposta para o Bruno executar.

Etiquetas: [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha uma objeção sozinho. Métrica que falta: "sem dado".

---

## 0. Respostas curtas

1. **Nesta conta a hora é controle, não alavanca.** Seguidores online ficam entre 386 e 430 das 11h às 22h; a hora mais fraca da faixa fica 10% abaixo do pico [FATO, `ig_best_times`; ESTIMATIVA: 386 / 430 = 0,90]. Dentro do mesmo formato (12 reels de animação com voz sintética), 11h, 18h e 20h deram a mesma faixa de alcance, 13 a 40, com uma exceção de 169 [FATO, `ig_post_stats`]. O formato separa 5,2 vezes: Bruno falando para a câmera, mediana de 167,5; animação, 32,5 [FATO, `ig_post_stats`]. Proposta: hora fixa por formato, sem gastar vaga com teste de hora.
2. **O "melhor horário" do `ig_best_times` muda com o tamanho da amostra:** 25 posts dá 21h; 35 posts (F1) dá 07h; 47 posts dá 09h [FATO, 3 leituras]. A própria ferramenta baseia a recomendação nos seguidores online, não nos posts [FATO, campo `basis`]. Não serve como sinal de hora.
3. **Grade de horário proposta:** reels base no domingo 18h30 e na segunda, quarta, quinta e sexta 21h00; o 6º reel, só com portão aberto, no sábado 18h30; carrosséis terça e sábado 12h00; Trial Reel de remake na terça 18h30; stories 09h00, 12h00 e 17h30, mais a chamada e o compartilhamento colados no reel do dia; leitura dos stories todo dia às 08h30; Módulo 7 na segunda às 19h00.
4. **Portão semanal (segunda 19h00):** a semana fechada vai de domingo a sábado e, às 19h de segunda, todos os reels dela já têm 48 h (o de sábado 18h30 fecha 48 h às 18h30). O domingo seguinte é vaga base e abre sempre que existir peça com o Bruno no quadro 0. O sábado seguinte é o 6º reel e só abre com três condições juntas (seção 4.4).
5. **Uma régua só, fixa por 4 semanas, em alcance de 48 h:** 27, 42, 106 e 150; pulo 60% e 75%. Ela vem da mediana de 53 do 00-SISTEMA e foi testada contra os 19 reels da fase atual: põe 12 de 12 reels de animação na zona PARAR, 4 de 4 reels com o Bruno na zona DOBRAR e os 3 sem rosto em MANTER [FATO, conta deste relatório sobre `ig_post_stats`].
6. **Métricas mínimas:** reel PARAR com alcance mediano abaixo de 42 ou pulo mediano acima de 75% em 2 reels do formato; MANTER de 42 a 105 com pulo até 75%; DOBRAR com 106 ou mais e pulo abaixo de 60%. Carrossel PARAR abaixo de 42 em 2; DOBRAR com 106 ou mais e 2 ou mais visitas ao perfil. Story: piso semanal de 982 views e 3 respostas (base de 17 a 24/10) [FATO, `ig_account_stats` 7 dias].
7. **Exceções da S1:** o portão de segunda 26/10 roda às 21h05 (o Dentista B fecha 48 h às 21h); o sábado 31/10 se decide num portão extra na terça 27/10 às 18h35, com o tl01 em 48 h. Enquanto a legenda do tl01 disser "O mais votado sai no próximo sábado", o sábado 31/10 é promessa pública e não decisão de portão [FATO, `listPosts`].
8. **Histórico do Módulo 7 contra a régua:** a única rodada (21/10) acertou o PARAR da animação e o DOBRAR do Bruno falando. Duas decisões não foram executadas: as 17 automações de palavra-chave seguem ativas [FATO, `listCommentAutomations`] e os "Próximos 7 dias" não saíram (nada publicado de 22 a 23/10) [FATO, `ig_posts`]. O portão precisa de uma linha "executado: sim ou não".

---

## 1. Consultas feitas (todas responderam; nenhum erro de consulta)

| # | Consulta (só leitura) | Parâmetros | Hora (SP) | Resultado |
|---|---|---|---|---|
| 1 | Buzzfy `ig_best_times` | America/Sao_Paulo, posts_to_analyze=50 | 14h10 | ok; 47 posts analisados; 4 reels fora da grade deixados de fora (2023 a 2025, conferido no item 12) |
| 2 | Buzzfy `ig_best_times` | America/Sao_Paulo, padrão de 25 posts | 14h11 | ok |
| 3 | Buzzfy `ig_posts` | kind=all, since=2026-09-29, limit=50 | 14h10 | 35 itens (30/09 a 21/10), nenhum Trial Reel |
| 4 | Buzzfy `ig_post_stats` | 20 ids + 15 ids (as 35 peças) | 14h11 | ok; mediana de reel 37,5 de alcance, 57 views, 5,85 s, pulo 70,9% (20 reels); mediana de feed 49 de alcance, 134,5 views, 0,5 visita (10 posts) |
| 5 | Buzzfy `ig_reel_checkup` | limit=20 | 14h12 | ok; normal 57 views e 70,9% de pulo; janela de sequência fechada |
| 6 | Buzzfy `ig_posts` | kind=stories | 14h12 | 3 stories ativos (09h33, 14h00, 14h03) |
| 7 | Buzzfy `ig_post_stats` | os 3 stories | 14h12 | ok, provisórios |
| 8 | Buzzfy `ig_account_stats` | 30 dias e 7 dias | 14h11 | ok |
| 9 | Buzzfy `ig_follower_growth` | 30 dias | 14h11 | ok; 22 e 23/10 pendentes |
| 10 | Buzzfy `buzzfy_playbook` | overview, checklists, hot_streaks, small_accounts | 14h13 | ok |
| 11 | PostZen `listPosts` | conta j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 a 24/11, por data | 14h14 | 16 publicações: 2 já publicadas (stories 14h00 e 14h03), 14 agendadas |
| 12 | Buzzfy `ig_posts` | kind=reels, limit=30 | 14h18 | 24 reels; os 4 fora da grade são de 2023 a 2025 |
| 13 | PostZen `listPosts` | mesma conta, status=published, 20/09 a 24/10 | 14h16 | 22 publicações pelo PostZen; 6 delas são stories |
| 14 | PostZen `listCommentAutomations` | mesma conta | 14h15 | 17 automações, todas ativas |
| 15 | PostZen `listCommentAutomationLogs` | TABULEIRO e CHECKLIST | 14h15 | TABULEIRO 0 log; CHECKLIST 1 log |

Arquivos do repositório lidos: `contexto.md`, `CLAUDE.md`, `sistema-instagram/00-SISTEMA.md` (ficha, Módulo 3, Módulo 7 e Projeção), `sistema-instagram/semanas/2026-10-21.md`, `entrevista-tv-camara/catalogo-formatos.md` (seções 5, F5 e 8), `modo-god-cronograma/run/00-enquadramento.md`, `run/01-pesquisa/F1`, `F2`, trechos de `F4` e `F5`, `modo-god-nichos/run/10-decision-brief.md`, `stories-objecoes/03-plano-7-dias.md`.

---

## 2. O que os dados dizem sobre hora e dia

### 2.1 Seguidores online (média de 27 dias, hora de São Paulo)

[FATO, `ig_best_times`, 14h10]

| Hora | 07h | 09h | 11h | 12h | 13h | 15h | 17h | **18h** | 19h | 20h | **21h** | 22h | 23h |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Online | 297 | 364 | 386 | 407 | 411 | 390 | 417 | **430** | 424 | 410 | **416** | 391 | 312 |
| Fração do pico | 69% | 85% | 90% | 95% | 96% | 91% | 97% | 100% | 99% | 95% | 97% | 91% | 73% |

[ESTIMATIVA] Frações: cada hora dividida por 430.
- Platô das 11h às 22h. 21h fica 3% abaixo das 18h. Online por dia da semana: sem dado (a ferramenta só dá a média por hora).
- A recomendação da própria ferramenta é "18h às 20h", com base nos seguidores online [FATO, campo `recommendation.basis = online_followers`].

### 2.2 Posts próprios por hora: o resultado muda com a amostra

| Leitura | Posts | Mediana | "Melhores horas" | "Melhores dias" | Fonte |
|---|---|---|---|---|---|
| Padrão (25) | 25 | 35 | 21h 73 (5 posts), 12h 66 (4), 18h 49 (6) | qua 104 (3), dom 70 (4), seg 53 (9) | [FATO, `ig_best_times`, 14h11] |
| 35 posts | 35 | sem dado | 07h 185 (2), 23h 180 (2), 11h 77 (6) | sáb 180 (2), sex 134 (2), qua 126 (7) | [FATO, F1, 13h3x] |
| 50 pedidos | 47 | 58 | 09h 150 (2), 17h 144 (2), 07h 142 (3) | sáb 180 (2), qua 117 (9), dom 106 (6) | [FATO, `ig_best_times`, 14h10] |

- A amostra de 47 inclui 12 posts de 2020 a 2025, conteúdo pessoal fora do nicho [FATO, `ig_posts`: só 35 peças desde 29/09].
- Cada "melhor hora" se apoia em 2 a 5 posts. O sábado de 180 são dois posts: "Ele nunca fez um anúncio" (308) e a Saga 1 (52) [FATO, `ig_post_stats`].
- O `contexto.md` (12h40) traz uma mistura dessas leituras (23h 180, 21h 73, 11h 66, 18h 49; sáb 180, sex 134, dom 106). Nenhuma das leituras de hoje reproduz a lista inteira. Isso não muda nada na decisão, porque nenhuma delas é sinal.

### 2.3 Mesmo formato, horas diferentes

Hora de São Paulo. Alcance orgânico com mais de 48 h [FATO, `ig_post_stats`, 14h11]. Grupos pela classificação da F1 (conferência visual das capas e tags do Buzzfy).

| Grupo | Hora | n | Alcance | Mediana | Pulo mediano |
|---|---|---|---|---|---|
| Reel de animação com voz sintética | 11h00 | 3 | 33, 34, 34 | 34 | 83,8% |
| Reel de animação com voz sintética | 18h00 a 18h47 | 6 | 13, 16, 25, 32, 40, 169 | 28,5 | 83,1% |
| Reel de animação com voz sintética | 20h00 | 2 | 27, 35 | 31 | 78,7% |
| Reel de animação com voz sintética | 21h30 | 1 | 14 | 14 | 85,7% |
| Reel com o Bruno falando | 11h11 (dom) | 1 | 166 | 166 | 45,7% |
| Reel com o Bruno falando | 21h00 a 23h06 | 3 | 128, 169, 308 | 169 | 49,6% |
| Reel sem rosto | 08h06, 15h05, 22h30 | 3 | 64, 54, 58 | 58 | 55,4% |
| Carrossel com foto do Bruno | 11h00 | 1 | 63 | 63 | |
| Carrossel com foto do Bruno | 12h00 a 13h00 | 3 | 71, 98, 126 | 98 | |
| Carrossel com foto do Bruno | 17h00 (dom) | 1 | 189 | 189 | |
| Carrossel da saga, capa sem rosto visível (Saga 1) | 23h40 (sáb) | 1 | 52 | 52 | |
| Estático com foto do Bruno | 07h44 a 09h50 | 3 | 133, 237, 197 | 197 | |
| Estático com foto do Bruno | 19h00 | 1 | 111 | 111 | |

Leitura:
- [FATO] A única comparação de hora com n razoável dentro de um formato (12 reels sintéticos) não separa as horas: 11h, 18h e 20h ficam na mesma faixa. O 169 das 18h29 é o "Você gravou o curso inteiro", com 86,9% de pulo; a F1 registra a hipótese de embalo do estouro de 03/10.
- [FATO] Reel com o Bruno: 166 às 11h11 e 128 a 308 entre 21h e 23h06. Nenhum reel com o Bruno saiu entre 12h e 20h59. Efeito da hora em reel com o Bruno: sem dado.
- [HIPÓTESE] Hora explica pouco perto do formato. Ganho máximo esperado de trocar de hora dentro do platô: perto de 10% [ESTIMATIVA: diferença de online entre 11h e 18h]; diferença de formato medida: 5,2 vezes [FATO].

### 2.4 Dia da semana

[FATO, `ig_post_stats`; medianas por este relatório sobre as 35 peças de 30/09 a 21/10]

| Dia | Peças | Mediana de alcance | Composição |
|---|---|---|---|
| dom | 6 | 112 | 90% (166), Saga 2 (189), Você gravou (169), Recusa (58), Escala reel (16) e estático (35) |
| seg | 9 | 35 | 7 de 9 são animação ou cartão de texto; com o Bruno: Equipe (128), Saga 3 (126) |
| ter | 7 | 27 | 6 de 7 são animação ou cartão de texto |
| qua | 7 | 133 | Prazer (237 e 133), 100 mil (134), Dentista A (169), Saga 5 (111), Médico (64), Perpétuo (33) |
| qui | 2 | 76 | Saga 6 (98), Cem mil (54) |
| sex | 2 | 134 | Bastidor (197), Saga 7 (71) |
| sáb | 2 | 180 | Ele nunca fez um anúncio (308), Saga 1 (52) |

| Reels por grupo | Fim de semana | Dia útil |
|---|---|---|
| Bruno falando | 166 e 308 (mediana 237) | 128 e 169 (mediana 148,5) |
| Animação | 16 e 169 | 10 reels, mediana 32,5 |
| Todos os reels | 5, mediana 166 | 14, mediana 34 |

- [FATO] Dia está confundido com formato: as séries de animação caíram quase todas na segunda e na terça.
- [FATO, `buzzfy_playbook` hot_streaks e overview] Entre contas, posts de sábado e domingo ficaram em 1,10x o normal do criador; dias úteis, 0,96x. Reels a menos de 6 h do anterior: 0,92x. 5 a 7 posts por semana: 7,0% dos reels estouram; 7 ou mais: 7,7%; 3 a 5: 6,0%.
- [HIPÓTESE] Fim de semana com reel ajuda um pouco; na conta, a direção bate (Bruno: 237 contra 148,5), com n de 2 contra 2.

### 2.5 Stories

| Métrica | Valor | Fonte |
|---|---|---|
| Views de story, 30 dias | 4.227 (40% das 10.453 views orgânicas) | [FATO, `ig_account_stats` 30 dias, 14h11; ESTIMATIVA para o %] |
| Views de story, 7 dias (17 a 24/10) | 982 (53% das 1.836 views; nenhuma de anúncio) | [FATO, `ig_account_stats` 7 dias; ESTIMATIVA para o %] |
| Alcance de story, 7 dias | 337 contas | [FATO, idem] |
| Respostas, 7 dias e 30 dias | 3 e 7 | [FATO, idem] |
| Visitas ao perfil, 7 dias | 74 | [FATO, idem] |
| Cliques no site e toques no link, 7 dias | 0 e 0 | [FATO, idem] |
| Views de story por dia | cerca de 141 (4.227 / 30) e 140 (982 / 7) | [ESTIMATIVA] |
| Story de hoje 09h33 (vídeo, academia, fora do PostZen), com 4,6 h | alcance 21, views 30, 15 toques para avançar, 6 deslizes para a próxima conta, 3 saídas, 1 interação, 0 resposta | [FATO, `ig_post_stats`, provisório] |
| Saída no story das 09h33 | 9 de 24 navegações (37,5%) | [ESTIMATIVA: (6 + 3) / 24] |
| Stories de 14h00 e 14h03 (PostZen) | 4 e 2 views com 0,1 a 0,2 h; insights só com 5 ou mais espectadores | [FATO, `ig_post_stats`] |
| Stories publicados por dia nos 30 dias | sem dado (o PostZen publicou 6 em 30 dias; os postados no app não ficam registrados) | [FATO, `listPosts` published] |
| Métrica por story de dias anteriores | sem dado (o Buzzfy só lê story nas 24 h em que ele está no ar) | [FATO, nota do `ig_posts`] |

### 2.6 O que o Módulo 7 já tem como histórico

- Uma rodada só: semana de 14 a 20/10, escrita em 21/10, mais o dado novo de 24/10 (Dentista A) [FATO, `00-SISTEMA.md` e `semanas/2026-10-21.md`].
- Seguidores: de 15/10 a 21/10, 0 entrada e 5 saídas (líquido -5); 22 e 23/10 pendentes [FATO, `ig_follower_growth`, 14h11].
- Funil: TABULEIRO 0 disparo (ligada só ao Dentista B, que sai hoje 21h); CHECKLIST 1 disparo, de um perfil cujo nome começa com "bruno" (provável teste, F1) [FATO, `listCommentAutomationLogs`].

---

## 3. Horários por formato e por dia da semana (proposta)

Regra de fundo: **hora fixa por formato**, para que a hora não se confunda com o formato na leitura do portão. Nenhuma vaga é gasta com teste de hora: para medir hora seriam 4 reels do mesmo formato (2 em cada hora) para um ganho esperado de até 10% [ESTIMATIVA, seção 2.3], contra 5,2 vezes de diferença de formato [FATO].

| Dia | Feed | Hora | Stories (horas fixas) | Leitura |
|---|---|---|---|---|
| dom | Reel base | 18h30 | 09h00, 12h00, 17h30 (chamada do reel), 18h35 (compartilhar o reel) | 08h30 stories de sábado |
| seg | Reel base | 21h00 | 09h00, 12h00, 17h30, 20h30 (chamada), 21h05 (compartilhar) | 08h30 stories; **19h00 Módulo 7 e portão** |
| ter | Carrossel | 12h00 | 09h00, 14h30, 17h30 | 08h30 stories; Trial Reel de remake 18h30 (opcional) |
| qua | Reel base | 21h00 | 09h00, 12h00, 17h30, 20h30, 21h05 | 08h30 stories |
| qui | Reel base | 21h00 | 09h00, 12h00, 17h30, 20h30, 21h05 | 08h30 stories |
| sex | Reel base | 21h00 | 09h00, 12h00, 17h30, 20h30, 21h05 | 08h30 stories; 23h59 prazo de peça para sábado e domingo |
| sáb | Carrossel 12h00; **6º reel 18h30 só com portão aberto** | 12h00 e 18h30 | 09h00, 12h00, 17h30 (chamada, se houver reel), 18h35 | 08h30 stories |

Por que cada hora:

| Formato | Hora | Base | Etiqueta |
|---|---|---|---|
| Reel nos dias úteis | 21h00 | 416 online (97% do pico); 3 dos 4 reels com o Bruno saíram entre 21h e 23h06 e fizeram 128 a 308; a S1 já está agendada às 21h (pb01, ci01, po01, pb02) e o plano de stories já tem chamada às 20h30 e compartilhamento às 21h05 | [FATO, `ig_best_times`, `ig_post_stats`, `listPosts`, `03-plano-7-dias.md`] |
| Reel de domingo | 18h30 | 18h é o pico (430); o tl01 já está agendado para dom 25/10 18h30 | [FATO, `ig_best_times`, `listPosts`] |
| Reel do portão (sábado) | 18h30 | Fecha 48 h na segunda 18h30, antes do portão das 19h; fica 21h30 depois do reel de sexta 21h | [FATO, conta de horas] |
| Carrossel | 12h00 | 407 online (95%); os 3 carrosséis com foto do Bruno entre 12h e 13h fizeram 71, 98 e 126; com terça e sábado, cada dia tem um post de feed e só o sábado com portão aberto chega a 2 | [FATO, `ig_best_times`, `ig_post_stats`]; escolha do dia [HIPÓTESE] |
| Trial Reel (remake da F2) | ter 18h30 | 21h30 depois do reel de segunda e 26h30 antes do de quarta; regra de 6 h entre reels, Trial Reel incluído | [FATO, playbook 0,92x a menos de 6 h]; Trial Reel contar na regra [HIPÓTESE, F2] |
| Stories | 09h00, 12h00, 17h30 | 364, 407 e 417 online; horários já usados no `03-plano-7-dias.md` | [FATO]; efeito da hora em story: sem dado |
| Leitura de stories | 08h30 | O story das 09h00 do dia anterior ainda está no ar (23,5 h) e o das 21h05 tem 11,5 h; depois disso a métrica some | [FATO, nota do `ig_posts`] |

Regras de espaçamento:
- No máximo 1 reel de feed por dia e 6 h ou mais entre reels, Trial Reel incluído [FATO, playbook; F2].
- No máximo 2 posts de feed por dia (CLAUDE.md e catálogo). Com a grade acima, só o sábado com portão aberto chega a 2.
- Feriados (seg 02/11, dom 15/11, sex 20/11): hora mantida. Alcance em feriado: sem dado. Reel lido em feriado não fecha PARAR sozinho (precisa de outro reel do formato fora de feriado).

Diferenças contra documentos anteriores, de propósito:
- Módulo 3 pedia reels seg, ter, qua, qui e sáb às 18h30 e carrosséis qua e sex às 12h [FATO, `00-SISTEMA.md`]. A agenda real e o plano de stories já estão em 21h nos dias úteis [FATO, `listPosts`]. Sem dado de hora que justifique mexer no que já está montado.
- Catálogo, seção 8: sábado fixo 18h30 para a TV e domingo com portão [FATO]. Aqui fica o contrário (seção 4.4): domingo base e sábado com portão.

---

## 4. Portão semanal

### 4.1 Régua única para 25/10 a 22/11

| Marco (alcance em 48 h) | Valor | Conta | Equivalente na base do Buzzfy (37,5) | Views aproximadas |
|---|---|---|---|---|
| Metade | 27 | 0,5 x 53 | 0,72x | 41 |
| Piso de PARAR | 42 | 0,8 x 53 | 1,12x | 64 |
| Mediana de referência | 53 | 00-SISTEMA, 17 reels | 1,41x | 81 |
| DOBRAR | 106 | 2 x 53 | 2,83x | 161 |
| TABULEIRO (CLAUDE.md) | 150 | regra escrita | 4,00x | 228 |

[ESTIMATIVA] Equivalentes: valor dividido por 37,5; views = alcance x 1,52, a mediana de views por alcance dos 19 reels da fase (de 1,15 a 2,21) [conta sobre `ig_post_stats`].

Pulo: abaixo de 60% para DOBRAR; acima de 75% para PARAR [catálogo seção 8; a régua do Buzzfy marca 45% e o normal da conta, 70,9%].

Por que alcance de 53 e não 37,5 de alcance ou 57 views:
1. **Separa os grupos que a conta já mediu.** O piso de 42 fica logo acima do maior alcance de animação (40, sem contar o 169 de pulo 86,9%) e abaixo do menor reel sem rosto (54). O 106 fica abaixo do menor reel com o Bruno (128) e acima de todo reel sem rosto (64) [FATO, `ig_post_stats`].
2. **A base do Buzzfy vai andar sozinha.** A mediana de 37,5 é dos 20 últimos reels, 12 deles de animação [FATO, `ig_post_stats` baseline]. Se os 10 próximos reels ficarem todos acima de 42, a mediana passa a ser a média dos dois menores reels novos (ou de um deles com o 169 do Dentista A) [ESTIMATIVA: dos 10 reels antigos que sobram na janela de 20, 9 têm 40 ou menos, e a mediana é a média do 10º e do 11º valor]. Um reel de 106 que hoje vale 2,83x pode valer perto de 1x daqui a 2 semanas. Régua em múltiplo trocaria a decisão sem o reel mudar.
3. **Bate com o que já está escrito:** CLAUDE.md (150), catálogo (42, 27, 106) e enquadramento (53 como base provisória).
- O x do Buzzfy (`vs_median_x`, `x_normal`) entra na planilha da rodada como coluna de referência, nunca como régua.

### 4.2 Teste da régua contra a fase atual (30/09 a 21/10)

[FATO, `ig_post_stats`; classificação por este relatório]

| Grupo | n | Alcance mediano | Pulo mediano | Assistido mediano | PARAR (alcance abaixo de 42 ou pulo acima de 75%) | MANTER | DOBRAR (106 ou mais e pulo abaixo de 60%) |
|---|---|---|---|---|---|---|---|
| Reel com o Bruno falando | 4 | 167,5 | 48,1% | 15,1 s | 0 | 0 | 4 |
| Reel sem rosto | 3 | 58 | 55,4% | 8,9 s | 0 | 3 | 0 |
| Reel de animação com voz sintética | 12 | 32,5 | 83,8% | 5,2 s | 12 (8 pelos dois critérios juntos) | 0 | 0 |
| Carrossel ou estático com foto do Bruno | 9 | 126 | | | 0 | 4 | 5 (com 2 ou mais visitas ao perfil) |
| Carrossel ou estático de texto | 6 | 34,5 | | | 5 | 1 (100 mil, 134) | 0 |

A Saga 1 (52 de alcance, capa com figura sem rosto visível, classificação da F1) fica fora dos dois grupos de feed; na régua, MANTER.

**Contrafactual da série 2** [ESTIMATIVA, aplicando a régua às datas reais]: rodando o portão na segunda 19/10 às 19h, a semana fechada de 11 a 17/10 tinha 8 reels de animação com mediana de 33,5 de alcance e 83,9% de pulo, PARAR pelos dois critérios. Não teriam saído o reel Funil (19/10 21h30, 14 de alcance), o reel Marqueteiro (20/10 18h30, 13), o estático Carrinho cheio (20/10 12h, 33) e o estático Fundo de funil (20/10 21h30, 19). A rodada real do Módulo 7 aconteceu em 21/10, depois deles.

### 4.3 Métricas mínimas por formato

Leitura com 48 h ou mais em `ig_post_stats` (reel e carrossel), `ig_account_stats` de 7 dias e leitura diária de stories. PARAR e DOBRAR pedem n de 2 ou mais do formato. Com n de 1, o formato fica em TESTAR, salvo as duas exceções escritas na tabela.

**Reel** (vale para todo reel: Bruno para a câmera, nicho, corte da TV, objeção, remake publicado no feed)

| Métrica (48 h) | PARAR | MANTER | DOBRAR | Base da conta |
|---|---|---|---|---|
| Alcance (mediana do formato) | abaixo de 42 | 42 a 105 | 106 ou mais | mediana 53 (00-SISTEMA); Bruno 167,5; animação 32,5 |
| Pulo (mediana do formato) | acima de 75% | até 75% | abaixo de 60% | normal 70,9%; Bruno 48,1%; animação 83,8% |
| Tempo assistido (desempate) | abaixo de 5,85 s | 5,85 s ou mais | 11,7 s ou mais | normal 5,85 s; Bruno 15,1 s; animação 5,2 s |
| Como combina | alcance **ou** pulo na coluna | o resto | alcance **e** pulo na coluna | |

- **Exceção 1, sequência com n de 1** [FATO, playbook hot_streaks e checklists]: reel com 3x o normal em views (171 ou mais) em 24 h, ou 150 ou mais de alcance em 48 h com pulo abaixo de 55%, ganha a próxima vaga (o sábado do portão ou a base seguinte), mudando só assunto ou só formato. Com 150 ou mais, o próximo do mesmo formato pode levar TABULEIRO (CLAUDE.md), uma palavra por mês.
- **Exceção 2, timelapse** [FATO, catálogo F5]: "abaixo de 0,8x da mediana com pulo acima de 75%, não se repete", com n de 1. Na régua: alcance abaixo de 42 e pulo acima de 75% no tl01 tira o timelapse do feed. Conflito com a regra de n de 2 do enquadramento (D6, opção b) e com a F2 (tl02 como Trial Reel para ter o 2º dado): fica para o julgamento.
- **Família da TV** [HIPÓTESE]: os cortes da entrevista com o Bruno em 3/4 falando com a repórter (pb, ci, po, pf como reel, ob) contam como uma família para o n de PARAR enquanto cada subformato tiver n de 1. Na segunda 02/11 a família terá n de 4 (pb01, ci01, po01, pb02) e o P&B sozinho, n de 2.
- Remake publicado como Trial Reel (F2): DOBRAR (segunda versão ou vaga de feed) com 106 ou mais e pulo abaixo do original (53,2% no "Ele nunca fez um anúncio", 45,7% no "90%", 49,6% no "Equipe") [FATO, `ig_reel_checkup`]; PARAR abaixo de 42. Pelo playbook, Trial Reel de conta pequena bateu o alcance usual 21% das vezes [FATO, small_accounts].
- Animação com voz sintética e estático de cartão de texto: já em PARAR (n de 12 e de 4) [FATO]. Nenhuma vaga vazia é preenchida com eles.

**Carrossel**

| Métrica (48 h) | PARAR | MANTER | DOBRAR | Base da conta |
|---|---|---|---|---|
| Alcance | abaixo de 42 em 2 | 42 a 105 | 106 ou mais | mediana de feed 49 (Buzzfy, 10 posts); os 8 carrosséis da fase, 84,5; feed com foto do Bruno, 126 (n 9) |
| Visitas ao perfil | | | 2 ou mais | mediana de feed 0,5 |
| Salvamento e compartilhamento | sem régua: 0 salvamento e 1 compartilhamento em 16 peças de feed | | | [FATO, `ig_post_stats`] |

**Story** (leitura diária às 08h30 por story; decisão semanal na segunda)

| Métrica | PARAR | MANTER | DOBRAR | Base |
|---|---|---|---|---|
| Views de story, 7 dias | abaixo de 982 por 2 semanas seguidas: voltar para 3 a 5 quadros por dia | 982 ou mais | | 982 em 17 a 24/10 [FATO] |
| Respostas, 7 dias | 0 por 2 semanas seguidas: trocar o tipo de pedido | 3 ou mais | 4 ou mais: o tipo que respondeu ganha mais um quadro por dia | 3 em 7 dias [FATO]; meta do enquadramento D5: 7 em 14 dias |
| Alcance de cada quadro sobre o do 1º quadro do dia | abaixo de 50% em 3 de 5 dias: a posição sai | 50% ou mais | | sem dado; o limite de 50% é [HIPÓTESE] e a 1ª semana monta a base |
| Saída (deslize para a próxima conta + toque para sair) sobre navegações | | | | 37,5% no story de 09h33 de hoje [ESTIMATIVA]; base: sem dado |

**Conta e funil** (registro no portão; não abre nem fecha vaga sozinho)

| Métrica | Base | Fonte |
|---|---|---|
| Seguidores líquidos na semana | -5 (15 a 21/10, 0 entrada) | [FATO, `ig_follower_growth`] |
| Piso de abandono do D4 de 21/10 | 12 líquidos em 14 dias, conferido em 18/11 | [FATO, `10-decision-brief.md`]; 6 por semana como ritmo [ESTIMATIVA: 12 / 2] |
| Disparos de TABULEIRO na semana | 0 | [FATO, `listCommentAutomationLogs`] |
| Visitas ao perfil, 7 dias | 74 | [FATO, `ig_account_stats`] |
| Cliques no site, 7 dias | 0 | [FATO, idem] |
| Diagnósticos agendados | sem dado (nenhuma ferramenta permitida lê a agenda) | |

### 4.4 O que abre e o que fecha no fim de semana

**Quando:** segunda às 19h00. A semana fechada vai de domingo a sábado. Às 19h de segunda, o reel de sábado 18h30 tem 48h30; os de domingo a sexta, 70 h ou mais [FATO, conta de horas]. Ler de manhã pega o reel de sábado com cerca de 40 h (a F4 já avisava). `ig_follower_growth` chega na segunda com os 2 últimos dias pendentes [FATO, nota da ferramenta].

**Ordem do portão:**
1. Ler (só leitura): `ig_reel_checkup` (20 reels), `ig_post_stats` dos ids da semana fechada, `ig_account_stats` de 7 dias, `ig_follower_growth` de 14 dias, `listCommentAutomationLogs` da palavra do mês, o arquivo diário de stories.
2. Dar a cada formato PARAR, MANTER, DOBRAR ou TESTAR pela seção 4.3.
3. Conferir execução da rodada anterior: cada PARAR e DOBRAR tem "executado: sim ou não".
4. Decidir domingo e sábado (tabelas abaixo).
5. Registrar em `conteudo/sistema-instagram/semanas/AAAA-MM-DD.md` e entregar ao Bruno a lista do que agendar no PostZen.

**Domingo seguinte, 18h30 (reel base)**

| Situação | Domingo |
|---|---|
| Existe formato em DOBRAR com peça pronta | Abre com ele (sequência, mudando só assunto ou só formato) |
| Não existe DOBRAR | Abre com o melhor formato medido que tenha peça pronta: MANTER antes de TESTAR, sempre com o Bruno no quadro 0 |
| Nenhuma peça com o Bruno no quadro 0 pronta até sexta 23h59 | Fecha: domingo só com stories e a semana fica com 4 reels, com o motivo escrito ("sem peça") |
| Única peça disponível é de formato em PARAR ou animação com voz sintética | Fecha. Nunca tapar vaga com formato parado |

**Sábado seguinte, 18h30 (6º reel, TESTAR com motivo escrito)**

Abre só com as três condições juntas:
1. A semana fechada, contando só os formatos que seguem na grade, tem mediana de alcance de 42 ou mais e pulo mediano de 75% ou menos.
2. Existe motivo escrito, um destes: (a) sequência de um DOBRAR ou de um reel que bateu a exceção 1; (b) segunda leitura de um formato em TESTAR (leva o n de 1 para 2 e destrava a decisão uma semana antes).
3. A peça está pronta, com o Bruno no quadro 0, e fica a 6 h ou mais de qualquer outro reel ou Trial Reel.

Fecha em qualquer outro caso; o sábado fica com o carrossel das 12h e os stories. Quando a semana fechada fica com mediana abaixo de 27 ou pulo mediano acima de 75%, além de fechar o sábado, o domingo seguinte só recebe o formato de maior alcance medido com o Bruno falando para a câmera (regra 2 do portão do catálogo, com o número da régua).

**Volume que sai daí:** base de 5 reels e 2 carrosséis por semana (CLAUDE.md). Com o sábado aberto, 6 reels: acima da regra, com motivo escrito e portão, como o enquadramento pede. Nunca 7.

### 4.5 Calendário dos portões (dias da semana conferidos com `date`)

| Portão | Hora | Lê com 48 h | Decide |
|---|---|---|---|
| seg 26/10 | **21h05** (exceção) | Dentista A (169, já lido) e Dentista B (sáb 24/10 21h, fecha 48 h às 21h); semana de 18 a 24/10 sem os formatos de animação, já em PARAR | Status da linha "Bruno para a câmera, dentista" (n de 2) e se o B libera TABULEIRO para o próximo do mesmo formato (150 ou mais) |
| ter 27/10 | **18h35** (extra) | tl01 (dom 25/10 18h30) | Sábado 31/10: tl02 só com tl01 em 42 ou mais e pulo até 75%. Enquanto a legenda do tl01 prometer o sábado, o portão não decide o 31/10 (a F4 propõe trocar a frase até dom 18h30) |
| seg 02/11 (Finados) | 19h00 | Dentista B, tl01, pb01, ci01, po01, pb02 e tl02 (se sair sáb 31/10 18h30, fecha 48 h às 18h30) | Sáb 07/11 e dom 08/11; família da TV com n de 4 |
| seg 09/11 | 19h00 | semana de 01 a 07/11 | Sáb 14/11 e dom 15/11 (feriado) |
| seg 16/11 | 19h00 | semana de 08 a 14/11 | Sáb 21/11 e dom 22/11 |
| seg 23/11 | 19h00 | semana de 15 a 21/11 | Semana 5 |

Conferências que caem fora da segunda e usam outra régua: qua 11/11 (nicho, D1 de 21/10: abandono com mediana dos 3 abaixo de 53 ou pulo acima de 75%) e qua 18/11 (D3 e D4 de 21/10) [FATO, `10-decision-brief.md`]. O nicho usa 53 como piso; esta frente usa 42 para PARAR. Conflito registrado na seção 6.

---

## 5. O histórico do Módulo 7 contra a régua

| Decisão de 21/10 [FATO, `00-SISTEMA.md`] | O que a régua diz hoje | Executado? |
|---|---|---|
| PARAR animação com voz sintética | PARAR confirmado: n de 12, mediana 32,5 e pulo 83,8% | Sim: nenhum reel de animação depois de 20/10 [FATO, `ig_posts`] |
| PARAR 3 posts por dia | Régua não mede ritmo. A série de 3 por dia somou 205 de alcance em 8 peças; a semana da saga, 1.370 em 11 [FATO, F1] | Sim: a agenda de 25 a 30/10 tem 1 reel por dia [FATO, `listPosts`] |
| PARAR 12 palavras-chave diferentes | Não é métrica de régua | **Não**: 17 automações ativas, 16 com 0 disparo [FATO, `listCommentAutomations`] |
| DOBRAR o Bruno falando para a câmera | DOBRAR confirmado: n de 4, mediana 167,5, pulo 48,1% | Em parte: Dentista A saiu (21/10); de 22 a 23/10 nada saiu [FATO, `ig_posts`] |
| DOBRAR a série bíblica | Em reel com o Bruno, n de 1 na zona DOBRAR (308, pulo 53,2%). Em carrossel, mediana 84,5 com n de 6: MANTER; só Saga 2 (189) e Saga 3 (126) na zona DOBRAR | Não: nenhuma peça da saga na agenda até 30/10 [FATO, `listPosts`] |
| DOBRAR número específico no gancho | Não separa: com o Bruno, 166 (90%); sem rosto, 54 (Cem mil) e 16 (Escala) | sem dado |
| TESTAR profissão nomeada | Dentista A n de 1 na zona DOBRAR (169, 46,6%); Médico sem rosto 64 (MANTER). O n de 2 com o Bruno fecha com o Dentista B em seg 26/10 21h | Sim |
| Tabela "Próximos 7 dias" (22 a 28/10) | Dias da semana trocados (aviso do catálogo) e peças de 22 e 23/10 não publicadas | Não [FATO, F5 e `ig_posts`] |

O que isso pede do portão: uma coluna "executado" por decisão e uma lista curta, com dono e prazo, do que o Bruno agenda ou desliga no PostZen.

---

## 6. Conflitos com outros documentos

1. **Sábado e domingo invertidos contra o catálogo (seção 8).** Catálogo: sábado fixo para a TV e domingo com portão. Aqui: domingo base e sábado com portão. Motivo: o reel de sábado 18h30 entra no portão de segunda com 48 h e o de domingo, com 24h30; o TESTAR precisa ser o que se lê completo na segunda seguinte. A S1 do PostZen já usa o domingo como base (tl01) e deixa o sábado livre [FATO, `listPosts`].
2. **Três medianas.** Enquadramento: 53 provisório; F2: 57 views; Buzzfy hoje: 37,5 de alcance. Esta frente propõe 53 fixo por 4 semanas, com o x do Buzzfy só como coluna (seção 4.1).
3. **Piso do nicho.** O brief de 21/10 abandona o nicho com mediana abaixo de 53 em 11/11; a régua daqui põe PARAR abaixo de 42. Um nicho com mediana entre 42 e 52 fica MANTER aqui e abandonado lá. Decisão do julgamento.
4. **Timelapse com n de 1** (catálogo F5) contra n de 2 (enquadramento D6 b e F2). Seção 4.3, exceção 2.
5. **Hora dos reels.** Módulo 3: 18h30; roteiros de nicho e PostZen: 21h. Esta frente fica com 21h nos dias úteis e 18h30 no fim de semana, sem teste de hora.
6. **Volume de stories.** O `03-plano-7-dias.md` tem 56 stories na semana (8 por dia); o enquadramento (D5) discute 3 a 5. Efeito do volume de story na conta: sem dado. A régua de story da seção 4.3 decide depois da 1ª semana de leituras diárias.
7. **`ig_best_times` no contexto.** Os números do `contexto.md` não se reproduzem às 14h10 em nenhuma das amostras (seção 2.2). Não muda decisão.

---

## 7. Lacunas

1. Seguidores online por dia da semana: sem dado (a ferramenta dá só a média por hora de 27 dias).
2. Reel com o Bruno entre 12h e 20h59: nenhum na conta. Efeito da hora em reel com o Bruno: sem dado.
3. Alcance em feriado (02/11, 15/11, 20/11): sem dado.
4. Métrica por story dos dias anteriores e número de stories por dia nos 30 dias: sem dado (o Buzzfy só lê story no ar; o PostZen registra 6 stories em 30 dias e os do app não aparecem).
5. Toques no link do sticker de diagnóstico: o `ig_post_stats` de story não traz esse campo; a UTM `?o=ig-stories` só se lê no site, fora das ferramentas permitidas. Sem dado.
6. Base por quadro de story (alcance sobre o 1º quadro, saída): sem dado até a 1ª semana de leituras diárias (25/10 a 31/10).
7. Seguidores de 22 e 23/10 pendentes no Instagram; o efeito do Dentista A em seguidores segue sem dado.
8. Resultado do Dentista B (sai hoje 21h) e do tl01 (amanhã 18h30): ainda não existem.
9. Diagnósticos agendados: sem dado.
10. A mediana de 53 não é recalculável hoje pelo Buzzfy (a janela atual dá 37,5); ela é um número documental do 00-SISTEMA (17 reels, 21/09 a 21/10).
11. Trial Reels: nenhum na fase atual [FATO, `ig_posts`]; desempenho de Trial Reel nesta conta: sem dado.
12. Todas as comparações têm n pequeno (4 reels com o Bruno; 1 a 3 posts por hora) e formato confundido com hora e dia.

---

## 8. Fontes

- Buzzfy, leituras de 24/10/2026 entre 14h10 e 14h18: `ig_best_times` (25 e 50), `ig_posts` (all desde 29/09; reels; stories), `ig_post_stats` (35 peças e 3 stories), `ig_reel_checkup` (20), `ig_account_stats` (30 e 7 dias), `ig_follower_growth` (30 dias), `buzzfy_playbook` (overview, checklists, hot_streaks, small_accounts).
- PostZen, leituras de 24/10/2026 entre 14h14 e 14h16: `listPosts` (agendados de 24/10 a 24/11; publicados de 20/09 a 24/10), `listCommentAutomations`, `listCommentAutomationLogs` (TABULEIRO qs747t4bq23a1qpnjskexg34vs8gx7hx; CHECKLIST qs7de23c7nzxzw2k4yjshgm5gd8g5dmx).
- Repositório: `/home/user/Disparo-/CLAUDE.md`; `conteudo/modo-god-cronograma/contexto.md`; `conteudo/modo-god-cronograma/run/00-enquadramento.md`; `conteudo/modo-god-cronograma/run/01-pesquisa/F1-auditoria-conta.md`, `F2-playbook-buzzfy.md`, `F4-entrevista-tv.md`, `F5-capacidade-e-estoque.md`; `conteudo/sistema-instagram/00-SISTEMA.md`; `conteudo/sistema-instagram/semanas/2026-10-21.md`; `conteudo/entrevista-tv-camara/catalogo-formatos.md`; `conteudo/modo-god-nichos/run/10-decision-brief.md`; `conteudo/stories-objecoes/03-plano-7-dias.md`.
- Contas de mediana, faixa de hora, dia e teste da régua: script de leitura no scratchpad da sessão, sobre os números copiados do `ig_post_stats` (nenhum dado novo além das consultas acima).
