# Plano da cadeira L · Reel do dentista · Agência Reunida Modo GOD · 21/10/2026

Cliente: O Estrategista (@o_estrategista.com.br).

| Campo | Conteúdo |
|---|---|
| Cadeira | L · Automação e atendimento |
| Persona | Engenheiro de automação, chatbot e mensuração (CAPI, conversões offline) |
| OTIMIZA PARA | Resposta rápida e dado limpo voltando para a plataforma |
| PONTO CEGO (assumido) | Ver tudo como fluxo e subestimar oferta e criativo. Compensação escrita: a seção 2 (pergunta contrária) mostra com conta que o gargalo provável deste reel é volume de lead, não atendimento. Por isso metade das ideias da seção 4 é sobre gancho, rosto, CTA legível e oferta da resposta, e eu não peço nenhuma automação nova para este reel |
| PERGUNTA CONTRÁRIA | E se o problema não for atender bem, e sim não ter lead para atender? Resposta na seção 2, pergunta 0 |

Etiquetas: [FATO] com fonte ao lado · [ESTIMATIVA] com conta ou premissa · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, nível 4, nunca fecha objeção sozinho.

Leituras novas desta cadeira (somente leitura, nada alterado em conta nenhuma), registradas em `run/02-cadeiras/evidencias-L/leituras-postzen-buzzfy-2026-10-21.md`: PostZen listCommentAutomations e listCommentAutomationLogs; Buzzfy ig_automations_list (recusado, plano MAX), ig_posts, ig_post_stats e ig_best_times.

---

## 1. Veredito (12 linhas)

1. Áudio (D1): remasterizar a partir do voz_master.wav com limitador de true peak, trilha com ducking e SFX, e medir no MP4 final de cada modelo, não no WAV. O corte de 40 dB nas pausas não tem método; proponho o método antes de julgar.
2. Modelo que defendo para publicar em 29/10: A enxuto com legenda palavra a palavra (opções 2 e 3 da D2 juntas). B (tela dividida com reacts) e C (tipografia cinética com órbita atrás da cabeça) são produzidos depois de A, em série, nunca em paralelo.
3. Achado que muda o atendimento: 6 regras de automação da conta toda estão ativas no PostZen, incluindo "caso" e "case" sem tolerância e com DM sobre a Tzur. Um dentista que comentar "no meu caso..." recebe a DM errada e queima a única resposta privada daquele comentário [FATO, PostZen 21/10/2026].
4. Não existe regra TABULEIRO no PostZen hoje [FATO, mesma leitura]. A porta "acima de 150 liga TABULEIRO" do plano final precisa ser criada e testada antes de 29/10.
5. Em 16 regras ativas houve 1 disparo desde 12/10, e o autor parece ser o próprio Bruno testando [FATO o disparo; HIPÓTESE o autor].
6. Pergunta contrária: sim, o gargalo provável é lead. Comentários por alcance nos reels com o Bruno: 0,84% [ESTIMATIVA, 5/598]. Com 106 de alcance, cerca de 0,9 comentário. Atendimento perfeito sobre menos de 1 lead dá zero.
7. Por isso: nenhuma automação nova para "dentista"; resposta manual em até 60 min nas primeiras 3 h; esforço extra vai para frame 0, rosto e CTA legível.
8. 474 mil na tela com rodapé "Fonte: CFO, out/2026". Legenda "no Brasil" corrigida. Trecho 24,94 a 29,04 s: legenda fiel ao que se ouve, decidida só depois de ouvir; o letreiro pode carregar a tese.
9. Tzur fora da tela. Mas a DM automática CASE já cita a Tzur desde 18/10 [FATO], o que choca com a autorização marcada como bloqueante no plano final.
10. Medição: D+1 (30/10) logs e comentários; D+2 (31/10) alcance de 48 h; D+7 (05/11) ig_post_stats; planilha com tempo de resposta em minutos e origem `?o=ig-dentista`.
11. CAPI e conversão offline ficam para depois de 18/11 (verba zero até lá [FATO, 06-plano-final.md linha 236]); hoje só registrar diagnóstico com post de origem para poder subir depois.
12. Probabilidade de o reel bater alcance >= 106 e pulo < 68% em 7 dias: 0,45 [PRIOR, faixa 0,25 a 0,65].

---

## 2. Respostas às perguntas

### 0. Pergunta contrária: e se o problema for não ter lead para atender?

É o cenário mais provável, e eu mudo o meu plano por causa dele.

- Comentários por alcance nos reels com o Bruno em cena: 307 de alcance e 3 comentários; 165 e 2; 126 e 0 [FATO, ig_post_stats 21/10/2026]. Soma 5 em 598 = 0,84% [ESTIMATIVA]. Incluindo o reel "Médico com agenda lotada" (63 e 1): 6 em 661 = 0,91% [ESTIMATIVA; se o Bruno está em cena nesse reel: sem dado].
- No alcance meta de 106: 106 x 0,0084 = 0,89 comentário esperado em 7 dias [ESTIMATIVA]. No alcance de 150: 1,3.
- Desses, quantos são dentistas e quantos qualificados: sem dado. Com 50% e 50% [PRIOR], a média de conversas qualificadas fica em 0,22 e a chance de pelo menos uma é 1 - e^-0,22 = 20% [ESTIMATIVA sobre PRIOR, Poisson].
- Histórico de automação: 16 regras ativas, 1 disparo somado [FATO, PostZen]. O 00-SISTEMA.md já registrava 1 disparo no mês [FATO, linha 26].
- Conclusão: o tempo de resposta só vale alguma coisa condicionado a existir um comentário. A alavanca de maior valor esperado é alcance e taxa de comentário (gancho, rosto no frame 0, CTA legível e uma razão para comentar). Minha cadeira entrega o mínimo de fluxo que não estraga o lead raro (sem disparo errado, resposta em até 60 min, origem registrada) e devolve o resto do esforço para o criativo.

### 1. Qual modelo defendo e quais ids entram

Defendo **A enxuto com legenda** como o publicado em 29/10. Motivos da minha cadeira: (a) é o único pipeline com custo por quadro medido [FATO, F26]; (b) mantém o rosto 98,6% do tempo [ESTIMATIVA, seção 3]; (c) N = 1 não separa formato de dia [00-enquadramento D3], então escolher o formato de menor risco de produção é a decisão que não depende de dado que não temos.

