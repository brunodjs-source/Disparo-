# F1 · Auditoria da conta @o_estrategista.com.br · rodada de 24/10/2026

Frente F1 da pesquisa do conselho Agência Reunida. Leituras ao vivo, somente leitura, feitas entre 14h48 e 14h54 de sábado 24/10/2026 (horário de São Paulo), depois do fato novo das 14h40 (a entrevista à TV Câmara Campinas vai ao ar na segunda-feira, 02/11/2026). Nada foi publicado, agendado ou alterado no Instagram, no Buzzfy ou no PostZen.

Esta versão substitui a das 13h42 (leituras de 13h28 a 13h40). A anterior está no histórico do git (commit 88433c7). A seção 3 lista o que mudou entre as duas leituras.

Etiquetas: [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha uma objeção sozinho. Métrica que falta: "sem dado".

---

## 0. Consultas feitas

Todas responderam. Nenhum erro de consulta.

| # | Consulta | Parâmetros | Resultado |
|---|---|---|---|
| 1 | Buzzfy `ig_posts` | kind=all, since=2026-09-29, limit=40 | 35 itens (30/09 a 22/10 UTC), next_cursor vazio |
| 2 | Buzzfy `ig_posts` | kind=stories | 3 stories ativos (09h33, 14h00, 14h03) |
| 3 | Buzzfy `ig_posts` | kind=all e stories, include_media_urls | 35 capas e 3 capas de story. A saída de 72 mil caracteres foi salva em arquivo pelo próprio ambiente e lida inteira por script (35 de 35 itens). Capas baixadas numa pasta temporária, montadas em 2 folhas e conferidas a olho |
| 4 | Buzzfy `ig_post_stats` | 20 ids + 18 ids (35 posts e 3 stories) | 38 itens, status ok |
| 5 | Buzzfy `ig_reel_checkup` | limit=20 | 20 reels, normal da conta, hot streak, candidatos a refazer; tags de vídeo só para 7 |
| 6 | Buzzfy `ig_account_stats` | 30 dias (24/09 17h48 UTC a 24/10 17h48 UTC) | ok |
| 7 | Buzzfy `ig_follower_growth` | 30 dias | ok; 22 e 23/10 pendentes |
| 8 | Buzzfy `ig_best_times` | America/Sao_Paulo, 25, 30 e 35 posts | ok nas 3 |
| 9 | Buzzfy `ig_audience` | this_month | ok |
| 10 | Buzzfy `buzzfy_playbook` | openings | ok |
| 11 | PostZen `listPosts` | accountId j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 a 23/11 | 20 itens: 2 publicados hoje, 18 agendados |
| 12 | PostZen `listPosts` | mesma conta, status=published | 22 itens (12/10 a 24/10) |
| 13 | PostZen `listCommentAutomations` | mesma conta | 17 automações, todas ativas |
| 14 | PostZen `listCommentAutomationLogs` | CHECKLIST, TABULEIRO, ETAPAS de story | 1, 0 e 0 logs |

Repositório conferido nesta rodada: `videos/v01` a `videos/v08` (cada pasta tem `tts.py` com a voz `AntonioNeural`; git log de 11/10: "Vídeo 01 (Pesquisa) com narração Microsoft neural Antonio"), `videos/serie2/roteiros.json` (vozes `pf_dora` e `pm_alex`) e `videos/serie2/*/timeline.json`, `videos/nichos/dentista/words.json` e `render/`, `conteudo/sistema-instagram/00-SISTEMA.md`, `CLAUDE.md`. Durações dos vídeos lidas com ffprobe nos arquivos do repositório.

---

## 1. Resumo

1. [FATO, ig_post_stats] Nos 30 últimos posts (02/10 a 21/10) há 17 reels. Os 4 com o Bruno falando para a câmera têm mediana de 167,5 de alcance, 259,5 views, 48,1% de pulo e 15,1 s assistidos. Os 12 de animação com voz sintética têm 32,5 de alcance, 40 views, 83,9% de pulo e 5,0 s. Diferença: 5,2x no alcance, 6,5x nas views, 35,8 pontos a menos de pulo.
2. [FATO, ig_post_stats] Os 4 reels com o Bruno somam 67 das 69 curtidas de reel, os 5 comentários de reel e os 2 únicos salvamentos dos 30 posts. Os 12 sintéticos somam 2 curtidas, nenhum comentário, nenhum salvamento.
3. [FATO, ig_post_stats + conferência visual das capas] No feed, as 7 peças com foto do Bruno na capa têm mediana de 111 de alcance e 23 visitas ao perfil somadas; as 6 de texto têm 34,5 e 1 visita.
4. [FATO, timeline.json + words.json + ig_post_stats] A frase de abertura dos sintéticos é curta e direta ("Seu carrinho cheio pode virar zero no caixa.", 8 palavras, aos 0,2 s) e mesmo assim os 12 perderam de 69% a 90% no começo (mediana 83,9%). Os reels com o Bruno abrem com preâmbulo ("Deixa eu te contar uma coisa.", "Ei, vem cá, escuta essa:") e seguraram mais. O que separa os grupos é rosto e voz, com a frase em segundo plano [HIPÓTESE com forte apoio nos dados, n=4 contra 12].
5. [FATO, ig_reel_checkup + tabela da seção 4] O horário não tem leitura própria: os 8 reels postados entre 18h e 20h59 são todos sintéticos, e 3 dos 4 reels com o Bruno saíram entre 21h e 23h06. O "melhor horário" do Buzzfy muda com o tamanho da amostra: 23h com 30 posts, 21h com 25, 07h com 35.
6. [FATO, PostZen] 17 automações de palavra-chave ativas e 1 disparo no total (CHECKLIST, carrossel de 12/10, de um perfil cujo nome começa com "bruno"). As 18 peças dos 30 com pedido de palavra-chave somam 2 comentários.
7. [FATO, ig_follower_growth] Último dia com seguidor novo: 13/10. De 14/10 a 21/10, 8 dias fechados seguidos com zero entrada. 22 e 23/10 (o Dentista A) seguem pendentes no Instagram.
8. [FATO, ig_post_stats, 0,8 h de vida] Os 2 stories de bastidor da TV que saíram às 14h00 e 14h03 têm o Bruno em cena e alcance provisório de 8 e 7. O story de 09h33 (academia, sem o Bruno visível) tem 26 em 5,3 h.
9. [FATO, PostZen listPosts] Depois do TL02 (sáb 31/10), não há nada agendado no feed até o TL03 (sáb 07/11). A semana da exibição (02/11 a 06/11) está vazia no PostZen.
10. Contexto conferido: quase tudo bate. Derrubados: as saídas de seguidor de 12/10 a 21/10 (6 no Buzzfy, 7 no contexto); o teto de pulo da série 2 (86,7% hoje, 93% no contexto, porque o Instagram revisou o Marqueteiro); o status de tl02 a tl05 (já agendados no PostZen). O CLAUDE.md e o 00-SISTEMA têm faixas desatualizadas (seção 2).

---

## 2. Confere o contexto, número a número

Contexto coletado às 12h40. Leitura desta frente: 14h48 a 14h54.

| Item do contexto.md | Valor no contexto | Leitura de hoje | Veredito |
|---|---|---|---|
| Seguidores, seguindo, posts | 1.618, 3.528, 57 | 1.618, 3.528, 57 [ig_account_stats] | Confirmado |
| Bio e link | "Estrategista Digital / Ide e pregai o evangelho! / Visitor Host @bnisyrius / Dev @dashpronow"; /v2/ | Mesmo texto, com emojis antes de cada linha; https://estrategistadelancamento.com.br/v2/ [ig_account_stats] | Confirmado. A bio proposta no Módulo 2 ainda não foi aplicada |
| Alcance 30 dias | 3.216; 1.907 de anúncio; orgânico perto de 1.300 | 3.216; 1.907 de anúncio; 2.792 não seguidores; 419 seguidores [ig_account_stats] | Confirmado. "Orgânico perto de 1.300" é [ESTIMATIVA] (3.216 menos 1.907 = 1.309): o Buzzfy avisa que as partes do alcance se sobrepõem e não somam |
| Views 30 dias | 12.652 (10.445 orgânicas) | 12.685 (10.478 orgânicas; 2.207 de anúncio, 17%) [ig_account_stats] | Confirmado na ordem de grandeza; +33 desde 12h40, quase tudo em story (+32) |
| Por tipo | story 4.219 views e 756 contas; reel 2.242 e 608; carrossel 1.788 e 340; post 2.154 e 322 | story 4.251 e 756; reel 2.243 e 608; carrossel 1.788 e 340; post 2.154 e 322; IGTV 41 e 34 [ig_account_stats] | Confirmado (story +32, reel +1). IGTV faltava no contexto |
| Engajamento 30 dias | 256 curtidas, 14 comentários, 3 salvamentos, 9 compartilhamentos, 7 respostas, 125 contas | Igual; total de interações 299; 1 repost [ig_account_stats] | Confirmado |
| Visitas e cliques | 447 visitas, 7 cliques no site | 447 e 7; toques no link 0 [ig_account_stats] | Confirmado |
| Seguidores 24/09 a 21/10 | 53 entraram, 13 saíram, líquido +40; pico de 19 em 29/09 | Igual [ig_follower_growth] | Confirmado |
| "quase tudo até 11/10" | sem número | 52 das 53 entradas até 11/10 [ig_follower_growth] | Confirmado |
| 12/10 a 21/10 | 1 entrada e 7 saídas | 1 entrada (13/10) e 6 saídas (13/10: 1; 15/10: 1; 16/10: 2; 17/10: 2) [ig_follower_growth] | **Derrubado em 1.** As 7 saídas só fecham contando 11/10, e aí as entradas viram 5 |
| Normal do reel | 57 views, pulo 70,9% | 57 views, pulo 70,9%, 20 reels (19 da fase atual mais o de 01/01/2025) [ig_reel_checkup] | Confirmado |
| Dentista A | 267 views, 169 alcance, 4,68x, pulo 46,6%, 13 s, 10 curtidas, 0 e 0 | Igual, com 65,8 h de vida, provisional=false [ig_post_stats] | Confirmado. Os números já assentaram |
| Série 2 (18 a 20/10) | 0,37x a 1,07x, pulo 79% a 93% | 0,39x (Marqueteiro) a 1,07x (Caixa); pulo 78,9% a 86,7% [ig_reel_checkup] | **Derrubado no teto.** O Marqueteiro passou de 21 para 22 views e de 92,9% para 86,7% de pulo entre 13h40 e 14h50, com 92 h de vida. O Instagram ainda revisa reel com mais de 48 h |
| Série de 12 a 14/10 | 0,58x a 0,93x, pulo 69% a 90% | 0,58x (Carrinho) a 0,93x (Aquecimento); pulo 69,4% a 89,7% [ig_reel_checkup] | Confirmado |
| Candidatos a refazer | "Ele nunca fez um anúncio" (04/10, 10,14x, 53%); 01/01/2025 (9,14x); Dentista A (4,68x); "04/10 14h" (4,42x); "Você gravou o curso inteiro" (11/10, 3,75x, 87%) | Mesma lista e mesma ordem [ig_reel_checkup remake_candidates] | Confirmado, com 2 ressalvas: as datas e a hora "14h" estão em UTC (em São Paulo, o "Ele nunca fez um anúncio" saiu sáb 03/10 às 23h06 e o "04/10 14h" é o reel "90%", dom 04/10 às 11h11); e 2 dos 5 são fracos para refazer (seção 8) |
| Janela de 48 h do Dentista A | fechada | window_open=false; hits: Dentista A (4,68x) e "Você gravou o curso inteiro" (3,75x) [ig_reel_checkup hot_streak] | Confirmado |
| Seguidores online | pico 18h (430), 19h (424), 17h (417), 21h (416) | Igual, média de 27 dias [ig_best_times] | Confirmado |
| Posts por hora e dia | 23h 180 (2), 21h 73 (5), 11h 66 (5), 18h 49 (6); sáb 180 (2), sex 134 (2), dom 106 (6) | Reproduz exatamente com 30 posts. Com 25: 21h 73 (5), 12h 66 (4), 18h 49 (6); qua 104 (3), dom 70 (4), seg 53 (9). Com 35: 07h 185 (2), 23h 180 (2), 11h 77 (6); sáb 180 (2), sex 134 (2), qua 126 (7) [ig_best_times] | Confirmado com a amostra de 30. O ranking muda com o tamanho da amostra; leitura na seção 5.5 |
| Público | 35-44 39,8%, 45-54 27,6%, 25-34 21,5%; Campinas 33% e 53% dos engajados; homens 59% dos engajados; alcance pende para 25-34 (28,7%) | Igual [ig_audience] | Confirmado. Ressalva do próprio Buzzfy: o alcance inclui anúncio, então o "pende para 25-34" pode refletir a segmentação do anúncio |
| PostZen, agenda de 24 a 30/10 | stories de 14h00 a 20h30, Dentista B 21h, tl01, pb01, car01, pf01, ci01, po01, pb02 | Igual nos horários. Os stories de 14h00 e 14h03 já saíram (platformPostId 18118234495799066 e 17954380989271814, os mesmos ids que o Buzzfy lê) [PostZen listPosts] | Confirmado |
| tl02 a tl05 | "Proposto e ainda não agendado" | Agendados: sáb 31/10, 07/11, 14/11 e 21/11, todos 18h30 [PostZen listPosts] | **Desatualizado.** Já estão no PostZen (o commit 318e97d registra o agendamento) |
| TABULEIRO | automação ativa no Dentista B, botão para /tabuleiro | Ativa, ligada ao post do Dentista B, botão para https://estrategistadelancamento.com.br/tabuleiro/?o=ig-tabuleiro, 0 disparo [PostZen] | Confirmado |
| 1 disparo de automação no mês | 1 | 1 (CHECKLIST, enviado) [PostZen listCommentAutomationLogs] | Confirmado. Ver a ressalva do teste na seção 5.4 |
| Marca do gravador desfocada no story de bastidor | sim | A capa do story de 14h00 mostra um objeto desfocado em primeiro plano, no canto inferior direito [conferência visual] | Confirmado o desfoque; que o objeto é o gravador vem do contexto |

Regras do CLAUDE.md e do 00-SISTEMA conferidas contra a leitura de hoje:

| Regra escrita | Número escrito | Hoje | Veredito |
|---|---|---|---|
| CLAUDE.md: reels com o Bruno falando | 2,4x a 5,8x acima da mediana | Alcance: 3,41x a 8,21x da mediana de 37,5; views: 3,61x a 10,14x da de 57 [ig_post_stats] | A direção se mantém; a faixa subiu porque a mediana caiu de 53 para 37,5 |
| CLAUDE.md: reels de animação com voz sintética | 0,15x a 0,8x, pulo 77% a 92% | Views: 0,39x a 1,07x em 11 reels e 3,75x no "Você gravou o curso inteiro"; pulo 69,4% a 89,7% [ig_reel_checkup] | **Derrubado em parte.** O piso de 0,15x e o teto de 92% sumiram quando os números assentaram; 2 dos 12 passaram de 1x. A regra de pôr o Bruno em cena continua de pé |
| 00-SISTEMA, ficha (linha 20) | Mediana de reel 53 de alcance, 74 views, 6,2 s, 68% de pulo (17 reels) | 37,5 de alcance, 57 views, 5,85 s, 70,9% (20 reels) [ig_post_stats baseline] | Desatualizado |
| 00-SISTEMA, linhas 42 a 44 | Marqueteiro 8 de alcance e 88% de pulo; Funil 13 e 92%; Escala 15 e 77% | Marqueteiro 14 e 86,7%; Funil 14 e 85,7%; Escala 16 e 78,9% [ig_post_stats] | Desatualizado (leitura antes de 48 h) |
| 00-SISTEMA, conclusão (linha 46) | "Os 10 últimos reels feitos em animação com voz sintética ficaram todos abaixo da mediana (de 8 a 39 de alcance)" | São 12 reels sintéticos; alcance de 14 a 40 em 11 deles e 169 no "Você gravou o curso inteiro"; 2 acima de 37,5 (Caixa 40, Pesquisa 169) | **Derrubado em parte** |
| 00-SISTEMA, Módulo 1, item 3 | Seguindo 3.523, deixar de seguir cerca de 3.000 | Seguindo 3.528 [ig_account_stats] | Subiu 5 desde 21/10: a limpeza não começou |

---

## 3. O que mudou entre a leitura das 13h40 e a das 14h50

| Item | 13h40 | 14h50 | Fonte |
|---|---|---|---|
| Reel Marqueteiro (20/10) | 13 de alcance, 21 views, 92,9% de pulo | 14, 22, 86,7% | ig_post_stats |
| Story de 09h33 | 20 de alcance, 25 views, 0 interação | 26, 33, 1 interação | ig_post_stats |
| Views da conta, 30 dias | 12.657 (story 4.224) | 12.685 (story 4.251) | ig_account_stats |
| Stories no ar | 1 | 3 (entraram 14h00 e 14h03) | ig_posts, PostZen |
| tl02 a tl05 no PostZen | não lidos na rodada anterior | agendados para 31/10, 07/11, 14/11 e 21/11, 18h30 | PostZen listPosts |
| Todo o resto (seguidores, Dentista A, demais posts, automações) | | sem mudança | |

---

## 4. A amostra: os 30 últimos posts, mais 5 de contexto e os stories ativos

Linhas 1 a 30: os 30 últimos posts do feed e de reels (02/10 a 21/10). Linhas 31 a 35: os 5 primeiros da fase atual (30/09 e 01/10), usados só como contexto. Hora de São Paulo. "x" é o múltiplo de alcance do Buzzfy: reel contra a mediana de reel (37,5), feed contra a mediana dos 10 últimos posts de feed (49). Pulo e tempo assistido só existem para reel. C/C/C/S = curtidas, comentários, compartilhamentos, salvamentos. VP = visitas ao perfil (o Buzzfy só traz para feed e story).

Coluna "Bruno": **fala** = Bruno falando para a câmera [Buzzfy tags talking_head e selfie_closeup em 3 reels; Dentista A por `words.json`, render e capa]; **sint.** = animação com narração sintética [repositório: `tts.py` com AntonioNeural em v01 a v08; `roteiros.json` com pf_dora e pm_alex na série 2]; **s/ rosto** = slideshow sem pessoa [Buzzfy framing=no_person]; **foto** = foto do Bruno na capa [conferência visual de hoje]; **texto** = cartão de texto (os 4 estáticos da série 2 têm só um avatar pequeno no cabeçalho).

Colunas "Gancho" e "CTA": classificação deste relatório, pela primeira linha da legenda, pela capa e, quando existe, pela fala inicial (`hook.said` do Buzzfy, `words.json` ou `timeline.json`).

| # | Dia e hora | Formato | Peça | Bruno | Gancho | CTA | Alcance | Views | x | Pulo | Assist. | C/C/C/S | VP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | qua 21/10 21h00 | reel | Dentista A | fala | público com número | pergunta aberta | 169 | 267 | 4,51 | 46,6% | 13,0 s | 10/0/0/0 | sem dado |
| 2 | ter 20/10 21h30 | estático | Fundo de funil | texto | consultoria | FUNIL | 19 | 40 | 0,39 | | | 0/0/0/0 | 0 |
| 3 | ter 20/10 18h30 | reel | Marqueteiro | sint. | consultoria | ESTRATEGISTA | 14 | 22 | 0,37 | 86,7% | 3,8 s | 0/0/0/0 | sem dado |
| 4 | ter 20/10 12h00 | estático | Carrinho cheio | texto | consultoria | CAIXA | 33 | 61 | 0,67 | | | 0/0/0/0 | 0 |
| 5 | seg 19/10 21h30 | reel | Fundo de funil | sint. | consultoria | FUNIL | 14 | 31 | 0,37 | 85,7% | 10,7 s | 0/0/0/0 | sem dado |
| 6 | seg 19/10 18h30 | reel | Carrinho cheio (Caixa) | sint. | consultoria | CAIXA | 40 | 61 | 1,07 | 82,2% | 3,6 s | 0/0/0/0 | sem dado |
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
| 18 | dom 11/10 18h29 | reel | Você gravou o curso inteiro (v01) | sint. | consultoria (dor) | PESQUISA | 169 | 214 | 4,51 | 86,9% | 5,0 s | 0/0/0/0 | sem dado |
| 19 | sex 09/10 12h00 | carrossel | Saga 7: nunca escreveu um livro | foto | personagem | TABULEIRO (sem automação) | 71 | 194 | 1,45 | | | 1/0/0/0 | 4 |
| 20 | qui 08/10 13h00 | carrossel | Saga 6: alimentou 5 mil | foto | personagem | salvar | 98 | 245 | 2,00 | | | 4/0/0/0 | 1 |
| 21 | qua 07/10 19h00 | estático | Saga 5: o maior evento | foto | personagem | enviar | 111 | 205 | 2,27 | | | 6/1/0/0 | 1 |
| 22 | ter 06/10 11h00 | carrossel | Saga 4: semeador | foto | personagem | salvar e enviar | 63 | 203 | 1,29 | | | 4/0/0/0 | 1 |
| 23 | seg 05/10 21h58 | reel | Problema de equipe | fala | público | marcar | 128 | 206 | 3,41 | 49,6% | 17,2 s | 14/0/0/0 | sem dado |
| 24 | seg 05/10 12h00 | carrossel | Saga 3: pescadores | foto | personagem | marcar | 126 | 287 | 2,57 | | | 5/0/0/0 | 3 |
| 25 | dom 04/10 22h30 | reel | O que você recusa | s/ rosto | consultoria | responder 1, 2 ou 3 | 58 | 75 | 1,55 | 67,2% | 6,2 s | 0/0/0/0 | sem dado |
| 26 | dom 04/10 17h00 | carrossel | Saga 2: 3 atalhos | foto | personagem | responder 1, 2 ou 3 | 189 | 362 | 3,86 | | | 2/0/1/0 | 2 |
| 27 | dom 04/10 11h11 | reel | 90% dos lançamentos que flopam | fala | número | pergunta aberta | 166 | 252 | 4,43 | 45,7% | 12,6 s | 13/2/0/0 | sem dado |
| 28 | sáb 03/10 23h40 | carrossel | Saga 1: 30 anos | texto (figura sem rosto visível) | personagem | salvar | 52 | 148 | 1,06 | | | 1/0/0/0 | 1 |
| 29 | sáb 03/10 23h06 | reel | Ele nunca fez um anúncio | fala | personagem | salvar e acompanhar | 308 | 578 | 8,21 | 53,2% | 18,7 s | 30/3/0/2 | sem dado |
| 30 | sex 02/10 09h50 | estático | Bastidor: café e uma pergunta | foto | bastidor | pergunta aberta | 197 | 400 | 4,02 | | | 6/1/0/0 | 11 |
| 31 | qui 01/10 15h05 | reel | Cem mil seguidores | s/ rosto | número | número da casa | 54 | 80 | 1,44 | 44,6% | 8,9 s | 1/0/0/0 | sem dado |
| 32 | qua 30/09 11h34 | carrossel | 100 mil seguidores, 14 vendas | texto | número | sem dado (legenda cortada) | 134 | 273 | 2,73 | | | 1/0/0/0 | 1 |
| 33 | qua 30/09 08h06 | reel | Médico com agenda lotada | s/ rosto | público | AGENDA (sem automação) | 64 | 102 | 1,71 | 55,4% | 9,4 s | 3/1/0/0 | sem dado |
| 34 | qua 30/09 07h55 | estático | Prazer, eu sou o Bruno (mineiro) | foto | apresentação | sem dado (legenda cortada) | 237 | 504 | 4,84 | | | 19/2/0/0 | 19 (1 seguidor) |
| 35 | qua 30/09 07h44 | estático | Prazer, eu não ensino a lançar | foto | apresentação | sem dado (legenda cortada) | 133 | 255 | 2,71 | | | 10/0/0/0 | 4 |

\* Carrinho (v06): 48,2 s de tempo médio num vídeo de 36,7 s [FATO, ig_post_stats; duração por ffprobe em `videos/v06/video06-carrinho-final.mp4`]. Mais que o vídeo inteiro, com 25 de alcance: alguém deixou em repetição. Anomalia, fora das medianas de tempo assistido.

Fora da amostra, mas dentro do normal do Buzzfy: reel de 01/01/2025 ("Resumo de 2024...", retrospectiva pessoal de fé, fora da grade do perfil): 213 de alcance, 521 views, 9,14x, pulo 49,8%, 5,1 s, 8 curtidas [FATO, ig_reel_checkup].

### Stories ativos (lidos às 14h50; números provisórios, menos de 48 h)

| Hora | Peça | Bruno | Vida | Alcance | Views | Navegação | Respostas | Fonte da peça |
|---|---|---|---|---|---|---|---|---|
| 09h33 | vídeo de 6 s, academia | não visível na capa | 5,3 h | 26 | 33 | 20 toques para avançar, 6 deslizes para a próxima conta, 3 saídas | 0 (1 interação) | fora do PostZen |
| 14h00 | st01, vídeo de 15 s, bastidor da TV ("TV CÂMARA CAMPINAS · BASTIDOR DA MINHA...") | em cena, sentado, sendo filmado | 0,8 h | 8 | 16 | 6 toques para avançar, 1 para voltar, 2 deslizes | 0 | PostZen |
| 14h03 | estático de bastidor ("Gravei uma entrevista para a TV Câmara Campinas. Em breve, o que eu disse.") | em cena | 0,8 h | 7 | 12 | 7 toques para avançar | 0 | PostZen |

[FATO, ig_post_stats, ig_posts e conferência visual das capas; duração pelo metadado do arquivo no CDN do Instagram]. Os stories de 15h00 em diante ainda não tinham saído na hora da leitura [FATO, PostZen: status scheduled].

---

## 5. Comparações

Medianas calculadas sobre a tabela da seção 4 [FATO, conta deste relatório]. Amostra principal: linhas 1 a 30. Entre parênteses, quando muda, a amostra de 35. Todos os n são pequenos: indício, não regra.

### 5.1 Por formato

| Formato | n | Alcance mediano | Views medianas | Curtidas | Coment. | Comp. | Salv. | VP |
|---|---|---|---|---|---|---|---|---|
| Reel | 17 | 34 | 52 | 69 | 5 | 0 | 2 | sem dado |
| Carrossel | 7 | 71 | 203 | 17 | 2 | 1 | 0 | 12 |
| Estático | 6 | 35 | 61 | 12 | 2 | 0 | 0 | 12 |
| Estático com foto do Bruno | 2 (4) | 154 (165) | 302,5 (327,5) | 12 (41) | 2 (4) | 0 | 0 | 12 (35) |
| Estático de texto (série 2) | 4 | 34 | 59,5 | 0 | 0 | 0 | 0 | 0 |
| Story (conta, 30 dias) | sem contagem de peças | 756 contas no total | 4.251 views, 40,6% das views orgânicas | | | | | |

- [FATO, ig_account_stats; ESTIMATIVA para o percentual, 4.251 dividido por 10.478] O story é o maior bloco de views orgânicas da conta em 30 dias.
- [FATO] O formato sozinho não explica: o reel tem a pior mediana porque 12 dos 17 reels são sintéticos. Reel com o Bruno é o grupo de maior alcance da amostra (seção 5.2).
- [FATO] Os 2 "Prazer, eu sou o Bruno" e o bastidor somam 34 visitas ao perfil e o único seguidor atribuído a um post da fase (1, no post de 07h55 de 30/09).

### 5.2 Por presença do Bruno

| Grupo | n | Alcance mediano | Views | Pulo mediano | Assistido mediano | Curtidas | Coment. | Salv. |
|---|---|---|---|---|---|---|---|---|
| Reel, Bruno falando | 4 | 167,5 (128 a 308) | 259,5 | 48,1% | 15,1 s | 67 | 5 | 2 |
| Reel, animação com voz sintética | 12 | 32,5 (14 a 169) | 40 | 83,9% | 5,0 s (sem o Carrinho) | 2 | 0 | 0 |
| Reel sintético sem o "Você gravou o curso inteiro" | 11 | 32 (14 a 40) | 38 | 83,8% | 5,2 s | 2 | 0 | 0 |
| Reel slideshow sem rosto | 1 (3) | 58 (58) | 75 (80) | 67,2% (55,4%) | 6,2 s (8,9 s) | 0 (4) | 0 (1) | 0 |
| Feed com foto do Bruno na capa | 7 (9) | 111 (126) | 245 (255) | | | 28 (57) | 2 (4) | 0 |
| Feed de texto ou sem rosto | 6 (7) | 34,5 (35) | 61 | | | 1 (2) | 2 | 0 |

- Fração do vídeo assistida em média [ESTIMATIVA: tempo médio do Buzzfy dividido pela duração do arquivo no repositório (ffprobe) ou pela tag `length_s` do Buzzfy]: Dentista A 36% (13 de 36,4 s); Ele nunca fez um anúncio 25% (18,7 de 74,6); Equipe 23% (17,2 de 74,7); 90% 18% (12,6 de 69,5). Sintéticos: de 9% (Recuperação, 3,4 de 36,4) a 22% (Captação, 8,5 de 38,2), com o Funil fora da faixa (48%, 10,7 de 22,5) e o Carrinho anômalo.
- O Dentista A, o único reel curto com o Bruno (36 s), reteve a maior fração entre os 4 [FATO para o número; HIPÓTESE para "curto segura mais", n=1].
- Capa na grade [FATO, conferência visual]: dos 4 reels com o Bruno, 2 têm o rosto na capa (Dentista A, 169; Ele nunca fez um anúncio, 308) e 2 têm capa de texto (Equipe, cartão "EQUIPE · etapa 3 de 7", 128; 90%, cartão "3 erros que eu mais vejo", 166). Efeito da capa: sem leitura com n=2 contra 2.
- Confusão de período: 3 dos 4 reels com o Bruno saíram de 03/10 a 05/10, na semana da saga, e todos os sintéticos de 11/10 a 20/10 [FATO]. O Dentista A (21/10) veio logo depois da pior semana (série 2, mediana 26 de alcance) e fez 169. É a melhor evidência de que o efeito vem do formato, mais do que do período, com n=1 [HIPÓTESE].

### 5.3 Por tipo de gancho

| Gancho | n | Alcance mediano | Faixa | Pulo mediano (reels) |
|---|---|---|---|---|
| Personagem ou contraste (saga bíblica e Ele nunca fez um anúncio) | 8 | 104,5 | 52 a 308 | 53,2% (1 reel) |
| Chamada de público (dentista, expert) | 2 (3 com o Médico) | 148,5 (128) | 128 a 169 (64 a 169) | 48,1% (49,6%) |
| Bastidor | 1 | 197 | | |
| Apresentação ("Prazer, eu sou o Bruno") | 0 (2) | (185) | (133 a 237) | |
| Número específico | 4 (6) | 34,5 (44,5) | 16 a 166 | 62,3% (45,7%) |
| Frase de consultoria em 2ª pessoa, sem personagem nem número | 15 | 33 | 14 a 169 | 83,9% |

Falas de abertura conferidas [FATO, Buzzfy `hook.said`, `words.json` e `timeline.json`]:

| Reel | Bruno | Primeira fala | Palavras até o assunto | Pulo |
|---|---|---|---|---|
| Ele nunca fez um anúncio | fala | "Deixa eu te contar uma coisa. Jesus foi o maior de todos. Sabe por quê?" | 6 de preâmbulo | 53,2% |
| 90% | fala | "Ei, vem cá, escuta essa: 90% dos lançamentos que floparam já estão mortos antes do..." | 5 de preâmbulo | 45,7% |
| Equipe | fala | "Essa é para você, expert, que gosta de fazer tudo sozinho e entrega pela metade." | 0; frase de 15 palavras | 49,6% |
| Dentista A | fala | "Dentistas, são mais de 474 mil colegas ativos no Brasil." ("474 mil" entre 2,0 e 3,1 s) | 0 | 46,6% |
| Caixa | sint. | "Seu carrinho cheio pode virar zero no caixa." (aos 0,2 s) | 0 | 82,2% |
| Marqueteiro | sint. | "Você não enriquece o marqueteiro. Você paga o erro dele." | 0 | 86,7% |
| Funil | sint. | "Fundo de funil não se compra. Você constrói em quatro etapas." | 0 | 85,7% |
| Escala | sint. | "Escala sete por sete? Nem a sua escala cinco por dois aguenta isso." | 0 | 78,9% |
| Oferta (v02) | sint. | "Seu produto é bom. A sua oferta é que não convence." (aos 0,6 s) | 0 | 83,8% |

- [FATO, buzzfy_playbook openings] O playbook manda cortar tudo antes da primeira palavra interessante e deixar a abertura em 8 palavras ou menos; cumprimento é o pior tipo de abertura medido (17% menos chance de estourar).
- Pela régua do playbook, as aberturas sintéticas são "melhores" (curtas, sem preâmbulo) e mesmo assim as 5 da tabela perderam de 78,9% a 86,7% no começo. As dos reels com o Bruno têm preâmbulo ou frase longa e perderam de 45,7% a 53,2%. Nesta conta, o que decide a abertura é o rosto e a voz do Bruno, e a frase vem depois [HIPÓTESE com apoio forte, n=4 contra 12].
- Cortar o preâmbulo dos melhores reels ("Deixa eu te contar uma coisa", "Ei, vem cá, escuta essa") é mudar uma coisa só, e o playbook aponta ganho [HIPÓTESE a testar, H2].
- [FATO] As 15 peças de gancho de consultoria não têm o Bruno em cena; o efeito do gancho não se separa do efeito do formato.
- [FATO, ig_post_stats] A saga de 7 dias caiu em alcance depois da etapa 2: 52, 189, 126, 63, 111, 98, 71 (etapas 1 a 7).

### 5.4 Por CTA (Buzzfy mais PostZen)

| CTA | n | Alcance mediano | Comentários | Resultado medido |
|---|---|---|---|---|
| Palavra-chave | 18 (19) | 33,5 (34) | 2, os dois no carrossel Checklist (3 com o Médico) | 1 disparo de automação no total |
| Pergunta aberta ou responder número | 5 (6) | 169 (167,5) | 3 (90%: 2; bastidor: 1; Dentista A: 0) | |
| Salvar | 4 | 80,5 | 3 | 2 salvamentos, os dois no "Ele nunca fez um anúncio" |
| Marcar alguém | 2 | 127 | 0 | |
| Enviar | 1 | 111 | 1 | 0 compartilhamento |

- [ESTIMATIVA, comentários divididos pelo alcance somado] Comentário por 100 contas alcançadas: palavra-chave 0,29 (2 em 700); pergunta aberta 0,39 (3 em 779); salvar 0,58 (3 em 521). Todos muito baixos.
- [FATO] O Dentista A pediu "Comenta aqui que eu te respondo" e teve 0 comentário com 169 de alcance e 10 curtidas.
- [FATO, PostZen listCommentAutomations] 17 automações ativas: TABULEIRO (Dentista B), ETAPAS de resposta de story, CASE, ESTRATEGISTA, ETAPAS série 2, FUNIL, CAIXA, ETAPAS Escala, RECUPERAÇÃO, PERPÉTUO, CARRINHO, EVENTO, PESQUISA, AQUECIMENTO, CAPTAÇÃO, OFERTA, CHECKLIST. 16 com 0 disparo. CHECKLIST: 1 disparado, 1 enviado.
- [FATO, listCommentAutomationLogs] O único disparo veio de um comentário "Checklist" no carrossel de 12/10, de um perfil cujo nome de usuário começa com "bruno". Se for teste do próprio Bruno, os leads reais por automação no período são zero [HIPÓTESE a confirmar com o Bruno].
- [FATO] A automação ETAPAS de resposta de story (conta toda) tem 0 log desde que foi criada.
- [FATO] O carrossel de 09/10 pediu TABULEIRO sem automação e o reel do Médico pediu AGENDA sem automação: esses comentários iriam para lugar nenhum.
- [FATO] O CTA de palavra-chave está quase todo em peça sintética ou de texto; o efeito do CTA não se separa do formato.
- [FATO, ig_post_stats] Compartilhamento: 1 em 35 peças (Saga 2). A conta registra 9 em 30 dias [ig_account_stats]. Os outros 8 vieram de story, de anúncio ou de post fora da janela: sem dado.

### 5.5 Por hora e dia

| Faixa (hora de São Paulo) | Reels | Alcance mediano | Composição |
|---|---|---|---|
| 06h a 11h59 | 4 | 34 | 3 sintéticos (33, 34, 34) e 90% com o Bruno (166) |
| 12h a 17h59 | 0 (1) | (54) | (Cem mil, sem rosto) |
| 18h a 20h59 | 8 | 29,5 | 8 sintéticos, nenhum com o Bruno |
| 21h a 23h59 | 5 | 128 | 3 com o Bruno (169, 128, 308), Recusa sem rosto (58), Funil sintético (14) |

| Faixa | Feed | Alcance mediano | Composição |
|---|---|---|---|
| 06h a 11h59 | 3 | 63 | bastidor (197), Saga 4 (63), Checklist (34) |
| 12h a 17h59 | 6 | 84,5 | Sagas 2, 3, 6 e 7 (189, 126, 98, 71), 2 estáticos de texto (35, 33) |
| 18h a 20h59 | 1 | 111 | Saga 5 |
| 21h a 23h59 | 3 | 35 | 2 estáticos de texto (35, 19), Saga 1 (52) |

- [FATO] Hora e formato estão confundidos: nenhum reel com o Bruno saiu entre 18h e 20h59, e só 1 sintético saiu depois das 21h. As médias por hora do Buzzfy medem o formato, não a hora [HIPÓTESE para a leitura].
- [FATO] Só entre sintéticos, o horário não mostra efeito: 11h, mediana 34 (n=3); 18h a 20h59, mediana 29,5 (n=8); 21h30, 14 (n=1).
- [FATO, ig_best_times] Os "melhores horários" são puxados por um post cada e mudam com a amostra. Com 30 posts: 23h (média 180) = Ele nunca fez um anúncio (308) mais a Saga 1 (52); sábado (180) = os mesmos dois. Com 35: 07h (185) = os dois "Prazer". Com 25: 21h (73), porque os posts de 03/10 e 30/09 saem da conta.
- [FATO, ig_best_times; ESTIMATIVA para o percentual] Seguidores online quase planos das 11h às 22h: de 386 (11h) a 430 (18h), diferença de 11%. Perto da diferença de 5x entre formatos, a hora é alavanca pequena [HIPÓTESE].

### 5.6 Por ritmo

| Período | Peças | Alcance mediano | Alcance somado | Curtidas | Seguidores novos no período |
|---|---|---|---|---|---|
| Semana da saga, 03 a 09/10 | 11 | 111 | 1.370 | 80 | 13 |
| Série 1, 11 a 14/10 (1 a 3 por dia) | 9 | 34 | 423 | 2 | 5 |
| Série 2, 18 a 20/10 (3 por dia) | 8 | 26 | 206 | 0 | 0 |

[FATO, ig_post_stats e ig_follower_growth; somas e medianas por este relatório]. O volume maior da série 2 deu o menor alcance somado da fase. O formato muda junto, então o efeito do volume sozinho segue sem prova isolada [HIPÓTESE], em linha com o aprendizado do CLAUDE.md ("3 posts por dia não aumentaram seguidores").

---

## 6. O que segura atenção e o que derruba

### Segura
1. **O Bruno falando para a câmera.** 4 de 4 reels acima de 3,4x a mediana de alcance; pulo de 45,7% a 53,2%; 15,1 s assistidos na mediana; 97% das curtidas de reel dos 30 posts (67 de 69) [FATO, ig_post_stats].
2. **Rosto e voz do Bruno nos primeiros segundos, mais do que a frase.** Mesmo com preâmbulo, os reels com o Bruno têm mediana de pulo 35,8 pontos menor que a dos sintéticos de abertura curta (48,1% contra 83,9%) [FATO para os números; HIPÓTESE para a causa].
3. **Foto do Bruno na capa do feed.** 111 contra 34,5 de alcance mediano; 23 contra 1 visita ao perfil [FATO].
4. **Personagem e contraste** (saga bíblica): 8 peças, mediana de 104,5; a única peça com salvamento e a única com compartilhamento da fase [FATO].
5. **Apresentação pessoal e bastidor**: os 3 estáticos de maior alcance de feed (237, 197, 133) e 34 das 48 visitas ao perfil vindas do feed nos 35 [FATO].
6. **Vídeo curto com o Bruno**: o Dentista A (36 s) reteve 36% do vídeo, contra 18% a 25% nos de 70 a 75 s [ESTIMATIVA, n=1].

### Derruba
1. **Animação com voz sintética.** 12 reels, mediana de 32,5 de alcance, 83,9% de pulo, 2 curtidas e nenhum comentário somados [FATO].
2. **Frase de consultoria sem personagem nem número** como gancho (15 peças, mediana 33) [FATO, com a confusão de formato da seção 5.3].
3. **Estático de cartão de texto** (série 2): 4 peças, mediana 34, zero interação, zero visita [FATO].
4. **Pedido de palavra-chave em peça de baixo alcance**: 18 pedidos nos 30 posts, 2 comentários, 1 disparo (provável teste) [FATO; HIPÓTESE para o teste].
5. **Três posts por dia**: série 2 com o menor alcance somado da fase e 8 dias seguidos sem seguidor novo de 14/10 a 21/10 [FATO]; causalidade do volume: [HIPÓTESE].
6. **Capa de reel que vende**: 11 dos 12 reels sintéticos aparecem na grade com o cartão "Comenta PALAVRA" como capa (todos menos o Marqueteiro, cuja capa é o funil "A ordem certa") [FATO, conferência visual de hoje]. O playbook aponta a abertura que vende como o sinal mais forte de gancho fraco [FATO, buzzfy_playbook openings]. Efeito da capa nesta conta: [HIPÓTESE].
7. **Story sem o Bruno**: o de 09h33 (academia, 6 s) teve 3 saídas e 6 deslizes para a próxima conta em 29 navegações [FATO, ig_post_stats]. Comparação com stories com o Bruno: sem dado ainda (os de 14h00 e 14h03 têm menos de 1 h).

---

## 7. Seguidores e caminho até o lead

- [FATO, ig_follower_growth] 30 dias: 53 entradas, 13 saídas, líquido +40. Até 11/10: 52 entradas. De 12/10 a 21/10: 1 entrada, 6 saídas, líquido -5. De 14/10 a 21/10: 0 entrada. 22 e 23/10 pendentes (incluem o Dentista A).
- [FATO] O pico de 19 entradas em 29/09 cai no dia de relatório que vai de 29/09 07h UTC a 30/09 07h UTC (o Buzzfy diz que o dia termina às 07h UTC), antes do primeiro post da fase (30/09 10h44 UTC). Causa: sem dado. Anúncio ou mudança de perfil: [HIPÓTESE].
- [FATO, ig_account_stats] 447 visitas ao perfil, 7 cliques no site, 0 toque em botão de link. [ESTIMATIVA] 7 cliques sobre 447 visitas = 1,6%. 53 seguidores sobre 447 visitas = 11,9%, como teto, porque seguidor também vem de fora do perfil.
- [FATO] Alcance de seguidores: 419 de 1.618 em 30 dias [ESTIMATIVA: 26%]. Não seguidores: 2.792. Do total, 1.907 vieram de anúncio.
- [FATO, ig_post_stats] Os números por post são só orgânicos ("Counts are organic only"). A comparação da seção 5 não tem anúncio dentro.
- [FATO, PostZen] 1 disparo de automação no mês. Diagnósticos marcados e vendas: sem dado nesta frente (contexto: 0 venda).

---

## 8. Leitura para o calendário da TV (exibição seg 02/11)

Só o que a auditoria sustenta. A decisão de calendário fica com o conselho.

1. [FATO, PostZen listPosts] Agenda de feed de 24/10 a 21/11: Dentista B (sáb 24/10 21h), TL01 (dom 25/10 18h30), PB01 (seg 26/10 21h), CAR01 (ter 27/10 12h), CI01 (qua 28/10 21h), PO01 (qui 29/10 21h), PB02 (sex 30/10 21h), TL02 (sáb 31/10 18h30), TL03 (07/11), TL04 (14/11), TL05 (21/11), estes três às 18h30. Story PF01 (ter 27/10 16h).
2. [FATO] De dom 01/11 a sex 06/11, a semana da exibição, não há nenhum post agendado. Depois de 31/10, o feed tem 1 reel por semana (os timelapses).
3. [FATO] De seg 26/10 a dom 01/11 estão agendados 5 reels (PB01, CI01, PO01, PB02, TL02) e 1 carrossel (CAR01). O ritmo aprovado é 5 reels e 2 carrosséis por semana [CLAUDE.md].
4. [FATO, seção 5.5] Nenhum reel com o Bruno saiu entre 18h e 20h59 até hoje. O TL01 (dom 18h30) e os TL02 a TL05 serão as primeiras leituras de reel com o Bruno nessa faixa. Como timelapse é outro formato (não é o Bruno falando para a câmera), o TL01 não testa a hora sozinho [HIPÓTESE]. Comparar com o PB01 (seg 21h) separa melhor.
5. [FATO, legendas no PostZen] Os CTAs da série da TV são quase todos pergunta aberta ou número nos comentários (TL01 a TL05, CAR01, CI01), mais direct (CAR01, PB02) e enviar (PB01). Só o Dentista B usa palavra-chave (TABULEIRO, com automação). Isso segue o dado da seção 5.4, com a ressalva de que a diferença lá está confundida com o formato.
6. [FATO] O PO01 diz "Comenta a palavra" sem dizer qual palavra na legenda, e não há automação ligada a ele. Se a palavra aparece no vídeo: sem dado (não conferido nesta frente).
7. [FATO, PostZen] Todas as legendas da série da TV têm 5 hashtags. O Buzzfy marca 6 ou mais como problema (o Dentista A tinha 8 e o Cem mil, 7).
8. [FATO, contexto e PostZen] A marcação da Mirna fica com o Bruno pelo app: o PostZen não marca pessoa nesses formatos. O Buzzfy não mostra de onde veio o alcance de cada post (marcação, explorar, seguidores): o efeito da marcação vai ficar sem dado por post. Dá para ver só no alcance de não seguidores da conta, semana a semana [FATO, ig_account_stats traz nonFollowers só no total].
9. [FATO] O TL01 e o TL02 já dizem na legenda "A entrevista vai ao ar na segunda, 02/11", coerente com a data nova.

---

## 9. Achados que os documentos ainda não tinham

1. **A semana da exibição está vazia no PostZen** (seção 8, item 2).
2. **O Instagram ainda mexe em reel com mais de 48 h**: o Marqueteiro mudou de 92,9% para 86,7% de pulo entre 13h40 e 14h50, com 92 h de vida [FATO]. Ler os números de um reel só depois de 72 h, ou registrar a hora da leitura.
3. **A abertura curta dos sintéticos não salvou o pulo** (seção 5.3). A frase de abertura pesa menos do que rosto e voz nesta conta [HIPÓTESE].
4. **Os 2 melhores reels abrem com preâmbulo** ("Deixa eu te contar uma coisa", "Ei, vem cá, escuta essa"). Cortar é o teste mais barato de um remake [HIPÓTESE, H2].
5. **2 dos 4 reels com o Bruno têm capa de texto na grade** (Equipe e 90%) [FATO].
6. **Capa CTA em 11 dos 12 reels sintéticos** [FATO]. Antes de publicar reel, conferir a capa escolhida no PostZen.
7. **O "melhor horário" do Buzzfy depende do tamanho da amostra** (23h com 30 posts, 21h com 25, 07h com 35) [FATO].
8. **O único disparo de automação pode ser teste** [HIPÓTESE]. Conferir com o Bruno.
9. **O Dentista A pediu comentário e teve 0** com 169 de alcance [FATO].
10. **"Você gravou o curso inteiro" é ponto fora da curva sem retenção**: 169 de alcance com 86,9% de pulo, 5 s assistidos e zero interação [FATO]. Foi o 11º post depois do estouro de 03/10 e o primeiro depois de um dia sem post (10/10); o Buzzfy diz que o empurrão de um estouro some em cerca de 10 posts [FATO, ig_reel_checkup hot_streak.protocol; contagem pela tabela]. O alcance pode ter vindo do resto desse embalo ou da pausa, mais do que do vídeo [HIPÓTESE].
11. **2 dos 5 "candidatos a refazer" são fracos**: o reel de 01/01/2025 é retrospectiva pessoal de fé, fora da grade e do nicho, com 5,1 s assistidos [FATO]; o "Você gravou o curso inteiro" tem 86,9% de pulo e nenhuma interação [FATO]. A lista do Buzzfy é mecânica (múltiplo de views) [FATO, ig_reel_checkup "why"]. Os 3 fortes para refazer têm o Bruno em cena: Ele nunca fez um anúncio, 90% e Dentista A.
12. **O melhor reel não tinha legenda queimada**: "Ele nunca fez um anúncio" tem `burned_subtitles=false`; Equipe e 90% têm `true` [FATO, Buzzfy tags]. O playbook mede legenda queimada como a maior mudança isolada (4,6x a mediana de views) [FATO, ig_reel_checkup for_you_to_check].
13. **Seguindo subiu de 3.523 para 3.528** desde 21/10 e a bio segue a antiga [FATO]. As correções 1 e 3 do Módulo 1 não começaram.

---

## 10. Hipóteses para o conselho testar (uma coisa por vez)

| # | Hipótese | Teste | Métrica e régua | Onde ler |
|---|---|---|---|---|
| H1 | Reel com o Bruno falando mantém alcance acima de 100 fora das 21h | Ler o PB01 (seg 21h) e o primeiro corte da TV que sair às 18h30 | Alcance em 72 h; acima de 100 confirma | ig_post_stats |
| H2 | Cortar o preâmbulo da abertura baixa o pulo | Remake do "Ele nunca fez um anúncio" ou do 90% começando na primeira palavra interessante | Pulo em 72 h contra 53,2% e 45,7% | ig_reel_checkup |
| H3 | Capa com o rosto do Bruno traz mais visitas ao perfil | Capas com rosto nos próximos reels | Visitas ao perfil por semana contra 447 em 30 dias | ig_account_stats |
| H4 | Legenda queimada no "Ele nunca fez um anúncio", mudando só isso | Repostar a mesma fala com legenda | Views contra 578 e pulo contra 53,2% | ig_post_stats |
| H5 | Pergunta aberta rende mais comentário que palavra-chave com alcance parecido | Comparar Dentista B (TABULEIRO) com PB01 e CI01 (pergunta) | Comentários por 100 de alcance | ig_post_stats, listCommentAutomationLogs |
| H6 | O Dentista A trouxe seguidores em 22 e 23/10 | Ler de novo na segunda | Entradas de 22 e 23/10 | ig_follower_growth |
| H7 | Story com o Bruno em cena segura mais que story sem ele | Ler os stories de hoje antes de expirarem (até dom 25/10, 14h a 20h30) | Saídas e deslizes por 100 views contra o de 09h33 (9 em 33) | ig_post_stats |
| H8 | A marcação da Mirna e a exibição de 02/11 aumentam o alcance de não seguidores | Ler a conta antes e depois de 02/11 | Alcance de não seguidores por semana contra 2.792 em 30 dias (1.907 de anúncio dentro) | ig_account_stats |

---

## 11. Lacunas

1. Tags de vídeo do Buzzfy só existem para 7 dos 20 reels. Gancho escrito na tela dos sintéticos: sem dado.
2. Se a voz dos reels "O que você recusa" e "Cem mil seguidores" é a do Bruno: sem dado (o Buzzfy marca voz própria com framing sem pessoa; o "Médico" marca voiceover).
3. Formato visual dos posts de 30/09 a 09/10 além das capas: sem dado (os arquivos do repositório começam em 11/10).
4. Curva de retenção por segundo: o Buzzfy entrega pulo e tempo médio, não o ponto de queda. Onde o espectador sai depois dos primeiros segundos: sem dado.
5. Visitas ao perfil e seguidores por reel: o Buzzfy não traz para reel. Seguidor por peça: sem dado (só o 1 do post de 07h55 de 30/09).
6. Stories expirados: métrica por story perdida (o Buzzfy só lê nas 24 h). Os stories de 13/10 e 18/10 publicados pelo PostZen: sem dado. Os 9 de hoje precisam ser lidos antes de expirarem.
7. Origem de 8 dos 9 compartilhamentos de 30 dias: sem dado.
8. Causa do pico de 19 seguidores em 29/09: sem dado. Calendário e alvo dos anúncios ficam com a frente de anúncios.
9. CTA dos posts "Prazer" e do carrossel "100 mil": a leitura do Buzzfy corta a legenda em 500 caracteres. Sem dado.
10. Autor do único disparo de automação: confirmar com o Bruno.
11. Seguidores de 22 e 23/10 pendentes no Instagram.
12. Capa escolhida para o Dentista B e para os cortes da TV no PostZen: o `listPosts` não mostra a capa. Sem dado.
13. Se os cortes da TV (PB01, CI01, PO01, PB02) têm o Bruno em cena nos 3 primeiros segundos e se a palavra do PO01 aparece no vídeo: não conferido nesta frente.
14. Horário de exibição do programa em 02/11: sem dado (contexto).
15. Todas as comparações têm n pequeno (4 reels com o Bruno; 1 a 2 peças em alguns grupos) e período confundido com formato.

---

## 12. Fontes

- Buzzfy, leituras de 24/10/2026, 14h48 a 14h54: `ig_posts` (4 chamadas), `ig_post_stats` (2), `ig_reel_checkup`, `ig_account_stats`, `ig_follower_growth`, `ig_best_times` (25, 30 e 35 posts), `ig_audience`, `buzzfy_playbook` (openings).
- PostZen, mesmo horário: `listPosts` (agenda de 24/10 a 23/11 e publicados), `listCommentAutomations` (accountId j97772ycndetk3f1wcdbh14p898g4b8w), `listCommentAutomationLogs` (CHECKLIST qs7de23c7nzxzw2k4yjshgm5gd8g5dmx; TABULEIRO qs747t4bq23a1qpnjskexg34vs8gx7hx; ETAPAS de story qs78ccqc3nf0axhc59frr8mewx8ghnvj).
- Links das peças (devolvidos pelo Buzzfy): https://www.instagram.com/reel/DexpShwiCJ0/ (Dentista A), https://www.instagram.com/reel/DeDhWnuoTLT/ (Ele nunca fez um anúncio), https://www.instagram.com/reel/DeE0ZL5ERFq/ (90%), https://www.instagram.com/reel/DeIjIM5ovUo/ (Equipe), https://www.instagram.com/reel/DeXoA6LxW6D/ (Você gravou o curso inteiro), https://www.instagram.com/reel/DeuzVnYgV00/ (Marqueteiro), https://www.instagram.com/p/Dd6K1ehEY1H/ (Prazer, mineiro), https://www.instagram.com/p/Dd_hjF6EQs_/ (bastidor), https://www.instagram.com/stories/o_estrategista.com.br/4015133260140693473 (story de 14h00), https://www.instagram.com/stories/o_estrategista.com.br/4015134743817455677 (story de 14h03).
- Repositório: `conteudo/modo-god-cronograma/contexto.md`, `conteudo/sistema-instagram/00-SISTEMA.md` (linhas 17, 20, 42 a 46), `CLAUDE.md` (linha 13), `videos/v01` a `videos/v08` (`tts.py`, `timeline.json`, mp4), `videos/serie2/roteiros.json` e `*/timeline.json`, `videos/nichos/dentista/words.json` e `render/`.
- Versão anterior desta frente: commit 88433c7 (leituras de 13h28 a 13h40).
