# Plano da cadeira I · Performance de mídia paga · Cronograma 25/10 a 22/11/2026 · @o_estrategista.com.br

Sábado, 24/10/2026, escrito entre 17h25 e 18h40 (horário de São Paulo). Trabalho isolado: não li os planos das outras cadeiras. Fontes de base: `contexto.md`, `run/00-enquadramento.md`, `run/01-fatos.md` (livro de fatos, numerado como "fato N"), as frentes F1 a F8 e as leituras próprias da seção 0.

**Persona:** diretor de performance em Google Ads e Meta Ads, com anos de leilão B2B e B2C no Brasil.

**OTIMIZA PARA:** lead qualificado ao menor custo, com controle do leilão. Nesta conta não há verba até 18/11 (decisão escrita de 21/10, fato 169). Então o "custo" aqui é o minuto do Bruno e a hora da agência, e o "leilão" é a distribuição do Instagram: o lance que eu controlo é o criativo (formato, gancho, quem está no quadro 0) e o espaçamento entre peças.

**PONTO CEGO, assumido por escrito:** eu tendo a subestimar canal de demanda criada, que é difícil de medir: a TV, a marcação da Mirna, os stories (de 54% a 56% das views da semana) e a indicação. Tendo a cortar o que não aparece no último clique. **Como compenso neste plano:**
1. A semana da TV não é julgada só pelo alcance de cada post. Ela tem 4 medidas de demanda: visitas ao perfil por dia, alcance de não seguidores em 7 dias, seguidores e directs que citam a TV (contados pelo Bruno).
2. Nenhuma peça da família da TV recebe PARAR na S2 com alcance entre 27 e 41 em 48 h se as visitas ao perfil de 02 a 04/11 ficarem em 21 ou mais por dia. Abaixo de 27, a régua vale.
3. Stories continuam todo dia mesmo com 0 clique medido, porque nenhuma ferramenta permitida lê toque em link (fato 67).
4. O que eu não sei medir fica escrito "sem dado", nunca "não funciona".

**PERGUNTA CONTRÁRIA:** e se a busca não tiver volume para crescer no ritmo que o cliente quer? Resposta na seção 1.2.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha uma objeção sozinho. Métrica que falta: "sem dado".

**Regra de operação:** nenhum agente publica, agenda ou altera nada no Instagram, no Buzzfy, no PostZen ou em conta de anúncio. Tudo que este plano manda mudar é ação do Bruno, com prazo, na seção 2, pergunta 21.

---

## 0. Leituras novas desta cadeira (só leitura, sábado 24/10, 17h24)

| # | Fato novo | Fonte | Muda o quê |
|---|---|---|---|
| N1 | 48 itens de 24/10 a 01/12: 5 publicados (stories de 14h00, 14h03, 15h00, 15h01 e 16h30) e 43 agendados. Entraram 28 stories de 25/10 a 31/10 (registro às 17h06, commit eeb4f21). O livro de fatos (15h46) contava 20 itens | PostZen `listPosts`, conta j97772ycndetk3f1wcdbh14p898g4b8w; `conteudo/stories-objecoes/06-agenda-postzen.md` | A semana 1 de stories já está agendada. O plano mexe só nas chamadas que dependem do ci01 |
| N2 | O feed agendado não mudou: Dentista B 24/10 21h, tl01 25/10 18h30, pb01 26/10 21h, car01 27/10 12h, ci01 28/10 21h, po01 29/10 21h, pb02 30/10 21h, tl02 31/10 18h30, tl03 07/11, tl04 14/11 e tl05 21/11 às 18h30. Nada de dom 01/11 a sex 06/11 | PostZen `listPosts` 17h24 | A semana da exibição continua vazia no feed |
| N3 | O story pf01 (ter 27/10 16h) usa agora o arquivo `pf01-dentista-story-v2.mp4` (versão "em dois meses") | PostZen `listPosts` e 06-agenda-postzen.md | A dúvida do fato 85 sobre qual versão vale fica resolvida a favor da v2 |
| N4 | 7 dias (17/10 20h24 a 24/10 20h24 UTC): alcance 576 (215 seguidores, 362 não seguidores), 0 de anúncio; views 2.055 (story 1.160, reel 448, post 280, carrossel 165); 77 visitas ao perfil; 0 clique no site; 0 toque em link; 2 comentários; 4 compartilhamentos; 3 respostas. Seguindo: 3.529 | Buzzfy `ig_account_stats` days=7, 17h24 | Base de story de 7 dias já está em 1.160, contra 982 às 14h11: a janela móvel não serve de base fixa |
| N5 | ob01 (17,9 s, render às 16h33), ob02 (28,37 s, 15h54) e ob03 (15,1 s, 17h00) têm render final, com cópia para o Instagram. Nenhum está no PostZen | `ffprobe` e `stat` em scratchpad/tv/render e scratchpad/tv/ig | A lacuna "render de ob01 a ob03" fecha. Folha de 4 quadros por segundo: não li |
| N6 | O mc04 renderizado vai de 1700,967 a 1705,567 s (4,6 s) e termina em "família." | `videos/tv-camara/cortes/mc04.spec.json` | O ponto de recorte já está escolhido dentro da faixa do 03-plano |
| N7 | A lista de stories à mão da semana 1 tem 27 itens de 25/10 a 31/10 (4, 4, 3, 4, 4, 4 e 4 por dia) | `conteudo/stories-objecoes/05-manuais-bruno.md`, conta minha | Carga à mão da S1 já está definida |
| N8 | O reel "Ele nunca fez um anúncio" (R1) tem 308 de alcance, que o `ig_post_stats` conta só como orgânico, e pulo de 53,2% | fatos 25, 35 e 140 | É o único reel da conta que hoje passa no portão de impulsionar do brief de 21/10 (300 ou mais de alcance orgânico e pulo abaixo de 55%) |

---

## 1. Veredito

### 1.1 Em 10 linhas

1. O gargalo desta conta hoje é captura e medição, não volume: em 7 dias foram 77 visitas ao perfil, 0 clique no site, 0 disparo real de automação e 0 venda [FATO, N4 e fatos 8 e 116].
2. D1: o ci01 sai de qua 28/10 e vai para seg 02/11 21h; pb01, car01, po01 e pb02 ficam. A S1 fecha em 5 reels e a S2 deixa de estar vazia na semana de maior demanda.
3. O resto da S2 é decidido por um portão da família da TV (pb01, po01 e pb02 com 48 h até dom 01/11 21h): se passar, entram ob01, ob03 e o "mais votado"; se não passar, entram remakes com o Bruno de frente.
4. Gravação é a ação de maior retorno por minuto: 1 bloco por semana até quarta 23h59, com 2 roteiros no mínimo. O 1º bloco abre com a selfie de 02/11.
5. O perfil vira página de destino antes de dom 01/11 18h: bio do Módulo 2 sem o número da Tzur, link `/tabuleiro/?o=ig-bio`, 3 fixados e destaque NA TV.
6. Mídia paga: zero até 18/11 e nunca com conteúdo da TV. De 19/11 em diante, o único reel que já passa no portão de impulsionar é o R1.
7. Busca paga fica fora das 4 semanas: o volume de busca é sem dado, e a meta de 10 diagnósticos por mês não fecha nem por busca nem por bio neste prazo.
8. Régua única do começo ao fim: 53 de alcance em 48 h (27, 42, 106 e 150; pulo de 60% e 75%), com uma coluna nova de minutos do Bruno por peça.
9. TABULEIRO: uma automação de conta toda com texto genérico a partir de dom 01/11, pedido só no post seguinte a um 150 em 48 h, no máximo 1 por semana e nunca em 02/11. As 5 automações de conta toda saem antes do tl01.
10. A chance de cumprir os critérios do enquadramento é baixa em todas as decisões (de 8% a 30%). O plano escolhe o caminho mais provável e mais barato de reverter, não um caminho seguro.

### 1.2 Resposta à pergunta contrária: e se a busca não tiver volume?

- [FATO] Não existe dado de volume de busca para os agentes: Planejador de Palavras-chave, Google Ads e Search Console ficam fora das ferramentas desta rodada, e o GA4 G-F91ET225YW só o Bruno lê (fatos 130 e 143).
- [FATO] O site recebeu 7 cliques vindos do Instagram em 30 dias e 0 em 7 dias (fato 14 e N4). Não há agenda on-line, e a origem `o=` se perde antes do WhatsApp (fatos 128 a 130).
- [PRIOR] Busca por termo de categoria ("estrategista de lançamento", "lançamento de infoproduto" com Campinas) tende a ter volume baixo para serviço B2B de nicho. A busca pelo nome do Bruno só existe depois que alguém o conhece. Nível 4: não fecha nada sozinho.
- **Consequência para o plano:** busca paga não entra nas 4 semanas, e a meta não depende de busca. O ritmo vem de demanda criada (reels com o Bruno, TV, marcação da Mirna, stories) e de captura no perfil (bio, fixados, direct e WhatsApp).
- **Como testar barato:** se o site estiver verificado no Search Console (sem dado), o Bruno compara as consultas com o nome dele e com "estrategista de lançamento" de 02 a 08/11 contra 19 a 25/10. Se a busca de marca subir depois da TV, uma campanha de pesquisa só de marca, com teto baixo, protege a captura [PRIOR]. Se não subir, busca não é canal agora.
- **Ritmo honesto:** para 10 diagnósticos por mês só pela bio, com 1,57% de clique e 100% de conversão depois do clique (premissa impossível, usada como piso), seriam 637 visitas por mês [ESTIMATIVA, F8: 10 / 0,0157]. O ritmo orgânico atual é de cerca de 330 visitas por mês [ESTIMATIVA: 77 / 7 x 30, N4]. Nem a busca nem a bio fecham a meta em 4 semanas. O que encurta o caminho é a conversa direta (direct e WhatsApp), que não depende de clique no site.

---

## 2. Respostas às 22 perguntas

### P1. Quais decisões o plano move, qual número muda, com que fonte e em que segunda é lido?

| D | O que o plano muda | Número que deve mexer | Fonte | Segunda de leitura |
|---|---|---|---|---|
| D1 | ci01 vai para seg 02/11 21h; po01 fica e é fixado de 01 a 08/11; S2 preenchida por portão; perfil vira página de destino | visitas ao perfil por dia de 02 a 04/11 (base 11,0 por dia [ESTIMATIVA: 77 / 7, N4]); alcance de não seguidores em 7 dias (base 362, N4); seguidores de 25/10 a 08/11 | `ig_account_stats`, `ig_follower_growth` | 02/11 (S1) e 09/11 (S2); saldo até 08/11 só fecha em 11/11 (fato derivado 5) |
| D2 | Bloco 1 até qua 28/10 23h59, com a selfie de 02/11 primeiro; piso de 1 roteiro por semana; ordem fixa sem gravação; conferência de nicho proposta para 16/11 | mediana de alcance e pulo dos reels de nicho em 48 h; reels com o Bruno de frente por semana | `ig_post_stats` | 09/11, 16/11 e 23/11 |
| D3 | S1 em 5 reels e 2 carrosséis (car02 novo em sáb 31/10); S2 a S4 em 5 e 2; carrosséis com foto do Bruno na capa | 0 vaga vazia; 0 dia com 2 reels; mediana semanal de alcance de reel | `listPosts`, `ig_posts`, `ig_post_stats` | toda segunda |
| D4 | S1 como está no PostZen (N1); S2 a S4 com 4 a 6 stories por dia e de 15 a 17 à mão por semana; ob01 a ob03 na S2 só se a família da TV passar | views de story em 7 dias com leitura fixa (segunda 19h); respostas por 14 dias | `ig_account_stats` | 09/11 e 16/11 |
| D5 | Régua de 53 de alcance com coluna de minutos do Bruno; exceção escrita da demanda criada na S2 | decisões executadas até a segunda seguinte; mediana da S4 contra a da S1 | arquivos `semanas/` e `ig_post_stats` | 26/10, 02/11, 09/11, 16/11 e 23/11 |
| D6 | 5 automações de conta toda desligadas antes do tl01; TABULEIRO de conta toda a partir de 01/11; linkTracking ligado; `o=` por porta; registro do funil toda segunda | disparos de TABULEIRO de terceiros; cliques no site; diagnósticos (número do Bruno) | `listCommentAutomationLogs`, `ig_account_stats`, Bruno | parcial em 04/11 (brief, fato 181), 09/11, 16/11; diagnóstico em 18/11 |

