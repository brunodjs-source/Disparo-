# Plano da cadeira E · Primeiros princípios · Reel do dentista · 21/10/2026

Cliente: O Estrategista (@o_estrategista.com.br). Conselho Agência Reunida Modo GOD.

- **Persona:** pensador que remonta o problema do zero e questiona a pergunta.
- **OTIMIZA PARA:** resolver a pergunta certa.
- **PONTO CEGO (assumido por escrito):** tendo a descartar o que já funciona só porque não foi provado do zero. **Compensação aplicada:** (1) nada do pipeline Tzur é jogado fora sem motivo medido; os 3 modelos usam seg.py, a máscara pronta, ov2.html e cap2.js; (2) o CTA gravado e o Bruno em cena ficam intactos, porque são as duas coisas com dado próprio; (3) cada vez que eu contrario o pedido, deixo a versão literal do pedido disponível como opção e digo o custo.
- **PERGUNTA CONTRÁRIA:** e se a pergunta do Bruno estiver errada? Resposta na seção 2.

Etiquetas: [FATO] com fonte · [ESTIMATIVA] com conta · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, nível 4, nunca fecha objeção sozinho. Trabalhei isolado: não li planos de outras cadeiras.

---

## 0. Fatos novos medidos por esta cadeira (entram no livro de fatos)

Todos de 21/10/2026, somente leitura, nada instalado. Evidências em `run/02-cadeiras/evidencias-E/` (ver LEIA.md).

| # | Fato | Fonte | Nível |
|---|---|---|---|
| E01 | O "forna que a gente disputa" é quase certamente efeito da redução de ruído. No raw.wav, o faster-whisper small, isolado no trecho e sem prompt, ouve "passa a **formar quem** disputa" com probabilidade 0,99 e 0,91 por palavra. No voz_master.wav, o mesmo modelo ouve "forçar" (0,46) ou "forna" (0,52) | trecho_whisper.log; leve_teste.log | 1 (ASR é proxy; falta o ouvido, B02) |
| E02 | Curva da redução de ruído arnndn sh sobre o raw: com mix 0,8 o trecho sai "formar quem" (0,93 e 0,95); com mix 0,9 e 1,0 vira "dessa forma que a gente". O joelho fica entre 0,8 e 0,9 | joelho_teste.log | 1 |
| E03 | Confiança média por palavra (proxy de inteligibilidade): raw 0,878; rn_std 0,849; rn_sh 0,858; rn_bd 0,854; voz_master 0,850. Toda redução de ruído existente custou de 2 a 3 pontos | inteligibilidade.log | 1 (proxy) |
| E04 | O critério de 40 dB depende do método. Pelo DR02 (janelas do alinhamento) o voz_master dá 16,0 dB. Por percentil de janelas de 50 ms (p90 menos p5) dá 41,6 dB, e o raw dá 14,4 dB | piso_percentil.log; dr02_compara.log | 1 |
| E05 | A cadeia proposta por esta cadeira (cadeia_E.sh: highpass 80 Hz, arnndn sh mix 0,8, gate suave, EQ, de-esser, compressor 3:1, loudnorm em 2 passadas com TP -1,5) mede: -14,2 LUFS, TP -1,5 dBTP no WAV; -14,3 LUFS, TP -1,4 dBTP no AAC 192k; LRA 1,6 LU; p90 menos p5 de 40,7 dB; confiança média de 0,868 a 0,880; "formar" a 0,94 | cadeia_E_medida.log | 1 |
| E06 | O AAC sobe o true peak em 0,1 a 0,2 dB: voz_master.wav -0,5 dBTP vira -0,3 dBTP no dentista-audio-masterizado.mp4; E_voz_final -1,5 vira -1,4. Isso resolve o conflito C7: limitar em -1,5 antes de codificar é o caminho para chegar a no máximo -1,0 no arquivo final | ffmpeg loudnorm nos 4 arquivos | 1 |
| E07 | O dentista-audio-masterizado.mp4 já versionado (commit 4c23ca0) está em 576x1024 e mede true peak de -0,3 dBTP. Pelo critério da D1, reprova | ffprobe e loudnorm | 1 |
| E08 | O case Tzur v2 não foi publicado: os 12 reels de 10/10 a 21/10/2026 no ig_posts não falam de Tzur. O "que já fazemos" (Modelo A) tem zero leitura de desempenho na conta | buzzfy-leitura-2026-10-21.md | 1 |
| E09 | Nos 3 melhores reels (Bruno em cena) os comentários foram 3, 2 e 0, ou de 0% a 1,2% do alcance. Compartilhamentos: 0 nos 7 reels lidos | ig_post_stats | 1 |
| E10 | O único reel anterior falando com uma profissão de saúde ("Médico com agenda lotada", 30/09) teve 63 de alcance (1,19x a mediana), 9,4 s assistidos, 56,3% de pulo e 1 comentário | ig_post_stats | 1 |
| E11 | O words-raw.json foi alinhado no voz_master.wav (chave única "voz_master.wav"), e não no raw. Os tempos de 24,94 a 29,04 s herdam o erro da redução de ruído | words-raw.json | 1 |
| E12 | scipy 1.18.1 existe no cbenv. Dá para manter só o maior componente conexo da máscara (P22) sem instalar nada | import no cbenv | 1 |

---

## 1. Veredito (12 linhas)

1. Entregar os 3 modelos, como o Bruno pediu, mas sabendo que a edição é a variável com menos evidência da conta: o que tem dado é o Bruno falando (E09, F13) e o que reprovou foi motion sem rosto (F13).
2. Áudio: trocar o voz_master pela cadeia_E. Ela já cumpre -14 LUFS, TP até -1,0 no AAC e cerca de 40 dB de piso, e preserva o "formar quem disputa" que a limpeza pesada apagou (E01 a E05).
3. Legenda corrigida em dois pontos, e as duas correções são fiéis ao que foi dito: "formar quem disputa" (E01) e "no Brasil" (a troca de "em" de 0,16 s não aparece na boca).
4. Modelo B é o que eu publicaria: letreiro 4D orbital e arquitetônico atrás do Bruno, rosto em tela cheia 100% do tempo, montado no pipeline Tzur. Ids: twoclipping-041659, gdgtify-929495, techhalla-498547 e twoclipping-000267.
5. Modelo A (Tzur v2 enxuto) fica como versão do "que já fazemos", com b-roll em só 2,42 s e rosto em 93,4% do tempo.
6. Modelo C (tela dividida com reacts em SVG): stokebuilder-356793, twoclipping-551116, alex-prompter-997524 e sab8a-475686. O rosto fica visível 100% do tempo, mas em tela cheia só 60,8%. Os 3 blocos divididos viram também 3 stories.
7. Os 3 abrem de jeitos diferentes de propósito (número, palavra-letreiro, título fixo com a pergunta), para que a escolha entre eles teste o gancho e não só o enfeite.
8. Na tela: "+474 mil dentistas ativos" com rodapé "Fonte: CFO, out/2026". Tzur fora da tela. CTA "Comenta: DENTISTA", sem TABULEIRO.
9. Nenhum corte de pausa: a tomada é única, e cortar pausa economiza no máximo 1,1 s ao custo de um jump cut (DR03).
10. A conversão real depende de alcance e de resposta rápida, não do efeito. Com cerca de 1% de comentário sobre o alcance (E09), 106 de alcance dá cerca de 1 comentário [ESTIMATIVA].
11. Métrica: ig_post_stats em 31/10 (48 h) e 05/11 (7 dias). Parar o formato se o alcance ficar abaixo de 53 e o pulo acima de 75%.
12. Primeira ação: o Bruno ouve 3 trechos de 5 s (voz_master, cadeia_E e raw) e escolhe, até 23/10.

