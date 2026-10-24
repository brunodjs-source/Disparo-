# Plano da cadeira L · Primeiros princípios · Cronograma de 25/10 a 22/11/2026 · @o_estrategista.com.br

Sábado, 24/10/2026, escrito entre 17h40 e 18h40 (horário de São Paulo). Trabalho isolado: não li nenhum plano de outra cadeira nem a pasta G-quadros.

| Campo | Texto |
|---|---|
| Persona | Pensador que remonta o problema do zero e questiona a pergunta |
| OTIMIZA PARA | Resolver a pergunta certa |
| PONTO CEGO | Descartar o que já funciona. Compensação escrita na seção 2.3: tudo o que já mediu bem ou já está agendado fica, e cada mudança traz o motivo e o custo |
| PERGUNTA CONTRÁRIA | E se a pergunta do Bruno estiver errada? Resposta na seção 2 |

**Etiquetas:** [FATO, fonte] dado lido; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, nível 4, que nunca fecha objeção sozinho. Métrica que falta: "sem dado". Nada foi publicado, agendado, alterado ou enviado. Toda mudança abaixo é uma ação do Bruno, com prazo.

**Lido:** `contexto.md`, `run/00-enquadramento.md`, `run/01-fatos.md` (185 fatos), o resumo das frentes F1 a F8 dado na tarefa, `CLAUDE.md`, `stories-objecoes/02-provas.md` (vetos), `03-plano-7-dias.md` (começo), `05-manuais-bruno.md`, `06-agenda-postzen.md`, `sistema-instagram/semanas/2026-10-21.md`, `00-SISTEMA.md` (Projeção), fichas `videos/tv-camara/cortes/*.spec.json` (ob01 a ob03, mc02, mc04, pf01, ci01).

---

## 0. Conferências próprias desta cadeira (só leitura, 17h41 a 17h47)

O livro de fatos foi fechado às 15h50. Desde então a agenda mudou. Estes fatos são novos ou atualizam o livro:

| # | Fato novo | Fonte | Hora | Pesa em |
|---|---|---|---|---|
| L1 | O PostZen tem agora 48 itens de 24/10 a 01/12: 5 stories publicados (14h00, 14h03, 15h00, 15h01, 16h30) e 43 agendados. Eram 20 às 15h46 | PostZen `listPosts`, conta j97772ycndetk3f1wcdbh14p898g4b8w | 17h41 | D3, D4 |
| L2 | Entraram 28 stories sem sticker de 25 a 31/10 (registro em `06-agenda-postzen.md`, commit eeb4f21 às 17h06). A S1 de stories já está agendada | `listPosts` e git log | 17h41 | D4 |
| L3 | O story pf01 (ter 27/10 16h) agora usa `pf01-dentista-story-v2.mp4` ("em dois meses", troca de transcrição registrada na ficha do ob02) | `listPosts` e `03-plano-7-dias.json` | 17h41 | D1, D4 |
| L4 | A S1 continua com 6 reels (tl01, pb01, ci01, po01, pb02, tl02) e nada agendado de dom 01/11 a sex 06/11 no feed | `listPosts` | 17h41 | D1, D3 |
| L5 | O mc02 do PostZen (dom 25/10 09h01) tem 1.370.775 bytes, igual ao `tv/ig/mc02.mp4` local de 4,27 s, a versão que começa em "Eu" | HEAD e `stat`, `ffprobe` | 17h45 | D1 |
| L6 | O mc04 local tem 4,60 s (render) e 4,608 s (versão ig); a ficha corta em 1700,967 a 1705,567 s, manchete "Eu construí patrimônio, eu construí família.", sem "estrategista digital". Não está no PostZen | `mc04.spec.json`, `ffprobe` | 17h46 | D1 |
| L7 | ob01, ob02 e ob03 já têm render final: 17,9 s (16h33), 28,37 s (15h54) e 15,1 s (17h00). Nenhum está no PostZen | `find`, `stat`, `ffprobe` | 17h45 | D4 |
| L8 | Quadros aos 0, 0,6 e 2,5 s de ob01 a ob03: o Bruno está em cena, de perfil virado para a esquerda, atrás do monitor, com o cartão "OBJEÇÃO · VOCÊ DIZ" no topo desde o quadro 0. Em nenhum quadro ele está de frente para a câmera | folha `scratchpad/cadeiraL/ob_folha.png` | 17h47 | D2, D4 |
| L9 | 7 dias (17/10 20h44 a 24/10 20h44 UTC), sem anúncio: alcance 577 (215 seguidores, 362 não seguidores); views 2.073 (story 1.178, reel 448, post 280, carrossel 165); 77 visitas ao perfil; 0 clique no site; 0 toque em link; 3 respostas; 2 comentários; 4 compartilhamentos; 0 salvamento; seguindo 3.529 | Buzzfy `ig_account_stats` days 7 | 17h44 | D1, D4, D6 |
| L10 | Pilha de stories de hoje, provisória: 09h33 (sem o Bruno visível) alcance 45 e 57 views com 8,2 h; st01 14h00 36 e 46; estático 14h03 34 e 42; 15h00 25 e 32; mc01 15h01 22 e 35, com 1 visita ao perfil; 16h30 11 e 16 com 1,2 h. 0 resposta em todos | `ig_posts` stories e `ig_post_stats` | 17h44 | D4 |
| L11 | Seguidores: 22 e 23/10 seguem pendentes; de 10 a 21/10, 5 entradas e 7 saídas (de 12 a 21/10, 1 e 6, igual ao livro) | `ig_follower_growth` days 14 | 17h41 | D1, D3 |

Consequência direta: a base de story da janela móvel de 7 dias cresce ao longo do dia (982 às 14h11, 1.041 às 15h30, 1.178 às 17h44). Comparar semana com semana só vale lido na mesma hora de segunda.

---

## 1. Veredito (12 linhas)

1. A pergunta "antes ou depois de 02/11" é a pergunta errada. O que move alcance aqui é o Bruno falando de frente para a câmera: 167,5 contra 32,5 de alcance, 4 de 4 reels entre 3,61x e 10,14x [FATO, F1 e F2]. A data não mediu nada ainda.
2. 02/11 é trava de texto ("vai ao ar" antes, "foi ao ar" só com horário confirmado) e um pico de visitas provável e pequeno: as edições do programa no site têm mediana de 80,5 views [FATO, F4]. Não é o eixo do mês.
3. O Bruno já respondeu o D1: "pode seguir". Os 5 cortes ficam nas datas. Mudo só 3 coisas, com motivo: tl02 de sáb 31/10 para dom 01/11 18h30 (S1 volta a 5 reels e o tl02 vira a véspera); po01 perde "Comenta a palavra"; ci01 só sai com a voz de "Ainda. Sempre vai ser." conferida.
4. No dia 02/11, o que pesa é o perfil que o visitante da TV encontra: bio, 3 posts fixados com o rosto do Bruno, destaque NA TV. Chamada só em story, com a hora quando houver fonte. Reel no dia só se for selfie gravada.
5. Depois de 02/11, "o que eu disse na TV" é contado pelo Bruno de frente, em selfie de 30 a 45 s, sem trava de conselho. O "mais votado" do tl01 sai ter 03/11 21h.
6. Gravação mínima: 2 falas por semana, 24 a 36 min [ESTIMATIVA, F5]; a primeira até qua 28/10 23h59. Semana sem gravação: ordem fixa, no máximo 4 reels, nunca voz sintética.
7. Régua única do começo ao fim: 53 de alcance em 48 h (27, 42, 106, 150; pulo 60% e 75%). Peça se decide com n de 1; formato só com n de 2 ou mais.
8. TABULEIRO: o Dentista B fica com outubro; em novembro, um post só, a primeira selfie de nicho. As outras 15 automações de comentário desligam antes do tl01.
9. As metas do enquadramento estão perto do teto do volume da conta: dou de 0,08 a 0,30 de chance por decisão. 10 diagnósticos por mês pedem 637 visitas ao perfil com 100% de conversão depois do clique, e o ritmo orgânico é de cerca de 317 [ESTIMATIVA, derivar 14]. O calendário é necessário e não basta.

---

## 2. A pergunta contrária: e se a pergunta do Bruno estiver errada?

### 2.1 Remontando do zero

O objetivo do sistema é diagnóstico (10 por mês) [FATO, contexto]. A cadeia que leva até lá, com os números de hoje:

| Elo | Número de hoje | Fonte |
|---|---|---|
| Contas alcançadas por semana, sem anúncio | 577 (362 não seguidores) | [FATO, L9] |
| Visitas ao perfil por semana | 77 | [FATO, L9] |
| Cliques no site por semana | 0 (7 em 30 dias, 1,57% das visitas) | [FATO, L9 e fato 14] |
| Toques em link | 0 | [FATO, L9] |
| Disparos de automação de terceiros | 0 (o único é provável teste do Bruno) | [FATO, fato 116] |
| Conversas comerciais no direct | 0 em 50 conversas | [FATO, fato 124] |
| Diagnósticos agendados | sem dado | só o Bruno |

Três coisas saltam quando se remonta assim.

**Primeira: o elo que mais muda o resultado não é a data, é o formato.** Bruno falando para a câmera tem mediana de 167,5 de alcance e 48,1% de pulo; animação sintética, 32,5 e 83,9% [FATO, fatos 25 e 27]. Os cortes da TV, todos, mostram o Bruno de perfil em 3/4, de costas ou atrás do monitor, nunca de frente [FATO, fato 88 e L8]. É um formato que a conta nunca mediu. No mercado, corte cru de programa de TV ficou em 0,0055x os seguidores (n de 3) e o criador contando como foi a entrevista ficou em 0,90x (n de 1) [FATO, fatos 155 e 157]. A pergunta do Bruno organiza o mês em torno do ativo que não tem medida e deixa em segundo plano o único que tem.

**Segunda: a data de 02/11 pesa em três coisas, e nenhuma é alcance.** (a) Texto: "vai ao ar" antes, "foi ao ar" só depois do horário confirmado [FATO, fato 6]. (b) Permissão: "Antes da data de exibição, só com o ok da produção" [FATO, fato 5]; a Mirna disse "pode seguir" de forma verbal [FATO, fato 4]. (c) Um pico de visitas ao perfil no dia e nos 2 seguintes, de tamanho sem dado: a TV passa num feriado, num canal legislativo local; as edições no site têm de 27 a 1.400 views, mediana de 80,5 [FATO, fato 136]. Nada disso pede reorganizar 16 peças agendadas.

**Terceira: o calendário sozinho não fecha a meta.** Mesmo com 150 de alcance em todos os reels (premissa do 00-SISTEMA), a conta da Projeção dá 9 diagnósticos feitos no Tabuleiro por mês e 3 conversas comerciais [FATO, 00-SISTEMA linha 419, conta deles]. Com o ritmo de hoje, 0 clique em 7 dias. A meta pede mais gente vendo o Bruno de frente e um pedido claro; pede também que "diagnóstico" tenha um nome só: o site usa a palavra para o teste de 12 casas e para a conversa de 30 minutos [FATO, fato 131]. Se a meta for 10 testes concluídos no mês, é uma meta; se for 10 conversas, é outra, umas 3 vezes maior [ESTIMATIVA, pela razão 1 em 3 da Projeção].

### 2.2 Onde a pergunta do Bruno está certa

- A exibição é um ativo de autoridade que não volta: "esteve na TV Câmara Campinas" serve para sempre na legenda, na bio e no destaque, e 53,1% dos engajados são de Campinas [FATO, fato 19].
- Os 35 minutos de entrevista são estoque com o Bruno em cena e com voz real, que a conta não tinha. Usar o estoque sem gravar é exatamente o que o contexto pede no curto prazo [FATO, contexto, "Capacidade"].
- Marcar a Mirna é barato e pode levar a peça a outro público ("@mention or collab" 1,13x entre contas) [FATO, fato 148]. O Bruno já decidiu fazer.

### 2.3 Ponto cego assumido: o que já funciona e fica

