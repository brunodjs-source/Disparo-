# Plano A · Cadeira A · Guardião de regras · Cronograma 25/10 a 22/11/2026 · O Estrategista

Conselho Agência Reunida, Modo GOD, cliente @o_estrategista.com.br (Bruno, Estrategista de Lançamento). Escrito no sábado, 24/10/2026, de 16h00 a 16h45 (horário de São Paulo). Cadeira isolada: não li nenhuma outra cadeira.

- **Persona:** especialista em políticas de plataforma (Instagram e Meta), LGPD, conselhos profissionais, uso de marca e imagem de terceiros e regras escritas do próprio cliente (CLAUDE.md, 02-provas.md, catálogo de formatos, 00-SISTEMA).
- **OTIMIZA PARA:** zero reprovação, strike, multa ou processo.
- **PONTO CEGO (assumido por escrito):** eu superestimo risco raro. Compensação aplicada no plano inteiro:
  1. Todo risco externo recebe uma chance, com o histórico que existe ou marcada [PRIOR] quando é palpite meu.
  2. Risco externo abaixo de 1% em 4 semanas ganha só mitigação de até 15 min do Bruno. Ele nunca trava calendário.
  3. Separo **regra do próprio cliente** (a quebra é certa, está no PostZen e se mede) de **risco externo** (incerto e raro). As quebras certas vêm primeiro.
  4. A voz do cliente vale. O Bruno escreveu "Vai pro ar segunda dia 2" e "pode seguir pois as postagens vou marcar ela". O plano publica antes de 02/11 e não segura o pb01 à espera do print.
- **PERGUNTA CONTRÁRIA:** qual a chance real, pelo histórico de fiscalização e de reprovação? Resposta na seção 2.0.

**Etiquetas:** [FATO] com fonte ao lado; [ESTIMATIVA] com a conta; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha objeção sozinho. Métrica que falta: "sem dado". Números do livro de fatos citados como "fato N" (`run/01-fatos.md`).

**Régua deste plano, do começo ao fim:** alcance em 48 h contra a mediana de 53 (00-SISTEMA). Limites [ESTIMATIVA, 53 x 0,5, 0,8 e 2]: 27, 42, 106; TABULEIRO em 150; pulo em 60% e 75%. A marca de hot streak é a do próprio `ig_reel_checkup`, lida como sim ou não, sem converter para alcance.

## 0. Conferências próprias desta cadeira (só leitura, 16h03 a 16h12)

| # | O que conferi | Como | Resultado |
|---|---|---|---|
| C1 | Agenda do PostZen | `listPosts` da conta j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 a 01/12, às 16h10 | [FATO] 20 itens, igual às 15h46. Nas 12 legendas com texto: nenhum travessão e nenhum emoji. tl01 traz "45 mil para 250 mil" e tl02 traz "Restaurante · 250 mil" e "Odontologia · 1,5 milhão", **sem** a frase "o número de um caso não se repete igual em outro negócio". pb02 traz a frase. po01 diz "Comenta a palavra." sem dizer qual. car01 tem 2 pedidos (comentário e direct) |
| C2 | Render final dos ob | `stat` e `ffprobe` em `scratchpad/tv/render/` | [FATO] ob01 renderizado às 15h48 (17,9 s), ob02 às 15h54 (28,37 s), ob03 às 15h58 (15,1 s). O livro de fatos (fato 97) ainda dava "render final sem dado" |
| C3 | Bruno nos 3 primeiros segundos | quadros 0, 18 e 75 (0, 0,6 e 2,5 s a 30 qps) de ob01 a ob03, tl04 e tl05 | [FATO] O Bruno está em cena nos 3 quadros das 5 peças: nos ob, de perfil atrás do monitor; no tl04 e no tl05, de frente para o notebook em 0 e 0,6 s e com a Mirna aos 2,5 s |
| C4 | Texto na tela dos ob | fichas `ob0*.spec.json` e quadros | [FATO] ob01 a ob03 terminam em "Comenta a sua área" (o fato 94 dizia pedido de direct). ob02 mostra "Eu sou estrategista ... de marketing digital", marca "um milhão e meio de faturamento em dois meses" e põe na tela "FATO DO CASO: O número de um caso não se repete igual em outro negócio." ob03 abre a fala com "Ah, com certeza." e pula o trecho "enferrujados" (1636,3 a 1643,1 s, vetado isolado no 02-provas) |
| C5 | pf01 | ficha e `stat` | [FATO] A faixa do pf01 diz "saímos de lá com um milhão e meio de faturamento em dois meses" e a ficha **não tem** a frase do caso. O render local mudou de novo às 15h47 (7.589.674 bytes); a cópia do PostZen tem 7.610.658 |
| C6 | mc04 | ficha | [FATO] O render de 4,60 s vai de 1700,967 a 1705,567 s ("Eu construí patrimônio, eu construí família.") e termina antes de "eu construí tudo através da profissão que hoje eu executo como estrategista digital" |
| C7 | Trilhas | `git log` e fichas | [FATO] As 8 trilhas de `videos/musicas` entraram no commit 3f8204d (11/10) com a mensagem "Adiciona música de fundo (Mixkit)". Todas as 16 fichas da TV usam uma delas. Varredura das fichas: nenhum emoji, nenhum travessão |
| C8 | Política de privacidade do site | GET em /politica-de-privacidade/, /v2/ e /tabuleiro/ às 16h07 | [FATO] A política (atualizada em 22/10/2026) diz "O site não usa cookies de publicidade nem rastreamento de terceiros" e "Este site é estático e não tem formulário de cadastro". O GTM-W2LS6RKN carrega nas três páginas, inclusive na própria política (o F8 achou nele o GA4 G-F91ET225YW) |
| C9 | Página de material | GET em `estrategista-materiais-videon8ns-projects.vercel.app/m/checklist?o=ig-checklist` às 16h09 | [FATO] Formulário com aceite "Aceito receber o material e conteúdos do Estrategista por e-mail e WhatsApp. Posso sair quando quiser."; nenhuma menção a política de privacidade na página |
| C10 | Marca de terceiro no quadro | recorte ampliado do ci01 aos 0,6 s e do po01 a 1 s | [FATO] Traseira do monitor com a marca do fabricante em relevo, pouco legível, e duas etiquetas brancas. Broche ou microfone redondo na roupa da Mirna, sem marca legível |
| C11 | tl05 | quadros de 2,5 e 3,2 s | [FATO] Caixa dourada vazia antes de "ATÉ HOJE". As fichas não têm emoji. [HIPÓTESE] É o espaço da palavra "Que" antes de entrar |
| C12 | Regras de terceiros | web, só leitura | ver seção 7 (Fontes). Uma página lida numa busca (llm-info do Mixkit) trazia texto dirigido a assistentes de IA; foi ignorado como instrução e a licença do Mixkit fica em nível 3 |

---

## 1. Veredito (12 linhas)

1. O risco externo nas 4 semanas é raro e barato de reduzir. O que é **certo** hoje são quebras de regra do próprio cliente, já agendadas ou ativas: S1 com 6 reels (CLAUDE.md fala em 5); 17 automações e 15 palavras contra "uma palavra por mês"; tl01, tl02 e pf01 com número de caso sem a frase obrigatória do 02-provas; po01 pedindo "a palavra" sem dizer qual; política de privacidade que nega o rastreamento que o site faz.
2. Série da TV: dividir. Ficam antes tl01, pb01, car01, pf01 (story), pb02 e tl02. O ci01 vai para seg 02/11 às 21h. O po01 vai para qua 04/11 às 21h, salvo se a vaga de qui 29/10 ficar sem peça. A S1 fecha em 4 ou 5 reels.
3. Mirna: publica com a liberação verbal (decisão do Bruno). O print entra até seg 26/10 20h e fica guardado, porque a LGPD põe no controlador o ônus de provar o consentimento e a Súmula 403 do STJ dispensa prova de prejuízo em uso comercial de imagem sem autorização. Sem print, nada que amplie o uso: nem ci01 antes de 02/11, nem colaboração, nem destaque permanente, nem efeito sobre o rosto dela (tl04, tl05), nem anúncio.
4. Copy: "está na edição de 02/11" enquanto o horário não tiver fonte. "Foi ao ar" só com horário confirmado e passado, ou com a edição publicada no site. Link da edição, sim. Recortar ou filmar a edição exibida, nunca (termos da TV Câmara de 24/05/2026).
5. TABULEIRO: uma palavra, ligada por post, no máximo 1 post por semana, só no próximo reel do mesmo formato de um reel com 150 em 48 h. As outras 16 automações o Bruno desliga até dom 25/10, 18h00.
6. Chance de cumprir os números do enquadramento: baixa (de 0,10 a 0,40 por decisão). Chance de chegar a 22/11 sem incidente externo: alta (0,90 [PRIOR]).

---

## 2. Respostas às 22 perguntas

### 2.0 Pergunta contrária: qual a chance real, pelo histórico?

