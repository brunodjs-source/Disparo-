# F5 · Capacidade e estoque · @o_estrategista.com.br

Frente F5 da pesquisa do conselho Agência Reunida. Rodada de sábado, 24/10/2026, escrita às 15h15 (São Paulo), depois do fato novo das 14h40 (a entrevista vai ao ar na segunda-feira, 02/11/2026; o Bruno marca a Mirna nas postagens). Substitui a versão das 14h10, que está no histórico do git (commit 88433c7). Só leitura: nada foi publicado, agendado ou alterado no Instagram, no Buzzfy ou no PostZen. Toda mudança abaixo é proposta para o Bruno executar.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, nível 4, que nunca fecha objeção sozinho. Métrica que falta: "sem dado".

**Horários:** datas de arquivo e de commit estão em UTC no sistema; aqui aparecem no horário de São Paulo (UTC menos 3 h).

**Régua:** esta frente conta peças, minutos e travas; não decide mediana. Onde cita desempenho, usa a do Buzzfy: normal de 57 views e pulo normal de 70,9% [FATO, `ig_reel_checkup` às 15h05].

---

## 0. Respostas curtas

1. **A agenda mudou depois das 14h10.** O PostZen tem agora 20 publicações de 24/10 a 23/11: 4 publicadas (stories de hoje) e 16 agendadas, com tl02 a tl05 agendados nos sábados 31/10, 07/11, 14/11 e 21/11 às 18h30 [FATO, `listPosts` às 15h08]. A legenda do tl01 trocou a promessa: "O mais votado eu solto inteiro depois que a entrevista for ao ar" [FATO, `listPosts`]. Isso cria um corte novo obrigatório depois de 02/11, trabalho só da agência.
2. **Vagas abertas de 01/11 a 21/11:** 12 reels (4 por semana, pois cada semana já tem 1 timelapse) e 7 carrosséis (1 da S1 e 2 por semana de S2 a S4) [ESTIMATIVA: regra de 5 reels e 2 carrosséis do CLAUDE.md menos o agendado]. A S1 já tem 6 reels agendados, 1 acima da regra [FATO, `listPosts`]. Se o portão tirar tl03 a tl05, as vagas de reel sobem para 15.
3. **Pronto, renderizado e fora da agenda: 3 reels, todos com trava.** Dentista C (brief do dentista o guarda para anúncio depois de 18/11), case Tzur v2 (autorização do cliente; fala "comenta estrategista" aos 48,4 s, que dispara a automação ESTRATEGISTA da conta toda) e pf01 como reel (só com DOBRAR) [FATO, seção 3.2].
4. **Sem gravação, com trabalho só da agência:** ob01 a ob03 (base composta às 14h36 e 14h37, render final sem dado), o "mais votado inteiro", 6 cortes do banco da entrevista, 3 remakes do arquivo do Instagram (Trial Reel), 41 estáticos de story do plano de 25 a 31/10 e 7 carrosséis. Somam de 4 a 10 reels de feed para 12 vagas, mais os 3 remakes fora da contagem de vagas [ESTIMATIVA, seção 8].
5. **Só com gravação do Bruno:** 19 roteiros de nicho (4 com teleprompter pronto), a selfie do REACT (20 min), o vídeo curto do dia 02/11 e 21 reels do Módulo 3. Desde a fala do dentista (entregue perto de 13h12 de 21/10) não entrou nenhuma gravação nova no repositório nem na pasta de trabalho [FATO, `find`].
6. **O que falta sem gravar é formato, não vaga.** Sem gravação, as 12 vagas fecham com cortes da TV, em que o Bruno aparece de perfil atrás do monitor [FATO, quadros 0 e 2,5 s de ob01 a ob03]. O formato que mediu melhor, o Bruno falando de frente para a câmera (mediana de 167,5 de alcance contra 32,5 da animação [FATO, F1]), só volta com gravação nova ou com os 3 remakes de 03 a 05/10, em 720p.
7. **Agenda mínima:** 1 bloco por semana. Bloco 1 até qua 28/10, 23h59: roteiro 1 (consórcio) e roteiro 3 (nutricionista), os dois do teleprompter, com as versões travadas, mais o vídeo curto de 02/11: de 31 a 49 min [ESTIMATIVA]. Blocos 2 a 4: 2 roteiros, de 24 a 42 min; a selfie do REACT entra no bloco 2, depois da exibição [ESTIMATIVA, seção 9]. Piso de uma semana apertada: 1 roteiro, de 12 a 18 min.
8. **Vídeo curto de 02/11 sem depender do feriado:** gravar no bloco 1 com a data falada ("segunda, 2 de novembro") e sem horário; o horário entra como texto quando a grade sair. A grade da TV Câmara só vai até dom 25/10 [FATO, tvcamaracampinas.com.br às 15h12]. Sem o vídeo, o dia fecha com o estático 7 já renderizado ("Vai ao ar segunda, 02/11"), um estático novo com o horário e as manchetes mc02 e mc03.
9. **Trial Reel pelo PostZen existe na ferramenta:** a descrição do `createPost` aceita `trialParams` em reel; conta não elegível falha só na hora de publicar [FATO, descrição da ferramenta, lida sem chamar]. Elegibilidade da conta: sem dado. A mesma descrição confirma que marcar pessoa (`userTags`) só vale em post de foto do feed, e que convite de colaborador pede o @ (até 3).
10. **A gravação é a menor parte da carga do Bruno.** Stories com sticker à mão (27 na S1), respostas à mão e marcação da Mirna em 9 reels e 1 story somam cerca de 5 vezes os minutos de gravação (de 139 a 278 min contra 31 a 49) [ESTIMATIVA com PRIOR dentro, seção 6].

---

## 1. Fontes conferidas nesta rodada

