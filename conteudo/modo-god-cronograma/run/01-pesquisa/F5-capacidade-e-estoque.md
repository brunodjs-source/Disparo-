# F5 · Capacidade e estoque · @o_estrategista.com.br

Frente F5 da pesquisa do conselho Agência Reunida. Rodada de sábado, 24/10/2026, escrita às 14h10 (São Paulo). Só leitura: nada foi publicado, agendado ou alterado no Instagram, no Buzzfy ou no PostZen. Toda mudança abaixo é proposta para o Bruno executar.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, nível 4, que nunca fecha objeção sozinho. Métrica que falta: "sem dado".

**Horários:** commits do git e datas de arquivo estão em UTC; aqui aparecem no horário de São Paulo (UTC menos 3 h).

**Régua usada nesta frente:** a do Buzzfy, 57 views de normal e pulo normal de 70,9% [FATO, `ig_reel_checkup` desta rodada]. Esta frente não decide mediana; só conta peças, minutos e travas.

---

## 0. Respostas curtas

1. **Pronto, renderizado e fora da agenda, com o Bruno em cena nos 3 primeiros segundos: 7 reels.** tl02, tl03, tl04, tl05, Dentista C, case Tzur v2 e pf01 como reel. Nenhum sai sem trava: os 4 timelapses dependem do portão (e da regra "uma vez só" do catálogo); o C, do brief do dentista; o Tzur, da autorização do cliente; o pf01, de DOBRAR.
2. **Com ficha e sem render, sem gravação:** ob01, ob02 e ob03 (trechos da TV) e 41 estáticos do plano de stories de 25 a 31/10. É trabalho só da agência.
3. **Sem gravação nova, com edição:** 3 remakes feitos do arquivo do próprio Instagram ("Ele nunca fez um anúncio" 10,14x, "90% dos lançamentos que flopam" 4,42x, "Problema de equipe" 3,61x). Os três são o Bruno falando para a câmera; os 3 arquivos responderam HTTP 200, em 720p. Mais 6 a 9 cortes novos da entrevista.
4. **Só com gravação do Bruno:** 19 roteiros de nicho, a selfie do REACT (20 min), a regravação do "Você gravou o curso inteiro" (o original não tem pessoa) e 21 reels do Módulo 3. Fila somada: 41 gravações e 1 selfie.
5. **O que falta não é vaga, é formato.** De 01 a 21/11 o feed fecha sem gravar (estoque e cortes da TV somam de 12 a 18 reels para 15 vagas) [ESTIMATIVA, seção 8]. O que não se fecha sem gravar é o Bruno falando para a câmera, o formato que mediu melhor (4 dos 6 reels da conta com 3x ou mais são o Bruno falando para a câmera: Ele nunca fez um anúncio, Dentista A, 90% e Problema de equipe; dos outros 2, um é slideshow sem pessoa e o outro é pessoal) [FATO, `ig_reel_checkup`], e a linha de nicho do D1 de 21/10. Fora os 3 remakes, os dois só existem com gravação nova.
6. **Agenda mínima:** 1 bloco por semana, entregue até quarta 23h59, de 24 a 36 min [ESTIMATIVA], com 2 roteiros de nicho no teleprompter e 2 tomadas do gancho de cada. O primeiro bloco (até qua 28/10) pede 3 roteiros (2 para a semana e 1 de reserva) e a selfie do REACT: de 56 a 74 min [ESTIMATIVA].
7. **Se não gravar:** a troca é decidida no portão de segunda; o estoque sai numa ordem fixa (seção 10); 5 reels por semana se a série da TV passar no portão, 3 se não passar; nunca animação com voz sintética; a conferência de nicho de 11/11 fica "sem dado (n = 0)", sem PARAR.
8. **A gravação mínima é a menor parte da carga do Bruno.** Stories com sticker postados à mão (27 na semana de 25 a 31/10) e respostas à mão (15 a 30 min por dia, estimativa de 21/10) somam mais que os 24 a 36 min de gravação [ESTIMATIVA com um PRIOR dentro, seção 6].
9. **Risco de estoque:** tl02 a tl05, mc02 a mc04 e a fonte da entrevista existem só no scratchpad desta sessão, que é temporário. Cópia no Drive: sem dado.

---

## 1. Fontes conferidas nesta rodada

