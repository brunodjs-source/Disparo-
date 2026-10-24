# F2 · Playbook do Buzzfy aplicado ao @o_estrategista.com.br

Frente F2 da pesquisa do conselho Agência Reunida. Rodada de sábado, 24/10/2026, escrita às 15h05 (São Paulo). Substitui a versão das 13h40 deste arquivo, escrita antes de dois fatos: a entrevista vai ao ar na **segunda-feira, 02/11/2026** (mensagem do Bruno: "Vai pro ar segunda dia 2"), e tl02 a tl05 entraram no PostZen perto de 14h40 (mídia do tl02 enviada às 14h40; commit 318e97d às 14h41). Só leitura: nada foi publicado, agendado ou alterado no Instagram, no Buzzfy ou no PostZen. Toda mudança abaixo é proposta para o Bruno executar.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, nível 4, que nunca fecha objeção sozinho. Métrica que falta: "sem dado".

**Base desta frente (uma só):** normal da conta = **57 views por reel**, pulo normal **70,9%** [FATO, Buzzfy `ig_reel_checkup`, 20 reels de 01/01/2025 a 21/10/2026, lido às 14h50]. Alcance mediano 37,5 e tempo assistido mediano 5,85 s, na mesma base [FATO, `ig_post_stats`, baseline]. O enquadramento e o catálogo usam 53 de alcance (outra base, 17 reels mais antigos): esta frente fica em views e não mistura as duas.

---

## 0. Respostas curtas

1. **Dentista A a 4,68x** [FATO, `ig_reel_checkup`]: quem explica é a regra 1 do playbook, a abertura. Pulo de 46,6% contra 70,9% da conta (24,3 pontos abaixo). No quadro 0 havia o Bruno, texto na tela e legenda queimada; a primeira palavra é a profissão ("Dentistas,"), o número chega aos 2,04 s ("474 mil") e a pergunta aberta aos 5,42 s; sem saudação e sem venda [FATO, `videos/nichos/dentista/words.json` e `engine/dent.html`]. As regras 2 (envio), 6 (reassistir) e 7 (legenda do post) não ajudaram: 0 compartilhamento, 0 salvamento, 35,7% da duração assistida, 8 hashtags e pedido de comentário.
2. **O tamanho do 4,68x**: 267 views = 0,165x os seguidores; o típico entre contas do playbook é 0,17x [ESTIMATIVA: 267 / 1.618]. O A ficou no nível de um reel típico de outras contas; o normal da conta (57 = 0,035x os seguidores) é que está baixo. Um estouro pela régua entre contas fica perto de 2.993 views [ESTIMATIVA: 1,85 x 1.618].
3. **Série 2 abaixo de 1x**: a regra 1 ao contrário. Os 4 reels de 18 a 20/10 tiveram pulo de 78,9% a 86,7%, todos acima do normal da conta, sem rosto e com voz sintética [FATO, `ig_reel_checkup` 14h50 e 00-SISTEMA]. Pesam junto: 8 posts de feed em 3 dias, 2 reels com 3 h de distância em 19/10 (playbook: menos de 6 h, 0,92x), cada ideia publicada 2 vezes (reel e estático) e 4 palavras-chave de comentário diferentes (pedido de comentário: 1,00x) [FATO, `ig_posts`]. O reel de domingo ficou em 0,56x: o playbook avisa que as alavancas de baixo (dia, hashtag) não resgatam uma abertura fraca.
4. **A exibição de 02/11 não está no playbook.** Ele mede cada reel contra os outros reels do mesmo perfil e não tem variável de TV [FATO, `buzzfy_playbook` overview e second_life]. O que ele dá para a semana da exibição são 4 travas, todas traduzidas de regras medidas: (a) a chamada para assistir vai na legenda e nos stories, nunca na primeira frase do reel (primeira frase que vende é o sinal mais forte de abertura fraca); (b) @ de quem aparece no vídeo na legenda: "@mention or collab" 1,13x; (c) de 02 a 04/11 o pedido da legenda é seguir (1,12x), porque gente nova chega ao perfil [HIPÓTESE, adaptação da regra de sequência]; (d) corte publicado antes de 02/11 só volta depois como remake com 2 mudanças reais, como Trial Reel.
5. **Sequência**: a janela de 48 h do Dentista A fechou sem post (`window_open: false`) [FATO]. Vale a parte de 2 semanas: 3 a 5 reels na mesma linha, mudando assunto ou formato, nunca os dois. Sem gravação nova, a linha tem 2 peças: Dentista B (hoje, 21h) e o pf01 subindo de story para reel, proposto para dom 01/11, 18h30 (fim de semana, véspera da exibição). Para cada reel da S1 que bater 171 views em 24 h há uma sequência pronta definida antes (seção 9.3).
6. **Remake**: R1 "Ele nunca fez um anúncio" (10,14x), R2 "90% dos lançamentos que flopam" (4,42x) e R3 "Problema de equipe" (3,61x) saem sem gravar, com 2 ou 3 mudanças reais cada, como Trial Reel postado pelo Bruno no app: dom 01/11, ter 03/11 e qui 05/11, 11h. Depois da exibição entra um segundo tipo de remake: o corte da TV que passar de 3x volta como "o que eu disse na TV".
7. **Achados novos desta versão** [FATO]: (a) a S1 (25 a 31/10) tem 6 reels agendados, porque o tl02 entrou no sábado 31/10; o CLAUDE.md manda 5; pelo playbook, 5 e 6 ficam na mesma faixa (5 a 7 por semana: 7,0% de estouro). (b) O ob02 usa os mesmos 21,4 s de fala do pf01, 82% do áudio dele [ESTIMATIVA: 21,4 / 25,97]: pf01 como reel e ob02 não cabem no feed na mesma quinzena sem 2 mudanças reais. (c) tl01, tl02 e tl03 têm o Bruno em cena aos 0,6 s e aos 2,5 s (quadros extraídos dos renders às 14h54). (d) A legenda do tl01 agora promete "O mais votado eu solto inteiro depois que a entrevista for ao ar": pelo playbook, essa entrega é a sequência por resposta a comentário, a partir de ter 03/11. (e) O tl02 agendado é o render com 10,4 s seguidos sem voz real (16,55 a 26,95 s), acima do teto de 8 s do catálogo: mesmo tamanho de arquivo no PostZen e no disco (17.086.179 bytes).

---

## 1. O que mudou desde a versão das 13h40

| Item | 13h40 | Agora (14h50) | Fonte |
|---|---|---|---|
| Publicações no PostZen de 24/10 a 23/11 | 16, nada depois de sex 30/10 | 20: entraram tl02 sáb 31/10, tl03 sáb 07/11, tl04 sáb 14/11 e tl05 sáb 21/11, todos às 18h30 | [FATO, `listPosts`; commit 318e97d às 14h41] |
| Legenda do tl01 | "O mais votado sai no próximo sábado." | "A entrevista vai ao ar na segunda, 02/11." e "O mais votado eu solto inteiro depois que a entrevista for ao ar." | [FATO, `listPosts`] |
| Legenda do tl02 | não agendado | "Parte 2 do bastidor...", "A entrevista vai ao ar na segunda, 02/11.", índice com 7 assuntos novos e "Comenta o número do assunto que você quer ver inteiro." | [FATO, `listPosts`] |
| "Você não enriquece o marqueteiro" | 0,37x, pulo 92,9% | 0,39x (22 views), pulo 86,7% | [FATO, `ig_reel_checkup`] |
| Faixa da série 2 | 0,37x a 1,07x; pulo 78,9% a 92,9% | 0,39x a 1,07x; pulo 78,9% a 86,7% | idem |
| Dentista A | 267 views, 169 alcance | sem mudança (65,8 h de vida) | idem |
| Posts de feed depois do A | nenhum | nenhum | [FATO, `ig_posts` desde 18/10] |
| Render de ob01 a ob03 | sem dado | nenhum .mp4 no disco; só as fichas `videos/tv-camara/cortes/ob0X.spec.json` | [FATO, busca no disco às 14h52] |