### P2. Qual régua?

**53 de alcance em 48 h, a mesma de 25/10 a 23/11.** Limites [ESTIMATIVA, fato derivado 2]: 27 (0,5x), 42 (0,8x), 53 (1x), 106 (2x) e 150 (portão da TABULEIRO, CLAUDE.md). Pulo: 60% e 75%.

Por que alcance e não views: alcance conta contas únicas e é a mesma unidade da regra dos 150 do CLAUDE.md; o portão de impulsionar do brief também é em alcance orgânico (300). Misturar com views (normal 57) quebra a comparação. Por que 53 e não 37,5: 53 é a base escrita no 00-SISTEMA, no catálogo e na F7 (fato 24); trocar a base no meio das 4 semanas quebra a comparação entre semanas. Sobre 37,5, os mesmos limites equivalem a 0,72x, 1,12x, 2,83x e 4,0x (fato derivado 2). O Buzzfy não recalcula o 53 hoje: fica fixo como número de régua, não como "normal da conta".

Coluna nova desta cadeira: **minutos do Bruno por peça** (gravação, marcação, sticker, Trial Reel), anotados por ele. Sem esse número, custo por resultado é sem dado.

### P3. Grade de dom 25/10 a dom 22/11, dia a dia e hora a hora

Dias da semana conferidos com o `date` do sistema (fato 2). Feriados: seg 02/11 (Finados), dom 15/11 (Proclamação da República) e sex 20/11 (Consciência Negra) (fato 3). Alcance em feriado: sem dado; a grade não muda nesses dias e a leitura deles sai separada.

Legenda: **PZ** = agendado no PostZen (já está ou o Bruno agenda); **mão** = Bruno posta no app; **ag** = leitura dos agentes. Horário de São Paulo.

#### S1 · dom 25/10 a sáb 31/10 · antes da exibição (5 reels, 2 carrosséis)

| Dia | Feed | Stories PZ (já agendados, N1) | Stories à mão (05-manuais, com as mudanças deste plano) | Leitura e ações com hora |
|---|---|---|---|---|
| dom 25/10 | **18h30 reel tl01** (PZ, fica) | 09h00 bastidor Ser Empreendedor; 09h01 mc02; 17h30 "DOM · 18H30 · NO FEED" | 09h02 enquete; 12h00 compartilhar Dentista B com enquete; 12h30 link do teste; **18h35 compartilhar tl01 com menção à Mirna e teste de marcar a Mirna no reel publicado** | Bruno, até 09h00: desligar ETAPAS de story. Até 18h29: desligar CASE, ESTRATEGISTA, ETAPAS, FUNIL e CAIXA. ag até 09h33: ler a pilha de stories de 24/10 antes de expirar. ag 21h: Dentista B com 24 h |
| seg 26/10 | **21h reel pb01** (PZ, fica) | 12h01 A VIRADA; 17h30 mc03; 17h31 A EQUIPE EXECUTA; 20h30 "SEG · 21H" | 09h00 compartilhar tl01 com enquete; 12h00 enquete; 17h32 link; 21h05 compartilhar pb01 e marcar a Mirna no reel | **ag 21h05: Módulo 7, rodada 1** (Dentista B com 48 h; seguidores de 22 e 23/10; base de story de 7 dias com a hora da leitura) em `semanas/2026-10-26.md` |
| ter 27/10 | **12h carrossel car01** (PZ, fica) | 14h31 NA TV · VAI AO AR SEG, 02/11; 14h32 A VIRADA; 14h33 CONTEI NA TV; 16h00 pf01 (v2) | 09h00 compartilhar pb01 com enquete; 12h05 marcar a Mirna na capa do car01; 14h30 enquete; 16h01 link | **ag 18h35: tl01 com 48 h (portão do tl02).** ag 21h: hot streak de tl01 e pb01 (`ig_reel_checkup`) |
| qua 28/10 | sem feed (o ci01 sai daqui) | 12h01 A VIRADA; 17h30 NA TV · TV CÂMARA; 17h31 NA TV; 17h32 CRITÉRIO; ~~20h30 "QUA · 21H"~~ (Bruno apaga, id m17fs6f2w0yyddqfw8p2vebqbd8gwcne, até 20h29) | 09h00 compartilhar car01; 12h00 enquete; 17h33 link (o 21h05 do ci01 vai para 02/11) | Bruno até 20h59: mover ci01 para 2026-11-03T00:00:00Z. **ag 21h: pb01 com 48 h** (1ª leitura da família da TV; decide TABULEIRO no pb02). **Bruno até 23h59: Bloco 1 de gravação** |
| qui 29/10 | **21h reel po01** (PZ, fica; legenda com um pedido) | 12h01 A VIRADA; 17h30 NA TV · VAI AO AR; 17h31 MÉTODO XEQUE-MATE; 20h30 "QUI · 21H" | ~~09h00 compartilhar ci01~~ (sai, sem substituto); 12h00 enquete; 17h32 link; 21h05 compartilhar po01 e marcar a Mirna | agência até 18h: car02 pronto para aprovação |
| sex 30/10 | **21h reel pb02** (PZ, fica; TABULEIRO no lugar do direct só se o pb01 passar de 150 com pulo abaixo de 60%) | 12h01 A VIRADA; 17h30 ALINHAMENTO; 17h31 DIAGNÓSTICO · 30 MIN; 20h30 "SEX · 21H" | 09h00 compartilhar po01 com enquete; 12h00 enquete; 12h02 link; 21h05 compartilhar pb02 e marcar a Mirna | Bruno até 20h59: agendar car02 para sáb 31/10 12h |
| sáb 31/10 | **12h carrossel car02** (novo); **18h30 reel tl02** (PZ, com portão) | 11h00 NA TV; 12h00 O QUE EU MAIS OUÇO; 12h01 A VIRADA; 12h02 NA TV · TV CÂMARA; 17h30 "SÁB · 18H30" | 09h00 compartilhar pb02 com enquete; 12h03 link; 18h35 compartilhar tl02 e marcar a Mirna; 19h30 enquete | Bruno até 20h: agendar mc04 para dom 01/11 09h00. ag 21h: po01 com 48 h |

Exceção de sequência (hot streak em tl01 ou pb01 na leitura de ter 27/10 21h): o ci01 fica em qua 28/10 21h (sequência em 24 a 48 h, fato 149), o po01 vai para qua 04/11 21h (2026-11-05T00:00:00Z, Bruno até qui 29/10 20h59) e a S1 continua em 5 reels.

#### S2 · dom 01/11 a sáb 07/11 · semana da exibição (5 reels, 2 carrosséis)

Dois caminhos, escolhidos pelo **portão da família da TV** em dom 01/11 21h30 (seção 2, P17). Caminho A: a família passou. Caminho B: não passou.

| Dia | Feed | Stories PZ | Stories à mão | Leitura e ações |
|---|---|---|---|---|
| dom 01/11 | 11h Trial Reel R1 (mão; opcional; não conta nos 5; só com conta elegível); **12h carrossel car03** | 09h00 mc04 (4,6 s); 12h00 objeção; 17h30 "AMANHÃ, SEG 02/11, NA TV CÂMARA CAMPINAS" (sem hora) | 12h02 link; contagem nativa só com a hora confirmada | Bruno até 18h: bio, link `/tabuleiro/?o=ig-bio`, 3 fixados (reel de 02/11 entra no dia; po01; R1) e destaque NA TV. Bruno até 18h: TABULEIRO de conta toda ligada e a do Dentista B desligada. ag 21h: pb02 com 48 h. **ag 21h30: portão da família da TV** |
| **seg 02/11 (Finados, exibição)** | **21h reel do dia:** ci01 (padrão) ou a selfie de 02/11 se gravada e editada até dom 01/11 18h (aí o ci01 vai para qua 04/11) | 09h00 estático "SEG · 02/11 · NA TV CÂMARA CAMPINAS / Ser Empreendedor, com a repórter Mirna Abreu / canal 11.3, NET 4, Vivo Fibra 9 e tvcamaracampinas.com.br" (sem hora, sem "hoje", sem "ao vivo"); 20h30 "SEG · 21H · NO FEED" | assim que a hora for confirmada: story com a hora, menção à Mirna e link para tvcamaracampinas.com.br/ao-vivo; 12h00, se a hora seguir sem dado: story com link para /programacao; depois da hora: selfie "Foi ao ar." (sem a tela da TV) e "Chegou pela TV Câmara? Me manda um oi no direct e conta a sua área."; 12h02 link do teste; 21h05 compartilhar o reel com menção | ag 06h e 11h: grade de 02/11 no site. ag 18h30: tl02 com 48 h. **ag 19h: Módulo 7** (lista do Bruno vence ter 03/11 11h). Nenhuma palavra-chave no dia |
| ter 03/11 | **12h carrossel car04** | 09h00 autoridade; 12h00 objeção; 17h30 frase | 09h00 compartilhar o reel de 02/11 com enquete "Concorda com o que eu disse na TV?"; link da edição quando sair no site ou no YouTube (vai para o destaque NA TV); resultado da votação do tl01; 12h05 compartilhar car04 | Bruno até 11h: executar a lista do Módulo 7 |
| qua 04/11 | **21h reel:** A = ob01; B = R2 como reel normal com 2 mudanças (se a selfie entrou em 02/11, o ci01 ocupa esta vaga) | 09h00; 12h00; 17h30; 20h30 "QUA · 21H" | 12h02 link; 21h05 compartilhar | ag 21h: reel de 02/11 com 48 h. Leitura parcial de diagnóstico do brief (fato 181), com o número do Bruno |
| qui 05/11 | **21h reel:** A = ob03; B = R3 como reel normal com 2 mudanças | 09h00; 17h30; 20h30 "QUI · 21H" | 12h00 objeção com enquete (no lugar do estático); 12h02 link; 21h05 compartilhar | |
| sex 06/11 | **21h reel:** o "mais votado inteiro" se o tl01 somar 5 votos ou mais e o render estiver pronto; senão nicho 1 do Bloco 1; senão ob02 (A) ou Dentista C só se o B tiver passado de 106 com pulo abaixo de 60% (B) | 09h00; 12h00; 17h30; 20h30 "SEX · 21H" | 12h02 link; 21h05 compartilhar | |
| sáb 07/11 | **18h30 reel tl03** (PZ, com portão) | 09h00; 12h00; 17h30; 18h00 "SÁB · 18H30" | 12h02 link; 18h35 compartilhar tl03 e marcar a Mirna (2º convite de colaboração só se ela aceitou o 1º) | |