| O que funciona | Evidência | O que este plano faz |
|---|---|---|
| Bruno falando para a câmera | 4 de 4 reels com 3,61x a 10,14x [FATO, fato 29] | Vira o centro do depois: selfies sobre a TV e de nicho; remakes dos 3 melhores |
| Agenda do PostZen já montada | 43 itens agendados, 28 stories da S1 [FATO, L1, L2] | Fica. Mexo em 4 itens, cada um com motivo e id |
| Stories | 54,6% das views de 7 dias [FATO, fato 56 e derivar 15]; 1.178 de 2.073 na minha leitura [FATO, L9] | Story todo dia nas 4 semanas, com a S1 como está |
| Capa com foto do Bruno no feed | 111 de alcance contra 34,5 de texto [FATO, fato 51] | Todo carrossel novo com foto do Bruno na capa |
| Reel do Bruno às 21h ou depois | Nenhum reel do Bruno saiu entre 12h e 20h59 [FATO, fato 39] | Mantenho 21h nos dias úteis; teste de 11h só no 02/11, uma vez |
| Linha do dentista | Dentista A 169 de alcance [FATO, fato 30] | B no ar hoje; C só com sinal do B; TABULEIRO de novembro na selfie de nicho |
| Destaque, bio e link da bio | 7 cliques em 30 dias, o único caminho medido [FATO, fato 14] | Mantenho o link /v2/; mudo o texto da bio para falar da TV |

O que eu descarto, com dado contra: animação com voz sintética (12 de 12 abaixo de 42 em alcance no teste da régua [FATO, F7]); 3 posts por dia (série 2: mediana 26 e 0 seguidor [FATO, fato 44]); 15 automações sem nenhum disparo de terceiro [FATO, fato 116].

### 2.4 A pergunta que eu responderia no lugar

"O que faz alguém da região de Campinas ver o Bruno de frente, entender que ele comanda lançamentos e pedir o diagnóstico, e o que muda no dia em que ele aparece na TV?" O resto do plano responde as 22 perguntas do enquadramento a partir dela.

---

## 3. Respostas às 22 perguntas

### P1. Quais decisões o plano move, qual número muda, com que fonte e em que segunda é lido?

| Decisão | O que muda contra a agenda de hoje | Número que muda | Fonte | Lido em |
|---|---|---|---|---|
| D1 | tl02 de sáb 31/10 para dom 01/11 18h30; po01 sem "Comenta a palavra"; ci01 com voz conferida; selfie em seg 02/11 11h (se gravada); "mais votado" em ter 03/11 21h | Reels na S1: 6 para 5 | `listPosts` 17h41 [FATO, L4] | seg 02/11 19h (S1) e seg 09/11 19h (S2) |
| D2 | Gravação de 90 min por semana (plano de 21/10, não feita) vira 2 falas por semana, 1 sobre a TV e 1 de nicho | Reels com o Bruno de frente por semana: 0 agendados de 25/10 a 22/11 para 2 a partir da S2 | `listPosts` [FATO, L1]; fato 105 | seg 09/11 e qua 11/11 |
| D3 | 5 reels e 2 carrosséis com 1 post de feed por dia como padrão; até 4 reels quando faltar peça com o Bruno | Dias com 2 reels: 0; carrosséis: 1 pronto, 7 a produzir | `listPosts`; fato 108 | toda segunda 19h |
| D4 | S1 de stories como está; da S2 em diante, 6 a 7 por dia com 3 à mão | Stories à mão por semana: 27 (03-plano) para cerca de 21 | fato 61; derivar 17 | toda segunda 19h, janela de 7 dias |
| D5 | Régua 53 fixa; no máximo 3 decisões por rodada, cada uma com dono e prazo | Decisões não executadas: base 3 de 8 em 21/10 | fatos 125 e 180 | toda segunda 19h |
| D6 | Desligar 15 automações de comentário; TABULEIRO em 1 post de novembro; linkTracking ligado | Automações ativas: 17 para 2 (TABULEIRO e ETAPAS de story) | fato 114 | toda segunda, pelo log |

### P2. Qual régua, quais limites, a mesma do começo ao fim?

Alcance em 48 h sobre a mediana fixa de 53 [FATO, 00-SISTEMA linha 20, fato 24]. Limites [ESTIMATIVA, derivar 2]: 27 (0,5x), 42 (0,8x), 53 (1x), 106 (2x), 150 (2,83x, regra da palavra-chave do CLAUDE.md). Pulo: 60% e 75%. A mesma régua de 25/10 a 23/11.

Por que 53 e não as outras duas:
- 37,5 é a mediana atual do Buzzfy e carrega 12 reels sintéticos [FATO, fato 23 e 184]. Usar 37,5 baixa a barra justo quando o formato bom volta, e cada PARAR viraria MANTER sem mudança real.
- 57 views é outra métrica. A regra do CLAUDE.md (150) e o brief de 21/10 (53) são em alcance [FATO, fatos 168 e 169]. Misturar quebra a comparação.
- Informação ao lado, nunca para decidir: o múltiplo sobre o normal do Buzzfy (57 views) e o múltiplo sobre a mediana do formato Bruno de frente (167,5), que mede o custo de oportunidade de cada vaga.

### P3. A grade está dia a dia e hora a hora, com dia da semana e feriados?

Sim, na seção 4. Dias da semana conferidos com `date` [FATO, fato 2]. Feriados [FATO, fato 3]:
- seg 02/11, Finados e dia da exibição: dia próprio, sem objeção nos stories, reel só se for selfie gravada, Módulo 7 lido pelos agentes às 19h.
- dom 15/11, Proclamação da República: carrossel às 12h e stories normais; é domingo, sem reel na grade.
- sex 20/11, Consciência Negra: reel às 21h normal.
- Alcance em feriado: sem dado com o Bruno. O único feriado medido (12/10) é de animação, 3 pares, mediana 34 contra 27 no dia seguinte [FATO, fato 41]. Trato como dia normal e meço.

### P4. Antes, no dia e depois de 02/11

**Antes (25/10 a 01/11)**
- Aquecimento: tl01 (dom 25/10 18h30), pb01, car01, ci01, po01, pb02 nas datas agendadas; tl02 na véspera, dom 01/11 18h30. A legenda do tl01 e do tl02 já diz "A entrevista vai ao ar na segunda, 02/11." [FATO, fatos 77 e 78].
- Bastidor: já agendado no PostZen (estático BASTIDOR dom 09h00, mc02 dom 09h01, mc03 seg 17h30) [FATO, L2].
- Contagem: no texto, nunca em sticker agendado. Os estáticos da S1 já levam "VAI AO AR SEG, 02/11" (ter 14h31, qui 17h30) [FATO, `listPosts`]. Não ponho "FALTAM N DIAS" novo: os stories já estão renderizados e agendados, e trocar 28 arquivos por uma contagem sem medida é o ponto cego ao contrário. Sticker nativo de contagem só se o horário chegar até dom 25/10 21h, postado à mão pelo Bruno em seg 26/10 09h, com a hora certa (lembrete do sticker usa a hora; sem hora, ele não serve) [FATO nível 3, fato 69; PRIOR 9].
- Carrossel car02 "As perguntas que a TV me fez" (só as perguntas, sem as respostas), sáb 31/10 12h, se a agência entregar até qui 29/10 18h. Motivo: no mercado, os 3 posts de antes que renderam eram convite ou bastidor, sem trecho do que foi dito [FATO, fato 156, n de 3].

**No dia (seg 02/11)**
- 08h30: os agentes leem tvcamaracampinas.com.br/programacao/2026-11-02; o Bruno pergunta a hora à Mirna.
- 09h00: story NA TV · SEG, 02/11 · [HORA] · canal 11.3, NET 4, Vivo Fibra 9, YouTube [FATO, fato 135]. Se a hora chegar até dom 01/11 18h, vai agendado; senão o Bruno posta à mão com a hora.
- Se a hora seguir sem dado às 11h: story à mão "Vai ao ar hoje na TV Câmara Campinas. A grade sai no site da emissora." com sticker de link para tvcamaracampinas.com.br/ao-vivo [FATO, /ao-vivo responde 200]. Nunca hora inventada, nunca "ao vivo".
- 09h01: mc04 (story agendado).
- 11h00: reel selfie "como foi a entrevista", só se gravado no bloco 1. Sem selfie, nenhum reel no dia.
- 30 min antes da hora confirmada: story à mão com menção à Mirna e link para /ao-vivo.
- Depois do horário passado e confirmado pelo Bruno: story à mão "Foi ao ar hoje, 02/11, às [hora]. Obrigado, [@ da Mirna] e equipe do Ser Empreendedor." Sem logo.
- 19h00: Módulo 7 lido pelos agentes. 20h30: chamada "TER · 21H · NO FEED".

**Depois (03/11 a 21/11)**
- ter 03/11 21h: "o mais votado inteiro" (promessa do tl01).
- Selfies "o que eu disse na TV": 1 por semana, com uma pergunta da entrevista como roteiro (seg 02/11, seg 09/11, seg 16/11, se gravadas).
- tl03 (07/11), tl04 (14/11), tl05 (21/11) com portão.
- ob01 e ob03 como substitutos de vaga; ob02 só a partir de 10/11 e só se o pf01 não virar reel.
- Link da edição exibida nos stories e no destaque NA TV, quando a emissora publicar [FATO, termos permitem link, fato 137].

### P5. pb01, car01, ci01, po01 e pb02, um por um

| Peça | Decisão | Motivo | Data e hora | O que o Bruno faz e até quando |
|---|---|---|---|---|
| pb01 (DJ por 20 anos) | Fica | Apresenta quem é o Bruno sem entregar método; "antes" no mercado foi convite e bastidor [FATO, fato 156]; Bruno em cena desde o quadro 0 [FATO, fato 88]; cadeia de stories já agendada (20h30 e 21h05) | seg 26/10 21h | Guardar o print do ok da Mirna até seg 26/10 18h; marcar a Mirna depois de publicar |
| car01 (computador e sonho) | Fica | Capa com os dois rostos (feed com foto do Bruno: 111 contra 34,5) [FATO, fato 51]; é o único carrossel pronto | ter 27/10 12h | Marcar a Mirna até 12h15 |
| ci01 (nem tudo é ouro) | Fica, com condição | Bruno pediu para seguir. Mas é a peça mais fraca na abertura: Bruno de costas até 2,5 s [FATO, fato 88] e a fala "Ainda. Sempre vai ser." tem dono em disputa (ficha: Bruno; transcrição: Mirna) [FATO, fato 91] | qua 28/10 21h | Agência ouve 1380,8 a 1382,38 s até ter 27/10 18h. Sem conferência até qua 28/10 12h: o Bruno tira o ci01 (vai para o banco) e apaga a chamada das 20h30 (m17fs6f2w0yyddqfw8p2vebqbd8gwcne). Se o Dentista B fechar 48 h com 106 ou mais e pulo abaixo de 60%, o Dentista C entra no lugar do ci01 |
| po01 (Método Xeque-Mate) | Fica, com legenda corrigida | A legenda pede "Comenta a palavra." sem dizer qual [FATO, fato 80]; a única palavra do mês é TABULEIRO | qui 29/10 21h | Trocar "Comenta a palavra." por "Comenta." no PostZen (m17ersdnwmmsk5e7fyw4jqwfdx8gwcxt) até qui 29/10 18h |
| pb02 (restaurante) | Fica | Caso com número e a ressalva "O número de um caso não se repete igual em outro negócio" já na legenda [FATO, `listPosts`] | sex 30/10 21h | Desligar a automação CASE (dispara com "caso") até sex 30/10 20h; marcar a Mirna |

Plano B, só se a Mirna ou a produção disserem que nada sai antes de 02/11: pb01 para ter 03/11 21h, ci01 para qua 04/11 21h, po01 para qui 05/11 21h, pb02 para sex 06/11 21h, car01 para qui 05/11 12h, e de 26 a 30/10 entram R1 a R3 como reels normais e ob01 e ob03. O "mais votado" vai para seg 09/11 21h. Prazo para o Bruno trocar: seg 26/10 20h.

### P6. A promessa do tl01

A promessa mudou. A legenda agendada diz "O mais votado eu solto inteiro depois que a entrevista for ao ar." [FATO, fato 77]. Ela não força nada na S1. Entrega: ter 03/11 21h, reel "o mais votado inteiro", na S2. A S1 fica em 5 reels porque o tl02 passa para dom 01/11, que já é S2 (semana de domingo a sábado). Sem 6º reel na S1, sem motivo a escrever.

Contagem dos votos: só o Bruno, no app (ig_comments fora da lista) [FATO, fato 143], até seg 02/11 12h. Com menos de 5 votos somados, segue o plano e diz isso nos stories [FATO, regra do catálogo, fato 170]: o assunto escolhido é o 6 "Zero reais", que não tem peça [FATO, enquadramento conflito 2].

### P7. Ordem de tl02 a tl05, portão e destino

