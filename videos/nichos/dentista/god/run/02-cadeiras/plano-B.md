# Cadeira B · Performance de mídia paga · Reel do dentista · Agência Reunida Modo GOD · 21/10/2026

Cliente: O Estrategista (@o_estrategista.com.br). Trabalho isolado: não li nenhum outro plano de cadeira.

| Campo | Conteúdo |
|---|---|
| Persona | Diretor de performance em Google Ads e Meta Ads, com anos de leilão B2B e B2C no Brasil |
| OTIMIZA PARA | Lead qualificado ao menor custo com controle do leilão |
| PONTO CEGO (assumido) | Subestimo canais de demanda criada, difíceis de medir. Aqui isso é perigoso, porque o reel orgânico é exatamente demanda criada e a verba é zero até 18/11/2026 [FATO, 06-plano-final.md linha 236]. Compensação escrita: (1) não descarto nada por "não ter atribuição"; (2) uso proxies medidos (pulo, tempo assistido, visita ao perfil, comentário de dentista, DM) em vez de exigir conversão rastreada; (3) trato o reel como criativo que também vai a leilão depois, e desenho para isso |
| PERGUNTA CONTRÁRIA | E se a busca não tiver volume para crescer no ritmo que o cliente quer? Resposta na seção 2.0 |

Etiquetas: [FATO] com fonte · [ESTIMATIVA] com a conta · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, nível 4, nunca fecha objeção sozinho.
Fontes de base: run/01-fatos.md (F01 a F76, C1 a C10, B01 a B25, DR01 a DR20, P01 a P22), run/01-pesquisa/F1 a F4, contexto.md, 00-enquadramento.md, words-raw.json, 06-plano-final.md, 00-SISTEMA.md. Evidência nova desta cadeira: run/02-cadeiras/evidencias-B/meta-ad-library-2026-10-21.md.

---

## 1. Veredito (12 linhas)

1. Fazer os 3 modelos do mesmo bruto, sem cortar pausa nenhuma: os 1093 quadros ficam presos a words-raw.json e a máscara pronta serve aos 3 [FATO, F27; DR04].
2. A = Tzur v2 enxuto com legenda palavra a palavra; sem confete, sem aplauso, sem "1.287 comentários" nem @ inventado [FATO, F32].
3. B = tela dividida com reacts e animação que representa a fala (stokebuilder-356793 + twoclipping-551116 + twoclipping-000267 + quietude do gdgtify-929495).
4. C = arquitetura de palavras atrás da cabeça com órbita (twoclipping-041659 + gdgtify-929495 + techhalla-498547 + alex-prompter-997524) e um título fixo que qualifica o público, feito para servir de criativo de anúncio em 4:5 depois.
5. Áudio: remasterizar a partir do voz_master.wav, mistura em numpy, loudnorm em duas passadas com TP -1,5 no PCM para cair até -1,0 dBTP depois do AAC, medido no MP4 final.
6. Antes de qualquer render: ouvir 24,94 a 29,04 s (B02) e as pausas de 13,37 e 31,63 s (B03). São 10 minutos e mudam legenda e cadeia de áudio.
7. Publicar em 29/10 o C como reel principal [HIPÓTESE, evidência fraca: F55]; A e B ficam como variantes.
8. Comparar modelos no orgânico é ruído (N = 1). A comparação limpa é um teste de criativo pago com os 3 no mesmo conjunto, só depois de 18/11 e só com teto escrito pelo Bruno.
9. Tela: "474 MIL" com rodapé "Soma dos 27 CROs · CFO, out/2026". Nunca "mais de 474 mil pessoas": a tabela pode contar inscrição duplicada [FATO, F68; B19].
10. Tzur fora da tela: não foi dito e a autorização não está confirmada [FATO, F10; B24].
11. Busca não é o canal deste produto: 1.432 anúncios ativos de "curso para dentistas" na Meta contra 13 de "lançamento curso odontologia" [FATO, Ad Library 21/10/2026]. Leitura: a demanda é criada no feed [HIPÓTESE].
12. Probabilidade de o reel publicado bater 106 de alcance e pulo abaixo de 68% em 7 dias: 0,45 [PRIOR com base em 3 reels do Bruno, faixa 0,25 a 0,65].

---

## 2. Resposta às perguntas

### 2.0 Pergunta contrária: e se a busca não tiver volume?

- Volume de busca no Google para "lançamento de curso para dentista" e afins: sem dado. Não tenho Planejador de Palavras-chave nem Google Trends nesta sessão, e não vou estimar.
- O que medi no lugar [FATO, ads_library_search, BR, ativos, 21/10/2026, evidencias-B]: "curso para dentistas" 1.432 anúncios ativos; "mentoria para dentistas" 335; "lançamento curso odontologia" 13. A contagem é teto (casa por palavra, inclui anúncio para paciente e de faculdade).
- Leitura [HIPÓTESE]: existe um mercado grande de dentista ensinando dentista, e ele compra atenção no feed da Meta, não em busca. O nosso cliente ideal (dentista com técnica que colega quer aprender) já está anunciando curso. Quem compra "estrategista de lançamento" quase nunca digita isso.
- Consequência para a cadeira: se a busca não tem volume, não existe leilão de busca para controlar. O crescimento tem de vir de demanda criada (reel) e, depois de 18/11, de distribuição paga do criativo que provar retenção. Por isso o modelo C é desenhado para virar anúncio (4:5, título que qualifica, entende sem som).
- O que mudaria isso: se o Bruno tiver acesso a uma conta Google Ads com Planejador e o volume mensal de termos como "como vender curso odontologia" passar de algumas centenas, abro um teste de busca pequeno. Hoje: sem dado.

### 2.1 Modelo que a cadeira defende e ids do repositório (pergunta 1)

Defendo produzir os 3 e publicar o C como principal. Motivo de performance: o C é o único que serve aos dois canais sem reedição (reel 9:16 hoje, anúncio 4:5 depois) e segue o único padrão de abertura com algum dado (título fixo com a tese em 4 de 4 reels de negócio ou saúde com gancho "good" [FATO nível 2, F55; N = 10, rating qualitativo]).

