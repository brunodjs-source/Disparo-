# F6 · Stories diários e objeções · @o_estrategista.com.br · rodada de 24/10/2026, versão das 15h30

Frente F6 da pesquisa do conselho Agência Reunida. Substitui a versão das 14h15 deste arquivo (histórico no git, commit 88433c7), escrita antes do fato novo: a entrevista à TV Câmara Campinas vai ao ar na **segunda-feira, 02/11/2026** (mensagem do Bruno: "Vai pro ar segunda dia 2" e "pode seguir pois as postagens vou marcar ela"). Horário da exibição: sem dado.

Somente leitura. Nada foi publicado, agendado, alterado ou enviado no Instagram, no Buzzfy, no PostZen ou em site. Toda mudança abaixo é proposta para o Bruno executar.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha uma objeção sozinho. Métrica que falta: "sem dado".

**O que esta frente não repete** (está em outro arquivo e só é citado pelo número):
- `conteudo/stories-objecoes/01-objecoes.md`: O1 a O12, com crença, contra-argumento na voz do Bruno e prova.
- `conteudo/stories-objecoes/02-provas.md`: inventário B, T, C, M, J, R e N com tempo da transcrição e a lista do que não pode ser dito.
- `conteudo/stories-objecoes/03-plano-7-dias.md`: os 56 stories de 25 a 31/10 e as fichas de ob01 a ob03.
- `run/01-pesquisa/F4-entrevista-tv.md` (versão das 15h15): o dia 02/11 hora a hora (seção 3.2), a marcação da Mirna e as 3 menções em story (seção 6), os termos de uso da TV Câmara e o que muda na copy depois da exibição.
- `run/01-pesquisa/F8-funil-diagnostico.md`: as 17 automações e o caminho até o diagnóstico.

---

## 0. Consultas desta versão

| # | Consulta (só leitura) | Parâmetros | Hora (SP) | Resultado |
|---|---|---|---|---|
| 1 | Buzzfy `ig_posts` | kind=stories | 15h19 | 5 stories no ar: 09h33 (vídeo, fora do PostZen), 14h00 (st01), 14h03 (estático de bastidor), 15h00 ("A pergunta da TV"), 15h01 (mc01) |
| 2 | Buzzfy `ig_post_stats` | os 5 ids, sem mediana | 15h19 | ok, todos provisórios |
| 3 | Buzzfy `ig_account_stats` | 7 dias (17/10 a 24/10, 18h19 UTC) | 15h19 | ok |
| 4 | Buzzfy `ig_account_stats` | 30 dias (24/09 a 24/10, 18h23 UTC) | 15h23 | ok |
| 5 | Buzzfy `ig_audience` | this_month, 3 públicos | 15h20 | ok |
| 6 | Buzzfy `ig_best_times` | America/Sao_Paulo, 35 posts | 15h20 | ok, 27 dias de seguidores online; números iguais aos da leitura das 14h05 |
| 7 | Buzzfy `buzzfy_reel_search` | reels em português sobre objeções de quem quer lançar | 15h21 | **ERRO**: "This account has used its 10 reel searches for today", próxima liberação perto de 16h45 UTC de amanhã. Registrado como erro: não existe leitura de mercado sobre objeções nesta versão |
| 8 | PostZen `listPosts` | conta j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 a 30/11, por data | 15h19 | 20 itens: 4 stories publicados hoje, 16 agendados |
| 9 | PostZen `listCommentAutomations` | mesma conta | 15h19 | 17 automações ativas, iguais às das 14h02 |
| 10 | PostZen `listCommentAutomationLogs` | ETAPAS de story (qs78ccqc3nf0axhc59frr8mewx8ghnvj) e TABULEIRO (qs747t4bq23a1qpnjskexg34vs8gx7hx) | 15h19 | 0 log nas duas |
| 11 | Meta, IG User Media (developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media) | WebFetch | 15h22 | aberta |
| 12 | Socialinsider, "2025 Instagram Stories Benchmarks" (socialinsider.io/blog/instagram-stories-benchmarks/) | WebFetch | 15h23 | aberta |
| 13 | Instagram, "Introducing Stories Highlights & Stories Archive" (about.instagram.com, 05/12/2017) | WebFetch | 15h22 | aberta |
| 14 | Guiding Tech, guia do sticker de contagem (guidingtech.com/instagram-countdown-sticker-guide/, atualizado em 17/07/2024) | WebFetch | 15h21 | aberta |
| 15 | Social Media Today, lançamento do sticker de contagem (13/12/2018) | WebFetch | 15h21 | aberta |
| 16 | Later, guia de stickers (later.com/blog/instagram-stories-countdown-sticker) | WebFetch | 15h21 | aberta, mas o trecho lido não chegou à parte da contagem. Nada deste arquivo se apoia nela |
| 17 | TV Câmara Campinas, termos de uso (tvcamaracampinas.com.br/termos, atualizados em 24/05/2026) | WebFetch | 15h22 | aberta |
| 18 | Repositório: `contexto.md`, `00-enquadramento.md` (14h45), `CLAUDE.md`, `00-SISTEMA.md` (Módulos 4 e 6, Perfil), F1, F2, F4, F5, F7 e F8 desta rodada, `estaticos/stories-frases/s.html`, `estaticos/destaque-comece-aqui/`, `videos/tv-camara/cortes/*.spec.json` | leitura | 15h00 a 15h25 | ok |

A Central de Ajuda do Instagram sobre o sticker de contagem não apareceu em nenhuma das duas buscas: o que está dito sobre contagem vem de fontes de terceiros (nível 3) e vai marcado assim.

Ferramentas fora da lista desta rodada: `ig_comments` e `ig_inbox`. Consequência: a frequência real de cada objeção continua sem dado.

---

## 1. Respostas curtas