#### S3 · dom 08/11 a sáb 14/11 (5 reels, 2 carrosséis)

| Dia | Feed | Stories PZ | Stories à mão | Leitura e ações |
|---|---|---|---|---|
| dom 08/11 | 11h Trial Reel R2 (mão; opcional; só se o R2 não foi ao feed na S2); **12h carrossel car05** | 09h00; 12h00; 17h30 | 12h02 link; 12h05 compartilhar car05 | |
| seg 09/11 | **21h reel nicho 1** (Bloco 1) ou, sem gravação, o próximo da ordem fixa (P13) | 09h00; 12h00; 17h30; 20h30 | 12h02 link; 21h05 compartilhar | **ag 19h: Módulo 7** (tl03 com 48h30; seguidores parciais) |
| ter 10/11 | **12h carrossel car06** | 09h00; 12h00; 17h30 | 12h02 link; 12h05 compartilhar | Bruno até 11h: lista do Módulo 7 |
| qua 11/11 | **21h reel nicho 2** | 09h00; 12h00; 17h30; 20h30 | 12h02 link; 21h05 compartilhar | ag: conferência de nicho do brief; com n abaixo de 3 escreve "não testado" e passa para 16/11. Saldo de seguidores até 08/11 fecha aqui |
| qui 12/11 | **21h reel:** REACT (se gravado no Bloco 2) ou ob02 ou corte do banco, se a família da TV estiver em MANTER | 09h00; 17h30; 20h30 | 12h00 caixa de pergunta; 12h02 link; 21h05 compartilhar | |
| sex 13/11 | **21h reel nicho 3** (Bloco 2) | 09h00; 12h00; 17h30; 20h30 | 12h02 link; 21h05 compartilhar | ag: seguidores dos 14 dias depois de 27/10 fecham nesta leitura (fato derivado 5) |
| sáb 14/11 | **18h30 reel tl04** (PZ, com portão; a Mirna viu o "Uau!" recortado antes) | 09h00; 12h00; 17h30; 18h00 | 12h02 link; 18h35 compartilhar | |

#### S4 · dom 15/11 a sáb 21/11 (5 reels, 2 carrosséis) e dom 22/11

| Dia | Feed | Stories PZ | Stories à mão | Leitura e ações |
|---|---|---|---|---|
| dom 15/11 (feriado) | 11h Trial Reel R3 (mão; opcional); **12h carrossel car07** | 09h00; 12h00; 17h30 | 12h02 link; 12h05 compartilhar | |
| seg 16/11 | **21h reel nicho 4** | 09h00; 12h00; 17h30; 20h30 | 12h02 link; 21h05 compartilhar | **ag 19h: Módulo 7** (tl04 com 48h30); conferência de nicho proposta (n de 3 ou mais) |
| ter 17/11 | **12h carrossel car08** | 09h00; 12h00; 17h30 | 12h02 link; 12h05 compartilhar | Bruno até 11h: lista do Módulo 7 |
| qua 18/11 | **21h reel DOBRAR:** sequência do melhor reel da S3 (mesma linha, muda só o assunto) ou nicho 5 | 09h00; 12h00; 17h30; 20h30 | 12h02 link; 21h05 compartilhar | conferências do brief de 21/10: seguidores, diagnóstico e fim do "só orgânico" (fato 169) |
| qui 19/11 | **21h reel:** nicho 5 ou corte do banco | 09h00; 17h30; 20h30 | 12h00 objeção com enquete; 12h02 link; 21h05 compartilhar | 1º dia em que o Bruno pode impulsionar, com o portão triplo (seção 3) |
| sex 20/11 (feriado) | **21h reel:** nicho 6 ou remake | 09h00; 12h00; 17h30; 20h30 | 12h02 link; 21h05 compartilhar | |
| sáb 21/11 | **18h30 reel tl05** (PZ, com portão; a Mirna viu o carimbo "AINDA?" antes) | 09h00; 12h00; 17h30; 18h00 | 12h02 link; 18h35 compartilhar | |
| dom 22/11 | **12h carrossel car09** (abre a S5) | 09h00; 12h00; 17h30 | 12h02 link; 12h05 compartilhar | seg 23/11 19h: Módulo 7 decide a S5 |

**Molde dos stories de S2 a S4** (D4): 09h00 PZ autoridade ou bastidor com foto do Bruno; 12h00 PZ objeção; 12h02 mão, link do teste com o estático 2510-1230 (o único pedido do dia); 17h30 PZ frase de efeito; 20h30 PZ chamada nos dias de reel das 21h (18h00 no sábado); 21h05 mão, compartilhar o reel (18h35 no sábado); 12h05 mão nos dias de carrossel. Enquete à mão 2 vezes por semana (no lugar do estático das 12h00) e caixa de pergunta 1 vez. De 15 a 17 stories à mão por semana [ESTIMATIVA: 7 links + 5 compartilhamentos de reel + 2 de carrossel + 2 enquetes + 1 caixa = 17; 15 nas semanas em que a enquete ocupa o horário do link], contra 27 na S1 (N7).

Contagem por semana, conferida dia a dia na tabela: S1 5 reels (tl01, pb01, po01, pb02, tl02) e 2 carrosséis; S2 5 e 2; S3 5 e 2; S4 5 e 2. Nenhum dia com 2 reels. Nenhum dia com mais de 2 posts de feed (o máximo é sáb 31/10 com car02 e tl02, e dom 01/11, 08/11 e 15/11 com Trial Reel e carrossel, se o Trial Reel for contado como feed). Menor distância entre reels: 21h30 (sex 21h para sáb 18h30), acima de 6 h [FATO, regra de 0,92x, fato 152]; Trial Reel às 11h de domingo fica 16h30 depois do reel de sábado.

### P4. Antes, no dia e depois de 02/11

**Antes (25/10 a 01/11):** aquecimento e bastidor com a data no texto, sem pedir que ninguém assista. Feed: tl01, pb01, car01, po01, pb02, car02 (objeção, fora da TV) e tl02. Stories: os 28 já agendados (N1), que levam "NA TV · VAI AO AR SEG, 02/11" em 27/10 e 29/10, mais mc02, mc03 e mc04. **Contagem:** é o rótulo com a data nos estáticos de TV, já agendados (N1), mais a véspera "AMANHÃ, SEG 02/11" em dom 01/11 17h30. A contagem com sticker nativo só entra se a hora chegar até dom 25/10 (F6), porque o lembrete do sticker precisa de hora [FATO nível 3, fato 69].

**No dia (seg 02/11):** uma chamada agendada às 09h00 sem hora; a chamada com a hora só à mão, depois de confirmada pela Mirna ou pela grade; se às 12h a hora seguir sem dado, story com link para a programação do site, sem prometer horário. "Foi ao ar" só depois do horário confirmado. Um reel só, às 21h. O dia é de captura: o pedido do dia é "me manda um oi no direct", porque é a única forma de atribuir lead à TV com as ferramentas de hoje [FATO, F8: `o=` não chega ao WhatsApp e o PostZen não conta clique].

**Depois (03/11 a 21/11):** link da edição em story e no destaque NA TV quando sair; resultado da votação do tl01; ob01 e ob03 (ou remakes, se a família da TV cair no portão); "mais votado inteiro" se houver 5 votos; tl03 a tl05 com portão; REACT se gravado; nicho a partir de seg 09/11.

### P5. pb01, car01, ci01, po01 e pb02, um por um

| Peça | Decisão | Motivo | Até quando o Bruno mexe no PostZen |
|---|---|---|---|
| pb01 (seg 26/10 21h) | **Fica** | Trajetória (DJ por 20 anos): apresenta o Bruno sem entregar caso nem método. É a 1ª leitura barata da família da TV (Bruno à mesa, de perfil em 3/4, fato 88), formato nunca medido nesta conta. Informação cedo vale mais que guardar a peça | legenda com o @ da Mirna, se houver, até seg 26/10 20h59 (id m17dqk63b0e1hk75xcevdwmc458gwmfn) |
| car01 (ter 27/10 12h) | **Fica** | Único carrossel pronto; capa com o Bruno e a Mirna (feed com foto do Bruno na capa teve mediana de 111 de alcance, fato 51). Ajuste: um pedido só, o direct ("Me manda a data no direct"), tirando "Comenta o número" | legenda até ter 27/10 11h59 (m174q9y41reqfn4eqhqrm124f58gwzbr) |
| ci01 (qua 28/10 21h) | **Move para seg 02/11 21h** | (1) Tira a S1 de 6 para 5 reels sem apagar nada. (2) Põe oferta na semana vazia em que a demanda é maior. (3) A frase do ci01 já foi anunciada com "NA TV · SEGUNDA, 02/11" (fato 30 do enquadramento). (4) É a peça com mais Mirna (voz e 10,7 s de rosto, fato 90): candidata ao convite de colaboração no dia em que o trabalho dela vai ao ar. (5) Risco que eu aceito por escrito: o ci01 abre com o Bruno de costas, sem o rosto, até 2,5 s (fato 88) | mover até qua 28/10 20h59 para 2026-11-03T00:00:00Z (m177cf21jjcv7fa2y1q1twc4n58gwe0n); apagar a chamada das 20h30 de 28/10; legenda versão A (com "Segue o perfil") agendada e versão B só depois da hora confirmada |
| po01 (qui 29/10 21h) | **Fica, e é fixado de dom 01/11 a dom 08/11** | (1) É a peça mais perto do diagnóstico (o Método Xeque-Mate tem o mesmo mapa dos 5 Lances do Tabuleiro, fato 129). Sair antes dá 4 dias a mais de captura. (2) Quem chega pela TV vê o topo da grade: fixar resolve "estar no topo" sem mover a data. (3) A leitura de 48 h (sáb 31/10 21h) entra no portão da família da TV antes da S2. (4) A promessa do tl01 é soltar "inteiro" o mais votado; o po01 tem 23,52 s e não é a versão inteira (fato 87), então não a quebra. Ajuste: um pedido só, "Qual dessas peças falta no seu lançamento? Comenta o nome dela que eu te respondo.", sem "Salva" | legenda até qui 29/10 20h59 (m17ersdnwmmsk5e7fyw4jqwfdx8gwcxt); fixar no app em dom 01/11 |
| pb02 (sex 30/10 21h) | **Fica** | Fecha a dupla PB com n de 2 antes do Módulo 7 de 02/11 (muda só o assunto em relação ao pb01). Pedido de direct funciona antes ou depois. TABULEIRO no lugar do direct só se o pb01 passar de 150 em 48 h com pulo abaixo de 60% (leitura de qua 28/10 21h) | legenda até sex 30/10 20h59 (m1718n57yvmtpyb4xnf3zsw7fn8gwe7q) |

### P6. A promessa do tl01

[FATO, `listPosts` 15h46 e 17h24, fato 77] A legenda do tl01 já não promete "o próximo sábado". Ela diz: "O mais votado eu solto inteiro depois que a entrevista for ao ar." Então a promessa não empurra a S1 para 6 reels: a S1 fica em 5 com o ci01 movido.