| Consulta ou arquivo (só leitura) | Hora (SP) | Resultado |
|---|---|---|
| PostZen `listPosts`, conta j97772ycndetk3f1wcdbh14p898g4b8w, 24/10 a 23/11 | perto de 13h50 | OK. 16 publicações "scheduled": 6 reels, 1 carrossel, 9 stories. Nada depois de sex 30/10 |
| Buzzfy `ig_posts` reels (24 itens, sem trial reels) e feed desde 01/09 (16 itens) | perto de 13h50 | OK. Último reel: Dentista A, 21/10 21h. Último post de feed: 20/10 21h30 |
| Buzzfy `ig_posts` por id com `include_media_urls`, os 3 candidatos a remake | perto de 13h55 | OK. `video_url_withheld: false` nos 3, com `media_url` |
| Pedido HEAD nos 3 `media_url` (cdninstagram.com) | perto de 13h56 | HTTP 200, `video/mp4` nos 3. A etiqueta de codificação decodificada diz `C3.720` (720p) e duração de 74 s, 69 s e 74 s |
| GET das 6 imagens de story agendadas para hoje (media.postzen.dev) | perto de 13h57 | HTTP 200. md5 iguais aos de `story-frase-1, 2, 6, 7, 9 e 10.png` |
| Buzzfy `buzzfy_playbook` (second_life, hot_streaks) | perto de 13h58 | OK |
| Buzzfy `ig_reel_checkup`, 5 ids (3 remakes, Dentista A, "Você gravou o curso inteiro") | perto de 14h05 | OK. Normal 57 views, pulo 70,9%. Tags de formato dos 3 remakes |
| `ffprobe` em 60 vídeos do repositório e 21 do scratchpad; quadros 0, 1 a 1,5 e 2,5 a 2,9 s de Dentista C, Tzur v1 e v2, anúncio a01, tl02 a tl05 e pf01 | 13h40 a 14h05 | OK |
| Logs de render `scratchpad/tv/fila*.log`, `git log`, `du`, `df` | 13h40 a 14h05 | OK |
| Arquivos: contexto.md, 00-enquadramento.md, F2-playbook-buzzfy.md, pecas-e-calendario.md, catalogo-formatos.md (seções 1, 4, 5, F1, F5 e 8), roteiros-20-videos.md, teleprompter-5-nichos.md, modo-god-nichos/run/10-decision-brief.md e 06-plano-final.md, 00-SISTEMA.md (Módulo 3), stories-objecoes/03-plano-7-dias.md e .json (versão gravada às 13h58), videos/cases/tzur/edit.json, videos/nichos/dentista/engine, videos/tv-camara/engine/ENGINE.md | 13h30 a 14h05 | OK |

Erros de consulta: nenhum. Google Drive não foi consultado: não está na lista de ferramentas desta rodada.

Aviso: o `03-plano-7-dias` estava sendo reescrito durante a rodada (a versão lida no começo tinha 42 stories; a gravada às 13h58 tem 56). As contagens abaixo são da versão das 13h58.

---

## 2. O que existe pronto

### 2.1 Já agendado no PostZen (ponto de partida, não é estoque livre)

[FATO, `listPosts`] 16 publicações: 6 reels (Dentista B sáb 24/10 21h; tl01 dom 25/10 18h30; pb01 seg 26/10 21h; ci01 qua 28/10 21h; po01 qui 29/10 21h; pb02 sex 30/10 21h), 1 carrossel (car01, ter 27/10 12h) e 9 stories (8 hoje, de 14h00 a 20h30, e o pf01 ter 27/10 16h). Os arquivos dessas 16 estão hospedados no PostZen.

### 2.2 Reels renderizados e fora da agenda

| Peça | Duração | Bruno nos 3 primeiros segundos | Onde está o arquivo | Trava | O que falta |
|---|---|---|---|---|---|
| tl02 | 35,3 s | Sim: Bruno no plano CB em 0 e 1,5 s; Z2 em 2,9 s [FATO, quadros extraídos] | Só em `scratchpad/tv/render/` | Portão: tl01 com 0,8x ou mais e pulo abaixo de 75% em 48 h (ter 27/10, 18h30); regra do catálogo "uma vez só" para timelapse; promessa da legenda do tl01 | Cópia fora do scratchpad; o Bruno agenda. Legenda pronta |
| tl03 | 36,0 s | Sim: CB em 0 e 1,5 s; em 2,9 s o cronômetro sobre o plano aberto [FATO, quadros] | Só no scratchpad | Portão do tl02 | Idem |
| tl04 | 34,4 s | Sim: CB em 0 e 1,5 s; Z2 em 2,9 s [FATO, quadros] | Só no scratchpad | Portão do tl03 | Idem |
| tl05 | 35,3 s | Sim: CB em 0 e 1,5 s; Z2 em 2,9 s [FATO, quadros] | Só no scratchpad | Portão do tl04 | Idem |
| Dentista C (9x16, 4x5 e leve) | 36,4 s | Sim: selfie com "Dentistas," no quadro 0 [FATO, quadros] | `videos/nichos/dentista/render/` | Brief do dentista de 21/10: o C fica como amostra e anúncio 4:5 depois de 18/11, com a Res. CFO 196/2019 conferida [FATO, enquadramento item 7]. É a terceira edição da mesma fala do A (no ar desde 21/10) e do B (hoje 21h). CTA falado "comenta a sua profissão" | Decisão do Bruno; render nenhum |
| Case Tzur v2 (v1 de 29,8 s também pronto) | 54,3 s | Sim: o primeiro corte é do Bruno (`edit.json`: `"src": "bruno"` com `start: 0`; legenda "Nós conseguimos" em 1 s, palavra do corte dele) [FATO]. Depois entra o depoimento do responsável de marketing do cliente | `videos/cases/tzur/` | Autorização da Tzur Capital em vídeo: bloqueante desde 23/10, status sem dado [FATO, 06-plano-final, seção 7, item 5]. A fala final pede "comenta estrategista" [FATO, `edit.json`], que liga a automação ESTRATEGISTA, contra a regra de uma palavra por mês. Estava previsto para qua 22/10 e não saiu [FATO, 00-SISTEMA e `ig_posts`] | Autorização; re-editar o fim para trocar o CTA |
| pf01 como reel | 24,0 s | Sim, mas em Z2: o Bruno de costas para a câmera e a Mirna de frente [FATO, quadros] | Scratchpad e PostZen (como story de ter 27/10) | Reel só com DOBRAR de profissão nomeada [FATO, pecas-e-calendario] | Nada |

