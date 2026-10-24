# F6 · Stories diários e objeções · @o_estrategista.com.br · rodada de 24/10/2026

Frente F6 da pesquisa do conselho Agência Reunida. Leituras feitas entre 14h02 e 14h15 de sábado, 24/10/2026 (São Paulo), todas só de leitura. Nada foi publicado, agendado, alterado ou enviado no Instagram, no Buzzfy, no PostZen ou nos sites. Toda mudança abaixo é proposta para o Bruno executar.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha uma objeção sozinho. Métrica que falta: "sem dado".

**O que esta frente não repete:** as 12 objeções com contra-argumento (`conteudo/stories-objecoes/01-objecoes.md`), o inventário de provas com tempos da transcrição e a lista do que não pode ser dito (`02-provas.md`) e o plano de stories de 25 a 31/10 com os 3 reels ob01 a ob03 (`03-plano-7-dias.md`). Aqui entram só dado novo, conferência e o que falta nesses arquivos. Base de reel não é usada nesta frente (story não tem mediana no Buzzfy: "stories have none", descrição do `ig_post_stats`).

---

## 0. Consultas feitas

| # | Consulta (só leitura) | Parâmetros | Hora (SP) | Resultado |
|---|---|---|---|---|
| 1 | Buzzfy `ig_posts` | kind=stories | 14h02 | 2 stories no ar: 09h33 (vídeo, postado à mão, fora do PostZen) e 14h00 (st01, vídeo, PostZen) |
| 2 | Buzzfy `ig_post_stats` | os 2 ids acima | 14h03 | ok. st01 com 0 h e tudo zerado (provisório); 09h33 com 4,5 h |
| 3 | Buzzfy `ig_account_stats` | 30 dias (24/09 17h02 a 24/10 17h02 UTC) | 14h02 | ok |
| 4 | Buzzfy `ig_account_stats` | 7 dias (17/10 a 24/10, 17h02 UTC) | 14h02 | ok |
| 5 | Buzzfy `ig_best_times` | America/Sao_Paulo, 35 posts | 14h05 | ok; 27 dias de seguidores online |
| 6 | Buzzfy `buzzfy_playbook` | small_accounts, checklists | 14h06 | ok. O playbook é de reels e não tem regra de story nos dois tópicos lidos |
| 7 | PostZen `listCommentAutomations` | accountId j97772ycndetk3f1wcdbh14p898g4b8w | 14h02 | 17 automações ativas; 1 de resposta de story (ETAPAS) |
| 8 | PostZen `listCommentAutomationLogs` | ETAPAS resposta de story (qs78ccqc3nf0axhc59frr8mewx8ghnvj) | 14h03 | 0 log, total 0 |
| 9 | PostZen `listPosts` | mesma conta, 24/10 a 23/11, por data | 14h02 | 16 itens: 1 publicado (st01 14h00) e 15 agendados |
| 10 | PostZen `listPosts` | mesma conta, status published | 14h04 | 21 itens desde 12/10; stories pelo PostZen só em 13/10 (2), 18/10 (2) e 24/10 (1) |
| 11 | Site `estrategistadelancamento.com.br/tabuleiro/?o=ig-stories` | WebFetch e download do HTML e de `js/tabuleiro.js` | 14h08 a 14h15 | abre; conteúdo conferido no código |
| 12 | Site `estrategistadelancamento.com.br/v2/` (link da bio) | WebFetch, HTML e `js/main.js` | 14h10 | abre. O resumo do WebFetch disse que os botões apontavam para "#"; o código mostra que o `main.js` troca todo `data-wa` por link de WhatsApp. Registro o erro do resumo e fico com o código |
| 13 | Página do PDF da ETAPAS (`.../m/checklist?o=ig-story-etapas`) | WebFetch e HTML | 14h12 | abre. O WebFetch disse que não havia grupo; o HTML mostra o grupo depois do envio do formulário. Fico com o HTML |
| 14 | Meta, referência IG User Media (developers.facebook.com) | WebFetch | 14h06 | aberta |
| 15 | Socialinsider, "2025 Instagram Stories Benchmarks" | WebFetch | 14h06 | aberta |
| 16 | Hypebot, 24/06/2021 (frequência, Mosseri) | WebFetch | 14h06 | aberta |
| 17 | Instagram, anúncio do sticker de link (about.instagram.com, 27/10/2021) | WebFetch | 14h07 | aberta |
| 18 | Buzzfy `ig_posts` kind=stories e `ig_post_stats` (3 ids, sem mediana) | 2ª leitura | 14h14 | 3 stories no ar (09h33, 14h00, 14h03); ok |
| 19 | Repositório: `transcricao.json` e `correcoes.json` (tv-camara), `conhecimento-o-estrategista.md`, `00-SISTEMA.md` (Módulo 6 e perfil), `estaticos/` (stories-frases, destaque-comece-aqui, stories-escala) | leitura | 14h10 | ok |

Nenhuma consulta voltou com erro. Duas leituras por resumo automático (itens 12 e 13) vieram incompletas e foram corrigidas pelo código da página; nenhuma conclusão abaixo se apoia nesses resumos.

Ferramentas fora da lista desta rodada e por isso não usadas: `ig_comments` e `ig_inbox` (texto de comentário e de direct). Consequência: a frequência real de cada objeção continua sem dado.

---

## 1. Respostas curtas