| Modelo | Ids misturados | Aproveita | Descarta |
|---|---|---|---|
| A | sab8a-475686, techhalla-498547, twoclipping-000267 | sab8a: contrato mínimo (legenda, grafismo, música). techhalla: mola por glifo com 125 ms e punch-in 1,00 a 1,08. 000267: lista de banidos, SFX pelo pico, -14 LUFS, cuidado com preserve-3d | techhalla: desalinhamento magenta e verde (é RGB split) e a paleta. Do Tzur: confete (partícula), aplauso, RGB split, tremida, contador e @ inventados [FATO, F32] |
| B | stokebuilder-356793, twoclipping-551116, twoclipping-000267, gdgtify-929495 | stokebuilder: rosto sempre visível quando o gráfico entra, texto fiel ao que foi dito, rosto entre gráficos. 551116: stickers recortados como reacts (em SVG), letras subindo por máscara, nada com pop seco. 000267: banidos e SFX pelo pico. gdgtify: quietude antes da virada | stokebuilder: meta de 35 a 50 momentos e PiP pequeno no canto (a fonte é 576x1024). 551116: quadrado 1440x1440, 8 subquadros (uso 3), números de views contando |
| C | twoclipping-041659, gdgtify-929495, techhalla-498547, alex-prompter-997524, twoclipping-000267 | 041659: órbita com metade de trás atrás da cabeça, palavra marcada no instante falado. gdgtify: palavras viram estrutura, relógio pela fala, quietude. techhalla: mola por glifo. alex-prompter: as 5 cenas mapeadas na fala (problema 0 a 13,84 s; caminho 13,84 a 22,70 s; o que eu faço 22,70 a 24,46 s; posição 24,46 a 32,00 s; chamada 32,00 a 35,92 s). 000267: 3 subquadros só no movimento | 041659: mapa de calor, pixel art, 4:3. gdgtify: palco só tipográfico sem pessoa (animação sem rosto falhou, F13). alex-prompter: cena de "prova" e "3 passos" que a fala não tem |

### 2.2 Rosto (pergunta 2)

| Modelo | Rosto de 0 a 3 s | Rosto visível no tempo total | Zoom máximo |
|---|---|---|---|
| A | Sim, tela cheia | 95,8% [ESTIMATIVA: 36,43 s menos 1,52 s de b-roll em tela cheia (A08), dividido por 36,43] | 1,08x (2,03x da fonte, conta 1,875 x 1,08) |
| B | Sim, tela cheia até 5,48 s | 100%. Em tela cheia 37,1% do tempo [ESTIMATIVA: 5,48 + 3,20 + 4,85 = 13,53 s de 36,43]; no resto, na janela 1080x1120 sem nova ampliação, então o rosto tem o mesmo tamanho em pixels | 1,00x (troca de layout no lugar de zoom) |
| C | Sim, tela cheia | 100% | 1,06x |

Os três ficam abaixo do teto de 1,25x e do critério de 80% (P16).

### 2.3 Listas de edição quadro a quadro (pergunta 3)

Regras comuns aos 3: saída 1080x1920, 30 fps, 1093 quadros, 36,43 s, base.mp4 como fonte (mesmos 1093 quadros do bruto, F02); frame = arredondar(t x 30); nenhuma pausa cortada; evento visual 2 quadros antes da palavra quando é entrada; SFX posicionado pelo pico medido (F35); máscara com maior componente conexo e sem o corte fixo em y=470 (F29, F30); render(t) puro, com semente pelo índice do quadro (F32). Zona útil 9:16: y 220 a 1470 [PRIOR, F63]. Zona útil 4:5 central: y 285 a 1635 [ESTIMATIVA: (1920 - 1350) / 2 = 285].

#### Modelo A · Tzur v2 enxuto com legenda

| # | Início s (frame) | Fim s (frame) | Palavra gatilho (words-raw.json) | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|---|
| A01 | 0,00 (0) | 2,08 (62) | Dentistas | base + frente | Legenda palavra a palavra 'DENTISTAS,' desde o frame 0 (y 1330 a 1470) | Base em P&B (saturação 0); punch-in 1,00 para 1,03 linear | sub a -24 dB no frame 0 |
| A02 | 1,58 (47) | 3,18 (95) | mais / de | áudio | sem texto | riser começa 1,58 s para o pico cair em 3,18 s (pico do arquivo 1596,6 ms) | riser |
| A03 | 2,08 (62) | 4,80 (144) | 474 | atrás | '474 MIL' dourado #E8B36A, faixa y 300 a 560 (passa atrás do topo da cabeça) | Volta da cor em varredura de 0,35 s; extrusão de 14 text-shadow, rotateX 55 para 0 em 0,55 s, mola por glifo com 125 ms entre letras | impact com pico em 2,63 s (fim da extrusão) |
| A04 | 2,08 (62) | 5,16 (155) | 474 | frente | Rodapé 'Soma dos 27 CROs · CFO, out/2026' (y 1440, 34 px) | Fade de 0,2 s | nenhum |
| A05 | 3,80 (114) | 5,16 (155) | colegas | frente | Legenda 'COLEGAS ATIVOS NO BRASIL' (corrigida de 'em') | Palavra ativa em dourado | nenhum |
| A06 | 5,48 (164) | 7,12 (214) | porque | frente | Legenda 'POR QUE VOCÊ AINDA SÓ' | Palavra ativa em dourado | nenhum |
| A07 | 7,68 (230) | 9,36 (281) | hora | atrás + frente | Atrás: 'HORA DE CADEIRA'. Frente: react SVG de relógio desenhado ao lado do ombro esquerdo | Letreiro entra como A03; relógio por stroke-dashoffset em 0,35 s com curva amortecida | tick com pico em 7,68 s |
| A08 | 11,14 (334) | 12,66 (380) | mesmo | tela cheia | B-roll creme: grade 3x3 de cartões de post idênticos, rótulos 'DIAGNÓSTICO' e 'CONCLUSÃO' (palavras ditas), sem dente nem boca | Entra por wipe dourado de 0,30 s; os 9 cartões viram juntos em 12,24 s | swipe com pico em 11,14 s |
| A09 | 12,66 (380) | 13,84 (415) | mesma / conclusão. | base | Volta ao rosto; legenda 'A MESMA CONCLUSÃO.' | Respiro de 0,30 s antes da troca (regra do Tzur) | whoosh com pico em 12,66 s |
| A10 | 15,08 (452) | 17,92 (538) | técnica | atrás | 'TÉCNICA' (vai virar a peça de apoio em A17) | Mola por glifo; fica parado depois de entrar | pop com pico em 15,63 s |
| A11 | 16,04 (481) | 17,92 (538) | dentistas | frente | React SVG: quadro de aula com 3 cabeças genéricas em traço | Traço desenhando em 0,40 s | nenhum |
| A12 | 17,92 (538) | 19,50 (585) | existe | atrás | 'UM MERCADO' | Mola por glifo | nenhum |
| A13 | 19,50 (585) | 20,10 (603) | (pausa) | todas | Tudo sai em 19,50 s; tela só com o Bruno | Quietude de 600 ms (gdgtify-929495): sem SFX, trilha descendo 12 dB | nenhum |
| A14 | 20,10 (603) | 20,64 (619) | Qual | frente | Legenda 'QUAL É?' maior (120 px) | Corte seco de tipo, sem efeito | nenhum |
| A15 | 20,64 (619) | 22,22 (667) | ensinar | atrás + base | 'ENSINAR O SEU COLEGA' | Punch-in 1,00 para 1,08 em 0,40 s, curva amortecida | whoosh com pico em 20,64 s (começa em 20,37 s, depois da quietude) |
| A16 | 22,70 (681) | 24,24 (727) | Eu | frente | Tarja 'Bruno · Estrategista de Lançamento' (y 1230) | Entrada lateral 0,35 s; punch-in volta a 1,00 | swipe com pico em 22,70 s |
| A17 | 26,38 (791) | 27,24 (817) | paciente | atrás | 'PACIENTE' riscado por traço dourado | Risco desenhado em 0,30 s | tick com pico em 26,88 s |
| A18 | 24,46 (734) | 29,04 (871) | você ... disputa. | frente | Legenda conforme decisão da pergunta 4 (ouvir antes, B02) | Palavra ativa em dourado | nenhum |
| A19 | 29,28 (878) | 31,58 (947) | Sua | atrás + frente | Atrás: 'TÉCNICA' de A10 desce e vira base; '2º PRODUTO' pousa em cima em 30,78 s. Frente: react SVG de duas caixas | Mola; caixas por traço | ding_si com pico em 31,18 s |
| A20 | 31,58 (947) | 32,00 (960) | (pausa) | atrás | Letreiros saem | Saída de 0,35 s | nenhum |
| A21 | 32,00 (960) | 35,92 (1078) | Dentista | frente | Cartão 'COMENTA: DENTISTA' com balão de comentário SVG e seta para baixo (y 1180 a 1420). Nenhum contador, nenhum @ | Digitação de 'DENTISTA' em 32,68 s; seta pulsa 2 vezes | typing com o primeiro clique em 32,68 s |
| A22 | 35,92 (1078) | 36,43 (1093) | respondo. | frente | '@o_estrategista.com.br' com varredura de luz | Varredura de 0,40 s, granulação com semente pelo índice do quadro | nenhum |