Ordem: tl02, tl03, tl04, tl05, como está agendado (pecas-e-calendario) [FATO, fato 173]. Só muda a data do tl02.

| Peça | Data | Portão que decide | Hora real da leitura | Regra |
|---|---|---|---|---|
| tl02 | dom 01/11 18h30 | tl01 com 48 h | ter 27/10 18h35 (48h05) | Sai do plano só se os dois falharem: alcance abaixo de 42 E pulo acima de 75%. Um critério ruim não basta com n de 1 |
| tl03 | sáb 07/11 18h30 | tl01 + tl02 (n de 2) | ter 03/11 18h35 (tl02 com 48h05) | Mediana dos 2 abaixo de 42 ou pulo mediano acima de 75%: PARAR o formato; tl03, tl04 e tl05 saem |
| tl04 | sáb 14/11 18h30 | tl01 a tl03 | seg 09/11 19h (tl03 com 48h30) | Mesma regra, n de 3 |
| tl05 | sáb 21/11 18h30 | tl01 a tl04 | seg 16/11 19h | Mesma regra; mostrar o carimbo "AINDA?" à Mirna antes |

Timelapse que não for ao feed: o Bruno apaga do PostZen, o arquivo vai para o Drive, e trechos de até 15 s podem virar story de bastidor. Não volta como reel.

Se o tl02 cair no portão: a vaga de dom 01/11 18h30 fica sem reel (o domingo é véspera; o feed já terá pb02, po01 e ci01 no topo).

### P8. mc02 a mc04

| Peça | Dia e hora | Situação |
|---|---|---|
| mc02 "Eu sou estrategista de marketing digital e lançamento de um produto." | dom 25/10 09h01 | Já no PostZen, versão que começa em "Eu" [FATO, L5] |
| mc03 "Cada cliente tem um produto específico e a gente vive esse produto." | seg 26/10 17h30 | Já no PostZen [FATO, `listPosts`] |
| mc04 "Eu construí patrimônio, eu construí família." | seg 02/11 09h01 | Agendar até dom 01/11 12h |

Recorte do mc04: 1705,567 s (dentro da faixa de 1705,2 a 1705,7 s), 4,60 s, como está renderizado [FATO, L6]. Não 1707,82 s. Motivo: o corte curto fecha uma frase inteira; o de 1707,82 s termina em "através da profissão", pedaço que só se completa com "que hoje eu executo como estrategista digital", termo vetado [FATO, 02-provas]. O mc04 não sai antes do tl02 no mesmo dia [FATO, enquadramento conflito 8]; com o tl02 em dom 01/11, a segunda 02/11 cumpre a regra.

### P9. Como a Mirna é marcada

| Peça | Imagem ou voz dela | Como | Quem e quando |
|---|---|---|---|
| tl01 | plano aberto | Agendado; marcação pelo app editando o post publicado (teste) | Bruno, dom 25/10 18h35 |
| pb01, ci01, po01, pb02, tl02, tl03, tl04, tl05 | Z2 ou voz [FATO, fato 90] | Agendado no PostZen; marcação pelo app até 15 min depois de publicar | Bruno |
| car01 | capa com os dois | Idem | Bruno, ter 27/10 até 12h15 |
| "mais votado inteiro" | provável | Convite de colaboração pelo PostZen (até 3 @), só com o ok dela e o @ | Bruno pede até sex 30/10; agenda até seg 02/11 12h |
| pf01 (story agendado) | Z2 de 0 a 6,45 s | Story agendado não leva menção (a API não põe sticker) [FATO, fato 66] | Sem marcação; registrar |
| Stories à mão com trecho dela | sim | Sticker de menção | Bruno, na hora |
| ob01 a ob03, selfies, nicho, remakes | não | Não marcar [HIPÓTESE 37, marcar onde ela não aparece é ruído] | |
| tl04 ("Uau!" recortado no rosto) e tl05 (carimbo "AINDA?") | sim | Mostrar a ela antes de marcar | Bruno, até seg 09/11 |

Tempo: 1 a 2 min por marcação [PRIOR 5, F5]; 10 peças de feed, cerca de 10 a 20 min nas 4 semanas [ESTIMATIVA].

Se o app não deixar marcar depois de publicado: o @ dela vai no texto da legenda. Para as peças ainda agendadas, o Bruno edita a legenda no PostZen ("Entrevista à TV Câmara Campinas, com @[mirna]") até 2 h antes de cada uma; para as já publicadas, edita a legenda no app. Se o @ não vier até seg 26/10 18h, o pb01 sai sem @ e recebe na edição depois. Que o @ no texto avisa a pessoa é [PRIOR 1], a conferir no tl01.

### P10. Copy depois de 02/11

Muda:
- "Foi ao ar em 02/11" só depois que o horário for confirmado e tiver passado [FATO, fato 6].
- Link da edição exibida em story (sticker), no destaque NA TV e "link nos stories" na legenda, quando a emissora publicar no site ou no YouTube. Compartilhar link e citar com a TV Câmara como fonte é permitido [FATO, fato 137].
- Minutos: só os da edição exibida, depois de vê-la. Os minutos do tl01 e do car01 contam da gravação do celular [FATO, fato 81]; não podem ser apresentados como minutos do programa.
- Tudo que diz "vai ao ar" sai do destaque NA TV em ter 03/11.

Continua vetado [FATO, 02-provas]: "ao vivo", "rede nacional", "a TV Câmara recomenda", "fui convidado pela TV", "entrevista exclusiva", "A TV me chamou de história de sucesso", "estrategista digital", "nós já faturamos mais de 3 milhões", "42 bilhões" como número do Bruno, qualquer promessa de resultado; logo da emissora; recortar ou filmar a exibição; republicar a edição inteira; anúncio pago com material da TV sem autorização escrita [FATO, termos, fato 137].

### P11. 5 reels e 2 carrosséis por semana? Dias com 2 reels? Quem faz os carrosséis?

| Semana | Reels | Carrosséis | Dias com 2 reels | Dias com mais de 2 posts de feed |
|---|---|---|---|---|
| S1 (25 a 31/10) | 5 (tl01, pb01, ci01, po01, pb02) | car01 + car02 se pronto (sáb 31/10 12h) | 0 | 0 |
| S2 (01 a 07/11) | 5 (tl02, selfie 02/11, mais votado, nicho 1, tl03) | car03 ter 03/11 12h, car04 qui 05/11 12h | 0 | 0 |
| S3 (08 a 14/11) | 5 (seg, qua, qui, sex 21h, tl04 sáb) | car05 dom 08/11 12h, car06 ter 10/11 12h | 0 | 0 |
| S4 (15 a 21/11) | 5 (seg, qua, qui, sex 21h, tl05 sáb) | car07 dom 15/11 12h, car08 ter 17/11 12h | 0 | 0 |
| dom 22/11 (abre S5) | 0 | car09 opcional, decidido em 16/11 | 0 | 0 |

Os 7 carrosséis que faltam (car02 a car08) são da agência, com foto de marca do Bruno na capa (f1 a f5, e1, e2) [FATO, fato 113]. Prazos de entrega pronta para agendar: car02 qui 29/10 18h; car03 sex 30/10 18h; car04 seg 02/11 12h; car05 e car06 sex 06/11 18h; car07 e car08 sex 13/11 18h. Assuntos propostos: car02 as perguntas da TV; car03 o que eu respondi (citação com fonte); car04 os 5 Lances do Tabuleiro; car05 as 4 casas de um lançamento (pesquisa, oferta, aquecimento, carrinho); car06 a car08 definidos pelo portão (objeção mais votada nas enquetes, caso com ressalva, nicho com leitura de conselho feita). Se o car02 não sair, a S1 fica com 1 carrossel, com o motivo escrito: falta de estoque, e a prioridade da agência na S1 é o render dos ob e das chamadas.

Dias com 2 posts de feed nas 4 semanas: só ter 03/11 (car03 às 12h e o mais votado às 21h, 9 h de distância). Nos outros dias, 1 post de feed ou nenhum. Nunca 3.

### P12. Bruno em cena nos 3 primeiros segundos

| Peça | Situação | Fonte |
|---|---|---|
| tl01, tl02, tl03 | Em cena aos 0,6 e 2,5 s | [FATO, fato 89] |
| tl04, tl05 | Sem dado nesta cadeira (não conferi quadros) | Agência confere até seg 09/11 |
| pb01, po01, pb02, pf01 | Em cena desde o quadro 0, perfil em 3/4, nunca de frente | [FATO, fato 88] |
| ci01 | De costas até 2,5 s, rosto não visível | [FATO, fato 88] |
| ob01, ob02, ob03 | Em cena, de perfil virado para a esquerda, atrás do monitor | [FATO, L8] |
| Dentista C | Selfie, "Dentistas," no quadro 0 | [FATO, fato 101] |
| Remakes R1, R2, R3 | Selfie, falando para a câmera | [FATO, fato 35] |
| Selfies novas (TV e nicho) | De frente desde o quadro 0, por regra de gravação | regra deste plano |
| Cortes novos do banco (pb03, CINEMA 02, MITO, PERGUNTA 01 e 02, SALA) | Sem ficha; Bruno em CB ou Z2, de perfil ou de costas | [FATO, fato 107] |

Leitura de primeiros princípios: a regra do CLAUDE.md diz "em cena". O aprendizado que a gerou é de rosto e voz (reels com o Bruno falando contra animação). Todas as peças da TV cumprem a letra; nenhuma cumpre o espírito com o rosto de frente. Por isso, todo corte novo do banco só entra se tiver o rosto do Bruno visível no quadro 0, e a S2 em diante depende de selfie.

### P13. Mínimo de gravação, data da próxima sessão, semana com zero

**Mínimo por semana:** 2 falas de 30 a 45 s, em selfie, de frente: 1 "o que eu disse na TV" (sem roteiro de teleprompter: o Bruno lê uma pergunta da entrevista e responde) e 1 de nicho com teleprompter. Conta [ESTIMATIVA, F5]: 12 a 18 min por fala, 24 a 36 min por bloco; 4 blocos dão de 96 a 144 min no mês.

Por que a fala da TV entra no mínimo: não depende das leituras de conselho (OAB, CFN 856, ABAC, CFP, CFO 196/2019, todas sem dado) [FATO, fato 103] e junta o formato que mediu bem com o ativo novo. O mercado tem 1 caso desse formato (0,90x) [FATO, fato 157]: evidência fraca, por isso fica como [HIPÓTESE] medida a partir de 02/11.

| Bloco | Prazo | O que gravar |
|---|---|---|
| 1 | qua 28/10 23h59 | Selfie TV 1 ("como foi a entrevista") + nicho 1: consórcio na versão sem a linha da ABAC (teleprompter pronto) [FATO, fato 103] |
| 2 | qua 04/11 23h59 | Selfie TV 2 + nicho 2: nutricionista se a CFN 856 estiver lida; senão dentista com assunto novo |
| 3 | qua 11/11 23h59 | Selfie TV 3 + nicho 3: psicólogo ou advogado só com leitura do CFP ou da OAB; senão consórcio 2 |
| 4 | qua 18/11 23h59 | Definido no portão de 16/11 |

A data da próxima sessão: sem dado (a buscar 20). Peço ao Bruno que marque o bloco 1 até seg 26/10.

**Semana com zero gravação, em ordem fixa:** (1) peças da TV já prontas e agendadas (timelapses com portão, "mais votado"); (2) remake R1 como Trial Reel ou, se a conta não for elegível, como reel normal com 2 mudanças; (3) ob01, depois ob03; (4) corte do banco com o rosto do Bruno visível no quadro 0, com ficha; (5) pf01 como reel, só com DOBRAR de profissão nomeada; (6) Dentista C, só pela condição do P14. Nunca voz sintética. Se a semana não fechar 5 com isso, fecha com 4, e o motivo vai escrito no arquivo da semana. Vaga vazia custa menos que reel sem rosto: a série de 3 posts por dia somou 206 de alcance em 8 peças [FATO, fato 44].

### P14. Dentista C e remakes

**Dentista C:** padrão, anúncio 4:5 depois de 18/11, como o brief do dentista guarda [FATO, fato 101]. Exceção: se o Dentista B fechar 48 h (seg 26/10 21h05) com 106 ou mais de alcance e pulo abaixo de 60%, o C entra no feed em qua 28/10 21h, no lugar do ci01, como 2ª sequência da linha (mesmo assunto, outro formato) [FATO, sequência 1,63x no 2º post, fato 149]. Não vai ao direct.

