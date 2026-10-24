# Plano C · Cadeira do Executor · Cronograma 25/10 a 22/11/2026 · @o_estrategista.com.br

Conselho Agência Reunida Modo GOD. Sábado, 24/10/2026, escrito às 16h30 (horário de São Paulo). Trabalho isolado: esta cadeira não leu os planos das outras cadeiras.

| | |
|---|---|
| **Persona** | Gerente de operação que transforma estratégia em tarefa com dono, prazo e custo |
| **OTIMIZA PARA** | O que dá para fazer na segunda-feira |
| **PONTO CEGO (assumido)** | Subestimar a escolha estratégica. Um plano bem executado de um formato errado continua errado. Compensação na seção 2.3: cada escolha operacional vem com o motivo estratégico medido, e o plano reserva vaga para o único formato que a conta já provou (o Bruno falando de frente para a câmera, mediana de 167,5 de alcance contra 32,5 da animação [FATO, fato 25 e 27]) |
| **PERGUNTA CONTRÁRIA** | Se a capacidade real de quem executa for metade da prevista, o que sobra do plano? Resposta na seção 2.2, com números |

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, nível 4, que nunca fecha objeção sozinho. Métrica que falta: "sem dado". "fato N" remete ao livro `run/01-fatos.md`; "a buscar N" e "derivar N", às seções 2 e 3 dele; F1 a F8, às frentes de `run/01-pesquisa/`.

**Régua única do começo ao fim:** alcance em 48 h sobre a mediana de 53 (00-SISTEMA): 27 (0,5x), 42 (0,8x), 53 (1x), 106 (2x), 150 (palavra-chave). Pulo: abaixo de 60% para DOBRAR, acima de 75% para PARAR. Views e o "x" do Buzzfy entram só como coluna de referência.

**Regra de operação desta cadeira:** nada foi publicado, agendado, alterado ou enviado. Toda ação de PostZen abaixo é proposta para a agência executar na sessão principal depois do ok escrito do Bruno (como já foi feito hoje com a série da TV e com tl02 a tl05 [FATO, git log 36318ca às 13h22 e 318e97d às 14h41]) ou para o próprio Bruno.

### Conferências próprias desta cadeira (só leitura, 16h20 a 16h30)

| # | O que conferi | Resultado | Muda o quê |
|---|---|---|---|
| C1 | `date` do sistema | 19h23 UTC = 16h23 em São Paulo de sáb 24/10. Dias da semana conferidos de 24/10/2026 a 22/01/2027: dom 25/10, seg 26/10, ter 27/10, qua 28/10, qui 29/10, sex 30/10, sáb 31/10, dom 01/11, seg 02/11, ter 03/11, qua 04/11, qui 05/11, sex 06/11, sáb 07/11, dom 08/11, seg 09/11, ter 10/11, qua 11/11, qui 12/11, sex 13/11, sáb 14/11, dom 15/11, seg 16/11, ter 17/11, qua 18/11, qui 19/11, sex 20/11, sáb 21/11, dom 22/11, seg 23/11, qua 23/12, sex 22/01/2027 | Datas da grade e das previsões |
| C2 | `find` e `ffprobe` na pasta temporária da sessão | **ob01, ob02 e ob03 têm render final**: `tv/render/ob01.mp4` (15h48, 17,9 s), `ob02.mp4` (15h54, 28,37 s), `ob03.mp4` (15h58, 15,1 s), 1080x1920; versões leves em `tv/ig/` (15h55 a 15h58); folhas `ob01-folha.jpg` a `ob03-folha.jpg` existem. Nota de 0 a 10 por efeito: sem dado | Atualiza o fato 97 ("render final: sem dado"). Os ob deixam de ser condição e viram estoque da S2 |
| C3 | Quadros aos 0 e 2,5 s das versões leves de ob01 a ob03 | O Bruno aparece de perfil atrás do monitor nos 6 quadros, com o cartão "OBJEÇÃO · VOCÊ DIZ" no alto; em nenhum ele olha para a câmera; a Mirna não aparece nesses quadros; o braço azul na borda (fato 97) não aparece nesses dois instantes | Pergunta 12 |
| C4 | `videos/tv-camara/cortes/mc04.spec.json` (modificado no disco, fora do commit) e `ffprobe` | Trecho de 1700,967 a 1705,567 s (4,6 s), fim "no vale de energia" depois de "família," (vira "família."), manchete "Eu construí patrimônio, eu construí família."; render de 4,60 s às 15h35 | Pergunta 8: o recorte já está decidido e renderizado na faixa do 03-plano |
| C5 | `tv/rev_ob/conferir.txt` | Em 1196,0 a 1204,1 s a transcrição da voz tratada diz "lançamento de engolamento"; a ficha do ob02 força "lançamento de um produto" | Conferir a legenda queimada do ob02 antes de agendar |
| C6 | `git log` | 36318ca (13h22 SP) "Agenda a série da entrevista no PostZen"; 318e97d (14h41) "timelapses 2 a 5 agendados"; c6fb79c (15h23) "Chamada do Dentista B com SÁB · 21H no lugar de HOJE" | A agência já executa no PostZen depois do ok: é a mão que este plano usa para poupar a do Bruno |
| C7 | Conta sobre o fato 56 e o fato 57 | A meta do D4 ("6 respostas em 14 dias, 2x a base de 3 em 7 dias") está errada na conta: 3 em 7 dias já é 6 em 14 dias. A meta é 1x a base de 7 dias e 1,8x a base de 30 dias (7 em 30 dias = 3,3 em 14 dias) [ESTIMATIVA] | D4: a meta não pede melhora sobre a semana atual |

---

## 1. Veredito

1. O gargalo é a mão do Bruno, não o estoque. Em 21/10 ele executou 3 de 8 decisões do Módulo 7 e entregou 1 fala de 36 s em 3 dias para um plano de 90 min por semana [FATO, fato 125 e 104]. Este plano foi desenhado para metade dessa capacidade.
2. Série da TV: mexer em uma peça só. O ci01 sai de qua 28/10 e vai para **ter 03/11, 21h**. pb01, car01, po01 e pb02 ficam onde estão. A S1 fecha em 5 reels sem exceção escrita.
3. Seg 02/11 (Finados e exibição): sem reel. Chamada só nos stories; o Módulo 7 é lido pelos agentes às 19h e a lista do Bruno vence ter 03/11, 11h.
4. A semana da exibição (S2) fecha com peças que já existem: ci01, ob02, ob01 (ou nicho gravado), o "mais votado inteiro" e o tl03. ob01 a ob03 têm render desde 15h58 de hoje [conferência C2].
5. Tudo que não exige o celular do Bruno passa para a agência depois de um ok semanal: legendas, datas, @ da Mirna, convite de colaboração, automações e Trial Reel pela API.
6. Lista do Bruno: no máximo 7 itens por semana. Story à mão obrigatório: 1 por dia (o link do teste). O resto da pilha vai agendado.
7. Gravação: 1 bloco por semana com 2 roteiros (24 a 36 min [ESTIMATIVA, F5]); piso de 1 roteiro. Sem gravação, ordem fixa de estoque, e a grade cai para 3 reels; vaga nunca é preenchida com formato em PARAR.
8. Régua única: alcance em 48 h sobre 53; n de 2 por formato para PARAR; reel de feriado não fecha PARAR sozinho.
9. TABULEIRO: uma automação de conta toda, ligada só no post cujo anterior da mesma linha passou 150 com pulo abaixo de 60%; as 6 automações de conta toda saem antes do tl01; o link da bio vai para /tabuleiro/?o=ig-bio, já aprovado no Módulo 2.
10. Ponto cego assumido: sem gravação, as 4 semanas viram cortes de perfil, um formato com n de 0. O plano protege isso com 1 vaga por semana para o Bruno de frente (nicho gravado ou remake).
11. Pelos critérios do enquadramento, a chance de sucesso é baixa em todas as decisões (de 0,05 a 0,22). O que este plano aumenta é a chance de o que foi decidido sair do papel.
12. Primeira tarefa: hoje, antes das 21h, o Bruno manda 1 mensagem à Mirna e 1 ok à agência (seção 4.1).

---

## 2. Capacidade, pergunta contrária e ponto cego

### 2.1 O que se sabe da capacidade

| Medida | Valor | Fonte |
|---|---|---|
| Decisões do Módulo 7 de 21/10 executadas | 3 sim, 1 em parte, 3 não, 1 sem dado, em 8 (37,5% sim) | [FATO, fato 125; derivar 30] |
| Gravação desde o plano de 90 min por semana | 1 fala de 36,4 s em 21/10, em 576x1024; nenhuma outra até 15h15 de 24/10 | [FATO, fato 104] |
| Reel previsto que não saiu | "Fila é teto", qui 23/10, sem arquivo | [FATO, fato 105] |
| Carga do Bruno no plano das frentes | 170 a 327 min por semana, gravação entre 15% e 18% | [ESTIMATIVA com PRIOR, F5 seção 6] |
| Stories à mão por semana | 27 no 03-plano; 20 no molde da F6 | [FATO, fato 61; derivar 17] |
| Execução no PostZen pela agência depois do ok | já feita hoje 3 vezes (13h22, 14h41, 15h23) | [FATO, conferência C6] |

Leitura [HIPÓTESE]: o que trava não é a falta de peça, é o número de toques que o Bruno precisa dar. Cada toque que a agência pode dar no lugar dele sai da lista dele.

### 2.2 Pergunta contrária: com metade da capacidade, o que sobra

A base medida já é perto de metade (37,5% das decisões de 21/10 executadas). O plano tem 3 camadas, e a metade de baixo corta da camada 3 para a 1.

| Camada | O que é | Minutos do Bruno por semana | Se a capacidade cair pela metade |
|---|---|---|---|
| 1. Sai sem o Bruno | 16 itens já no PostZen (tl01 a tl05, pb01, car01, ci01, po01, pb02, pf01) [FATO, fato 74]; tudo que a agência renderiza e agenda depois de 1 ok por semana (ob01 a ob03, carrosséis, stories agendados, legendas, automações, Trial Reel pela API) | 10 a 15 (ler e responder o pacote) [PRIOR] | **Fica inteira.** É o plano mínimo |
| 2. Toque curto do Bruno | 1 story com link por dia (7); conversa com a Mirna (1 vez); link da bio (1 vez); contar votos do tl01 (1 vez); números de segunda (GA4, WhatsApp, diagnósticos) | 20 a 35 [PRIOR: 1 a 2 min por story; 10 min por conversa] | Fica a conversa com a Mirna e o link da bio; o link diário cai para 3 por semana (dias de reel com o Bruno de frente ou dias de objeção com mais respostas) |
| 3. Toque longo do Bruno | Gravação (24 a 36 min [ESTIMATIVA, F5]); compartilhar reel com menção (até 5); marcar a Mirna na mídia; caixa de pergunta; respostas a comentários e directs; Trial Reel pelo app se a API recusar | 45 a 90 [ESTIMATIVA com PRIOR] | Gravação cai para o piso (1 roteiro, 12 a 18 min [ESTIMATIVA, F5]); saem compartilhamentos, marcação na mídia (fica o @ na legenda), caixa e Trial pelo app (fica só o R1) |

**Conta da metade** [ESTIMATIVA com PRIOR]: o plano cheio pede de 75 a 140 min por semana do Bruno (camadas 1 a 3), contra 170 a 327 do plano das frentes. Na metade, sobram de 40 a 70 min: o ok semanal, a conversa com a Mirna, o link da bio, 3 links por semana e 1 roteiro.