Legenda palavra a palavra (camada da frente) roda em todo o vídeo, grupos de até 4 palavras, y 1330 a 1470, palavra ativa em #E8B36A, exceto durante A08.

#### Modelo B · Tela dividida com reacts e animação que representa a fala

| # | Início s (frame) | Fim s (frame) | Palavra gatilho (words-raw.json) | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|---|
| B01 | 0,00 (0) | 5,48 (164) | Dentistas | tela cheia + frente | Legenda palavra a palavra desde o frame 0 | Rosto em tela cheia, sem zoom | nenhum |
| B02 | 2,08 (62) | 5,16 (155) | 474 | frente | Contador '474 MIL' (y 1120 a 1300, abaixo do queixo) e rodapé 'Soma dos 27 CROs · CFO, out/2026' | Contador de 0 a 474 em 0,9 s, desaceleração exponencial, termina em 2,98 s | coin com pico em 2,98 s |
| B03 | 3,18 (95) | 4,80 (144) | mil | atrás | 'MIL' curto atrás da cabeça (o único letreiro atrás antes do painel) | Extrusão como A03 | nenhum |
| B04 | 5,48 (164) | 5,83 (175) | porque | tela dividida | Painel 1080x800 desce no topo; Bruno passa para a janela de baixo 1080x1120, recorte que segue o centro da máscara | Deslocamento de 0,35 s, x(t) = 1 - (1 + wt)e^(-wt), sem quique; linha dourada de 4 px | whoosh com pico em 5,83 s |
| B05 | 5,83 (175) | 9,36 (281) | hora / cadeira | tela dividida (painel) | Relógio SVG grande; rótulo 'HORA DE CADEIRA' em 8,30 s. Sem ícone de cadeira odontológica | Ponteiros giram e travam em 8,80 s | tick a cada 0,5 s de 7,68 a 8,80 s, -26 dB |
| B06 | 9,36 (281) | 13,32 (400) | quase / mesmo / diagnóstico | tela dividida (painel) | Grade 3x3 de cartões de post; rótulos 'DIAGNÓSTICO' em 11,38 s e 'CONCLUSÃO' em 12,66 s | Cartões aparecem copiados um do outro (carimbo); viram juntos | shutter com pico em 11,38 s e 12,66 s |
| B07 | 13,84 (415) | 17,92 (538) | Se / técnica / dentistas | tela dividida (painel) | Figura em traço no centro com 3 figuras olhando; balões vazios com reticências (sem frase inventada) | Balões sobem por máscara, um a cada 0,30 s a partir de 16,04 s | pop com pico em 16,04, 16,34 e 16,64 s |
| B08 | 17,92 (538) | 19,50 (585) | existe / mercado. | tela dividida (painel) | Porta em traço que abre; rótulo 'UM MERCADO' | Porta gira em 0,6 s | nenhum |
| B09 | 19,50 (585) | 20,10 (603) | (pausa) | tela cheia | Painel sobe; Bruno volta à tela cheia | Deslocamento de 0,35 s e depois quietude: sem SFX, trilha descendo 12 dB | whoosh com pico em 19,50 s, curto |
| B10 | 20,10 (603) | 22,70 (681) | Qual / ensinar | atrás + tela cheia | Atrás: 'ENSINAR' grande (o pedido de letreiro 4D aparece aqui no B) | Extrusão como A03, entra em 20,64 s | impact com pico em 21,19 s |
| B11 | 22,70 (681) | 24,46 (734) | Eu / desenho | tela dividida (painel) | Linha do tempo em traço que se desenha da esquerda para a direita, 5 nós sem rótulo | Traço segue a voz de 22,82 a 24,24 s | nenhum |
| B12 | 24,46 (734) | 29,28 (878) | você ... disputa. | tela dividida (painel) | 'PACIENTE' riscado em 26,38 s; plano abre e mostra a figura ensinando um grupo | Zoom-out do painel (só o painel, nunca o rosto) | swipe com pico em 26,88 s |
| B13 | 29,28 (878) | 31,58 (947) | Sua / segundo / produto. | tela dividida (painel) | Caixa 'TÉCNICA' se duplica em '2º PRODUTO' | Duplicação com deslocamento lateral 0,4 s | ding_si com pico em 31,18 s |
| B14 | 31,58 (947) | 32,00 (960) | (pausa) | tela cheia | Painel sobe; tela cheia | Deslocamento de 0,35 s | whoosh com pico em 31,93 s |
| B15 | 32,00 (960) | 35,92 (1078) | Dentista / comenta | frente | Balão de comentário SVG 'DENTISTA' e seta (y 1180 a 1420) | Digitação em 32,68 s | typing com o primeiro clique em 32,68 s |
| B16 | 35,92 (1078) | 36,43 (1093) | respondo. | frente | '@o_estrategista.com.br' | Fade 0,3 s | nenhum |

Legenda palavra a palavra sobre a linha divisória (y 780 a 860) durante a tela dividida e em y 1330 a 1470 em tela cheia. Painel em JPEG por pipe (capture.js), reacts em SVG próprio, nenhum glifo de coração, check ou X como texto, nenhum emoji.

#### Modelo C · Arquitetura de palavras e órbita, pronto para anúncio