---

## 2. Pergunta contrária: e se a pergunta do Bruno estiver errada?

Ela está certa no que pede e errada em três premissas implícitas. Separo fato de hipótese.

**Premissa 1: "o efeito estilo After Effects atrai conversão."** Os dados não sustentam nem derrubam. [FATO, E08] O formato Tzur v2 nunca foi publicado. [FATO, F13 e 00-SISTEMA] Os reels com mais motion na conta (letras 3D, ícones girando, voz sintética) foram os piores. A voz sintética confunde a comparação, então isso não prova que motion atrapalha. [FATO, E09] Nos melhores reels, comentários ficaram entre 0% e 1,2% do alcance. [ESTIMATIVA] Com a meta de 106 de alcance, saem de 0 a 1,3 comentários. A edição mexe na retenção (pulo e tempo assistido), e a retenção mexe no alcance. A conversa, porém, nasce do alcance multiplicado pela taxa de comentário e termina na resposta do Bruno. **Pergunta certa 1:** qual edição segura mais gente nos 3 primeiros segundos e até a virada aos 20 s, sem esconder o rosto? Por isso defendo B, com o rosto em tela cheia o tempo todo.

**Premissa 2: "tirar todo o ruído é masterizar."** [FATO, E01 a E03] A limpeza pesada apagou um consoante: "formar" virou "forna". E foi justamente na frase da virada ("passa a formar quem disputa"), a mais importante para quem vende curso a dentista. **Pergunta certa 2:** quanto ruído dá para tirar sem perder palavra? A curva E02 responde: arnndn com mix 0,8 e um gate suave nas pausas, chegando a 40,7 dB por percentil (E05).

**Premissa 3: "3 modelos = 3 apostas."** [FATO, 06-plano-final.md] Só um vai ao feed em 29/10. [HIPÓTESE P15] Publicar 3 versões do mesmo bruto pode dividir a distribuição. **Pergunta certa 3:** o que os outros 2 rendem além de comparação estética? (a) Viram moldes para consórcio e nutricionista: o mesmo pipeline, só trocando words.json e textos. (b) C vira 3 stories, e o CLAUDE.md pede stories diários. (c) Se a conta tiver trial reels (B23, sem dado), A roda só para não seguidores.

**O que NÃO muda (compensação do ponto cego):** o Bruno pediu letreiro atrás, reacts, tela dividida e acabamento profissional. Os 3 modelos entregam isso. Não proponho trocar a peça por "só legenda", porque isso descartaria o pedido e o pipeline sem dado que justifique.

---

## 3. Respostas às 14 perguntas

**1. Qual modelo e quais ids.** Defendo B para publicar. A e C entram como entregas completas.

| Modelo | Ids misturados | Aproveita | Descarta |
|---|---|---|---|
| A · Tzur v2 enxuto | sab8a-475686, techhalla-498547, twoclipping-000267 (mais o pipeline Tzur) | sab8a: contrato mínimo (legenda, grafismo, música). techhalla: mola por glifo com 125 ms entre letras, punch-in até 1,08, pré-passe de 8 stills. twoclipping-000267: lista de banidos, tmix de 3 subquadros, SFX pelo pico, aviso do preserve-3d | Do Tzur v2: confete, aplausos, RGB split, tremida, glifos ♥ ✓ ✕, "1.287 comentários" e @ fictícios (F32). Do techhalla: desalinhamento magenta e verde, paleta ácida, "STOP SCROLLING" |
| B · Letreiro 4D orbital (defendido) | twoclipping-041659, gdgtify-929495, techhalla-498547, twoclipping-000267 | 041659: órbita com metade de trás escondida pela cabeça (camada back) e metade da frente na camada front; palavra-chave sublinhada no instante em que é falada; máscara estendida além da borda. gdgtify: relógio pela fala, palavras que viram estrutura, quietude de 400 ms. techhalla: mola por glifo. 000267: banidos, tmix, SFX pelo pico | 041659: mapa de calor na silhueta, pixel art, 4:3, a passagem "cair pela cabeça" (esconde o rosto). gdgtify: palco sem pessoa, 1080x1080, laço infinito |
| C · Tela dividida com reacts | stokebuilder-356793, twoclipping-551116, alex-prompter-997524, sab8a-475686 | stokebuilder: o gráfico entra e o Bruno continua na tela, com texto fiel ao dito e rosto cheio entre os gráficos. 551116: stickers vetoriais com borda branca recortada como react, letras subindo por máscara, P&B que vira cor. alex-prompter: 5 cenas mapeadas na fala | stokebuilder: PiP no canto (o rosto de 576 px perde nitidez) e a meta de 35 a 50 momentos. 551116: quadrado 1440, 12 retratos, "views contando" e "MATCH %" (métrica inventada), 8 subquadros (fico com 3). alex-prompter: a cena "prova" sem fonte e os "3 passos" que a fala não diz |

**2. Rosto.** O Bruno aparece de 0 a 3 s nos 3, em tela cheia. Tempo com rosto visível: A 93,4% (o b-roll cobre de 10,24 a 12,66 s, 2,42 s de 36,43); B 100%; C 100% visível, 60,8% em tela cheia (14,28 s divididos). [ESTIMATIVA, somas das listas da seção 4.] Zoom máximo no rosto: A 1,10x; B 1,08x; C 1,00x (a janela de 1080x1120 é recorte sem nova ampliação, F4 e conflito C9). Ampliação total sobre a fonte: no máximo 1,875 x 1,10 = 2,06x [ESTIMATIVA], abaixo dos 2,34x de 1,25x (DR06).

**3. Lista quadro a quadro.** Seção 4, para os 3 modelos. Frames a 30 fps = round(t x 30), contados sobre a linha do tempo sem cortes.

**4. Trecho 24,94 a 29,04 s.** Legenda: "você deixa de disputar paciente e passa a formar quem disputa." Ela é fiel, não corrigida: o raw diz isso segundo o ASR (E01 e E02). Nenhum corte e nenhuma regravação. Antes do render, realinhar só este trecho no áudio da cadeia_E: faster-whisper com palavra por tempo, 24,4 a 29,6 s, substituindo as palavras 53 a 63 do words-raw.json. Condição: o Bruno confirma de ouvido (B02). Se ele ouvir "forna", a legenda escreve o que ele ouvir.

**5. "em Brasil".** Legenda "no Brasil". Motivos: (a) "em" dura 0,16 s (4,80 a 4,96), e a diferença de boca entre "em" e "no" não aparece a 30 fps num plano de selfie [HIPÓTESE, conferir no quadro 144]; (b) com o som desligado, "em Brasil" parece erro de digitação para um público profissional [PRIOR]; (c) o roteiro aprovado diz "no Brasil" (06-plano-final.md seção 2.2). Isto é revisão de português, e não muda o sentido.