| Consulta ou arquivo (só leitura) | Hora (SP) | Resultado |
|---|---|---|
| PostZen `listPosts`, conta j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 03h00 UTC a 24/11 03h00 UTC, ordenado por data | 15h08 | OK. 20 itens: 4 publicados, 16 agendados |
| PostZen `listCommentAutomations`, mesma conta | 15h14 | OK. 17 automações ativas; TABULEIRO com 0 disparo; ESTRATEGISTA e CASE valem para a conta toda |
| PostZen: descrição da ferramenta `createPost` (esquema carregado, ferramenta não chamada) | 15h14 | Lida. `trialParams` em reel; `collaborators` até 3 em feed, reel e carrossel; `userTags` só em post de foto do feed |
| Buzzfy `ig_reel_checkup`, 5 últimos reels | 15h05 | OK. Normal 57 views e 70,9% de pulo; janela de sequência fechada; 5 candidatos a refazer |
| Buzzfy `ig_reel_checkup`, 5 ids (3 remakes, "Você gravou o curso inteiro", "O que você recusa") | 15h07 | OK, com tags de formato |
| Buzzfy `ig_posts`, reels de 03 a 06/10 com `include_media_urls` | 15h06 | OK. 4 reels; `video_url_withheld: false` nos 3 remakes |
| Pedido HEAD nos 3 `media_url` dos remakes (cdninstagram.com) | 15h06 | HTTP 200, `video/mp4`, 7.668.112, 4.917.903 e 5.715.025 bytes; etiqueta `C3.720` (720p) |
| Buzzfy `buzzfy_playbook` (second_life) | 15h07 | OK |
| GET das 6 imagens de story de hoje (media.postzen.dev) e md5 contra `estaticos/stories-frases` | 15h10 | HTTP 200 nas 6 |
| HEAD de tl02 a tl05, pf01 e Dentista B em media.postzen.dev, tamanho contra o render local | 15h11 | HTTP 200; tamanho igual ao do render local nos 6 |
| tvcamaracampinas.com.br/programacao/2026-11-02 e 2026-10-26 (leitura com `curl`) | 15h12 | HTTP 200, mas redireciona para 24/10; a grade publicada vai de 19/10 a 25/10 |
| `ffprobe`, `ffmpeg` (quadros 0 e 2,5 s das bases de ob01 a ob03), `du`, `df`, `find`, `md5sum`, `git log`, logs `fila*.log` e `rev_ob/r*.log` | 15h00 a 15h15 | OK |
| Arquivos: contexto.md, 00-enquadramento.md, F1, F2 e F3 (versões de 14h48 a 15h07), F4, pecas-e-calendario.md, catalogo-formatos.md (seções 1, 4, F1 e 8), roteiros-20-videos.md, teleprompter-5-nichos.md, 10-decision-brief.md, 00-SISTEMA.md (Módulo 3), 03-plano-7-dias.md e .json, fichas `videos/tv-camara/cortes/*.spec.json`, `videos/cases/tzur/edit.json`, `estaticos/stories-frases/s.html` | 15h00 a 15h15 | OK |

**Erros de consulta:** nenhum. **Não consultado:** Google Drive (fora da lista de ferramentas desta rodada), `ig_inbox` e qualquer agenda do Bruno.

---

## 2. O que mudou desde a versão das 14h10

| Item | 14h10 | 15h15 |
|---|---|---|
| Agenda no PostZen | 16 itens, nada depois de sex 30/10 | 20 itens; tl02 sáb 31/10, tl03 sáb 07/11, tl04 sáb 14/11, tl05 sáb 21/11, todos 18h30 [FATO, `listPosts`; commit 318e97d às 14h41] |
| Promessa do tl01 | "O mais votado sai no próximo sábado" | "O mais votado eu solto inteiro depois que a entrevista for ao ar" [FATO, `listPosts`] |
| Legendas | sem data | tl01 e tl02 dizem "A entrevista vai ao ar na segunda, 02/11." [FATO] |
| Reels na S1 | 5 | 6 (tl02 entrou no sáb 31/10) [FATO] |
| Arquivo só na pasta temporária | tl02 a tl05, mc02 a mc04, fonte | tl02 a tl05 têm cópia no PostZen com o mesmo tamanho [FATO, HEAD]. Continuam só na pasta temporária: mc02 a mc04, as bases de ob01 a ob03 e a fonte da entrevista |
| ob01 a ob03 | só ficha | base composta às 14h36 e 14h37 (537, 864 e 453 quadros); fichas de ob02 e ob03 editadas às 15h01; render final sem dado [FATO, `rev_ob/r1.log` a `r3.log`, `git status`] |
| Voz no ob01 | conferir se é do Bruno | a ficha registra: "Boca conferida no Z2: a Mirna fica parada de 1312,5 a 1326,4 s; quem fala é o Bruno" [FATO, `ob01.spec.json`] |
| Trial Reel pelo PostZen | sem dado | a ferramenta aceita `trialParams`; elegibilidade da conta sem dado [FATO, descrição do `createPost`] |
| Estáticos de frase | 7 e 8 com "EM BREVE" | 7, 8 e 9 renderizados de novo com a data de 02/11 [FATO, commit 318e97d] |

---

## 3. O que existe pronto

### 3.1 Agendado no PostZen (ponto de partida, não é estoque livre)

[FATO, `listPosts` 15h08, horário de São Paulo]

| Semana | Reels | Carrossel | Stories |
|---|---|---|---|
| sáb 24/10 (hoje) | Dentista B 21h00 (TABULEIRO) | | 4 publicados (14h00, 14h03, 15h00, 15h01); 4 agendados (16h30, 18h00, 19h30, 20h30) |
| S1, dom 25 a sáb 31/10 | tl01 dom 18h30; pb01 seg 21h; ci01 qua 21h; po01 qui 21h; pb02 sex 21h; tl02 sáb 18h30 (6) | car01 ter 12h | pf01 ter 16h |
| S2, dom 01 a sáb 07/11 | tl03 sáb 18h30 (1) | nenhum | nenhum |
| S3, dom 08 a sáb 14/11 | tl04 sáb 18h30 (1) | nenhum | nenhum |
| S4, dom 15 a sáb 21/11 | tl05 sáb 18h30 (1) | nenhum | nenhum |