| # | Início s (frame) | Fim s (frame) | Palavra gatilho (words-raw.json) | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|---|
| C01 | 0,00 (0) | 31,58 (947) | Dentistas | frente (título fixo) | 'PARA DENTISTA QUE DOMINA UMA TÉCNICA' (y 300 a 420, dentro do recorte 4:5) | Entra pronto no frame 0, sem animação | nenhum |
| C02 | 0,00 (0) | 35,92 (1078) | todas | frente (legenda) | Legenda palavra a palavra, 2 a 4 palavras por vez (y 1330 a 1470) | Cinza para branco em 0,2 s no tempo da palavra (notdwd-998633) | nenhum |
| C03 | 2,08 (62) | 5,16 (155) | 474 / mil | atrás + frente | Órbita fina dourada em volta da cabeça; '474 MIL' corre na órbita e passa atrás na metade de trás. Rodapé 'Soma dos 27 CROs · CFO, out/2026' | Órbita se desenha em 0,5 s (twoclipping-041659); 3 subquadros de motion blur só no desenho | riser com pico em 3,18 s |
| C04 | 7,68 (230) | 9,36 (281) | hora / cadeira | atrás | 'HORA DE CADEIRA' vira viga deitada na parede atrás da cabeça | Assenta com curva amortecida | sub com pico em 8,30 s |
| C05 | 11,38 (341) | 13,32 (400) | diagnóstico / conclusão | atrás | A viga trinca no meio em 12,66 s | Trinca por máscara, sem partícula | tick com pico em 12,66 s |
| C06 | 15,08 (452) | 17,92 (538) | técnica | atrás | 'TÉCNICA' sobe de trás do ombro e vira pilar vertical à esquerda | Mola por glifo, 125 ms entre letras (techhalla-498547) | pop com pico em 15,63 s |
| C07 | 19,12 (574) | 19,50 (585) | mercado. | atrás | 'MERCADO' vira viga horizontal no topo | Assenta em 0,3 s | nenhum |
| C08 | 19,50 (585) | 20,10 (603) | (pausa) | todas | Tudo congela | Quietude de 600 ms: sem SFX, trilha a -inf, nenhum quadro de movimento | nenhum |
| C09 | 20,64 (619) | 22,22 (667) | ensinar | atrás | 'ENSINAR' vira pilar vertical à direita | Mola; punch-in lento 1,00 para 1,06 de 20,64 a 31,58 s | whoosh com pico em 20,64 s |
| C10 | 26,38 (791) | 27,24 (817) | paciente | atrás | Viga 'HORA DE CADEIRA' cai para fora de quadro | Queda com gravidade, 0,5 s, motion blur de 3 subquadros | impact com pico em 26,88 s |
| C11 | 30,78 (923) | 31,58 (947) | segundo / produto. | atrás | '2º PRODUTO' pousa como telhado sobre os pilares 'TÉCNICA' e 'ENSINAR' | Pouso de 0,4 s, sem quique | ding_si com pico em 31,18 s |
| C12 | 31,58 (947) | 32,00 (960) | (pausa) | atrás + frente | Título fixo sai; estrutura encolhe para um ponto | 0,35 s | whoosh com pico em 31,93 s |
| C13 | 32,00 (960) | 35,92 (1078) | Dentista / comenta | frente | Balão 'COMENTA: DENTISTA' no lugar do título (y 300 a 420) | Digitação em 32,68 s | typing com o primeiro clique em 32,68 s |
| C14 | 35,92 (1078) | 36,43 (1093) | respondo. | frente | '@o_estrategista.com.br' | Fade 0,3 s | nenhum |

Entregas do C: 9:16 (1080x1920) e 4:5 (1080x1350, recorte y 285 a 1635). Título, legenda e rodapé ficam dentro do recorte 4:5, então o mesmo render serve ao anúncio sem refazer texto [ESTIMATIVA de faixa, conta acima].

### 2.4 Trecho 24,94 a 29,04 s (pergunta 4)

- Primeiro ouvir (B02, cerca de 5 min). Sem isso, nenhuma legenda desse trecho é renderizada.
- Se o Bruno disse "formar quem disputa": legenda normal com esse texto.
- Se disse mesmo "forna que a gente disputa": legenda fiel até "passa a" (27,58 s) e, de 27,58 a 29,04 s, a legenda dá lugar ao letreiro "PACIENTE" riscado (A17, B12, C10). Letreiro é ilustração, não transcrição, então não põe na boca do Bruno palavra que ele não disse. Corte de fala: proibido.
- Regravação: só se o Bruno achar o trecho inaceitável ao ouvir. A sessão de 26/10 já está marcada [FATO, 06-plano-final.md linha 158]; como as 3 listas são paramétricas em words-raw.json, uma tomada nova custa só alinhar de novo e renderizar (47 a 53 min, DR08). Regravar só o áudio do trecho: não, porque desalinha da boca.

### 2.5 "em Brasil" (pergunta 5)

Legenda corrigida para "no Brasil". Motivo de performance: quem assiste sem som lê a legenda, e erro de preposição custa credibilidade na abertura, onde o pulo é decidido. Corrigir preposição não muda sentido nem cria fato. A diferença dura 0,16 s (4,80 a 4,96 s) [FATO, words-raw.json].

### 2.6 474 mil (pergunta 6)

"474 MIL" com rodapé "Soma dos 27 CROs · CFO, out/2026", 2,08 a 5,16 s. Não escrever "mais de 474 mil dentistas": a página não diz se conta pessoa ou inscrição e a soma pode duplicar quem tem inscrição secundária [FATO, F68; B19 aberto]. O Bruno fala "mais de 474 mil colegas"; a fala fica, o texto na tela é o que a fonte sustenta.

### 2.7 Áudio (pergunta 7)

Cadeia, na ordem:
1. Ouvir B02 e B03. Se as pausas de 13,37 a 13,79 s e 31,63 a 31,95 s forem cauda de palavra ou respiração, não mexer; se forem ruído, aplicar o passo 3.
2. Fonte: voz_master.wav (-14,2 LUFS, TP -0,5 dBTP) [FATO, F04]. Filtro passa-alta em 80 Hz, de-esser leve (deesser do ffmpeg), sem EQ agressivo.
3. Expansor para baixo só nas 8 janelas de pausa de words-raw.json (F07), com 40 ms de rampa em cada borda e atenuação de até 12 dB [HIPÓTESE: fecha a distância fala e pausa sem soar cortado; testar no ouvido].
4. Trilha lounge do som.py, mistura em numpy por amostra a 48 kHz: 14 dB abaixo da voz no curto prazo durante a fala (dentro dos 10 a 15 dB do notdwd-998633, F1 seção 5), ducking de 6 dB pela voz, descida de 12 dB na quietude de 19,50 a 20,10 s (A e B) e silêncio total no C.
5. SFX: pico entre 18 e 24 dB abaixo do pico da voz [PRIOR, P03], posição pelo pico medido (F35).
6. loudnorm em duas passadas (medir e aplicar com measured_I, measured_TP, measured_LRA, linear=true): I -14, TP -1,5, LRA 7. TP -1,5 no PCM porque a codificação AAC pode subir o pico [PRIOR: valor do sobressinal não medido aqui]; o alvo continua -1,0 dBTP no arquivo final (resolve o conflito C7 a favor da medida final).
7. Medir no MP4 final de cada modelo: ffmpeg ebur128=peak=true. Aceite: -15 a -13 LUFS e TP até -1,0 dBTP. Voz acima da trilha em todas as janelas de fala (DR20).
8. Critério dos 40 dB: medir no stem de voz. Na mistura a trilha ocupa as pausas por desenho, então o número não diz nada sobre ruído. Hoje nenhuma versão chega a 40 dB pelo método do DR02 (melhor média: rn_bd 16,3 dB) [FATO, DR02]; o 40 dB é PRIOR (P01) e eu proponho trocar por "nenhum ruído audível na escuta do Bruno nas 8 pausas".