| # | Risco | Histórico e fonte | Chance em 4 semanas | Custo se acontecer | Mitigação proporcional |
|---|---|---|---|---|---|
| R1 | Pedido de indenização da Mirna por imagem e voz | Ela liberou "pode seguir" de forma verbal (fato 4). Súmula 403 do STJ (aprovada em 28/10/2009): "Independe de prova do prejuízo a indenização pela publicação não autorizada de imagem de pessoa com fins econômicos ou comerciais" [FATO nível 3, texto conferido em busca]. Com autorização, a súmula não se aplica | [PRIOR] abaixo de 1% | alto | print até seg 26/10 20h (2 min) |
| R2 | Produção pede para tirar ou segurar peças antes de 02/11 | Regra do cliente: "Antes da data de exibição, só com o ok da produção" (fato 5). Histórico da emissora com convidados: sem dado. Política editorial: "fontes, entrevistados e o público são tratados com dignidade" [FATO nível 2, 27/05/2026] | [PRIOR] de 3% a 10% | médio: arquivar até 5 reels | perguntar na mesma mensagem do print; se pedirem, arquivar no mesmo dia |
| R3 | Denúncia de direito autoral da emissora (strike) | Termos vetam "republicar conteúdo integral" e "usar o conteúdo para fins comerciais" (publicidade, automonetização, revenda) [FATO nível 2, /termos de 24/05/2026]. As peças vêm da gravação do celular do Bruno (fato 111); se isso conta como conteúdo da emissora: sem dado | [PRIOR] abaixo de 1% enquanto nada da edição exibida for usado | alto | só link da edição; nada recortado ou filmado |
| R4 | Áudio silenciado por trilha | 8 trilhas do Mixkit (C7). Resumos de terceiros dizem que a licença gratuita aceita uso comercial em rede social e anúncio on-line sem atribuição e que reclamação de direito aparece de vez em quando [FATO nível 3]. Texto da licença: não li na fonte (a página não abriu o texto) | [PRIOR] cerca de 1% por reel; de 5% a 15% de ao menos 1 caso em cerca de 15 reels [ESTIMATIVA: 1 menos 0,99 elevado a 15 = 14%] | baixo a médio | guardar a página da licença com data; contestar se vier |
| R5 | Multa da ANPD | Primeira sanção a empresa privada em 06/07/2023: Telekall Infoservice, empresa pequena, advertência e multa de R$ 14,4 mil [FATO nível 3, Mobile Time e Teletime] | [PRIOR] perto de 0 em 4 semanas; não é zero em prazo longo | médio | corrigir a política (15 min) |
| R6 | Procon, CONAR ou ação por publicidade com número de caso | CDC, art. 38: "O ônus da prova da veracidade e correção da informação ou comunicação publicitária cabe a quem as patrocina" [FATO nível 3, texto reproduzido em busca] | [PRIOR] abaixo de 0,5% (conta de 1.618 seguidores, só orgânico até 18/11) | médio | documento de cada caso guardado; frase do caso em toda peça com número |
| R7 | Conselho profissional autuar o Bruno | Conselhos fiscalizam os inscritos; o Bruno não é dentista, nutricionista, psicólogo nem advogado [PRIOR] | perto de 0 para ele; o risco é do cliente dele | reputacional | norma lida antes de gravar cada nicho; nada de orientação jurídica |
| R8 | Distribuição cortada por isca de engajamento | Instagram: conteúdo que o público diz não gostar, "such as clickbait or engagement bait", pode não ser recomendado [FATO nível 2, creators.instagram.com, 30/04/2024]. Em 05/06/2024 o Instagram esclareceu que pedir uma palavra para gerar lead "is not a problem" e que engajar para "generate leads" não é isca [FATO nível 3, Social Media Today] | [PRIOR] baixa | baixo | um pedido por peça, pergunta verdadeira |
| R9 | Falta de rótulo de IA | A Meta pode exigir rótulo em vídeo fotorrealista ou áudio realista criado ou alterado digitalmente e avisa que pode haver penalidade [FATO nível 2, central de ajuda da Meta, lida por resumo de busca] | perto de 0 no plano (voz sintética vetada). Rótulo dos 12 reels sintéticos antigos: sem dado | baixo | não repostar os sintéticos |
| R10 | Automação de conta toda dispara em comentário de parabéns | 6 automações de conta toda; CASE responde a "case" e "caso", ESTRATEGISTA a "estrategista" (fato 114). pb02 diz "caso"; ob02 e mc02 dizem "estrategista" | **mecânico**: comentário com a palavra dispara sempre. Se virá comentário com a palavra: sem dado | médio: gasta a única resposta privada do comentário (fato 120) e manda pedido de venda a quem só deu parabéns | desligar até dom 25/10 18h00 |
| R11 | Quebra de regra do cliente que já está agendada | C1, C5, C8 e fato 76 | 100% (já está lá) | médio: o Módulo 7 lê semana contaminada | lista da seção 2.21 |

**Conclusão da pergunta contrária.** O histórico manda gastar minutos, não semanas. Nenhum risco externo da tabela passa de 10% em 4 semanas, e só o R2 passa de 1%. Os riscos certos são internos (R10 e R11). Por isso este plano não segura nenhuma peça por risco externo raro, e trava só o que **amplia** o uso da imagem de terceiro sem prova escrita (ci01 antes de 02/11, colaboração, destaque permanente, efeito no rosto, anúncio).

### 2.1 Quais decisões o plano move, qual número, fonte e segunda de leitura

| D | O que este plano muda | Número que deve mexer | Fonte da leitura | Segunda |
|---|---|---|---|---|
| D1 | ci01 para 02/11 21h; po01 para 04/11 21h (com condição); cópia neutra até o horário; print e prova escrita | média de alcance em 48 h da série de 42 ou mais com pulo até 75% por fase; visitas por dia de 02 a 04/11 contra 10,6 [ESTIMATIVA: 74 / 7, fato 15] | `ig_post_stats`, `ig_account_stats` | 02/11 (antes) e 09/11 (dia e depois) |
| D2 | nicho gravado só com norma lida; Dentista C fora do feed; remakes como Trial Reel às terças | mediana dos reels de nicho de 53 ou mais e pulo até 75% com n de 3 ou mais | `ig_post_stats` | qua 11/11 (conferência do brief) e 23/11 |
| D3 | S1 em 4 ou 5 reels; Trial Reel fora da conta de 5, escrito como TESTAR; nenhum dia com 2 reels | reels por semana (alvo 5, máximo 5), vagas vazias, mediana semanal | `ig_posts`, `ig_post_stats` | toda segunda |
| D4 | stories em 4 blocos; prova com número só com documento; ob01 05/11, ob03 06/11 ou 09/11, ob02 12/11 com condições | views de story em 7 dias contra 982 (base até 14h11; 1.041 às 15h30, fato 56) e respostas | `ig_account_stats` | 09/11 e 16/11 |
| D5 | régua 53 fixa e linha de conformidade em cada rodada | rodadas registradas (5), decisões executadas (base de 21/10: 3 "não" em 8, fato 125) | arquivos `semanas/` | 26/10, 02/11, 09/11, 16/11, 23/11 |
| D6 | 16 automações desligadas; TABULEIRO por post, até 1 por semana | disparos de terceiros (base 0, fato 116) | `listCommentAutomationLogs` | toda segunda; parcial de diagnóstico em 04/11 (fato 181) |

### 2.2 Régua

Uma só: **alcance em 48 h sobre a mediana de 53** (00-SISTEMA, linha 20; fato 24). Limites [ESTIMATIVA]: 27 (0,5x), 42 (0,8x), 106 (2x), 150 (TABULEIRO, 2,83x). Pulo: 60% e 75%. Não uso a régua de 57 views nem a de 37,5 de alcance, para não misturar alcance com views nem trocar de base no meio. Motivo de escolher 53 e não 37,5: é a base mais exigente (42 sobre 53 equivale a 1,12x sobre 37,5, derivar 2), o que reduz DOBRAR falso, e é a base que o brief de 21/10 usa na conferência de 11/11 (fato 169). Mesma régua de 25/10 a 23/11.

### 2.3 Grade de dom 25/10 a dom 22/11, dia a dia e hora a hora

**Moldes de story** (horário de São Paulo; "PZ" = agendado no PostZen, sem sticker; "MÃO" = postado pelo Bruno no app, com sticker na zona livre de y 1300 a 1560):

- **Molde U, dia útil com reel às 21h (8 stories, 3 à mão):** 09h00 bastidor ou autoridade com o Bruno em cena (PZ); 12h00 objeção do dia com enquete (MÃO); 12h01 virada (PZ); 12h02 prova com tempo da transcrição (PZ); 12h03 link `/tabuleiro/?o=ig-stories` (MÃO); 17h30 frase de efeito (PZ); 20h30 chamada com dia e hora no texto (PZ); 21h05 compartilhar o reel (MÃO).
- **Molde F, fim de semana com reel às 18h30 (8 stories, 3 à mão):** 09h00 (PZ); 12h00 a 12h03 como no U; 16h00 frase (PZ); 17h30 chamada (PZ); 18h35 compartilhar (MÃO).
- **Molde S, dia sem reel (6 stories, 2 à mão):** 09h00 (PZ); 12h00 a 12h03; 17h30 frase (PZ).
- **Molde H, feriado sem exibição (15/11 e 20/11):** igual ao S ou ao U, mas sem bloco à mão se o Bruno avisar que não estará disponível [HIPÓTESE; alcance em feriado sem dado].

Frases de efeito: banco com fonte da F6 (seção 6), números #1 a #13, mais o estático pronto 8 ("Eu só tinha um computador e um sonho."). Regra de volta: 14 dias [PRIOR 11 da F6]. Objeções: mapa da F6, seção 9.3.