Como cumprir: o Bruno conta os votos à mão até seg 02/11 12h (nenhuma ferramenta permitida lê o texto dos comentários, fato 143). Com 5 votos ou mais, a agência monta a versão longa do assunto mais votado a partir da gravação do celular (nunca da edição exibida, fato 137), com até 90 s [HIPÓTESE: a duração de 6 s a 2 min fica perto do normal, fato 153], para sex 06/11 21h. Com menos de 5 votos (regra do catálogo, fato 170), story de ter 03/11 diz o resultado sem fingir votação e cumpre o "inteiro" com o link da edição exibida, que é a entrevista inteira.

### P7. Ordem de tl02 a tl05, portão e destino de quem sai

Ordem: a que já está no PostZen [FATO, N2]: tl02 sáb 31/10, tl03 sáb 07/11, tl04 sáb 14/11, tl05 sáb 21/11, às 18h30. Trocar a ordem tem custo e nenhum dado a favor.

| Leitura | Data e hora reais | Regra |
|---|---|---|
| tl01 com 48 h | ter 27/10 18h30 (lida às 18h35) | tl02 fica se o tl01 tiver 27 ou mais de alcance e não cair nos dois critérios ruins juntos (abaixo de 42 **e** pulo acima de 75%, regra do catálogo, fato 170). Sai se ficar abaixo de 27 ou nos dois critérios ruins |
| tl02 com 48 h | seg 02/11 18h30 | com n de 2 (tl01 e tl02): PARAR a família de timelapse se a mediana ficar abaixo de 42 ou o pulo mediano acima de 75%. tl03 a tl05 saem do feed |
| tl03 com 48h30 | seg 09/11 19h | MANTER ou PARAR com n de 3 |
| tl04 com 48h30 | seg 16/11 19h | idem; decide o tl05 |

Timelapse que sai do feed vira stories em trechos de 15 s às 09h00 e banco; o sábado 18h30 recebe a próxima peça com o Bruno de frente da ordem fixa (P13). O tl02 tem 10,4 s sem voz real, acima do teto de 8 s do catálogo (fato 92): se a agência não refizer o trecho até sex 30/10, o Bruno aceita o risco por escrito no arquivo da semana.

### P8. mc02 a mc04

mc02 dom 25/10 09h01 e mc03 seg 26/10 17h30 já estão agendados [FATO, N1]. mc04 em **dom 01/11 09h00**, véspera, depois do tl02, como manda a regra do laço (fato 87 do enquadramento). **Ponto de recorte: 1705,567 s** (render atual de 4,6 s, N6), que fica dentro da faixa de 1705,2 a 1705,7 s e termina em "família.", sem "eu construí tudo através da profissão que hoje eu executo como estrategista digital". Motivo: o render existe (custo zero), a frase fecha sentido sozinha e o termo "estrategista digital" foi tirado da bio pelo Módulo 1 (fato 96). O recorte de 1707,82 s exigiria render novo e termina no meio da ideia.

### P9. Marcação da Mirna

| Peça | Como | Quem e quando | Se o app não deixar marcar depois |
|---|---|---|---|
| Reels e carrosséis agendados com imagem ou voz dela (tl01, pb01, car01, po01, pb02, tl02, ci01, tl03, tl04, tl05, ob01 a ob03 se ela aparecer no quadro) | @ no texto da legenda (se o Bruno tiver o @ antes) e marcação na mídia pelo app depois de publicar | Bruno, até 15 min depois de cada publicação; 1 a 2 min por peça [PRIOR, fato 4.1 n. 5]; anota "marcada: sim ou não" no arquivo da semana | @ no texto da legenda pelo PostZen antes de publicar, para as peças seguintes; o reel de 02/11 sai à mão pelo app, com marcação ou convite de colaboração |
| Stories com trecho dela | sticker de menção, só em story à mão | Bruno, 3 vezes: dom 25/10 18h35, a chamada com a hora em 02/11 e o compartilhamento das 21h05 de 02/11 | não muda (story agendado nunca leva sticker, fato 66) |
| Convite de colaboração | campo de colaboradores no PostZen ou no app | só no reel de 02/11 (ci01), com o @ e o ok dela antes; o 2º no tl03 só se ela aceitou o 1º | se a API recusar, o Bruno publica o reel de 02/11 à mão |
| tl04 e tl05 | marcar só depois de ela ver o recorte do "Uau!" e o carimbo "AINDA?" | Bruno manda as peças a ela até sex 13/11 e sex 20/11 | se ela não aprovar, a peça sai sem marcação ou vai para o banco |

Teste que decide o caminho: dom 25/10 18h35, no tl01 publicado (fato a buscar 5). O efeito da marcação no alcance não se separa por post (fato 4.2 n. 58): medida por semana no alcance de não seguidores (base 362 em 7 dias, N4).

### P10. Copy depois de 02/11

Muda: "Foi ao ar" passa a valer, só depois do horário confirmado; o link da edição no site ou no YouTube da emissora entra em story, no destaque NA TV e na legenda, com a TV Câmara como fonte (termos, fato 137); minutos da edição só depois de conferidos na edição exibida (os minutos do car01 e do tl01 contam da gravação do celular, fato 81). Continua vetado: "ao vivo", "rede nacional", "a TV Câmara recomenda", "fui convidado pela TV", "entrevista exclusiva", "A TV me chamou de história de sucesso" (fato 6); logo da emissora; filmar ou recortar a exibição; republicar a edição inteira; **qualquer uso pago de peça da TV** (uso comercial vetado pelos termos e liberação da Mirna só verbal, fatos 4 e 137).

### P11. 5 reels e 2 carrosséis por semana; quem produz os carrosséis

Sim nas 4 semanas (tabela da P3). A S1 precisa de 1 carrossel novo (car02, sáb 31/10); S2 a S4 precisam de 6; dom 22/11 abre a S5 com o car09. Total: 8 carrosséis novos. **Quem produz:** a agência, sem gravação, com foto de marca do Bruno na capa (7 fotos disponíveis, fato 113); o car01 levou cerca de 36 min de calendário de agência (fato 112) [ESTIMATIVA: 8 x 36 min = 4 h 48 min]. **Prazo:** pronto para aprovação até a sexta 18h da semana anterior (car02 até qui 29/10 18h). **Quem agenda:** o Bruno. **Linha:** car02 objeção "não tenho tempo"; car03 os 5 Lances do Tabuleiro; car04 "o que a TV perguntou e o que eu respondi" (único da TV, depois de 02/11); car05 a car09 objeções, critério e método, alternando. Regra desta cadeira: carrossel sem imagem nem frase da TV fica elegível a impulsionar depois de 18/11.

### P12. Bruno em cena nos 3 primeiros segundos

| Peça | Situação | Fonte |
|---|---|---|
| tl01, tl02, tl03 | sim, aos 0,6 e 2,5 s | fato 89 |
| tl04, tl05 | sem dado: agência confere quadros 0, 0,6, 1,5 e 2,5 s até sex 13/11 | lacuna |
| pb01, po01, pb02, pf01 | sim desde o quadro 0, de perfil em 3/4, sem olhar para a câmera | fato 88 |
| ci01 | de costas, sem o rosto, até 2,5 s: cumpre só a letra da regra | fato 88 |
| ob01 a ob03 | de perfil atrás do monitor nos quadros 0 e 2,5 s: cumpre a letra | fato 97 |
| Dentista B | tela cheia até 3,18 s | fato 89 |
| Dentista C | selfie com "Dentistas," no quadro 0 | fato 101 |
| R1 a R3 | talking head em selfie; quadro 0 do remake a conferir | fato 35 |
| Cortes novos, nicho, selfie de 02/11, REACT | regra escrita na ficha: Bruno de frente no quadro 0 | CLAUDE.md |

Leitura de performance: a regra está cumprida na letra, mas o formato medido (5,2x) é o Bruno **falando de frente** (fato 25). Nenhuma peça da TV mede isso; é exatamente o que o portão da família da TV testa.

### P13. Mínimo de gravação por semana e semana sem gravação

**Mínimo:** 1 bloco por semana, entregue até quarta 23h59, com 2 roteiros e 2 tomadas do gancho, de 24 a 36 min [ESTIMATIVA, F5: 12 a 18 min por roteiro]. **Piso numa semana apertada:** 1 roteiro, de 12 a 18 min. **Bloco 1, até qua 28/10 23h59:** (1) selfie de 02/11 com a data falada e sem hora, 2 tomadas [PRIOR: de 5 a 8 min]; (2) nutricionista versão A; (3) consórcio sem a linha da ABAC. Total de 29 a 44 min [ESTIMATIVA]. **Bloco 2, até qua 04/11:** psicólogo e advogado (só se o provimento da OAB estiver lido) e a selfie do REACT depois da exibição (20 min pela estimativa do catálogo, fato 106). **Blocos 3 e 4:** até qua 11/11 e qua 18/11, definidos pelo Módulo 7 da segunda anterior. Data da próxima sessão marcada: sem dado (fato a buscar 20).

**Semana com zero gravação, ordem fixa:** (1) família da TV pronta (ob01, ob03, ob02 por último, porque repete 82% do áudio do pf01, fato 95), só se o portão estiver em MANTER; (2) o "mais votado inteiro" com 5 votos; (3) R2 e R3 como reel normal com 2 mudanças reais (únicas peças prontas com o Bruno de frente); (4) cortes do banco (pb03, CINEMA 02, MITO e outros, fato 107), com ficha; (5) Dentista C só se o B passar de 106 com pulo abaixo de 60%. Nunca voz sintética (fato 27). Se nada disso passar, a semana fica com 4 reels e a vaga vazia é registrada como "não executado", nunca preenchida com animação.

### P14. Dentista C e remakes

**Dentista C:** fica fora do feed e fora do anúncio até duas condições: o Dentista B passar de 106 com pulo abaixo de 60% em 48 h (seg 26/10 21h05) e o Bruno decidir por escrito como fica o portão de impulsionar para peça nunca publicada. Motivo de performance: o brief de 21/10 guarda o C como amostra e anúncio 4:5 depois de 18/11 (fato 101), mas o portão de impulsionar do mesmo brief pede 300 de alcance orgânico (fato 169), que um criativo nunca publicado não tem. Antes de anúncio: Res. CFO 196/2019 conferida (sem dado). Com o B acima de 106, o C pode ir ao feed na S2 (sex 06/11, caminho B) como sequência de formato.

**Remakes:** R1 "Ele nunca fez um anúncio" (10,14x), R2 "90%" (4,42x) e R3 "Problema de equipe" (3,61x), em 720p (fato 37). Saem sem gravar: R1 como Trial Reel em dom 01/11 11h; R2 e R3 como Trial Reel em dom 08/11 e dom 15/11, ou como reel normal na S2 se a família da TV cair no portão. Quem posta: o Bruno, no app (elegibilidade pela API: sem dado, fato 139). Chance de um repost bater o alcance usual: 35% com original de 5x ou mais e 15% de 2 a 5x, entre contas [FATO nível 2, fato 150]. Cada remake leva 2 mudanças reais (abrir no ápice, legenda queimada nova, capa com o rosto). A legenda do R1 promete uma saga que acabou (fato 37): legenda nova.

### P15. Stories por dia