O contexto.md (versão das 14h40) ainda lista tl02 a tl05 como "proposto e ainda não agendado" e a série 2 com 0,37x e 93% de pulo. Esta frente usa a leitura ao vivo.

---

## 2. Fontes conferidas nesta rodada

| Consulta (só leitura) | Hora (SP) | Resultado |
|---|---|---|
| Buzzfy `buzzfy_playbook`: overview, openings, formats, shares_and_saves, hot_streaks, second_life, small_accounts, checklists | 14h48 | OK. "The Viral Reels Playbook, 2026 Edition (Buzzfy Research, September 2026)", 531.037 criadores, cada um comparado consigo mesmo |
| Buzzfy `buzzfy_playbook`: captions, length_and_pace (apoio) | 14h49 | OK |
| Buzzfy `ig_reel_checkup`, 20 últimos reels | 14h49 | OK. Normal 57 views, pulo 70,9%; `shares_per_100_likes` do normal: null; janela de sequência fechada; 5 candidatos a remake |
| Buzzfy `ig_reel_checkup` com `until` 31/12/2024 | 14h55 | OK. 4 reels de 2021 a 2024 (conteúdo de igreja, fora do posicionamento), pulo de 5,7% a 22,1%; poucos para normal, sem multiplicador e sem candidato a remake |
| Buzzfy `ig_post_stats`, 10 reels (Dentista A, série 2, R1 a R3, "Você gravou o curso inteiro", resumo de 2024) | 14h50 | OK. Nota da ferramenta: contagem só orgânica |
| Buzzfy `ig_posts` desde 18/10 (9 itens) e 3 consultas por id (R1, R2, R3) | 14h50 a 14h53 | OK. R1 a R3 com `video_url_withheld: false` |
| PostZen `listPosts`, conta j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 a 23/11 | 14h50 | OK. 20 publicações: 2 publicadas (stories de 14h00 e 14h03), 18 agendadas |
| Cabeçalho HTTP das mídias do tl02 e do tl03 no PostZen (`curl -I`) | 14h53 | OK. Tamanho igual ao render do disco |
| Repositório: `videos/tv-camara/cortes/*.spec.json`, `videos/tv-camara/dados/transcricao.json`, `videos/nichos/dentista/words.json` e `engine/dent.html`, `ffprobe` dos renders (dentista e scratchpad `tv/render/`), quadros de 0,6 s e 2,5 s de tl01 a tl03, `conteudo/entrevista-tv-camara/*`, `conteudo/stories-objecoes/03-plano-7-dias.md`, `conteudo/sistema-instagram/*`, `run/00-enquadramento.md`, `run/01-pesquisa/F4-entrevista-tv.md` | 14h50 a 14h56 | OK |

Erros de consulta nesta rodada: nenhum.

---

## 3. Régua da conta (views em 48 h, normal 57)

| Marco | Multiplicador | Views | Fonte da regra |
|---|---|---|---|
| Metade | 0,5x | 29 | catálogo, seção 8 |
| Piso do portão | 0,8x | 46 | catálogo, seção 8 |
| Normal | 1x | 57 | `ig_reel_checkup` |
| Dobro | 2x | 114 | catálogo (DOBRAR) |
| Sinal: pede sequência e entra na lista de remake | 3x | 171 | playbook, checklists e hot_streaks |
| Estouro | 5x | 285 | playbook, checklists |
| Típico entre contas (0,17x os seguidores) | | 275 | playbook, small_accounts |
| Igual ao número de seguidores | | 1.618 | playbook: 64% dos estouros passam disso |
| Estouro entre contas (1,85x os seguidores) | | 2.993 | playbook, small_accounts |

[ESTIMATIVA] Cada linha é 57 vezes o multiplicador, arredondado, ou 1.618 vezes a fração de seguidores.

- **Pulo** [FATO, playbook, openings e checklists]: meta abaixo de 40%; abaixo de 30% é "hit em formação"; acima de 45%, ou acima do próprio normal (70,9%), o conserto é a abertura. Chance de estouro por faixa: abaixo de 20%, 51%; 20 a 25%, 44%; 25 a 30%, 32%; 30 a 35%, 20%; 35 a 40%, 12%; 40 a 45%, 7%; 45 a 50%, 4%; 50 a 55%, 3%; 55 a 60%, 2%; 60 a 70%, 1%.
- **Envio**: com menos de 50 curtidas o Buzzfy não pontua compartilhamento por 100 curtidas [FATO, nota do `ig_reel_checkup`]; nenhum reel da conta passou de 30 curtidas. A régua útil é compartilhamento por 1.000 contas alcançadas (playbook, shares_and_saves): com pulo de 35 a 50%, a chance vai de 4% (0 a 1 por mil) a 16% (8 ou mais). Com alcance perto de 170, 2 compartilhamentos já dão 11,8 por mil [ESTIMATIVA: 2 / 169 x 1.000].

---

## 4. As regras do playbook, uma a uma, na conta