**O que se perde na metade:**
- A linha de nicho chega a 11/11 com n de 2 a 3 (A, B e no máximo 1 roteiro novo): "não testado" na conferência, nunca PARAR.
- O feed das S3 e S4 fica com 3 reels por semana, quase todos cortes da TV com o Bruno de perfil; o Bruno de frente só volta pelos remakes em 720p.
- A medição de objeção cai para o total de respostas do `ig_account_stats` (sem enquete contada à mão).
- A TABULEIRO depende de algum post passar 150; a meta do D6 fica perto de zero.
- O "mais votado inteiro" e o link da edição seguem, porque são trabalho da agência.

**Regra de encolhimento automático** (para não depender de ninguém lembrar): se a linha "executado" da rodada do Módulo 7 ficar abaixo de 50% em 2 segundas seguidas, a semana seguinte já sai no modo metade, sem nova decisão: grade de 3 reels e 2 carrosséis, 3 links por semana, sem compartilhamento à mão.

### 2.3 Ponto cego assumido e compensação

**O que esta cadeira tende a errar:** escolher o que é fácil de executar (cortes da TV já renderizados, 6 min de agência cada [ESTIMATIVA, F5 seção 7]) e chamar isso de plano. O fácil aqui é um formato sem medida: o Bruno de perfil, numa conversa, olhando para a repórter [FATO, fato 88]. O formato medido é outro: o Bruno falando de frente para a câmera (4 de 4 em DOBRAR) [FATO, F7 seção 5.2].

**Compensação, escrita como regra:**
1. Toda semana de S2 a S4 reserva 1 vaga para o Bruno de frente (nicho gravado; se não houver, remake de R1 a R3 no feed com 2 ou mais mudanças reais). É a única vaga que a falta de estoque não fecha.
2. Teto de cortes da TV no feed a partir da S3: 3 por semana quando houver peça com o Bruno de frente pronta.
3. O portão de 02/11 lê a família "corte da TV" com n de 3 (pb01, po01, pb02). Se ela cair em PARAR, os cortes saem do feed mesmo com estoque pronto e o "mais votado" vira story com link.
4. A TV é tratada como prova de longo prazo (bio, destaque, objeções O1 e O14) e não só como estoque de reels de 4 semanas: o banco de cortes não precisa acabar em novembro.

---

## 3. Grade dia a dia e hora a hora (25/10 a 22/11)

### 3.1 Moldes de stories

"PZ" = agendado no PostZen pela agência depois do ok (sem sticker). "MÃO" = postado pelo Bruno no app (sticker na zona livre, y de 1300 a 1560 [FATO, fato 174]). Story agendado não leva sticker [FATO, fato 66].

**Molde U · dia útil com reel às 21h (8 stories, 1 à mão obrigatório, 1 opcional)**

| Hora | Tipo pedido | O que vai | Sobe por |
|---|---|---|---|
| 09h00 | Autoridade do Bruno, bastidor | Bruno em cena (mc, trecho de 5 a 15 s da gravação do celular, foto e1 ou e2). S1: rótulo "NA TV · SEG, 02/11" e sub "FALTAM N DIAS" quando o 1º story for estático. De 03/11 em diante: "O QUE EU DISSE NA TV" ou prova do 02-provas com o tempo da transcrição | PZ |
| 12h00 | Quebra de objeção | "O QUE EU MAIS OUÇO" com a frase do cliente e a linha "Isso é você? Responde SIM ou NÃO." | PZ |
| 12h01 | Virada | Contra-argumento do 01-objecoes | PZ |
| 12h02 | Prova de autoridade | Item do 02-provas com tempo da transcrição | PZ |
| 12h03 | Pedido único | "Em 4 minutos você vê em qual casa o seu lançamento trava." + link `/tabuleiro/?o=ig-stories` (com `&p=profissão` em dia de nicho) | **MÃO, obrigatório** |
| 17h30 | Frase de efeito | Banco da F6 (14 frases com fonte) | PZ |
| 20h30 | Chamada | Dia e hora no texto ("QUI · 21H · NO FEED"), nunca "hoje" | PZ |
| 21h05 | Compartilhar o reel | Post do dia | MÃO, opcional (camada 3) |

**Molde S · sábado e domingo com reel às 18h30:** igual ao U, com frase às 16h00, chamada às 17h30 e compartilhamento às 18h35.
**Molde L · dia sem reel:** sem chamada e sem compartilhamento (6 stories, 1 à mão).
**Molde F · feriado de 15/11 e 20/11:** só PZ; o link do dia vai escrito no texto, sem sticker [HIPÓTESE: o Bruno não posta à mão em feriado; alcance em feriado sem dado].
**Molde TV · seg 02/11:** seção 3.2, linha de 02/11.

Por que a objeção pede resposta e não enquete [HIPÓTESE, ideia 54]: o voto de enquete só se lê à mão no app, antes de expirar [FATO, fato 67], e a métrica do D4 é resposta de story, que o Buzzfy lê por story e por semana [FATO, fato 56 e tabela da F4 com respostas por story]. A resposta também abre conversa no direct, que é a porta da conversa de 30 min. Custo: responder dá mais trabalho que votar, então o número de respostas por story deve ser menor que o de votos [HIPÓTESE]. Se o Bruno tiver capacidade sobrando na S1 (linha "feito" acima de 80%), a enquete volta como MÃO na S3.

### 3.2 Tabela dia a dia

Feed com hora, peça e quem sobe. Plano A = com gravação; Plano Z = sem gravação. Objeções pelo mapa da F6 (seção 9.3); frases pelo banco da F6 (seção 6, números do banco).

| Data | Feed | Stories (o que muda no molde) | Mão do Bruno | Leitura e prazo |
|---|---|---|---|---|
| **sáb 24/10** (hoje) | 21h00 Dentista B, TABULEIRO (PZ, já agendado) | 16h30 a 20h30 já agendados | Apagar a chamada das 20h30 depois das 21h (1 min); mandar a mensagem à Mirna e o ok do pacote 1 (seção 4.1) | Agentes leem a pilha de hoje antes de dom 09h33 (a buscar 9) |
| **dom 25/10** | 18h30 **tl01** (PZ, fica; @ da Mirna na legenda se chegar até 17h) | Molde S. 09h00 mc02 (rótulo NA TV · SEG, 02/11); objeção O1; frase 1 ("Lançamento é xadrez. A maioria joga dama."); 17h30 chamada DOM · 18H30 · NO FEED | 12h03 link; 18h35 compartilhar o tl01 com **menção à Mirna (1 de 3)** e testar se o app deixa marcar pessoa no reel publicado (anotar sim ou não) | Até 09h: ETAPAS de story desligada; até 18h30: 5 automações de conta toda desligadas (pacote 1); 21h Dentista B com 24 h |
| **seg 26/10** | 21h00 **pb01** (PZ, fica; legenda com a data e o @) | Molde U. 09h00 mc03 + FALTAM 7 DIAS; O2; frase 2 ("O lead que não comprou vale mais do que o que comprou.") | 12h03 link; ok do pacote S1 até 18h | **21h05 portão extra**: Dentista B com 48 h (status da linha de nicho; TABULEIRO para o próximo do mesmo formato se fizer 150) |
| **ter 27/10** | 12h00 **car01** (PZ, fica; legenda com 1 pedido) | Molde L. 09h00 FALTAM 6 DIAS; O8; 12h03 com `&p=dentista`; 16h00 pf01 (PZ, já agendado; conferir qual arquivo vale, fato 85); frase 6 | 12h03 link | **18h35 portão extra**: tl01 com 48 h decide o tl02 (seção 5, pergunta 7). 21h: pb01 com 24 h (171 views ou mais sobe o pb02 para qua 28/10). Até 23h59: agência muda o ci01 para ter 03/11 |
| **qua 28/10** | 12h00 **car02 "Os 5 Lances"** (NOVO, PZ, capa com foto do Bruno). 21h sem reel (o ci01 saiu) | Molde L. 09h00 FALTAM 5 DIAS; O3; frase 9 (literal da TV, C5) | 12h03 link. **Bloco 1 de gravação até 23h59** | 21h: pb01 com 48 h (TABULEIRO no pb02 se passar 150 com pulo abaixo de 60%) |
| **qui 29/10** | 21h00 **po01** (PZ, fica; legenda "Comenta qual delas.") | Molde U. 09h00 FALTAM 4 DIAS; O4 (o sub "Quinta, 21h, eu explico no feed" do 03-plano continua certo); frase 10 (literal, M5) | 12h03 link | Agência: corte do trecho sem voz do tl02 (se o portão o manteve) até 23h59 |
| **sex 30/10** | 21h00 **pb02** (PZ, fica) | Molde U. 09h00 FALTAM 3 DIAS; O6; frase 8 (literal, M3) | 12h03 link; **link da bio para /tabuleiro/?o=ig-bio** | Pacote S2 entregue ao Bruno até 12h; cancelamento do tl02 (se for o caso) até 23h59 |
| **sáb 31/10** | 18h30 **tl02** (PZ, com portão) | Molde S. 09h00 FALTAM 2 DIAS; O5; frase 12 | 12h03 link; ok do pacote S2 até 12h | |
| **dom 01/11** | 11h00 **R1 como Trial Reel** (PZ com `trialParams`; fora da contagem). 12h00 **car03** (CARROSSEL 02 da TV, quiz; última lâmina "SEG, 02/11") | Molde L. 09h00 **mc04** (4,6 s, conferência C4) + FALTA 1 DIA; O12; frase 13 | 12h03 link. Contagem com sticker só se o horário estiver confirmado | 23h: agentes leem a pilha de domingo (F6 seção 11). R1: se a API recusar, o Bruno posta pelo app (camada 3) |
| **seg 02/11** (Finados, exibição) | Sem reel. Sem carrossel | **Molde TV.** 08h00 agentes leem /programacao/2026-11-02. 09h00 estático "SEG · 02/11 · NA TV CÂMARA CAMPINAS / Programa Ser Empreendedor, com a repórter Mirna Abreu / Canal 11.3 aberto, NET 4, Vivo Fibra 9 e tvcamaracampinas.com.br" (PZ). Se a grade sair até 08h30: estático com o horário às 10h00 (PZ, ok antecipado no pacote S2). 17h30 frase 14 (literal, M11). 20h30 "Chegou aqui pela TV Câmara? Responde este story com a sua área." (PZ). Sem bloco de objeção | Com horário confirmado: story com a hora, **menção à Mirna (2 de 3)** e link `/ao-vivo` ("Assistir na TV Câmara"). Se às 12h o horário seguir sem dado: story "A partir de hoje, 02/11, na TV Câmara Campinas." com link `/programacao`. 12h03 link do teste com `o=ig-tv`. Contar os votos do tl01 até 12h | 18h30 tl02 com 48 h; **19h Módulo 7 pelos agentes** (S1 inteira); lista do Bruno vence ter 03/11 11h |
| **ter 03/11** | 11h00 R2 Trial (só se o R1 saiu pela API). 12h00 **car04** (CARROSSEL 03 da TV, "O que eu disse na TV", tema mais votado). 21h00 **ci01** (PZ, movido; legenda nova; convite de colaboração se houver @ e ok; abertura corrigida) | Molde U. 09h00 "O QUE EU DISSE NA TV"; O14; frase 7; story do resultado da votação do tl01 (PZ, texto) | 12h03 link; 21h05 compartilhar o ci01 com **menção à Mirna (3 de 3)**; link da edição quando ela aparecer no site | Agentes conferem a página do programa de 02 a 06/11 |
| **qua 04/11** | 21h00 **ob02** (PZ; "Nunca ouvi falar de você"; legenda conferida, C5) | Molde U. O9; frase 11 (literal, M9) | 12h03 link | **Bloco 2 de gravação até 23h59** |
| **qui 05/11** | 11h00 R3 Trial (só se o R1 saiu pela API). 21h00 A: **nicho consórcio** (bloco 1) / Z: **ob01** | Molde U. O11; frase do nicho do dia ou rodízio | 12h03 link (`&p=consorcio` no Plano A) | 21h: ci01 com 48 h |
| **sex 06/11** | 21h00 **"mais votado inteiro"** (com 1 voto ou mais); com 0 voto: A nutricionista / Z ob03 | Molde U. O13 | 12h03 link | Cancelamento do tl03 (se o portão de 02/11 mandou) até 23h59 |
| **sáb 07/11** | 18h30 **tl03** (PZ, portão de 02/11; TABULEIRO se o tl02 fez 150 com pulo abaixo de 60%) | Molde S. Caixa de pergunta no lugar da objeção (MÃO, camada 3) | 12h03 link | |
| **dom 08/11** | 12h00 **car05** "Seguidor x comprador" (versão nova, capa com foto) | Molde L. O15 só como pergunta (sem virada: prova fraca, F6) | 12h03 link | |
| **seg 09/11** | 21h00 A: nicho nutricionista / Z: R1 no feed se o Trial fez 53 ou mais com pulo abaixo de 60%; senão ob01 ou ob03 (o que sobrou) | Molde U. Rodízio de objeções | 12h03 link; números da segunda | **19h Módulo 7** (S2; tl03 com 48h30); leitura parcial de seguidores |
| **ter 10/11** | 12h00 **car06** (CARROSSEL 04 da TV) | Molde L. O7 só depois da conferência das regras dos conselhos; senão rodízio | 12h03 link | Agência agenda o que o portão aprovou até 11h |
| **qua 11/11** | 21h00 A: psicólogo (bloco 2) / Z: **vaga do Bruno de frente**: R1 no feed como nova versão (3 mudanças) | Molde U. O10 só se o Bruno confirmar cliente, ano e papel | 12h03 link | **Conferência de nicho** (brief de 21/10), 21h; saldo de seguidores até 08/11 fecha hoje (derivar 5) |
| **qui 12/11** | 21h00 A: ob que sobrou / Z: corte do banco (pb03) só se a família TV não estiver em PARAR; senão fechado | Molde U. Objeção com mais respostas na S1 | 12h03 link | |
| **sex 13/11** | 21h00 A: advogado (só com o provimento da OAB lido) ou consórcio 6 / Z: R2 no feed se o Trial passou; senão fechado | Molde U. 2ª objeção com mais respostas | 12h03 link. **Bloco 3 até 23h59** | Seguidores de 28/10 a 10/11 fecham hoje (derivar 5) |
| **sáb 14/11** | 18h30 **tl04** (portão de 09/11; a Mirna viu o "Uau!" antes) | Molde S. Caixa | 12h03 link | |
| **dom 15/11** (Proclamação) | 12h00 **car07** "Oferta em 5 pilares" (capa com foto) | **Molde F** (só PZ) | nada | Reel de feriado não existe nesse dia |
| **seg 16/11** | 21h00 A: nicho do bloco 3 / Z: vaga do Bruno de frente (R2 ou R3 como nova versão) | Molde U. Rodízio | 12h03 link; números da segunda | **19h Módulo 7** (S3) |
| **ter 17/11** | 12h00 **car08** "Carrinho" (capa com foto) | Molde L | 12h03 link | |
| **qua 18/11** | 21h00 A: 2º nicho do bloco 3 / Z: corte do banco ou fechado | Molde U | 12h03 link; **número de diagnósticos agendados** | **Conferência de seguidores e diagnóstico** (brief de 21/10). **Bloco 4 até 23h59** |
| **qui 19/11** | 21h00 A: reel do Bruno de frente fora de nicho (Módulo 3) / Z: fechado | Molde U | 12h03 link | |
| **sex 20/11** (Consciência Negra) | 21h00 A: ob ou remake / Z: fechado | **Molde F**, mais a chamada das 20h30 se houver reel | nada | Reel de feriado não fecha PARAR sozinho |
| **sáb 21/11** | 18h30 **tl05** (portão de 16/11; a Mirna viu o "AINDA?" antes) | Molde S | 12h03 link | |
| **dom 22/11** | 12h00 car09 "Resumo do mês" só com o portão de 16/11; 6º reel não existe (abre a S5) | Molde L | 12h03 link | **seg 23/11 19h Módulo 7** (S4, decide a S5) |

