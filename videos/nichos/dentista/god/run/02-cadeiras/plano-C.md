# Plano da cadeira C · Reel do dentista · Agência Reunida Modo GOD · 21/10/2026

Cliente: O Estrategista (@o_estrategista.com.br). Bruno, Estrategista de Lançamento.

| Campo | Conteúdo |
|---|---|
| Cadeira | C · Otimista de crescimento |
| Persona | Estrategista de crescimento que procura o maior potencial e alternativas criativas |
| OTIMIZA PARA | Crescimento e opções fora do óbvio |
| PONTO CEGO (assumido por escrito) | A dificuldade real de execução. Eu tendo a contar o teto da ideia e esquecer o custo de fazer. Compensação neste plano: cada modelo tem nível 1 (obrigatório), nível 2 e nível 3 (corta primeiro), um teste de 300 quadros antes do render cheio, uma regra de corte de escopo com data, e a conta refeita com tudo 2 vezes mais difícil (seção 2, pergunta contrária) |
| PERGUNTA CONTRÁRIA | E se executar for duas vezes mais difícil do que parece? Resposta na seção 1.1 |

Etiquetas: [FATO] com a fonte ao lado · [ESTIMATIVA] com a conta ou a premissa · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, evidência nível 4, nunca fecha objeção sozinho.
Insumos lidos: contexto.md, run/00-enquadramento.md, run/01-fatos.md, F1, F4 (inteiros nas seções usadas), resumos de F2 e F3 da tarefa, words-raw.json, transcricao-tempos.txt, frames-amostra.jpg, 06-plano-final.md (seções 2.2 e 7), 00-SISTEMA.md (ficha de entrada).
Medição nova desta cadeira (nível 1, scripts e logs em run/02-cadeiras/evidencias-C/): expansor guiado pela transcrição no voz_master.wav, piso de ruído no miolo das pausas e loudnorm em duas passadas medido depois de AAC 192k.

---

## 0. Veredito (12 linhas)

1. Fazer os 3 modelos do mesmo bruto, sobre uma base comum construída uma vez: áudio master único, máscara corrigida e lista de edição ligada a palavras (edit.json), não a segundos.
2. Áudio: remasterizar a partir do voz_master.wav com expansor guiado pela transcrição e pela energia, e loudnorm em duas passadas com alvo de true peak -1,5 dBTP para sobrar margem ao AAC. Testei: -14,4 LUFS e -1,4 dBTP depois de AAC [FATO, evidencias-C/ebur_aac.log].
3. O corte de 40 dB nas pausas, do jeito que está escrito, falha por causa do método, não do som. Proponho trocar por piso no miolo das pausas abaixo de -45 dBFS mais o ouvido do Bruno.
4. Modelo A = Tzur v2 enxuto: letreiro 3D nasce atrás da cabeça em 6 momentos, 2 inserts gráficos, reacts em SVG, bloco final sem prova inventada. Rosto em cerca de 91% do tempo.
5. Modelo B (defendo como o principal para 29/10) = Lousa Dividida: tela dividida em que o painel de cima é uma lousa de aula desenhando o que o Bruno diz. É a resposta literal a "dividindo com reacts e animações que representam", e o formato encena a tese (ensinar o colega). Rosto em 100% do tempo, 33% em tela cheia.
6. Modelo C (aposta fora do óbvio) = Tabuleiro 4D: um tabuleiro em perspectiva atrás da cabeça de onde as palavras sobem como peças e viram estrutura (gdgtify), com órbita passando atrás da cabeça (twoclipping-041659). Liga a peça à marca Xeque-Mate. Rosto em 100%.
7. Prompts misturados: sab8a-475686, stokebuilder-356793, twoclipping-551116, twoclipping-041659, gdgtify-929495, techhalla-498547, twoclipping-000267, alex-prompter-997524, notdwd-998633, everestchris6-399895, l3d1c-632524.
8. Legenda: "no Brasil" corrigido; trecho 24,94 a 29,04 s só depois de ouvir (B02); "FORMAR QUEM DISPUTA" entra como título da tese, não como legenda.
9. Na tela: "+474 mil dentistas ativos" com rodapé "Fonte: CFO, out/2026". Tzur fora da tela. Sem dente, cadeira odontológica, boca, preço ou promessa.
10. O maior ganho de crescimento não é este reel, é o molde: com edit.json por palavra, os outros 4 nichos (consórcio, nutri, psicólogo, advogado) custam só a gravação e cerca de 10 a 15 min de máquina cada.
11. Se tudo for 2 vezes mais difícil: A e B saem no prazo, C sai reduzido ou vai para o nicho seguinte. Corte de escopo decidido até 27/10, 12h.
12. Probabilidade de o reel principal bater 106 de alcance e pulo abaixo de 68% em 7 dias: 0,42, faixa 0,25 a 0,60 [PRIOR com base nos fatos F12 a F16].

### 0.1 Resposta à pergunta contrária: e se executar for duas vezes mais difícil?

| Item | Conta de base | Dobrado | Cabe no prazo? |
|---|---|---|---|
| Render de máquina dos 3 | [ESTIMATIVA] A 951 s (F4) + B cerca de 567 s + C cerca de 900 s (contas da pergunta 9) = cerca de 41 min | cerca de 82 min | Sim. Máquina livre até 28/10 |
| Trabalho humano ou de agente (escrever HTML, ajustar máscara, conferir) | [PRIOR] A 3 a 4 h, B 5 a 7 h, C 6 a 9 h, base comum 3 h = 17 a 23 h | 34 a 46 h | Apertado. De 22/10 a 28/10 são 7 dias, e o consórcio (publica 27/10) e a nutri (31/10) disputam o mesmo pipeline [FATO, 06-plano-final.md linha 194] |
| Refações depois de ver | [PRIOR] 1 rodada por modelo | 2 rodadas | Só se a base comum ficar pronta até 23/10 |
| Aprovação do áudio pelo Bruno | 1 rodada até 23/10 | 2 rodadas até 24/10 | Sim, o áudio é curto |

Regra que eu me imponho por causa do ponto cego:
- Ordem fixa: base comum (áudio, máscara, edit.json) → A → B → C. O C nunca atrasa A e B.
- Teste de 300 quadros por modelo antes do render cheio (B13 do livro de fatos). Se o custo por quadro medido passar de 2 vezes a estimativa, corta o nível 3 daquele modelo.
- 27/10 às 12h: se o C não tiver contato de 20 stills aprovado (l3d1c-632524), ele sai reduzido (tabuleiro e peças, sem órbita e sem a ponte de peças) ou vai para o reel do nutricionista.
- Se dobrar e ainda assim faltar tempo, o que eu sacrifico primeiro é o C, depois o bloco final do A. O B não se corta, porque é o candidato principal.

---

## 1. Respostas às 14 perguntas

### P1. Qual modelo a cadeira defende e quais ids entram

Defendo fazer os três, com o B como peça principal para 29/10, o C como a aposta de teto alto e o A como controle (o que já fazemos).

| Modelo | Base | Ids do repositório | Aproveita | Descarta |
|---|---|---|---|---|
| A · Tzur v2 enxuto | ov2.html + cap2.js + seg.py + comp.py (videos/cases/tzur) | sab8a-475686, techhalla-498547, twoclipping-000267, everestchris6-399895 | sab8a: contrato mínimo (corte de respiro, legenda, grafismo, música). techhalla: mola por glifo com escalonamento de 125 ms, punch-in de 1,0 a 1,08, pré-passe de 8 stills. twoclipping-000267: lista de banidos, 3 subquadros, SFX pelo pico. everestchris6: régua de QA (nada parado acima de 0,5 s, contraste 4,5:1, entender sem som) | techhalla: desalinhamento magenta e verde (é RGB split), paleta ácida, "STOP SCROLLING". Tzur: confete, tremida, RGB split, "1.287 comentários" e @ inventados, glifos ♥ ✓ ✕ como texto [FATO, F32] |
| B · Lousa Dividida | modelo.html da Série 2 (painel) + comp.py (janela do Bruno) + cap2.js (legenda) | stokebuilder-356793, twoclipping-551116, notdwd-998633, gdgtify-929495 (só a quietude), l3d1c-632524 | stokebuilder: rosto sempre visível quando o gráfico entra, gráfico só dentro de frase inteira, texto fiel, rosto entre gráficos. twoclipping-551116: stickers recortados com borda branca como reacts, letras subindo por máscara, "nada aparece com pop seco". notdwd: no máximo 7 palavras de legenda, cinza para branco em 0,2 s, voz 10 a 15 dB acima da música. gdgtify: 400 ms de quietude em 19,60 a 20,00 s. l3d1c: legenda medida para caber na zona segura | stokebuilder: PiP no canto (rosto pequeno a partir de 576x1024 perde nitidez) e a meta de 35 a 50 momentos. twoclipping-551116: quadrado 1440x1440, contadores de views e "MATCH %" (métrica inventada), 8 subquadros |
| C · Tabuleiro 4D | ov2.html (camadas back e front) + comp.py | gdgtify-929495, twoclipping-041659, techhalla-498547, twoclipping-000267, alex-prompter-997524, twoclipping-551116 (legenda) | gdgtify: palavras viram estrutura, frase final apoiada nas anteriores, relógio pela fala, quietude de 400 ms, seek(t) puro. twoclipping-041659: órbita com a metade de trás escondida pela cabeça, palavra sublinhada no instante em que é falada, máscara estendida além da borda. techhalla: mola por glifo. twoclipping-000267: banidos, 3 subquadros, cuidado com preserve-3d. alex-prompter: esqueleto de 5 cenas mapeado na fala | gdgtify: palco 100% tipográfico sem pessoa (animação sem rosto ficou de 0,15x a 0,8x [FATO, CLAUDE.md]) e 1080x1080. twoclipping-041659: mapa de calor na silhueta, pixel art, 4:3, "fall through the head" (esconde o rosto). alex-prompter: cena de "prova" e "3 passos" que a fala não tem |