S1: os 28 agendados (N1) e os 27 à mão de 05-manuais (N7), com 2 itens a menos (qua 28/10 21h05 e qui 29/10 09h00, que eram do ci01) e a chamada de qua 28/10 20h30 apagada. Cerca de 8 por dia, como já está [FATO].

S2 a S4: de 4 a 6 por dia, no molde da P3. Agendados no PostZen: autoridade às 09h00, objeção às 12h00, frase às 17h30, chamada às 20h30. À mão: link do teste às 12h02, compartilhar reel às 21h05 e carrossel às 12h05, 2 enquetes e 1 caixa por semana. De onde vem cada frase: provas e objeções do `02-provas.md` e do `04-estaticos.json` (39 estáticos renderizados, commit 2b3a7d8); frases de efeito livres 3 e 4 (fato 62) e o banco de 14 frases com fonte da F6; frase repetida só depois de 14 dias [PRIOR]. Pedido único do dia: o link do teste. Agência entrega os estáticos da semana até a sexta 18h anterior; o Bruno agenda.

### P16. ob01 a ob03

Render pronto (N5). Pendente: a folha de 4 quadros por segundo com nota por efeito (regra do CLAUDE.md) e a voz do ob01 conferida (a ficha registra que quem fala é o Bruno, fato 98; o 03-plano marcava a faixa da Mirna). **Prazo:** folha e conferência de voz até sex 30/10 18h. **Onde entram:** caminho A da S2, ob01 qua 04/11 21h e ob03 qui 05/11 21h; ob02 por último (S3, qui 12/11), porque repete 82% do áudio do pf01. Pedido: "Comenta a sua área que eu te respondo." com resposta à mão (as 5 automações de conta toda já desligadas; a tela do ob02 traz "ESTRATEGISTA", fato 8 da F8). **Substituto** se não passarem na folha ou se a família da TV cair: R2 e R3 como reel normal; os ob vão para stories de 15 s.

### P17. PARAR, MANTER, DOBRAR e TESTAR

Régua da P2, alcance em 48 h, por formato:

| Decisão | Regra | n mínimo |
|---|---|---|
| PARAR | mediana abaixo de 42 ou pulo mediano acima de 75% | 2 posts do formato (nunca com n de 1) |
| MANTER | mediana de 42 a 105 | 2 |
| DOBRAR | 106 ou mais com pulo abaixo de 60% | 1 para abrir sequência; 2 para ganhar vaga fixa |
| TESTAR | formato novo ou exceção escrita, no máximo 1 por semana, com motivo no arquivo | 1 |
| Carrossel | DOBRAR pede também 2 ou mais visitas ao perfil | 2 |
| Story | views de 7 dias na leitura fixa de segunda 19h contra a leitura de 26/10 21h05; 3 respostas por semana | semana |

**Portão da família da TV** (pb01, po01, pb02, todos à mesa em 3/4): dom 01/11 21h30, com pb01 e po01 em 48 h e pb02 em 48 h às 21h. Mediana de 42 ou mais com pulo até 75%: caminho A da S2. Abaixo disso, caminho B. Exceção da demanda criada (meu ponto cego): o ci01 de 02/11 fica no caminho B como TESTAR escrito, porque é a peça do dia da exibição e da colaboração.

**Coluna de custo:** cada peça no arquivo da semana leva "minutos do Bruno". Leitura: alcance por minuto do Bruno. [ESTIMATIVA] Um corte da TV com 42 de alcance e 2 min de marcação dá 21 por minuto; um roteiro de nicho com 167,5 (mediana do formato, fato 25) e 18 min de gravação dá 9,3 por minuto, mas é o único formato que gerou comentário e salvamento (fato 26). Por isso o plano não troca um pelo outro: usa os dois.

**Segundas:** 26/10 21h05 (rodada curta: Dentista B e base); 02/11 19h; 09/11 19h; 16/11 19h; 23/11 19h (decide a S5). **Rodada de 02/11 (feriado e exibição):** os agentes leem e escrevem às 19h; os stories da exibição têm prioridade para o Bruno no dia; a lista dele vence ter 03/11 11h; no arquivo, a linha "feriado e exibição" separa o que é efeito do dia.

### P18. TABULEIRO

- **Automações:** o Bruno desliga CASE, ESTRATEGISTA, ETAPAS, FUNIL e CAIXA de comentário antes do tl01 (dom 25/10 18h29) e a ETAPAS de story antes de dom 25/10 09h00. Motivo: a série usa "caso" e "estrategista", e cada comentário aceita uma resposta privada só, uma vez (fatos 114 e 120). As 10 ligadas a posts antigos podem ficar (0 comentário nesses posts, F8).
- **Novembro:** uma automação TABULEIRO de conta toda, criada pelo Bruno até dom 01/11 18h, com o texto genérico da F8 (seção 8), botão para `/tabuleiro/?o=ig-tab` e **linkTracking ligado**; a do Dentista B é desligada no mesmo minuto (duas automações com a mesma palavra: qual responde é sem dado, fato a buscar 32).
- **Em qual post:** só no post seguinte da mesma linha de um reel que passou de 150 de alcance em 48 h, com pulo abaixo de 60% [HIPÓTESE do reforço, n de 1 de cada lado, fato 122]; no máximo 1 por semana; nunca em 02/11; nunca em story. Candidatos com data: pb02 (se pb01 passar, leitura qua 28/10 21h); tl03 (se tl02 passar, seg 02/11 18h30); próximo nicho (se o nicho anterior passar); tl04 e tl05 (leituras de 09/11 e 16/11). Se nenhum passar, novembro fica sem post com a palavra: a regra é teto, não meta.
- **Pedidos de direct das legendas:** um pedido por legenda; post com TABULEIRO não pede direct, número nem salvar.
- **Contagem de cada etapa** (toda segunda, no arquivo da semana): (1) alcance e pulo do post anterior da linha, agente; (2) comentários do post, agente; (3) disparos da TABULEIRO por diferença de total entre segundas, tirando perfis do Bruno, agente; (4) visitas ao perfil e cliques no site, agente; (5) cliques no botão do direct com o linkTracking, agente se o PostZen mostrar [HIPÓTESE]; (6) `tabuleiro_start`, `tabuleiro_complete` e `generate_lead` no GA4, Bruno; (7) mensagens no WhatsApp que começam com "Fiz O Tabuleiro" e com "Quero agendar o Primeiro Lance", Bruno; (8) directs que citam a TV de 02 a 08/11, Bruno; (9) diagnósticos de 30 min agendados; (10) realizados; (11) propostas e vendas, Bruno. Sem o número do Bruno: "sem dado".

### P19. O que muda em cada post contra o anterior da mesma linha

| Linha | Sequência | O que muda |
|---|---|---|
| P&B da TV | pb01 trajetória, pb02 caso do restaurante | assunto |
| Timelapse | tl01 bastidor, tl02 empreender e família, tl03 a pergunta da TV, tl04 de trás para frente, tl05 a régua do tempo | assunto (o recurso de montagem do tl04 e do tl05 varia dentro do mesmo formato) |
| Cinema e pontos | ci01 e po01 são peças únicas; tl05 repete o assunto do ci01 em outro formato | formato |
| Objeção | ob01 tempo, ob03, ob02 | assunto (a objeção) |
| Nicho falado | Dentista A, B (tela dividida), C (prédio de palavras), depois nutricionista, consórcio, psicólogo, advogado | A para B para C: formato; nicho novo: assunto, com o formato de selfie do A |
| Carrossel | car01 frases da TV, car02 objeção, car03 os 5 Lances, car04 a pergunta da TV | assunto; capa com foto do Bruno fixa |
| Remake | R contra o original | 2 mudanças reais por regra de segunda vida (fato 150), exceção escrita à regra de uma mudança |

### P20. Regras de texto

Conferido neste plano: sem travessão, sem emoji, sem promessa de resultado, sem os nomes vetados, nenhuma frase "não é X, é Y" nas legendas propostas, nada da lista vetada do `02-provas.md` (fato 6), nenhum logo de terceiro (TV, BNI). Números de caso só como fato do caso, com a frase de que o número não se repete igual em outro negócio. A bio proposta tira o "Case: de 6 para 20 mi/mês" enquanto a autorização da Tzur é sem dado (fato 102). Cada legenda nova passa pela agência com essa lista antes de o Bruno agendar.

### P21. O que depende só do Bruno, com prazo

| Até | Ação | Onde |
|---|---|---|
| hoje 20h59 | `&p=dentista` no botão da TABULEIRO do Dentista B (F8) | PostZen |
| dom 25/10 09h00 | desligar a ETAPAS de story | PostZen |
| dom 25/10 18h29 | desligar CASE, ESTRATEGISTA, ETAPAS, FUNIL e CAIXA | PostZen |
| dom 25/10 18h30 | falar com a Mirna: print da liberação, @, horário de 02/11, ok para publicar antes de 02/11, convite de colaboração no reel de 02/11 | conversa |
| dom 25/10 18h35 | compartilhar o tl01 com menção e testar marcar pessoa no reel publicado; anotar o resultado | app |
| seg 26/10 | dizer se bruno26111982 é perfil dele; informar a campanha dos 1.907 de alcance pago (datas, custo, objetivo) | arquivo da semana |
| seg 26/10 20h59 a sex 30/10 20h59 | legendas de pb01, car01, po01 e pb02 (P5) | PostZen |
| qua 28/10 20h29 | apagar a chamada de qua 28/10 20h30 | PostZen |
| qua 28/10 20h59 | mover o ci01 para 2026-11-03T00:00:00Z | PostZen |
| qua 28/10 23h59 | Bloco 1 de gravação (selfie de 02/11 primeiro) | celular, enviado como documento |
| sex 30/10 | disponibilidade no feriado de 02/11; cópia de tl02 a tl05, mc02 a mc04, ob01 a ob03 e fonte da entrevista no Drive | Drive |
| sáb 31/10 20h | agendar mc04 e car02 | PostZen |
| dom 01/11 18h | bio e link novos; 3 fixados; destaque NA TV; TABULEIRO de conta toda com linkTracking; desligar a do Dentista B | app e PostZen |
| seg 02/11 | stories da exibição; versão B da legenda do ci01 só depois da hora; convite de colaboração se combinado | app e PostZen |
| ter 03/11 11h e toda terça 11h | executar a lista do Módulo 7 e marcar "executado: sim ou não" | PostZen e app |
| toda segunda 19h | GA4 (3 eventos), mensagens de WhatsApp, directs que citam a TV, diagnósticos agendados e realizados, minutos gastos | arquivo da semana |
| depois de cada publicação com ela | marcar a Mirna e anotar | app |
| até 18/11 | teto de verba escrito, se quiser impulsionar de 19/11 em diante | arquivo da semana |

### P22. Etiquetas

Cada número deste plano leva [FATO] com fonte ou o número do fato no livro, [ESTIMATIVA] com a conta, [HIPÓTESE] ou [PRIOR]. O que falta está escrito "sem dado": volume de busca, horário da exibição, @ da Mirna, audiência da TV, alcance em feriado, votos do tl01, GA4, WhatsApp, diagnósticos, custo e origem do alcance pago de outubro, elegibilidade de Trial Reel, quadros de tl04 e tl05.

---

## 3. Mídia paga: o que esta cadeira prepara sem gastar

### 3.1 Regras que já existem