Fora desta tabela: Dentista A (publicado em 21/10) e Dentista B (agendado hoje).

### 2.3 Stories prontos

- **Vídeos da entrevista fora da agenda:** mc02 (4,5 s), mc03 (11,0 s) e mc04 (9,5 s), só no scratchpad [FATO, ffprobe]. O mc04 precisa de render novo sem "como estrategista digital" [FATO, 03-plano-7-dias, "Conferir antes de publicar"]. Os reposts das 9h usam o arquivo do próprio reel do dia anterior.
- **Estáticos de frase (`estaticos/stories-frases`):** 10 PNG. Seis vão ao ar hoje: 1, 2, 6, 7, 9 e 10 [FATO, md5 iguais aos do PostZen]. Livres: o 3 ("Lançamento é xadrez. A maioria joga dama.") e o 4 ("O lead que não comprou vale mais do que o que comprou."). O 5 repete a frase do 9 ("Nem tudo que vemos é ouro"), que sai hoje às 19h30. O 8 tem o rótulo "NA TV · EM BREVE", vencido depois que a série estreia, e a frase é a capa do car01 de terça.
- **Plano de 25 a 31/10 (03-plano-7-dias, versão das 13h58):** 56 stories. 15 usam vídeo que já existe; 41 são estáticos com ficha e sem render. 27 estão marcados MANUAL (têm sticker e o Bruno posta pelo app, na hora) e 29 AGENDADO [FATO, contagem no .json].
- **Destaque "Comece aqui":** capa pronta (`estaticos/destaque-comece-aqui`). Stories animados da Escala (3): já usados [FATO, contexto.md]. `stories-hoje` (3, de 13/10): uso anterior sem dado.

### 2.4 Carrosséis

- car01 (6 lâminas 1080x1350): agendado para ter 27/10 12h. **É o único carrossel pronto.**
- `estaticos/checklist` (8 slides): são as mesmas 10 perguntas do carrossel publicado em 12/10 [FATO, `q.json` e legenda do post em `ig_posts`]. Já usado.

### 2.5 Fotos e material de base

- 7 fotos de marca: f1 a f5, e1 e e2 [FATO, `estaticos/stories-frases`]. As 3 fotos de `stories-hoje` e o `rosto-torre.jpg` têm o mesmo tamanho em bytes de f3, f4 e f1 (cópias).
- Fonte da entrevista para cortes novos: `scratchpad/entrevista/src/` (entrevista-1080p.mp4, entrevista-zoom.mp4, entrevista-audio.m4a; a pasta soma 958 MB) [FATO, `du`]. O original fica no rascunho de release do GitHub e no Drive [FATO, ENGINE.md e pecas-e-calendario].
- Motores prontos: entrevista (`videos/tv-camara/engine`, 9 modelos) e dentista (`videos/nichos/dentista/engine`, modelos A, B e C).

### 2.6 Estoque que não entra no feed orgânico

| Peça | Por que não entra |
|---|---|
| v01 a v08 (8 reels de 36 a 38 s) e série 2 r1 a r5 (5 reels e 5 estáticos 4x5) | Animação com voz sintética, já publicados de 11 a 20/10. O CLAUDE.md exige o Bruno nos 3 primeiros segundos de todo reel |
| Stories s01 a s08 | Chamadas dos reels v01 a v08, com voz sintética (`tts.py`; commit de 11/10 cita "voz feminina"): anunciam reels que já saíram |
| Anúncio a01-campinas (38,2 s, 9x16 e 4x5) e 4 estáticos 4x5 por nicho | Animação sem o Bruno nos quadros 0, 1 e 2,5 s [FATO, quadros]; peça de anúncio, e a verba é zero até 18/11 (D4 de 21/10) |
| Reel de 01/01/2025 (9,14x) | Resumo pessoal de fé, fora da grade (`on_profile_grid: false`) e fora do posicionamento [FATO, F1 e `ig_posts`] |
| 9 PDFs de `materiais/pdfs` e a apresentação BNI | Material das automações e de reunião, não post |

