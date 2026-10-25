# 07 · Red team · Cronograma de 25/10 a 22/11/2026 · O Estrategista (@o_estrategista.com.br)

> **Este red team é outra instância do mesmo modelo que escreveu as cadeiras, os juízes e o plano. É autocrítica estruturada, não verificação independente. Onde o conselho disse "sim", este documento procurou de propósito o "não".**

Sábado, 24/10/2026, das 20h17 às 20h45 (São Paulo). Alvo: `run/06-plano-final.md`.

**Lido inteiro:** `run/06-plano-final.md`, `run/01-fatos.md`, `contexto.md`, `/home/user/Disparo-/CLAUDE.md`, `run/07-verificacao/V1.md` e `V2.md` (para não repetir o que os verificadores já apontaram e para usar o que eles leram às 20h10). Trechos: `run/00-enquadramento.md` (seções 1 a 3 e critérios de sucesso), `stories-objecoes/06-agenda-postzen.md` (nota da pausa).

**Leituras próprias, só leitura, de 20h17 a 20h25:** PostZen `listPosts` e `listCommentAutomations` da conta j97772ycndetk3f1wcdbh14p898g4b8w; Buzzfy `ig_follower_growth` (14 dias), `ig_posts` (stories ativos) e `ig_post_stats` dos 7 stories de hoje; `gh api` do repositório (visibilidade); `git grep`, `ls`, `du` e `df` no disco; 2 buscas na web e 1 página de jornal lida (eleição). Nada foi publicado, agendado, alterado ou enviado. A única escrita é este arquivo.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha uma objeção sozinho. "Fato N" aponta para `run/01-fatos.md`; "V1 Pn" e "V2 item n" para os verificadores. Métrica que falta: "sem dado".

---

## 0. O que esta leitura achou e o plano não tem

1. **Domingo, 25/10, é o 2º turno da eleição para presidente.** "O segundo turno está marcado para domingo, 25 de outubro", com Flávio Bolsonaro e Lula na disputa [FATO nível 3, tribunadejundiai.com.br, matéria de 04/10/2026 20h57, lida às 20h18]. São Paulo não tem 2º turno para governador [FATO nível 3, resumo de busca, 20h18], mas Campinas vota para presidente. O plano põe o reel do case às 21h e a chamada dele às 20h30 desse domingo, que já estão agendados [FATO, `listPosts` 20h19: m17184z919q3m3k3p130658phh8gwc29 para 2026-10-26T00:00Z e m173vxc7ttk8ceqzxdnbk8days8gx44h para 2026-10-25T23:30Z]. Só a cadeira A citou o 2º turno (ideia 60: "25/10, 2º turno: nada político; leitura do tl01 com cautela"); o enquadramento, o livro de fatos, os juízes e o plano final não falam dele [FATO, `grep` por "turno" em `run/`, 20h26]. A janela de 48 h do Dentista B (sáb 21h a seg 21h), que decide o portão G1 e a linha de nicho, cobre o domingo inteiro.
2. **Os 7 stories de hoje tiveram 0 resposta.** Alcance provisório por story, do primeiro ao último: 58 (09h33), 50 (14h00), 49 (14h03), 47 (15h00), 43 (15h01), 36 (16h30), 21 (18h00, com 2,3 h de vida); 0 resposta, 0 compartilhamento, 0 seguidor e 1 visita ao perfil somados [FATO, `ig_post_stats` 20h20, provisório]. A base do D4 tinha 3 respostas em 7 dias [fato 56].
3. **As 6 automações de conta toda seguem ligadas.** 17 ativas; CASE ("case", "caso"), ESTRATEGISTA, ETAPAS, FUNIL e CAIXA em comentário e ETAPAS em resposta de story, todas sem post; TABULEIRO com 0 disparo; CHECKLIST com 1 [FATO, `listCommentAutomations` 20h19]. A CASE e a ESTRATEGISTA mandam "diagnóstico gratuito de 30 minutos" no direct [FATO, mesmo retorno].
4. **Seguidores, 10 a 21/10: 5 entradas, 7 saídas, saldo -2; 22 e 23/10 ainda pendentes** [FATO, `ig_follower_growth` 14 dias, 20h19].
5. **O repositório é público e cita terceiros.** Visibilidade "public" [FATO, `gh api` 20h22]. Dos 773 arquivos rastreados, 97 citam o nome da empresa do cliente do case e 49 citam a repórter [FATO, `git grep` 20h23], incluindo análises de "risco de relação" com ela [FATO, `git grep`: `01-fatos.md`, `F4-entrevista-tv.md`, `plano-B.md`]. Este arquivo também vai para lá se for commitado; por isso ele não repete o nome da empresa.
6. **O estoque pronto mora numa pasta que o Bruno não alcança.** Os renders da TV (ci01, mc02, mc04, ob01, ob02, ob03, pb01, pb02, pf01, po01, tl01 e o case) estão em `scratchpad/tv/ig/` dentro do contêiner desta sessão; a pasta ocupa 12 GB e o disco tem 10 GB livres [FATO, `ls`, `du` e `df` 20h17]. O plano manda o Bruno copiar para o Drive (seção 4, sáb 24/10 à noite), mas o Bruno não tem acesso de arquivo a esse contêiner [HIPÓTESE forte: a pasta fica em `/tmp/claude-0/...` da sessão na nuvem], e o Drive está fora das ferramentas desta rodada [fato 143]. Os ob01 a ob03 já existem como mp4 (o livro de fatos dizia "render final sem dado", fato 97). O PostZen guarda cópias comprimidas das peças que estão em rascunho [FATO, `listPosts`; fato 84]; mc02 e mc04 não estão lá [fato 86]; ob01 a ob03 no PostZen: sem dado nesta leitura.
7. **Tamanho do plano contra quem executa.** 15.601 palavras, 32 condições escritas como "só com", "só se", "só quando" ou "só depois", 20 linhas com dono "Bruno" na seção 4 e 16 decisões do cliente na seção 7 [FATO, contagem em `06-plano-final.md` às 20h22]. A execução medida da rodada anterior foi de 3 "sim" em 8 [fato 125].
8. **O próprio plano prevê o fracasso como cenário central.** Chance de cumprir o critério inteiro: D1 0,10; D2 0,20; D3 0,08; D4 0,10; D5 0,08; e chance de 1 conversa de 30 min até 18/11 de 0,15 [FATO, `06-plano-final.md`, seção 2; números sem etiqueta, V1 P2]. O pre-mortem abaixo descreve o caminho mais provável, não uma cauda.