O "letreiro 4D" pedido pelo Bruno, como esta cadeira lê: letreiro com extrusão 3D (profundidade) mais tempo (nasce escondido atrás da cabeça e sobe até repousar acima dela). Nenhum prompt do repositório faz isso com pessoa filmada [FATO, F41: zero prompts citam rembg ou segmentação]; vem do nosso pipeline Tzur, com a órbita do twoclipping-041659 como refinamento.

### P2. Rosto de 0 a 3 s, porcentagem do tempo e zoom máximo

| Modelo | Rosto de 0 a 3 s | Rosto visível no total | Rosto em tela cheia | Zoom máximo | Ampliação total da fonte |
|---|---|---|---|---|---|
| A | Sim, desde o quadro 0 (P&B até 2,08 s) | [ESTIMATIVA] 33,09 de 36,43 s = 90,8% (inserts: 11,38 a 13,32 s e 22,82 a 24,24 s, somando 3,36 s) | 90,8% | 1,08 | 2,03x (1,875 x 1,08) |
| B | Sim, tela cheia de 0 a 5,16 s | [ESTIMATIVA] 100% (tela cheia ou janela de 1080x1120) | [ESTIMATIVA] 5,16 + 2,43 + 4,43 = 12,02 s = 33,0% (0 a 5,16; 20,00 a 22,43; 32,00 a 36,43) | 1,12 (CTA) | 2,10x |
| C | Sim, desde o quadro 0 | 100% | 100% | 1,10 (CTA) | 2,06x |

Todos ficam abaixo do teto de 1,25x [FATO, contexto.md] e do critério de 80% (HIPÓTESE da D2). A janela do Bruno no B é recorte do base.mp4 sem nova ampliação [FATO de geometria, F4 4.1].

### P3. Lista de edição quadro a quadro

Regras comuns aos 3:
- Saída 1080x1920, 30 fps, quadro = round(t x 30), linha do tempo sem corte de pausa: 0 a 36,43 s, quadros 0 a 1092 [FATO, base.mp4 tem 1093 quadros a 30 fps, F02]. Não corto pausas: somam 2,98 s [FATO, F07], e cada corte em selfie de mão vira pulo de imagem que precisaria de punch-in para esconder, gastando o orçamento de zoom.
- Cada evento é guardado no edit.json pelo índice da palavra em words-raw.json, não pelo segundo. Se o Bruno regravar, o render se refaz sozinho.
- Zona segura: textos entre y 230 e y 1460 [PRIOR, VibeRoll nível 3, DR09]. Legenda palavra a palavra em y 1300 a 1440 nos trechos de tela cheia, 2 a 4 palavras por grupo, palavra ativa em ouro #E8B36A, entrada cinza para branco em 0,2 s (notdwd-998633). No B, nos trechos divididos, a legenda fica sobre a linha divisória (y 760 a 860).
- Letreiro de trás: nasce em y cerca de 600 (escondido pela máscara da cabeça) e sobe até repousar na faixa de y 240 a 440. O topo da pessoa varia de y 252 a 555, mediana 420 [FATO, F29], então o letreiro em repouso fica quase todo visível e só o pé das letras some quando o Bruno ergue a cabeça. Isso dá o "saindo de trás" sem perder leitura.
- SFX: início = quadro do evento visual menos o pico medido [FATO, F35]. Picos: whoosh 268,5 ms, riser 1596,6 ms, swipe 137,1 ms, typing 27,6 ms (primeiro clique), impact 4,2 ms, pop 2,6 ms, tick 2,6 ms, ding 6,6 ms, coin 2,5 ms, sub 3,7 ms.
- Motion blur: 3 subquadros em t - 1/120, t, t + 1/120 só nas janelas de movimento marcadas "MB"; 5 nas transições de tela [PRIOR, F4 4.3]. Mistura em numpy com alfa pré-multiplicado.
- Animação de entrada padrão: curva criticamente amortecida x(t) = 1 - (1 + wt)e^(-wt), sem quique (twoclipping-000267 bane easing elástico).

#### Modelo B · Lousa Dividida (principal)