---

## 3. Com ficha e sem render (agência, sem gravação)

| Peça | Duração pela ficha | Bruno no quadro 0 | O que falta antes do render | Data sugerida no plano |
|---|---|---|---|---|
| ob01 (O2 "Não tenho tempo pra lançar") | 13,5 s, ou 12,1 s se o fim da frase for ilegível | Sim, plano CB falando desde o quadro 0 (ficha) | Ouvir 1316,2 a 1326,4 s e confirmar que a boca é do Bruno (a diarização marca M em parte do trecho) | qua 04/11, 21h |
| ob02 (O1 "Nunca ouvi falar de você") | 25,8 s | Sim, CB em 1199,5 s (ficha) | Ouvir "case" em 1232,3 s (confiança 0,33) | seg 02/11, 21h |
| ob03 (O8 "Meu consultório vive de indicação") | 9,0 s | Sim, CB em 1635,4 s (ficha) | Conferir os 2 cortes (1636,1 s e 1648,2 s) | sex 06/11, 21h |
| mc04 (story) | cerca de 5 s | Não se aplica (story) | Novo fim entre 1705,2 e 1705,7 s | sáb 31/10, 11h |
| 41 estáticos do plano de 7 dias | 1 quadro | Não se aplica | Render no `s.html` | 25 a 31/10 |

[FATO, 03-plano-7-dias.md e .json, versão das 13h58]. A voz da Mirna saiu dos 3 reels de objeção nesta versão; a pergunta dela entra só como texto.

---

## 4. Sem gravação nova, com edição

### 4.1 Cortes novos da entrevista (agência; fonte no scratchpad)

A produzir pelo catálogo e pelo pecas-e-calendario: os assuntos 1 ("Desde criancinha") e 6 ("Zero reais") do índice do tl01, que não têm peça; pb03; CINEMA 02; MITO; PROFISSAO como reel; SALA; PERGUNTA 01 e 02; CARROSSEL 02 a 04 [FATO, pecas-e-calendario "O que falta produzir" e enquadramento D3]. São de 6 a 9 reels e 3 carrosséis, sem minuto do Bruno.

### 4.2 Remakes do arquivo do próprio Instagram

| Reel | Normal | Pulo | Duração | Formato pelas tags do Buzzfy | Legenda queimada | Primeiro corte |
|---|---|---|---|---|---|---|
| "Ele nunca fez um anúncio" (sáb 03/10, 23h06) | 10,14x | 53,2% | 74,6 s | Selfie, fala própria para a câmera | Não | 9,3 s |
| "90% dos lançamentos que flopam" (dom 04/10, 11h11) | 4,42x | 45,7% | 69,5 s | Selfie, fala própria | Sim | sem corte medido |
| "Problema de equipe" (seg 05/10, 21h58) | 3,61x | 49,6% | 74,7 s | Selfie, fala própria | Sim | sem corte medido |

[FATO, `ig_reel_checkup` e `ig_posts` desta rodada; HEAD HTTP 200 nos 3 arquivos].

- **Regra do playbook:** mudar pelo menos duas coisas reais (abertura nova, legenda se houver fala, corte de 20% a 40%, resposta a um comentário) e postar como Trial Reel, que vai primeiro para quem não segue; se passar do alcance usual, compartilhar no feed [FATO, `buzzfy_playbook` second_life]. Para o "Ele nunca fez um anúncio" a legenda queimada é a mudança disponível; a legenda do post promete "uma saga de 7 dias" que já acabou em 09/10 e precisa sair.
- **Limite do arquivo:** é a cópia do Instagram, em 720p [FATO, etiqueta `C3.720`]. O render sai em 1080x1920 a partir de 720 de largura; perda visível: [HIPÓTESE] a conferir na folha de quadros. O original do celular existe: sem dado.
- **Quem posta:** o Bruno, no app, como Trial Reel [FATO, F2]. Se o PostZen agenda Trial Reel: sem dado.
- **Fora dos remakes sem gravação:** "Você gravou o curso inteiro" (11/10, 3,75x, pulo 86,9%) é slideshow com narração e sem pessoa [FATO, tags `framing: no_person`, `audio: voiceover`]. Refazer com o Bruno em cena é gravação nova.

---

## 5. O que depende de gravação do Bruno