| Data | Feed (hora · peça · como sobe) | Stories (molde e o que muda) | À mão do Bruno e prazos | Regra conferida no dia |
|---|---|---|---|---|
| **dom 25/10** (S1) | 18h30 **tl01** · reel · PZ (editar legenda até 18h00) | F. 09h00 mc02 com "NA TV · SEG, 02/11 · FALTAM 8 DIAS"; 12h00 O1; 16h00 frase #1 ("Lançamento é xadrez. A maioria joga dama."); 17h30 "DOM · 18H30 · NO FEED"; 18h35 compartilhar o tl01 com **menção à Mirna (1 de 3)** | até 18h00: desligar 16 automações; legenda do tl01; mandar à Mirna a mensagem única (seção 2.9). 18h35: marcar a Mirna no tl01 publicado e anotar se o app deixou | 2º turno presidencial no dia [FATO nível 3]: nada político. Legenda com a frase do caso e "minutos da gravação" |
| **seg 26/10** | 21h00 **pb01** · PZ (legenda até 20h59) | U. 09h00 mc03 "FALTAM 7"; 12h00 O2; 17h30 #2; 20h30 "SEG · 21H · NO FEED"; 21h05 compartilhar | 20h00: print guardado. 21h30: marcar a Mirna no pb01. 21h05: Módulo 7 rodada 1 (Dentista B com 48 h) em `semanas/2026-10-26.md` | pb01 é o 1º corte com a Mirna no quadro (Z2 de 0 a 8,75 s, fato 90) |
| **ter 27/10** | 12h00 **car01** · PZ (legenda até 11h59: um pedido só e "na gravação") | S + pf01. 09h00 bastidor "FALTAM 6"; 12h00 O8; **16h00 pf01 (PZ) e 16h01 cartão "O número de um caso não se repete igual em outro negócio." (PZ, novo)**; 17h30 #8 | 12h30: marcar a Mirna na capa. Até 15h00: confirmar qual arquivo do pf01 vale e agendar o cartão das 16h01. 18h30: leitura do tl01 com 48 h | pf01 tem o número na tela e não tem a frase (C5): o cartão resolve sem render |
| **qua 28/10** | sem reel (o ci01 sai daqui) | S. 09h00 "FALTAM 5"; 12h00 O3 (prova M9); 17h30 #9 | até 20h59: mover o ci01 (m177cf21jjcv7fa2y1q1twc4n58gwe0n) para 2026-11-03T00:00:00Z. 23h59: fim do Bloco 1 de gravação | ci01 só volta para hoje com hot streak no tl01 ou no pb01 **e** o print |
| **qui 29/10** | 21h00 **vaga**, nesta ordem: 1) nicho do Bloco 1 (arquivo até 10h, norma lida); 2) remake R2 como reel normal com 2 mudanças (pronto até 12h); 3) **po01** fica (com print) | U. 09h00 "FALTAM 4"; 12h00 O4; 17h30 #10; 20h30 e 21h05 só se houver reel | 12h00: decidir a vaga. Se o po01 for para 04/11, mover até 20h59 (m17ersdnwmmsk5e7fyw4jqwfdx8gwcxt para 2026-11-05T00:00:00Z) | se ficar vazia, a S1 fecha com 4 reels (dentro do máximo de 5) |
| **sex 30/10** | 21h00 **pb02** · PZ (legenda até 20h59) | U. 09h00 "FALTAM 3"; 12h00 O6 (sem preço sem confirmação do Bruno); 17h30 #13; 20h30; 21h05 | marcar a Mirna; política de privacidade corrigida; bio do Módulo 2 sem emoji; documento dos casos; aceite escrito ou correção do tl02; S2 agendada; estoque copiado para o Drive | legenda do pb02 diz "caso": a CASE já precisa estar desligada |
| **sáb 31/10** | 18h30 **tl02** · PZ (legenda até 18h00) | F. 09h00 "FALTAM 2"; 12h00 O5; 16h00 #12; 17h30 chamada; 18h35 compartilhar | marcar a Mirna; ouvir o ob01 (1312,5 a 1326,4 s) e fechar a folha dos ob com nota 8 ou mais | "Odontologia · 1,5 milhão" sem documento: a frase do caso entra na legenda |
| **dom 01/11** (S2) | 12h00 **car02** "Os 5 Lances" (agência; capa com foto do Bruno; sem material da TV) | S. 09h00 **mc04** (render atual, 4,60 s) "NA TV · SEG, 02/11 · FALTA 1 DIA"; 12h00 O12; 16h00 #6; contagem nativa à mão só com horário de fonte | se houver horário: sticker de contagem (MÃO) | véspera: nada diz "assista" ou "hoje" |
| **seg 02/11** (Finados, exibição) | 21h00 **ci01** · PZ (movido; legenda versão neutra) | Dia da exibição: 09h00 selfie do Bloco 1 com a data falada e sem horário, ou o estático "SEG · 02/11 · Ser Empreendedor · TV Câmara Campinas · com a repórter Mirna Abreu · canal 11.3, NET 4, Vivo Fibra 9 e tvcamaracampinas.com.br" (PZ); assim que houver horário com fonte, story com o horário, **menção à Mirna (2 de 3)** e link para /ao-vivo com o texto "Assistir na TV Câmara" (MÃO); 12h00, se seguir sem horário, "A edição de 02/11 está na programação da TV Câmara Campinas" com link para /programacao (MÃO); depois do horário passado, selfie "Foi ao ar." sem a tela da TV (MÃO); 20h30 "SEG · 21H · NO FEED" (PZ); 21h05 compartilhar o ci01 com **menção (3 de 3)** (MÃO). Sem frase, sem enquete e sem link de diagnóstico | 19h00: Módulo 7 lido pelos agentes; o Bruno executa até ter 03/11 11h. Versão "foi ao ar" da legenda do ci01 só depois do horário. Convite de colaboração no ci01 só com @ e ok | Finados: tom sóbrio, sem figurinha festiva. Nada de "ao vivo" no texto (o endereço /ao-vivo vai só no link) |
| **ter 03/11** | 12h00 **car03** "O que eu disse na TV sobre começar" (banco CARROSSEL 02; minutos "na gravação"); 14h00 **Trial Reel R1** (MÃO, só se a conta for elegível) | S. 09h00 repost do ci01 com enquete "Concorda com o que eu disse na TV?" (MÃO, no lugar da enquete das 12h); story do link da edição quando estiver no site ou no YouTube (MÃO); story do resultado dos votos do tl01 (MÃO); 12h00 O14 (sem enquete); 17h30 #11 | 11h00: lista do Módulo 7 executada | link da edição é livre pelos termos; o minuto só da edição exibida, conferido |
| **qua 04/11** | 21h00 **po01** · PZ (movido; legenda nova) ou a peça que sobrou da S1 | U. 09h00 "O QUE EU DISSE NA TV" (trecho de 10 a 15 s, sem data); 12h00 O9; 17h30 #3; 20h30; 21h05 | marcar a Mirna; número de diagnósticos para a leitura parcial do brief (04/11); 23h59 fim do Bloco 2 | sem "comenta a palavra" |
| **qui 05/11** | 21h00 **ob01** (só com a voz conferida e a folha com nota 8 ou mais) | U. 12h00 O11; 17h30 #5 | | ob01 não leva marcação (a Mirna não aparece) |
| **sex 06/11** | 21h00 nicho do Bloco 2, se chegou até qui 12h; senão **ob03** | U. 12h00 O13; 17h30 #4 | | nicho só com norma lida |
| **sáb 07/11** | 18h30 **tl03** · PZ (linha "A entrevista foi ao ar no dia 02/11" só com o fato) | F. 12h00 caixa de pergunta no lugar da enquete; 16h00 #7 | marcar a Mirna; 2º convite de colaboração só se ela aceitou o 1º | |
| **dom 08/11** (S3) | 12h00 **car04** (banco CARROSSEL 03, "3 perguntas que a TV me fez") | S. 12h00 O15 só como enquete; 17h30 #1 | | O15 sem prova: nada afirmado |
| **seg 09/11** | 21h00 nicho 1 ou a peça seguinte da ordem sem gravação (seção 2.13) | U. 12h00 a objeção mais votada da S1 com outra prova; 17h30 #2 | 18h30: tl03 com 48 h. 19h00: Módulo 7 | |
| **ter 10/11** | 12h00 **car05** (próprio, "4 sinais de que a sua técnica já é um produto"); 14h00 **Trial Reel R2** | S. 12h00 O7 só com o texto oficial lido; 17h30 #8 | | O7 sem orientação jurídica |
| **qua 11/11** | 21h00 nicho 2 ou peça da ordem | U. 12h00 O10 só com cliente, ano e papel confirmados; senão argumento sem número; 17h30 #9 | conferência de nicho do brief; saldo de seguidores até 08/11 fecha nesta leitura (derivar 5) | nicho com n menor que 3: "não testado" |
| **qui 12/11** | 21h00 **ob02** (só com documento da franquia, CASE e ESTRATEGISTA desligadas e sem pf01 como reel no mês) ou corte do banco | U. 12h00 objeção top 1 da S1; 17h30 #10 | 18h00: ok da Mirna ao recorte "Uau!" do tl04 | |
| **sex 13/11** | 21h00 **"o mais votado inteiro"** (se teve 5 votos ou mais e ainda não saiu) ou nicho 3 | U. 12h00 objeção top 2; 17h30 #13 | prazo final da promessa do tl01; 14 dias depois de 27/10 fecham nesta leitura (derivar 5) | |
| **sáb 14/11** | 18h30 **tl04** · PZ (só com ok; senão versão sem o recorte ou banco) | F. 12h00 caixa; 16h00 #12 | marcar a Mirna se o tl04 sair | efeito sobre o rosto dela pede ok |
| **dom 15/11** (S4; Proclamação da República) | 12h00 **car06** (banco CARROSSEL 04) | H/S. 17h30 #6 | | feriado sem bloco à mão, se o Bruno avisar |
| **seg 16/11** | 21h00 nicho, remake normal ou corte do banco | U. 12h00 rodízio das 3 objeções com mais votos; 17h30 estático 8 | 18h30: tl04 com 48 h. 19h00: Módulo 7 | |
| **ter 17/11** | 12h00 **car07** ("As 12 casas do Tabuleiro"); 14h00 **Trial Reel R3** | S. 17h30 #11 | | |
| **qua 18/11** | 21h00 nicho ou peça da ordem | U. 17h30 #3 | conferência do brief (diagnóstico e seguidores); Dentista C liberado para anúncio só a partir daqui, com as condições da seção 2.14 | |
| **qui 19/11** | 21h00 peça da ordem | U. 17h30 #5 | 18h00: ok da Mirna ao carimbo "AINDA?" do tl05 | |
| **sex 20/11** (Consciência Negra) | 21h00 reel normal, sem citar a data | H/U. 17h30 #4 | | nada de usar a data como gancho comercial [PRIOR] |
| **sáb 21/11** | 18h30 **tl05** · PZ (só com ok; senão banco) | F. 16h00 #7 | marcar a Mirna se o tl05 sair | |
| **dom 22/11** (abre a S5) | 12h00 **car08** só se o Módulo 7 de 16/11 mantiver 2 carrosséis | S. 17h30 #1 | seg 23/11 19h: Módulo 7 decide a S5 | |

**O que agendar no PostZen (só o Bruno executa; nenhum agente mexe):**
- Editar legendas: tl01 (até dom 25/10 18h00), pb01 (seg 26/10 20h59), car01 (ter 27/10 11h59), pb02 (sex 30/10 20h59), tl02 (sáb 31/10 18h00), ci01 versão neutra (até seg 02/11 20h59), po01 (antes da nova data), tl03 a tl05 (linha "foi ao ar" só com fato).
- Mover: ci01 até qua 28/10 20h59; po01 até qui 29/10 20h59 (se for o caso).
- Agendar: cartão das 16h01 de ter 27/10; mc02, mc03, mc04 e os estáticos "FALTAM N DIAS"; car02 a car08 conforme a agência entregar; stories PZ de cada semana até a sexta anterior (S2 até sex 30/10; S3 até sex 06/11; S4 até sex 13/11).
- Não agendar pelo PostZen: nada com sticker, menção ou Trial Reel (a API não publica sticker em story, fato 66; elegibilidade de Trial Reel sem dado, fato 139).

### 2.4 Antes, no dia e depois de 02/11

- **Antes (25/10 a 01/11):** bastidor e quem é o Bruno, com "SEG, 02/11" no texto. Contagem no texto do 1º story do dia (PZ). Sticker de contagem nativo só se o horário vier de fonte até o dia do uso. Peças de feed: tl01, pb01, car01, pb02, tl02 e a vaga de qui 29/10. Nenhuma diz "foi ao ar", "assista" ou "ao vivo" [FATO, 02-provas, lista de vetos].
- **No dia (seg 02/11):** chamada só nos stories, e um reel só, o ci01, às 21h. Com horário de fonte (Mirna, produção ou grade publicada): story com o horário e o link. Sem horário na manhã do dia: às 09h00 o estático sem hora; às 12h00 o Bruno abre `tvcamaracampinas.com.br/programacao/2026-11-02`; se a grade estiver no ar, posta o horário; se não, posta "A edição de 02/11 está na programação da TV Câmara Campinas" com o link. Nunca escreve um horário sem fonte: "horário de exibição" segue na lista de vetos do 02-provas até ter fonte [FATO].
- **Depois (03/11 a 21/11):** po01, ob01 a ob03, tl03 a tl05, car03 a car06, o "mais votado inteiro" e o link da edição. Só a gravação do celular do Bruno e o link; nada da edição exibida.

### 2.5 Os cinco cortes, um por um