Os arquivos dessas 20 publicações estão hospedados no PostZen.

### 3.2 Reels renderizados e fora da agenda

| Peça | Duração | Bruno nos 3 primeiros segundos | Arquivo | Trava | Esforço para sair |
|---|---|---|---|---|---|
| Dentista C (9x16, 4x5 e leve) | 36,4 s | Sim, selfie falando "Dentistas," no quadro 0 [FATO, quadros da versão das 14h10] | `videos/nichos/dentista/render/` | Brief do dentista de 21/10: amostra e anúncio 4:5 depois de 18/11, com a Res. CFO 196/2019 conferida [FATO, enquadramento item 11]. Terceira edição da mesma fala do A (no ar) e do B (hoje 21h) | Zero de agência; decisão do Bruno |
| Case Tzur v2 (v1 de 29,8 s também pronto) | 54,3 s | Sim, primeiro corte é do Bruno (`edit.json`, `"src": "bruno"`) [FATO] | `videos/cases/tzur/` | Autorização da Tzur Capital: sem dado. A fala pede "comenta estrategista" de 48,4 s a 48,8 s [FATO, `edit.json`], que dispara a automação ESTRATEGISTA, ativa na conta toda [FATO, `listCommentAutomations`] | Re-editar o fim (trocar o CTA): sem medida |
| pf01 como reel | 24,0 s | Em cena, mas no Z2: o Bruno de costas e a Mirna de frente [FATO, quadros da versão das 14h10] | PostZen (como story de ter 27/10) e pasta temporária | Reel só com DOBRAR de profissão nomeada [FATO, pecas-e-calendario] | Zero |

### 3.3 Com ficha e base composta, sem render final (agência, sem gravação)

| Peça | Base composta | Quadro 0 e 2,5 s da base | O que falta | Data sugerida no 03-plano |
|---|---|---|---|---|
| ob01 (O2 "Não tenho tempo pra lançar") | 537 quadros, 17,9 s | Bruno de perfil atrás do monitor; um braço de camisa azul na borda esquerda [FATO, conferência visual] | Render final com cartão, legenda e CTA; folha de 4 quadros por segundo | qua 04/11, 21h |
| ob02 (O1 "Nunca ouvi falar de você") | 864 quadros, 28,8 s | Idem [FATO] | Idem; a ficha foi editada às 15h01 | seg 02/11, 21h |
| ob03 (O8 "Meu consultório vive de indicação") | 453 quadros, 15,1 s | Idem [FATO] | Idem; ficha editada às 15h01 | sex 06/11, 21h |

[FATO, `rev_ob/r1.log` a `r3.log` e `conferir.txt`] A revisão de áudio de 5 trechos (comparação entre a transcrição bruta e a voz tratada) estava aberta às 14h38. Os 3 não pedem nada do Bruno; o CTA deles é "Me manda a sua área no direct" [FATO, `ob01.spec.json`]. [HIPÓTESE] O braço na borda é da repórter: conferir se pede marcação.

### 3.4 Stories prontos

- **Vídeos da entrevista fora da agenda:** mc02 (4,5 s), mc03 (11,0 s) e mc04 (9,5 s), só na pasta temporária [FATO, `ls`]. O mc04 pede recorte novo sem "como estrategista digital" [FATO, enquadramento item 8].
- **Estáticos de frase (10 PNG):** 5 já usados hoje, com md5 igual ao do PostZen: 1 ("Você atende", 16h30), 2 ("Fila é teto", 18h00), 6 (chamada das 21h, 20h30), 9 ("Nem tudo é ouro" com NA TV · SEGUNDA, 02/11, 19h30) e 10 ("A pergunta da TV", 15h00) [FATO, md5]. O estático de bastidor das 14h03 não bate com nenhum arquivo atual: o 7 foi renderizado de novo às 14h41 [FATO, md5 e commit 318e97d].
- **Livres:** 3 ("Lançamento é xadrez. A maioria joga dama."), 4 ("O lead que não comprou vale mais do que o que comprou."), 7 (BASTIDOR, "Gravei uma entrevista para a TV Câmara Campinas. Vai ao ar segunda, 02/11.") e 8 (NA TV · SEGUNDA, 02/11, "Eu só tinha um computador e um sonho.") [FATO, `s.html`]. O 8 repete a frase do mc01 (publicado hoje às 15h01) e da capa do car01. O 5 repete a frase do 9.
- **Plano de 25 a 31/10 (03-plano-7-dias.json):** 56 stories, 15 com vídeo que já existe e 41 estáticos com ficha e sem render; 27 MANUAL (sticker, o Bruno posta pelo app) e 29 AGENDADO [FATO, contagem no .json]. De 01/11 em diante: nenhum plano.

### 3.5 Carrosséis

- car01 (6 lâminas): agendado ter 27/10 12h. **Único carrossel pronto.**
- `estaticos/checklist` (8 slides): as 10 perguntas do carrossel de 12/10, já usado [FATO, versão das 14h10].

### 3.6 Fotos e fonte

- 7 fotos de marca em `estaticos/stories-frases` (f1 a f5, e1, e2) [FATO, `ls`].
- Fonte da entrevista para cortes novos: `scratchpad/entrevista/src/` com 3 arquivos (1080p de 177 MB, zoom de 259 MB, áudio de 34 MB); a pasta `entrevista` soma 958 MB; `tv/render` soma 2,6 GB [FATO, `ls` e `du`]. O original fica no rascunho de release do GitHub e no Drive [FATO, ENGINE.md].
- Motores: entrevista (`videos/tv-camara/engine`, 10 modelos, com `objecao.html`) e dentista (modelos A, B e C) [FATO, `ls`].