1. **Story segue sendo o maior bloco de views da conta.** 7 dias: 1.029 de 1.884 views (54,6%); 30 dias: 4.283 de 10.510 views orgânicas (40,8%) [FATO, `ig_account_stats` 15h19 e 15h23; ESTIMATIVA para os percentuais]. Cerca de 143 a 147 views de story por dia [ESTIMATIVA: 4.283 / 30 e 1.029 / 7].
2. **Story conversa pouco.** 3 respostas em 7 dias e 7 em 30 dias: 2,9 e 1,6 por 1.000 views de story [ESTIMATIVA, supondo que "replies" da conta sejam respostas a story].
3. **Primeira pilha da TV medida hoje.** O st01 (Bruno em cena) chegou a 16 contas em 1,3 h, o estático de bastidor a 12 [FATO, `ig_post_stats` 15h19]. O estático seguinte teve 75% do alcance do st01 [ESTIMATIVA: 12 / 16]. n de 1, menos de 2 h de vida: registro, não conclusão.
4. **Frequência:** 6 a 8 por dia, num molde de 4 blocos com 2 ou 3 stories à mão por dia, e **nenhum teste de frequência na semana da exibição** (01 a 07/11), porque a TV mexe no alcance ao mesmo tempo. O teste de carga vai para a S3 (08 a 14/11), dia sim, dia não (seção 3) [HIPÓTESE].
5. **Contagem para 02/11:** a contagem diária vai no texto do 1º story do dia ("SEG, 02/11 · FALTAM N DIAS"), agendada no PostZen, sem story a mais. O sticker de contagem nativo tem opção "dia todo", fica salvo no perfil e pode ser reusado em stories novos [FATO nível 3, Guiding Tech 2024]: vale criar um só se o horário vier da Mirna até dom 25/10 de manhã; sem horário, fica o texto (seção 5).
6. **ETAPAS:** ativa, 0 disparo, 0 log, só dispara com "etapa" ou "etapas" e entrega PDF com formulário [FATO, PostZen]. Recomendação: stories não pedem palavra nenhuma; o único pedido é o link do diagnóstico. Os 2 stories do `03-plano` que dizem que a resposta "cai na automação ETAPAS" precisam de outra linha (seção 7).
7. **Destaque "NA TV": sim, faz sentido**, no lugar do PROVA (que ainda não existe), como 2º destaque, de 25/10 até a rodada de 23/11, com quatro condições: sem logo, sem texto vencido (st01 e qualquer "vai ao ar" saem do destaque em 03/11), ok da Mirna para uso permanente e o link da edição só depois que ela estiver no site (seção 8).
8. **Objeções:** nenhuma frequência medida. Três objeções novas entram como hipótese: O13 "Eu vendo serviço, não curso", O14 "TV de Câmara não prova nada" (nasce com a própria exibição) e O15 "Meu público é daqui de Campinas". O mapa da seção 9 liga cada objeção a uma prova do `02-provas.md` e a um dia de 25/10 a 21/11.
9. **Frase de efeito:** 28 dias pedem 28 frases; prontas e livres há 2 (`story-frase-3` e `story-frase-4`). A seção 6 lista 14 frases com fonte, sem texto novo.

---

## 2. Linha de base (medida agora)

### 2.1 Conta

| Métrica | 7 dias (17 a 24/10) | 30 dias (24/09 a 24/10) | Fonte |
|---|---|---|---|
| Views de story | 1.029 | 4.283 | [FATO, `ig_account_stats`] |
| Contas alcançadas por story | 337 | 756 | idem |
| Views da conta | 1.884 (0 de anúncio) | 12.717 (2.207 de anúncio; 10.510 orgânicas) | idem |
| Respostas / repostagens | 3 / 1 | 7 / 1 | idem |
| Visitas ao perfil / cliques no site | 74 / 0 | 447 / 7 | idem |
| Seguidores / seguindo | 1.618 / 3.528 | | idem |

### 2.2 A pilha de hoje

| Story | Postado | Vida | Alcance | Views | Avançar | Voltar | Deslizar | Sair | Respostas | Fonte |
|---|---|---|---|---|---|---|---|---|---|---|
| Vídeo fora do PostZen (academia, sem o Bruno visível, segundo o F1) | 09h33 | 5,8 h | 31 | 40 | 22 | 0 | 6 | 3 | 0 | [FATO, `ig_post_stats` 15h19, provisório] |
| st01, bastidor da TV (vídeo, Bruno em cena) | 14h00 | 1,3 h | 16 | 24 | 11 | 2 | 2 | 3 | 0 | idem |
| Estático de bastidor | 14h03 | 1,3 h | 12 | 18 | 9 | 2 | 0 | 1 | 0 | idem |
| "A pergunta da TV" (estático) | 15h00 | 0,3 h | abaixo de 5 | 4 | | | | | | idem |
| mc01 (vídeo, voz da Mirna) | 15h01 | 0,3 h | abaixo de 5 | 3 | | | | | | idem |

Contas [ESTIMATIVA, sobre as navegações registradas]:
- Saída (deslizar + sair) / navegações: 09h33, 29% (9 de 31); st01, 28% (5 de 18); estático, 8% (1 de 12).
- Alcance do estático das 14h03 sobre o do st01: 12 de 16, 75%. Não é a mesma coisa que retenção pessoa a pessoa: a ferramenta não diz quem viu os dois.
- A definição de saída do Buzzfy pode não ser a do Socialinsider (23,8% no 1º story, 20,5% no 2º [FATO, Socialinsider 2025]); não comparar os números.

Leitura: é a primeira vez que a conta tem uma pilha seguida com o Bruno em cena lida no mesmo dia. A pilha de hoje termina às 20h30 e expira entre dom 25/10 09h33 e 20h30. **A leitura completa só existe se alguém rodar `ig_posts` kind=stories e `ig_post_stats` antes de dom 25/10 09h33** (Buzzfy só lê story nas 24 h e com 5 ou mais espectadores [FATO, nota do `ig_post_stats`]).

### 2.3 Público