**6. 474 mil.** Na tela: "+474 mil dentistas ativos" e rodapé "Fonte: CFO, out/2026", com 28 px de altura, visível pelo menos 2,0 s (de 2,08 a 5,16 s). Base: soma de 474.659 nas 27 linhas do CFO (F68). "Mais de 474 mil" vale também para a leitura de 474.640 (C2). Lacuna B19: se a soma conta inscrição dupla, "ativos" segue certo para inscrições. Plano B se o Bruno preferir: "Mais de 470 mil dentistas ativos", que também cabe nas duas leituras.

**7. Áudio.** Cadeia de voz: cadeia_E.sh (E05), igual para os 3 modelos.
- (1) highpass 80 Hz; (2) arnndn sh com mix 0,8; (3) +15 dB e agate com limiar 0,08, ratio 6, range -24 dB, ataque de 3 ms e release de 200 ms; (4) EQ -2 dB em 250 Hz e +2 dB em 3,2 kHz; (5) deesser i=0,3; (6) acompressor 3:1; (7) loudnorm em 2 passadas na voz.
- Trilha: lounge própria do som.py da Série 2 (evita licença), com volume base de 0,085 (cerca de -21 dB, o mesmo do add_music.sh) e sidechain com threshold 0,02, ratio 5, ataque de 20 ms e release de 350 ms. Alvo: trilha de 18 a 24 dB abaixo da voz nos trechos falados [PRIOR, notdwd-998633 diz 10 a 15 dB; escolho mais baixo porque a voz tem ruído residual].
- SFX da biblioteca própria (F35), posicionados pelo pico, de 18 a 24 dB abaixo do pico da voz (P03). No B, a trilha zera em 19,62 a 20,02 s (quietude).
- Mistura final: loudnorm em 2 passadas com I=-14, TP=-1,5 e LRA=7, depois AAC 192k.
- Medição no MP4 final de cada modelo (DR19): aceitar de -15 a -13 LUFS e TP até -1,0 dBTP. Medir também a voz acima da trilha em janelas de 400 ms (DR20), com RMS da voz menos RMS da trilha de pelo menos 12 dB em 100% das janelas faladas.
- Piso: método por percentil (p90 menos p5 de 50 ms) de pelo menos 35 dB no stem de voz, mais a escuta das pausas de 13,32 a 13,84 s e 19,50 a 20,10 s.

**8. Upscale.** Não refazer o base.mp4: ele já tem 1080x1920 a 30 fps e 1093 quadros, e a máscara (589 s de CPU) foi feita sobre ele (F02, F27). Riscos e tratamento:
- (a) aspecto lavado: unsharp leve (5:5:0,4) testado em 1 quadro (P18);
- (b) halo da máscara de 320x320 (F31): erodir 1 px e esfumar 3 px na escala de 1080; letreiro de trás em ouro sobre fundo escuro, nunca branco perto do cabelo;
- (c) gente ao fundo em 44 quadros (F30): manter só o maior componente conexo com scipy.ndimage.label no cbenv (E12);
- (d) linha mk[:470]=0 do comp.py: remover, porque o topo da cabeça passa de y=470 em 71,6% dos quadros (F29).
O método original da ampliação é sem dado (B17).

**9. Pipeline e tempo.** Só ferramentas existentes:
- seg.py, já rodado; mask.mp4 pronto;
- ov2.html adaptado em 3 arquivos (ovA, ovB, ovC) com render(t, layer) determinístico, sem Math.random (F32);
- cap2.js no Playwright;
- comp.py com as correções do item 8;
- ffmpeg para tmix, mistura e x264 crf 18.
Tempos [ESTIMATIVA, F4 DR08, sem render completo cronometrado]: A cerca de 951 s, B cerca de 887 s, C de 1008 a 1319 s; os 3 em série dão de 47 a 53 min. Em paralelo fica pior (F28). Antes de cada render cheio, cronometrar 300 quadros (B13) e fazer o pré-passe de 8 stills (techhalla).

**10. CTA.** Usar o gravado: "Dentista, comenta a sua profissão aqui que eu te respondo" (32,00 a 35,92 s). Na tela: "Comenta: DENTISTA" a partir de 32,68 s ("comenta"). Sem TABULEIRO: ele só entra se o alcance passar de 150 em 48 h (CLAUDE.md). Se "dentista" contar como palavra-chave do mês, a decisão é do Bruno (06-plano-final.md, D3); o CTA falado já está gravado e não muda.

**11. Conformidade.** A Res. CFO 196/2019 já foi lida no texto oficial (F72, evidencias-F3/res-cfo-196-2019.txt), o que corrige a premissa da pergunta.
- Nenhum modelo mostra boca, dente real, raio X, instrumental, cadeira odontológica reconhecível, procedimento, antes e depois, preço, "grátis", promessa de faturamento ou agenda, nem "melhor técnica".
- "Hora de cadeira" vira ícone genérico de relógio sobre uma cadeira estilizada de escritório. Nada de cadeira odontológica [HIPÓTESE P11: ícone de dente, só como contorno abstrato, e só no C; dá para retirar sem custo].
- Art. 44 do Código de Ética: nenhuma crítica à técnica de colega. "Mesmo diagnóstico e mesma conclusão" se refere ao formato de post, não à técnica [HIPÓTESE, B21].

**12. Prova Tzur.** Fora da tela nos 3. Motivos: o Bruno não disse (F10); texto na tela tem que ser fiel ao dito (stokebuilder-356793); a autorização do cliente Tzur não existe por escrito (B24); e o case nunca foi publicado (E08). Posso pôr na legenda do post só com autorização escrita do Bruno e do Tzur.

**13. Métrica.** Fontes: ig_post_stats (Buzzfy), com alcance, views, tempo médio assistido, pulo, comentários e compartilhamentos; listCommentAutomationLogs (PostZen); planilha manual de conversas.
- Leituras: 31/10/2026 (48 h) e 05/11/2026 (7 dias); registro em semanas/2026-11-02.md e semanas/2026-11-09.md (Módulo 7).
- Critério de sucesso da D2 e da D3: alcance de 106 ou mais e pulo abaixo de 68%.
- Conflito C1: adoto 68% porque é a mediana medida. 60% fica como meta de esforço e não como critério (06-plano-final.md).
- Parar: alcance abaixo de 53 e pulo acima de 75% em 7 dias faz parar o formato de nicho com esse modelo.
- TABULEIRO: alcance de 150 em 48 h.
- Conversa: pelo menos 1 comentário de dentista respondido pelo Bruno em até 2 h [PRIOR sobre o tempo].

**14. Regras de texto.** Nenhuma tela usa travessão, emoji, "não é X, é Y" ou nomes proibidos. Os reacts são SVG desenhados, nunca glifos ♥ ✓ ✕ (F32). Conferência automática antes do render: grep pelos caracteres U+2014 e U+2013, pela faixa de emoji e pelos 3 nomes nos arquivos ovA, ovB e ovC.

---

## 4. Listas de edição quadro a quadro