| Item | Quantidade | Minutos do Bruno | Trava antes de gravar ou de publicar | O que destrava |
|---|---|---|---|---|
| Roteiros de nicho (`roteiros-20-videos.md`, 5 nichos, 4 semanas) | 19 (o 2, dentista, já saiu) | 12 a 18 min por roteiro [ESTIMATIVA: 60 a 90 min para 5, linha 9 do próprio documento]. Medida real: sem dado | Advogado: provimento de publicidade da OAB não lido. Nutricionista: vigência da CFN 856 no DOU, prazo 28/10. Consórcio: BCB 285/2023 e regra da ABAC; o teleprompter manda gravar a tomada com e sem a linha dos 41,9%. Psicólogo: regras do CFP; o +151,1% segue sem fonte primária. Linha do case Tzur no teleprompter: gravar também a versão sem case enquanto a autorização não chega [FATO, 10-decision-brief, 06-plano-final e teleprompter] | Linha de nicho do D1 de 21/10 e o formato do Bruno falando para a câmera |
| Selfie do REACT | 1 sessão: 6 reacts (saem 3), 12 aberturas "Isso eu falei na TV." e a abertura do timelapse | 20 min [estimativa do catálogo, F1 e seção 8] | Mesmo enquadramento dos reels de nicho; o catálogo queria a selfie até qui 29/10 para o REACT 01 no sáb 31/10, data hoje proposta para o tl02 | REACT 01 a 03 e PB versão A |
| Regravar "Você gravou o curso inteiro" | 1 reel de cerca de 30 s | 12 a 18 min [ESTIMATIVA, mesma conta] | Nenhuma | Remake com rosto do tema que teve 169 de alcance |
| Reels do Módulo 3 com o Bruno (saga regravada, agenda cheia, médico, psicólogo, live lotada, Tzur lance a lance, convite e outros) | 21 dos 22 reels da tabela (o 1 é o case v2, pronto) [FATO, contagem no 00-SISTEMA] | 18 min cada [ESTIMATIVA, 90 min para 5 reels no 00-SISTEMA] | Sem trava escrita além das regras de texto | Linha geral do Bruno para a câmera |

**Fila somada:** 19 + 21 + 1 = 41 gravações e 1 selfie [FATO, contagem]. A 2 roteiros por semana entram 8 nas 4 semanas, cerca de 20% da fila [ESTIMATIVA].

**O que aconteceu com a capacidade planejada (fatos, amostra curta):**
- [FATO, 00-SISTEMA de 21/10] O plano previa 1 sessão de gravação de 90 min por semana (5 reels) e 2 h de edição.
- [FATO, `git log`] A última gravação nova do Bruno para a câmera no repositório é a do dentista: áudio masterizado em 21/10 às 13h26.
- [FATO, `ig_posts`] Depois do Dentista A (21/10, 21h) nada foi publicado até 14h de hoje. O reel "Fila é teto" com o Bruno, previsto para qui 23/10 nos "Próximos 7 dias", não saiu e não tem arquivo no repositório.
- [FATO, enquadramento item 9] A sessão de gravação de seg 26/10 do plano de nichos: confirmação sem dado.
- Leitura: em 3 dias depois do plano de 90 min por semana entrou 1 fala de 36 s. É pouca amostra para chamar de ritmo, mas basta para não planejar em cima de 90 min [HIPÓTESE].

---

## 6. Carga do Bruno fora da gravação

| Tarefa | Quantidade | Minutos | Fonte |
|---|---|---|---|
| Stories com sticker postados à mão (enquete, link, compartilhar post) | 27 de 25 a 31/10 | Sem dado. [PRIOR] 1 a 2 min cada: 27 a 54 min na semana | 03-plano-7-dias.json |
| Respostas à mão ("comenta a sua profissão que eu te respondo") | Todo dia com reel de nicho no ar | 15 a 30 min por dia [ESTIMATIVA do D3 de 21/10]: 105 a 210 min na semana | 10-decision-brief |
| Postar os remakes como Trial Reel no app | 3 | Sem dado | F2 |
| Agendar no PostZen (agente não agenda) | De 01 a 21/11: cerca de 15 reels, 6 carrosséis e os stories AGENDADO | Sem dado | enquadramento |
| Uma vez: print da Mirna, data de exibição, autorização da Tzur, decisão escrita da palavra-chave, ouvir 922,1 a 924,2 s, 1584,3 a 1592,0 s e 1423,0 s, confirmar a parte variável do contrato (story de sex 30/10) | 8 itens | Sem dado | enquadramento, 02-provas, 03-plano |

[ESTIMATIVA, com um PRIOR dentro] Somando só o que tem número (gravação mínima, stories manuais pelo PRIOR e respostas): de 156 min (24 + 27 + 105) a 300 min (36 + 54 + 210) por semana. A gravação fica entre 12% e 15% dessa carga. Se faltar tempo ao Bruno, cortar stories manuais (passar para AGENDADO, sem sticker) libera mais minutos do que cortar a gravação, com a perda da medição por objeção.

---

## 7. Esforço de produção da agência