| # | Regra e número do playbook [FATO, `buzzfy_playbook`] | Onde a conta está [FATO, salvo marcação] | Tradução para 25/10 a 07/11 (série da TV e exibição) |
|---|---|---|---|
| 1 | **Abertura.** Típico perde 57%; estouros, 38%. Abaixo de 30% de pulo, 1 em 3 estoura. Primeira frase: sem saudação, curta (até 8 palavras), específica, pergunta aberta, precisa da imagem, não vende. Texto na tela desde o quadro 0: 1,18x | Normal 70,9%. Menor pulo dos 20: 44,6% ("Cem mil seguidores", sem rosto, abre com "100 mil seguidores, 14 vendas"). 4 reels com o Bruno falando: 45,7% a 53,2%. 11 reels sem rosto de 12 a 20/10: 69,4% a 89,7% [`ig_reel_checkup`] | Nenhum reel da conta abaixo de 40%. Nos cortes da TV a primeira frase é fala da entrevista: pb01 abre em "Pois é", pb02 e pf01 em "Bom" [`transcricao.json`]. A chamada para a exibição nunca é a primeira frase de um reel |
| 2 | **Envio.** Estouro: 1 compartilhamento a cada 8 curtidas; típico, 1 a cada 55. Salvamento: 7 por 100 curtidas no estouro, menos de 2 no típico. Três motivos: "é a sua cara", "você precisa disso", "você não vai acreditar" | 0 compartilhamento nos 20 reels. Salvamento só no R1 (2, ou 6,7 por 100 curtidas, o único que pedia "Salva") [`ig_post_stats`, `ig_posts`]. Os 9 compartilhamentos de 30 dias vieram de outros tipos de post [contexto.md]; por peça: sem dado | Pedido de envio com destinatário nomeado: legenda do pb01 ("Manda para um expert que vai lançar este ano.") e vídeo do pf01 ("Manda para um dentista que precisa ouvir isso.") e do ci01 ("Manda para quem precisa ouvir isso.") [`listPosts` e fichas] |
| 3 | **Abrir no ápice.** Recortado para abrir no melhor momento: história +4,8 pontos de retenção; comparação +3,0. História: 2 s do ápice e depois "como chegamos aqui". Passo a passo mantém a abertura natural | O número que paga o vídeo chega aos 16,3 s no pb01, 18,5 a 21,0 s no pb02 e 17,8 s no pf01; assistido mediano da conta: 5,85 s [`transcricao.json`, contado do início do trecho; `ig_post_stats`] | Seção 7. Candidatos ao recorte: pb02 (antes de sex 30/10) e pf01 se subir para reel |
| 4 | **Formato.** História 1,20x; filmagem crua 1,11x; tutorial 1,08x; lista 1,07x; antes e depois 1,01x; vitrine 0,97x; talking head 0,91x; montagem 0,75x. Contas de 1 a 5 mil: história 1,28x, montagem 0,69x | Os 4 com o Bruno são talking head selfie (tags do Buzzfy em R1 a R3). Os sem rosto com tags são "slideshow_text" | pb01 história; pb02 antes e depois contado como história; po01 lista; ci01 diálogo; tl01 e tl02 têm de 39% a 49% do tempo em plano aberto acelerado [F4]: montagem [HIPÓTESE]; tl03 a tl05 têm de 61% a 68% de voz real [F4] |
| 5 | **Legenda queimada.** Mesmo vídeo com legenda, mostrado a quem não segue: 4,6x as views | Dentista A, B e C com legenda desde a primeira palavra [`dent.html`]. R1 sem legenda queimada (`burned_subtitles: false`). Os sem rosto de outubro também tinham legenda | Toda a série da TV tem legenda [fichas]. É a maior mudança disponível no remake do R1 |
| 6 | **Reassistir.** Assistido sobre duração: acima de 150%, 33%; 100 a 150%, 22%; 80 a 100%, 19%; 30 a 40%, 11%; abaixo de 20%, 5%. Duração quase não importa; versão cortada em 30 a 40% segurou quase como a original | A: 13 s de 36,4 s = 35,7%. R1: 18,7 de 74,6 s = 25%. R2: 12,6 de 69,5 s = 18%. R3: 17,2 de 74,7 s = 23% [ESTIMATIVA: assistido do `ig_post_stats` sobre a duração das tags e do `ffprobe`] | Remake com corte de 20 a 40%. Os cortes da TV já são curtos (19,5 a 36,6 s) |
| 7 | **Legenda do post.** 1 a 5 hashtags 1,04x; 6 ou mais 0,91x; 600 caracteres ou mais 1,12x; em branco 0,78x. "@mention or collab" 1,13x; número na linha 1 1,11x; pergunta 1,06x. Pedido: salvar 1,16x; seguir 1,12x; enviar 1,10x; "comenta" e "link na bio" não somam. Um pedido só | A: 8 hashtags e "Comenta aqui". Agendados: 5 hashtags em todos; nenhum com @; maior legenda sem hashtags: tl01 com 489 caracteres [`listPosts`, contagem às 14h55]; po01 e car01 com 2 pedidos | O @ da Mirna na legenda é a regra medida mais próxima de "marcar a Mirna": 1,13x. O PostZen leva texto com @ [HIPÓTESE: a limitação registrada no contexto é de marcação na mídia, não de texto]. @ dela: sem dado |
| 8 | **Sequência.** Post seguinte a um estouro: 1,81x de chance; o 2º, 1,63x; o 3º, 1,52x; o 10º, 1,13x. Hit (3x ou mais): 1ª sequência em 24 h, 2ª em 48 h; depois 3 a 5 na mesma linha em 2 semanas, mudando uma coisa; deixar 1 ou 2 reels prontos; pedir para seguir nas sequências; um post fraco não muda o plano | Janela do A fechou sem post. O A ficou em "signal" (3x ou mais); "breakout" começa em 5x [`ig_reel_checkup`] | Seção 9. O 1,81x foi medido depois de estouros de 5x; no A é extrapolação [HIPÓTESE] |
| 9 | **Segunda vida.** Original 5x ou mais: repost bate o alcance usual 35% das vezes; 2 a 5x: 15%; 1 a 2x: 7%. Por pulo do original: abaixo de 30%, 37%; 30 a 40%, 26%; 40 a 50%, 16%. Nova versão de um repost que ganhou: 34%. Mudar 2 coisas reais (abertura, legenda queimada, corte de 20 a 40%, resposta a comentário) e postar como Trial Reel | Lista do Buzzfy: 10,14x, 9,14x, 4,68x, 4,42x, 3,75x | Seção 10. Corte publicado antes de 02/11 e reaproveitado depois é repost: entra nesta regra |
| 10 | **Conta pequena.** 64% dos estouros passam do número de seguidores. Contas de 1 a 5 mil: 74% tiveram ao menos um estouro em 22 meses. Trial Reel de conta pequena bate o alcance usual 21% das vezes | Maior reel dos 20: 578 views = 0,36x os seguidores [ESTIMATIVA: 578 / 1.618] | Estouro pela régua entre contas: 1.618 views ou mais. Nenhum reel da conta chegou lá |
| 11 | **Ritmo.** 7 ou mais por semana: 7,7% dos reels estouram; 5 a 7: 7,0%; 3 a 5: 6,0%. Reel a menos de 6 h do anterior: 0,92x. Sábado e domingo: 1,10x; dias úteis 0,96x | 12 e 13/10: 3 reels por dia (11h, 18h e 20h); 19/10: reels às 18h30 e 21h30 [`ig_reel_checkup`, horário convertido de UTC] | Agendado: no máximo 1 reel por dia; S1 com 6 reels; sáb 31/10 e sáb 07/11 com reel; dom 01/11 vazio [`listPosts`]. Trial Reel conta para a distância de 6 h [HIPÓTESE] |

---

## 5. Por que o Dentista A deu 4,68x

| Métrica [FATO, `ig_post_stats`, 65,8 h depois de sair] | Dentista A | Normal da conta | x normal |
|---|---|---|---|
| Views | 267 | 57 | 4,68 |
| Alcance | 169 | 37,5 | 4,51 |
| Pulo | 46,6% | 70,9% | 24,3 pontos abaixo |
| Assistido médio | 13 s | 5,85 s | 2,22 |
| Curtidas / comentários / compartilhamentos / salvamentos | 10 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | |
| Duração | 36,37 s [FATO, `ffprobe` em `render/dentista-A-9x16.mp4`] | | |
| Saída | qua 21/10, 21h00 | | |

**Regras que explicam a alta**
- **Regra 1, abertura** [FATO]: Bruno em cena desde o quadro 0 (modelo A, vídeo dele como base); título na tela e legenda desde 0,0 s [`dent.html`]; primeira palavra "Dentistas," (profissão nomeada: o "é a sua cara" do playbook); número específico aos 2,04 s ("474 mil"); pergunta aberta aos 5,42 s ("Por que você ainda só vende hora de cadeira?") [`words.json`]; sem saudação e sem venda.
- **Dentro da conta, o rosto separa** [FATO, `ig_reel_checkup`]: os 4 reels com o Bruno falando ficaram entre 3,61x e 10,14x (mediana 4,55x [ESTIMATIVA: média de 4,42 e 4,68]). Os 11 sem rosto de 12 a 20/10 ficaram entre 0,39x e 1,07x. Pelo playbook, talking head é 0,91x entre contas: a vantagem do rosto aqui vem de a base da conta ser feita de reels sem rosto [HIPÓTESE].
- **O rosto não é a única variável** [FATO e HIPÓTESE]: 4 reels sem rosto de 30/09 a 11/10 ficaram entre 1,32x e 3,75x ("Médico com agenda lotada" 1,79x; "Cem mil seguidores" 1,40x com o menor pulo da conta, 44,6%; "O que você recusa" 1,32x; "Você gravou o curso inteiro" 3,75x). A queda abaixo de 1x começa em 12/10, junto com 3 reels por dia e a voz sintética [FATO, 00-SISTEMA]. Se a voz desses 4 era sintética: sem dado (o Buzzfy marca `own_voice_on_camera` em 01/10 e 05/10 e `voiceover` em 30/09 e 11/10, e não separa voz sintética).

**Regras que não dispararam (o que faltou para virar estouro)**
- Frase de abertura com 10 palavras e 5,4 s; o playbook pede até 8 [FATO, `words.json`]. O pulo ficou na faixa de 45 a 50% (4% de chance) e o próprio Buzzfy manda o conserto 1, abertura (`fix_it_step: 1`).
- Envio zero: o pedido era comentar ("Comenta aqui"), medido em 1,00x; terminou com 0 comentário [FATO, `ig_posts`].
- Reassistir: 35,7% da duração (faixa de 30 a 40%, 11% de chance) [ESTIMATIVA].
- Legenda: 8 hashtags (0,91x, flag `hashtags_6_plus`) e 499 caracteres [FATO].
- Dia útil (0,96x contra 1,10x no fim de semana) e saiu depois de 4 reels fracos [FATO, `ig_posts`].

**Leitura para o próximo da linha** [HIPÓTESE]: mantendo rosto, profissão nomeada e número, o que mais move a chance é a frase de abertura com até 8 palavras (alvo: pulo abaixo de 40%, faixa de 12%) e um motivo de envio com destinatário ("Manda para um dentista que...").