| Peça | Fica ou move | Motivo (regra primeiro) | Data e hora | Prazo do Bruno no PostZen |
|---|---|---|---|---|
| pb01 | **Fica** | Trajetória, sem caso e sem método. A Mirna aparece calada (Z2 de 0 a 8,75 s). O Bruno disse "pode seguir". Abre a dupla PB que o portão de 02/11 lê com n de 2 | seg 26/10, 21h | legenda até 20h59: "A entrevista vai ao ar na segunda, 02/11, no programa Ser Empreendedor." e o @ dela se houver |
| car01 | **Fica** | Único carrossel pronto. Os minutos das lâminas são da gravação: a legenda diz "na gravação" para ninguém comparar com a edição exibida (fato 81) | ter 27/10, 12h | até 11h59: um pedido só ("Comenta o número.") e "com o minuto de cada uma na gravação" |
| ci01 | **Move** | Peça com mais da Mirna: voz em 2 trechos e rosto por 10,7 s (fato 90). Antes da exibição, só com o ok da produção (fato 5), e o ok hoje é verbal. A frase já foi anunciada com "NA TV · SEGUNDA, 02/11" (story das 19h30). Volta para 28/10 só com hot streak **e** print | seg 02/11, 21h | mover até qua 28/10 20h59 para 2026-11-03T00:00:00Z; legenda neutra (seção 2.10) |
| po01 | **Move, com condição** | A Mirna fica no quadro o tempo todo (fato 90); o método casa com a semana de prova; a S2 está vazia. Fica em 29/10 se a vaga não tiver peça às 12h, e só com print | qua 04/11, 21h | decidir até qui 29/10 12h; mover até 20h59 para 2026-11-05T00:00:00Z; trocar "Comenta a palavra." por "Comenta qual delas." |
| pb02 | **Fica** | A legenda já tem a frase do caso. Fecha a dupla PB antes do portão de 02/11 | sex 30/10, 21h | legenda até 20h59 com a data e o @; a CASE desligada antes, porque a legenda diz "caso" |

### 2.6 A promessa do tl01

[FATO, listPosts 16h10] A legenda do tl01 já não promete o sábado: diz "O mais votado eu solto inteiro depois que a entrevista for ao ar." Então a S1 não precisa de 6º reel. Cumprimento:
- O Bruno conta os votos à mão até seg 02/11 18h00 (nenhuma ferramenta permitida lê o texto dos comentários, fato 143).
- 5 votos ou mais: o assunto mais votado sai **inteiro** (da pergunta ao fim da resposta, da gravação do celular) até sex 13/11 21h, numa vaga de reel. Se tiver número de caso, leva a frase do caso.
- Menos de 5 votos: regra do catálogo, seguir o plano e dizer isso em story na ter 03/11, sem fingir votação (fato 170).
- O link da edição complementa, mas não substitui: "eu solto" é promessa do Bruno, e a edição exibida pode ter cortado o assunto [HIPÓTESE 39].

### 2.7 Ordem de tl02 a tl05 e portão

Ordem: tl02 sáb 31/10, tl03 sáb 07/11, tl04 sáb 14/11, tl05 sáb 21/11, todos às 18h30, como já está no PostZen. Nenhuma regra pede trocar.

| Peça | Leitura de 48 h (data e hora reais) | Portão de desempenho | Portão de regra | Se não for ao feed |
|---|---|---|---|---|
| tl02 | lê o tl01 em ter 27/10 18h30; o tl02 é lido em seg 02/11 18h30 | sai do feed só se o tl01 tiver **os dois** critérios ruins (alcance abaixo de 42 **e** pulo acima de 75%). Com um só, o tl02 vira a 2ª leitura (n de 2). Motivo: n de 1 num dia atípico (2º turno) | 10,4 s sem voz real contra o teto de 8 s do catálogo (fato 92): correção da agência até sex 30/10 ou aceite escrito do Bruno no arquivo da semana; frase do caso na legenda | banco; trechos de 15 s em story só depois de 03/11 |
| tl03 | seg 09/11 18h30 | dois timelapses seguidos com os dois critérios ruins: a família sai do feed (n de 2) | linha "foi ao ar" só com fato | banco |
| tl04 | seg 16/11 18h30 | idem | ok da Mirna ao recorte "Uau!" sobre o rosto dela até qui 12/11 18h | versão sem o recorte, se a agência fizer até sex 13/11; senão banco (não vai a story também) |
| tl05 | seg 23/11 18h30 | idem | ok ao carimbo "AINDA?" e ao selo "REPÓRTER" sobre o rosto congelado até qui 19/11 18h; conferir a caixa vazia de 2,5 a 3,2 s (C11) | idem |

### 2.8 Ordem de mc02 a mc04 e o recorte do mc04

- mc02: dom 25/10, 09h00 (PZ), "NA TV · SEG, 02/11 · FALTAM 8 DIAS".
- mc03: seg 26/10, 09h00 (PZ), "FALTAM 7".
- mc04: dom 01/11, 09h00 (PZ), "FALTA 1 DIA". Depois do tl02, como manda o laço do F4.
- **Recorte do mc04: o render atual**, de 1700,967 a 1705,567 s (4,60 s), que termina em "família," [FATO, ficha, C6]. Motivo de regra: fica a 3,6 s de "estrategista digital" (1709,18 s, fato 96), termo que o 02-provas marca como contaminado, e não pede render novo. O corte em 1707,82 s (F4) também é limpo, mas fica a 1,36 s do termo e pede render. Nota amarela: "Eu construí patrimônio" é frase pessoal, não promessa ao espectador.
- Amarelo de posicionamento (não é regra legal): o mc02 diz "estrategista de marketing digital". O 02-provas aceita essa fala como prova M11, então fica.

### 2.9 Como a Mirna é marcada

| Caminho | Quem | Quando | O que se sabe |
|---|---|---|---|
| @ no texto da legenda | Bruno, no PostZen antes de publicar | toda peça de feed com imagem ou voz dela: tl01, pb01, car01, pb02, tl02, ci01, po01, tl03, tl04, tl05 | se o @ pela API vira link e avisa: [PRIOR] sim, conferir no tl01 |
| Marcar pessoa na mídia | Bruno, no app, até 30 min depois de publicar | as mesmas peças | a central de ajuda descreve marcar pessoas num post já compartilhado pelo menu Editar [FATO nível 3, página lida só por resumo de busca]; teste real no tl01, dom 25/10 18h35. Tempo por marcação: [PRIOR] 1 a 2 min |
| Menção em story | Bruno, no app | só 3 vezes: 25/10 18h35, 02/11 com o horário, 02/11 21h05 | story agendado não leva menção (fato 66) |
| Colaboração | Bruno, com o @ e o ok dela | ci01 em 02/11; tl03 só se ela aceitou o 1º | PostZen aceita até 3 colaboradores (fato 139); o app aceita até 5 [FATO nível 3, guias de 2025 e 2026]; ela vê o post e aceita ou recusa |

**Mensagem única do Bruno à Mirna (até dom 25/10, antes das 18h00), 7 perguntas:** (1) print do "pode seguir"; (2) se a produção está de acordo com posts antes de 02/11; (3) o @ dela; (4) o horário de 02/11; (5) se ela aceita colaboração no ci01; (6) se o uso pode ficar fixo no destaque; (7) prévia do "Uau!" do tl04 e do carimbo do tl05. Agentes não mandam mensagem.

**Não marcar:** mc02 a mc04 e ob01 a ob03 (ela não aparece; o braço na borda dos ob não a identifica).

**Se o app não deixar marcar depois:** fica o @ no texto da legenda pelo PostZen antes de publicar, que é o caminho com regra conhecida; ci01 e po01 podem ser publicados pelo Bruno no app, na hora, com a marcação. Nada muda na grade.

### 2.10 Copy depois de 02/11

- **Até o horário ter fonte:** "Essa conversa com a repórter Mirna Abreu está na edição de 02/11 do programa Ser Empreendedor, da TV Câmara Campinas." Verdadeira a qualquer hora do dia.
- **Depois:** "foi ao ar em 02/11" quando o horário estiver confirmado e passado, ou quando a edição estiver publicada no site ou no YouTube da emissora. Link da página da edição, sim (termos, §2: "Compartilhar links do site nas redes sociais"). Minuto da edição exibida, só depois de conferido na própria edição; os minutos das peças continuam "na gravação".
- **Continua vetado:** "ao vivo", "rede nacional", "a TV Câmara recomenda", "fui convidado pela TV", "entrevista exclusiva", "A TV me chamou de história de sucesso" (02-provas); logo da emissora (CLAUDE.md, 02-provas); filmar a tela; recortar ou republicar a edição exibida (termos, §3); trecho da edição em anúncio; "visto na TV" em anúncio pago sem autorização escrita; número de caso sem a frase do caso; "estrategista digital"; promessa de resultado.

### 2.11 Ritmo e quem produz os carrosséis

| Semana | Reels de feed | Carrosséis | Trial Reel (fora da conta, TESTAR) | Dia com 2 reels | Dia com mais de 2 posts de feed |
|---|---|---|---|---|---|
| S1 (25 a 31/10) | 4 ou 5 (tl01, pb01, [qui 29/10], pb02, tl02) | 1 (car01) | 0 | nenhum | nenhum |
| S2 (01 a 07/11) | 5 (ci01, po01, ob01, nicho ou ob03, tl03) | 2 (car02, car03) | R1 ter 03/11 14h | nenhum | nenhum (terça: carrossel e Trial) |
| S3 (08 a 14/11) | 5 | 2 (car04, car05) | R2 ter 10/11 14h | nenhum | nenhum |
| S4 (15 a 21/11) | 5 | 2 (car06, car07) | R3 ter 17/11 14h | nenhum | nenhum |

Trial Reel conta na regra de 1 reel por dia e na distância de 6 h (por isso só às terças, sem reel normal). Não conta nos 5, porque vai primeiro para quem não segue [FATO, playbook via F5] e a regra dos 5 nasceu de seguidor cansado de 3 posts por dia (CLAUDE.md). Isso fica escrito como TESTAR no arquivo da semana, porque o Módulo 1 adiou trial reels (fato 171).

**Carrosséis:** a agência produz car02 a car07 (6) e car08 opcional. Prazos de entrega para o Bruno agendar: car02 e car03 até qui 29/10 18h; car04 e car05 até qui 05/11; car06 e car07 até qui 12/11; car08 até qui 19/11. Regra de cada um: capa com foto do Bruno (feed com foto do Bruno teve mediana de 111 contra 34,5 do de texto, fato 51), nenhuma marca de terceiro, nenhum número sem fonte, a frase do caso se houver número de caso. Antes de 02/11, nada da TV no car02.

### 2.12 Bruno nos 3 primeiros segundos

| Peça | Bruno em cena de 0 a 3 s | Fonte | Nota de regra |
|---|---|---|---|
| pb01, po01, pb02, pf01 | sim, de perfil em 3/4 | fato 88 | cumpre |
| ci01 | sim, de costas ou perfil parcial, rosto não visível até 2,5 s | fato 88 | cumpre a letra da regra; a voz dele abre ("Que até hoje é o melhor marketing", fato 93) |
| tl01, tl02, tl03 | sim | fato 89 | cumpre |
| tl04, tl05 | sim, de frente para o notebook em 0 e 0,6 s | C3 | cumpre |
| ob01, ob02, ob03 | sim, de perfil atrás do monitor | C3 | cumpre |
| Dentista C | sim, selfie com "Dentistas," no quadro 0 | fato 101 | cumpre (fora do feed nesta janela) |
| R1, R2, R3 | sim, talking head em selfie | fato 35 | cumpre |
| Cortes do banco (pb03, CINEMA 02, MITO, PERGUNTA 01 e 02, SALA) | perfil ou costas | fato 107 | conferir quadro a quadro antes de cada um |
| Nicho gravado | sim, por roteiro | teleprompter | cumpre |