| Modelo | Ids misturados | Aproveita | Descarta |
|---|---|---|---|
| A (defendo) | sab8a-475686, twoclipping-041659, twoclipping-000267, techhalla-498547 | sab8a: contrato mínimo (talking head, legenda, grafismo, música) [F45]. 041659: órbita cuja metade de trás passa atrás da cabeça e legenda presa ao tempo de cada palavra [F42]. 000267: lista de banidos, SFX pelo pico medido, loudnorm -14, aviso de preserve-3d [F48]. techhalla: punch-in de 1,0 a 1,08 e mola por glifo [F46] | techhalla: desalinhamento magenta e verde (é RGB split, banido em 000267). ov2.html: prova social inventada, glifos ♥ ✓ ✕, RGB split, tremida, confete com Math.random [F32]. Abertura manifesto com aplausos |
| B | stokebuilder-356793, twoclipping-551116, techhalla-498547 | stokebuilder: rosto sempre presente quando o gráfico ocupa a tela e proibição de inventar número [F44], adaptado para divisão horizontal. 551116: stickers recortados como reacts e letras subindo por máscara [F43] | 8 subquadros (custo 17.472 capturas, F1); emoji; P&B de 551116 (já usado em A) |
| C | gdgtify-929495, twoclipping-041659, alex-prompter-997524 | gdgtify: o relógio é a fala, quietude de 400 ms [F47]. 041659: órbita atrás da cabeça. alex-prompter: esqueleto de 5 cenas mapeado nos tempos da fala [F49] | Cena de "prova" do alex-prompter (o Bruno não disse prova nenhuma, F10); qualquer cena sem rosto |

### 2. Rosto de 0 a 3 s, porcentagem e zoom

- Rosto do quadro 0 ao 90 em A, B e C: sim (regra da conta [FATO, CLAUDE.md]).
- A: única tela cheia sem rosto é a pausa de 13,32 a 13,84 s (0,52 s). Rosto em (36,43 - 0,52)/36,43 = 98,6% [ESTIMATIVA].
- B: tela dividida com o Bruno numa janela de 1080x1120 embaixo [F4, C9] de 3,00 a 32,00 s, tela cheia de 0 a 3 s e no CTA. Rosto em 100% do tempo, menor na janela [ESTIMATIVA].
- C: rosto em 100%, com texto atrás e na frente; nenhuma cena só de tipografia.
- Zoom máximo: 1,08x em A (techhalla), 1,06x em B, 1,10x em C. Todos abaixo de 1,25x. Ampliação total da fonte em A: 1,875 x 1,08 = 2,03x [ESTIMATIVA, DR06].

### 3. Lista de edição quadro a quadro

Ver seção 3 (Modelo A completo, 22 eventos). Para B e C, a seção 3 traz o mapa por bloco de fala com os mesmos quadros de words-raw.json; a lista evento por evento de B e C fica para depois do render cronometrado de A (B13), porque o custo de C é sem dado [F4].

### 4. Trecho 24,94 a 29,04 s ("forna que a gente disputa")

- Regra: a legenda escreve o que se ouve, nunca o roteiro. Cortar fala é proibido.
- Ordem: ouvir o trecho no voz_master.wav e no raw.wav (B02) antes de render. O alinhamento dá 0,04 s para "gente" e 0,06 s para "a" [FATO, words-raw.json], o que é curto demais para três palavras; sinal de erro de transcrição [HIPÓTESE].
- Se ouvir "formar quem disputa": legenda "passa a formar quem disputa".
- Se ouvir "forma que a gente disputa" ou algo próximo: legenda fiel ("passa a formar o que a gente disputa", só o que for ouvido), e a tese vai para o letreiro atrás ("FORMAR QUEM DISPUTA"), que é título e não citação.
- "deixa disputar" (24,94 a 26,20 s): mesma regra. Se o "de" não está no áudio, a legenda não o inventa.
- Regravação: só se o Bruno, ao ouvir, achar a frase confusa. Custo dele, não meu.

### 5. "em Brasil" (4,80 a 5,16 s)

Legenda corrigida para "no Brasil". É troca de uma preposição de 0,16 s, sem mudança de sentido, e a boca não distingue "em" de "no" a essa velocidade [HIPÓTESE]. Registro a correção no log de edição do modelo (dado limpo: toda divergência entre áudio e legenda fica escrita).

### 6. 474 mil na tela

Com rodapé "Fonte: CFO, out/2026" de 2,08 a 5,16 s. Número na tela: "474 MIL", nunca 474.659 (a tabela muda ao longo do dia [FATO, C2] e a soma pode contar inscrição duas vezes [FATO, F68]).

### 7. Áudio: cadeia, alvos e medida

Cadeia proposta (só ffmpeg e numpy, nada instalado):
1. Entrada: voz_master.wav (-14,2 LUFS, TP -0,5 dBTP [FATO, F04]). Qual cadeia gerou o voz_master: sem dado (B01).
2. Pausas: expansor para baixo (agate do ffmpeg) só nas janelas de pausa do words-raw.json com 50 ms de guarda em cada borda, redução de no máximo 12 dB [PRIOR]. Motivo: DR02 mede 16,0 dB entre fala e pausa no master [ESTIMATIVA, 01-fatos]; um gate de 40 dB deixa a voz com cara de robô [PRIOR] e a conta já mostrou que voz sintética falha [FATO, F13].
3. Presença: EQ +2 dB em 3,5 kHz, corte abaixo de 80 Hz; de-esser leve [PRIOR].
4. Voz: loudnorm em duas passadas, I=-14, TP=-1,0, LRA=7, linear=true.
5. Trilha: entre 18 e 22 dB abaixo da voz nos trechos falados [PRIOR], ducking por sidechaincompress, silêncio total na quietude de 19,50 a 20,10 s.
6. SFX: cada um alinhado pelo pico medido (whoosh 268,5 ms, riser 1596,6 ms, swipe 137,1 ms, typing 27,6 ms até o primeiro clique; demais entre 2,5 e 6,6 ms [FATO, F35]), entre 18 e 24 dB abaixo do pico da voz [PRIOR, P03].
7. Mistura: loudnorm em duas passadas no mix, TP=-1,0. Depois codificar AAC e **medir de novo no MP4 final** com ebur128 (true peak) e loudnorm print_format=json. A codificação AAC pode subir o pico [PRIOR]; por isso o alvo é medido no arquivo entregue.
8. Relatório por modelo em JSON (LUFS, TP, LRA, RMS fala e RMS pausa, voz menos trilha por janela de 400 ms, DR20), salvo ao lado do MP4.