---

## 6. Por que a série 2 ficou abaixo de 1x

**Linha do tempo** [FATO, `ig_posts` e `ig_reel_checkup` às 14h50; horário de São Paulo]

| Dia | Hora | Peça | Tipo | x normal | Pulo | Pedido na legenda |
|---|---|---|---|---|---|---|
| dom 18/10 | 18h47 | "Escala 7x7? Nem a sua escala 5x2 aguenta isso." | reel | 0,56 | 78,9% | Comenta ETAPAS |
| dom 18/10 | 21h30 | "Escala 7x7? Nem a sua 5x2 aguenta." | estático | | | Comenta ETAPAS |
| seg 19/10 | 12h00 | "Você não enriquece o marqueteiro..." | estático | | | Comenta ESTRATEGISTA |
| seg 19/10 | 18h30 | "Seu carrinho cheio pode virar zero no caixa." | reel | 1,07 | 82,2% | Comenta CAIXA |
| seg 19/10 | 21h30 | "Fundo de funil não se compra..." | reel | 0,54 | 85,7% | Comenta FUNIL |
| ter 20/10 | 12h00 | "Seu carrinho cheio..." | estático | | | Comenta CAIXA |
| ter 20/10 | 18h30 | "Você não enriquece o marqueteiro..." | reel | 0,39 | 86,7% | Comenta ESTRATEGISTA |
| ter 20/10 | 21h30 | "Fundo de funil não se compra..." | estático | | | Comenta FUNIL |

Assistido médio dos 4 reels: 3,6 a 10,7 s [FATO, `ig_post_stats`]. Duração dos 4: sem dado (o Buzzfy não analisou esses vídeos: `tags: null`).

**Regras que explicam**
1. **Abertura (regra 1)** [FATO]: os 4 com pulo acima do normal da conta (8 a 16 pontos acima), todos na faixa de 60% ou mais (1% de chance). Sem rosto e com voz sintética [FATO, 00-SISTEMA, "3 piores"].
2. **Formato (regra 4)** [HIPÓTESE]: animação sem situação que muda fica do lado de montagem e vitrine (0,69x a 0,97x), longe de história (1,28x em contas de 1 a 5 mil).
3. **Repetição** [FATO, `ig_posts`]: as 4 ideias saíram 2 vezes cada, como reel e como estático, com 2h43 a 30h30 de distância. O playbook diz que o Instagram limita o alcance do que vê como repetido (second_life); se isso pesou aqui: sem dado.
4. **Ritmo (regra 11)** [FATO]: 8 posts de feed em 3 dias; 2 reels no mesmo dia com 3 h de distância (19/10). A série anterior (12 a 14/10) teve 3 reels por dia, com 2 h entre os das 18h e das 20h, e ficou entre 0,58x e 0,93x. O Módulo 7 de 21/10 já mediu que 3 posts por dia não aumentaram seguidores [FATO, 00-SISTEMA].
5. **Pedido (regra 7)** [FATO]: 4 palavras-chave de comentário diferentes, medidas em 1,00x. Nenhum pedido de envio, salvamento ou seguir.
6. **Fim de semana não resgata** [FATO, playbook overview: "the bottom ones won't rescue a weak opening"]: o reel de domingo ficou em 0,56x.

O caso que não encaixa: "Você gravou o curso inteiro" (11/10, sem rosto, narração) teve 3,75x de views e 169 de alcance com pulo de 86,9% e 5 s assistidos [FATO, `ig_post_stats`, contagem orgânica]. Causa: sem dado.

---

## 7. A série da entrevista contra o playbook (o que está agendado e o que está proposto)

Tempos de fala contados do início do trecho da ficha (`seg` em `videos/tv-camara/cortes/<id>.spec.json`), pela transcrição palavra a palavra [FATO, `transcricao.json`]. Datas e legendas [FATO, PostZen `listPosts` às 14h50]. Duração [FATO, `ffprobe` em `scratchpad/tv/render/`]. Quadros de tl01 a tl03 [FATO, extraídos aos 0,6 s e 2,5 s às 14h54].

| Peça | Sai | Duração | Quadro 0 e 3 primeiros segundos | Primeira fala | Ápice | Formato no playbook | Pedido |
|---|---|---|---|---|---|---|---|
| Dentista B | sáb 24/10, 21h00 | 36,37 s | Bruno em tela cheia até 3,18 s, depois tela dividida [`dent.html`, `splitS`] | a mesma do A | "você deixa de disputar paciente e passa a formar quem disputa" | talking head com painel | Comenta TABULEIRO |
| tl01 | dom 25/10, 18h30 | 36,5 s | "35 MINUTOS EM 35 SEGUNDOS" sobre o Bruno de frente ao laptop; aos 2,5 s, Bruno e Mirna na mesa | voz real a partir de 1,8 s | laço fecha aos 27 s | montagem com laço [HIPÓTESE] | Comenta o número (legenda avisa 02/11) |
| pb01 | seg 26/10, 21h00 | 19,5 s | Z2, frase inteira na tela | "Pois é, essa daí foi uma virada, né?" | "profissão" aos 15,3 s; "20" aos 16,3 s | história | Manda para um expert |
| car01 | ter 27/10, 12h00 | 6 lâminas | capa "Eu só tinha um computador e um sonho." | | | carrossel (fora da régua de reels) | Comenta o número; Me manda a data no direct |
| pf01 (story) | ter 27/10, 16h00 | 24,0 s | "DENTISTA, ESSE CASE EU CONTEI NA TV" de 0 a 2 s | "Bom, o primeiro de tudo foi fazendo..." | "milhão" aos 17,8 s | história com profissão nomeada | no vídeo: Manda para um dentista |
| ci01 | qua 28/10, 21h00 | 36,6 s | gancho "O MELHOR MARKETING" | "Que até hoje é o melhor marketing."; a Mirna pergunta "Ainda?" aos 2,4 s | "ouro" aos 14,3 s | diálogo | E você, o que teria respondido? |
| po01 | qui 29/10, 21h00 | 23,5 s | Z2 | "Então você precisa ter os gatilhos corretos" | conceitos desde 1,2 s | lista (a mais salva depois de tutorial: 12,2 por 100 curtidas) | Comenta a palavra; Salva |
| pb02 | sex 30/10, 21h00 | 26,6 s | Z2, frase inteira na tela | "Bom, eu decidi, então, ir para o marketing digital..." | "45" aos 18,5 s; "250" aos 21,0 s | antes e depois contado como história | Me manda a data no direct |
| tl02 | sáb 31/10, 18h30 | 35,3 s | "PARTE 2: EMPREENDER EM 35 SEGUNDOS" sobre o Bruno de frente; aos 2,5 s, Bruno e Mirna | voz real a partir de 1,6 s; 10,4 s sem voz real de 16,55 a 26,95 s [`tl02.spec.json`, `voz_trechos`] | "família" perto de 30,2 s | montagem com laço [HIPÓTESE] | Comenta o número (legenda avisa 02/11) |
| tl03 | sáb 07/11, 18h30 | 36,0 s | pergunta da Mirna na tela "Você foi investir em EQUIPAMENTO?" com o Bruno de frente | a pergunta da TV desde 0,14 s | resposta aos 28,1 s ("UM BOM COMPUTADOR") | pergunta aberta e resposta (família 3 do swipe file) [HIPÓTESE] | Comenta o seu primeiro investimento |
| ob02 (proposto, 03-plano) | seg 02/11, 21h00 | ficha 25,97 s; render: sem dado | objeção "Nunca ouvi falar de você." | trecho do mc02 + os 21,4 s do pf01 | "um milhão e meio" perto de 22,1 s | história com objeção | no vídeo: Me manda a sua área no direct |
| ob01 (proposto) | qua 04/11, 21h00 | ficha 12,4 s de fala; render: sem dado | objeção "Não tenho tempo pra lançar." | "O que eu fiz?" (voz a conferir: Bruno ou Mirna) [03-plano] | "equipe" perto de 6,0 s | história com objeção | no vídeo: Me manda a sua área no direct |
| ob03 (proposto) | sex 06/11, 21h00 | ficha 9,4 s de fala; render: sem dado | objeção "Meu consultório vive de indicação." | "Ah, com certeza." | "potencializar o seu negócio" perto de 8,1 s | história com objeção | no vídeo: Me manda a sua área no direct |