**Remakes**, todos sem gravar, cada um com 2 mudanças reais: legenda queimada e texto na tela desde o quadro 0 (1,18x) [FATO, fatos 145 e 147]. Não corto o preâmbulo: as aberturas do Bruno com preâmbulo tiveram de 45,7% a 53,2% de pulo [FATO, fato 38]. Legenda nova, sem a promessa vencida da saga [FATO, fato 37].

| Remake | Original | Data | Como |
|---|---|---|---|
| R1 "Ele nunca fez um anúncio" | 10,14x, pulo 53,2% | qua 04/11 14h | Trial Reel pelo app, postado pelo Bruno; segunda vida de 35% para original de 5x ou mais [FATO, fato 150] |
| R2 "90% dos lançamentos que flopam" | 4,42x, pulo 45,7% | qua 11/11 14h | Trial Reel |
| R3 "Problema de equipe" | 3,61x, pulo 49,6% | qua 18/11 14h | Trial Reel |

Trial Reel não conta nos 5 reels da semana e conta na distância de 6 h [HIPÓTESE 32]; às 14h ele fica a 7 h do reel das 21h. Se a conta não for elegível (a falha só aparece na publicação [FATO, fato 139]), o R1 vira o 1º substituto de vaga vazia, como reel normal, contado nos 5.

### P15. Stories por dia, horários, tipos, PostZen ou à mão, fonte de cada frase

**S1 (25 a 31/10):** como está. 28 agendados no PostZen [FATO, L2] mais a lista à mão do `05-manuais-bruno.md` (3 a 4 por dia). Ajustes: sáb 31/10 17h30 (chamada SÁB 18H30) sai; os manuais de 31/10 18h35 e 01/11 09h00 (compartilhar tl02) passam para dom 01/11 18h35. Ordem de prioridade dos manuais, se faltar tempo: (1) link do diagnóstico, (2) compartilhar o reel na hora, (3) enquete da objeção, (4) repost das 09h. O link é o único caminho do story até o diagnóstico; foram 0 toques e 0 cliques em 7 dias [FATO, L9].

**S2 a S4:** 6 a 7 por dia.

| Hora | Tipo | Via | Fonte da frase |
|---|---|---|---|
| 09h00 | Autoridade ou bastidor, com o Bruno em cena | PostZen | 02-provas (B, M, C), fotos e1, e2; depois de 02/11, "FOI AO AR" com link |
| 12h00 | Objeção como o cliente fala + enquete | à mão | 01-objecoes O1 a O12 e F6 O13 a O15 |
| 12h01 | Virada na voz do Bruno | PostZen | contra-argumento da objeção, 01-objecoes |
| 12h02 | Prova com fonte | PostZen | citação literal com tempo na transcrição, ou caso com a ressalva |
| 12h03 | Link do diagnóstico (DIAGNÓSTICO · 12 CASAS) | à mão | estático f1 já existente; link /tabuleiro/?o=ig-stories |
| 17h30 | Frase de efeito | PostZen | estáticos livres 3 e 4 [FATO, fato 62] e banco de 14 frases com fonte da F6 |
| 20h30 | Chamada do reel ("DIA · 21H · NO FEED"), só em dia de reel | PostZen | título do reel |
| 21h05 (18h35 no sábado) | Compartilhar o reel publicado | à mão | |

À mão por semana: 3 por dia nos dias com reel e 2 nos outros, cerca de 19 a 21 [ESTIMATIVA]. Toda frase entre aspas é literal da transcrição, com o tempo; caso só como fato do caso com a ressalva; nenhuma frase da lista vetada.

### P16. ob01 a ob03

Render: pronto (17,9 s, 28,37 s, 15,1 s) [FATO, L7]. Falta a folha de 4 quadros por segundo com nota de 0 a 10 por efeito (CLAUDE.md) e ouvir: ob01 de 1316,2 a 1326,4 s (a ficha diz que é o Bruno) [FATO, fatos 98 e 99]; ob02 "case" com confiança 0,33 [FATO, `03-plano-7-dias.json`]. Prazo da agência: sex 30/10 18h.

Lugar: nenhum em 02/11 (o 03-plano punha o ob02 no dia). Os três são o Bruno de perfil atrás do monitor [FATO, L8], formato sem medida; entram como substitutos de vaga a partir da S2, nesta ordem: ob01 (objeção "não tenho tempo", força 9), ob03 ("vive de indicação", força do O8 sem número), ob02. O ob02 usa 82% do áudio do pf01 [FATO, derivar 23]: só a partir de ter 10/11 (14 dias depois do story pf01) e só se o pf01 não virar reel. Pedido na tela "Comenta a sua área" [FATO, fichas]: é pergunta aberta, sem palavra-chave; fica.

Substituto se não ficarem prontos: R1 remake, depois corte do banco com rosto visível.

### P17. PARAR, MANTER, DOBRAR, TESTAR

| Decisão | Regra | n mínimo |
|---|---|---|
| PARAR um formato | Mediana de alcance em 48 h abaixo de 42 ou pulo mediano acima de 75% | 2 peças do formato. Com n de 1: "não testado", nunca PARAR |
| Segurar uma peça | A próxima peça do mesmo formato sai do plano se a anterior falhar nos dois critérios (abaixo de 42 e pulo acima de 75%) | 1 (decisão de peça, não de formato) |
| MANTER | Mediana de 42 a 105 | 1 |
| DOBRAR | 106 ou mais com pulo abaixo de 60%; a próxima vaga livre vai para a mesma linha, mudando assunto ou formato, nunca os dois | 1 para a próxima peça; 2 para dar mais vagas por semana |
| TESTAR | 1 variável por teste, hipótese escrita antes, no máximo 1 teste por semana, lido em 48 h | |
| Carrossel | Mesma régua de alcance; DOBRAR pede também 2 ou mais visitas ao perfil | 2 |
| Story | Views de 7 dias lidas sempre na seg 19h; respostas por semana | |
| Palavra-chave | 150 ou mais de alcance em 48 h no post anterior do mesmo formato | 1 |

Formatos para a régua: (1) Bruno de frente (selfie, nicho e TV); (2) corte da TV com o Bruno de perfil (pb, po, pf, mais votado); (3) TV de costas ou atrás do monitor (ci01, ob); (4) timelapse; (5) remake; (6) carrossel.

Rodadas: seg 26/10 21h05 (Dentista B com 48 h; decide C e TABULEIRO), ter 27/10 18h35 (tl01; decide tl02), seg 02/11 19h, seg 09/11 19h, seg 16/11 19h, seg 23/11 19h (decide a S5). Datas herdadas: qua 11/11 (nicho do brief), sex 13/11 (seguidores de 14 dias fecham, derivar 5), qua 18/11 (seguidores e diagnóstico do brief).

Rodada de 02/11 (feriado e exibição): os agentes leem o Buzzfy e o PostZen às 19h e escrevem `semanas/2026-11-02.md`; lê a S1 inteira (pb02 com 46 h, provisório). O Bruno lê e executa até ter 03/11 11h. Se a exibição cair às 18h (hipótese pela grade desta semana [HIPÓTESE 35]), a leitura não muda de hora: ela é dos agentes.

No máximo 3 decisões por rodada, cada uma com dono e prazo, e a linha "executado: sim ou não". Em 21/10 foram 8 decisões e 3 ficaram sem execução [FATO, fato 125].

### P18. TABULEIRO, outras automações, pedidos de direct, contagem até o diagnóstico

- Outubro: Dentista B (24/10 21h), já ligado [FATO, fato 117].
- Novembro: um post só, o nicho 1 em qua 04/11 21h (selfie de nicho gravada no bloco 1). Condição: o anterior do mesmo formato passou de 150 em 48 h; o Dentista A fez 169 [FATO, fato 30]. Sem nicho gravado até qua 18/11, novembro fica sem TABULEIRO. Nunca em 02/11.
- Nova automação TABULEIRO com texto genérico (o atual fala com dentista [FATO, fato 117]), botão para /tabuleiro/?o=ig-tabuleiro-nov e linkTracking ligado [HIPÓTESE 51, passa a contar cliques]. O Bruno cria até ter 03/11.
- Antes do tl01 (dom 25/10 18h): o Bruno desliga as 15 automações de comentário que não são a TABULEIRO do B. Fica também a ETAPAS de story (só dispara com "etapa", não atrapalha a série). Motivos: uma palavra por mês (CLAUDE.md); 0 disparo de terceiro em 30 dias [FATO, fato 116]; CASE dispara com "caso" e ESTRATEGISTA com "estrategista", palavras da série [FATO, fato 114]; cada comentário aceita uma resposta privada só [FATO, fato 120], e a automação gastaria a chance de o Bruno responder à mão.
- Pedidos de direct nas legendas ("Me manda a data no direct", car01 e pb02) ficam: são pedido aberto, sem palavra. Um pedido por peça daqui para frente.
- Teste de ponta a ponta antes de 04/11: um perfil que não é do Bruno comenta TABULEIRO no Dentista B, recebe o direct, toca no botão, faz o teste e chega ao WhatsApp. Feito por alguém de confiança do Bruno, registrado com print.

Contagem, toda segunda:

| Etapa | Onde se lê | Quem |
|---|---|---|
| Comentários com "tabuleiro" | `listCommentAutomationLogs`, tirando perfis do Bruno | agentes |
| Direct enviado | log (sent ou failed) | agentes |
| Toque no botão | linkTracking, se ligado | Bruno (interface) |
| Teste começado e concluído | GA4 G-F91ET225YW, tabuleiro_start e tabuleiro_complete | Bruno |
| Mensagem no WhatsApp ("Fiz O Tabuleiro", "Quero agendar o Primeiro Lance") | WhatsApp | Bruno |
| Conversa de 30 min agendada e feita | agenda | Bruno |
| Proposta e venda | Bruno | Bruno |

O que o Bruno não informar fica "sem dado", nunca estimado.

### P19. O que muda em cada post contra o anterior da mesma linha

| Linha | Sequência | O que muda |
|---|---|---|
| Dentista | A (21/10) para B (24/10) para C (só com sinal) | Formato (selfie, tela dividida, prédio de palavras); assunto igual |
| Cortes da TV | pb01, ci01, po01, pb02, mais votado | Assunto; formato igual (corte com placa e legenda), o mais votado muda a duração |
| Timelapse | tl01 a tl05 | Assunto (35 minutos, família, pergunta da TV, de trás pra frente, régua do tempo); formato igual |
| Selfie TV | 1 (como foi), 2 e 3 (uma pergunta cada) | Assunto; formato igual |
| Nicho | consórcio, nutricionista ou dentista, psicólogo ou advogado | Assunto (profissão); formato igual |
| Remake | R1, R2, R3 contra os originais | Formato (legenda queimada e texto no quadro 0); assunto igual |
| Objeção (ob) | ob01, ob03, ob02 | Assunto; formato igual |
| Carrossel | car01 a car08 | Assunto; formato igual, sempre com foto do Bruno na capa |

### P20. Regras de texto

Conferido nas legendas agendadas [FATO, `listPosts` 17h41]: nenhuma com travessão, emoji, "ao vivo", "foi ao ar" ou nome vetado. Uma correção: po01 ("Comenta a palavra."). Uma atenção: o ci01 tem "Até hoje o melhor marketing é o olho no olho." e nenhuma construção "não é X, é Y"; ok. Para tudo o que for novo: sem travessão, sem emoji, sem promessa de resultado, sem HighClass, Júnior Prazeres ou Felipe Roser, no máximo uma "não é X, é Y" por peça, sem as frases vetadas do 02-provas, sem logo de terceiro (TV Câmara, BNI ou outra) em estático ou interface recriada. A bio atual tem emojis e "Estrategista Digital" [FATO, L9]: a proposta de bio nova (seção 4, dom 01/11) vem sem os dois.

Proposta de bio, para o Bruno trocar até dom 01/11 21h (cerca de 147 caracteres [ESTIMATIVA, contagem]):

> Estrategista de Lançamento
> Você atende. Eu comando o seu lançamento.
> Na TV Câmara Campinas, Ser Empreendedor, 02/11
> Conversa de 30 min no link