Convenções:
- Tempo em segundos com o frame a 30 fps entre colchetes.
- Camadas: ATRÁS = camada back, composta sob a máscara; FRENTE = camada front; CHEIA = tela cheia sem o Bruno; DIVIDIDA = painel de cima com o Bruno embaixo.
- Legenda nos 3 modelos: FRENTE, de 2 a 4 palavras, palavra ativa em #E8B36A, demais em branco com sombra; y de 1240 a 1420 (respeita os 450 px de baixo, F63); entra em 0,12 s por máscara.
- SFX: o início do arquivo é o tempo do evento menos o pico (F35): whoosh 0,27 s antes, swipe 0,14 s antes, riser 1,60 s antes; pop e tick no próprio quadro.
- Palavras de 53 a 63 serão realinhadas (item 4). Até lá, uso os limites do trecho.

### 4.1 Modelo A · Tzur v2 enxuto (o que já fazemos)

| Início [fr] | Fim [fr] | Gatilho (words-raw) | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|
| 0,00 [0] | 2,08 [62] | "Dentistas" | FRENTE + vídeo | legenda "Dentistas, são mais de" | vídeo em P&B (Tzur), legenda visível no quadro 0 | trilha entra em fade de 0,6 s |
| 0,48 [14] | 2,08 [62] | antecipa "474" | áudio | (nenhum) | (nenhuma) | riser começa em 0,48 e culmina em 2,08 |
| 2,08 [62] | 5,16 [155] | "474" | ATRÁS | "+474 MIL" (Cinzel, ouro, extrusão de 14 sombras) | P&B vira cor em 0,32 s; letreiro sobe de trás da cabeça com rotateX de 55° a 0° e mola por glifo a 125 ms | impact no 62 |
| 3,80 [114] | 5,16 [155] | "colegas" | FRENTE | rodapé "Fonte: CFO, out/2026" (28 px, y 1460) e legenda "dentistas ativos no Brasil" | fade 0,2 s | (nenhum) |
| 5,16 [155] | 5,48 [164] | pausa | ATRÁS | "+474 MIL" sai | saída de 0,35 s | (nenhum) |
| 5,48 [164] | 7,68 [230] | "porque" | vídeo | legenda "Por que você ainda só vende" | punch-in de 1,00 a 1,06 em 0,4 s | (nenhum) |
| 7,68 [230] | 9,36 [281] | "hora" | ATRÁS | "HORA DE CADEIRA" | mola por glifo; relógio SVG pequeno gira um quarto de volta | tick no 230 e no 249 |
| 9,36 [281] | 10,24 [307] | "quase" | FRENTE | legenda "e quase todo perfil" | (nenhuma) | (nenhum) |
| 10,24 [307] | 12,66 [380] | "perfil" | CHEIA (b-roll) | grade 3x3 de 9 cartões de post idênticos, em SVG neutro, com "diagnóstico" e "conclusão" escritos (sem boca, sem dente) | entra com 0,30 s de respiro (Tzur); os cartões acendem em sequência a 80 ms | swipe começando em 10,10 |
| 12,66 [380] | 13,84 [415] | "conclusão." | vídeo | legenda "e a mesma conclusão." | volta ao Bruno com 0,30 s de respiro; punch-out para 1,00 | whoosh começando em 12,39 |
| 13,84 [415] | 17,92 [538] | "Se" | FRENTE | legenda; "técnica" e "aprender" em ouro | (nenhuma) | (nenhum) |
| 17,92 [538] | 19,50 [585] | "existe" | ATRÁS | "UM MERCADO" | mola por glifo | (nenhum) |
| 20,10 [603] | 20,64 [619] | "Qual" | FRENTE | react SVG: ponto de interrogação desenhado à mão, borda branca | traço se desenha em 0,25 s e balança de leve | pop no 603 |
| 20,64 [619] | 22,70 [681] | "ensinar" | ATRÁS | "ENSINAR O SEU COLEGA" | mola por glifo; punch-in de 1,06 a 1,10 | whoosh começando em 20,37 |
| 22,70 [681] | 24,46 [734] | "Eu" | FRENTE | react SVG: lápis traçando uma linha de planta (blueprint) | desenho de traço em 0,6 s | typing no 685 |
| 24,46 [734] | 29,28 [878] | "você" (trecho realinhado) | FRENTE | legenda fiel "você deixa de disputar paciente / e passa a formar quem disputa" | "formar quem disputa" em ouro | (nenhum) |
| 29,28 [878] | 32,00 [960] | "Sua" | ATRÁS | "SEGUNDO PRODUTO" | mola por glifo; punch-out para 1,00 em 31,58 | ding_si no 923 ("segundo") |
| 32,00 [960] | 36,43 [1093] | "Dentista" | FRENTE (bloco final) | "Comenta: DENTISTA" a partir de 980 ("comenta"); @o_estrategista.com.br a partir de 1061 | vinheta escura de 30% nas bordas, Bruno sempre visível; cartão sobe por máscara em 0,3 s | sub no 980; trilha em fade-out de 2,5 s |

Rosto: 93,4% (sai só de 10,24 a 12,66 s). Zoom máximo: 1,10x.

### 4.2 Modelo B · Letreiro 4D orbital e arquitetônico (defendido)

Ideia única: as palavras faladas viram peças de uma estrutura na parede atrás do Bruno. Cada peça se apoia na anterior (gdgtify), e na virada uma órbita passa atrás e na frente da cabeça (twoclipping-041659). O rosto fica em tela cheia 100% do tempo.

| Início [fr] | Fim [fr] | Gatilho | Camada | Texto | Animação | SFX |
|---|---|---|---|---|---|---|
| 0,00 [0] | 1,14 [34] | "Dentistas" | ATRÁS | "DENTISTAS" já de pé atrás da cabeça desde o quadro 0 (legível sem animação) | leve parallax pelo vidstab (B18) ou fixo | trilha baixa |
| 0,00 [0] | 36,43 [1093] | todas | FRENTE | legenda palavra a palavra | sublinhado em ouro na palavra-chave no instante dito (041659) | (nenhum) |
| 2,08 [62] | 5,16 [155] | "474" | ATRÁS | "+474 MIL" desce e vira a VIGA DE BASE horizontal em y 300 a 420 | mola por glifo de 125 ms; tmix de 3 subquadros na queda | impact no 62; riser de 0,48 a 2,08 |
| 3,80 [114] | 5,16 [155] | "colegas" | FRENTE | rodapé "Fonte: CFO, out/2026" | fade 0,2 s | (nenhum) |
| 7,68 [230] | 8,80 [264] | "hora" | ATRÁS | "HORA DE CADEIRA" vira um BLOCO apoiado na viga, com uma linha de teto fina por cima (o teto da hora) | encaixe com mola; a linha de teto desce 40 px | tick no 230 |
| 10,24 [307] | 13,32 [400] | "perfil" | ATRÁS | "MESMO DIAGNÓSTICO" e "MESMA CONCLUSÃO" repetidos 3 vezes em fileira, em cinza (peças iguais, empilhadas) | cópias deslizam a 80 ms uma da outra | swipe começando em 10,10 |
| 15,08 [452] | 15,48 [464] | "técnica" | ATRÁS | "TÉCNICA" vira uma COLUNA vertical em ouro, à esquerda da cabeça | sobe de trás do ombro; as fileiras cinza recuam com 50% de opacidade (opacidade no pai, nunca no preserve-3d, 000267) | pop no 452 |
| 17,92 [538] | 19,50 [585] | "existe um mercado." | ATRÁS | "MERCADO" vira a VERGA sobre a coluna | encaixe | (nenhum) |
| 19,50 [585] | 20,10 [603] | pausa de 0,60 s | todas | tudo parado | QUIETUDE: nada se move de 19,62 a 20,02 [589 a 601], 0,40 s (gdgtify, DR05) | trilha zera em 19,62 e volta em 20,02 |
| 20,10 [603] | 20,64 [619] | "Qual é" | FRENTE | legenda "Qual é?" | (nenhuma) | (nenhum) |
| 20,64 [619] | 22,70 [681] | "ensinar" | ATRÁS + FRENTE | "ENSINAR O SEU COLEGA" escrito ao longo de uma ÓRBITA elíptica em volta da cabeça | a metade de trás da órbita vai na camada ATRÁS (some atrás da cabeça) e a metade da frente na FRENTE; 1 volta em 2,0 s; punch-in de 1,00 a 1,08; tmix de 3 subquadros | whoosh começando em 20,37 |
| 22,70 [681] | 24,24 [727] | "Eu desenho seu lançamento" | ATRÁS | a estrutura toda ganha linhas de cota (planta técnica), traço de 1 px em ouro | traço se desenha em 0,8 s | typing no 685 |
| 24,46 [734] | 29,04 [871] | "você deixa de disputar..." | ATRÁS | a fileira cinza de "MESMO DIAGNÓSTICO" cai para fora do quadro pela base; fica a coluna "TÉCNICA" | queda com aceleração, sem quique (sem easing elástico, 000267) | swipe no fim de "disputar" |
| 29,28 [878] | 32,00 [960] | "Sua técnica vira um segundo produto." | ATRÁS | "SEGUNDO PRODUTO" vira o TELHADO apoiado na coluna "TÉCNICA" e na verga "MERCADO" | encaixe final; punch-out para 1,00 em 31,58 | ding_si no 923 |
| 32,00 [960] | 36,43 [1093] | "Dentista, comenta..." | FRENTE | "Comenta: DENTISTA" em cartão sólido a partir de 980; @o_estrategista.com.br a partir de 1061 | a estrutura escurece 40% atrás; o cartão sobe por máscara | sub no 980; fade-out da trilha |