Medida de "ruído nas pausas": proponho trocar o 40 dB [PRIOR sem método] por dois números medidos: (a) RMS das 5 pausas de 0,3 s ou mais, com 50 ms de guarda, abaixo de -45 dBFS; (b) aprovação do Bruno num A/B cego de 10 s (master atual contra master novo). O -45 é PRIOR e está escrito como tal.

### 8. Upscale de 576x1024 para 1080x1920

- Usar o base.mp4 já ampliado (1093 quadros, 30 fps, 1080x1920 [FATO, F02]). Motivo de mensuração: os quadros do base.mp4 batem 1 a 1 com a máscara pronta e com round(t x 30) da lista; trocar o método de ampliação muda a contagem e quebra o alinhamento.
- Método usado no base.mp4: sem dado (F23). Conferir no metadado antes do render (B17).
- Riscos: rosto lavado (P18: unsharp leve, teste de 1 quadro); halo no recorte porque o rembg trabalha em 320x320 [FATO, F31]: suavizar a borda da máscara em 2 a 3 px e usar só o maior componente conexo para tirar quem passa ao fundo nos 44 quadros de F30 (P22).
- Zoom limitado a 1,08x para não passar de 2,03x da fonte.

### 9. Pipeline e tempo de render

Ferramentas: Playwright + Chromium (ov2.html adaptado, render(t, layer)), ffmpeg 6.1.1, numpy, máscara rembg já pronta [FATO, F27]. Nada instalado.

Conta do A [ESTIMATIVA, custos de F26]: trás 0,099 + frente 0,131 + composição numpy 0,45 + x264 0,072 = 0,752 s por quadro x 1093 = 822 s (cerca de 14 min). Com a composição no ffmpeg (0,071 s): 0,301 x 1093 = 329 s (cerca de 5,5 min), se o teste B15 confirmar. Motion blur de 3 subquadros só nas janelas de movimento (cerca de 25% do tempo [PRIOR]): mais 0,23 x 2 x 0,25 x 1093 = 126 s. F4 estimou 951 s para A; uso a faixa de 822 a 951 s. B e C: 887 s e 1008 a 1319 s [ESTIMATIVA, F4]. Em série; em paralelo fica 2 a 5 vezes mais lento [FATO, F28].

Correções obrigatórias de QA antes do render:
- comp.py hoje pula PNG faltante em silêncio [FATO, F33]: trocar por falha com mensagem e contar 1093 PNG por camada antes de compor.
- comp.py zera a máscara acima de y=470 [FATO, F29]: em 71,6% dos quadros isso põe o letreiro por cima da cabeça. Remover o corte fixo.
- Constantes do Tzur (54,2 s, P&B até 4,28 s, bloco em 44,45 s [FATO, F34]) viram parâmetros lidos de um JSON por modelo.
- Math.random no render(t) [FATO, F32]: trocar por semente fixa para render determinístico.

### 10. CTA

- Usa o gravado: "Dentista, comenta a sua profissão aqui que eu te respondo" (32,00 a 35,92 s) [FATO, F11]. Esta tomada não tem a versão "segue o perfil" [FATO, words-raw.json].
- Texto na tela: "COMENTA: DENTISTA". Motivo da minha cadeira: comentário de uma palavra é fácil de achar e contar em ig_comments; "a sua profissão" gera respostas soltas.
- Sem regra de automação para "dentista": resposta manual. Se o Bruno decidir que "dentista" conta como palavra-chave do mês (pendente desde o plano final, D3), o texto na tela passa a "Comenta a sua profissão" e nada mais muda.
- TABULEIRO só com alcance >= 150 em 48 h [FATO, CLAUDE.md], e a regra precisa ser criada antes (não existe hoje).
- Legenda do post e comentário fixado dizem o que a pessoa recebe ao comentar, sem promessa: "Eu te respondo com o primeiro passo para transformar a sua técnica em aula para colegas." [HIPÓTESE: razão concreta para comentar sobe a taxa].

### 11. Conformidade com publicidade odontológica

A Res. CFO 196/2019 foi lida no texto oficial pela F3 [FATO, F72], o que atualiza a pergunta 11 do enquadramento. Na tela: nenhuma boca, dente real, raio X, instrumental, procedimento, antes e depois, preço, "grátis", promessa de faturamento ou de agenda. Reacts e ícones genéricos em SVG desenhado. A DM manual não promete resultado e não cita preço (Código de Ética, art. 44 [FATO, F73]). Ponto da minha cadeira: a DM automática CASE fala em "sete para oito dígitos"; se disparar para um dentista, é promessa de resultado entregue no privado. Mais um motivo para excluir "dentista" dessas regras.

### 12. Prova Tzur

Fora da tela. O Bruno não disse [FATO, F10], e o plano final põe a autorização como bloqueante [FATO, 06-plano-final.md seção 7 item 5]. Achado: a regra CASE no PostZen manda DM com a Tzur Capital desde 18/10/2026 [FATO, listCommentAutomations]. Ou a autorização já existe, ou a DM está no ar sem ela. O Bruno decide; eu só registro o conflito.

### 13. Métrica, fonte, data e critério de parar

| Métrica | Fonte | Leitura | Critério |
|---|---|---|---|
| Disparo errado de automação no reel | listCommentAutomationLogs das 6 regras da conta toda | D+1, 30/10 | 1 disparo errado: pausar a regra que disparou e responder à mão |
| Comentários totais e de dentista | ig_comments ou ig_posts (contagem) | D+1 e D+7 | 0 comentários com alcance >= 106: trocar a porta (CTA), não o nicho [06-plano-final.md seção 4] |
| Tempo até a 1ª resposta (min) | horário do comentário menos horário da resposta, na planilha | a cada comentário | mediana acima de 60 min nas primeiras 3 h: rever a hora de publicar |
| Alcance de 48 h | ig_post_stats | D+2, 31/10 | >= 150: criar e ligar TABULEIRO no comentário fixado |
| Alcance, views, assistido, pulo | ig_post_stats | D+7, 05/11 | alcance < 53 e pulo > 75%: parar o nicho nesse formato; >= 106 e pulo < 68%: critério da D2 cumprido |
| Conversa qualificada (definição 8.5 do plano final) | planilha | D+7 e D+30 | 0 em 30 dias com alcance >= 106: a porta falhou |
| Diagnóstico com origem ig-dentista | agenda + parâmetro o=ig-dentista | D+30, D+60 | sem regra nova; só registro |