- [FATO, brief de 21/10, fato 169] Só orgânico até 18/11. Depois, impulsionar só com teto escrito, reel com 300 ou mais de alcance orgânico e pulo abaixo de 55%, os três juntos. O reel de consórcio nunca é impulsionado.
- [FATO, termos da TV Câmara de 24/05/2026, fato 137] Uso comercial do conteúdo da emissora é vetado. A liberação da Mirna é verbal e fala do uso nas redes do Bruno (fato 4). **Nenhuma peça com imagem ou voz da entrevista vai para anúncio** sem autorização escrita que cubra anúncio. Se a gravação de bastidor no celular do Bruno conta como conteúdo da emissora: sem dado (não é parecer jurídico).

### 3.2 Criativos elegíveis hoje

| Criativo | Alcance orgânico | Pulo | Passa no portão de 300 e 55%? | Observação |
|---|---|---|---|---|
| R1 "Ele nunca fez um anúncio" (03/10) | 308 | 53,2% | **sim** | legenda promete saga encerrada (fato 37): trocar a legenda antes |
| R2 "90%" (04/10) | 166 | 45,7% | não (alcance) | |
| R3 "Problema de equipe" (05/10) | 128 | 49,6% | não | |
| Dentista A (21/10) | 169 | 46,6% | não | |
| Dentista C | nunca publicado | sem dado | não pela letra do brief | Res. CFO 196/2019: sem dado |
| Qualquer peça da TV | | | **nunca** | termos da emissora |
| Reels de nicho gravados, remakes, carrosséis sem TV | sem dado | sem dado | entram se passarem até 18/11 | |

### 3.3 Antes de gastar (S1 a S4, custo zero)

1. O Bruno informa de onde vieram os 1.907 de alcance pago dos 30 dias (fato 10): campanha, datas, custo e objetivo. Sem isso, custo por resultado anterior é sem dado.
2. **Armadilha da janela:** os 7 dias até 24/10 tiveram 0 de anúncio (N4). [ESTIMATIVA] Até meados de novembro, cerca de 1.900 contas pagas saem da janela de 30 dias, e o alcance de 30 dias vai cair sem que nada tenha piorado. O Módulo 7 compara só orgânico e só janelas de 7 dias com hora fixa.
3. `o=` diferente por porta (ig-bio, ig-stories, ig-tab, ig-manual) e pedido ao desenvolvedor do site para que o `o=` entre na mensagem do WhatsApp do Tabuleiro (fato 129: hoje não entra).
4. linkTracking ligado na TABULEIRO nova.
5. Registro semanal do funil (P18) desde 26/10: sem base de conversão orgânica, o primeiro impulsionamento não tem com o que ser comparado.

### 3.4 Primeiro impulsionamento, se o Bruno quiser (19/11 em diante)

- Criativo: o reel que passar no portão de 300 e 55% até 18/11 com o melhor pulo; hoje só o R1 passa.
- Objetivo: visitas ao perfil ou mensagens [PRIOR sobre os objetivos disponíveis], nunca alcance.
- Público: região de Campinas, de 35 a 54 anos [FATO, fato 19: Campinas e vizinhas somam 69,9% dos engajados; 35 a 54 anos são 65,7% dos engajados].
- Ferramenta: Gerenciador de Anúncios com o post existente, para manter os números do orgânico e controlar posicionamento [PRIOR].
- Valor e duração: o teto escrito do Bruno (sem dado). O 00-SISTEMA cita R$ 20 a R$ 30 por dia para o case Tzur [FATO, 00-SISTEMA, linha 419], que depende de autorização sem dado.
- Leitura: custo por visita ao perfil e directs recebidos, contra a taxa orgânica de 13,4 visitas por 100 contas alcançadas [ESTIMATIVA: 77 / 576, N4]. O primeiro é compra de medida: nada de estender sem leitura do Módulo 7.

### 3.5 Google

Sem campanha de busca nas 4 semanas (seção 1.2). Única ação: o Bruno olha o Search Console, se o site estiver verificado, de 02 a 08/11.

---

## 4. Decisões

### D1. Série da entrevista em torno de 02/11

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) Manter os 5 cortes de 26 a 30/10 | S1 fica com 6 reels; nada a mexer no PostZen | S2 vazia na semana de maior demanda; quem chega pela TV encontra o feed parado desde sábado |
| (b) Mover os 5 para 03/11 a 13/11 | S2 e S3 cheias de TV | S1 fica sem reel nos dias úteis; zero leitura da família da TV antes da exibição; 5 peças do mesmo material em sequência |
| (c) Dividir: ci01 para 02/11, o resto fica, po01 fixado; S2 por portão (minha posição) | S1 em 5; S2 com reel no dia; leitura de n de 3 antes da S2 | o portão decide se a S2 aposta na TV ou no Bruno de frente; custo de reverter baixo |
| (d) Não mexer e decidir em 26/10 | adia | o ci01 continuaria em 28/10 sem decisão; perde a janela de mover |
| (e) Fora do óbvio: perfil como página de destino primeiro (bio, link, fixados, destaque, story de captura "Chegou pela TV?") e ordem dos cortes em segundo plano | a etapa medida (1,57% de clique) recebe a única mudança que mexe nela | se a TV trouxer visitas, a captura já está pronta; se não trouxer, o custo foi 15 min do Bruno (estimativa do 00-SISTEMA) |

**Premissas:** (1) a família da TV, à mesa e de perfil, segura 42 de alcance [HIPÓTESE, sem medida]; (2) quem viu a TV procura o perfil [HIPÓTESE 45]; (3) o Bruno executa a mudança do ci01 até qua 28/10 20h59; (4) a Mirna não se opõe a ver a voz dela num reel de 02/11.

**Posição:** (c) com (e) junto.

**Probabilidade de sucesso pelo critério do enquadramento** (média de 42 ou mais com pulo até 75% em cada fase, 21 ou mais visitas por dia de 02 a 04/11, saldo positivo de 25/10 a 08/11): **0,18**, faixa [0,08; 0,32], confiança 0,40. A parte mais fraca é a de 21 visitas por dia (base 11,0, N4); a mais forte é o saldo positivo de seguidores [HIPÓTESE: 10 reels com o Bruno em cena contra semanas de -2 e 0].

### D2. Gravação, mínimo semanal e estoque sem gravação

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 1 bloco por semana, 2 roteiros, 24 a 36 min; o 1º com a selfie de 02/11 (minha posição) | 2 reels de nicho por semana a partir da S3 e 1 na S2 | o formato medido (5,2x) volta ao feed; cada reel de nicho vira candidato a impulsionar depois de 18/11 |
| (b) 1 sessão de 60 a 90 min com 5 roteiros | mais estoque | carga do Bruno; o plano de 21/10 já pedia isso e não saiu (fato 105) |
| (c) Sessão quinzenal com 10 roteiros | estoque grande de uma vez | 1 falha derruba 2 semanas |
| (d) Zero gravação | grade só com TV, ob, remakes e C | se a família da TV falhar, a conta fica sem o formato que funciona |
| (e) Fora do óbvio: gravar ganchos, não roteiros. 6 tomadas de abertura de 2 roteiros, cada uma testada como Trial Reel, como se testa criativo de anúncio | descobre o gancho que segura antes de gastar roteiro inteiro | depende de Trial Reel elegível (sem dado); poucos dados por teste |

**Premissas:** (1) o Bruno grava ao menos 2 dos 4 blocos [PRIOR: nenhuma gravação desde 21/10, fato 104]; (2) o formato de selfie mantém mediana acima de 53 (fato 25, n de 4, período confundido); (3) as leituras de conselho (OAB, CFN 856, ABAC) não bloqueiam os 2 primeiros roteiros.

**Posição:** (a), com a conferência de nicho do brief passando de 11/11 para 16/11 (com n de 3 ou mais) e a ordem fixa da P13 para semana sem gravação.

**Probabilidade de sucesso** (2 reels de nicho por semana com gravação; mediana de 53 ou mais com pulo até 75% na conferência com n de 3; 1 reel de nicho com 106 ou mais até 23/11; 0 sintético; 0 sem o Bruno): **0,30**, faixa [0,15; 0,45], confiança 0,45. Se o Bruno gravar, a chance sobe muito [HIPÓTESE 16]; o risco é ele não gravar.

### D3. Grade, ritmo e operação

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 5 reels e 2 carrosséis fixos (minha posição) | S1 em 5 com o ci01 movido; 8 carrosséis novos | carga de agência de cerca de 4 h 48 min [ESTIMATIVA]; leitura limpa entre semanas |
| (b) 6 reels só na S1 | promessa do tl01 já não pede (fato 77) | 6º reel sem motivo |
| (c) 6 a 7 reels com portão | mais chance de estouro entre contas (7,7% contra 7,0%, fato 152) | mais peça fraca no feed; a conta já mostrou que 3 por dia não somou (fato 44) |
| (d) 3 reels e 2 carrosséis sem gravação | menos risco de formato fraco | menos leitura e menos presença na semana da TV |
| (e) Fora do óbvio: 4 reels e 3 carrosséis na S2 | carrossel com foto do Bruno tem mediana de 111 (fato 51), acima de qualquer formato da TV ainda não medido | quebra a regra de 5 e 2 por uma semana; precisa de motivo escrito como TESTAR |

**Premissas:** (1) a agência entrega os carrosséis até a sexta 18h; (2) o Bruno agenda uma semana por vez depois do portão; (3) 21h e 18h30 não pioram o alcance (fatos 39 e 40: hora não separou resultado dentro do formato).

**Posição:** (a). Horários: 21h nos dias úteis, 18h30 no sábado, carrossel às 12h no domingo e na terça (S1: terça e sábado), Trial Reel às 11h no domingo.

**Probabilidade de sucesso** (0 vaga vazia, 0 dia com 2 reels, mediana semanal de 42 ou mais nas 4 semanas e de 106 ou mais em 2, ganho líquido de 12 em 14 dias depois de 27/10): **0,15**, faixa [0,07; 0,28], confiança 0,40. As semanas fechadas tiveram medianas de 64, 128, 33,5 e 16 (fato 43): 106 em 2 semanas só acontece com gravação.

### D4. Stories e ob01 a ob03

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 03-plano estendido (8 por dia, 27 à mão) | mais views de story | carga à mão que não se sustenta 4 semanas [HIPÓTESE] |
| (b) 3 a 5 por dia | menos carga | menos views; story é o maior bloco de views (N4: 1.160 de 2.055) |
| (c) 6 a 8 em 4 blocos | equilíbrio da F6 | 20 à mão por semana |
| (d) S1 como está e S2 a S4 com 4 a 6 por dia e de 15 a 17 à mão; ob na S2 só com portão (minha posição) | a semana já agendada não mexe; a carga cai pela metade depois | se as views caírem, a régua de story mostra na segunda |
| (e) Fora do óbvio: story como captura, não como alcance. Um pedido de direct por dia ("me conta a sua área") no lugar do link | gera conversa, que é o produto do funil | toque em link fica sem número de qualquer forma; directs exigem resposta do Bruno em 24 h |

**Premissas:** (1) views de story dependem mais da quantidade de dias com story do que de 8 contra 5 por dia [HIPÓTESE, sem teste]; (2) o Bruno sustenta 2 stories à mão por dia; (3) a família da TV passa no portão para os ob irem ao feed.