1. **Story é o maior bloco de views orgânicas da conta.** 7 dias: 981 de 1.835 views (53,5%). 30 dias: 4.226 de 10.452 orgânicas (40,4%) [FATO, `ig_account_stats` 14h02; ESTIMATIVA para os percentuais]. São cerca de 140 views de story por dia nas duas janelas [ESTIMATIVA: 981 / 7 e 4.226 / 30].
2. **Story conversa pouco.** 3 respostas em 7 dias e 7 em 30 dias, cerca de 1,7 resposta por 1.000 views de story em 30 dias [FATO, `ig_account_stats`; ESTIMATIVA: 7 / 4.226 x 1.000, supondo que "replies" da conta sejam respostas a story].
3. **A automação ETAPAS de story só dispara se a resposta tiver "etapa" ou "etapas".** Está ativa, com 0 disparo e 0 log [FATO, `listCommentAutomations` e `listCommentAutomationLogs`]. O `03-plano-7-dias.md` manda "Responde este story com a sua área" e diz que a resposta "cai na automação ETAPAS" (dom 25/10 09h02 e sex 30/10 17h31). Como está configurada, uma resposta "dentista" não dispara nada: chega no direct e só o Bruno responde. E quando dispara, a ETAPAS entrega o PDF do checklist, não o diagnóstico.
4. **TABULEIRO não tem gatilho em story.** A automação TABULEIRO é só de comentário e só no post do Dentista B [FATO, `listCommentAutomations`: trigger "comment", postId do Dentista B]. Story com "responde TABULEIRO" não dispararia nada.
5. **A origem "story" some no caminho até o WhatsApp.** O link `/tabuleiro/?o=ig-stories` abre o teste, mas a mensagem pronta do WhatsApp leva só nota, gargalo e profissão (quando o link tem `?p=`), sem o `o` [FATO, `js/tabuleiro.js`, linhas 36 a 45 e 110 a 125]. O Bruno não consegue separar, pela mensagem, quem veio do story e quem veio do comentário.
6. **Todo sticker é à mão.** A API do Instagram não publica sticker em story [FATO, Meta: "Publishing stickers (i.e., link, poll, location) is not supported"], então story do PostZen sai sem enquete, caixa ou link. Hoje os 8 stories agendados sobem pelo PostZen como "postType: story" [FATO, `listPosts`], logo nenhum pode levar enquete, caixa ou link, salvo se o Bruno postar outro story à mão.
7. **Frequência: a conta não tem dado por quantidade de stories.** O Buzzfy só lê story nas 24 h [FATO, nota do `ig_posts`] e o PostZen só registra os que ele mesmo publicou. A evidência externa é fraca e não concorda: "dois stories por dia" (Mosseri, 2021, por fonte secundária) contra "pelo menos 6 stories por dia" (Socialinsider, 2025, como tática, sem medida). Proposta [HIPÓTESE]: 6 a 8 por dia em 4 blocos, com o 1º story do dia sempre com o Bruno em cena e o teste lido no Módulo 7 (seção 3).
8. **Horário pesa pouco; ordem pesa mais.** Seguidores online ficam entre 339 e 430 de 08h a 22h, pico às 18h (430) [FATO, `ig_best_times`]. Story fica 24 h no ar. Quem abre o perfil uma vez por dia vê a pilha do dia em ordem [PRIOR], e as saídas se concentram nos 3 primeiros [FATO, Socialinsider 2025]. O 1º story do dia é o mais visto e hoje, no `03-plano`, é um repost do post de ontem.
9. **Sequência:** o `03-plano` tirou a frase de efeito e a caixa de pergunta ("um pedido por dia"). Proponho um molde diário com os 7 tipos pedidos sem quebrar essa regra: enquete e caixa medem, não pedem; o único pedido segue sendo o link do diagnóstico (seção 5).
10. **Destaques:** o estado atual no perfil é sem dado (nenhuma ferramenta permitida lê destaque). O 00-SISTEMA decidiu 4 (COMECE AQUI, PROVA, MÉTODO, QUEM SOU), mas não existe capa PROVA, e o COMECE AQUI de hoje tem só os 3 stories animados do Escala, sem o Bruno (seção 8).
11. **Objeções:** "20 anos de estratégia de divulgação" não se sustenta como escrito. A transcrição tem "profissão por 20 anos" (a noite: DJ, casas e festas) e, em outro trecho, "eu já executava toda a estratégia da divulgação das festas", marcado como fala da repórter pela diarização (seção 9.2). Uma objeção nova entra como hipótese: "Eu vendo serviço, não curso" (seção 9.3).

---

## 2. Linha de base dos stories (medida)

### 2.1 Conta

| Métrica | 7 dias (17 a 24/10) | 30 dias (24/09 a 24/10) | Fonte |
|---|---|---|---|
| Views de story | 981 | 4.226 | [FATO, `ig_account_stats`, 14h02] |
| Contas alcançadas por story | 337 | 756 | idem |
| Views totais da conta | 1.835 (0 de anúncio) | 12.659 (2.207 de anúncio; 10.452 orgânicas) | idem |
| Views de reel / carrossel / post | 444 / 165 / 244 | 2.242 / 1.788 / 2.154 | idem |
| Respostas (conta) | 3 | 7 | idem |
| Comentários / compartilhamentos / salvamentos | 2 / 4 / 0 | 14 / 9 / 3 | idem |
| Visitas ao perfil / cliques no site | 74 / 0 | 447 / 7 | idem |