[FATO, `ig_audience` this_month, 15h20]
- Campinas: 33% dos seguidores, 53,1% das contas engajadas e 38,2% das alcançadas. Somando as cidades da região que aparecem na lista de engajados (Valinhos 6,3%, Hortolândia 4,2%, Sumaré 4,2%, Nova Odessa 2,1%), a região de Campinas passa de 70% de quem engajou [ESTIMATIVA: 53,1 + 6,3 + 4,2 + 4,2 + 2,1 = 69,9, sem contar cidades fora do top 8].
- Engajados: 59,4% homens; 35 a 54 anos somam 65,7%.
- A TV Câmara é local [FATO, F4]. O público que reage aos stories também é [FATO, acima]. Esse é o principal argumento a favor do destaque NA TV (seção 8).

---

## 3. Frequência

**Fatos.**
- A conta não tem registro de quantos stories saíram por dia antes de hoje: o Buzzfy só lê nas 24 h e o PostZen só guarda os que ele mesmo publicou [FATO, nota do `ig_posts`; `listPosts`].
- Hoje: 9 stories no dia (1 à mão às 09h33 e 8 pelo PostZen, de 14h00 a 20h30) [FATO, `ig_posts` e `listPosts`].
- `03-plano-7-dias`: 56 stories de 25 a 31/10, 27 à mão [FATO].
- Régua externa: "Post at least 6 Stories per day" e "sweet spot sits roughly between 6 and 13 Stories", em marcas de 1 mil a 1 milhão de seguidores, jan a mai/2025, com duas amostras não conciliadas na página (161.180 e 113.361) [FATO, Socialinsider 2025, nível 3]. Nenhuma fonte mede conta de expert brasileiro com 1.600 seguidores.

**Proposta [HIPÓTESE].**
- **S1 (25 a 31/10) e S2 (01 a 07/11):** molde da seção 4, com 8 stories em dia de reel e 6 a 7 nos outros. Sem teste de frequência nessas duas semanas.
- **Por que não testar na S2:** a exibição de 02/11, o feriado e a marcação da Mirna mudam o alcance na mesma semana. Qualquer diferença de views seria atribuída à quantidade de stories sem ser [PRIOR]. Um fator por vez.
- **S3 (08 a 14/11), teste de carga dentro da semana:** dom, ter, qui e sáb com o molde cheio (8); seg, qua e sex com 5 (sem a prova separada, sem a frase de efeito, sem o compartilhamento à mão; a prova vira a sub da virada). Comparar por dia: alcance do story mais visto da pilha (o mais perto de "contas únicas" que a ferramenta dá) e toques no link do diagnóstico (contagem do Bruno no app).
- **Regra de decisão para a S4:** se os dias de 5 mantiverem o alcance do story mais visto a 90% ou mais do dos dias de 8 e não tiverem menos toques no link, a S4 fica com 5 [o limite de 90% é PRIOR]. Senão, fica o molde cheio.
- **Custo da leitura:** o teste só existe se a pilha for lida toda noite, às 23h, nos 7 dias da S3 (`ig_posts` kind=stories e `ig_post_stats`). Sem essa leitura diária, o resultado é sem dado.

---

## 4. Horários e o molde diário com os 8 tipos pedidos

[FATO, `ig_best_times` 15h20] Seguidores online de 339 (08h) a 430 (18h), curva plana até 22h (391). Story fica 24 h no ar [FATO, Meta: "Stories expire after 24 hours"]: a hora define quem vê primeiro e a ordem da pilha. Online em feriado: sem dado.

Os horários são os do F7 e do `03-plano`; muda a ordem e entra a contagem. "AGENDADO" vai pelo PostZen, sem sticker. "À MÃO" é postado pelo Bruno no app, com o sticker na zona livre (y 1300 a 1560, em 1080 x 1920, regra do `03-plano`).

### 4.1 Dia útil com reel às 21h (fase ANTES, 25/10 a 01/11)

| Hora | Tipo pedido | O que vai | Como sobe |
|---|---|---|---|
| 09h00 | Bastidor + contagem | Bruno em cena (trecho de 5 a 15 s da gravação do celular, mc02, mc03, foto e1 ou e2), rótulo "NA TV · SEG, 02/11" e sub "FALTAM N DIAS" | AGENDADO |
| 12h00 | Quebra de objeção | "O QUE EU MAIS OUÇO" com a frase do cliente (objeção do dia, seção 9) | À MÃO: enquete de medição |
| 12h01 | Quebra de objeção (virada) | Contra-argumento do `01-objecoes.md` | AGENDADO |
| 12h02 | Prova de autoridade | Item do `02-provas.md` com tempo da transcrição | AGENDADO |
| 12h03 | Pedido único | DIAGNÓSTICO · 12 CASAS | À MÃO: link `/tabuleiro/?o=ig-stories` (mais `&p=profissão` em dia de nicho) |
| 17h30 | Frase de efeito | FRASE DO DIA (seção 6), sem pedido | AGENDADO |
| 20h30 | Chamada para o reel do dia | Dia e hora no texto ("SEG · 21H · NO FEED"), nunca "hoje" | AGENDADO |
| 21h05 | Fecho | Compartilhar o reel publicado | À MÃO: compartilhar post (e menção à Mirna onde o F4 manda) |

Total: 8 stories, 3 à mão. Fim de semana com reel às 18h30: frase às 16h00, chamada às 17h30, compartilhamento às 18h35. Dia sem reel: sai a dupla chamada e compartilhamento (6 stories, 2 à mão).

### 4.2 Enquete e caixa de pergunta