| # | Início s (q) | Fim s (q) | Palavra gatilho | Camada | Texto na tela | Animação | SFX (início) |
|---|---|---|---|---|---|---|---|
| B1 | 0,00 (0) | 2,08 (62) | "Dentistas" | tela cheia, frente | Título fixo, 2 linhas, y 250 a 420: "DENTISTA: HORA DE CADEIRA OU SEGUNDO PRODUTO?" | Já presente no quadro 0, sem entrada (F53: 10 de 10 têm texto no quadro 0). Push lento 1,00 a 1,02 | nenhum |
| B2 | 2,08 (62) | 5,16 (155) | "474" | tela cheia, atrás | "+474 MIL" ouro com extrusão de 14 sombras | Título recolhe por máscara em 0,2 s (q62 a q68). Letreiro sobe de trás da cabeça, rotateX 55° para 0°, mola por glifo 125 ms (techhalla), chega em q95 ("mil"). Punch-in 1,00 a 1,06 de q62 a q95. MB q62 a q95 | riser 1,58 s (q47) culmina em q95; impact 3,18 s (q95) |
| B3 | 2,33 (70) | 5,48 (164) | "474" | tela cheia, frente | Rodapé 26 px em y 1250: "Fonte: CFO, out/2026" | Opacidade 0 a 1 em 0,2 s | nenhum |
| B4 | 0,00 (0) | 36,43 (1092) | cada palavra | frente | Legenda fiel, com "no Brasil" (P5) e trecho 24,94 a 29,04 s conforme P4 | Grupo de 2 a 4 palavras, palavra ativa em ouro | nenhum |
| B5 | 5,16 (155) | 5,51 (165) | pausa após "Brasil," | tela dividida | nenhum | Painel 1080x800 desce do topo, Bruno desliza para a janela de baixo (1080x1120, recorte que segue o centro da máscara), linha dourada de 4 px. 0,35 s. MB 5 subquadros. "+474 MIL" sai por cima | whoosh 5,21 s (q156), pico em 5,48 |
| B6 | 5,48 (164) | 7,68 (230) | "porque" | painel | "VOCÊ AINDA SÓ VENDE" | Letras sobem por linha de máscara uma a uma (twoclipping-551116) | nenhum |
| B7 | 7,68 (230) | 8,80 (264) | "hora" | painel + react | "HORA DE CADEIRA" e relógio de traço; react: ampulheta recortada com borda branca perto da linha | Relógio se desenha (stroke-dashoffset 0,4 s), ponteiro dá uma volta até q264. Ampulheta entra em q244 com balanço lento | tick em q230, q244, q249 a -24 dB |
| B8 | 9,36 (281) | 12,10 (363) | "quase" | painel | Grade 3x3 de cartões de perfil genéricos (retângulos com linhas, sem foto) que viram para "DIAGNÓSTICO" | Cartões viram em cascata de 60 ms a partir de q341 ("diagnóstico"). MB q341 a q363 | swipe 11,24 s (q337) |
| B9 | 12,24 (367) | 13,32 (400) | "mesma" | painel + react | Cartões viram para "CONCLUSÃO"; react: sinal de igual desenhado à mão carimba no centro | Carimbo em q380 com escala 1,2 a 1,0 amortecida | pop 12,66 s (q380) |
| B10 | 13,32 (400) | 13,84 (415) | pausa | painel | nenhum | Grade se recolhe a um ponto em 0,3 s; painel limpo | nenhum (respiro) |
| B11 | 13,84 (415) | 16,04 (481) | "Se" | painel | "UMA TÉCNICA" com estrela de 5 pontas em traço | Estrela se desenha em q452 ("técnica") | nenhum |
| B12 | 16,04 (481) | 17,92 (538) | "dentistas" | painel | "QUE OS DENTISTAS QUEREM APRENDER"; 12 ícones de pessoa genéricos em arco | Pessoas surgem em cascata de 40 ms; setas finas saem da estrela em q515 ("aprender") | tick 16,04 s (q481) a -24 dB |
| B13 | 17,92 (538) | 19,50 (585) | "existe" | painel | "EXISTE UM MERCADO." | As 12 pessoas se rearrumam formando a palavra MERCADO (gdgtify: palavra vira estrutura), fecham em q585. MB q560 a q585 | coin 19,12 s (q574) |
| B14 | 19,50 (585) | 20,00 (600) | pausa de 0,60 s | painel congelado | "EXISTE UM MERCADO." | Quietude: nada se mexe de q588 a q600 (400 ms), trilha em silêncio | nenhum, trilha a zero |
| B15 | 20,00 (600) | 20,64 (619) | "Qual" | tela cheia | nenhum além da legenda | Corte seco para tela cheia em q600. Punch-in 1,00 a 1,08 em 0,2 s | sub 20,10 s (q603) |
| B16 | 20,64 (619) | 22,70 (681) | "ensinar" | tela cheia, atrás | "ENSINAR" (grande) e "O SEU COLEGA" (menor) | Sobe de trás da cabeça, mola por glifo, repousa em q635. Zoom volta a 1,00 entre q667 e q681 | impact 21,17 s (q635) |
| B17 | 22,43 (673) | 22,78 (683) | "Eu" | tela dividida | nenhum | Divisão volta, 0,35 s, MB 5 subquadros | whoosh 22,43 s (q673), pico 22,70 |
| B18 | 22,82 (685) | 24,24 (727) | "desenho" | painel | "EU DESENHO SEU LANÇAMENTO" e planta de 5 nós ligados | Nós acendem em q685, q696, q706, q711, q720; traço ouro liga cada um | tick em cada nó a -24 dB |
| B19 | 24,94 (748) | 26,88 (806) | "deixa" | painel | "DISPUTAR PACIENTE" | Letras sobem por máscara em q763 ("disputar") | nenhum |
| B20 | 26,88 (806) | 29,04 (871) | "passa" | painel + react | Traço ouro risca "DISPUTAR PACIENTE"; sobe "FORMAR QUEM DISPUTA" (título da tese, ver P4); react: quadro de aula recortado | Risco em 0,25 s a partir de q806; título sobe a partir de q827 | swipe 26,74 s (q802); ding 28,27 s (q848) a -24 dB |
| B21 | 29,28 (878) | 31,58 (947) | "Sua" | painel | Caixa 1 "HORA DE CADEIRA" (com o relógio de B7) e caixa 2 "SEGUNDO PRODUTO" | Caixa 1 encolhe para a esquerda em q887 ("técnica"); caixa 2 sobe e pousa em q923 ("segundo"), sem quique | impact 30,78 s (q923); coin 31,18 s (q935) |
| B22 | 31,73 (952) | 32,08 (962) | pausa após "produto." | tela cheia | nenhum | Painel sobe e sai, Bruno volta à tela cheia, MB 5 subquadros | whoosh 31,73 s (q952), pico 32,00 |
| B23 | 32,00 (960) | 35,92 (1078) | "Dentista" | tela cheia, atrás | "COMENTA: DENTISTA" | Sobe de trás da cabeça a partir de q980 ("comenta"), repousa em q996. Punch-in lento 1,00 a 1,12 de q960 a q1078 | impact 33,22 s (q997) |
| B24 | 33,82 (1015) | 35,92 (1078) | "profissão" | frente, react | Balão de comentário SVG perto do ombro, sem nome de usuário e sem contador, digitando "dentista"; seta desenhada à mão apontando para o lado direito, onde fica o botão de comentário | Digitação de q1015 a q1032; seta se desenha em q1038 ("que") | typing 33,79 s (q1014); pop 35,36 s (q1061) |
| B25 | 35,92 (1078) | 36,43 (1092) | fim | tela cheia | "COMENTA: DENTISTA" fica | Tudo parado; trilha some em 0,5 s | nenhum |

#### Modelo A · Tzur v2 enxuto

| # | Início s (q) | Fim s (q) | Palavra gatilho | Camada | Texto na tela | Animação | SFX (início) |
|---|---|---|---|---|---|---|---|
| A1 | 0,00 (0) | 2,08 (62) | "Dentistas" | tela cheia, frente | "DENTISTA" em y 260, fixo desde o quadro 0 | Bruno em P&B (manifesto do Tzur, sem confete) | nenhum |
| A2 | 2,08 (62) | 5,48 (164) | "474" | tela cheia, atrás | "+474 MIL"; rodapé "Fonte: CFO, out/2026" | Cor volta em 0,2 s em q62; letreiro sobe de trás da cabeça, mola por glifo, repousa em q95. Punch-in 1,00 a 1,06 | riser 1,58 s (q47); impact 3,18 s (q95) |
| A3 | 0,00 (0) | 36,43 (1092) | cada palavra | frente | Legenda palavra a palavra (cap2.js com words-raw.json) | Grupo de 2 a 4 palavras | nenhum |
| A4 | 7,68 (230) | 9,70 (291) | "hora" | atrás + react | "HORA DE CADEIRA"; react relógio SVG perto do ombro | Letreiro sobe; relógio se desenha | whoosh 7,95 s (q239), pico na chegada em q247 |
| A5 | 11,38 (341) | 13,32 (400) | "diagnóstico" | insert tela cheia | Grade de cartões iguais: "DIAGNÓSTICO" e, em q380, "CONCLUSÃO" | Insert entra 0,30 s depois do início de "diagnóstico" (respiro do Tzur medido a partir de q332) e sai na pausa. MB na entrada | swipe 11,24 s (q337) |
| A6 | 15,08 (452) | 16,64 (499) | "técnica" | frente, react | Estrela de traço perto do ombro | Desenha em 0,4 s | pop 15,08 s (q452) |
| A7 | 17,92 (538) | 19,50 (585) | "existe" | atrás | "MERCADO" | Sobe de trás da cabeça | coin 19,12 s (q574) |
| A8 | 19,60 (588) | 20,00 (600) | pausa | todas | nenhum novo | Quietude de 400 ms | trilha a zero |
| A9 | 20,64 (619) | 22,70 (681) | "ensinar" | atrás | "ENSINAR O SEU COLEGA" | Sobe, punch-in 1,00 a 1,08 | impact 21,17 s (q635) |
| A10 | 22,82 (685) | 24,24 (727) | "desenho" | insert tela cheia | "EU DESENHO SEU LANÇAMENTO" com planta de 5 nós | Insert de 1,42 s | whoosh 22,55 s (q677) |
| A11 | 24,94 (748) | 29,04 (871) | "deixa" | frente, terço inferior acima da legenda | "DISPUTAR PACIENTE" riscado e depois "FORMAR QUEM DISPUTA" | Risco em q806 ("passa"), título em q827 | swipe 26,74 s (q802) |
| A12 | 29,28 (878) | 31,58 (947) | "Sua" | atrás + react | "2º PRODUTO"; react duas caixas SVG | Letreiro sobe e repousa em q923 ("segundo") | impact 30,78 s (q923) |
| A13 | 31,58 (947) | 32,00 (960) | pausa | todas | nenhum | Barras de cinema 2,35:1 entram em 0,4 s | whoosh 31,73 s (q952) |
| A14 | 32,00 (960) | 36,43 (1092) | "Dentista" | bloco final: atrás + frente | "COMENTA: DENTISTA" atrás; balão SVG digitando "dentista", sem contador e sem @ | Granulação com semente pelo índice do quadro, grade quente, punch-in 1,00 a 1,05 | typing 33,79 s (q1014); ding 35,35 s (q1061) |

#### Modelo C · Tabuleiro 4D