---

## 1. Pre-mortem: domingo, 22/11/2026, o plano fracassou

**Como parece o fracasso.** Nenhuma conversa de 30 min agendada pelo Instagram. Saldo de seguidores de 28/10 a 10/11 abaixo de 12. A série da TV saiu pela metade, tarde, ou não saiu. O feed teve semanas com 1 ou 2 reels e várias "vagas vazias com motivo". O Módulo 7 registrou rodadas com quase tudo em TESTAR ou "não testado". A régua de 23/11 não tem dado para decidir a S5.

| # | Causa | Mecanismo | Evidência de hoje | Sinal precoce (data) | Chance [PRIOR] |
|---|---|---|---|---|---|
| 1 | O Bruno não gravou | O D2 pede 1 bloco por semana. Com a TV pausada, o único estoque com o Bruno de frente é o case e 3 remakes; sem bloco, a grade de 5 reels vira 1 ou 2 | 36,4 s gravados de 21/10 13h12 a 24/10 15h15 [fato 104]; sessão de 90 min do plano de 21/10 não aconteceu [fato 105]; dia do bloco 1 sem dado [a buscar 20] | sem dia marcado até seg 26/10 12h; sem arquivo até qua 28/10 23h59 | alta |
| 2 | A série da TV não entrou, ou entrou e saiu | Pausa sem motivo registrado; liberação só verbal da repórter, enquanto os termos dizem que o titular é a Câmara e que pedidos vão à Assessoria de Imprensa [V2 item 2; fato 137]; data da 1ª exibição incerta (na semana de 19/10 a edição nova só entrou na TV na terça, 01h [V2 item 4]) | pausa às 18h45 [FATO, `06-agenda-postzen.md`]; peças da TV em rascunho às 20h19 [FATO, `listPosts`] | nenhuma ordem escrita até sex 30/10 17h; nenhum pedido feito à assessoria até seg 26/10 | alta |
| 3 | O plano era maior do que a pessoa que executa | 16 decisões do cliente, 7 prazos só no domingo (08h30, 09h02, 10h, 16h, 18h29, 20h e 21h). Cada "sem resposta" tem padrão, então o padrão vira o plano: pausa mantida, case como está, automações ligadas, rótulo trocado | item 7 da seção 0; 3 "sim" em 8 [fato 125] | menos de 4 dos 7 prazos de domingo cumpridos até 21h | alta |
| 4 | A meta nunca esteve ao alcance do canal | Com cerca de 11 visitas por dia e 1,57% de clique, o perfil entrega perto de 5 cliques por mês [ESTIMATIVA: 317 visitas x 1,57%, derivar 14]; 10 conversas pedem 637 visitas com 100% de conversão [derivar 14]. Nada no plano cria demanda fora do Instagram | 577 contas, 2 comentários e 0 clique em 7 dias [FATO, `ig_account_stats` 19h42, plano seção 0]; 0 conversa comercial em 50 directs [fato 124]; 0 venda [fato 8] | 0 clique no site na leitura de seg 02/11 | alta |
| 5 | Calendário hostil | 2º turno em 25/10, possível contestação na semana seguinte (em 2022, bloqueios de estrada de 31/10 a 04/11, com pico de 420 trechos em 01/11 [FATO nível 3, PRF citada pelo Diário do Nordeste e pelo InvestNews]), Finados em 02/11, feriados em 15 e 20/11, Black Friday em 27/11 [PRIOR: campanhas de novembro disputam atenção]. As leituras de 48 h caem em dias atípicos e a régua classifica errado | item 1 da seção 0 | Dentista B com 48 h abaixo de 42 na seg 26/10 21h05 | média |
| 6 | Automação disparou onde não devia | CASE casa com "caso", palavra comum ("no caso", "caso queira"); ESTRATEGISTA casa com elogio ("parabéns, estrategista"). Na volta da TV, comentário de parabéns recebe direct de venda e gasta a única resposta privada daquele comentário [fato 120; hipótese 46] | 6 de conta toda ligadas às 20h19 [FATO]; decisão de 21/10 de parar palavras-chave não executada [fato 125] | qualquer log de CASE ou ESTRATEGISTA em post que não seja o case | média |
| 7 | O Módulo 7 ficou cego | Sem gravação e com a TV pausada, quase todo formato fica com n de 0 ou 1 até 23/11; a regra pede n de 2 para PARAR ou DOBRAR. A base de 53 vem de outra janela; a atual é 37,5 [fato 23 e 24]. Ninguém tem a tarefa de abrir a sessão das rodadas (dono "agentes", sem agendamento escrito) | plano, D5; seção 4 tem 3 linhas de "agentes" e nenhuma diz quem dispara | rodada de seg 26/10 21h05 sem registro em `semanas/2026-10-26.md` até ter 27/10 12h | média |
| 8 | Volume de stories sem resposta | 26 a 30 stories por semana na S1 [plano D4; V1 P18], com "balão" e "virada" todo dia útil. O pedido não gera resposta e a pilha cansa | 7 stories hoje, 0 resposta; alcance cai de 58 no 1º para 36 e 21 nos últimos (provisório) [FATO, `ig_post_stats` 20h20]; 7 respostas em 30 dias [fato 57] | 0 resposta nos balões de seg 26 a qua 28/10 | média |
| 9 | Repetição punida | Dentista C é a 3ª edição da mesma fala [fato 101]; R2 e R3 já têm legenda, então ganham no máximo 1 mudança real [V2 item 6]; ob02 usa 82% do áudio do pf01 [derivar 23]. O playbook diz que o Instagram limita alcance de repetição [V2 item 6] | estoque fora da TV é quase todo repetição | Dentista C ou R1 abaixo de 27 em 48 h | média |
| 10 | Estoque perdido ou reputação exposta | Contêiner reciclado leva 12 GB de renders; repositório público com 97 arquivos que citam o cliente do case e 49 que citam a repórter é achado por um dos dois | itens 5 e 6 da seção 0 | cópia do estoque sem executor definido até dom 25/10 | baixa, impacto alto |