- **Render medido** [FATO, `scratchpad/tv/fila*.log`]: pb01, 587 quadros em 60,7 s; pb02, 799 em 90,8 s; mc01, 344 em 36,8 s; tl03, 1.080 em 85,6 s. São de 0,08 a 0,11 s por quadro; o catálogo supunha 0,3 s por quadro por camada. [ESTIMATIVA] Um reel de 35 s captura em cerca de 1,5 min (1.050 x 0,09 s).
- **Tempo de calendário observado** [FATO, `git log`, horário de SP]: 24/10, motor da entrevista 06h49, fichas e legendas de 10 cortes 07h26, car01 08h02, tl02 08h48 (mixagem 09h05), tl03 a tl05 em revisão 10h55, corrigidos 11h12, renderizados 11h42. 21/10, dentista: áudio 13h26, motor 18h07, os 3 modelos 18h59, com o motor feito do zero e um conselho do modo GOD rodando no mesmo período.
- **Por peça, com motor pronto** [ESTIMATIVA, tempo de calendário e não de trabalho]: corte da TV com ficha, cerca de 6 min (10 peças em 64 min, do motor às 06h49 ao render do pf01 às 07h53); timelapse, cerca de 50 min (3 em 2h37); carrossel, cerca de 36 min; reel de nicho Modelo A, até 1h50 (5h33 dividido por 3; é teto, porque inclui o motor).
- **Reel de nicho novo não é só render:** o `dent.html` tem letreiros, painel e rodapé escritos para o dentista; cada fala nova pede `words.json` (Whisper), `headtop.json` (altura da cabeça por quadro) e lista de letreiros nova [FATO, `engine/cap.js` e `dent.html`]. Mais a folha de 4 quadros por segundo com nota por efeito (CLAUDE.md).
- **Remake do arquivo do Instagram:** sem medida. [PRIOR] 1 a 2 h cada.
- **Conclusão:** o gargalo da grade é o minuto do Bruno, não a agência.

---

## 8. Oferta contra demanda, 25/10 a 22/11

Demanda pelo CLAUDE.md: 5 reels e 2 carrosséis por semana, mais stories diários.

| Semana | Agendado | Pronto ou com ficha, sem gravação | Só com gravação | Buraco |
|---|---|---|---|---|
| S1, 25 a 31/10 | 5 reels da TV e car01 | tl02 (proposto para sáb 31/10, seria o 6º reel); 41 estáticos e 15 vídeos de story | REACT 01 (se a selfie sair até qui 29/10) | 1 carrossel (só o car01 existe) |
| S2, 01 a 07/11 | Nada | ob01 a ob03; tl03 com portão; remakes como Trial Reel; cortes novos da TV | 2 roteiros do bloco 1 | Stories de 01/11 em diante sem plano; 2 carrosséis |
| S3, 08 a 14/11 | Nada | tl04 com portão; cortes novos da TV | 2 roteiros do bloco 2 | Stories e 2 carrosséis |
| S4, 15 a 21/11 | Nada | tl05 com portão; cortes novos da TV | 2 roteiros do bloco 3 | Stories e 2 carrosséis |

**Reels de S2 a S4 (15 vagas)** [ESTIMATIVA]: sem gravação e sem trava externa somam de 12 a 18 (ob01 a ob03: 3; tl03 a tl05: 0 a 3, pelo portão; cortes novos: 6 a 9; remakes: 3, que só ocupam vaga de feed se baterem o alcance usual). Com trava: Dentista C, case Tzur e pf01 (3). Com a gravação mínima: 6 (2 por semana).

**Carrosséis (7 a produzir: 1 da S1 e 6 de S2 a S4)** [ESTIMATIVA]: sem material do Bruno há 8 fontes (CARROSSEL 02 a 04 da TV, e do Módulo 3: Os 5 Lances, Seguidor x comprador em versão nova, Carrinho, Oferta em 5 pilares, Resumo do mês). Com material do Bruno: Recusas, Bastidor do dia do lançamento, Print do carrinho. Nenhum desses 11 tem arquivo hoje: `estaticos/` e `videos/tv-camara/carrossel/` só guardam o checklist (já usado) e o car01 [FATO, lista de pastas e busca por "5 lances"].

**Stories:** o plano cobre só 25 a 31/10. Para S2 a S4 há 5 objeções sem dia (O7, O9, O10, O11, O12) e o banco de provas do 02-provas.md [FATO, 03-plano]. Trabalho só da agência, menos os stickers.

---

## 9. Agenda mínima de gravação semanal (proposta)