| # | Início s (q) | Fim s (q) | Palavra gatilho | Camada | Texto na tela | Animação | SFX (início) |
|---|---|---|---|---|---|---|---|
| C1 | 0,00 (0) | 2,08 (62) | "Dentistas" | atrás + frente | Frente: "DENTISTA" fixo em y 250 desde o quadro 0. Atrás: tabuleiro 6x6 em perspectiva (rotateX 62°), linhas ouro a 15%, horizonte em y cerca de 300, borda da frente passando atrás da cabeça | Tabuleiro já presente no quadro 0; deriva lenta presa à parede pelo inverso do tr.trf [HIPÓTESE, B18] | nenhum |
| C2 | 2,08 (62) | 3,80 (114) | "474" | atrás | "474 MIL" | Cada glifo sobe de uma casa do tabuleiro como bloco extrudado (é o piso da estrutura). Mola 125 ms, repousa em q95. Punch-in 1,00 a 1,06. MB | riser 1,58 s (q47); impact 3,18 s (q95) |
| C3 | 2,33 (70) | 5,48 (164) | "474" | frente | Rodapé "Fonte: CFO, out/2026" | Opacidade 0,2 s | nenhum |
| C4 | 3,80 (114) | 5,48 (164) | "colegas" | atrás + frente | nenhum | Órbita fina ouro se desenha em volta da cabeça em 0,8 s; metade de trás na camada back (escondida pela máscara), metade da frente na front (twoclipping-041659). Some até q164 | swipe 3,66 s (q110) a -24 dB |
| C5 | 7,68 (230) | 8,80 (264) | "hora" | atrás | "HORA DE CADEIRA" | Peça pequena sobe na casa da esquerda | tick 7,68 s (q230) |
| C6 | 9,36 (281) | 13,32 (400) | "quase" | atrás | "DIAGNÓSTICO" repetido em 6 peças iguais | Cópias brotam uma a uma em q341; em q380 ("mesma") todas tombam deitadas na casa, sem quique | swipe 12,52 s (q376) |
| C7 | 13,32 (400) | 13,84 (415) | pausa | atrás | nenhum | Peças afundam no tabuleiro | nenhum |
| C8 | 15,08 (452) | 17,92 (538) | "técnica" | atrás | "TÉCNICA" | Sobe como viga horizontal larga acima da cabeça | impact 15,63 s (q469), na chegada |
| C9 | 17,92 (538) | 19,50 (585) | "existe" | atrás | "MERCADO" | Sobe como coluna embaixo da viga, segurando a TÉCNICA (gdgtify: carga e apoio) | coin 19,12 s (q574) |
| C10 | 19,60 (588) | 20,00 (600) | pausa | todas | nenhum | Quietude de 400 ms, trilha a zero | nenhum |
| C11 | 20,10 (603) | 20,64 (619) | "Qual" | tela cheia | nenhum | Punch-in 1,00 a 1,08 em 0,2 s | sub 20,10 s (q603) |
| C12 | 20,64 (619) | 22,70 (681) | "ensinar" | atrás + frente | "ENSINAR" | Arco se forma sobre a viga; a órbita volta uma vez em volta da cabeça | impact 21,17 s (q635) |
| C13 | 22,82 (685) | 24,24 (727) | "desenho" | atrás | "LANÇAMENTO" escrito no tabuleiro | Linhas de planta ouro se desenham no tabuleiro ligando as peças (5 nós) | tick em q685, q696, q706, q711, q720 |
| C14 | 24,94 (748) | 29,04 (871) | "deixa" | atrás | "DISPUTAR PACIENTE" e depois "FORMAR QUEM DISPUTA" | A peça "DISPUTAR PACIENTE" desliza para fora do tabuleiro em q806 ("passa"); "FORMAR QUEM DISPUTA" sobe no topo da estrutura em q827 | swipe 26,74 s (q802) |
| C15 | 29,28 (878) | 31,58 (947) | "Sua" | atrás | "2º PRODUTO" | Peça pousa em cima da viga TÉCNICA apoiada no MERCADO em q923 (a frase final se apoia nas anteriores, gdgtify) | impact 30,78 s (q923); coin 31,18 s (q935) |
| C16 | 31,58 (947) | 32,00 (960) | pausa | atrás | nenhum | Estrutura recua e baixa a 30% de brilho | nenhum |
| C17 | 32,00 (960) | 35,92 (1078) | "Dentista" | atrás + frente | Atrás: "COMENTA: DENTISTA" sobe da borda da frente do tabuleiro. Frente: balão SVG digitando "dentista" e seta à mão para o botão de comentário | Punch-in 1,00 a 1,10 | typing 33,79 s (q1014); pop 35,36 s (q1061) |
| C18 | 35,92 (1078) | 36,43 (1092) | fim | atrás | tabuleiro volta ao estado do quadro 0 | Fecha em ciclo, como no gdgtify | nenhum |
| C19 | 0,00 (0) | 36,43 (1092) | cada palavra | frente | Legenda com letras subindo por linha de máscara (twoclipping-551116) | 2 a 4 palavras | nenhum |

### P4. Trecho 24,94 a 29,04 s ("forna que a gente disputa")

Posição: ouvir antes de decidir (B02, cerca de 5 min). Cortar fala está fora de questão.
- Se o ouvido confirmar "formar quem disputa", a transcrição é que errou e a legenda certa já é a fiel.
- Se o ouvido confirmar a fala embolada: a legenda mostra só o que se ouve com clareza, e a tese entra como título na tela ("FORMAR QUEM DISPUTA", eventos B20, A11 e C14). O título é frase do roteiro do próprio Bruno, não fato nem citação, então não fere a regra do stokebuilder de não inventar dado.
- Regravação só se o Bruno ouvir e não aceitar. O caminho barato é regravar o reel inteiro na sessão de 26/10 [FATO, 06-plano-final.md linha 158]. Como a lista é guardada por palavra, o render se refaz com o novo alinhamento. Remendar só o áudio desse trecho deixaria a boca fora de sincronia por 4,1 s, então não recomendo.

Dado de apoio: "a" tem 0,06 s e "gente" 0,04 s no alinhamento [FATO, F08], o que sugere erro de alinhamento ou fala corrida, sem decidir qual dos dois.

### P5. "em Brasil" (4,80 a 5,16 s)

Legenda corrigida para "no Brasil". A diferença na boca é uma sílaba em 5 quadros (q144 a q149), e eu não espero que alguém perceba [PRIOR]. Na tela, o erro gramatical custa mais credibilidade com dentista do que a troca custa em sincronia. A regra de texto fiel do stokebuilder-356793 trata de fato, número e citação, e não de concordância.

### P6. 474 mil na tela

"+474 mil dentistas ativos", com rodapé "Fonte: CFO, out/2026". O número vem da soma das 27 linhas por CRO, que deu 474.659 numa leitura e 474.640 em outra no mesmo dia [FATO, F68, C2]. Arredondado para "+474 mil", ele vale para as duas leituras. A ressalva de que a soma pode contar duas vezes quem tem mais de uma inscrição (B19) não muda o "+474 mil" para menos de 474 mil só se a duplicação for menor que 659. Isso é sem dado, então registro a ressalva [HIPÓTESE]. Se o CFO publicar método que derrube o número abaixo de 474.000, a tela troca para "mais de 470 mil".

### P7. Áudio: cadeia exata

Base: voz_master.wav (-14,2 LUFS, true peak -0,5 dBTP) [FATO, F04]. A cadeia que o gerou é sem dado (B01). Não refaço a partir do raw, porque o voz_master tem a mesma distância fala e pausa que o melhor RNNoise, 16,0 contra 16,3 dB [FATO, DR02, reconferido em evidencias-C/gate_teste.log].

Cadeia comum aos 3 modelos:
1. Expansor híbrido em numpy: ganho 1 dentro das janelas de palavra (30 ms antes, 80 ms depois) **ou** quando o RMS de 20 ms passar de -35 dBFS; fora disso, -20 dB, com rampas de 20 ms.
   - Por que híbrido: no teste só com a transcrição, o trecho de 31,58 a 31,78 s mede -13 a -18 dBFS, nível de fala, e é provavelmente o fim de "produto." que o alinhamento cortou cedo [FATO, evidencias-C/gate_teste.log]. Um expansor só por transcrição comeria esse fim.
   - Em 13,56 a 13,64 s há um evento de -12,5 dBFS no meio da pausa [FATO, mesmo log]. Pode ser respiração, estalo ou ruído, e o B03 fecha isso no ouvido. Se for ruído, tira à mão com ganho de -20 dB só nesses 80 ms.
2. highpass 80 Hz, deesser i=0,3 [FATO: os dois filtros existem neste ffmpeg 6.1.1]. EQ de presença (+2 dB em 3,5 kHz) só se o Bruno pedir [PRIOR].
3. Trilha (lounge sintetizada em numpy, som.py da Série 2) com ducking pela voz (sidechaincompress do add_music.sh). Voz 12 a 18 dB acima da trilha nos trechos falados [PRIOR, notdwd-998633 diz 10 a 15 dB e ducking de -18 dB]. Trilha a zero na quietude de 19,60 a 20,00 s.
4. SFX somados em numpy por índice de amostra a 48 kHz, cada um com o pico no quadro do evento, entre -18 e -24 dB abaixo do pico da voz [PRIOR, P03].
5. loudnorm em duas passadas, I=-14, TP=-1,5, LRA=7, linear=true, com os valores medidos na primeira passada.
6. Mux em AAC 192k, 48 kHz. Medida final com ebur128 (peak=true) **no MP4 final** de cada modelo, mais o DR20 (voz acima da trilha em toda janela de 400 ms com fala).