### 3.7 Estoque que não entra no feed orgânico

| Peça | Motivo |
|---|---|
| v01 a v08, série 2 (r1 a r5 e 5 estáticos), stories s01 a s08 | Animação com voz sintética, já publicados de 11 a 20/10; CLAUDE.md exige o Bruno nos 3 primeiros segundos |
| Anúncio a01-campinas e 4 estáticos por nicho | Voz clonada e animação sem o Bruno no quadro 0; verba zero até 18/11 (D4 de 21/10) |
| Áudios de `scratchpad/minhavoz` (13/10) | Material da voz clonada do anúncio, sem imagem |
| Reel de 01/01/2025 (9,14x) | Pessoal, fora da grade e do posicionamento [FATO, F1] |

---

## 4. Sem gravação nova, com edição da agência

### 4.1 Cortes novos da entrevista

- **"O mais votado inteiro"** (promessa da legenda do tl01): 1 corte, depois de 02/11 [FATO, `listPosts`]. Se o mais votado for o assunto 2, 3, 5 ou 7, o trecho já saiu cortado antes da exibição (pb01, pb02, ci01, po01); se for o 4, é o pf01; o 1 e o 6 não têm peça [FATO, pecas-e-calendario]. Em todos os casos "inteiro" pede uma versão mais longa que os cortes de 20 a 37 s [HIPÓTESE sobre a leitura da promessa].
- **Banco do catálogo e do pecas-e-calendario:** pb03 ("eu construí tudo"), CINEMA 02, MITO, PERGUNTA 01 e 02, SALA [FATO]. São 6, nenhum com ficha. CARROSSEL 02 a 04 também.
- Todos têm o Bruno em cena no plano CB ou Z2, de perfil ou de costas, nunca de frente para a câmera [FATO, recortes fixos do catálogo e quadros de ob01 a ob03].

### 4.2 Remakes do arquivo do próprio Instagram

| Reel | Normal | Pulo | Duração | Formato (tags do Buzzfy) | Legenda queimada | Primeiro corte |
|---|---|---|---|---|---|---|
| R1 "Ele nunca fez um anúncio" (sáb 03/10, 23h06) | 10,14x | 53,2% | 74,6 s | talking head, selfie, fala própria para a câmera | Não | 9,3 s |
| R2 "90% dos lançamentos que flopam" (dom 04/10, 11h11) | 4,42x | 45,7% | 69,5 s | talking head, selfie | Sim | sem corte medido |
| R3 "Problema de equipe" (seg 05/10, 21h58) | 3,61x | 49,6% | 74,7 s | talking head, selfie | Sim | sem corte medido |

[FATO, `ig_reel_checkup` e `ig_posts` às 15h06 e 15h07; HEAD HTTP 200 nos 3 arquivos, 720p]

- **Regra do playbook:** mudar pelo menos 2 coisas reais (abertura nova, legenda se houver fala, corte de 20% a 40%, resposta a comentário) e postar como Trial Reel; se passar do alcance usual, compartilhar no feed. Remake de reel com 5x ou mais bate o alcance usual em 35% das vezes; de 2x a 5x, em 15% [FATO, `buzzfy_playbook` second_life].
- **Quem posta:** pelo PostZen, se a conta for elegível a Trial Reel (`trialParams`, graduação MANUAL ou automática) [FATO, descrição do `createPost`]; elegibilidade: sem dado, e a falha só aparece na hora de publicar. Se falhar, o Bruno posta pelo app.
- **Limite do arquivo:** 720p [FATO]. Original do celular: sem dado. Qualidade no 1080x1920: [HIPÓTESE], conferir na folha de quadros.
- **R1:** a legenda promete "uma saga de 7 dias" que acabou em 09/10 e precisa sair [FATO, `ig_posts`].
- **Fora dos remakes sem gravação:** "Você gravou o curso inteiro" (3,75x, pulo 86,9%) é slideshow com narração e sem pessoa [FATO, tags `no_person`, `voiceover`]. Refazer com o Bruno é gravação nova (dia 11 do Módulo 3). Tem automação própria: PESQUISA, ligada a esse post [FATO, `listCommentAutomations`].

---

## 5. O que depende de gravação do Bruno

| Item | Quantidade | Minutos do Bruno | Trava antes de gravar ou publicar | O que destrava |
|---|---|---|---|---|
| Roteiros de nicho (`roteiros-20-videos.md`) | 19 (o 2 saiu em 21/10). Com teleprompter pronto: consórcio, nutricionista (versões A e B), psicólogo e advogado [FATO, `teleprompter-5-nichos.md`] | 12 a 18 por roteiro [ESTIMATIVA: 60 a 90 min para 5, linha 9 do próprio documento]. Medida real: sem dado | Consórcio: tomada com e sem a linha dos 41,9% (ABAC). Nutricionista: versão A ou B pela vigência da CFN 856 (leitura prevista até 28/10). Psicólogo e advogado: linha do case Tzur, gravar também sem case; advogado só com o provimento da OAB lido; psicólogo: +151,1% segue nível 3 [FATO, teleprompter e 10-decision-brief]. Status das leituras: sem dado | Linha de nicho do D1 de 21/10 e o Bruno falando para a câmera |
| Selfie do REACT | 1 sessão: 6 reacts (saem 3), 12 aberturas "Isso eu falei na TV." e a abertura do timelapse | 20 [FATO, estimativa do catálogo, ficha F1] | Mesmo enquadramento dos reels de nicho. O gancho "Dei uma entrevista para a TV Câmara Campinas" vale antes; "Fui ao ar" só depois do horário confirmado [FATO, catálogo e 02-provas] | REACT 01 a 03 e PB versão A |
| Vídeo curto do dia 02/11 (seção 5.1) | 1 fala de 10 a 15 s, 2 tomadas | 3 a 5 [ESTIMATIVA: 2 tomadas de 15 s e preparo] | Horário da exibição: sem dado. Proibido "ao vivo", "rede nacional", "a TV me convidou" e similares [FATO, 02-provas] | Rosto do Bruno no dia da exibição |
| Reels do Módulo 3 com o Bruno | 21 dos 22 reels da tabela (o dia 1 é o case v2) [FATO, contagem no 00-SISTEMA] | 18 cada [ESTIMATIVA, 90 min para 5 no 00-SISTEMA] | Regras de texto. Sobreposições: dia 11 é o "Você gravou o curso inteiro"; dia 26 (objeção tempo) é coberto pelo ob01; dias 16 e 22 são dentista e advogado | Linha geral do Bruno para a câmera |