Conflito de corte de pulo: 68% (D2) contra 60% (plano final) [FATO, C1]. Leio os dois e escrevo os dois na rodada; o critério formal desta cadeira é o do enquadramento (68%).

Hora de publicar: os seguidores online atingem o pico às 18h (425) e às 12h estão em 405 [FATO, ig_best_times]. Os posts próprios foram melhor às 12h (4 posts, média 62 de alcance) [FATO]. A diferença de seguidores online é de 5% [ESTIMATIVA, 425/405]. Critério da minha cadeira: publicar na hora em que o Bruno pode responder em até 60 min nas 3 horas seguintes.

### 14. Regras de texto

Todo texto de tela da seção 3 em PT-BR, sem travessão, sem emoji, sem HighClass, Júnior Prazeres ou Felipe Roser. A única estrutura de contraste é a da fala ("deixa de disputar paciente e passa a formar quem disputa"); nenhum letreiro cria outra.

---

## 3. Lista de edição

Linha do tempo sem cortar pausas: 36,43 s, quadros 0 a 1093 a 30 fps, idênticos ao base.mp4 e à máscara [FATO, F02 e F27]. Motivo: uma única fonte de verdade para tempo (words-raw.json); cortar pausas obrigaria a recalcular todos os quadros e a refazer a máscara. Quadro = round(t x 30).

Camadas: ATRÁS (atrás da pessoa, recortada pela máscara), FRENTE (sobre a pessoa, nunca sobre o retângulo do rosto), TELA CHEIA, TELA DIVIDIDA. Zona livre de texto: 220 px de cima e 450 px de baixo [PRIOR, F63].

### 3.1 Modelo A enxuto com legenda (evento a evento)

| # | Início s (quadro) | Fim s (quadro) | Palavra que dispara | Camada | Texto | Animação | SFX (início = evento menos pico) |
|---|---|---|---|---|---|---|---|
| A01 | 0,00 (0) | 3,00 (90) | "Dentistas" | FRENTE, y 240 a 330 | DENTISTA QUE ENSINA DENTISTA | Letras sobem por máscara em 8 quadros, já legíveis no quadro 0 (entra pronta, anima só o brilho) | nenhum |
| A02 | 0,00 (0) | 35,92 (1078) | cada palavra | FRENTE, y 1300 a 1420 | legenda de 2 a 4 palavras, palavra ativa em #E8B36A | troca a cada palavra, sem salto | nenhum |
| A03 | 0,00 (0) | 2,08 (62) | "Dentistas" | TELA CHEIA (cor) | (sem texto) | P&B que vira cor em 8 quadros a partir de 2,08 s (62 a 70) | riser de 0,48 s (14) a 2,08 s (62) |
| A04 | 2,08 (62) | 5,16 (155) | "474" | ATRÁS, y 300 a 560 | 474 MIL | Contagem 0 a 474 de 62 a 95, "MIL" entra em 3,18 s (95); extrusão de 14 text-shadow, rotateX 55° para 0° em 0,55 s [F24]; saída 0,35 s | impact em 2,075 s (62) |
| A05 | 2,08 (62) | 5,16 (155) | "474" | FRENTE, y 1430 a 1465 | Fonte: CFO, out/2026 | fade 6 quadros | nenhum |
| A06 | 4,80 (144) | 5,16 (155) | "em" | FRENTE (legenda) | no Brasil | correção registrada no log | nenhum |
| A07 | 7,68 (230) | 9,36 (281) | "hora" | ATRÁS, y 300 a 560 | HORA DE CADEIRA | mesma extrusão de A04 | tick em 7,675 s (230) |
| A08 | 7,68 (230) | 8,80 (264) | "hora" | FRENTE, lado direito, x 780 a 1000, y 620 a 840 | (ícone) | relógio SVG desenhado por traço em 12 quadros, ponteiro gira 1 volta | nenhum extra |
| A09 | 9,82 (295) | 13,32 (400) | "todo" | ATRÁS, y 280 a 600 | grade de 6 cartões de perfil iguais (ícone genérico, sem boca nem dente) | cartões entram um a um a cada 3 quadros | nenhum |
| A10 | 11,38 (341) | 13,32 (400) | "diagnóstico" e "conclusão" | ATRÁS (sobre os cartões) | DIAGNÓSTICO / CONCLUSÃO | carimbo em 4 quadros em 11,38 (341) e 12,66 (380), sem easing elástico [F48] | shutter em 11,375 s (341) e 12,655 s (380) |
| A11 | 13,32 (400) | 13,84 (415) | pausa após "conclusão." | TELA CHEIA | 474 MIL PERFIS IGUAIS? | a grade recua até virar mosaico de cartões iguais; único trecho sem rosto (0,52 s) | whoosh em 13,05 s (392); swipe em 13,70 s (411) na volta |
| A12 | 13,84 (415) | 17,92 (538) | "Se" | TELA CHEIA (vídeo) | (legenda) | punch-in 1,00 para 1,06, curva amortecida | nenhum |
| A13 | 15,08 (452) | 17,92 (538) | "técnica" | ATRÁS, y 300 a 560 | SUA TÉCNICA | extrusão; órbita de 041659: a palavra gira, metade de trás passa atrás da cabeça | whoosh em 14,81 s (444) |
| A14 | 17,92 (538) | 19,50 (585) | "existe" | FRENTE, lado esquerdo, x 80 a 300 | (ícone) | seta SVG subindo, traço em 10 quadros | pop em 19,115 s (573) no "mercado." |
| A15 | 19,50 (585) | 20,10 (603) | pausa após "mercado." | TELA CHEIA (vídeo) | (nada novo) | quietude de 0,60 s: tela parada, punch volta a 1,00, trilha em silêncio [F47] | nenhum |
| A16 | 20,64 (619) | 22,22 (667) | "ensinar" | ATRÁS, y 300 a 600, 2 linhas | ENSINAR O SEU COLEGA | órbita atrás da cabeça (041659), 3 subquadros de motion blur | whoosh em 20,37 s (611) |
| A17 | 21,82 (655) | 22,70 (681) | "colega?" | FRENTE, canto inferior esquerdo, y 1050 a 1250 | (react) | plateia SVG de 5 silhuetas, mãos levantam em escada de 3 quadros | pop em 21,815 s (654) |
| A18 | 22,70 (681) | 24,94 (748) | "Eu" | FRENTE, y 1180 a 1260 | Bruno · Estrategista de Lançamento | lower third entra da esquerda em 8 quadros | typing em 22,79 s (684) |
| A19 | 22,82 (685) | 24,24 (727) | "desenho" | FRENTE, lado direito, x 760 a 1000, y 600 a 840 | (ícone) | tabuleiro de xadrez desenhado por traço, uma peça avança uma casa em 23,70 s (711) | tick em 23,695 s (711) |
| A20 | 27,24 (817) | 29,28 (878) | "a" (antes de "forna") | ATRÁS, y 300 a 560 | FORMAR QUEM DISPUTA | extrusão; só entra se B02 for ouvido (seção 2, pergunta 4) | whoosh em 26,97 s (809) |
| A21 | 30,78 (923) | 32,00 (960) | "segundo" | ATRÁS, y 300 a 560 | SEGUNDO PRODUTO | extrusão; punch-in 1,00 para 1,08 de 29,28 (878) a 31,58 (947) | impact em 30,775 s (923); ding_si em 31,175 s (935) |
| A22 | 32,00 (960) | 36,43 (1093) | "Dentista" | FRENTE, y 1080 a 1260 (abaixo do queixo) | COMENTA: DENTISTA | cartão sobe por máscara em 8 quadros; em "profissão" 33,82 (1015) a palavra DENTISTA pulsa 1,00 para 1,05 e volta, sem elástico; seta SVG aponta para o canto inferior direito | swipe em 31,86 s (956); pop em 32,675 s (980) |