**Posição:** (d), com 1 dia por semana no formato (e) a partir da S3 (quinta, no lugar do link), como TESTAR.

**Probabilidade de sucesso** (views de story por semana na base, 6 respostas a cada 14 dias, ob01 a ob03 com média de 42 e pulo até 75%): **0,20**, faixa [0,10; 0,35], confiança 0,35. Ressalva: a base de 982 do enquadramento era da janela até 14h11; às 17h24 a mesma janela marcou 1.160 (N4). Proponho base nova lida em seg 26/10 21h05.

### D5. Portão do Módulo 7

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 53 de alcance (27, 42, 106, 150) com coluna de minutos do Bruno (minha posição) | mesma régua do CLAUDE.md e do brief | comparável entre semanas e com o portão de impulsionar |
| (b) Views do `ig_reel_checkup` (57) | mais sensível a reassistir | mistura unidade com a regra dos 150 |
| (c) 37,5 de alcance | base mais recente | 106 vira 2,83x: régua mais frouxa no DOBRAR |
| (d) Mediana refeita a cada rodada | acompanha a conta | a comparação entre semanas some |
| (e) Fora do óbvio: régua em custo, alcance por minuto do Bruno | põe preço no minuto dele | sem minuto anotado vira sem dado; usada como coluna, não como régua |

**Premissas:** (1) o Bruno executa a lista até terça 11h; (2) os agentes leem na hora de 48 h; (3) o Instagram revisa reel com mais de 48 h (fato 33), então a leitura vale com a hora escrita.

**Posição:** (a), com (e) como coluna.

**Probabilidade de sucesso** (5 rodadas registradas, todas as decisões executadas até a segunda seguinte, nenhum PARAR com n de 1, mediana da S4 acima da S1): **0,12**, faixa [0,05; 0,25], confiança 0,45. A base de execução é 3 "sim" em 8 decisões em 21/10 (fato 125, corrigido no fato 180).

### D6. TABULEIRO e caminho até o diagnóstico

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) TABULEIRO em todo post de novembro que cumprir 150 | mais pedidos | fere o "1 por semana" do Módulo 1 (fato 171) |
| (b) Um único post no mês | leitura estrita | se esse post não passar, o mês fica sem teste |
| (c) Uma automação de conta toda, pedido só no post seguinte a um 150 com pulo abaixo de 60%, 1 por semana, 5 de conta toda desligadas, linkTracking e registro do funil (minha posição) | caminho único e contado | depende do Bruno desligar e ligar no prazo |
| (d) Não ligar em novembro até 1 disparo real | menos ruído | zero teste do caminho |
| (e) Fora do óbvio: na semana da TV, nenhuma palavra; captura por direct ("Chegou pela TV?") e bio com link do teste | atribui lead à TV, que é o único sinal possível hoje | depende de resposta à mão do Bruno em 24 h |

**Premissas:** (1) haverá ao menos 2 posts com 150 em 48 h até 16/11 [HIPÓTESE]; (2) comentário com a palavra aparece com retenção (fato 4.2 n. 47); (3) o Bruno informa os números do WhatsApp e do GA4 toda segunda.

**Posição:** (c) com (e) em 02 a 08/11.

**Probabilidade de sucesso** (3 disparos de terceiros até 22/11 e 1 diagnóstico agendado até 18/11): **0,08**, faixa [0,03; 0,18], confiança 0,50. O teto de comentários de qualquer tipo em 5 posts no nível do Dentista A é de 3,7 a 5,5 (fato derivado 13); a previsão do brief para diagnóstico é 1, de 0 a 3, com probabilidade 0,2 (fato 169).

---

## 5. Ideias e hipóteses numeradas

| # | Ideia ou hipótese | Confiança | Evidência |
|---|---|---|---|
| 1 | O perfil é a página de destino da TV: bio, link, fixados e destaque prontos até dom 01/11 18h | média | 77 visitas e 0 clique em 7 dias (N4); 1,57% em 30 dias (fato 14) |
| 2 | Bio do Módulo 2 sem o "Case: de 6 para 20 mi/mês" enquanto a autorização da Tzur for sem dado | alta | fato 102; 00-SISTEMA, Etapa 3 |
| 3 | Link da bio `/tabuleiro/?o=ig-bio`, a única troca que mexe na etapa medida e leva nota e gargalo ao WhatsApp | média | tabuleiro.js (fato 129); Módulo 2 aprovado e não aplicado (fato 132) |
| 4 | Fixar po01, R1 e o reel de 02/11 de 01 a 08/11 | média | [PRIOR] fixados ficam no topo da grade; po01 é o método |
| 5 | Destaque NA TV com o link da edição, sem logo, a partir de ter 03/11 | média | termos da TV (fato 137); destaque sem limite (fato 68) |
| 6 | Story "Chegou pela TV Câmara? Me manda um oi no direct e conta a sua área" como única atribuição da TV | alta | o `o=` não chega ao WhatsApp e o clique não é contado (fatos 114 e 129) |
| 7 | Contar directs que citam a TV de 02 a 08/11 | alta | fato a buscar 27 |
| 8 | Registro semanal das 11 etapas do funil no arquivo da semana | alta | F8, seção 9 |
| 9 | linkTracking ligado mostra o clique no botão do direct | média | hipótese 51 do livro |
| 10 | `o=` diferente por porta | alta | o parâmetro já existe nos links (fato 117) |
| 11 | O `o=` entrar na mensagem do WhatsApp do Tabuleiro | média | tabuleiro.js não leva (fato 129) |
| 12 | Desligar as 5 automações de conta toda antes do tl01 | alta | fatos 114 e 120; "caso" e "estrategista" na série (F8) |
| 13 | Uma TABULEIRO de conta toda a partir de 01/11 com texto genérico | média | F8, R7; log traz o post de cada disparo (fato 119) |
| 14 | Nenhuma palavra-chave em 02/11 | alta | 00-SISTEMA, Módulo 1 (fato 171) |
| 15 | ci01 em seg 02/11 21h | média | frase já anunciada para 02/11; Mirna em voz e rosto (fato 90) |
| 16 | po01 fica em 29/10 e é fixado na semana da TV | média | custo zero de mudança; método ligado aos 5 Lances (fato 129) |
| 17 | Portão da família da TV com n de 3 em dom 01/11 21h30 decide a S2 | média | regra de n mínimo do enquadramento; fato derivado 7 |
| 18 | Exceção da demanda criada: família da TV em MANTER com 27 a 41 se as visitas passarem de 21 por dia | baixa | compensação do ponto cego, sem base |
| 19 | Selfie de 02/11 como prioridade 1 do Bloco 1 | média | Bruno de frente: 5,2x no alcance (fato 25) |
| 20 | Selfie com a data falada e sem hora; hora só em texto | alta | horário sem dado (fato 133) |
| 21 | R2 e R3 como reel normal com 2 mudanças se a família da TV cair | média | únicos estoques com o Bruno de frente sem gravar (fato 35) |
| 22 | R1, R2 e R3 como Trial Reel aos domingos 11h, um por semana | média | segunda vida 35% e 15% (fato 150); Trial de conta pequena 21% (fato 151) |
| 23 | Trial Reel como laboratório de criativo para o impulsionamento de 19/11 | média | vai primeiro a quem não segue (enquadramento, D2) |
| 24 | O R1 já passa no portão de impulsionar | alta | 308 orgânico e 53,2% (N8) |
| 25 | Nunca impulsionar peça da TV | alta | termos (fato 137) |
| 26 | Dentista C fora do feed e do anúncio até decisão escrita sobre o portão de 300 | média | fatos 101 e 169 |
| 27 | A janela de 30 dias vai perder cerca de 1.900 contas pagas até meados de novembro | alta | 1.907 pagas em 30 dias e 0 em 7 dias (fato 10 e N4) |
| 28 | Pedir ao Bruno a campanha dos 1.907 (custo, datas, objetivo) | alta | sem base de custo hoje |
| 29 | Busca paga fora das 4 semanas | média | volume sem dado; 7 cliques em 30 dias |
| 30 | Search Console: consultas de marca 02 a 08/11 contra 19 a 25/10 | baixa | verificação do site: sem dado |
| 31 | Coluna "minutos do Bruno" no Módulo 7 | média | custo hoje é sem dado |
| 32 | Corte da TV custa menos minuto do Bruno por conta alcançada que roteiro de nicho, se passar de 42 | baixa | [ESTIMATIVA] 21 contra 9,3 por minuto (P17) |
| 33 | Tirar o "compartilhar o reel de ontem" das 09h00 de S2 a S4 | média | duplica o compartilhamento das 21h05 (05-manuais) |
| 34 | Cerca de 15 stories à mão por semana de S2 a S4 | média | 27 na S1 (N7); capacidade sem dado |
| 35 | Leitura fixa de story na segunda 19h | alta | janela móvel de 982 a 1.160 no mesmo dia (fato 56 e N4) |
| 36 | 2 enquetes e 1 caixa por semana | baixa | 3 respostas em 7 dias (N4) |
| 37 | Carrosséis com foto do Bruno na capa | média | 111 contra 34,5 (fato 51) |
| 38 | Carrosséis sem conteúdo da TV ficam elegíveis a impulsionar | média | fato 137 |
| 39 | car03 "Os 5 Lances" ligado ao resultado do Tabuleiro | média | o teste entrega um dos 5 Lances (fato 129) |
| 40 | Um pedido por legenda; po01 com "Comenta o nome dela que eu te respondo" | média | "comenta" e "link na bio" não somam (fato 148) |
| 41 | car01 com um pedido só: o direct | média | F8, seção 6 |
| 42 | Marcar a Mirna só onde ela aparece | média | hipótese 37 |
| 43 | Teste de marcação no tl01 publicado | alta | fato a buscar 5 |
| 44 | Convite de colaboração só no reel de 02/11 e no tl03 se aceito | média | F4, seção 6.4 |
| 45 | Mostrar tl04 e tl05 à Mirna antes de marcar | alta | efeitos sobre o rosto dela (fato 90) |
| 46 | Ouvir quem diz "Ainda. Sempre vai ser." antes do convite | alta | ficha e transcrição divergem (fato 91) |
| 47 | Conferir tl04 e tl05 nos quadros de 0 a 3 s até 13/11 | alta | sem dado hoje |
| 48 | tl02 com o trecho de 10,4 s sem voz: refazer ou aceitar o risco por escrito | média | fato 92 |
| 49 | tl02 sai só com os dois critérios ruins juntos ou abaixo de 27 | média | catálogo (fato 170) |
| 50 | mc04 no corte de 1705,567 s, em dom 01/11 09h00 | média | N6 |
| 51 | ob02 por último entre os ob | média | 82% do áudio do pf01 (fato 95) |
| 52 | Folha de 4 quadros por segundo dos ob até sex 30/10 | alta | regra do CLAUDE.md; render pronto (N5) |
| 53 | Menos de 5 votos: dizer nos stories e cumprir com o link da edição | média | catálogo (fato 170) |
| 54 | Conferência de nicho de 11/11 para 16/11 com n de 3 | média | nenhum reel de nicho até 09/11 sem gravação |
| 55 | Bloco 1: selfie, nutricionista A, consórcio sem a linha da ABAC | média | F5; travas (fato 103) |
| 56 | Piso de 1 roteiro por semana | alta | [ESTIMATIVA, F5] 12 a 18 min |
| 57 | Ordem fixa sem gravação: ob, mais votado, R2 e R3, banco, C condicional | média | P13 |
| 58 | Nunca voz sintética | alta | 32,5 de alcance e 83,9% de pulo (fato 27) |
| 59 | Distância de 6 h entre reels, Trial incluído | média | 0,92x (fato 152) |
| 60 | Feriados como dia normal na grade, lidos à parte | média | hipótese 24; 12/10 com animação (fato 41) |
| 61 | 21h nos dias úteis e 18h30 no sábado, como já está | média | hora não separou dentro do formato (fatos 39 e 40) |
| 62 | Reescrever a projeção do 00-SISTEMA em 26/10 | alta | a conta soma teste de 12 casas e conversa de 30 min (fato 131) |
| 63 | Declarar a meta de 10 diagnósticos fora de alcance nas 4 semanas, com a conta | alta | 637 visitas por mês contra cerca de 330 (seção 1.2) |
| 64 | Contar conversa de 30 min separada do teste de 12 casas | alta | fato 131 |
| 65 | Responder à mão comentário de profissão no mesmo dia, com `&p=` | média | o `p` aceita 6 profissões (fato 129) |
| 66 | `&p=dentista` no botão da TABULEIRO do Dentista B hoje | média | F8, seção 6 |
| 67 | Véspera (dom 01/11 17h30) sem hora | média | horário sem dado |
| 68 | Contagem nativa só com a hora confirmada | média | lembrete precisa de hora (fato 69, nível 3) |
| 69 | Agentes leem a grade da TV em 02/11 às 06h e 11h | alta | só a semana corrente fica no ar (fato 133) |
| 70 | Views da página da edição até 09/11 como medida secundária | média | mediana de 80,5 e máximo de 1.400 (fato 136) |
| 71 | Selfie "Foi ao ar" sem a tela da TV | alta | termos e catálogo (fato 137) |
| 72 | Impulsionar com objetivo de visitas ou mensagens, região de Campinas, 35 a 54 anos | baixa | fato 19; [PRIOR] sobre objetivos |
| 73 | Público de quem interagiu com o perfil como base de remarketing de 19/11 em diante | baixa | [PRIOR] |
| 74 | Gerenciador de Anúncios com post existente no lugar do botão impulsionar | baixa | [PRIOR] |
| 75 | Seguindo 3.529 contra 1.618 seguidores: medir não seguidores alcançados, não seguidores totais | baixa | N4; 00-SISTEMA (só 419 seguidores alcançados) |
| 76 | Ler a pilha de stories de 24/10 antes de dom 25/10 09h33 | alta | expira em 24 h (fato 67) |
| 77 | Dentista B com 106 e pulo abaixo de 60% abre TABULEIRO para o próximo nicho gravado | média | F8, R5 |
| 78 | tl03 com TABULEIRO só se o tl02 passar de 150 com pulo abaixo de 60% | média | F8, R5 |
| 79 | "Executado: sim ou não" por item, com hora | média | 3 de 8 executadas em 21/10 (fato 180) |
| 80 | Decisão não executada até terça 11h não é reaberta no portão seguinte sem motivo novo | baixa | evita portão que só adia |
| 81 | Levar o link da edição à reunião do BNI | baixa | "Visitor Host" na bio (fato 9); efeito sem dado |
| 82 | Mandar a gravação como documento, não pelo aplicativo de mensagem | média | 576x1024 na última fala (fato 104; hipótese 52) |
| 83 | Uma enquete por semana no formato "direct" no lugar do link, a partir da S3, como TESTAR | baixa | 0 conversa comercial em 50 (fato 124) |