### 3.3 Contagem por semana

| Semana | Reels (Plano A) | Reels (Plano Z) | Carrosséis | Dia com 2 posts de feed | Trial Reel (fora da contagem) |
|---|---|---|---|---|---|
| S1, 25 a 31/10 | 5: tl01, pb01, po01, pb02, tl02 (4 se o portão tirar o tl02) | igual | 2: car01, car02 | nenhum | nenhum |
| S2, 01 a 07/11 | 5: ci01, ob02, consórcio, mais votado, tl03 | 5: ci01, ob02, ob01, mais votado (ou ob03), tl03 | 2: car03, car04 | ter 03/11 (car04 12h e ci01 21h) | R1, e R2 e R3 se a API aceitar |
| S3, 08 a 14/11 | 5 | 3 a 5 (cai se a família TV parar) | 2: car05, car06 | nenhum | |
| S4, 15 a 21/11 | 5 | 2 a 4 | 2: car07, car08 | nenhum | |

Distância entre reels, Trial incluído: menor intervalo de 10 h (Trial às 11h e reel às 21h no mesmo dia) [ESTIMATIVA, conta de horas]; nenhum abaixo de 6 h (playbook mede 0,92x abaixo de 6 h [FATO, fato 152]).

---

## 4. Lista de execução (dono, prazo, custo)

### 4.1 Lista do Bruno (máximo 7 itens por semana; o resto é opcional)

Minutos marcados [PRIOR] quando não medidos. Cada item ganha "feito" ou "não feito" no arquivo da semana.

**Hoje, sáb 24/10, até 21h (2 toques):**
1. Mensagem à Mirna, uma só, com 5 perguntas: o @ dela; o horário de 02/11; o print da liberação; se a produção está ok com posts antes de 02/11; se ela aceita ser colaboradora em 1 reel (ci01). 5 a 10 min [PRIOR].
2. Ok à agência para o **pacote 1**: desligar ETAPAS de story (até dom 09h) e CASE, ESTRATEGISTA, ETAPAS de comentário, FUNIL e CAIXA (até dom 18h30); pôr `&p=dentista` no botão da TABULEIRO do Dentista B antes das 21h, se der tempo. 1 min.

**S1, 25 a 31/10:**
| # | Item | Prazo | Minutos |
|---|---|---|---|
| 1 | Compartilhar o tl01 com menção à Mirna e testar marcar pessoa no reel publicado | dom 25/10 18h35 | 3 [PRIOR] |
| 2 | Link do teste no story das 12h03 | todo dia | 7 a 14 [PRIOR] |
| 3 | Ok do pacote S1 (legendas, car02, mudança do ci01, stories de 26 a 31/10) | seg 26/10 18h | 10 [PRIOR] |
| 4 | Dizer se `bruno26111982` é perfil dele | seg 26/10 | 1 |
| 5 | Bloco 1 de gravação: consórcio e nutricionista, só as versões sem linha travada, 2 tomadas do gancho, arquivo como documento ou pelo Drive | qua 28/10 23h59 | 24 a 36 [ESTIMATIVA, F5]; piso 12 a 18 |
| 6 | Link da bio para `/tabuleiro/?o=ig-bio` | sex 30/10 | 2 [PRIOR] |
| 7 | Ok do pacote S2 (ci01, ob02, ob01, car03, car04, R1, stories da S2 e do 02/11, ok antecipado do estático com horário) | sáb 31/10 12h | 10 [PRIOR] |

**S2, 01 a 07/11:**
| # | Item | Prazo | Minutos |
|---|---|---|---|
| 1 | Stories do dia 02/11 com horário, menção e link (ou a versão sem horário às 12h) | seg 02/11 | 5 [PRIOR] |
| 2 | Contar os votos do tl01 e mandar à agência | seg 02/11 12h | 2 [PRIOR] |
| 3 | Link do teste às 12h03 | todo dia | 7 a 14 |
| 4 | Compartilhar o ci01 com menção à Mirna (3 de 3) | ter 03/11 21h05 | 1 [PRIOR] |
| 5 | Bloco 2: psicólogo sem a linha da Tzur e advogado (só com OAB lido) ou consórcio 6 | qua 04/11 23h59 | 24 a 36 |
| 6 | Ok do pacote S3 (inclui o "mais votado inteiro") | qua 04/11 | 10 |
| 7 | Números de segunda: `tabuleiro_start`, `tabuleiro_complete` e `generate_lead` no GA4; mensagens "Fiz O Tabuleiro" e "Quero agendar o Primeiro Lance" no WhatsApp; diagnósticos agendados e feitos | seg 09/11 | 10 [PRIOR] |

**S3, 08 a 14/11:** ok do pacote S4; link diário; bloco 3 até sex 13/11; mostrar à Mirna o "Uau!" do tl04 até seg 09/11 e o "AINDA?" do tl05 até seg 16/11; números de segunda; confirmar cliente, ano e papel do caso "100 mil seguidores" (para a O10) e onde ficam o restaurante e a franquia (para a O15); responder directs da semana.
**S4, 15 a 21/11:** ok do pacote S5; link diário (fora dos feriados); bloco 4 até qua 18/11; número de diagnósticos agendados para a conferência de qua 18/11; números de segunda.

**Opcionais (camada 3, só com folga):** compartilhar o reel às 21h05 ou 18h35; marcar a Mirna na mídia (se o teste do tl01 der certo); caixa de pergunta aos sábados; Trial Reel pelo app se a API recusar (só R1); vídeo curto de 02/11 (3 a 5 min [ESTIMATIVA, F5]).

### 4.2 Lista da agência (sessão principal, depois do ok escrito)

