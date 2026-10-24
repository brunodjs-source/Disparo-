# Plano H · Cadeira H (CRO e landing page) · Conselho Agência Reunida Modo GOD

Cliente: @o_estrategista.com.br (Bruno, Estrategista de Lançamento). Cronograma de dom 25/10 a dom 22/11/2026. Escrito no sábado 24/10/2026, das 17h03 às 17h25 (horário de São Paulo). Trabalho isolado: não abri os planos A a F.

| Campo | Texto |
|---|---|
| **Persona** | Especialista em conversão de página e oferta |
| **OTIMIZA PARA** | Oferta, prova, fricção e velocidade, nesta ordem |
| **PONTO CEGO (assumido por escrito)** | Achar que a página resolve falta de demanda. Compensação: (1) antes de propor qualquer mudança de página, faço a conta do teto dela (seção 2); (2) limito o trabalho de página e de perfil a 6 mudanças baratas, com prazo e custo; (3) quando uma peça "perto da oferta" disputa vaga com uma peça que gera demanda medida (o Bruno de frente para a câmera), a demanda ganha; (4) nenhuma mudança de bio ou de link é julgada antes de 150 visitas ao perfil acumuladas, e nenhuma segunda mudança entra antes de 23/11 |
| **PERGUNTA CONTRÁRIA** | "E se o problema estiver antes do clique?" Resposta curta: está, na maior parte. Em 7 dias, 576 contas alcançadas, 77 visitas ao perfil e 0 clique no site [FATO, `ig_account_stats` 17h11]. Mesmo que o clique fosse perfeito, ~330 visitas por mês não fecham 10 diagnósticos. A resposta completa está na seção 2 |

**Etiquetas.** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha uma objeção sozinho. Métrica que falta: "sem dado". Número de fato citado como "fato N" vem do livro `run/01-fatos.md`; "N1" a "N12" são conferências desta cadeira (seção 0).

**Lido:** `contexto.md`, `run/00-enquadramento.md`, `run/01-fatos.md` (185 fatos), as 8 frentes `run/01-pesquisa/F1` a `F8` (F4, F5, F6, F7 e F8 nas seções que tocam esta cadeira), `CLAUDE.md`, `stories-objecoes/02-provas.md` (seção "O que NÃO pode ser dito"), `05-manuais-bruno.md` e `06-agenda-postzen.md` (este escrito às 17h06, depois do livro de fatos).

**Regra de operação.** Nada foi publicado, agendado, alterado ou enviado. Nenhum formulário foi enviado e nenhum teste foi respondido no site. Toda mudança abaixo é ação do Bruno ou da agência, com prazo.

---

## 0. Conferências próprias desta cadeira (só leitura, 17h03 a 17h12)

| # | O que conferi | Resultado | Fonte e hora |
|---|---|---|---|
| N1 | Agenda do PostZen da conta j97772ycndetk3f1wcdbh14p898g4b8w, de 24/10 a 01/12 | **48 itens**: 5 stories publicados hoje (14h00, 14h03, 15h00, 15h01, 16h30) e 43 agendados. Entraram **28 stories de 25 a 31/10**, todos sem sticker (bate com `06-agenda-postzen.md`). Feed igual ao livro de fatos: Dentista B sáb 24/10 21h; tl01 dom 25/10 18h30; pb01 seg 26/10 21h; car01 ter 27/10 12h; ci01 qua 28/10 21h; po01 qui 29/10 21h; pb02 sex 30/10 21h; tl02 sáb 31/10 18h30; tl03 07/11, tl04 14/11, tl05 21/11, 18h30. **Nada de dom 01/11 a sex 06/11.** mc02 (dom 25/10 09h01) e mc03 (seg 26/10 17h30) já estão agendados | PostZen `listPosts`, 17h10 |
| N2 | Stories que dependem da hora do feed | Chamadas agendadas: seg 26/10 20h30 (pb01), qua 28/10 20h30 "QUA · 21H · NO FEED" (ci01), qui 29/10 17h30, 17h31 "MÉTODO XEQUE-MATE" e 20h30 (po01), sex 30/10 20h30 (pb02), sáb 31/10 17h30 (tl02). O story pf01 de ter 27/10 16h trocou de arquivo: `pf01-dentista-story-v2.mp4`, título "dentista na TV, em dois meses" | PostZen `listPosts`, 17h10 |
| N3 | Conta, 7 dias (17/10 20h11 UTC a 24/10 20h11 UTC) | Alcance 576 (215 seguidores, 362 não seguidores), 0 de anúncio; views 2.054 (story 1.159, reel 448); **77 visitas ao perfil, 0 clique no site, 0 toque em link**; 2 comentários, 4 compartilhamentos, 3 respostas. Tipo de conta: MEDIA_CREATOR. Nome: "Bruno Israel Gonçalves". Bio sem mudança, com emojis e primeira linha "Estrategista Digital". Link: /v2/. Seguindo: 3.529 | Buzzfy `ig_account_stats` days 7, 17h11 |
| N4 | Automações | 17 ativas, sem mudança. TABULEIRO: 0 disparo. CHECKLIST: 1. Direct da TABULEIRO promete "em qual etapa o seu lançamento trava: pesquisa, oferta, aquecimento ou carrinho" e fala de "agenda cheia" e "segundo produto" (texto de dentista). CASE e ESTRATEGISTA mandam para a página inicial com "agenda um diagnóstico" | PostZen `listCommentAutomations`, 17h11 |
| N5 | Página do link da bio, `/v2/` | HTML de 11.459 bytes; título "A Partida · Estrategista de Lançamento (versão cinema)"; 423 palavras; **nenhuma imagem do Bruno**; **0 menção** a TV Câmara, Ser Empreendedor ou Mirna; 6 botões "Agendar o Primeiro Lance" com `href="#"` que o `main.js` troca por wa.me; a oferta ("Trinta minutos, gratuito... Se não fizer sentido, o diagnóstico fica de presente") só aparece no último bloco; o menu mostra "v1 · imersiva" e "v2 · cinema" ao visitante | GET, 17h03 |
| N6 | Peso da `/v2/` | O `cinema.js` baixa **129 quadros JPG que somam 7.097.863 bytes**; o aviso "carregando a partida…" sai depois de 12 quadros (715.575 bytes). HTML, JS e CSS somam 201.771 bytes. Total: **7.299.634 bytes**. Os quadros vêm com `cache-control: max-age=0, must-revalidate` | GET quadro a quadro e cabeçalhos, 17h05 a 17h08 |
| N7 | Página do teste, `/tabuleiro/?o=ig-tabuleiro` | HTML de 22.213 bytes; com JS e CSS, **248.621 bytes** (29 vezes menos que a `/v2/`); título "Teste de Lançamento Grátis: diagnóstico em 12 casas"; "Nada de e-mail, nada de cadastro"; nenhuma imagem do Bruno; 0 menção à TV; o botão do resultado diz "Levar meu tabuleiro pro diagnóstico (abre o WhatsApp)" e "Trinta minutos sobre o seu caso" | GET, 17h03 |
| N8 | `/primeiro-lance/` | 29.104 bytes, 1.736 palavras, 1 foto do Bruno de 4.059 bytes, 1 botão de WhatsApp, 0 menção à TV | GET, 17h03 |
| N9 | Atribuição no código | O `main.js` grava `page_origin: location.pathname` em todo evento (`generate_lead`, `cta_click`): **o `?o=` não entra no evento**. Só um caminho diferente (por exemplo `/tv/`) separa a origem dentro dos eventos | `js/main.js`, linhas 29 a 43, 17h04 |
| N10 | Rodapé das páginas de entrada | "Lançamento Certo" e "Agência Tráfego Pago" apontam para agenciatrafegopago.com.br | GET, 17h03 |
| N11 | Tempo até o primeiro byte, medido deste servidor (não de um celular) | 0,33 s a 0,57 s nas 4 páginas | curl, 17h03 |
| N12 | O que é vetado dizer | Além da lista do fato 6: "estrategista digital" está marcado como termo contaminado no 02-provas ("Usa o termo 'estrategista digital', marcado como contaminado") | `02-provas.md`, seção "O que NÃO pode ser dito" |

---

## 1. Veredito (até 12 linhas)

1. O gargalo maior está antes do clique: 576 contas, 77 visitas ao perfil e 2 comentários em 7 dias [FATO, N3]. Nenhuma página fecha 10 diagnósticos com ~330 visitas por mês [ESTIMATIVA, seção 2].
2. O clique também está quebrado, e consertar é barato: a bio abre com "Estrategista Digital" (termo vetado, N12) e o link leva a uma página de 7,3 MB sem foto, sem prova e sem TV [FATO, N5, N6].
3. D1, divisão: ficam tl01, pb01, car01, pb02 e tl02. O ci01 vai para seg 02/11 21h (único reel do dia). O po01 vai para qua 04/11 21h só se a vaga de qui 29/10 receber um reel de nicho gravado; sem gravação, ele fica.
4. A TV é prova, não motor de alcance: cortes crus de TV ficaram em 0,0055x os seguidores no mercado [FATO 155]; o motor medido da conta é o Bruno de frente para a câmera, 167,5 contra 32,5 de alcance [FATO 25, 27]. Uma gravação de 30 min por semana vale mais que qualquer ajuste de página.
5. Até dom 25/10 17h: bio nova, link para `/tabuleiro/?o=ig-bio`, 5 automações de conta toda e a ETAPAS de story desligadas.
6. TABULEIRO: só depois de 02/11, só em reel de nicho cujo anterior da linha fez 150 ou mais com pulo abaixo de 60% em 48 h, no máximo 1 por semana, direct reescrito para bater com a página.
7. Régua única do começo ao fim: alcance em 48 h sobre 53 (27, 42, 106, 150; pulo 60% e 75%). O pedido de cada post é julgado à parte, por respostas a cada 100 contas.
8. Previsão honesta [PRIOR]: 1 diagnóstico de 30 min agendado até 18/11 (0 a 3) e 1 disparo de TABULEIRO de terceiro até 22/11 (0 a 4).

---

## 2. Ponto cego e pergunta contrária, por escrito

### 2.1 O funil medido

| Etapa | 7 dias (lido 17h11) | 30 dias (lido 14h50 e 15h30) | Taxa | Fonte |
|---|---|---|---|---|
| Contas alcançadas | 576 (362 não seguidores, 0 de anúncio) | 3.216 (1.907 de anúncio) | | [FATO, N3; fato 10] |
| Visitas ao perfil | 77 | 447 | 13,4% do alcance em 7 dias [ESTIMATIVA, 77 / 576] | [FATO, N3; fato 14] |
| Cliques no site | 0 | 7 | 0% em 7 dias; 1,57% em 30 dias [ESTIMATIVA, 7 / 447] | [FATO, N3; fato 14] |
| Comentários | 2 | 14 | 0,35 por 100 contas em 7 dias | [FATO, N3; fato 13] |
| Disparos de automação | sem dado por período | 1 (CHECKLIST, possível teste) | | [FATO, N4; fato 116] |
| Teste iniciado e concluído; clique no WhatsApp | sem dado (GA4 só o Bruno lê) | sem dado | | [FATO, fato 130] |
| Diagnósticos de 30 min agendados | sem dado | sem dado | | [FATO, fato 8 e 143] |
| Vendas | 0 | 0 | | [FATO, contexto.md] |

### 2.2 O teto da página (a conta que segura o meu ponto cego)

- [ESTIMATIVA] Visitas orgânicas por mês no ritmo atual: 77 / 7 x 30 = **330**.
- [ESTIMATIVA] Para 10 diagnósticos por mês, a conversão de visita em diagnóstico precisaria ser 10 / 330 = **3,0%**. Hoje a visita vira clique em 1,57%. Mesmo com 100% dos cliques virando diagnóstico (impossível), faltaria metade.
- [ESTIMATIVA com PRIOR] Se a página dobrar o clique para 3% e 20% dos cliques virarem conversa marcada (as duas taxas são palpite, sem dado da conta), a conta pede 10 / (0,03 x 0,20) = **1.667 visitas por mês**, cerca de 5 vezes as 330 de hoje.
- Leitura: a página mexe na taxa; o volume vem de antes do clique (alcance, retenção, formato e o evento da TV). Uma não substitui a outra.

### 2.3 O que fica antes do clique e quanto pesa