Teste desta cadeira, só com a voz (sem trilha e sem SFX), já feito:
- Saída: -14,4 LUFS, true peak -1,5 dBTP no WAV e -1,4 dBTP depois do AAC 192k [FATO, evidencias-C/ebur_wav.log e ebur_aac.log]. O AAC subiu o pico em 0,1 dB, e é por isso que o alvo é -1,5 e não -1,0.
- Atenção: na primeira passada, highpass mais deesser levaram o true peak a +1,55 dBTP antes do loudnorm [FATO, ln_pass1.json]. Todo filtro antes do loudnorm pode subir o pico, então a medida que vale é sempre a do arquivo final.
- Piso no miolo das pausas de 0,40 s ou mais, cortando 100 ms de cada borda, antes e depois do expansor a -20 dB [FATO, evidencias-C/piso_teste.log]:

| Pausa | Antes | Depois |
|---|---|---|
| 13,42 a 13,74 s | -18,7 dBFS | -38,7 dBFS |
| 19,60 a 20,00 s | -28,7 dBFS | -48,7 dBFS |
| 22,32 a 22,60 s | -48,2 dBFS | -68,5 dBFS |
| 31,68 a 31,90 s | -18,7 dBFS | -38,7 dBFS |

  Os dois -38,7 são o evento de 13,56 s e a cauda de "produto.", e não ruído de fundo.
- Distância média fala e pausa pelo método do DR02: 16,0 dB antes; 23,2 com -12 dB; 25,8 com -20 dB; 28,1 com -30 dB [FATO, gate_teste.log]. O método mede cauda de palavra como se fosse ruído, por isso nunca chega a 40 dB.

Proposta de critério no lugar dos 40 dB (que é PRIOR): piso no miolo das pausas de 0,40 s ou mais abaixo de -45 dBFS, depois de tirar o que o ouvido do B03 classificar como fala ou respiração, e o Bruno ouvindo no fone sem ouvir chiado.

### P8. Upscale de 576x1024 para 1080x1920

- Uso o base.mp4 que já existe: 1080x1920, 1093 quadros a 30 fps, encoder libx264 [FATO, ffprobe desta cadeira]. O método de ampliação usado nele é sem dado (B17).
- Não reamplio a partir do raw. O raw tem taxa de quadro variável [FATO, F02], e um novo mapeamento de quadros desalinharia a máscara pronta (589 s de segmentação [FATO, F27]).
- Risco no rosto: pele lavada e blocos de compressão crescem com o zoom. Mitigação: zoom no máximo 1,12 (2,10x da fonte), punch-in só em trechos curtos, e unsharp leve (5:5:0,4) só na camada do Bruno, testado em 1 quadro antes [PRIOR, P18].
- Risco no recorte rembg: a máscara sai de 320x320 [FATO, F31], cerca de 6 px por ponto na vertical em 1920.
  - Mitigação: erodir 2 a 4 px e suavizar a borda; manter só o maior componente conexo (scipy.ndimage.label, disponível no cbenv, scipy 1.18.1 [FATO, conferido]), o que resolve os 44 quadros com gente ao fundo [FATO, F30]; tirar o corte fixo em y=470 do comp.py [FATO, F29: 71,6% dos quadros passam dele].
  - O B usa a máscara só nos 12,0 s de tela cheia, então o halo aparece em menos tempo.

### P9. Pipeline e tempo de render

Só o que já existe: Playwright + Chromium, ffmpeg 6.1.1, numpy, scipy do cbenv, rembg (máscara pronta), HTML, CSS 3D e SVG. Nada instalado. Não uso Three.js no C: o tabuleiro sai com CSS 3D (rotateX), a mesma técnica do letreiro do ov2.html, para ficar na faixa de custo medida. Gotcha anotado: nenhuma opacidade ou filtro em elemento preserve-3d [FATO, F48].

| Modelo | Conta | Total [ESTIMATIVA] | Dobrado |
|---|---|---|---|
| A | F4: máscara pronta + trás 108 s + frente 120 s + bloco final com granulação 151 s + composição 568 s + trilha 4 s | 951 s, cerca de 16 min | 32 min |
| B | painel JPEG por pipe 732 q x 0,08 = 59 s + trás só na tela cheia 361 q x 0,099 = 36 s + legenda 1093 x 0,131 = 143 s + subquadros 79 s (F4) + composição numpy 361 x 0,52 = 188 s + overlay ffmpeg nos quadros divididos 732 x 0,071 = 52 s + áudio 10 s | cerca de 567 s, cerca de 9,5 min | 19 min |
| C | trás 1093 x 0,131 (teto da faixa medida) = 143 s + frente 143 s + subquadros só nas entradas, cerca de 12 janelas de 0,5 s: 180 q x 2 x 0,131 = 47 s + composição 568 s + áudio 10 s | cerca de 911 s, cerca de 15 min | 30 min |
| Total em série | | cerca de 40 min | cerca de 81 min |

Premissas:
- Custos por quadro de F26 [FATO, testes curtos].
- Os 361 quadros de tela cheia do B saem de 0 a 5,16 s, 20,00 a 22,43 s e 32,00 a 36,43 s: 12,02 s x 30.
- Custo do glifo em CSS 3D no tabuleiro: sem dado. O teste de 300 quadros (B13 e B14) fecha isso.
- Rodar em paralelo piora: o teste concorrente ficou 2 a 5 vezes mais lento [FATO, F28].

### P10. CTA

Usa o gravado: "Dentista, comenta a sua profissão aqui que eu te respondo" (32,00 a 35,92 s) [FATO, F11]. Na tela, "COMENTA: DENTISTA" atrás da cabeça e o balão digitando "dentista". TABULEIRO não entra: a regra é só em post com alcance de 150 ou mais [FATO, CLAUDE.md], e esse alcance ainda não existe. A visual de tabuleiro do Modelo C é marca, não palavra-chave. A legenda do post também não pede TABULEIRO. Se o reel passar de 150 de alcance, o comentário fixado pode oferecer TABULEIRO depois (decisão do Bruno).

### P11. Conformidade com publicidade odontológica

- Base: Res. CFO 196/2019 e Código de Ética, lidos no texto oficial pela F3 [FATO, F72 e F73, evidencias-F3/res-cfo-196-2019.txt]. A pergunta diz "não lida no oficial", mas o livro de fatos registra a leitura. Sigo o livro.
- Nos 3 modelos: sem boca, dente, raio X, procedimento, instrumental, antes e depois, preço, "grátis", promessa de faturamento ou agenda, "melhor técnica", caso de terceiro.
- Esta cadeira vai além da F3 por precaução: sem ícone de dente e sem cadeira odontológica (P11 do livro é hipótese). "Hora de cadeira" vira relógio e ampulheta.
- A grade de "perfis" do B8, do A5 e do C6 usa retângulos genéricos, sem foto de perfil real nem de paciente, para não virar crítica a colega identificável (art. 44 XII proíbe crítica à técnica de colega [FATO, F73]).
- Nenhum número de alunos, faturamento ou resultado.
- Ressalva: se o Bruno não é inscrito em CRO (B20, sem dado), o código o alcança pelo dentista que aparece, reposta ou contrata (art. 45) [HIPÓTESE, F3].

### P12. Prova (Tzur)

Fora da tela nos 3 modelos:
- O Bruno não disse o Tzur nesta tomada [FATO, F10].
- A autorização da Tzur Capital está pendente e bloqueante [FATO, 06-plano-final.md seção 7 item 5].
- Prova sem fala vira texto solto.

A cena de "prova" do alex-prompter-997524 é ocupada pelo único número com fonte (474 mil, CFO). Se a autorização chegar até 23/10 e o Bruno regravar em 26/10 com a frase do case, a lista por palavra recebe um evento novo sem refazer o resto.

### P13. Métrica, fonte, data e critério de parar

| Métrica | Fonte | Leitura | Critério |
|---|---|---|---|
| Alcance, views, tempo médio assistido e pulo do reel publicado | ig_post_stats (Buzzfy), só leitura | sáb 31/10/2026 (48 h) e qui 05/11/2026 (7 dias) | Sucesso: alcance de 106 ou mais e pulo abaixo de 68% em 7 dias. Meta esticada: pulo abaixo de 60% (06-plano-final.md, conflito C1; adoto 68% como corte e 60% como meta esticada) |
| Comentários com "dentista" | listCommentAutomationLogs (PostZen) e ig_comments, só leitura | 31/10 e 05/11 | Conversa qualificada de dentista é a métrica principal do plano [FATO, 06-plano-final.md linha 77]; meta [PRIOR] 1 ou mais em 7 dias |
| Áudio | ebur128 no MP4 final de cada modelo | ao fim de cada render, até 23/10 para o áudio | -15 a -13 LUFS e TP até -1,0 dBTP; piso das pausas como na P7 |
| Júri cego | 3 cadeiras, notas de clareza e acabamento de 0 a 10, vendo os 3 renders como X, Y e Z, primeiro sem som e depois com som | 28/10 | B ou C com nota igual ou maior que a do A |