Rosto: 100% em tela cheia. Zoom máximo: 1,08x. Banidos ausentes: shockwave, partículas, RGB split, camera shake, lens flare, neon, piso de grade, fundo piscando e easing elástico (000267). Risco técnico principal: a órbita depende da máscara perto da cabeça; por isso o item 8 (c) e (d) vem antes.

### 4.3 Modelo C · Tela dividida explicativa com reacts

Janela do Bruno: 1080x1120 recortada do base.mp4 (sem nova ampliação), com o recorte seguindo o centro da máscara, embaixo (y 800 a 1920). Painel de cima: 1080x800 opaco, preto #141210, desenho em SVG, renderizado em JPEG por pipe (0,077 s por quadro, F26). Entrada e saída da divisão: carrossel de 0,55 s (551116).

| Início [fr] | Fim [fr] | Gatilho | Camada | Texto | Animação | SFX |
|---|---|---|---|---|---|---|
| 0,00 [0] | 5,48 [164] | "Dentistas" | vídeo cheio + FRENTE | título fixo no topo desde o quadro 0: "Você ainda só vende hora de cadeira?" (palavras ditas aos 5,48 s); legenda embaixo | o título entra no quadro 0 já legível | trilha entra |
| 2,08 [62] | 5,16 [155] | "474" | FRENTE | "+474 mil dentistas ativos" e "Fonte: CFO, out/2026" | letras sobem por máscara (551116) | impact no 62 |
| 5,48 [164] | 13,32 [400] | "porque" | DIVIDIDA (S1) | cena 1, PROBLEMA (alex-prompter): relógio SVG sobre uma cadeira de escritório estilizada, com "HORA DE CADEIRA"; em 10,24 [307] vira uma grade de 9 cartões iguais com "MESMO DIAGNÓSTICO / MESMA CONCLUSÃO" | carrossel de 0,55 s na entrada; react: sticker vetorial de "sobrancelha levantada" (traço, não emoji) em 11,14 [334] | swipe começando em 5,34; tick no 230; pop no 334 |
| 13,32 [400] | 20,10 [603] | "Se você domina" | vídeo cheio | legenda; "técnica" em ouro | painel sai em 0,55 s; punch nenhum | whoosh começando em 13,05 |
| 20,10 [603] | 24,24 [727] | "Qual é? Ensinar o seu colega. Eu desenho seu lançamento" | DIVIDIDA (S2) | cena 2, MERCADO: um ícone de pessoa (contorno) liga-se por linhas a 12 ícones menores (ensinar colega); em 22,82 [685] tudo vira uma planta técnica com "LANÇAMENTO" | painel em P&B que vira cor em "ensinar" (619), como no 551116; react: sticker de lápis | pop no 603; whoosh começando em 20,37; typing no 685 |
| 24,24 [727] | 29,28 [878] | "você deixa de disputar..." | vídeo cheio | legenda fiel com "formar quem disputa" em ouro | painel sai | swipe começando em 24,10 |
| 29,28 [878] | 31,58 [947] | "Sua técnica vira um segundo produto." | DIVIDIDA (S3) | cena 3, SEGUNDO PRODUTO: uma caixa "TÉCNICA" se duplica em duas caixas, com "1" e "2" | duplicação com mola amortecida | ding_si no 923 |
| 31,58 [947] | 36,43 [1093] | "Dentista, comenta..." | vídeo cheio + FRENTE | cena 5, CTA: "Comenta: DENTISTA" a partir de 980; @o_estrategista.com.br a partir de 1061 | cartão sobe por máscara | sub no 980; fade-out |

Cena 4 (prova) do alex-prompter: retirada de propósito, porque não há prova dita nem autorizada. Rosto visível 100%; em tela cheia 22,15 s de 36,43 s = 60,8% [ESTIMATIVA: 36,43 - (7,84 + 4,14 + 2,30)]. Stories: S1, S2 e S3, cada um com legenda e CTA "o vídeo completo está no perfil", viram 3 stories de 5 a 8 s [HIPÓTESE].

---

## 5. Decisões

### D1 · Áudio masterizado

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. voz_master como está | zero trabalho | TP -0,3 no AAC reprova (E07); "forna" fica na fala (E01); a legenda vai brigar com o ouvido |
| 2. Remasterizar a partir do voz_master (limitador, EQ, de-esser, trilha) | corrige o TP | a perda do "formar" é irreversível a partir dele; o mix esconde o piso, mas não devolve a consoante |
| 3. Refazer do raw comparando rn_std, rn_sh e rn_bd | escolhe o menos ruim dos 3 | os 3 perdem 2 a 3 pontos de inteligibilidade (E03); comparar só esses 3 não sai do problema |
| 4. **Fora do óbvio: cadeia por inteligibilidade (cadeia_E: arnndn mix 0,8 e gate suave), escolhida por escuta cega do Bruno em 3 trechos de 5 s** | já medida: -14,2 LUFS, TP -1,4 no AAC, 40,7 dB por percentil, "formar" a 0,94 (E05) | o Bruno decide pelo ouvido e não pelo número; cria o padrão de áudio para os outros nichos; risco de gate audível |
| 5. Regravar 24,94 a 29,04 s | resolveria uma fala ruim | E01 mostra que a fala está boa; regravar muda o timbre e a sala; descartada |

