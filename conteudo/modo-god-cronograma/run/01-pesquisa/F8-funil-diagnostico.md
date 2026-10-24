# F8 · Do conteúdo ao diagnóstico de 30 minutos · rodada de 24/10/2026, versão das 15h45

Frente F8 (funil-diagnostico) da pesquisa do conselho Agência Reunida para @o_estrategista.com.br. Substitui a versão das 14h25 deste arquivo (histórico no git, commit 88433c7), escrita antes do fato novo: a entrevista à TV Câmara Campinas vai ao ar na **segunda-feira, 02/11/2026** (mensagem do Bruno: "Vai pro ar segunda dia 2" e "pode seguir pois as postagens vou marcar ela"). Horário da exibição: sem dado.

Leituras ao vivo, somente leitura, entre 15h30 e 15h45 de sábado 24/10/2026 (horário de São Paulo). Nada foi publicado, agendado, alterado ou enviado no Instagram, no Buzzfy, no PostZen ou no site. Nenhum formulário foi enviado e nenhum teste foi respondido: as páginas e os scripts foram baixados com GET e lidos no código. Toda mudança abaixo é ação do Bruno, com prazo.

Etiquetas: [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha uma objeção sozinho. Métrica que falta: "sem dado".

---

## 0. Consultas feitas (todas responderam; nenhum erro de consulta)

| # | Fonte | Consulta e parâmetros | Hora (SP) | Resultado |
|---|---|---|---|---|
| 1 | PostZen `listCommentAutomations` | accountId j97772ycndetk3f1wcdbh14p898g4b8w | 15h30 | 17 automações, todas isActive true; textos, botões e palavras iguais aos das 14h05 |
| 2 | PostZen `listCommentAutomationLogs` | uma chamada por automação, as 17, limit 50 | 15h31 | 16 com total 0; CHECKLIST com total 1 (o mesmo registro das 14h05) |
| 3 | PostZen `listPosts` | mesma conta, de 24/10 00h a 30/11 23h59, sortBy scheduledFor, limit 100 | 15h32 | 20 posts: 4 stories publicados hoje (14h00, 14h03, 15h00, 15h01) e 16 agendados (24/10 16h30 a 21/11 18h30), já com tl02 a tl05 |
| 4 | Buzzfy `ig_account_stats` | 30 dias (24/09 15h30 a 24/10 15h30) | 15h30 | ok |
| 5 | Buzzfy `ig_account_stats` | 7 dias (17/10 a 24/10) | 15h30 | ok, 0 de anúncio |
| 6 | Buzzfy `ig_follower_growth` | 30 dias | 15h31 | ok; 22 e 23/10 pendentes |
| 7 | Buzzfy `ig_posts` | since 2026-09-24, limit 50; e kind stories | 15h31 | 35 itens de feed; 5 stories ativos |
| 8 | Buzzfy `ig_post_stats` | 32 ids em 3 chamadas: os 19 reels desde 24/09, os 5 posts de palavra-chave sem leitura, Checklist, Saga 7, "Antes de qualquer tabuleiro" e os 5 stories de hoje | 15h33 a 15h41 | ok; stories com dado provisório |
| 9 | Site (GET) | `/tabuleiro/?o=ig-tabuleiro`, `/v2/`, `/?o=ig-case`, `/primeiro-lance/`, `js/tabuleiro.js`, `js/main.js`, `js/cinema.js` | 15h33 a 15h35 | todos 200 |
| 10 | Site de materiais (GET) | `estrategista-materiais-videon8ns-projects.vercel.app/m/checklist?o=ig-checklist` | 15h33 | 200 |
| 11 | Contêiner GTM público (GET) | `googletagmanager.com/gtm.js?id=GTM-W2LS6RKN` | 15h36 | 200; GA4 G-F91ET225YW com 6 eventos |
| 12 | TV Câmara (GET) | `/programacao/2026-11-02`, `/programacao/2026-10-26`, `/termos` | 15h37 | 200; as duas datas redirecionam para 24/10 (grade de 02/11 não publicada) |

Não usei ferramenta fora da lista permitida (nada de `ig_comments`, `ig_inbox` ou `getCommentAutomation`). Quando cito o direct, a fonte é o `stories-objecoes/01-objecoes.md`, que leu o `ig_inbox` em outra rodada.

---

## 1. Resumo

1. [FATO, `listCommentAutomations` 15h30] Nada mudou nas automações desde as 14h05: 17 ativas, 15 palavras. Só 3 levam a diagnóstico (TABULEIRO, CASE, ESTRATEGISTA); 14 levam a PDF ou material com formulário de 9 campos. 6 valem para a conta toda: CASE ("case", "caso"), ESTRATEGISTA, ETAPAS, FUNIL e CAIXA em comentário, e ETAPAS em resposta de story.
2. [FATO, logs das 17] Um disparo em todas somadas: CHECKLIST, comentário "Checklist" de `bruno26111982`. [HIPÓTESE] É teste do Bruno; se for, a conta tem 0 lead real vindo de automação. TABULEIRO: 0 log, ligada só ao Dentista B, que sai hoje às 21h.
3. [FATO, `ig_post_stats`] 19 peças pediram palavra-chave desde 24/09: alcance somado 764, mediana 34, 3 comentários (0,39 por 100 contas). A única delas acima de 150 foi o reel "Você gravou o curso inteiro" (PESQUISA): 169 de alcance, pulo de 86,9%, 5 s assistidos e **0 comentário**. Os 4 reels com o Bruno, sem palavra-chave: 771 de alcance somado e 5 comentários (0,65 por 100). O portão dos 150 é necessário e não basta.
4. [FATO, `ig_account_stats`] 30 dias: 447 visitas ao perfil, 7 cliques no site (1,57%), 0 toque em botão de link, 14 comentários, 7 respostas de story. Últimos 7 dias, sem anúncio: 571 contas, 74 visitas, 0 clique, 2 comentários, 3 respostas.
5. [FATO, site às 15h33] A bio leva a `/v2/` ("A Partida", versão cinema): 6 botões abrem o WhatsApp com a mensagem padrão "Quero agendar o Primeiro Lance (diagnóstico de lançamento)." e nenhum leva ao Tabuleiro. Nenhuma das 5 páginas abertas cita a TV Câmara. Não há agenda on-line em nenhuma: o diagnóstico de 30 minutos é marcado na conversa do WhatsApp.
6. [FATO, `gtm.js` público] O contêiner GTM-W2LS6RKN tem GA4 (G-F91ET225YW) com 6 eventos: `tabuleiro_start`, `tabuleiro_complete` (nota, gargalo, profissão), `generate_lead` (clique em WhatsApp), `cta_click`, `file_download` e `calculadora_complete`. Os números existem no GA4 do Bruno; nenhuma ferramenta permitida aos agentes lê. O `o=ig-...` não entra em nenhum evento nem na mensagem do WhatsApp.
7. **Semana da exibição.** [FATO, `listPosts`] De dom 01/11 a sex 06/11 não há nada agendado no PostZen. [HIPÓTESE] Quem viu a TV e procura o Bruno chega pela busca, pelo perfil e pela bio, e não por comentário com palavra: a bio e o `/v2/` são a porta da semana, e hoje nenhuma das duas diz o que acontece depois nem cita a TV.
8. **Risco novo de automação na semana da TV.** A CASE dispara com "caso" e a ESTRATEGISTA com "estrategista", em qualquer post [FATO]. A série usa as duas palavras: "Contei esse caso" (pb02), "um dos casos" (ob02), "BRUNO · ESTRATEGISTA DE LANÇAMENTO" na tela do ob02 [FATO, `listPosts` e `03-plano-7-dias.md`]. Um comentário como "parabéns, estrategista" recebe um direct que diz "Pra eu te mostrar onde o seu dinheiro está vazando" [HIPÓTESE sobre a frequência]. E cada comentário só aceita uma resposta privada [FATO, PostZen]: se a automação responder, o Bruno não consegue mandar a resposta privada dele naquele comentário.
9. [ESTIMATIVA] Pela bio, a semana da TV rende de 0,5 a 1 clique: 32 a 63 visitas de 02 a 04/11 (10,6 por dia de base ou 21 por dia da meta D1) vezes 1,57%. Pelo comentário, até 22/11, o teto com 5 posts TABULEIRO no nível do Dentista A fica em 3,7 a 5,5 comentários de qualquer tipo. Nenhum dos dois caminhos, sozinho, chega a 10 diagnósticos por mês.
10. **Encaixe proposto.** TABULEIRO só na peça seguinte do mesmo formato de um reel que passou de 150 em 48 h (catálogo da entrevista, linhas 341 e 591), no máximo 1 por semana, com 4 leituras datadas: Dentista B (seg 26/10, 21h), pb01 (qua 28/10, 21h, abre o pb02), tl02 (seg 02/11, 18h30, abre o tl03) e tl03 (seg 09/11, 18h30, abre o tl04). No dia 02/11, nenhuma palavra: seguir e direct. CASE, ESTRATEGISTA, ETAPAS, FUNIL e CAIXA desligadas pelo Bruno antes do tl01 (dom 25/10, 18h30).

---

## 2. Mapa das 17 automações [FATO, `listCommentAutomations` e `listCommentAutomationLogs`, 15h30]

Todas: ativas, Instagram, público "any" (seguidor ou não), direct sem atraso, resposta pública sem atraso nas 16 de comentário, linkTracking false, alsoMatchInDms false (palavra digitada no direct não dispara nada), matchMode "word" (palavra inteira). Regras do PostZen lidas na descrição das ferramentas [FATO]: um comentário aceita uma resposta privada, uma vez, em até 7 dias; resposta de story vira direct normal dentro da janela de 24 h.

| # | Nome no PostZen | Gatilho | Palavras | Onde vale | Botão leva a | Destino | Disparos (stats / log) |
|---|---|---|---|---|---|---|---|
| 1 | TABULEIRO · Reel Dentista B (palavra do mês) | comentário | tabuleiro, tabuleiros (tolera erro) | só o Dentista B (postId m170mzbzy38d7td2vhggm4v2dx8gx767, sáb 24/10 21h) | `/tabuleiro/?o=ig-tabuleiro` | teste de 12 casas, depois WhatsApp | 0 / 0 |
| 2 | ETAPAS · resposta de Story (conta toda) | resposta de story | etapas, etapa | todo story | `.../m/checklist?o=ig-story-etapas` | PDF com formulário | 0 / 0 |
| 3 | CASE · diagnóstico (conta toda, sem citar cliente) | comentário | case, caso (sem tolerância a erro) | todo post | `/?o=ig-case` (página inicial) | página inicial, depois WhatsApp | 0 / 0 |
| 4 | ESTRATEGISTA · série 2 (conta toda) | comentário | estrategista (tolera erro) | todo post | `/?o=ig-estrategista` (página inicial) | página inicial, depois WhatsApp | 0 / 0 |
| 5 | ETAPAS · série 2 (conta toda) | comentário | etapas, etapa | todo post | `.../m/checklist?o=ig-etapas` | PDF com formulário | 0 / 0 |
| 6 | FUNIL · série 2 (conta toda) | comentário | funil | todo post | `.../m/checklist?o=ig-funil` | PDF com formulário | 0 / 0 |
| 7 | CAIXA · série 2 (conta toda) | comentário | caixa | todo post | `.../m/recuperacao?o=ig-caixa` | PDF com formulário | 0 / 0 |
| 8 | ETAPAS · Reels Escala 7x7 | comentário | etapas, etapa | um post (postId m1748g817gjwzraqn6wa67h3a18ghjqf, fora dos posts que o `listPosts` devolve) | `.../m/checklist?o=ig-etapas` | PDF com formulário | 0 / 0 |
| 9 | RECUPERAÇÃO · Reels 07 | comentário | recuperação e variações, recuperar | reel de 13/10 | `.../m/recuperacao?o=ig-recuperacao` | PDF com formulário | 0 / 0 |
| 10 | PERPÉTUO · Reels 08 | comentário | perpétuo e variações | reel de 14/10 | `.../m/perpetuo?o=ig-perpetuo` | material com formulário | 0 / 0 |
| 11 | CARRINHO · Reels 06 | comentário | carrinho, carrinhos | reel de 13/10 | `.../m/carrinho?o=ig-carrinho` | material com formulário | 0 / 0 |
| 12 | EVENTO · Reels 05 | comentário | evento, eventos | reel de 13/10 | `.../m/evento?o=ig-evento` | material com formulário | 0 / 0 |
| 13 | PESQUISA · Reels 01 | comentário | pesquisa, pesquisar | reel de 11/10 (id do Instagram 18091659392202122) | `.../m/pesquisa?o=ig-pesquisa` | material com formulário | 0 / 0 |
| 14 | AQUECIMENTO · Reels 04 | comentário | aquecimento, aquecer | reel de 12/10 | `.../m/aquecimento?o=ig-aquecimento` | material com formulário | 0 / 0 |
| 15 | CAPTAÇÃO · Reels 03 | comentário | captação e variações | reel de 12/10 | `.../m/captacao?o=ig-captacao` | material com formulário | 0 / 0 |
| 16 | OFERTA · Reels 02 | comentário | oferta, ofertas | reel de 12/10 | `.../m/oferta?o=ig-oferta` | material com formulário | 0 / 0 |
| 17 | CHECKLIST · carrossel 10 perguntas | comentário | checklist, check list, checklis | carrossel de 12/10 | `.../m/checklist?o=ig-checklist` | PDF com formulário | 1 / 1 |

Leitura:
- [FATO] 15 palavras ativas ao mesmo tempo, contra a regra de uma por mês (CLAUDE.md) e contra o PARAR de 21/10 ("12 palavras-chave diferentes", 00-SISTEMA, Módulo 7). A decisão segue sem execução 3 dias depois [FATO, F7].
- [FATO] O direct da TABULEIRO promete mostrar "em qual etapa o seu lançamento trava: pesquisa, oferta, aquecimento ou carrinho"; a página entrega o gargalo em um dos 5 Lances (A Abertura, O Gambito, O Meio-Jogo, O Xeque-Mate, A Promoção) [FATO, `js/tabuleiro.js`]. Mapas diferentes entre a promessa e a entrega.
- [FATO] O direct da TABULEIRO é texto de dentista ("Para quem tem agenda cheia, é o primeiro passo antes de transformar a técnica num segundo produto"). Serve ao Dentista B e não serve a peça da TV nem a outro nicho.
- [FATO, página de material] O formulário pede 9 campos (nome, WhatsApp, e-mail, Instagram, profissão, seguidores, se já lançou, quando pensa em lançar, maior dificuldade) mais o aceite, e envia para `/api/lead` no domínio `*.vercel.app`. Para onde vai e se alguém preencheu: sem dado.
- [FATO] O log do PostZen traz o id do post do Instagram de cada disparo (platformPostId) e não traz data nem hora.

---

## 3. O que disparou

- [FATO, log da CHECKLIST] Um registro: comentário "Checklist" (commentId 18093530426454537), autor `bruno26111982`, no post 18010053242992517 (carrossel "10 perguntas antes de abrir o carrinho", 12/10); resposta pública "sent"; direct "sent" com botões mantidos (buttonsDropped false).
- [FATO, `ig_post_stats`] O carrossel tem 34 de alcance, 2 comentários, 0 visita ao perfil, 0 seguidor. [HIPÓTESE] Os 2 comentários são o "Checklist" e a resposta pública automática da conta. Ler o texto exige `ig_comments`, fora da lista: sem dado.
- [FATO] A CHECKLIST foi ligada pelo id do PostZen e o log traz o id do Instagram. É o precedente de que a ligação por post agendado funciona depois da publicação, que é o caso da TABULEIRO no Dentista B.
- [FATO, `ig_posts`] Duas peças pediram palavra sem automação: Saga 7 (09/10, "Comenta TABULEIRO que eu te mando o diagnóstico gratuito", 71 de alcance, 0 comentário) e Médico (30/09, "Comenta AGENDA", 64 de alcance, 1 comentário que não recebeu nada automático).
- [FATO, `ig_account_stats`] 7 respostas de story em 30 dias e 3 em 7 dias; a ETAPAS de story tem 0 log, então nenhuma resposta trazia "etapa".
- [FATO, `01-objecoes.md`, leitura do `ig_inbox` de 12 a 24/10] Nas 50 conversas mais recentes do direct: nenhuma conversa comercial, nenhuma pergunta de preço, prazo ou método. Há menções da TV Câmara e da Mirna.

---

## 4. O caminho hoje e onde ele quebra

### 4.1 As portas que existem

| Porta | Caminho | O que chega ao Bruno | Estado |
|---|---|---|---|
| A. Comentário TABULEIRO | comentário no Dentista B, resposta pública, direct com botão "Fazer o diagnóstico", `/tabuleiro/?o=ig-tabuleiro`, 12 perguntas, resultado, botão de WhatsApp, horário combinado à mão | "Fiz O Tabuleiro no site. Deu N de 12 casas de pé e o gargalo caiu no Lance X, nome. [Sou profissão.] Queria olhar isso com você." A profissão só entra com `&p=` no link; a origem nunca [FATO, `js/tabuleiro.js`] | abre hoje 21h; 0 log |
| B. Comentário CASE ou ESTRATEGISTA | "case", "caso" ou "estrategista" em qualquer post, direct que diz "agenda um diagnóstico gratuito de 30 minutos", página inicial longa (35 KB), botão de WhatsApp | "Quero agendar o Primeiro Lance (diagnóstico de lançamento)." [FATO, `js/main.js`] | ativa; 0 log |
| C. Link da bio | perfil, `/v2/`, um dos 6 botões "Agendar o Primeiro Lance", WhatsApp | a mesma mensagem padrão; não se separa de quem veio do Google | 7 cliques em 30 dias, 0 em 7 dias |
| D. Link em story | sticker para `/tabuleiro/?o=ig-stories` (à mão, plano de stories) e daí igual à A | igual à A, sem a origem | depende do plano de stories (F6) |
| E. Palavra de material | palavra de material, direct, página na vercel, formulário de 9 campos, PDF, grupo de WhatsApp | sem dado | 1 disparo, possível teste |
| F. Direct à mão | "Me manda a data no direct", resposta de story, comentário de profissão ou de área | o que a pessoa escrever | 0 conversa comercial em 50 [FATO, 01-objecoes] |
| G. Quem viu a TV (nova, a partir de 02/11) | TV, busca do nome ou do perfil, perfil, bio, `/v2/`, WhatsApp; ou direct espontâneo | mensagem padrão ou direct livre | [HIPÓTESE] Se o programa mostra o @ do Bruno na tela: sem dado. Audiência da TV: sem dado; views da página de cada edição no site: mediana de 80,5 nas 20 últimas [FATO, F4] |

### 4.2 Números por etapa

| Etapa | 30 dias (24/09 a 24/10) | 7 dias (17 a 24/10) | Fonte |
|---|---|---|---|
| Alcance | 3.216 contas (1.907 de anúncio) | 571 contas (0 de anúncio; 212 seguidores, 360 não seguidores) | [FATO, `ig_account_stats`] |
| Views | 12.720 (10.513 orgânicas) | 1.896 (story 1.041) | [FATO, `ig_account_stats`] |
| Comentários | 14 | 2 | [FATO] |
| Respostas de story | 7 | 3 | [FATO] |
| Visitas ao perfil | 447 | 74 | [FATO] |
| Cliques no site (link da bio) | 7 (1,57% das visitas) | 0 | [FATO] |
| Toques em botão de link | 0 | 0 | [FATO] |
| Seguidores | +53 e -13 (24/09 a 21/10); de 12 a 21/10, 1 entrada e 7 saídas; 22 e 23/10 pendentes | | [FATO, `ig_follower_growth`] |
| Disparos de automação | 1 (CHECKLIST, possível teste) | sem dado por período (o log não tem data) | [FATO, logs] |
| Cliques no botão do direct | sem dado (linkTracking false) | sem dado | [FATO] |
| Teste iniciado e concluído | existe no GA4 G-F91ET225YW; sem dado para os agentes | sem dado | [FATO, `gtm.js`] |
| Clique no WhatsApp do site | evento `generate_lead` no GA4; sem dado para os agentes | sem dado | [FATO, `gtm.js` e `js/main.js`] |
| Mensagens no WhatsApp | sem dado (só o Bruno vê) | sem dado | |
| Diagnósticos de 30 min agendados | sem dado | sem dado | |
| Diagnósticos realizados | sem dado | sem dado | |
| Vendas | 0 | 0 | [FATO, contexto.md] |

### 4.3 Onde o caminho quebra (do mais pesado ao mais leve)

1. **Topo: pouca gente vê e quase ninguém comenta.** [FATO] 571 contas em 7 dias, 2 comentários (0,35 por 100). Os 4 reels com o Bruno são os únicos com comentário: "Ele nunca fez um anúncio" 308 de alcance e 3 comentários, "90%" 166 e 2, "Equipe" 128 e 0, Dentista A 169 e 0 [FATO, `ig_post_stats`]. Automação só age depois do comentário.
2. **Pedido de palavra sem atenção.** [FATO] 19 peças pediram palavra: 764 de alcance somado, mediana 34, 3 comentários. O caso que derruba a leitura simples da regra dos 150: o reel PESQUISA passou de 150 (169) com automação ligada e teve 0 comentário; tinha 86,9% de pulo e 5 s assistidos. O Dentista A, com o mesmo alcance (169), tinha 46% de pulo e 13 s, e pediu "comenta aqui que eu te respondo" sem palavra: 0 comentário também. [HIPÓTESE] Alcance sem retenção não gera comentário; com retenção, a amostra (n de 1) não mostra comentário ainda.
3. **A bio não diz o que vende e não leva ao teste.** [FATO, `ig_account_stats` e site] A bio segue "Estrategista Digital / Ide e pregai o evangelho! / Visitor Host @bnisyrius / Dev @dashpronow" e o link é `/v2/`, que abre em "carregando a partida..." e manda ao WhatsApp com a mensagem padrão. O Módulo 2 do 00-SISTEMA pediu `/tabuleiro/?o=ig-bio`; não foi aplicado. 447 visitas, 7 cliques; nos 7 dias, 74 e 0.
4. **Palavras demais e de uso comum, justo na semana da TV.** [FATO] 5 palavras de comentário valem para a conta toda; "caso", "caixa", "funil" e "etapa" são do dia a dia, e "estrategista" é o nome do perfil e o cargo na tela do ob02. [HIPÓTESE] Comentário de parabéns ou de opinião recebe direct de diagnóstico ou de PDF e consome a única resposta privada daquele comentário.
5. **Destino errado em 2 das 3 automações de diagnóstico.** [FATO] CASE e ESTRATEGISTA dizem "toca no botão e agenda" e o botão abre a página inicial; não há agenda on-line em nenhuma página aberta.
6. **"Diagnóstico" quer dizer duas coisas.** [FATO] O site chama de diagnóstico o teste de 12 casas ("Teste de Lançamento Grátis: diagnóstico em 12 casas", 4 minutos, sem cadastro) e a conversa de 30 minutos ("Diagnóstico de lançamento gratuito: o Primeiro Lance", videochamada ou WhatsApp). A legenda do Dentista B promete "o diagnóstico de 12 casas"; o estático diário do plano de stories diz "DIAGNÓSTICO · 12 CASAS"; a meta do sistema conta "10 diagnósticos por mês" de 30 minutos; a Projeção do 00-SISTEMA soma as duas coisas ("2% de clique no Tabuleiro, são 9 diagnósticos feitos por mês").
7. **A origem se perde.** [FATO] O `o=ig-...` fica só no endereço. Os eventos gravam `page_origin: location.pathname` (sem o parâmetro) e a mensagem do WhatsApp não leva a origem. [PRIOR] O GA4 grava o endereço completo da página na visualização por padrão; se essa propriedade guarda: sem dado. O PostZen não conta o clique no botão (linkTracking false).
8. **Quem chega pela TV não acha a TV.** [FATO] As 5 páginas abertas têm 0 menção à TV Câmara ou ao Ser Empreendedor. [HIPÓTESE] Quem vem da entrevista cai numa página sem ligação com o que acabou de ver.
9. **Do WhatsApp à venda, nada registrado.** [FATO, 00-SISTEMA, Módulo 6] Existem 3 perguntas de qualificação e um follow-up de +1, +4 e +10 dias, escritos. Se foram usados: sem dado. Vendas: 0.

---

## 5. A semana da exibição pelo olhar do funil

### 5.1 Fatos da semana

- [FATO, mensagem do Bruno e contexto.md] Exibição na seg 02/11/2026, Finados. Horário: sem dado. [FATO, site da TV às 15h37] A grade de 26/10 e de 02/11 não está publicada (redireciona para 24/10).
- [FATO, `listPosts`] Agendado em volta: tl02 sáb 31/10 18h30 (legenda: "A entrevista vai ao ar na segunda, 02/11."), depois nada até tl03 sáb 07/11 18h30. De dom 01/11 a sex 06/11 o PostZen está vazio.
- [FATO, F4] Proposta da frente da entrevista: ci01 de qua 28/10 para seg 02/11 21h, com legenda versão A que termina em "Segue o perfil: os próximos trechos da entrevista saem aqui."; po01 de qui 29/10 para qua 04/11 21h, com "Comenta qual delas.". [FATO, `03-plano-7-dias.md`] Proposta da frente de stories: ob02 seg 02/11 21h, ob01 qua 04/11 21h, ob03 sex 06/11 21h, todos com "Comenta a sua área que eu te respondo." As vagas de 02 e 04/11 coincidem; o conselho escolhe.
- [FATO, F4, termos da TV Câmara de 24/05/2026] Pode compartilhar link e citar trecho com a emissora como fonte; não pode republicar conteúdo integral nem usar o conteúdo da emissora para fins comerciais. As peças do "depois" usam a gravação do celular do Bruno.
- [FATO, contexto.md] O Bruno marca a Mirna pelo app; o PostZen não marca pessoa em reel, carrossel nem story.

### 5.2 O que o funil pede para a semana

1. **A porta da semana é a bio, não o comentário.** [HIPÓTESE] Quem viu a TV procura o nome e chega ao perfil. Hoje encontra quatro identidades na bio e um link que não diz o que acontece ao tocar. A decisão do link (manter `/v2/`, trocar por `/tabuleiro/?o=ig-bio` como o Módulo 2 aprovou, ou `/primeiro-lance/`, que explica os 30 minutos) é do Bruno e precisa estar feita antes de dom 01/11. É a única troca que mexe na etapa medida (1,57% de clique). Qualquer uma das três leva ao mesmo WhatsApp; só a do Tabuleiro chega com a nota e o gargalo na mensagem.
2. **Nenhuma palavra-chave em 02/11.** O dia é de quem não conhece o Bruno, e a regra do Módulo 1 diz que o pedido de palavra a quem não confia ainda vira zero [FATO, 00-SISTEMA, item 4]. No dia: seguir (ci01, versão A do F4) ou comentar a área (ob02), e nos stories a chamada para assistir e o link do teste, cada um no seu story.
3. **Uma pergunta que separa quem veio da TV.** Story à mão a partir do horário confirmado: "Chegou pela TV Câmara? Me manda um oi no direct e conta a sua área." Sem palavra e sem automação; o Bruno conta quantos directs citam a TV. É a única atribuição possível da TV ao funil com as ferramentas de hoje [FATO: o `o` não chega ao WhatsApp e o PostZen não conta clique].
4. **Desligar as 5 automações de conta toda antes do primeiro reel da série** (tl01, dom 25/10, 18h30). Motivo: a série usa "caso" e "estrategista" e atrai comentário de parabéns; a resposta automática consome a resposta privada do comentário e manda PDF ou "dinheiro vazando" a quem só cumprimentou [HIPÓTESE sobre a frequência; FATO sobre a regra de uma resposta privada].
5. **Responder à mão dentro das janelas.** Comentário: resposta privada em até 7 dias; resposta de story: direct em até 24 h [FATO, PostZen]. Com 0,35 a 0,65 comentário por 100 contas, a carga é pequena: 10 reels da série a 53 a 169 de alcance dão de 2 a 11 comentários [ESTIMATIVA: 10 × 53 × 0,0035 = 1,9; 10 × 169 × 0,0065 = 11].
6. **Ler a semana com números que existem.** Visitas ao perfil por dia de 02 a 04/11 contra 10,6 [ESTIMATIVA, 74 / 7]; cliques no site; directs que citam a TV (Bruno); mensagens "Fiz O Tabuleiro" e "Quero agendar o Primeiro Lance" (Bruno); `generate_lead` e `tabuleiro_complete` no GA4 (Bruno).

### 5.3 Contas da semana [ESTIMATIVA]

- Bio, de 02 a 04/11: 10,6 visitas por dia × 3 = 32 visitas × 1,57% = 0,5 clique. Na meta D1 do enquadramento (21 por dia): 63 × 1,57% = 1,0 clique.
- Para 10 diagnósticos por mês só pela bio, com 1,57% de clique e 100% de conversão depois do clique (premissa impossível, usada como piso): 10 / 0,0157 = 637 visitas por mês: 1,4 vez as 447 de 30 dias com anúncio e 2 vezes o ritmo orgânico de 317 por mês (74 / 7 × 30).
- Leitura: a TV pode mexer no volume de visitas (sem dado de quanto); a bio mexe na taxa de clique. Uma não substitui a outra.

---

## 6. Peças agendadas e propostas: pedidos e colisões

Fonte das legendas e horários: [FATO, `listPosts` 15h32]. Propostas de outras frentes: F4 e `03-plano-7-dias.md`. As sugestões são do Bruno decidir; nenhum agente mexe no PostZen.

| Quando (hoje no PostZen) | Peça | Pedido hoje | Proposta de outra frente | Automação que pode disparar | Risco para o funil | O que o funil pede |
|---|---|---|---|---|---|---|
| sáb 24/10 21h | Dentista B | legenda: "Comenta TABULEIRO que eu te mando o diagnóstico de 12 casas."; fala de 32,0 a 35,3 s: "Dentista, comenta a sua profissão aqui que eu te respondo." [FATO, `videos/nichos/dentista/words.json`; B tem 36,37 s como o A] | | TABULEIRO; CASE e ESTRATEGISTA se o comentário trouxer a palavra | dois pedidos; "dentista" não recebe nada automático | antes das 21h, `&p=dentista` no botão da TABULEIRO [FATO: `tabuleiro.js` aceita]; responder à mão os comentários de profissão no mesmo dia |
| dom 25/10 18h30 | tl01 | "Comenta o número do assunto que você quer ver inteiro. O mais votado eu solto inteiro depois que a entrevista for ao ar." | fica (F4) | nenhuma (números) | compromisso público de soltar o mais votado | manter; contagem à mão |
| seg 26/10 21h | pb01 | "Manda para um expert que vai lançar este ano." | fica, legenda com a data e o @ (F4) | nenhuma | nenhum | leitura de 48 h em qua 28/10 21h decide TABULEIRO no pb02 |
| ter 27/10 12h | car01 | "Comenta o número." e "Me manda a data no direct." | fica com os dois pedidos; a cadeira de playbook decide (F4) | nenhuma | dois pedidos (regra S6 do F2: um por legenda) | se ficar um, que seja o direct: é o que leva à conversa |
| ter 27/10 16h | pf01 (story) | sem texto | | ETAPAS de story só com "etapa" | baixo | no estático do teste do dia (à mão), link com `&p=dentista` (F6) |
| qua 28/10 21h | ci01 | "E você, o que teria respondido?" | mover para seg 02/11 21h, versão A com "Segue o perfil" (F4) | CASE ("no meu caso"), ESTRATEGISTA | alto se ficar a pergunta aberta com a CASE ligada [HIPÓTESE] | apoiar a versão A ou desligar a CASE antes |
| qui 29/10 21h | po01 | "Qual dessas peças falta no seu lançamento? Comenta a palavra." e "Salva..." | mover para qua 04/11 21h, "Comenta qual delas." (F4) | nenhuma | "comenta a palavra" parece palavra-chave sem automação | um pedido, com resposta à mão que leva ao teste: o po01 fala dos lances do Método Xeque-Mate, o mesmo mapa do resultado do Tabuleiro |
| sex 30/10 21h | pb02 | "Vai lançar nos próximos 90 dias? Me manda a data no direct." | fica (F4) | CASE só se o comentário trouxer "caso" (a legenda diz "Contei esse caso") | baixo | se o pb01 passar de 150 em 48 h (e, com o reforço proposto na R3, pulo abaixo de 60%), pode levar TABULEIRO no lugar do direct (catálogo, linha 341), com automação criada pelo Bruno até sex 30/10 20h59; senão, manter o direct |
| sáb 31/10 18h30 | tl02 | "Comenta o número do assunto que você quer ver inteiro." | fica, com portão (F4) | nenhuma | dois tl seguidos pedindo número | leitura de 48 h em seg 02/11 18h30 decide TABULEIRO no tl03 |
| seg 02/11 21h (vaga vazia) | ci01 (F4) ou ob02 (03-plano) | | ci01: "Segue o perfil"; ob02: "Comenta a sua área que eu te respondo." | ESTRATEGISTA (cargo na tela do ob02), CASE ("um dos casos") | médio [HIPÓTESE] | sem TABULEIRO no dia; as 5 de conta toda já desligadas |
| qua 04/11 21h (vaga vazia) | po01 (F4) ou ob01 (03-plano) | | "Comenta qual delas." ou "Comenta a sua área" | nenhuma, com as de conta toda desligadas | baixo | resposta à mão com o link do teste |
| sex 06/11 21h (vaga vazia) | ob03 (03-plano) | | "Comenta a sua área que eu te respondo." | idem | baixo | idem |
| sáb 07/11 18h30 | tl03 | "Comenta o seu primeiro investimento." | | nenhuma | baixo | TABULEIRO no lugar do pedido se o tl02 passar no portão |
| sáb 14/11 18h30 | tl04 | "Comenta o número da parada que você quer ver inteira." | | nenhuma | promete "ver inteira" sem dizer quando | TABULEIRO se o tl03 passar no portão |
| sáb 21/11 18h30 | tl05 | "Comenta SIM ou NÃO: o tête-à-tête ainda é o melhor marketing?" | | nenhuma | baixo | TABULEIRO se o tl04 passar no portão |

[FATO] Hoje só o Dentista B usa palavra-chave com automação. Os pedidos da série são número, enviar, seguir, área e direct, nenhum deles palavra-chave: nenhum fere a regra de uma palavra por mês.

---

## 7. Como o cronograma encaixa a TABULEIRO

**R1. Uma palavra, a mesma em outubro e novembro: TABULEIRO** [FATO, CLAUDE.md]. As outras 14 saem das legendas. As 5 de comentário de conta toda (CASE, ESTRATEGISTA, ETAPAS, FUNIL, CAIXA) são desligadas pelo Bruno antes do tl01 (dom 25/10, 18h30); a ETAPAS de story, antes de dom 25/10 09h00 (F6). Desligar em vez de apagar guarda a configuração [HIPÓTESE sobre o PostZen: o campo isActive existe, FATO]. As 10 ligadas a posts antigos podem ficar: esses posts têm 0 comentário, menos o Checklist com 2.

**R2. No máximo um post com TABULEIRO por semana** [FATO, 00-SISTEMA, Módulo 1, item 4].

**R3. O portão: 150 de alcance em 48 h, lido no `ig_post_stats`, no post anterior do mesmo formato** [FATO, CLAUDE.md; catálogo da entrevista, linhas 133, 341 e 591; precedente do Dentista A em `semanas/2026-10-21.md`]. Proposta de reforço, sem ferir a regra: exigir também pulo abaixo de 60% [HIPÓTESE, base n de 1: o reel PESQUISA teve 169 de alcance, 86,9% de pulo e 0 comentário; o Dentista A, 169 e 46%]. O F7 usa 55% na exceção de sequência; o conselho escolhe um número só.

**R4. O que é "mesmo formato".** Proposta: a linha de produção da peça. Nicho falado (Dentista A, B e C contam como uma linha, porque o B já recebeu a palavra pelo A [FATO]); P&B da entrevista (pb01, pb02); timelapse (tl01 a tl05); cinema (ci01); pontos (po01); objeção (ob01 a ob03). O precedente vale para o próximo da linha, uma vez. O B consumiu o precedente do A; a linha de nicho só reabre se o próprio B passar no portão.

**R5. Leituras datadas e o que cada uma abre.**

| Leitura (48 h) | Data e hora | Se passar | Se não passar |
|---|---|---|---|
| Dentista B | seg 26/10, 21h | próximo reel de nicho falado (Dentista C ou gravação nova) pode levar TABULEIRO | próximo de nicho sai sem palavra, com "comenta a sua profissão" e resposta à mão |
| pb01 | qua 28/10, 21h | pb02 (sex 30/10) pode levar TABULEIRO | pb02 fica com o direct |
| tl02 | seg 02/11, 18h30 | tl03 (sáb 07/11) pode levar TABULEIRO | tl03 fica com a pergunta |
| ci01, se for para 02/11 | qua 04/11, 21h | nenhum outro cinema pronto | |
| tl03 | seg 09/11, 18h30 | tl04 (sáb 14/11) | tl04 fica com o número |
| tl04 | seg 16/11, 18h30 | tl05 (sáb 21/11) | tl05 fica com SIM ou NÃO |
| reel de nicho com TABULEIRO ou sem | 48 h depois de cada um | o próximo de nicho | |

Se duas linhas abrirem na mesma semana, uma só leva a palavra (R2). Proposta de desempate: nicho falado antes de corte da TV, porque o teste aceita a profissão no link e o público do nicho é o Tier 1 da ficha [HIPÓTESE].

**R6. Nunca no dia 02/11** (seção 5.2) e nunca em story [FATO: a TABULEIRO dispara com comentário, não com resposta de story]. No story, o pedido é o link do teste (F6).

**R7. Uma automação para novembro, criada pelo Bruno.** A de hoje é presa ao Dentista B e tem texto de dentista. Duas formas:
- (a) Uma por post, como hoje: botão com `o=ig-tab-AAMMDD` e `&p=<profissão>` em post de nicho. Custo: uma automação nova a cada post; quem comentar "tabuleiro" em outro post não recebe nada.
- (b) Uma só, de conta toda, a partir de dom 01/11, com texto genérico (seção 8), e a do Dentista B desligada no mesmo momento (dois gatilhos na mesma palavra: qual responde é sem dado). O pedido continua só nos posts que passaram no portão; o log do PostZen já traz o post de cada disparo [FATO], então a origem por post não se perde no PostZen. Custo: a profissão sai do link (o texto da mensagem fica sem "Sou dentista").
- Proposta: (b), pelo custo operacional menor e porque "tabuleiro" não é palavra do dia a dia [HIPÓTESE]. Decisão do Bruno.

**R8. Um pedido por legenda.** Post com TABULEIRO não pede salvar, número nem direct.

**R9. Teto honesto.** Até 22/11 cabem no máximo 5 posts com a palavra (Dentista B e um por semana de S1 a S4). [ESTIMATIVA] 5 × 169 × 0,65 por 100 = 5,5 comentários de qualquer tipo; com 0,44 por 100 (conta toda), 3,7. A meta D6 do enquadramento (3 disparos de perfis que não são do Bruno até 22/11) só acontece se pelo menos 3 linhas abrirem e quase todo comentário for a palavra. Diagnósticos: a previsão de 21/10 é 1 agendado até 18/11, faixa de 0 a 3, probabilidade 0,2 [FATO, `10-decision-brief.md`, D3]. Taxas de disparo para clique, clique para WhatsApp e WhatsApp para agendamento: sem dado.

---

## 8. Chamadas para o direct sem promessa de resultado

Critério (CLAUDE.md): sem promessa de resultado, sem travessão, sem emoji, no máximo uma "não é X, é Y" por peça. Nada de palavra para digitar no direct: nenhuma palavra no direct dispara automação [FATO, alsoMatchInDms false nas 17], e pedir uma cria uma segunda palavra sem automação. Nada da lista do `02-provas.md` ("ao vivo", "entrevista exclusiva", "fui convidado pela TV", "a TV Câmara recomenda", "rede nacional") e nada de "foi ao ar" antes do horário confirmado (F4).

**Antes da exibição (25/10 a 01/11), na legenda, uma por peça:**
1. "Vai lançar nos próximos 90 dias? Me manda a data no direct." (já no car01 e no pb02)
2. "Me conta no direct qual é a sua área e quando pensa em lançar."

**No dia (02/11):**
- Legenda: seguir (ci01, versão A do F4) ou "Comenta a sua área que eu te respondo." (ob02). Um dos dois, não os dois.
- Story à mão, depois do horário confirmado: "Chegou pela TV Câmara? Me manda um oi no direct e conta a sua área."
- Story do teste no seu próprio quadro: "Em 4 minutos você vê em qual casa o seu lançamento trava." com o link `/tabuleiro/?o=ig-stories` (texto que bate com o destino, F6).

**Depois (03/11 a 21/11):**
3. "Quer olhar o seu lançamento comigo por 30 minutos? Me chama no direct."
4. "Comenta a sua área que eu te respondo." (ob01 a ob03; resposta à mão)
5. Só em post que passou no portão: "Comenta TABULEIRO que eu te mando o teste de 12 casas." ou "Comenta TABULEIRO que eu te mostro em qual casa o seu lançamento trava." (o que o teste entrega). A variante "o mesmo diagnóstico que fiz com a Tzur" fica de fora enquanto a autorização da Tzur estiver pendente [FATO, F5].

**Texto do direct da TABULEIRO de novembro (proposta para o Bruno configurar):**
> Oi! Aqui é o Bruno. O Tabuleiro são 12 perguntas sobre o seu próximo lançamento, em 4 minutos e sem cadastro. No fim aparece a casa que está mais vazia. Toca no botão, responde e, se fizer sentido, me manda o resultado no WhatsApp que a gente marca 30 minutos.
> [Fazer o teste]

Base: "Diagnóstico em 4 minutos", "Nada de e-mail, nada de cadastro" e o botão que abre o WhatsApp [FATO, `/tabuleiro/`]. Não cita "4 etapas": a página mostra 5 Lances.

**Resposta à mão para comentário de área ou de profissão (dentro de 7 dias):**
- Pública: "Te mandei no direct."
- Privada (uma por comentário): "Oi, aqui é o Bruno. Obrigado por comentar. Se quiser ver em qual casa o seu lançamento está mais vazio, são 12 perguntas: estrategistadelancamento.com.br/tabuleiro/?o=ig-manual&p=<profissão>. Se fizer sentido depois, me chama aqui que a gente marca 30 minutos."
- Profissões que o `p` aceita: medico, advogado, psicologo, nutricionista, dentista, consorcio [FATO, `js/tabuleiro.js`]. Outra área: link sem `p`.

**Resposta a quem mandou a data ou a área no direct:** as 3 perguntas de qualificação do Módulo 6 (área e seguidores; se já vende on-line e quanto, por alto; se lança em 90 dias). Follow-up de +1, +4 e +10 dias só com quem respondeu; o de +10 ("Abri 4 horários de diagnóstico esta semana") só vale se for verdade naquela semana.

**Evitar:** "garantido", "você vai faturar", número de caso como promessa para quem lê (o ob02 e o pb02 já trazem a ressalva "O número de um caso não se repete igual em outro negócio"), "vagas" sem número real de horários, números de cliente sem autorização. O direct da ESTRATEGISTA ("Pra eu te mostrar onde o seu dinheiro está vazando") afirma um vazamento antes de ver o caso [PRIOR: tom de pressão]; desligada a automação (R1), o texto sai de circulação.

---

## 9. Como contar cada etapa (toda segunda, no Módulo 7)

| Etapa | Número | Quem lê | Fonte | Observação |
|---|---|---|---|---|
| 1. Alcance e pulo do post anterior da linha em 48 h | contas, % | agente | `ig_post_stats` | portão da R3 |
| 2. Comentários do post com TABULEIRO | total | agente | `ig_post_stats` | pode incluir a resposta pública da conta [HIPÓTESE] |
| 3. Disparos da TABULEIRO | total, sent, failed, skipped, gated | agente | `listCommentAutomationLogs` | o log não tem data: guardar o total de cada segunda e fazer a diferença; tirar perfis de teste do Bruno; o platformPostId dá o post |
| 4. Visitas ao perfil e cliques no site | por semana; de 02 a 04/11 por dia | agente | `ig_account_stats` | atraso de até 48 h |
| 5. Clique no botão do direct | cliques | sem dado hoje | PostZen, se o Bruno ligar o linkTracking [HIPÓTESE sobre o que passa a mostrar] | |
| 6. Teste iniciado e concluído; clique no WhatsApp | `tabuleiro_start`, `tabuleiro_complete`, `generate_lead` | Bruno | GA4 G-F91ET225YW | os eventos gravam o caminho da página, não o `o` |
| 7. Mensagens no WhatsApp | quantas começam com "Fiz O Tabuleiro no site" e quantas com "Quero agendar o Primeiro Lance" | Bruno | WhatsApp | as duas frases são fixas no código [FATO] |
| 8. Directs que citam a TV | total de 02 a 08/11 | Bruno | direct | a única atribuição da TV |
| 9. Diagnóstico de 30 min agendado | total | Bruno | agenda dele | contar separado do teste de 12 casas |
| 10. Diagnóstico realizado | total | Bruno | agenda dele | a meta de 10 por mês conta aqui |
| 11. Proposta e venda | total | Bruno | anotação dele | |

Registro: `conteudo/sistema-instagram/semanas/AAAA-MM-DD.md`, uma linha por etapa, com "sem dado" quando o Bruno não informar. O Módulo 7 de seg 02/11 cai no feriado e no dia da exibição; as leituras 1 a 4 não dependem dele.

---

## 10. O que depende só do Bruno (nenhum agente mexe)

| # | Ação | Prazo | Por quê |
|---|---|---|---|
| 1 | Pôr `&p=dentista` no botão da TABULEIRO do Dentista B | hoje, antes das 21h | a mensagem do WhatsApp passa a dizer a profissão |
| 2 | Responder à mão os comentários de profissão do Dentista B | no mesmo dia; no máximo 7 dias | a fala do vídeo promete "eu te respondo" |
| 3 | Decidir a ETAPAS de story (F6, seção 7) | antes de dom 25/10, 09h00 | o plano de stories conta com ela e ela só dispara com "etapa" |
| 4 | Desligar CASE, ESTRATEGISTA, ETAPAS (comentário), FUNIL e CAIXA | antes de dom 25/10, 18h30 (tl01) | colisão com "caso" e "estrategista" na série da TV; regra de uma palavra; PARAR de 21/10 sem execução |
| 5 | Dizer se `bruno26111982` é perfil dele e listar perfis de teste | até seg 26/10 | o único disparo do mês pode ser teste |
| 6 | Escolher o link e o texto da bio | antes de dom 01/11 | é a porta de quem vem da TV (seção 5.2) |
| 7 | Responder às leituras de portão (R5) e, se abrir, criar a automação | pb02: até sex 30/10 20h59; tl03: até sáb 07/11 18h29; tl04 e tl05: na sexta anterior | a automação precisa existir antes de o post sair |
| 8 | Escolher entre automação por post e de conta toda para novembro (R7) | até sáb 31/10 | a de hoje tem texto de dentista |
| 9 | Ajustar car01 (um pedido) e po01 ("comenta a palavra") | ter 27/10 11h59 e antes da data final do po01 | seção 6 |
| 10 | Pedir à Mirna o horário da exibição | o quanto antes | sem ele, nenhum story do dia diz a hora (F4) |
| 11 | Informar toda segunda as etapas 6 a 11 da seção 9 | toda segunda | sem isso a meta de 10 diagnósticos não é medida |
| 12 | Decisão escrita: "comenta a sua área" ou "a sua profissão" conta como segunda palavra? | estava para 24/10 | D3 de 21/10; os ob01 a ob03 usam o pedido |
| 13 | Ligar o linkTracking na automação que ficar | quando quiser | contaria o clique no botão do direct [HIPÓTESE] |

---

## 11. Lacunas

- Quem é `bruno26111982` e se o único disparo é teste: sem dado.
- Texto dos 14 comentários do mês e quanto deles é resposta da própria conta: sem dado (`ig_comments` fora da lista).
- Data e hora dos disparos: o log do PostZen não traz.
- Cliques no botão do direct: sem dado (linkTracking false).
- Números do GA4 G-F91ET225YW (testes iniciados e concluídos, cliques no WhatsApp) e se a propriedade guarda o endereço com o `o`: sem dado para os agentes.
- Mensagens no WhatsApp, diagnósticos agendados e realizados, propostas: sem dado (só o Bruno).
- Destino do formulário `/api/lead` das páginas de material e se alguém preencheu: sem dado.
- Qual automação responde quando um comentário traz duas palavras, ou quando duas automações têm a mesma palavra: sem dado.
- Se o Instagram entrega o direct com botão para quem não segue esta conta: 1 envio com botão mantido, de perfil que pode ser do Bruno; sem dado para terceiros.
- Horário da exibição de 02/11 e se o programa mostra o @ do Bruno: sem dado. Audiência da TV: sem dado.
- Alcance da conta em feriado (02/11, 15/11, 20/11): sem dado.
- Curva de comentários por hora depois da publicação: sem dado.
- Se a regra dos 150 com pulo abaixo de 60% separa post que gera comentário de post que não gera: n de 1 de cada lado; sem dado para afirmar.
- O post ligado à ETAPAS Escala 7x7 (m1748g817gjwzraqn6wa67h3a18ghjqf) não aparece no `listPosts`: se ainda aponta para o reel de 18/10, sem dado.

---

## 12. Fontes

- PostZen, 24/10/2026, 15h30 a 15h32: `listCommentAutomations` (accountId j97772ycndetk3f1wcdbh14p898g4b8w); `listCommentAutomationLogs` das 17 automações (TABULEIRO qs747t4bq23a1qpnjskexg34vs8gx7hx, ETAPAS story qs78ccqc3nf0axhc59frr8mewx8ghnvj, CASE qs79dctypcnz18m9wbeb7cg4en8gh8fm, ESTRATEGISTA qs7309wynnp8dgvy96k67nfj558ggz2r, ETAPAS série 2 qs7e2jwpb31ezb4j5yhrc33pr58gg2fm, FUNIL qs71kgp5n4q612z8rsxm281xv18ggsma, CAIXA qs7a5zdzhvnwcgbvq1nw8mqhv98ghgk3, ETAPAS Escala qs7dq2rat6g8bqgxestrsbtpcd8gh99h, RECUPERAÇÃO qs778j27er6qrvcgabhp21w8p18g4cs6, PERPÉTUO qs7erh1mjx3k60s7pwbyf32ccx8g5wjk, CARRINHO qs7dgrqzmagwwsp4tycewr9f7s8g5znd, EVENTO qs79jy0xghkfp4cbpf77c2va1d8g519c, PESQUISA qs7a2m00grw2kqpbqr6b90xhb98g5v6b, AQUECIMENTO qs7057drwtjy4v1rxbeks131358g5j07, CAPTAÇÃO qs7b0pe73a3ym5mq4gc3svnq3h8g581c, OFERTA qs75rd7mmagmpbw73s0v8dx48n8g4pj7, CHECKLIST qs7de23c7nzxzw2k4yjshgm5gd8g5dmx); `listPosts` (mesma conta, 24/10 a 30/11).
- Buzzfy, 24/10/2026, 15h30 a 15h41: `ig_account_stats` (30 e 7 dias), `ig_follower_growth` (30 dias), `ig_posts` (desde 24/09; stories ativos), `ig_post_stats` (18386625754239681, 18354334132173198, 18121966600729052, 17889060588617582, 18010053242992517, 18337869829273388, 17995270031834903, 17912745426542222, 18475767697117883, 17907942183576061, 18132487157503394, 18035848712883339, 18108193625266844, 18113139875614712, 18130543543811478, 18093643208680305, 18012829418994819, 18156735856556789, 18117956657006877, 18118217153074281, 18091659392202122, 18093434834176117, 17872136757645672, 18016028789753059, 18143385994717530, 18124578748833604 e os stories 18126070586490029, 17957608836082053, 17954380989271814, 18118234495799066, 18052167683804505).
- Site, 24/10/2026, 15h33 a 15h36, GET: https://estrategistadelancamento.com.br/tabuleiro/?o=ig-tabuleiro, https://estrategistadelancamento.com.br/v2/, https://estrategistadelancamento.com.br/?o=ig-case, https://estrategistadelancamento.com.br/primeiro-lance/, https://estrategistadelancamento.com.br/js/tabuleiro.js?v=2026-10-22, https://estrategistadelancamento.com.br/js/main.js?v=2026-10-22, https://estrategistadelancamento.com.br/js/cinema.js, https://estrategista-materiais-videon8ns-projects.vercel.app/m/checklist?o=ig-checklist, https://www.googletagmanager.com/gtm.js?id=GTM-W2LS6RKN.
- TV Câmara, 24/10/2026, 15h37, GET: https://www.tvcamaracampinas.com.br/programacao/2026-11-02 e /2026-10-26 (redirecionam para 24/10), https://www.tvcamaracampinas.com.br/termos (200; conteúdo lido pela F4).
- Repositório: `CLAUDE.md`; `conteudo/modo-god-cronograma/contexto.md`; `run/00-enquadramento.md` (D3, D6, perguntas 15 e 18); `conteudo/sistema-instagram/00-SISTEMA.md` (ficha, Módulos 1, 6 e 7, Projeção); `conteudo/sistema-instagram/semanas/2026-10-21.md`; `conteudo/modo-god-nichos/run/10-decision-brief.md` (D3); `conteudo/entrevista-tv-camara/pecas-e-calendario.md` e `catalogo-formatos.md` (linhas 133, 214, 341 e 591); `conteudo/stories-objecoes/01-objecoes.md` (leitura do direct) e `03-plano-7-dias.md` (ob01 a ob03, stories de 01 e 02/11); `videos/nichos/dentista/words.json` e `render/dentista-B-9x16.mp4` (36,37 s); frentes irmãs `F1-auditoria-conta.md`, `F4-entrevista-tv.md` (seções 0, 4 e 5), `F5-capacidade-e-estoque.md` (Tzur), `F6-stories-e-objecoes.md` (seção 7) e `F7-horarios-e-portao.md` (exceção de sequência).