**Regras do bloco**
- Um bloco por semana, em qualquer dia de seg a qua, com o arquivo entregue até quarta 23h59. A agência edita qui e sex; o portão de segunda aprova; o Bruno agenda.
- Mesmo enquadramento do Dentista A (selfie, luz de frente, celular na altura dos olhos): o letreiro atrás da cabeça usa o `headtop.json` da selfie e o REACT pede o mesmo enquadramento [FATO, catálogo F1].
- Cada roteiro com 2 tomadas do gancho: o gatilho intermediário do D1 de 21/10 já prevê trocar o hook se o primeiro nicho ficar abaixo de 53 [FATO, 10-decision-brief]. Onde houver linha travada (ABAC, case Tzur), gravar as 2 versões.
- Tempo por roteiro: 12 a 18 min [ESTIMATIVA, roteiros-20-videos.md]. Medir o primeiro bloco com cronômetro e corrigir esta tabela no Módulo 7.
- Reserva: o playbook manda ter 1 ou 2 reels prontos e esperando para o dia em que um estoura [FATO, `buzzfy_playbook` hot_streaks]. Só o bloco 1 grava a reserva; depois, 2 por semana mantêm 1 na fila.

| Bloco | Gravar até | Publica em | Mínimo | Acréscimo recomendado | Minutos [ESTIMATIVA] | Por quê |
|---|---|---|---|---|---|---|
| 1 | qua 28/10 | S2, 01 a 07/11 | Roteiro 17, Dentista "Curso que ninguém comprou"; roteiro 1, Consórcio "Cota no direct" (na versão do teleprompter, tomadas com e sem a linha da ABAC) | Roteiro 12, Dentista "Guerra de preço" (reserva); selfie do REACT (20 min) | Mínimo 24 a 36; com acréscimo 56 a 74 | O 17 repete o formato do Dentista A e muda só o assunto, como manda o playbook, dentro das 2 semanas depois do A (até cerca de 04/11). O 1 é o primeiro dos 3 nichos fixos do D1 de 21/10, que precisam estar no ar até seg 09/11 para a conferência de qua 11/11 |
| 2 | qua 04/11 | S3, 08 a 14/11 (nutricionista até seg 09/11, 21h) | Roteiro 3, Nutricionista (versão do teleprompter escolhida pela leitura da CFN 856, prazo 28/10); roteiro 9, Psicólogo "Teto de horas" (o +151,1% não entra; se for a versão do teleprompter, a linha do case vai nas 2 versões) | Roteiro 6, Consórcio "Banco" | 24 a 36 (36 a 54 com o acréscimo) | Fecha os 3 fixos antes de 11/11; psicólogo é o extra fixo do D2 de 21/10 |
| 3 | qua 11/11 | S4, 15 a 21/11 | Pela conferência de 11/11. Nicho com mediana de 53 ou mais e pulo mediano até 75%: os 2 nichos de maior número recebem o roteiro da semana 3 (11, 12 ou 13). Abaixo: 2 reels do Bruno para a câmera fora de nicho (regravar "Você gravou o curso inteiro" e "Fila é teto", Módulo 3), mudando o assunto e mantendo o formato | Advogado (roteiro 5) só com o provimento da OAB lido | 24 a 36 | A regra pede n de 2 por formato antes de PARAR (red team de 21/10) |
| 4 | qua 18/11 | S5, de 22/11 em diante | Pelo Módulo 7 de 16/11 | Selfie do REACT, se ainda não existir | 24 a 36 | |

**Se o Bruno só tiver 15 min numa semana:** gravar 1 roteiro (o próximo da sequência do dentista). Mantém 1 reel por semana do Bruno para a câmera; a linha de nicho do D1 fica com n menor que 3 em 11/11.

---

## 10. Plano se ele não gravar

**Gatilho:** nenhum arquivo até quarta 23h59. No portão de segunda, as 2 vagas de nicho da semana seguinte passam para o estoque, nesta ordem:

1. **ob01 a ob03** (trecho da TV, o Bruno falando desde o quadro 0; render da agência). Já ocupam 3 vagas na S2 pelo plano.
2. **Remakes como Trial Reel**, a 6 h ou mais de qualquer reel do feed (o playbook mede 0,92x para reel com menos de 6 h do anterior): "Ele nunca fez um anúncio" primeiro (10,14x; a mudança que falta é a legenda queimada), depois "90%" e "Problema de equipe". Pede o Bruno no app só para postar.
3. **tl03 a tl05**, um por sábado, só com o portão do anterior.
4. **Cortes novos da TV:** o assunto mais votado no tl01 (o 1 e o 6 pedem corte novo), pb03, CINEMA 02, MITO. PROFISSAO como reel só com DOBRAR.
5. **Case Tzur v2**, só com a autorização escrita da Tzur e o fim re-editado sem "comenta estrategista".
6. **Dentista C** fica fora até o brief do dentista ser revisto (o brief o guarda para anúncio 4:5 depois de 18/11).

Nunca: animação com voz sintética (v01 a v08, série 2, s01 a s08, anúncio a01) nem reel sem o Bruno nos 3 primeiros segundos [FATO, CLAUDE.md].

**Grade da semana sem gravação** (regra do catálogo, seção 8): 5 reels se a média dos reels da TV ficar em 0,8x ou mais com pulo abaixo de 75%; 3 reels (sábado com rosto e 2 de objeção ou remake) se ficar abaixo de 0,5x ou com pulo médio acima de 75%. Carrosséis e stories seguem, porque não dependem do Bruno.