- **Enquete:** uma por dia, sempre no story da objeção (12h00), sempre de medição (SIM / NÃO ou par de objeções). Nunca no mesmo story do link.
- **Caixa de pergunta:** uma por semana. S1: qui 29/10, "O que você perguntaria se fosse a repórter?" (proposta do F4, seção 3.1). S2 a S4: sábado, "Qual a sua maior dúvida antes de chamar um estrategista?" (`01-objecoes.md`, seção 5). A caixa entra no lugar da enquete daquele dia, para não somar um pedido.
- **Por que a caixa volta** (o `03-plano` tirou): é o único instrumento que traz a objeção com as palavras do público, e a frequência de objeção é sem dado [FATO, `01-objecoes.md` seção 1].

### 4.3 Os três tempos da série

| Fase | Datas | Bloco das 09h00 | O que muda no resto |
|---|---|---|---|
| ANTES | dom 25/10 a dom 01/11 | Bastidor + "NA TV · SEG, 02/11 · FALTAM N DIAS" | Molde 4.1 |
| NO DIA | seg 02/11 (Finados) | A grade do F4, seção 3.2 (estático das 09h00, horário confirmado, "Foi ao ar", chamada e compartilhamento do reel) | **Sem bloco de objeção** [HIPÓTESE]: o dia já tem 5 a 6 stories da TV e uma objeção a mais pede outra enquete e outro link à mão num feriado. A frase de efeito do dia é literal da TV (seção 6) |
| DEPOIS | ter 03/11 a sáb 21/11 | "O QUE EU DISSE NA TV": trechos de 10 a 15 s da gravação do celular, rótulo "NA TV CÂMARA CAMPINAS" sem data | Molde 4.1 com as objeções O7 e O9 a O15 (seção 9). "Foi ao ar" só depois do horário confirmado [FATO, F4] |

Carga à mão [ESTIMATIVA]: semana com 5 dias de reel e 2 sem reel = 5 x 3 + 2 x 2 = 19 stories à mão, mais 1 caixa = 20 (o `03-plano` tem 27). A diferença vem de tirar o repost das 09h00 (que levava enquete) do 1º lugar da pilha: o reel de ontem já foi compartilhado às 21h05 ou 18h35.

**Por que o 1º story do dia é o Bruno em cena e não o repost de ontem:** o 1º story tem a maior saída da pilha [FATO, Socialinsider 2025: 23,8%] e a regra medida da conta é o Bruno em cena [FATO, CLAUDE.md, 21/10/2026]. Na pilha de hoje, o story sem o Bruno (09h33) e o st01 tiveram saída parecida (29% e 28%), com horas de vida diferentes [ESTIMATIVA, seção 2.2]: não há dado da conta que decida isso ainda. [HIPÓTESE]

---

## 5. Stickers e contagem

### 5.1 Fatos da plataforma

- [FATO, Meta, IG User Media, aberta às 15h22] "Publishing stickers (i.e., link, poll, location) is not supported"; menção sem sticker é suportada. Story do PostZen sai sem enquete, caixa, link ou contagem.
- [FATO, `ig_post_stats`] O Buzzfy não traz votos de enquete, respostas de caixa, toques em link nem lembretes de contagem. Tudo isso só se lê no app, à mão.
- [FATO nível 3, Guiding Tech, atualizado em 17/07/2024] O sticker de contagem tem a opção "All day" ("tap on the All day toggle at the bottom to turn it off" para escolher hora); "Since the countdowns stay in your profile, you can always add them again to your Stories"; "If you like someone's Countdown, you can share it on your Story"; e remover a contagem "will also remove your Instagram Story".
- [FATO nível 3, Social Media Today, 13/12/2018] Quem toca no sticker pode "set a reminder for when the countdown ends" e "share the countdown with their followers".
- Se o Instagram ainda avisa o criador de quem pediu lembrete, e em que hora o lembrete dispara com "dia todo": sem dado (as fontes abertas não dizem; nenhuma é da Central de Ajuda).
- Se dá para mudar a hora de uma contagem já criada: sem dado.

### 5.2 Contagem para 02/11: proposta

| Peça | Quando | Como sobe | Condição |
|---|---|---|---|
| Texto "NA TV · SEG, 02/11" com sub "FALTAM N DIAS" no 1º story do dia | dom 25/10 (faltam 8) a dom 01/11 (falta 1) | AGENDADO | Nenhuma. A data é a âncora; o número é secundário, porque o story fica no ar até a manhã seguinte |
| Sticker de contagem criado uma vez, com o horário, título "TV CÂMARA · SEG 02/11" | dom 25/10, 09h00, no 1º story (que passa a ir à mão nesse dia) | À MÃO | Só se a Mirna passar o horário antes. Reusar em qua 28/10, sáb 31/10 e dom 01/11, sempre no 1º story (que vai à mão nesses dias: +4 à mão na S1) |
| Sem horário até dom 25/10 | | | Fica só o texto. Contagem com "dia todo" não entra: a hora do lembrete é sem dado e um aviso de madrugada num feriado não ajuda a assistir às 18h [PRIOR]. O F4 chega à mesma regra por outro caminho ("sem horário, não sai") |

O que a contagem mede: número de lembretes pedidos, lido pelo Bruno no app, se o app mostrar [sem dado]. Seria a única medida de intenção de assistir antes de 02/11.

### 5.3 Regras de sticker

| Sticker | Para que | Regra |
|---|---|---|
| Enquete | Medir objeção | 1 por dia, no story da objeção; nunca junto com link |
| Caixa de pergunta | Colher objeção com as palavras do público | 1 por semana, no lugar da enquete do dia; responder em story sem expor quem perguntou [PRIOR] |
| Link | O único pedido | `/tabuleiro/?o=ig-stories`; em dia de nicho, `&p=dentista` (ou medico, advogado, psicologo, nutricionista, consorcio): a profissão chega na mensagem do WhatsApp, a origem não [FATO, `js/tabuleiro.js`, versão das 14h15 deste arquivo] |
| Compartilhar post | Levar ao reel | Logo depois de o reel sair; apagar a chamada |
| Menção | Mirna | Só nos 3 momentos do F4 (seção 6.3). Story agendado não leva menção |
| Contagem | Lembrete para 02/11 | Seção 5.2 |