1. **Formato.** Reel com o Bruno falando para a câmera: mediana de 167,5 de alcance e 48,1% de pulo (n 4). Animação com voz sintética: 32,5 e 83,9% (n 12) [FATO 25, 27]. É a maior alavanca medida da conta, 5,2 vezes.
2. **Gravação parada.** Nenhuma gravação nova desde 21/10 13h12 [FATO 104]; o reel "Fila é teto" de 23/10 não saiu [FATO 105]. Sem gravação, o formato que funciona fica restrito a 3 remakes em 720p [FATO 37].
3. **A TV é evento de tamanho desconhecido.** Audiência: sem dado. As 20 edições do programa no site têm de 27 a 1.400 views, mediana de 80,5 [FATO 136]. A exibição cai em Finados [FATO 3]. No mercado, cortes crus de TV ficaram de 0,004x a 0,025x os seguidores; o que mais rendeu "depois" foi manchete em texto e o criador contando como foi (n de 1 cada) [FATO 155, 157].
4. **Pedido de palavra a quem não confia.** 19 peças com palavra-chave somaram 764 de alcance e 3 comentários [FATO 122]; no mercado em português, palavra-chave fica em 0,043x os seguidores contra 0,081x dos outros pedidos, e 0 de 9 estouros de contas pequenas usou palavra [FATO 164].
5. **Seguidores parados.** De 12 a 21/10, 1 entrada e 6 saídas [FATO 17].

### 2.4 O que isso faz com o plano

- Faço só as mudanças de página e de perfil que custam minutos e mexem no ponto medido (1,57%): bio, link, automações, rótulo do link do story, texto do direct e 3 posts fixados. Custo do Bruno: cerca de 30 min no total [PRIOR].
- A parte de página que pede agência (caminho `/tv/` para atribuição, bloco da TV com foto na `/tabuleiro/`, sufixo de origem na mensagem do WhatsApp) fica opcional e com teto de 2 h de agência [PRIOR], e só entra se a agência tiver folga depois das peças de feed.
- A grade dá prioridade à gravação semanal e aos remakes como Trial Reel, que falam com quem ainda não segue.
- O critério de sucesso do D6 conta só o caminho por comentário, que é o de maior fricção. Proponho somar ao critério os testes concluídos (`tabuleiro_complete`) e as mensagens "Fiz O Tabuleiro no site", que o Bruno lê.

---

## 3. O perfil como página de entrada: auditoria da cadeira

Para quem vem da TV, a página de entrada é o perfil: nome, bio, link, destaques e as primeiras linhas da grade. A tabela segue a ordem da persona: oferta, prova, fricção, velocidade.

| Elemento | Estado | Problema | Mudança proposta | Quem | Prazo | Custo |
|---|---|---|---|---|---|---|
| Bio, linha 1 | "Estrategista Digital", com emoji [FATO, N3] | Oferta: termo contaminado no 02-provas [FATO, N12]; o site e a placa dos cortes dizem "Estrategista de Lançamento" [FATO 88] | Versão A abaixo | Bruno | dom 25/10, 17h | 2 min [PRIOR] |
| Bio, linhas 2 a 4 | Fé, BNI, Dev Dashpro [FATO 9] | Oferta: quatro identidades e nenhuma diz o que ele faz por quem chega | Versão A até 02/11, versão B a partir de ter 03/11 | Bruno | idem | idem |
| Link | `/v2/` [FATO, N3] | Fricção e velocidade: 7,3 MB, 6 botões "Agendar" sem agenda on-line, seletor "v1 · imersiva / v2 · cinema" à vista [FATO, N5, N6, fato 128]; prova: nenhuma foto e nenhuma menção à TV | `estrategistadelancamento.com.br/tabuleiro/?o=ig-bio` (Módulo 2 já aprovou e não foi aplicado [FATO 132]) | Bruno | dom 25/10, 17h | 1 min |
| Destaques | COMECE AQUI com 3 stories animados da Escala, sem o Bruno; PROVA não existe [FATO 64] | Prova ausente no topo do perfil | Destaque "NA TV" a partir de ter 03/11, só com stories sem "vai ao ar", com o link da edição quando sair (F6) | Bruno | ter 03/11 | 5 min [PRIOR] |
| Grade | 11 dos 12 reels sintéticos aparecem com a capa "Comenta PALAVRA" [FATO 45] | Prova: o que quem chega vê primeiro é pedido, não o Bruno | Fixar 3 posts no topo: car03 "Prazer", R1 "Ele nunca fez um anúncio" (308 de alcance, o maior com o Bruno [FATO 25]) e pb02 (caso com número e ressalva) | Bruno | dom 01/11, 22h | 3 min; o recurso de fixar até 3 posts é [PRIOR], conferir no app |
| Direct da TABULEIRO | Texto de dentista e promessa de "4 etapas" contra 5 Lances na página [FATO, N4; fato 117] | Oferta: promessa e entrega não batem | Texto novo na seção 4, pergunta 18 | Bruno | antes do primeiro post de novembro com TABULEIRO | 5 min |
| Link do story | Rótulo "Diagnóstico de 12 casas" [FATO, 05-manuais] | Oferta: "diagnóstico" nomeia o teste e a conversa de 30 min [FATO 131]; na sex 30/10 o story "DIAGNÓSTICO · 30 MIN" sai no mesmo dia | Rótulo "Teste de 12 casas · 4 min" | Bruno | dom 25/10 | 0 |
| Atribuição | `?o=` não entra no evento nem no WhatsApp [FATO, N9; fato 129] | Sem saber se a TV trouxe alguém | Mínimo: story à mão "Chegou pela TV Câmara? Me manda um oi no direct e conta a sua área." (F8). Opcional (agência): página em caminho próprio `/tv/` | Bruno; agência | seg 02/11; `/tv/` até sex 30/10 | 0; `/tv/` [PRIOR] 1 h |
| Página do teste | Sem foto e sem TV [FATO, N7] | Prova | Opcional: uma linha "Entrevista ao programa Ser Empreendedor, TV Câmara Campinas, 02/11/2026" com foto do Bruno acima das perguntas; depois de 02/11, o link da edição (termos permitem link e citação com fonte [FATO 137]); sem logo da emissora | agência | sex 30/10 | [PRIOR] 30 a 60 min |

**Bio proposta (o Bruno decide; sem emoji, sem travessão, sem promessa):**

Versão A, de dom 25/10 a seg 02/11 (130 caracteres, contados):
> Estrategista de Lançamento
> Comando lançamentos de quem já tem audiência.
> Na TV Câmara Campinas em 02/11.
> Teste de 12 casas, 4 min:

Versão B, a partir de ter 03/11 (132 caracteres):
> Estrategista de Lançamento
> Comando lançamentos de quem já tem audiência.
> Entrevista na TV Câmara Campinas.
> Teste de 12 casas, 4 min:

Se o Bruno quiser manter a linha de fé, ela entra no lugar da linha 4 (132 caracteres) e o link fica sem rótulo. "Comando" segue o posicionamento "comanda, não ensina" [FATO, 02-provas].

---

## 4. Respostas às 22 perguntas

### P1. Quais decisões o plano move, qual número muda, com que fonte e em que segunda é lido?

| Decisão | O que o plano move | Número que deve mudar | Base | Fonte | Leitura |
|---|---|---|---|---|---|
| D1 | ci01 para 02/11; po01 condicional para 04/11; legendas com data e um pedido | Alcance médio em 48 h dos reels da série por fase (piso 42, pulo até 75%) | sem dado (nenhuma peça saiu) | `ig_post_stats` | seg 02/11 19h (antes), seg 09/11 19h (dia e começo do depois), seg 23/11 (depois) |
| D1 | Bio, link e story "Chegou pela TV?" | Visitas ao perfil por dia de 02 a 04/11 (alvo 21) | 10,6 a 11,0 por dia [ESTIMATIVA, 74 / 7 e 77 / 7] | `ig_account_stats` days 1 lido em 03, 04 e 05/11; total de 7 dias em seg 09/11 | seg 09/11 |
| D1, D6 | Link da bio para o teste | Cliques no site por semana e taxa sobre visitas | 0 em 7 dias; 1,57% em 30 dias | `ig_account_stats` | seg 02/11 (semana só com a bio nova) e seg 09/11 (semana da TV) |
| D2 | Bloco de gravação até ter 27/10 23h59 (ideal) ou qua 28/10 23h59 (final) | Mediana de alcance e pulo dos reels de nicho, n de 3 | Dentista A 169 e 46,6%; B sem dado | `ig_post_stats` | qua 11/11 |
| D3 | Grade 5 reels e 2 carrosséis, ordem da semana da TV, 3 posts fixados | Mediana semanal de alcance de reel; seguidores | semanas fechadas 64, 128, 33,5 e 16; seguidores -5 de 12 a 21/10 | `ig_post_stats`, `ig_follower_growth` | toda segunda; saldo até 08/11 fecha em 11/11 |
| D4 | Um pedido por dia nos stories, com rótulo que bate com o destino | Views de story por semana; respostas a cada 14 dias; toques no link (Bruno) | views de 7 dias de 982 (até 14h11) a 1.159 (17h11); 3 respostas | `ig_account_stats`; app (Bruno) | toda segunda às 19h, janela de 7 dias com a mesma hora |
| D5 | Régua única e régua de pedido | Respostas a cada 100 contas por tipo de pedido | palavra-chave 0,39; reels com o Bruno 0,65 [FATO 122, 123] | `ig_post_stats` | toda segunda |
| D6 | 6 automações desligadas; TABULEIRO só pós-02/11 com portão | Disparos de terceiros; testes concluídos; mensagens "Fiz O Tabuleiro" | 0; sem dado; sem dado | `listCommentAutomationLogs`; GA4 e WhatsApp (Bruno) | toda segunda; parcial de diagnóstico em qua 04/11 [FATO 181]; final em qua 18/11 |

### P2. Qual régua?

**Alcance em 48 h sobre a mediana de 53** (00-SISTEMA [FATO 24]), a mesma do começo ao fim:

| Marco | Alcance em 48 h | Conta | Views de referência [ESTIMATIVA, x 1,52, fato derivado 4] |
|---|---|---|---|
| Metade | 27 | 0,5 x 53 | 41 |
| Piso de PARAR | 42 | 0,8 x 53 | 64 |
| Referência | 53 | | 80 |
| DOBRAR | 106 | 2 x 53 | 161 |
| TABULEIRO | 150 | CLAUDE.md | 228 |

Pulo: abaixo de 60% para DOBRAR; acima de 75% para PARAR. Motivos: separa os grupos já medidos (animação até 40, sem rosto a partir de 54, Bruno a partir de 128 [FATO 27, 28, 25]); a base do Buzzfy (37,5) anda sozinha e mudaria a régua no meio das 4 semanas [FATO 23]; bate com o CLAUDE.md (150) e com a regra de abandono do nicho (53) [FATO 169]. Views do `ig_reel_checkup` entram na planilha como coluna de referência, nunca como régua.

**Acréscimo da cadeira: régua de pedido**, separada da de formato. Respostas (comentário, direct citado pelo Bruno ou toque no botão) a cada 100 contas alcançadas, por tipo de pedido (palavra, direct, pergunta, seguir, enviar). PARAR um tipo de pedido com 0 resposta em 2 posts com 106 ou mais de alcance; DOBRAR com 1 ou mais por 100 contas em 2 posts. Base: palavra-chave 0,39; reels com o Bruno 0,65 [FATO 122, 123]. [ESTIMATIVA: os cortes são escolha minha, não medida]

### P3. A grade está dia a dia e hora a hora, com feriados?

Sim, seção 5, com dia da semana conferido no `date` (dom 25/10 a dom 22/11; seg 23/11; ter 24/11; qui 24/12; sáb 23/01/2027) [FATO, `date` às 17h10]. Feriados [FATO 3]: seg 02/11 (Finados e exibição) tem grade própria; dom 15/11 e sex 20/11 mantêm a hora e o formato; reel lido em feriado entra na mediana, mas não fecha PARAR sozinho (F7). Alcance em feriado: sem dado; o único feriado medido (12/10) é de animação, com 3 pares [FATO 41].

### P4. O que sai antes, no dia e depois de 02/11?

**Antes (dom 25/10 a dom 01/11): aquecimento, bastidor, contagem.**
- Feed: tl01 (dom 25/10 18h30), pb01 (seg 26/10 21h), car01 (ter 27/10 12h), reel de nicho ou po01 (qui 29/10 21h), pb02 (sex 30/10 21h), car02 "Os 5 Lances" (sáb 31/10 12h), tl02 (sáb 31/10 18h30, com portão), car03 "Prazer. Eu sou o Bruno." (dom 01/11 12h).
- Stories: os 28 já agendados no PostZen [FATO, N1] mais os manuais do `05-manuais-bruno.md`, com 3 mudanças (seção 5). Contagem: texto "NA TV · SEG, 02/11" já presente nos estáticos agendados [FATO, N1]; o sticker de contagem nativo só entra se o horário chegar até dom 25/10 (F6).
- Todo texto diz "vai ao ar segunda, 02/11"; nada diz "assista", "foi ao ar" ou "ao vivo" [FATO 6].