Trilha: entra em 0,00 s entre 18 e 22 dB abaixo da voz, silêncio de 19,50 a 20,10 s, fade de 0,30 s no fim [PRIOR]. Sem bloco final depois da fala: o cartão do CTA é o bloco final (cauda muda depois de 35,92 s só de 0,51 s).

Rosto: 98,6% do tempo [ESTIMATIVA]. Zoom máximo 1,08x. Letreiros ATRÁS nunca cobrem rosto por construção; FRENTE nunca entra no retângulo do rosto (checar por quadro contra a máscara: se mais de 2% de pixels de FRENTE caem sobre a máscara entre y 450 e 1000, o render falha no QA [PRIOR, corte]).

### 3.2 Modelo B (tela dividida com reacts) · mapa por bloco

| Bloco | Início s (quadro) | Fim s (quadro) | Gatilho | Camada | Painel de cima (1080x800) | SFX |
|---|---|---|---|---|---|---|
| B1 | 0,00 (0) | 3,00 (90) | "Dentistas" | TELA CHEIA | título fixo DENTISTA QUE ENSINA DENTISTA | nenhum |
| B2 | 3,00 (90) | 5,48 (164) | "mil" | TELA DIVIDIDA | contador 474 MIL + Fonte: CFO, out/2026 | swipe em 2,86 s (86) |
| B3 | 5,48 (164) | 9,36 (281) | "porque" | TELA DIVIDIDA | relógio SVG e cadeira genérica de escritório (nunca cadeira odontológica) | tick em 7,675 s (230) |
| B4 | 9,36 (281) | 13,84 (415) | "quase" | TELA DIVIDIDA | grade de perfis iguais com DIAGNÓSTICO e CONCLUSÃO | shutter 11,375 e 12,655 s |
| B5 | 13,84 (415) | 20,10 (603) | "Se" | TELA DIVIDIDA | sticker recortado "técnica" vira seta de mercado; quietude 19,50 a 20,10 | pop 19,115 s |
| B6 | 20,10 (603) | 24,46 (734) | "Qual" | TELA DIVIDIDA | plateia de colegas com mão levantada; tabuleiro | whoosh 20,37 s |
| B7 | 24,46 (734) | 32,00 (960) | "você" | TELA DIVIDIDA | de 1 cadeira para 1 sala de aula (ícones genéricos); SEGUNDO PRODUTO | impact 30,775 s |
| B8 | 32,00 (960) | 36,43 (1093) | "Dentista" | TELA CHEIA | COMENTA: DENTISTA | pop 32,675 s |

### 3.3 Modelo C (tipografia cinética com órbita) · mapa por cena (5 cenas do alex-prompter)

| Cena | Início s (quadro) | Fim s (quadro) | Gatilho | Palavras que viram arquitetura (ATRÁS) | Quietude |
|---|---|---|---|---|---|
| C1 Problema | 0,00 (0) | 13,32 (400) | "Dentistas" | 474 MIL, HORA DE CADEIRA, MESMO DIAGNÓSTICO | nenhuma |
| C2 Mercado | 13,84 (415) | 19,50 (585) | "Se" | SUA TÉCNICA, MERCADO | 19,50 a 20,10 s (0,60 s, cabe 400 ms com guarda [DR05]) |
| C3 Virada | 20,10 (603) | 22,22 (667) | "Qual" | ENSINAR O SEU COLEGA (órbita completa atrás da cabeça) | nenhuma |
| C4 O que eu faço | 22,70 (681) | 31,58 (947) | "Eu" | DESENHO, LANÇAMENTO, SEGUNDO PRODUTO | nenhuma |
| C5 Nome e CTA | 32,00 (960) | 36,43 (1093) | "Dentista" | COMENTA: DENTISTA (FRENTE) | nenhuma |

---

## 4. Decisões

### D1 · Áudio masterizado

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. voz_master.wav como está | zero trabalho | TP -0,5 dBTP fica acima do alvo [FATO, F04]; depois de somar trilha e SFX o pico sobe mais [PRIOR] |
| 2. Remasterizar do voz_master com medida no MP4 final (minha) | 3 arquivos dentro do alvo medido | cria relatório JSON por modelo que serve de régua para os 5 nichos |
| 3. Refazer do raw.wav comparando rn_std, rn_sh, rn_bd | resolve B01 e pode ganhar 0,3 dB de separação (rn_bd 16,3 contra master 16,0 [ESTIMATIVA, DR02]) | mais tempo para um ganho medido pequeno |
| 4. Regravar só 24,94 a 29,04 s | fala limpa no trecho duvidoso | troca de ambiente e de timbre no meio do reel [PRIOR]; depende do Bruno |
| 5. Fora do óbvio: A/B cego de 10 s para o Bruno antes de mixar os 3 | a aprovação vira dado registrado antes do render | evita o pedido de refazer depois de 3 renders; custo de 1 mensagem |