**Conta de composição** [ESTIMATIVA]: o plano dá 0,35 de chance de a família da TV fazer 42 ou mais em 48 h (D1), logo 0,65 de ela ficar fora do feed ou em PARAR. Se a chance de o Bruno deixar de gravar em 2 ou mais das 4 semanas for de 0,6 [PRIOR], e as duas coisas forem independentes, a chance de S3 e S4 terem 2 reels ou menos por semana fica perto de 0,6 x 0,65 = 0,39. Não são independentes de verdade (se a pausa cair, o Bruno pode gravar mais por causa da TV), então o número é só ordem de grandeza.

---

## 2. Piores casos por decisão

| Decisão | Pior caso | O que reduz o dano |
|---|---|---|
| D1 Série da TV | (1) A pausa cai, as peças saem antes de 02/11 com a repórter marcada, e a Assessoria de Imprensa da Câmara, titular do conteúdo [V2 item 2], pede a retirada por uso sem autorização prévia em perfil comercial. As peças somem na semana da exibição e a repórter fica exposta por ter liberado o que não era dela liberar [HIPÓTESE]. Em Campinas estão 53% dos engajados [fato 19]: o constrangimento é local e visível | pedido escrito à assessoria antes de qualquer peça; sem resposta, a TV entra só como link da edição oficial e destaque sem trecho |
| D1 Série da TV | (2) A edição não estreia em 02/11 (estreia de madrugada na terça, como na semana de 19/10 [V2 item 4], ou muda de semana). As legendas do tl01 e do tl02 dizem "A entrevista vai ao ar na segunda, 02/11." [fato 77 e 78] e o story de 21h10 pergunta "Chegou pela TV Câmara?" numa noite sem exibição | tirar a data das legendas até ter a grade publicada; a chamada de 02/11 só com horário de fonte |
| D2 Gravação | (1) Nenhum bloco até 22/11. A conta passa 4 semanas sem o único formato que mede bem [fato 25], com seguidores já em -2 nos 14 dias lidos hoje [FATO, `ig_follower_growth` 20h19] | grade sem gravação como padrão (seção 8, item 4); gravação como bônus |
| D2 Gravação | (2) O Bruno grava nicho de saúde e a fala bate numa norma de conselho (a CFN 856, em vigor, veda mostrar resultado de si ou de terceiros na divulgação de método [V2 item 5]). Profissionais da área apontam o erro nos comentários; a linha de nicho perde credibilidade com o público que ela quer | norma lida antes de gravar, como o plano já pede; frase de caso fora de roteiro de saúde |
| D3 Grade | (1) O ok de sexta falha 2 vezes seguidas; a agência não agenda; semanas com feed parado e stories só dos já agendados | ok tácito: o que a agência mandar até quinta 18h e o Bruno não vetar até sexta 18h vai ao ar |
| D3 Grade | (2) O piso de 3 reels empurra repetição (Dentista C, remakes com 1 mudança) e o alcance cai abaixo de 27, puxando a mediana semanal da S2 e da S3 | piso de 3 só com peça nova; repetição conta como TESTAR, fora do piso |
| D4 Stories | (1) 26 a 30 stories por semana, 0 resposta, alcance por story caindo de cerca de 50 para cerca de 20; o público aprende a pular a pilha | teto de 4 stories por dia até haver 3 respostas em uma semana |
| D4 Stories | (2) As respostas chegam, a ETAPAS está desligada e o Bruno não responde em 24 h: quem levantou a mão some | resposta em lote 2 vezes por dia, em horário fixo, ou manter a automação de resposta com texto sem venda |
| D5 Portão | (1) As 5 rodadas saem com n de 0 ou 1 em quase todo formato; o ciclo termina sem nenhum PARAR nem DOBRAR com fundamento | regra de "decisão com n de 1" para o que é barato reverter (tirar do feed, mover hora) |
| D5 Portão | (2) A base de 53 manda para PARAR um formato que, sobre a base atual de 37,5, estaria em MANTER (mediana entre 30 e 42). A família da TV sai do feed por um corte de régua, não por desempenho | ler as duas bases e só fechar PARAR quando as duas concordarem |
| D6 TABULEIRO | (1) As 6 de conta toda seguem ligadas (como às 20h19). A repórter, a emissora ou um conhecido comenta "caso" ou "estrategista" num post da TV e recebe direct automático com "onde o seu dinheiro está vazando"; o print circula | desligar as 6 antes de qualquer post da TV; se não forem desligadas, a TV não volta |
| D6 TABULEIRO | (2) 0 disparo de terceiro e 0 conversa até 18/11, e a rodada conclui "palavra-chave não funciona" quando o problema é volume (577 contas por semana) e canal | separar na leitura "falta de gente" de "falta de pedido"; abrir uma frente fora do Instagram (seção 8, item 9) |
| Reel do case (seção 7, item 2) | (1) O cliente ou o responsável de marketing pede a retirada (nome, logo, faturamento, imagem), ou um comprador procura a empresa e não acha registro público [V2 item 3] e lê "1.282 comentários" da interface recriada como prova social inventada | autorização escrita do cliente; tirar o número de comentários do cartão |
| Reel do case | (2) Sai às 21h da noite de apuração do 2º turno. As 48 h ficam rebaixadas e entram na régua como dado do formato "Bruno de frente", que sustenta o plano inteiro | mover para seg 26/10 21h (vaga livre com a pausa) ou ler as 48 h fora da régua |

