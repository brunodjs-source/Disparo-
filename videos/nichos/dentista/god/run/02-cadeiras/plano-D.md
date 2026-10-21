# Plano da cadeira D · Comercial consultivo · Reel do dentista · Agência Reunida Modo GOD · 21/10/2026

Cliente: O Estrategista (@o_estrategista.com.br).

- **Persona:** diretor comercial de venda consultiva, do lead ao contrato.
- **OTIMIZA PARA:** contrato assinado com margem no menor ciclo.
- **PONTO CEGO (assumido por escrito):** achar que tudo se resolve no fechamento. Compensação adotada neste plano: antes de falar de fechamento, contei quantos leads o reel consegue gerar com os números reais da conta (seção 2, P13, e ideias 1 a 12). A conta mostra que o gargalo está antes do fechamento, então o plano trata o reel como peça de topo e de qualificação, e cobra uma fonte de lead fora do reel.
- **PERGUNTA CONTRÁRIA:** e se não houver lead suficiente para o time fechar? Resposta na seção 2, P13, e no pre-mortem.

Etiquetas: [FATO] com fonte · [ESTIMATIVA] com conta · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, nível 4, nunca fecha objeção sozinho.

Trabalhei isolado: não abri plano-A.md nem plano-B.md.

---

## 0. Dado novo trazido por esta cadeira (consulta só de leitura)

Rodei `ig_posts` e `ig_post_stats` (Buzzfy) em 21/10/2026, cerca de 17h UTC, nos 18 reels da conta de 30/09 a 20/10/2026, sem os trial reels do Buzzfy. Leitura apenas.

| Medida | Valor | Etiqueta |
|---|---|---|
| Alcance somado dos 18 reels | 1.230 | [FATO, ig_post_stats 21/10/2026] |
| Comentários somados | 6 (3 no "Ele nunca fez um anúncio", 2 no "90% dos lançamentos", 1 no "Médico com agenda lotada") | [FATO, idem] |
| Comentários por 100 de alcance | 0,49 | [ESTIMATIVA: 6 / 1.230] |
| Reels com alcance de 106 ou mais | 4 de 18 (307, 168, 165, 126) | [FATO, idem] |
| Reels com alcance de 150 ou mais | 3 de 18 (307, 168, 165) | [FATO, idem] |
| Reels com alcance de 106 ou mais e pulo abaixo de 68% | 3 de 18 (307 com 53,4%; 165 com 46,0%; 126 com 50,4%), os três com o Bruno falando segundo o 00-SISTEMA.md | [FATO, idem; formato pelo 00-SISTEMA.md] |
| Mediana de alcance desta janela | 34 | [ESTIMATIVA: mediana dos 18; difere da mediana 53 do 00-SISTEMA.md, que usou 17 reels de outra janela] |
| Reel mais parecido com o do dentista (saúde, "agenda lotada", 30/09) | alcance 63, pulo 56,3%, 1 comentário | [FATO, idem]. Formato (Bruno ou animação): sem dado |
| Reel "Você gravou o curso inteiro" (11/10) | alcance 168 com 87,4% de pulo e 0 comentários | [FATO, idem]. Formato: sem dado. Mostra que alcance alto sem retenção não trouxe conversa |
| 3 reels de 19 e 20/10 | ainda provisórios (menos de 48 h) | [FATO, idem] |

---

## 1. Veredito (até 12 linhas)

1. O reel sozinho não enche o funil: com 0,49 comentário por 100 de alcance, a meta de 106 dá cerca de 0,5 comentário e o melhor reel da conta (307) daria cerca de 1,5 [ESTIMATIVA]. O trabalho do vídeo é alcance, retenção e uma porta clara; o volume de lead precisa de uma fonte fora do reel.
2. Publicar o **Modelo A** em 29/10 (Tzur v2 enxuto: letreiro 3D atrás só nos picos, título fixo com a tese no quadro 0, legenda palavra a palavra, rosto em 94,7% do tempo, bloco final sobre o rosto). É o formato mais perto do único dado que temos (Bruno falando em tela cheia, 2,4x a 5,8x a mediana).
3. **Modelo B** = tela dividida com reacts SVG e animação que representa a fala (stokebuilder-356793 + twoclipping-551116 + gdgtify-929495 + twoclipping-000267). Atende ao pé da letra "dividindo com reacts" e lê sem som: vira o ativo que o Bruno manda no direct.
4. **Modelo C** = 5 capítulos sobre o rosto, na ordem de uma conversa de venda (problema, implicação, mercado, o que eu faço, próximo passo), com órbita de texto atrás da cabeça (alex-prompter-997524 + twoclipping-041659 + techhalla-498547 + gdgtify-929495). Fica pronto para virar anúncio quando houver verba (zero até 18/11/2026).
5. Áudio: uma voz final única para os 3, remasterizada a partir do voz_master.wav (true peak hoje -0,5 dBTP), aprovada pelo Bruno antes do render dos vídeos. Trilha e SFX por modelo, medidos no MP4 final.
6. Na tela: "+474 mil" com "Fonte: CFO, out/2026"; legenda "no Brasil"; nenhum case Tzur; nenhuma boca, dente, preço ou promessa.
7. Métrica que manda: conversa qualificada de dentista em 7 dias (planilha, definição da seção 8.5 do 06-plano-final.md). Alcance e pulo são secundários.

---

## 2. Respostas às 14 perguntas

### P1. Qual modelo a cadeira defende e quais prompts entram

A cadeira defende **A para publicar em 29/10**, com B e C produzidos no mesmo ciclo porque o Bruno pediu os três ("faça um modelo no que ja fazemos e faça outros 2"), cada um com um trabalho diferente no funil.

| Modelo | Trabalho no funil | Prompts (ids) | O que aproveita | O que descarta |
|---|---|---|---|---|
| A | Alcance orgânico no feed em 29/10 | sab8a-475686 (contrato mínimo: respiros, legenda, grafismo, música); techhalla-498547 (punch-in 1,00 para 1,08); twoclipping-000267 (lista de banidos, SFX pelo pico, -14 LUFS) | Pipeline Tzur v2 (seg.py, ov2.html, cap2.js, comp.py) [FATO, contexto.md] | Do ov2.html: "1.287 comentários" e @ fictícios, ♥ ✓ ✕ como texto, RGB split, tremida, confete e aplausos [FATO, F32]. Do techhalla: RGB split e paleta magenta e verde |
| B | Ativo de direct e de stories: explica a ideia sem som | stokebuilder-356793 (rosto sempre visível quando o gráfico ocupa a tela; não inventar número); twoclipping-551116 (stickers como reacts, letras subindo por máscara); gdgtify-929495 (quietude de 400 ms; a fala é o relógio); twoclipping-000267 (motion blur por subquadros só nas transições, banidos) | Painel no topo com cenas do modelo.html (count, cross, cta) [FATO, F4 linha 88]; reacts em SVG desenhado | Emoji e glifos; 8 subquadros do twoclipping-551116 (custo; uso 5 só nas transições); P&B que vira cor (fica só no A) |
| C | Versão para anúncio e para qualificar: estrutura de conversa de venda | alex-prompter-997524 (5 cenas em cerca de 30 s); twoclipping-041659 (órbita atrás da cabeça, legenda presa à palavra, transição que atravessa a cabeça); techhalla-498547 (mola por letra com escalonamento de 125 ms); gdgtify-929495 (palavras como arquitetura, quietude) | Selos de capítulo "1/5" a "5/5" | A cena "prova" do alex-prompter (não há prova dita nem autorizada, ver P12); RGB split; partículas |

Suplentes não usados: everestchris6-399895 entra só como régua de QA se o júri cego pedir; notdwd-998633 e l3d1c-632524 não entram [FATO, F1].