---

## 6. Frase de efeito: o banco para 28 dias

**Estoque pronto** [FATO, `estaticos/stories-frases/s.html` e F5]: 5 FRASE DO DIA no modelo; 1 e 2 saem hoje ("Você atende...", "Fila de espera..."), e a 5 tem a mesma frase do story das 19h30 de hoje ("Nem tudo que vemos é ouro.", com o rótulo NA TV). Livres: 3 ("Lançamento é xadrez. A maioria joga dama.") e 4 ("O lead que não comprou vale mais do que o que comprou.").

**Banco com fonte, sem texto novo** (render no mesmo modelo, uma palavra em ouro):

| # | Frase | Fonte | Cuidado |
|---|---|---|---|
| 1 | Lançamento é xadrez. A maioria joga dama. | `story-frase-3` (hook 17, 35/50) | pronta |
| 2 | O lead que não comprou vale mais do que o que comprou. | `story-frase-4` (hook 21, 36/50) | pronta |
| 3 | Advogado vende hora. E hora acaba. | Hook 10, 40/50 (Módulo 4) | dia de nicho advogado |
| 4 | Psicólogo com fila de espera tem um produto pronto e não percebeu. | Hook 16, 41/50 | dia de nicho psicólogo |
| 5 | Nutricionista com agenda cheia: o seu próximo paciente é um aluno. | Hook 22, 38/50 | dia de nicho nutricionista |
| 6 | Preço errado para cima tem conserto. Para baixo, quase nunca. | Hook 28, 38/50 | opinião do Bruno; não usar no dia do "é caro" junto com preço |
| 7 | Sua live lotou e ninguém comprou. Eu sei o motivo. | Hook 15, 38/50 | o `03-plano` já usa como objeção O4 em 29/10: não repetir na mesma semana |
| 8 | “Cada cliente tem um produto específico e a gente vive esse produto.” | M3, 1580,7 a 1583,8 s | literal da TV |
| 9 | “As pessoas me contratavam para resolver problemas nas empresas delas.” | C5, 1078,4 a 1083,9 s | literal da TV |
| 10 | “Saber convencer as pessoas quebrando a objeção delas.” | M5, 1304,1 a 1307,6 s | literal da TV |
| 11 | “Os clientes chegam pra gente machucados.” | M9, 1402,0 a 1403,6 s | já é prova em 28/10; como frase, só depois de 03/11 |
| 12 | Curso te dá o mapa. A partida precisa de quem comande. | Contra-argumento O12 (`01-objecoes.md`) | no dia da O12, vira a virada; como frase, em outro dia |
| 13 | Mais verba numa ordem errada só acelera o erro. | Contra-argumento O9 | idem |
| 14 | “Eu sou estrategista de marketing digital e lançamento de um produto.” | M11, 1199,9 a 1204,0 s (começa em "Eu" e "um produto" pela pontuação forçada, `videos/tv-camara/cortes/ob02.spec.json`) | frase do dia 02/11 (literal, Bruno, sem data na tela) |

Fora do banco, de propósito: hooks 1, 2, 6, 24 e 29 (afirmação ou número sem fonte), 3 e 26 (regras do case de 6 para 20; o 26 cita o nome do cliente), 14 e 19 (recusas sem fonte de episódio, vetadas no `02-provas.md`).

Conta [ESTIMATIVA]: 14 frases cobrem 14 dos 28 dias de 25/10 a 21/11. O resto repete as que tiverem menor saída na leitura noturna, com pelo menos 14 dias entre uma volta e outra [PRIOR]. Uma "não é X, é Y" por peça: a frase 2 do estoque de hoje ("Fila de espera não é sucesso. É teto.") já gasta a da peça dela.

---

## 7. Automação ETAPAS

**Estado às 15h19** [FATO, `listCommentAutomations` e `listCommentAutomationLogs`]:
- "ETAPAS · resposta de Story (conta toda)": gatilho story_reply, palavras "etapas" e "etapa" (palavra inteira, tolera erro de digitação, não vale em direct digitado), público qualquer. Leva ao direct com botão "Baixar o PDF" para `.../m/checklist?o=ig-story-etapas` (formulário de 9 campos, grupo do WhatsApp e, no 3º passo, o Tabuleiro [FATO, versão das 14h15 deste arquivo, HTML da página]). 0 disparado, 0 enviado, 0 log.
- TABULEIRO: gatilho comment, só no Dentista B (hoje 21h). 0 log.
- 17 automações ativas, 15 palavras; só a CHECKLIST tem 1 envio [FATO].
- Resposta de story usa direct comum dentro da janela de 24 h [FATO, descrição da ferramenta PostZen].

**O que não fecha.**
1. A regra do CLAUDE.md é uma palavra por mês (TABULEIRO), e só em post com 150 de alcance ou mais. Story desta conta chega a 12 a 31 contas cada (seção 2.2). TABULEIRO em story fere a regra dos 150; ETAPAS em story fere a regra de uma palavra.
2. O `03-plano` conta com a ETAPAS em dois stories: dom 25/10 09h02 (enquete do caso de 6 para 20, "Votou SIM? Responde este story.") e sex 30/10 17h31 ("Responde este story com a sua área"). Uma resposta "sim" ou "dentista" não dispara nada: cai no direct e só o Bruno responde.
3. Quando dispara, a ETAPAS leva a material, não ao diagnóstico (F8).

**Recomendação [HIPÓTESE]:**
- Stories não pedem palavra. O pedido do dia é o link do diagnóstico, que funciona sem automação.
- Os dois stories do `03-plano`: trocar a linha por "Toque no link: Diagnóstico de 12 casas." (dom 25/10, no estático de 09h02, sem a enquete virar pedido) e, em sex 30/10 17h31, manter "Responde este story com a sua área" só se o Bruno se comprometer a responder à mão em até 24 h; senão, a sub vira "Toque no link: Diagnóstico de 12 casas.".
- A ETAPAS de story: o Bruno desliga, junto com as ETAPAS de comentário que o F8 (R1) manda desligar. Ligada, ela não custa nada, mas mantém uma segunda palavra ativa na conta. A decisão e o clique são dele, antes de dom 25/10 09h00.