---

## 3. Atores irracionais (ou racionais com interesse contrário)

| Ator | Comportamento | Efeito no plano | Defesa barata |
|---|---|---|---|
| Assessoria de Imprensa da Câmara (titular do conteúdo) | não responde por semanas (órgão público), ou responde "não" para uso em perfil comercial [V2 item 2; fato 137] | a porta do D1 nunca abre; o maior estoque pronto não sai | pedir hoje por escrito; o plano roda sem a TV por padrão |
| A repórter | muda de ideia ao ver efeitos sobre o rosto (tl04 com "Uau!" recortado, tl05 com carimbo "AINDA?" e selo "REPÓRTER" [fato 90]) ou é cobrada pela chefia por ter liberado [HIPÓTESE] | pede para tirar tudo, inclusive o que já saiu | nenhum efeito sobre o rosto dela; marcação só depois do ok escrito |
| O Bruno como aprovador único | pausa sem motivo registrado (18h45) e decide fora do conselho (decisão do case registrada em nota lida às 19h50) [FATO, plano seção 0]; não executa o que decidiu (3 em 8) [fato 125] | o plano escrito e o plano real se separam em dias | pedir o motivo da pausa; 1 decisão por dia, não 6 |
| Cliente do case | retira a autorização ou contesta o número | reel sai do ar; "6 para 20" vira passivo | autorização escrita com nome, logo, número e imagem |
| Meta (plataforma) | reprova impulsionamento do case (alegação de faturamento na tela) [PRIOR: política de anúncio não lida]; limita direct automático se um pico de comentários com palavra comum disparar dezenas de mensagens [PRIOR]; derruba reel por denúncia de direito autoral [HIPÓTESE] | perde peça ou capacidade de responder | não impulsionar o case; desligar as de conta toda |
| PostZen e Buzzfy (fornecedores) | falha silenciosa de agendamento, desconexão do Instagram, limite de consulta (a busca de reels do Buzzfy já esgotou em 24/10 [fato 141]) | post não sai; Módulo 7 sem dado | os agentes conferem `listPosts` 1 h antes de cada post de feed; erro de consulta é "sem dado", nunca zero |
| Concorrente que corta preço | oferece diagnóstico grátis ou mentoria barata na região | baixo em 4 semanas: a porta de entrada do Bruno já é grátis ("diagnóstico gratuito de 30 minutos" [FATO, `listCommentAutomations` 20h19]); o preço da venda depois do diagnóstico é sem dado | nenhuma ação agora |
| Lead que some | faz o Tabuleiro, cai no WhatsApp e não responde, ou marca e não aparece | a única conversa do mês não vira nada | follow-up de +1, +4 e +10 dias do Módulo 6 [fato 132], com uso sem dado |
| Público em clima de eleição | comentário político no reel do case ou nos posts da semana seguinte [HIPÓTESE]; a bio tem frase religiosa [fato 9] | moderação à mão, atenção desviada | não publicar no domingo à noite; não responder política |

---

## 4. Cisnes negros