- Premissas: o voz_master é a melhor base disponível (DR02 mostra rn_bd e master quase iguais); AAC sobe pico [PRIOR]; o Bruno aprova por ouvido, não por número.
- Posição: opção 2 mais a 5.
- Probabilidade de sucesso pelo critério do enquadramento (incluindo os 40 dB): 0,45, faixa [0,25, 0,65]. Sem o critério de 40 dB: 0,75. Confiança: 0,55.

### D2 · Modelo A

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. Tzur v2 fiel | máximo de efeitos | abertura manifesto e bloco final carregam itens banidos e prova social inventada [F32]; mais tempo sem fala |
| 2. Tzur v2 enxuto (4 a 6 letreiros) | menos ruído visual, rosto 98,6% | menos "After Effects" aparente [PRIOR] |
| 3. Fiel mais legenda | legenda soma ao excesso | texto demais competindo com o rosto [PRIOR] |
| 4. Fora do óbvio: enxuto mais legenda, com QA automático de render (contagem de PNG, máscara por quadro, relatório de áudio) (minha) | render que falha alto em vez de sair errado | o mesmo QA vale para B, C e os outros 4 nichos |

- Premissas: o efeito "Bruno em cena" (2,4x a 5,8x [FATO, F13]) se mantém em nicho estreito, o que é a premissa mais frágil [06-plano-final.md D1]; letreiro atrás não derruba retenção (sem dado [F66]).
- Posição: opção 4.
- Probabilidade (produção dentro do critério e, se publicado, alcance >= 106 e pulo < 68% em 7 dias): 0,40, faixa [0,20, 0,60]. Só produção: 0,80. Confiança: 0,40.

### D3 · Modelos B e C

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. B punchy + gdgtify; C explainer 5 cenas | dois estilos de texto parecidos com A | júri tem dificuldade de separar [PRIOR] |
| 2. B tela dividida com reacts; C tipografia cinética com órbita (minha) | atende literalmente "dividindo com reacts" e "letreiro 4D atrás" | B reduz o tamanho do rosto; C tem custo de render sem dado |
| 3. Só B agora, C depois do resultado | menos trabalho | contraria o pedido "faça outros 2" [FATO, pedido do Bruno] |
| 4. Não fazer B e C | zero custo | contraria o pedido |
| 5. Fora do óbvio: B e C renderizados primeiro como amostra de 10 s (quadros 0 a 300) e só renderizados inteiros se o Bruno aprovar a amostra | corta tempo de render perdido | dá o render cronometrado que falta (B13) antes do gasto cheio |

- Premissas: o pedido do Bruno vale mais que a economia; N = 1 não mede desempenho entre modelos [00-enquadramento D3].
- Posição: opção 2 executada pelo caminho da opção 5.
- Probabilidade (júri cego >= A e, se publicado, alcance >= 106 e pulo < 68%): 0,30, faixa [0,15, 0,50]. Confiança: 0,35.

---

## 5. Ideias e hipóteses (78)