As linhas de fé, do BNI e da DashPro são decisão dele; com elas a bio passa do limite de 150 caracteres [PRIOR, limite do Instagram]. Depois de 02/11, a 3ª linha vira "Entrevista na TV Câmara Campinas, 02/11". O link /v2/ fica (único caminho medido: 7 cliques em 30 dias [FATO, fato 14]; os botões de lá abrem o WhatsApp com o pedido do Primeiro Lance, a conversa de 30 min [FATO, fato 128]). Se o Bruno trocar o link para /tabuleiro/?o=ig-bio, a 4ª linha vira "Diagnóstico de 12 casas no link".

### P21. O que depende só do Bruno, com prazo

| # | Ação | Prazo |
|---|---|---|
| 1 | Desligar as 15 automações de comentário (fica TABULEIRO do B e ETAPAS de story) | dom 25/10 18h |
| 2 | Testar a marcação da Mirna no tl01 publicado e ver se o @ na legenda vira link | dom 25/10 18h35 a 21h |
| 3 | Guardar o print do ok da Mirna; perguntar se vale para publicar antes de 02/11; pedir o @ e o horário da exibição | seg 26/10 18h |
| 4 | Copiar para o Drive tl02 a tl05, mc02 a mc04, ob01 a ob03 e a fonte da entrevista (hoje só na pasta temporária) [FATO, fato 110] | seg 26/10 23h59 |
| 5 | Marcar a data do bloco de gravação 1 | seg 26/10 |
| 6 | Mover o tl02 para dom 01/11 18h30 (m171fp82kqkbcw5h3xggewpev18gwe2g) e apagar o story de 31/10 17h30 (m1725qcdrthtrr16rsffjnymfd8gwdrz), ou apagar o tl02 se cair no portão | ter 27/10 21h |
| 7 | Gravar o bloco 1 (2 falas) | qua 28/10 23h59 |
| 8 | Trocar a legenda do po01 | qui 29/10 18h |
| 9 | Contar os votos do tl01 | seg 02/11 12h |
| 10 | Bio nova, 3 posts fixados, destaque NA TV | dom 01/11 21h |
| 11 | Stories à mão (lista diária) e marcação da Mirna em cada peça com ela, com "feito" ou "não feito" | todo dia |
| 12 | Trial Reels R1, R2, R3 pelo app | qua 04/11, 11/11, 18/11, 14h |
| 13 | Criar a TABULEIRO de novembro com linkTracking | ter 03/11 |
| 14 | Teste de ponta a ponta do caminho TABULEIRO com um perfil de confiança | ter 03/11 |
| 15 | Números de GA4, WhatsApp e diagnósticos agendados e feitos | toda segunda 18h |
| 16 | Dizer se bruno26111982 é perfil dele | seg 26/10 |
| 17 | Apagar o rascunho de release público da entrevista no GitHub [FATO, fato 111] | sem prazo escrito; sugiro seg 26/10 |
| 18 | Definir o que conta como "diagnóstico" na meta de 10 por mês: o teste de 12 casas ou a conversa de 30 min | seg 02/11, antes da rodada |

### P22. Etiquetas e "sem dado"

Cada número deste plano tem etiqueta ou fonte ao lado. As lacunas estão na seção 9 e escritas "sem dado" onde aparecem.

---

## 4. Grade dia a dia, hora a hora (dom 25/10 a dom 22/11)

Legenda: **[PZ]** já agendado no PostZen (não mexer, salvo indicação); **[PZ novo]** agendar (Bruno, com arquivo da agência); **[M]** à mão pelo Bruno no app; **[A]** leitura dos agentes. Horário de São Paulo. Semana de domingo a sábado.

### S1 · 25 a 31/10 (antes da exibição) · 5 reels e 1 ou 2 carrosséis

| Dia | Feed | Stories | Leituras e ações |
|---|---|---|---|
| dom 25/10 | 18h30 reel tl01 [PZ] | 09h00 BASTIDOR [PZ]; 09h01 mc02 [PZ]; 09h02 caso 6 para 20 + enquete [M]; 12h00 compartilhar Dentista B + enquete [M]; 12h30 link diagnóstico [M]; 17h30 DOM 18H30 [PZ]; 18h35 compartilhar tl01 [M] | 08h30 ler a pilha de 24/10 antes de expirar [A]; até 18h desligar 15 automações [M]; 18h35 teste de marcação no tl01 [M]; 21h Dentista B com 24 h [A] |
| seg 26/10 | 21h00 reel pb01 [PZ] | 09h00 compartilhar tl01 + enquete [M]; 12h00 objeção O2 + enquete [M]; 12h01 A VIRADA [PZ]; 17h30 mc03 [PZ]; 17h31 A EQUIPE EXECUTA [PZ]; 17h32 link [M]; 20h30 SEG 21H [PZ]; 21h05 compartilhar pb01 [M] | até 18h print e ok da Mirna, @ e hora [M]; 21h05 Módulo 7 especial: Dentista B com 48 h decide C e TABULEIRO [A]; 21h15 marcar Mirna no pb01 [M] |
| ter 27/10 | 12h00 car01 [PZ] | 09h00 compartilhar pb01 + enquete [M]; 14h30 objeção O8 + enquete [M]; 14h31 VAI AO AR SEG 02/11 [PZ]; 14h32 A VIRADA [PZ]; 14h33 CONTEI NA TV [PZ]; 16h00 pf01 v2 [PZ]; 16h01 link [M] | 12h15 marcar Mirna no car01 [M]; 18h ouvir ci01 1380,8 a 1382,38 s (agência); 18h35 tl01 com 48h05 decide tl02 [A]; até 21h mover ou apagar tl02 e apagar story 31/10 17h30 [M] |
| qua 28/10 | 21h00 reel ci01 [PZ] (ou Dentista C, se o B passou; ou nada, se a voz não foi conferida até 12h) | 09h00 compartilhar car01 [M]; 12h00 objeção O3 + enquete [M]; 12h01 A VIRADA [PZ]; 17h30 TV CÂMARA CAMPINAS [PZ]; 17h31 NA TV [PZ]; 17h32 CRITÉRIO [PZ]; 17h33 link [M]; 20h30 QUA 21H [PZ]; 21h05 compartilhar ci01 [M] | 21h pb01 com 48 h [A]; até 23h59 bloco de gravação 1 [M] |
| qui 29/10 | 21h00 reel po01 [PZ, legenda corrigida] | 09h00 compartilhar ci01 + enquete [M]; 12h00 objeção O4 + enquete [M]; 12h01 A VIRADA [PZ]; 17h30 VAI AO AR SEG 02/11 [PZ]; 17h31 MÉTODO XEQUE-MATE [PZ]; 17h32 link [M]; 20h30 QUI 21H [PZ]; 21h05 compartilhar po01 [M] | até 18h legenda do po01 [M]; 18h car02 pronto (agência) |
| sex 30/10 | 21h00 reel pb02 [PZ] | 09h00 compartilhar po01 + enquete [M]; 12h00 objeção O6 + enquete [M]; 12h01 A VIRADA [PZ]; 12h02 link [M]; 17h30 ALINHAMENTO [PZ]; 17h31 DIAGNÓSTICO 30 MIN [PZ]; 20h30 SEX 21H [PZ]; 21h05 compartilhar pb02 [M] | até 18h folha de ob01 a ob03, car03 e estático DOM 18H30 de 01/11 (agência); até 20h confirmar CASE desligada [M] |
| sáb 31/10 | 12h00 car02 [PZ novo], se pronto. Sem reel (tl02 foi para dom 01/11) | 09h00 compartilhar pb02 + enquete [M]; 11h00 NA TV [PZ]; 12h00 O QUE EU MAIS OUÇO [PZ]; 12h01 A VIRADA [PZ]; 12h02 TV CÂMARA CAMPINAS [PZ]; 12h03 link [M]; 17h30 SÁB 18H30 [PZ] **apagar**; 19h30 enquete O5 TEMPO ou MEDO [M] | 12h15 compartilhar car02 no story [M] |

### S2 · 01 a 07/11 (semana da exibição) · 5 reels e 2 carrosséis

| Dia | Feed | Stories | Leituras e ações |
|---|---|---|---|
| dom 01/11 (véspera) | 18h30 reel tl02 [PZ, data nova], se passou no portão | 09h00 VÉSPERA · NA TV SEG, 02/11, com o Bruno em cena [PZ novo]; 12h00 objeção O12 + enquete [M]; 12h01 virada O12 "Curso te dá o mapa. A partida precisa de quem comande." [PZ novo]; 12h02 link [M]; 17h30 DOM 18H30 NO FEED [PZ novo]; 18h35 compartilhar tl02 + marcar Mirna [M]; 20h30 SEG, 02/11 · TV CÂMARA CAMPINAS · canais (e a hora, se houver fonte) [PZ novo] | até 12h agendar mc04 para 02/11 [M]; até 21h bio nova, 3 fixados (Dentista A, car01, tl02) e destaque NA TV [M]; até 18h hora da exibição define se o story das 09h de 02/11 vai agendado [M] |
| seg 02/11 (Finados, exibição) | 11h00 reel selfie TV 1 "como foi a entrevista" [PZ novo], só se gravada no bloco 1 | 09h00 NA TV · SEG, 02/11 · [HORA] · canais [PZ novo ou M]; 09h01 mc04 [PZ novo]; 11h05 compartilhar selfie [M]; 12h02 link [M]; hora menos 30 min: story com menção à Mirna e link /ao-vivo [M], só com hora confirmada; depois da exibição confirmada: "Foi ao ar hoje, 02/11, às [hora]" com agradecimento e menção [M]; 20h30 TER · 21H · NO FEED [PZ novo] | 08h30 grade no site [A]; se sem hora às 11h, story com link /ao-vivo sem hora [M]; 12h votos do tl01 [M]; 19h Módulo 7 [A]; o Bruno executa até ter 03/11 11h |
| ter 03/11 | 12h00 car03 "O que eu respondi" [PZ novo]; 21h00 reel "o mais votado inteiro" [PZ novo] (colaboração com a Mirna se ela aceitar) | 09h00 FOI AO AR · SEG, 02/11 + link da edição, se publicada [M]; 12h00 objeção O14 "TV de Câmara não prova nada" + enquete [M]; 12h01 virada [PZ novo]; 12h02 prova: caso com ressalva [PZ novo]; 12h03 link [M]; 12h05 compartilhar car03 [M]; 17h30 frase de efeito [PZ novo]; 20h30 chamada [PZ novo]; 21h05 compartilhar + marcar [M] | 11h tirar do destaque tudo que diz "vai ao ar" [M]; 18h35 tl02 com 48h05 decide tl03 [A]; criar a TABULEIRO de novembro e o teste de ponta a ponta [M] |
| qua 04/11 | 14h00 Trial Reel R1 [M]; 21h00 reel nicho 1 (consórcio) com TABULEIRO [PZ novo]. Sem gravação: ob01 sem palavra | 09h00 autoridade [PZ novo]; 12h00 objeção O9 + enquete [M]; 12h01 virada "Mais verba numa ordem errada só acelera o erro." [PZ novo]; 12h02 prova "Você precisa ter os gatilhos corretos" (1608,3 s) [PZ novo]; 12h03 link [M]; 17h30 frase [PZ novo]; 20h30 chamada [PZ novo]; 21h05 compartilhar [M] | até 23h59 bloco de gravação 2 [M]; 05/11 e 06/11 ler visitas ao perfil de 02 a 04/11 (o Buzzfy atrasa até 48 h) [A] |
| qui 05/11 | 12h00 car04 "Os 5 Lances do Tabuleiro" [PZ novo] | 09h00 autoridade [PZ novo]; 12h00 objeção O11 + enquete [M]; 12h01 virada [PZ novo]; 12h02 prova "vou aprender com você" (1490,4 s) [PZ novo]; 12h03 link [M]; 12h05 compartilhar car04 [M]; 17h30 frase [PZ novo] | sem reel (a semana fecha 5 com tl02, selfie, mais votado, nicho 1 e tl03) |
| sex 06/11 | sem post. Se faltar reel na semana (selfie ou nicho não gravados, ou tl02 fora): 21h00 ob01 ou R1 normal [PZ novo] | 09h00 autoridade [PZ novo]; 12h00 objeção O13 + enquete [M]; 12h01 virada [PZ novo]; 12h02 prova [PZ novo]; 12h03 link [M]; 17h30 frase [PZ novo] | 18h agência entrega a S3 (car05, car06, cortes) |
| sáb 07/11 | 18h30 reel tl03 [PZ], se passou no portão | 09h00 autoridade [PZ novo]; 12h00 objeção O5 em versão nova + enquete [M]; 12h03 link [M]; 17h30 SÁB 18H30 [PZ novo]; 18h35 compartilhar + marcar [M] | até 12h Bruno agenda a S3 [M] |