1. **Perda do estoque.** O contêiner desta sessão é reciclado antes da cópia. Os ob01 a ob03, mc02 a mc04 e os masters de alta (pb01 98,9 MB, ci01 106,0 MB, pb02 150,7 MB [fato 84]) somem; no PostZen ficam só cópias comprimidas das peças em rascunho, e nada dos mc [fato 86]. Refazer o passe custa cerca de 3 h 15 min [fato 111], se a fonte da entrevista sobreviver. Sinal: nenhuma cópia feita até dom 25/10. Defesa: definir quem copia (um agente com permissão de escrita no Drive pedida pelo Bruno, ou o Bruno baixando pelo PostZen o que estiver lá).
2. **Resultado da eleição contestado.** Em 2022, depois do 2º turno, houve bloqueios de estrada por 5 dias [FATO nível 3, PRF via Diário do Nordeste, InvestNews e Money Times]. Em 2026 isso cairia de 26 a 30/10, a semana inteira da S1. Efeito: atenção desviada, Bruno com agenda mexida, leituras de 48 h de uma semana atípica tratadas como normais.
3. **Retirada por direito autoral.** Se a emissora sobe a edição no YouTube e no Facebook com gestão de direitos, o áudio da gravação do celular do Bruno (a mesma conversa) pode casar com o áudio exibido e o reel ser silenciado ou bloqueado [HIPÓTESE; uso de gestão de direitos pela emissora: sem dado].
4. **Restrição da conta.** Ação em massa de direct automático, denúncias ou login suspeito levam a bloqueio temporário. A conta é o único canal do sistema [PRIOR].
5. **Exposição do repositório público.** O cliente do case, a repórter ou um concorrente acham arquivos que discutem faturamento sem fonte, autorização pendente e "risco de relação" [FATO, item 5 da seção 0]. Sinal: nenhum. Defesa: o Bruno decide tornar o repositório privado.
6. **O Bruno fora por 1 a 2 semanas** (saúde, família, trabalho de cliente). Ele é o único rosto e o único aprovador [PRIOR].
7. **Mudança de produto do Instagram** no meio do ciclo (Trial Reel, colaboração, regras de direct automático) ou queda geral em 02/11 [PRIOR].
8. **Cisne positivo desperdiçado.** Um reel passa de 3x o normal (171 views [derivar 3]) ou a edição da TV ganha destaque no perfil da emissora. O playbook pede a 1ª sequência em 24 h e a 2ª em 48 h [V2 item 7], mas o plano só agenda depois do ok de sexta e não tem peça de sequência pré-aprovada. A janela fecha antes da próxima rodada. Defesa: protocolo de sequência (seção 8, item 5). E com a bio do Módulo 2 só até dom 01/11, um pico de visitas antes disso cai na bio antiga com "Estrategista Digital" e link para /v2/ [fato 9 e 132].

---

## 5. Hipóteses contrárias testadas de propósito

O conselho votou "sim" em quase tudo (de 10 a 14 votos de 14 na opção vencedora, nas 6 decisões, plano seção 8). Aqui, para cada "sim" que sustenta o plano, a hipótese oposta e o que os dados dizem dela.

| O conselho aceitou | Hipótese contrária | O que os dados dizem | Veredito do red team |
|---|---|---|---|
| A TV organiza a grade de novembro | A TV rende pouco no feed e custa risco; vale como prova (link, destaque, bio) e não como reel | cortes crus de TV no mercado: 0,0055x os seguidores (n de 3) [fato 155]; edições no site: mediana de 80,5 views [fato 136]; Bruno de perfil à mesa: n de 0 nesta conta [fato 88]; o próprio D1 dá 0,35 de chance de 42 ou mais | contrária não refutada. "TV fora do feed" devia ser uma opção (e) pontuada no D1; hoje ela só aparece como critério de abandono |
| O Bruno de frente rende de 3x a 8x por ser formato | O efeito é do período | 3 dos 4 reels são de 03 a 05/10 [fato 35], semanas de +35 e +9 seguidores [fato 18], com anúncio rodando em algum momento dos 30 dias (1.907 contas [fato 10], datas sem dado [a buscar 39]); o único fora do período é o Dentista A, n de 1 (169) [fato 30]. O Dentista B não testa isso: muda o visual e repete a fala | contrária não refutada, mas também sem prova. O próximo reel novo com o Bruno de frente é o único teste; ele depende de gravação |
| 1 bloco de gravação por semana é viável | O Bruno não vai gravar com regularidade em novembro | 36,4 s em 3 dias e 90 min não cumpridos [fato 104 e 105] | contrária é a mais provável. A grade sem gravação devia ser o padrão |
| "Responde este story" gera resposta | O pedido diário não gera resposta nesta conta | 7 stories hoje, 0 resposta [FATO, 20h20]; 7 respostas em 30 dias [fato 57]; o plano dá 0,15 para a meta de 12 | contrária favorecida. O teste de seg a sex do D4 resolve; enquanto isso, não somar stories |
| Reel é o formato de feed que importa | Estático com foto do Bruno rende parecido e não pede gravação | estáticos "Prazer" e bastidor com 237, 197 e 133 de alcance e 34 das 48 visitas vindas do feed [fato 53]; feed com foto: mediana 111 e 23 visitas, contra 34,5 e 1 do texto [fato 51]. Ressalva: o "Prazer, mineiro" é de 30/09, colado no pico de seguidores de 29/09 [fato 16 e 53] | hipótese a testar, barata: 1 estático de foto por semana fora da conta dos carrosséis |
| TABULEIRO por post é o caminho até o diagnóstico | A palavra-chave não move nada aqui; o diagnóstico vem da rede local do Bruno | 19 peças com palavra-chave, 3 comentários [fato 122]; 0 de 9 estouros de contas até 6 mil seguidores usou palavra-chave [fato 164]; 0 conversa comercial em 50 directs [fato 124]; Campinas tem 53% dos engajados [fato 19]; origem dos clientes atuais: sem dado | contrária não refutada. Teste: o Bruno escreve de onde vieram os últimos 5 clientes (10 min) |
| Domingo à noite é bom horário (fim de semana 1,10x [fato 152]) | Domingo, 25/10, à noite é o pior horário do mês | 2º turno presidencial em 25/10 [FATO nível 3]; resultado costuma sair no começo da noite [PRIOR] | contrária vence por precaução: mover custa 0 |
| "Pode seguir" não levanta a pausa | A pausa era para esperar o conselho refazer as datas, e não um veto ao conteúdo | a pausa (18h45) veio cerca de 4 h depois da data nova (14h40) e logo depois do último juiz (18h44), enquanto o conselho refazia as datas [FATO, horários no plano, seções 0 e 8]; motivo sem dado | indecidível sem o motivo; uma pergunta de uma linha resolve. Se for isso, a porta do D1 atrasa a S1 sem razão |