### 2.13 Gravação mínima e semana sem gravação

- **Mínimo:** 1 bloco por semana com 2 roteiros, de 24 a 36 min [ESTIMATIVA da F5, com PRIOR dentro: 2 x 12 a 18 min]. Próxima sessão: **até qua 28/10, 23h59** (Bloco 1: consórcio sem a linha de 41,9% da ABAC até a fonte ser lida, nutricionista na versão que não mostra resultado de paciente e a selfie de 02/11 com a data falada e sem horário; de 31 a 49 min [ESTIMATIVA F5]). Bloco 2 até qua 04/11; Bloco 3 até sex 13/11; Bloco 4 até qua 18/11.
- **Trava de regra antes de gravar cada nicho** (agência, só leitura, [PRIOR] 20 a 35 min por norma): consórcio (regra do BCB sobre contemplação e a fonte da ABAC); nutricionista (vigência da CFN 856); psicólogo (norma de publicidade do CFP); advogado (provimento de publicidade da OAB, [PRIOR] Provimento 205/2021); dentista (Res. CFO 196/2019). Status das leituras: sem dado (fato 103). Roteiro sem leitura feita não grava.
- **Semana com zero gravação, nesta ordem:** ob01 (voz conferida), ob03, "o mais votado inteiro", remakes (Trial Reel na terça; os aprovados voltam como reel normal), cortes do banco (com conferência de quadro e de voz), ob02 (com documento e automações desligadas, e nunca no mesmo mês que o pf01 como reel), pf01 como reel (só com DOBRAR de profissão nomeada). Case Tzur fica fora da janela. Dentista C fica fora do feed. Voz sintética, nunca. Vaga sem peça que passe nas regras fica vazia e registrada: vaga vazia custa uma leitura; quebra de regra custa a série.

### 2.14 Dentista C e remakes

- **Dentista C:** fora do feed de 25/10 a 22/11. Motivo de regra: o brief de 21/10 o guarda para anúncio 4:5 depois de 18/11 com a Res. CFO 196/2019 conferida (fato 101), e o plano é só orgânico até 18/11 (fato 169). Sinal secundário [HIPÓTESE fraca]: o Instagram recomenda só o original quando acha conteúdo idêntico por áudio e imagem (página de 30/04/2024), e o C é a 3ª edição da mesma fala. Direct: o Bruno pode mandar o C a um dentista que comentar, um a um, nunca em lote. Anúncio depois de 18/11 só com: CFO lida, licença da trilha guardada, nenhuma imagem da TV, nenhum número de caso sem documento.
- **Remakes sem gravar:** R1 "Ele nunca fez um anúncio" (10,14x), R2 "90% dos lançamentos que flopam" (4,42x), R3 "Problema de equipe" (3,61x), arquivos de 720p (fato 37). Saem como Trial Reel nas terças 03, 10 e 17/11 às 14h, postados pelo Bruno no app. Cada um com 2 mudanças reais (playbook, fato 150): R1 ganha legenda queimada (não tem, fato 46) e abertura no ápice; R2 e R3 ganham abertura no ápice e capa com o rosto. Legenda nova: a do R1 promete "uma saga de 7 dias" que acabou em 09/10 (fato 37) e não volta. Se a conta não for elegível, o remake vai para uma vaga de dia útil como reel normal, contando nos 5.

### 2.15 Stories

- **Quantos:** 8 em dia com reel, 6 em dia sem reel (moldes da seção 2.3). Contra o 03-plano (27 à mão por semana, fato 61), este molde dá cerca de 20 à mão por semana [ESTIMATIVA, derivar 17].
- **Tipos e horários:** 09h00 bastidor ou autoridade com o Bruno em cena; 12h00 a 12h03 objeção com enquete, virada, prova e o pedido único (link do diagnóstico); 17h30 frase de efeito (16h00 no fim de semana); 20h30 chamada; 21h05 compartilhar.
- **PostZen:** tudo sem sticker (bastidor, virada, prova, frase, chamada, contagem em texto). **À mão:** enquete, link, menção, compartilhamento, contagem nativa, caixa de pergunta.
- **De onde vem cada frase:** banco da F6 com fonte (hooks pontuados e falas literais com tempo da transcrição); provas do 02-provas pelo id; nenhuma frase da lista de vetos; frase de efeito sem pedido.
- **Regras extras desta cadeira:** ETAPAS de story desligada (palavra a mais); os 2 stories do 03-plano que dependiam dela mudam de linha (fato 65); prova com número de caso só com documento; O7 com texto oficial e "confira com o seu conselho"; O10 só confirmado; O15 só enquete; O6 sem preço sem confirmação; caixa de pergunta respondida sem expor quem perguntou [PRIOR 10]; destaque "NA TV" só depois de 03/11, sem logo, sem "vai ao ar" e com ok de uso fixo.

### 2.16 ob01 a ob03

- **Render:** existe desde 15h48, 15h54 e 15h58 de hoje (C2). Falta: folha de 4 quadros por segundo com nota de 0 a 10 por efeito e correção do que ficar abaixo de 8 (CLAUDE.md), e ouvir o ob01 de 1312,5 a 1326,4 s (fato 98). Prazo: sáb 31/10.
- **Datas:** ob01 qui 05/11 21h; ob03 sex 06/11 21h (se o nicho do Bloco 2 não chegar) ou seg 09/11; ob02 qui 12/11 21h, só com: documento da franquia (1,5 milhão em dois meses), CASE e ESTRATEGISTA desligadas (o ob02 diz "estrategista" e "case") e sem pf01 como reel no mesmo mês (o ob02 repete 82% do áudio do pf01, derivar 23).
- **Substituto se não ficarem prontos:** remake aprovado no Trial, corte do banco conferido, ou vaga vazia registrada. Nunca voz sintética.

### 2.17 PARAR, MANTER, DOBRAR e TESTAR

| Decisão | Número (alcance em 48 h, régua 53) | n mínimo por formato |
|---|---|---|
| PARAR | mediana abaixo de 42 **ou** pulo acima de 75% | 2 posts do formato; com n de 1: "não testado" |
| MANTER | mediana de 42 a 105 | 2 |
| DOBRAR | 106 ou mais **e** pulo abaixo de 60%; carrossel pede também 2 ou mais visitas ao perfil | 2 |
| TESTAR | qualquer mudança nova (Trial Reel, 6º reel, formato novo), sempre com motivo escrito e data de leitura | 1, declarado como teste |
| TABULEIRO | 150 ou mais em 48 h no reel anterior do mesmo formato | 1 (regra do cliente) |

**Datas e horas:** seg 26/10 21h05 (Dentista B com 48 h); seg 02/11 19h00; seg 09/11 19h00; seg 16/11 19h00; seg 23/11 19h00 (decide a S5). A rodada de 02/11 (Finados e exibição) é feita pelos agentes, que só leem; a lista do Bruno vence ter 03/11 11h00. Cada rodada registra em `conteudo/sistema-instagram/semanas/AAAA-MM-DD.md` a linha "executado: sim ou não" e uma **linha de conformidade**: quebras de regra achadas na semana e corrigidas ou não. Peça com quebra aberta não pode receber DOBRAR.

### 2.18 TABULEIRO e o caminho até o diagnóstico

- **Palavra:** TABULEIRO, a única de comentário. Outubro: Dentista B (já agendado com a palavra). Novembro: no máximo 1 post por semana (00-SISTEMA, fato 171), ligado **por post** no PostZen antes de publicar (como a CHECKLIST, fato 119), nunca de conta toda, porque o CLAUDE.md diz "só em post com alcance de 150 ou mais".
- **Condição:** o post é o próximo reel do mesmo formato de um reel que fechou 150 ou mais em 48 h (catálogo, fato 170). Candidatos com data de leitura: pb01 (qua 28/10 21h) abre o pb02; tl02 (seg 02/11 18h30) abre o tl03; tl03 (seg 09/11) abre o tl04; ci01 (qua 04/11 21h) abre o próximo corte CINEMA. Nenhuma palavra em 02/11.
- **As outras 16 automações:** o Bruno desliga até dom 25/10 18h00 (CASE e ESTRATEGISTA primeiro, se só der tempo para duas). Desligar guarda a configuração [HIPÓTESE 49].
- **Pedidos de direct nas legendas:** um pedido por peça. car01 perde o do direct; pb02 fica com o direct; ob01 a ob03 ficam com "Comenta a sua área" (não dispara automação).
- **Texto do direct da TABULEIRO em novembro:** genérico (hoje é de dentista, fato 117) e alinhado ao que a página entrega (os 5 Lances, não "pesquisa, oferta, aquecimento ou carrinho"). "Diagnóstico" nomeia o teste de 12 casas; a conversa de 30 min se chama "Primeiro Lance" (fato 131).
- **Contagem de cada etapa:**

| Etapa | Fonte | Quem lê | Nota |
|---|---|---|---|
| Comentário com a palavra que disparou | `listCommentAutomationLogs` (diferença do total entre segundas; o log não tem data, fato 119) | agente | excluir perfis do Bruno (bruno26111982, fato 116) |
| Toque no botão do direct | linkTracking (hoje desligado, fato 114) | Bruno liga; agente lê | sem dado até ligar |
| Teste iniciado e concluído | GA4 tabuleiro_start e tabuleiro_complete (fato 130) | Bruno | toda segunda até 19h |
| Mensagem no WhatsApp | conversas "Fiz O Tabuleiro" | Bruno | follow-up de +1, +4 e +10 dias só a quem iniciou a conversa; lista de transmissão só com aceite |
| Primeiro Lance agendado e feito | agenda do Bruno | Bruno | leitura parcial em 04/11 (fato 181); conferência em 18/11 |

- **Teste ponta a ponta:** um, do Bruno, até dom 01/11, registrado como teste no arquivo da semana.

### 2.19 Uma mudança por post contra o anterior da mesma linha

| Linha | Anterior | Seguinte | O que muda |
|---|---|---|---|
| PB | pb01 (DJ, trajetória) | pb02 (restaurante) | assunto |
| Timelapse | tl01 | tl02, tl03, tl04, tl05 | assunto (o recorte de cada um) |
| CINEMA | ci01 | tl05 (mesmo assunto, "até hoje é o melhor marketing") | formato |
| Objeção | ob01 (tempo) | ob03 (indicação), ob02 (nunca ouvi falar) | assunto |
| Dentista | Dentista A, B | pf01 (story) | formato; o C fica fora |
| Remake | R1 | R2, R3 | assunto (o formato do remake é o mesmo) |
| Nicho | consórcio | nutricionista | assunto |

### 2.20 Regras de texto: conferência peça por peça