**O que se perde sem gravar:**
- A linha de nicho: a conferência de 11/11 fica sem dado (n = 0). Registrar como "não testado", nunca como PARAR.
- O Bruno falando para a câmera fica restrito aos 3 remakes de 03 a 05/10. Sequência de estouro (3 a 5 na mesma linha) não tem peça.
- REACT 01 a 03 e PB versão A não existem.
- O CTA "comenta a sua profissão" não ganha post novo de nicho.

**Se o Bruno também não postar à mão:** os stories vão só AGENDADO, sem enquete, link e compartilhamento; caem os reposts das 9h e a medição por objeção; os remakes não saem (Trial Reel pelo PostZen: sem dado). Fica no ar o que o PostZen agenda: reels, carrosséis e stories sem sticker.

---

## 11. Riscos de capacidade

1. **Arquivo só no scratchpad.** tl02 a tl05, mc02 a mc04, as fichas renderizadas e a fonte da entrevista (958 MB) estão em `/tmp/claude-0/.../scratchpad/`, temporário [FATO, `find` e `du`]. O que já foi agendado tem cópia no PostZen. O próprio plano manda copiar para o Drive antes de agendar; cópia feita: sem dado.
2. **Fonte da entrevista e o release público.** A pendência de segurança manda apagar o rascunho de release do GitHub, onde fica o original [FATO, pecas-e-calendario e ENGINE.md]. Sem o scratchpad e sem o release, um corte novo pede baixar o .mov do Drive e refazer o passe de vídeo, cerca de 3 h 15 min [FATO, custo no catálogo].
3. **Disco:** 12 GB livres de 252 GB [FATO, `df`].
4. **Remake em 720p** [FATO, etiqueta do arquivo]; qualidade final: [HIPÓTESE].
5. **Autorizações paradas:** print da Mirna (verbal às 13h20) e Tzur (sem dado). A Mirna aparece no plano Z2 de quase todas as peças da TV [FATO, pecas-e-calendario].
6. **Leituras regulatórias** antes de gravar ou publicar nicho: OAB, CFN 856, BCB e ABAC, CFP, CFO 196/2019. Status: sem dado.
7. **Promessa do tl01** ("o mais votado sai no próximo sábado"): se o mais votado for o assunto 1 ou 6, a peça não existe e pede corte novo até sex 30/10 [FATO, enquadramento item 2].
8. **Plano de stories em edição durante a rodada:** a contagem de 56 pode mudar.

---

## 12. Respostas às perguntas do enquadramento que tocam esta frente

- **P6, Bruno nos 3 primeiros segundos:** Dentista C sim (selfie no quadro 0); tl02 a tl05 sim (CB no quadro 0); ob01 a ob03 sim pela ficha (CB no quadro 0), conferir no render; remakes sim (selfie com fala própria); case Tzur sim (primeiro corte do Bruno); pf01 em Z2, com o Bruno de costas para a câmera.
- **P11, mínimo de gravação:** 2 roteiros por semana, de 24 a 36 min [ESTIMATIVA], entregues até quarta 23h59; primeiro bloco até qua 28/10, com 3 roteiros e a selfie do REACT (56 a 74 min). Semana sem gravação: seção 10.
- **P12, Dentista C e remakes:** o C está pronto e com o Bruno no quadro 0, mas o brief do dentista o guarda para anúncio depois de 18/11; no feed seria a terceira edição da mesma fala em 3 dias de distância. Remakes: 3 saem sem gravação (arquivo do Instagram, 720p); 1 pede gravação ("Você gravou o curso inteiro"); o de 01/01/2025 não entra. Nenhum remake está renderizado [FATO, enquadramento item 8].
- **P14, ob01 a ob03:** com ficha, sem render; produção só da agência, sem o Bruno; datas do plano 02, 04 e 06/11; substituto se não ficarem prontos: os remakes como Trial Reel e os cortes novos da TV.

---

## 13. Lacunas

- Minutos reais de gravação por roteiro: nenhum registro da sessão do dentista.
- Se a sessão de seg 26/10 existe e quantas horas por semana o Bruno tem para gravar.
- Cópia no Drive dos renders e da fonte da entrevista.
- Original em alta dos 3 remakes no celular do Bruno.
- Status das leituras da OAB, da CFN 856, do BCB e da ABAC, do CFP e da CFO 196/2019.
- Autorização da Tzur Capital; print da liberação da Mirna; data de exibição do programa.
- Se o PostZen agenda Trial Reel.
- Minutos do Bruno por story manual, por agendamento e por resposta (a faixa de 15 a 30 min por dia é estimativa de 21/10).
- Tempo de agência por remake e por reel de nicho com o motor pronto.
- Resultado do portão do tl01 (ter 27/10, 18h30), que decide quantos timelapses entram.
- Uso anterior dos 3 stories de `stories-hoje`.