Contas derivadas [ESTIMATIVA, divisão simples]:
- Views de story por dia: 140 (7 dias) e 141 (30 dias). Quantos stories saíram por dia nessas janelas: sem dado. Por isso não dá para calcular views por story.
- Views por conta alcançada: 2,9 (7 dias) e 5,6 (30 dias). Quem vê story volta a ver.
- Teto de seguidores que viram algum story: 20,8% em 7 dias (337 / 1.618) e 46,7% em 30 dias (756 / 1.618), se todo alcance de story fosse de seguidor. O Buzzfy não separa seguidor de não seguidor por tipo de mídia.
- Respostas por 1.000 views de story: 3,1 (7 dias) e 1,7 (30 dias).
- No ritmo de 30 dias, 14 dias dão cerca de 3,3 respostas. A meta do D5 do `00-enquadramento` (7 ou mais em 14 dias) pede mais que o dobro.

### 2.2 Stories no ar agora

| Story | Postado | Idade | Alcance | Views | Toque para avançar | Deslize para outra conta | Saída | Respostas | Fonte |
|---|---|---|---|---|---|---|---|---|---|
| Vídeo de 09h33 (à mão, fora do PostZen; cena de academia segundo o F1) | 24/10 09h33 | 4,5 h | 21 | 27 | 14 | 6 | 3 | 0 | [FATO, `ig_post_stats`, 14h03, provisório] |
| st01 bastidor da TV | 24/10 14h00 | 0 h | 0 | 0 | 0 | 0 | 0 | 0 | idem |
| 2ª leitura, 14h14: vídeo de 09h33 | | 4,7 h | 21 | 31 | 15 | 6 | 3 | 0 | [FATO, `ig_post_stats`, 14h14] |
| 2ª leitura, 14h14: st01 | | 0,2 h | 0 | 7 | 0 | 0 | 0 | 0 | idem |
| 2ª leitura, 14h14: estático de bastidor (14h03) | | 0,2 h | 0 | 4 | 0 | 0 | 0 | 0 | idem |

Do story de 09h33, na 1ª leitura [ESTIMATIVA, sobre views]: 51,9% tocaram para avançar, 22,2% deslizaram para outra conta, 11,1% saíram. Foi o único story no ar, então foi primeiro e último da pilha ao mesmo tempo. É n de 1. Na 2ª leitura o alcance de st01 e do estático segue 0 com 7 e 4 views: abaixo de 5 viewers a ferramenta não abre o resto [FATO, nota do `ig_post_stats`]. Com 12 minutos de vida, nada a concluir.

### 2.3 Régua externa (nível 3, para orientar, nunca para julgar a conta)

[FATO, Socialinsider, "2025 Instagram Stories Benchmarks", página aberta às 14h06] Stories de marcas de 1 mil a 1 milhão de seguidores, janeiro a maio de 2025. A página dá duas amostras sem conciliar (161.180 na introdução e 113.361 na metodologia).
- Taxa de saída por posição: 23,8% no 1º story, 20,5% no 2º, 18,5% no 3º, 15,7% no 4º, 13,3% no 9º e cerca de 12,5% no 15º. Não há número do 5º ao 8º.
- Toque para avançar na faixa de 1 mil a 5 mil seguidores: 56,82% em imagem e 50,50% em vídeo.
- Saída na faixa de 1 mil a 5 mil: 12,82% em imagem e 13,42% em vídeo. A página diz que a diferença entre formatos é "pretty small".
- Tática escrita, sem medida: "Post at least 6 Stories per day to boost visibility" e parar antes do 14º, salvo se o conteúdo pedir.
- Nada sobre stickers: a página não traz número de enquete, caixa ou link.

[ESTIMATIVA] Aplicando em cadeia as saídas do 1º ao 4º (0,762 x 0,795 x 0,815 x 0,843), cerca de 42% de quem começa a pilha chega ao 5º story. Premissa: a "taxa de saída" do relatório é a fração que sai em cada posição. Não é a conta do Bruno; serve para mostrar por que o que vai no fim da pilha (chamada do reel, link) é visto por menos gente.

A definição de saída do Buzzfy (toque de saída, separado do deslize para outra conta) pode não ser a mesma do relatório: não compare o 11,1% do story de 09h33 com os 23,8% do relatório.

---

## 3. Frequência

**O que a conta registra.**
- [FATO, PostZen `listPosts` published] Stories publicados pelo PostZen: 13/10 (2, às 18h30 e 18h32), 18/10 (Escala 2/3 e 3/3, às 19h26 e 19h31) e 24/10 (st01, 14h00). Os postados à mão (como o de 09h33 de hoje) não ficam registrados em nenhuma ferramenta permitida depois de 24 h.
- [FATO, `listPosts`] Hoje: 8 stories agendados entre 14h00 e 20h30, mais o de 09h33. São 9 no dia.
- [FATO, `03-plano-7-dias.md`] Semana de 25 a 31/10: 56 stories (8 por dia), 29 agendados e 27 manuais.

**O que dizem as fontes externas (todas abertas, nível 3).**
- [FATO, Hypebot, 24/06/2021] O artigo diz que Adam Mosseri sugeriu dois posts de feed por semana e dois stories por dia para crescer. É paráfrase do site, sem a fala original; tem 5 anos.
- [FATO, Socialinsider 2025] "Post at least 6 Stories per day", como tática; saídas maiores nos 3 primeiros; "the middle of the sequence is now the strongest reach zone".
- As duas não concordam e nenhuma mede conta de expert brasileiro com 1.600 seguidores. Nenhuma fecha a decisão.

