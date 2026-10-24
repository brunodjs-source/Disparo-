# F1 · Auditoria da conta @o_estrategista.com.br · rodada de 24/10/2026

Frente F1 da pesquisa do conselho Agência Reunida. Leituras ao vivo, somente leitura, feitas entre 13h28 e 13h40 de sábado 24/10/2026 (horário de São Paulo). Nada foi publicado, agendado ou alterado no Instagram, no Buzzfy ou no PostZen.

Etiquetas: [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha uma objeção sozinho. Métrica que falta: "sem dado".

---

## 0. Consultas feitas (todas responderam; nenhum erro de consulta)

| # | Consulta | Parâmetros | Resultado |
|---|---|---|---|
| 1 | Buzzfy `ig_posts` | kind=all, limit=50 | 50 itens; os 35 primeiros são a fase atual (30/09 a 22/10 UTC); os outros 15 são de 2020 a 2025, conteúdo pessoal |
| 2 | Buzzfy `ig_posts` | kind=stories | 1 story ativo (24/10, 09h33) |
| 3 | Buzzfy `ig_posts` | since=2026-09-29, include_media_urls | 35 itens com capa. A saída passou do limite de tela e foi salva em arquivo; o arquivo foi lido inteiro por script. As 35 capas foram baixadas para conferência visual numa pasta temporária (não publicadas) |
| 4 | Buzzfy `ig_post_stats` | 20 ids + 17 ids (35 da fase, 1 story, 1 reel de 2025) | 37 itens, status ok |
| 5 | Buzzfy `ig_reel_checkup` | 2 chamadas de 10 ids | 20 reels; tags de vídeo só para 7 |
| 6 | Buzzfy `ig_account_stats` | 30 dias (24/09 16h31 UTC a 24/10 16h31 UTC) | ok |
| 7 | Buzzfy `ig_follower_growth` | 30 dias | ok; 22 e 23/10 pendentes |
| 8 | Buzzfy `ig_best_times` | America/Sao_Paulo, 35 posts | ok |
| 9 | Buzzfy `ig_audience` | this_month | ok |
| 10 | Buzzfy `buzzfy_playbook` | openings, small_accounts | ok |
| 11 | PostZen `listCommentAutomations` | accountId j97772ycndetk3f1wcdbh14p898g4b8w | 17 automações ativas |
| 12 | PostZen `listPosts` | mesma conta, status=published | 20 posts publicados pelo PostZen (12/10 a 22/10) |
| 13 | PostZen `listCommentAutomationLogs` | CHECKLIST e TABULEIRO | 1 log e 0 log |

Fontes do repositório usadas para classificar formato e voz: `videos/v01` a `videos/v08` (git log de 11/10: "Vídeo 01 (Pesquisa) com narração Microsoft neural Antonio"; pastas com `t0.wav` a `t*.wav`, `index.html` e `capture.js`, sem arquivo de câmera), `videos/serie2/roteiros.json` (vozes `pf_dora`, `pm_alex`), `videos/serie2/*/timeline.json` e `videos/v0*/timeline.json` (duração da narração), `videos/nichos/dentista/words.json` e `render/` (Dentista A), `conteudo/sistema-instagram/00-SISTEMA.md`, `conteudo/modo-god-cronograma/contexto.md`, `videos/nichos/dentista/god/run/02-cadeiras/evidencias-E/buzzfy-leitura-2026-10-21.md`.

---

## 1. Resumo

1. [FATO, ig_post_stats] Nos 19 reels da fase atual, os 4 com o Bruno falando para a câmera têm mediana de 167,5 de alcance, 259,5 views, 48,1% de pulo e 15,1 s assistidos. Os 12 de animação com voz sintética têm 32,5 de alcance, 40 views, 83,8% de pulo e 5,2 s. Diferença: 5,2x no alcance, 6,5x nas views, 35,7 pontos a menos de pulo.
2. [FATO, ig_post_stats] Os 4 reels com o Bruno somam 67 das 73 curtidas de reel, 5 dos 6 comentários de reel e os 2 únicos salvamentos da fase. Os 12 sintéticos somam 2 curtidas e nenhum comentário.
3. [FATO, ig_post_stats + conferência visual das capas] No feed, as 9 peças com foto do Bruno na capa têm mediana de 126 de alcance e 46 visitas ao perfil somadas; as 7 de texto têm mediana de 35 e 2 visitas.
4. [FATO, ig_best_times + tabela da seção 3] O horário não tem leitura própria: todos os 8 reels postados entre 18h e 20h são sintéticos, e 3 dos 4 reels com o Bruno saíram entre 21h e 23h06. O "melhor horário" de 23h (média 180) é um reel e um carrossel; o de 07h (185) são os dois posts "Prazer, eu sou o Bruno".
5. [FATO, PostZen listCommentAutomations + logs] 17 automações de palavra-chave ativas, 1 disparo no total (CHECKLIST, carrossel de 12/10). As 19 peças com CTA de palavra-chave somam 3 comentários.
6. [FATO, ig_follower_growth] Último dia com seguidor novo: 13/10 (1). De 14/10 a 21/10, 8 dias fechados seguidos com zero seguidor novo.
7. [FATO, conferência visual] 11 dos 12 reels sintéticos aparecem no Instagram com a capa do cartão final "Comenta PALAVRA". Nenhum documento do repositório registrava isso.
8. Contexto conferido: quase todos os números batem. Um erro: de 12/10 a 21/10 foram 6 saídas, e não 7. Duas regras do CLAUDE.md e do 00-SISTEMA precisam de número novo (seção 2).

---

## 2. Confere o contexto, número a número

Leitura de hoje entre 13h28 e 13h40. Contexto coletado às 12h40.

| Item do contexto.md | Valor no contexto | Leitura de hoje | Veredito |
|---|---|---|---|
| Seguidores, seguindo, posts | 1.618, 3.528, 57 | 1.618, 3.528, 57 [ig_account_stats] | Confirmado |
| Bio e link | "Estrategista Digital / Ide e pregai o evangelho! / Visitor Host @bnisyrius / Dev @dashpronow"; /v2/ | Igual, com emojis no texto da bio; link https://estrategistadelancamento.com.br/v2/ [ig_account_stats] | Confirmado. A bio do Módulo 2 ainda não foi aplicada |
| Alcance 30 dias | 3.216; 1.907 de anúncio; orgânico perto de 1.300 | 3.216; 1.907 de anúncio; 2.792 não seguidores; 419 seguidores [ig_account_stats] | Confirmado. "Orgânico perto de 1.300" é [ESTIMATIVA] (3.216 menos 1.907 = 1.309): o Buzzfy avisa que as partes do alcance se sobrepõem e não somam |
| Views 30 dias | 12.652 (10.445 orgânicas) | 12.657 (10.450 orgânicas; 2.207 de anúncio) [ig_account_stats] | Confirmado (+5 desde as 12h40) |
| Por tipo | story 4.219 views e 756 contas; reel 2.242 e 608; carrossel 1.788 e 340; post 2.154 e 322 | story 4.224 e 756; reel 2.242 e 608; carrossel 1.788 e 340; post 2.154 e 322; IGTV 41 e 34 [ig_account_stats] | Confirmado (story +5). IGTV faltava no contexto |
| Engajamento 30 dias | 256 curtidas, 14 comentários, 3 salvamentos, 9 compartilhamentos, 7 respostas, 125 contas | Igual; total de interações 299; 1 repost [ig_account_stats] | Confirmado |
| Visitas e cliques | 447 visitas, 7 cliques no site | 447, 7; toques no link 0 [ig_account_stats] | Confirmado |
| Seguidores 24/09 a 21/10 | 53 entraram, 13 saíram, líquido +40; pico de 19 em 29/09 | Igual [ig_follower_growth] | Confirmado |
| "quase tudo até 11/10" | sem número | 52 das 53 entradas até 11/10 [ig_follower_growth] | Confirmado |
| 12/10 a 21/10 | 1 entrada e 7 saídas | 1 entrada (13/10) e 6 saídas (13/10: 1; 15/10: 1; 16/10: 2; 17/10: 2) [ig_follower_growth] | **Derrubado em 1.** As 7 saídas só fecham contando 11/10, e aí as entradas viram 5 |
| Normal do reel | 57 views, pulo 70,9% | 57 views, pulo 70,9%, 20 reels (19 da fase mais o de 01/01/2025) [ig_reel_checkup] | Confirmado |
| Dentista A | 267 views, 169 alcance, 4,68x, pulo 46,6%, 13 s, 10 curtidas, 0 e 0 | Igual, com 64,5 h [ig_post_stats] | Confirmado. Alcance de 167 (58 h) para 169 (64,5 h): a curva já achatou |
| Série 2 (18 a 20/10) | 0,37x a 1,07x, pulo 79% a 93% | 0,37x (Marqueteiro) a 1,07x (Caixa); pulo 78,9% a 92,9% [ig_reel_checkup] | Confirmado |
| Série de 12 a 14/10 | 0,58x a 0,93x, pulo 69% a 90% | 0,58x (Carrinho) a 0,93x (Aquecimento); pulo 69,4% a 89,7% [ig_reel_checkup] | Confirmado |
| Candidatos a refazer | "Ele nunca fez um anúncio" (04/10, 10,14x, 53%); 01/01/2025 (9,14x); Dentista A (4,68x); "04/10 14h" (4,42x); "Você gravou o curso inteiro" (11/10, 3,75x, 87%) | Mesma lista [ig_reel_checkup remake_candidates] | Confirmado, com 2 ressalvas: as datas e a hora "14h" estão em UTC (no horário de São Paulo, o "Ele nunca fez um anúncio" saiu sáb 03/10 às 23h06 e o "90%" dom 04/10 às 11h11); e 2 dos 5 candidatos são fracos para refazer (seção 7) |
| Janela de 48 h do Dentista A | fechada | window_open=false [ig_reel_checkup hot_streak] | Confirmado |
| Seguidores online | pico 18h (430), 19h (424), 17h (417), 21h (416) | Igual, média de 27 dias [ig_best_times] | Confirmado |
| Posts por hora e dia | 23h 180 (2), 21h 73 (5), 11h 66 (5), 18h 49 (6); sáb 180 (2), sex 134 (2), dom 106 (6) | Com 35 posts: 07h 185 (2), 23h 180 (2), 11h 77 (6), 21h 73 (5), 18h 49 (6); sáb 180 (2), sex 134 (2), qua 126 (7) [ig_best_times] | Muda com o tamanho da amostra (o contexto usou o padrão de 25). Leitura na seção 4.5 |
| Público | 35-44 39,8%, 45-54 27,6%, 25-34 21,5%; Campinas 33% e 53% dos engajados; homens 59% dos engajados; alcance pende para 25-34 (28,7%) | Igual [ig_audience] | Confirmado. Ressalva do próprio Buzzfy: o alcance inclui anúncio, então o "pende para 25-34" pode refletir a segmentação do anúncio |

Regras do CLAUDE.md e do 00-SISTEMA conferidas contra a leitura de hoje:

| Regra escrita | Número escrito | Hoje | Veredito |
|---|---|---|---|
| CLAUDE.md: reels com o Bruno falando | 2,4x a 5,8x acima da mediana | Alcance: 3,41x a 8,21x da mediana de 37,5; views: 3,61x a 10,14x da de 57 [ig_post_stats] | A direção se mantém; a faixa subiu porque a mediana caiu de 53 para 37,5 |
| CLAUDE.md: reels de animação com voz sintética | 0,15x a 0,8x, pulo 77% a 92% | Views: 0,37x a 1,07x em 11 reels e 3,75x no "Você gravou o curso inteiro"; pulo 69,4% a 92,9% [ig_reel_checkup] | **Derrubado em parte.** O piso de 0,15x sumiu quando os números assentaram; 2 dos 12 passaram de 1x. A regra de pôr o Bruno em cena continua de pé |
| 00-SISTEMA, ficha | Mediana de reel 53 de alcance, 74 views, 6,2 s, 68% de pulo (17 reels) | 37,5 de alcance, 57 views, 5,85 s, 70,9% (20 reels) [ig_post_stats baseline] | Desatualizado |
| 00-SISTEMA, conclusão | "Os 10 últimos reels feitos em animação com voz sintética ficaram todos abaixo da mediana (de 8 a 39 de alcance)" | São 12 reels sintéticos; alcance de 13 a 40 em 11 deles e 169 no "Você gravou o curso inteiro"; 2 acima de 37,5 (Caixa 40, Pesquisa 169) | **Derrubado em parte** |
| 00-SISTEMA, Módulo 1, item 3 | Seguindo 3.523, deixar de seguir cerca de 3.000 | Seguindo 3.528 [ig_account_stats] | O número subiu 5 desde 21/10: a limpeza não começou |

---

## 3. A amostra: as 35 peças da fase atual (30/09 a 21/10)

Os 30 mais recentes são as linhas 1 a 30 (02/10 a 21/10). As linhas 31 a 35 fecham a fase (30/09 e 01/10). Hora de São Paulo. "x" é o múltiplo de alcance que o Buzzfy calcula: reel contra a mediana de reel (37,5), feed contra a mediana dos 10 últimos posts de feed (49). Pulo e tempo assistido só existem para reel. C/C/C/S = curtidas, comentários, compartilhamentos, salvamentos. VP = visitas ao perfil (o Buzzfy só traz para feed e story).

Coluna "Bruno": **fala** = Bruno falando para a câmera [Buzzfy tags talking_head/selfie_closeup para 3 reels; Dentista A pela capa, pelo render e pelo contexto]; **sint.** = animação com narração sintética [repositório, ver seção 0]; **s/ rosto** = slideshow sem pessoa [Buzzfy tag framing=no_person; se a voz é a do Bruno: sem dado]; **foto** = foto do Bruno na capa [conferência visual das capas, 24/10]; **texto** = cartão de texto (os 4 estáticos da série 2 têm só um avatar pequeno no cabeçalho).

Colunas "Gancho" e "CTA": classificação deste relatório, feita pela primeira linha da legenda, pela capa e, quando existe, pelo `hook.said` do Buzzfy.

| # | Dia e hora | Formato | Peça | Bruno | Gancho | CTA | Alcance | Views | x | Pulo | Assist. | C/C/C/S | VP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | qua 21/10 21h00 | reel | Dentista A | fala | público + número | pergunta aberta | 169 | 267 | 4,51 | 46,6% | 13,0 s | 10/0/0/0 | sem dado |
| 2 | ter 20/10 21h30 | estático | Fundo de funil | texto | consultoria | FUNIL | 19 | 40 | 0,39 | | | 0/0/0/0 | 0 |
| 3 | ter 20/10 18h30 | reel | Marqueteiro | sint. | consultoria | ESTRATEGISTA | 13 | 21 | 0,35 | 92,9% | 3,8 s | 0/0/0/0 | sem dado |
| 4 | ter 20/10 12h00 | estático | Carrinho cheio | texto | consultoria | CAIXA | 33 | 61 | 0,67 | | | 0/0/0/0 | 0 |
| 5 | seg 19/10 21h30 | reel | Fundo de funil | sint. | consultoria | FUNIL | 14 | 31 | 0,37 | 85,7% | 10,7 s | 0/0/0/0 | sem dado |
| 6 | seg 19/10 18h30 | reel | Carrinho cheio | sint. | consultoria | CAIXA | 40 | 61 | 1,07 | 82,2% | 3,6 s | 0/0/0/0 | sem dado |
| 7 | seg 19/10 12h00 | estático | Marqueteiro | texto | consultoria | ESTRATEGISTA | 35 | 58 | 0,71 | | | 0/0/0/0 | 0 |
| 8 | dom 18/10 21h30 | estático | Escala 7x7 | texto | número | ETAPAS | 35 | 61 | 0,71 | | | 0/0/0/0 | 0 |
| 9 | dom 18/10 18h47 | reel | Escala 7x7 | sint. | número | ETAPAS | 16 | 32 | 0,43 | 78,9% | 5,4 s | 0/0/0/0 | sem dado |
| 10 | qua 14/10 11h00 | reel | Perpétuo (v08) | sint. | consultoria | PERPÉTUO | 33 | 38 | 0,88 | 89,7% | 5,0 s | 0/0/0/0 | sem dado |
| 11 | ter 13/10 20h00 | reel | Recuperação (v07) | sint. | consultoria | RECUPERAÇÃO | 27 | 34 | 0,72 | 85,2% | 3,4 s | 0/0/0/0 | sem dado |
| 12 | ter 13/10 18h00 | reel | Carrinho (v06) | sint. | consultoria | CARRINHO | 25 | 33 | 0,67 | 69,6% | 48,2 s* | 0/0/0/0 | sem dado |
| 13 | ter 13/10 11h00 | reel | Evento (v05) | sint. | consultoria | EVENTO | 34 | 46 | 0,91 | 69,4% | 4,9 s | 0/0/0/0 | sem dado |
| 14 | seg 12/10 20h00 | reel | Aquecimento (v04) | sint. | consultoria | AQUECIMENTO | 35 | 53 | 0,93 | 72,2% | 5,5 s | 2/0/0/0 | sem dado |
| 15 | seg 12/10 18h00 | reel | Captação (v03) | sint. | consultoria | CAPTAÇÃO | 32 | 42 | 0,85 | 83,9% | 8,5 s | 0/0/0/0 | sem dado |
| 16 | seg 12/10 11h00 | reel | Oferta (v02) | sint. | consultoria | OFERTA | 34 | 52 | 0,91 | 83,8% | 5,4 s | 0/0/0/0 | sem dado |
| 17 | seg 12/10 06h00 | carrossel | 10 perguntas | texto | número | CHECKLIST | 34 | 75 | 0,69 | | | 0/2/0/0 | 0 |
| 18 | dom 11/10 18h29 | reel | Você gravou o curso inteiro (v01) | sint. | consultoria | PESQUISA | 169 | 214 | 4,51 | 86,9% | 5,0 s | 0/0/0/0 | sem dado |
| 19 | sex 09/10 12h00 | carrossel | Saga 7: nunca escreveu um livro | foto | personagem | TABULEIRO (sem automação) | 71 | 194 | 1,45 | | | 1/0/0/0 | 4 |
| 20 | qui 08/10 13h00 | carrossel | Saga 6: alimentou 5 mil | foto | personagem | salvar | 98 | 245 | 2,00 | | | 4/0/0/0 | 1 |
| 21 | qua 07/10 19h00 | estático | Saga 5: o maior evento | foto | personagem | enviar | 111 | 205 | 2,27 | | | 6/1/0/0 | 1 |
| 22 | ter 06/10 11h00 | carrossel | Saga 4: semeador | foto | personagem | salvar e enviar | 63 | 203 | 1,29 | | | 4/0/0/0 | 1 |
| 23 | seg 05/10 21h58 | reel | Problema de equipe | fala | público | marcar | 128 | 206 | 3,41 | 49,6% | 17,2 s | 14/0/0/0 | sem dado |
| 24 | seg 05/10 12h00 | carrossel | Saga 3: pescadores | foto | personagem | marcar | 126 | 287 | 2,57 | | | 5/0/0/0 | 3 |
| 25 | dom 04/10 22h30 | reel | O que você recusa | s/ rosto | consultoria | responder 1, 2 ou 3 | 58 | 75 | 1,55 | 67,2% | 6,2 s | 0/0/0/0 | sem dado |
| 26 | dom 04/10 17h00 | carrossel | Saga 2: 3 atalhos | foto | personagem | responder 1, 2 ou 3 | 189 | 362 | 3,86 | | | 2/0/1/0 | 2 |
| 27 | dom 04/10 11h11 | reel | 90% dos lançamentos que flopam | fala | número | pergunta aberta | 166 | 252 | 4,43 | 45,7% | 12,6 s | 13/2/0/0 | sem dado |
| 28 | sáb 03/10 23h40 | carrossel | Saga 1: 30 anos | figura sem rosto visível | personagem | salvar (legenda cortada) | 52 | 148 | 1,06 | | | 1/0/0/0 | 1 |
| 29 | sáb 03/10 23h06 | reel | Ele nunca fez um anúncio | fala | personagem | salvar e acompanhar | 308 | 578 | 8,21 | 53,2% | 18,7 s | 30/3/0/2 | sem dado |
| 30 | sex 02/10 09h50 | estático | Bastidor: café e uma pergunta | foto | bastidor | pergunta aberta | 197 | 400 | 4,02 | | | 6/1/0/0 | 11 |
| 31 | qui 01/10 15h05 | reel | Cem mil seguidores | s/ rosto | número | número da casa | 54 | 80 | 1,44 | 44,6% | 8,9 s | 1/0/0/0 | sem dado |
| 32 | qua 30/09 11h34 | carrossel | 100 mil seguidores, 14 vendas | texto | número | sem dado (legenda cortada) | 134 | 273 | 2,73 | | | 1/0/0/0 | 1 |
| 33 | qua 30/09 08h06 | reel | Médico com agenda lotada | s/ rosto | público | AGENDA (sem automação) | 64 | 102 | 1,71 | 55,4% | 9,4 s | 3/1/0/0 | sem dado |
| 34 | qua 30/09 07h55 | estático | Prazer, eu sou o Bruno (mineiro) | foto | apresentação | sem dado (legenda cortada) | 237 | 504 | 4,84 | | | 19/2/0/0 | 19 (1 seguidor) |
| 35 | qua 30/09 07h44 | estático | Prazer, eu não ensino a lançar | foto | apresentação | sem dado (legenda cortada) | 133 | 255 | 2,71 | | | 10/0/0/0 | 4 |

\* Carrinho (v06): 48,2 s de tempo médio num vídeo de cerca de 37 s de narração [FATO, ig_post_stats; duração pelo `videos/v06/timeline.json`]. Mais que o vídeo inteiro com 25 de alcance: alguém deixou em repetição. Anomalia, fora da leitura de retenção.

Fora da fase, mas dentro da mediana do Buzzfy: reel de 01/01/2025 (fora da grade do perfil, retrospectiva pessoal de fé): 213 de alcance, 521 views, 9,14x, pulo 49,8%, 5,1 s, 8 curtidas [FATO, ig_post_stats].

Story ativo (único no ar às 13h30): vídeo de 6 s postado às 09h33, cena de academia, sem o Bruno no quadro da capa, fora do PostZen. Provisório: alcance 20, views 25, 14 toques para avançar, 5 deslizes para a próxima conta, 3 saídas, 0 resposta [FATO, ig_post_stats e ig_posts; duração pelo metadado do arquivo]. Os 8 stories e o reel Dentista B agendados para hoje começam às 14h e não tinham saído na hora da leitura [FATO, PostZen listPosts published: nada em 24/10].

---

## 4. Comparações

Medianas calculadas sobre a tabela da seção 3 [FATO, conta deste relatório]. Amostras pequenas: servem como indício, não como regra.

### 4.1 Por formato

| Formato | n | Alcance mediano | Views medianas | Curtidas | Coment. | Comp. | Salv. |
|---|---|---|---|---|---|---|---|
| Reel | 19 | 35 | 53 | 73 | 6 | 0 | 2 |
| Carrossel | 8 | 84,5 | 224 | 18 | 2 | 1 | 0 |
| Estático com foto do Bruno | 4 | 165 | 327,5 | 41 | 4 | 0 | 0 |
| Estático de texto (série 2) | 4 | 34 | 59,5 | 0 | 0 | 0 | 0 |

- Os 2 estáticos "Prazer, eu sou o Bruno" e o bastidor somam 34 visitas ao perfil e o único seguidor atribuído a um post da fase (1, no post de 07h55) [FATO, ig_post_stats].
- Na conta inteira, em 30 dias, o story é o maior bloco de views orgânicas: 4.224 de 10.450 (40%) [FATO, ig_account_stats; ESTIMATIVA para o percentual, pela divisão].
- O formato sozinho não explica: o reel tem a pior mediana porque 12 dos 19 reels são sintéticos. Reel com o Bruno é o formato com o maior alcance da fase (seção 4.2).

### 4.2 Por presença do Bruno

| Grupo | n | Alcance mediano | Views | Pulo mediano | Assistido mediano | Curtidas | Coment. | Salv. |
|---|---|---|---|---|---|---|---|---|
| Reel, Bruno falando | 4 | 167,5 (128 a 308) | 259,5 | 48,1% | 15,1 s | 67 | 5 | 2 |
| Reel, animação com voz sintética | 12 | 32,5 (13 a 169) | 40 | 83,8% | 5,2 s | 2 | 0 | 0 |
| Reel sintético sem o "Você gravou o curso inteiro" | 11 | 32 (13 a 40) | 38 | 83,8% | 5,4 s | 2 | 0 | 0 |
| Reel slideshow sem rosto (Recusa, Cem mil, Médico) | 3 | 58 | 80 | 55,4% | 8,9 s | 4 | 1 | 0 |
| Feed com foto do Bruno na capa | 9 | 126 (63 a 237) | 255 | | | 57 | 4 | 0 |
| Feed de texto ou sem rosto | 7 | 35 (19 a 134) | 61 | | | 2 | 2 | 0 |

- Fração do vídeo assistida em média [ESTIMATIVA: tempo médio do Buzzfy dividido pela duração do arquivo ou da narração no repositório; para os reels sem arquivo, duração pela tag `length_s` do Buzzfy]: Dentista A 36% (13 s de 36,4 s); Equipe 23% (17,2 de 74,7); Ele nunca fez um anúncio 25% (18,7 de 74,6); 90% 18% (12,6 de 69,5). Sintéticos: de 9% (Recuperação, 3,4 de 36,4) a 22% (Captação, 8,5 de 38,2), com o Funil fora da faixa (48%, 10,7 de 22,5) e o Carrinho anômalo.
- Os 4 reels com o Bruno abrem falando direto com quem assiste [FATO, Buzzfy `hook.said` e `words.json`]: "Deixa eu te contar uma coisa. Jesus foi o maior de todos. Sabe por quê?" (Ele nunca fez um anúncio); "Ei, vem cá, escuta essa: 90% dos lançamentos que floparam já estão mortos antes do..." (90%); "Essa é para você, expert, que gosta de fazer tudo sozinho e entrega pela metade" (Equipe); "Dentistas, são mais de 474 mil colegas ativos no Brasil. Por que você ainda só vende hora de cadeira?" (Dentista A).
- Mesmo os melhores ficam acima de 45% de pulo. Pela tabela do playbook do Buzzfy, de 45% a 55% a chance de estouro é de 3% a 4%; de 40% a 45%, 7%; de 35% a 40%, 12%; abaixo de 30%, 32% ou mais [FATO, buzzfy_playbook openings]. O normal da conta (70,9%) está 13,9 pontos pior que o reel típico do playbook (57%) [FATO, ig_reel_checkup].
- Confusão de período: 3 dos 4 reels com o Bruno saíram de 03/10 a 05/10, na semana da saga, e todos os sintéticos de 11/10 a 20/10. O Dentista A (21/10) veio logo depois da pior semana (mediana 26 de alcance) e fez 169 [FATO]. É a melhor evidência de que o efeito é do formato e não do período, com n=1 [HIPÓTESE].

### 4.3 Por tipo de gancho

| Gancho | n | Alcance mediano | Faixa | Pulo mediano (reels) |
|---|---|---|---|---|
| Personagem ou contraste (saga bíblica) | 8 | 104,5 | 52 a 308 | 53,2% (1 reel) |
| Apresentação ("Prazer, eu sou o Bruno") | 2 | 185 | 133 a 237 | |
| Bastidor | 1 | 197 | | |
| Chamada de público (dentista, médico, expert) | 3 | 128 | 64 a 169 | 49,6% |
| Número específico | 6 | 44,5 | 16 a 166 | 45,7% |
| Frase de consultoria em 2ª pessoa, sem personagem nem número | 15 | 33 | 13 a 169 | 83,8% |

- Dentro de cada gancho, a presença do Bruno decide [FATO, tabela da seção 3]: número com o Bruno, 166 (90%); número sem rosto, 54 (Cem mil) e 16 (Escala). Chamada de público com o Bruno, 169 e 128; sem rosto, 64 (Médico).
- O gancho de consultoria aparece em 15 peças, todas sem o Bruno em cena, e por isso não dá para separar o efeito do gancho do efeito do formato [FATO]. A leitura do 00-SISTEMA (Módulo 1, item 7: o hook precisa de personagem, número ou contradição) continua compatível com os dados, sem prova isolada [HIPÓTESE].
- A saga de 7 dias caiu em alcance depois da etapa 2: 52, 189, 126, 63, 111, 98, 71 (etapas 1 a 7) [FATO, ig_post_stats].

### 4.4 Por CTA (Buzzfy mais PostZen)

| CTA | n | Alcance mediano | Comentários | Resultado medido |
|---|---|---|---|---|
| Palavra-chave | 19 | 34 | 3 (2 no Checklist, 1 no Médico) | 1 disparo de automação no total |
| Pergunta aberta ou responder número | 6 | 167,5 | 3 (90%: 2; bastidor: 1) | |
| Salvar | 4 | 80,5 | 3 | 2 salvamentos, os dois no "Ele nunca fez um anúncio" |
| Marcar alguém | 2 | 127 | 0 | |
| Enviar | 1 | 111 | 1 | 0 compartilhamento |

- [FATO, PostZen listCommentAutomations, 13h3x] 17 automações ativas na conta (TABULEIRO, ETAPAS de story, CASE, ESTRATEGISTA, ETAPAS série 2, FUNIL, CAIXA, ETAPAS Escala, RECUPERAÇÃO, PERPÉTUO, CARRINHO, EVENTO, PESQUISA, AQUECIMENTO, CAPTAÇÃO, OFERTA, CHECKLIST). 16 com 0 disparo. CHECKLIST: 1 disparado, 1 enviado.
- [FATO, listCommentAutomationLogs] O único disparo veio de um comentário "Checklist" no carrossel de 12/10, de um perfil cujo nome de usuário começa com "bruno". Se for teste do próprio Bruno, os leads reais por automação no período são zero [HIPÓTESE a confirmar com o Bruno].
- [FATO] A TABULEIRO está ligada só ao post do Dentista B (agendado para hoje 21h) e tem 0 log. O carrossel de 09/10 pediu TABULEIRO sem automação e o reel do Médico pediu AGENDA sem automação: o comentário iria para lugar nenhum.
- O CTA de palavra-chave está quase todo em peça sintética ou de texto; o efeito do CTA não se separa do formato [FATO]. O que dá para afirmar: com mediana de 34 de alcance, 19 pedidos de comentário renderam 3 comentários [FATO].
- Compartilhamento: 1 em 35 peças (Saga 2) [FATO, ig_post_stats]; a conta registra 9 em 30 dias [FATO, ig_account_stats]. Os outros 8 vieram de story, de anúncio ou de post fora da janela: sem dado.

### 4.5 Por hora e dia

| Faixa (hora de São Paulo) | Reels | Alcance mediano dos reels | Composição |
|---|---|---|---|
| 06h a 11h | 5 | 34 | 3 sintéticos (33, 34, 34), 90% com o Bruno (166), Médico sem rosto (64) |
| 12h a 17h | 1 | 54 | Cem mil, sem rosto |
| 18h a 20h | 8 | 29,5 | 8 sintéticos, nenhum com o Bruno |
| 21h a 23h | 5 | 128 | 3 com o Bruno (169, 128, 308), Recusa (58), Funil sintético (14) |

- Hora e formato estão confundidos: nenhum reel com o Bruno foi postado entre 18h e 20h, e só 1 sintético saiu depois das 21h [FATO]. A média de 21h (73 em 5 posts) e a de 18h (49 em 6) medem o formato, não a hora [FATO para a composição; HIPÓTESE para a leitura].
- Os "melhores horários" do Buzzfy são puxados por um post cada: 23h (média 180) = Ele nunca fez um anúncio (308) mais a Saga 1 (52); 07h (185) = os dois "Prazer" (237 e 133); sábado (180) = os mesmos dois de 23h [FATO, ig_best_times + tabela].
- Seguidores online quase planos das 11h às 22h: de 386 (11h) a 430 (18h), diferença de 11% [FATO, ig_best_times; ESTIMATIVA para o percentual]. A hora é alavanca pequena perto da diferença de 5x entre formatos [HIPÓTESE].

### 4.6 Por ritmo

| Período | Peças | Alcance mediano | Alcance somado | Curtidas | Seguidores novos no período |
|---|---|---|---|---|---|
| Semana da saga, 03 a 09/10 | 11 | 111 | 1.370 | 80 | 13 (03/10 a 09/10) |
| Série 1, 11 a 14/10 (1 a 3 por dia) | 9 | 34 | 423 | 2 | 5 (11/10 a 14/10) |
| Série 2, 18 a 20/10 (3 por dia) | 8 | 26 | 205 | 0 | 0 (18/10 a 21/10) |

[FATO, ig_post_stats e ig_follower_growth; somas e medianas por este relatório]. O volume maior da série 2 deu o menor alcance somado da fase. O formato muda junto, então o efeito do volume sozinho segue sem prova isolada [HIPÓTESE], em linha com o aprendizado do CLAUDE.md ("3 posts por dia não aumentaram seguidores").

---

## 5. O que segura atenção e o que derruba

### Segura
1. **O Bruno falando para a câmera nos primeiros segundos.** 4 de 4 reels acima de 3,4x a mediana de alcance; pulo de 45,7% a 53,2%; 15,1 s assistidos na mediana; 92% das curtidas de reel da fase (67 de 73) [FATO, ig_post_stats].
2. **Abertura falando com quem assiste**, com nome de público, número ou pergunta ("Dentistas, são mais de 474 mil...", "Ei, vem cá, escuta essa: 90%...") [FATO, Buzzfy hook.said e words.json]. Peso isolado da frase: sem dado, porque todas as aberturas desse tipo têm o Bruno em cena.
3. **Foto do Bruno na capa do feed.** 126 contra 35 de alcance mediano; 46 contra 2 visitas ao perfil [FATO].
4. **Personagem e contraste** (saga bíblica): 8 peças, mediana de 104,5; a única peça com salvamento e a única com compartilhamento da fase [FATO].
5. **Apresentação pessoal e bastidor**: os 3 estáticos de maior alcance de feed (237, 197, 133) e 34 das 48 visitas ao perfil vindas do feed [FATO].
6. **Vídeo curto com o Bruno**: o Dentista A (36 s) reteve a maior fração do vídeo entre os reels com o Bruno (36% contra 18% a 25% nos de 70 a 75 s) [ESTIMATIVA, n=1].

### Derruba
1. **Animação com voz sintética.** 12 reels, mediana de 32,5 de alcance, 83,8% de pulo, 2 curtidas e nenhum comentário somados [FATO].
2. **Frase de consultoria sem personagem nem número** como gancho (15 peças, mediana 33) [FATO, com a confusão de formato da seção 4.3].
3. **Estático de cartão de texto** (série 2): 4 peças, mediana 34, zero interação, zero visita [FATO].
4. **Pedido de palavra-chave em peça de baixo alcance**: 19 pedidos, 3 comentários, 1 disparo (provável teste) [FATO; HIPÓTESE para o teste].
5. **Três posts por dia**: série 2 com o menor alcance somado da fase e 8 dias seguidos sem seguidor novo de 14/10 a 21/10 [FATO]; causalidade do volume: [HIPÓTESE].
6. **Capa de reel que vende**: 11 dos 12 reels sintéticos aparecem na grade com o cartão final "Comenta PALAVRA" como capa (Funil, Caixa, Escala/ETAPAS, Perpétuo, Recuperação, Carrinho, Evento, Aquecimento, Captação, Oferta, Pesquisa) [FATO, conferência visual das capas]. O vídeo começa na fala (ex.: Funil abre em 0,2 s com "Fundo de funil não se compra" [FATO, `videos/serie2/r3-funil/timeline.json`]), então a capa só afeta quem chega pela grade ou pela aba de reels. O playbook do Buzzfy aponta a abertura que vende como o sinal mais forte de gancho fraco [FATO, buzzfy_playbook openings]. Efeito da capa nesta conta: [HIPÓTESE].

---

## 6. Seguidores e caminho até o lead

- [FATO, ig_follower_growth] 30 dias: 53 entradas, 13 saídas, líquido +40. Até 11/10: 52 entradas. De 12/10 a 21/10: 1 entrada, 6 saídas, líquido -5. De 14/10 a 21/10: 0 entrada. 22 e 23/10 pendentes (incluem o Dentista A).
- [FATO] O pico de 19 entradas em 29/09 cai no dia de relatório que vai de 29/09 07h UTC a 30/09 07h UTC (o Buzzfy diz que o dia termina às 07h UTC), antes do primeiro post da fase (30/09 10h44 UTC). Causa: sem dado. Anúncio ou mudança de perfil: [HIPÓTESE].
- [FATO, ig_account_stats] 447 visitas ao perfil, 7 cliques no site (1,6%), 0 toque em botão de link. [ESTIMATIVA] 53 seguidores sobre 447 visitas = 11,9%, como teto, porque seguidor também vem de fora do perfil.
- [FATO] Alcance de seguidores: 419 de 1.618 (26%) em 30 dias. Não seguidores: 2.792. Do total, 1.907 vieram de anúncio.
- [FATO, ig_post_stats] Os números por post são só orgânicos ("Counts are organic only"). A comparação da seção 4 não tem anúncio dentro.
- [FATO, PostZen] 1 disparo de automação no mês (seção 4.4). Diagnósticos marcados e vendas: sem dado nesta frente (contexto: 0 venda).

---

## 7. Achados que os documentos ainda não tinham

1. **Capa CTA nos reels sintéticos** (seção 5, item 6). Antes de publicar reel, conferir a capa escolhida no PostZen.
2. **Hora confundida com formato** (seção 4.5). Nenhum dado desta conta separa o efeito da hora.
3. **O único disparo de automação pode ser teste** (seção 4.4). Conferir com o Bruno.
4. **8 dias fechados sem seguidor novo** (14 a 21/10).
5. **"Você gravou o curso inteiro" é um ponto fora da curva sem retenção**: 169 de alcance com 86,9% de pulo, 5 s assistidos e zero interação [FATO]. Foi o 11º post depois do estouro de 03/10 e o primeiro depois de um dia inteiro sem post (10/10); o protocolo do Buzzfy diz que o empurrão de um estouro some em cerca de 10 posts [FATO, ig_reel_checkup hot_streak.protocol; contagem pela tabela da seção 3]. Leitura de que o alcance veio do resto desse embalo ou da pausa, e não do vídeo: [HIPÓTESE].
6. **2 dos 5 "candidatos a refazer" são fracos**: o reel de 01/01/2025 é retrospectiva pessoal de fé, fora da grade e fora do nicho, com 5,1 s assistidos [FATO]; o "Você gravou o curso inteiro" tem 86,9% de pulo e nenhuma interação [FATO]. A lista do Buzzfy é mecânica (múltiplo de views) [FATO, ig_reel_checkup "why"]. Os 3 fortes para refazer têm o Bruno em cena: Ele nunca fez um anúncio, 90% e Dentista A.
7. **O melhor reel não tinha legenda queimada**: "Ele nunca fez um anúncio" tem `burned_subtitles=false`; Equipe e 90% têm `true` [FATO, Buzzfy tags]. O playbook mede legenda queimada como a maior mudança isolada (4,6x a mediana) [FATO, ig_reel_checkup for_you_to_check]. Refazer esse reel com legenda é mudar uma coisa só [HIPÓTESE a testar].
8. **Hashtags demais em 2 reels**: Dentista A com 8 e Cem mil com 7; o Buzzfy marca 6 ou mais como passo 5 de correção [FATO, ig_reel_checkup flags].
9. **Seguindo subiu de 3.523 para 3.528** desde 21/10 e a bio segue a antiga [FATO]. As correções 1 e 3 do Módulo 1 não começaram.

---

## 8. Hipóteses para o conselho testar (uma coisa por vez)

| # | Hipótese | Teste | Métrica e régua | Onde ler |
|---|---|---|---|---|
| H1 | Reel com o Bruno em cena mantém mediana de alcance acima de 100 em qualquer horário | Pôr 1 reel com o Bruno às 18h30 (horário onde só houve sintético) | Alcance em 48 h; acima de 100 confirma | ig_post_stats |
| H2 | Abertura de até 8 palavras com número ou nome de público baixa o pulo para menos de 45% | Mesmo roteiro com 2 aberturas em semanas diferentes | Pulo em 48 h contra 48,1% (mediana dos 4 com o Bruno) | ig_reel_checkup |
| H3 | Capa com o rosto do Bruno aumenta visitas ao perfil vindas da grade | Capas com rosto nos próximos reels | Visitas ao perfil por semana contra 447 em 30 dias | ig_account_stats |
| H4 | Remake do "Ele nunca fez um anúncio" com legenda queimada, mudando só isso | Repostar a mesma fala com legenda | Views contra 578 e pulo contra 53,2% | ig_post_stats |
| H5 | Pergunta aberta rende mais comentário que palavra-chave com o mesmo alcance | Alternar CTA em reels com o Bruno de alcance parecido | Comentários por 100 de alcance | ig_post_stats, listCommentAutomationLogs |
| H6 | O Dentista A gerou seguidores em 22 e 23/10 | Ler de novo na segunda | Entradas de 22 e 23/10 | ig_follower_growth |

---

## 9. Lacunas

1. Tags de vídeo do Buzzfy só existem para 7 dos 20 reels; gancho falado do Dentista A veio do `words.json`, e o dos sintéticos, dos `timeline.json`. Gancho escrito na tela dos sintéticos: sem dado.
2. Se a voz dos reels "O que você recusa" e "Cem mil seguidores" é a do Bruno: sem dado (o Buzzfy marca "voz própria", sem rosto).
3. Formato visual dos posts de 30/09 a 09/10 fora das capas: sem dado (o repositório começa em 11/10).
4. Curva de retenção por segundo: o Buzzfy entrega pulo e tempo médio, não o ponto de queda. Onde o espectador sai depois dos 3 s: sem dado.
5. Visitas ao perfil e seguidores por reel: o Buzzfy não traz para reel. Seguidor por peça: sem dado (só o 1 do post de 07h55).
6. Stories que já expiraram: métrica por story perdida (o Buzzfy só lê nas 24 h). Só o story de 09h33 de hoje foi lido. Os 8 de hoje precisam ser lidos antes de expirarem (até dom 25/10, 14h a 20h30).
7. Origem de 8 dos 9 compartilhamentos de 30 dias: sem dado.
8. Causa do pico de 19 seguidores em 29/09: sem dado. Calendário e alvo dos anúncios ficam com a frente de anúncios.
9. CTA dos posts "Prazer" e do carrossel "100 mil": a leitura do Buzzfy corta a legenda em 500 caracteres. Sem dado.
10. Autor do único disparo de automação: confirmar com o Bruno.
11. Seguidores de 22 e 23/10 pendentes no Instagram.
12. Todas as comparações têm n pequeno (4 reels com o Bruno, 1 reel por gancho em alguns grupos) e período confundido com formato.

---

## 10. Fontes

- Buzzfy, leituras de 24/10/2026, 13h28 a 13h40: `ig_posts` (3 chamadas), `ig_post_stats` (2), `ig_reel_checkup` (2), `ig_account_stats`, `ig_follower_growth`, `ig_best_times`, `ig_audience`, `buzzfy_playbook` (openings, small_accounts).
- PostZen, 24/10/2026, 13h3x: `listCommentAutomations` e `listPosts` (accountId j97772ycndetk3f1wcdbh14p898g4b8w), `listCommentAutomationLogs` (CHECKLIST qs7de23c7nzxzw2k4yjshgm5gd8g5dmx; TABULEIRO qs747t4bq23a1qpnjskexg34vs8gx7hx).
- Links das peças: https://www.instagram.com/reel/DexpShwiCJ0/ (Dentista A), https://www.instagram.com/reel/DeDhWnuoTLT/ (Ele nunca fez um anúncio), https://www.instagram.com/reel/DeE0ZL5ERFq/ (90%), https://www.instagram.com/reel/DeIjIM5ovUo/ (Equipe), https://www.instagram.com/reel/DeXoA6LxW6D/ (Você gravou o curso inteiro), https://www.instagram.com/p/Dd6K1ehEY1H/ (Prazer, mineiro), https://www.instagram.com/p/Dd_hjF6EQs_/ (bastidor).
- Repositório: `conteudo/modo-god-cronograma/contexto.md`, `conteudo/sistema-instagram/00-SISTEMA.md`, `CLAUDE.md`, `videos/v01` a `videos/v08`, `videos/serie2/roteiros.json` e `timeline.json`, `videos/nichos/dentista/words.json` e `render/`, `videos/nichos/dentista/god/run/02-cadeiras/evidencias-E/buzzfy-leitura-2026-10-21.md`.