| Até | Tarefa | Peça ou id |
|---|---|---|
| sáb 24/10 21h | `&p=dentista` no botão da TABULEIRO (se houver ok) | automação TABULEIRO do Dentista B |
| dom 25/10 08h30 | Agendar os stories de dom 25/10 (mc02, O1, frase 1, chamada 17h30) | PZ |
| dom 25/10 09h e 18h30 | Desligar ETAPAS de story; desligar as 5 de conta toda | pacote 1 |
| dom 25/10 17h | @ da Mirna na legenda do tl01, se chegar | m171tvpw4z0c0rxz7fpak824bd8gx35v |
| seg 26/10 12h | Pacote S1: legendas de pb01 (data e @), car01 (1 pedido), po01 ("Comenta qual delas."), pb02 (data e @); car02 renderizado com folha; stories de 26 a 31/10 renderizados; nova data e legenda do ci01 | pb01 m17dqk63b0e1hk75xcevdwmc458gwmfn; car01 m174q9y41reqfn4eqhqrm124f58gwzbr; po01 m17ersdnwmmsk5e7fyw4jqwfdx8gwcxt; pb02 m1718n57yvmtpyb4xnf3zsw7fn8gwe7q |
| ter 27/10 23h59 | Mover o ci01 para ter 03/11 21h (2026-11-04T00:00:00Z) | m177cf21jjcv7fa2y1q1twc4n58gwe0n |
| qui 29/10 23h59 | Se o tl02 ficou: cortar o trecho sem voz (10,4 s) para 8 s ou menos e trocar a mídia até sex 30/10; se não der, registrar o risco | m171fp82kqkbcw5h3xggewpev18gwe2g |
| sex 30/10 | ci01 com a abertura trocada para um quadro com o rosto do Bruno até 2,5 s, folha e nota | ci01 |
| sex 30/10 12h | Pacote S2: legendas de ci01 e ob02; notas de 0 a 10 nas folhas de ob01 a ob03; legenda queimada do ob02 conferida em 1199,9 a 1204,0 s; edição do R1 (transcrição, abertura nova, Legenda Gigante, corte de 20 a 40%); car03 e car04; stories da S2 e do 02/11 | ob01 a ob03; R1 |
| sex 30/10 20h59 | Se o pb01 passou 150 com pulo abaixo de 60%: criar a TABULEIRO de conta toda (texto da F8 seção 8) e trocar o pedido do pb02 | pb02 |
| sáb 31/10 | Agendar a S2 inteira; mc04 para dom 01/11 09h | PZ |
| seg 02/11 08h30 | Se a grade sair: render do estático com o horário e agendamento às 10h | ok antecipado |
| qua 04/11 | "Mais votado inteiro" renderizado (60 a 120 s [HIPÓTESE sobre a duração]) com folha e nota | corte novo |
| qui 05/11, qui 12/11, qui 19/11 | Pacotes S3, S4 e S5 | |
| toda segunda 19h | Módulo 7 com registro em `semanas/AAAA-MM-DD.md`, linha "executado: sim ou não", lista do Bruno de até 7 itens | |

### 4.3 Leituras dos agentes (só leitura)

| Quando | O quê | Ferramenta |
|---|---|---|
| até dom 25/10 09h33 | Pilha de stories de sáb 24/10 | `ig_posts` kind=stories, `ig_post_stats` |
| dom 25/10 21h; seg 26/10 21h05 | Dentista B com 24 e 48 h; logs da TABULEIRO | `ig_post_stats`, `ig_reel_checkup`, `listCommentAutomationLogs` |
| seg 26/10 | Seguidores de 22 e 23/10 | `ig_follower_growth` |
| ter 27/10 18h35 e 21h | tl01 com 48 h; pb01 com 24 h | `ig_post_stats`, `ig_reel_checkup` |
| qua 28/10 21h | pb01 com 48 h | `ig_post_stats` |
| todo dia 23h (S3 obrigatório) | Pilha de stories do dia | `ig_posts`, `ig_post_stats` |
| 31/10, 01/11 e 02/11 às 08h | Grade de 02/11 no site | tvcamaracampinas.com.br/programacao/2026-11-02 |
| 02 a 06/11 | Edição do Bruno na página do programa | site da TV |
| a partir de dom 25/10 13h45 | Buscas de mercado que não rodaram (bastidor de TV) | `buzzfy_reel_search` (10 por dia) |
| seg 19h (26/10 21h05, 02, 09, 16 e 23/11) | Módulo 7 | Buzzfy e PostZen permitidos |

---

## 5. Respostas às 22 perguntas

**1. Quais decisões o plano move, qual número muda, com que fonte e em que segunda é lido?**

| D | O que o plano faz | Número que deve mexer | Fonte | Lido em |
|---|---|---|---|---|
| D1 | Move só o ci01 (para ter 03/11); 02/11 sem reel; S2 com estoque pronto | Alcance médio em 48 h dos reels da série por fase (antes e depois) e pulo médio; visitas ao perfil por dia de 02 a 04/11 (base 10,6 [ESTIMATIVA, 74 / 7]); saldo de seguidores de 25/10 a 08/11 (base de 12 a 21/10: 1 entrada e 6 saídas [FATO, fato 17]) | `ig_post_stats`, `ig_account_stats`, `ig_follower_growth` | seg 02/11 (antes), seg 09/11 (depois e visitas), qua 11/11 (saldo fecha) |
| D2 | 1 bloco por semana com 2 roteiros; Plano Z com ordem fixa; vaga semanal do Bruno de frente | Mediana de alcance e pulo dos reels de nicho (n de 3 ou mais) | `ig_post_stats` | qua 11/11 e seg 23/11 |
| D3 | Teto de 5 reels e 2 carrosséis, piso de 3; semana agendada até sexta; agência executa | Reels por semana; mediana semanal de alcance de reel; seguidores líquidos | `ig_posts`, `ig_post_stats`, `ig_follower_growth` | toda segunda; seguidores em 13/11 e 18/11 |
| D4 | 7 a 8 stories por dia, 1 à mão; objeção pede resposta; ob02, ob01, ob03 na S2 e S3 | Views de story em 7 dias (base 1.041 [FATO, fato 56, 15h30]); respostas em 7 dias (base 3); alcance e pulo dos ob | `ig_account_stats`, `ig_post_stats` | 09/11 e 16/11 |
| D5 | Régua única e regra de encolhimento | Rodadas registradas; % de decisões executadas (base 37,5%) | arquivos de semana | toda segunda |
| D6 | Automações de conta toda desligadas; TABULEIRO de conta toda só com portão; bio no teste | Disparos de TABULEIRO de terceiros (base 0); cliques no site em 7 dias (base 0) | `listCommentAutomationLogs`, `ig_account_stats`, número do Bruno | 09/11 (parcial; o brief pede leitura parcial de diagnóstico em 04/11 [FATO, fato 181]) e 23/11 |

**2. Qual régua?** Alcance em 48 h sobre 53, do começo ao fim. Limites: 27, 42, 53, 106 e 150; pulo 60% e 75% [ESTIMATIVA, conta sobre 53; F7 seção 5.1]. Motivos: separa os grupos já medidos (animação até 40 fica abaixo de 42; o menor reel com o Bruno, 128, fica acima de 106) [FATO, F7 seção 5.1]; a mediana de 37,5 do Buzzfy anda sozinha com os reels novos e mudaria a decisão no meio das 4 semanas [ESTIMATIVA, F7]. Views (57 de normal) ficam como coluna de referência.

**3. Grade dia a dia e hora a hora, com feriados?** Seção 3.2. Dias da semana conferidos com `date` (C1). Feriados: seg 02/11 sem reel e com Molde TV; dom 15/11 só carrossel e stories agendados; sex 20/11 com reel às 21h no Plano A e stories agendados. Reel de feriado entra na mediana e não fecha PARAR sozinho [F7 seção 4.4].

**4. Antes, no dia e depois de 02/11?**
- **Antes (24/10 a 01/11):** tl01, pb01, car01, pf01 (story), po01, pb02, tl02 e car02 no feed; 1º story de cada dia com o Bruno em cena e "NA TV · SEG, 02/11"; "FALTAM N DIAS" no texto do 1º story quando ele for estático (derivar 26: dom 25/10 faltam 8 até dom 01/11 falta 1); mc02, mc03 e mc04 nas manhãs de 25/10, 26/10 e 01/11. Sticker de contagem nativo só se o horário chegar antes [F6 seção 5.2].
- **No dia (seg 02/11):** stories do Molde TV. Se o horário seguir sem dado na manhã: às 12h, story "A partir de hoje, 02/11, na TV Câmara Campinas." com link para `/programacao`; agentes releem a grade às 08h; se a grade sair até 08h30, estático com a hora às 10h pelo PostZen (ok antecipado). Nada de "foi ao ar" sem a hora confirmada [FATO, fato 6].
- **Depois (03/11 a 21/11):** ci01 (ter 03/11), ob02, ob01, "mais votado inteiro", tl03 a tl05, car04 e car06 (carrosséis da TV), link da edição em story quando sair no site, objeção O14 no dia 03/11.

**5. Os 5 cortes, um por um.**

| Peça | Hoje | Decisão | Motivo | Quem mexe e até quando |
|---|---|---|---|---|
| pb01 | seg 26/10 21h | **Fica** | Apresenta o Bruno (DJ por 20 anos) sem entregar caso nem método; abre a dupla P&B que o portão de 02/11 lê com n de 2; o Bruno disse "pode seguir" [FATO, fato 1] | Agência troca a legenda (data e @) até seg 26/10 20h59 |
| car01 | ter 27/10 12h | **Fica** | Único carrossel pronto [FATO, fato 108]; os minutos são "na gravação" | Agência deixa 1 pedido (o direct) até ter 27/10 11h59 |
| ci01 | qua 28/10 21h | **Move para ter 03/11 21h** | (1) Tira a S1 de 6 para 5 reels sem exceção escrita [FATO, fato 76]; (2) é a peça com mais Mirna (voz em 2 trechos, rosto em 10,7 s) [FATO, fato 90], e o convite de colaboração depois da exibição pede menos da liberação que ainda é verbal [FATO, fato 4 e 5]; (3) a frase já foi anunciada com "NA TV · SEGUNDA, 02/11" [FATO, F4]; (4) é o assunto 5 do índice, que a legenda do tl01 promete para depois da exibição [FATO, fato 77]; (5) em 03/11 a leitura de 48 h não cai em feriado; (6) a legenda sai certa sem troca à mão no feriado; (7) dá 10 dias para corrigir a abertura, que mostra o Bruno de costas até 2,5 s [FATO, fato 88] | Agência muda a data até ter 27/10 23h59 (2026-11-04T00:00:00Z) e troca o arquivo até sex 30/10 |
| po01 | qui 29/10 21h | **Fica** | A própria condição da F4 para ele ficar (vaga de qui 29/10 sem peça de nicho até qua 28/10 12h) é o cenário mais provável: nenhuma gravação desde 21/10 [FATO, fato 104]. Mexer custa 1 edição no PostZen e 4 stories do 03-plano; ficar não custa nada | Agência troca "Comenta a palavra" por "Comenta qual delas." até qui 29/10 20h59 |
| pb02 | sex 30/10 21h | **Fica** (sobe para qua 28/10 21h só se o pb01 fizer 171 views ou mais em 24 h) | Fecha a dupla P&B com n de 2 antes do portão de 02/11; a subida é a sequência do playbook (1,81x depois de estouro [FATO, fato 149]) sem mudar a contagem | Legenda até sex 30/10 20h59; se subir, data até ter 27/10 23h59 |

**6. Promessa do tl01.** A promessa do sábado já saiu da legenda; hoje ela diz "O mais votado eu solto inteiro depois que a entrevista for ao ar" [FATO, fato 77]. A S1 fica em 5 reels sem precisar dela. Cumprimento: o Bruno conta os votos até seg 02/11 12h; com 1 voto ou mais, a agência faz o corte longo do assunto vencedor (duração e abertura novas, 2 mudanças contra o corte já publicado [FATO, fato 150]) para sex 06/11 21h; com 0 voto, story em ter 03/11 dizendo isso, com o link da edição quando sair, e o plano segue (regra do catálogo para menos de 5 votos [FATO, fato 170]).