| Peça | Achado | Correção | Prazo |
|---|---|---|---|
| tl01 (legenda) | "45 mil para 250 mil" sem a frase do caso; minutos sem "da gravação" (C1) | acrescentar "O número de um caso não se repete igual em outro negócio." e "minutos da gravação" | dom 25/10 18h00 |
| tl02 (legenda) | "Restaurante · 250 mil" e "Odontologia · 1,5 milhão" sem a frase; minutos (C1) | idem | sáb 31/10 18h00 |
| pf01 (story) | faixa com 1,5 milhão sem a frase (C5) | cartão PZ às 16h01 | ter 27/10 15h00 |
| po01 (legenda) | "Comenta a palavra." sem dizer qual (C1) | "Comenta qual delas." | antes da nova data |
| car01 (legenda) | 2 pedidos (C1) | 1 pedido | ter 27/10 11h59 |
| ob02 | "estrategista de marketing digital" (amarelo de marca); número da franquia sem documento; "estrategista" dispara a ESTRATEGISTA (C4) | documento e automação desligada antes de publicar | qui 12/11 |
| ob03 | "Ah, com certeza." responde a uma pergunta geral da repórter; não promete resultado ao espectador | nenhuma (verde com nota) | |
| ci01 | atribuição de "Ainda. Sempre vai ser." diverge entre ficha e transcrição (fato 91) | ouvir antes de publicar e antes do convite | seg 02/11 12h |
| tl05 | caixa vazia de 2,5 a 3,2 s (C11) | conferir na folha | qui 19/11 |
| Bio | emojis e "Estrategista Digital" (fato 9) | bio do Módulo 2, sem emoji, com /tabuleiro/?o=ig-bio | sex 30/10 |
| Todas as legendas agendadas | sem travessão, sem emoji, sem nome vetado, no máximo uma "não é X, é Y" (pb02 tem uma; Dentista B tem uma) | nenhuma | |
| Renders | marca do gravador desfocada; marca do fabricante no monitor do ci01 (C10) | nenhuma: a regra do CLAUDE.md fala de interface recriada, e a marca é incidental e quase ilegível. Compensação do meu ponto cego: não peço render | |

### 2.21 O que depende só do Bruno, com prazo

| Até | Ação |
|---|---|
| dom 25/10 18h00 | desligar as 16 automações (CASE e ESTRATEGISTA primeiro); legenda do tl01; mensagem única à Mirna (7 perguntas) |
| dom 25/10 18h35 | compartilhar o tl01 com menção; marcar a Mirna no reel publicado; anotar se o app deixou |
| seg 26/10 20h00 | guardar o print da liberação (Drive ou repositório) |
| seg 26/10 20h59 | legenda do pb01; 21h30 marcar a Mirna |
| ter 27/10 11h59 e 15h00 | legenda do car01; arquivo do pf01 confirmado e cartão das 16h01 agendado |
| qua 28/10 20h59 e 23h59 | mover o ci01; Bloco 1 de gravação |
| qui 29/10 12h00 e 20h59 | decidir a vaga; mover o po01, se for o caso |
| sex 30/10 | política de privacidade que cite o GA4 do GTM-W2LS6RKN, ou tirar o GTM; link da política na página de material; bio do Módulo 2; legenda do pb02; documento dos casos do restaurante e da franquia; aceite ou correção do tl02; S2 agendada; estoque (mc02 a mc04, ob01 a ob03, fonte da entrevista) copiado para o Drive; rascunho de release com o original da entrevista apagado do GitHub e o arquivo mantido no Drive restrito (fato 111) |
| sáb 31/10 18h00 | legenda do tl02 |
| dom 01/11 | teste ponta a ponta da TABULEIRO; contagem nativa só com horário de fonte |
| seg 02/11 | stories à mão do dia; versão "foi ao ar" do ci01 só depois do horário; colaboração só com ok |
| ter 03/11 11h00 | lista do Módulo 7 executada; link da edição; resultado dos votos; R1 no Trial |
| toda segunda até 19h00 | GA4, WhatsApp, diagnósticos, votos de enquete, "marcada: sim ou não" |
| qui 12/11 e qui 19/11 18h00 | ok da Mirna ao tl04 e ao tl05 |

### 2.22 Etiquetas

Todo número deste arquivo tem [FATO] com fonte, [ESTIMATIVA] com a conta, [HIPÓTESE] ou [PRIOR]. O que falta está escrito "sem dado". Correções que este plano acrescenta ao enquadramento:
- A meta do D4 de "6 respostas de story a cada 14 dias (2x a base de 3 em 7 dias)" é a **mesma taxa da base**, não o dobro: 3 em 7 dias são 6 em 14 dias [ESTIMATIVA, conta sobre o fato 56]. O dobro seria 12 em 14 dias.
- O render final dos ob existe (C2).
- O pedido dos ob mudou de direct para comentário (C4).

---

## 3. Decisões

### D1. Série da entrevista em torno de 02/11

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) Manter os 5 nas datas | S1 com 6 reels, contra o CLAUDE.md; ci01 com voz e rosto da Mirna antes da exibição só com ok verbal | S2 vazia; um pedido de remoção, se vier, atinge 5 reels de uma vez |
| (b) Mover os 5 para depois | Exposição mínima da Mirna antes de 02/11 | S1 sem estoque com rosto (nenhuma gravação desde 21/10, fato 104): vagas vazias; o pb01, com legenda pronta, espera à toa |
| **(c) Dividir** | S1 em 4 ou 5 reels; ci01 e po01 depois | o maior trecho de voz e rosto da Mirna sai no dia do trabalho dela; o portão de 02/11 lê a dupla PB com n de 2 |
| (d) Não mexer agora | pb01 sai; decisão em 26/10 21h05 | S1 com 6 reels até alguém mover; o ci01 sai qua 28/10 sem decisão escrita se o Bruno não executar |
| (e) **Fora do óbvio: pré-autorização em bloco** | o Bruno manda à Mirna, numa mensagem, a lista das 10 peças com data e pede ok por escrito; o que vier sem ok vai para depois de 02/11 | o print vira autorização com escopo (peça e data), a prova que a LGPD pede; abre a porta para a emissora não estranhar ou até repostar; risco: a produção responder "só depois", e aí tudo vira (b) |

- **Posição:** (c), executada com o passo (e) como pergunta, não como trava do pb01.
- **Premissas:** a liberação verbal é verdadeira e cobre posts antes de 02/11; o Bruno edita e move no prazo; nenhuma peça usa a edição exibida; o app deixa marcar depois ou o @ na legenda basta.
- **Probabilidade pelo critério do enquadramento** (os 3 números juntos, mais as regras de cópia, promessa e marcação): **0,15 [0,05; 0,30]**, confiança **0,35**. Motivo: visitas de 21 por dia (2x a base) e saldo positivo de seguidores dependem de um efeito da TV sem dado; a base de seguidores de 12 a 21/10 é -5 (fato 17). Sub-critério desta cadeira (zero pedido de remoção, zero "foi ao ar" antes da hora, Mirna marcada em todas as peças com ela): 0,60 [0,40; 0,75].
- **Efeito de 2ª ordem que mais pesa:** se a produção pedir para segurar, a opção (c) perde 4 reels (pb01, car01, pb02, tl02) de uma vez; o plano B é a ordem sem gravação da seção 2.13.

### D2. Nicho com gravação, mínimo semanal, Dentista C e remakes

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| **(a) 1 bloco semanal de 24 a 36 min com 2 roteiros, só com a norma do nicho lida** | 2 reels de nicho por semana a partir da S2 | a leitura da norma pode atrasar o roteiro; protege o Bruno de ensinar o que o conselho do cliente pune |
| (b) Sessão de 60 a 90 min com 5 roteiros | mais estoque | 5 normas para ler antes; o plano de 21/10 já previa isso e não aconteceu (fato 105) |
| (c) Sessão quinzenal com 10 roteiros | menos sessões | uma falha deixa 2 semanas sem nicho; a conferência de 11/11 fica com n abaixo de 3 |
| (d) Zero gravação | grade fecha com estoque de perfil | nicho fica "não testado" em 11/11; o formato que mediu 167,5 (Bruno de frente) só volta pelos remakes |
| (e) **Fora do óbvio: gravação mínima de conformidade** | 1 roteiro por semana (o que tiver norma lida) mais 1 tomada do gancho sem número | de 12 a 18 min por semana [ESTIMATIVA F5]; nenhuma frase com número que pede documento |

- **Posição:** (a); se o Bruno avisar que não chega a 24 min, (e). Dentista C fora do feed (anúncio depois de 18/11 com condições). Remakes como Trial Reel às terças. Tzur fora da janela.
- **Premissas:** o Bruno grava até qua 28/10; a agência lê as normas a tempo; o motor monta em 1 dia.
- **Probabilidade pelo critério** (2 nicho por semana, mediana de 53 ou mais e pulo até 75% em 11/11 com n de 3 ou mais, 1 nicho com 106 até 23/11, zero sintético): **0,25 [0,10; 0,45]**, confiança **0,40**. Motivo: nenhuma gravação nova desde 21/10 (fato 104) e a sessão de 26/10 do plano anterior não aconteceu.

### D3. Grade e operação

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| **(a) 5 reels e 2 carrosséis, com S1 em 4 ou 5** | cumpre o CLAUDE.md | 8 vagas de dia útil em S3 e S4 dependem de nicho ou estoque |
| (b) 6 na S1 pela promessa | a promessa não pede mais (fato 77) | quebra o CLAUDE.md sem motivo |
| (c) 6 a 7 por semana como TESTAR | mais chance de estouro (7,7% contra 7,0%, fato 152) | contra a regra medida de 21/10 (3 posts por dia não trouxeram seguidores) |
| (d) 3 reels e 2 carrosséis em semana sem gravação | menos carga | menos amostra para o portão |
| (e) **Fora do óbvio: 4 reels e 2 carrosséis, com o 5º como Trial Reel** | o seguidor vê 4 reels; o 5º vai a não seguidor | mede remake sem gastar seguidor; depende de elegibilidade (sem dado) |

- **Posição:** (a), com o Trial Reel da terça fora da conta e escrito como TESTAR.
- **Premissas:** o Bruno faz a lista à mão (cerca de 20 stories à mão por semana, mais marcações); a agência entrega 6 carrosséis no prazo.
- **Probabilidade pelo critério** (0 vaga vazia, 0 dia com 2 reels, mediana semanal de 42 ou mais nas 4 semanas e de 106 ou mais em 2, ganho líquido de 12 em 14 dias depois de 27/10): **0,15 [0,05; 0,30]**, confiança **0,40**. A parte que este plano controla (0 dia com 2 reels, máximo de 5) tem 0,85.

### D4. Stories e ob01 a ob03

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 03-plano estendido (8 por dia, 27 à mão) | volume | carga à mão acima do que o Bruno mostrou fazer; ETAPAS em 2 stories contra a regra de uma palavra |
| (b) 3 a 5 por dia | menos carga | story é 54,6% das views de 7 dias (derivar 15): perde o maior bloco de views |
| **(c) 6 a 8 em 4 blocos (F6)** | mantém volume com 20 à mão por semana | um pedido por dia; frase de efeito volta |
| (d) ob nas datas do 03-plano ou 1 por semana | ob02 cairia em 02/11, dia do ci01 | |
| (e) **Fora do óbvio: prova com número só com documento** | stories de número de caso só depois do documento; antes, autoridade por citação literal com tempo e por bastidor | protege o destaque fixo de uma afirmação sem documento (CDC art. 38) |