**Fila somada:** 19 + 21 = 40 gravações, mais a selfie do REACT e o vídeo de 02/11 [FATO, contagem]. A 2 roteiros por semana entram 8 nas 4 semanas, 20% da fila [ESTIMATIVA].

### 5.1 Vídeo curto do dia 02/11

- **Função:** chamada para assistir, com o rosto do Bruno, num dia em que o feed pode ficar sem reel (F2 e F4 recomendam nenhum reel extra no dia [FATO]).
- **Texto sugerido** (sem promessa, sem travessão, sem "hoje" para poder ir agendado, regra do 03-plano [FATO]): "Segunda, 2 de novembro, a minha entrevista para a TV Câmara Campinas vai ao ar no programa Ser Empreendedor. O horário está aqui na tela." Duração de 8 a 12 s lida em ritmo normal [ESTIMATIVA, 25 palavras].
- **Quando gravar:** no bloco 1 (até qua 28/10). Assim o dia 02/11 não depende do Bruno num feriado [FATO, 02/11 é Finados, enquadramento]. Pode sair no dom 01/11 (véspera) e na seg 02/11, pelo PostZen como story.
- **Horário:** a grade publicada vai só até dom 25/10 [FATO, site às 15h12]. Quando sair, a agência põe o horário como texto (minutos). Se a grade não sair até dom 01/11 à noite, o texto vira "Confira o horário na grade da TV Câmara Campinas" e o link entra como sticker à mão.
- **Opção do próprio dia:** se a grade sair e o Bruno quiser, uma tomada nova com o horário falado, postada à mão: de 2 a 5 min [ESTIMATIVA].
- **Esforço da agência:** legenda queimada e faixa "NA TV" no modelo de manchete: [PRIOR] 15 a 30 min. Sem edição, o Bruno posta a tomada crua com texto do app.
- **Sem o vídeo:** estático 7 já renderizado, estático novo com o horário (render no `s.html`, minutos) e mc02 ou mc03. O dia fica coberto; perde-se o rosto.

### 5.2 Capacidade observada (fatos, amostra curta)

- [FATO, `git log`] Teleprompter dos 5 nichos no commit de 21/10 às 12h17.
- [FATO, `ls` na pasta de trabalho] A fala do dentista chegou como `raw.mp4` às 13h12 de 21/10: 36,4 s, 576x1024, uma tomada. Foram 55 min entre o commit do teleprompter e a chegada do arquivo, para 1 de 5 roteiros. Se o texto chegou ao Bruno antes do commit, o intervalo real é maior; o tempo de gravação dentro disso: sem dado.
- [FATO, `find`] Depois disso, nenhum arquivo de gravação nova do Bruno no repositório nem na pasta de trabalho até 15h15 de hoje. Gravações que estejam no celular dele: sem dado.
- [FATO, 00-SISTEMA] O plano de 21/10 previa 1 sessão de 90 min por semana (5 reels). A sessão de seg 26/10 do plano de nichos: confirmação sem dado.
- [FATO, 00-SISTEMA e `ig_posts`] O reel "Fila é teto" previsto para qui 23/10 não saiu e não tem arquivo.
- Leitura: 1 fala de 36 s em 3 dias depois de um plano de 90 min por semana. Pouca amostra para chamar de ritmo, mas basta para não planejar em cima de 90 min [HIPÓTESE].
- Arquivo recebido em 576x1024 [FATO]: o render sai em 1080x1920 a partir de uma imagem menor. [HIPÓTESE] Veio comprimido pelo aplicativo de mensagem; pedir o envio como documento ou pelo Drive mantém a resolução.

---

## 6. Carga do Bruno fora da gravação

| Tarefa | Quantidade | Minutos | Fonte |
|---|---|---|---|
| Stories com sticker postados à mão | 27 de 25 a 31/10 | Sem dado. [PRIOR] 1 a 2 min cada: 27 a 54 min na semana | 03-plano-7-dias.json |
| Marcar a Mirna depois de publicar | 9 reels agendados com plano Z2 ou aberto, ou voz dela (tl01 a tl05, pb01, pb02, ci01, po01), e o story pf01 [FATO, fichas `*.spec.json`] | Sem dado. [PRIOR] 1 a 2 min cada: 10 a 20 min em 4 semanas, 7 a 14 só na S1. Se o app deixa marcar reel já publicado: sem dado | fichas e contexto.md |
| Convite de colaboração (alternativa à marcação) | Até 3 @ por reel ou carrossel, pelo PostZen | Zero do Bruno, mas pede o @ da Mirna (sem dado) e o aceite dela | descrição do `createPost` |
| Respostas à mão em comentário e direct | Todo dia com reel de nicho no ar | 15 a 30 min por dia [ESTIMATIVA do D3 de 21/10]: 105 a 210 min na semana | 10-decision-brief |
| Remakes como Trial Reel | 3 | Zero se o PostZen publicar; sem dado se for pelo app ([PRIOR] 3 a 5 min cada) | `createPost` e F2 |
| Agendar no PostZen o que o conselho aprovar | S2 a S4: 12 reels, 7 carrosséis e os stories AGENDADO | Sem dado. Os agentes desta pesquisa não agendam | enquadramento |
| Uma vez | Print da liberação da Mirna; @ dela; horário da exibição; autorização da Tzur; ouvir 922,1 a 924,2 s e 1423,0 s; copiar o estoque para o Drive | Sem dado | enquadramento, seção 13 |