**7. tl02 a tl05.** Ordem do PostZen mantida (31/10, 07/11, 14/11, 21/11, 18h30) [FATO, fato 74]: zero mudança. Portões em horas reais de 48 h:
- tl01: ter 27/10 18h35. 106 ou mais com pulo abaixo de 60%, ou 42 ou mais com pulo até 75%: tl02 fica. Só um critério ruim: sai o tl02 e o tl03 vira a 2ª leitura. Abaixo de 27, ou abaixo de 42 com pulo acima de 75%: saem tl02 a tl05 [F7 seção 5.4].
- tl02: seg 02/11 18h30 (lido às 19h); tl03: seg 09/11 18h30; tl04: seg 16/11 18h30. Com n de 2 ou mais, a família segue a régua geral pela mediana.
- Cancelamento: até sex 23h59 antes do sábado (agência, com o ok da lista).
- Timelapse fora do feed: trechos de 15 s no story das 09h e banco. Sábado sem timelapse recebe reel com o Bruno no quadro 0 só se a semana ficaria abaixo de 5; senão fica fechado com o motivo escrito.

**8. mc02 a mc04.** mc02 dom 25/10 09h00; mc03 seg 26/10 09h00; mc04 dom 01/11 09h00 (véspera, depois do tl02). Recorte do mc04: **1700,967 a 1705,567 s, fim depois de "família,"**, dentro da faixa de 1705,2 a 1705,7 s do 03-plano, e não 1707,82 s. Motivos: o render de 4,60 s já existe (15h35) e a ficha documenta o corte no vale de energia [FATO, conferência C4]; tira "através da profissão que hoje eu executo como estrategista digital", termo que o Módulo 1 tirou da bio [FATO, ficha do mc04]. Conferir o ticker "Uma profissão por 20 anos" antes de agendar [FATO, fato 100].

**9. Marcação da Mirna.**

| Caminho | Quem | Onde | Custo | Se falhar |
|---|---|---|---|---|
| @ no texto da legenda | Agência, no PostZen, em lote, assim que o Bruno mandar o @ | tl01, pb01, car01, po01, pb02, tl02, ci01, tl03, tl04, tl05, car04 e car06 se ela estiver nas lâminas | 0 min do Bruno | Sem o @, a linha sai da legenda (F4 seção 5) |
| Convite de colaboração | Agência, campo `collaborators` [FATO, fato 139] | Só ci01 (ter 03/11); tl03 só se ela aceitar o 1º | 0 min do Bruno; pede o @ e o ok dela | Post segue só no perfil do Bruno |
| Menção em story | Bruno, à mão | 3 momentos: dom 25/10 18h35, seg 02/11 (story com a hora), ter 03/11 21h05 | 1 a 2 min cada [PRIOR] | Fica a menção da legenda |
| Marcar na mídia depois de publicar | Bruno, no app | Só se o teste do tl01 der certo; camada 3 | 1 a 2 min por peça [PRIOR, palpite 5] | Se o app não deixar marcar depois, **nada de publicar à mão só para marcar**: fica o @ na legenda e o convite no ci01 |
| Não marcar | | mc02 a mc04 e ob01 a ob03 (ela não aparece nos quadros conferidos, C3) | | |

Antes de marcar no tl04 e no tl05, a Mirna vê o efeito sobre o rosto dela; sem ok, a agência troca o efeito ou o reel sai [FATO, fato 90; HIPÓTESE, palpite 37].

**10. Copy depois de 02/11.** "Foi ao ar" só depois do horário confirmado; antes disso vale "exibe desde segunda, 02/11", com a mensagem do Bruno como fonte [FATO, fato 1]. Link da edição em story quando ela aparecer no site (compartilhar link é livre pelos termos) [FATO, fato 137]. Minutos da edição exibida só depois de conferir na própria edição; os minutos do car01 e do tl01 contam da gravação do celular [FATO, fato 81]. Continua vetado: "ao vivo", "rede nacional", "a TV Câmara recomenda", "fui convidado pela TV", "entrevista exclusiva", "A TV me chamou de história de sucesso" [FATO, fato 6]; recortar ou filmar a exibição; republicar a edição inteira; usar o conteúdo em anúncio pago sem autorização escrita [FATO, fato 137]; logo da emissora.

**11. 5 reels e 2 carrosséis por semana?** Teto de 5 e 2, piso de 3 e 2 (seção 3.3). Nenhum dia com 2 reels; no máximo 2 posts de feed por dia (só ter 03/11 chega a 2). Os 7 carrosséis que faltam: a agência produz, cerca de 36 min cada [ESTIMATIVA, F5 seção 7], todos com foto do Bruno na capa (feed com foto: mediana 111; de texto: 34,5 [FATO, fato 51]): car02 até seg 26/10 12h; car03 e car04 até sex 30/10 12h; car05 e car06 até qui 05/11; car07 e car08 até qui 12/11; car09 (opcional, dom 22/11) até qui 19/11. Fontes: CARROSSEL 02 a 04 da TV e os temas do Módulo 3 sem material do Bruno (Os 5 Lances, Seguidor x comprador, Oferta em 5 pilares, Carrinho, Resumo do mês) [FATO, F5 seção 8]. "Os 5 Lances" usa só o texto do /tabuleiro/ (A Abertura, O Gambito, O Meio-Jogo, O Xeque-Mate, A Promoção) [FATO, fato 129].

**12. Bruno em cena nos 3 primeiros segundos?**

| Peça | Situação | Fonte |
|---|---|---|
| Dentista C | Sim, selfie com "Dentistas," no quadro 0 | [FATO, fato 101] |
| tl01, tl02, tl03 | Sim, aos 0,6 e 2,5 s | [FATO, fato 89] |
| tl04, tl05 | Sim pela ficha (CB no quadro 0); quadro não conferido: agência confere antes dos portões de 09/11 e 16/11 | [FATO, F5 seção 12] |
| ob01 a ob03 | Sim, de perfil atrás do monitor, aos 0 e 2,5 s | [FATO, conferência C3] |
| pb01, po01, pb02, pf01 | Sim, de perfil em 3/4, desde o quadro 0 | [FATO, fato 88] |
| ci01 | **Não no sentido da regra:** de costas, sem o rosto visível até 2,5 s. Corrigir a abertura até sex 30/10 | [FATO, fato 88] |
| R1 a R3 | Sim, selfie com fala própria | [FATO, fato 35] |
| "Mais votado" e cortes do banco | Regra de corte: começar num quadro com o rosto do Bruno visível | regra deste plano |
| Nicho gravado | Selfie, Bruno no quadro 0 | teleprompter e ficha F1 do catálogo |

**13. Mínimo de gravação.** 2 roteiros por semana, 24 a 36 min (2 x 12 a 18 min [ESTIMATIVA, F5 seção 9]); piso de 1 roteiro, 12 a 18 min. Gravar só a versão sem linha travada (sem a linha da ABAC, sem a linha da Tzur; nutricionista na versão que não depende da CFN 856), o que corta de 4 a 8 min por bloco [ESTIMATIVA, F5]. Próxima sessão: data sem dado; prazo do bloco 1 qua 28/10 23h59. Sequência: bloco 1 consórcio e nutricionista (publicam qui 05/11 e seg 09/11 e entram na conferência de 11/11 com 48 h); bloco 2 psicólogo e advogado ou consórcio 6 (até qua 04/11); bloco 3 pela conferência de 11/11 (até sex 13/11); bloco 4 pelo Módulo 7 de 16/11 (até qua 18/11). Semana com zero gravação, em ordem: ob que sobrou; "mais votado inteiro"; remake R1 a R3 (Trial e, na vaga do Bruno de frente, nova versão no feed); tl03 a tl05 com portão; cortes do banco (só com a família TV fora de PARAR); pf01 como reel só com DOBRAR; Tzur v2 só com autorização escrita e sem "comenta estrategista"; vaga fechada com motivo. Nunca animação, voz sintética ou voz clonada [FATO, CLAUDE.md; fato 27].

**14. Dentista C e remakes.** Dentista C: fora do feed e do direct; vai para o banco de anúncio depois de 18/11, com a Res. CFO 196/2019 conferida, como manda o brief do dentista [FATO, fato 101]. Motivo operacional: seria a 3ª edição da mesma fala em 2 semanas, e a sequência do Dentista B, se ele passar, vai para nicho gravado (outro assunto, mesmo formato). Remakes: R1, R2 e R3 sem gravação, como Trial Reel, às 11h de dom 01/11, ter 03/11 e qui 05/11 [F2 seção 10.3]. Quem posta: a agência pelo PostZen com `trialParams` [FATO, fato 139]; o R1 testa a elegibilidade (a falha só aparece na publicação). Se a API recusar, o Bruno posta só o R1 pelo app. Entrada no feed: 53 ou mais em 48 h com pulo abaixo de 60%; nos Planos Z, a vaga semanal do Bruno de frente pode usar R1 e R2 como nova versão no feed (3 mudanças) mesmo sem Trial [HIPÓTESE, ideia 46].

**15. Stories por dia.** 7 a 8 em dia de reel, 6 em dia sem reel (moldes da seção 3.1). PostZen: 5 a 7 por dia, sem sticker. À mão: 1 obrigatório (link, 12h03) e 1 opcional (compartilhar). Total à mão por semana: 7 a 12, contra 27 do 03-plano e 20 da F6 [FATO, fato 61; derivar 17]. Origem de cada frase: objeção do 01-objecoes, virada do 01-objecoes, prova do 02-provas com tempo da transcrição, frase de efeito do banco de 14 da F6 (seção 6), bastidor da gravação do celular e mc02 a mc04.

**16. ob01 a ob03.** Render final pronto desde 15h58 de hoje (C2). Antes de agendar: nota de 0 a 10 por efeito nas folhas, corrigir o que ficar abaixo de 8 [FATO, CLAUDE.md]; conferir "um produto" na legenda do ob02 (C5) e "e ter a" no ob01 [FATO, 03-plano]. Prazo: sex 30/10 12h. Datas: ob02 qua 04/11 21h; ob01 qui 05/11 21h no Plano Z (seg 09/11 ou depois no Plano A); ob03 na S3. Pedido da legenda igual ao do vídeo: "Me manda a sua área no direct." [FATO, fato 94]. Substituto se não passarem na folha: "mais votado inteiro", remake no feed, pf01 como reel só com DOBRAR.

**17. PARAR, MANTER, DOBRAR, TESTAR.**

| Decisão | Reel (mediana do formato em 48 h) | Carrossel | Story (semana) |
|---|---|---|---|
| PARAR | Alcance abaixo de 42 ou pulo acima de 75%, com n de 2 ou mais | Abaixo de 42 em 2 | Views abaixo de 982 por 2 semanas seguidas |
| MANTER | 42 a 105 | 42 a 105 | 982 ou mais |
| DOBRAR | 106 ou mais e pulo abaixo de 60%, n de 2 ou mais | 106 ou mais e 2 visitas ao perfil ou mais | Respostas 4 ou mais em 7 dias: o tipo que respondeu ganha mais um quadro |
| TESTAR | n de 1; ocupa no máximo 1 vaga por semana | n de 1 | Teste de carga só na S3 |

Formatos para contar n: Bruno de frente (hoje DOBRAR, n de 4 [FATO, F7]); corte da TV de perfil (família, n de 0; pb, po, ci, ob, "mais votado" e banco contam juntos); timelapse (regra própria da pergunta 7); carrossel com foto; carrossel de texto e animação (já em PARAR [FATO, F7 seção 5.2]). Segundas: 26/10 21h05 (extra), ter 27/10 18h35 (extra), 02/11, 09/11, 16/11 e 23/11 às 19h. Rodada de 02/11: agentes leem às 19h a S1 inteira; nenhuma tarefa do Bruno no feriado além dos stories do dia; lista dele vence ter 03/11 11h; nada da S2 depende dessa rodada além do tl03 e da família TV.