**No dia (seg 02/11, Finados): chamada para assistir.**
- 08h30: o Bruno confere o horário (Mirna ou `tvcamaracampinas.com.br/programacao/2026-11-02`).
- 09h00 (agendado, sem hora): estático com foto do Bruno "SEG · 02/11 · NA TV CÂMARA CAMPINAS / Programa Ser Empreendedor, com a repórter Mirna Abreu / Canal 11.3 aberto, NET 4, Vivo Fibra 9 e tvcamaracampinas.com.br" (onde assistir, [FATO 135]).
- Com horário confirmado e ainda por vir: story à mão "SEG · 02/11 · ÀS __H NA TV CÂMARA CAMPINAS", menção à Mirna e link para `/ao-vivo` ("Assistir na TV Câmara").
- Se às 12h o horário seguir sem dado: story à mão "A partir de hoje, 02/11, na TV Câmara Campinas." com link para `/programacao` ("Horários na programação"). Se o horário já tiver passado (01h ou 06h, padrão desta semana [FATO 134]), pula a chamada e vai para o "Foi ao ar".
- Depois do horário confirmado: selfie "Foi ao ar." (à mão, sem a tela da TV no quadro) e, em outro story, "Chegou pela TV Câmara? Me manda um oi no direct e conta a sua área." Esse é o único jeito de atribuir a TV ao funil com as ferramentas de hoje [FATO 129, N9].
- 20h30 chamada; **21h00 ci01** (versão A da legenda, vale com ou sem horário); 21h05 compartilhar com menção à Mirna. Se o programa passar entre 20h e 22h, o ci01 vai para 30 min depois do fim (o Bruno muda no PostZen até 18h).
- Nenhuma palavra-chave no dia.

**Depois (ter 03/11 a sáb 21/11): o que eu disse na TV.**
- ter 03/11: repost do ci01 com enquete; car04 "O que eu disse na TV"; resultado da votação do tl01; story com o link da edição quando ela subir no site ou no YouTube (o Bruno confere antes o minuto em que aparece).
- qua 04/11: po01 (se moveu) ou reel de nicho. sex 06/11: "o mais votado inteiro" (promessa do tl01). tl03, tl04 e tl05 nos sábados, com portão. ob01 a ob03 de S3 a S4.
- Bio versão B; destaque "NA TV".

### P5. pb01, car01, ci01, po01 e pb02, um por um

| Peça | Decisão | Motivo (oferta, prova, fricção) | Data e hora | Ação do Bruno no PostZen e prazo |
|---|---|---|---|---|
| pb01 | **Fica** | Apresenta o Bruno (trajetória) e não entrega método; o antes precisa de quem é ele para a TV ter a quem promover. Bruno em cena desde o quadro 0, de perfil em 3/4 [FATO 88] | seg 26/10 21h | Legenda até seg 26/10 20h59: acrescentar "A entrevista vai ao ar na segunda, 02/11, no programa Ser Empreendedor." Um pedido só (o atual "Manda para um expert que vai lançar este ano.") |
| car01 | **Fica** | Único carrossel pronto [FATO 108]; capa com o Bruno; a S1 precisa de 2 carrosséis | ter 27/10 12h | Legenda até ter 27/10 11h59: "com o minuto de cada uma **na gravação**"; data de 02/11; **um pedido só**: "Vai lançar nos próximos 90 dias? Me manda a data no direct." (sai o "Comenta o número"). Motivo: o pedido de direct é o que leva à conversa, e a S1 já pede número no tl01 e no tl02 |
| ci01 | **Muda para seg 02/11 21h** | A frase já foi anunciada com "NA TV · SEGUNDA, 02/11" [FATO 58, story das 19h30]; tem voz e rosto da Mirna por 10,7 s [FATO 90]: depois da exibição a marcação e o convite fazem sentido; o dia 02/11 precisa de um reel pronto e a semana de 01 a 06/11 está vazia [FATO, N1]; é o assunto 5 da legenda do tl01, que promete o "depois" | seg 02/11 21h | Mover até qua 28/10 20h59 para 2026-11-03T00:00:00Z; apagar o story "QUA · 21H · NO FEED" de qua 28/10 20h30 até 20h29; legenda versão A (F4, seção 5) |
| po01 | **Muda para qua 04/11 21h, com condição** | É a peça mais perto da oferta (Método Xeque-Mate, o mesmo mapa dos 5 Lances do teste [FATO 129]): prova ao lado do pedido rende mais depois da exibição [PRIOR]. Condição, pelo meu ponto cego: só sai de qui 29/10 se a vaga receber um reel de nicho gravado (formato medido) até ter 27/10 23h59 e aprovado na folha até qua 28/10 12h. Sem isso, fica | qua 04/11 21h ou qui 29/10 21h | Decisão até qua 28/10 12h; mover até qui 29/10 20h59 para 2026-11-05T00:00:00Z. Legenda: trocar "Comenta a palavra" (não diz qual [FATO 80]) por "Qual dessas peças falta no seu lançamento? Comenta qual delas." e tirar o "Salva..." (um pedido). Se mover, apagar ou trocar os stories de qui 29/10 17h31 "MÉTODO XEQUE-MATE" e 20h30 "QUI · 21H" se não houver reel |
| pb02 | **Fica** | Caso com número (45 mil para 250 mil) e a ressalva "O número de um caso não se repete igual em outro negócio" já escrita [FATO, N1]: prova que não depende da exibição; fecha a dupla P&B com n de 2 para o portão de 02/11 | sex 30/10 21h | Legenda até sex 30/10 20h59: "Contei esse caso na entrevista à TV Câmara Campinas, que vai ao ar na segunda, 02/11." Pedido único: direct. Sem TABULEIRO antes de 02/11 (seção 4, P18) |

### P6. A promessa do tl01

[FATO 77, N1] A legenda já diz "O mais votado eu solto inteiro depois que a entrevista for ao ar" e não fala mais de sábado. A S1 fica em 5 reels sem o 6º (tl01, pb01, nicho ou po01, pb02, tl02). Entrega: **sex 06/11 21h**, "o mais votado inteiro", na S2. O Bruno conta os votos no app até ter 03/11 12h (o `ig_comments` está fora da lista [FATO 143]) e anuncia o resultado em story na ter 03/11 19h. Com menos de 5 votos somados, segue a regra do catálogo ("seguir o plano e dizer isso nos stories" [FATO 170]) e sai o assunto 6, "Zero reais", que ainda não tem peça [FATO, F5 4.1]. "Inteiro" quer dizer mais longo que os cortes de 20 a 37 s [HIPÓTESE 54].

Mudança no tl02 (sáb 31/10): trocar "Comenta o número do assunto que você quer ver inteiro." por "Segue o perfil: segunda, 02/11, a entrevista vai ao ar e os trechos saem aqui." Motivo: o tl02 cria uma segunda promessa de "inteiro" sem data, divide a votação e pede comentário a quem ainda não confia; na véspera, o pedido que casa com o momento é seguir (1,12x entre contas [FATO 148]). [HIPÓTESE, confiança média]

### P7. Ordem de tl02 a tl05 e portão

Ordem: tl02 (sáb 31/10), tl03 (sáb 07/11), tl04 (sáb 14/11), tl05 (sáb 21/11), todos às 18h30, como estão [FATO, N1]. O tl03 paga o story "A pergunta da TV" de hoje; tl04 cobre o assunto 1 (origem); tl05 fecha com o assunto do ci01 em outro formato.

| Portão | Lê | Data e hora real de 48 h | Decide |
|---|---|---|---|
| Extra | tl01 (dom 25/10 18h30) | ter 27/10 18h35 | tl02, pela tabela da F7 5.4: 106 ou mais com pulo abaixo de 60%, ou 42 ou mais com pulo até 75%: fica. Só um critério ruim: sai só o tl02, o tl03 vira 2ª leitura. Abaixo de 27, ou abaixo de 42 com pulo acima de 75%: saem tl02 a tl05 |
| Módulo 7 | tl02 (sáb 31/10 18h30) | seg 02/11 18h30 (lido às 19h, 48h30) | tl03 |
| Módulo 7 | tl03 | seg 09/11 19h | tl04; a Mirna vê o recorte do "Uau!" antes |
| Módulo 7 | tl04 | seg 16/11 19h | tl05; a Mirna vê o carimbo "AINDA?" antes |

Timelapse que não for ao feed: o Bruno cancela no PostZen até a sexta 23h59 anterior; a agência corta trechos de 10 a 15 s para o bloco das 09h00 dos stories; o arquivo vai para o banco. A vaga do sábado recebe, nesta ordem, peça com o Bruno no quadro 0: reel de nicho gravado, REACT, remake que passou como Trial Reel, ob. Sem peça, a semana fica com 4 reels e o motivo escrito. Correção do tl02 (10,4 s sem voz real, acima do teto de 8 s [FATO 92]): agência até sex 30/10 23h59, ou o Bruno aceita o risco por escrito.

### P8. mc02 a mc04 e o recorte do mc04

- mc02: dom 25/10 09h01 e mc03: seg 26/10 17h30, **já agendados** [FATO, N1]. Só o Bruno no quadro e na voz [FATO 90].
- mc04: **dom 01/11 09h00**, rótulo "NA TV · SEG, 02/11 · FALTA 1 DIA", agendado pela agência até sáb 31/10. Sai depois do tl02, como manda a regra do laço [FATO, enquadramento item 8].
- Recorte: **1707,82 s** ("profissão"), 7,2 s, dentro da faixa de 7 a 10 s do catálogo e antes de "estrategista digital" (1709,18 s), termo vetado [FATO 96, N12]. O render atual tem 4,60 s [FATO 86]: se a folha mostrar que ele termina numa palavra limpa e passa de 8 na nota, vale; a cadeira de stories decide ouvindo. A minha preferência é 7,2 s, porque fecha a frase "eu construí tudo através da profissão", que é prova de trajetória.

### P9. Marcação da Mirna

| Caminho | Quando usar | Quem | Tempo | Se não der |
|---|---|---|---|---|
| Agendar no PostZen e marcar depois pelo app | Toda peça de feed com imagem ou voz dela: tl01, pb01, car01, pb02, tl02, ci01, po01, tl03, tl04, tl05 e os carrosséis da TV [FATO 90] | Bruno | 1 a 2 min por peça [PRIOR 5] | Se o app não deixar marcar em reel publicado (teste no tl01, dom 25/10 18h35 [a buscar 5]), passa para o @ no texto da legenda, editado no PostZen antes de publicar |
| @ no texto da legenda | Todas as acima, assim que o Bruno tiver o @ | Bruno | 1 min por legenda | Se o @ da API não virar link (conferir no tl01 publicado [PRIOR 1]), fica só a menção em story |
| Menção em story à mão | 3 momentos: dom 25/10 18h35 (tl01), seg 02/11 com o horário, seg 02/11 21h05 (ci01) (F4) | Bruno | 1 min | Story agendado não leva menção [FATO 139] |
| Convite de colaboração (PostZen `collaborators`) | Só no ci01 (02/11), com o @ e o ok dela; tl03 só se ela aceitar o primeiro | Bruno | 2 min | Sem @ ou sem ok: não convida |

Antes de marcar: ela vê o tl04 ("Uau!" recortado no rosto) e o tl05 (carimbo "AINDA?") [FATO 90]; ouvir quem diz "Ainda. Sempre vai ser." no ci01 [FATO 91]. Peça sem ela (mc02 a mc04, car02, car03, nicho, remakes) não leva marcação [HIPÓTESE 37].

### P10. Copy depois de 02/11

- Muda: "Foi ao ar" só depois que o horário confirmado passar [FATO 6]; link da página da edição no site ou no YouTube quando existir (compartilhar link e citar com fonte é permitido [FATO 137]); minuto da edição exibida só depois de o Bruno conferir (os minutos do car01 e do tl01 são da gravação do celular [FATO 81]); bio versão B; legendas de tl03 a tl05 com a linha "A entrevista foi ao ar no dia 02/11, no programa Ser Empreendedor, da TV Câmara Campinas." (F4).
- Continua vetado [FATO 6, 02-provas]: "ao vivo", "rede nacional", "a TV Câmara recomenda", "fui convidado pela TV", "entrevista exclusiva", "A TV me chamou de história de sucesso", "estrategista digital", número de seguidores e de views na tela, logo da emissora, filmar ou recortar a exibição, republicar a edição inteira, anúncio pago com conteúdo da emissora sem autorização escrita.

### P11. 5 reels e 2 carrosséis por semana? Quem faz os carrosséis?

| Semana | Reels | Carrosséis | Máximo de reels num dia | Máximo de posts de feed num dia |
|---|---|---|---|---|
| S1 (25 a 31/10) | 5: tl01, pb01, nicho ou po01, pb02, tl02 (4 se o portão tirar o tl02) | 2: car01, car02 | 1 | 2 (sáb 31/10) |
| S2 (01 a 07/11) | 5: ci01, po01 ou nicho, nicho, "mais votado", tl03 | 2: car03 (dom 01/11), car04 (ter 03/11) | 1 | 2 (ter 03/11 conta 1 de feed; o Trial Reel não entra na grade) |
| S3 (08 a 14/11) | 5: nicho, ob01, REACT ou corte, nicho, tl04 | 2: car05 (dom 08/11), car06 (ter 10/11) | 1 | 1 |
| S4 (15 a 21/11) | 5: nicho, REACT ou nicho, ob03, ob02 ou corte, tl05 | 2: car07 (dom 15/11), car08 (ter 17/11) | 1 | 1 |
| dom 22/11 (abre a S5) | 0 | car09 | 0 | 1 |