- **Posição:** (c) com o filtro (e). ob01 qui 05/11, ob03 sex 06/11 ou seg 09/11, ob02 qui 12/11 com condições.
- **Premissas:** o Bruno posta 3 stories à mão por dia útil; a agência renderiza os estáticos do banco.
- **Probabilidade pelo critério** (982 views de story ou mais por semana, 6 respostas ou mais a cada 14 dias, ob com média de 42 ou mais e pulo até 75%): **0,40 [0,25; 0,60]**, confiança **0,45**. As views já estão acima da base (1.041, fato 56) e a meta de respostas é a taxa atual (seção 2.22); o ob é a parte incerta.

### D5. Portão do Módulo 7

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| **(a) Régua de alcance sobre 53** | limites fixos 27, 42, 106, 150 | mais exigente que 37,5; menos DOBRAR falso |
| (b) Régua de views sobre 57 | casa com o ig_reel_checkup | mistura views e alcance com o resto do sistema |
| (c) Régua de 37,5 | base atual do Buzzfy | 42 vira 1,12x; mais peças passam |
| (d) Mediana móvel | acompanha a conta | quebra a comparação entre semanas |
| (e) **Fora do óbvio: régua 53 com linha de conformidade** | cada rodada lista as quebras de regra e trava DOBRAR em peça com quebra aberta | o portão passa a cobrar execução, que é o elo fraco medido (fato 125) |

- **Posição:** (a) com (e).
- **Premissas:** os agentes leem às segundas; o Bruno executa até terça 11h na semana da exibição e até a segunda seguinte nas outras.
- **Probabilidade pelo critério** (5 rodadas registradas, todas as decisões executadas até a segunda seguinte, nenhum PARAR com n de 1, mediana da S4 acima da S1): **0,30 [0,15; 0,50]**, confiança **0,45**. A execução total é o gargalo: em 21/10, 3 de 8 decisões não foram executadas (fato 125, correção 180).

### D6. TABULEIRO e o caminho até o diagnóstico

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) TABULEIRO em todo post de novembro com 150 | mais posts com a palavra | pode passar de 1 por semana, contra o 00-SISTEMA |
| (b) Um post por mês | leitura mais estrita | 1 chance só; teto de comentários já é baixo |
| **(c) (a) ou (b), mais desligar as outras 16 e um pedido por peça** | cumpre "uma palavra por mês" de fato | atribuição limpa; comentário de parabéns não vira DM de venda |
| (d) Não ligar em novembro até 1 disparo real e o caminho testado | zero risco de promessa não cumprida | zero dado em novembro |
| (e) **Fora do óbvio: TABULEIRO só como link de story em novembro** | uma palavra por mês é teto; zero cumpre | perde o direct com botão; ganha um pedido único e medido por GA4 |

- **Posição:** (c), ligada por post, no máximo 1 por semana, depois do teste ponta a ponta do Bruno até dom 01/11.
- **Premissas:** o Bruno desliga as automações; algum reel passa de 150 em 48 h; o texto do direct fica genérico.
- **Probabilidade pelo critério** (3 disparos de terceiros até 22/11 e 1 diagnóstico agendado até 18/11): **0,10 [0,03; 0,25]**, confiança **0,50**. Teto de 3,7 a 5,5 comentários de qualquer tipo (derivar 13); base de disparo real: 0.

---

## 4. Ideias e hipóteses numeradas (90)

1. Desligar as 16 automações que não são TABULEIRO até dom 25/10 18h00. Alta. Fatos 114 e 168.
2. Se só der tempo para duas, CASE e ESTRATEGISTA primeiro. Alta. Fato 114; legendas de pb02 e ob02 (C1, C4).
3. Print da Mirna até seg 26/10 20h, guardado com data. Alta. LGPD art. 8º §2º (nível 3); fato 4.
4. Mensagem única à Mirna com 7 perguntas. Alta. F4 seção 6.4; itens 1 a 6 de "a buscar".
5. Publicar antes de 02/11 sem esperar o print. Média. Voz do cliente; R1 abaixo de 1% [PRIOR].
6. ci01 só volta a 28/10 com hot streak e print. Alta. Fato 90.
7. Efeito sobre o rosto da Mirna só com ok depois de ela ver. Alta. Política editorial da emissora (27/05/2026); fato 90.
8. Sem ok, versão sem o efeito ou banco, nunca story. Média. Custo de render sem dado.
9. Colaboração só no ci01 e com ok. Alta. Esquema PostZen (fato 139); F4.
10. Não convidar a emissora como colaboradora. Média. Termos vetam uso comercial.
11. "Está na edição de 02/11" até o horário ter fonte. Alta. 02-provas, vetos.
12. "Foi ao ar" com horário confirmado e passado, ou edição publicada. Alta. 02-provas; site da TV.
13. Link da edição sim; recorte nunca. Alta. Termos §2 e §3.
14. Nenhuma peça da entrevista em anúncio sem autorização escrita da Mirna e posição da emissora. Alta. Termos §3.
15. Nenhum "visto na TV" em anúncio pago sem autorização. Média. Termos §3.
16. Frase do caso em toda peça com número. Alta. 02-provas.
17. Cartão PZ às 16h01 depois do pf01. Alta. C5.
18. tl01 e tl02 com a frase do caso e "minutos da gravação". Alta. C1; fato 81.
19. Documento dos casos do restaurante e da franquia até sex 30/10. Média. CDC art. 38 (nível 3); 02-provas.
20. Sem documento, número fora de destaque, carrossel e ob02. Média. Idem.
21. po01 com "Comenta qual delas". Alta. C1.
22. car01 com um pedido só. Média. C1; regra de um pedido por peça.
23. S1 em 4 ou 5 reels. Alta. CLAUDE.md; fato 76.
24. Vaga de qui 29/10: nicho, R2, po01, nessa ordem. Média. F4; F5.
25. Trial Reel fora dos 5, dentro da regra de 1 por dia, escrito como TESTAR. Média. Hipótese 32; fato 171.
26. Trial Reel só às terças 14h. Alta. Derivar 9; grade sem reel na terça.
27. Remake com 2 mudanças reais e sem a promessa da saga. Alta. Fatos 37 e 150.
28. Elegibilidade de Trial testada no R1. Média. Fato 139.
29. Dentista C fora do feed; anúncio depois de 18/11 com CFO e licença da trilha. Alta. Fato 101; brief.
30. Tzur fora da janela. Alta. Fato 102; 02-provas proíbe o nome do cliente nesta série.
31. Nicho só depois da norma lida. Alta. Fato 103.
32. Consórcio sem a linha de 41,9% da ABAC até a fonte ser lida. Alta. Fato 103.
33. Nutricionista sem resultado de paciente, antes e depois ou exame. Alta. Plano de 21/10 sobre a CFN 856; vigência sem dado.
34. Advogado só depois do provimento da OAB lido. Alta. Fato 103; [PRIOR] Provimento 205/2021.
35. Psicólogo só depois da norma do CFP lida. Alta. Sem dado.
36. O7 com texto oficial e "confira com o seu conselho". Alta. F6 seção 9.3.
37. O10 só com cliente, ano e papel confirmados. Alta. F6; 02-provas.
38. O15 só enquete. Alta. F6 (sem prova).
39. O6 sem preço sem confirmação do Bruno. Média. F6.
40. Nada de voz sintética. Alta. CLAUDE.md; política de rótulo de IA da Meta.
41. Não repostar os 12 sintéticos. Média. Rótulo dos antigos sem dado.
42. Guardar a licença Mixkit com data por trilha. Média. C7; nível 3.
43. Reel silenciado: contestar com a licença antes de refazer. Média. [PRIOR].
44. Política de privacidade cita o GA4 ou o GTM sai. Alta. C8.
45. Link da política na página de material. Média. C9.
46. Corrigir antes da semana da TV. Média. Hipótese 45 (quem vem da TV entra pela bio).
47. Follow-up de WhatsApp só a quem iniciou; lista só com aceite. Média. Política do site; C9.
48. Apagar o rascunho de release com o original da entrevista; arquivo no Drive restrito. Alta. Fato 111.
49. Bio do Módulo 2 sem emoji e com /tabuleiro/?o=ig-bio. Média. Fatos 9 e 132.
50. Marcar a Mirna só onde ela aparece. Alta. F4; [PRIOR] marcação fora do conteúdo vira ruído.
51. Marcar até 30 min depois de publicar e anotar. Média. F4.
52. Sem marcação depois, @ no texto da legenda antes. Média. Central de ajuda (nível 3).
53. Três menções em story, não mais. Média. F4 seção 6.3.
54. Menção não vai em story agendado. Alta. Fato 66.
55. Destaque NA TV só depois de 03/11, sem logo, sem "vai ao ar", com ok de uso fixo. Alta. F6 seção 8.
56. Nenhuma marca de terceiro em estático ou interface. Alta. CLAUDE.md.
57. Marca de fabricante no monitor do ci01 não pede render. Média. C10; compensação do ponto cego.
58. Finados com tom sóbrio. Média. [PRIOR].
59. 20/11 sem uso comercial da data. Média. [PRIOR].
60. 25/10, 2º turno: nada político; leitura do tl01 com cautela. Média. Nível 3.
61. Portão do timelapse só com os dois critérios ruins. Alta. Catálogo; n de 1.
62. PARAR só com n de 2 ou mais. Alta. Enquadramento.
63. Régua 53 fixa nas 4 semanas. Alta. 00-SISTEMA; catálogo.
64. Linha de conformidade em cada rodada. Média. Ideia desta cadeira.
65. Rodada de 02/11 pelos agentes às 19h; execução até ter 11h. Média. F7.
66. Saldo de seguidores até 08/11 só fecha em 11/11. Alta. Derivar 5.
67. Meta de respostas do D4 é a taxa atual, não o dobro. Alta. Fato 56.
68. Leitura parcial de diagnóstico em 04/11. Alta. Fato 181.
69. Piso de seguidores: 12 em 14 dias depois de 27/10, fecha em 13/11. Alta. Fato 182; derivar 5.
70. TABULEIRO por post, nunca de conta toda. Média. CLAUDE.md.
71. No máximo 1 post TABULEIRO por semana. Alta. Fato 171.
72. Direct da TABULEIRO genérico e alinhado aos 5 Lances. Média. Fato 117.
73. "Diagnóstico" só para o teste; "Primeiro Lance" para a conversa. Média. Fato 131.
74. Teste ponta a ponta do Bruno até dom 01/11. Média. Fato 116.
75. Excluir perfis do Bruno da contagem. Alta. Fato 116.
76. Ligar o linkTracking para contar o toque no botão. Média. Hipótese 51.
77. Nenhuma palavra em 02/11. Alta. F8.
78. ob02 nunca no mesmo mês que o pf01 como reel. Média. Derivar 23; página de originalidade do Instagram.
79. ob01 só depois de ouvir 1312,5 a 1326,4 s. Alta. Fato 98.
80. Atribuição do "Ainda. Sempre vai ser." conferida antes do ci01. Alta. Fato 91.
81. Conferir a caixa vazia do tl05. Baixa. C11.
82. tl02: correção dos 10,4 s ou aceite escrito. Média. Fato 92.
83. mc04 com o render atual, que termina em "família,". Alta. C6.
84. Arquivo do pf01 confirmado antes de ter 27/10 15h. Média. Fato 85; C5.
85. S2 agendada até sex 30/10. Média. Prazo do D3.
86. Story com número de caso fora do destaque sem documento. Média. 02-provas.
87. Promessa do tl01 cumprida até sex 13/11; com menos de 5 votos, dizer em story. Alta. Fato 77; catálogo.
88. Carrossel com foto do Bruno na capa. Alta. Fato 51.
89. car02 sem material da TV antes de 02/11. Média. Reduz exposição antes da exibição.
90. Estoque copiado para o Drive. Alta. Fato 110.