---

## 8. Destaques e o "NA TV"

### 8.1 O que existe

- [FATO, 00-SISTEMA, Módulo 1 item 9 e Perfil] Decisão de 4 destaques, nesta ordem para quem chega frio: COMECE AQUI, PROVA, MÉTODO, QUEM SOU. Capas prontas: xeque-mate, quem sou, tabuleiro, método, bastidor e COMECE AQUI. **Não há capa PROVA** nem destaque PROVA.
- [FATO, `estaticos/destaque-comece-aqui/textos-direct.md`] O COMECE AQUI leva os 3 stories animados da Escala 7x7, sem o Bruno e sem voz dele.
- [FATO, Instagram, 05/12/2017] "Highlights stay on your profile until you remove them, and you can have as many highlights as you'd like"; o destaque se monta com stories do arquivo, com capa e nome escolhidos; quem visita o perfil toca e assiste.
- [FATO, termos da TV Câmara, 24/05/2026] Permitido: "Compartilhar links do site nas redes sociais" e "Citar trechos do conteúdo em publicações jornalísticas, acadêmicas ou pessoais" com a TV Câmara como fonte. Proibido: "Republicar conteúdo integral sem autorização prévia da emissora" e "Usar o conteúdo para fins comerciais". Os termos não falam de logo.
- [FATO, `videos/tv-camara/cortes/st01.spec.json`] O st01 termina com o cartão "AMANHÃ, 18H30, NO FEED". [FATO, `s.html`] O estático de bastidor do modelo diz "Vai ao ar segunda, 02/11." e os estáticos com rótulo "NA TV · SEGUNDA, 02/11" levam a data.
- Estado e views dos destaques no perfil hoje: sem dado (nenhuma ferramenta permitida lê destaque).

### 8.2 Um destaque "NA TV" faz sentido?

**Sim, no lugar do PROVA, por tempo definido** [HIPÓTESE]. Motivos:
1. É a única prova de terceiro publicável agora. O case de 6 para 20 (C1 e C2) espera a reedição do vídeo v2 [FATO, `02-provas.md`].
2. Quem engaja é de Campinas e região (53,1% só Campinas) [FATO, `ig_audience`], e a TV é de Campinas.
3. Story some em 24 h; destaque fica [FATO, Instagram 2017]. A série no feed vai até 21/11 (tl05 agendado [FATO, `listPosts`]); o destaque guarda o que os stories da série mostraram.
4. O PROVA não existe: chamar de NA TV não tira lugar de nada e mantém 4 destaques.

**Contra, e por isso as condições:**
- Texto vencido. st01 ("AMANHÃ, 18H30") não entra. Tudo com "vai ao ar" ou "SEGUNDA, 02/11" entra até 02/11 e sai em ter 03/11, trocado pela versão "NA TV CÂMARA CAMPINAS" sem data ou por "Foi ao ar" (só com horário confirmado, F4).
- Autorização. A liberação da Mirna é verbal e fala de uso nas redes [FATO, contexto.md]; destaque é permanente. Perguntar na mesma conversa em que o Bruno pede o @ e o horário (F4, seção 6.4) se o destaque está ok. Sem resposta, o destaque fica só com peças em que ela não aparece nem fala (mc02, mc03, B1).
- Nome e capa. "NA TV" em texto, preto e ouro, Cinzel; nada de logo da emissora; nunca "a TV recomenda" nem "ao vivo" [FATO, `02-provas.md` e F4].
- Edição exibida: só o link (termos). Nada de filmar a tela da TV nem recortar a edição.
- Peso da prova: as edições do programa no site têm de 27 a 1.400 views, mediana de 80,5 [FATO, F4, conta sobre a página do programa]. O destaque se apoia no que o Bruno disse na entrevista. Nenhum número de audiência entra nele, e como a entrevista surgiu é sem dado [FATO, `02-provas.md`].

**Conteúdo, na ordem, só com peças que existem ou já estão no `03-plano`:**

| Ordem | Peça | Entra | Sai |
|---|---|---|---|
| 1 | B1: "Gravei uma entrevista para a TV Câmara Campinas." (estático e1) | dom 25/10 | ter 03/11, trocado pela versão sem "vai ao ar" |
| 2 | mc02: "Eu sou estrategista de marketing digital e lançamento de um produto." (refeito começando em "Eu") | dom 25/10 | fica |
| 3 | Compartilhamento do tl01 (com a menção à Mirna) | dom 25/10, 18h35 | fica |
| 4 | M8 e M9 (estáticos "NA TV" de qua 28/10) | qua 28/10 | fica |
| 5 | pf01 (franquia odontológica, fato do caso) | ter 27/10, 16h | fica; é de dentista, vai depois das peças gerais |
| 6 | "Foi ao ar." (F4) | seg 02/11, só com horário confirmado | fica |
| 7 | "A entrevista inteira está aqui", com link da edição (F4) | quando a edição estiver no site ou no YouTube | fica |
| 8 | DIAGNÓSTICO · 12 CASAS com link | dom 25/10 | fica, sempre por último |

**Os outros três, sem gravar nada:**
- COMECE AQUI (1º): pôr na frente "Você atende. Eu desenho e comando o seu lançamento." (story-frase-1, que sai hoje), mc02 e o DIAGNÓSTICO com link; os 3 da Escala vão para o fim ou saem (são animação sem o Bruno, contra a regra medida de 21/10).
- MÉTODO (3º): po01 compartilhado e M2 ("Cada lance tem data, responsável, número esperado e plano B.").
- QUEM SOU (4º): pb01 compartilhado, mc01 e J8 (Campinas) depois de conferido.