**18. TABULEIRO.** Uma palavra, TABULEIRO, numa automação de conta toda com o texto genérico da F8 (seção 8), criada pela agência depois do ok no primeiro post que passar no portão a partir de sex 30/10; a do Dentista B sai no mesmo momento. Condição: o post anterior da mesma linha fez 150 ou mais em 48 h com pulo abaixo de 60%; no máximo 1 post por semana; nunca em 02/11, nunca em story. Candidatos com data: pb02 (se pb01 passar, lido qua 28/10 21h); tl03 (tl02, seg 02/11 18h30); tl04 (tl03, seg 09/11); tl05 (tl04, seg 16/11); nicho seguinte (nicho anterior, 48 h depois). Desempate: nicho falado antes de corte da TV [F8 R5]. Outras 16 automações: as 5 de comentário de conta toda e a ETAPAS de story desligadas antes do tl01; as 10 presas a posts antigos ficam (0 comentário nesses posts) [F8 R1]. Pedidos de direct: 1 pedido por legenda; "área" e "data" sempre no direct, nunca como comentário. Contagem por etapa, toda segunda: alcance e pulo do post anterior (agente); comentários (agente); disparos pela diferença do total do log, sem perfis do Bruno (agente); visitas e cliques (agente); `tabuleiro_start`, `tabuleiro_complete`, `generate_lead` (Bruno, GA4); mensagens com as 2 frases fixas (Bruno, WhatsApp); diagnósticos agendados e feitos (Bruno). Sem o número do Bruno: "sem dado".

**19. Uma mudança por post na mesma linha.**

| Linha | Sequência | Muda | Mantém |
|---|---|---|---|
| P&B da TV | pb01 para pb02 | assunto (DJ para restaurante) | formato |
| Timelapse | tl01 para tl02 para tl03 para tl04 para tl05 | assunto (índice, investimento, origem, olho no olho) | formato |
| Objeção | ob02 para ob01 para ob03 | objeção (O1, O2, O8) | formato |
| Nicho falado | Dentista A, B, depois consórcio, nutricionista, psicólogo | B: formato; depois, profissão | modelo A da selfie |
| Corte longo | "mais votado inteiro" contra o corte já publicado do mesmo assunto | duração e abertura (é remake, pede 2 mudanças) | assunto |
| Remake | R1, R2, R3 contra o original | abertura, legenda, corte (2 ou 3, regra de segunda vida) | fala |
| Carrossel | car01 (TV), car02 (5 Lances), car03 (quiz TV), car04 (TV), car05 a car08 (Módulo 3) | assunto | carrossel com foto do Bruno na capa |
| ci01 e tl05 | mesmo assunto ("o melhor marketing") | formato | assunto |

**20. Regras de texto.** As legendas novas deste plano são poucas e foram conferidas: sem travessão, sem emoji, sem promessa de resultado, sem os nomes vetados, no máximo uma "não é X, é Y", nada da lista do 02-provas, sem logo de terceiro. Legenda do ci01 para ter 03/11 (versão A da F4 com a data trocada):
> Até hoje o melhor marketing é o olho no olho.
> Essa conversa com a repórter Mirna Abreu [@ dela] está na edição do programa Ser Empreendedor que a TV Câmara Campinas exibe desde segunda, 02/11.
> Na entrevista eu disse que nem tudo que vemos é ouro. Muita gente vende o que não consegue cumprir, e o cliente chega machucado. Por isso o encontro ainda decide a venda.
> Segue o perfil: os próximos trechos da entrevista saem aqui.

Story de objeção (linha nova): "Isso é você? Responde SIM ou NÃO." Story de 02/11, 20h30: "Chegou aqui pela TV Câmara? Responde este story com a sua área." car02, legenda: "Os 5 Lances de um lançamento, do jeito que o Tabuleiro mostra. Salva para conferir antes do próximo." As demais legendas são as da F4 (pb01, car01, pb02, po01), já conferidas lá.

**21. O que depende só do Bruno, com prazo.**

| Item | Prazo |
|---|---|
| Mensagem à Mirna: @, horário, print, ok da produção para antes de 02/11, colaboração | hoje, sáb 24/10; resposta até dom 25/10 17h |
| Ok dos pacotes (1, S1, S2, S3, S4, S5) | sáb 24/10; seg 26/10 18h; sáb 31/10 12h; qua 04/11; qua 11/11; qua 18/11 |
| Teste de marcar pessoa no reel publicado | dom 25/10 18h35 |
| Gravação | qua 28/10, qua 04/11, sex 13/11, qua 18/11, sempre 23h59 |
| Link da bio | sex 30/10 |
| Votos do tl01 | seg 02/11 12h |
| Stickers (link diário, menções, contagem, caixa) | diário; menções em 25/10, 02/11 e 03/11 |
| Trial Reel pelo app (só se a API recusar o R1) | dom 01/11 11h |
| Mostrar tl04 e tl05 à Mirna | seg 09/11 e seg 16/11 |
| Perfil `bruno26111982` | seg 26/10 |
| Números de GA4, WhatsApp e diagnósticos | toda segunda a partir de 02/11 (opcional no feriado) |
| Cópia do estoque para o Drive (mc02 a mc04, ob01 a ob03, fonte da entrevista) | até sex 30/10 |
| Autorização escrita da Tzur (se quiser o case v2) | sem prazo |
| Original em alta de R1 a R3 no celular, se existir | sex 30/10 |

**22. Etiquetas.** Cada número deste arquivo tem etiqueta. As faltas estão como "sem dado" (seção 11).

---

## 6. Decisões D1 a D6

### D1 · Série da entrevista em torno de 02/11

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) Manter os 5 nas datas | Zero edição; S1 com 6 reels | S1 acima da regra pede TESTAR escrito; ci01 sai antes do dia dela; a semana da exibição depende só de estoque |
| (b) Mover os 5 para depois | 5 edições e 5 legendas; S1 com 2 a 3 reels | Semana antes da TV sem cadência; vagas da S1 sem peça (nada gravado); car01 era o único carrossel |
| (c) Dividir (F4: ci01 para 02/11, po01 para 04/11) | 2 edições; S1 com 4 e 1 vaga | A vaga de qui 29/10 sem peça devolve o po01 pela própria condição; ci01 no feriado com troca A e B à mão |
| (d) Não mexer agora | Decide em 26/10 21h05 | pb01 já saiu; a decisão fica refém do relógio |
| **(e) Fora do óbvio, minha: mover só o ci01, para ter 03/11 21h, e corrigir a abertura dele** | 1 edição; S1 em 5 exatos; 02/11 sem reel | Leitura do ci01 fora do feriado; legenda sem troca no feriado; perde-se a janela de feed no próprio dia 02/11 (efeito sem dado) |
| (f) Fora do óbvio: TV como prova permanente e teto de 3 cortes por semana a partir da S3 | Menos cortes no feed | Banco dura até dez/jan; exige peça com o Bruno de frente |

- **Premissas:** o ok da produção para publicar antes de 02/11 vem no print [sem dado]; o formato corte de perfil fica em 42 ou mais [sem dado, n de 0]; o @ chega antes das peças.
- **Posição:** (e), com o teto de (f) a partir da S3.
- **Probabilidade de sucesso pelo critério do enquadramento:** 0,15 [0,06; 0,28]. Conta [PRIOR]: série em 42 ou mais com pulo até 75% em cada fase, cerca de 0,35 (formato novo); visitas de 21 por dia de 02 a 04/11, cerca de 0,25 (base 10,6, feriado, audiência da TV com mediana de 80,5 views no site [FATO, fato 136]); saldo positivo de 25/10 a 08/11, cerca de 0,45; as três juntas, com correlação.
- **Confiança:** 0,40.

### D2 · Gravação, Dentista C e remakes

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 1 bloco semanal de 2 roteiros (24 a 36 min) | 2 nichos por semana a partir da S2 | Conferência de 11/11 com n de 4 (A, B e 2 novos) |
| (b) 60 a 90 min com 5 roteiros | 5 nichos por semana | Base: 1 fala em 3 dias contra 90 min planejados [FATO, fato 104 e 105]; repete o plano que não saiu |
| (c) Quinzenal com 10 | Estoque grande de uma vez | Uma sessão perdida zera 2 semanas |
| (d) Zero gravação | Só TV, ob, remakes | 4 semanas de formato sem medida; nicho "não testado" |
| **(e) Fora do óbvio: piso de 1 roteiro gravado só na versão sem linha travada, no mesmo dia do ok semanal, e vaga semanal do Bruno de frente fechada com remake quando não houver gravação** | Toque menor; nenhuma peça presa a leitura regulatória pendente | O Bruno de frente aparece toda semana mesmo no Plano Z |

- **Premissas:** o Bruno tem 24 a 36 min por semana [sem dado]; remake em 720p segura em 1080x1920 [HIPÓTESE, palpite 55]; Trial Reel elegível [sem dado].
- **Posição:** (a) com o piso e a vaga de (e); Dentista C no banco de anúncio depois de 18/11; R1 a R3 como Trial.
- **Probabilidade:** 0,22 [0,10; 0,38]. Conta [PRIOR]: bloco 1 gravado até 28/10, cerca de 0,35; 2 nichos por semana de S2 a S4, cerca de 0,25; mediana de 53 ou mais com pulo até 75% em 11/11 se gravado, cerca de 0,7; 0 voz sintética e 0 reel sem o Bruno, cerca de 0,9 (depende da agência).
- **Confiança:** 0,45.

### D3 · Grade e operação

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 5 e 2 fixos | Volume previsível | Força vaga preenchida com o que houver |
| (b) 6 só na S1 | Cumpre agenda atual | TESTAR sem motivo medido |
| (c) 6 a 7 com portão | Mais chance de estouro (7,7% contra 7,0% [FATO, fato 152]) | Mais carga e mais corte de perfil |
| (d) Reduzida 3 e 2 | Menos carga | Menos amostra por semana |
| **(e) Fora do óbvio: teto 5 e 2, piso 3 e 2; a agência agenda a semana inteira até sexta com 1 ok; o portão de segunda só cancela ou troca; oks condicionais escritos de antemão** | O Bruno dá 1 toque por semana na grade | Cancelar é mais barato que agendar; vaga fechada vira dado ("sem peça") e não filler |

- **Premissas:** a agência segue com acesso ao PostZen da conta [FATO, C6]; o Bruno responde o pacote em até 24 h [sem dado].
- **Posição:** (e).
- **Probabilidade:** 0,06 [0,02; 0,15]. O critério pede "0 vaga vazia", e este plano aceita vaga fechada por desenho no Plano Z: esse sub-critério falha sempre que o piso entrar. Mediana semanal de 106 ou mais em 2 semanas depende de nicho gravado.
- **Confiança:** 0,40.

### D4 · Stories e ob01 a ob03

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 03-plano estendido (27 à mão por semana) | Mais instrumentos | Carga acima da capacidade medida |
| (b) 3 a 5 por dia | Menos carga | Views de story podem cair abaixo de 982 |
| (c) 6 a 8 em 4 blocos (F6, 20 à mão) | Molde bom | Ainda 20 toques por semana |
| (d) ob nas datas do 03-plano, 1 por semana, ou só banco | | ob02 no feriado e no mesmo horário do ci01 |
| **(e) Fora do óbvio: 7 a 8 por dia quase tudo agendado; objeção pede resposta por texto (o Buzzfy lê, abre direct); 1 story à mão por dia (link); ob02, ob01, ob03 na S2 e S3** | 7 toques por semana | Resposta é métrica do D4 e porta da conversa; menos votos que enquete [HIPÓTESE] |