### P2. Rosto de 0 a 3 s, percentual e zoom

| Modelo | Rosto de 0 a 3 s | Rosto visível no tempo total | Rosto em tela cheia | Zoom máximo |
|---|---|---|---|---|
| A | Sim, quadro 0, em P&B até 2,08 s | 94,7% [ESTIMATIVA: só o b-roll de 11,38 a 13,32 s esconde o rosto, 1,94 s de 36,40 s] | 94,7% | 1,08x (A11) |
| B | Sim, tela cheia até 3,80 s | 100% (na tela dividida o Bruno fica na janela de 1080x1120) | 43,5% [ESTIMATIVA: tela dividida em 3,80 a 13,32 s, 17,92 a 20,10 s e 22,70 a 31,58 s = 20,58 s, 56,5%] | 1,10x (B09) |
| C | Sim, tela cheia o tempo todo | 100% | 100% | 1,08x (C08) |

Todos abaixo do limite de 1,25x. Com 1,10x a ampliação total sobre a fonte fica em 2,06x [ESTIMATIVA: 1,875 x 1,10], contra 2,34x no limite (DR06).

### P3. Listas de edição quadro a quadro

Regras comuns aos três:
- Linha do tempo sem nenhum corte: os tempos são os do words-raw.json, quadro = arredondamento de t x 30. O vídeo termina em 36,40 s (quadro 1092). Motivo comercial: cortar as pausas economiza no máximo 2,98 s (F07) e cria risco de sincronia; a quietude de 0,60 s em 19,50 s serve de virada.
- As listas são ancoradas na palavra, não no segundo. Se a sessão de gravação de 26/10 (06-plano-final.md, linhas 158 e 574) trouxer uma tomada nova do dentista, basta realinhar com faster-whisper e recalcular os quadros pela mesma palavra.
- Faixa do letreiro de trás: y 120 a 450. De 120 a 252 a faixa fica livre da cabeça em 100% dos quadros [ESTIMATIVA, DR10]; de 252 a 450 a cabeça cobre parte das letras, que é o efeito pedido. O comp.py precisa deixar de zerar a máscara acima de y=470, senão o letreiro passa por cima da cabeça em 71,6% dos quadros [FATO, F29].
- Zona segura: nada essencial acima de y 220 nem abaixo de y 1470 [PRIOR, VibeRoll, F63].
- SFX começam no tempo do evento menos o pico medido do arquivo (F35).

#### Modelo A · Tzur v2 enxuto

| # | Início s (quadro) | Fim s (quadro) | Palavra que dispara | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|---|
| A01 | 0,00 (0) | 2,08 (62) | Dentistas | frente | Título fixo: "Dentista: sua técnica pode virar um segundo produto" (caixa alta, 2 linhas, y 240 a 400) | letras sobem por máscara, 0,30 s, mola amortecida; vídeo em P&B | nenhum (a voz começa no quadro 0) |
| A02 | 0,00 (0) | 36,40 (1092) | Dentistas | frente | Legenda palavra a palavra, grupos de 2 a 4 palavras, y 1250 a 1400; palavra ativa em ouro #E8B36A | pop de escala 0,92 para 1,00 em 4 quadros | nenhum |
| A03 | 1,58 (47) | 3,18 (95) | mais | áudio | (sem texto) | riser cujo pico (1596,6 ms) cai em 3,18 s | riser |
| A04 | 2,08 (62) | 4,80 (144) | 474 | atrás | "+474 MIL" com extrusão de 14 text-shadow, faixa y 120 a 450 | rotateX 55 para 0 em 0,55 s; título A01 sai para cima em 0,25 s; P&B vira cor em 0,30 s | impact no quadro 62 |
| A05 | 2,08 (62) | 5,16 (155) | 474 | frente | Rodapé "Fonte: CFO, out/2026" (corpo 28 px, y 1180, à esquerda) | fade 0,20 s | nenhum |
| A06 | 3,80 (114) | 5,16 (155) | colegas | atrás | "DENTISTAS ATIVOS" abaixo do 474 MIL, corpo menor | entra por máscara de baixo para cima, 0,30 s | nenhum |
| A07 | 7,68 (230) | 9,36 (281) | hora | atrás | "HORA DE CADEIRA" | rotateX 55 para 0, 0,55 s; o 474 MIL sai em 0,35 s a partir de 7,33 s | tick no quadro 230 |
| A08 | 7,62 (229) | 9,36 (281) | hora | frente | React SVG: relógio desenhado em traço, junto ao ombro esquerdo | stroke-dashoffset 0,35 s + escala amortecida | nenhum |
| A09 | 11,38 (341) | 13,32 (400) | diagnóstico | tela cheia | B-roll: grade 3x3 de cards iguais com as palavras DIAGNÓSTICO e CONCLUSÃO (sem foto, sem boca, sem dente) | cards entram em cascata de 60 ms; corte seco de volta ao rosto em 13,32 s | swipe com pico (137,1 ms) em 11,38 s |
| A10 | 13,32 (400) | 13,84 (415) | (pausa) | tela cheia | Rosto do Bruno, sem texto novo (respiro de 0,30 s do Tzur v2 cabe aqui) | nenhuma | whoosh com pico em 13,84 s (início 13,57) |
| A11 | 15,08 (452) | 17,92 (538) | técnica | atrás | "SUA TÉCNICA" | rotateX 55 para 0; punch-in 1,00 para 1,08 de 15,08 a 17,92 s | pop no quadro 452 |
| A12 | 17,12 (514) | 17,92 (538) | aprender | frente | React SVG: quadro de aula com 3 traços | desenho de traço 0,30 s, nasce 2 quadros antes da palavra | nenhum |
| A13 | 17,92 (538) | 19,50 (585) | existe | atrás | "EXISTE UM MERCADO" | troca do letreiro por máscara horizontal 0,30 s; zoom volta a 1,00 em 0,40 s | nenhum |
| A14 | 19,50 (585) | 20,10 (603) | (pausa) | atrás | Letreiro A13 parado | nenhuma (quietude de 0,60 s, trilha some 0,40 s) | nenhum |
| A15 | 20,64 (619) | 22,22 (667) | ensinar | atrás | "ENSINAR O SEU COLEGA" em ouro, maior letreiro do vídeo | rotateX 55 para 0 em 0,45 s | impact no quadro 619 |
| A16 | 22,70 (681) | 24,94 (748) | Eu | frente | Tarja de nome: "Bruno \| Estrategista de Lançamento" (y 1060) | desliza da esquerda 0,30 s | swipe com pico em 22,70 s |
| A17 | 26,38 (791) | 27,58 (827) | paciente | atrás | "DISPUTAR PACIENTE" (cinza, riscado em traço) | entra 0,30 s; risco desenha em 0,25 s a partir de 27,24 s | nenhum |
| A18 | 27,58 (827) | 29,04 (871) | forna | atrás | "FORMAR QUEM DISPUTA" (ouro). Texto editorial, independe do que a legenda escrever | cross: o anterior sai para baixo, este sobe, 0,35 s | pop no quadro 827 |
| A19 | 30,78 (923) | 31,58 (947) | segundo | atrás | "SEGUNDO PRODUTO" | rotateX 55 para 0, 0,45 s | impact no quadro 923 |
| A20 | 31,12 (934) | 31,58 (947) | produto. | frente | React SVG: duas caixas lado a lado, a segunda sobe | traço 0,30 s | nenhum |
| A21 | 32,00 (960) | 36,40 (1092) | Dentista | atrás | Marca "O ESTRATEGISTA" com varredura de luz (sem granulação aleatória) | varredura 0,8 s, semente fixa por quadro | sub no quadro 960 |
| A22 | 32,68 (980) | 36,40 (1092) | comenta | frente | Card do CTA: "Comenta: DENTISTA" (y 1060 a 1200), legenda continua embaixo | digitação letra a letra 0,6 s | typing com primeiro clique em 32,68 s (início 32,65) |