### S3 · 08 a 14/11 · 5 reels e 2 carrosséis

| Dia | Feed | Stories | Leituras e ações |
|---|---|---|---|
| dom 08/11 | 12h00 car05 [PZ novo] | 09h00 autoridade; 12h00 enquete O15 "meu público é daqui" (só enquete, sem prova [FATO, F6]) [M]; 12h03 link [M]; 12h05 compartilhar car05 [M]; 17h30 frase | |
| seg 09/11 | 21h00 reel selfie TV 2 [PZ novo]; sem gravação: ob03 | 09h00 FOI AO AR + link da edição; 12h00 O1 com a TV como prova [M]; 12h01 virada; 12h02 prova; 12h03 link [M]; 17h30 frase; 20h30 chamada; 21h05 compartilhar [M] | 19h Módulo 7 [A]; tl03 com 48h30; até 18h números do Bruno |
| ter 10/11 | 12h00 car06 [PZ novo] | 09h00 autoridade; 12h00 O7 "meu conselho não deixa" só com a regra conferida, senão O2 em versão nova [M]; 12h01 virada; 12h02 prova; 12h03 link [M]; 17h30 frase | ob02 liberado a partir de hoje, se o pf01 não virou reel |
| qua 11/11 | 14h00 Trial Reel R2 [M]; 21h00 reel nicho 2 [PZ novo]; sem gravação: R1 normal ou corte do banco com rosto | 09h00 autoridade; 12h00 O10 só com o caso confirmado, senão O3 [M]; 12h01 virada; 12h02 prova; 12h03 link [M]; 17h30 frase; 20h30 chamada; 21h05 compartilhar [M] | conferência do nicho do brief: mediana de A, B e nicho 1 [A]; seguidores até 08/11 fecham [A]; até 23h59 bloco 3 [M] |
| qui 12/11 | 21h00 reel: corte do banco com rosto visível no quadro 0, ou ob01, ou pf01 como reel só com DOBRAR [PZ novo] | 09h00 autoridade; 12h00 O4 em versão nova [M]; virada, prova, link, frase; 20h30 chamada; 21h05 compartilhar [M] | |
| sex 13/11 | 21h00 reel: selfie TV 3 se o bloco 3 saiu, ou nicho 3, ou R2 normal [PZ novo] | 09h00 autoridade; 12h00 O6 em versão nova [M]; virada, prova, link, frase; 20h30 chamada; 21h05 compartilhar [M] | seguidores de 28/10 a 10/11 fecham (piso do brief: 12) [A]; 18h agência entrega a S4 |
| sáb 14/11 | 18h30 reel tl04 [PZ], se passou no portão | 09h00 autoridade; 12h00 enquete [M]; 12h03 link [M]; 17h30 SÁB 18H30; 18h35 compartilhar + marcar [M] | até 12h Bruno agenda a S4 [M] |

### S4 · 15 a 21/11 · 5 reels e 2 carrosséis

| Dia | Feed | Stories | Leituras e ações |
|---|---|---|---|
| dom 15/11 (Proclamação da República) | 12h00 car07 [PZ novo] | 09h00 autoridade; 12h00 O8 em versão nova [M]; 12h03 link [M]; 12h05 compartilhar car07 [M]; 17h30 frase | alcance em feriado registrado [A] |
| seg 16/11 | 21h00 reel selfie TV ou nicho do bloco 3 [PZ novo] | 09h00 autoridade; 12h00 O9 em versão nova [M]; virada, prova, link, frase; 20h30 chamada; 21h05 compartilhar [M] | 19h Módulo 7 [A]; tl04 com 48h30 decide tl05 |
| ter 17/11 | 12h00 car08 [PZ novo] | 09h00 autoridade; 12h00 O11 [M]; virada, prova, link, frase | |
| qua 18/11 | 14h00 Trial Reel R3 [M]; 21h00 reel nicho 3 ou substituto [PZ novo] | 09h00 autoridade; 12h00 O12 [M]; virada, prova, link, frase; 20h30 chamada; 21h05 compartilhar [M] | conferência do brief: seguidores e diagnóstico [A e Bruno]; até 23h59 bloco 4 [M] |
| qui 19/11 | 21h00 reel: ob ou corte com rosto ou remake normal [PZ novo] | 09h00 autoridade; 12h00 O13 [M]; virada, prova, link, frase; 20h30 chamada; 21h05 compartilhar [M] | Dentista C liberado para anúncio 4:5 (brief), decisão do Bruno |
| sex 20/11 (Consciência Negra) | 21h00 reel do bloco 4 ou substituto [PZ novo] | 09h00 autoridade; 12h00 O14 em versão nova [M]; virada, prova, link, frase; 20h30 chamada; 21h05 compartilhar [M] | alcance em feriado registrado [A] |
| sáb 21/11 | 18h30 reel tl05 [PZ], se passou no portão | 09h00 autoridade; 12h00 enquete [M]; 12h03 link [M]; 17h30 SÁB 18H30; 18h35 compartilhar + marcar [M] | |
| dom 22/11 (abre S5) | 12h00 car09 opcional, decidido em 16/11 | 09h00 autoridade; 12h00 O1 com 4 semanas de prova [M]; 12h03 link [M]; 17h30 frase | seg 23/11 19h Módulo 7 decide a S5 [A] |

Distância entre reels: o menor intervalo da grade é de 16h30 (dom 01/11 18h30 para seg 02/11 11h) [ESTIMATIVA, conta de horas]; nenhum abaixo de 6 h, Trial Reel incluído (7 h).

---

## 5. Decisões: opções, efeitos, premissas, posição, probabilidade

Probabilidade de sucesso = chance de o critério do enquadramento ser cumprido, do jeito que ele está escrito (com as correções do livro de fatos). Faixa = [mín, máx]. Confiança = quanto confio na minha própria estimativa, de 0 a 1. Tudo isso é [PRIOR].

### D1. Série da entrevista em torno de 02/11

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) Manter os 5 cortes nas datas, mover só o tl02 para a véspera, dia em story e perfil, depois com selfies e o mais votado | Respeita o "pode seguir"; S1 em 5; 4 itens a editar no PostZen | Os assuntos 2, 3, 5 e 7 do índice se esgotam antes da TV; o depois depende de gravação |
| (b) Mover os 5 para 03 a 13/11 | Depois fica cheio de TV; S1 vazia, pede remakes e nicho | 16 stories de chamada já agendados ficam errados; contraria o "pode seguir"; S1 sem rosto se não houver remake |
| (c) Dividir: apresentação antes, método e caso depois | ci01 e po01 para depois | Mexe em 2 peças e 4 stories de chamada; o critério de divisão não tem dado |
| (d) Fora do óbvio: tirar a TV do eixo. Cortes ficam como estão, o feed do depois vira o Bruno de frente contando a TV, e a data vira operação de perfil (bio, fixados, destaque, link) | O formato medido volta ao centro | Depende de gravação; se não houver, volta a ser (a) |
| (e) Fora do óbvio 2: usar a TV fora do Instagram. O Bruno manda o link da edição, com uma frase pessoal, para a rede de Campinas (clientes, BNI) | Visitas e conversas que o Instagram não traz | Fora da medição dos agentes; termos da TV permitem link [FATO, fato 137] |

**Posição:** (a) com (d) no depois. (e) como sugestão ao Bruno, decisão dele.
**Premissas:** "pode seguir" vale como ok para publicar antes; o print chega até seg 26/10; a marcação pelo app funciona ou o @ no texto basta; a TV traz pouco tráfego direto.
**Probabilidade:** 0,15 [0,05, 0,35]. **Confiança:** 0,5.
**Por que tão baixo:** o critério soma três números, e dois deles (21 visitas por dia de 02 a 04/11 e saldo positivo de 25/10 a 08/11) dependem mais da audiência da TV, sem dado, do que da organização. As 4 opções ficam a 0,03 umas das outras na minha conta: o critério não separa as opções. Fato que sustenta: visitas de 7 dias, 77 [FATO, L9]; 21 por dia pede 2x [ESTIMATIVA, derivar 1].
**Efeito de 2ª ordem da posição:** se o Bruno não gravar, o depois vira só TV de perfil e timelapse, formatos sem medida; e o mais votado repete um assunto que o seguidor já viu.

### D2. Gravação, nicho, Dentista C e remakes

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 2 falas por semana: 1 selfie da TV + 1 nicho, 24 a 36 min | 2 reels de frente por semana | O teste de nicho anda devagar: com 1 nicho por semana, n de 3 só em 11/11 se contar A e B |
| (b) Sessão de 90 min com 5 roteiros | 5 reels por semana | Já foi plano em 21/10 e não aconteceu [FATO, fato 105] |
| (c) Zero gravação, estoque | Nenhuma carga de gravação | A conta volta ao normal de 37,5 a 57; S3 e S4 com cortes de perfil |
| (d) Fora do óbvio: depois de cada conversa de diagnóstico, o Bruno grava 40 s contando a pergunta que ouviu, sem dado do cliente | Conteúdo nasce do funil | Depende de haver conversas (hoje, sem dado); cuidado com sigilo |

**Posição:** (a), com R1 a R3 como Trial Reel e o C pela condição do B.
**Premissas:** o Bruno consegue 30 min por semana; o formato selfie mantém mais de 100 de alcance fora da fase da saga [HIPÓTESE 16]; consórcio sem a linha da ABAC é publicável.
**Probabilidade:** 0,30 [0,15, 0,50]. **Confiança:** 0,45.
**Conta:** chance de os blocos acontecerem toda semana 0,4 [PRIOR, nenhuma gravação desde 21/10, fato 104]; dado que acontecem, chance de mediana de 53 ou mais e pulo até 75% de 0,8 [PRIOR, 4 de 4 reels do Bruno acima de 128 de alcance]; 0,4 x 0,8 = 0,32.
**Efeito de 2ª ordem:** a selfie da TV pode render mais que o nicho e puxar a grade para "autoridade" no lugar de "profissão nomeada", adiando a resposta do brief de 21/10.

### D3. Grade e operação

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 5 reels e 2 carrosséis fixos, 1 post de feed por dia, até 4 reels quando faltar peça com o Bruno | Cumpre o CLAUDE.md; nenhum dia com 2 reels | 7 carrosséis a produzir pesam na agência |
| (b) 6 reels na S1 com motivo | Mantém o tl02 no sábado | Fere a regra sem dado a favor; S2 começa vazia |
| (c) 6 a 7 por semana como TESTAR | Mais vagas | Sem estoque com rosto, enche de formato sem medida |
| (d) 3 reels e 2 carrosséis sem gravação | Menos carga | Pode ser lido como abandono; perde o sábado |
| (e) Fora do óbvio: agendar só a semana seguinte, sempre no sábado, depois de ver os números da semana corrente | Menos peça agendada errada | Pede disciplina semanal da agência e do Bruno |

**Posição:** (a) com (e).
**Premissas:** a agência entrega os carrosséis nos prazos; o Bruno agenda no sábado; feriado não derruba alcance [HIPÓTESE 24].
**Probabilidade:** 0,12 [0,05, 0,30]. **Confiança:** 0,45.
**Por que:** o critério pede 0 vaga vazia (minha posição aceita semana de 4), mediana semanal de 42 ou mais nas 4 semanas, 106 ou mais em 2 delas, e ganho líquido de 12 seguidores nos 14 dias depois de 27/10. O último sozinho: 0,3 [PRIOR; últimas semanas +9, -2 e 0, fato 18].
**Efeito de 2ª ordem:** um post de feed por dia deixa o perfil com cara de ativo para quem chega pela TV e deixa cada post sozinho no dia, sem disputa.

### D4. Stories e ob01 a ob03

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 03-plano estendido (8 por dia, 27 à mão) | Mais views de story | Carga à mão que o Bruno pode não cumprir; nenhum dado de execução ainda |
| (b) 3 a 5 por dia | Pouca carga | Views de story caem; story é 57% das views de 7 dias [FATO, L9: 1.178 de 2.073] |
| (c) S1 como está; S2 em diante 6 a 7 por dia, 3 à mão | Equilíbrio | Precisa de cerca de 25 estáticos novos por semana da agência [ESTIMATIVA] |
| (d) Fora do óbvio: 3 vezes por semana, um story falado de 15 s do Bruno de frente no lugar do estático das 09h | O formato que funciona no feed testado no story | Mais um item à mão; sem dado de story falado |