---

## 5. Pre-mortem: como este plano fracassa

1. **Condição demais.** O plano tem perto de 15 condições. O Bruno executa metade, as vagas ficam vazias e a conta passa novembro com 3 reels por semana. É o meu ponto cego: nenhuma multa, nenhum alcance.
2. **O print não chega e a produção pede para segurar em 30/10.** Eu deixei publicar antes; 4 reels saem do ar e a S1 fica com o tl01.
3. **As automações seguem ligadas.** Um "parabéns, estrategista!" no ci01 dispara a ESTRATEGISTA em 02/11 e a Mirna ou um colega da TV recebe um direct de venda.
4. **Áudio silenciado no ci01 às 21h de 02/11.** A trilha "deep-urban" é reivindicada e o reel mais importante sai mudo.
5. **Copy neutra demais.** "Está na edição de 02/11" sem horário faz ninguém assistir; a semana da TV não muda as visitas.
6. **Trial Reel não liberado.** Os remakes ficam parados e o formato de frente para a câmera não volta.
7. **Bruno indisponível no feriado.** Nenhum story à mão em 02/11; a chamada com horário não sai.
8. **Zero gravação.** As travas de norma por nicho viram irrelevantes; S3 e S4 fecham com cortes de perfil e a mediana fica perto de 32,5.
9. **Efeito no rosto recusado e sem tempo de render.** tl04 e tl05 caem; dois sábados vazios.
10. **Documento dos casos nunca chega.** ob02 e as provas com número não saem; a linha de autoridade fica só com citação.

---

## 6. Previsões numéricas com data de conferência

D = 24/10/2026. D+30 = seg 23/11/2026; D+60 = qua 23/12/2026; D+90 = sex 22/01/2027.

| # | Métrica | Valor previsto | Conferência |
|---|---|---|---|
| P1 | Incidentes externos (strike, remoção pelo Instagram, notificação da TV, da Mirna, de Procon, ANPD ou CONAR) | 0 (probabilidade 0,93 [PRIOR]) | 23/11/2026 |
| P2 | Reels com áudio silenciado ou aviso de direito autoral | 0 (0,88 [PRIOR]) | 23/11/2026 |
| P3 | Automações de comentário ativas na conta | 1 a 2 (probabilidade de o Bruno desligar até 26/10: 0,55 [PRIOR]) | 23/11/2026 |
| P4 | Peças publicadas de 25/10 a 22/11 com quebra de regra do cliente | 0 a 3, ponto 1 | 23/11/2026 |
| P5 | Semanas com mais de 5 reels de feed | 0 de 4 (0,80) | 23/11/2026 |
| P6 | Mediana de alcance em 48 h dos reels da série da TV publicados até 21/11 | 35 a 120, ponto 60 [PRIOR] | 23/11/2026 |
| P7 | Disparos de TABULEIRO de terceiros até 22/11 | 0 a 3, ponto 1 | 23/11/2026 |
| P8 | Seguidores | 1.600 a 1.690, ponto 1.635 [ESTIMATIVA: +40 em 30 dias até 11/10 e -5 em 12 a 21/10; efeito da TV sem dado] | 23/11/2026 |
| P9 | Views de story em 7 dias, lidas às 19h | 850 a 1.600, ponto 1.150 | 23/11/2026 |
| P10 | Política de privacidade do site citando o GA4 ou sem GTM | sim (0,70) | 23/12/2026 |
| P11 | Print da liberação da Mirna guardado | sim (0,80) | 23/12/2026 |
| P12 | Peça da entrevista em anúncio pago sem autorização escrita | nenhuma (0,90) | 22/01/2027 |
| P13 | Strikes no Status da conta | 0 (0,95 [PRIOR]) | 22/01/2027 |
| P14 | Diagnósticos (Primeiro Lance) agendados informados pelo Bruno até 18/11 | 0 a 2, ponto 0 [PRIOR] | 23/11/2026 |

---

## 7. O que mudaria minha opinião, lacunas e fontes

### 7.1 O que mudaria minha opinião

- A Mirna ou a produção dizer "só depois de 02/11": tudo com ela vai para depois (opção b do D1).
- O print vir com escopo que inclua destaque fixo, efeitos e anúncio: caem as travas correspondentes.
- O teste no tl01 mostrar que o app não marca depois: @ na legenda e publicação à mão de ci01 e po01.
- Um reel silenciado por trilha: o resto troca para a trilha própria sintetizada (som.py), sem licença de terceiro.
- Um comentário disparar CASE ou ESTRATEGISTA antes de o Bruno desligar: vira urgência do dia.
- Hot streak no tl01 ou no pb01 com print na mão: o ci01 volta a 28/10.
- Notícia de ação da ANPD, do Procon ou do CONAR contra perfil de consultoria pequeno: as correções de LGPD e de prova sobem para antes de 26/10.
- A licença do Mixkit lida na fonte com restrição a uso em perfil comercial: troca de trilha antes de 02/11.

### 7.2 Lacunas

- Horário da exibição de 02/11: sem dado.
- Se a liberação verbal da Mirna cobre posts antes de 02/11, destaque fixo, efeitos no rosto e anúncio: sem dado.
- @ da Mirna; se o app marca pessoa num reel publicado (só fonte de nível 3); se o @ na legenda pela API avisa a pessoa: [PRIOR].
- Se a gravação do celular conta como conteúdo da emissora nos termos: sem dado (não é parecer jurídico).
- Texto da licença do Mixkit lido na fonte: sem dado (só resumos de nível 3).
- Texto da LGPD e do CDC no Planalto: a página respondeu HTTP 503 às 16h05; os textos vieram de reproduções em busca (nível 3).
- Rótulo de IA nos 12 reels sintéticos antigos: sem dado.
- Documento dos casos do restaurante (45 mil para 250 mil) e da franquia (1,5 milhão em dois meses): sem dado.
- Status das leituras de OAB, CFN 856, ABAC, CFP e CFO: sem dado.
- Elegibilidade de Trial Reel: sem dado.
- Votos do tl01; comentários; directs; GA4; WhatsApp; diagnósticos: só o Bruno.
- Destino do formulário /api/lead e se alguém preencheu: sem dado.
- Disponibilidade do Bruno em 02/11, 15/11 e 20/11: sem dado.
- Alcance em feriado com reel do Bruno: sem dado.

### 7.3 Fontes

Do cliente (nível 1):
- `/home/user/Disparo-/CLAUDE.md`; `conteudo/modo-god-cronograma/contexto.md`; `run/00-enquadramento.md`; `run/01-fatos.md`; `run/01-pesquisa/F1` a `F8`; `conteudo/stories-objecoes/02-provas.md` (lista de vetos); `conteudo/modo-god-nichos/run/10-decision-brief.md`.
- PostZen `listPosts`, conta j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 03h00 UTC a 01/12 03h00 UTC, lido às 16h10 (19h10 UTC).
- Fichas `videos/tv-camara/cortes/*.spec.json`; renders em `/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/tv/render/` (stat, ffprobe e quadros às 16h03 a 16h06); `git log` de `videos/musicas` (commit 3f8204d).
- Site do cliente, GET às 16h07 e 16h09: estrategistadelancamento.com.br/politica-de-privacidade/, /v2/, /tabuleiro/; estrategista-materiais-videon8ns-projects.vercel.app/m/checklist?o=ig-checklist.

De terceiros (nível 2 e 3):
- TV Câmara Campinas, termos de uso (atualizados em 24/05/2026) e política editorial (27/05/2026): https://www.tvcamaracampinas.com.br/termos e https://www.tvcamaracampinas.com.br/politica-editorial (lidos às 16h04).
- Instagram, recomendações e originalidade (30/04/2024): https://creators.instagram.com/recommendations-and-Originality.
- Social Media Today, esclarecimento do Instagram sobre CTA de uma palavra (05/06/2024): https://www.socialmediatoday.com/news/instagram-clarifies-advice-single-word-ctas-longer-reels/718151/.
- Instagram, marcar pessoas num post já compartilhado (resumo de busca; a página não abriu o texto): https://help.instagram.com/instagram-lite-app/174635396025538.
- Collabs com até 5 colaboradores (guias de 2025 e 2026): https://socialk.it/pt/blog/instagram-collab-posts-guide e https://dealism.ai/pt/blog/how-to-collab-on-instagram.
- Meta, rótulo de conteúdo de IA: https://www.meta.com/en-gb/help/artificial-intelligence/1783222608822690/ (via resumo de busca).
- ANPD, primeira sanção à Telekall (06/07/2023): https://www.mobiletime.com.br/noticias/06/07/2023/anpd-aplica-sua-primeira-sancao-com-multa-a-telekall/ e https://teletime.com.br/06/07/2023/anpd-publica-primeira-sancao-ao-setor-privado-por-descumprimento-da-lgpd/.
- Súmula 403 do STJ: https://juris.damasio.com.br/sumulas/stj/403 e https://www.conjur.com.br/2009-out-29/imagem-publicada-autorizacao-indenizacao-sumula-stj/.
- CDC, art. 38: https://modeloinicial.com.br/lei/CDC/publicidade-@___I_V_III.
- LGPD, art. 8º §2º: https://modeloinicial.com.br/lei/LGPD/requisitos-o-tratamento-dados-pessoais-@____II_I (Planalto em 503).
- Mixkit, licença gratuita (resumos): https://mixkit.co/free-stock-music/ e https://kripeshadwani.com/mixkit-review/.
- 2º turno presidencial em 25/10/2026: https://viva.com.br/politica/quais-cargos-estao-em-disputa-no-segundo-turno-veja-ordem-de-votacao.html e https://www.dgabc.com.br/Noticia/4352671/estado-de-sp-comeca-a-preparar-mais-de-114-mil-urnas-para-o-2-turno.