Nota: o "bloco final cinematográfico" do Tzur v2 vira A21 e A22, por cima do rosto e dentro dos 36,40 s. No Tzur ele vinha depois da fala (44,45 s, F34) com granulação de 0,838 s por quadro (F26) e prova social inventada (F32). Aqui a fala termina em 35,92 s; um bloco depois disso seria tempo morto no fim, que é onde o CTA precisa estar.

#### Modelo B · Tela dividida com reacts

| # | Início s (quadro) | Fim s (quadro) | Palavra que dispara | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|---|
| B01 | 0,00 (0) | 3,80 (114) | Dentistas | tela cheia | Rosto do Bruno; título fixo "Dentista: sua técnica pode virar um segundo produto" (y 240 a 400) | letras sobem por máscara 0,30 s | nenhum |
| B02 | 0,00 (0) | 36,40 (1092) | Dentistas | frente | Legenda palavra a palavra sobre a linha divisória (y 780 a 860 no modo dividido; y 1250 a 1400 em tela cheia) | pop 4 quadros | nenhum |
| B03 | 2,08 (62) | 3,80 (114) | 474 | frente | "+474 MIL" grande, sobre o peito do Bruno (y 1000 a 1200) | contagem 0 para 474 em 0,9 s, curva amortecida | riser com pico em 3,18 s (início 1,58) |
| B04 | 3,80 (114) | 5,48 (164) | colegas | tela dividida | Painel 1080x800: "+474 mil dentistas ativos" e rodapé "Fonte: CFO, out/2026"; Bruno em 1080x1120 embaixo | painel desce 0,35 s, x(t) = 1 - (1 + wt)e^(-wt); 5 subquadros na transição | whoosh com pico em 3,80 s (início 3,53) |
| B05 | 5,48 (164) | 9,36 (281) | porque | tela dividida | Painel: relógio SVG com ponteiro girando e a frase "SÓ HORA DE CADEIRA" (entra em 7,68 s) | traço 0,35 s; frase sobe por máscara em "hora" | tick no quadro 230 |
| B06 | 6,20 (186) | 7,12 (214) | você | frente | React SVG: balão com ponto de interrogação, junto ao ombro | escala amortecida 0,25 s | pop no quadro 186 |
| B07 | 9,36 (281) | 13,32 (400) | quase | tela dividida | Painel: grade 3x3 de cards iguais "DIAGNÓSTICO" e "CONCLUSÃO"; em 12,24 s um sinal de igual em traço cobre a grade | cascata de 60 ms por card | swipe com pico em 9,36 s |
| B08 | 13,32 (400) | 13,84 (415) | (pausa) | tela cheia | Painel sobe, Bruno volta para tela cheia | 0,35 s, 5 subquadros | whoosh com pico em 13,84 s (início 13,57) |
| B09 | 13,84 (415) | 17,92 (538) | Se | tela cheia | Rosto; punch-in 1,00 para 1,10 até 17,92 s | zoom linear lento | nenhum |
| B10 | 17,12 (514) | 17,92 (538) | aprender | frente | React SVG: três mãos levantadas em traço, ao lado da cabeça | traço 0,30 s, 2 quadros antes da palavra | pop no quadro 516 |
| B11 | 17,92 (538) | 19,50 (585) | existe | tela dividida | Painel: um ponto ouro que se divide em 12 contornos de pessoas, frase "EXISTE UM MERCADO" | divisão em 0,6 s | whoosh com pico em 17,92 s |
| B12 | 19,50 (585) | 20,10 (603) | (pausa) | tela dividida | Quietude: painel congela, trilha some | nenhuma por 0,40 s (19,62 a 20,02 s) | nenhum |
| B13 | 20,10 (603) | 22,22 (667) | Qual | tela cheia | Rosto; em 20,64 s "ENSINAR O SEU COLEGA" entra na frente, y 1000 a 1200, com mola por letra (escalonamento 40 ms) | painel sobe 0,25 s | impact no quadro 619 |
| B14 | 22,70 (681) | 24,46 (734) | Eu | tela dividida | Painel: tabuleiro de xadrez se desenhando em traço; tarja "Bruno \| Estrategista de Lançamento" | traço 0,6 s | swipe com pico em 22,70 s |
| B15 | 24,46 (734) | 27,58 (827) | você | tela dividida | Painel: setas de vários lados batendo num ponto, frase "DISPUTAR PACIENTE" | setas 0,4 s, frase riscada em 27,24 s | nenhum |
| B16 | 27,58 (827) | 29,28 (878) | forna | tela dividida | Painel (cross do modelo.html): o ponto vira fonte e solta setas para fora, frase "FORMAR QUEM DISPUTA" | cross 0,35 s | pop no quadro 827 |
| B17 | 29,28 (878) | 31,58 (947) | Sua | tela dividida | Painel: caixa 1 "ATENDIMENTO"; em 30,78 s sobe a caixa 2 "CURSO PARA COLEGAS" com "SEGUNDO PRODUTO" | caixa 2 sobe 0,35 s | impact no quadro 923 |
| B18 | 31,58 (947) | 32,00 (960) | (pausa) | tela cheia | Painel sobe, Bruno em tela cheia | 0,35 s, 5 subquadros | whoosh com pico em 32,00 s (início 31,73) |
| B19 | 32,68 (980) | 36,40 (1092) | comenta | frente | Card "Comenta: DENTISTA" (y 1000 a 1150) e react SVG de balão de comentário | digitação 0,6 s; balão em traço 0,25 s | typing com início em 32,65 s |

Geometria da tela dividida: painel opaco 1080x800 em cima, Bruno 1080x1120 embaixo recortado do base.mp4 sem nova ampliação, recorte acompanhando o centro da máscara com média móvel de 9 quadros, linha divisória de 4 px em #E8B36A [HIPÓTESE, F4 4.1]. Fico com 1080x1120 e não com 1080x960 (conflito C9) porque evita nova ampliação.

#### Modelo C · Cinco capítulos sobre o rosto