---

## 6. Teste de premissas

Nota: SOLIDA (os dados sustentam e é difícil virar), ABALAVEL (há dado, mas pequeno ou confundido), FRAGIL (palpite, contradita por dado, ou depende de alguém que ainda não respondeu). Nível de evidência: 1 dado primário do cliente; 2 ferramenta oficial ou fonte primária de terceiro; 3 fonte secundária; 4 palpite.

### D1. Série da TV

| Premissa | Nota | Nível | Impacto | Como testar barato |
|---|---|---|---|---|
| A pausa cai até sex 30/10 | FRAGIL | 4 | alta | perguntar ao Bruno o motivo da pausa, não só "cai ou fica" (2 min) |
| A liberação verbal da repórter basta para publicar | FRAGIL | 2 | alta | pedido escrito à Assessoria de Imprensa pelo canal da página /equipe (Bruno, 10 min) [V2 item 2] |
| A 1ª exibição na TV é seg 02/11 | ABALAVEL | 1 | media | perguntar à repórter "horário e canal da 1ª exibição"; os agentes leem /programacao/2026-11-02 quando sair |
| As peças com o Bruno de perfil fazem perto de 50 de alcance em 48 h | FRAGIL | 4 | media | publicar 1 peça da TV como Trial Reel antes de pôr a série no feed (só com a pausa levantada) |
| O "antes" (convite e bastidor) rende mais que o "depois" | FRAGIL | 2 | baixa | nenhum barato; aceitar como indício (n de 3 por fase [fato 155]) |
| A TV dobra as visitas ao perfil de 02 a 04/11 | FRAGIL | 2 | media | visitas em 7 dias na seg 09/11 contra 77 [V1 P5] |

### D2. Gravação, nicho, Dentista C e remakes

| Premissa | Nota | Nível | Impacto | Como testar barato |
|---|---|---|---|---|
| O Bruno grava de 24 a 36 min por semana | FRAGIL | 1 | alta | 5 min de aberturas de frente até seg 26/10 (o piso do próprio plano) |
| O efeito do Bruno de frente é do formato, não do período | ABALAVEL | 1 | alta | o próximo reel novo com o Bruno de frente, lido em 48 h; o Dentista B não serve |
| Remake recupera alcance (35% com original de 5x ou mais) | FRAGIL | 2 | media | R1 como Trial Reel; os 35% foram medidos em Trial Reel [V2 item 6] e Trial de conta pequena bate o usual em 21% [fato 151] |
| O Dentista C se beneficia da sequência do B | FRAGIL | 2 | baixa | nenhum: o 1,81x é de depois de estouro de 5x e em 24 h a 48 h [V2 item 7] |
| As normas dos conselhos não travam os roteiros | ABALAVEL | 3 | media | a agência lê CFN 856, CFO 196/2019 e 118/2012, CFP e o provimento da OAB antes de cada gravação (30 min) |

### D3. Grade

| Premissa | Nota | Nível | Impacto | Como testar barato |
|---|---|---|---|---|
| Existe peça aprovada para 5 vagas de reel por semana | FRAGIL | 1 | alta | contagem do estoque aprovado toda quinta 18h, antes do ok |
| O Bruno dá o ok semanal na sexta 18h | FRAGIL | 1 | alta | a 1ª sexta (30/10); trocar por ok tácito se faltar |
| A hora pesa pouco e o formato pesa muito | ABALAVEL | 1 | baixa | só animação foi testada por hora [fato 40]; aceitar |
| Feriado e dia de eleição não derrubam alcance | FRAGIL | 1 | media | 3 pares de animação em 1 feriado [fato 41]; tratar 25/10, 02/11, 15/11 e 20/11 como dias fora da régua |
| Carrossel com foto do Bruno segura a grade sem gravação | ABALAVEL | 1 | media | mediana 111 com foto contra 34,5 sem [fato 51]; ler car02 e car03 em 48 h |

### D4. Stories e ob01 a ob03