Parar:
- Alcance abaixo de 53 em 48 h: o modelo publicado não é usado no nicho seguinte [FATO, regra do 00-enquadramento D4].
- Pulo acima de 75% em 7 dias: o modelo sai do molde [PRIOR, corte do 06-plano-final.md linha 203 aplicado a um reel].

### P14. Regras de texto

- Todo texto de tela está em PT-BR, sem travessão e sem emoji; reacts são SVG.
- Há uma única frase de contraste por peça: "deixa de disputar paciente e passa a formar quem disputa". Ela não usa a forma "não é X, é Y".
- Nenhuma menção a HighClass, Júnior Prazeres ou Felipe Roser.
- Este arquivo também foi escrito sem travessão.

---

## 2. Decisões

### D1 · Áudio masterizado

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. voz_master.wav como está | Zero trabalho | TP -0,5 dBTP estoura com trilha e SFX [FATO, R12 de F4]; o Bruno ouve chiado nas pausas de 13,4 e 31,7 s |
| 2. Remasterizar do voz_master com limitador, de-esser, EQ, trilha, SFX e medida final | Resolve LUFS e TP | Não mexe no piso das pausas (16,0 dB de distância) |
| 3. Refazer do raw comparando rn_std, rn_sh e rn_bd | Ganho de 0,3 dB no máximo (16,3 contra 16,0) [FATO, DR02] | Custa uma rodada e não resolve a causa |
| 4. Regravar o trecho de 24,94 a 29,04 s | Resolve a frase | Quebra a sincronia da boca; melhor regravar tudo em 26/10 |
| **5. Fora do óbvio: expansor híbrido (transcrição mais energia) e um master único para os 3, com alvo de TP de -1,5 por causa do AAC e critério de piso no lugar dos 40 dB** | -14,4 LUFS e -1,4 dBTP depois de AAC já testados; pausas limpas passam de -48 para -68 dBFS | O mesmo master e o mesmo expansor servem aos 5 nichos; o critério de áudio vira medida repetível em vez de PRIOR |

- Premissas: o B03 confirma que os eventos de 13,56 s e 31,6 s são respiração ou fim de palavra [HIPÓTESE]. O Instagram não normaliza para cima nem para baixo de um jeito que mude a percepção [sem dado, B05]. A trilha da Série 2 não briga com a voz [PRIOR].
- **Posição: opção 5**, que contém a 2.
- Probabilidade pelo critério do enquadramento, que inclui os 40 dB pelo método do DR02: **0,35**, faixa [0,15, 0,55]. O critério escrito é quase impossível pelo método. Pelo critério proposto (piso abaixo de -45 dBFS mais o ouvido), a probabilidade seria 0,75 [PRIOR].
- Confiança: 0,6.

### D2 · Modelo A

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. Tzur v2 fiel (manifesto, confete, aplausos, bloco final) | Mais "efeito" | Traz partículas, tremida e RGB split (banidos) e prova inventada [FATO, F32]; o bloco de 0,838 s por quadro pesa |
| 2. Tzur v2 enxuto, letreiro em 4 momentos | Mais limpo e barato | Pode parecer pouco "After Effects" para o pedido |
| 3. Tzur v2 fiel com legenda palavra a palavra | Legenda ajuda a entender sem som | Mantém os problemas da opção 1 |
| **4. Fora do óbvio: Tzur v2 enxuto com 6 letreiros que nascem atrás da cabeça e repousam acima dela, 2 inserts, legenda palavra a palavra e bloco final com granulação de semente fixa** | Mantém a assinatura (P&B que vira cor, letreiro 3D, bloco cinematográfico) sem banidos; rosto em 90,8% | O A vira o controle limpo da comparação com B e C; o ov2.html sai consertado (máscara, semente, duração por parâmetro) para o Tzur e para os próximos cases |

- Premissas: a correção da máscara (maior componente, sem y=470) funciona nos 783 quadros afetados [HIPÓTESE, teste em 4 quadros: 17,4 s, 19,4 s, 26,8 s e 33,9 s]. O letreiro em repouso na faixa de y 240 a 440 é legível [HIPÓTESE].
- **Posição: opção 4.**
- Probabilidade de cumprir produção e desempenho (alcance de 106 ou mais e pulo abaixo de 68%, se for o publicado): **0,42**, faixa [0,25, 0,60]. A produção sozinha: 0,85.
- Confiança: 0,4. O desempenho do formato Tzur v2 é sem dado [FATO, F19].

### D3 · Modelos B e C

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. B punchy (sab8a + gdgtify), C explainer de 5 cenas | Fácil de explicar | O C explainer tende a ter tela cheia de gráfico e menos rosto; sab8a tem 86 caracteres e não dá direção [FATO, F45] |
| 2. B tela dividida, C tipografia arquitetônica (gdgtify) | Atende o "dividindo" e o "4D" | Próximo da minha opção, mas a tela dividida genérica não diz nada sobre a tese |
| 3. Só B agora, C depois | Menos risco | Perde a chance de ter 3 moldes prontos para 4 nichos que gravam em 26/10 |
| 4. Não fazer B e C | Zero custo | Não atende "faça outros 2" do Bruno |
| **5. Fora do óbvio: B Lousa Dividida (a tela dividida é uma aula: o formato encena "ensinar o seu colega") e C Tabuleiro 4D (palavras sobem como peças de um tabuleiro atrás da cabeça e viram estrutura, ligando a peça à marca Xeque-Mate)** | Duas leituras literais do pedido ("dividindo com reacts e animações", "letreiro 4D atrás") com rosto em 100% | O B vira molde de explicação para nutri e psicólogo; o C vira assinatura visual da marca (tabuleiro) que pode abrir a série de carrosséis e a palavra TABULEIRO quando houver alcance de 150 |

- Premissas:
  - O júri cego dá ao B nota de clareza maior que a do A [PRIOR, P05].
  - O tabuleiro é lido como estrutura, não confunde [HIPÓTESE, risco principal do C].
  - A janela de 1080x1120 mostra cabeça e ombros sem nova ampliação [PRIOR, P19].
- **Posição: opção 5.**
- Probabilidade pelo critério (júri igual ou maior que o A, e, se publicado, 106 ou mais e pulo abaixo de 68%): **0,38**, faixa [0,20, 0,58].
  - Só a parte do júri: B 0,65 e C 0,55 [PRIOR].
  - O desempenho é N = 1, exploratório.
- Confiança: 0,3.

---

## 3. Ideias e hipóteses numeradas (85)

### Áudio
1. Expansor híbrido (transcrição ou energia) no lugar do só por transcrição. Confiança alta. Evidência: cauda de "produto." de 31,58 a 31,78 s em nível de fala [FATO, gate_teste.log].
2. Alvo de TP -1,5 dBTP antes do AAC. Alta. AAC subiu 0,1 dB no teste [FATO, ebur_aac.log].
3. Medir loudness sempre no MP4 final, nunca no WAV. Alta. Mesmo log; DR19.
4. Trocar o critério de 40 dB por piso no miolo das pausas abaixo de -45 dBFS. Média. piso_teste.log; P01 é PRIOR.
5. Um master de voz único para os 3 modelos. Alta. As 3 versões usam a mesma fala; evita 3 aprovações.
6. Silêncio total da trilha na quietude de 19,60 a 20,00 s. Média. gdgtify-929495 [FATO, F47].
7. Ouvir o evento de 13,56 s antes de decidir se tira. Alta. -12,5 dBFS no meio da pausa [FATO, gate_teste.log].
8. Não refazer a redução de ruído a partir do raw. Média. rn_bd ganha só 0,3 dB [FATO, DR02].
9. Voz 12 a 18 dB acima da trilha nas falas. Média. notdwd-998633 [FATO nível 2]; valor final PRIOR.
10. SFX na faixa de -18 a -24 dB do pico da voz. Baixa. P03 é PRIOR.
11. Room tone (piso de -60 dBFS) nas pausas em vez de silêncio digital, para não soar "buraco". Baixa. PRIOR de mixagem; nenhum dado na conta.
12. Guardar a cadeia como script versionado (master_voz.sh) em videos/nichos/dentista. Alta. B01: a cadeia do voz_master não está registrada [FATO].