[ESTIMATIVA com PRIOR dentro] Numa semana com o bloco mínimo: gravação de 31 a 49 min, stories à mão de 27 a 54, respostas de 105 a 210, marcações de 7 a 14. Soma de 170 a 327 min. A gravação fica entre 15% e 18% da carga. Se faltar tempo, cortar stories à mão (passar a AGENDADO, sem sticker) libera mais minutos do que cortar a gravação, ao custo da medição por objeção.

---

## 7. Esforço de produção da agência

- **Captura medida** [FATO, `fila*.log`]: st01, 450 quadros em 37,2 s; tl04, 1.031 em 84,2 s; tl05, 1.059 em 94,3 s e 109,2 s; tl01, 1.095 em 102,9 s a 113,3 s; tl03, 1.080 em 202,2 s. De 0,08 a 0,19 s por quadro. O tl01 foi capturado 4 vezes no dia [FATO, fila3, 5, 7 e 12]: o custo maior foi a revisão.
- **Tempo de calendário observado** [FATO, `git log` em SP]: motor da entrevista 06h49; fichas e legendas de 10 cortes 07h26; car01 08h02; tl02 08h48; tl03 a tl05 em revisão 10h55, corrigidos 11h12, renderizados 11h42; data nova e tl02 a tl05 agendados 14h41; fichas de ob01 a ob03 14h42. Dentista em 21/10: áudio 13h26, motor 18h07, 3 modelos 18h59.
- **Por peça, com motor pronto** [ESTIMATIVA, tempo de calendário, não de trabalho]: corte da TV com ficha, cerca de 6 min (10 peças de 06h49 ao pf01 às 07h53); timelapse, cerca de 52 min (3 de 09h05 a 11h42); carrossel, cerca de 36 min (07h26 a 08h02); reel de nicho, teto de 1h51 (5h33 por 3, com o motor feito do zero).
- **Reel de nicho novo não é só render:** cada fala pede `words.json`, `headtop.json` e letreiros novos, mais a folha de 4 quadros por segundo com nota por efeito [FATO, motor do dentista e CLAUDE.md].
- **Remake:** sem medida. [PRIOR] 1 a 2 h cada.
- **Conclusão:** o gargalo da grade é o minuto do Bruno. A agência fecha as 12 vagas em contagem; o que ela não fabrica é o Bruno de frente para a câmera.

---

## 8. Oferta contra demanda, 25/10 a 22/11

Demanda pelo CLAUDE.md: 5 reels e 2 carrosséis por semana, mais stories diários.

| Semana | Agendado | Vagas abertas | Sem gravação e sem trava externa | Com trava | Com o bloco mínimo |
|---|---|---|---|---|---|
| S1, 25 a 31/10 | 6 reels e car01 | 0 reel (1 acima); 1 carrossel | 41 estáticos de story a renderizar | | Nada: o bloco 1 publica na S2 |
| S2, 01 a 07/11 | tl03 | 4 reels; 2 carrosséis | ob01, ob02, ob03 (3); "mais votado inteiro" (1); remakes R1 a R3 como Trial Reel (fora da conta de vagas) | pf01 (DOBRAR) | Consórcio e nutricionista (2) |
| S3, 08 a 14/11 | tl04 | 4 reels; 2 carrosséis | Cortes do banco (até 6, sem ficha) | Tzur v2 (autorização) | Psicólogo e o 2º do bloco 2 (2) |
| S4, 15 a 21/11 | tl05 | 4 reels; 2 carrosséis | Cortes do banco | Dentista C (brief, depois de 18/11) | 2 pela conferência de 11/11 |

**Reels de S2 a S4 (12 vagas)** [ESTIMATIVA]: sem gravação e sem trava externa, de 4 (ob01 a ob03 e o mais votado) a 10 (com os 6 do banco). Com trava: 3. Com o bloco mínimo: 6. Com gravação, a S2 fecha com 2 nichos, 2 ob e o tl03; sem gravação, com 3 ob, o mais votado e o tl03, todos da entrevista.

**Carrosséis (7 a produzir)** [ESTIMATIVA]: há 8 fontes sem material do Bruno (CARROSSEL 02 a 04 da TV; do Módulo 3: Os 5 Lances, Seguidor x comprador em versão nova, Carrinho, Oferta em 5 pilares, Resumo do mês) e 3 que pedem material dele (Recusas, Bastidor do dia do lançamento, Print do carrinho). Nenhum dos 11 tem arquivo [FATO, `ls estaticos/` e `videos/tv-camara/carrossel/`]. A cerca de 36 min cada, 7 carrosséis somam cerca de 4 h 12 min de agência [ESTIMATIVA].

**Stories:** plano só até 31/10. Para S2 a S4 há 5 objeções sem dia (O7, O9, O10, O11, O12), o banco de provas do 02-provas.md, os estáticos livres 3, 4, 7 e 8 e as manchetes mc02 a mc04 [FATO]. Trabalho só da agência, menos os stickers.

**Concentração de formato sem gravação:** a S1 tem 6 reels da entrevista seguidos [FATO]. Sem gravação, S2 a S4 somam mais 12 da entrevista, 18 em 4 semanas [ESTIMATIVA]. A regra 5 do portão do catálogo ("dois formatos sem selfie seguidos abaixo de 0,5x: só REACT e PB versão A ficam no feed") não tem saída sem gravação, porque os dois pedem selfie [FATO, catálogo seção 8].

---

## 9. Agenda mínima de gravação semanal (proposta)

