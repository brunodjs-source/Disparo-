# Plano da cadeira H · Forasteiro · Reel do dentista · 21/10/2026

- Persona: leigo inteligente que só conhece o pedido do Bruno e o contexto do cliente (contexto.md, transcrição, words-raw.json, frames-amostra.jpg e medições que eu mesmo rodei nos arquivos do bruto).
- OTIMIZA PARA: clareza e senso comum.
- PONTO CEGO (assumido por escrito): falta de contexto técnico. Não li pesquisas, planos de outras cadeiras, o código do case Tzur, nem os prompts do repositório além do resumo que está no contexto. Compensação: (1) medi eu mesmo o que dava para medir sem instalar nada (ffprobe, loudnorm, envelope RMS em numpy, lista de filtros do ffmpeg), registrado em evidencias-H/medicoes-H.txt; (2) toda afirmação técnica que não medi vai como [PRIOR] e nunca fecha objeção sozinha; (3) onde o meu senso comum bate de frente com a técnica, eu deixo a pergunta aberta em vez de decidir.
- PERGUNTA CONTRÁRIA: o que alguém de fora acharia estranho aqui? Resposta completa na seção 1.1.

Etiquetas: [FATO] com fonte; [ESTIMATIVA] com conta ou premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4.

---

## 1. Veredito (até 12 linhas)

1. Fazer os 3 modelos, mas publicar no feed só um por vez. Os 3 repetem a mesma fala de 36 s; publicar os 3 seguidos é o que um seguidor mais estranharia.
2. Áudio: remasterizar a partir de voz_master.wav, que já está em -14,2 LUFS mas com true peak de -0,5 dBTP e duas pausas com ruído só 31,6 a 33,5 dB abaixo da voz [FATO, medicoes-H.txt]. Não está pronto.
3. Modelo A: gramática Tzur v2, porém sem confete e sem aplausos. Celebrar o número de dentistas do país não faz sentido para quem está de fora: ninguém ganhou nada ali.
4. Modelo B: tela dividida (Bruno em cima, animação da fala embaixo, reacts desenhados). Motivo de senso comum: o Bruno pediu com essas palavras ("dividindo tela com reacts e animações"). Ids: sab8a-475686 mais twoclipping-000267.
5. Modelo C: tipografia que constrói um prédio de palavras atrás do Bruno, do térreo "hora de cadeira" ao "segundo produto". Ids: gdgtify-929495 mais twoclipping-000267. Descarto alex-prompter-997524: pede prova e 3 passos que a fala não tem.
6. O CTA gravado pede "comenta a sua profissão" num vídeo só para dentistas. Na tela, escrever "COMENTE: DENTISTA" para não confundir.
7. Na tela, legenda corrigida só onde o Whisper errou de forma provável ("no Brasil"); o trecho 24,94 a 29,04 s ganha letreiro com a ideia limpa, sem fingir que é legenda literal. Ninguém regrava 4 s isolados.
8. "474 MIL" só aparece grande com rodapé de fonte verificada. Sem fonte anotada até o render, o letreiro diz "DENTISTAS DO BRASIL".
9. Tzur não entra na tela: não foi dito e não há autorização registrada no contexto.
10. Rosto do Bruno de 0 a 3 s nos 3 modelos; rosto visível em 95,7% (A), 100% (B) e 98,9% (C) do tempo [ESTIMATIVA, conta na pergunta 2].

### 1.1 O que alguém de fora acharia estranho (pergunta contrária)

1. Três vídeos com a mesma fala. Se forem ao feed, o seguidor ouve o mesmo discurso três vezes.
2. "Dentista, comenta a sua profissão": se o vídeo é só para dentista, qual profissão ele comentaria além de "dentista"? Parece CTA de outro vídeo reaproveitado.
3. "Eu desenho seu lançamento": eu quem? Em nenhum momento o vídeo diz quem é o Bruno nem o que é um lançamento.
4. Confete e aplausos no número 474 mil (herança do Tzur): o número é tamanho de mercado, não conquista.
5. Um número gigante na tela, para um público que pode conhecer o número oficial da própria profissão, sem dizer de onde veio.
6. Legenda que diz uma coisa e áudio que diz outra ("forna que a gente disputa").
7. "Reacts": se forem clipes de terceiros (memes, famosos reagindo), é imagem de outras pessoas sem autorização.
8. Pessoas reconhecíveis passando no fundo do coworking (visível nos quadros 4 e 5 de frames-amostra.jpg [FATO]). Quem são, autorizaram?
9. O pedido diz "letreiro 4D". 4D não existe em edição de vídeo; interpreto como 3D com profundidade (letra saindo de trás da pessoa). Vale confirmar com o Bruno em uma linha.
10. Medir três estilos com um vídeo publicado (N = 1) e chamar de teste.
11. Um vídeo que fala "você deixa de disputar paciente" logo depois de "eu desenho seu lançamento": a ligação entre ensinar colegas e o serviço do Bruno fica implícita.
12. Selfie de mão tremendo e letreiro parado no espaço: se o fundo mexe e o letreiro não, parece adesivo colado na tela.

---

## 2. Respostas às 14 perguntas

### P1. Qual modelo a cadeira defende e quais ids entram

Defendo os 3, com a ordem de publicação A primeiro, porque é o que o Bruno reconhece como "nosso" e é o mais barato de revisar. Se eu tivesse de escolher um só para publicar, escolheria B, por ser o que o Bruno pediu literalmente e o que deixa o rosto em cena 100% do tempo.

| Modelo | Ids do repositório | Aproveita | Descarta |
|---|---|---|---|
| A | nenhum novo (pipeline do case Tzur v2: ov2.html, cap2.js, comp.py, seg.py [FATO, contexto.md]); toma de twoclipping-000267 só a lista de banidos e o loudnorm | letreiro 3D atrás via rembg, b-roll com respiro de 0,30 s, reacts, bloco final, P&B que vira cor no número | confete e aplausos (o número não é conquista; confete também é "partículas", item banido do twoclipping) |
| B | sab8a-475686 + twoclipping-000267 | sab8a: cortes punchy, legenda, grafismo, música. twoclipping: match cut entre tela cheia e tela dividida, motion blur real por subframes com tmix, SFX alinhado ao pico, loudnorm -14, lista de banidos | do twoclipping, a máscara de tipo (fica para C); do sab8a, qualquer corte que corte fala |
| C | gdgtify-929495 + twoclipping-000267 | gdgtify: palavras que viram arquitetura, seek(t) determinístico, um momento de quietude de 400 ms. twoclipping: máscara de tipo e match cut, SFX no pico, banidos | alex-prompter-997524 inteiro (5 cenas com "3 passos" e "prova": a fala não tem 3 passos e a prova, o Tzur, não foi dita; forçar exigiria texto que o Bruno não falou) |

Resumo dos prompts conforme contexto.md [FATO]; eu não abri os arquivos dos prompts (ponto cego).

### P2. Rosto de 0 a 3 s, porcentagem e zoom