Carrosséis: a agência faz os 8 que faltam (car02 a car09), cerca de 36 min cada [ESTIMATIVA, F5 seção 8], **sempre com foto do Bruno na capa** (feed com foto: mediana 111 de alcance e 23 visitas ao perfil; de texto: 34,5 e 1 [FATO 51]). Prazos: car02 e car03 até sex 30/10 23h59; os demais até a sexta 23h59 anterior à semana. Fontes sem gravação [FATO, F5 seção 8]: Os 5 Lances, CARROSSEL 02 a 04 da TV, Seguidor x comprador, Oferta em 5 pilares, Resumo do mês; car03 "Prazer" usa as fotos de marca [FATO 113]. Carrossel não pronto não vira carrossel de texto (texto está em PARAR, n 6, mediana 34,5 [FATO, F7 5.2]): a vaga fecha e o motivo vai para o arquivo da semana.

### P12. Bruno em cena nos 3 primeiros segundos

| Peça | Conferido | Situação |
|---|---|---|
| tl01, tl02, tl03 | Sim, aos 0,6 e 2,5 s [FATO 89] | Ok |
| tl04, tl05 | sem dado (quadros não extraídos) | Agência confere antes de cada portão |
| pb01, po01, pb02, pf01 | Sim desde o quadro 0, de perfil em 3/4, sem olhar para a câmera [FATO 88] | Ok pela letra da regra; formato não medido na conta |
| ci01 | De costas, sem rosto até 2,5 s [FATO 88] | Fere o espírito da regra (rosto e voz). Agência troca os 3 primeiros segundos por um quadro com o rosto dele até sex 30/10 23h59; tempo de render: sem dado. Se não der, sai como está e o motivo vai para o arquivo |
| Dentista C | Selfie com "Dentistas," no quadro 0 [FATO 101] | Ok |
| ob01 a ob03 | De perfil atrás do monitor, braço de camisa azul na borda esquerda [FATO 97] | Ok pela letra; o braço na borda pede ajuste de recorte na folha de 4 quadros por segundo |
| R1 a R3 | Selfie, falando para a câmera [FATO 35] | Ok |
| Cortes do banco e "mais votado" | Bruno no plano CB ou Z2, de perfil ou de costas [FATO 107] | Conferir corte a corte; de costas no quadro 0 não sai |
| Nicho e REACT | Selfie (F5) | Ok |

### P13. Mínimo de gravação por semana

- **Mínimo: 1 bloco por semana com 2 roteiros de nicho no teleprompter, 2 tomadas do gancho cada.** [ESTIMATIVA, F5 seção 9] 12 a 18 min por roteiro, 24 a 36 min por bloco. O bloco 1 acrescenta o vídeo de 02/11 (3 a 5 min) e as versões travadas (consórcio com e sem a linha da ABAC; nutricionista A e B): 31 a 49 min. O bloco 2 acrescenta o REACT (20 min [FATO 106]) depois da exibição.
- **Datas:** bloco 1, **ideal até ter 27/10 23h59** (deixa a agência editar na quarta e o nicho sair na qui 29/10 21h), prazo final qua 28/10 23h59 (nicho vai para a S2). Bloco 2 até qua 04/11 23h59 (psicólogo com e sem a linha da Tzur; advogado só com o provimento da OAB lido, senão consórcio 6; REACT). Bloco 3 até sex 13/11 23h59, pela conferência de qua 11/11. Bloco 4 até qua 18/11 23h59 (S5). Sessão marcada: sem dado [a buscar 20].
- **Piso numa semana apertada:** 1 roteiro (12 a 18 min). No bloco 1: 1 roteiro e o vídeo de 02/11 (15 a 23 min).
- **Semana com zero gravação, em ordem fixa** (F5 seção 10, que adoto): ob01 a ob03 com render aprovado; "o mais votado inteiro"; remakes R1 a R3 como Trial Reel; tl03 a tl05 com portão; cortes do banco (pb03 primeiro); pf01 como reel só com DOBRAR; Case Tzur v2 só com autorização escrita e sem "comenta estrategista"; Dentista C fica fora (P14). Nunca voz sintética, nunca reel sem o Bruno nos 3 primeiros segundos.

### P14. Dentista C e remakes

- **Dentista C: anúncio 4:5 depois de 18/11**, como guarda o brief do dentista, com a Res. CFO 196/2019 conferida [FATO 101]. Não vai ao feed nas 4 semanas: é a 3ª edição da mesma fala (A no ar, B hoje) [FATO 101] e o playbook pede mudar uma coisa por vez [FATO 149]. No direct: só se um dentista que comentou no B pedir mais, o Bruno manda o vídeo pelo celular [HIPÓTESE, confiança baixa].
- **Remakes sem gravar, como Trial Reel pelo app, pelo Bruno**: R1 "Ele nunca fez um anúncio" ter 03/11 14h; R2 "90% dos lançamentos que flopam" ter 10/11 14h; R3 "Problema de equipe" ter 17/11 14h. Cada um com 2 mudanças reais feitas pela agência até a sexta 23h59 anterior (abertura no ápice, corte de 20% a 40%, legenda queimada no R1, legenda do post sem a "saga de 7 dias") [FATO 35, 37, 150]. Elegibilidade a Trial Reel: sem dado; se o app não oferecer, o remake fica no banco e não entra no feed (segunda vida bate o alcance usual só 15% das vezes com original de 2x a 5x [FATO 150]). Se o Trial bater o alcance usual, o Bruno compartilha no feed e ele conta como reel da semana seguinte.
- Por que remake interessa a esta cadeira: Trial Reel vai primeiro a quem não segue [FATO, F5], ou seja, trabalha antes do clique.

### P15. Stories por dia

Molde de dia útil com reel (F6 4.1, que adoto com 3 mudanças desta cadeira):

| Hora | Tipo | O que vai | Como sobe | Fonte da frase |
|---|---|---|---|---|
| 09h00 | Autoridade e bastidor (antes: contagem "NA TV · SEG, 02/11 · FALTAM N DIAS"; depois: "O QUE EU DISSE NA TV") | Bruno em cena: trecho de 10 a 15 s da gravação do celular, manchete mc ou foto | PostZen | transcrição com tempo (02-provas) |
| 12h00 | Quebra de objeção | "O QUE EU MAIS OUÇO" + enquete | À mão | 01-objecoes e mapa F6 9.3 |
| 12h01 | Virada | contra-argumento | PostZen | 01-objecoes |
| 12h02 | Prova | item do 02-provas com tempo | PostZen | 02-provas |
| 12h03 | **Pedido único do dia** | link `/tabuleiro/?o=ig-stories` (com `&p=` em dia de nicho), rótulo **"Teste de 12 casas · 4 min"** | À mão | página do teste [FATO, N7] |
| 17h30 | Frase de efeito | sem pedido | PostZen | banco de 14 frases com fonte (F6 seção 6) |
| 20h30 | Chamada do reel | "SEG · 21H · NO FEED" (dia e hora, nunca "hoje") | PostZen | |
| 21h05 | Compartilhar o reel | com menção à Mirna onde a P9 manda | À mão | |

Total: 8 stories, 3 à mão. Sábado: chamada 17h30 e compartilhamento 18h35; caixa de pergunta no lugar da enquete. Domingo e dia sem reel: 6 stories, 2 à mão. Feriado (15/11 e 20/11): sem enquete; o link fica (1 à mão).

Mudanças desta cadeira: (1) o rótulo do link bate com o destino; (2) em dia de nicho o link leva `&p=<profissão>`, e a profissão chega na mensagem do WhatsApp [FATO 129]; (3) a ETAPAS de story é desligada e nenhum story pede "responde este story" (a automação só dispara com "etapa" e entrega PDF [FATO 118]). O Bruno anota todo dia, antes de expirar, votos da enquete e **toques no link** (o Buzzfy não lê [FATO 67]).

### P16. ob01 a ob03

- **Prazo:** render final, conferência da voz do ob01 (segmento de 1312,5 a 1326,4 s, que o 03-plano marcou com f0 da faixa da Mirna [FATO 98]) e folha de 4 quadros por segundo com nota 8 ou mais por efeito: **agência até sex 30/10 18h**. Ajustar o braço azul na borda [FATO 97].
- **Datas titulares:** ob01 qua 11/11 21h; ob03 qui 19/11 21h; ob02 sex 20/11 21h (feriado). O ob02 repete 82% do áudio do pf01 [FATO 95]: vai por último, longe do story do pf01 (27/10).
- **Reserva:** se não houver gravação, ob01 e ob03 sobem para a S2 (qua 04/11 ou qui 05/11), na ordem da P13.
- **Substituto se não ficarem prontos:** corte do banco pb03 ("eu construí tudo"), depois CINEMA 02, sempre com o Bruno no quadro 0.
- Pedido dos ob: "Me manda a sua área no direct" [FATO 94]; resposta à mão com o link do teste e `&p=`.

### P17. PARAR, MANTER, DOBRAR e TESTAR

| Decisão | Formato | Pedido |
|---|---|---|
| PARAR | Mediana de alcance em 48 h abaixo de 42, ou pulo mediano acima de 75%, **com n de 2 ou mais** do formato | 0 resposta em 2 posts com 106 ou mais de alcance |
| MANTER | 42 a 105 | resposta abaixo de 1 por 100 contas |
| DOBRAR | 106 ou mais com pulo abaixo de 60% (carrossel: também 2 ou mais visitas ao perfil) | 1 ou mais por 100 contas em 2 posts |
| TESTAR | Formato ou pedido com n de 0 ou 1: registra a expectativa, a data de leitura e nunca leva a PARAR | idem |

n mínimo por formato: 2 para PARAR; 3 para a conferência de nicho de 11/11 (com menos: "não testado", nunca PARAR [FATO 169]). Reel lido em feriado não fecha PARAR sozinho.

Datas: seg 26/10 21h05 (Dentista B com 48 h); ter 27/10 18h35 (tl01, extra); **seg 02/11 19h** (Finados: só os agentes leem; o tl02 fecha 48 h às 18h30; a lista do Bruno vence ter 03/11 11h; a rodada não espera a exibição e o funil da TV entra na rodada de 09/11, porque o `ig_account_stats` atrasa até 48 h [FATO 140]); seg 09/11, 16/11 e 23/11 às 19h. Conferências fora da segunda: qua 04/11 (parcial de diagnóstico [FATO 181]), qua 11/11 (nicho), qua 11/11 (saldo de seguidores até 08/11), sex 13/11 (14 dias depois de 27/10) e qua 18/11 (seguidores e diagnóstico).

### P18. TABULEIRO e o caminho até o diagnóstico

- **Antes de dom 25/10 18h30, o Bruno desliga** CASE, ESTRATEGISTA, ETAPAS (comentário), FUNIL, CAIXA e a ETAPAS de story [FATO 114, N4]. Motivo: a série da TV usa "caso" e "estrategista" [FATO, F8 seção 1] e cada comentário aceita uma resposta privada só [FATO 120]; parabéns receberia "onde o seu dinheiro está vazando". As 10 ligadas a posts antigos ficam (0 comentário nesses posts).
- **Onde entra em novembro:** no primeiro reel de nicho publicado depois de 02/11, **se** o anterior da linha de nicho (o Dentista B) fizer 150 ou mais de alcance **e** pulo abaixo de 60% em 48 h (leitura de seg 26/10 21h05). Depois, no máximo 1 post por semana [FATO 171], sempre no próximo reel de nicho cujo anterior passou na mesma régua. Nunca em 02/11, nunca em timelapse ou corte da TV (público frio e sem profissão no link), nunca em story.
- **Forma:** uma automação por post, criada pelo Bruno antes de o post sair, com botão `/tabuleiro/?o=ig-tab-AAMMDD&p=<profissão>` e `linkTracking` ligado. Direct proposto (bate com a página: 5 Lances, 4 minutos, sem cadastro [FATO 129, N7]):
  > Oi! Aqui é o Bruno. O Tabuleiro são 12 perguntas sobre o seu próximo lançamento, em 4 minutos e sem cadastro. No fim aparece em qual dos 5 lances o seu plano está mais vazio. Toca no botão e, se fizer sentido, me manda o resultado no WhatsApp que a gente marca 30 minutos.