**Regras do bloco**
- 1 bloco por semana, com o arquivo entregue até quarta 23h59. A agência edita quinta e sexta; o portão de segunda aprova; o agendamento segue o que o conselho decidir.
- Mesmo enquadramento do Dentista A: selfie, luz de frente, celular na altura dos olhos [FATO, ficha F1 do catálogo]. O letreiro atrás da cabeça usa o `headtop.json` da selfie.
- Enviar o arquivo original (documento ou Drive), não comprimido [HIPÓTESE da seção 5.2].
- Cada roteiro com 2 tomadas do gancho: o D1 de 21/10 já prevê trocar o gancho se o primeiro nicho ficar abaixo de 53 [FATO, 10-decision-brief]. Onde houver linha travada (ABAC, CFN 856, case Tzur), gravar as 2 versões.
- Medir o primeiro bloco com cronômetro e corrigir esta tabela no Módulo 7.
- Reserva: o playbook pede 1 ou 2 reels prontos esperando o dia em que um estoura [FATO, `buzzfy_playbook` hot_streaks, versão das 14h10].

| Bloco | Gravar até | Publica em | Mínimo | Acréscimo | Minutos [ESTIMATIVA] | Por quê |
|---|---|---|---|---|---|---|
| 1 | qua 28/10, 23h59 | S2, 01 a 07/11 | Roteiro 1, Consórcio "Cota no direct" (tomadas com e sem a linha da ABAC); roteiro 3, Nutricionista (versões A e B do teleprompter, que mudam nas linhas 1 e 2); vídeo curto de 02/11 | Roteiro 17, Dentista "Curso que ninguém comprou" (reserva) | Mínimo 31 a 49 (24 a 36 dos 2 roteiros, 4 a 8 das versões, 3 a 5 do vídeo); com acréscimo 43 a 67 | Fecha os 3 fixos do D1 de 21/10 (consórcio, dentista com A e B, nutricionista) no ar antes da conferência de qua 11/11, com 48 h. Muda o assunto e mantém o formato do Dentista A, como manda o playbook. Os 2 roteiros e o vídeo já têm texto pronto. Muda a versão das 14h10 (que punha o 17 no mínimo): o 17 vira reserva porque o dentista já tem A e B |
| 2 | qua 04/11, 23h59 | S3, 08 a 14/11 | Psicólogo do teleprompter (com e sem a linha da Tzur); Advogado do teleprompter só com o provimento da OAB lido, senão roteiro 6, Consórcio "Banco" | Selfie do REACT (20), gravada depois da exibição: o gancho "Fui ao ar na TV Câmara Campinas" só vale depois do horário confirmado | Mínimo 27 a 42; com REACT 47 a 62 | Psicólogo é o extra fixo do D2 de 21/10. O REACT na semana seguinte à exibição usa a data como gancho (F4) sem carregar o bloco 1 |
| 3 | sex 13/11, 23h59 | S4, 15 a 21/11 | Pela conferência de qua 11/11. Nicho com mediana de 53 ou mais e pulo mediano até 75%: 2 roteiros da semana 3 dos nichos de maior número (11, 12 ou 13). Abaixo: 2 reels do Bruno para a câmera fora de nicho (Módulo 3, dia 11 "Você gravou o curso inteiro" regravado e dia 4 "Agenda cheia"), mudando o assunto e mantendo o formato | Advogado (roteiro 5 ou 10) se o provimento da OAB estiver lido | 24 a 36 | O prazo vai a sexta porque a conferência é na quarta. A regra pede n de 2 por formato antes de PARAR (red team de 21/10) |
| 4 | qua 18/11, 23h59 | S5, de 22/11 em diante | Pelo Módulo 7 de 16/11 | Selfie do REACT, se não existir | 24 a 36 | |

**Soma das 4 semanas** [ESTIMATIVA]: mínimo de 106 a 163 min (cerca de 27 a 41 min por semana); com reserva e REACT, de 138 a 201 min.

**Piso de uma semana apertada:** 1 roteiro, de 12 a 18 min (o próximo da sequência). No bloco 1, o piso é 1 roteiro e o vídeo de 02/11: de 15 a 23 min. A linha de nicho fica com n menor que 3 em 11/11.

---

## 10. Plano se ele não gravar

**Gatilho:** nenhum arquivo até o prazo do bloco. No portão de segunda, as 2 vagas de nicho da semana seguinte passam para o estoque, nesta ordem:

1. **ob01 a ob03** (render da agência; o Bruno de perfil desde o quadro 0). Já ocupam 3 vagas na S2 pelo 03-plano.
2. **"O mais votado inteiro"** (corte novo, depois de 02/11; cumpre a promessa da legenda do tl01).
3. **Remakes R1, R2 e R3 como Trial Reel**, pelo PostZen se a conta for elegível, senão pelo app; a 6 h ou mais de qualquer reel do feed (o playbook mede 0,92x para reel com menos de 6 h do anterior [FATO, F2]). Só ocupam vaga do feed se baterem o alcance usual. São o único Bruno de frente para a câmera disponível sem gravar.
4. **tl03 a tl05**, já agendados, cada um só com o portão do anterior.
5. **Cortes do banco:** pb03, CINEMA 02, MITO, PERGUNTA 01 e 02, SALA.
6. **pf01 como reel**, só com DOBRAR.
7. **Case Tzur v2**, só com a autorização escrita da Tzur e o fim re-editado sem "comenta estrategista".
8. **Dentista C** fica fora até o brief do dentista ser revisto.

Nunca: animação com voz sintética, voz clonada, nem reel sem o Bruno nos 3 primeiros segundos [FATO, CLAUDE.md].

**Grade da semana sem gravação** (regra do catálogo, seção 8): 5 reels se a média dos reels da entrevista ficar em 0,8x ou mais com pulo abaixo de 75%; 3 reels (sábado e 2 de objeção ou remake) se ficar abaixo de 0,5x ou com pulo médio acima de 75%. Carrosséis e stories seguem, porque não dependem do Bruno.