- Sim nos 3 modelos: de 0,00 a 3,00 s (quadros 0 a 90) o Bruno está em tela cheia falando "Dentistas, são mais de 474 mil".
- Porcentagem [ESTIMATIVA, conta sobre 36,43 s = 1093 quadros, FATO ffprobe base.mp4]:
  - A: rosto some só no b-roll de 10,54 a 12,10 s (47 quadros). 1046/1093 = 95,7%.
  - B: rosto sempre visível (tela cheia ou metade de cima). 100%.
  - C: rosto parcial dentro das letras de 20,64 a 21,04 s (12 quadros). 1081/1093 = 98,9% com rosto inteiro, 100% com rosto pelo menos parcial.
- Zoom máximo: 1,18x em A e C (no "Qual é?"), 1,15x em B. Teto de 1,25x respeitado.
- Conta de nitidez: o bruto é 576x1024 e vira 1080x1920, fator 1,875. Com zoom de 1,18x o fator efetivo sobre o pixel original é 2,21x; no teto de 1,25x seria 2,34x [ESTIMATIVA, aritmética].
- Na tela dividida (B), a metade de cima é 1080x960. Recortando 576x512 do bruto em volta do rosto e ampliando 1,875x, o rosto fica do mesmo tamanho que na tela cheia: zoom 1,0x relativo ao bruto ampliado [ESTIMATIVA, aritmética]. Posição do rosto no bruto, medida a olho em frames-amostra.jpg (cada quadro 270x480 representa 576x1024): topo da cabeça entre y 235 e 300, queixo perto de y 736 [ESTIMATIVA]. O recorte de 512 de altura fica justo; o topo do cabelo pode ser cortado nos quadros em que o Bruno sobe o celular. Mitigação: recorte que acompanha a caixa do rosto tirada de mask.mp4.

### P3. Listas de edição quadro a quadro

Regras comuns aos 3 modelos:
- 30 fps de saída. O bruto tem 1093 quadros com média de 29,99 fps (avg_frame_rate 655800/21869) [FATO, ffprobe]. O "31,6 fps" do contexto é a taxa máxima (r_frame_rate 600/19), não a média. Portanto 1 quadro do bruto = 1 quadro da saída, sem descartar quadro.
- Linha do tempo sem cortes: a duração final é 36,43 s e os tempos batem 1:1 com words-raw.json. Isso evita cortar sílaba e mantém as listas alinhadas à transcrição. Corte de respiro fica como variação opcional (ideia 41).
- Quadro = arredondamento de segundos x 30.
- Zonas seguras [PRIOR]: interface do Instagram cobre por volta de 0 a 220 px no topo, de 1500 a 1920 px embaixo e 120 px à direita.
- Rosto na tela cheia 1080x1920 [ESTIMATIVA, frames-amostra x4]: topo da cabeça y 440 a 600, olhos y 860 a 940, boca y 1120 a 1200, queixo y 1380. Faixa livre para letreiro atrás: y 220 a 560. Legenda: y 1400 a 1490.
- Camadas: "atrás" = entre o fundo e a silhueta do Bruno (máscara rembg); "frente" = sobre tudo; "tela cheia" = vídeo do Bruno ocupando 1080x1920; "tela dividida" = Bruno em 1080x960 em cima e painel animado em 1080x960 embaixo.
- Reacts = reações gráficas desenhadas em SVG (balão de pergunta, carimbo, sublinhado, seta, marca de checagem). Sem emoji, sem clipe de terceiros.
- Nenhum item banido do twoclipping: sem shockwave, partículas, confete, RGB split, camera shake, lens flare, neon.

#### Modelo A · Tzur v2 adaptado

| # | Início s (q) | Fim s (q) | Palavra gatilho | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|---|
| A1 | 0,00 (0) | 2,08 (62) | Dentistas | tela cheia P&B + frente legenda | DENTISTAS | push-in lento 1,00 para 1,06; legenda cap2.js palavra a palavra | grave curto em q3 |
| A2 | 2,08 (62) | 3,80 (114) | 474 / mil | atrás | 474 MIL (ou DENTISTAS DO BRASIL se sem fonte) | P&B vira cor em 8 quadros a partir de q62; letreiro 3D Three.js sobe de trás da cabeça em 10 quadros; contador rola de 0 a 474 entre q62 e q82 | impacto em q62; tique de contador q62 a q82 |
| A3 | 2,08 (62) | 5,16 (155) | 474 | frente, canto superior esquerdo, 26 px | Fonte: CFO, out/2026 (só se verificado) | fade 6 quadros | nenhum |
| A4 | 3,80 (114) | 5,16 (155) | colegas, ativos, em, Brasil | frente legenda | COLEGAS ATIVOS NO BRASIL | legenda palavra a palavra; letreiro 474 MIL fica atrás, assentado | nenhum |
| A5 | 5,16 (155) | 5,48 (164) | respiro | tela cheia | (sem texto) | letreiro afunda atrás do ombro em 8 quadros | nenhum |
| A6 | 5,48 (164) | 7,68 (230) | porque | tela cheia + legenda | POR QUE VOCÊ AINDA SÓ VENDE | punch-in 1,00 para 1,12 em 4 quadros em q164 | whoosh leve com pico em q164 |
| A7 | 7,68 (230) | 8,80 (264) | hora | atrás | HORA DE CADEIRA | letreiro 3D sobe de trás em 10 quadros; ícone de relógio de linha ao lado | dois tiques de relógio, q230 e q249 |
| A8 | 8,80 (264) | 10,54 (316) | quase | tela cheia + legenda | QUASE TODO PERFIL POSTA | zoom volta a 1,05; letreiro desce | nenhum |
| A9 | 10,54 (316) | 12,10 (363) | perfil, posta, mesmo, diagnóstico | b-roll tela cheia (motion HTML) | MESMO DIAGNÓSTICO | grade 3x3 de cartões de post genéricos idênticos (blocos cinza com a palavra DIAGNÓSTICO, sem dente, sem boca), entrada em cascata de 2 quadros; entra 0,30 s depois de "perfil" e sai em q363 | cliques secos a cada cartão, baixo |
| A10 | 12,10 (363) | 13,32 (400) | mesma, conclusão | tela cheia + react frente | MESMA CONCLUSÃO | volta ao Bruno; react: carimbo IGUAL entra em q380 a 30 graus sobre o ombro esquerdo, fora do rosto | carimbo em q380 |
| A11 | 13,84 (415) | 17,92 (538) | Se, técnica, aprender | tela cheia + legenda | SE VOCÊ DOMINA UMA TÉCNICA... | em q452 rótulo SUA TÉCNICA no canto superior; em q515 react sublinhado sob "APRENDER" | traço de caneta em q515 |
| A12 | 17,92 (538) | 19,50 (585) | existe, mercado | atrás | EXISTE UM MERCADO | letreiro 3D sobe de trás em 10 quadros | impacto médio q574 |
| A13 | 19,50 (585) | 20,64 (619) | Qual, é | tela cheia | QUAL É? (legenda) | quietude: trilha a zero de q588 a q600 (400 ms); zoom lento 1,12 para 1,18 | nenhum (o silêncio é o efeito) |
| A14 | 20,64 (619) | 22,22 (667) | ensinar, colega | atrás | ENSINAR O SEU COLEGA | maior letreiro do vídeo, 2 linhas, sobe de trás em 8 quadros com sombra projetada na parede | impacto forte q619 com pico alinhado |
| A15 | 22,70 (681) | 24,24 (727) | Eu, desenho, lançamento | frente terço inferior esquerdo (y 1250) | Bruno · Estrategista de Lançamento | linha desenha o retângulo do nome em 12 quadros | lápis riscando q685 a q706 |
| A16 | 24,46 (734) | 26,20 (786) | você, deixa, disputar | frente, faixa alta (y 260 a 420) | DE DISPUTAR PACIENTE | texto entra em q748; risco atravessa em q786 | traço de marcador q786 |
| A17 | 26,38 (791) | 29,04 (871) | paciente, forna, disputa | frente, faixa alta | PARA FORMAR QUEM DISPUTA | texto novo entra em q827, o riscado sai | whoosh curto q827 |
| A18 | 29,28 (878) | 31,58 (947) | técnica, segundo, produto | atrás | SEGUNDO PRODUTO | letreiro 3D sobe de trás; react carimbo "2" em q923 | impacto q923 |
| A19 | 31,58 (947) | 32,00 (960) | respiro | tela cheia | (sem texto) | barras pretas de 120 px entram em cima e embaixo (bloco cinematográfico, sem cobrir rosto) | ar grave crescendo |
| A20 | 32,00 (960) | 35,92 (1078) | Dentista, comenta, aqui | frente, y 1400 a 1490 | COMENTE: DENTISTA | caixa de comentário desenhada, cursor digita "dentista" 1 letra a cada 2 quadros a partir de q980; botão enviar pisca em q1032 ("aqui") | teclado baixo q980 a q1000; pop q1032 |
| A21 | 35,92 (1078) | 36,43 (1093) | fim | frente | @o_estrategista.com.br | fade da trilha 15 quadros | cauda |