**Proposta [HIPÓTESE], para o conselho decidir.**
- 6 a 8 stories por dia, divididos em 4 blocos (seção 4), com teto de 9 e piso de 4 em dia sem peça nova.
- Teste de duas semanas, lido no Módulo 7: S1 (25 a 31/10) no ritmo do `03-plano` (cerca de 8 por dia); S2 (01 a 07/11) com o mesmo molde e 6 por dia (sem o repost das 9h e sem o 2º estático de prova). Critério de leitura: views de story por dia e respostas por 1.000 views, por `ig_account_stats` de 7 dias em 02/11 e 09/11, e a retenção de cada bloco (seção 10). Se 6 por dia mantiver 90% ou mais das views diárias de 8 por dia, fica 6, porque custa menos ao Bruno. O 90% é [PRIOR].
- Capacidade [FATO, contexto.md: "não dá para supor gravação diária"; `03-plano`: 27 manuais por semana]. Postar à mão não é gravar, mas prende o Bruno ao celular em hora marcada. Proposta [HIPÓTESE]: no máximo 2 janelas manuais por dia (12h e a noite do reel). O que precisa de sticker cai nessas janelas; o resto vai pelo PostZen.

---

## 4. Horários

[FATO, `ig_best_times`, 27 dias, seguidores online por hora, São Paulo]

| Hora | 07h | 08h | 09h | 10h | 11h | 12h | 13h | 14h | 15h | 16h | 17h | 18h | 19h | 20h | 21h | 22h | 23h |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Online | 297 | 339 | 364 | 374 | 386 | 407 | 411 | 396 | 390 | 396 | 417 | 430 | 424 | 410 | 416 | 391 | 312 |

- A curva é plana de 08h a 22h: a diferença entre 09h e o pico das 18h é de 66 pessoas [ESTIMATIVA: 430 menos 364].
- Story fica 24 h no ar [FATO, Meta: "Stories expire after 24 hours"]. O horário de publicação decide quem vê primeiro e o que fica no topo da pilha; a hora em si pesa menos que no reel [PRIOR].
- O `ig_best_times` de hoje mudou um pouco desde o contexto (12h40): com 35 posts, as melhores horas de post próprio são 07h (185, 2 posts), 23h (180, 2) e 11h (77, 6); 21h tem média 73 (5) e 18h, 49 (6); mediana 54 [FATO, `ig_best_times` 14h05]. É sobre feed e reel, não sobre story.

**Blocos propostos [HIPÓTESE]:**

| Bloco | Dia útil (reel às 21h) | Fim de semana (reel às 18h30) | Online na hora |
|---|---|---|---|
| A · abertura | 09h00 | 10h00 | 364 / 374 |
| B · objeção | 12h00 a 12h03 | 12h00 a 12h03 | 407 |
| C · frase e medição | 17h30 | 16h00 | 417 / 396 |
| D · reel | 20h30 chamada e 21h05 compartilhamento | 17h30 chamada e 18h35 compartilhamento | 410 a 430 |

O fim de semana desloca C para 16h para a chamada do reel das 18h30 não ficar colada na frase do dia. Os horários de B e D são os do `03-plano`; muda só a abertura e o bloco C.

---

## 5. Sequência diária: molde com os 7 tipos pedidos

Regra que se mantém do `03-plano`: um pedido por dia (o link do Diagnóstico de 12 casas). Enquete e caixa entram como medição, sem pedir nada. "AGENDADO" vai pelo PostZen sem sticker; "MANUAL" é postado pelo Bruno no app com o sticker na zona livre.

| Ordem | Tipo pedido | Bloco | O que vai | Sticker | Como sobe | Fonte do conteúdo | Métrica |
|---|---|---|---|---|---|---|---|
| 1 | Bastidor | A | Bruno em cena: trecho de 5 a 15 s da TV (B4, st01, mc01 a mc04) enquanto houver; depois, foto ou vídeo do dia de trabalho | nenhum | AGENDADO | `02-provas.md` B1 a B4; `videos/tv-camara/cortes/` | Saída e deslize do 1º story (é o mais visto) |
| 2 | Quebra de objeção | B | "O QUE EU MAIS OUÇO", a frase do cliente | Enquete de medição (SIM / NÃO) | MANUAL | `01-objecoes.md`, frase "como o cliente fala" | Votos da enquete (contagem à mão) |
| 3 | Quebra de objeção (virada) | B | Contra-argumento na voz do Bruno | nenhum | AGENDADO | `01-objecoes.md` | Toque para avançar |
| 4 | Prova de autoridade | B | Frase literal da TV, case como fato do caso ou critério do método | nenhum | AGENDADO | `02-provas.md` (com tempo da transcrição) | Saída no story |
| 5 | Pedido (diagnóstico) | B | Estático DIAGNÓSTICO · 12 CASAS | Link `/tabuleiro/?o=ig-stories` (mais `&p=profissão` em dia de nicho) | MANUAL | `03-plano` (f1.jpg) | Mensagens de WhatsApp que chegam com nota (contagem do Bruno) |
| 6 | Frase de efeito | C | FRASE DO DIA, uma por dia, sem pedido | nenhum | AGENDADO | `estaticos/stories-frases/` (story-frase-1 a 5 prontas) | Toque para avançar e saída |
| 7 | Caixa de pergunta | C | Só 1 vez por semana (sábado): "Qual a sua maior dúvida antes de chamar um estrategista?" | Caixa de pergunta | MANUAL | `01-objecoes.md`, seção 5 | Respostas lidas e registradas por objeção |
| 8 | Chamada para o reel do dia | D | Dia e hora no texto, nunca "HOJE" | nenhum | AGENDADO | `03-plano` | Alcance do reel na 1ª hora |
| 9 | (fecho) | D | Compartilhar o reel publicado | Compartilhar post | MANUAL | | Toques no post (sem dado pelo Buzzfy) |