**Dia 02/11 sem o vídeo curto:** estático 7, estático com o horário e mc02 ou mc03, todos pelo PostZen; link da grade como sticker à mão, se houver.

**O que se perde sem gravar:**
- A linha de nicho: a conferência de 11/11 fica "não testado (n = 0)", nunca PARAR.
- O Bruno de frente para a câmera fica restrito aos 3 remakes de 03 a 05/10, em 720p.
- REACT 01 a 03 e PB versão A não existem; a regra 5 do portão perde a saída.
- O CTA "comenta a sua profissão" não ganha post novo.

**Se o Bruno também não postar à mão:** stories só AGENDADO, sem enquete, link e compartilhamento; cai a medição por objeção; a marcação da Mirna não acontece (o PostZen só convida colaborador com o @); remakes só saem se a conta for elegível a Trial Reel pela API.

---

## 11. Riscos de capacidade

1. **Arquivo só na pasta temporária:** mc02 a mc04, as bases de ob01 a ob03, as folhas de quadros e a fonte da entrevista (958 MB) [FATO, `ls` e `du`]. As 20 peças agendadas têm cópia no PostZen; tl02 a tl05, pf01 e Dentista B com tamanho idêntico ao render [FATO, HEAD]. Cópia no Drive: sem dado (Drive fora da lista desta rodada).
2. **Fonte e release público:** a pendência de segurança manda apagar o rascunho de release do GitHub, onde fica o original [FATO, pecas-e-calendario]. Sem a pasta temporária e sem o release, um corte novo pede baixar o .mov do Drive e refazer o passe de vídeo, cerca de 3 h 15 min [FATO, custo no catálogo].
3. **Disco:** 11 GB livres [FATO, `df`]; a pasta temporária desta sessão ocupa 12 GB [FATO, `du`].
4. **Promessa do tl01:** o "mais votado inteiro" depois de 02/11 é compromisso público a partir de dom 25/10, 18h30 [FATO, legenda].
5. **Trial Reel:** elegibilidade da conta sem dado; a falha só aparece na hora de publicar [FATO, descrição do `createPost`].
6. **Autorizações paradas:** print da Mirna (verbal), @ dela, Tzur [FATO, contexto.md e enquadramento].
7. **Leituras regulatórias** antes de gravar ou publicar nicho: OAB, CFN 856, ABAC, CFP, CFO 196/2019. Status: sem dado.
8. **Feriado na exibição:** 02/11 é Finados; disponibilidade do Bruno no dia: sem dado. O vídeo curto gravado no bloco 1 tira essa dependência.
9. **Resolução da gravação:** a última chegou em 576x1024 [FATO].
10. **Stories depois de 31/10:** sem plano; 41 estáticos da S1 ainda sem render [FATO].

---

## 12. Respostas às perguntas do enquadramento que tocam esta frente

- **P12, Bruno nos 3 primeiros segundos:** Dentista C sim (selfie no quadro 0); tl02 a tl05 sim pela ficha (CB no quadro 0); ob01 a ob03 sim, de perfil atrás do monitor, com um braço na borda esquerda [FATO, quadros 0 e 2,5 s das bases]; remakes sim (selfie com fala própria); case Tzur sim; pf01 em Z2, de costas.
- **P13, mínimo de gravação:** 1 bloco por semana, entregue até quarta 23h59 (sexta no bloco 3). Bloco 1 até qua 28/10: consórcio, nutricionista e o vídeo de 02/11, de 31 a 49 min [ESTIMATIVA]. Blocos 2 a 4: 2 roteiros, de 24 a 42 min. Semana sem gravação: seção 10.
- **P14, Dentista C e remakes:** C pronto, mas guardado para anúncio depois de 18/11 pelo brief; no feed seria a terceira edição da mesma fala. Remakes: 3 saem sem gravação, como Trial Reel, pelo PostZen se a conta for elegível; nenhum renderizado; "Você gravou o curso inteiro" pede gravação; o de 01/01/2025 não entra.
- **P16, ob01 a ob03:** base composta às 14h36 e 14h37, render final sem dado, revisão de áudio aberta; sem o Bruno. Substituto se não ficarem prontos: o "mais votado inteiro" e os remakes como Trial Reel.
- **P21, o que depende só do Bruno:** gravação (bloco 1 até qua 28/10), marcação da Mirna (9 reels e 1 story; a primeira no tl01, dom 25/10, 18h30), stickers (27 na S1), o @ e o print da Mirna, o horário da exibição se a grade não sair, autorização da Tzur, envio do arquivo original, cópia do estoque para o Drive.

---

## 13. Lacunas

- Minutos reais de gravação por roteiro: o único registro são os 55 min entre o commit do teleprompter e a chegada da fala do dentista, que não medem a gravação.
- Se existe sessão marcada (seg 26/10 ou outra) e quantos minutos por semana o Bruno tem.
- Horário da exibição de 02/11 (grade publicada só até 25/10).
- Elegibilidade da conta a Trial Reel pela API.
- Se o app deixa marcar a Mirna num reel já publicado; @ dela.
- Render final de ob01 a ob03 e o resultado da revisão de áudio.
- Cópia no Drive dos renders e da fonte; original em alta dos 3 remakes.
- Status das leituras da OAB, CFN 856, ABAC, CFP e CFO 196/2019.
- Autorização da Tzur Capital; print da Mirna.
- Minutos do Bruno por story à mão, por marcação e por resposta.
- Tempo de agência por remake e por reel de nicho com o motor pronto.
- Resultado dos portões do tl01 (ter 27/10, 18h30) e do tl02 (seg 02/11, 18h30), que decidem quantos timelapses ficam.
- Qual assunto o tl01 vai eleger, que define o tamanho do "mais votado inteiro".