- **Premissas:** o volume de 7 a 8 por dia segura as views (hoje 1.041 em 7 dias [FATO, fato 56]); ob passam na folha.
- **Posição:** (e). Correção registrada: a meta de 6 respostas em 14 dias é 1x a base de 7 dias (C7).
- **Probabilidade:** 0,18 [0,08; 0,35]. Conta [PRIOR]: 982 ou mais em cada uma das semanas lidas, cerca de 0,45; 6 respostas em 14 dias, cerca de 0,6; ob com média de 42 ou mais e pulo até 75%, cerca de 0,45.
- **Confiança:** 0,45.

### D5 · Portão do Módulo 7

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) 53 de alcance | Separa os grupos medidos | Mediana de 53 não se recalcula (17 reels de 21/09 a 21/10) [FATO, fato 24] |
| (b) 57 views | Igual ao Buzzfy | Views pesam story e repetição; outra unidade |
| (c) 37,5 de alcance | Base atual | Sobe sozinha com reels novos |
| (d) Mediana móvel | Sempre atual | Muda a decisão no meio das 4 semanas |
| **(e) Fora do óbvio: (a) mais uma régua de execução: a rodada só vale com "executado" registrado; abaixo de 50% por 2 rodadas, a semana seguinte entra no modo metade sem nova decisão** | O plano encolhe sozinho | Menos decisões que não saem; menos volume |

- **Premissas:** os agentes rodam toda segunda; o Bruno registra "feito".
- **Posição:** (a) com (e).
- **Probabilidade:** 0,08 [0,03; 0,20]. "Todas as decisões executadas até a segunda seguinte" contra a base de 37,5% é o que derruba [FATO, fato 125].
- **Confiança:** 0,40.

### D6 · TABULEIRO e caminho até o diagnóstico

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| (a) TABULEIRO em todo post que passar 150 | Mais chances | Fere "no máximo 1 por semana" do Módulo 1 [FATO, fato 171] |
| (b) Um post por mês | Leitura estrita | Uma chance só em novembro |
| (c) (a) ou (b) com revisão das 6 de conta toda e um pedido por peça | Remove colisão com "caso" e "estrategista" | O Bruno precisa dar o ok |
| (d) Nada em novembro até 1 disparo real | Zero risco de pedido vazio | Zero dado novo |
| **(e) Fora do óbvio: a porta da TV é a bio; trocar o link da bio para /tabuleiro/?o=ig-bio (já aprovado no Módulo 2 e não aplicado [FATO, fato 132]) e ligar `alsoMatchInDms` na TABULEIRO de conta toda** | Mexe na etapa medida (1,57% de clique [FATO, fato 14]) | Quem manda "tabuleiro" no direct também recebe o botão [HIPÓTESE] |

- **Premissas:** algum post passa 150 com pulo abaixo de 60%; o Bruno informa os números.
- **Posição:** (c) com no máximo 1 por semana, automação de conta toda, e (e).
- **Probabilidade:** 0,05 [0,01; 0,12]. Conta [PRIOR]: 3 disparos de terceiros até 22/11, cerca de 0,08 (19 peças com palavra renderam 3 comentários [FATO, fato 122]; teto de 3,7 a 5,5 comentários de qualquer tipo [ESTIMATIVA, derivar 13]); 1 diagnóstico até 18/11, 0,2 pelo brief [FATO, fato 169]; juntos e correlacionados.
- **Confiança:** 0,50.

---

## 7. Ideias e hipóteses numeradas (85)

Confiança: alta, média ou baixa.

| # | Ideia ou hipótese | Confiança | Evidência |
|---|---|---|---|
| 1 | Mover só o ci01, para ter 03/11 21h | média | fatos 74, 76, 88, 90; F4 seção 4 |
| 2 | po01 fica em qui 29/10 21h | alta | fato 104; condição da F4 seção 8 |
| 3 | S1 fecha em 5 reels sem TESTAR escrito | alta | contagem sobre o fato 74 |
| 4 | car02 "Os 5 Lances" em qua 28/10 12h, fora da TV e ligado ao teste | média | fatos 51 e 129 |
| 5 | Toda capa de carrossel com foto do Bruno | alta | fato 51; F7 seção 5.2 |
| 6 | Seg 02/11 sem reel; só stories | média | F2 seção 9.5; feriado sem dado |
| 7 | Corrigir a abertura do ci01 (de costas até 2,5 s) antes de 03/11 | média | fato 88; CLAUDE.md |
| 8 | A agência faz no PostZen toda edição de legenda, data, @ e automação depois do ok | alta | conferência C6 |
| 9 | Lista do Bruno com no máximo 7 itens por semana e minutos | média | fato 125 |
| 10 | Regra de encolhimento: abaixo de 50% de execução em 2 rodadas, modo metade | média | fato 125; derivar 30 |
| 11 | @ da Mirna em lote nas legendas assim que o Bruno mandar | alta | fato 139; playbook 1,13x (fato 148) |
| 12 | Marcar na mídia só se o teste do tl01 der certo; nunca publicar à mão só para marcar | média | a buscar 5; palpite 2 |
| 13 | Convite de colaboração só no ci01; tl03 só se ela aceitar | média | F4 seção 6.4; fato 139 |
| 14 | Menção em story só em 3 momentos | média | F4 seção 6.3 |
| 15 | Mostrar à Mirna tl04 e tl05 antes; sem ok, trocar efeito ou cancelar | alta | fato 90; palpite 37 |
| 16 | tl02 só fica com tl01 em 42 ou mais e pulo até 75% | alta | F7 seção 5.4 |
| 17 | Cortar o trecho sem voz do tl02 para 8 s ou menos se ele ficar | média | fato 92 |
| 18 | Ordem tl02 a tl05 mantida como no PostZen | alta | fato 74 |
| 19 | Timelapse fora do feed vira trecho de 15 s no story das 09h | média | F4 e F7 |
| 20 | mc02, mc03 e mc04 no bloco das 09h de 25/10, 26/10 e 01/11 | média | F4 seção 4; F6 seção 4 |
| 21 | mc04 com o recorte já renderizado, fim em "família." | alta | conferência C4 |
| 22 | "FALTAM N DIAS" no texto do 1º story; sticker nativo só com horário | média | F6 seção 5.2; fato 66 |
| 23 | "Exibe desde segunda, 02/11" vale antes de "foi ao ar" | alta | fatos 1 e 6 |
| 24 | Link da edição em story; nada de filmar a exibição | alta | fato 137 |
| 25 | Votos do tl01 contados até seg 02/11 12h; "inteiro" em sex 06/11 | média | fato 77 |
| 26 | Com 0 voto, story dizendo isso e o plano segue | alta | fato 170 |
| 27 | "Inteiro" muda duração e abertura contra o corte já publicado | média | fato 150 |
| 28 | ob02 em qua 04/11: a objeção de quem chega pela TV, 2 dias depois | média | F6 O1; conferência C2 |
| 29 | ob01 em qui 05/11 no Plano Z | média | conferência C2 |
| 30 | ob03 na S3 | média | conferência C2 |
| 31 | Conferir "um produto" na legenda queimada do ob02 | alta | conferência C5 |
| 32 | Nota de 0 a 10 por efeito nas folhas dos ob antes de agendar | alta | CLAUDE.md; folhas existem (C2) |
| 33 | Bloco 1 só com as versões sem linha travada | média | fato 103; F5 seção 9 |
| 34 | Piso de gravação: 1 roteiro | média | F5 seção 9 |
| 35 | Enviar gravação como documento ou pelo Drive | média | fato 104; palpite 52 |
| 36 | Vídeo curto de 02/11 fora do mínimo | média | F5 seção 5.1 |
| 37 | Ordem fixa de estoque na semana sem gravação | alta | F5 seção 10 |
| 38 | Nunca animação, voz sintética ou clonada | alta | fato 27; CLAUDE.md |
| 39 | Dentista C só no banco de anúncio depois de 18/11 | alta | fato 101 |
| 40 | R1 como Trial pelo PostZen testa a elegibilidade sem minuto do Bruno | média | fatos 139 e 142 |
| 41 | R2 e R3 só se a API aceitar o R1 | média | seção 2.2 |
| 42 | Trial vai ao feed com 53 ou mais e pulo abaixo de 60% | baixa | régua; fato 151 (21% entre contas pequenas) |
| 43 | Trial não conta nos 5 reels; conta na distância de 6 h | média | palpite 32; fato 152 |
| 44 | Reels seg, qua, qui e sex às 21h; sábado 18h30; carrosséis ter e dom 12h | média | F7 seção 4.1 |
| 45 | dom 15/11 só com agendados | média | F6 seção 9.3; alcance em feriado sem dado |
| 46 | Vaga semanal do Bruno de frente, com remake como nova versão no feed no Plano Z | baixa | fatos 25 e 150 (35% com original de 5x ou mais) |
| 47 | Régua única de alcance sobre 53 | alta | F7 seção 5.1 |
| 48 | Família "corte da TV" conta n junta para PARAR | média | F8 R4; leitura deste plano |
| 49 | PARAR da família no portão de 02/11 tira ob e banco do feed | média | F4 seção 8 |
| 50 | Portões extras em 26/10 21h05 e 27/10 18h35 | alta | F7 seção 5.7 |
| 51 | Rodada de 02/11 sem tarefa do Bruno no feriado | alta | F7 seção 5.7 |
| 52 | Ler a pilha de domingo 01/11 às 23h | alta | F6 seção 11 |
| 53 | 1 story à mão obrigatório por dia | média | fato 66; seção 2 |
| 54 | Objeção pede resposta por texto, sem enquete | baixa | fatos 56 e 67 |
| 55 | A meta de respostas do D4 é 1x a base, não 2x | alta | conferência C7 |
| 56 | Caixa de pergunta só com folga | média | seção 2.2 |
| 57 | Frase de efeito às 17h30 todo dia, do banco com fonte | média | F6 seção 6 |
| 58 | Story de 20h30 em 02/11: "Chegou aqui pela TV Câmara? Responde este story" | média | F8 seção 5.2 |
| 59 | Link do teste com `o=ig-tv` na semana da TV | baixa | palpite 12; fato 130 |
| 60 | Desligar as 5 de conta toda e a ETAPAS de story antes do tl01 | alta | fato 114; palpite 46 |
| 61 | Uma TABULEIRO de conta toda com texto genérico | média | F8 R7 |
| 62 | Pulo abaixo de 60% junto com 150 no portão da palavra | baixa | fato 122 (n de 1 de cada lado) |
| 63 | `alsoMatchInDms` ligado na TABULEIRO de conta toda | baixa | fato 114 |
| 64 | Link da bio para `/tabuleiro/?o=ig-bio` até sex 30/10 | média | fatos 128 e 132 |
| 65 | `linkTracking` ligado na TABULEIRO | baixa | palpite 51 |
| 66 | `&p=dentista` no botão da TABULEIRO hoje | média | fato 129 |
| 67 | Um pedido por legenda; car01 só com o direct | média | fato 148; F8 R8 |
| 68 | po01 com "Comenta qual delas." | alta | fato 80 |
| 69 | Pedido de área sempre no direct | média | fato 94 |
| 70 | 5 números de segunda do Bruno em 10 min | média | F8 seção 9 |
| 71 | "Feito ou não feito" por item no arquivo da semana | alta | critério do D3 |
| 72 | Copiar mc02 a mc04, ob01 a ob03 e a fonte para o Drive | alta | fato 110 |
| 73 | Um pacote semanal de aprovação numa mensagem | média | seção 2 |
| 74 | Semana agendada até sexta; portão só cancela ou troca | média | seção 6 D3 |
| 75 | Teto de 3 cortes da TV por semana a partir da S3 com peça de frente pronta | baixa | seção 2.3 |
| 76 | TV como prova permanente: destaque NA TV sem logo e com link, linha na bio | média | F6 seção 8; fato 68 |
| 77 | Saldo de seguidores até 08/11 só fecha em 11/11 | alta | derivar 5; fato 140 |
| 78 | Responder à mão os comentários de profissão do Dentista B no mesmo dia | média | fato 94 (fala promete resposta) |
| 79 | Agência confere CFN 856 e ABAC antes do bloco 1; senão só versão sem a linha | média | fato 103 |
| 80 | Manter 1 reel pronto de reserva para sequência de estouro (ob03) | média | playbook (F5 seção 9) |
| 81 | pb01 com 171 views em 24 h sobe o pb02 para qua 28/10 | baixa | F2 seção 9.3 |
| 82 | Dentista B em DOBRAR manda a sequência para nicho gravado, não para o C | média | fato 101; F7 seção 6.3 |
| 83 | Ouvir "Ainda. Sempre vai ser." no ci01 antes do convite | alta | fato 91 |
| 84 | Uma mensagem à Mirna com as 5 perguntas, hoje | alta | a buscar 1, 3 e 4 |
| 85 | Agentes releem a grade de 02/11 às 08h de 31/10, 01/11 e 02/11 | alta | fato 133 |