**Leituras pelo playbook**
- **A favor da série** [FATO]: o Bruno em cena nos 3 primeiros segundos em todas as peças conferidas (fichas e quadros de tl01 a tl03); texto na tela desde o quadro 0; legenda queimada; 1 reel por dia; tl01, tl02 e tl03 no fim de semana; 5 hashtags.
- **Ápice tarde** [FATO e HIPÓTESE]: em pb01, pb02 e pf01 o número chega entre 16 e 21 s, quase 3 vezes o assistido mediano da conta (5,85 s). A maior parte de quem assiste sai antes do número [HIPÓTESE, a medir pelo pulo e pelo assistido de cada um]. A primeira linha da legenda já traz o número em pb01 e pb02 ("Fui DJ por 20 anos."; "Um restaurante que vendia 45 mil."), medido em 1,11x.
- **Proposta TESTAR, uma peça só** [HIPÓTESE]: o pb02 ganha 2 s do ápice no quadro 0 ("colocamos ele para vender 250 mil", trecho literal) e volta ao começo, como manda o flash-forward do playbook para história. O pb01 sai como está e serve de comparação. Muda só a montagem. Prazo: novo render e troca do arquivo no PostZen pelo Bruno antes de sex 30/10, 21h. Tempo de render: sem dado. Leitura: pulo do pb02 abaixo do pb01 em 48 h.
- **Cuidado no pf01** [FATO, 02-provas e CLAUDE.md]: abrir no "milhão e meio" põe o número de um caso na primeira frase; a regra da conta pede a frase de que o número não se repete igual. Se o pf01 virar reel, o ápice no quadro 0 só com essa frase na tela (o ob02 já traz a caixa "FATO DO CASO" com ela aos 22,23 s [`ob02.spec.json`]).
- **Timelapse** [HIPÓTESE]: pela régua de formato, tl01 e tl02 tendem a ficar abaixo de história. O catálogo dá nota 6,5 e manda não repetir abaixo de 0,8x com pulo acima de 75% [FATO, catálogo F5]. O tl02 agendado tem 10,4 s sem voz real, acima do teto de 8 s da mesma ficha [FATO].
- **Repetição dentro da série** [FATO, fichas]: ob02 reaproveita 21,4 s do pf01; ob01 reaproveita o trecho do mc03 (1580,7 a 1584,1 s); tl05 reaproveita perto de 6,6 s do ci01; tl02 reaproveita 2,4 s do pb02 ("250 mil"). Pelo playbook, só o par pf01 e ob02 passa do que se chamaria repetição [HIPÓTESE: o playbook não dá o percentual de áudio que o Instagram trata como repetido].

---

## 8. A exibição de 02/11 pela régua do playbook

### 8.1 O que o playbook mede e o que não mede
- [FATO, `buzzfy_playbook`] Mede reels contra os outros reels do mesmo criador: abertura, envio, formato, legenda, sequência depois de um hit, repost como Trial Reel, ritmo e dia da semana. Não mede TV, evento externo nem feriado.
- [FATO, contexto.md e 00-enquadramento] Exibição na seg 02/11 (Finados), horário sem dado. Campinas tem 33% dos seguidores e 53% dos engajados. As edições recentes do programa no site da TV Câmara têm de 27 a 124 views [F4]. Quantas pessoas chegam ao perfil por causa da TV: sem dado.
- Consequência: nenhum número do playbook diz se os cortes rendem mais antes ou depois de 02/11. O que ele dá são travas de execução (8.2) e a mecânica de custo de cada escolha (8.3).

### 8.2 Travas para a semana da exibição (traduzidas de regras medidas)

| Trava | Regra de origem [FATO, playbook] | Aplicação |
|---|---|---|
| E1. A chamada para assistir nunca é a primeira frase de um reel | openings: "A promotional first line was the strongest sign of a weak hook"; captions: "An offer or link goes in the caption, not the opening line" | A data vai na linha 2 da legenda (como já está no tl01 e no tl02) e nos stories. O quadro 0 continua com a frase mais interessante do corte |
| E2. @ da Mirna no texto da legenda das peças com imagem ou voz dela | captions: "@mention or collab" 1,13x; "Tag who's in it" | Pede o @ dela (sem dado). A marcação na mídia continua à mão pelo Bruno no app. Se o @ no texto avisa a Mirna: [PRIOR] sim, sem fonte nesta rodada |
| E3. Pedido de seguir de seg 02/11 a qua 04/11 | hot_streaks: "Ask for the follow on the follow-ups: new viewers are on the profile now" (1,12x) | [HIPÓTESE] Quem vem da TV chega ao perfil como quem vem de um hit. Um pedido por legenda: nas peças desses 3 dias o pedido da legenda é seguir. Conflito com o CTA queimado no vídeo dos ob (seção 11) |
| E4. Peça vista antes de 02/11 só volta depois como remake | second_life: "Change at least two real things... Post the remake as a Trial Reel" | O "o que eu disse na TV" de um corte já publicado leva nova abertura e corte de 20 a 40%, ou resposta a comentário; sai como Trial Reel; só vai ao feed se bater o alcance usual |
| E5. Promessa do tl01 vira sequência por resposta a comentário | hot_streaks: "the other side of the story, or an answer to the top comment, ideally as a reply-to-comment reel" | "O mais votado eu solto inteiro depois que a entrevista for ao ar" sai a partir de ter 03/11, como reel de resposta ao comentário (feito no app pelo Bruno). Com menos de 5 votos somados, a regra do catálogo manda seguir a nota e dizer isso nos stories [FATO, catálogo F5]. Assuntos 1 e 6 do tl01 não têm peça pronta [FATO, 00-enquadramento] |
| E6. "Foi ao ar" só depois do horário confirmado | regra da conta, não do playbook [FATO, 00-enquadramento, item 2] | Vale para legenda, quadro 0 e remake |

### 8.3 Manter os 5 cortes antes de 02/11 ou mover para depois: o que o playbook acrescenta (insumo do D1, sem decidir)

| Mecânica [FATO, playbook; aplicação HIPÓTESE] | Manter de 26 a 30/10 (como está) | Mover para 03/11 em diante |
|---|---|---|
| Sequência em 48 h | Se um corte bater 171 views, a sequência está pronta na própria grade (mesma linha, outro assunto) | Antes de 02/11 a linha da TV fica com tl01 e tl02 (montagem [HIPÓTESE]); a única história com rosto pronta para seguir um sinal é o pf01 |
| Segunda vida | O que sair antes só volta depois como remake: 15% de chance de bater o alcance usual se o original ficar entre 2 e 5x; 7% entre 1 e 2x | Os cortes chegam inéditos ao feed depois da exibição; nada a remontar |
| Ritmo | S1 com 6 reels (já agendado) | S1 precisa de outro estoque com rosto: R1 a R3 (edição, prazo sem dado) ou Dentista C (terceira edição da mesma fala); S2 recebe 5 cortes + ob + tl03 para 6 dias (passa de 1 por dia ou empurra para a S3) |
| Fim de semana (1,10x) | tl01 e tl02 ocupam sábado e domingo | igual |
| Efeito da TV | sem dado | sem dado |

Leitura [HIPÓTESE]: o único ponto assimétrico do playbook é a prontidão da sequência (a favor de manter) contra o custo de remontar depois (a favor de mover). O resto é igual ou sem dado.

---

## 9. Protocolo de sequência · dom 25/10 a sáb 07/11

### 9.1 Leituras (Buzzfy `ig_reel_checkup` ou `ig_post_stats`, só leitura)