Total: 8 por dia útil, 9 no sábado (com a caixa). Em S2, se o teste da seção 3 passar a 6, saem a ordem 4 (a prova vai para dentro da virada como sub) e a ordem 9 (o repost do reel fica para o bloco A do dia seguinte).

**O que muda contra o `03-plano-7-dias.md` (delta, nada mais):**
1. O 1º story do dia deixa de ser o repost do post de ontem e passa a ser o Bruno em cena. Motivo: é o story com mais gente e com a maior saída [FATO, Socialinsider 2025: 23,8% no 1º]; e a regra medida da conta é o Bruno em cena [FATO, CLAUDE.md, 21/10/2026]. O repost de ontem vira o fecho do dia anterior (compartilhamento às 21h05 ou 18h35, que o `03-plano` já tem). [HIPÓTESE]
2. Volta a frase de efeito (ordem 6), agendada, sem sticker: não é pedido. As 5 FRASE DO DIA do `s.html` estão prontas [FATO, `estaticos/stories-frases/s.html`]. Conferência: "Fila de espera não é sucesso. É teto." é a construção "não é X, é Y" daquela peça; não juntar outra no mesmo estático.
3. Volta a caixa de pergunta, 1 vez por semana, como o `01-objecoes.md` (seção 5) já pede e o `03-plano` tirou. Motivo: a frequência de objeção é sem dado e a caixa é a única ferramenta que traz a frase do público com as palavras dele.
4. "Responde este story com a sua área" só fica se o Bruno aceitar responder à mão: não há automação para isso (seção 7).
5. As duas janelas manuais (12h e noite) concentram os 4 stories com sticker do dia: enquete, link, caixa (sábado) e compartilhamento.

**Regras do CLAUDE.md aplicadas a story:** sem travessão, sem emoji, sem promessa de resultado, sem os nomes vetados, uma "não é X, é Y" por peça, nada na borda nem no rodapé (a barra de resposta do story fica embaixo), preto e ouro, Cinzel e Playfair itálico, nenhum logo de terceiro (TV Câmara, BNI, shopping só em texto).

---

## 6. Stickers

**Fatos da plataforma.**
- [FATO, Meta, IG User Media, aberta 14h06] "Publishing stickers (i.e., link, poll, location) is not supported; however mentioning users without a sticker is supported." Menção sem sticker pode ir pela API; enquete, caixa e link, não.
- [FATO, Instagram, anúncio de 27/10/2021] O sticker de link foi liberado para todas as contas, exceto contas novas e as que compartilham repetidamente discurso de ódio ou desinformação.
- [FATO, `ig_post_stats`] Por story o Buzzfy traz alcance, views, compartilhamentos, interações, visitas ao perfil, seguidores, respostas e navegação (avançar, deslizar, sair). Não traz votos de enquete, respostas de caixa nem toques no link. Isso só se lê no app, à mão.

| Sticker | Para que | Regra | Como ler |
|---|---|---|---|
| Enquete | Medir objeção (par TEMPO x MEDO, SIM / NÃO) | Uma por dia, no story da objeção; nunca pedir voto e link no mesmo story | Votos no app, anotados em `stories-objecoes/02-medicao.md` antes de 24 h [PRIOR sobre quanto tempo o app guarda o resultado: sem dado confirmado] |
| Caixa de pergunta | Colher objeção com as palavras do público | 1 por semana; responder em story só sem expor quem perguntou [PRIOR] | Respostas no app; classificar por O1 a O13 |
| Link | O único pedido do dia (diagnóstico) | `?o=ig-stories` para o site; em dia de nicho somar `&p=dentista` (ou medico, advogado, psicologo, nutricionista, consorcio) | O `o` só chega ao analytics do site (sem ferramenta permitida: sem dado). O `p` entra na mensagem do WhatsApp [FATO, `js/tabuleiro.js`] |
| Compartilhar post | Levar ao reel do dia | Logo depois de o reel sair | Toques no post: sem dado pelo Buzzfy |
| Menção | Não usar para marcar a TV ou a Mirna sem o print da liberação | [FATO, contexto.md: liberação verbal, print pendente] | |

Zona livre do sticker: a do `03-plano` (y 1300 a 1560, em 1080 x 1920), longe da barra de resposta e da lateral direita.

---

## 7. Automação ETAPAS e o caminho até o diagnóstico

**O que está configurado [FATO, `listCommentAutomations`, 14h02].**

| Automação | Gatilho | Palavras | Onde vale | Leva a | Disparos |
|---|---|---|---|---|---|
| ETAPAS · resposta de Story (conta toda) | story_reply | etapas, etapa (palavra inteira, tolera erro de digitação; não vale em direct digitado) | qualquer story | Direct com botão "Baixar o PDF" para `.../m/checklist?o=ig-story-etapas` | 0 enviados, 0 disparados; 0 log |
| ETAPAS · série 2 (conta toda) | comment | etapas, etapa | qualquer post | mesmo PDF (`o=ig-etapas`) | 0 |
| ETAPAS · Reels Escala 7x7 | comment | etapas, etapa | um post | mesmo PDF | 0 |
| TABULEIRO · Reel Dentista B | comment | tabuleiro, tabuleiros | só o Dentista B | Direct com botão para `/tabuleiro/?o=ig-tabuleiro` | 0 |