---

## 8. Pre-mortem desta cadeira

Escrito como se fosse 23/11 e o plano tivesse falhado.

1. **O ok semanal não veio.** Os pacotes ficaram sem resposta; a agência não agendou; os stories voltaram a sair à mão quando o Bruno lembrava. O plano dependia de 1 toque por semana e nem esse saiu [HIPÓTESE; base: 37,5% de execução, fato 125]. Sinal precoce: pacote S1 sem ok até ter 27/10.
2. **Nenhuma gravação.** As 4 semanas viraram cortes de perfil; a família TV caiu em PARAR em 02/11 ou 09/11; a vaga do Bruno de frente foi preenchida por remake em 720p, que repetiu fala vista há 1 mês. Sinal precoce: bloco 1 vazio em qua 28/10.
3. **A Mirna pediu para não publicar antes de 02/11, ou não respondeu.** pb01, car01, po01 e pb02 saíram sem o print; ela se incomodou com a série. O plano não tinha alternativa pronta para mover 4 peças em 48 h. Sinal: resposta dela até dom 25/10.
4. **O corte de perfil se comportou como a animação** (pulo acima de 75%). O plano demorou até 02/11 para parar a família porque exigia n de 2, e 6 reels da S1 já tinham saído.
5. **O feriado esvaziou a semana da exibição** e o ci01 de 03/11 saiu depois do pico de procura, que foi na própria segunda. A cadeira trocou alcance por leitura limpa e perdeu a janela [HIPÓTESE; alcance em feriado sem dado].
6. **A objeção por resposta não respondeu.** Sem enquete, as respostas caíram para 0 ou 1 por semana; a medição de objeção sumiu e o D4 falhou no número que o próprio plano escolheu.
7. **Trial Reel não era elegível** e o Bruno não postou pelo app; os 3 remakes não saíram; o Plano Z ficou sem o Bruno de frente.
8. **A TABULEIRO nunca ligou** porque nenhum post passou 150; o caminho até o diagnóstico ficou só na bio, com 1,57% de clique sobre 74 visitas por semana [FATO, fato 14 e 15].
9. **A agência errou num pacote** (legenda com "foi ao ar" antes da hora, @ errado, arquivo velho do pf01 [FATO, fato 85]) e o Bruno, sem tempo de revisar, aprovou. Execução delegada sem conferência.
10. **O estoque sumiu da pasta temporária** antes da cópia para o Drive (mc02 a mc04, ob, fonte de 958 MB) [FATO, fato 110]; refazer custa cerca de 3 h 15 min [FATO, fato 111].

---

## 9. Previsões numéricas

Todas [PRIOR] salvo indicação; base entre parênteses.

| # | Métrica | Previsão | Faixa | Conferência |
|---|---|---|---|---|
| 1 | Reels de feed publicados de 25/10 a 21/11 (`ig_posts`) | 16 | 12 a 20 | D+30, seg 23/11/2026 |
| 2 | Reels com o Bruno de frente para a câmera no feed, 25/10 a 21/11 | 2 | 0 a 7 | D+30, 23/11 |
| 3 | Seguidores (`ig_account_stats`), base 1.618 | 1.630 | 1.600 a 1.670 | D+30, 23/11 |
| 4 | Saldo de seguidores de 25/10 a 08/11 (`ig_follower_growth`), base -5 em 10 dias | +3 | -6 a +20 | qua 11/11 |
| 5 | Visitas ao perfil por dia, média de 02 a 04/11, base 10,6 | 14 | 8 a 30 | seg 09/11 |
| 6 | Mediana de alcance em 48 h dos cortes da TV de perfil (pb01, po01, pb02, ci01, ob) | 45 | 25 a 110 | D+30, 23/11 |
| 7 | Disparos de TABULEIRO de terceiros até 22/11, base 0 | 0 | 0 a 2 | D+30, 23/11 |
| 8 | Rodadas do Módulo 7 registradas de 26/10 a 23/11 | 4 de 5 | 3 a 5 | D+30, 23/11 |
| 9 | Itens da lista do Bruno feitos, S1 a S4, base 37,5% | 50% | 30% a 70% | D+30, 23/11 |
| 10 | Views de story em 7 dias lidas em seg 23/11 19h, base 1.041 | 1.000 | 750 a 1.350 | D+30, 23/11 |
| 11 | Views da edição do Bruno na página do programa (mediana das edições 80,5) | 120 | 30 a 600 | D+30, 23/11 |
| 12 | Blocos de gravação entregues até qua 18/11 | 1 | 0 a 4 | qua 18/11 |
| 13 | Seguidores | 1.645 | 1.590 a 1.720 | D+60, qua 23/12/2026 |
| 14 | Disparos de TABULEIRO de terceiros acumulados desde 25/10 | 1 | 0 a 5 | D+60, 23/12 |
| 15 | Diagnósticos de 30 min agendados desde 25/10 (número do Bruno; sem o número, "sem dado") | 1 | 0 a 3 | D+60, 23/12 |
| 16 | Seguidores | 1.660 | 1.580 a 1.780 | D+90, sex 22/01/2027 |
| 17 | Reels com o Bruno de frente acumulados desde 25/10 | 6 | 0 a 20 | D+90, 22/01/2027 |
| 18 | Cortes da TV ainda no banco, sem publicar | 4 | 0 a 8 | D+90, 22/01/2027 |

---

## 10. O que mudaria a opinião desta cadeira

| Se | Então |
|---|---|
| A Mirna ou a produção pedir nada antes de 02/11 | Opção (b) do D1 para pb01, car01, po01 e pb02; a S1 fica com tl01, car02, tl02 e o que houver de nicho ou remake |
| O print vier com ok para antes e o horário for entre 20h e 22h | ci01 volta para seg 02/11, depois do fim do programa |
| O bloco 1 chegar até qua 28/10 | Plano A na S2; ob01 vai para a S3 |
| tl01 ou pb01 com 106 ou mais e pulo abaixo de 60% | A família TV ganha DOBRAR; o teto de 3 cortes por semana sai |
| pb01, po01 e pb02 abaixo de 42 ou com pulo acima de 75% | Família TV em PARAR em 02/11; S2 só com ci01, mais votado (como story) e o Bruno de frente |
| Execução da lista acima de 80% na S1 | Molde F6 cheio na S3 (enquete à mão de volta; caixa semanal) |
| A API aceitar Trial Reel | R2 e R3 entram; o remake no feed da vaga Z espera o resultado do Trial |
| O app deixar marcar pessoa em reel publicado | Marcação na mídia vira camada 2 |
| A objeção por resposta der 0 em 7 dias | Enquete volta à mão na semana seguinte |
| Alguém de fora disparar a TABULEIRO | A automação de conta toda vale também para os posts de nicho seguintes |

---

## 11. Lacunas

- Horário da exibição de 02/11; se a edição reprisa; quando sobe no site; minuto em que o Bruno aparece (a buscar 1 e 2).
- @ da Mirna, print, ok da produção para antes de 02/11, aceite de colaboração (a buscar 3 e 4).
- Se o app deixa marcar pessoa em reel publicado; se o @ pela API avisa a pessoa (a buscar 5 e 6).
- Elegibilidade a Trial Reel pela API; desempenho de Trial nesta conta (a buscar 7).
- Sessão de gravação, minutos reais por roteiro, minutos do Bruno por story à mão (a buscar 20 e 29).
- Nota de 0 a 10 por efeito nas folhas de ob01 a ob03 (conferência C2).
- Quadro aos 0 e 2,5 s de tl04 e tl05 (só ficha).
- Qual arquivo do pf01 vale (fato 85).
- Votos do tl01 (a buscar 12).
- Alcance da conta em feriado com reel do Bruno (a buscar 35).
- Desempenho do corte da TV de perfil: n de 0.
- Respostas por story com pedido de resposta em texto: sem dado até a S1 rodar.
- Números do GA4, WhatsApp e diagnósticos (a buscar 25 e 26).
- Status das leituras da OAB, CFN 856, ABAC, CFP e CFO 196/2019 (a buscar 21).
- Autorização da Tzur (a buscar 22).
- Cópia no Drive do estoque (a buscar 24).
- Se o Bruno responde o pacote semanal em até 24 h.

---

## 12. Fontes

- Livro de fatos `run/01-fatos.md` (15h50) e enquadramento `run/00-enquadramento.md` (14h45); `contexto.md` (14h40).
- Frentes: `run/01-pesquisa/F4-entrevista-tv.md` (seções 0 a 10), `F5-capacidade-e-estoque.md` (inteira), `F6-stories-e-objecoes.md` (seções 3 a 11), `F7-horarios-e-portao.md` (seções 4 a 6), `F8-funil-diagnostico.md` (seções 5 a 10), `F2-playbook-buzzfy.md` (seções 9.3 a 10.7).
- Repositório: `/home/user/Disparo-/CLAUDE.md`; `conteudo/stories-objecoes/03-plano-7-dias.md` (cabeçalho, mapa, 25 e 26/10, ob01 a ob03); `conteudo/entrevista-tv-camara/catalogo-formatos.md` (linhas 19, 228 a 252, 557 a 588); `conteudo/entrevista-tv-camara/pecas-e-calendario.md` (linha 153); `videos/tv-camara/cortes/mc04.spec.json` (disco, 16h25).
- Conferências desta cadeira, só leitura, 16h20 a 16h30: `date`; `git log` e `git show --stat 318e97d`; `git status` de `videos/tv-camara/cortes/`; `find`, `stat` e `ffprobe` em `scratchpad/tv/render/` e `scratchpad/tv/ig/` (ob01 a ob03, mc02, mc04); quadros aos 0 e 2,5 s das versões leves de ob01 a ob03 (extraídos para conferência visual e apagados em seguida; nada ficou fora desta pasta); `scratchpad/tv/rev_ob/conferir.txt`.
- Nenhuma consulta a Buzzfy ou PostZen foi feita por esta cadeira: os números de conta vêm do livro de fatos e das frentes, com a hora de coleta delas.