| Premissa | Nota | Nível | Impacto | Como testar barato |
|---|---|---|---|---|
| "Responde este story" gera resposta acima da base | FRAGIL | 1 | media | 5 leituras de seg a sex já previstas no D4; hoje: 0 em 7 stories |
| O Bruno responde em 24 h e faz 2 itens à mão por dia | FRAGIL | 1 | media | lista "feito" da S1 lida na seg 02/11 |
| Volume de stories não derruba o alcance por story | ABALAVEL | 1 | baixa | contas de story em 7 dias toda segunda contra 342 |
| Os pilares substituem a TV como prova | FRAGIL | 4 | baixa | alcance dos stories de pilar contra o dos stories de TV de hoje, na mesma posição da pilha |
| O rótulo "O QUE EU MAIS OUÇO" é verdadeiro | ABALAVEL | 1 | baixa | marcação do Bruno nas 6 frases (0 objeção escrita registrada [fato 127]) |

### D5. Portão do Módulo 7

| Premissa | Nota | Nível | Impacto | Como testar barato |
|---|---|---|---|---|
| A base de 53 é a referência certa | ABALAVEL | 1 | alta | classificar cada rodada também sobre 37,5 e anotar onde as duas discordam |
| Haverá n de 2 ou mais por formato até 23/11 | FRAGIL | 1 | alta | contar, na rodada de 02/11, quantos formatos têm n de 2 |
| As rodadas acontecem no horário | FRAGIL | 4 | media | o Bruno diz quem abre a sessão de seg 26/10 21h05 (1 min) |
| O Buzzfy segue conectado e com dado | SOLIDA | 1 | media | respondeu a todas as consultas de hoje; erro vira "sem dado" |
| Teto de 3 ações por rodada sobe a execução | FRAGIL | 4 | media | execução da rodada de 26/10 lida em 02/11 |

### D6. TABULEIRO e funil

| Premissa | Nota | Nível | Impacto | Como testar barato |
|---|---|---|---|---|
| O gargalo está antes do comentário (falta gente) | SOLIDA | 1 | alta | já medido: 577 contas, 2 comentários, 0 clique em 7 dias |
| O Bruno desliga as 16 automações no prazo | FRAGIL | 1 | media | `listCommentAutomations` dom 25/10 18h30 |
| Comentário de parabéns vai disparar CASE ou ESTRATEGISTA | ABALAVEL | 4 | media | não testar no ar: desligar antes |
| Por post dá atribuição por peça | FRAGIL | 2 | media | linkTracking só aceita falso [V2 item 1]; o Bruno confere se o GA4 guarda o o= no page_location [V2 item 8] |
| O Instagram orgânico gera as conversas de 30 min | FRAGIL | 1 | alta | o Bruno escreve a origem dos últimos 5 clientes e das últimas 5 conversas (10 min) |
| "Comenta ESTRATEGISTA" no case gera conversa | FRAGIL | 1 | baixa | log da automação do case em 48 h |

---

## 7. Sensibilidade: as 3 premissas de maior impacto

| Decisão | Premissa | Valor atual | Limiar em que a recomendação vira | Vira dentro da faixa plausível? |
|---|---|---|---|---|
| D2 (e D3) | O Bruno grava 1 bloco por semana | 36,4 s gravados de 21/10 13h12 a 24/10 15h15 [fato 104]; 0 bloco marcado [a buscar 20]; 90 min não cumpridos [fato 105] | Com a probabilidade do bloco em nota 1 (no máximo 1 bloco nas 4 semanas) e o impacto em 3, a opção (a) cai de 76 para 63 e perde para uma (d) refeita com estático de foto do Bruno, que faz 67; com a (d) original (60), (a) perde só com impacto 2 (58) [ESTIMATIVA: pesos fixos do plano, notas do red team] | sim: o valor de hoje já está abaixo do limiar |
| D1 | A pausa cai e a TV tem autorização a tempo | pausa desde 24/10 18h45, motivo sem dado; peças em rascunho às 20h19 [FATO, `listPosts`]; nenhum pedido à assessoria [V2 item 2] | ordem escrita depois de sex 30/10 17h: (c) vira (b) pelo próprio mapa; sem ordem até seg 09/11 19h: a série sai do ciclo; se o motivo da pausa for pedido da emissora ou da produção, nenhuma das 4 opções vale e a certa é "TV só como link e destaque" | sim: qualquer data entre amanhã e "nunca" é plausível |
| D1 e D5 | A família da TV (Bruno de perfil) faz 42 ou mais de alcance em 48 h | n de 0; previsão do plano 50 (25 a 110) sem conta [V1 P2]; referências: Bruno de frente 167,5, sem rosto 58, animação 32,5 [fato 25, 27 e 28]; corte cru de TV no mercado a 0,0055x os seguidores, perto de 9 views nesta conta [ESTIMATIVA: 1.618 x 0,0055] | mediana abaixo de 42 com n de 2 (régua sobre 53) tira a série do feed; sobre a base atual de 37,5 o corte seria 30 [ESTIMATIVA: 0,8 x 37,5]: entre 30 e 42 a decisão depende só da base escolhida | sim: 42 fica no meio da faixa de 25 a 110 do próprio plano, que dá 0,65 de chance de não chegar lá |

**Leitura.** As três viram dentro da faixa plausível, e a primeira já virou. Nenhuma das três depende de mais análise: dependem de uma resposta do Bruno (gravar, motivo da pausa) ou de um pedido escrito a terceiro (assessoria). Fora do top 3, a base da régua (53 contra 37,5) também vira na faixa: formatos com mediana entre 30 e 42 mudam de PARAR para MANTER conforme a base, e a animação (32,5) cai exatamente nesse intervalo [fato 27].

---

## 8. O que o red team muda no plano

Em ordem de custo de não fazer. Nenhum agente executa nada disso; são pedidos ao Bruno ou à agência.