### Modelo A
13. Letreiro nasce atrás da cabeça e repousa acima dela (y 240 a 440). Alta. Topo da pessoa de 252 a 555, mediana 420 [FATO, F29].
14. Tirar mk[:470]=0 do comp.py. Alta. 71,6% dos quadros passam de 470 [FATO, F29].
15. Manter só o maior componente conexo da máscara. Alta. 44 quadros com gente ao fundo [FATO, F30].
16. P&B até "474" (2,08 s) e cor no número. Média. Assinatura do Tzur [FATO, contexto.md]; efeito no pulo sem dado.
17. Tirar confete, tremida e RGB split. Alta. twoclipping-000267 bane [FATO, F48].
18. Tirar "1.287 comentários" e os @ fictícios. Alta. F32; regra de não inventar.
19. Granulação com semente pelo índice do quadro. Alta. R9 do F4.
20. Inserts limitados a 3,36 s (9,2%). Média. P09 (no máximo 30%) e F13 (rosto vence).
21. Duração e marcas do Tzur por parâmetro (sem 54,2 fixo). Alta. F34.
22. Trocar o pass do comp.py por erro quando faltar PNG. Alta. F33.

### Modelo B
23. Painel de cima como lousa de aula: o formato encena "ensinar o colega". Média. Leitura criativa; sem dado de desempenho.
24. Janela do Bruno recortada do base sem nova ampliação. Alta. F4 4.1.
25. Recorte que segue o centro da máscara, média móvel de 9 quadros. Média. F4 4.1.
26. Tela cheia de 0 a 5,16 s. Alta. Regra dos 3 s [FATO, CLAUDE.md].
27. Tela cheia em "Qual é? Ensinar o seu colega" como virada. Média. Contraste de layout no ponto de virada; PRIOR.
28. Reacts como stickers SVG com borda branca recortada. Alta. twoclipping-551116 [FATO, F43]; regra sem emoji.
29. Grade de 9 cartões iguais para "o mesmo diagnóstico". Média. Representa a fala literalmente; 06-plano-final cita 91% de 78 perfis com o mesmo formato [FATO nível 3 lá].
30. Pessoas que viram a palavra MERCADO. Média. gdgtify, palavra vira estrutura.
31. Planta de 5 nós em "desenho seu lançamento", sem nomear lances na tela. Média. Oferta Xeque-Mate 5 Lances [FATO, 00-SISTEMA.md]; nada prometido.
32. "DISPUTAR PACIENTE" riscado e "FORMAR QUEM DISPUTA" subindo. Alta. É a frase de contraste do roteiro [FATO, 06-plano-final.md linha 139].
33. Duas caixas para "segundo produto". Média. Representação direta.
34. Painel em JPEG por pipe. Alta. 0,08 s por quadro contra 0,10 a 0,23 s do PNG [FATO, F26].
35. Máscara só nos 12,0 s de tela cheia. Alta. Corta cerca de 380 s de composição [ESTIMATIVA, P9].

### Modelo C
36. Tabuleiro em perspectiva atrás da cabeça como palco do letreiro 4D. Média. Pedido literal de "letreiro 4D atrás"; marca Xeque-Mate [FATO, 00-SISTEMA.md].
37. Glifos de "474 MIL" sobem das casas como blocos. Média. techhalla mola por glifo [FATO, F46].
38. Órbita com a metade de trás escondida. Alta. twoclipping-041659 [FATO, F42] e camadas back e front do cap2.js.
39. "DIAGNÓSTICO" duplicado que tomba em "mesma conclusão". Média. Representa a fala; sem dado de desempenho.
40. TÉCNICA como viga, MERCADO como coluna, 2º PRODUTO pousado em cima. Média. gdgtify: a frase final se apoia nas anteriores [FATO, F47].
41. Linhas de planta no tabuleiro em "desenho seu lançamento". Média. Liga oferta e imagem.
42. CSS 3D em vez de Three.js. Alta. Custo medido só para CSS e HTML [FATO, F26]; Three.js sem dado.
43. Tabuleiro preso à parede pelo tr.trf. Baixa. B18, não testado.
44. Sem "fall through the head". Alta. Esconde o rosto; F13.
45. Fecho em ciclo (último quadro igual ao primeiro). Baixa. gdgtify; efeito em replay sem dado.
46. Versão reduzida do C pronta como fallback (sem órbita e sem estrutura). Alta. Compensa o ponto cego.
47. Contato de 20 stills antes do render. Alta. l3d1c-632524 e everestchris6 [FATO, F1 seção 5].

### Pipeline e execução
48. edit.json com eventos por índice de palavra. Alta. Permite regravar sem refazer a lista; 5 nichos gravam em 26/10 [FATO, 06-plano-final.md linha 158].
49. Base comum (áudio, máscara, edit.json) antes de qualquer modelo. Alta. Os três dependem dela.
50. Ordem A, B, C, em série, nunca em paralelo. Alta. F28: concorrência fica 2 a 5 vezes mais lenta.
51. Teste de 300 quadros por modelo antes do render cheio. Alta. B13.
52. Composição com filtros do ffmpeg onde não há máscara. Média. Overlay ffmpeg 0,071 s contra 0,52 s do numpy [FATO, F26].
53. Subquadros só nas janelas de movimento. Alta. F4 4.3; DR07.
54. Mistura de subquadros em alfa pré-multiplicado, não tmix em RGBA. Média. Hipótese de borda escura (B16).
55. render(t) puro, sem Math.random. Alta. R9.
56. Unsharp leve só na camada do Bruno. Baixa. P18.
57. Apagar PNG depois de compor. Alta. 0,5 a 2,4 GB por camada [ESTIMATIVA, DR15]; 18 GB livres [FATO, F21].
58. Gerar versão leve (cerca de 2,5 Mb/s) para envio ao Bruno por WhatsApp. Média. Tzur leve 2,55 Mb/s [FATO, F25].
59. Corte de escopo do C decidido em 27/10, 12h. Alta. Ponto cego.
60. Régua de QA da everestchris6: nada parado acima de 0,5 s fora da quietude, contraste 4,5:1, entende sem som. Média. F1 seção 5.

### Distribuição e crescimento
61. Publicar o B como reel principal em 29/10. Média. Rosto em 100% e resposta literal ao pedido; sem dado de desempenho.
62. Testar o C como trial reel (só não seguidores), se a conta tiver o recurso. Baixa. B23 sem dado; ig_trial_reels_change existe no Buzzfy, mas é escrita e só o Bruno decide.
63. Guardar o A como controle para o reel do consórcio ou do nutricionista. Média. Comparação entre nichos com N = 1; exploratório.
64. Capa do reel no quadro com "+474 MIL" atrás da cabeça. Média. Número específico ajudou o reel "90%" (165 de alcance) [FATO, 00-SISTEMA.md]; causalidade é hipótese.
65. Primeira linha da legenda do post igual ao hook falado. Média. F53 e F54 (texto no quadro 0).
66. Transformar os 7 painéis do B em carrossel da mesma semana. Média. Ritmo de 2 carrosséis por semana [FATO, CLAUDE.md]; reaproveita o render.
67. Stories no dia: enquete "Você já ensinou um colega?". Baixa. PRIOR; stories diários fazem parte do ritmo [FATO, CLAUDE.md].
68. Comentário fixado do Bruno repetindo "Comenta: dentista". Baixa. PRIOR.
69. Responder cada comentário de dentista em até 24 h com uma pergunta. Alta. Item 3 da seção 7 do 06-plano-final.md [FATO].
70. Usar o tabuleiro como assinatura visual recorrente da marca. Baixa. Hipótese de reconhecimento; sem dado.
71. Molde B para nutricionista e psicólogo (explicação) e molde C para consórcio (estrutura). Baixa. Encaixe por tema, PRIOR.
72. Não publicar os 3 do mesmo bruto na mesma semana. Média. P15 (sem precedente) e risco de canibalizar.
73. Versão de 15 s do B (hook e CTA) para stories. Baixa. PRIOR; reaproveitamento.
74. Título fixo de tese no quadro 0 em B e C, não só legenda. Média. F55: 4 de 4 com gancho "good" usam título fixo (N = 10, qualitativo).
75. Manter 36 s em vez de esticar para 60 a 80 s. Média. Statusphere e Kapwing se contradizem (C6); melhor reel do Bruno teve 18,6 s assistidos [FATO, F14].

