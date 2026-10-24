# F8 · Do conteúdo ao diagnóstico de 30 minutos · rodada de 24/10/2026

Frente F8 (funil-diagnostico) da pesquisa do conselho Agência Reunida para @o_estrategista.com.br. Leituras ao vivo, somente leitura, entre 14h05 e 14h25 de sábado 24/10/2026 (horário de São Paulo). Nada foi publicado, agendado, alterado ou enviado no Instagram, no Buzzfy, no PostZen ou no site. Nenhum formulário foi enviado e nenhum teste foi respondido: as páginas foram baixadas com GET e lidas no código.

Etiquetas: [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha uma objeção sozinho. Métrica que falta: "sem dado".

---

## 0. Consultas feitas (todas responderam; nenhum erro de consulta)

| # | Fonte | Consulta e parâmetros | Resultado |
|---|---|---|---|
| 1 | PostZen `listCommentAutomations` | accountId j97772ycndetk3f1wcdbh14p898g4b8w | 17 automações, todas com isActive true |
| 2 | PostZen `listCommentAutomationLogs` | uma chamada por automação, as 17, limit 50 | 16 com total 0; CHECKLIST com total 1 |
| 3 | PostZen `listPosts` | mesma conta, limit 100, sortBy scheduledFor | 36 posts: 22 publicados (12/10 a 24/10) e 14 agendados (24/10 a 30/10) |
| 4 | Buzzfy `ig_account_stats` | 30 dias (24/09 17h17 a 24/10 17h17 UTC) | ok |
| 5 | Buzzfy `ig_account_stats` | 7 dias (17/10 a 24/10) | ok |
| 6 | Buzzfy `ig_posts` | since 2026-09-24, limit 50 | 35 itens |
| 7 | Buzzfy `ig_post_stats` | Dentista A, carrossel Checklist, reel Médico, carrossel Saga 7, 2 stories de hoje | ok; os 2 stories com dado provisório (menos de 1 h no ar) |
| 8 | Buzzfy `ig_post_stats` | "Ele nunca fez um anúncio", "90%", "Problema de equipe" | ok |
| 9 | Site (GET, sem envio) | `/tabuleiro/?o=ig-tabuleiro`, `/v2/`, `/?o=ig-case`, `/primeiro-lance/`, `/lancamento-para-dentistas/`, `js/tabuleiro.js`, `js/main.js` | todos 200 |
| 10 | Site de materiais (GET, sem envio) | `estrategista-materiais-videon8ns-projects.vercel.app/m/checklist?o=ig-checklist` | 200 |

Não usei ferramenta fora da lista permitida (nada de `ig_comments`, `ig_inbox` ou `getCommentAutomation`). Quando cito o direct, a fonte é o arquivo de outra frente que leu o `ig_inbox`.

---

## 1. Resumo

1. [FATO, `listCommentAutomations`] 17 automações ativas com 15 palavras diferentes. Só 3 levam a diagnóstico (TABULEIRO, CASE, ESTRATEGISTA). As outras 14 levam a PDF ou material com formulário de 9 campos. 6 valem para a conta toda: 5 de comentário (CASE, ESTRATEGISTA, ETAPAS, FUNIL, CAIXA) e 1 de resposta de story (ETAPAS).
2. [FATO, logs das 17] Um disparo em todas as automações somadas: CHECKLIST, comentário "Checklist" no carrossel de 12/10, do perfil `bruno26111982`, com direct e resposta pública enviados. [HIPÓTESE] É teste do próprio Bruno. Se for, a conta tem 0 lead real vindo de automação.
3. [FATO] TABULEIRO tem 0 log e está ligada só ao reel Dentista B, agendado para hoje às 21h e ainda não publicado. Há precedente de que a ligação por post do PostZen funciona depois da publicação: a CHECKLIST também foi ligada pelo id do PostZen e o log dela traz o id do Instagram do carrossel (18010053242992517).
4. [FATO, `ig_account_stats`] 30 dias: 447 visitas ao perfil, 7 cliques no site (1,6%), 0 toque em botão de link, 14 comentários. Últimos 7 dias, sem anúncio: 74 visitas, 0 clique, 2 comentários.
5. [FATO, `ig_posts` e `ig_post_stats`] 19 peças pediram palavra-chave e renderam 3 comentários. Os 4 reels com o Bruno em cena somam 771 de alcance e 5 comentários. O Dentista A (169 de alcance, pedido "comenta aqui que eu te respondo") teve 0 comentário.
6. [FATO, site] O link da bio vai para `/v2/` ("A Partida", versão cinema). Os 6 botões dessa página abrem o WhatsApp com a mensagem padrão e não passam pelo Tabuleiro. CASE e ESTRATEGISTA mandam para a página inicial, embora o direct diga "agenda um diagnóstico". Só a TABULEIRO leva ao teste de 12 casas.
7. [FATO, `js/tabuleiro.js`] O teste termina num botão de WhatsApp com mensagem pronta (nota, gargalo e profissão, esta só quando o link traz `&p=`). A origem (`o=ig-...`) não entra na mensagem. O agendamento acontece na conversa do WhatsApp; o site não tem agenda on-line.
8. [FATO] Rastreio de clique do PostZen desligado nas 17 automações (linkTracking false). O site tem o contêiner GTM-W2LS6RKN com os eventos `tabuleiro_start`, `tabuleiro_complete` e `generate_lead`, mas nenhuma ferramenta permitida aos agentes lê esses números. Do clique no botão em diante, tudo é sem dado para nós.
9. [ESTIMATIVA] O caminho da bio, sozinho, não chega a 10 diagnósticos por mês: no ritmo orgânico dos últimos 7 dias são cerca de 317 visitas e 5 cliques por mês. Mesmo que todo clique virasse diagnóstico, seriam 5. Pelo comentário, com até 5 posts TABULEIRO até 22/11 a 169 de alcance e 0,65 comentário por 100 contas, o teto fica em cerca de 5,5 comentários de qualquer tipo. A meta D6 de 5 disparos de TABULEIRO até 22/11 exige que quase todo comentário seja a palavra.
10. [FATO mais HIPÓTESE] Riscos nas peças já agendadas: "caso" é palavra da automação CASE, que vale para a conta toda, e o CI01 (qua 28/10) pede resposta aberta; o PO01 (qui 29/10) pede "Comenta a palavra" sem automação; o CAR01 (ter 27/10) faz dois pedidos na mesma legenda.

---

## 2. Mapa das 17 automações [FATO, `listCommentAutomations` e `listCommentAutomationLogs`, 24/10]

Todas: ativas, plataforma Instagram, público "any" (seguidor ou não), direct sem atraso (e resposta pública sem atraso nas 16 de comentário), linkTracking false, alsoMatchInDms false (palavra digitada no direct não dispara nada), matchMode "word" (palavra inteira).

| # | Nome no PostZen | Gatilho | Palavras | Onde vale | Botão leva a | Tipo de destino | Disparos (stats / log) |
|---|---|---|---|---|---|---|---|
| 1 | TABULEIRO · Reel Dentista B (palavra do mês) | comentário | tabuleiro, tabuleiros (tolera erro) | só o Dentista B (postId m170mzbzy38d7td2vhggm4v2dx8gx767, agendado 24/10 21h) | `/tabuleiro/?o=ig-tabuleiro` | teste de 12 casas, depois WhatsApp | 0 / 0 |
| 2 | ETAPAS · resposta de Story (conta toda) | resposta de story | etapas, etapa | todo story | `.../m/checklist?o=ig-story-etapas` | PDF com formulário | 0 / 0 |
| 3 | CASE · diagnóstico (conta toda, sem citar cliente) | comentário | case, caso (sem tolerância a erro) | todo post | `/?o=ig-case` (página inicial) | página inicial, depois WhatsApp | 0 / 0 |
| 4 | ESTRATEGISTA · série 2 (conta toda) | comentário | estrategista | todo post | `/?o=ig-estrategista` (página inicial) | página inicial, depois WhatsApp | 0 / 0 |
| 5 | ETAPAS · série 2 (conta toda) | comentário | etapas, etapa | todo post | `.../m/checklist?o=ig-etapas` | PDF com formulário | 0 / 0 |
| 6 | FUNIL · série 2 (conta toda) | comentário | funil | todo post | `.../m/checklist?o=ig-funil` | PDF com formulário | 0 / 0 |
| 7 | CAIXA · série 2 (conta toda) | comentário | caixa | todo post | `.../m/recuperacao?o=ig-caixa` | PDF com formulário | 0 / 0 |
| 8 | ETAPAS · Reels Escala 7x7 | comentário | etapas, etapa | um post (postId m1748g817gjwzraqn6wa67h3a18ghjqf, que não aparece entre os 36 posts do `listPosts`) | `.../m/checklist?o=ig-etapas` | PDF com formulário | 0 / 0 |
| 9 | RECUPERAÇÃO · Reels 07 | comentário | recuperação, recuperacao, recuperaçao, recuperar | reel de 13/10 | `.../m/recuperacao?o=ig-recuperacao` | PDF com formulário | 0 / 0 |
| 10 | PERPÉTUO · Reels 08 | comentário | perpétuo, perpetuo, perpetua, perpétua | reel de 14/10 | `.../m/perpetuo?o=ig-perpetuo` | material com formulário | 0 / 0 |
| 11 | CARRINHO · Reels 06 | comentário | carrinho, carrinhos | reel de 13/10 | `.../m/carrinho?o=ig-carrinho` | material com formulário | 0 / 0 |
| 12 | EVENTO · Reels 05 | comentário | evento, eventos | reel de 13/10 | `.../m/evento?o=ig-evento` | material com formulário | 0 / 0 |
| 13 | PESQUISA · Reels 01 | comentário | pesquisa, pesquisar | reel de 11/10 (ligado pelo id do Instagram 18091659392202122; o reel não está no `listPosts`) | `.../m/pesquisa?o=ig-pesquisa` | material com formulário | 0 / 0 |
| 14 | AQUECIMENTO · Reels 04 | comentário | aquecimento, aquecer | reel de 12/10 | `.../m/aquecimento?o=ig-aquecimento` | material com formulário | 0 / 0 |
| 15 | CAPTAÇÃO · Reels 03 | comentário | captação, captacao, captaçao | reel de 12/10 | `.../m/captacao?o=ig-captacao` | material com formulário | 0 / 0 |
| 16 | OFERTA · Reels 02 | comentário | oferta, ofertas | reel de 12/10 | `.../m/oferta?o=ig-oferta` | material com formulário | 0 / 0 |
| 17 | CHECKLIST · carrossel 10 perguntas | comentário | checklist, check list, checklis | carrossel de 12/10 | `.../m/checklist?o=ig-checklist` | PDF com formulário | 1 / 1 |

Leitura:
- [FATO] 15 palavras de comentário ou story ativas ao mesmo tempo, contra a regra de uma por mês (CLAUDE.md) e contra o PARAR de 21/10 ("12 palavras-chave diferentes", 00-SISTEMA, Módulo 7).
- [FATO] O texto do direct da TABULEIRO diz que o teste mostra "em qual etapa o seu lançamento trava: pesquisa, oferta, aquecimento ou carrinho". A página mostra o gargalo em um dos 5 Lances (Abertura, Gambito, Meio-Jogo, Xeque-Mate, Promoção) [FATO, `js/tabuleiro.js`]. A promessa do direct e o que a página entrega usam mapas diferentes.
- [FATO] O direct da TABULEIRO fala de "agenda cheia" e de "transformar a técnica num segundo produto": é texto de dentista. Serve para o Dentista B e não serve para um post de outro tema em novembro.
- [FATO, página de material] O formulário dos materiais pede 9 campos (nome, WhatsApp, e-mail, Instagram, profissão, seguidores, se já lançou, quando pensa em lançar, maior dificuldade) mais o aceite. O site de materiais está num endereço `*.vercel.app`, fora do domínio da marca. [PRIOR] Endereço fora da marca pesa contra a confiança de quem chega frio.

---

## 3. O que disparou

- [FATO, `listCommentAutomationLogs` da CHECKLIST] Um registro: comentário "Checklist" (commentId 18093530426454537), autor `bruno26111982`, no post 18010053242992517 (carrossel "10 perguntas antes de abrir o carrinho", 12/10 06h); resposta pública com status "sent"; direct com status "sent", botões mantidos (buttonsDropped false). O registro não traz data nem hora.
- [FATO, `ig_post_stats`] O carrossel tem 34 de alcance, 2 comentários, 0 visita ao perfil e 0 seguidor.
- [HIPÓTESE] Os 2 comentários são o "Checklist" e a resposta pública automática da conta ("Te mandei no direct..."), já que a contagem do Instagram pode incluir a resposta do dono. Ler os comentários exige `ig_comments`, fora da lista permitida: sem dado.
- [HIPÓTESE] O autor é o próprio Bruno testando (o nome de usuário começa com "bruno"). Quem confirma: o Bruno.
- [FATO, `ig_posts`] Três peças pediram palavra que não tinha automação: Saga 7 (carrossel de 09/10, "Comenta TABULEIRO que eu te mando o diagnóstico gratuito", 71 de alcance, 0 comentário), Médico (reel de 30/09, "Comenta AGENDA", 64 de alcance, 1 comentário) e "Cem mil seguidores" (reel de 01/10, "Comenta o número da sua casa", 0 comentário). Quem comentou não recebeu nada automático.
- [FATO, `stories-objecoes/01-objecoes.md`, leitura do `ig_inbox` de 12 a 24/10] Nas 50 conversas mais recentes do direct, nenhuma conversa comercial e nenhuma pergunta de preço, prazo ou método.

---

## 4. O caminho hoje, etapa por etapa

### 4.1 As portas que existem

| Porta | Caminho | Origem que chega ao Bruno | Estado |
|---|---|---|---|
| A. Comentário TABULEIRO | comentário no Dentista B, resposta pública, direct com botão "Fazer o diagnóstico", `/tabuleiro/?o=ig-tabuleiro`, 12 perguntas, resultado, botão "Levar meu tabuleiro pro diagnóstico (abre o WhatsApp)", conversa, horário combinado à mão, diagnóstico de 30 min | Mensagem "Fiz O Tabuleiro no site. Deu N de 12 casas de pé e o gargalo caiu no Lance X..." sem a origem e, sem `&p=`, sem a profissão [FATO, `js/tabuleiro.js`] | abre hoje 21h; 0 log |
| B. Comentário CASE ou ESTRATEGISTA | comentário com "case", "caso" ou "estrategista" em qualquer post, direct, página inicial (texto longo, 35 KB de HTML), botão de WhatsApp com mensagem padrão | "Quero agendar o Primeiro Lance (diagnóstico de lançamento)." [FATO, `js/main.js` e HTML] | ativa; 0 log |
| C. Link da bio | perfil, `/v2/`, um dos 6 botões "Agendar o Primeiro Lance", WhatsApp com mensagem padrão | mesma mensagem padrão; o Bruno não separa bio de Google | 7 cliques em 30 dias, 0 em 7 dias |
| D. Link em story | sticker para `/tabuleiro/?o=ig-stories` (plano de stories, postado à mão) e daí igual à porta A | igual à A; o `o` some | depende do plano de stories (F6) |
| E. Palavra de material | comentário com palavra de material, direct, página na vercel, formulário de 9 campos, PDF, grupo de WhatsApp e, no 3º passo, o Tabuleiro [FATO, F6 seção 7] | sem dado (o formulário vai para um destino que não conferi) | 1 disparo, possivelmente teste |
| F. Direct à mão | resposta de story sem "etapa", direct espontâneo, comentário de profissão | o que a pessoa escrever | 0 conversa comercial em 50 [FATO, 01-objecoes] |

### 4.2 Números por etapa

| Etapa | 30 dias (24/09 a 24/10) | 7 dias (17 a 24/10) | Fonte |
|---|---|---|---|
| Alcance | 3.216 contas, 1.907 de anúncio | 571 contas, 0 de anúncio | [FATO, `ig_account_stats`] |
| Comentários | 14 | 2 | [FATO, `ig_account_stats`] |
| Visitas ao perfil | 447 | 74 | [FATO, `ig_account_stats`] |
| Cliques no site (link da bio) | 7 (1,6% das visitas) | 0 | [FATO, `ig_account_stats`] |
| Toques em botão de link | 0 | 0 | [FATO, `ig_account_stats`] |
| Disparos de automação | 1 (CHECKLIST, possível teste) | sem dado por período (o log não traz data) | [FATO, logs] |
| Cliques no botão do direct | sem dado (linkTracking false) | sem dado | [FATO, `listCommentAutomations`] |
| Tabuleiro iniciado e concluído | sem dado para os agentes (eventos existem no GTM) | sem dado | [FATO, `js/tabuleiro.js`] |
| Mensagens no WhatsApp | sem dado | sem dado | só o Bruno vê |
| Diagnósticos de 30 min agendados | sem dado | sem dado | só o Bruno sabe |
| Diagnósticos realizados | sem dado | sem dado | só o Bruno sabe |
| Vendas | 0 | 0 | [FATO, contexto.md] |

### 4.3 Onde o caminho quebra (do mais pesado ao mais leve)

1. **Topo: pouca gente vê e quase ninguém comenta.** [FATO] 571 contas em 7 dias sem anúncio, 2 comentários. [FATO, `ig_posts` e `ig_post_stats`] Os 4 reels com o Bruno são os únicos com comentário em volume: 308 de alcance e 3 comentários ("Ele nunca fez um anúncio"), 166 e 2 ("90%"), 128 e 0 ("Problema de equipe"), 169 e 0 (Dentista A). Nenhuma automação conserta isso: ela só age depois do comentário.
2. **Pedido de comentário onde não havia alcance.** [FATO, F1 seção 4.4 conferida com `ig_posts`] 19 peças pediram palavra-chave, com mediana de 34 de alcance, e renderam 3 comentários. A regra dos 150 (CLAUDE.md) existe por causa disso.
3. **A bio não leva ao teste.** [FATO, `ig_account_stats` e site] O link é `/v2/`, uma página de "versão cinema" que abre com "carregando a partida..." e manda para o WhatsApp com a mensagem padrão. O Módulo 2 do 00-SISTEMA pediu `/tabuleiro/?o=ig-bio` com o texto "Faça o diagnóstico de 12 casas"; não foi aplicado (a bio segue "Estrategista Digital / Ide e pregai o evangelho! / Visitor Host @bnisyrius / Dev @dashpronow"). Dos 447 que visitaram o perfil, 7 clicaram. Nos últimos 7 dias, 74 e 0.
4. **Palavras demais, e de uso comum.** [FATO] 15 palavras ativas, 5 de comentário valendo para a conta toda. "Caso", "caixa", "funil" e "etapa" são palavras do dia a dia. [HIPÓTESE] Comentário como "no meu caso foi assim" num reel da TV dispara o direct da CASE oferecendo diagnóstico a quem só deu opinião, e isso mistura a contagem de leads. Não testei (seria escrever na conta).
5. **Destino errado em 2 das 3 automações de diagnóstico.** [FATO] CASE e ESTRATEGISTA dizem "toca no botão e agenda um diagnóstico gratuito de 30 minutos", e o botão abre a página inicial, um texto longo em que o agendamento é um botão de WhatsApp. Não há agenda on-line em nenhuma página aberta [FATO, links de `/`, `/v2/`, `/primeiro-lance/`, `/tabuleiro/`].
6. **"Diagnóstico" quer dizer duas coisas.** [FATO] O site chama de diagnóstico o teste de 12 casas ("Teste de Lançamento Grátis: diagnóstico em 12 casas", 4 minutos, sem cadastro) e também a conversa de 30 minutos ("O Primeiro Lance", por videochamada ou WhatsApp). A legenda do Dentista B promete "o diagnóstico de 12 casas"; a meta do sistema é "10 diagnósticos por mês" com a porta "diagnóstico gratuito de 30 min" [FATO, 00-SISTEMA, ficha]. A Projeção do 00-SISTEMA soma as duas coisas: "2% de clique no Tabuleiro, são 9 diagnósticos feitos por mês". Sem separar, a contagem da meta fica ambígua.
7. **A origem se perde e ninguém conta.** [FATO] O `o=ig-...` entra na página, mas a mensagem de WhatsApp não leva a origem, e o evento `tabuleiro_complete` grava só o caminho da página (`location.pathname`), sem o parâmetro. Se o GA4 do contêiner guarda o endereço completo da página: sem dado. O PostZen não conta o clique no botão (linkTracking false). O único passo que os agentes leem depois do comentário é o log de disparo.
8. **Do WhatsApp à venda, nada registrado.** [FATO, 00-SISTEMA, Módulo 6] Existem 3 perguntas de qualificação e um follow-up de +1, +4 e +10 dias, escritos. Se foram usados com alguém: sem dado. Vendas: 0. Diagnósticos realizados no mês: sem dado.

---

## 5. Contas que limitam o plano

Todas são [ESTIMATIVA], com a conta e a premissa ao lado.

**5.1 Taxa de comentário.**
- Conta toda: 14 comentários sobre 3.216 contas alcançadas = 0,44 por 100 contas. Premissa: alcance de anúncio incluído; comentário do próprio dono pode estar contado.
- Reels com o Bruno: 5 comentários sobre 771 contas (308 + 166 + 128 + 169) = 0,65 por 100 contas. Premissa: esses 4 pediram "salva", "responde aqui", "marca aqui" ou "comenta aqui", nenhum pediu palavra-chave.

**5.2 Teto do caminho da bio.**
- Ritmo orgânico: 74 visitas em 7 dias × 30 / 7 = cerca de 317 visitas por mês. Com 1,6% de clique (7 de 447), cerca de 5 cliques por mês.
- Para 10 diagnósticos com 1,6% de clique e 100% de conversão depois do clique (premissa impossível, usada só como piso): 10 / 0,016 = 625 visitas por mês, o dobro do ritmo atual.
- Leitura: trocar o link da bio de `/v2/` para o Tabuleiro mexe na taxa de clique, que hoje é a parte medida; não mexe no volume de visitas.

**5.3 Teto de disparos de TABULEIRO até 22/11.**
- Máximo de posts com a palavra: o Dentista B (24/10) mais 1 por semana em novembro dentro da janela (01 a 07/11, 08 a 14/11, 15 a 21/11 e o domingo 22/11 se cair numa semana nova) = 4 a 5 posts. Regra "no máximo 1 palavra-chave por semana, sempre a mesma no mês" [FATO, 00-SISTEMA, Módulo 1, item 4].
- Com 5 posts a 169 de alcance (o nível do Dentista A) e 0,65 comentário por 100 contas: 5 × 169 × 0,0065 = 5,5 comentários de qualquer tipo. Com 0,44: 3,7.
- Comparação: a D6 do enquadramento pede 5 ou mais disparos de TABULEIRO até 22/11. Pela conta, só acontece se cada post TABULEIRO ficar no nível do Dentista A e quase todo comentário for a palavra. A conta mostra o teto otimista; a previsão realista fica abaixo dele.
- Diagnósticos: a previsão registrada em 21/10 é 1 agendado até 18/11, faixa de 0 a 3, probabilidade 0,2 [FATO, 00-enquadramento, D6]. Não há taxa medida de disparo para clique, de clique para WhatsApp nem de WhatsApp para agendamento. Qualquer número aqui seria [PRIOR].

**5.4 Tempo do Bruno.**
- 10 diagnósticos × 30 minutos = 5 horas por mês só de conversa, sem contar o WhatsApp antes e depois. Respostas à mão em comentário de profissão: tempo por resposta sem dado.

---

## 6. Peças já agendadas (24 a 30/10): pedidos e colisões

Fonte das legendas e horários: [FATO, `listPosts`, 24/10]. Fonte das palavras: seção 2. As sugestões são do Bruno decidir; nenhum agente mexe no PostZen.

| Quando | Peça | Pedido na legenda ou na fala | Automação que pode disparar | Risco | Sugestão |
|---|---|---|---|---|---|
| sáb 24/10 21h | Reel Dentista B | Legenda: "Comenta TABULEIRO que eu te mando o diagnóstico de 12 casas." Fala de 32,0 a 35,3 s: "Dentista, comenta a sua profissão aqui que eu te respondo." [FATO, `videos/nichos/dentista/words.json`; o B usa a mesma gravação do A, contexto.md] | TABULEIRO (só neste post). CASE se o comentário tiver "caso" | Dois pedidos. Quem comenta "dentista" não recebe nada automático; o Bruno precisa responder à mão. [HIPÓTESE] Comentário com "tabuleiro" e "caso" juntos: qual automação responde é sem dado (o Instagram permite uma resposta privada por comentário) | Antes das 21h: pôr `&p=dentista` no botão da TABULEIRO, para a mensagem do WhatsApp dizer "Sou dentista" [FATO: `tabuleiro.js` aceita `p=dentista`]. Responder à mão todo comentário de profissão no mesmo dia (texto na seção 8) |
| dom 25/10 18h30 | Reel tl01 | "Comenta o número do assunto que você quer ver inteiro." | nenhuma (números não disparam) | baixo para o funil (a promessa "o mais votado sai no próximo sábado" é de outra frente) | manter o pedido de número; nada de palavra |
| seg 26/10 21h | Reel pb01 | "Manda para um expert que vai lançar este ano." | nenhuma | nenhum | manter |
| ter 27/10 12h | Carrossel car01 | "Comenta o número." e "Vai lançar nos próximos 90 dias? Me manda a data no direct." | nenhuma | dois pedidos na mesma legenda (regra S6 do F2: um pedido por legenda) | ficar com um. Se o objetivo é lead, ficar com o direct |
| ter 27/10 16h | Story pf01 | sem texto | ETAPAS de story só se a resposta tiver "etapa" | baixo | nenhuma |
| qua 28/10 21h | Reel ci01 | "E você, o que teria respondido?" (o tema é cliente que "chega machucado") | CASE ("caso"), CAIXA, FUNIL, ETAPAS, ESTRATEGISTA, todas de conta toda | [HIPÓTESE] alto: resposta aberta sobre experiência ruim usa "no meu caso" com naturalidade e recebe o direct de diagnóstico | desligar a CASE (ou tirar "caso") antes de 28/10 21h; resposta à mão |
| qui 29/10 21h | Reel po01 | "Qual dessas peças falta no seu lançamento? Comenta a palavra." e "Salva para conferir antes do próximo lançamento." | nenhuma (gatilho, jogada, posicionamento e momento não são palavras de automação) | dois pedidos; "comenta a palavra" parece palavra-chave sem automação, e quem comentar espera resposta | trocar para pergunta aberta ("Qual peça falta no seu?") ou só "Salva"; se ficar, resposta à mão |
| sex 30/10 21h | Reel pb02 | "Vai lançar nos próximos 90 dias? Me manda a data no direct." | nenhuma | nenhum; é o modelo de chamada para o direct sem promessa | manter |

[FATO] Nenhuma das peças de 25 a 30/10 pede TABULEIRO, o que bate com a regra: nenhuma é do mesmo modelo do Dentista A (letreiro, Bruno falando) nem vem de um anterior do mesmo formato com 150 em 48 h.

---

## 7. Como o cronograma encaixa a TABULEIRO

**R1. Uma palavra, a mesma em outubro e novembro: TABULEIRO.** [FATO, CLAUDE.md: "Uma palavra-chave por mês (TABULEIRO)"]. As outras 14 palavras saem de circulação nas legendas, e as 5 de comentário que valem para a conta toda (CASE, ESTRATEGISTA, ETAPAS, FUNIL, CAIXA) são desligadas pelo Bruno antes do CI01 (qua 28/10 21h). Cada automação tem o campo isActive [FATO, `listCommentAutomations`]; desligar em vez de apagar guarda a configuração para voltar atrás [HIPÓTESE sobre o comportamento do PostZen]. As 10 ligadas a posts antigos podem ficar ou ser desligadas para limpar a contagem: esses posts têm 0 comentário, menos o Checklist com 2 [FATO, `ig_posts`]; alcance novo deles: sem dado.

**R2. No máximo um post TABULEIRO por semana** [FATO, 00-SISTEMA, Módulo 1, item 4].

**R3. Condição dos 150, lida em 48 h reais.** Duas leituras possíveis da regra "só em post com alcance de 150 ou mais":
- (a) Antecipada, que é o precedente de 21/10 [FATO, semanas/2026-10-21.md]: o post seguinte do mesmo formato recebe a palavra quando o anterior passou de 150 em 48 h. O Dentista B recebeu por causa do Dentista A (169).
- (b) Retroativa [HIPÓTESE]: o post sai com pergunta aberta; se passar de 150 em 48 h, o Bruno cria a automação ligada a ele e deixa um comentário próprio fixado com o pedido TABULEIRO. Cumpre a regra ao pé da letra, mas pega o post já na fase em que entra pouco comentário novo (sem dado sobre a curva de comentários da conta).
- Para o cronograma, ficar com (a) e registrar (b) como teste se nenhum post de novembro se qualificar por (a).

**R4. Qual post de novembro.** O primeiro reel com o Bruno falando para a câmera, no mesmo modelo de um anterior que passou de 150 em 48 h. Candidatos pela leitura de hoje: um reel de nicho no Modelo A (letreiro), se o Bruno gravar com o teleprompter; ou o remake de "Ele nunca fez um anúncio" (308 de alcance, Bruno em cena) com o Bruno gravando de novo. O Dentista B só abre caminho para o Modelo B (tela dividida) se ele mesmo passar de 150 em 48 h (leitura na seg 26/10 às 21h). Peças da TV, timelapses e estáticos não recebem a palavra.

**R5. Uma automação nova por post TABULEIRO, criada pelo Bruno.** A atual está presa ao Dentista B e o texto do direct é de dentista. Para cada post novo: palavra "tabuleiro", botão para `/tabuleiro/?o=ig-tab-AAMMDD` (um `o` por post) e `&p=<profissão>` quando o post for de nicho. Texto do direct na seção 8, sem citar "4 etapas" (a página mostra 5 Lances).

**R6. Abaixo de 150, sem palavra.** Pedido de seguir, salvar, enviar, pergunta aberta ou chamada para o direct (seção 8), com resposta à mão. É a "porta dupla" escolhida em 21/10 [FATO, `modo-god-nichos/run/10-decision-brief.md`, D3]. A decisão escrita do Bruno sobre se "comenta a sua profissão" conta como segunda palavra tinha prazo em 24/10: sem dado.

**R7. Um pedido por legenda.** Se a peça pede TABULEIRO, não pede salvar nem direct. Se pede direct, não pede número.

**R8. Stories carregam o link, não a palavra.** A TABULEIRO não dispara em resposta de story [FATO, gatilho "comment"]. O pedido diário do plano de stories é o link `/tabuleiro/?o=ig-stories` (F6 e `stories-objecoes/03-plano-7-dias.md`). Os dois stories que dizem que a resposta "cai na automação ETAPAS" estão errados como a automação está hoje [FATO, F6 seção 7].

**Encaixe por semana (só a parte do funil; a grade completa é de outras frentes).**

| Semana | Post com TABULEIRO | Condição | Chamada nas outras peças | Leitura |
|---|---|---|---|---|
| sáb 24/10 | Dentista B, 21h | precedente do Dentista A (169) | stories do dia sem palavra | seg 26/10 21h: alcance, pulo, comentários e logs da TABULEIRO |
| 25 a 31/10 | nenhum | nenhuma peça do mesmo modelo | número (tl01), enviar (pb01), direct (car01, pb02), pergunta aberta (ci01, po01) com resposta à mão | Módulo 7 de seg 02/11 |
| 01 a 07/11 | até 1 | reel do Bruno no modelo de um anterior com 150 em 48 h (Modelo A, ou Modelo B se o Dentista B passar de 150) | direct e pergunta aberta | 48 h depois do post e seg 09/11 |
| 08 a 14/11 | até 1 | mesma regra | idem | 48 h depois e seg 16/11 |
| 15 a 21/11 | até 1 | mesma regra | idem | 48 h depois e seg 23/11 |
| dom 22/11 | 0 ou 1 | mesma regra, se cair numa semana sem TABULEIRO | idem | seg 23/11 |

Se nenhum reel de novembro se qualificar, a palavra fica sem post no mês. Pôr TABULEIRO num post sem a condição para "não perder o mês" vai contra a regra e contra o dado da seção 4.3, item 2.

---

## 8. Chamadas para o direct sem promessa de resultado

Critério de texto (CLAUDE.md): sem promessa de resultado, sem travessão, sem emoji, no máximo uma "não é X, é Y" por peça. Nenhuma palavra digitada no direct dispara automação [FATO, alsoMatchInDms false nas 17], então pedir uma palavra no direct cria uma segunda palavra sem automação. As chamadas abaixo não pedem palavra.

**Na legenda (feed), uma por peça:**
1. "Vai lançar nos próximos 90 dias? Me manda a data no direct." (já em uso no pb02 e no car01)
2. "Quer olhar o seu lançamento comigo por 30 minutos? Me chama no direct."
3. "Me conta no direct qual é a sua área e quando pensa em lançar."
4. Em post TABULEIRO (só com a condição da R3): "Comenta TABULEIRO que eu te mando o teste de 12 casas." Variante do Módulo 6 que segue valendo: "Comenta TABULEIRO que eu te mostro em qual casa o seu lançamento trava." (é o que o teste entrega). Evitar a variante "o mesmo diagnóstico que fiz com a Tzur" enquanto a autorização da Tzur estiver pendente [FATO, F5].

**Em story:**
- Sticker de link para `/tabuleiro/?o=ig-stories` com o texto "Teste de 12 casas" (o texto bate com o destino).
- "Responde este story com a sua área." Só com resposta à mão; não dispara nada.

**Texto do direct para a automação TABULEIRO de novembro (proposta para o Bruno configurar):**
> Oi! Aqui é o Bruno. O Tabuleiro são 12 perguntas sobre o seu próximo lançamento, em 4 minutos e sem cadastro. No fim aparece a casa que está mais vazia. Toca no botão, responde e, se fizer sentido, me manda o resultado no WhatsApp que a gente marca 30 minutos.
> [Fazer o teste]

Base: "Diagnóstico em 4 minutos", "Nada de e-mail, nada de cadastro" e o botão que abre o WhatsApp [FATO, página `/tabuleiro/`].

**Resposta à mão para comentário de profissão (abaixo de 150 ou no Dentista B):**
- Pública: "Te mandei no direct."
- Privada (uma por comentário, permitida pelo Instagram): "Oi, aqui é o Bruno. Obrigado por comentar. Se quiser ver em qual casa o seu lançamento está mais vazio, são 12 perguntas: estrategistadelancamento.com.br/tabuleiro/?o=ig-manual&p=<profissão>. Se fizer sentido depois, me chama aqui que a gente marca 30 minutos."
- Profissões aceitas pelo `p`: medico, advogado, psicologo, nutricionista, dentista, consorcio [FATO, `js/tabuleiro.js`].

**Follow-up:** usar o do Módulo 6 (+1, +4 e +10 dias) só com quem respondeu. O de +10 dias fala em "4 horários de diagnóstico esta semana": só vale se for verdade naquela semana.

**Evitar (promessa de resultado ou pressão):** "que eu te mostro como vender X", "garantido", "você vai faturar", número de faturamento como promessa para quem lê, "vagas" sem número real de horários, e números de cliente sem autorização. O direct da ESTRATEGISTA ("Pra eu te mostrar onde o seu dinheiro está vazando") afirma um vazamento antes de ver o caso [PRIOR: tom de pressão; a regra do CLAUDE.md não proíbe de forma explícita]. Com a ESTRATEGISTA desligada (R1), o texto sai de circulação.

---

## 9. Como contar cada etapa (toda segunda, no Módulo 7)

| Etapa | Número | Quem lê | Fonte | Observação |
|---|---|---|---|---|
| 1. Alcance do post TABULEIRO em 48 h | contas | agente | `ig_post_stats` | condição dos 150 |
| 2. Comentários do post | total | agente | `ig_post_stats` | pode incluir a resposta pública automática da conta [HIPÓTESE, seção 3] |
| 3. Disparos e envios da TABULEIRO | total, sent, failed, skipped, gated | agente | `listCommentAutomationLogs` | o log não tem data: guardar o total de cada segunda e fazer a diferença; tirar contas de teste (lista de perfis de teste do Bruno) |
| 4. Clique no botão do direct | cliques | sem dado hoje | PostZen, se o Bruno ligar o linkTracking [HIPÓTESE: o PostZen passa a contar] | |
| 5. Teste iniciado e concluído | eventos `tabuleiro_start` e `tabuleiro_complete` | Bruno | GA4 ou GTM (fora das ferramentas dos agentes) | o evento grava o caminho, não o `o` |
| 6. Mensagens no WhatsApp | quantas começam com "Fiz O Tabuleiro no site" e quantas com "Quero agendar o Primeiro Lance" | Bruno | WhatsApp | as duas frases são fixas no código [FATO]; a primeira vem do teste, a segunda de qualquer outra página |
| 7. Diagnóstico de 30 min agendado | total | Bruno | agenda dele | contar separado do teste de 12 casas |
| 8. Diagnóstico realizado | total | Bruno | agenda dele | a meta de 10 por mês conta aqui |
| 9. Proposta e venda | total | Bruno | anotação dele | |

Registro: `conteudo/sistema-instagram/semanas/AAAA-MM-DD.md`, uma linha por etapa, com "sem dado" quando o Bruno não informar.

---

## 10. O que depende só do Bruno (nenhum agente mexe)

| # | Ação | Prazo | Por quê |
|---|---|---|---|
| 1 | Pôr `&p=dentista` no botão da TABULEIRO do Dentista B | hoje antes das 21h | a mensagem do WhatsApp passa a dizer a profissão |
| 2 | Responder à mão os comentários de profissão do Dentista B | no mesmo dia de cada comentário | a fala do vídeo promete "eu te respondo" |
| 3 | Dizer se `bruno26111982` é perfil dele e listar perfis de teste | até seg 26/10 | o único disparo do mês pode ser teste |
| 4 | Desligar CASE, ESTRATEGISTA, ETAPAS (comentário), FUNIL e CAIXA | antes de qua 28/10 21h (ci01) | colisão de palavra comum e regra de uma palavra |
| 5 | Decidir o que fazer com a ETAPAS de story (opções do F6, seção 7) | antes de dom 25/10 09h02 (primeiro story que cita a ETAPAS) | o plano de stories conta com ela para a resposta de área |
| 6 | Trocar o link da bio de `/v2/` para `/tabuleiro/?o=ig-bio` (Módulo 2) | quando decidir; é a única troca que mexe na etapa medida (1,6% de clique) | a bio hoje não passa pelo teste |
| 7 | Ajustar car01 (um pedido) e po01 ("comenta a palavra") | antes de ter 27/10 12h e qui 29/10 21h | seção 6 |
| 8 | Informar toda segunda as etapas 5 a 9 da seção 9 | toda segunda | sem isso a meta de 10 diagnósticos não é medida |
| 9 | Decisão escrita sobre "comenta a sua profissão" como segunda palavra | estava para 24/10 | D3 de 21/10 |
| 10 | Ligar o linkTracking nas automações que ficarem | quando quiser | conta o clique no botão do direct [HIPÓTESE sobre o que o PostZen mostra] |

---

## 11. Lacunas

- Quem é `bruno26111982` e se o único disparo é teste: sem dado.
- Texto dos 14 comentários do mês e quanto deles é resposta da própria conta: sem dado (`ig_comments` fora da lista permitida).
- Data e hora dos disparos: o log do PostZen não traz.
- Cliques no botão do direct: sem dado (linkTracking false).
- Visitas, testes iniciados e concluídos e cliques no WhatsApp do site: os eventos existem no GTM-W2LS6RKN, mas nenhuma ferramenta permitida lê. Se o GA4 está ligado ao contêiner: sem dado.
- Mensagens recebidas no WhatsApp, diagnósticos agendados e realizados no mês: sem dado (só o Bruno).
- Para onde vai o formulário das páginas de material e se alguém preencheu: sem dado (não enviei nada).
- Qual automação responde quando um comentário traz duas palavras ("tabuleiro" e "caso"): sem dado.
- Se o Instagram entrega o direct com botão para quem não segue a conta nesta conta: há 1 envio com botão mantido, de um perfil que pode ser do Bruno; sem dado para terceiros.
- O post ligado à ETAPAS Escala 7x7 (m1748g817gjwzraqn6wa67h3a18ghjqf) não aparece entre os 36 posts do `listPosts`; se a automação ainda aponta para o reel de 18/10: sem dado.
- Curva de comentários por hora depois da publicação (para a leitura retroativa da R3): sem dado.
- Tempo de carregamento da `/v2/` no celular: sem dado.

---

## 12. Fontes

- PostZen, 24/10/2026, entre 14h05 e 14h16: `listCommentAutomations` (accountId j97772ycndetk3f1wcdbh14p898g4b8w); `listCommentAutomationLogs` das 17 automações (ids na seção 2: TABULEIRO qs747t4bq23a1qpnjskexg34vs8gx7hx, CHECKLIST qs7de23c7nzxzw2k4yjshgm5gd8g5dmx, CASE qs79dctypcnz18m9wbeb7cg4en8gh8fm, ESTRATEGISTA qs7309wynnp8dgvy96k67nfj558ggz2r, ETAPAS story qs78ccqc3nf0axhc59frr8mewx8ghnvj, ETAPAS série 2 qs7e2jwpb31ezb4j5yhrc33pr58gg2fm, FUNIL qs71kgp5n4q612z8rsxm281xv18ggsma, CAIXA qs7a5zdzhvnwcgbvq1nw8mqhv98ghgk3, ETAPAS Escala qs7dq2rat6g8bqgxestrsbtpcd8gh99h, RECUPERAÇÃO qs778j27er6qrvcgabhp21w8p18g4cs6, PERPÉTUO qs7erh1mjx3k60s7pwbyf32ccx8g5wjk, CARRINHO qs7dgrqzmagwwsp4tycewr9f7s8g5znd, EVENTO qs79jy0xghkfp4cbpf77c2va1d8g519c, PESQUISA qs7a2m00grw2kqpbqr6b90xhb98g5v6b, AQUECIMENTO qs7057drwtjy4v1rxbeks131358g5j07, CAPTAÇÃO qs7b0pe73a3ym5mq4gc3svnq3h8g581c, OFERTA qs75rd7mmagmpbw73s0v8dx48n8g4pj7); `listPosts` (mesma conta).
- Buzzfy, 24/10/2026, 14h17 a 14h22: `ig_account_stats` (30 e 7 dias), `ig_posts` (desde 24/09), `ig_post_stats` (18386625754239681, 18010053242992517, 17995270031834903, 18337869829273388, 17954380989271814, 18118234495799066, 18354334132173198, 18121966600729052, 17889060588617582).
- Site, 24/10/2026, 14h16 a 14h20, GET: https://estrategistadelancamento.com.br/tabuleiro/?o=ig-tabuleiro, https://estrategistadelancamento.com.br/v2/, https://estrategistadelancamento.com.br/?o=ig-case, https://estrategistadelancamento.com.br/primeiro-lance/, https://estrategistadelancamento.com.br/lancamento-para-dentistas/, https://estrategistadelancamento.com.br/js/tabuleiro.js?v=2026-10-22, https://estrategistadelancamento.com.br/js/main.js?v=2026-10-22, https://estrategista-materiais-videon8ns-projects.vercel.app/m/checklist?o=ig-checklist.
- Repositório: `CLAUDE.md`; `conteudo/modo-god-cronograma/contexto.md`; `conteudo/modo-god-cronograma/run/00-enquadramento.md` (D3, D6, perguntas 16 e 19); `conteudo/sistema-instagram/00-SISTEMA.md` (ficha, Módulos 1, 6 e 7, Projeção); `conteudo/sistema-instagram/semanas/2026-10-21.md`; `conteudo/modo-god-nichos/run/10-decision-brief.md` (D3); `conteudo/stories-objecoes/01-objecoes.md` (leitura do direct) e `03-plano-7-dias.md`; `videos/nichos/dentista/words.json`; frentes irmãs `F1-auditoria-conta.md` (seção 4.4), `F2-playbook-buzzfy.md` (S6), `F5-capacidade-e-estoque.md` (Tzur) e `F6-stories-e-objecoes.md` (seção 7).