- **Teste de ponta a ponta** pelo Bruno antes do primeiro uso, com um perfil de teste anotado (fica fora da contagem).
- **Pedidos de direct das legendas** ("Me manda a data no direct", "Me manda a sua área no direct"): ficam, um por legenda; o Bruno responde no mesmo dia com as 3 perguntas do Módulo 6 [FATO 132] e o link do teste com `&p=`.
- **Como cada etapa é contada (toda segunda):** alcance e pulo do post anterior da linha (`ig_post_stats`); comentários do post; disparos da TABULEIRO por diferença de total entre segundas, sem perfis de teste (`listCommentAutomationLogs`, o log não tem data [FATO 119]); visitas e cliques (`ig_account_stats`); cliques no botão do direct (`linkTracking`, [HIPÓTESE 51]); `tabuleiro_start`, `tabuleiro_complete` e `generate_lead` (GA4, Bruno); mensagens que começam com "Fiz O Tabuleiro no site" e com "Quero agendar o Primeiro Lance" (WhatsApp, Bruno; as duas frases são fixas no código [FATO 129]); directs que citam a TV (Bruno); conversa de 30 min agendada e realizada (Bruno), contada à parte do teste de 12 casas. Sem o número do Bruno: "sem dado".

### P19. O que muda em cada post contra o anterior da mesma linha

| Linha | Sequência | O que muda | O que fica |
|---|---|---|---|
| P&B da entrevista | pb01 (trajetória) para pb02 (caso do restaurante) | assunto | formato, plano em 3/4, placa |
| Timelapse | tl01 a tl05 | assunto de cada parte | formato |
| Nicho falado | Dentista A, B (formato tela dividida, mesmo assunto), consórcio, nutricionista, psicólogo, advogado | depois do B, só a profissão | selfie, letreiro atrás da cabeça, gancho com a profissão no quadro 0 |
| Objeção | ob01, ob03, ob02 | a objeção | formato |
| Carrossel | car01 a car09 | assunto | foto do Bruno na capa, 1 pedido |
| Remake | R1, R2, R3 | 2 mudanças reais cada (exceção escrita: o playbook pede 2 para segunda vida [FATO 150]; Trial Reel não alimenta a leitura da linha) | o assunto original |
| Corte da TV fora da P&B | ci01 (cinema), po01 (pontos) | cada um é o 1º da sua linha | |

### P20. Regras de texto

Conferidas nas legendas e textos que este plano propõe (bio, car01, po01, tl02, direct da TABULEIRO, stories do dia 02/11): sem travessão, sem emoji, sem promessa de resultado, sem os três nomes vetados pelo CLAUDE.md, nenhuma frase "não é X, é Y", nada da lista do 02-provas (inclusive "estrategista digital", que sai da bio), sem logo de terceiro, sem número da conta na tela. O story pf01 v2 ("em dois meses", N2) precisa ser conferido contra o veto "em 2 meses você" do 02-provas: como fato do caso, com a ressalva, pode; como promessa a quem lê, não. Prazo: agência até seg 26/10 12h.

### P21. O que depende só do Bruno

| # | Ação | Prazo |
|---|---|---|
| 1 | Bio versão A e link `/tabuleiro/?o=ig-bio` | dom 25/10 17h |
| 2 | Desligar CASE, ESTRATEGISTA, ETAPAS (comentário), FUNIL, CAIXA e ETAPAS de story | dom 25/10 09h (story) e 18h30 (comentário) |
| 3 | Pôr `&p=dentista` no botão da TABULEIRO do Dentista B | sáb 24/10 20h59 (F8) |
| 4 | Pedir à Mirna o @, o horário da exibição e o print da liberação; perguntar se aceita marcação em série e convite | o quanto antes; @ até dom 25/10 18h30; print até seg 26/10 21h |
| 5 | Testar marcar pessoa no tl01 publicado e ver se o @ da legenda vira link | dom 25/10 18h35 |
| 6 | Gravar o bloco 1 | ideal ter 27/10 23h59; final qua 28/10 23h59 |
| 7 | Mover ci01; decidir po01; editar legendas de pb01, car01, po01, pb02, tl02; apagar ou trocar as chamadas que dependem deles | P5 |
| 8 | Contar votos do tl01 | ter 03/11 12h |
| 9 | Marcações, menções, stickers e compartilhamentos da lista diária, com "feito" ou "não feito" | diário |
| 10 | Trial Reels R1 a R3 pelo app | ter 03/11, 10/11 e 17/11, 14h |
| 11 | Fixar 3 posts; destaque NA TV; bio versão B | dom 01/11 22h; ter 03/11 |
| 12 | Criar cada TABULEIRO de novembro e testar o caminho | antes do post |
| 13 | Dizer se `bruno26111982` é perfil dele | seg 26/10 |
| 14 | Informar toda segunda: GA4 (3 eventos), mensagens das 2 frases fixas no WhatsApp, directs que citam a TV, toques no link do story, conversas agendadas e realizadas | toda segunda até 18h |
| 15 | Disponibilidade no feriado de 02/11 | sex 30/10 |
| 16 | Cópia no Drive do estoque que só existe na pasta temporária [FATO 110] | o quanto antes |

### P22. Etiquetas

Todo número deste plano tem etiqueta. O que falta está escrito "sem dado" (lacunas, seção 11). Os números da seção 9 são previsões [PRIOR] com faixa, para calibrar o conselho, e não entram em decisão nenhuma.

---

## 5. Grade dia a dia e hora a hora (dom 25/10 a dom 22/11)

Legenda: **PZ** já agendado no PostZen [FATO, N1]; **PZ\*** já agendado, o Bruno edita (legenda ou data); **PZ+** novo, o Bruno agenda; **MÃO** o Bruno posta no app; **AG** leitura dos agentes. Dias da semana conferidos no `date`.

### S1 · dom 25/10 a sáb 31/10 (antes da exibição)

**dom 25/10 (faltam 8 dias)**
| Hora | Peça | Tipo | Como | Nota |
|---|---|---|---|---|
| até 09h00 | desligar a ETAPAS de story | automação | Bruno | o story das 09h02 deixa de pedir "responde este story" |
| 09h00 | BASTIDOR · SER EMPREENDEDOR | story | PZ | |
| 09h01 | mc02 | story | PZ | |
| 09h02 | estático 2510-0902 + enquete | story | MÃO | sem a linha "Votou SIM? Responde este story." |
| 12h00 | compartilhar o Dentista B + enquete "Você é dentista?" | story | MÃO | |
| 12h30 | link `/tabuleiro/?o=ig-stories&p=dentista`, rótulo "Teste de 12 casas · 4 min" | story | MÃO | rótulo e `&p=` mudam |
| até 17h00 | bio versão A e link `/tabuleiro/?o=ig-bio` | perfil | Bruno | |
| até 18h29 | desligar CASE, ESTRATEGISTA, ETAPAS, FUNIL e CAIXA | automação | Bruno | |
| 17h30 | DOM · 18H30 · NO FEED | story | PZ | |
| 18h30 | **tl01** | reel | PZ | @ da Mirna na legenda se chegar |
| 18h35 | compartilhar o tl01, menção à Mirna (1ª de 3) | story | MÃO | testar marcar pessoa no reel publicado |
| 21h00 | Dentista B com 24 h e logs da TABULEIRO | leitura | AG | |

**seg 26/10 (faltam 7)**
| Hora | Peça | Tipo | Como | Nota |
|---|---|---|---|---|
| 09h00 | compartilhar o tl01 + enquete | story | MÃO | |
| 12h00 | estático 2610-1200 + enquete | story | MÃO | |
| 12h01 | A VIRADA | story | PZ | |
| 17h30 | mc03 | story | PZ | |
| 17h31 | NA TV · A EQUIPE EXECUTA | story | PZ | |
| 17h32 | link do teste | story | MÃO | rótulo novo |
| 20h30 | SEG · 21H · NO FEED | story | PZ | |
| 21h00 | **pb01** | reel | PZ\* | legenda com a data até 20h59 |
| 21h05 | compartilhar o pb01; marcar a Mirna no pb01 | story e marcação | MÃO | |
| 21h05 | Portão do Dentista B (48 h): linha de nicho e TABULEIRO de novembro | Módulo 7 extra | AG | registrar em `semanas/2026-10-26.md` |

**ter 27/10 (faltam 6)**
| Hora | Peça | Tipo | Como | Nota |
|---|---|---|---|---|
| 09h00 | compartilhar o pb01 + enquete | story | MÃO | |
| 12h00 | **car01** | carrossel | PZ\* | legenda até 11h59: "na gravação", data, só o pedido de direct; marcar a Mirna na capa |
| 14h30 | estático 2710-1430 + enquete | story | MÃO | |
| 14h31 a 14h33 | NA TV · VAI AO AR SEG, 02/11; A VIRADA; CONTEI NA TV | story | PZ | |
| 16h00 | pf01 v2 | story | PZ | conferir "em dois meses" até seg 26/10 12h |
| 16h01 | link do teste com `&p=dentista` | story | MÃO | |
| 18h35 | Portão extra do tl01 (48 h): decide tl02 a tl05 | leitura | AG | |
| 23h59 | Bloco 1 de gravação, prazo ideal | gravação | Bruno | consórcio, nutricionista, vídeo de 02/11 |

**qua 28/10 (faltam 5)**
| Hora | Peça | Tipo | Como | Nota |
|---|---|---|---|---|
| 09h00 | compartilhar o car01 | story | MÃO | |
| 12h00 | estático 2810-1200 + enquete | story | MÃO | |
| 12h00 | decisão da vaga de qui 29/10: nicho aprovado na folha ou po01 fica | decisão | agência e Bruno | |
| 12h01 | A VIRADA | story | PZ | |
| 17h30 a 17h32 | NA TV · TV CÂMARA CAMPINAS; NA TV; CRITÉRIO | story | PZ | |
| 17h33 | link do teste | story | MÃO | |
| 20h29 | apagar "QUA · 21H · NO FEED" | story | Bruno | o ci01 saiu desta data |
| 20h59 | mover o ci01 para 2026-11-03T00:00:00Z | reel | PZ\* | sem reel hoje |
| 21h00 | pb01 com 48 h | leitura | AG | |
| 23h59 | Bloco 1, prazo final | gravação | Bruno | |

**qui 29/10 (faltam 4)**
| Hora | Peça | Tipo | Como | Nota |
|---|---|---|---|---|
| 09h00 | estático 7 "BASTIDOR · Vai ao ar segunda, 02/11." | story | PZ+ | troca o repost do ci01 do 05-manuais |
| 12h00 | estático 2910-1200 + enquete | story | MÃO | |
| 12h01 | A VIRADA | story | PZ | |
| 17h30 | NA TV · VAI AO AR SEG, 02/11 | story | PZ | |
| 17h31 | MÉTODO XEQUE-MATE | story | PZ ou apagar | fica só se o po01 ficar |
| 17h32 | link do teste (com `&p=` se o reel for de nicho) | story | MÃO | |
| 20h30 | QUI · 21H · NO FEED | story | PZ | |
| 21h00 | **reel de nicho gravado (consórcio)** ou **po01** | reel | PZ+ ou PZ\* | nunca vazio |
| 21h05 | compartilhar; marcar a Mirna se for o po01 | story | MÃO | |

**sex 30/10 (faltam 3)**
| Hora | Peça | Tipo | Como | Nota |
|---|---|---|---|---|
| 09h00 | compartilhar o reel de quinta + enquete | story | MÃO | |
| 12h00 | estático 3010-1200 + enquete | story | MÃO | |
| 12h01 | A VIRADA | story | PZ | |
| 12h02 | link do teste | story | MÃO | rótulo "teste" no mesmo dia do "DIAGNÓSTICO · 30 MIN" |
| 17h30 e 17h31 | ALINHAMENTO; DIAGNÓSTICO · 30 MIN | story | PZ | |
| 18h00 | ob01 a ob03: render, voz do ob01, folha com nota 8 ou mais | produção | agência | |
| 20h30 | SEX · 21H · NO FEED | story | PZ | |
| 21h00 | **pb02** | reel | PZ\* | legenda com a data; só o pedido de direct |
| 21h05 | compartilhar o pb02; marcar a Mirna | story | MÃO | |
| 23h59 | tl02 corrigido ou risco aceito; mc04 em 1707,82 s; car02 e car03; abertura do ci01; R1 com 2 mudanças | produção | agência | |

**sáb 31/10 (faltam 2)**
| Hora | Peça | Tipo | Como | Nota |
|---|---|---|---|---|
| 09h00 | compartilhar o pb02 + enquete | story | MÃO | |
| 11h00 | NA TV | story | PZ | |
| 12h00 | **car02 "Os 5 Lances do Xeque-Mate"** (capa com foto; pedido: salvar) | carrossel | PZ+ | |
| 12h00 a 12h02 | O QUE EU MAIS OUÇO; A VIRADA; NA TV · TV CÂMARA CAMPINAS | story | PZ | |
| 12h03 | link do teste | story | MÃO | |
| 17h30 | SÁB · 18H30 · NO FEED | story | PZ | apagar se o tl02 sair |
| 18h30 | **tl02** (portão de ter 27/10) | reel | PZ\* | pedido: seguir |
| 18h35 | compartilhar o tl02; marcar a Mirna | story | MÃO | |
| 19h30 | estático 3110-1930 + enquete TEMPO / MEDO DE ERRAR | story | MÃO | |