- [FATO, descrição da ferramenta PostZen] Resposta de story usa direct comum dentro da janela de 24 h de mensagem; comentário dá direito a uma resposta privada, uma vez, em até 7 dias.
- [FATO, HTML da página do PDF] Depois do formulário (nome, WhatsApp, e-mail, Instagram, profissão, faixa de seguidores, faturamento de lançamento, prazo e maior dificuldade), a página mostra 3 passos: baixar o PDF, "Entre no Grupo do Estrategista" (grupo no WhatsApp) e "Faça o diagnóstico gratuito O Tabuleiro".
- [FATO, página `/tabuleiro/`] 12 perguntas, "Diagnóstico em 4 minutos", "Nada de e-mail, nada de cadastro." No fim, o botão "Levar meu tabuleiro pro diagnóstico (abre o WhatsApp)" e a linha "Trinta minutos sobre o seu caso. Se não fizer sentido, o diagnóstico fica de presente."
- [FATO, `/v2/` e `js/main.js`] O link da bio leva à página "A Partida"; os botões "Agendar o Primeiro Lance" viram link de WhatsApp pelo script. Não citam a TV nem cases.

**Os dois caminhos do story hoje.**
- Link no story: story, `/tabuleiro/`, 12 casas, WhatsApp com nota e gargalo. Funciona sem automação. Origem: perdida na mensagem.
- Resposta ao story: só vira automação se tiver "etapa"; e aí leva ao PDF com formulário de 9 campos, grupo e, no 3º passo, ao Tabuleiro. Qualquer outra resposta cai no direct do Bruno.

**O que não fecha.**
1. "Responde com a sua área" (`03-plano`, dom 09h02 e sex 17h31; CTA 2 do Módulo 6) depende de resposta manual. Quanto tempo o Bruno leva para responder: sem dado.
2. ETAPAS é uma segunda palavra ativa ao lado do TABULEIRO, contra a regra de uma palavra por mês [FATO, CLAUDE.md] e contra o PARAR de 21/10 (12 palavras) [FATO, 00-SISTEMA, Módulo 7]. O `00-enquadramento` (seção 5, item 5) já levantou isso para os comentários; para story é a única automação que existe.
3. A ETAPAS de story leva a material e grupo, não a diagnóstico. Para a meta de 10 diagnósticos por mês [FATO, contexto.md], é um caminho mais longo.

**Opções para o Bruno (configuração é dele; nenhuma foi feita) [HIPÓTESE cada uma]:**
- (a) Manter ETAPAS de story como está e não usar "responde etapas" nos stories: o story pede só o link. Custo zero; a automação fica parada.
- (b) Trocar a palavra da ETAPAS de story para TABULEIRO e o botão para `/tabuleiro/?o=ig-story-reply`: uma palavra no mês em comentário e em story, e o story passa a ter dois caminhos para o mesmo destino. Mexe numa configuração da conta.
- (c) Sem automação: "Responde com a sua área" e resposta manual com as 3 perguntas de qualificação do Módulo 6 [FATO, 00-SISTEMA]. Depende de tempo do Bruno.
- Em qualquer opção, pôr `&p=` no link em dia de nicho para a profissão chegar na mensagem, já que a origem não chega.

---

## 8. Destaques

**O que existe [FATO].**
- 00-SISTEMA (Módulo 1, item 9, e Perfil): "existem 5 capas prontas (xeque-mate, quem sou, tabuleiro, método, bastidor) e agora a 'Comece aqui'. Reduzir para 4: COMECE AQUI, PROVA, MÉTODO, QUEM SOU." Ordem para quem chega frio: COMECE AQUI, PROVA, MÉTODO, QUEM SOU.
- As 5 capas estão no Drive (`conhecimento-o-estrategista.md`, inventário, pasta destaques, não lidas). A do COMECE AQUI está em `estaticos/destaque-comece-aqui/capa-comece-aqui.png`. **Não há capa PROVA** em nenhuma das duas listas.
- `estaticos/destaque-comece-aqui/textos-direct.md`: o COMECE AQUI leva os 3 stories da Escala 7x7, como primeiro destaque. Esses stories são animação com trilha gerada por código, sem voz e sem o Bruno (`estaticos/stories-escala/som.py` e `story-1-som.mp4` a `story-3-som.mp4`).
- Estado atual dos destaques no perfil, quantos são, quantas views têm: sem dado (nenhuma ferramenta permitida lê destaque).
- Destaque se monta a partir de story já publicado e arquivado [fonte secundária, nível 3: guias de terceiros na busca; a Central de Ajuda do Instagram não abriu na busca].

**Proposta [HIPÓTESE] com o que já está pronto (nada a gravar):**