| # | Início s (quadro) | Fim s (quadro) | Palavra que dispara | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|---|
| C01 | 0,00 (0) | 9,36 (281) | Dentistas | frente | Selo de capítulo "1/5 O PROBLEMA" (canto superior esquerdo, y 240) | mola por letra, escalonamento 125 ms (techhalla-498547) | nenhum |
| C02 | 0,00 (0) | 36,40 (1092) | Dentistas | frente | Legenda presa ao tempo de cada palavra (twoclipping-041659), 2 a 3 palavras, y 1250 a 1400 | palavra ativa sobe 6 px e ganha ouro | nenhum |
| C03 | 2,08 (62) | 5,16 (155) | 474 | atrás | "474 MIL" como bloco arquitetônico atrás da cabeça (gdgtify-929495), rodapé frente "Fonte: CFO, out/2026" | bloco cresce do chão da faixa y 450 para cima em 0,5 s | riser com pico em 3,18 s |
| C04 | 7,68 (230) | 9,36 (281) | hora | atrás | "HORA DE CADEIRA" empilhado em 3 andares | andares caem um a um, 80 ms cada, curva amortecida | tick no quadro 230 |
| C05 | 9,36 (281) | 13,32 (400) | quase | frente | Selo "2/5 TODO PERFIL IGUAL"; a palavra "MESMO" se repete 6 vezes em linhas iguais atrás da cabeça | linhas entram em cascata de 60 ms | nenhum |
| C06 | 13,32 (400) | 13,84 (415) | (pausa) | atrás | Transição que atravessa a cabeça (twoclipping-041659): faixa ouro passa por trás da máscara da esquerda para a direita | 0,30 s, 3 subquadros | whoosh com pico em 13,84 s (início 13,57) |
| C07 | 13,84 (415) | 22,22 (667) | Se | frente | Selo "3/5 O MERCADO" | mola por letra | nenhum |
| C08 | 15,08 (452) | 17,92 (538) | técnica | atrás | "SUA TÉCNICA" com punch-in 1,00 para 1,08 | zoom lento | pop no quadro 452 |
| C09 | 17,92 (538) | 19,50 (585) | existe | atrás | "EXISTE UM MERCADO" como parede de letras | letras sobem por máscara | nenhum |
| C10 | 19,50 (585) | 20,10 (603) | (pausa) | atrás | Quietude de 400 ms: tudo parado, trilha some (19,62 a 20,02 s) | nenhuma | nenhum |
| C11 | 20,64 (619) | 22,22 (667) | ensinar | atrás e frente | Órbita "ENSINAR O SEU COLEGA / " girando em volta da cabeça: metade de trás atrás da máscara, metade da frente na frente | 1 volta em 1,6 s, 3 subquadros | impact no quadro 619 |
| C12 | 22,70 (681) | 29,04 (871) | Eu | frente | Selo "4/5 O QUE EU FAÇO" e tarja "Bruno \| Estrategista de Lançamento" | mola por letra; tarja desliza 0,30 s | swipe com pico em 22,70 s |
| C13 | 26,38 (791) | 27,58 (827) | paciente | atrás | "DISPUTAR PACIENTE" em cinza | risca em traço a partir de 27,24 s | nenhum |
| C14 | 27,58 (827) | 29,04 (871) | forna | atrás | "FORMAR QUEM DISPUTA" em ouro, sobe por trás da cabeça | máscara de tipo, 0,35 s | pop no quadro 827 |
| C15 | 29,28 (878) | 36,40 (1092) | Sua | frente | Selo "5/5 O PRÓXIMO PASSO" | mola por letra | nenhum |
| C16 | 30,78 (923) | 31,58 (947) | segundo | atrás | "SEGUNDO PRODUTO" com dois blocos lado a lado | bloco 2 cresce 0,4 s | impact no quadro 923 |
| C17 | 32,68 (980) | 36,40 (1092) | comenta | frente | Card "Comenta: DENTISTA" (y 1000 a 1150) | digitação 0,6 s | typing com início em 32,65 s |

Lógica comercial do C: os 5 capítulos seguem a ordem de uma conversa consultiva (situação e problema, implicação, mercado, solução, próximo passo). Os selos "1/5" a "5/5" prometem um fim visível [HIPÓTESE: segura retenção; sem dado na conta].

### P4. Trecho 24,94 a 29,04 s ("forna que a gente disputa")

- Cortar fala está fora (regra do contexto.md).
- Primeiro ouvir (B02, cerca de 10 min). "que a gente" ocupa 0,10 s no alinhamento (F08), o que sugere erro de alinhamento automático mais do que fala real [HIPÓTESE].
- Se o ouvido confirmar "formar quem disputa": legenda fiel, e o problema some.
- Se o ouvido confirmar outra coisa: a legenda escreve o que foi dito, com grafia normal. A ideia limpa vai no letreiro editorial "FORMAR QUEM DISPUTA" (A18, B16, C14), que é grafismo e não precisa bater com a boca.
- Regravar só o áudio desse trecho fica fora, porque a boca não bateria. Se a tomada de 26/10 sair melhor, ela substitui o bruto inteiro e as listas são realinhadas pela palavra (P3).

### P5. "em Brasil" (4,80 a 5,16 s)

Legenda corrigida para "no Brasil". São duas letras numa palavra de 0,16 s (F09), o roteiro aprovado diz "no Brasil" (06-plano-final.md linha 63) e F3 recomenda a correção. Para um público que avalia a credibilidade de quem vende, um erro de português na tela custa mais do que uma diferença mínima com a boca [PRIOR].

### P6. 474 mil na tela

Com fonte. Texto "+474 mil" e rodapé "Fonte: CFO, out/2026" (A05, B04, C03). Motivo: o comprador é profissional de saúde e desconfia de número solto; a fonte vale como prova [PRIOR]. O número exato (474.659) não vai para a tela, porque a tabela muda ao longo do dia (C2) e pode contar inscrição em vez de pessoa (B19) [FATO, F68].

### P7. Áudio

Cadeia proposta, a partir do voz_master.wav e não do raw, porque ele já está em -14,2 LUFS e falta só o pico (F04, DR01):
1. B01: procurar no scratchpad/dent qual cadeia gerou o voz_master (15 min). Se não achar, seguir mesmo assim.
2. Filtro passa-alta em 80 Hz [PRIOR].
3. De-esser leve na faixa de 5 a 8 kHz [PRIOR].
4. Expansor para baixo só nas pausas: limiar logo abaixo do nível da fala, razão de 2:1 a 3:1, sem gate seco, para não cortar cauda de palavra. Objetivo: tirar as pausas de 16,0 dB (DR02) para perto de 30 dB [PRIOR].
5. Loudnorm em duas passadas para -14 LUFS integrado e TP -1,5 dBTP. Uso -1,5 no limitador para sobrar margem: o MP4 final em AAC precisa medir até -1,0 dBTP. Isso resolve o conflito C7 sem escolher lado.
6. Gate de aprovação: o Bruno ouve a voz_final.wav de 36,4 s antes dos 3 renders. Uma aprovação vale para os três.
7. Trilha por modelo, 18 a 22 LU abaixo da voz [PRIOR]. Ducking por sidechaincompress com a voz como chave. Some de 19,62 a 20,02 s (quietude) nos três.
8. SFX: 18 a 24 dB abaixo do pico da voz (P03, PRIOR), alinhados pelo pico (F35). Nenhum som de moeda ou caixa registradora: soaria como promessa de dinheiro.
9. Medida no arquivo final de cada modelo: `ffmpeg -i final.mp4 -af ebur128=peak=true -f null -`, com critério de -15 a -13 LUFS, TP até -1,0 dBTP (DR19) e voz acima da trilha em toda janela de fala de 400 ms (DR20).

Sobre o critério de 40 dB: é PRIOR (P01), e nenhuma versão chega lá pelo método do DR02. Proponho trocar por "pausas de 0,3 s ou mais, sem 50 ms de borda, pelo menos 30 dB abaixo da fala, mais o ouvido do Bruno". Se ficar 40 dB, a D1 falha por construção.

### P8. Upscale de 576x1024 para 1080x1920

- O base.mp4 já está em 1080x1920 a 30 fps, mas o método é sem dado (F23, B17).
- Passo 1: ler o metadado do base.mp4. Se não der para saber o método, refazer com `scale=1080:1920:flags=lanczos` e `fps=30` a partir do raw (VFR, F02), com unsharp leve [HIPÓTESE, P18], e comparar um quadro do rosto.
- Riscos: pele lavada e blocos de compressão no rosto (fonte a 1,31 Mb/s, F4 R1). A borda da máscara tem halo, porque o rembg trabalha em 320x320 (F31), o que dá cerca de 6 px por ponto na vertical.
- Mitigações:
  - zoom de no máximo 1,10x;
  - borda da máscara com desfoque de 3 a 5 px;
  - letreiro de trás só na faixa de cima, onde o halo cai sobre cabelo e parede, nunca em volta do rosto;
  - ficar só com o maior componente conexo da máscara, para tirar quem passa ao fundo nos 44 quadros de F30 [HIPÓTESE, P22].