### S2 · dom 01/11 a sáb 07/11 (semana da exibição)

| Data | Feed (hora) | Stories (fora do molde) | À mão do Bruno | Leitura |
|---|---|---|---|---|
| dom 01/11 (falta 1) | 12h00 **car03 "Prazer. Eu sou o Bruno."** (capa com foto; pedido: seguir) PZ+ | 09h00 mc04 "NA TV · SEG, 02/11 · FALTA 1 DIA" PZ+; 17h30 frase PZ+ | 09h05 compartilhar o tl02; 12h03 link; contagem com horário e menção, se houver horário; 22h00 fixar car03, R1 e pb02 | 08h30 stories de sábado (AG) |
| **seg 02/11 (Finados, exibição)** | **21h00 ci01** PZ\* (legenda versão A) | 09h00 estático "onde assistir" sem hora PZ+; 17h30 frase literal da TV PZ+; 20h30 "SEG · 21H · NO FEED" PZ+ | 08h30 conferir o horário; story com horário, menção e link `/ao-vivo` (se houver); 12h00 story `/programacao` se o horário seguir sem dado; 12h03 link do teste; depois do horário: "Foi ao ar." e "Chegou pela TV Câmara? Me manda um oi no direct e conta a sua área."; 21h05 compartilhar o ci01 com menção (3ª de 3); convite de colaboração no ci01 se houver @ e ok | **19h00 Módulo 7** (AG; lê a S1; tl02 com 48h30); lista do Bruno até ter 03/11 11h |
| ter 03/11 | 12h00 **car04 "O que eu disse na TV"** (CARROSSEL 02; pedido: direct) PZ+; 14h00 Trial Reel R1 (MÃO) | molde; objeção O14 "TV de Câmara não prova nada" | 09h00 repost do ci01 + enquete; 12h00 enquete; 12h03 link; story com o link da edição quando subir (+ destaque NA TV); 19h00 resultado da votação do tl01 | bio versão B (Bruno) |
| qua 04/11 | 21h00 **po01** (se moveu) ou **nicho** PZ+ | molde; O9 | 3 à mão do molde | 21h ci01 com 48 h (AG); parcial de diagnóstico (Bruno) |
| qui 05/11 | 21h00 **nicho (nutricionista)** ou ob01 PZ+; TABULEIRO só se o 1º nicho depois de 02/11 for este e o B tiver passado | molde; O11 | 3 à mão; criar a TABULEIRO do post, se for o caso | |
| sex 06/11 | 21h00 **"o mais votado inteiro"** PZ+ | molde; O13 | 3 à mão | |
| sáb 07/11 | 18h30 **tl03** PZ (portão de 02/11) | 17h30 chamada; caixa de pergunta no lugar da enquete | 18h35 compartilhar; marcar a Mirna; convite só se ela aceitou o 1º | |

### S3 · dom 08/11 a sáb 14/11

| Data | Feed (hora) | Stories (fora do molde) | À mão do Bruno | Leitura |
|---|---|---|---|---|
| dom 08/11 | 12h00 **car05** (CARROSSEL 03 da TV; capa com foto) PZ+ | O15 só com enquete, sem virada | 2 à mão | |
| seg 09/11 | 21h00 **nicho (psicólogo, bloco 2)**; reserva ob01 PZ+ | molde; rodízio das objeções mais votadas | 3 à mão | **19h00 Módulo 7** (S2; funil da semana da TV) |
| ter 10/11 | 12h00 **car06 "Seguidor x comprador"** PZ+; 14h00 Trial Reel R2 (MÃO) | molde; O7 só depois da conferência das regras do conselho | 3 à mão | |
| qua 11/11 | 21h00 **ob01** (reserva pb03) PZ+ | molde; O10 só se o Bruno confirmar o caso | 3 à mão | **conferência de nicho** (n de 3); saldo de seguidores até 08/11 |
| qui 12/11 | 21h00 **REACT 01** (bloco 2); reserva corte pb03 PZ+ | molde; 1ª objeção mais votada da S1 | 3 à mão | |
| sex 13/11 | 21h00 **nicho (advogado ou consórcio 6, bloco 2)**; reserva ob03 PZ+ | molde; 2ª objeção mais votada | 3 à mão | ganho líquido de 28/10 a 10/11; 23h59 bloco 3 |
| sáb 14/11 | 18h30 **tl04** PZ (portão de 09/11; Mirna viu o recorte) | caixa de pergunta | 18h35 compartilhar; marcar a Mirna | |

### S4 · dom 15/11 a sáb 21/11

| Data | Feed (hora) | Stories (fora do molde) | À mão do Bruno | Leitura |
|---|---|---|---|---|
| dom 15/11 (Proclamação da República) | 12h00 **car07** (CARROSSEL 04 da TV) PZ+ | feriado: sem enquete | 1 à mão (link) | |
| seg 16/11 | 21h00 **nicho (bloco 3, pela conferência de 11/11)**; reserva ob02 PZ+ | molde; rodízio | 3 à mão | **19h00 Módulo 7** (S3) |
| ter 17/11 | 12h00 **car08 "Oferta em 5 pilares"** PZ+; 14h00 Trial Reel R3 (MÃO) | molde | 3 à mão | |
| qua 18/11 | 21h00 **REACT 02 ou nicho (bloco 3)**; reserva corte do banco PZ+ | molde | 3 à mão | **conferência de 18/11** (seguidores e diagnóstico); 23h59 bloco 4 |
| qui 19/11 | 21h00 **ob03** PZ+ | molde | 3 à mão | |
| sex 20/11 (Consciência Negra) | 21h00 **ob02** ou nicho PZ+ | feriado: sem enquete | 2 à mão (link e compartilhar) | |
| sáb 21/11 | 18h30 **tl05** PZ (portão de 16/11; Mirna viu o carimbo) | caixa de pergunta | 18h35 compartilhar; marcar a Mirna | |

### dom 22/11 (abre a S5)

| Hora | Peça | Como | Nota |
|---|---|---|---|
| 12h00 | **car09 "Resumo do mês"** (capa com foto) | PZ+ | decidido no Módulo 7 de 16/11 |
| molde de domingo | 6 stories, 2 à mão | PZ+ e MÃO | |
| seg 23/11 19h00 | Módulo 7 (S4) e decisão da S5 | AG | registrar em `semanas/2026-11-23.md` |

Espaçamento [FATO, F7 e conta de horas]: no máximo 1 reel por dia; Trial Reel de terça às 14h fica 17 h depois do reel de segunda e 31 h antes do de quarta; reel de sábado 18h30 fica 21h30 depois do de sexta. Nenhum dia com mais de 2 posts de feed.

---

## 6. Decisões D1 a D6

Probabilidade de sucesso = chance de cumprir o critério do enquadramento, com as correções do livro de fatos (saídas de 12 a 21/10 são 6; promessa do tl01 já mudou; maior edição tem 1.400 views; base de story é janela móvel; leitura parcial de diagnóstico em 04/11; piso de seguidores é 12 em 14 dias depois de 27/10).

### D1. Série da entrevista em torno de 02/11

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) Manter os 5 nas datas | S1 cheia com 6 reels; S2 vazia de peça pronta | O dia da chegada de quem viu a TV encontra o perfil sem nada novo; a Mirna aparece 7 vezes antes de o trabalho dela ir ao ar só com ok verbal [FATO 4, 5] |
| (b) Mover os 5 para depois | S1 com 2 reels prontos (tl01, tl02) | Vagas da S1 sem peça com o Bruno de frente; seguidores seguem parados na semana em que mais importa aquecer |
| **(c) Dividir pelo papel de cada peça** (minha base) | Ficam os que apresentam o Bruno e o caso; vão o ci01 (depende da exibição) e o po01 (mais perto da oferta, condicional) | O "depois" ganha 2 peças prontas; a S1 cumpre 5; a decisão do po01 obriga o Bruno a gravar até ter 27/10 para tirar a peça da S1 |
| (d) Não mexer agora | Nenhum custo hoje | O ci01 sai qua 28/10 antes de a decisão ser lida; o dia 02/11 fica sem reel |
| (e) Fora do óbvio: **a TV como prova, não como série** | Só 3 cortes no feed (pb01, pb02, ci01); po01 e tl03 a tl05 vão para stories e para a página `/tv/` | Libera 4 vagas de feed para o Bruno de frente (gravação ou remake); depende de gravação, que não existe desde 21/10 |

- **Premissas:** o formato de mesa em 3/4 fica entre a animação e o Bruno de frente [HIPÓTESE]; prova perto do pedido converte mais [PRIOR]; a ok verbal da Mirna vale para publicar antes [sem dado]; o horário chega até a manhã de 02/11 [sem dado].
- **Posição: (c)**, com (e) como saída automática se o Módulo 7 de 02/11 mostrar a família da TV abaixo de 42 com n de 2 ou mais.
- **Probabilidade de sucesso pelo critério:** 0,15 [0,07; 0,30]. Os três números juntos (alcance médio de 42 ou mais por fase, 21 visitas por dia de 02 a 04/11, saldo positivo de 25/10 a 08/11) dependem de um formato sem medida e de um evento sem audiência conhecida. **Confiança:** 0,35.

### D2. Gravação de nicho, Dentista C e remakes

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| **(a) 1 bloco semanal de 24 a 36 min, 2 roteiros** (minha base) | 2 reels de nicho por semana a partir da S2 | n de 3 em 11/11; linha de TABULEIRO com profissão no link |
| (b) 60 a 90 min com 5 roteiros | 5 por semana | O plano de 21/10 era este e não aconteceu [FATO 105]: risco de zero |
| (c) Quinzenal com 10 | Estoque grande | Um bloco perdido apaga 2 semanas |
| (d) Zero gravação | Série da TV e estoque | 18 reels da entrevista em 4 semanas [ESTIMATIVA, F5]; regra 5 do portão sem saída |
| (e) Fora do óbvio: **um roteiro de 10 minutos no dia em que houver 10 minutos** | Sem sessão marcada; a agência mantém a fila pronta | Tira a barreira da "sessão"; perde o lote e a luz igual |

- **Premissas:** o Bruno tem 30 min por semana [sem dado]; reel de nicho com o Bruno de frente repete o 128 a 308 dos 4 que existem [HIPÓTESE 16]; Trial Reel disponível na conta [sem dado].
- **Posição: (a)**, com (e) como regra de piso (se não houver bloco, 1 roteiro avulso vale). Dentista C fica para anúncio depois de 18/11. Remakes como Trial Reel às terças 14h.
- **Probabilidade:** 0,25 [0,12; 0,40]. O ponto fraco é a gravação acontecer. **Confiança:** 0,40.

### D3. Grade, horários, feriados e trabalho à mão

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 5 reels e 2 carrosséis fixos | Ritmo do CLAUDE.md | Pede 8 carrosséis da agência |
| (b) 6 reels na S1 | Cumpre a promessa antiga | A promessa já mudou [FATO 77]: sem motivo |
| (c) 6 a 7 com portão | Mais chance de estouro (7,7% contra 7,0% [FATO 152]) | Mais estoque fraco no feed; o ritmo de 3 por dia não somou seguidores [CLAUDE.md] |
| (d) Grade reduzida sem gravação | Menos peça fraca | Vaga vazia |
| (e) Fora do óbvio: **grade desenhada para o momento da chegada** | 5 e 2, com car03 "Prazer" na véspera, ci01 no dia, 3 posts fixados e todo carrossel com foto | O topo do perfil vira página de entrada para quem vem da TV; o "Prazer" foi o maior gerador de visita ao perfil da fase [FATO 53] |

- **Premissas:** a agência entrega 8 carrosséis (cerca de 4 h 48 min [ESTIMATIVA, 8 x 36 min]); o Bruno faz cerca de 20 stories à mão por semana [ESTIMATIVA, F6]; o recurso de fixar posts existe na conta [PRIOR].
- **Posição: (a) + (e).**
- **Probabilidade:** 0,12 [0,05; 0,25] (0 vaga vazia, mediana de 42 nas 4 semanas e 106 em 2, ganho de 12 em 14 dias depois de 27/10). **Confiança:** 0,35.

### D4. Stories e ob01 a ob03

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 03-plano estendido, 27 à mão por semana | Mais medição | Carga do Bruno acima do que ele entrega [HIPÓTESE] |
| (b) 3 a 5 por dia | Menos carga | Menos views de story, o maior bloco de views da conta [FATO 57] |
| (c) 6 a 8 em 4 blocos (F6) | Molde estável, 3 à mão por dia | Medição diária possível |
| (d) ob nas datas do 03-plano (02, 04, 06/11) | ob02 em 02/11 disputa com o ci01 | Render sem dado |
| (e) Fora do óbvio: **story como página de conversão** | Um pedido por dia, rótulo igual ao destino, toque no link anotado como métrica principal | Liga story a clique, a única ponte de 1 toque até o teste |