| Peça | Sai | Leitura de 24 h | Leitura de 48 h |
|---|---|---|---|
| Dentista B | sáb 24/10, 21h00 | dom 25/10, 21h00 | seg 26/10, 21h00 |
| tl01 | dom 25/10, 18h30 | seg 26/10, 18h30 | ter 27/10, 18h30 |
| pb01 | seg 26/10, 21h00 | ter 27/10, 21h00 | qua 28/10, 21h00 |
| car01 | ter 27/10, 12h00 | qua 28/10, 12h00 | qui 29/10, 12h00 |
| ci01 | qua 28/10, 21h00 | qui 29/10, 21h00 | sex 30/10, 21h00 |
| po01 | qui 29/10, 21h00 | sex 30/10, 21h00 | sáb 31/10, 21h00 |
| pb02 | sex 30/10, 21h00 | sáb 31/10, 21h00 | dom 01/11, 21h00 |
| tl02 | sáb 31/10, 18h30 | dom 01/11, 18h30 | seg 02/11, 18h30 |
| R1, Trial Reel (proposto) | dom 01/11, 11h00 | seg 02/11, 11h00 | ter 03/11, 11h00 |
| pf01 como reel (proposto) | dom 01/11, 18h30 | seg 02/11, 18h30 | ter 03/11, 18h30 |
| R2, Trial Reel (proposto) | ter 03/11, 11h00 | qua 04/11, 11h00 | qui 05/11, 11h00 |
| "O mais votado" (proposto) | ter 03/11, 21h00 | qua 04/11, 21h00 | qui 05/11, 21h00 |
| ob01 (proposto) | qua 04/11, 21h00 | qui 05/11, 21h00 | sex 06/11, 21h00 |
| R3, Trial Reel (proposto) | qui 05/11, 11h00 | sex 06/11, 11h00 | sáb 07/11, 11h00 |
| ob03 (proposto) | sex 06/11, 21h00 | sáb 07/11, 21h00 | dom 08/11, 21h00 |
| tl03 | sáb 07/11, 18h30 | dom 08/11, 18h30 | seg 09/11, 18h30 |

[FATO, conta sobre as datas] Toda a S1 fecha 48 h até seg 02/11, 18h30 (o último é o tl02): o Módulo 7 de 02/11 lê a S1 inteira a partir das 18h30. A leitura de 24 h pode vir marcada `provisional` [FATO, campo do `ig_reel_checkup`].

### 9.2 Regras

- **S1. Sinal** (171 views ou mais na leitura de 24 h, ou 2 compartilhamentos ou mais com alcance até 250): a sequência pré-definida (9.3) ocupa a próxima vaga de feed dentro de 48 h da saída do sinal. A peça deslocada vai para a primeira vaga livre a partir de ter 03/11. Quem troca no PostZen é o Bruno.
- **S2. Estouro** (285 views ou mais): além de S1, a legenda da sequência pede para seguir ("Segue para ver a parte 2", 1,12x) e o reel entra na lista de remake (seção 10).
- **S3. Entre 46 e 170 views**: a grade segue como está.
- **S4. Fraco** (abaixo de 46 views com pulo acima de 75%): um post fraco não muda o plano [FATO, playbook hot_streaks e checklists]. PARAR só com 2 reels do mesmo formato nessa faixa (D5 do enquadramento). Exceção do timelapse: a regra do catálogo F5 para o formato depois de 1 fraco; se o conselho seguir o F5 e o tl01 cair nessa faixa, o tl02 sai do feed e vai como Trial Reel no sáb 31/10, 11h, e a vaga das 18h30 fica com o pf01 como reel (adiantado de dom 01/11) [HIPÓTESE].
- **S5.** Nenhuma sequência muda assunto e formato ao mesmo tempo.
- **S6.** Um pedido por legenda. Sequência pede seguir; peça com destinatário nomeado pede envio; de 02 a 04/11 o pedido é seguir (E3); TABULEIRO só na regra da conta (150 de alcance em 48 h no anterior do mesmo formato).
- **S7.** No máximo 1 reel de feed por dia e 6 h ou mais entre reels, Trial Reel incluído.
- **S8.** Sábado e domingo ficam com reel (1,10x).
- **S9.** Travas E1 a E6 da seção 8.2 em toda peça de 25/10 a 07/11.

### 9.3 Mapa de sequência (definido antes, como manda o playbook: "keep one or two reels finished and waiting")

| Se bater S1 | Sequência | Pronta? | Muda | Mantém | Vaga dentro de 48 h | Deslocado vai para |
|---|---|---|---|---|---|---|
| Dentista B | pf01 como reel | sim (24,0 s) | formato (corte da TV) | dentista, profissão nomeada no quadro 0 | seg 26/10, 21h00 (a vaga de 24 h é o tl01, já anunciado no story st01) | pb01 para dom 01/11, 18h30; o story pf01 de ter 27/10 sai do PostZen (repetiria o reel do dia anterior) |
| tl01 | tl02 "Parte 2" | sim (35,3 s) | assunto (outro índice) | formato timelapse | ter 27/10, 18h30 (dia do car01 às 12h: 2 posts de feed, dentro da regra) | sáb 31/10, 18h30 fica com o tl03; a fila de sábados anda uma casa |
| pb01 | pb02 | sim | assunto | formato P&B, história com número | qua 28/10, 21h00 | ci01 para sex 30/10, 21h00 (o TESTAR de abertura do pb02 passa a vencer qua 28/10, 21h) |
| ci01 | tl05 (régua do tempo, termina em "o melhor marketing") | sim (35,3 s) | formato | assunto | sex 30/10, 21h00 | pb02 para qui 05/11, 21h00 (primeira vaga livre depois de 02/11; ter 03/11 é do "mais votado"), já como "o que eu disse na TV"; a vaga de 21/11 do tl05 fica livre |
| po01 | sem sequência pronta | não | | | | carrossel do Método Xeque-Mate na S2 (a produzir) |
| pb02 | pf01 como reel | sim | assunto (restaurante para dentista) | formato: corte da TV, história com número | dom 01/11, 18h30 (já é a vaga proposta do pf01) | nada |
| tl02 | tl03 | sim (36,0 s) | assunto | timelapse da mesma gravação | seg 02/11, 18h30 (dia da exibição; "a pergunta da TV" no dia da TV) | sáb 07/11 fica com o tl04 |
| pf01 como reel | roteiro 7 "Medo do código" (dentista) | não: depende de gravação | formato (volta ao modelo A) | dentista | primeira vaga livre depois da gravação | |
| Trial Reel que bater o alcance usual | segunda versão do mesmo remake | não | 2 mudanças reais | | S3 | |

**Se o D1 mover os cortes para depois de 02/11**, o mapa vale com as datas novas; o que muda está na seção 8.3: antes de 02/11 só tl01, tl02 e pf01 servem de sequência.

[FATO, contas de `listPosts`] Nenhuma troca acima muda a contagem de reels da S1 (6), porque cada sequência ocupa a vaga de uma peça que sai. A S1 continua acima da regra de 5 do CLAUDE.md: o 6º reel (tl02) precisa de motivo escrito (D3).

### 9.4 A linha do Dentista A: 3 a 5 reels até 07/11

| Peça | Muda em relação ao A | Depende de | Situação |
|---|---|---|---|
| Dentista B | formato (tela dividida); fala, abertura e duração iguais | nada | agendado sáb 24/10, 21h [FATO, `listPosts`] |
| pf01 como reel | formato (corte da TV) | o catálogo deixa o reel de PROFISSAO para quando o Módulo 7 mandar DOBRAR profissão nomeada; o A ficou em 4,68x, acima do 2x do DOBRAR [FATO, catálogo F11 e `ig_reel_checkup`]; e não repetir o ob02 na mesma quinzena | pronto; proposto dom 01/11, 18h30 |
| Roteiro 7 "Medo do código" (dentista) | assunto (outra dor do mesmo público), modelo A igual | gravação | roteiro pronto [FATO, roteiros-20-videos] |
| Roteiro de outra profissão (consórcio, nutricionista) | assunto (outra profissão), modelo A igual | gravação | roteiro pronto |