### Medição e aprendizado
76. Registrar o resultado em semanas/2026-11-05.md com o modelo usado. Alta. Regra do Módulo 7 [FATO, CLAUDE.md].
77. Júri cego de 3 cadeiras primeiro sem som. Média. B25; 80,2% dos clipes com legenda sugere consumo sem som [nível 3, F61].
78. Ler ig_post_stats em 48 h e 7 dias. Alta. P13.
79. Anotar o tempo humano gasto em cada modelo. Alta. B13 e o ponto cego desta cadeira; sem esse dado o molde não tem custo conhecido.
80. Anotar o tempo de render cronometrado real de cada modelo. Alta. DR08 é estimativa.
81. Comparar o pulo do B com a mediana de 68%. Alta. F12.
82. Se B, C e A forem publicados em nichos diferentes, ler como exploratório e não como teste. Alta. 00-enquadramento D3 e D4.
83. Pedir ao Bruno a nota dele (0 a 10) para cada modelo antes de publicar. Média. B04; aprovação de primeira faz parte do critério da D1.
84. Medir a sincronia de legenda em 35,9 s ("respondo"). Alta. R2 do F4.
85. Se nenhum modelo passar de 53 de alcance em 48 h, voltar ao Bruno falando com corte simples no próximo nicho. Média. F13: o que vence é o rosto, não a edição.

---

## 4. Pre-mortem: como o plano da cadeira C fracassa

1. **O tempo humano estoura** e o consórcio (27/10) come a semana. O C nem começa e o B sai sem o painel bem acabado. Sinal precoce: base comum não pronta em 23/10. Resposta: o C sai reduzido, e o B usa cenas do modelo.html quase sem mudança.
2. **O tabuleiro confunde.** Dentista não lê o tabuleiro como estrutura e o C parece enfeite. Sinal: júri dá clareza abaixo de 6. Resposta: C sem tabuleiro, só a arquitetura de palavras.
3. **A tela dividida encolhe o rosto** e o pulo sobe, porque o aprendizado medido é "Bruno em cena", e em 67% do tempo ele fica na metade de baixo. Sinal: pulo acima da mediana de 68% em 48 h. Resposta: o próximo nicho usa o A ou o C.
4. **O letreiro "por trás" falha:** halo de 6 px e a máscara 1 quadro atrasada fazem o letreiro vazar na borda do cabelo. O "4D" parece colagem. Sinal: contato de 20 stills. Resposta: erodir mais e usar letreiro só em repouso acima da cabeça.
5. **O expansor come fala** que o alinhamento marcou errado (como em 31,58 s). Sinal: o Bruno ouve corte. Resposta: subir o limiar de energia ou desligar o expansor naquela pausa.
6. **O trecho de 24,94 a 29,04 s é mesmo embolado** e o Bruno não aceita. A regravação de 26/10 muda os tempos. Resposta: o edit.json por palavra existe exatamente para isso; se não estiver pronto, o atraso cai sobre o C.
7. **O nicho é estreito.** Mesmo bem editado, o reel fica perto de 50 a 90 de alcance, porque reels de terceiros falando com dentista sobre negócio tiveram de 78 a 764 views [FATO, F58 e 06-plano-final.md linha 29]. Resposta: separar efeito do nicho de efeito da edição comparando com o consórcio.
8. **Excesso de efeito.** O pedido puxa para "After Effects"; somando letreiro, reacts, painel e SFX, a peça fica barulhenta e o pulo sobe. Sinal: júri ou Bruno dizem "poluído". Resposta: cortar reacts primeiro, depois SFX.
9. **Risco de conselho.** Um CRO lê a grade de "perfis iguais" como crítica a colegas. Resposta: cartões genéricos sem nome; se houver dúvida, trocar por "O MESMO POST" sem grade.
10. **A comparação vira opinião.** Com N = 1, quem ganhar o júri vira "o melhor" sem dado. Resposta: tratar tudo como exploratório (ideia 82).

---

## 5. Previsões numéricas com data de conferência

Datas contadas a partir da publicação prevista, qui 29/10/2026. Todas [PRIOR], exceto onde indicado.

| Métrica | Valor previsto | Faixa | Conferir em | Fonte da leitura |
|---|---|---|---|---|
| Alcance do reel do dentista em 7 dias | 120 | 55 a 260 | 05/11/2026 | ig_post_stats |
| Pulo do reel do dentista em 7 dias | 62% | 50% a 74% | 05/11/2026 | ig_post_stats |
| Comentários com "dentista" em 7 dias | 3 | 0 a 12 | 05/11/2026 | listCommentAutomationLogs, ig_comments |
| D+30: reels publicados no molde (edit.json) entre os 5 nichos | 4 | 2 a 5 | 28/11/2026 | conteudo/sistema-instagram/semanas |
| D+30: tempo humano por reel novo no molde | 2 h | 1 a 4 h | 28/11/2026 | registro da ideia 79 |
| D+30: tempo de máquina por reel novo no molde | 15 min | 10 a 30 min | 28/11/2026 | registro da ideia 80 |
| D+60: mediana de alcance dos reels com o Bruno editados no molde | 95 | 60 a 160 | 28/12/2026 | ig_post_stats |
| D+60: pulo mediano desses reels | 63% | 55% a 72% | 28/12/2026 | ig_post_stats |
| D+90: conversas qualificadas de dentista somadas | 4 | 0 a 10 | 27/01/2027 | ig_comments e inbox, só leitura |
| D+90: diagnósticos agendados vindos de dentista | 1 | 0 a 3 | 27/01/2027 | agenda do Bruno (item 6 da seção 7 do 06-plano-final.md) |
| D+90: seguidores | 1.900 | 1.750 a 2.200 | 27/01/2027 | ig_account_stats (base 1.618 [FATO, F15]; ritmo atual +45 líquidos em 30 dias [FATO, 00-SISTEMA.md] daria cerca de 1.753 [ESTIMATIVA]) |

---

## 6. O que mudaria minha opinião

- Ouvir o trecho de 24,94 a 29,04 s (B02) e achar a fala embolada e inaceitável: a regravação de 26/10 vira o caminho, e o C cai para o nicho seguinte.
- O júri dar ao A clareza e acabamento acima de B e C: o A vira o principal e eu retiro a defesa do B.
- Teste de 300 quadros do C com custo acima de 2 vezes a estimativa: o C vai para a versão reduzida sem discussão.
- Métrica do Tzur v2, se ele tiver sido publicado (B06), com pulo bem abaixo de 68%: o A ganha peso como principal.
- O B03 mostrar que os eventos de 13,56 s e 31,6 s são ruído: o expansor precisa de edição manual nesses trechos e a D1 fica mais cara.
- O CRO ou o Bruno vetarem a grade de perfis: troca de cena no B8, no A5 e no C6.
- Primeiro reel do molde abaixo de 53 de alcance em 48 h: paro de investir em edição pesada e volto ao Bruno falando com corte simples (ideia 85).

## 7. Lacunas

- Não ouvi o áudio. As medições da P7 são numéricas; B02 e B03 só fecham no ouvido.
- Não abri os prompts do repositório nem as páginas do CFO. Uso F1, F3 e o livro de fatos.
- Não vi F2 por inteiro, só o resumo da tarefa.
- Tempo humano de produção: sem dado. As horas da seção 0.1 são PRIOR.
- Custo do tabuleiro em CSS 3D por quadro: sem dado.
- Se a conta tem trial reels: sem dado (B23).
- Leitura do tabuleiro pelo público dentista: sem dado, risco principal do C.
- Desempenho de tela dividida, react e letreiro atrás em talking head de negócio: sem dado em qualquer fonte [FATO, F66].
- O teste de áudio não incluiu trilha nem SFX. A medida que vale é a do MP4 final.

## 8. Fontes

- /home/user/Disparo-/videos/nichos/dentista/god/contexto.md, words-raw.json, transcricao-tempos.txt, frames-amostra.jpg
- /home/user/Disparo-/videos/nichos/dentista/god/run/00-enquadramento.md
- /home/user/Disparo-/videos/nichos/dentista/god/run/01-fatos.md (F01 a F76, C1 a C10, B01 a B25, DR01 a DR20, P01 a P22)
- /home/user/Disparo-/videos/nichos/dentista/god/run/01-pesquisa/F1-repo-opus-prompts.md e F4-viabilidade-pipeline.md
- /home/user/Disparo-/conteudo/modo-god-nichos/run/06-plano-final.md (seções 2.2 e 7, linhas 29, 77, 139, 158, 161, 194, 203)
- /home/user/Disparo-/conteudo/sistema-instagram/00-SISTEMA.md (ficha de entrada, melhores e piores)
- /home/user/Disparo-/CLAUDE.md
- Medições desta cadeira em /home/user/Disparo-/videos/nichos/dentista/god/run/02-cadeiras/evidencias-C/: gate_teste.py e gate_teste.log (expansor e distância fala e pausa), piso_teste.py e piso_teste.log (piso no miolo das pausas), ln_pass1.json, ebur_wav.log e ebur_aac.log (loudnorm em duas passadas e medida depois de AAC 192k), voz_C_teste.wav e voz_C_teste.m4a (só voz, sem trilha, não é entrega)
- ffprobe do base.mp4 (encoder libx264) e conferência de scipy 1.18.1 no cbenv, 21/10/2026