Legenda cap2.js ativa em todo trecho sem letreiro de frente, na faixa y 1400 a 1490.

#### Modelo B · Tela dividida com reacts (sab8a + twoclipping)

| # | Início s (q) | Fim s (q) | Palavra gatilho | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|---|
| B1 | 0,00 (0) | 2,08 (62) | Dentistas | tela cheia + legenda | DENTISTAS | punch-in 1,00 para 1,08 em q0 | grave curto q3 |
| B2 | 2,08 (62) | 5,16 (155) | 474, mil | tela cheia + frente faixa alta | 474 MIL / COLEGAS ATIVOS NO BRASIL + rodapé fonte (ou DENTISTAS DO BRASIL) | contador de dígitos rolando q62 a q82; sem rembg | tique de contador |
| B3 | 5,48 (164) | 5,75 (172) | porque | transição | (sem texto) | match cut: o Bruno sobe para a metade de cima em 8 quadros com motion blur por subframes (tmix); painel de baixo entra de baixo | whoosh com pico em q164 |
| B4 | 5,75 (172) | 8,80 (264) | vende, hora, cadeira | tela dividida | painel: agenda de horários 08h a 18h se enchendo; rótulo HORA DE CADEIRA em q230 | blocos da agenda preenchem 1 a cada 3 quadros; relógio gira | tiques de relógio |
| B5 | 8,80 (264) | 13,32 (400) | perfil, diagnóstico, conclusão | tela dividida | painel: grade 3x3 de posts genéricos iguais; MESMO DIAGNÓSTICO; react carimbo REPETIDO em q380 | cascata de cartões a cada 2 quadros a partir de q307 | cliques; carimbo q380 |
| B6 | 13,84 (415) | 17,92 (538) | técnica, dentistas, aprender | tela dividida | painel: um cartão dourado SUA TÉCNICA com setas para pictogramas de pessoas rotulados COLEGAS | setas desenham em 10 quadros a partir de q452; pictogramas aparecem em q481 | traço q452 |
| B7 | 17,92 (538) | 19,50 (585) | existe, mercado | tela dividida | painel: pictogramas se multiplicam em grade; MERCADO | multiplicação em 3 ondas, q538, q556, q574 | impacto médio q574 |
| B8 | 19,50 (585) | 20,64 (619) | Qual, é | tela dividida | painel preto; depois "?" grande em q603 | quietude: painel preto e trilha a zero de q588 a q600 | nenhum |
| B9 | 20,64 (619) | 22,22 (667) | ensinar, colega | tela cheia (match cut de volta) + frente sobre o peito (y 1300 a 1480) | ENSINAR O SEU COLEGA | painel some para baixo em 6 quadros; texto cinético 3 batidas: ENSINAR (q619), O SEU (q646), COLEGA (q655) | impacto forte q619 |
| B10 | 22,70 (681) | 24,24 (727) | Eu, desenho, lançamento | tela dividida + terço inferior na emenda | painel: planta azul (blueprint) traça uma linha do tempo de lançamento; nome Bruno · Estrategista de Lançamento | traço por stroke-dashoffset em 30 quadros | lápis |
| B11 | 24,46 (734) | 29,04 (871) | deixa, disputar, paciente, forna, disputa | tela dividida | painel: DISPUTAR PACIENTE (riscado em q786) e seta para FORMAR QUEM DISPUTA (q827) | seta cresce da esquerda para a direita em 10 quadros | marcador q786; whoosh q827 |
| B12 | 29,28 (878) | 31,58 (947) | técnica, segundo, produto | tela dividida | painel: dois cartões lado a lado, 1 ATENDIMENTO e 2 SUA TÉCNICA; react marca de checagem em q935 | segundo cartão vira de costas para frente em 8 quadros a partir de q923 | impacto q923 |
| B13 | 31,58 (947) | 32,00 (960) | respiro | transição | (sem texto) | painel troca para o CTA | ar grave |
| B14 | 32,00 (960) | 35,92 (1078) | Dentista, comenta, aqui | tela dividida | painel: caixa de comentário desenhada digitando "dentista"; título COMENTE: DENTISTA | digitação 1 letra a cada 2 quadros a partir de q980; seta para baixo pulsa 2 vezes | teclado; pop q1032 |
| B15 | 35,92 (1078) | 36,43 (1093) | fim | tela cheia | @o_estrategista.com.br | Bruno volta a tela cheia em 6 quadros | cauda |

Legenda na emenda entre as metades (y 930 a 990) durante toda a tela dividida; na tela cheia, faixa y 1400 a 1490.

#### Modelo C · Prédio de palavras (gdgtify + twoclipping)