| # | Ideia ou hipótese | Confiança | Evidência |
|---|---|---|---|
| 1 | Excluir "dentista", "dentistas" e "profissão" das 6 regras da conta toda (excludeKeywords) antes de 29/10, com aprovação do Bruno | alta | PostZen: regras ativas sem postId [FATO] |
| 2 | Alternativa à 1: pausar CASE de 29/10 a 05/11, porque "caso" é palavra comum em português | alta | CASE: palavras case e caso, matchMode word [FATO] |
| 3 | A DM errada queima a única resposta privada do comentário | alta | descrição PostZen: "one private reply ever, within 7 days" [FATO, nível 2] |
| 4 | Criar a regra TABULEIRO só depois de 150 de alcance em 48 h, mas deixá-la escrita e revisada antes | alta | não existe regra TABULEIRO [FATO]; CLAUDE.md |
| 5 | Ligar linkTracking na regra TABULEIRO | média | 16 de 16 regras com linkTracking false [FATO]; sem dado de clique hoje |
| 6 | Link da DM manual com `?o=ig-dentista` | alta | 06-plano-final.md 9.2 |
| 7 | Não criar regra "dentista": o volume esperado é menor que 1 comentário | alta | 0,84% de comentário por alcance [ESTIMATIVA] |
| 8 | Responder à mão em até 60 min nas 3 primeiras horas | média | 24 h do plano final é PRIOR; comentário respondido rápido pode puxar resposta de volta [HIPÓTESE] |
| 9 | Publicar na hora em que o Bruno está livre para responder | alta | critério da cadeira; ig_best_times mostra diferença pequena entre 12h e 18h [FATO] |
| 10 | Planilha com horário do comentário e da resposta, em minutos | alta | métrica do plano final sem tempo de resposta medido |
| 11 | Coluna "modelo publicado" (A, B ou C) e "versão do arquivo" na planilha | alta | 3 versões do mesmo bruto |
| 12 | Hash sha256 do MP4 publicado no registro da semana | média | dado limpo; evita dúvida sobre qual render subiu |
| 13 | Conferir logs das 6 regras gerais em D+1 | alta | 06-plano-final.md linha 167 |
| 14 | Contar comentários por ig_comments, não por logs (misses não entram no log) | alta | PostZen: "Misses are not logged" [FATO] |
| 15 | O disparo único do CHECKLIST foi teste do próprio Bruno | média | autor bruno26111982 [FATO o nome; HIPÓTESE a pessoa] |
| 16 | Marcar no registro da semana que o número real de leads por automação é 0 se 15 se confirmar | média | ideia 15 |
| 17 | Registrar o conflito: DM CASE cita Tzur antes da autorização confirmada | alta | PostZen CASE [FATO]; plano final seção 7 item 5 |
| 18 | A DM CASE ("sete para oito dígitos") para um dentista vira promessa de resultado no privado | média | Res. 196/2019 e art. 44 [FATO, F72 e F73]; leitura da cadeira |
| 19 | Gargalo deste reel é volume de lead | alta | seção 2, pergunta 0 |
| 20 | Texto legível no quadro 0 com a tese | média | 10 de 10 reels top com texto no frame 0 [FATO, F53] |
| 21 | Título fixo "DENTISTA QUE ENSINA DENTISTA" de 0 a 3 s | média | F55, N = 10, rating qualitativo |
| 22 | Rosto 98,6% do tempo no A | alta | conta da seção 3 |
| 23 | Único corte sem rosto na pausa de 0,52 s, sem fala por cima | média | F07 |
| 24 | Quietude de 0,60 s antes de "Qual é" | média | gdgtify [F47]; DR05 |
| 25 | CTA na tela "COMENTA: DENTISTA" uniformiza a resposta e facilita contar | média | leitura da cadeira; sem dado |
| 26 | Legenda do post diz o que a pessoa recebe ao comentar | média | 4,8% de comentário com CTA claro em @clinicavolpe [FATO, F56] |
| 27 | Comentário fixado do Bruno com a mesma frase | média | idem |
| 28 | Story no dia com caixinha "qual a sua especialidade?" para segunda porta | média | plano final, CTAs para direct; resposta de story abre a janela de DM [FATO, descrição PostZen] |
| 29 | Story repostando o reel 2 h depois | baixa | sem dado de efeito na conta |
| 30 | Não publicar B e C na mesma conta na mesma semana | média | P15, sem precedente |
| 31 | Usar B ou C como anúncio só depois de 18/11, se houver verba | média | verba zero [FATO, F18] |
| 32 | Quando houver verba, subir "diagnóstico agendado" como conversão offline com origem do post | média | persona; planilha já registra origem |
| 33 | CAPI só depois que o formulário do Tabuleiro gravar `o` | média | 06-plano-final.md 9.2 marca isso como HIPÓTESE |
| 34 | Conferir no painel do site se `o=ig-dentista` grava | alta | idem |
| 35 | Buzzfy sem plano MAX: sem teste a seco de regra; testar regra nova com comentário de conta de teste e apagar depois (só com o Bruno) | média | erro Buzzfy call_id 955cc31d [FATO] |
| 36 | comp.py deve falhar alto se faltar PNG | alta | F33 |
| 37 | Contar 1093 PNG por camada antes de compor | alta | F02, F33 |
| 38 | Remover o corte fixo de y=470 do comp.py | alta | F29 |
| 39 | Maior componente conexo da máscara para tirar quem passa ao fundo | média | F30, P22 |
| 40 | Suavizar borda da máscara 2 a 3 px | média | F31 |
| 41 | Semente fixa no lugar de Math.random | alta | F32 |
| 42 | Constantes do Tzur viram JSON por modelo | alta | F34 |
| 43 | Linha do tempo sem cortar pausas, uma fonte de tempo | média | DR04; custo de recalcular |
| 44 | QA automático: pixels de FRENTE sobre o rosto acima de 2% falham | média | regra do enquadramento D2 |
| 45 | Relatório JSON de áudio por modelo | alta | DR19, DR20 |
| 46 | Medir loudness no MP4 final, não no WAV | alta | AAC pode subir pico [PRIOR]; critério D1 é no arquivo final |
| 47 | True peak -1,0 em vez do -1,5 do add_music.sh | média | C7; alvo da D1 |
| 48 | Expansor de até 12 dB só nas pausas | média | DR02 mede 16 dB; gate forte soa sintético [PRIOR] |
| 49 | Trocar o critério de 40 dB por RMS de pausa abaixo de -45 dBFS mais A/B cego | média | P01 sem método |
| 50 | A/B cego de 10 s para o Bruno antes de mixar | média | B04 |
| 51 | Ouvir 24,94 a 29,04 s antes de render | alta | B02 |
| 52 | Legenda fiel ao ouvido, tese no letreiro | alta | F08 |
| 53 | "no Brasil" corrigido e registrado | média | F09, F3 |
| 54 | Rodapé "Fonte: CFO, out/2026" | alta | F68 |
| 55 | Nunca mostrar 474.659 | alta | C2 |
| 56 | Riser terminando exatamente em "474" | média | pico de 1596,6 ms [F35] |
| 57 | SFX pelo pico medido em todos os eventos | alta | F35, F48 |
| 58 | Nenhum SFX na quietude | média | F47 |
| 59 | Ícones em SVG desenhado, nunca glifo de fonte | alta | F32 |
| 60 | Nenhuma cadeira odontológica, só cadeira genérica | média | Res. 196/2019 sobre equipamento [F72] |
| 61 | Lower third "Bruno · Estrategista de Lançamento" em 22,70 s | média | Res. 196/2019 pede identificação de quem divulga (aplicação ao Bruno: HIPÓTESE, P13) |
| 62 | B renderizado em amostra de 300 quadros antes do inteiro | alta | B13 |
| 63 | Render em série | alta | F28 |
| 64 | Motion blur só nas janelas de movimento | média | DR07 |
| 65 | tmix pegando quadros com select mod 3 = 2 | baixa | F4, não testado |
| 66 | Teste de borda escura do tmix em alfa reto | média | B16 |
| 67 | O formato com mais rosto tem mais chance de distribuir | média | F13, F14 |
| 68 | Nicho estreito puxa o alcance para baixo | média | F58: maior reel do recorte dentista com 764 views |
| 69 | Profissão nomeada no gancho não garantiu alcance: o reel do médico teve 63 | média | ig_post_stats 17995270031834903 [FATO] |
| 70 | O reel do médico pediu "Comenta AGENDA" sem regra AGENDA: o comentário que veio ficou sem disparo | média | ig_posts e listCommentAutomations [FATO]; resposta manual: sem dado |
| 71 | Rodada semanal do Módulo 7 em 02/11 já registra D+4 do dentista | média | CLAUDE.md |
| 72 | Se alcance >= 106 e 0 comentário: testar CTA, não formato | alta | 06-plano-final.md seção 4 |
| 73 | Se alcance < 53: o problema é distribuição, e nenhuma mudança de atendimento ajuda | alta | seção 2, pergunta 0 |
| 74 | Pausar as 5 regras da conta toda de temas da série 2 que não têm mais posts ativos | baixa | regras de 18/10 sem disparo [FATO]; depende do Bruno |
| 75 | Revisar a resposta pública padrão sem emoji (a conta de outro negócio usa emoji, a do Estrategista não) | baixa | listCommentAutomations [FATO]; regra de texto |
| 76 | Guardar a planilha como fonte única do Módulo 7 para leads | média | 00-SISTEMA.md, Módulo 7 |
| 77 | Responder comentário com pergunta de audiência na 1ª DM, faturamento só no diagnóstico | média | 06-plano-final.md 8.4 |
| 78 | Fazer o A primeiro e usar o tempo medido para decidir a data de B e C | alta | B13; F4 |