**Posição:** (c), com (d) como TESTAR na S3 (seg, qua e sex às 09h), medido pela saída do 1º story. ob01 a ob03 como substitutos de vaga a partir da S2, nunca em 02/11.
**Premissas:** a S1 agendada sai sem erro; a leitura de story na mesma hora toda segunda; os ob passam na folha até 30/10.
**Probabilidade:** 0,25 [0,10, 0,45]. **Confiança:** 0,5.
**Conta:** 982 views ou mais toda semana, 0,65 [PRIOR; hoje 1.178 com uma pilha cheia, L9]; 6 respostas a cada 14 dias, 0,45 [PRIOR; base 3 em 7 dias, L9]; ob com média de 42 ou mais, 0,55, mas com chance de nem entrarem; produto dos três, perto de 0,15 a 0,25.
**Efeito de 2ª ordem:** a enquete diária mede objeção, mas o voto não chega aos agentes [FATO, fato 67]; sem o Bruno anotar, a linha de objeção não aprende.

### D5. Portão do Módulo 7

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) Régua 53 fixa | Comparável de 25/10 a 23/11 e com o brief de 21/10 | Pode ficar alta se a conta continuar fraca |
| (b) 57 views | Bate com o ig_reel_checkup | Mistura métrica com a regra dos 150 de alcance |
| (c) 37,5 de alcance | Mais fácil de passar | Mais MANTER sem mérito |
| (d) Mediana refeita a cada rodada | Acompanha a conta | Quebra a comparação entre semanas |
| (e) Fora do óbvio: comparar cada formato com o melhor formato disponível (Bruno de frente, 167,5), e não com a conta | Mostra o custo de cada vaga | n do Bruno ainda é 4; vira informação, não regra |

**Posição:** (a), com (e) ao lado só como informação; no máximo 3 decisões por rodada.
**Premissas:** os agentes conseguem ler o Buzzfy toda segunda; o Bruno lê o arquivo e marca "executado".
**Probabilidade:** 0,15 [0,05, 0,35]. **Confiança:** 0,55.
**Conta:** 5 rodadas registradas, 0,75 [PRIOR]; todas as decisões executadas até a segunda seguinte, 0,3 [PRIOR, base de 3 de 8 sem execução, fato 125]; S4 acima da S1, 0,45 [PRIOR, a S1 tem o embalo do Dentista A e da TV]; nenhum PARAR com n de 1, 0,95 (regra escrita).
**Efeito de 2ª ordem:** decidir menos por rodada aumenta a execução e deixa o aprendizado mais lento; a primeira resposta sobre formato TV só sai em 09/11.

### D6. TABULEIRO e o caminho

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) TABULEIRO em todo post de novembro que cumprir 150 | Mais chances | Fere "uma por mês" na leitura estrita |
| (b) Um post por mês | Cumpre a regra | Poucas chances: teto de 3,7 a 5,5 comentários de qualquer tipo até 22/11 [ESTIMATIVA, derivar 13] |
| (c) (a) ou (b) mais desligar as automações de conta toda | Menos colisão com a série | Nenhum custo visível (0 disparo) |
| (d) Não ligar até testar o caminho de ponta a ponta | Menos risco de quebra | Perde a 1ª selfie de nicho |
| (e) Fora do óbvio: aceitar que palavra-chave não é o caminho nesta conta e pôr o peso no pedido aberto e no link da bio | Palavra-chave rende 0,043x contra 0,081x de outros pedidos no mercado; 0 de 9 estouros pequenos a usaram [FATO, fato 164] | Contraria uma regra do CLAUDE.md; precisa de 1 mês de dado próprio antes |

**Posição:** (b) mais (c) mais o teste de (d) antes de 04/11; (e) como hipótese a decidir em 23/11 com o resultado de novembro.
**Premissas:** o nicho 1 é gravado; a nova TABULEIRO dispara com texto genérico; o Bruno informa os diagnósticos.
**Probabilidade:** 0,08 [0,02, 0,20]. **Confiança:** 0,6.
**Conta:** 3 disparos de terceiros até 22/11 com 2 posts (B e nicho 1) a cerca de 170 de alcance e 0,65 comentário por 100 contas dariam 2,2 comentários de qualquer tipo [ESTIMATIVA, derivar 12]; 3 disparos de TABULEIRO pedem mais que isso. 1 diagnóstico agendado até 18/11, 0,3 [PRIOR]; o produto dos dois, perto de 0,05 a 0,1.
**Efeito de 2ª ordem:** com 0 disparo em novembro, o caminho da palavra-chave fica refutado com dado próprio, e dezembro pode testar outro pedido sem discutir regra.

---

## 6. Ideias e hipóteses numeradas

| # | Ideia ou hipótese | Confiança | Evidência |
|---|---|---|---|
| 1 | A data de 02/11 é trava de texto e de permissão, não alavanca de alcance | média | fatos 5, 6, 136 e 155 (n de 3 por fase) |
| 2 | O formato Bruno de frente decide o alcance nesta conta | alta | fatos 25, 27 e 29 (n 4 contra 12, período confundido) |
| 3 | Os cortes da TV são um formato novo, sem medida: Bruno de perfil, de costas ou atrás do monitor | alta como fato | fato 88 e L8 |
| 4 | O "pode seguir" do Bruno responde o D1 por padrão: datas mantidas | alta | mensagem do Bruno, fato 1 |
| 5 | Mover o tl02 para dom 01/11 18h30 resolve a regra dos 5 e cria a véspera | média | fatos 76 e 78, L4 |
| 6 | A legenda do tl02 fica literal na véspera ("vai ao ar na segunda, 02/11") | alta | fato 78 |
| 7 | A selfie "o que eu disse na TV" junta o formato medido com o ativo novo, sem trava de conselho | média | fatos 25, 103 e 157 (n de 1) |
| 8 | Gravação mínima menor aumenta a chance de a gravação acontecer | média | fatos 104 e 105 (90 min planejados, 0 gravados) |
| 9 | Bio nova com a TV e "Estrategista de Lançamento" antes de 02/11 | média | fato 9 (bio do Módulo 2 não aplicada), 02-provas (termo contaminado) |
| 10 | Fixar 3 posts com o rosto do Bruno até dom 01/11 21h | média | fato 51 (111 contra 34,5) |
| 11 | Destaque NA TV no lugar do PROVA, que não existe | média | fatos 64 e 68 |
| 12 | Nenhum reel em 02/11 sem selfie gravada | média | fato 155 (no dia, 0,045x, n de 3) |
| 13 | Story agendado com "SEG, 02/11", nunca "HOJE" nem "AMANHÃ" | alta | 03-plano (story fica 24 h) |
| 14 | Sem hora às 11h de 02/11, story com link para /ao-vivo e "a grade sai no site" | média | fato 135 |
| 15 | "Foi ao ar" só com o horário confirmado e passado | alta | fato 6 |
| 16 | Story de agradecimento à Mirna depois da exibição | média | PRIOR 3 (menção avisa) |
| 17 | @ no texto da legenda como plano B da marcação | média | fato 139; PRIOR 1; 1,13x (fato 148) |
| 18 | O teste no tl01 em 25/10 18h35 decide o método de marcação das 10 peças | alta | a buscar 5 |
| 19 | Marcar a Mirna só onde ela aparece ou fala | alta | fato 90; hipótese 37 |
| 20 | Mostrar tl04 e tl05 à Mirna antes | média | fato 90 (recorte e carimbo no rosto dela) |
| 21 | Convite de colaboração em uma peça só, o mais votado, com o ok dela | baixa | fato 139; hipótese 36 |
| 22 | Desligar 15 automações de comentário antes do tl01 | alta | fatos 114, 116 e 125 |
| 23 | CASE e ESTRATEGISTA colidiriam com comentários da série | média | fato 114; hipótese 46 |
| 24 | po01 sem "Comenta a palavra" | alta | fato 80 |
| 25 | ci01 só com a voz de "Ainda. Sempre vai ser." conferida | alta | fato 91 |
| 26 | ci01 é a peça de abertura mais fraca da S1 | média | fato 88 (de costas até 2,5 s) |
| 27 | Dentista C no lugar do ci01 se o B fizer 106 ou mais com pulo abaixo de 60% | média | fato 149 (2º post da sequência, 1,63x) |
| 28 | Sem sinal do B, o C fica para anúncio depois de 18/11 | alta | fato 101 |
| 29 | R1 primeiro entre os remakes | média | fato 150 (35% com original de 5x ou mais) |
| 30 | Remake com legenda queimada e texto no quadro 0 | média | fatos 145 e 147 |
| 31 | Remake sem cortar o preâmbulo | média | fato 38 |
| 32 | Trial Reel não conta nos 5 e conta nos 6 h | baixa | hipótese 32 |
| 33 | Conta não elegível: R1 vira o 1º substituto como reel normal | média | fato 139 |
| 34 | Régua 53 fixa nas 4 semanas | alta | fatos 24, 168 e 169 |
| 35 | Peça decide com n de 1; formato só com n de 2 | média | critério do D5; fato 33 (revisão depois de 48 h) |
| 36 | No máximo 3 decisões por rodada, com dono e prazo | média | fatos 125 e 180 |
| 37 | Rodada de 02/11 pelos agentes às 19h; Bruno executa até ter 03/11 11h | alta | enquadramento conflito 4 |
| 38 | tl02 sai do plano só se o tl01 falhar nos dois critérios | média | fato 173 e regra de n |
| 39 | tl03 a tl05 decididos com n de 2 timelapses ou mais | média | fato 170 |
| 40 | O mais votado do tl01 sai ter 03/11 21h | alta | fato 77 |
| 41 | Com menos de 5 votos, assunto 6 "Zero reais", dito nos stories | média | fato 170; hipótese 38 |
| 42 | mc04 cortado em 1705,567 s | alta | L6 e 02-provas |
| 43 | mc04 em seg 02/11 09h01 | média | enquadramento conflito 8 |
| 44 | car02 com as perguntas e car03 com as respostas | baixa | fato 156 (antes = convite sem trecho, n de 3) |
| 45 | Todo carrossel com foto do Bruno na capa | alta | fato 51 |
| 46 | 1 post de feed por dia como grade padrão | média | fato 152 (0,92x a menos de 6 h); fato 44 |
| 47 | 21h nos reels de dia útil | alta | fato 39 |
| 48 | Selfie de 02/11 às 11h testa a hora com o formato do Bruno | baixa | R2 às 11h11 com 4,42x (fato 35, n de 1) |
| 49 | Feriado tratado como dia normal e medido | média | fato 41 (n de 3, animação) |
| 50 | Stories da S1 como estão | alta | L2 |
| 51 | Prioridade dos manuais: link, compartilhar, enquete, repost | média | L9 (0 clique e 0 toque em 7 dias) |
| 52 | Da S2 em diante, 3 stories à mão por dia | média | derivar 18 (170 a 327 min por semana) |
| 53 | Story das 09h sempre com o Bruno em cena | baixa | hipótese 61; L10 mostra o story sem o Bruno com o maior alcance da pilha, mas com 8,2 h de vida |
| 54 | Ler a pilha de stories todo dia às 08h30 | alta | fato 67 |
| 55 | Linha "feito ou não feito" para cada item à mão | alta | critério do D3 |
| 56 | ob01 a ob03 só como substitutos a partir da S2 | média | L8; derivar 23 |
| 57 | ob02 só a partir de 10/11 e sem pf01 reel | média | hipótese 34 |
| 58 | Copiar o estoque para o Drive até seg 26/10 | alta | fato 110 |
| 59 | Apagar o rascunho de release público | alta | fato 111 |
| 60 | Link da edição sim; recorte da exibição nunca | alta | fato 137 |
| 61 | Nada de anúncio pago com material da TV sem autorização escrita | alta | fato 137 |
| 62 | Minutos do tl01 e do car01 não valem para a edição exibida | média | fato 81; hipótese 39 |
| 63 | O14 respondida com caso e método, não com a própria TV | média | F6 |
| 64 | Pedir ao Bruno os números de diagnóstico toda segunda 18h | alta | fato 143 |
| 65 | linkTracking ligado na TABULEIRO de novembro | média | hipótese 51 |
| 66 | TABULEIRO de novembro na 1ª selfie de nicho | média | fato 30 e regra do catálogo (fato 170) |
| 67 | Texto genérico na nova TABULEIRO | alta | fato 117 |
| 68 | O Bruno manda o link da edição à rede de Campinas | baixa | fato 19 (53,1% dos engajados), fato 137 |
| 69 | A meta de 10 diagnósticos não fecha só com o Instagram no volume de hoje | alta como conta | derivar 14; 00-SISTEMA Projeção |
| 70 | Definir se "diagnóstico" da meta é o teste ou a conversa | alta | fato 131 |
| 71 | Pico de visitas em 02 a 04/11 sem grupo de controle: indício, não prova | alta | enquadramento D1 |
| 72 | Ler não seguidores por semana para ver a marcação e a TV | média | derivar 28; L9 (362 não seguidores) |
| 73 | A mediana da S4 acima da S1 é improvável se a S1 levar o embalo do A e da TV | baixa | fato 43 |
| 74 | Selfie da TV com uma pergunta da entrevista como roteiro, sem teleprompter | média | fato 104 (fala de 36,4 s em uma tomada) |
| 75 | Abrir a selfie dizendo quem fala e onde falou ("Me perguntaram na TV Câmara...") | baixa | fato 162 (gancho de autoridade, n de 3) |
| 76 | Nada novo com "estrategista digital" | alta | 02-provas |
| 77 | Janela de 7 dias de story lida sempre na mesma hora | alta | fato 56 e L9 |
| 78 | A pilha perde cerca de 30% do 1º ao 4º story | média | L10 (36, 34, 25, 22, provisório) |
| 79 | Plano B pronto se a produção pedir "só depois de 02/11" | alta como contingência | fato 5 |
| 80 | A chamada de sáb 31/10 17h30 precisa sair com o tl02 | alta | L1 |
| 81 | Vaga vazia custa menos que reel sem rosto ou sintético | média | fatos 27 e 44 |
| 82 | Não fazer REACT de 20 min nestas 4 semanas | média | fato 106 (20 min contra 40 s de selfie) |
| 83 | S3 e S4 como vaga com regra até o portão, não peça fixa | média | Módulo 7 |
| 84 | TESTAR na S3: selfie da TV contra corte da TV no mesmo assunto (só o formato muda) | média | fato 157 contra fato 155 |
| 85 | Pedido de seguir na legenda de 02 a 04/11 | baixa | fato 148 (1,12x); hipótese 31 |
| 86 | Story falado de 15 s do Bruno 3 vezes por semana na S3 | baixa | fato 25 levado para story, sem dado de story |
| 87 | Se o B estourar, o próximo post (pb01) já ganha o efeito de sequência, mesmo sendo outra linha | média | fato 149 (o 1,81x é do post seguinte) |
| 88 | A conta do 00-SISTEMA (150 de alcance por reel) só vale nas semanas com 2 selfies ou mais | média | fato 25; Projeção |
| 89 | Votos de enquete e respostas anotados pelo Bruno antes de expirar, senão a linha de objeção não aprende | alta | fato 67 |
| 90 | Novembro com 0 disparo de TABULEIRO refuta o caminho da palavra-chave com dado próprio | média | fatos 122 e 164 |