### 2.8 Upscale (pergunta 8)

- Manter base.mp4 (1080x1920, 30 fps, mesmos 1093 quadros) como fonte dos 3, porque a máscara foi feita nele [FATO, F02, F27]. Método de ampliação dele: sem dado (B17); ler o metadado antes do render.
- Zoom máximo 1,08x: 2,03x da fonte [ESTIMATIVA: 1,875 x 1,08]. Fica longe dos 2,34x do teto (DR06).
- Riscos: halo de 6 px na borda da máscara (F31), atraso de cerca de 1 quadro em movimento rápido (F4 R4), gente ao fundo em 44 quadros (F30). Mitigação: maior componente conexo, erosão e desfoque de 2 a 4 px na borda, letreiro que não brigue com a cor do cabelo.
- Unsharp leve depois da ampliação: só se um quadro de teste mostrar ganho (P18).

### 2.9 Pipeline e tempo (pergunta 9)

Só o que existe: Playwright + Chromium, ffmpeg 6.1.1, numpy, scipy, rembg (já rodado), HTML/SVG. Nada instalado.
Tempo [ESTIMATIVA, F4 seção 2.1, a partir de custos medidos por quadro]: A cerca de 951 s, B cerca de 887 s, C 1008 a 1319 s; os 3 em série 47 a 53 min com a máscara pronta. Não rodar em paralelo (2 a 5 vezes mais lento, F28). Antes do render cheio: 300 quadros cronometrados por modelo (B13) e conferência de 1093 PNG por camada (F33). A exportação 4:5 do C: 1 passada de crop no ffmpeg, cerca de 0,072 s por quadro [ESTIMATIVA a partir do x264 medido, F26: 1093 x 0,072 = 79 s].

### 2.10 CTA (pergunta 10)

Usa o gravado "Dentista, comenta a sua profissão aqui que eu te respondo" (32,00 a 35,92 s). Na tela: "COMENTA: DENTISTA" com balão SVG e seta. Nada de contador nem nome fictício. TABULEIRO não entra no vídeo; vai para o comentário fixado só se o alcance passar de 150 em 48 h [FATO, CLAUDE.md]. A promessa "eu te respondo" exige resposta do Bruno em até 24 h [FATO, 06-plano-final.md seção 7].

### 2.11 Publicidade odontológica (pergunta 11)

A Res. 196/2019 já foi lida no texto oficial (F72), então essa pendência caiu. Nos 3 modelos: sem boca, dente, raio X, procedimento, instrumental, antes e depois, preço, "grátis", promessa de faturamento ou de agenda [FATO, F72, F73]. Evito também ícone de cadeira odontológica (equipamento; leitura conservadora do F72, HIPÓTESE). "Sua técnica vira um segundo produto" é fala do Bruno sobre negócio; não vai para título nem para anúncio pago como promessa.

### 2.12 Prova Tzur (pergunta 12)

Fora da tela. Não foi dito (F10), a autorização em vídeo segue aberta (B24) e um número de faturamento em reel para dentista pode ser lido como promessa de resultado [HIPÓTESE]. A prova desta peça é o número do CFO com fonte.

### 2.13 Métrica, fonte, data e critério de parar (pergunta 13)

| Métrica | Fonte | Leitura | Critério |
|---|---|---|---|
| Alcance, views, tempo médio assistido, pulo | ig_post_stats (Buzzfy) | 31/10 (48 h) e 05/11/2026 (7 dias) | Meta: alcance >= 106 e pulo < 68% (D2, D3). Registro também do corte de 60% do plano (C1) |
| Comentários com a profissão | ig_comments (Buzzfy) e listCommentAutomationLogs (PostZen), só leitura | 30/10 e 05/11 | >= 2 de dentista em 7 dias [PRIOR] |
| DM qualificada de dentista (tem técnica e audiência) | planilha de leads | 05/11 e 28/11 | >= 1 até 28/11 |
| Visitas ao perfil vindas do reel | ig_post_stats | 05/11 | registro, sem meta (sem base por post) |
| Parar | | 05/11 | alcance < 53 e pulo > 75%: parar o modelo publicado nesse nicho [FATO, 06-plano-final.md seção 4] |
| Teste pago dos 3 criativos (só depois de 18/11 e com teto escrito) | Gerenciador de Anúncios, só leitura por mim | 4 dias após ligar | métrica: visualizações de 3 s / impressões e ThruPlay / impressões; vence quem abrir 5 pontos percentuais de vantagem com pelo menos 900 impressões por criativo [ESTIMATIVA: n = 1,96² x 0,3 x 0,7 / 0,03² = 896, para margem de 3 pontos com taxa perto de 30%, PRIOR] |

### 2.14 Regras de texto (pergunta 14)

Português do Brasil, nenhum travessão, nenhum emoji, nenhuma frase "não é X, é Y" na tela dos 3 modelos, nenhuma menção aos três nomes vetados no CLAUDE.md. Conferência automática antes do render: busca pelos caracteres U+2014 e U+2013 e pelos intervalos Unicode de emoji nos HTML e na lista de edição.

---

## 3. Decisões

### D1 · Áudio masterizado

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. voz_master.wav como está | Zero trabalho | TP -0,5 estoura depois da trilha e dos SFX; reprova no critério (F04, DR01) |
| 2. Remasterizar do voz_master (cadeia da 2.7) | Fecha loudness e TP com medida no arquivo final | Uma cadeia só para os 3; se B03 mostrar ruído, o expansor resolve sem voltar ao raw |
| 3. Refazer do raw.wav comparando rn_std, rn_sh, rn_bd | Pode achar redução melhor | Mais 1 a 2 h de escuta; DR02 mostra diferença pequena entre as versões (14,3 a 16,3 dB) |
| 4. Fora do óbvio: trocar o critério de 40 dB por escuta do Bruno nas 8 pausas e medir ruído no stem de voz | Critério passa a medir o que importa | Acaba a discussão de número sem método (P01); exige o Bruno ouvir 8 trechos |
| 5. Regravar só o áudio de 24,94 a 29,04 s | Corrige a fala | Desalinha da boca; inviável num talking head |