[ESTIMATIVA] Sem gravação, a linha chega a 2 de 3 a 5. Para o mínimo de 3, falta 1 roteiro gravado no modelo A até perto de sáb 31/10; para 5, faltam 3. Data da próxima sessão: sem dado.

Abertura dos roteiros pelo playbook [HIPÓTESE, texto a aprovar pelo Bruno]: a do roteiro 7 tem 11 palavras ("Dentista, você tem medo de postar e tomar processo no conselho?"); corte de até 8 palavras: "Dentista, medo de processo no conselho?". O CTA falado dos roteiros ("comenta a sua profissão") é pedido de comentário (1,00x); trocar por envio ou por seguir é decisão do conselho, porque o comentário é a porta do lead.

**Dentista B e a repetição** [FATO e HIPÓTESE]: pela regra de sequência, o B muda uma coisa (formato) e está dentro. Pela de segunda vida, ele repete a fala, a primeira frase, a legenda queimada e a duração do A 3 dias depois: 0 das 4 mudanças reais da lista. Se o Instagram trata o B como repetido: sem dado. Sem motivo medido, o B sai como está e a leitura de 24 h decide.

### 9.5 A semana da exibição (dom 01/11 a sáb 07/11), com a S1 como está

| Dia | Feed (reel) | Trial Reel (app) | Pedido da legenda | Dependência |
|---|---|---|---|---|
| dom 01/11 | 18h30 pf01 como reel (véspera; data na linha 2) | 11h00 R1 | envio ("Manda para um dentista") | o Bruno sobe o arquivo e marca a Mirna; o story pf01 de 27/10 já terá expirado (efeito de story para reel: sem dado) |
| seg 02/11 (Finados, exibição) | sem reel novo, ou tl03 às 18h30 se o tl02 bater S1 | | seguir | chamada para assistir só em stories; horário da exibição sem dado; Módulo 7 a partir das 18h30 |
| ter 03/11 | 21h00 "o mais votado", reel de resposta ao comentário do tl01 | 11h00 R2 | seguir | votos do tl01; peça pronta só para os assuntos 2, 3, 4, 5 e 7; se o assunto já saiu na S1, a versão inteira precisa de 2 mudanças (resposta ao comentário e nova abertura) |
| qua 04/11 | 21h00 ob01 | | seguir | render e conferência da voz de 1316,2 a 1326,4 s [FATO, 03-plano] |
| qui 05/11 | sem reel | 11h00 R3 | | R3 e ob01 tratam de equipe: se o ob01 bater S1, o R3 já é a sequência dele (mesmo assunto, formato selfie) |
| sex 06/11 | 21h00 ob03 | | um pedido | render |
| sáb 07/11 | 18h30 tl03 (agendado) | | Comenta o primeiro investimento | |

[ESTIMATIVA, contagem da tabela] S2 com 5 reels de feed (pf01, mais votado, ob01, ob03, tl03), dentro da regra de 5, sem reel no dia da exibição. Cada peça que o mapa 9.3 empurrar para a S2 soma um reel; acima de 5, sai primeiro o ob03 (render sem dado) e depois o ob01. O ob02 sai desta quinzena porque o pf01 ocupa o mesmo áudio; se o conselho preferir o ob02 no feed, o pf01 fica só como story e a linha do Dentista A volta a 1 peça sem gravação. Reel no dia 02/11: o playbook não tem número para feriado nem para dia de TV; fica como TESTAR do conselho (D3), com motivo escrito se entrar.

---

## 10. Protocolo de remake (segunda vida) · 25/10 a 07/11

### 10.1 Candidatos

| Reel | Saiu (SP) | x normal | Pulo | Duração | Legenda queimada | Chance do playbook pelo original | Entra? |
|---|---|---|---|---|---|---|---|
| R1 "Ele nunca fez um anúncio" | sáb 03/10, 23h06 | 10,14 | 53,2% | 74,6 s | não | 35% (5x ou mais); faixa de pulo acima de 50%: sem número no playbook | sim |
| R2 "90% dos lançamentos que flopam" | dom 04/10, 11h11 | 4,42 | 45,7% | 69,5 s | sim | 15% (2 a 5x); 16% (pulo de 40 a 50%) | sim |
| R3 "Problema de equipe" | seg 05/10, 21h58 | 3,61 | 49,6% | 74,7 s | sim | 15%; 16% | sim |
| Dentista A | qua 21/10, 21h00 | 4,68 | 46,6% | 36,4 s | sim | 15%; 16% | não: B e C já são reedições da mesma fala |
| Resumo de 2024 | ter 31/12/2024, 21h02 | 9,14 | 49,8% | sem dado | sem dado | 35% | não: resumo pessoal de ano, fora do posicionamento e fora da grade (`on_profile_grid: false`) |
| "Você gravou o curso inteiro" | dom 11/10, 18h29 | 3,75 | 86,9% | 37,6 s | sim | 15% | não nas 2 semanas: sem rosto; cumprir o CLAUDE.md pede abertura com o Bruno, ou seja, gravação |
| 4 reels de 2021 a 2024 | | sem multiplicador | 5,7% a 22,1% | | | | não: conteúdo de igreja, fora do posicionamento, 6 a 30 hashtags; sem normal na época para comparar [FATO, `ig_reel_checkup` com `until`] |

Fontes [FATO]: `ig_reel_checkup`, `ig_post_stats`, tags do Buzzfy (duração, legenda queimada e primeira fala) e `ig_posts` (data em UTC convertida para São Paulo).

### 10.2 Mudanças por remake (o playbook pede 2 ou mais)

| Remake | Abertura nova | Legenda queimada | Corte de 20 a 40% | Total | Gravação |
|---|---|---|---|---|---|
| R1 | sai "Deixa eu te contar uma coisa." e abre em "Jesus foi o maior de todos." (6 palavras), com "ELE NUNCA FEZ UM ANÚNCIO" na tela desde o quadro 0 [primeira fala: FATO, tags do Buzzfy] | entra (Legenda Gigante) | 74,6 s para 45 a 60 s [ESTIMATIVA] | 3 | não |
| R2 | sai "Ei, vem cá, escuta essa:" e abre no "90% dos lançamentos que floparam..." | já tem | 69,5 s para 42 a 56 s | 2 | não |
| R3 | a frase de 15 palavras ("Essa é para você, expert, que gosta de fazer tudo sozinho e entrega pela metade.") vira um trecho literal mais curto; qual: sem dado até transcrever | já tem | 74,7 s para 45 a 60 s | 2 | não |

- **Arquivo de origem**: nenhum dos 3 está no repositório. O Instagram libera o vídeo dos 3 (`video_url_withheld: false`) [FATO, `ig_posts` às 14h53]; o link é temporário; a cópia sai em 720p [F5]. O original do celular do Bruno, se existir, é melhor. Transcrição palavra a palavra antes de editar (regra de edição do CLAUDE.md).
- **Texto fiel**: só corte, nenhuma palavra reescrita.
- **Legenda do post**: até 5 hashtags e um pedido só ("Salva", 1,16x). O R1 original anunciava "uma saga de 7 dias" e pedia "Salva e me acompanha até sexta" [FATO, `ig_posts`]: o remake não repete a promessa. O R3 pedia "Marca aqui" (marcar alguém, 1,10x) e pode manter.

### 10.3 Como sai
- Como **Trial Reel** (vai primeiro para quem não segue) [FATO, playbook second_life]. Quem posta é o Bruno, no app. Se o PostZen agenda Trial Reel: sem dado. O Módulo 1 deixou trial reels para depois e o catálogo diz que essa decisão é do Módulo 7 [FATO, catálogo seção 8]: decisão do conselho.
- Se Trial Reel conta na regra de 5 reels por semana: decisão do Bruno [HIPÓTESE: não conta, porque não vai à grade nem aos seguidores].
- Datas [HIPÓTESE], 11h, a 6 h ou mais de qualquer reel do feed e no máximo 1 por dia: R1 dom 01/11 (7h30 antes do pf01; 16h30 depois do tl02); R2 ter 03/11 (10 h antes do "mais votado"); R3 qui 05/11 (dia sem reel no feed). Edição do R1 pronta até sex 30/10.
- A exibição não muda as datas: Trial Reel vai para quem não segue e não ocupa vaga de feed [FATO, playbook]. Se o Trial Reel aparece para quem chega ao perfil vindo da TV: sem dado.