Paleta preto e ouro da série 2 (#141210, #E8B36A, Cinzel + Playfair itálico) [FATO, contexto.md]. Fundo do vídeo escurecido 35% e dessaturado 50% atrás do Bruno para a tipografia ler [HIPÓTESE].

| # | Início s (q) | Fim s (q) | Palavra gatilho | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|---|
| C1 | 0,00 (0) | 2,08 (62) | Dentistas | atrás | DENTISTAS | viga horizontal de letras se monta da esquerda, 1 letra a cada 2 quadros (9 letras, q0 a q18) | tique seco por letra, baixo |
| C2 | 2,08 (62) | 3,80 (114) | 474, mil | atrás | 474 / MIL | "4", "7", "4" sobem como pilares de trás dos ombros (q62, q70, q78); MIL desce como verga sobre eles em q95 | baque grave q62 e q95 |
| C3 | 3,80 (114) | 5,16 (155) | colegas, Brasil | atrás + frente rodapé | COLEGAS ATIVOS NO BRASIL gravado na verga; rodapé fonte (ou troca para DENTISTAS DO BRASIL) | gravação por máscara em 12 quadros | nenhum |
| C4 | 5,48 (164) | 8,80 (264) | vende, hora, cadeira | atrás | HORA DE CADEIRA | pilares descem; laje única HORA DE CADEIRA assenta na linha dos ombros em q230 | baque q230 |
| C5 | 8,80 (264) | 13,32 (400) | perfil, mesmo, diagnóstico | atrás | MESMO repetido como tijolos de uma parede | parede se preenche de q307 a q363; todos os tijolos viram cinza em q380 (react tipográfico) | cliques por fileira |
| C6 | 13,84 (415) | 17,92 (538) | técnica, aprender | atrás | SUA TÉCNICA | bloco dourado entra como pedra angular sobre a laje em q452 | baque metálico q452 |
| C7 | 17,92 (538) | 19,50 (585) | existe, mercado | atrás | MERCADO | câmera virtual da camada de tipo recua; aparece o contorno de um prédio em linhas; o vídeo do Bruno não recebe zoom | ar subindo |
| C8 | 19,50 (585) | 20,10 (603) | pausa | tudo | (tipo a 30% de opacidade) | quietude gdgtify: tudo para de q588 a q600 (400 ms) | trilha a zero |
| C9 | 20,10 (603) | 20,64 (619) | Qual, é | frente topo (y 240 a 360) | QUAL É? | fino, surge em 4 quadros | nenhum |
| C10 | 20,64 (619) | 21,04 (631) | ensinar | frente tela cheia (máscara de tipo) | ENSINAR | palavra ocupa a tela; o vídeo do Bruno aparece só dentro das letras (12 quadros) | whoosh com pico em q631 |
| C11 | 21,04 (631) | 22,22 (667) | o seu colega | atrás | O SEU COLEGA | letras de ENSINAR crescem 1 para 6 até sumir (match cut de volta ao vídeo inteiro, motion blur por tmix); O SEU COLEGA vira o segundo andar | baque q646 |
| C12 | 22,70 (681) | 24,24 (727) | Eu, desenho, lançamento | atrás + frente terço inferior | contorno do prédio em linha de planta; Bruno · Estrategista de Lançamento | stroke-dashoffset 30 quadros | lápis |
| C13 | 24,46 (734) | 29,04 (871) | deixa, disputar, forna, disputa | atrás | DISPUTAR PACIENTE sai (q786) e FORMAR QUEM DISPUTA entra (q827) | vigas deslizam lateralmente em 10 quadros | arrasto q786; encaixe q827 |
| C14 | 29,28 (878) | 31,58 (947) | segundo, produto | atrás | SEGUNDO PRODUTO | segundo andar se completa e acende em ouro em q923 | impacto q923 |
| C15 | 32,00 (960) | 35,92 (1078) | Dentista, comenta, aqui | frente, y 1400 a 1490 | COMENTE: DENTISTA | letras se montam 1 a cada 2 quadros a partir de q980; sublinhado em q1032 | pop q1032 |
| C16 | 35,92 (1078) | 36,43 (1093) | fim | frente | @o_estrategista.com.br | prédio escurece | cauda |

Sem legenda palavra a palavra em C (a própria tipografia carrega as palavras-chave) [HIPÓTESE: perde clareza para quem vê sem som; ver ideia 33].

### P4. Trecho 24,94 a 29,04 s ("forna que a gente disputa")

- [FATO, words-raw.json]: o Whisper registrou "você deixa disputar, paciente passa a forna que a gente disputa", com "gente" durando 0,04 s (28,24 a 28,28) e "técnica" seguinte com 0,20 s. Durações assim indicam que o Whisper está inseguro nesse trecho [PRIOR].
- O texto pretendido, segundo o contexto, é "Você deixa de disputar paciente e passa a formar quem disputa" [FATO, contexto.md].
- Posição: (1) alguém escuta o trecho no fone, 3 vezes, e anota o que de fato foi dito; (2) se soar como "formar quem disputa", legenda corrigida; (3) se soar como "a gente disputa", a legenda fica fiel no rodapé e a ideia limpa vai no letreiro (DE DISPUTAR PACIENTE riscado, PARA FORMAR QUEM DISPUTA), que é texto de apoio e não transcrição. Regravar só 4 s é pior: luz, enquadramento e cabelo mudam e o corte denuncia. Se for regravar, regrava os 36 s inteiros (custo para o Bruno em torno de 2 minutos [ESTIMATIVA]), e isso vira um quarto vídeo, sem atrasar os 3.
- Essa construção "deixa de X e passa a Y" conta como a única frase de contraste permitida por peça.

### P5. "em Brasil" (4,80 a 5,16 s)

Legenda corrigida para "NO BRASIL". "Em" dura 0,16 s [FATO, words-raw.json]; "no" e "em" curtos se confundem no reconhecimento [PRIOR]. Ninguém fala "em Brasil" em português do Brasil; se ele falou, a legenda corrigida não muda o sentido e o espectador não vai estranhar. Conferir no fone junto com o trecho da P4.

### P6. 474 mil na tela

- Não verifiquei a fonte (cadeira forasteira não lê a pesquisa). O contexto exige fonte CFO ou texto genérico [FATO, contexto.md].
- Regra: se até o render alguém anotar valor, data e URL do CFO em run/01-fatos.md e o valor arredondado bater com 474 mil, o letreiro mostra 474 MIL com rodapé "Fonte: CFO, out/2026" em 26 px no canto superior esquerdo. Se o número oficial for diferente, mostrar o oficial e não o falado gera conflito com o áudio: nesse caso, letreiro DENTISTAS DO BRASIL e legenda fiel ao áudio.
- O rodapé precisa dizer o que é contado ("inscritos ativos") se for esse o recorte da fonte [HIPÓTESE].

### P7. Áudio

Cadeia proposta, a partir de voz_master.wav (48 kHz mono [FATO, medicoes-H.txt]):
1. Escuta cega no celular (alto-falante e fone) de raw, rn_std, rn_sh, rn_bd e voz_master, 5 s cada, no trecho 24 a 29 s. Medição não diz se a voz soa robótica; ouvido diz [PRIOR].
2. highpass=f=80.
3. agate (expansor) só para baixar as pausas: alvo de chão de ruído pelo menos 40 dB abaixo da mediana da voz. Hoje as pausas 24,24 e 31,58 estão a 33,5 e 31,6 dB [FATO, medicoes-H.txt]. Ataque curto, release de 150 ms para não comer fim de palavra [PRIOR].
4. equalizer f=3500 g=+2 (presença), deesser.
5. Trilha: lounge sintetizada em numpy (som.py da série 2) [FATO, contexto.md], integrada em torno de -26 LUFS antes do ducking; sidechaincompress com a voz como chave (razão 8, ataque 5 ms, release 250 ms) para ficar de 15 a 20 LU abaixo da voz nos trechos falados [PRIOR]. Na quietude de 19,60 a 20,00 s, trilha a zero.
6. SFX com pico até -6 dBFS antes do limitador, alinhados pelo pico ao quadro da lista.
7. Mix final: loudnorm em duas passadas, I=-14, TP=-1.5, LRA=7, linear=true. Motivo do -1,5: a codificação AAC costuma subir o pico real alguns décimos de dB [PRIOR]; com -1,5 sobra margem para fechar até -1,0 no arquivo final.
8. AAC 192 kbps 48 kHz.
9. Medição no MP4 final de cada modelo: ffmpeg -i final.mp4 -af ebur128=peak=true e loudnorm print_format=summary; mais o envelope RMS das 7 pausas (script de medicoes-H.txt). Aprovação: -15 a -13 LUFS, TP até -1,0 dBTP, pausas 40 dB abaixo da voz, voz acima da trilha em todo trecho falado.
10. Observação de leigo: voz_master tem LRA de 1,6 LU [FATO]; isso é voz muito achatada. Se na escuta parecer cansativa, aliviar a compressão antes do loudnorm [HIPÓTESE].

### P8. Upscale 576x1024 para 1080x1920

- Já existe base.mp4 em 1080x1920, 30 fps, 1093 quadros [FATO, ffprobe]. Não sei o método usado (lacuna). Também existe tr.trf, arquivo do vidstabdetect [FATO, arquivo presente], o que sugere estabilização já calculada.
- Método proposto: scale com lanczos e unsharp leve (5:5:0,6) [PRIOR], estabilização vidstab com suavização moderada para o letreiro não parecer adesivo (ideia 12).
- Risco no recorte: mask.mp4 está em 360x640 [FATO, ffprobe]. Ampliar a máscara 3x para 1080x1920 cria serrilhado e halo no cabelo. Rodar o rembg de novo em 576x1024 ajuda pouco se o modelo trabalha internamente em resolução baixa [PRIOR: u2net costuma usar entrada de 320x320]. Mitigação: amaciar a borda (erodir 2 px e desfocar 3 px), usar letreiro de cor escura ou com sombra perto da cabeça, e testar alpha matting (pymatting está instalado no cbenv [FATO]) em 30 quadros antes de rodar tudo.
- Risco no rosto: fator 1,875 mais zoom de 1,18 = 2,21x sobre o pixel original; pele pode ficar lisa demais com unsharp forte [PRIOR].

### P9. Pipeline e tempo

- Ferramentas presentes, conferidas sem instalar [FATO, medicoes-H.txt]: ffmpeg com todos os filtros citados, rembg + pymatting + onnxruntime no cbenv do scratchpad, Playwright em /opt/node-tools, node 22, faster_whisper no scratchpad. cv2 ausente: nada de OpenCV.
- Tempo medido: rembg levou 589,4 s para 1093 quadros, 0,54 s por quadro [FATO, seg.log]. A máscara já existe, então A e C podem reaproveitá-la.
- Tempo de render no Playwright: sem dado. Conta para orientar: 1093 quadros x t por quadro. Se t = 0,3 s, cerca de 5,5 min por modelo; se t = 1,0 s, cerca de 18 min [ESTIMATIVA, t é premissa]. Motion blur por subframes multiplica isso pelo número de subframes (4x vira 22 a 73 min) [ESTIMATIVA]; por isso aplicar só nos quadros de transição.
- Medir o primeiro render e registrar em evidências antes de prometer prazo.

### P10. CTA

- Usar o gravado: "Dentista, comenta a sua profissão aqui que eu te respondo" (32,00 a 35,92 s) [FATO, words-raw.json].
- Texto na tela: COMENTE: DENTISTA. Senso comum: "sua profissão" num vídeo para dentista confunde; a palavra na tela tira a dúvida e casa com a fala ("Dentista, comenta").
- TABULEIRO não entra: a regra do CLAUDE.md permite a palavra-chave só em post com alcance de 150 ou mais [FATO, CLAUDE.md], e este ainda não tem alcance.
- Lacuna: não sei se existe automação de comentário para "dentista". Se não existir, "eu te respondo" é manual e o Bruno precisa de tempo reservado para responder no dia.

### P11. Publicidade odontológica

- O vídeo fala com dentistas sobre negócio, quem anuncia é o Bruno. Mesmo assim, por cautela: nenhuma imagem de boca, dente, procedimento, antes e depois, preço ou promessa de resultado nas três listas. Os grafismos usam cartões genéricos, agenda, pictogramas e tipografia.
- "Ensinar o seu colega" e "segundo produto" não prometem número. Não escrever valores de faturamento, nem "fature X".
- Lacuna: não li a Resolução CFO 196/2019 no texto oficial. Antes de publicar, alguém lê o texto oficial e confirma que nada na peça conflita, inclusive se o dentista que vende curso a colegas tem regra própria.

### P12. Tzur

Não entra na tela em nenhum dos 3. Motivos: (1) não foi dito [FATO, contexto.md]; texto de prova sem fala parece colagem; (2) não há registro de autorização para usar nome ou resultado do Tzur em peça para dentistas no material que li. Se houver autorização escrita, a prova vai na legenda do post ou num próximo reel em que o Bruno diga o case.

### P13. Métrica, fonte, data e critério de parar

- Fonte: Buzzfy ig_post_stats (alcance, taxa de pulo, comentários, salvamentos) e PostZen listCommentAutomationLogs, se houver automação [FATO, CLAUDE.md].
- Data: se A for publicado em 29/10/2026, leitura em D+1 (30/10), D+3 (01/11) e D+7 (05/11/2026).
- Sucesso: alcance de 106 ou mais e pulo abaixo de 68% em 7 dias (medianas da conta, segundo o enquadramento; não conferi esses números).
- Parar: em D+3, alcance abaixo de 53 (metade da mediana) e pulo acima de 75% [HIPÓTESE de corte] = não publicar B nem C no feed com esta mesma fala; B e C viram material para stories ou para teste fora do feed.
- Métrica que o leigo olharia primeiro: quantos dentistas comentaram "dentista". Sem esse número, alcance alto pode ser só gente que não é dentista.

### P14. Regras de texto

Todas as telas acima: português do Brasil, sem travessão, sem emoji, uma única frase de contraste por peça (DE DISPUTAR PACIENTE / PARA FORMAR QUEM DISPUTA), sem citar os três nomes vetados no CLAUDE.md. O separador do terço inferior é ponto médio (·), não travessão. Verificação final: grep pelos caracteres de travessão (U+2014 e U+2013) e pelos três nomes vetados nos HTML e nas legendas antes do render.

---

## 3. Decisões

### D1. Como entregar o áudio masterizado

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| a. voz_master como está | zero trabalho | true peak -0,5 dBTP fica fora do alvo e pausas com 31,6 dB; ao somar trilha, pico sobe; risco de pedido de refazer |
| b. Remasterizar de voz_master (minha posição) | pico e pausas corrigidos em minutos | se o ruído de fundo já virou artefato na voz, a remasterização não conserta |
| c. Refazer do raw comparando rn_std, rn_sh, rn_bd | melhor chance de voz natural | dobra o tempo; o bruto tem relação voz/ruído de 8 a 12 dB [FATO, medicoes-H.txt], então qualquer cadeia vai precisar de redução forte |
| d. Regravar só 24,94 a 29,04 | resolve a fala truncada | emenda visível e audível; não resolve ruído do resto |
| e. Fora do óbvio: escuta cega de 2 minutos com o Bruno antes de qualquer cadeia | decide pelo ouvido de quem aprova | evita retrabalho se ele já odiar o timbre do voz_master |

Premissas: o Bruno aprova pelo ouvido no celular, não pelo medidor; voz_master não tem artefato audível [HIPÓTESE].
Posição: b, precedida de e. Se a escuta reprovar voz_master, c.
Probabilidade de sucesso pelo critério (3 de 3 arquivos no alvo e zero pedido de refazer): 0,60, faixa [0,45; 0,75]. A parte técnica (LUFS e pico) é quase certa [PRIOR 0,95]; o que pesa é o "zero pedido de refazer" e as pausas a 40 dB sem cortar respiração.
Confiança: 0,5.

### D2. Modelo A

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| a. Tzur v2 fiel com confete e aplausos | igual ao que o Bruno conhece | celebra um número que não é conquista; confete é partícula banida no twoclipping; parece reaproveitado |
| b. Tzur v2 enxuto, letreiro em 4 momentos | limpo | pode parecer pobre perto do Tzur v2 |
| c. Fiel + legenda palavra a palavra | mais clareza sem som | tela cheia demais com letreiro, legenda e reacts |
| d. Fora do óbvio (minha posição): gramática Tzur v2 (P&B que vira cor, letreiro 3D atrás, b-roll, reacts, bloco final) sem confete e aplausos, com contador, legenda cap2.js só onde não há texto de frente, letreiro em 6 momentos | mantém a identidade e corrige o que não faz sentido | se o Bruno associar confete à "nossa marca", ele pode pedir de volta |

Premissas: rosto de 0 a 3 s e Bruno falando mantêm o padrão medido de 2,4x a 5,8x a mediana [FATO, CLAUDE.md]; o gancho "Dentistas" filtra quem não é dentista, o que pode subir o pulo [HIPÓTESE].
Efeito de 2ª ordem principal: se o pulo subir por causa do filtro, o número "ruim" pode ser o certo para conversão. Ler comentários junto.
Probabilidade de sucesso (produção ok e, se publicado, alcance de 106 ou mais e pulo abaixo de 68%): 0,45, faixa [0,30; 0,65]. Produção sozinha: 0,85.
Confiança: 0,35.

### D3. Modelos B e C

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| a. B = talking head punchy + tipografia arquitetônica; C = explainer 5 cenas | dois estilos diferentes | C força "3 passos" e "prova" que a fala não tem; vira texto inventado |
| b. B = tela dividida; C = tipografia arquitetônica (minha posição) | atende o pedido literal ("dividindo tela") e entrega um estilo que nenhum outro modelo tem | tela dividida reduz o rosto pela metade; pode parecer "vídeo de corte" se o painel for fraco |
| c. Só B agora, C depois do resultado | economiza render | descumpre o pedido de 3 modelos |
| d. Não fazer B e C | menor custo | descumpre o pedido |
| e. Fora do óbvio: B e C feitos, mas só A vai ao feed; B e C vão para stories ou teste fora do feed | evita repetição para o seguidor | comparação entre modelos fica sem dado de feed |

Premissas: o Bruno quis dizer "tela dividida" com "dividindo dela" [HIPÓTESE forte pelo contexto da frase]; tipografia sobre fundo escurecido lê no celular [HIPÓTESE].
Posição: b para a forma, e para a publicação.
Probabilidade de sucesso pelo critério (nota de júri cego igual ou maior que A nas duas e, se uma for publicada, alcance de 106 ou mais e pulo abaixo de 68%): 0,40, faixa [0,25; 0,60].
Confiança: 0,30 (N = 1, júri de 3 cadeiras que já conhecem o pipeline A).

---

## 4. Ideias e hipóteses numeradas

1. Publicar só um modelo no feed por vez. Confiança alta. Evidência: os 3 usam o mesmo bruto e a mesma fala [FATO, contexto.md].
2. Trocar confete e aplausos do A por contador rolando. Alta. Evidência: 474 mil é tamanho de mercado, não conquista [FATO, transcrição]; confete é partícula, banida no twoclipping [FATO, contexto.md].
3. Na tela, COMENTE: DENTISTA. Alta. Evidência: CTA gravado diz "sua profissão" num vídeo para dentista [FATO, words-raw.json].
4. Terço inferior "Bruno · Estrategista de Lançamento" em "Eu desenho seu lançamento". Alta. Evidência: a fala não diz quem é o "eu" [FATO, transcrição].
5. B em tela dividida porque o Bruno escreveu "dividindo tela com reacts e animações". Alta. Evidência: pedido literal no contexto.md.
6. Descartar alex-prompter-997524. Média. Evidência: pede 3 passos e prova; a fala não tem e o Tzur não foi dito [FATO, contexto.md].
7. Linha do tempo sem cortes, 36,43 s, alinhada 1:1 com words-raw.json. Média. Evidência: 1093 quadros a 29,99 fps médios [FATO, ffprobe]; proibido cortar fala.
8. Saída a 30 fps sem reamostragem pesada. Alta. Evidência: avg_frame_rate 29,99 [FATO, ffprobe]; o "31,6 fps" é taxa máxima.
9. Legenda "NO BRASIL" corrigida. Média. Evidência: "em" com 0,16 s [FATO]; confusão "no/em" é comum no reconhecimento [PRIOR].
10. Escutar 24 a 29 s no fone antes de decidir a legenda. Alta. Evidência: "gente" com 0,04 s [FATO, words-raw.json].
11. Regravar só 4 s é pior que não regravar. Média. Evidência: selfie de mão, luz e enquadramento mudam [PRIOR].
12. Estabilizar com vidstab antes de pôr letreiro atrás. Média. Evidência: selfie de mão [FATO, contexto.md]; tr.trf já existe [FATO].
13. O letreiro atrás também esconde pessoas que passam no fundo. Média. Evidência: pessoas visíveis nos quadros 4 e 5 [FATO, frames-amostra.jpg].
14. Desfocar levemente o fundo (não o Bruno) em B e C. Baixa. Evidência: fundo movimentado de coworking [FATO, contexto.md]; ganho de leitura [HIPÓTESE].
15. Usar mask.mp4 existente em vez de rodar rembg de novo. Média. Evidência: rembg custou 589,4 s [FATO, seg.log].
16. Testar pymatting em 30 quadros antes de decidir refazer a máscara. Média. Evidência: máscara em 360x640 [FATO]; pymatting instalado [FATO].
17. Letreiro escuro ou com sombra junto ao cabelo para esconder halo. Média. Evidência: máscara ampliada 3x [ESTIMATIVA]; halo em borda ampliada [PRIOR].
18. Remasterizar de voz_master, não refazer do zero. Média. Evidência: já está em -14,2 LUFS [FATO].
19. Limitar a -1,5 dBTP antes do AAC. Média. Evidência: AAC sobe pico real [PRIOR].
20. Expansor nas pausas 24,24 e 31,58. Média. Evidência: 33,5 e 31,6 dB abaixo da voz [FATO, medicoes-H.txt].
21. Aliviar compressão se a voz cansar. Baixa. Evidência: LRA 1,6 LU [FATO]; efeito no ouvido [HIPÓTESE].
22. Escuta cega das 5 versões de voz com o Bruno. Alta. Evidência: aprovação é dele [FATO, enquadramento D1].
23. O bruto é muito ruidoso: relação voz/ruído de 8 a 12 dB. Alta. Evidência: medicoes-H.txt [FATO].
24. Na próxima gravação, microfone de lapela ou sala fechada. Alta. Evidência: item 23; ganho [PRIOR].
25. Quietude de 400 ms na pausa antes de "Qual é?" (19,60 a 20,00 s) em vez de dentro da fala. Média. Evidência: pausa de 0,60 s em 19,50 a 20,10 [FATO, words-raw.json]; colocar silêncio sobre "Qual é?" exigiria cortar a trilha sob a fala, não o silêncio.
26. "ENSINAR O SEU COLEGA" é o maior letreiro do vídeo. Alta. Evidência: é a resposta da pergunta central [FATO, transcrição].
27. O "desenho" de "Eu desenho seu lançamento" vira traço de planta (blueprint). Média. Evidência: verbo literal da fala [FATO]; ganho de memória [HIPÓTESE].
28. Metáfora do prédio em C: térreo "hora de cadeira", segundo andar "segundo produto". Média. Evidência: "segundo produto" está na fala [FATO]; leitura pelo leigo [HIPÓTESE].
29. Nenhum dente, boca ou cadeira odontológica nos grafismos. Alta. Evidência: restrição CFO no contexto.md [FATO].
30. Cartões de post genéricos (blocos) para "mesmo diagnóstico", sem fotos de outros perfis. Alta. Evidência: usar post real de terceiro expõe pessoa real [PRIOR].
31. Reacts desenhados, nunca clipes de terceiros. Alta. Evidência: direito de imagem [PRIOR]; regra sem emoji [FATO, CLAUDE.md].
32. Nada de comentários falsos na animação do CTA. Alta. Evidência: prova social inventada fere a regra de não inventar dado [FATO, tarefa].
33. C sem legenda palavra a palavra perde quem vê sem som. Média. Evidência: [HIPÓTESE]; testar com 3 pessoas sem som.
34. B com legenda na emenda das duas metades. Média. Evidência: posição livre de rosto e de painel [ESTIMATIVA, layout].
35. Rodapé de fonte em 26 px no canto superior esquerdo. Média. Evidência: zona segura [PRIOR].
36. Sem fonte verificada, letreiro DENTISTAS DO BRASIL. Alta. Evidência: restrição do contexto.md [FATO].
37. O número oficial diferente de 474 mil cria conflito com o áudio. Alta. Evidência: o áudio é imutável sem regravação [FATO].
38. Gancho "Dentistas" filtra quem não é dentista e pode subir o pulo. Média. Evidência: [HIPÓTESE]; mediana de pulo 68% vem de conteúdo para público amplo [PRIOR].
39. Ler comentários de dentistas junto com alcance. Alta. Evidência: objetivo do pedido é conversão [FATO, pedido].
40. TABULEIRO fora deste reel. Alta. Evidência: regra de alcance 150 [FATO, CLAUDE.md].
41. Variação opcional com respiros cortados (economia de cerca de 2,2 s). Baixa. Evidência: soma das pausas 0,32 + 0,52 + 0,48 + 0,22 + 0,24 + 0,42 = 2,20 s [ESTIMATIVA, words-raw.json], sem contar a pausa do "Qual é?".
42. Não cortar a pausa de 19,50 a 20,10: é onde mora a quietude. Alta. Evidência: item 25.
43. Zoom máximo de 1,18x. Alta. Evidência: teto 1,25x [FATO, contexto.md]; fator efetivo 2,21x [ESTIMATIVA].
44. Recorte da tela dividida acompanha a caixa do rosto tirada de mask.mp4. Média. Evidência: topo da cabeça varia de y 235 a 300 no bruto [ESTIMATIVA, frames-amostra.jpg].
45. Motion blur por subframes só nas transições. Média. Evidência: multiplica tempo de render [ESTIMATIVA].
46. Medir o primeiro render e registrar tempo. Alta. Evidência: tempo de render sem dado.
47. Bloco cinematográfico do A com barras de 120 px, não 2,39:1. Média. Evidência: barras 2,39:1 em 1080 de largura deixam 452 px de altura útil e cortam o rosto [ESTIMATIVA, 1080/2,39].
48. SFX baixos e alinhados ao pico, no máximo um por segundo. Média. Evidência: twoclipping alinha pelo pico [FATO, contexto.md]; excesso cansa [PRIOR].
49. Trilha a zero na quietude. Alta. Evidência: gdgtify pede um momento de quietude [FATO, contexto.md].
50. Grep de travessão e nomes proibidos nos HTML antes do render. Alta. Evidência: regras de texto [FATO, CLAUDE.md].
51. Confirmar com o Bruno o que é "4D" em uma linha. Média. Evidência: termo não existe em edição [PRIOR].
52. Ordem de publicação A primeiro. Média. Evidência: é o pipeline conhecido e o menos arriscado [FATO, contexto.md].
53. Se A ficar abaixo de 53 de alcance em D+3, B e C não vão ao feed com esta fala. Média. Evidência: [HIPÓTESE de corte].
54. B e C podem virar stories com enquete "você ensina sua técnica?". Baixa. Evidência: stories diários [FATO, CLAUDE.md]; adesão [HIPÓTESE].
55. A conversa em DM vale mais que alcance. Média. Evidência: pedido é conversão [FATO]; peso [PRIOR].
56. Reservar tempo do Bruno para responder comentários no dia. Média. Evidência: "eu te respondo" é promessa gravada [FATO].
57. Verificar se há automação para "dentista" no PostZen. Média. Evidência: lacuna.
58. A legenda do post (texto abaixo do vídeo) pode explicar o que é "lançamento" em uma linha. Média. Evidência: o vídeo não explica [FATO, transcrição].
59. Na legenda do post, também valem as regras sem travessão e sem promessa. Alta. Evidência: CLAUDE.md.
60. Ler a CFO 196/2019 oficial antes de publicar. Alta. Evidência: não lida [FATO, enquadramento].
61. O Bruno não é dentista: o vídeo não pode sugerir que ele é. Alta. Evidência: "colegas" na fala pode soar como se ele fosse dentista [HIPÓTESE]; o terço inferior resolve.
62. "Colegas" dito por quem não é dentista pode soar estranho. Média. Evidência: a palavra está na fala [FATO]; percepção [HIPÓTESE]. Na tela, usar "dentistas", não "colegas", onde possível.
63. Usar a paleta preto e ouro só em C para os 3 parecerem diferentes. Média. Evidência: série 2 já tem essa paleta [FATO].
64. A com as cores do vídeo (P&B para cor), B com painel claro para contraste com o escritório. Baixa. Evidência: [HIPÓTESE estética].
65. Júri cego das 3 versões precisa de alguém de fora do pipeline. Média. Evidência: cadeiras que conhecem o A tendem a preferir A [PRIOR].
66. Mostrar os 3 vídeos a 3 dentistas reais antes de publicar, sem som. Baixa. Evidência: [HIPÓTESE]; custo baixo.
67. O CTA final com caixa de comentário desenhada deixa claro onde tocar. Média. Evidência: [PRIOR].
68. Nenhum texto de frente sobre olhos e boca: faixas y 860 a 940 e 1120 a 1200 vetadas. Alta. Evidência: posição medida a olho [ESTIMATIVA, frames-amostra.jpg].
69. Letreiro atrás só na faixa y 220 a 560. Média. Evidência: parede livre acima da cabeça [FATO, contexto.md]; números [ESTIMATIVA].
70. Validar as listas com um quadro exportado por linha (contact sheet) antes do render completo. Alta. Evidência: custo de render sem dado.
71. Entregar também a versão "limpa" de cada modelo sem SFX. Baixa. Evidência: facilita refazer áudio [PRIOR].
72. Guardar stems (voz, trilha, SFX) separados. Alta. Evidência: custo de reverter baixo depende disso [FATO, enquadramento D1].
73. O critério "voz acima da trilha em todo trecho falado" se mede por janela de 50 ms com voz e trilha em stems. Média. Evidência: método de medicoes-H.txt.
74. Nome do arquivo final com modelo e data, ex.: dentista-A-2026-10-22.mp4. Baixa. Evidência: organização [PRIOR].
75. Registrar a rodada no 00-SISTEMA após publicar. Alta. Evidência: regra do CLAUDE.md.
76. Se o pulo do A ficar acima de 68% mas vierem 5 ou mais comentários "dentista", manter o formato. Média. Evidência: item 38 [HIPÓTESE].
77. Se B tiver nota de clareza maior que A no júri, testar tela dividida em outro nicho do plano. Baixa. Evidência: plano de 5 nichos citado no contexto [FATO].
78. Upscale com unsharp leve para não plastificar a pele. Média. Evidência: [PRIOR].
79. Não usar inteligência de "upscale por IA" de serviço externo: nada instalado, nada enviado a terceiros. Alta. Evidência: restrições da tarefa [FATO].
80. Se a máscara falhar no cabelo, em A mudar o letreiro para frente em 2 dos 6 momentos, longe do rosto. Média. Evidência: plano B de produção [PRIOR].

---

## 5. Pre-mortem da cadeira H

Daqui a 30 dias o plano falhou. Como:
1. A escuta revelou que voz_master soa metálica; refizemos do raw, e o bruto com relação voz/ruído de 8 a 12 dB não deu voz natural em nenhuma cadeia. O Bruno pediu regravação. (Mais provável.)
2. Tirar o confete do A irritou o Bruno: para ele era a assinatura. O A pareceu "menos" que o Tzur v2.
3. A tela dividida do B ficou com cara de vídeo de cortes amador porque o painel de baixo tinha grafismo simples demais.
4. O prédio de palavras do C ficou abstrato: leigo não entendeu a metáfora, e sem legenda quem viu sem som não pegou a mensagem.
5. O halo da máscara 360x640 apareceu no cabelo nos 6 letreiros do A, visível no celular.
6. Ninguém verificou o 474 mil a tempo; o letreiro caiu para DENTISTAS DO BRASIL e o gancho perdeu força.
7. O A foi publicado, o pulo foi 78% porque quem não é dentista saiu no segundo 1, e a cadeira leu isso como fracasso, quando houve 6 comentários de dentistas.
8. Os comentários chegaram e ninguém respondeu no mesmo dia.
9. Render com subframes levou horas e atrasou a entrega além de 23/10.
10. Meu ponto cego: a lista de banidos do twoclipping, as regras do gdgtify ou o código do Tzur v2 têm detalhes que eu não li e contradizem parte das listas.

---

## 6. Previsões numéricas

Todas [PRIOR] ou [ESTIMATIVA], com premissa de que A é publicado em 29/10/2026 e B ou C, se publicados, depois de 05/11.

| Data de conferência | Métrica | Valor previsto |
|---|---|---|
| 23/10/2026 | arquivos finais com -15 a -13 LUFS e TP até -1,0 dBTP | 3 de 3 [PRIOR 0,9] |
| 23/10/2026 | pedidos do Bruno para refazer áudio | 0 ou 1 [PRIOR] |
| 05/11/2026 (D+7 do A) | alcance do A | entre 120 e 500 [PRIOR, premissa: Bruno em cena 2,4x a 5,8x a mediana de 106 dá 254 a 615; desconto pelo filtro "Dentistas"] |
| 05/11/2026 | pulo do A | entre 60% e 75% [PRIOR] |
| 05/11/2026 | comentários com "dentista" no A | entre 2 e 12 [PRIOR] |
| 20/11/2026 (D+30 de hoje) | modelos publicados no feed | 1 ou 2 de 3 [PRIOR] |
| 20/11/2026 | conversas em DM com dentista iniciadas pelo reel | entre 1 e 6 [PRIOR] |
| 20/12/2026 (D+60) | diferença de alcance entre o melhor e o pior modelo publicado | dentro de mais ou menos 50% (indistinguível com N = 1) [PRIOR] |
| 20/12/2026 | palavra-chave TABULEIRO usada em algum reel do nicho dentista | sim, se algum passou de 150 de alcance [PRIOR 0,5] |
| 19/01/2027 (D+90) | dentistas em conversa comercial originados deste reel | entre 0 e 3 [PRIOR] |
| 19/01/2027 | formato B (tela dividida) reaproveitado em outro nicho | sim [PRIOR 0,4] |

---

## 7. O que mudaria minha opinião, lacunas e fontes

### O que mudaria minha opinião
- Se a escuta mostrar que voz_master é natural e as pausas não incomodam no celular, aceito D1 opção a com só o limitador; 31,6 dB pode ser inaudível na prática.
- Se o Bruno disser que confete é assinatura da marca, devolvo o confete ao A, mas fora do número 474 mil (por exemplo, no CTA).
- Se "dividindo dela" significar outra coisa (dividir a fala em blocos, por exemplo), B deixa de ser tela dividida e vira talking head punchy com b-roll (sab8a puro).
- Se o número oficial do CFO não for 474 mil, a peça precisa de regravação do gancho ou de letreiro genérico.
- Se houver autorização escrita do Tzur, considero a prova na legenda do post.
- Se o primeiro render medir mais de 2 min por segundo de vídeo, corto o motion blur por subframes.

### Lacunas
- Não escutei o áudio (só medi). Não sei se a voz soa natural.
- Não li os prompts do repositório, o código do Tzur v2, a pesquisa nem os planos de outras cadeiras.
- Não verifiquei 474 mil, nem as medianas de alcance 106 e pulo 68% (vêm do enquadramento).
- Não li a Resolução CFO 196/2019.
- Não sei o método de upscale usado em base.mp4.
- Não sei se existe automação para "dentista".
- Tempo de render do Playwright: sem dado.
- Posições de rosto são estimativas a olho em 5 quadros de amostra.

### Fontes
- /home/user/Disparo-/videos/nichos/dentista/god/contexto.md
- /home/user/Disparo-/CLAUDE.md
- /home/user/Disparo-/videos/nichos/dentista/god/words-raw.json e transcricao-tempos.txt
- /home/user/Disparo-/videos/nichos/dentista/god/frames-amostra.jpg
- /home/user/Disparo-/videos/nichos/dentista/god/run/02-cadeiras/evidencias-H/medicoes-H.txt (ffprobe, loudnorm, envelope RMS, lista de filtros, ferramentas presentes, seg.log)
- Pedido do Bruno e enquadramento das decisões D1 a D3 (texto da tarefa)