### P9. Pipeline e tempo de render

Só o que já existe: Playwright e Chromium, ffmpeg 6.1.1 (tmix, loudnorm, ebur128, sidechaincompress), numpy, rembg com a máscara já pronta (F27), faster-whisper e HTML, Canvas e SVG. Nada instalado.

| Modelo | Estimativa de render com a máscara pronta | Fonte |
|---|---|---|
| A | cerca de 951 s; sem a granulação por quadro do bloco final, cerca de 800 s [ESTIMATIVA: 951 menos 151 s do bloco, F4 linha 68] | F4 |
| B | cerca de 887 s | F4 linha 69 |
| C | 1008 a 1319 s, mais a mistura de subquadros em numpy (sem dado) | F4 linha 70 |
| Total em série | 45 a 53 min [ESTIMATIVA] | F4. Não rodar em paralelo (F28) |

Antes do render cheio, cronometrar 300 quadros de cada modelo (B13). Se A passar de 20 min, a composição vai para filtros do ffmpeg (cerca de 8 min, F4).

### P10. CTA

- Usar o gravado: "Dentista, comenta a sua profissão aqui que eu te respondo" (32,00 a 35,92 s, F11).
- Texto na tela: "Comenta: DENTISTA" (A22, B19, C17). O card fica até o último quadro.
- TABULEIRO não entra na tela nem na legenda. Só vai para o comentário fixado se o reel passar de 150 de alcance em 48 h (CLAUDE.md, F20).
- A promessa "eu te respondo" é um compromisso comercial. Resposta pública em até 2 h nas primeiras 48 h e 1ª DM do roteiro 8.4 do 06-plano-final.md [PRIOR para o prazo]. Quem demora a responder perde a conversa [PRIOR].
- Legenda do post: a do 06-plano-final.md linha 399 ("Dentista: se colegas te perguntam como você faz, isso já é um segundo produto. Comenta a sua profissão que eu te respondo.").

### P11. Conformidade com publicidade odontológica

- Nada de boca, dente real, raio X, instrumental, procedimento, antes e depois, preço, "grátis", sorteio ou promessa de faturamento ou de agenda (Res. CFO 196/2019, F72; Código de Ética arts. 35 e 44, F73).
- O pedido diz "CFO 196/2019 não lida no oficial", mas F3 leu o texto oficial (evidencias-F3/res-cfo-196-2019.txt). A pendência está fechada no fato e aberta só na interpretação (B21).
- Os reacts são relógio, quadro de aula, mãos, caixas, balão e tabuleiro. Nenhum ícone de dente ou de cadeira odontológica, porque a P11 do livro de fatos é só interpretação. Custo comercial de tirar o ícone: nenhum. Custo de errar: o dentista que repostar responde junto (art. 45, F73).
- O letreiro "SEGUNDO PRODUTO" e o título "pode virar" ficam como possibilidade, não como resultado garantido.
- "Diagnóstico" na tela aparece como palavra de perfil de clínica, sem imagem.

### P12. Prova (Tzur)

Não entra. O Bruno não disse (F10) e não há autorização escrita (B24; 06-plano-final.md seção 7 item 5). Pôr o case na tela sem ele ter dito e sem autorização é prova sem lastro; se o dentista perguntar na DM, a conversa fica mais difícil. A autoridade vem da tarja "Bruno | Estrategista de Lançamento" e do próprio raciocínio. A linha "Eu desenho lançamento para quem ensina" está prevista na sessão de 26/10 (06-plano-final.md linha 531) e pode entrar numa tomada futura.

### P13. Métrica, fonte, data e critério de parar. E a pergunta contrária

**Métricas**
| Métrica | Fonte | Leitura | Critério |
|---|---|---|---|
| Conversa qualificada de dentista (principal) | planilha de leads, definição 8.5 do 06-plano-final.md | 05/11/2026 (D+7 da publicação) | 0 com alcance de 106 ou mais: TESTAR a porta, não o nicho |
| Comentários "dentista" e respostas | ig_comments (Buzzfy) e listCommentAutomationLogs (PostZen), leitura | 31/10 (48 h) e 05/11 | 150 ou mais de alcance em 48 h: liga TABULEIRO no fixado |
| Alcance, views, tempo assistido, pulo | ig_post_stats (Buzzfy) | 31/10 e 05/11 | Abaixo de 53 e pulo acima de 75%: PARAR o formato; 106 ou mais e pulo abaixo de 68%: sucesso da D2; abaixo de 60%: DOBRAR pela regra do 06-plano-final.md (conflito C1 registrado; reporto os dois cortes) |
| Diagnósticos agendados e realizados vindos do dentista | agenda do Bruno, coluna origem | 18/11/2026 | 0 somando os 5 nichos: trocar a oferta de porta (06-plano-final.md D3) |
| Tempo até a primeira resposta | planilha | a cada lead | acima de 24 h: falha de processo, não do vídeo |

**Pergunta contrária: e se não houver lead suficiente para o time fechar?**
É o cenário mais provável, e não um caso extremo.
- **Comentários esperados:** 0,49 comentário por 100 de alcance (seção 0). Na meta de 106, cerca de 0,5 comentário; no melhor reel da conta (307), cerca de 1,5 [ESTIMATIVA].
- **Comentários para 1 contrato:** com taxas que são PRIOR (30% dos comentários viram conversa qualificada, 30% das conversas viram diagnóstico, 20% dos diagnósticos viram contrato), 1 contrato pede cerca de 56 comentários [ESTIMATIVA: 1 / (0,3 x 0,3 x 0,2)]. Isso dá cerca de 11 mil de alcance pela taxa atual [ESTIMATIVA: 56 / 0,0049], ou mais de 100 vezes a meta do reel.

O plano responde em três frentes:
1. **O reel é ativo de venda, não a fonte de volume.** O Modelo B (sem som, tela dividida) é feito para o Bruno mandar no direct, à mão, a dentistas que ele já conhece ou que já ensinam. Agente nenhum manda mensagem. Meta sugerida: 10 envios por dia útil por 10 dias [PRIOR].
2. **Stories por 3 dias com a enquete da seção 10 do 06-plano-final.md** ("Você tem audiência no Instagram?"). Quem marcar "Sim" recebe a 1ª DM. Captura quem viu e não comentou.
3. **O Modelo C fica pronto como anúncio para depois de 18/11**, quando a verba deixa de ser zero (F18). A decisão de gastar é do Bruno.

Se nem assim houver lead, o critério é trocar a porta e a oferta de entrada antes de culpar o nicho ou o formato.

### P14. Regras de texto

- Todo texto de tela das 3 listas está em PT-BR, sem travessão e sem emoji.
- Única estrutura de contraste: "DISPUTAR PACIENTE" virando "FORMAR QUEM DISPUTA", que é a estrutura aprovada do dentista (06-plano-final.md linha 139).
- Nenhuma citação de HighClass, Júnior Prazeres ou Felipe Roser.
- O separador da tarja é a barra vertical "|", não o travessão.

---

## 3. Decisões: opções, efeitos, premissas, posição e probabilidade