- Premissas: voz_master é a melhor base (B01 aberto); o AAC sobe o pico em menos de 0,5 dB [PRIOR]; o Bruno aprova pelo ouvido, não pelo número.
- Posição: 2 com 4.
- Probabilidade de sucesso pelo critério do enquadramento (3 de 3 dentro de loudness e TP, voz acima da trilha, zero pedido de refazer; 40 dB trocado por escuta): 0,60, faixa [0,40, 0,80]. Com o 40 dB literal no stem: 0,30, faixa [0,15, 0,50] (DR02).
- Confiança: 0,6.

### D2 · Modelo A

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. Tzur v2 fiel | Máximo "After Effects" | Abertura em P&B até 4,28 s esconde a cor no trecho em que o pulo é decidido; confete e RGB split estão na lista de banidos (F48) |
| 2. Tzur v2 enxuto | Menos ruído visual | Pode parecer menos "profissional" para o Bruno |
| 3. Fiel + legenda palavra a palavra | Entende sem som | Tela cheia de camadas competindo |
| 4. Fora do óbvio: A como molde paramétrico (lê words-raw.json, marcações e textos de um JSON) | Regravação ou outro nicho custam só render | O mesmo molde vira padrão dos 5 nichos do 06-plano-final.md |

- Premissas: efeito Bruno em cena se repete no nicho (F13; premissa mais frágil do plano dos nichos); P&B curto (até 2,08 s, quadro 62) ainda dá o contraste da virada de cor sem atrasar a cor [HIPÓTESE].
- Posição: 2 + legenda (de 3) + 4. P&B só até "474" (2,08 s). Sem confete, aplauso, RGB split, tremida, contador e @ inventados.
- Probabilidade pelo critério do enquadramento: produção 0,80 [0,65, 0,90]; desempenho, se for o publicado (alcance >= 106 e pulo < 68% em 7 dias), 0,45 [0,25, 0,65] [PRIOR: os 3 reels do Bruno com dado ficaram em 126, 165 e 307 com pulo de 46% a 53% (00-SISTEMA.md); desconto de nicho porque reels de negócio para dentista de terceiros ficaram de 78 a 764 views (F58)].
- Confiança: 0,45.

### D3 · Modelos B e C

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. B = sab8a + gdgtify; C = alex-prompter + máscara de tipo | Duas variações de tipografia | B e C ficam parecidos entre si; ninguém atende "dividindo com reacts" |
| 2. B = tela dividida com reacts; C = tipografia arquitetônica | Cobre o pedido literal do Bruno | C sem rosto fere F13 se não for posto atrás da pessoa |
| 3. Só B agora | Menos render | O Bruno pediu 3 |
| 4. Não fazer B e C | Nenhum custo | Fere o pedido |
| 5. Fora do óbvio: B = tela dividida com reacts (stokebuilder + 551116 + 000267 + gdgtify); C = arquitetura atrás da cabeça com órbita e título fixo que qualifica o público, exportado em 9:16 e 4:5 para virar anúncio | Três hipóteses de abertura diferentes (A: P&B que vira cor; B: contador; C: título fixo) | Depois de 18/11 os 3 viram um teste de criativo limpo no leilão, que o orgânico N = 1 não dá |

- Premissas: título fixo segura a abertura (P06, nível 2 fraco); tela dividida sem nova ampliação mantém o rosto no mesmo tamanho (P19); o júri cego mede acabamento, não conversão (P17).
- Posição: 5.
- Probabilidade pelo critério do enquadramento (B e C com nota de júri >= A, produção dentro das regras e, se um for publicado, alcance >= 106 e pulo < 68%): 0,35 [0,20, 0,55].
- Confiança: 0,40.

### D4 (exploratória, só registro da cadeira)

Publicar só o C em 29/10. A e B não vão para a mesma conta na mesma semana (P15, sem precedente). Se a conta tiver trial reels (B23), A vai como trial para não seguidores. Depois de 18/11, com teto escrito, os 3 entram como 3 anúncios num conjunto só.

---

## 4. Ideias e hipóteses numeradas