---

## 7. Pre-mortem: como este plano fracassa

Escrito como se fosse 23/11 e tudo tivesse dado errado.

1. **O Bruno não gravou.** O bloco 1 não saiu até 28/10, nem os seguintes. A S2 ficou com tl02, mais votado, ob01, tl03 e um remake; a S3 e a S4 com cortes de perfil e timelapses. A conta voltou ao normal de 37,5 a 57. Meu plano pôs o peso do depois na selfie e não tinha força para obrigar a gravação. Sinal de alerta: qua 28/10 23h59 sem arquivo. Resposta prevista: remakes como reels normais a partir da S2.
2. **A produção da TV reclamou dos cortes antes da exibição.** O "pode seguir" foi da Mirna, não da produção; ela pediu para tirar. O plano B existia, mas pb01, car01 e ci01 já tinham saído. Sinal: print não chegou até seg 26/10 18h.
3. **A TV não trouxe ninguém.** Visitas ao perfil de 02 a 04/11 ficaram na base de 10 a 11 por dia. Não é falha do plano (ele previa isso), mas o Bruno pode ler como falha da série inteira e abandonar a linha boa junto.
4. **A carga à mão não foi feita.** Stories com sticker, marcações e compartilhamentos ficaram pela metade; os números de story caíram, e o Módulo 7 não soube se foi o conteúdo ou a execução, porque a linha "feito" não foi preenchida.
5. **A régua fixa de 53 virou PARAR para tudo.** Com o Bruno de perfil, os cortes ficaram em 30 a 45, e a regra mandou parar formatos inteiros no meio da semana da TV. Eu defendi n de 2, mas 2 peças fracas de um formato novo ainda são pouco.
6. **TABULEIRO com 0 disparo.** O nicho 1 não foi gravado, novembro ficou sem palavra, e o caminho até o diagnóstico seguiu sem nenhuma medida além dos 7 cliques do mês.
7. **Erro de agenda.** Ao mover o tl02, o Bruno esqueceu o story das 17h30 de sábado, que chamou "SÁB 18H30 NO FEED" para um reel que não saiu. Pequeno, mas visível.
8. **Meu ponto cego se confirmou ao contrário.** Ao proteger o que funcionava, mantive 5 cortes de TV que esgotaram o miolo antes da exibição; quem viu a TV encontrou o feed repetindo o que acabou de ver.

---

## 8. Previsões numéricas com data de conferência

Todas [PRIOR] salvo indicação; conferência pelos agentes com Buzzfy e PostZen, e pelo Bruno quando o dado for dele.

| Métrica | Previsão (faixa) | Data de conferência |
|---|---|---|
| Mediana de alcance em 48 h dos 5 reels da S1 | 60 (35 a 110); chance de 42 ou mais: 0,65 | seg 02/11 19h |
| Alcance do tl01 em 48 h | 45 (20 a 90) | ter 27/10 18h35 |
| Alcance do Dentista B em 48 h | 90 (40 a 170) | seg 26/10 21h05 |
| Visitas ao perfil por dia de 02 a 04/11 | 13 (8 a 25); chance de 21 ou mais: 0,2 | sex 06/11 |
| Saldo de seguidores de 25/10 a 08/11 | +4 (-6 a +20); chance de positivo: 0,6 | qua 11/11 |
| Ganho líquido de 28/10 a 10/11 (piso do brief: 12) | +6 (-4 a +25); chance de 12 ou mais: 0,3 | sex 13/11 e qua 18/11 |
| Mediana de alcance dos reels de nicho (A, B, nicho 1) | 120 (60 a 170), se o nicho 1 sair | qua 11/11 |
| Disparos de TABULEIRO de terceiros até 22/11 | 1 (0 a 4); chance de 3 ou mais: 0,12 | seg 23/11 |
| Diagnóstico agendado até 18/11 | sem dado para os agentes; palpite 0 a 2, chance de 1 ou mais: 0,3 | qua 18/11 (número do Bruno) |
| Views da edição do Bruno no site da TV Câmara | 150 (40 a 600); chance de passar de 124: 0,55 | seg 09/11 |
| Views de story em 7 dias, lidas seg 19h | 1.150 (800 a 1.600) | seg 23/11 (D+30) |
| Mediana semanal de alcance de reel na S4 | 70 (35 a 150); chance de passar a S1: 0,45 | seg 23/11 (D+30) |
| Rodadas do Módulo 7 registradas de 26/10 a 23/11 | 5 de 5 (3 a 5); chance de 5: 0,75 | seg 23/11 (D+30) |
| Seguidores | 1.630 (1.605 a 1.670) | seg 23/11 (D+30) |
| Reels com o Bruno de frente publicados de 25/10 a 22/11 | 5 (0 a 10) | seg 23/11 (D+30) |
| Seguidores | 1.650 (1.600 a 1.730) | qua 23/12/2026 (D+60) |
| Reels com o Bruno de frente publicados de 25/10 a 23/12 | 10 (2 a 18) | qua 23/12/2026 (D+60) |
| Diagnósticos no mês de dezembro | sem dado; palpite 1 (0 a 4), pelo número do Bruno | qua 23/12/2026 (D+60) |
| Seguidores | 1.680 (1.600 a 1.800) | sex 22/01/2027 (D+90) |
| Visitas ao perfil orgânicas em 30 dias | 400 (250 a 700) | sex 22/01/2027 (D+90) |
| Parte dos reels dos últimos 30 dias com o Bruno de frente | 50% (20% a 80%) | sex 22/01/2027 (D+90) |

---

## 9. O que mudaria minha opinião, lacunas e fontes

### 9.1 O que mudaria minha opinião

- Se os 5 cortes da S1 fecharem com mediana de 106 ou mais e pulo abaixo de 60%: a TV de perfil funciona, e o depois deve ganhar mais cortes e menos selfies. Troco a prioridade do P13.
- Se as visitas ao perfil de 02 a 04/11 passarem de 30 por dia: a TV traz gente, e o dia 02/11 merece reel e mais stories nas próximas aparições.
- Se a Mirna ou a produção pedirem para segurar: plano B do P5 no mesmo dia.
- Se a selfie da TV 1 ficar abaixo de 42 com pulo acima de 75%: a vantagem do Bruno vem do assunto ou do período, não do rosto (hipótese 16 refutada), e a régua do CLAUDE.md precisa de nova leitura.
- Se o Bruno informar que já tem diagnósticos agendados vindos de fora do Instagram: o peso da série muda de captar para dar prova a quem já conversa.
- Se a conta for elegível a Trial Reel e o R1 bater o alcance usual: remakes viram linha fixa de 1 por semana.
- Se o teste de ponta a ponta da TABULEIRO falhar: novembro sem palavra e com pedido aberto.

### 9.2 Lacunas (sem dado)

- Horário da exibição de 02/11; se reprisa; quando sobe no site e no YouTube; em que minuto o Bruno aparece.
- @ da Mirna, se aceita marcação em série, colaboração e uso permanente no destaque; se o "pode seguir" vale como ok da produção.
- Se o app deixa marcar pessoa em reel e carrossel publicados; se o @ no texto avisa.
- Votos do tl01; data do bloco de gravação 1; minutos reais por fala.
- Elegibilidade a Trial Reel e se ele conta nos 5.
- Quadros de tl04 e tl05 nos 3 primeiros segundos (não conferidos nesta cadeira).
- Folha de 4 quadros por segundo e notas de ob01 a ob03; quem diz "Ainda. Sempre vai ser." no ci01.
- Seguidores de 22 e 23/10 (pendentes às 17h41).
- Audiência da TV; alcance em feriado com o Bruno.
- GA4, WhatsApp, diagnósticos agendados e feitos; definição de "diagnóstico" da meta.
- Leituras de conselho (OAB, CFN 856, ABAC, CFP, CFO 196/2019).
- Se a gravação do celular conta como conteúdo da emissora para os termos de uso (não é parecer jurídico).
- Autorização da Tzur para o case v2.

### 9.3 Fontes

- Repositório: `CLAUDE.md`; `conteudo/modo-god-cronograma/contexto.md`; `run/00-enquadramento.md`; `run/01-fatos.md` (fatos 1 a 185, a buscar 1 a 43, derivar 1 a 33, palpites 1 a 62); `conteudo/sistema-instagram/00-SISTEMA.md` (linhas 20 e 407 a 419); `semanas/2026-10-21.md`; `stories-objecoes/01-objecoes.md`, `02-provas.md` (linhas 120 a 163), `03-plano-7-dias.md` e `.json`, `05-manuais-bruno.md`, `06-agenda-postzen.md`; `videos/tv-camara/cortes/*.spec.json`; git log (commits eeb4f21, 9603c3c, 2b3a7d8).
- PostZen `listPosts`, conta j97772ycndetk3f1wcdbh14p898g4b8w, de 24/10 03h00 UTC a 01/12 03h00 UTC, ordenado por data, 48 itens, lido às 17h41.
- Buzzfy, 17h41 a 17h44: `ig_follower_growth` (14 dias), `ig_account_stats` (7 dias), `ig_posts` (stories), `ig_post_stats` (6 stories de 24/10, sem mediana).
- HEAD em media.postzen.dev do mc02 (1.370.775 bytes, 17h45); `stat` e `ffprobe` dos renders locais de mc02, mc04 e ob01 a ob03 na pasta da sessão (`scratchpad/tv/render` e `scratchpad/tv/ig`); folha de quadros `scratchpad/cadeiraL/ob_folha.png` (17h47).
- Frentes F1 a F8 pelo resumo dado na tarefa e pelos números citados no livro de fatos.