### D1 · Áudio masterizado

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. voz_master.wav como está | Zero tempo | True peak -0,5 dBTP fica acima do alvo; com trilha e SFX somados o pico sobe mais. Falha no critério |
| 2. Remasterizar a partir do voz_master (limitador, de-esser, EQ, trilha com ducking, SFX) | Cerca de 30 a 60 min [PRIOR] | Herda a cadeia desconhecida do voz_master (B01); se ele tiver artefato de redução de ruído, fica |
| 3. Refazer do raw comparando rn_std, rn_sh e rn_bd | Controle total da cadeia | Mais 1 a 2 h [PRIOR]; DR02 mostra que as 3 ficam entre 14,3 e 16,3 dB, sem vantagem medida sobre o master (16,0) |
| 4. Regravar só o trecho 24,94 a 29,04 s | Resolve "forna" no áudio | A boca não bate; proibido na prática. A sessão de 26/10 já cobre uma tomada nova inteira |
| 5. Fora do óbvio: uma voz final única com aprovação do Bruno antes de qualquer render, e trilha e SFX como faixas por modelo | Uma aprovação vale para os 3 vídeos; refazer áudio não obriga a refazer vídeo | Encurta o ciclo: o Bruno aprova 36 s de áudio por WhatsApp em minutos, sem esperar 50 min de render |

- **Premissas:** o Bruno ouve no celular e aprova em até 24 h [PRIOR]; o expansor sobe a distância fala e pausa sem engolir cauda de palavra [HIPÓTESE]; o AAC do MP4 sobe o pico em menos de 0,5 dB [PRIOR].
- **Posição:** opção 2 com a opção 5 (gate de aprovação) e a opção 3 como recurso, se o Bruno reprovar o timbre.
- **Probabilidade de sucesso pelo critério do enquadramento** (3 de 3 arquivos em LUFS e TP, 40 dB, voz acima da trilha, zero refação): 0,35, faixa [0,15; 0,55]. Sem o corte de 40 dB: 0,70, faixa [0,50; 0,85]. Confiança: 0,55.

### D2 · Modelo A

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. Tzur v2 fiel (manifesto P&B, confete, aplausos, bloco final depois da fala) | Mais "efeito" | Bloco final depois de 35,92 s é tempo morto no lugar do CTA; confete e tremida estão na lista de banidos; prova social inventada (F32) passaria para a tela |
| 2. Tzur v2 enxuto, letreiro só nos picos | Menos ruído visual, rosto em 94,7% | Pode parecer "simples demais" para o pedido "estilo adobe effects" |
| 3. Tzur v2 fiel com legenda palavra a palavra | Lê sem som | Tela carregada: letreiro, legenda, b-roll e reacts brigam |
| 4. Fora do óbvio: enxuto com título fixo da tese no quadro 0 e a virada P&B para cor no "474", sem confete; bloco final por cima do rosto durante o CTA | Texto no quadro 0 (10 de 10 dos reels de referência, F53) e efeito de abertura sem custo de banidos | A tese escrita filtra quem entra: dentista sem interesse em ensinar sai cedo e sobe o pulo, mas quem fica é mais qualificado [HIPÓTESE] |

- **Premissas:** o efeito "Bruno falando" (F13) vale no nicho dentista (a premissa mais frágil, 06-plano-final.md D1); o título fixo não derruba a retenção dos 3 primeiros segundos [HIPÓTESE, F55 com N = 10]; o comp.py é corrigido no corte de y=470 (F29).
- **Posição:** opção 4, com a legenda da opção 3 em grupos de 2 a 4 palavras (lista A).
- **Probabilidade de sucesso pelo critério do enquadramento:**
  - produção: 0,85;
  - alcance de 106 ou mais e pulo abaixo de 68% em 7 dias: 0,40, faixa [0,20; 0,60]. Base: 3 de 3 reels com o Bruno falando passaram do critério nesta janela e 3 de 18 de todos os reels (seção 0), com desconto de nicho não medido;
  - as duas juntas: 0,35, faixa [0,15; 0,55].
- **Confiança:** 0,40.

### D3 · Modelos B e C

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. B = punchy com tipografia arquitetônica; C = explainer de 5 cenas com match cut | Dois estilos novos | Nenhum dos dois atende "dividindo com reacts" ao pé da letra; o Bruno pode pedir de novo |
| 2. B = tela dividida com reacts; C = tipografia arquitetônica | Atende o pedido literal | C sem função comercial clara |
| 3. Só B agora, C depois do primeiro resultado | Economiza 17 a 22 min de render (F4) | Contraria o pedido de 3 modelos; o resultado de N = 1 não decide formato |
| 4. Não fazer B e C | Zero custo | Descumpre o pedido |
| 5. Fora do óbvio: B e C definidos pela função no funil. B = tela dividida com reacts, para direct e stories sem som. C = 5 capítulos na ordem de uma conversa de venda, para anúncio futuro | Cada vídeo tem um uso depois de 29/10, não só uma estética | Mede cada um pela métrica do seu uso (respostas no direct para B; custo por conversa para C, quando houver verba); evita publicar 3 versões do mesmo bruto no feed (P15) |

- **Premissas:** a tela dividida com 1080x1120 mantém o rosto legível (P19); um júri cego de 3 cadeiras julga acabamento e não conversão (P17); o Bruno aceita usar B no direct [HIPÓTESE].
- **Posição:** opção 5.
- **Probabilidade de sucesso pelo critério do enquadramento** (júri cego dá a B e a C nota igual ou maior que a de A, mais o critério de produção): 0,35, faixa [0,15; 0,55]. O desempenho publicado fica exploratório (N = 1). Confiança: 0,35.

---

## 4. Ideias e hipóteses numeradas (85)

Confiança: alta, média ou baixa. Evidência ao lado.

**Funil e volume de lead**
1. O reel do dentista, sozinho, gera menos de 1 comentário esperado na meta de 106. Alta. 6 comentários em 1.230 de alcance (ig_post_stats, 21/10/2026).
2. O gargalo comercial da conta está no volume de conversas, não no fechamento: 1 disparo e 0 vendas em 30 dias. Alta. 00-SISTEMA.md.
3. Um contrato de dentista pede cerca de 56 comentários com taxas PRIOR. Baixa (as taxas são palpite). Conta da P13.
4. O reel deve ser tratado como ativo de prospecção 1 a 1 (Bruno manda no direct). Média. Ticket de R$ 25 mil mais R$ 8 mil por mês (00-SISTEMA.md) paga o tempo de prospecção manual [PRIOR].
5. 10 envios manuais por dia útil, por 10 dias, para dentistas que já ensinam ou têm audiência. Baixa. PRIOR, sem taxa de resposta medida.
6. Lista de prospecção montada só com perfis públicos e leitura, sem mensagem por agente. Alta (regra). Restrições do contexto.md.
7. Stories com enquete por 3 dias depois do reel capturam quem viu e não comentou. Média. 06-plano-final.md seção 10; 0,49% de comentário mostra que o comentário é uma porta estreita.
8. A pergunta da 1ª DM ("você já tem audiência ou já vende curso?") é a qualificação certa para o ICP do Tier 1. Média. 06-plano-final.md 8.4; público do 00-SISTEMA.md.
9. Faturamento só no diagnóstico, não na DM. Baixa. HIPÓTESE do próprio 06-plano-final.md 8.5.
10. O reel "médico com agenda lotada" (63 de alcance, 1 comentário) é o análogo mais próximo e sugere teto baixo para saúde. Média. ig_post_stats 21/10/2026; formato sem dado.
11. Alcance sem retenção não gera conversa: o reel de 168 com 87,4% de pulo teve 0 comentários. Média. ig_post_stats; N = 1.
12. A verba zero até 18/11 limita o volume ao orgânico e ao 1 a 1. Alta. F18.
13. O Modelo C deve sair pronto como anúncio de comentário para quando houver verba. Média. F18; sem dado de custo por conversa.
14. Uma parceria de post com um dentista que já ensina traria público certo. Baixa. PRIOR; nada na base.
15. A resposta pública em até 2 h nas primeiras 48 h aumenta a conversa. Baixa. PRIOR de venda consultiva; sem dado na conta.
16. Registrar a hora de cada comentário e da resposta na planilha. Alta (custo zero). 06-plano-final.md D3 pede a planilha.
17. Quem comenta "dentista" e não tem audiência recebe "segue o perfil" e não recebe oferta de diagnóstico. Alta. 06-plano-final.md 8.4 item 4.
18. Quantos dentistas comentam e não são o ICP é a métrica de ruído do CTA. Média. Definição 8.5.