| Destaque | O que entra, na ordem | Origem |
|---|---|---|
| COMECE AQUI | 1) "Você atende. Eu desenho e comando o seu lançamento." (story-frase-1); 2) mc02 (Bruno na TV: "estrategista de marketing digital e lançamento de produto"); 3) um par objeção e virada (O1 ou O2); 4) DIAGNÓSTICO · 12 CASAS com link. Os 3 da Escala vão para o fim ou saem | `stories-frases`, `cortes/mc02`, `03-plano` |
| PROVA | B1 e st01 (bastidor da TV), pf01 (franquia odontológica, fato do caso), compartilhamento do pb02 (restaurante, com a ressalva), C1 só depois da reedição do vídeo do case | `02-provas.md` |
| MÉTODO | po01 compartilhado, M2 ("Cada lance tem data, responsável, número esperado e plano B"), M10 (critério "se faltam 10 dias, eu digo não"). Os "5 Lances em 5 stories" do 00-SISTEMA: arquivo sem dado no repositório | `02-provas.md`, 00-SISTEMA |
| QUEM SOU | pb01 compartilhado (trajetória), mc01 ("um computador e um sonho"), J8 (Campinas, Shopping Dom Pedro, sem logo), R1 (BNI), mc04 só depois do recorte (F4: termina em "estrategista digital") | `02-provas.md`, F4 |

- Capa PROVA: precisa ser feita no padrão das outras (preto e ouro). Ou o Bruno reaproveita a capa "bastidor" com outro nome: decisão dele.
- Destaque não leva número cru da conta, data de exibição do programa nem "a TV recomenda" [FATO, `02-provas.md`, "O que NÃO pode ser dito"].
- Medição: visitas ao perfil e cliques no site da conta (74 e 0 em 7 dias [FATO, `ig_account_stats`]); views por destaque: sem dado.

---

## 9. Objeções e provas: o que esta rodada acrescenta

### 9.1 Dado novo sobre objeção
- Nenhum. As ferramentas permitidas não leem texto de comentário nem de direct. Em 7 dias a conta teve 2 comentários e 3 respostas [FATO, `ig_account_stats`]. A frequência de cada uma das 12 objeções continua sem dado, como o `01-objecoes.md` já registra.
- O único instrumento de medição em produção é a enquete do `03-plano` (contagem manual) e a caixa semanal proposta na seção 5.

### 9.2 As 4 provas que o pedido cita, conferidas

| Prova do pedido | O que se sustenta | Fonte | Limite |
|---|---|---|---|
| Entrevista na TV | Entrevista ao programa Ser Empreendedor, TV Câmara Campinas, repórter Mirna Abreu; imagem e voz liberadas de forma verbal | [FATO, contexto.md, atualização das 13h20] | Print por escrito pendente; data de exibição sem dado; nunca "foi ao ar" nem "a TV recomenda" |
| 20 anos de estratégia de divulgação | "Na verdade, acabou sendo uma profissão por 20 anos, né?" (Bruno, 999,8 a 1003,9 s) e "vivi por 20 anos, inclusive numa casa renomada aqui do Shopping Dom Pedro" (Bruno, 1685,7 a 1692,8 s) falam da noite: DJ, casas noturnas e festas (1007,9 a 1023,8 s). "Então eu já estava no digital nesse mercado, porém, não estava como o DJ, mas fazia as festas" (Bruno, 1153,7 a 1160,0 s) | [FATO, `videos/tv-camara/dados/transcricao.json` com `correcoes.json`] | A frase "Então eu já executava toda a estratégia da divulgação das festas" (1160,4 a 1165,0 s) está marcada M pela diarização, com f0 de 226 Hz; o `03-plano` mediu a Mirna entre 191 e 266 Hz e o Bruno entre 124 e 187 Hz perto de 1316 s, e a frase anterior do Bruno (1153,7 s) tem 178 Hz. Pelo conteúdo é resposta do Bruno, mas precisa ser ouvida. Mesmo confirmada, ela não diz por quanto tempo. A base de conhecimento fala em 13 anos de marketing digital, número declarado [FATO, `conhecimento-o-estrategista.md`, seção 0]. Texto seguro: "20 anos na noite, como DJ, dono de casa e produtor de festas" e, só depois de ouvir 1160,4 s, "fazendo a divulgação das festas". Nunca "20 anos de marketing" nem "20 anos de estratégia" |
| Cases contados por ele | Restaurante (45 mil para 250 mil) e franquia odontológica (1,5 milhão com dois meses), contados na TV; case de 6 para 20 mi/mês, contado pelo responsável de marketing do cliente | [FATO, `02-provas.md` C1 a C4] | Os dois da TV só existem na fala do Bruno; sem período do restaurante; regras do case de 6 para 20 no `02-provas.md` |
| Método | Método Xeque-Mate dito na TV (1611,7 a 1624,5 s); O Tabuleiro no ar hoje: 12 perguntas, 4 minutos, sem cadastro, e "Trinta minutos sobre o seu caso. Se não fizer sentido, o diagnóstico fica de presente." | [FATO, `02-provas.md` M1; página `/tabuleiro/` aberta às 14h08] | A frase do site é texto do Bruno, não fala da TV; usar sem aspas de TV |

A frase "Fui DJ por 20 anos" já está na legenda agendada do pb01 [FATO, `listPosts`]. Pela transcrição, os 20 anos cobrem a noite inteira (DJ, casas e festas), não só o DJ. É simplificação, não número inventado; fica registrada aqui sem pedido de mudança.

### 9.3 Objeção que falta no `01-objecoes.md` (hipótese)