### 10.4 Leitura e decisão (48 h depois)

| Resultado do Trial Reel | Decisão [FATO, regra do playbook; números da conta] |
|---|---|
| Alcance acima de 37,5 (alcance usual da conta) | vai para o feed numa vaga da S3 e ganha uma segunda versão (playbook: 34% de nova vitória) |
| Alcance de 150 ou mais | além disso, o próximo do mesmo formato pode levar TABULEIRO (regra da conta) |
| Alcance até 37,5 | fica como teste; nada vai ao feed; não muda o plano |

O alcance usual do playbook inclui seguidores e o Trial Reel não: a régua de 37,5 é literal do playbook e baixa para esta conta [ESTIMATIVA]. O conselho pode subir a régua de entrada no feed para 0,8x ou 2x do normal em views (46 ou 114).

### 10.5 Remake dos cortes da TV depois de 02/11 (o "o que eu disse na TV")
- **Quem entra** [FATO, regra do playbook]: só o corte da S1 com 171 views ou mais em 48 h (3x). Abaixo disso o playbook dá 7% (original de 1 a 2x) a 15% (2 a 5x) de chance ao repost.
- **Duas mudanças reais** [HIPÓTESE, a aprovar]: abertura no ápice (pb02: "colocamos ele para vender 250 mil"; pb01: "acabou sendo uma profissão por 20 anos"; ci01: "nem tudo que vemos é ouro") e corte de 20 a 40%, ou formato de resposta a comentário. Rótulo "foi ao ar" só depois do horário confirmado.
- **Quando**: Trial Reel a partir de ter 03/11, 11h, numa vaga que R2 ou R3 não ocupem, ou na S3.

### 10.6 Fora das 2 semanas
- **Dentista C no feed**: terceira edição da mesma fala de 36,37 s, com a mesma abertura [FATO, `ffprobe` e `dent.html`]. Pelo playbook, só com 2 mudanças reais e como Trial Reel; pelo brief do dentista de 21/10, amostra em outubro e anúncio 4:5 depois de 18/11, com a Res. CFO 196/2019 conferida [FATO, `videos/nichos/dentista/god/run/10-decision-brief.md`]. Fica fora até o Bruno decidir.
- **Remake do próprio Dentista A**: fora pelo mesmo motivo.
- **"Você gravou o curso inteiro"**: entra quando houver gravação (abertura com o Bruno, corte para cerca de 30 s, como pede o 00-SISTEMA).

### 10.7 O plano de 4 semanas do playbook, encaixado no calendário [FATO, checklists; datas HIPÓTESE]
- Semana 1, achar os vencedores: feito nesta frente. A conta tem 24 reels com dados (20 na base e 4 de 2021 a 2024), não 50. Com 3x ou mais: 6 (R1, resumo de 2024, A, R2, "Você gravou", R3). Com pulo abaixo de 35%: nenhum desde 2025. Os 2 formatos que eles dividem: talking head selfie (4) e texto com narração (1); o resumo de 2024 sem dado de formato.
- Semana 2, remontar e testar: R1 a R3 como Trial Reel de 01 a 05/11.
- Semana 3, correr atrás da sequência: S1 a S9 desta seção, de 25/10 a 07/11.
- Semana 4, dobrar: segunda versão de cada Trial Reel que ganhou, a partir de 08/11.

---

## 11. Conflitos com outros documentos

1. **Três bases.** Esta frente usa 57 views. O enquadramento, o catálogo e o F4 usam 53 de alcance; a rodada de 21/10 usou 37,5 de alcance. Em views, 0,8x = 46 e 2x = 114; em 53 de alcance, 42 e 106. Não misturar.
2. **contexto.md contra PostZen.** O contexto (14h40) diz que tl02 a tl05 estão "propostos e ainda não agendados"; o PostZen (14h50) mostra os 4 agendados aos sábados, 18h30. Vale o PostZen.
3. **Ritmo da S1.** 6 reels agendados (tl01, pb01, ci01, po01, pb02, tl02) contra 5 do CLAUDE.md. O playbook põe 5 e 6 na mesma faixa (7,0%) e avisa que quem posta mais pode diferir em outras coisas: não sustenta mudar a regra nem condena o 6º.
4. **"Uma coisa por vez" contra "duas mudanças reais".** A sequência pede mudar só assunto ou formato; o remake pede 2 mudanças reais para não ser visto como repetido. O Dentista B cumpre a primeira e falha a segunda, porque é a mesma fala.
5. **PARAR com n de 1.** O catálogo F5 para o timelapse depois de um só fraco; o playbook diz que um post fraco não muda o plano; o D5 do enquadramento pede n de 2. A saída proposta em S4 (tl02 como Trial Reel) atende os três.
6. **pf01 contra ob02.** O 03-plano põe o ob02 no feed em seg 02/11, 21h; esta frente propõe o pf01 como reel em dom 01/11, 18h30. Os dois têm os mesmos 21,4 s de fala. Um dos dois por quinzena.
7. **Pedido de seguir contra o CTA queimado dos ob.** E3 pede "seguir" na legenda de 02 a 04/11; ob01 a ob03 trazem no vídeo "Me manda a sua área no direct" [FATO, fichas]. O playbook mede o pedido da legenda; vídeo e legenda com pedidos diferentes somam 2 pedidos na mesma peça. Decisão do conselho (D4 e D6).
8. **Pedido de comentário.** O playbook mede "comenta" em 1,00x; a conta depende do comentário para o lead (TABULEIRO, votação do tl01 e do tl02, CTA falado dos roteiros). O A pediu comentário e teve 0.
9. **tl02 com 10,4 s sem voz real.** O F4 pediu correção antes de agendar; o arquivo agendado é o render da ficha atual [FATO, tamanho igual]. Corrigir pede novo render e troca do arquivo pelo Bruno antes de sáb 31/10, 18h30.
10. **Horário do contexto.** O contexto.md lista "reel de 04/10 14h (4,42x)"; o horário é UTC. Em São Paulo o R2 saiu dom 04/10, 11h11, e o R1 sáb 03/10, 23h06 [FATO, `ig_posts`]. Os 2 maiores hits de outubro saíram no fim de semana.

---

## 12. Lacunas (sem dado)

- Efeito da exibição na TV sobre visitas ao perfil, seguidores e alcance dos reels; horário da exibição; audiência do programa.
- Se o @ da Mirna na legenda a notifica e se ela reposta; o @ dela.
- Se o Instagram trata como repetidos: Dentista B contra A; pf01 story contra pf01 reel; pf01 contra ob02.
- Render de ob01 a ob03 e a conferência da voz no ob01.
- Formato, gancho e duração da série 2 e do Dentista A pelo Buzzfy (`tags: null`); se a voz dos sem rosto de 30/09 a 11/10 era sintética.
- Divisão seguidor e não seguidor por reel (o `ig_post_stats` não traz).
- Compartilhamento por 100 curtidas pontuável: nenhum reel da conta passa de 50 curtidas.
- Se stories contam como "post seguinte" na queda do efeito de sequência; o efeito de sequência (1,81x) foi medido depois de estouros de 5x e o A ficou em 4,68x.
- Por que "Você gravou o curso inteiro" teve 169 de alcance com 86,9% de pulo.
- Arquivo original dos remakes R1 a R3 e transcrição completa deles.
- Se o PostZen agenda Trial Reel; se Trial Reel conta no ritmo de 5 reels e na distância de 6 h; se aparece para quem chega ao perfil.
- Tempo de render para refazer a abertura do pb02 ou o trecho sem voz do tl02.
- Alcance em feriado (02/11).
- Votos do tl01 e do tl02 (os posts ainda não saíram).
- Data da próxima gravação do Bruno.
- Os números do playbook são padrões medidos em 531.037 criadores, sem garantia para esta conta [FATO, a própria ferramenta: "patterns across real accounts, not guarantees"].
