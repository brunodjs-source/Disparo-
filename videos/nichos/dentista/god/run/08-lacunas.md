# 08 · Lacunas · Passada 1 · 21/10/2026

Arquivo lido: run/06-plano-final.md. Pergunta: o que falta para o Bruno executar amanhã sem voltar a perguntar.

| # | Seção | Lacuna | O que foi escrito |
|---|---|---|---|
| L1 | 7 D1 / itens 1 a 3 | Cadeia de áudio descrita, sem comando executável nem critério de aceite por comando | Seção 9.1: comandos ffmpeg de 2 passadas, ebur128 de aceite, uso do add_music.sh |
| L2 | 2 (coluna Música) | "trilha" sem arquivo escolhido | Seção 9.2: hazy-after-hours nos 3, com lista e durações por ffprobe; zerar 19,50 a 20,10 s |
| L3 | 2.1, 2.2, 2.3 | Intervalos de pausa sem linha nas tabelas quadro a quadro | Seção 9.3: regra de manter o estado anterior, sem SFX e sem legenda |
| L4 | 2 e 6 | Sem pasta, nome e especificação dos arquivos de saída nem ordem de comandos; 4:5 do C sem comando | Seção 9.4 |

Números sem fonte e sem etiqueta que restam no plano (leitura manual): 3. Trilha a -30 LUFS (A01, B01), ducking de 8 dB (A02) e o volume=-12dB das pausas na 9.1. Parâmetros de desenho (px, quadros, zoom) não entram na conta.

# 08 · Lacunas · Passada 2 · 21/10/2026

| # | Seção | Lacuna | O que foi escrito |
|---|---|---|---|
| L5 | 2.1 a 2.3 (coluna SFX) | SFX citados sem arquivo, sem atraso por evento e sem nível | Seção 10.1: pasta nichos/dentista/sfx, durações por ffprobe, tabela de adelay do A, coin.wav proibido |
| L6 | D2 / 9.4 | comp.py preso ao Tzur (N de 54,2 s, base.mov, aplausos, nome de saída) | Seção 10.2: o que trocar e onde copiar |
| L7 | 2 (paleta) | Fontes não instaladas no sistema; caminho não dito | Seção 10.3: caminho do @font-face; sans da legenda como hipótese |
| L8 | 2.2 | Tela dividida sem comando de montagem nem posição do recorte do Bruno | Seção 10.4: comando vstack, Y=400 como hipótese com checagem em still |
| L9 | 2.3 / D3 | Modelo C sem arquivo de partida | Seção 10.5: predio.html a partir de serie2/modelo.html |

Números sem fonte e sem etiqueta que restam no plano (leitura manual): 3, os mesmos da passada 1 (trilha a -30 LUFS, ducking de 8 dB, volume=-12dB). Os números novos desta passada têm fonte ou etiqueta.

# 08 · Lacunas · Passada 3 · 21/10/2026

| # | Seção | Lacuna | O que foi escrito |
|---|---|---|---|
| L1 | 10.2, 10.4 | Plano mandava fazer upscale e máscara sem dizer que base.mp4 (1080x1920, 1093 quadros) e mask.mp4 já existem no scratch | 11.1: caminhos, ffprobe, seg.log; base_A.mp4 = SCR/base.mp4; conferência de alinhamento |
| L2 | 10.2 / D2 | comp.py: P&B fixo até 4,28 s e áudio puxado de base.mov; base.mp4 não tem áudio | 11.2: troca para P&B até 2,08 com rampa de 6 quadros, entrada de áudio = voz_v2 ou mixagem SFX |
| L3 | 2.1 / Modelo A | ov2.html tem letreiros do Tzur no código e cap2.js fixa 54,2 s; não havia edit.json do dentista | 11.3: a/edit.json gerado do words-raw.json (79 palavras, "no Brasil"), lista dos letreiros com tempos, troca para 1093 quadros, stills primeiro |

Números sem fonte e sem etiqueta que restam no plano (leitura manual): 3, os mesmos das passadas 1 e 2 (trilha a -30 LUFS, ducking de 8 dB, volume=-12dB).

# 08 · Lacunas · Passada 4 · 21/10/2026

| # | Seção | Lacuna | O que foi escrito |
|---|---|---|---|
| L1 | 10.4 / 2.2 Modelo B | painel_B.mp4 mandado fazer com serie2/modelo.html, mas a página é 1080x1920 de fundo claro, tem legenda, marca e confete próprios, o capture.js exige voz.wav, e não há tipo de cena para grade de pontos, relógio, planta ou seta; o cards usa ✓ e ✕ vetados | 12.1: b/timeline.json gerado (8 segmentos, só tipos existentes), lista de trocas no painel.html e no capture.js, 1093 quadros sem áudio, reacts como SVG estático, stills de aceite |
| L2 | 4 / D2 | CTA promete resposta e a D2 manda duas perguntas na DM, mas não havia texto da resposta nem da DM | 12.2: respostas públicas, DM com as duas perguntas e colunas da planilha, marcadas como hipótese |

Números sem fonte e sem etiqueta que restam no plano (leitura manual): 3, os mesmos das passadas anteriores (trilha a -30 LUFS, ducking de 8 dB, volume=-12dB). Os números novos desta passada têm fonte ou etiqueta; segundos de still e px de layout são parâmetros de desenho.