**O13 · "Eu vendo serviço, não curso."** Variações: "Meu negócio é atendimento, não infoproduto." · "Não tenho o que ensinar."
- Por que entra: o pedido desta frente nomeia "expert e prestador de serviço"; as 12 objeções falam de consultório e de infoprodutor. A O8 trata da indicação, não do produto. Frequência: sem dado. [HIPÓTESE]
- Prova disponível, sem número novo:
  - Os dois cases contados na TV são de negócio de serviço e de varejo, não de curso: restaurante (C4) e franquia odontológica (C3) [FATO, `02-provas.md`].
  - "Cada cliente tem um produto específico e a gente vive esse produto." (M3, 1580,7 a 1583,8 s) [FATO, `02-provas.md`].
  - "As pessoas me contratavam para resolver problemas nas empresas delas." (C5, 1078,4 a 1083,9 s) [FATO, `02-provas.md`].
  - A linha do Dentista B já agendada: "Se a sua técnica faz outro dentista perguntar 'como você fez isso?', ela já é um segundo produto." [FATO, `listPosts`, legenda do Dentista B].
- Cuidado: o serviço do Bruno é comando de lançamento [FATO, base de conhecimento 3.1]. A virada não pode prometer que todo serviço vira curso; o texto seguro é a pergunta da técnica que o colega quer aprender. Promessa de resultado: nenhuma.

**Variação da O1, sem virar objeção nova:** "Você virou estrategista de lançamento agora?" A bio atual ainda diz "Estrategista Digital" e o reposicionamento é de 29/07/2026 [FATO, `ig_account_stats` e base de conhecimento]. Prova: "em 2015 já estava no digital" (J6) e os 20 anos na noite, com os limites da tabela acima.

### 9.4 Conflitos entre os arquivos de objeção, para o conselho resolver
1. **O10 "Minha audiência é pequena".** O `01-objecoes.md` usa o caso "100 mil seguidores, 14 vendas" (deck do BNI). O `02-provas.md` diz que não há prova para essa objeção e manda não inventar caso. A base de conhecimento mostra que o caso está no deck com a linha "Isso aconteceu de verdade. O dono achava que o problema era o preço." e que saiu 4 vezes [FATO, `conhecimento-o-estrategista.md`]. Cliente, ano e papel do Bruno no caso: sem dado. Até o Bruno confirmar, fica como relato dele, sem número na tela.
2. **ETAPAS no `03-plano`.** Os dois stories que dizem "a resposta cai na automação ETAPAS" estão errados como a automação está hoje (seção 7).
3. **Percentual na O6.** O `03-plano` já pede para o Bruno confirmar se todo contrato tem parte variável; a base de conhecimento mostra duas propostas, uma com 20% e outra com 5% de success fee [FATO, base 3.1]. Sem confirmação, o story de sex 30/10 17h30 usa a versão condicional que o próprio `03-plano` propõe.

---

## 10. Como ler stories no Módulo 7

- **Janela:** o Buzzfy só lê story enquanto está no ar e com 5 viewers ou mais [FATO, nota do `ig_post_stats`]. Story não tem mediana na ferramenta.
- **Leitura de hoje:** os 9 stories de 24/10 expiram entre dom 25/10 09h33 e 20h30. Uma leitura no domingo às 09h20 pega os 9 (os da noite com cerca de 13 h). Uma segunda às 13h50 completa os 8 do PostZen. Ids: `ig_posts` kind=stories na hora.
- **Por story:** alcance, views, respostas, avançar, deslizar, sair, visitas ao perfil, seguidores.
- **Por bloco (métrica nossa):** retenção do bloco = views do último story do bloco / views do primeiro. Saída do story = (sair + deslizar) / views.
- **Por dia e semana:** views de story e respostas por `ig_account_stats` de 7 dias, toda segunda.
- **Fora do Buzzfy (à mão, pelo Bruno):** votos de enquete, respostas de caixa, toques no link, mensagens de WhatsApp com nota do Tabuleiro (dizem a profissão quando o link tem `&p=`).
- **Automação:** `listCommentAutomationLogs` da ETAPAS de story e da TABULEIRO toda segunda.
- **Registro:** `conteudo/stories-objecoes/02-medicao.md` (já previsto no `01-objecoes.md`, ainda não existe) e a rodada em `sistema-instagram/semanas/`.

---

## 11. Lacunas

- Quantos stories saíram por dia antes de hoje e quanto cada um teve: sem dado (expiraram; só 5 ficaram no PostZen).
- Nenhuma leitura de story com o Bruno em cena ainda: o st01 tinha 0 h na leitura. Os 8 de hoje precisam ser lidos antes de expirar.
- Votos de enquete, respostas de caixa e toques em link de story: nenhuma ferramenta permitida lê. Contagem manual do Bruno.
- Texto de comentário e de direct: fora da lista de ferramentas desta rodada. Frequência de objeção: sem dado.
- Analytics do site (o `o=ig-stories` só chega lá; a página tem Google Tag Manager): sem ferramenta permitida, sem dado.
- Mensagens de WhatsApp com nota do Tabuleiro e diagnósticos agendados: só o Bruno sabe. Sem dado.
- Estado e views dos destaques no perfil: sem dado. Capa PROVA: não existe. Arquivo dos "5 Lances em 5 stories": sem dado.
- Tempo de resposta do Bruno ao direct: sem dado. Decide se "responde com a sua área" é viável.
- Trecho 1160,4 a 1165,0 s ("estratégia da divulgação das festas"): ouvir antes de usar.
- Caso "100 mil seguidores, 14 vendas": cliente, ano e papel do Bruno sem dado.
- Fontes externas sobre frequência: uma de 2021 por paráfrase e uma de marcas em 2025 com duas amostras não conciliadas. Nenhuma sobre conta de expert brasileiro pequena.
- A Central de Ajuda do Instagram sobre destaques não abriu na busca; o que está dito sobre arquivo e montagem de destaque vem de guias de terceiros.