---

## 6. Pre-mortem da cadeira L

Em 20/11/2026 o plano falhou. Como:
1. O reel teve 60 de alcance e 0 comentários. Todo o cuidado de atendimento ficou sem uso. Era o cenário de maior probabilidade e a cadeira sabia.
2. Ninguém mexeu nas regras da conta toda; um dentista escreveu "no meu caso..." e recebeu a DM da Tzur com "sete para oito dígitos". Perdeu-se o lead e ficou um registro de promessa de resultado no privado.
3. O Bruno publicou às 12h e só viu o comentário à noite; a mediana de resposta foi de 8 h e a métrica de tempo virou enfeite.
4. O render do A saiu com 3 quadros faltando porque o comp.py ainda engolia o erro; o reel teve um salto visível no 474 mil.
5. O loudness foi medido no WAV e o MP4 subiu para -0,3 dBTP depois do AAC.
6. A planilha não foi preenchida; o Módulo 7 voltou a escrever "sem dado" em leads.
7. B e C consumiram a semana de render, e o A atrasou a publicação de 29/10.
8. O letreiro "FORMAR QUEM DISPUTA" entrou sem ninguém ouvir o trecho, e um comentário apontou que a frase falada era outra.

---

## 7. Previsões numéricas

Datas a partir de hoje, 21/10/2026: D+30 = 20/11/2026, D+60 = 20/12/2026, D+90 = 19/01/2027.

| Métrica | Previsão | Faixa | Fonte da leitura | Conferência |
|---|---|---|---|---|
| Alcance do reel do dentista em 7 dias | 95 [PRIOR] | 45 a 220 | ig_post_stats, lido em 05/11 | D+30, 20/11/2026 |
| Comentários de dentista no reel em 7 dias | 1 [ESTIMATIVA: 106 x 0,84%] | 0 a 4 | ig_comments | D+30, 20/11/2026 |
| Disparos errados das regras gerais no reel (se nada mudar) | 0, com probabilidade 0,15 de pelo menos 1 [PRIOR] | 0 a 2 | listCommentAutomationLogs | D+30, 20/11/2026 |
| Mediana do tempo até a 1ª resposta | 60 min ou menos, probabilidade 0,55 [PRIOR] | 10 min a 12 h | planilha | D+30, 20/11/2026 |
| Conversas qualificadas de dentista vindas do reel | 0; probabilidade de pelo menos 1: 0,25 [ESTIMATIVA sobre PRIOR] | 0 a 2 | planilha | D+30, 20/11/2026 |
| Diagnósticos agendados com origem ig-dentista | 0; probabilidade de pelo menos 1: 0,12 [PRIOR] | 0 a 2 | agenda + `o=ig-dentista` | D+60, 20/12/2026 |
| Disparos somados de todas as regras do Estrategista desde 21/10 | 3 [PRIOR] | 0 a 12 | listCommentAutomations stats | D+60, 20/12/2026 |
| Contrato vindo do nicho dentista | probabilidade 0,03 [PRIOR] | 0 a 1 | CRM | D+90, 19/01/2027 |
| Mediana de alcance de reel da conta (baseline Buzzfy) | 90 [PRIOR, se o Bruno seguir em cena] | 55 a 160 | ig_post_stats baseline | D+90, 19/01/2027 |

---

## 8. O que mudaria a minha opinião, lacunas e fontes

**Mudaria a minha opinião:**
- Alcance de 150 ou mais em 48 h e 3 ou mais comentários de dentista: volume deixa de ser o gargalo e passo a pedir regra de automação com linkTracking.
- O Bruno não conseguir responder em até 60 min: passo a defender uma regra "dentista" com DM curta que só faz a pergunta de audiência (sem link), para segurar a janela.
- B02 mostrar que a frase dita é "formar quem disputa": tiro a ressalva do letreiro A20.
- Render cronometrado de C abaixo de 15 min: C deixa de ir para o fim da fila.
- Dado do case Tzur v2 publicado com alcance alto e pulo baixo: aumenta a confiança no A fiel.

**Lacunas:**
- Não ouvi o áudio (B02, B03).
- Teste a seco das regras: sem dado (Buzzfy pede plano MAX; PostZen não tem teste a seco). O comportamento do typoTolerance em "caixa", "funil" e "etapa": sem dado.
- Se o autor do único disparo é o Bruno: hipótese pelo nome.
- Se o Bruno está em cena no reel do médico: sem dado.
- Taxa de dentistas entre os comentadores e de qualificados: sem dado.
- Se a conta tem trial reels: sem dado (B23).
- Se o formulário do Tabuleiro grava o parâmetro `o`: sem dado.
- Datasets e pixel da Meta não consultados: sem dado para CAPI; irrelevante até haver verba.
- Custo real de render de B e C: sem dado (B13, B14).
- O case Tzur v2 não aparece entre os 20 reels mais recentes [FATO, ig_posts 21/10/2026]: não foi publicado até hoje, então B06 fica sem dado por falta de publicação.

**Fontes:**
- `run/02-cadeiras/evidencias-L/leituras-postzen-buzzfy-2026-10-21.md` (PostZen listCommentAutomations e listCommentAutomationLogs; Buzzfy ig_posts, ig_post_stats, ig_best_times, ig_automations_list com erro call_id 955cc31d-c97f-4c8d-bb53-ea43def92608), todas em 21/10/2026.
- `videos/nichos/dentista/god/contexto.md`, `words-raw.json`, `transcricao-tempos.txt`.
- `run/00-enquadramento.md`, `run/01-fatos.md` (F01 a F76, C1 a C10, B01 a B25, DR01 a DR20, P01 a P22).
- `run/01-pesquisa/F1` a `F4`.
- `conteudo/sistema-instagram/00-SISTEMA.md` (ficha, Módulos 1, 6 e 7).
- `conteudo/modo-god-nichos/run/06-plano-final.md` (seções 2.2, 3, 4, 5 D3, 6, 7, 8.4, 8.5, 9.1, 9.2).
- `CLAUDE.md` do projeto.