- **Premissas:** o ASR serve de proxy para o ouvido humano [HIPÓTESE]; o gate com release de 200 ms não corta finais de palavra [HIPÓTESE, ouvir 13,32 e 31,58 s]; o Instagram não renormaliza de um jeito que mude a escolha [sem dado, B05].
- **Posição:** opção 4, com a 2 como reserva se o Bruno preferir o timbre do voz_master na escuta cega.
- **Probabilidade de sucesso** pelo critério (3 de 3 dentro de LUFS e TP, voz acima da trilha, zero pedido de refazer; 40 dB medido por percentil): **0,65 [0,45; 0,80]**. A parte técnica fica perto de 0,95 [ESTIMATIVA, E05 já passa]; "zero pedido de refazer" é o risco.
- **Confiança:** 0,6.

### D2 · Modelo A

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. Tzur v2 fiel (manifesto, confete, bloco final em tela cheia) | máxima continuidade | herda banidos e prova inventada (F32); o bloco final esconde o rosto no CTA |
| 2. **Tzur v2 enxuto, com legenda, b-roll só em 10,24 a 12,66 s e bloco final com o Bruno visível** | rosto em 93,4% | molde reaproveitável; a única comparação limpa com B é b-roll contra estrutura atrás |
| 3. Tzur v2 fiel mais legenda (cap2.js) | mais texto | poluição: legenda, letreiro e b-roll competindo no mesmo quadro |
| 4. Fora do óbvio: A sem efeito, só legenda e o número (controle mínimo, sab8a puro) | mede o que o efeito acrescenta | contraria "no que já fazemos"; fica como variante interna, não como entrega |

- **Premissas:** o P&B que vira cor no número segura o primeiro segundo [PRIOR]; o b-roll curto não derruba a retenção [HIPÓTESE].
- **Posição:** opção 2.
- **Probabilidade de sucesso** pelo critério (produção e, se publicado, alcance de 106 ou mais com pulo abaixo de 68%): produção 0,85; desempenho 0,35; conjunta **0,30 [0,15; 0,45]**. Base: de 6 reels de 30/09 a 06/10, 3 passaram de 106 e 5 tiveram pulo abaixo de 68% (E09 e buzzfy-leitura); o único reel para profissão de saúde teve 63 (E10), daí o desconto.
- **Confiança:** 0,45.

### D3 · Modelos B e C

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. B = sab8a + gdgtify punchy; C = explainer de 5 cenas sobre o rosto com máscara de tipo | cobre "punchy" e "explicar" | o C sobre o rosto empilha texto em cima da cara |
| 2. **B = letreiro 4D orbital e arquitetônico (041659, gdgtify, techhalla, 000267); C = tela dividida com reacts (stokebuilder, 551116, alex-prompter, sab8a)** | atende literalmente "letreiro 4D atrás" e "dividindo com reacts"; B fica com o rosto em 100% | B vira o molde do nicho; C vira stories; os 3 se diferenciam no gancho (número, palavra, título fixo) |
| 3. Só B agora, C depois do resultado | economiza de 17 a 22 min de render | contraria o pedido de 3 modelos |
| 4. Fora do óbvio: B e C iguais na edição, mudando só os 3 primeiros segundos (3 ganchos) | isolaria a única variável com sinal (gancho e título, F55) | não entrega "estilo After Effects" nem "dividindo"; registro como ideia para o próximo nicho |

- **Premissas:** o júri cego dá nota a acabamento e não a conversão (P17); a órbita não descola da cabeça com a máscara corrigida [HIPÓTESE, teste de 300 quadros]; a janela de 1080x1120 mostra cabeça e ombros (P19).
- **Posição:** opção 2. B é o candidato a publicar; C serve de stories e de reserva.
- **Probabilidade de sucesso** pelo critério (nota de júri igual ou maior que A em B e C, e, se um for publicado, 106 ou mais com pulo abaixo de 68%): júri 0,6; desempenho de B 0,38; conjunta **0,30 [0,15; 0,45]**.
- **Confiança:** 0,4.

### D4 · Publicação (exploratória, porque a pergunta contrária mexe nela)

- **Posição:** publicar só o B em 29/10. A fica no arquivo como molde. Os 3 blocos do C entram como stories no mesmo dia, de 2 a 4 h depois do reel [HIPÓTESE].
- **Por quê:** o B maximiza a única variável com dado (rosto em tela cheia). Os stories do C são o ritmo diário que o CLAUDE.md já pede, sem gastar um segundo reel com o mesmo bruto (P15).
- **Probabilidade de leitura limpa:** 0,5 [0,3; 0,7] (N = 1).
- **Confiança:** 0,35. A decisão final é do Bruno.

---

## 6. Ideias e hipóteses numeradas (80)