**Conversão dentro do vídeo**
19. Título fixo com a tese no quadro 0 nos três modelos. Média. F53 (10 de 10 com texto no quadro 0) e F55 (N = 10).
20. O título fixo escrito como possibilidade ("pode virar") e não como resultado. Alta. Res. 196/2019 veda promessa (F72).
21. O card "Comenta: DENTISTA" fica na tela do primeiro quadro do "comenta" até o último quadro. Média. F56 (CTA com palavra explícita teve 4,8% contra 0,48%).
22. O CTA não ganha bloco depois da fala; o vídeo acaba 0,48 s depois de "respondo.". Média. F34 mostra bloco depois da fala no Tzur; tempo morto no fim [PRIOR].
23. A tarja "Bruno | Estrategista de Lançamento" em 22,70 s, quando ele diz "Eu desenho", ancora quem vende. Média. Roteiro; sem dado.
24. O "474 mil" com fonte funciona como prova para público técnico. Média. F68; PRIOR sobre o efeito.
25. Nenhum número além do 474 mil na tela. Alta. stokebuilder-356793 proíbe inventar número (F44).
26. A legenda corrige "em Brasil" para "no Brasil". Média. F09; F3.
27. O letreiro "FORMAR QUEM DISPUTA" carrega a ideia mesmo que a fala tenha saído truncada. Média. F08.
28. A quietude em 19,50 a 20,10 s marca a virada para "Qual é? Ensinar o seu colega". Média. gdgtify-929495 (F47); DR05 mostra que cabe.
29. O maior letreiro do vídeo é "ENSINAR O SEU COLEGA", porque é a oferta. Média. Roteiro; leitura comercial.
30. "SEGUNDO PRODUTO" sem som de moeda. Alta. Res. 196/2019 veda mercantilização (F72).
31. A legenda do post repete a tese e o CTA. Média. 06-plano-final.md linha 399.
32. A capa do reel mostra o Bruno com "Dentista: sua técnica pode virar um segundo produto". Média. F13 (rosto) e F53.
33. O B funciona sem som e por isso serve para o direct. Média. Painel explica cada frase; sem dado de taxa de visualização sem som na conta.
34. Os capítulos "1/5" a "5/5" do C seguram até o fim. Baixa. HIPÓTESE; nenhum dado.
35. O C segue a ordem de conversa consultiva (problema, implicação, mercado, solução, próximo passo). Média. alex-prompter-997524 (F49) adaptado.

**Edição e formato**
36. Rosto em tela cheia em 94,7% do A. Alta (conta da lista). Lista A.
37. Rosto visível em 100% do B, em tela cheia só em 43,5%. Alta (conta). Lista B.
38. O risco do B é o rosto menor na tela dividida. Média. F13 mede rosto, não tamanho de rosto; sem dado.
39. Zoom de no máximo 1,10x nos três. Alta. DR06 e F4 R1.
40. O comp.py precisa trocar o corte fixo de y=470 por máscara inteira. Alta. F29 (71,6% dos quadros).
41. Letreiro de trás na faixa y 120 a 450. Alta. DR10.
42. Ficar só com o maior componente da máscara tira quem passa ao fundo. Média. F30; P22.
43. Borda da máscara com desfoque de 3 a 5 px. Média. F31 (320x320).
44. Sem RGB split, tremida, confete ou partículas nos três. Alta. F48.
45. Reacts em SVG desenhado, sem ♥ ✓ ✕. Alta. F32; regra sem emoji.
46. Nenhum ícone de dente ou cadeira odontológica. Média. P11 é só interpretação; custo zero de tirar.
47. B-roll do A só em 11,38 a 13,32 s, sem foto. Alta. Res. 196/2019.
48. Motion blur só nas transições (3 a 5 subquadros). Média. F4 4.3; custo F26.
49. render(t) com semente fixa por quadro (granulação e varredura). Alta. F32 (Math.random).
50. Tela dividida com 1080x1120 sem nova ampliação. Média. F4 4.1; conflito C9.
51. Painel do B feito com cenas do modelo.html (count, cross, cta). Média. F37; F4 linha 88.
52. Nenhum corte de pausa: os tempos ficam iguais ao words-raw.json. Média. Corta no máximo 2,98 s (F07) e protege a sincronia.
53. Listas ancoradas na palavra, para realinhar se a tomada de 26/10 substituir esta. Alta. 06-plano-final.md linhas 158 e 574.
54. Legenda em grupos de 2 a 4 palavras. Média. F62 e F63 (nível 3).
55. A órbita do C usa a máscara para a metade de trás. Média. twoclipping-041659 (F42); cap2.js já separa camadas.
56. O P&B que vira cor no "474" fica só no A. Média. Pipeline Tzur; evita repetir efeito entre modelos.
57. Cronometrar 300 quadros de cada modelo antes do render cheio. Alta. B13; F26 vem de testes curtos.
58. Renders em série, nunca em paralelo. Alta. F28.

**Áudio**
59. Uma voz final única para os três modelos. Alta. Mesmo bruto; reduz o retrabalho.
60. Aprovação do áudio antes do render dos vídeos. Alta. Ciclo menor; custo de reverter baixo (D1).
61. Limitador em -1,5 dBTP para o MP4 medir até -1,0. Média. C7; o AAC sobe o pico [PRIOR].
62. Expansor nas pausas no lugar de gate seco. Média. DR02 (16,0 dB hoje); risco de cortar cauda.
63. Trocar o critério de 40 dB por 30 dB mais o ouvido. Média. DR02: nenhuma versão chega a 40.
64. Ouvir 13,37 a 13,79 s e 31,63 a 31,95 s antes de mexer. Alta. B03.
65. Trilha some na quietude de 19,62 a 20,02 s. Média. gdgtify-929495.
66. Trilha 18 a 22 LU abaixo da voz. Baixa. PRIOR.
67. SFX pelo pico medido de cada arquivo. Alta. F35.
68. Medir ebur128 no MP4 final de cada modelo e anexar o resultado à entrega. Alta. DR19.

**Conformidade e risco**
69. Nada de case Tzur na tela. Alta. F10; B24.
70. Nada de "grátis" na tela, nem para o diagnóstico. Alta. Art. 44 (F73). O diagnóstico gratuito fica só na DM, que é conversa privada [HIPÓTESE sobre o alcance da regra].
71. Se o Bruno não é inscrito em CRO, o risco recai sobre o dentista que repostar. Média. P13; art. 45 (F73).
72. Não marcar dentista nenhum no post. Média. Art. 45; evita envolver terceiro.
73. "Diagnóstico" na tela só como palavra, sem imagem clínica. Alta. F72.
74. O novo capítulo de publicidade do CFO pode mudar as regras. Média. F75.

**Medição e decisão**
75. Métrica principal: conversa qualificada em 7 dias. Alta. 06-plano-final.md seção 8.
76. Reportar o pulo contra 68% e contra 60%. Alta. Conflito C1.
77. Publicar só o A no feed em 29/10; B e C não vão ao feed na mesma semana. Média. P15 (sem precedente); o uso de B e C é outro.
78. Se a conta tiver trial reels, testar o C como trial. Baixa. B23 sem dado.
79. N = 1 não decide formato; a decisão de formato espera 3 nichos. Alta. 00-enquadramento D3.
80. Ler ig_post_stats em 31/10 (48 h) e 05/11 (7 dias). Alta. 06-plano-final.md seção 4.
81. Registrar a rodada em semanas/2026-11-02.md (Módulo 7). Alta. CLAUDE.md.
82. Se o alcance passar de 150 em 48 h, ligar TABULEIRO no fixado. Alta. F20.
83. O reel de 29/10 tem a semana dividida com consórcio (27/10) e nutricionista (31/10); comparar os 3 na mesma régua. Média. 06-plano-final.md D1.
84. Na próxima tomada, pedir ao Bruno 2 s de silêncio no início e no fim, para medir o ruído de fundo. Média. B03; DR02 não teve pausa limpa.
85. Fixar o protocolo do júri cego antes de mostrar os vídeos (quem, escala de 1 a 5, o que vê). Alta. B25.