**Quando reavaliar:** Módulo 7 de seg 23/11. Views por destaque: sem dado. Medida possível: visitas ao perfil e cliques no site por semana (`ig_account_stats`), antes e depois de 25/10. Quando o case de 6 para 20 for reeditado, o conselho decide se o NA TV vira PROVA (com a TV dentro) ou se fica um 5º destaque.

---

## 9. Objeções: o mapa com prova e dia

### 9.1 O que é medido

- Frequência real de cada objeção: **sem dado**. O `01-objecoes.md` registrou 0 objeção escrita em comentário (2 comentários de terceiros em 120 dias) e em direct (50 conversas). Esta versão não pôde reler: `ig_comments` e `ig_inbox` estão fora da lista, e a busca de mercado no Buzzfy deu erro de limite (seção 0, item 7).
- Instrumentos que vão existir a partir de 25/10: enquete diária no story da objeção e caixa semanal, contados à mão pelo Bruno.

### 9.2 Objeções novas (hipóteses, frequência sem dado)

**O13 · "Eu vendo serviço, não curso."** Variações: "Meu negócio é atendimento." · "Não tenho o que ensinar."
- Por que entra: a frente pede "expert e prestador de serviço"; as 12 objeções falam de consultório e de infoprodutor, e a O8 trata de indicação, não do produto.
- Prova: os dois casos contados na TV são de negócio que não é curso, restaurante (C4) e franquia odontológica (C3); M3 ("Cada cliente tem um produto específico..."); C5 ("As pessoas me contratavam para resolver problemas nas empresas delas."); a legenda do Dentista B agendada para hoje ("Se a sua técnica faz outro dentista perguntar 'como você fez isso?', ela já é um segundo produto.") [FATO, `02-provas.md` e `listPosts`].
- Limite: o serviço do Bruno é comando de lançamento; a virada não promete que todo serviço vira curso.

**O14 · "TV de Câmara? Isso não prova nada."** Variações: "Qualquer um aparece em TV local." · "Pagou para aparecer?"
- Por que entra: nasce com a própria prova. A partir de 25/10 a TV é a prova principal dos stories, e as edições do programa têm audiência pequena no site (mediana de 80,5 views) [FATO, F4]. [HIPÓTESE] quem não é de Campinas pesa menos a emissora.
- Prova: o conteúdo da entrevista. Casos C3 e C4 como fato do caso, Método Xeque-Mate (M1) e a fala da repórter T2 ("Você mostra mesmo que está antenado.", 1208,5 a 1210,9 s) como pergunta da entrevista, nunca como selo. Depois de 02/11, o link da edição deixa qualquer um conferir.
- Limite: como a entrevista surgiu é sem dado [FATO, `02-provas.md`]: a virada não diz "fui convidado" nem "não paguei".

**O15 · "Meu público é daqui de Campinas. Lançamento é para quem vende para o Brasil todo."**
- Por que entra: 53,1% de quem engaja é de Campinas [FATO, `ig_audience`]; o Bruno ocupa a cadeira de estrategista de lançamento num grupo de negócios local (R1) [FATO, `02-provas.md`].
- Prova: **fraca**. Onde ficam o restaurante e a franquia: sem dado. J8 (Shopping Dom Pedro) é carreira na noite, não marketing. Sem caso local com número.
- Uso: só na caixa de pergunta e na enquete até o Bruno dizer onde foram os casos. Sem story de virada.

Variação da O1, sem virar objeção nova: "Se ele é bom, por que tem 1.618 seguidores?" A resposta já está no contra-argumento da O1 (quem aparece é o expert). Número de seguidores nunca na tela [FATO, `02-provas.md`, "O que NÃO pode ser dito"].

### 9.3 Mapa de 25/10 a 21/11

Prova pelo id do `02-provas.md`. "Conferir" = ouvir o áudio antes de usar (lista do `02-provas.md` e do `03-plano`).

| Objeção | Etapa | Prova | Estado da prova | Dia proposto | O que a exibição muda |
|---|---|---|---|---|---|
| O1 Nunca ouvi falar de você | Confiança | B1, mc02 (M11), C1 | B1 e M11 prontos; C1 como texto da bio, vídeo v2 só reeditado | dom 25/10 (`03-plano`) | Depois de 02/11 ganha "Foi ao ar" e o link da edição |
| O2 Não tenho tempo | Desejo | M3, M4 | M3 pronto; M4 conferir (1320,5 s marcado M) | seg 26/10 | nada |
| O8 Isso é pra infoprodutor | Descoberta | M6, C3 (pf01) | prontos | ter 27/10 | nada |
| O3 Já me queimei | Confiança | M7, M8, M9, M10 | prontos | qua 28/10 | Se o ci01 for para 02/11 (F4), a chamada das 20h30, o compartilhamento das 21h05 e o repost de qui 09h00 do `03-plano` mudam; a objeção fica no dia |
| O4 Já tentei e não vendeu | Confiança | M1, M2 | prontos | qui 29/10 | Se o po01 for para 04/11 (F4), a sub "Quinta, 21h, eu explico no feed.", a chamada e o compartilhamento mudam |
| O6 É caro | Ação | M10 e a frase dos 30 min do deck | parte variável do contrato: conferir com o Bruno | sex 30/10 | nada |
| O5 Medo de me expor | Desejo | M2, J10, "você passa a segurança" | J10 por estático até o mc04 ser recortado; conferir "pro seu" (1423,0 s) | sáb 31/10 | nada |
| O12 Vou fazer um curso | Desejo | M1, M4 | M4 conferir | dom 01/11 | nada |
| (nenhuma) | | | | seg 02/11 | dia da exibição (seção 4.3) |
| O14 TV de Câmara não prova | Confiança | C3, C4, M1, T2 | prontos; link da edição quando existir | ter 03/11 | nasce com a exibição |
| O9 Meu problema é tráfego | Interesse | M1 e "gatilhos corretos" (1608,3 a 1611,2 s), C1 | prontos | qua 04/11 | casa com o po01, se ele for para 04/11 |
| O11 Não sei se compraria | Interesse | "vou aprender com você" (1490,4 a 1495,4 s), M5, Lance 1 | prontos | qui 05/11 | nada |
| O13 Vendo serviço, não curso | Descoberta | C3, C4, C5, M3 | prontos | sex 06/11 | nada |
| Caixa semanal | | | | sáb 07/11 | |
| O15 Público local | Descoberta | sem prova | Bruno informa onde foram C3 e C4 | dom 08/11, só enquete | nada |
| O10 Audiência pequena | Interesse | sem prova aceita | conflito entre `01-objecoes` (caso 100 mil e 14 vendas) e `02-provas` (sem prova); o Bruno confirma cliente, ano e papel | qua 11/11, só se confirmado; senão, argumento sem número | nada |
| O7 Meu conselho não deixa | Descoberta | C3 e as resoluções (fonte secundária) | regra de cada conselho a conferir; nada de orientação jurídica | ter 10/11, só depois da conferência | nada |
| As 2 objeções com mais SIM na S1 | | as mesmas da S1, com outra prova | | qui 12/11 e sex 13/11 | |
| Caixa semanal | | | | sáb 14/11 | |
| S4 (15 a 21/11) | | rodízio das 3 objeções com mais votos e respostas de caixa em S1 a S3 | | dom 15/11 e sex 20/11 são feriado: molde sem bloco à mão [HIPÓTESE; alcance em feriado sem dado] | |