| # | Ideia ou hipótese | Confiança | Evidência |
|---|---|---|---|
| 1 | Trocar o voz_master pela cadeia_E nos 3 modelos | alta | E01 a E05 |
| 2 | Escuta cega do Bruno: 3 trechos de 5 s (24,5 a 29,5 s) com voz_master, cadeia_E e raw, sem dizer qual é qual | alta | B02, B04 |
| 3 | A legenda de 24,94 a 29,04 s é "deixa de disputar paciente e passa a formar quem disputa" | alta | E01, E02 |
| 4 | Realinhar só as palavras 53 a 63 na cadeia_E antes do render | alta | E11 |
| 5 | O limitador vai a -1,5 dBTP antes do AAC para chegar a no máximo -1,0 depois | alta | E06 |
| 6 | Medir LUFS e TP no MP4 final, não no WAV | alta | E06, E07 |
| 7 | Trocar o critério de 40 dB por "p90 menos p5 de 50 ms de pelo menos 35 dB no stem de voz, mais escuta" | média | E04 |
| 8 | Gate com release de 200 ms não come final de palavra | média | E05 (ASR), falta ouvido |
| 9 | O mix 0,8 do arnndn é o joelho para esta sala e este microfone; outro bruto pede outro valor | média | E02 |
| 10 | Padronizar a curva de mix (0,6 a 1,0) como teste fixo de áudio para os 5 nichos | média | E02 |
| 11 | Usar a trilha própria do som.py para evitar licença e repetição de Mixkit | média | contexto.md, Série 2 |
| 12 | Trilha de 18 a 24 dB abaixo da voz | média | notdwd-998633 (10 a 15 dB), P03 |
| 13 | A trilha mascara o piso residual das pausas | baixa | sem medição DR20 |
| 14 | Zerar a trilha na quietude de 0,40 s antes de "Qual é" | média | gdgtify-929495, DR05 |
| 15 | SFX posicionados pelo pico e não pelo início | alta | twoclipping-000267, F35 |
| 16 | No máximo 9 SFX por modelo; nada de SFX em toda troca | média | Choppity contra VibeRoll (C4) |
| 17 | Publicar o B e não o A | média | E09, F13 (rosto em tela cheia) |
| 18 | O rosto em tela cheia 100% do tempo segura melhor que o b-roll | baixa | F13 é Bruno contra voz sintética, não b-roll contra rosto |
| 19 | Os 3 modelos abrem com ganchos de texto diferentes (número, palavra-letreiro, título fixo) | média | F54, F55 |
| 20 | O título fixo do C ("Você ainda só vende hora de cadeira?") é o gancho mais forte em texto | baixa | F55 (N = 10, rating qualitativo) |
| 21 | Texto legível no quadro 0 nos 3 | alta | F53 (10 de 10) |
| 22 | "DENTISTAS" já de pé atrás da cabeça no quadro 0 (B) | média | F53, pedido do letreiro |
| 23 | Legenda "no Brasil" | média | F09, 06-plano-final.md |
| 24 | Rodapé "Fonte: CFO, out/2026" visível pelo menos 2 s | alta | F68, contexto.md |
| 25 | "+474 mil" vale para as duas leituras do dia | alta | C2 |
| 26 | Plano B para o número: "Mais de 470 mil" | média | B19 |
| 27 | Tzur fora da tela e da legenda do post sem autorização escrita | alta | F10, B24, E08 |
| 28 | Remover a linha mk[:470]=0 do comp.py | alta | F29 |
| 29 | Manter só o maior componente conexo da máscara com scipy no cbenv | alta | F30, E12 |
| 30 | Erodir 1 px e esfumar 3 px a máscara para reduzir o halo | média | F31 |
| 31 | Letreiro de trás em ouro e nunca branco perto do cabelo | média | F31 (halo visível em fundo claro) |
| 32 | Não refazer o base.mp4; aplicar unsharp 5:5:0,4 testado em 1 quadro | média | F27, P18 |
| 33 | Zoom máximo de 1,10x (A), 1,08x (B) e 1,00x (C) | alta | DR06, techhalla |
| 34 | Não cortar pausas: a economia máxima útil é de 1,1 s e o jump cut fica visível | média | DR03, F01 |
| 35 | Preservar a pausa de 0,60 s (19,50 a 20,10) como quietude | alta | DR05, gdgtify |
| 36 | Banir confete, aplausos, RGB split e tremida herdados do ov2.html | alta | F32, 000267 |
| 37 | Tirar a prova social inventada do ov2.html ("1.287 comentários") | alta | F32 |
| 38 | render(t) sem Math.random; semente fixa na granulação | alta | F32, gdgtify (seek(t) determinístico) |
| 39 | O comp.py tem que falhar alto quando faltar PNG, em vez de pular em silêncio | alta | F33 |
| 40 | Constantes de duração lidas do words.json, não fixas em 54,2 s | alta | F34 |
| 41 | tmix de 3 subquadros só nas janelas de movimento (queda do 474, órbita, carrossel) | média | C8, DR07 |
| 42 | Cronometrar 300 quadros por modelo antes do render cheio | alta | B13 |
| 43 | Pré-passe de 8 stills por modelo para o Bruno aprovar antes do render | alta | techhalla-498547 |
| 44 | Rodar os 3 renders em série, nunca em paralelo | alta | F28 |
| 45 | Opacidade só no elemento pai, nunca no preserve-3d | alta | twoclipping-000267 |
| 46 | A órbita de B dá 1 volta em 2,0 s, sem quique | média | 041659, 000267 (sem easing elástico) |
| 47 | Metade de trás da órbita na camada back, metade da frente na front | alta | F42, cap2.js |
| 48 | Estender a máscara além da borda do quadro (ombro cortado) | média | 041659 |
| 49 | A estrutura de B se apoia em peças anteriores: viga 474, coluna técnica, verga mercado, telhado segundo produto | média | gdgtify |
| 50 | "Hora de cadeira" como bloco sob uma linha de teto: metáfora de teto sem prometer resultado | média | Res. 196/2019 (F72) |
| 51 | A queda da fileira "mesmo diagnóstico" fala de formato de post, não de técnica de colega | média | art. 44 (F73), B21 |
| 52 | C com janela de 1080x1120 sem nova ampliação | média | F4, C9 |
| 53 | O painel de C em JPEG por pipe, mais barato | alta | F26 |
| 54 | Reacts como stickers vetoriais com borda branca, nunca emoji | alta | 551116, CLAUDE.md |
| 55 | Nenhuma cadeira odontológica reconhecível nos ícones | alta | F72 |
| 56 | Ícone de dente só como contorno abstrato e só no C; dá para retirar | baixa | P11 |
| 57 | Os 3 blocos de C como stories do dia 29/10 | média | CLAUDE.md (stories diários) |
| 58 | Stories levam ao reel com "o vídeo completo está no perfil" | baixa | sem dado |
| 59 | A e C viram moldes para consórcio e nutricionista (trocam words.json e textos) | média | 06-plano-final.md (mesma moldura nos 5) |
| 60 | Conferir se a conta tem trial reels antes de decidir A como teste | média | B23 |
| 61 | O Bruno responde cada comentário de dentista em até 2 h nas primeiras 48 h | baixa | PRIOR; o CTA promete "eu te respondo" |
| 62 | Primeira resposta com pergunta de qualificação (técnica, audiência), antes de oferecer diagnóstico | média | 06-plano-final.md D3 |
| 63 | Comentário esperado com 106 de alcance: cerca de 1 | média | E09 (0% a 1,2%) |
| 64 | A meta de 106 é exigente para nicho de saúde: o único precedente deu 63 | média | E10 |
| 65 | O pulo abaixo de 68% é provável com o Bruno em cena (5 de 6 reels de 30/09 a 06/10) | média | buzzfy-leitura |
| 66 | Capa do reel: quadro com "+474 MIL" atrás do Bruno, para a grade | média | F53 |
| 67 | Primeira linha da legenda do post repete o gancho falado | média | 00-SISTEMA módulo de hooks |
| 68 | Legenda do post sem "grátis", preço ou promessa | alta | F73 |
| 69 | Checagem automática de travessão, emoji e nomes nos HTML antes do render | alta | CLAUDE.md |
| 70 | Registrar a rodada em semanas/ com os 3 tempos de render reais | alta | CLAUDE.md, B13 |
| 71 | O formato Tzur v2 não tem leitura na conta; tratá-lo como hipótese, não como padrão | alta | E08 |
| 72 | Publicar o case Tzur antes do dentista daria o primeiro dado do formato A | baixa | E08; depende de autorização (B24) |
| 73 | O dentista que interessa (técnica com demanda de colegas e audiência) é uma fração pequena dos 474 mil | média | 00-SISTEMA (público 20 mil a 500 mil seguidores), F70 (até 34,1% com especialidade) |
| 74 | Um gancho alternativo para o mesmo bruto em teste futuro: "Se você domina uma técnica que os dentistas querem aprender" (13,84 s) como abertura | baixa | 06-plano-final.md hook (a) |
| 75 | Vídeo com 36 s está no intervalo dos vencedores da conta (30 a 45 s) | média | 00-SISTEMA otimização 8 |
| 76 | Mediana de 82,5 s dos virais não vale para conta de 1.618 seguidores | média | F59, F65 contra contas pequenas (F2 #9) |
| 77 | Júri cego: 3 cadeiras veem os 3 MP4 sem rótulo, notam clareza e acabamento de 0 a 10, sem ver o raciocínio | média | B25, everestchris6-399895 |
| 78 | Medir DR20 (voz acima da trilha) em janelas de 400 ms em 100% das janelas faladas | alta | DR20 |
| 79 | Entregar ao Bruno o voz_final em WAV separado, para reuso em corte de stories | média | pedido de áudio masterizado |
| 80 | Se o Bruno reprovar a cadeia_E pelo timbre, a reserva é o voz_master com limitador -1,5 e a legenda "formar quem disputa" assim mesmo | média | E01, E06 |

---

## 7. Pre-mortem da cadeira E (como este plano fracassa)

1. **O gate soa cortado.** O ASR não ouve bombeamento de ruído entre palavras; o Bruno ouve. Sinal precoce: reprovação na escuta cega. Defesa: release de 300 ms ou range de -18 dB e nova medição; a reserva é a ideia 80.
2. **O proxy de ASR engana.** O "formar" pode ter vindo do contexto do modelo de linguagem e não da consoante. Defesa: a escuta do Bruno decide (B02).
3. **A órbita descola da cabeça.** Máscara de 320x320, cabelo e movimento da selfie. Defesa: teste de 300 quadros em 19,5 a 23 s antes do render cheio; se falhar, a órbita vira só metade da frente, um arco sob o queixo.
4. **O B parece "menos After Effects" que o A.** O Bruno pediu efeito e eu priorizei rosto. Defesa: o júri cego e a escolha dele. A está pronto como alternativa.
5. **O nicho, e não a edição, segura o alcance em 60.** E10 sugere isso. Neste caso nenhum modelo passa de 106, e o conselho vai culpar o formato. Defesa: ler alcance com pulo e tempo assistido juntos. Pulo abaixo de 60% com alcance baixo aponta para distribuição de nicho, não para edição.
6. **Ninguém comenta, ou comentam não dentistas.** Com cerca de 1% de comentário (E09), 0 comentários em 7 dias é provável. Defesa: não declarar o formato morto só por isso (D3 do 06-plano: testar a porta).
7. **O render estoura o tempo.** Nenhum render completo foi cronometrado (B13). Defesa: cronometrar 300 quadros e cortar subquadros se passar de 25 min por modelo.
8. **Problema com o CFO.** Um ícone ou a "cadeira" lida como odontológica. Defesa: retirar ícones de dente e de cadeira odontológica, que não custa nada.
9. **Três versões confundem o Bruno.** Ele quer decidir rápido. Defesa: entregar com recomendação única (B) e uma linha por modelo.
10. **Eu descartei o que funciona.** Se o Tzur v2 fiel fosse o que o Bruno tinha em mente, o enxuto frustra. Defesa: a opção 1 de D2 continua a 1 render de distância (custo baixo).

---

## 8. Previsões numéricas com data de conferência

Supondo que o B é publicado em 29/10/2026. Se for outro modelo, valem as mesmas previsões com um desconto de 10% no alcance para o A e de 15% para o C [PRIOR].

| # | Métrica | Valor previsto [faixa] | Fonte de leitura | Conferência |
|---|---|---|---|---|
| P1 | Áudio: 3 de 3 MP4 finais entre -15 e -13 LUFS e TP até -1,0 | sim, probabilidade 0,9 | ffmpeg loudnorm | 23/10/2026 |
| P2 | Bruno escolhe a cadeia_E na escuta cega | probabilidade 0,6 | mensagem do Bruno | 23/10/2026 |
| P3 | Bruno confirma "formar quem disputa" de ouvido | probabilidade 0,85 | mensagem do Bruno | 23/10/2026 |
| P4 | Alcance do reel em 7 dias | 85 [45; 160] | ig_post_stats | 05/11/2026 |
| P5 | Pulo em 7 dias | 58% [48%; 70%] | ig_post_stats | 05/11/2026 |
| P6 | Tempo médio assistido | 11 s [7; 17] | ig_post_stats | 05/11/2026 |
| P7 | Comentários de dentista em 7 dias | 1 [0; 3] | ig_post_stats, PostZen, planilha | 05/11/2026 |
| P8 | D+30: alcance acumulado do reel | 100 [50; 190] | ig_post_stats | 20/11/2026 |
| P9 | D+30: conversas qualificadas de dentista | 1 [0; 3] | planilha manual | 20/11/2026 |
| P10 | D+60: diagnósticos agendados vindos do reel do dentista | 0 [0; 1] | planilha manual | 20/12/2026 |
| P11 | D+60: reels de outros nichos feitos com o molde A, B ou C | 3 [0; 6] | git log de videos/nichos | 20/12/2026 |
| P12 | D+90: mediana de alcance dos reels com o Bruno em cena desde 29/10 | 90 [55; 150] | ig_post_stats, Módulo 7 | 19/01/2027 |
| P13 | D+90: a cadeia de áudio da cadeira E (ou derivada) é o padrão dos reels | probabilidade 0,55 | arquivos de áudio em videos/ | 19/01/2027 |

Todas as faixas são [PRIOR], ancoradas em E09, E10 e F12. Nenhuma tem conta de distribuição, e N = 1.

---

## 9. O que mudaria minha opinião

- O Bruno ouve "forna" no raw: a legenda passa a escrever o que ele ouvir, e o argumento da premissa 2 perde força.
- A escuta cega prefere o voz_master: fica a reserva (ideia 80).
- O teste de 300 quadros mostra a órbita descolando: B perde a órbita, e passo a defender A para publicar.
- Aparece métrica do Tzur v2 publicado (ou de outro reel com letreiro atrás) acima da mediana: A sobe de reserva para principal.
- buzzfy_reel_detail no plano pago mostra que os talking heads de negócio que funcionam usam b-roll pesado: reduzo o peso de "rosto 100%".
- A conta tem trial reels: A vira teste paralelo em vez de arquivo.

## 10. Lacunas

- Não ouvi o áudio. E01 a E05 são proxies de ASR e de nível.
- Não vi os vídeos de referência nem os remakes dos prompts (B10). A técnica vem do texto do prompt, via F1.
- Não rodei render nenhum. Os tempos vêm de F4 (DR08).
- A edição dos 3 reels vencedores da conta é sem dado (não está no repositório).
- O efeito de nicho no alcance: um precedente só (E10).
- Se a soma do CFO conta pessoas ou inscrições (B19). Se o Bruno é inscrito em CRO (B20).
- Especificação de loudness do Instagram (B05).
- Recurso de trial reels na conta (B23).

## 11. Fontes

- Arquivos do projeto: contexto.md; run/00-enquadramento.md; run/01-fatos.md; run/01-pesquisa/F1 a F4; words-raw.json; transcricao-tempos.txt; CLAUDE.md; conteudo/sistema-instagram/00-SISTEMA.md; conteudo/modo-god-nichos/run/06-plano-final.md (seções 2.2, 4 e 5); videos/add_music.sh; videos/cases/tzur/ (lista de arquivos, git log).
- Medições desta cadeira: run/02-cadeiras/evidencias-E/ (trecho_whisper, inteligibilidade, piso_percentil, leve_teste, joelho_teste, gate_teste_E, cadeia_E.sh, cadeia_E_medida, dr02_compara, buzzfy-leitura-2026-10-21.md).
- Buzzfy (somente leitura, 21/10/2026): ig_posts de reels de 20/09 a 21/10/2026; ig_post_stats de 7 reels com comparação à mediana.
- Repositório awesome-opus5-5-videos: ids citados conforme F1 (data/videos.json, commit 92aee2f5). Não reabri os prompts.
- CFO: F3 e evidencias-F3 (Res. 196/2019, Código de Ética 118/2012, CSV de ativos). Não reabri as páginas.