Total: 83.

---

## 6. Pre-mortem: como este plano fracassa

1. **O Bruno não grava.** Nenhuma gravação desde 21/10 (fato 104). Sem a selfie e sem nicho, a S2 a S4 dependem da família da TV e de remakes. Se a família da TV ficar entre 27 e 41, a conta passa 4 semanas sem o único formato com mediana acima de 106. Sinal de alarme: qua 28/10 23h59 sem arquivo.
2. **A carga à mão não acontece.** Desligar automações, marcar a Mirna, stickers, mover o ci01, agendar car02 e mc04, bio nova: são mais de 30 ações na S1. Em 21/10, 3 de 8 decisões foram executadas (fato 180). Sinal: o tl01 sai com a CASE ligada e um "caso" num comentário recebe direct de diagnóstico.
3. **A TV não traz ninguém.** Exibição em feriado, horário sem dado, audiência sem dado. Visitas ao perfil ficam em 11 por dia, e o plano leu demais um evento pequeno. Meu ponto cego empurra para o lado oposto: o risco é eu concluir "a TV não funciona" com 3 dias de dado.
4. **A Mirna retira a liberação** ao ver efeitos sobre o rosto dela ou marcação em série. A série some da grade de uma vez; sobram remakes.
5. **Medição falha.** Sem GA4, WhatsApp e diagnósticos informados pelo Bruno, D6 termina em "sem dado" e o portão de impulsionar de 19/11 decide no escuro.
6. **Impulsionamento por impulso.** O Bruno impulsiona um corte da TV na semana da exibição. Fere os termos da emissora e queima a relação.
7. **A queda da janela de 30 dias é lida como crise** e alguém manda trocar a estratégia em meados de novembro.
8. **Trial Reel não é liberado** e os remakes ficam presos, ou saem como reel normal e repetem o que os seguidores já viram.
9. **Duas TABULEIRO com a mesma palavra** respondem ao mesmo comentário, ou nenhuma responde.
10. **O portão vira burocracia:** 5 leituras extras na S1 (26/10, 27/10 duas vezes, 28/10, 31/10, 01/11) e o Bruno deixa de olhar.

---

## 7. Previsões numéricas com data de conferência

D+30 a partir de dom 25/10 = 24/11; D+60 = 23/12; D+90 = 22/01/2027.

| # | Métrica | Previsão | Faixa | Conferência | Fonte |
|---|---|---|---|---|---|
| P1 | Mediana de alcance em 48 h dos reels publicados de 25/10 a 21/11 | 58 | 38 a 100 | seg 23/11 (D+30) | `ig_post_stats` |
| P2 | Média de visitas ao perfil por dia de 02 a 04/11 | 15 | 9 a 35 | seg 09/11 | `ig_account_stats` |
| P3 | Seguidores líquidos de 25/10 a 21/11 | +14 | -6 a +45 | qua 25/11 | `ig_follower_growth` |
| P4 | Disparos de TABULEIRO de perfis que não são do Bruno até 22/11 | 1 | 0 a 4 | seg 23/11 | `listCommentAutomationLogs` |
| P5 | Cliques no site em 30 dias | 5 | 1 a 14 | ter 24/11 (D+30) | `ig_account_stats` |
| P6 | Views de story em 7 dias, leitura de seg 23/11 19h | 900 | 600 a 1.400 | seg 23/11 | `ig_account_stats` |
| P7 | Reels com 106 ou mais de alcance em 48 h, de 25/10 a 21/11 | 3 | 1 a 7 | seg 23/11 | `ig_post_stats` |
| P8 | Alcance total de 30 dias (com a parte paga saindo da janela) | 1.500 | 1.100 a 2.300 | ter 24/11 | `ig_account_stats` |
| P9 | Views da página da edição do Bruno no site da TV | 110 | 40 a 700 | seg 09/11 | site da TV Câmara |
| P10 | Seguidores | 1.640 | 1.610 a 1.720 | qua 23/12 (D+60) | `ig_account_stats` |
| P11 | Diagnósticos de 30 min agendados de 25/10 a 23/12 (número do Bruno) | 2 | 0 a 6 | qua 23/12 (D+60) | Bruno |
| P12 | Alcance orgânico de 30 dias | 1.700 | 1.100 a 3.000 | sex 22/01/2027 (D+90) | `ig_account_stats` |
| P13 | Impulsionamentos feitos de 19/11 a 22/01 | 1 | 0 a 3 | sex 22/01/2027 (D+90) | Bruno |

Todas são [ESTIMATIVA] desta cadeira, ancoradas nas bases citadas na seção 2. Custo por resultado de impulsionamento: sem previsão, porque não há base de custo (seção 3.3).

---

## 8. O que mudaria minha opinião

- pb01 com 106 ou mais e pulo abaixo de 60% em qua 28/10: a família da TV vira DOBRAR, o ci01 pode voltar a 28/10 e a S2 fica toda com a TV.
- pb01 e po01 abaixo de 27: tiro a família da TV do feed já na S2, salvo o ci01 de 02/11.
- O Bruno grava o Bloco 1 inteiro: nicho entra na S2 e a conferência volta para 11/11.
- A Mirna confirma a hora até dom 25/10: contagem nativa entra e a chamada de 02/11 vai agendada com a hora.
- Visitas ao perfil acima de 30 por dia em 02 a 04/11: a TV é canal, e eu reabro a ideia de autorização escrita da emissora para uso pago (sem promessa de que venha).
- A campanha dos 1.907 tiver custo por visita conhecido: o primeiro impulsionamento ganha régua de custo.
- O Search Console mostrar busca de marca subindo depois da TV: campanha de pesquisa só de marca, com teto baixo.
- Trial Reel não elegível: remakes vão ao feed só no caminho B.

## 9. Lacunas

Horário da exibição; @ e ok escrito da Mirna; se o app marca pessoa em reel publicado; elegibilidade de Trial Reel; votos do tl01; folha de quadros dos ob; quadros de 0 a 3 s de tl04 e tl05; sessão de gravação e minutos do Bruno; leituras de OAB, CFN 856, ABAC, CFP e Res. CFO 196/2019; autorização da Tzur; GA4, WhatsApp e diagnósticos; origem, custo e datas do alcance pago de outubro; volume de busca e verificação no Search Console; alcance em feriado; audiência da TV; se a gravação do celular conta como conteúdo da emissora; qual automação responde quando duas têm a mesma palavra; teto de verba.

## 10. Fontes

- Leituras desta cadeira, 24/10 às 17h24 (São Paulo), só leitura: PostZen `listPosts` (conta j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 03h00 UTC a 01/12 03h00 UTC, ordenado por data, limite 100: 48 itens); Buzzfy `ig_account_stats` days=7; `ffprobe` e `stat` dos renders ob01 a ob03 no scratchpad da sessão; `videos/tv-camara/cortes/mc04.spec.json`, `mc02.spec.json`, `ob01.spec.json`; `git log` (commits eeb4f21 e 2b3a7d8).
- Repositório: `CLAUDE.md`; `conteudo/modo-god-cronograma/contexto.md`; `run/00-enquadramento.md`; `run/01-fatos.md`; `run/01-pesquisa/F1` a `F8` (F4 seções 3 a 9 e F8 seções 1 a 9 lidas por inteiro); `conteudo/stories-objecoes/05-manuais-bruno.md`, `06-agenda-postzen.md` e `02-provas.md` (linhas 130 a 150); `conteudo/sistema-instagram/00-SISTEMA.md` (Etapa 3, Projeção); `conteudo/modo-god-nichos/run/10-decision-brief.md` (D4).
- Não usei ferramenta fora da lista permitida (nada de conta de anúncio, `ig_comments`, `ig_inbox` ou Drive) e não li os planos das outras cadeiras.