- **Premissas:** as views de story se mantêm com 6 a 8 por dia [HIPÓTESE]; o Bruno anota toques antes de expirar [sem dado]; ob passam na folha até sex 30/10 [sem dado].
- **Posição: (c) + (e)**; ob01 qua 11/11, ob03 qui 19/11, ob02 sex 20/11, sobem para a S2 só sem gravação.
- **Probabilidade:** 0,20 [0,10; 0,35]. Views de 982 por semana é provável (hoje 1.159 [FATO, N3]); 6 respostas em 14 dias e ob com média de 42 são incertos. **Confiança:** 0,35.

### D5. Portão do Módulo 7

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| **(a) Alcance em 48 h sobre 53** | Régua fixa | Comparável entre semanas |
| (b) Views sobre 57 | Bate com o `ig_reel_checkup` | Views mistura reassistir; régua anda com a base |
| (c) Alcance sobre 37,5 | Base atual do Buzzfy | A base sobe sozinha quando a animação sai [F7] |
| (d) Mediana refeita a cada rodada | Acompanha a conta | Quebra a comparação |
| (e) Fora do óbvio: **régua de formato mais régua de pedido** | Formato julgado por alcance; pedido julgado por respostas por 100 contas | Para de culpar o formato pelo pedido errado e vice-versa |

- **Premissas:** 48 h é leitura estável o bastante (o Instagram ainda revisa depois [FATO 33]); o Bruno executa a lista até terça 11h [sem dado; base de 21/10: 3 "não" em 8 [FATO 180]].
- **Posição: (a) + (e).**
- **Probabilidade:** 0,20 [0,10; 0,35] (5 rodadas registradas, todas as decisões executadas, nenhum PARAR com n de 1, S4 acima da S1). **Confiança:** 0,40.

### D6. TABULEIRO e o caminho até o diagnóstico

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) Todo post de novembro com 150 | Mais pedidos de palavra | Palavra-chave associada a menos alcance no mercado [FATO 164] |
| (b) Um único post no mês | Pouco ruído | Teto de 1 a 2 comentários |
| (c) (a) ou (b) mais desligar as 6 de conta toda | Tira a colisão com "caso" e "estrategista" | O Bruno responde parabéns à mão |
| (d) Não ligar até testar de ponta a ponta | Zero risco de direct errado | Zero disparo |
| (e) Fora do óbvio: **porta sem comentário** | Bio e story levam ao teste em 1 toque; TABULEIRO vira exceção com portão | O caminho principal deixa de depender de comentário (0,35 por 100 contas) |

- **Premissas:** quem vem da TV entra pelo perfil e pela bio, não pelo comentário [HIPÓTESE 45]; o teste de 12 casas qualifica quem pensa em lançar [HIPÓTESE]; o Bruno informa os números do GA4 e do WhatsApp [sem dado].
- **Posição: (c) + (e)**, com TABULEIRO só depois de 02/11, só em nicho, com portão de 150 e pulo abaixo de 60%, no máximo 1 por semana, e o critério de sucesso somando testes concluídos e mensagens "Fiz O Tabuleiro".
- **Probabilidade pelo critério do enquadramento** (3 disparos de terceiros até 22/11 e 1 diagnóstico até 18/11): 0,07 [0,03; 0,15]. O critério conta só a porta de maior fricção. **Confiança:** 0,40.

---

## 7. Ideias e hipóteses numeradas (85)

Confiança: alta, média ou baixa. Evidência ao lado.

**A. Perfil como página de entrada**
1. Trocar "Estrategista Digital" por "Estrategista de Lançamento" na 1ª linha da bio. Alta. Termo contaminado [FATO, N12]; o site e a placa dizem "de Lançamento" [FATO 88].
2. Link da bio para `/tabuleiro/?o=ig-bio`. Média. Aprovado no Módulo 2 e não aplicado [FATO 132]; 29 vezes mais leve [FATO, N6, N7]; resultado chega ao WhatsApp com nota e gargalo [FATO 129].
3. Linha da TV na bio desde 25/10. Média. Data com fonte [FATO 1]; quem vem da TV procura pelo perfil [HIPÓTESE 45].
4. Uma só mudança de bio e link até 23/11, julgada só depois de 150 visitas acumuladas. Alta (método). 77 visitas por semana [FATO, N3].
5. Fixar car03, R1 e pb02 no topo na véspera. Média. Feed com foto do Bruno: 23 visitas contra 1 [FATO 51]; recurso de fixar [PRIOR].
6. Toda capa de carrossel com foto do Bruno. Alta. 111 contra 34,5 de alcance [FATO 51].
7. Carrossel "Prazer" na véspera da TV. Média. "Prazer, mineiro" teve 19 visitas e o único seguidor atribuído [FATO 53].
8. Destaque NA TV a partir de 03/11, com o link da edição. Média. PROVA não existe [FATO 64]; link permitido [FATO 137].
9. Não arquivar os 12 reels sintéticos agora. Média. Efeito na base do Buzzfy: sem dado; fixar resolve o topo sem mexer na base.
10. Não pôr botão de WhatsApp no perfil agora. Baixa. Pula o teste e perde nota e gargalo [FATO 129]; disponibilidade em conta de criador [PRIOR].
11. Manter o nome "Bruno Israel Gonçalves". Baixa. Se a TV mostra o @ ou o nome: sem dado [a buscar 34].
12. Bio versão B em 03/11 ("Entrevista na TV Câmara Campinas"), sem "foi ao ar". Alta. Veto de "foi ao ar" antes do horário confirmado [FATO 6].

**B. Página e caminho**
13. A `/v2/` não serve para tráfego do Instagram: 7,3 MB e 129 quadros. Alta. [FATO, N6]
14. [ESTIMATIVA, premissa de 5 Mbit/s no 4G] A `/v2/` leva cerca de 1,5 s até o aviso sair e cerca de 11,7 s para baixar inteira; a `/tabuleiro/` cerca de 0,4 s. Média.
15. O seletor "v1 · imersiva / v2 · cinema" no menu tira credibilidade. Baixa. [FATO, N5]; efeito sem dado.
16. "Agendar" sem agenda on-line cria expectativa que o WhatsApp não cumpre. Baixa. [FATO 128]; [PRIOR].
17. A oferta da `/v2/` aparece só no fim, depois de 6 botões. Média. [FATO, N5]
18. Página em caminho próprio `/tv/` para separar a origem nos eventos. Média. `page_origin` grava só o caminho [FATO, N9].
19. Linha da TV com foto do Bruno acima das perguntas da `/tabuleiro/`. Média. Página sem foto e sem TV [FATO, N7].
20. Sufixo de origem na mensagem do WhatsApp (por exemplo "(ig-bio)"). Média. A origem nunca entra [FATO 129].
21. Chamar o teste de "teste de 12 casas" e a conversa de "conversa de 30 minutos". Alta. "Diagnóstico" nomeia as duas [FATO 131].
22. Rótulo do link do story "Teste de 12 casas · 4 min". Alta. Mesmo motivo; story "DIAGNÓSTICO · 30 MIN" na sex 30/10 [FATO, N1].
23. Direct da TABULEIRO com "5 lances". Alta. Promessa de 4 etapas contra 5 Lances [FATO, N4; fato 129].
24. `&p=<profissão>` em todo link de nicho. Alta. A profissão entra na mensagem [FATO 129].
25. Ligar o `linkTracking` na TABULEIRO de novembro. Média. Hoje false [FATO 114]; o que passa a mostrar [HIPÓTESE 51].
26. Tirar das páginas de entrada o rodapé que leva a outra marca. Baixa. [FATO, N10]; efeito sem dado.
27. Foto do Bruno da `/primeiro-lance/` tem 4 KB. Baixa. [FATO, N8]; nitidez no celular sem dado.
28. Não reformar a página antes de haver demanda. Alta (ponto cego). Seção 2.

**C. Automações**
29. Desligar as 5 de comentário de conta toda antes do tl01. Alta. Colisão com "caso" e "estrategista" [FATO 114; F8].
30. Desligar a ETAPAS de story antes de dom 25/10 09h. Alta. 0 disparo e entrega PDF [FATO 118].
31. TABULEIRO por post, não de conta toda. Média. Mantém a profissão e o texto do nicho [FATO 129]; custo de uma automação por post.
32. TABULEIRO só em nicho. Média. Público de nicho é o Tier 1 [HIPÓTESE, F8]; corte da TV não tem profissão.
33. Nunca TABULEIRO em 02/11. Alta. Pedido de palavra a quem não confia vira zero [FATO 171].
34. As 10 ligadas a posts antigos ficam. Média. Posts com 0 comentário [FATO, F8].
35. Perfis de teste fora da contagem. Alta. O único disparo pode ser teste [FATO 116].
36. Teste de ponta a ponta antes do 1º uso. Alta. Caminho nunca usado por terceiro [FATO 116, 117].

**D. Pedido (a oferta de cada post)**
37. Um pedido por legenda: car01 só com direct. Média. Pedido de direct leva à conversa [FATO, F8 seção 6].
38. po01: "Comenta qual delas" e resposta à mão com o link do teste. Média. "Comenta a palavra" não diz qual [FATO 80].
39. tl02: pedido de seguir na véspera. Média. Seguir 1,12x [FATO 148]; dois tl seguidos pedindo número.
40. ci01 versão A: "Segue o perfil". Média. Playbook e F4.
41. Story "Chegou pela TV Câmara?" depois da exibição. Alta. Única atribuição possível [FATO 129, N9].
42. Régua de pedido separada da régua de formato. Média. Pedido de palavra com 169 de alcance teve 0 comentário [FATO 122].
43. "Me manda a data no direct" qualifica por prazo de lançamento. Média. [FATO 80]; efeito sem dado.
44. Palavra-chave tende a cortar alcance. Média. 0,043x contra 0,081x [FATO 164].
45. Pergunta aberta rende mais comentário que palavra com alcance parecido. Média. [HIPÓTESE 60; FATO 123]
46. Pedido de salvar no carrossel de método. Média. Salvar 1,16x [FATO 148].
47. ci01 tem dois pedidos (falado e escrito). Baixa. [FATO 94]; aceitar, porque o falado é enviar.
48. Nenhum pedido de "responde este story". Alta. ETAPAS só com "etapa" [FATO 118].

**E. Série da TV**
49. ci01 para 02/11 21h. Alta. Frase anunciada para 02/11 [FATO 58]; Mirna em 10,7 s [FATO 90]; semana vazia [FATO, N1].
50. po01 condicional ao nicho gravado. Média. Ponto cego compensado (seção 2).
51. pb01, car01 e pb02 ficam. Média. Apresentam o Bruno e o caso; S1 precisa de 5.
52. A TV é prova, não motor de alcance. Média. Cortes crus de TV 0,0055x [FATO 155].
53. Três menções em story, marcação à mão no feed. Média. [FATO 139]; F4.
54. Convite de colaboração só no ci01. Média. Precisa do @ e do ok [FATO 139].
55. mc04 em 1707,82 s. Média. Fecha a frase antes de "estrategista digital" [FATO 96].
56. Corrigir o trecho de 10,4 s sem voz do tl02. Média. Acima do teto de 8 s [FATO 92].
57. Abertura do ci01 com o rosto do Bruno. Média. De costas até 2,5 s [FATO 88].
58. "Na gravação" no car01. Alta. Minutos do celular [FATO 81].
59. "Foi ao ar" só depois do horário confirmado. Alta. [FATO 6]
60. Nada de filmar a exibição ou usar logo da emissora. Alta. Termos [FATO 137]; CLAUDE.md.

**F. Demanda e gravação**
61. Bloco 1 até ter 27/10 23h59. Média. Deixa o nicho entrar na S1 [F5].
62. Vídeo de 02/11 gravado sem hora falada. Alta. Horário sem dado [FATO 133].
63. REACT no bloco 2, depois da exibição. Média. "Fui ao ar" só depois [FATO 6]; criador contando a entrevista: 0,90x (n 1) [FATO 157].
64. Remakes como Trial Reel às terças 14h. Média. Vai a quem não segue [F5]; espaçamento de 17 h [F7].
65. R1 sem a "saga de 7 dias" na legenda. Alta. Saga acabou em 09/10 [FATO 37].
66. Dentista C para anúncio depois de 18/11. Média. Brief do dentista [FATO 101].
67. Primeiro TABULEIRO de novembro no primeiro nicho depois de 02/11. Média. F8 R5.
68. Nunca animação com voz sintética. Alta. 32,5 de alcance e 83,9% de pulo [FATO 27].
69. Aberturas "Pois é" e "Bom" nos cortes podem pesar no pulo. Baixa. 0 de 28 cortes de entrevista no mercado abrem assim [FATO 165]; o preâmbulo funcionou com o Bruno de frente [FATO 38].
70. Remake bate o alcance usual só 15% das vezes com original de 2x a 5x. Alta (é dado do playbook). [FATO 150]
71. Cortes do depois com o ápice no quadro 0. Média. Abrir no ápice: história +4,8 pontos [FATO 147].
72. Reel pronto de reserva para o dia em que um estourar. Média. Sequência 1,81x [FATO 149].