| # | Ideia ou hipótese | Confiança | Evidência |
|---|---|---|---|
| 1 | Não cortar nenhuma pausa; os 3 modelos usam os mesmos 1093 quadros | alta | F02, F27, DR04 |
| 2 | Molde paramétrico lendo words-raw.json e um JSON de eventos | alta | F34 mostra constantes fixas do Tzur que quebram em outro bruto |
| 3 | Trocar o corte fixo y=470 pela máscara inteira com maior componente conexo | alta | F29, F30 |
| 4 | Contar 1093 PNG por camada antes de compor; trocar o "pass" por erro | alta | F33 |
| 5 | Semente pelo índice do quadro em tudo que é aleatório | alta | F32, F4 R9 |
| 6 | P&B só até 2,08 s (quadro 62), cor volta no "474" | média | F34 (Tzur usava 4,28 s); a cor no momento do número é o gatilho da virada |
| 7 | Sem confete, aplauso, RGB split, tremida | alta | F48 linha 18 |
| 8 | Sem contador de comentários nem @ fictício | alta | F32; regra de não inventar dado |
| 9 | Rodapé "Soma dos 27 CROs · CFO, out/2026" | alta | F68 |
| 10 | Não escrever "mais de 474 mil" na tela | alta | F68 (pessoa ou inscrição: sem dado) |
| 11 | Legenda "no Brasil" corrigida | média | F09; erro de preposição sem mudança de sentido |
| 12 | Ouvir 24,94 a 29,04 s antes de renderizar legenda | alta | F08, C3 |
| 13 | Se a fala estiver mesmo truncada, letreiro "PACIENTE" riscado no lugar da legenda em 27,58 a 29,04 s | média | stokebuilder proíbe inventar fala (F44) |
| 14 | Regravar só se o Bruno reprovar ao ouvir, aproveitando a sessão de 26/10 | média | 06-plano-final.md linha 158 |
| 15 | Quietude de 600 ms em 19,50 a 20,10 s | média | F47, DR05 |
| 16 | Nenhum SFX dentro da quietude; whoosh começa em 20,37 s | alta | conta: 20,64 - 0,2685 |
| 17 | SFX pelo pico, nunca pelo início do arquivo | alta | F35, F48 |
| 18 | loudnorm em duas passadas com TP -1,5 no PCM | média | C7; sobressinal do AAC é PRIOR |
| 19 | Medir loudness no MP4 final, não no WAV | alta | critério da D1 |
| 20 | Medir o ruído das pausas no stem de voz | alta | a trilha ocupa a pausa na mistura por desenho |
| 21 | Trocar 40 dB por escuta do Bruno nas 8 pausas | média | P01, DR02 |
| 22 | Expansor só nas janelas de pausa com rampa de 40 ms | baixa | hipótese técnica; testar no ouvido |
| 23 | Trilha 14 dB abaixo da voz durante a fala | média | notdwd-998633 (F1 seção 5), nível 2 sem desempenho |
| 24 | Silêncio total da trilha na quietude do C | baixa | gdgtify pede quietude absoluta (F47) |
| 25 | Zoom máximo 1,08x (2,03x da fonte) | alta | DR06, F4 R1 |
| 26 | Tela dividida sem nova ampliação: rosto fica do mesmo tamanho em pixels | média | F4 4.1, P19 |
| 27 | Recorte da janela do B segue o centro da máscara com média móvel de 9 quadros | média | F4 4.1 |
| 28 | Curva amortecida sem quique em todas as entradas | alta | F48 bane easing elástico |
| 29 | Reacts em SVG desenhado à mão, nunca glifo nem emoji | alta | CLAUDE.md; F32 |
| 30 | Evitar ícone de cadeira odontológica | média | F72 (equipamento), leitura conservadora |
| 31 | Relógio como react de "hora de cadeira" | média | fala em 7,68 a 8,80 s |
| 32 | Grade 3x3 de posts idênticos para "o mesmo diagnóstico e a mesma conclusão" | média | fala em 9,36 a 13,32 s; 91% de 78 perfis (06-plano-final.md linha 62, fonte UFPB/Revico) |
| 33 | Balões vazios com reticências como plateia, sem frase inventada | média | F44 |
| 34 | Título fixo do C qualifica o público: "PARA DENTISTA QUE DOMINA UMA TÉCNICA" | média | F55; qualificar no criativo reduz lead sem perfil [PRIOR de leilão] |
| 35 | C exportado em 4:5 com texto dentro de y 285 a 1635 | alta | conta de recorte; reuso em anúncio |
| 36 | Texto essencial nunca acima de y 285 em nenhum modelo | média | mesma conta; letreiro atrás pode passar disso como decoração |
| 37 | Publicar o C como principal | baixa | F55 fraco; nenhum dado de formato na conta (F19) |
| 38 | A como trial reel para não seguidores, se o recurso existir | baixa | B23 sem dado |
| 39 | Não publicar os 3 na mesma semana | média | P15 |
| 40 | Teste pago dos 3 criativos no mesmo conjunto depois de 18/11 | média | resolve N = 1; verba só com teto escrito (F18) |
| 41 | Mínimo de cerca de 900 impressões por criativo no teste | média | conta na 2.13 |
| 42 | Métrica do teste: visualização de 3 s por impressão e ThruPlay por impressão | alta | são as métricas que o leilão de vídeo devolve |
| 43 | Custo do teste: 2.700 impressões x CPM | média | CPM da conta: sem dado; com CPM de R$ 20 [PRIOR] daria cerca de R$ 54 |
| 44 | Público de remarketing com quem assistiu 50% do reel, para depois de 18/11 | baixa | tamanho mínimo de público: sem dado |
| 45 | Não impulsionar com "promover" no app: perde controle de público e de posicionamento | média | prática de leilão [PRIOR] |
| 46 | Busca não é canal deste produto agora | média | Ad Library: 13 anúncios para "lançamento curso odontologia" contra 1.432 para "curso para dentistas" |
| 47 | O cliente ideal já anuncia curso na Meta: ângulo futuro "você já anuncia seu curso" | média | Ad Library, títulos como "Curso online de facetas em resina" |
| 48 | Usar a Ad Library como lista de prospecção qualificada (só leitura, sem mensagem automática) | média | 1.432 anúncios ativos; contato só pelo Bruno |
| 49 | Hook alternativo para o próximo nicho: "Dentista, você já vende curso?" | baixa | idem 47 |
| 50 | Comentário com a profissão é sinal barato de público certo | média | F56 (4,8% com palavra-chave) |
| 51 | Resposta do Bruno em até 24 h, com pergunta de técnica e audiência | alta | 06-plano-final.md seção 7 |
| 52 | Planilha com origem "reel dentista modelo C" | alta | atribuição manual compensa o ponto cego |
| 53 | Perguntar "onde me conheceu" na primeira resposta | média | proxy de demanda criada |
| 54 | Leitura de 48 h para decidir TABULEIRO | alta | CLAUDE.md |
| 55 | Não usar a regra de 60% de pulo como meta única; registrar 60% e 68% | alta | C1 |
| 56 | Previsão de alcance com N = 3 reels do Bruno: mediana perto de 110, faixa larga | baixa | 00-SISTEMA.md (126, 165, 307) e F58 |
| 57 | Em A, b-roll só uma vez (1,52 s) para manter rosto em 95,8% | média | F13, P09 |
| 58 | B-roll do A em creme com wipe dourado e respiro de 0,30 s | média | F22, Tzur |
| 59 | Letreiro "TÉCNICA" que entra em 15,08 s volta como base do "2º PRODUTO" | média | gdgtify (F47): frase final apoiada nas anteriores |
| 60 | Órbita com metade de trás atrás da cabeça no "474" do C | média | F42 |
| 61 | Motion blur só nas janelas de movimento, 3 subquadros | média | F48, C8; custo DR07 |
| 62 | Mistura de subquadros em alfa pré-multiplicado | média | F4 4.3; B16 aberto |
| 63 | Nenhum blur sintético sobre o vídeo do Bruno | alta | F4 4.3 |
| 64 | Pré-passe de 8 a 20 stills antes de cada render cheio | alta | techhalla e l3d1c (F1) |
| 65 | Render cronometrado de 300 quadros por modelo antes do cheio | alta | B13 |
| 66 | Renders em série, nunca em paralelo | alta | F28 |
| 67 | Versão leve de cada modelo para envio (cerca de 12 MB) | média | DR14 |
| 68 | Conferência automática de travessão e emoji nos arquivos de texto | alta | regra do projeto |
| 69 | Tarja "Bruno · Estrategista de Lançamento" em 22,70 s, quando ele diz "Eu desenho" | média | fala em 22,70 a 24,24 s |
| 70 | Sem número de inscrição de CRO na tela enquanto a inscrição do Bruno for sem dado | média | P13, B20 aberto |
| 71 | CTA na tela "COMENTA: DENTISTA" sem contador | alta | F11, F32 |
| 72 | "@o_estrategista.com.br" nos últimos 0,51 s | média | fala termina em 35,92 s |
| 73 | Capa do reel: quadro 62 a 95 do C (rosto + "474 MIL" + título) | média | capa aparece na grade e no perfil; F53 |
| 74 | Legenda da postagem com a fonte do CFO por extenso | alta | F68 |
| 75 | Primeira linha da legenda da postagem repete o título do C | baixa | coerência de mensagem [PRIOR] |
| 76 | Conferir sincronia em 35,9 s ("respondo") nos 3 | alta | F4 R2 |
| 77 | Se o C perder do A em retenção no teste pago, o molde dos 5 nichos vira o A | média | regra de não proteger decisão antiga (CLAUDE.md) |
| 78 | Se nenhum dos 3 passar de 53 de alcance, a causa provável está no nicho; não refazer edição antes de 11/11 | média | 06-plano-final.md seção 6 |
| 79 | Registrar a rodada em semanas/2026-11-05.md | alta | CLAUDE.md, Módulo 7 |
| 80 | O próximo nicho reaproveita o molde do vencedor com troca só de JSON | média | ideia 2 |