---

## 5. Pre-mortem da cadeira D

É 20/11/2026 e o plano fracassou. Os caminhos mais prováveis:
1. **O reel bateu a meta e não veio lead.** Alcance de 120, 2 comentários, nenhum dentista com audiência. O plano tratou o reel como fonte de lead e a fonte externa (envios manuais, stories) não aconteceu, porque dependia do tempo do Bruno. É o modo de falha mais provável [PRIOR].
2. **O comentário veio e a resposta atrasou.** A promessa "eu te respondo" foi cumprida em 3 dias, e a conversa esfriou. Sem a planilha, ninguém viu.
3. **O título fixo filtrou demais.** O pulo subiu acima de 75%, o reel não distribuiu e a regra PARAR desligou o nicho por um efeito de edição, não de mercado.
4. **A tela dividida encolheu o rosto.** O B, mandado no direct, foi aberto e fechado: o painel parecia aula e não conversa.
5. **O áudio voltou.** O Bruno pediu outra voz depois dos renders, porque o gate de aprovação foi pulado para ganhar tempo, e os 50 min de render se repetiram.
6. **A regra do CFO mudou.** O capítulo novo de publicidade (F75) saiu e um dentista que repostou recebeu notificação. O risco era baixo e o custo caiu sobre o comprador.
7. **A tomada de 26/10 substituiu o bruto** e as listas ancoradas em segundos tiveram de ser refeitas. Mitigado pela âncora na palavra, mas só se o comp.py ler as listas por índice de palavra.
8. **Diagnóstico sem fechamento.** Veio 1 diagnóstico, mas o dentista não tinha caixa para R$ 25 mil mais R$ 8 mil por mês. A qualificação por audiência não mede capacidade de pagar.

---

## 6. Previsões numéricas com data de conferência

Publicação considerada: Modelo A em qui 29/10/2026. Todas são PRIOR ou ESTIMATIVA, com a base indicada.

| Métrica | Valor previsto (faixa) | Base | Conferir em |
|---|---|---|---|
| Alcance do reel do dentista em 7 dias | 95 (40 a 250) | 3 reels com o Bruno de 126 a 307 nesta janela; desconto de nicho [PRIOR] | 05/11/2026 e registro em D+30, 20/11/2026 |
| Pulo do reel do dentista | 60% (48% a 75%) | reels com o Bruno: 46,0% a 53,4% [FATO]; nicho novo [PRIOR] | 20/11/2026 (D+30) |
| Comentários de dentista no reel | 1 (0 a 4) | 0,49 por 100 de alcance [ESTIMATIVA] | 20/11/2026 (D+30) |
| Conversas qualificadas de dentista (todas as fontes) | 1 (0 a 4); P(1 ou mais) = 0,45 | inclui envios manuais do B [PRIOR] | 20/11/2026 (D+30) |
| Diagnósticos de dentista realizados | 0 (0 a 2); P(1 ou mais) = 0,25 | [PRIOR] | 20/12/2026 (D+60) |
| Contrato assinado com dentista | 0; P(1 ou mais) = 0,05 (0,01 a 0,12) | [PRIOR]; ciclo de venda consultiva de ticket alto | 19/01/2027 (D+90) |
| Arquivos finais dentro de -15 a -13 LUFS e TP até -1,0 dBTP | 3 de 3; P = 0,85 | voz_master já em -14,2 (F04) | 23/10/2026 e registro em 20/11/2026 |
| Áudio aprovado pelo Bruno sem refação | P = 0,60 | [PRIOR] | 23/10/2026 |
| Render real do Modelo A | 13 a 20 min | F4 [ESTIMATIVA] | primeiro render cheio |
| Reels do dentista com alcance de 150 ou mais em 48 h | P = 0,20 | 3 de 18 reels passaram de 150 (ig_post_stats) com desconto de nicho | 31/10/2026 |

---

## 7. O que mudaria minha opinião, lacunas e fontes

### O que mudaria minha opinião
- Se o reel tiver 3 ou mais comentários de dentista com audiência em 7 dias, o reel passa a ser fonte de lead e o envio manual vira reforço.
- Se o B mandado no direct tiver mais respostas que o link da bio, o B vira o formato padrão de prospecção dos 5 nichos.
- Se o júri cego der ao C nota maior que ao A, o C sobe para o feed no próximo nicho.
- Se B19 mostrar que a tabela do CFO conta inscrições e não pessoas, "+474 mil dentistas" vira "+474 mil inscrições ativas" ou sai da tela.
- Se o ouvido (B03) mostrar ruído real nas pausas de 13,37 s e 31,63 s, a opção 3 da D1 (refazer do raw) passa à frente.
- Se o Bruno decidir que "comenta a sua profissão" conta como palavra-chave (06-plano-final.md D3), o CTA de tela vira "Segue o perfil" e a métrica principal muda para seguidores do post.

### Lacunas
- Taxas de comentário para conversa, de conversa para diagnóstico e de diagnóstico para contrato: sem dado; todas PRIOR.
- Formato (Bruno ou animação) dos reels de 168, 63 e 53 de alcance: sem dado nesta consulta.
- Margem do contrato: sem dado; só o preço de referência.
- Taxa de visualização sem som na conta: sem dado.
- Não ouvi o áudio (B02, B03).
- Não abri os prompts do repositório; uso F1 e o livro de fatos.
- Desempenho do Tzur v2 e de tela dividida, react ou texto atrás da pessoa: sem dado (F19, F66).
- Se a conta tem trial reels: sem dado (B23).
- Se o Bruno é inscrito em CRO: sem dado (B20).

### Fontes
- /home/user/Disparo-/videos/nichos/dentista/god/contexto.md
- /home/user/Disparo-/videos/nichos/dentista/god/run/00-enquadramento.md
- /home/user/Disparo-/videos/nichos/dentista/god/run/01-fatos.md (F01 a F76, C1 a C10, B01 a B25, DR01 a DR20, P01 a P22)
- /home/user/Disparo-/videos/nichos/dentista/god/run/01-pesquisa/F1-repo-opus-prompts.md, F2-padroes-virais-talking-head.md, F3-cfo-e-fatos.md, F4-viabilidade-pipeline.md
- /home/user/Disparo-/videos/nichos/dentista/god/words-raw.json e transcricao-tempos.txt
- /home/user/Disparo-/videos/nichos/dentista/god/frames-amostra.jpg (enquadramento do rosto)
- /home/user/Disparo-/conteudo/sistema-instagram/00-SISTEMA.md (ficha, oferta, ticket, funil)
- /home/user/Disparo-/conteudo/modo-god-nichos/run/06-plano-final.md (seções 2.2, 4, 5 D3, 8.4, 8.5, 9, 10)
- /home/user/Disparo-/CLAUDE.md
- Buzzfy `ig_posts` (reels, sem trial reels) e `ig_post_stats` (18 ids, compare_to_median=false), 21/10/2026 cerca de 17h UTC, só leitura
- Script das listas: /tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/chD/listas.py (quadros = arredondamento de t x 30)