**G. Medição**
73. Base de story fixa: janela de 7 dias lida na seg 26/10 às 19h. Alta. Janela móvel de 982 a 1.159 [FATO 56, N3].
74. Leitura diária da pilha de stories às 08h30. Alta. Métrica some em 24 h [FATO 67].
75. GA4 toda segunda pelo Bruno: `tabuleiro_start`, `tabuleiro_complete`, `generate_lead`. Alta. [FATO 130]
76. Contar no WhatsApp as 2 frases fixas. Alta. [FATO 129]
77. Contar directs que citam a TV de 02 a 08/11. Alta. [F8]
78. Visitas ao perfil por dia de 02 a 04/11 com `days 1`. Média. Atraso de até 48 h [FATO 140].
79. Saldo de seguidores até 08/11 só em 11/11. Alta. 2 dias pendentes [FATO 140].
80. Reel em feriado não fecha PARAR sozinho. Média. F7.
81. Contar conversa de 30 min à parte do teste. Alta. [FATO 131]
82. Toques no link do story anotados pelo Bruno. Média. O Buzzfy não lê [FATO 67].
83. Views da página da edição do Bruno no site até 09/11. Média. Mediana 80,5, máximo 1.400 [FATO 136, 178].
84. Linha "executado: sim ou não" em toda decisão. Alta. Base de 21/10 com 3 "não" [FATO 180].
85. Critério do D6 somando testes concluídos e mensagens "Fiz O Tabuleiro". Média. O critério atual mede só a porta de maior fricção (seção 2).

---

## 8. Pre-mortem da cadeira: como este plano fracassa

1. **O Bruno não grava.** Nada desde 21/10 [FATO 104]. A S1 fica com o po01 na qui 29/10, a S2 a S4 com cortes de mesa em 3/4 e ob; a família da TV cai abaixo de 42 com n de 2 em 02/11 ou 09/11 e não há peça com o Bruno de frente para entrar. O plano vira o plano (d) do D2 sem ter escolhido.
2. **A TV traz quase ninguém.** Edição local, feriado, audiência sem dado; 80,5 views de mediana no site [FATO 136]. A bio nova e o link novo ficam sem tráfego para mostrar efeito, e a cadeira lê ruído como resultado.
3. **Eu mudei tudo de uma vez.** Bio, link, automações e legendas mudam no mesmo fim de semana. Se os cliques subirem ou caírem, não dá para dizer o que causou. Mitigação escrita: o pacote é lido como um todo, e nenhuma segunda mudança entra antes de 23/11.
4. **O teste afasta quem veio da TV.** O público do Ser Empreendedor é dono de negócio local; o teste pergunta de isca, evento e carrinho [FATO, N7]. Quem não lança sai na 1ª pergunta. Se em 09/11 os cliques forem 0 de novo, a hipótese de qualificar pelo teste cai, e a bio volta para uma página de conversa (`/primeiro-lance/`).
5. **Carga à mão acima da capacidade.** Cerca de 20 stories por semana, marcações, compartilhamentos, Trial Reels, fixar, automações, votos, GA4, WhatsApp. No feriado de 02/11 o Bruno some e o dia sai só com o agendado.
6. **A Mirna ou a produção pedem para tirar algo antes de 02/11.** O ok é verbal [FATO 4]; a regra escrita pede ok da produção [FATO 5]. pb01, car01 e pb02 saem antes.
7. **Trial Reel não existe para a conta.** A falha só aparece na hora de publicar [FATO 139]; os 3 remakes ficam no banco.
8. **Agência sem folga.** 8 carrosséis, 3 ob, mc04, tl02, abertura do ci01, remakes e 41 estáticos de story [FATO 61]. As peças "opcionais" de página nunca saem, o que é aceitável; os carrosséis atrasam, o que não é.
9. **Medição cega depois do clique.** O Bruno não informa GA4 e WhatsApp; D6 fica "sem dado" e o conselho decide no escuro.
10. **Interpretação da regra da palavra.** Alguém lê "uma por mês" como "um post por mês" e trava o TABULEIRO no Dentista B; ou lê como "todo post com 150" e espalha palavra no feed frio.

---

## 9. Previsões numéricas com data de conferência

D = dom 25/10/2026. D+30 = ter 24/11/2026; D+60 = qui 24/12/2026; D+90 = sáb 23/01/2027. Todas [PRIOR], com faixa.

| # | Métrica | Previsão | Faixa | Fonte da leitura | Conferir em |
|---|---|---|---|---|---|
| 1 | Seguidores (`followersNow`) | 1.640 | 1.605 a 1.700 | `ig_account_stats` | ter 24/11/2026 (D+30) |
| 2 | Saldo de seguidores de 25/10 a 08/11 | +6 | -4 a +25 | `ig_follower_growth` | qua 11/11/2026 |
| 3 | Ganho líquido de 28/10 a 10/11 (piso do brief: 12) | +7 | -3 a +25 | `ig_follower_growth` | sex 13/11/2026 |
| 4 | Visitas ao perfil em 7 dias, lidas seg 09/11 19h | 120 | 70 a 300 | `ig_account_stats` days 7 | seg 09/11/2026 |
| 5 | Cliques no site em 30 dias | 8 | 2 a 25 | `ig_account_stats` | ter 24/11/2026 (D+30) |
| 6 | Cliques sobre visitas em 30 dias (base 1,57%) | 2,0% | 0,7% a 5% | `ig_account_stats` | ter 24/11/2026 (D+30) |
| 7 | Disparos de TABULEIRO de terceiros, acumulado | 1 | 0 a 4 | `listCommentAutomationLogs` | seg 23/11/2026 |
| 8 | Conversas de 30 min agendadas de 25/10 a 18/11 | 1 | 0 a 3 | número do Bruno (sem ele: sem dado) | qua 18/11/2026 |
| 9 | Mediana de alcance em 48 h dos reels da série da TV de 25/10 a 21/11 | 60 | 35 a 120 | `ig_post_stats` | seg 23/11/2026 |
| 10 | Mediana de alcance em 48 h dos reels de nicho gravados (n de 3) | 120 | 60 a 200 (sem gravação: não testado) | `ig_post_stats` | qua 11/11/2026 |
| 11 | Views de story em 7 dias, lidas às 19h | 1.100 | 750 a 1.600 | `ig_account_stats` days 7 | seg 23/11/2026 |
| 12 | Views da página da edição do Bruno no site da TV | 110 | 30 a 600 (sem dado se não publicada) | tvcamaracampinas.com.br | seg 09/11/2026 |
| 13 | Seguidores | 1.665 | 1.600 a 1.800 | `ig_account_stats` | qui 24/12/2026 (D+60) |
| 14 | Conversas de 30 min agendadas, acumulado desde 25/10 | 2 | 0 a 6 | número do Bruno | qui 24/12/2026 (D+60) |
| 15 | Seguidores | 1.690 | 1.590 a 1.900 | `ig_account_stats` | sáb 23/01/2027 (D+90) |
| 16 | Cliques no site em 30 dias | 8 | 2 a 30 | `ig_account_stats` | sáb 23/01/2027 (D+90) |

---

## 10. O que mudaria minha opinião

- **Cliques de 09/11 em 3 ou mais por semana com visitas parecidas às de hoje:** a página pesava mais do que eu dei; abro a fila de página (caminho `/tv/`, foto, linha da TV) antes de 16/11.
- **Visitas ao perfil de 02 a 04/11 acima de 63 com 0 clique:** o problema passou a ser a bio ou o teste; troco o link para `/primeiro-lance/` na seg 09/11 e mudo uma coisa só.
- **Família da TV com mediana de 106 ou mais e pulo abaixo de 60% em 02/11:** a TV é motor de alcance, e não só prova; adoto a opção (a) do D1 para o depois (mais cortes, inclusive do banco) e a exceção de sequência.
- **Dentista B com 150 ou mais e pulo abaixo de 60%, mais comentários "tabuleiro" de terceiros:** a palavra rende nesta conta; a TABULEIRO vai a todo nicho que passar, no máximo 1 por semana.
- **Mirna ou produção vetarem publicação antes de 02/11:** passo para a opção (b) do D1 e a S1 vira Bruno de frente, remakes e nicho.
- **Trial Reel indisponível:** os remakes saem do plano; não entram no feed como repost.
- **O Bruno informar que já tem diagnósticos vindo de fora do Instagram:** o funil da conta pesa menos na meta de 10, e a cadeira reduz o trabalho de página a zero.

---

## 11. Lacunas

- Horário da exibição em 02/11 e se a edição reprisa na semana: sem dado (grade só até 25/10 [FATO 133]).
- Audiência da TV e se o programa mostra o @ ou o nome do Bruno: sem dado.
- @ da Mirna, aceite de marcação em série e de colaboração, print da liberação: sem dado.
- Se o app deixa marcar pessoa em reel publicado; se o @ da legenda pela API vira link: sem dado (teste em 25/10).
- Elegibilidade da conta a Trial Reel: sem dado.
- Recurso de fixar posts na conta: [PRIOR], conferir no app.
- Gravação: sessão marcada e minutos reais por roteiro: sem dado.
- Números do GA4, mensagens no WhatsApp, conversas agendadas e realizadas: sem dado para os agentes.
- Toques no link dos stories e votos de enquete: só o Bruno vê.
- Quem é `bruno26111982`: sem dado.
- Velocidade real da `/v2/` e da `/tabuleiro/` num celular no app do Instagram: sem dado (medi bytes e tempo até o primeiro byte deste servidor, N6, N11).
- Se o teste de 12 casas afasta o dono de negócio local que veio da TV: sem dado.
- Render final e voz de ob01 a ob03; quadros de tl04 e tl05 nos 3 primeiros segundos; tempo de render para a abertura do ci01: sem dado.
- Status das leituras de OAB, CFN 856, ABAC, CFP e CFO 196/2019: sem dado.
- Alcance da conta em feriado com reel do Bruno: sem dado.
- Se "em dois meses" no pf01 v2 é fato do caso ou promessa: conferir (N2).
- Onde fica o site (`site-build`): não está neste repositório; quem publica mudança de página: agência, prazo e acesso sem dado.

---

## 12. Fontes

- **Conferências desta cadeira, 24/10/2026, 17h03 a 17h12 (São Paulo), só leitura:**
  - PostZen `listPosts`, accountId j97772ycndetk3f1wcdbh14p898g4b8w, de 2026-10-24T03:00Z a 2026-12-01T03:00Z, sortBy scheduledFor, limit 100: 48 itens (17h10).
  - PostZen `listCommentAutomations`, mesma conta (17h11).
  - Buzzfy `ig_account_stats`, days 7, período 17/10 20h11 UTC a 24/10 20h11 UTC (17h11).
  - GET em https://estrategistadelancamento.com.br/v2/, /tabuleiro/?o=ig-tabuleiro, /primeiro-lance/ e / (17h03); /js/main.js?v=2026-10-22, /js/cinema.js, /js/tabuleiro.js?v=2026-10-22 (17h04); /v2/frames/manifest.json e os 129 quadros /v2/frames/s1-001.jpg a s1-129.jpg (17h05 a 17h08); cabeçalhos de /v2/frames/s1-001.jpg e /vendor/gsap.min.js; tamanho de /vendor/gsap.min.js, /vendor/ScrollTrigger.min.js, /vendor/lenis.min.js, /js/heroes.js, /css/style.css e /assets/bruno-autor.jpg. Nenhum formulário enviado, nenhum teste respondido.
  - `date` do sistema para os dias da semana de 25/10/2026 a 23/01/2027.
- **Repositório:** `/home/user/Disparo-/CLAUDE.md`; `conteudo/modo-god-cronograma/contexto.md`; `run/00-enquadramento.md`; `run/01-fatos.md` (fatos 1 a 185, a buscar 1 a 43, derivados 1 a 33, palpites 1 a 62); `run/01-pesquisa/F1-auditoria-conta.md` a `F8-funil-diagnostico.md`; `conteudo/stories-objecoes/02-provas.md` (seção "O que NÃO pode ser dito"), `05-manuais-bruno.md` e `06-agenda-postzen.md`.
- **Terceiros citados via livro de fatos:** playbook e biblioteca do Buzzfy (fatos 144 a 167); site e termos da TV Câmara Campinas (fatos 133 a 138); Meta, IG User Media (fato 66); Wikipédia, Feriados no Brasil (fato 3).