---

## 5. Pre-mortem da cadeira B (05/11/2026, deu errado)

1. O C saiu "limpo demais" e o Bruno achou que não era "After Effects". Rejeitou e publicou o A sem teste. Sinal antecipado: nota do Bruno nos stills do pré-passe.
2. O título fixo do C ocupou espaço do rosto e o pulo subiu acima de 68%. A tese de F55 era N = 10 com rating qualitativo.
3. O reel teve 40 de alcance e o nicho puxou para baixo (F58). Meu plano não tinha como separar as duas causas no orgânico.
4. Verba continuou zero depois de 18/11, o teste pago nunca rodou e a comparação entre modelos ficou sem resposta. Meu principal argumento dependia de uma decisão do Bruno.
5. O 4:5 do C cortou o letreiro de trás (ele vive em y 300 a 560, parte acima de 285 some) e o anúncio ficou sem o efeito. Aceito: o 4:5 carrega título e legenda; o letreiro fica só no 9:16.
6. O AAC subiu o pico mais que 0,5 dB e o arquivo final passou de -1,0 dBTP. Mitigação: medir o MP4 e repetir com TP -2,0.
7. O trecho 24,94 a 29,04 s estava truncado de verdade, a solução do letreiro pareceu remendo e o Bruno pediu para regravar depois do render.
8. A automação PostZen não registrou os comentários "dentista" e a contagem de conversa ficou em zero por falha de medida (06-plano-final.md seção 6).
9. O render do C passou de 22 min porque a mistura de subquadros em numpy custou mais que o previsto (custo sem dado, F4).
10. Subestimei o efeito de marca do Tzur v2 que o Bruno já mostrou a clientes: o A tinha valor de continuidade que eu não medi.

---

## 6. Previsões numéricas

Publicação suposta: qui 29/10/2026. D+30 = 28/11/2026; D+60 = 28/12/2026; D+90 = 27/01/2027.

| # | Métrica | Valor previsto | Faixa | Conferir em | Base |
|---|---|---|---|---|---|
| 1 | Alcance do reel publicado em 7 dias | 110 | 50 a 260 | 05/11/2026 | PRIOR; 3 reels do Bruno (126, 165, 307) com desconto de nicho (F58) |
| 2 | Pulo do reel publicado em 7 dias | 58% | 48% a 70% | 05/11/2026 | PRIOR; reels do Bruno 46% a 53%, mediana da conta 68% |
| 3 | Comentários de dentista até D+30 | 2 | 0 a 8 | 28/11/2026 | PRIOR; 12 comentários em 30 dias na conta toda (00-SISTEMA.md) |
| 4 | DM qualificada de dentista até D+30 | 1 | 0 a 3 | 28/11/2026 | PRIOR |
| 5 | Diagnóstico agendado vindo do reel do dentista até D+60 | 0 (probabilidade de >= 1: 0,30) | 0 a 2 | 28/12/2026 | PRIOR; 1 disparo e 0 venda em 30 dias (00-SISTEMA.md) |
| 6 | Teste pago dos 3 criativos rodado até D+60 | probabilidade 0,35 | | 28/12/2026 | depende de teto escrito do Bruno (F18) |
| 7 | Se o teste rodar: visualização de 3 s por impressão do melhor criativo | 28% | 18% a 40% | 28/12/2026 | PRIOR, sem histórico da conta |
| 8 | Se o teste rodar: o C vence em ThruPlay por impressão | probabilidade 0,35 | 0,20 a 0,50 | 28/12/2026 | PRIOR; 3 opções, leve vantagem pelo rosto em 100% |
| 9 | Contrato fechado com dentista vindo deste reel até D+90 | probabilidade 0,08 | 0,02 a 0,15 | 27/01/2027 | PRIOR; 0 venda no histórico |
| 10 | 3 de 3 arquivos finais dentro de -15 a -13 LUFS e TP até -1,0 dBTP | probabilidade 0,85 | 0,70 a 0,95 | 23/10/2026 | medição técnica, loudnorm em duas passadas |
| 11 | Render dos 3 em série abaixo de 60 min de máquina | probabilidade 0,65 | | 23/10/2026 | DR08 (47 a 53 min) sem refação |

---

## 7. O que mudaria minha opinião

- O Bruno, vendo os stills, rejeitar o C como "pouco After Effects": publico o A e o C vira só criativo de anúncio.
- ig_post_stats do Tzur v2 (B06) com pulo abaixo de 55%: o A vira o principal.
- Escuta de B02 mostrando fala truncada grave: regravação em 26/10 antes de qualquer publicação.
- Volume de busca medido acima de algumas centenas por mês para termos do produto: abro teste de busca.
- Conta com trial reels (B23): testo A e B no orgânico antes de qualquer verba.
- CRO dizer que ícone genérico, número do CFO ou o próprio tema é publicidade irregular (B21): reescrevo tela dos 3.

## 8. Lacunas

- Volume de busca: sem dado (sem Planejador e sem Trends nesta sessão).
- CPM e custo por resultado de qualquer conta do Bruno: sem dado. A conta de anúncio de O Estrategista não aparece na listagem lida (evidencias-B); origem dos 1.907 de alcance pago do 00-SISTEMA.md: sem dado.
- Gasto e resultado dos 1.432 anúncios de "curso para dentistas": a biblioteca não mostra.
- Não ouvi o áudio; B02 e B03 seguem abertos.
- Não renderizei nada; os tempos são estimativa de F4.
- Desempenho de qualquer dos 3 formatos na conta: sem dado (F19).
- Pessoa ou inscrição na tabela do CFO: sem dado (B19).
- Sobressinal do AAC sobre o true peak: não medido.

## 9. Fontes

- run/01-fatos.md (F01 a F76, C1 a C10, B01 a B25, DR01 a DR20, P01 a P22), lido em 21/10/2026.
- run/01-pesquisa/F1-repo-opus-prompts.md, F2-padroes-virais-talking-head.md, F3-cfo-e-fatos.md, F4-viabilidade-pipeline.md.
- run/00-enquadramento.md; contexto.md; words-raw.json (79 palavras, tempos usados nas listas); transcricao-tempos.txt.
- conteudo/modo-god-nichos/run/06-plano-final.md (linhas 60 a 78, 158, 161, 170 a 186, 236, seção 7).
- conteudo/sistema-instagram/00-SISTEMA.md (linhas 15 a 40: mediana, 3 melhores, alcance pago de 1.907).
- CLAUDE.md do projeto.
- Meta Ad Library via ads_library_search, BR, ativos, 21/10/2026: run/02-cadeiras/evidencias-B/meta-ad-library-2026-10-21.md.
- ads_get_ad_accounts (só leitura), 21/10/2026: listagem de contas, nenhuma de O Estrategista.