1. **Tirar o reel do case e a chamada dele da noite do 2º turno.** Seg 26/10 21h está livre com a pausa mantida (o mapa do D1 só usa essa vaga se a ordem chegar até seg 17h). Dono: Bruno. Prazo: dom 25/10 18h. Custo: 2 min. Se ele mantiver, as 48 h do case e do Dentista B entram na régua com a marca "dia de eleição" e não fecham PARAR nem DOBRAR sozinhas, como os feriados.
2. **Perguntar o motivo da pausa**, junto com "cai ou fica". Muda qual linha do mapa vale e se a TV precisa da assessoria. Dono: Bruno. Prazo: dom 25/10 16h. Custo: 2 min.
3. **Pedido escrito à Assessoria de Imprensa da Câmara** para usar trechos da gravação em perfil profissional, antes e depois de 02/11 [V2 item 2]. Sem resposta, a TV entra só como link da edição oficial e destaque sem trecho. Dono: Bruno. Prazo: seg 26/10. Custo: 10 min.
4. **Grade sem gravação como padrão.** Por semana: 2 carrosséis com foto do Bruno, 1 estático de foto (TESTAR, fora da conta dos carrosséis), R1 a R3 pela escada do D2, Dentista C pelo G1. Cada bloco gravado acrescenta 2 reels por cima. Assim o fracasso nº 1 não zera o feed. Dono: agência. Prazo: grade da S2 até qui 29/10.
5. **Protocolo de sequência pré-aprovado.** Se qualquer reel passar de 171 views em 24 h [derivar 3], a próxima peça da mesma linha (escolhida agora pelo Bruno, por exemplo as aberturas de frente ou o R1) sai em até 24 h sem esperar a sexta. Dono: Bruno escolhe a peça; agência agenda. Custo: 5 min agora.
6. **Ok tácito na sexta.** O que a agência mandar até quinta 18h e o Bruno não vetar até sexta 18h vai ao ar. Corta a dependência mais frágil do D3.
7. **Dono das rodadas do Módulo 7.** Escrever quem abre a sessão de seg 26/10 21h05 e das segundas seguintes. Sem isso, o D5 não acontece.
8. **Automações de conta toda: 1 lote só, domingo até 18h29.** Se não forem desligadas, nenhuma peça da TV volta, mesmo com a pausa levantada.
9. **Uma frente fora do Instagram para a meta.** O Bruno escreve de onde vieram os últimos 5 clientes. Se vierem da rede local, a TV vira motivo de mensagem pessoal dele para contatos quentes, com o link da edição depois que ela for ao ar (o Bruno manda, nenhum agente manda). Custo: 10 min para saber.
10. **Estoque e repositório.** Definir quem copia os renders (o Bruno não alcança a pasta da sessão) e decidir se o repositório fica privado. Dono: Bruno. Prazo: dom 25/10.
11. **Teto de stories enquanto não houver resposta.** No máximo 4 por dia até a primeira semana com 3 respostas; o resto do molde do D4 espera.

---

## Fontes

- `run/06-plano-final.md` (inteiro); `run/01-fatos.md` (inteiro); `run/07-verificacao/V1.md` e `V2.md` (inteiros); `run/00-enquadramento.md` (seções 1 a 3 e critérios de sucesso); `contexto.md`; `/home/user/Disparo-/CLAUDE.md`; `stories-objecoes/06-agenda-postzen.md` (nota da pausa).
- PostZen `listPosts` (sem filtro, página 1 de 4, 73 itens no total) e `listCommentAutomations`, conta j97772ycndetk3f1wcdbh14p898g4b8w, lidos às 20h19 de 24/10.
- Buzzfy `ig_follower_growth` (14 dias), `ig_posts` (kind stories) e `ig_post_stats` dos 7 stories ativos, lidos às 20h19 e 20h20 de 24/10 (números de story provisórios).
- `gh api repos/brunodjs-source/Disparo-` (visibility public), `git grep -l` por nome do cliente do case e da repórter, `ls`, `du` e `df` da pasta da sessão, contagem de palavras e condições no plano: 20h17 a 20h23 de 24/10.
- Eleição: [Tribuna de Jundiaí, 04/10/2026](https://tribunadejundiai.com.br/politica/eleicoes-2026/flavio-bolsonaro-e-lula-vao-disputar-segundo-turno-pela-presidencia-da-republica/) (lida às 20h18); resultados de busca sobre o 2º turno e os estados com 2º turno para governador: [Investnews](https://investnews.com.br/economia/estados-segundo-turno-eleicoes-2026/amp/), [Congresso em Foco](https://www.congressoemfoco.com.br/noticia/123236/quando-e-qual-e-o-dia-do-segundo-turno-das-eleicoes-2026).
- Bloqueios de 2022: [Diário do Nordeste](https://diariodonordeste.verdesmares.com.br/ultima-hora/pais/bloqueios-ilegais-em-rodovias-chegaram-ao-pico-na-madrugada-desta-terca-1-diz-prf-1.3295945), [InvestNews](https://investnews.com.br/economia/protestos-bolsonaristas-em-rodovias-perdem-forca-e-recuam-em-todo-pais/), [Money Times](https://www.moneytimes.com.br/interdicoes-parciais-em-estradas-por-protestos-bolsonaristas-caem-para-11-no-pais) (resultados de busca, nível 3, 20h24).