---

## 10. O que muda no `03-plano-7-dias` com a data de 02/11 (só o delta)

1. "Sem contagem regressiva" e "Nenhum texto cita data de ida ao ar" deixam de valer: a data tem fonte (mensagem do Bruno) e já foi publicada hoje às 19h30 no rótulo "NA TV · SEGUNDA, 02/11" [FATO, `listPosts`]. A contagem entra no texto do 1º story (seção 5.2).
2. dom 25/10 09h02: a linha "Votou SIM? Responde este story." aponta para a ETAPAS, que não dispara (seção 7).
3. qua 28/10 20h30 e 21h05, qui 29/10 09h00 (ci01) e qui 29/10 17h30, 20h30, 21h05 e sex 30/10 09h00 (po01): dependem das decisões do F4 (ci01 até ter 27/10 21h; po01 até qua 28/10 12h).
4. sex 30/10 17h31: "Responde este story com a sua área" diz que cai na ETAPAS (seção 7).
5. sáb 31/10 17h30: o `03-plano` diz que o tl02 não está agendado. Está: sáb 31/10 18h30, com "A entrevista vai ao ar na segunda, 02/11." na legenda [FATO, `listPosts`].
6. O repost das 09h00 sai do 1º lugar da pilha (seção 4.3). O reel de ontem já foi compartilhado na noite anterior.
7. Hoje, sáb 24/10: a chamada das 20h30 ("story-teaser-21h.png", chamada "Hoje 21h no feed") segue agendada [FATO, `listPosts`]; o `03-plano` já manda apagar depois das 21h. Continua pendente para o Bruno.

---

## 11. Como medir stories no Módulo 7

- **Toda noite às 23h** (pelo menos nos 7 dias da S3): `ig_posts` kind=stories e `ig_post_stats` da pilha. Por story: alcance, views, avançar, voltar, deslizar, sair, respostas, visitas ao perfil. Por dia: alcance do story mais visto e retenção do bloco (alcance do último story do bloco dividido pelo do primeiro).
- **Toda segunda:** `ig_account_stats` de 7 dias (views e alcance de story, respostas, visitas ao perfil, cliques no site) e os logs da ETAPAS de story e da TABULEIRO.
- **À mão, pelo Bruno, antes de o story expirar:** votos de cada enquete, respostas de caixa (classificadas de O1 a O15), toques no link, lembretes da contagem (se houver), repostagem da Mirna nas 3 menções, mensagens de WhatsApp com nota do Tabuleiro.
- **Registro:** `conteudo/stories-objecoes/02-medicao.md` (previsto no `01-objecoes.md`, ainda não existe) e a rodada em `sistema-instagram/semanas/`.
- **Leitura de 02/11:** cai no feriado e no dia da exibição. A pilha de dom 01/11 expira entre seg 09h00 e 18h35; quem rodar o Módulo 7 às 18h30 de seg perde a de domingo de manhã. Ler a pilha de domingo às 23h de domingo.

---

## 12. Lacunas

- Frequência real de cada objeção: sem dado (sem `ig_comments` e `ig_inbox` nesta rodada; busca de mercado no Buzzfy com erro de limite).
- Horário da exibição de 02/11: sem dado. Decide se a contagem nativa entra.
- Como o sticker de contagem se comporta hoje (aviso ao criador, hora do lembrete com "dia todo", editar a hora): só fontes de terceiros de 2018 e 2024; Central de Ajuda não encontrada.
- Pilha de hoje: lida com menos de 2 h nos stories da TV; a leitura completa precisa acontecer antes de dom 25/10 09h33.
- Quantos stories saíram por dia antes de hoje e quanto cada um teve: sem dado.
- Estado e views dos destaques no perfil: sem dado. Capa NA TV (ou PROVA): não existe.
- Se a liberação verbal da Mirna cobre destaque permanente: sem dado.
- Onde ficam o restaurante e a franquia odontológica: sem dado (decide a O15).
- Caso "100 mil seguidores, 14 vendas": cliente, ano e papel do Bruno sem dado (decide a O10).
- Tempo de resposta do Bruno ao direct: sem dado (decide se "Responde com a sua área" fica).
- Alcance da conta em feriado (02/11, 15/11 e 20/11): sem dado.
- Toques em link, votos e respostas de caixa: nenhuma ferramenta permitida lê; dependem da contagem do Bruno.
