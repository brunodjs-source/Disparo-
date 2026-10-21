# Plano da cadeira J · Reel do dentista · Agência Reunida Modo GOD · 21/10/2026

Cliente: O Estrategista (@o_estrategista.com.br).

| Campo | Valor |
|---|---|
| Cadeira | J, Pessimista de risco |
| Persona | guardião de caixa no papel de CFO: unit economics, CAC, payback, corte de desperdício |
| OTIMIZA PARA | preservar caixa e cortar desperdício |
| PONTO CEGO (assumido) | o custo de não agir. Minha tendência é cortar B e C, adiar e pedir mais dado. Compenso por escrito: a seção 0.2 calcula o custo de não fazer nada antes de qualquer corte, e nenhum corte desta cadeira derruba um item pedido pelo Bruno; no máximo muda a ordem ou o acabamento |
| PERGUNTA CONTRÁRIA | quanto custa não fazer nada? Resposta na seção 0.2 |

Etiquetas: [FATO] com a fonte ao lado · [ESTIMATIVA] com a conta ou a premissa · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, evidência nível 4, nunca fecha objeção sozinho.

Trabalhei isolado: não abri os planos das outras cadeiras. Insumos lidos: contexto.md, 00-enquadramento.md, 01-fatos.md, F1 a F4, words-raw.json, transcricao-tempos.txt, CLAUDE.md, 00-SISTEMA.md (linhas 1 a 60), 06-plano-final.md (seções 2.2, 4, 5 e linhas 155 a 161 e 570 a 580).

Medições novas desta cadeira (21/10/2026, evidência em run/02-cadeiras/evidencias-J/):
- **J-M1** [FATO] O arquivo já entregue `videos/nichos/dentista/dentista-audio-masterizado.mp4` (576x1024, AAC 48 kHz, 36,44 s) mede -14,2 LUFS e **true peak -0,3 dBTP** (ffmpeg loudnorm summary). A codificação AAC subiu o pico de -0,5 (wav) para -0,3. O que já foi entregue ao Bruno não cumpre o alvo de -1,0 dBTP da D1.
- **J-M2** [FATO] Loudnorm em duas passadas com linear=true sobre voz_master.wav, saída AAC 192 kb/s, medido de novo no m4a: alvo TP -1,0 deu -14,2 LUFS e **-0,9 dBTP (falha por 0,1 dB)**; alvo TP -1,5 deu **-14,4 LUFS e -1,3 dBTP (passa)**; alvo TP -2,0 deu -14,6 LUFS e -1,9 dBTP. Arquivo: evidencias-J/teste_tp_aac.log. Conclusão: o -1,5 do add_music.sh (conflito C7) é o valor certo para aplicar antes do AAC; o -1,0 é o valor certo para conferir no arquivo final. Os dois números não se contradizem: um é alvo de processo e o outro é critério de aceite.
- **J-M3** [FATO] base.mp4 do dentista: 1080x1920, 30/1 fps, 1093 quadros, 13,36 Mb/s, codificado por ffmpeg (Lavc60.31.102 libx264, crf 14). O filtro de ampliação usado não fica gravado no arquivo: sem dado (B17 continua aberto, mas sabemos que foi o ffmpeg desta máquina).
- **J-M4** [FATO] A sessão única de gravação de seg 26/10 já prevê "Dentista, completo com case, 2 tomadas" e "Dentista, prova sem case" (06-plano-final.md linhas 158 e 574 a 575). Uma tomada nova do dentista tem custo marginal perto de zero para o Bruno, porque ele já estará gravando.

---

## 0. Veredito e pergunta contrária

### 0.1 Veredito (12 linhas)

1. Fazer os 3 modelos, em série e com portão de custo: A primeiro (publicável), B segundo, C terceiro. Nenhum é cortado; C só muda de data se estourar o portão.
2. A = Tzur v2 enxuto com legenda palavra a palavra: 8 letreiros 3D atrás, 1 b-roll de 1,7 s, 4 reacts SVG, CTA digitando. Sai o que custa e não converte: confete, RGB split, tremida, granulação por quadro e prova social inventada.
3. B = tela dividida (Bruno embaixo, painel com reacts e animações em cima): é o pedido literal "dividindo com reacts e animações que representam". Ids: stokebuilder-356793, twoclipping-551116, twoclipping-000267.
4. C = título fixo com a tese e tipografia cinética presa à fala, com órbita atrás da cabeça e 600 ms de quietude. Ids: gdgtify-929495, twoclipping-041659, techhalla-498547, sab8a-475686.
5. Os 3 dividem o custo fixo: máscara pronta (589 s já gastos), base.mp4 pronto, um master de áudio e uma camada de legenda. Custo marginal de máquina: cerca de 14, 15 e 15 min [ESTIMATIVA, seção 2 P9].
6. Linha do tempo sem corte de pausa (36,43 s, 1093 quadros): zero retrabalho de sincronia e a lista quadro a quadro sai direto do words-raw.json.
7. Áudio: master novo a partir de voz_master.wav, loudnorm em duas passadas com TP -1,5 antes do AAC, aceite no MP4 final em -15 a -13 LUFS e TP até -1,0. O arquivo já entregue falha no pico (J-M1) e precisa ser trocado.
8. O critério de 40 dB nas pausas é PRIOR sem método, e nenhuma versão chega lá (DR02). Não gasto horas perseguindo esse número: ouvido do Bruno mais B03 (5 min).
9. Texto de tela: "no Brasil" corrigido; "+474 mil dentistas ativos" com rodapé "Fonte: CFO, out/2026"; Tzur fora da tela; trecho 24,94 a 29,04 s ouvido antes e, no padrão, legenda corrigida em bloco, sem destaque palavra a palavra.
10. Publicar só 1 versão em 29/10. As outras 2 viram molde para consórcio, nutri, psicólogo e advogado, onde se pagam.
11. Parar: alcance abaixo de 53 em 48 h significa que o modelo não se repete; refação acima de 1 rodada por modelo tira o modelo do ciclo.
12. Probabilidade de o modelo publicado bater alcance de 106 ou mais e pulo abaixo de 68% em 7 dias: 0,40 [faixa 0,20 a 0,55], PRIOR ancorado em F12 a F14.

### 0.2 Quanto custa não fazer nada? (pergunta contrária, respondida antes dos cortes)

| Item | Conta | Valor |
|---|---|---|
| Caixa gasto para fazer A | verba zero até 18/11 [FATO, F18]; ferramentas já existem [FATO, F21]; SFX sintetizados próprios, sem licença [FATO, F35] | R$ 0 de desembolso [ESTIMATIVA: o custo de assinatura e de máquina é fixo, já pago, e não muda com mais um render] |
| Custo já afundado | bruto gravado, voz_master, máscara de 589,4 s, tr.trf, base.mp4 [FATO, F04, F27, F36, J-M3] | não volta se nada for feito |
| Alcance perdido no slot de 29/10 | reel com o Bruno: 126 a 307 nos 3 melhores [FATO, 00-SISTEMA]; reel de animação que costuma ocupar o slot: 8 a 39 [FATO, 00-SISTEMA] | [ESTIMATIVA] de 87 (126 menos 39) a 299 (307 menos 8) contas por slot perdido |
| Leads | 1 disparo em 30 dias, 0 vendas, objetivo de 10 diagnósticos por mês [FATO, 00-SISTEMA ficha] | lacuna de 9 diagnósticos por mês; cada semana sem reel com o Bruno no nicho atrasa a primeira leitura do nicho dentista em 7 dias |
| Valor de 1 cliente | referência R$ 25 mil de setup + R$ 8 mil por mês [FATO, 00-SISTEMA ficha, propostas RE/MAX e ZMedicAir] | [ESTIMATIVA] R$ 49 mil nos 3 primeiros meses (25 + 3 x 8), sem o percentual de infoproduto; churn: sem dado |
| Ponto de equilíbrio | custo de atenção do Bruno para revisar 3 versões de 36 s: cerca de 20 min [ESTIMATIVA: 3 vídeos x 36 s x 3 vezes = 5,4 min + leitura da folha de decisão]; valor da hora do Bruno: sem dado | qualquer probabilidade de fechar 1 cliente acima de cerca de 1% paga a revisão se a hora do Bruno valer até R$ 1.470 [ESTIMATIVA: 0,01 x 49.000 / (20/60)]. A taxa real de fechamento por reel é sem dado |
| Pedido do Bruno | ele pediu 3 modelos de forma explícita | recusar B e C custa confiança no conselho e o molde para 4 nichos seguintes [HIPÓTESE, não mensurável em R$] |

Leitura: não fazer nada custa de 87 a 299 contas de alcance no slot [ESTIMATIVA], 7 dias de atraso no sinal do nicho e o caixa já afundado, contra R$ 0 de desembolso para fazer A. Fazer A é obrigatório pela conta. B e C ficam em pé pelo valor de molde (uma construção, 5 nichos de uso), não pelo reel de 29/10. Onde minha persona economiza de verdade é no tempo do Bruno e nas refações, não em cortar modelos.

---

## 1. Respostas às 14 perguntas

### P1. Qual modelo a cadeira defende e quais ids entram

Defendo **A como o publicado em 29/10** e **B e C produzidos como moldes reaproveitáveis**, com ordem A, B, C. Motivo de caixa: A reaproveita quase todo o código do Tzur v2 (F22) e é o de menor risco técnico; B e C reaproveitam a máscara e a camada de legenda de A, e o custo marginal deles é o painel ou a tipografia.

| Modelo | Ids do repositório | Aproveito | Descarto e por quê |
|---|---|---|---|
| A | twoclipping-000267 (F48) | lista de banidos, SFX pelo pico medido, loudnorm -14 | 60 fps (dobra o custo e a fonte só tem 30 quadros reais, F4 2.1); tmix de 3 subquadros no vídeo inteiro (A não precisa) |
| A | sab8a-475686 (F45) | contrato mínimo: talking head cortado em edição com legenda, grafismo e música | nada a descartar: o prompt tem 86 caracteres |
| A | techhalla-498547 (F46) | punch-in suave de 1,00 a 1,08 | desalinhamento magenta e verde (é RGB split, banido pelo 000267) |
| B | stokebuilder-356793 (F44) | rosto sempre visível quando o gráfico ocupa a tela (vira janela de baixo em vez de PiP); proibição de inventar fato ou número | PiP pequeno (rosto pequeno some no celular [HIPÓTESE]); prompt é parcial no JSON |
| B | twoclipping-551116 (F43) | stickers recortados com borda branca como react (em SVG, nunca emoji); letras subindo por máscara | P&B que vira cor (já está em A, não duplico); 8 subquadros (custo 2,7x o de 3, DR07) |
| B | twoclipping-000267 (F48) | banidos, SFX pelo pico, curva sem quique | 60 fps |
| C | gdgtify-929495 (F47) | a fala é o relógio; quietude de pelo menos 400 ms (uso a pausa real de 0,60 s, 19,50 a 20,10 s); seek(t) determinístico | palavras como arquitetura em tela cheia sem rosto (fere F13) |
| C | twoclipping-041659 (F42) | órbita com a metade de trás escondida pela cabeça (usa a mesma máscara de A) | transição que atravessa a cabeça (custo de máscara dupla sem dado) |
| C | techhalla-498547 (F46) | mola por letra com escalonamento de 125 ms (4 quadros a 30 fps) | magenta e verde; pré-passe de 8 stills (não precisa com render(t) puro) |
| C | sab8a-475686 (F45) | título fixo mais legenda sobre talking head | nada |
| Nenhum | alex-prompter-997524 (F49) | nada | o esqueleto de 5 cenas tem uma cena de "prova" que este bruto não tem (o Tzur não foi dito, F10). Usar o esqueleto obrigaria inventar prova ou deixar buraco |

### P2. Rosto de 0 a 3 s, porcentagem do tempo e zoom

| Modelo | Rosto de 0 a 3 s | Rosto visível no total | Zoom máximo |
|---|---|---|---|
| A | sim, tela cheia de f0 a f306 | 34,73 de 36,43 s = **95,3%** [ESTIMATIVA: só o b-roll de 10,24 a 11,94 s esconde o rosto] | **1,10x** (2,06x da fonte: 1,875 x 1,10) |
| B | sim, tela cheia de f0 a f113 | **100%** (na tela dividida o Bruno fica na janela de 1080x1120) | 1,10x em tela cheia; 1,00x na janela (recorte sem nova ampliação, F4 4.1) |
| C | sim, tela cheia o vídeo todo | **100%** | 1,08x (techhalla) |

Fico abaixo do limite de 1,25x de propósito. A fonte é 576x1024 (F01) e 1,25x daria 2,34x da fonte (DR06). Cada ponto de zoom a mais aumenta o risco de pele lavada, e refazer o render custa outro ciclo de revisão do Bruno, que é o recurso mais caro deste plano.

### P3. Lista de edição quadro a quadro

Regras comuns aos 3: saída de 30 fps, quadro = round(t x 30) a partir de words-raw.json [FATO, F06]; linha do tempo de 0 a 36,43 s sem cortar pausa (1093 quadros, f0 a f1092). Zona segura: nada essencial acima de y=220 nem abaixo de y=1470 [PRIOR, F63]. Paleta do repositório: preto #141210, dourado #E8B36A, creme #F6F1E8 (F37). Curva de entrada sem quique: x(t) = 1 - (1 + wt)e^(-wt) (F4 4.1). SFX: início = quadro do evento visual menos o pico medido do arquivo (F35).

Camadas: **BASE** (base.mp4 em tela cheia), **TRÁS** (PNG da camada back, recortada pela máscara), **FRENTE** (PNG da camada front), **PAINEL** (só no B: JPEG opaco 1080x800 em cima), **JANELA** (só no B: Bruno em 1080x1120 embaixo).

#### 3.A Modelo A · Tzur v2 enxuto com legenda palavra a palavra (lista completa)

**Letreiros atrás (camada TRÁS).** Faixa vertical de y=120 a 450: a parte de cima fica sempre livre, porque o topo da pessoa nunca sobe acima de y=252 (DR10), e a de baixo passa atrás da cabeça. O comp.py precisa usar a máscara inteira, sem o corte em y=470 (F29). Extrusão de 14 text-shadow, rotateX de 55° para 0°, escala de 0,85 para 1, entrada em 0,55 s (17 quadros), saída em 0,35 s (11 quadros), como no ov2.html (F24).

| # | Início s (f) | Fim s (f) | Palavra que dispara | Camada | Texto | Animação | SFX (início s) |
|---|---|---|---|---|---|---|---|
| A01 | 0,00 (0) | 2,08 (62) | "Dentistas" | TRÁS | DENTISTA | já pronto no f0, sem entrada (texto legível no frame 0, F53); saída f52 a f62 | nenhum |
| A02 | 0,00 (0) | 2,08 (62) | "Dentistas" | BASE | (vídeo em P&B) | P&B de f0 a f61; vira cor em 0,2 s, f62 a f68, no "474" | nenhum |
| A03 | 2,08 (62) | 5,51 (165) | "474" | TRÁS | +474 MIL | entrada f62 a f79; saída f155 a f165 | whoosh no fim da entrada: 2,36 (f71) |
| A04 | 3,18 (95) | 3,18 (95) | "mil" | FRENTE | (sem texto) | marca de batida | impact: 3,18 (f95) |
| A05 | 2,08 (62) | 5,51 (165) | "474" | FRENTE | Fonte: CFO, out/2026 | rodapé de 30 px em y=1400, creme a 80%, fade de 6 quadros | nenhum |
| A06 | 5,48 (164) | 8,80 (264) | "porque" | BASE | (sem texto) | punch-in de 1,00 para 1,06 com mola; volta a 1,00 de f264 a f273 | nenhum |
| A07 | 7,68 (230) | 9,15 (275) | "hora" | TRÁS | HORA DE CADEIRA | entrada f230 a f247; saída f264 a f275 | pop: 7,68 (f230) |
| A08 | 7,61 (228) | 9,36 (281) | "hora" | FRENTE | (react SVG: relógio) | traço que se desenha em 0,35 s junto ao ombro direito (x 760 a 960, y 1000 a 1200); sai em 0,25 s | nenhum |
| A09 | 10,24 (307) | 11,94 (358) | "perfil" | FRENTE (tela cheia) | b-roll: grade 3x2 de cartões de post idênticos, rótulos "diagnóstico" e "conclusão" | wipe da esquerda em 0,2 s (f307 a f313) e saída f358 a f364; respiro de 0,30 s antes de "conclusão." | whoosh: 10,17 (f305); swipe na saída: 12,00 (f360) |
| A10 | 17,92 (538) | 19,85 (596) | "existe" | TRÁS | EXISTE UM MERCADO | entrada f538 a f555; saída f585 a f596 | riser que culmina no fim de "mercado.": 17,90 (f537) |
| A11 | 18,83 (565) | 19,85 (596) | "um" | FRENTE | (react SVG: gráfico subindo) | traço em 0,30 s perto do ombro esquerdo | nenhum |
| A12 | 19,50 (585) | 20,10 (603) | pausa depois de "mercado." | todas | (só a legenda some) | quietude de 0,60 s: nada se move; trilha em zero com fade de 60 ms | silêncio |
| A13 | 20,64 (619) | 22,57 (677) | "ensinar" | TRÁS | ENSINAR O SEU COLEGA | entrada f619 a f636; saída f667 a f677 | impact: 20,64 (f619) |
| A14 | 20,57 (617) | 22,70 (681) | "ensinar" | FRENTE | (react SVG: quadro de aula) | traço em 0,35 s junto ao ombro direito | nenhum |
| A15 | 20,64 (619) | 22,22 (667) | "ensinar" | BASE | (sem texto) | punch-in de 1,00 para 1,10; volta de f667 a f681 | nenhum |
| A16 | 22,70 (681) | 24,24 (727) | "Eu" | FRENTE | Bruno · Estrategista de Lançamento | tarja em y=1080, entra em 0,25 s pela esquerda | shutter: 22,82 (f685) |
| A17 | 24,94 (748) | 27,23 (817) | "deixa" | TRÁS | DISPUTAR PACIENTE | entrada f748 a f765; risco dourado desenhado de f782 a f791; saída f806 a f817 | swipe no risco: 26,06 (f782) |
| A18 | 27,24 (817) | 29,39 (882) | "a" (depois de "passa") | TRÁS | FORMAR QUEM DISPUTA | entrada f817 a f834; saída f871 a f882 | whoosh: 27,52 (f826) |
| A19 | 30,78 (923) | 31,93 (958) | "segundo" | TRÁS | 2º PRODUTO | entrada f923 a f940; saída f947 a f958 | ding_si: 31,17 (f935, "produto.") |
| A20 | 30,71 (921) | 32,00 (960) | "segundo" | FRENTE | (react SVG: duas caixas de produto) | traço em 0,35 s | nenhum |
| A21 | 32,68 (980) | 35,92 (1078) | "comenta" | FRENTE | Comenta: DENTISTA (balão de comentário em SVG; a palavra digita letra a letra de f980 a f1007) | balão entra em 0,25 s; cursor pisca a cada 15 quadros | typing: 32,65 (f980) |
| A22 | 32,00 (960) | 35,92 (1078) | "Dentista" | BASE | (sem texto) | punch-in lento de 1,00 para 1,08 | nenhum |
| A23 | 35,92 (1078) | 36,43 (1092) | fim de "respondo." | FRENTE | @o_estrategista.com.br | fade de 0,2 s em y=1420; o vídeo continua por baixo, sem bloco de granulação | pop: 35,92 (f1078) |

**Legenda palavra a palavra (camada FRENTE, y de 1180 a 1340, palavra ativa em #E8B36A, até 4 palavras por grupo, quebra em pontuação ou pausa).**

| Grupo | Início s (f) | Fim s (f) | Texto na tela | Observação |
|---|---|---|---|---|
| L01 | 0,00 (0) | 2,08 (62) | DENTISTAS, SÃO MAIS DE | |
| L02 | 2,08 (62) | 4,40 (132) | 474 MIL COLEGAS | |
| L03 | 4,40 (132) | 5,16 (155) | ATIVOS NO BRASIL | "em" falado; tela escreve "no" (P5) |
| L04 | 5,48 (164) | 6,82 (205) | POR QUE VOCÊ AINDA | a transcrição escreve "porque"; é pergunta |
| L05 | 6,82 (205) | 7,68 (230) | SÓ VENDE | |
| L06 | 7,68 (230) | 8,80 (264) | HORA DE CADEIRA? | |
| L07 | 8,80 (264) | 10,66 (320) | E QUASE TODO PERFIL | fica por cima do b-roll |
| L08 | 10,66 (320) | 12,10 (363) | POSTA O MESMO DIAGNÓSTICO | |
| L09 | 12,10 (363) | 13,32 (400) | E A MESMA CONCLUSÃO. | |
| L10 | 13,84 (415) | 15,08 (452) | SE VOCÊ DOMINA UMA | |
| L11 | 15,08 (452) | 16,64 (499) | TÉCNICA QUE OS DENTISTAS | |
| L12 | 16,64 (499) | 17,92 (538) | QUEREM APRENDER, | |
| L13 | 17,92 (538) | 19,50 (585) | EXISTE UM MERCADO. | |
| L14 | 20,10 (603) | 20,64 (619) | QUAL É? | |
| L15 | 20,64 (619) | 22,22 (667) | ENSINAR O SEU COLEGA. | |
| L16 | 22,70 (681) | 24,24 (727) | EU DESENHO SEU LANÇAMENTO. | |
| L17 | 24,46 (734) | 26,88 (806) | VOCÊ DEIXA DE DISPUTAR PACIENTE | bloco inteiro, sem destaque por palavra (P4) |
| L18 | 26,88 (806) | 29,04 (871) | E PASSA A FORMAR QUEM DISPUTA. | bloco inteiro, sem destaque por palavra (P4) |
| L19 | 29,28 (878) | 30,52 (916) | SUA TÉCNICA VIRA | |
| L20 | 30,52 (916) | 31,58 (947) | UM SEGUNDO PRODUTO. | |
| L21 | 32,00 (960) | 33,58 (1007) | DENTISTA, COMENTA | |
| L22 | 33,58 (1007) | 34,60 (1038) | SUA PROFISSÃO AQUI | a fala não tem "a" antes de "sua" (words-raw.json) |
| L23 | 34,60 (1038) | 35,92 (1078) | QUE EU TE RESPONDO. | |

Trocas de estímulo em A: A01, A03, A06, A07, A09, A10, A12, A13, A16, A17, A18, A19, A21, A23 = 14 em 36,4 s, uma a cada 2,6 s em média [ESTIMATIVA]. Fica acima da faixa de 7 a 12 de DR12, que é PRIOR, e abaixo do ritmo brainrot (P08).

#### 3.B Modelo B · tela dividida com reacts e animação da fala (eventos principais)

Layout: **F** = tela cheia; **S** = PAINEL 1080x800 em cima e JANELA 1080x1120 embaixo, recortada do base.mp4 seguindo o centro da máscara (média móvel de 9 quadros, F4 4.1). Linha dourada de 4 px entre os dois. A transição de F para S, ou de S para F, leva 0,35 s (11 quadros) com a curva amortecida. Os letreiros de trás de A (A03, A13, A17, A18) são reaproveitados nos trechos F. Painel em JPEG por pipe (0,08 s por quadro, F26). A legenda fica sobre a linha divisória.

| # | Início s (f) | Fim s (f) | Palavra que dispara | Camada | Texto ou cena | Animação | SFX (início s) |
|---|---|---|---|---|---|---|---|
| B01 | 0,00 (0) | 3,80 (114) | "Dentistas" | BASE F + TRÁS | DENTISTA, depois +474 MIL (A01, A03) | como A | whoosh 2,36 (f71); impact 3,18 (f95) |
| B02 | 3,80 (114) | 4,17 (125) | "colegas" | PAINEL entra | (transição para S) | painel desce de y=-800 a y=0 em 11 quadros | swipe 3,70 (f111) |
| B03 | 3,80 (114) | 7,68 (230) | "colegas" | PAINEL | +474 mil dentistas ativos · Fonte: CFO, out/2026 | número com letras subindo por máscara (551116), 0,5 s | nenhum |
| B04 | 7,68 (230) | 8,80 (264) | "hora" | PAINEL | HORA DE CADEIRA + relógio SVG | traço do relógio em 0,35 s; ponteiro gira 1 volta | tick 7,68 (f230) |
| B05 | 8,80 (264) | 13,32 (400) | "e quase" | PAINEL | grade 3x2 de cartões de post idênticos | cartões entram um a um a cada 4 quadros a partir de "perfil" (f307) | pop em f307, f311, f315 (3 só, para não poluir) |
| B06 | 13,84 (415) | 19,50 (585) | "Se" | PAINEL | TÉCNICA, seta, COLEGAS QUEREM APRENDER, mais 3 stickers SVG de mão levantada com borda branca | stickers entram em "dentistas" (f481), "querem" (f499) e "aprender" (f515) | pop 16,04 (f481), 16,64 (f499), 17,18 (f515); riser 17,90 (f537) |
| B07 | 19,50 (585) | 19,87 (596) | pausa depois de "mercado." | volta para F | (painel sobe) | transição de 11 quadros, depois quietude até f603 | silêncio |
| B08 | 20,10 (603) | 22,70 (681) | "Qual" | BASE F + TRÁS | ENSINAR O SEU COLEGA (A13) | punch-in 1,10 (A15) | impact 20,64 (f619) |
| B09 | 22,70 (681) | 24,46 (734) | "Eu" | PAINEL (S) | SEU LANÇAMENTO: planta desenhada em traço (grade, 3 blocos, seta) | traço de f685 a f727 | shutter 22,82 (f685) |
| B10 | 24,46 (734) | 29,28 (878) | "você" | BASE F + TRÁS | DISPUTAR PACIENTE, depois FORMAR QUEM DISPUTA (A17, A18) | como A | swipe 26,06 (f782); whoosh 27,52 (f826) |
| B11 | 29,28 (878) | 32,00 (960) | "Sua" | PAINEL (S) | cena "cross" da Série 2: HORA DE CADEIRA riscado vira SEGUNDO PRODUTO | risco em f923; troca em f935 | ding_si 31,17 (f935) |
| B12 | 32,00 (960) | 36,43 (1092) | "Dentista" | BASE F + FRENTE | Comenta: DENTISTA (A21) e assinatura (A23) | como A | typing 32,65 (f980); pop 35,92 (f1078) |

Tempo em S: de f114 a f585, de f681 a f734 e de f878 a f960, somando 606 quadros = 20,2 s = 55% [ESTIMATIVA]. Rosto visível: 100%. Ícone de cadeira odontológica fica de fora: o relógio diz "hora de cadeira" sem o risco da Res. 196/2019 sobre identificar equipamento (F72; P11 segue como hipótese). Trocar de ícone custa zero e tira o risco.

#### 3.C Modelo C · título fixo e tipografia cinética presa à fala (eventos principais)

O título fixo fica no topo, de y=220 a 400, e a tipografia cinética usa as paredes dos lados da cabeça, de y=500 a 1100 (contexto.md: parede livre acima e dos lados). Mola por letra com escalonamento de 4 quadros (techhalla). Motion blur com 3 subquadros em t - 1/120, t e t + 1/120, só nas janelas marcadas com "mb" (cerca de 6 s no total), com mistura em alfa pré-multiplicado (F4 4.3).

| # | Início s (f) | Fim s (f) | Palavra que dispara | Camada | Texto | Animação | SFX (início s) |
|---|---|---|---|---|---|---|---|
| C01 | 0,00 (0) | 36,43 (1092) | "Dentistas" | FRENTE | DENTISTA: SUA TÉCNICA É UM SEGUNDO PRODUTO | já pronto no f0 (F53, F55) | nenhum |
| C02 | 2,08 (62) | 5,51 (165) | "474" | TRÁS (parede esquerda) | 474 / MIL em dois pilares de letras | mola por letra, mb; rodapé "Fonte: CFO, out/2026" na FRENTE em y=1400 | impact 3,18 (f95) |
| C03 | 7,68 (230) | 9,15 (275) | "hora" | TRÁS (parede direita) | HORA / CADEIRA empilhadas como blocos | sobem por letra; em f264 caem com curva amortecida, sem quique, mb | tick 7,68 (f230) |
| C04 | 10,24 (307) | 13,32 (400) | "perfil" | TRÁS (as duas paredes) | MESMO repetido 6 vezes em grade | cópias entram a cada 3 quadros | nenhum (silêncio de SFX pedido pela C4 da Choppity, F62) |
| C05 | 15,08 (452) | 19,50 (585) | "técnica" | TRÁS | TÉCNICA, depois MERCADO, em degraus | cada degrau entra na palavra-chave ("técnica" f452, "aprender" f515, "mercado." f574) | riser 17,90 (f537) |
| C06 | 19,50 (585) | 20,10 (603) | pausa | todas | (tudo congela) | quietude de 0,60 s (gdgtify, mínimo de 400 ms) | silêncio, trilha em zero |
| C07 | 20,64 (619) | 22,70 (681) | "ensinar" | TRÁS + FRENTE | ENSINAR O SEU COLEGA · em anel | órbita em volta da cabeça, metade de trás escondida pela máscara (041659), 1 volta em 2,07 s, mb | impact 20,64 (f619) |
| C08 | 22,82 (685) | 24,24 (727) | "desenho" | TRÁS | grade de planta em traço na parede | traço se desenha | shutter 22,82 (f685) |
| C09 | 24,94 (748) | 29,28 (878) | "deixa" | TRÁS | DISPUTAR PACIENTE cai letra por letra em f791; FORMAR QUEM DISPUTA sobe por máscara em f817 | mb nas duas trocas | swipe 26,06 (f782); whoosh 27,52 (f826) |
| C10 | 30,78 (923) | 31,93 (958) | "segundo" | TRÁS + BASE | 2º PRODUTO grande | punch-in de 1,00 para 1,08 em f923 a f947, mb | ding_si 31,17 (f935) |
| C11 | 32,68 (980) | 35,92 (1078) | "comenta" | FRENTE | Comenta: DENTISTA | digita letra a letra | typing 32,65 (f980) |
| C12 | 35,92 (1078) | 36,43 (1092) | fim | FRENTE | @o_estrategista.com.br | fade | pop 35,92 (f1078) |

Legenda de C: os mesmos 23 grupos de A, em y=1180 a 1340. Rosto visível: 100%.

### P4. Trecho de 24,94 a 29,04 s ("forna que a gente disputa")

Escolha: **ouvir antes de decidir (B02, cerca de 5 min) e, no padrão, legenda corrigida em bloco**: "VOCÊ DEIXA DE DISPUTAR PACIENTE" (24,46 a 26,88 s) e "E PASSA A FORMAR QUEM DISPUTA." (26,88 a 29,04 s), sem destaque palavra a palavra nesses dois grupos (L17 e L18). Motivos de custo:
- Cortar fala é proibido (contexto.md).
- A legenda fiel a uma transcrição automática com palavras de 0,04 s (F08) pode estar mostrando um erro do alinhador, e não da fala.
- O bloco sem destaque por palavra esconde a diferença de 2 a 3 palavras entre boca e texto [HIPÓTESE], sem custo de render.
- Regravar só esse trecho não serve, porque a voz nova não casaria com a boca do vídeo. Regravar a tomada inteira já está no calendário de 26/10 (J-M4) com custo marginal perto de zero. Se o ouvido disser que a frase está ininteligível, a versão publicada passa a usar a tomada de 26/10, e os moldes A, B e C se rerenderizam a partir do novo words.json (cerca de 45 min de máquina, seção P9).

### P5. "em Brasil" (4,80 a 5,16 s)

**Corrigido na legenda para "no Brasil"** (L03). É uma preposição em 0,36 s, com risco de descasamento perto de zero e custo zero. A frente F3 recomenda o mesmo. O letreiro de trás nem usa a palavra.

### P6. 474 mil na tela

**"+474 mil" com rodapé "Fonte: CFO, out/2026"** (A05, B03, C02). Base: 474.659 na soma das 27 linhas por CRO e 474.640 em outra leitura do mesmo dia (F68, C2). "+474 mil" vale para as duas leituras. O rodapé custa 1 linha de HTML e protege contra a objeção "de onde saiu?", além de seguir a regra do projeto de pôr fonte em todo número. A página não diz se conta pessoa ou inscrição (B19); "+474 mil" arredonda para baixo e absorve esse risco [ESTIMATIVA: a diferença entre as leituras é de 19, muito menor que os 659 de folga].

### P7. Áudio: cadeia exata

1. Entrada: voz_master.wav (48 kHz mono, -14,2 LUFS, TP -0,5 dBTP, F04). Não refaço a redução de ruído a partir do raw.wav agora: DR02 mostra que voz_master (16,0 dB) fica na faixa das outras reduções (14,3 a 16,3 dB) e que nenhuma chega a 40 dB. Refazer custa tempo e não tem ganho medido.
2. De-esser: desligado no padrão. Só entra se o Bruno ouvir chiado (o filtro deesser existe no ffmpeg 6.1, mas o ganho não foi medido; não gasto sem pedido).
3. Mistura em numpy por índice de amostra (F4 4.4): voz em 0 dB; cada SFX com o pico entre 18 e 24 dB abaixo do pico da voz [PRIOR, P03], posicionado pelo pico medido (F35); trilha lounge da Série 2 a 0,085 linear com sidechaincompress pela voz (threshold 0,02, ratio 5, como no add_music.sh, F22); trilha em zero com fade de 60 ms na quietude de 19,50 a 20,10 s.
4. Loudnorm em duas passadas: medir; aplicar I=-14, **TP=-1,5**, LRA=11, linear=true com os valores medidos; codificar AAC 192 kb/s 48 kHz. Base: J-M2 mostra que TP -1,0 antes do AAC termina em -0,9 (falha) e que TP -1,5 termina em -1,3 (passa) com -14,4 LUFS.
5. Aceite no MP4 final de cada modelo (DR19): loudnorm print_format=summary e ebur128 peak=true. Passa se ficar entre -15 e -13 LUFS e com TP até -1,0 dBTP. Voz acima da trilha: RMS em janelas de 400 ms só nos trechos de fala (DR20), com pelo menos 10 dB de folga [PRIOR].
6. Pausas: ouvir 13,37 a 13,79 s e 31,63 a 31,95 s (B03). Registro a medida de DR02 no arquivo final, mas não a uso como portão: o corte de 40 dB é PRIOR sem método (P01).
7. Trocar o `dentista-audio-masterizado.mp4` já entregue, que tem TP -0,3 dBTP (J-M1), por uma versão que passe no aceite do passo 5.

### P8. Ampliação de 576x1024 para 1080x1920

Reaproveito o base.mp4 que já existe (1080x1920, 30 fps CFR, 1093 quadros, crf 14, codificado pelo ffmpeg desta máquina, J-M3). Não amplio de novo: o custo já foi pago e uma nova ampliação não tem ganho medido. O filtro usado é sem dado (B17). Riscos e controle:
- Pele lavada no zoom: zoom máximo de 1,10x (2,06x da fonte).
- Halo no recorte: a máscara de 360x640 vem de 320x320 interno (F31), cerca de 6 px por ponto na vertical. Desfoco a borda em 3 px e encolho 2 px (F4 R3).
- Gente ao fundo em 44 quadros (F30): fico só com o maior componente conexo. O scipy existe no cbenv (F4, cabeçalho) e falta no python3 do sistema (medido por esta cadeira).
- Corte em y=470 (F29): sai do comp.py.
- Unsharp leve (P18) só se o quadro de teste mostrar pele lavada; teste de 1 quadro.

### P9. Pipeline e tempo de render

Só ferramentas existentes: Playwright com Chromium, ffmpeg 6.1.1, numpy, rembg (máscara já pronta), HTML, SVG e Canvas. Nada instalado.

| Modelo | Conta [ESTIMATIVA com os custos por quadro de F26] | Total |
|---|---|---|
| A | trás 1093 x 0,099 = 108 s; frente 1093 x 0,131 = 143 s; composição 1093 x 0,52 = 568 s; áudio 10 s; sem bloco de granulação (economiza 151 s em relação à conta da F4) | cerca de 829 s, 14 min |
| B | painel 1093 x 0,08 = 87 s; frente 1093 x 0,131 = 143 s; subquadros em 10 janelas (150 x 4 x 0,131 = 79 s); composição 568 s; áudio 10 s | cerca de 887 s, 15 min (conta da F4) |
| C | trás 108 s; frente 143 s; subquadros só em cerca de 6 s (180 quadros x 2 extras x 0,131 = 47 s); composição 568 s; áudio 10 s; mistura dos subquadros em numpy: sem dado | cerca de 876 s, 15 min, mais o custo sem dado da mistura |
| Os três em série | 829 + 887 + 876 | cerca de 43 min; em paralelo piora (F28) |

Não otimizo a composição para filtros do ffmpeg agora (economizaria cerca de 470 s por modelo, F4 2.1): o teste custa cerca de 15 min, tem risco de borda diferente (B15) e economiza menos de 25 min de máquina no total. O tempo de máquina é barato; o caro é refação.

Antes de cada render cheio: render cronometrado de 300 quadros (B13). Portão: se o custo por quadro medido passar de 2x o estimado, o motion blur de C cai para 1 subquadro (sem blur) e o B perde os subquadros.

Conferências obrigatórias antes da composição: 1093 PNG por camada (o comp.py pula quadro faltante em silêncio, F33); render(t) sem Math.random (F32).

### P10. CTA

Uso o CTA gravado: "Dentista, comenta sua profissão aqui que eu te respondo" (32,00 a 35,92 s, F11; a fala não tem o "a", words-raw.json). Texto na tela: **"Comenta: DENTISTA"** em balão SVG digitando (A21). TABULEIRO não entra no vídeo: só no comentário fixado e só se o alcance passar de 150 em 48 h (F20; 06-plano-final.md seção 4). Custo escondido: "eu te respondo" exige resposta à mão do Bruno (00-enquadramento, gatilho 2). Por isso entra no plano o tempo de resposta como métrica (P13).

### P11. Conformidade com a publicidade odontológica

A Res. 196/2019 foi lida no texto oficial pela F3 (F72). A pergunta 11 diz que não foi, mas o livro de fatos corrige isso. Nos 3 modelos não entra boca, dente real, raio X, procedimento, instrumental, cadeira odontológica, antes e depois, preço, "grátis", sorteio, promessa de faturamento ou de agenda, "melhor técnica" nem caso de terceiro (F72, F73). Reacts só como ícones genéricos: relógio, quadro de aula, gráfico, caixa, mão levantada e balão. Nenhum comentário inventado com @ e nenhum contador falso: o bloco final do ov2.html com "1.287 comentários" sai (F32). "Segundo produto" é afirmação de modelo de negócio, não promessa de resultado [HIPÓTESE, P12; B21 continua aberto]. O Bruno pode não ser inscrito em CRO (B20), mas o art. 45 alcança o dentista que repostar (F73).

### P12. Prova Tzur

**Não entra na tela.** Os motivos:
1. O Bruno não disse o case nesta tomada (F10), e um rodapé sem fala fica solto.
2. A autorização do cliente Tzur é sem dado (B24).
3. "De 6 para 20 milhões" ao lado de dentista pode ser lido como promessa de faturamento (F72, vedada).

Custo de deixar de fora: zero de render. Custo de pôr sem autorização: risco de relação com cliente e de conselho, que não cabe em R$ 0 de verba. A tomada "com case" de 26/10 (J-M4) é o lugar certo para essa decisão, com autorização escrita.

### P13. Métrica, fonte, data e critério de parar

| Métrica | Fonte | Leitura | Corte |
|---|---|---|---|
| Alcance | ig_post_stats (Buzzfy), só leitura | 48 h (sáb 31/10 12h) e 7 dias (qui 05/11) | abaixo de 53 em 48 h: o modelo não se repete no próximo nicho; 106 ou mais em 7 dias: passa |
| Pulo | ig_post_stats | 7 dias (05/11) | abaixo de 68% = passa a afirmação da D2 e D3; abaixo de 60% = DOBRAR pelo 06-plano-final; acima de 75% = PARAR o formato no nicho. Os dois cortes (C1) não brigam: 68% é o piso de sucesso e 60% é o gatilho de dobrar |
| Tempo médio assistido | ig_post_stats | 7 dias | referência de 6,2 s (mediana) e 18,6 s (melhor), F12 e F14 |
| Comentários "dentista" e conversas qualificadas | ig_comments e listCommentAutomationLogs (PostZen), só leitura; planilha de leads | 7 dias | 0 conversa com alcance de 106 ou mais: TESTAR a porta, não o formato (06-plano-final seção 4) |
| Tempo de resposta do Bruno aos comentários | planilha de leads | 7 dias | mediana acima de 24 h [PRIOR] = o CTA "eu te respondo" está custando lead |
| Custo de produção por modelo | log da agência (horas de agente e minutos do Bruno) | ao fim de cada render | refação acima de 1 rodada por modelo tira o modelo do ciclo; render acima de 2x o estimado corta o blur |

Registro em conteudo/sistema-instagram/semanas/2026-11-05.md (Módulo 7).

### P14. Regras de texto

Português do Brasil, sem travessão, sem emoji, sem citar HighClass, Júnior Prazeres ou Felipe Roser. A única estrutura de contraste dos 3 vídeos é a falada, "deixa de disputar paciente e passa a formar quem disputa" (06-plano-final linha 139); nenhum letreiro cria uma segunda. O separador "·" da tarja não é travessão. Conferência automática antes do render: busca pelos códigos U+2014 e U+2013 (travessão e meia-risca) e pela faixa de emoji em todos os HTML e JSON de texto.

---

## 2. Decisões: opções, efeitos, premissas e posição

### D1. Áudio masterizado

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. voz_master.wav como está | custo zero | TP -0,5 no wav e -0,3 no AAC (J-M1): falha no aceite e com SFX somados piora |
| 2. Remaster a partir de voz_master: TP -1,5 antes do AAC, duas passadas, mistura com trilha e SFX, aceite no MP4 final | cerca de 10 min de máquina por modelo; passa no pico (J-M2) | vira cadeia padrão dos 5 nichos: um script, cinco usos |
| 3. Refazer do raw.wav comparando rn_std, rn_sh e rn_bd | horas de escuta comparada | ganho medido de no máximo 0,3 dB de distância fala e pausa (16,3 contra 16,0, DR02); atraso na aprovação |
| 4. Regravar só 24,94 a 29,04 s | voz nova | não casa com a boca; inútil para vídeo de selfie |
| 5. Fora do óbvio: não mexer na fala agora; usar a tomada de 26/10 se o ouvido reprovar o trecho (J-M4) | zero hoje | depende da sessão acontecer; pode empurrar a publicação se a sessão atrasar |

Premissas: o Bruno avalia o áudio pelo ouvido, não pelo número de 40 dB [HIPÓTESE]; a mistura com trilha e SFX não sobe o LRA nem o pico além do que a segunda passada corrige [HIPÓTESE, conferível no aceite].
**Posição: opção 2, com a 5 como seguro.** O critério de 40 dB é um PRIOR que nenhuma versão cumpre (DR02). Pelo critério escrito no enquadramento, a probabilidade de sucesso é baixa. Se o critério de pausa virar ouvido mais registro, sobe para 0,70 [faixa 0,55 a 0,85].
**Probabilidade pelo critério do enquadramento: 0,15 [faixa 0,05 a 0,30]. Confiança: 0,6.**

### D2. Modelo A

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. Tzur v2 fiel (manifesto P&B, confete, aplausos, bloco final com granulação) | cerca de 16 min de render, com 151 s só na granulação (F4 2.1) | carrega confete (partícula, banido), RGB split, tremida e prova social inventada (F32); arrisca regra do CLAUDE.md e da F48 |
| 2. Tzur v2 enxuto (4 letreiros) | mais barato | pode parecer pobre diante do "estilo After Effects" pedido [HIPÓTESE] |
| 3. Tzur v2 fiel + legenda palavra a palavra | mais completo | soma os custos e os riscos da opção 1 |
| 4. Fora do óbvio: A enxuto com 8 letreiros, legenda palavra a palavra, P&B só até o "474" (2 s), sem confete, sem granulação e sem prova inventada | cerca de 14 min de render; 95,3% de rosto | vira o molde-base: B e C herdam os letreiros e a legenda, e o custo de B e C cai |
| 5. Letreiro só na frente, sem máscara | economiza a composição (568 s) | fere "letreiro saindo de trás" pedido pelo Bruno; descartada |

Premissas: o efeito do Bruno falando (2,4x a 5,8x, F13) se repete em nicho estreito [HIPÓTESE frágil; terceiros do nicho tiveram de 494 a 764 views, F58]; o letreiro atrás não derruba retenção (sem dado, F66).
**Posição: opção 4.**
**Probabilidade pelo critério do enquadramento (produção ok e, se publicado, alcance de 106 ou mais e pulo abaixo de 68% em 7 dias): 0,35 [faixa 0,18 a 0,52].** Conta: produção 0,85 [PRIOR] x desempenho 0,40 [PRIOR, faixa 0,20 a 0,55; os 3 melhores reels com o Bruno passariam (F14 e 00-SISTEMA), mas o nicho puxa para baixo (F58)]. **Confiança: 0,4.**

### D3. Modelos B e C

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. B = sab8a + gdgtify; C = alex-prompter + máscara de tipo | C precisa de cena de prova que não existe (F10) | inventar prova fere a regra; deixar buraco quebra o esqueleto |
| 2. B = tela dividida; C = gdgtify | cobre o pedido literal "dividindo com reacts"; C com rosto 100% | B usa a biblioteca da Série 2, o que reaproveita código pago |
| 3. Só B agora, C depois do resultado | economiza cerca de 15 min de máquina e horas de agente | descumpre "faça outros 2"; perde o molde de C para os 4 nichos seguintes; o custo de não agir passa a ser confiança |
| 4. Não fazer B e C | menor custo | descumpre o pedido; meu ponto cego em ação |
| 5. Fora do óbvio: B e C como moldes parametrizados por words.json, renderizados no dentista como prova e reaproveitados em consórcio, nutri, psicólogo e advogado; ordem A, B, C com portão de custo | custo marginal de cerca de 15 min de máquina por modelo, uma vez | amortização em 5 nichos [ESTIMATIVA: 1 construção para 5 usos]; se o portão estourar, C muda de data, mas não morre |

Premissas: júri cego de 3 cadeiras mede acabamento, não conversão (P17); B entrega clareza da mensagem por mostrar a representação ao lado do rosto [HIPÓTESE]; o protocolo do júri ainda não existe (B25).
**Posição: opção 5 com o conteúdo da opção 2.** B = tela dividida (stokebuilder-356793, twoclipping-551116, twoclipping-000267). C = título fixo e tipografia cinética com órbita e quietude (gdgtify-929495, twoclipping-041659, techhalla-498547, sab8a-475686).
**Probabilidade pelo critério do enquadramento (júri igual ou acima de A nas duas peças e, se uma for publicada, 106 ou mais e pulo abaixo de 68%): 0,30 [faixa 0,15 a 0,50]. Confiança: 0,35.**

---

## 3. Ideias e hipóteses numeradas (80)

| # | Ideia ou hipótese | Confiança | Evidência |
|---|---|---|---|
| 1 | O arquivo de áudio já entregue falha no pico (-0,3 dBTP) e precisa ser trocado antes do Bruno aprovar | alta | J-M1 |
| 2 | Aplicar TP -1,5 antes do AAC e aceitar -1,0 no arquivo final resolve o conflito C7 | alta | J-M2 |
| 3 | Medir sempre no MP4 final, nunca no wav: o AAC sobe o pico em cerca de 0,2 a 0,4 dB | alta | J-M1 (wav -0,5 para AAC -0,3); J-M2 (-1,5 para -1,3) |
| 4 | O corte de 40 dB nas pausas não deve ser portão de aprovação | alta | DR02, P01 |
| 5 | Refazer a redução de ruído a partir do raw não paga o tempo | média | DR02: 16,0 contra no máximo 16,3 dB |
| 6 | Ouvir B02 e B03 custa 5 min e fecha 2 incertezas de texto e áudio | alta | F08, DR02 |
| 7 | Não cortar pausas economiza retrabalho de sincronia em 3 modelos | alta | DR03, DR04: tempos saem direto do words-raw.json |
| 8 | Cortar só as pausas acima de 0,5 s ganharia 1,1 s e mataria a quietude de C | alta | DR03, DR05 |
| 9 | A máscara já paga (589,4 s) deve servir aos 3 modelos | alta | F27 |
| 10 | O corte em y=470 do comp.py põe letreiro sobre a cabeça em 71,6% dos quadros e deve sair | alta | F29 |
| 11 | Faixa de letreiro de y=120 a 450 deixa a parte de cima sempre legível | alta | DR10 (topo mínimo em y=252) |
| 12 | Maior componente conexo da máscara resolve as 44 pessoas ao fundo | média | F30, P22 |
| 13 | O confete do Tzur é partícula banida e custa determinismo; sai | alta | F32, F48 |
| 14 | O bloco com granulação custa 151 s e não tem ganho medido; sai | média | F26, F4 2.1 |
| 15 | Prova social inventada no bloco final é risco de reputação e de regra; sai | alta | F32, CLAUDE.md |
| 16 | Glifos de coração, check e X usados como texto viram SVG; evita leitura de emoji | alta | F32, F4 4.2 |
| 17 | Zoom máximo de 1,10x protege a pele numa fonte de 576 px | média | DR06, F4 R1 |
| 18 | Texto legível no frame 0 nos 3 modelos | média | F53 (10 de 10, N = 10) |
| 19 | Título fixo com a tese em C testa o padrão dos 4 reels com gancho "good" | baixa | F55 (rating qualitativo, N = 4) |
| 20 | A tela dividida é a leitura mais literal de "dividindo com reacts" | média | pedido do Bruno; 00-enquadramento item 6 |
| 21 | Na tela dividida, o rosto fica 100% visível, o que respeita F13 | alta | F4 4.1; F13 |
| 22 | Relógio no lugar de cadeira odontológica tira um risco de conselho a custo zero | média | F72; P11 |
| 23 | Stickers de mão levantada sem texto evitam comentário inventado | alta | F32; F43 |
| 24 | alex-prompter-997524 não serve sem prova falada | alta | F10, F49 |
| 25 | Órbita atrás da cabeça é o efeito do repositório mais próximo do "letreiro 4D" | média | F42 |
| 26 | Mola por letra com 4 quadros de escalonamento dá acabamento de After Effects sem RGB split | baixa | F46; qualidade visual sem dado (B10) |
| 27 | Motion blur só nas janelas de movimento corta o custo de C de 17 a 22 min para cerca de 15 | média | F4 2.1; DR07 |
| 28 | 60 fps dobra o custo sem ganho, porque a fonte tem 30 quadros reais | alta | F02, F4 2.1 |
| 29 | Render em paralelo piora nesta máquina | alta | F28 |
| 30 | Render cronometrado de 300 quadros antes do cheio evita perder 15 min num erro | alta | B13; F33 |
| 31 | Conferir 1093 PNG por camada antes de compor evita vídeo sem letreiro | alta | F33 |
| 32 | Otimizar a composição para ffmpeg não paga agora | média | F4 2.1 (cerca de 470 s por modelo; teste de 15 min, risco de borda) |
| 33 | Publicar só 1 versão em 29/10; as outras viram molde | média | P15 (canibalização é hipótese); 06-plano seção 5 D1 |
| 34 | B e C valem mais como moldes para 4 nichos do que como reels do dentista | média | 06-plano-final: consórcio, nutri, psicólogo, advogado no mesmo mês |
| 35 | A tomada de 26/10 pode substituir o bruto de hoje com custo marginal perto de zero | média | J-M4 |
| 36 | Moldes parametrizados por words.json fazem a troca de tomada custar só o render | alta | arquitetura cap2.js e edit.json (F22) |
| 37 | Revisão do Bruno numa folha só, com 3 vídeos e 3 perguntas, economiza idas e vindas | média | PRIOR de processo |
| 38 | Teto de 1 rodada de refação por modelo | média | PRIOR de caixa; F4 (cada refação soma render e revisão) |
| 39 | "+474 mil" absorve a diferença entre 474.640 e 474.659 | alta | F68, C2 |
| 40 | O rodapé de fonte custa zero e responde à objeção de origem | alta | CLAUDE.md (separar fato de hipótese); F68 |
| 41 | "no Brasil" corrigido não gera descasamento perceptível | média | F09 (0,36 s) |
| 42 | Legenda em bloco nos 2 grupos da virada esconde 2 a 3 palavras de diferença | baixa | F08; HIPÓTESE |
| 43 | Regravar só o trecho é inútil em vídeo de selfie | alta | voz nova não casa com a boca |
| 44 | O Tzur fora da tela custa zero e remove risco de autorização e de promessa | alta | F10, B24, F72 |
| 45 | "Comenta: DENTISTA" na tela reforça o CTA falado | média | F56 (CTA de palavra-chave: 4,8% contra 0,48%, N = 10, outro nicho) |
| 46 | TABULEIRO fica fora do vídeo e só entra no comentário fixado com 150 ou mais | alta | F20 |
| 47 | O tempo de resposta do Bruno é o gargalo escondido do CTA | média | 00-enquadramento gatilho 2 |
| 48 | Pulo abaixo de 68% como piso e abaixo de 60% como gatilho de dobrar resolvem C1 | média | F17, 06-plano seção 4 |
| 49 | A leitura de 48 h decide se o modelo se repete no consórcio ou na nutri | média | 06-plano seção 5 |
| 50 | Comparar A, B e C pelo desempenho com N = 1 é ruído | alta | 00-enquadramento D3 |
| 51 | Um trial reel de B para não seguidores poderia dar uma segunda leitura barata | baixa | B23 sem dado |
| 52 | Sem verba até 18/11, nenhum modelo deve ser impulsionado | alta | F18 |
| 53 | O nicho dentista falando de negócio tem teto baixo de distribuição | média | F58 (máximo de 764 views) |
| 54 | Meta de 106 é alcançável pelo histórico do Bruno falando | média | F14, DR17 |
| 55 | A quietude de 0,60 s antes de "Qual é?" é o melhor ponto de virada do roteiro | média | F07, F47 |
| 56 | SFX alinhado pelo pico evita o efeito "atrasado" | alta | F35, F48 |
| 57 | Riser antes da quietude e silêncio depois cria contraste sem efeito banido | baixa | F47; PRIOR |
| 58 | Poucos SFX (cerca de 12) bastam; mais que isso compete com a voz | baixa | F62 (Hormozi sem SFX nas transições), C4 |
| 59 | A trilha lounge sintetizada evita licença e custo | alta | contexto.md (som.py) |
| 60 | O de-esser só entra com queixa do Bruno | média | ganho sem dado |
| 61 | Reacts a 2 quadros antes da palavra dão a sensação de reação e não de atraso | baixa | F4 4.2; PRIOR |
| 62 | Punch-in de 1,10 em "ensinar o seu colega" marca a tese sem perder qualidade | média | F46, DR06 |
| 63 | A tarja "Bruno · Estrategista de Lançamento" em "Eu desenho" substitui a prova ausente | baixa | F10; HIPÓTESE |
| 64 | Na tela dividida, a legenda sobre a linha divisória não cobre boca nem gráfico | média | F4 4.1 |
| 65 | O recorte da janela pelo centro da máscara segura a cabeça sem zoom extra | média | P19 |
| 66 | O vidstab para prender o letreiro à parede pode ficar para depois | média | B18 não testado; custo de corte de borda (F4 R7) |
| 67 | Halo de 6 px na borda da máscara aparece no cabelo; desfoque de 3 px e erosão de 2 px resolvem | média | F31, F4 R3 |
| 68 | Taxa de quadro variável não afeta, porque o base.mp4 já é CFR | alta | F02, J-M3 |
| 69 | O arquivo final pesa cerca de 64 MB, e a versão leve, cerca de 12 MB | média | DR14 |
| 70 | Apagar os PNG depois da composição libera de 0,5 a 2,4 GB por modelo | alta | DR15, F21 (18 GB livres) |
| 71 | Registrar horas de agente e minutos do Bruno por modelo cria o primeiro dado de custo de produção da conta | alta | sem dado hoje (F4 lacunas) |
| 72 | O júri cego precisa de protocolo escrito antes de ver os vídeos | alta | B25 |
| 73 | Se A passar de 150 de alcance em 48 h, o molde A vira padrão dos 4 nichos seguintes | baixa | F20; PRIOR |
| 74 | Se A ficar abaixo de 53, o problema provável é nicho e gancho, não edição | baixa | F58; N = 1 |
| 75 | A legenda palavra a palavra é o item de maior retorno por custo do plano | média | F61 (80,2% com legenda, nível 3); custo de 143 s |
| 76 | O b-roll de 1,7 s é o único trecho sem rosto em A e não deve crescer | média | F13; P09 (no máximo 30%) |
| 77 | Descrever a cena do b-roll com cartões genéricos evita copiar perfil real de dentista | alta | F72 (caso de terceiro vedado) |
| 78 | O Bruno pode rejeitar A por "parecer barato" sem o bloco final; uma assinatura animada de 0,5 s mitiga | baixa | pré-mortem; pedido "estilo adobe effects" |
| 79 | O valor de 1 cliente (cerca de R$ 49 mil em 3 meses) torna irracional economizar no reel e racional economizar em refação | média | 00-SISTEMA ficha (ticket de referência) |
| 80 | Conversa qualificada de dentista é a métrica que paga o plano; alcance é só proxy | média | 06-plano seção 2.2 (métrica principal) |

---

## 4. Pré-mortem da cadeira J (como este plano fracassa)

1. **Economia que parece pobreza.** O Bruno pediu "profissional estilo adobe effects". Ao tirar o bloco cinematográfico, a granulação e o confete, A pode parecer simples. Ele pede refação e a refação custa mais que o render que economizei. Sinal: a aprovação escrita de A não vem de primeira. Defesa: assinatura animada, letreiros com extrusão completa e quadro de teste aprovado antes do render cheio.
2. **Portão vira gaveta.** C fica atrás de A e B e "muda de data" duas vezes até sumir. O Bruno pediu 3 e recebe 2. É o meu ponto cego em ação. Defesa: data fixa para C, sex 23/10, 18h; se estourar, C sai sem blur, mas sai.
3. **A tomada de 26/10 não acontece ou atrasa.** O seguro da P4 some e a frase da virada fica com legenda em bloco que não casa com a boca. Defesa: decisão de ouvido (B02) até 22/10.
4. **O aceite passa e o ouvido reprova.** -14,4 LUFS e -1,3 dBTP no número, mas a pausa de 13,4 s tem respiração alta (DR02: 4 a 6 dB abaixo da fala). O Bruno ouve "ruído", que era o pedido número 2 dele. Defesa: B03 antes de entregar, com fade de 30 ms nas pausas confirmadas como ruído.
5. **Os moldes não são reaproveitados.** Os nichos seguintes mudam de roteiro ou de enquadramento e o valor de molde de B e C vira zero. Defesa: os moldes leem words.json e lista de letreiros em JSON, sem tempos fixos no código (F34 mostra o erro do Tzur).
6. **Linha do tempo longa demais.** Sem cortar as pausas, 2,98 s de pausa (8%) pesam no pulo, se a regra da VibeRoll estiver certa (P10). Defesa: só a leitura de 7 dias diz. Se o pulo passar de 68%, o próximo nicho testa corte das pausas acima de 0,5 s.
7. **N = 1 lido como verdade.** Um alcance ruim em 29/10 vira "o formato não funciona", quando pode ser o dia ou o nicho (F58). Defesa: a regra da P13 só decide se o modelo se repete, nunca mata o formato do Bruno falando.
8. **Erro de conselho por detalhe.** Um react, o "segundo produto" ou o balão é lido como mercantilização. Defesa: lista do P11 conferida quadro a quadro antes do render. B21 continua aberto.
9. **Estimativa de render errada.** A mistura de subquadros em numpy custa mais que o previsto e o C estoura. Defesa: teste de 300 quadros e portão de 2x.
10. **Atenção do Bruno é o gargalo real.** Três vídeos, uma folha de decisão e um áudio para aprovar em 2 dias podem deixar tudo parado. Defesa: entregar A primeiro, sozinho, com uma pergunta só: "aprova para 29/10?".

---

## 5. Previsões numéricas com data de conferência

| # | Métrica | Previsão [faixa] | Etiqueta | Conferência |
|---|---|---|---|---|
| PV1 | LUFS integrado e TP do MP4 final de cada modelo | -14,4 LUFS [-14,8 a -14,0]; TP -1,3 dBTP [-1,6 a -1,0] | ESTIMATIVA pela J-M2 | 23/10/2026 (aceite da D1) |
| PV2 | Tempo de render medido por modelo | A 14 min [11 a 20]; B 15 min [12 a 22]; C 15 min [12 a 25] | ESTIMATIVA pela F26 | no render, até 23/10/2026 |
| PV3 | Rodadas de refação até a aprovação do Bruno | A 1 [0 a 2]; B 1 [0 a 2]; C 1 [0 a 3] | PRIOR | 28/10/2026 |
| PV4 | Alcance do reel publicado do dentista em 7 dias | 95 [50 a 200] | PRIOR ancorado em F12, F14 e F58 | 05/11/2026 |
| PV5 | Pulo do reel publicado em 7 dias | 62% [50% a 75%] | PRIOR ancorado em F12 e F14 | 05/11/2026 |
| PV6 (D+30) | Alcance acumulado do reel do dentista | 120 [60 a 260] | PRIOR | 20/11/2026 |
| PV7 (D+30) | Conversas qualificadas de dentista atribuídas ao reel | 1 [0 a 3] | PRIOR; base: 1 disparo em 30 dias (00-SISTEMA) | 20/11/2026 |
| PV8 (D+30) | Moldes B ou C usados em pelo menos 1 nicho seguinte | probabilidade de 0,55 [0,30 a 0,75] | PRIOR | 20/11/2026 |
| PV9 (D+60) | Diagnósticos agendados vindos de dentista | 0 [0 a 2] | PRIOR | 20/12/2026 |
| PV10 (D+60) | Moldes A, B ou C usados em pelo menos 3 reels publicados no total | probabilidade de 0,45 [0,20 a 0,70] | PRIOR | 20/12/2026 |
| PV11 (D+90) | Vendas a dentista atribuídas ao reel | 0 [0 a 1] | PRIOR | 19/01/2027 |
| PV12 (D+90) | Custo de produção por reel registrado na planilha (horas de agente e minutos do Bruno) | registro existe para pelo menos 5 reels: probabilidade de 0,50 [0,25 a 0,70] | PRIOR | 19/01/2027 |

---

## 6. O que mudaria minha opinião

- O Bruno ouvir o arquivo novo e reprovar o ruído: subo a prioridade da opção 3 da D1 (refazer do raw) e aceito o custo de horas.
- O render de teste de C custar mais de 2x o estimado: C sai sem motion blur, sem discussão.
- B02 mostrar que ele disse "formar quem disputa": a legenda dos grupos L17 e L18 volta a ter destaque palavra a palavra.
- Métrica do case Tzur v2 (B06) aparecer com alcance abaixo de 53: o letreiro atrás perde a prioridade e A vira variante, com B como principal.
- A sessão de 26/10 ser cancelada: o bruto de hoje é o definitivo, e o ouvido de B02 vira bloqueante.
- Leitura de 48 h acima de 150: o molde do modelo publicado vira padrão dos 4 nichos e o custo de construção se paga.
- O Bruno dizer que prefere publicar as 3 versões: aceito, com 7 dias entre elas e sem impulsionar (P15 é hipótese, não fato).

## 7. Lacunas

- Não ouvi o áudio. B02 e B03 continuam abertos.
- Valor da hora do Bruno: sem dado. O ponto de equilíbrio da seção 0.2 é condicional.
- Taxa de fechamento por reel e churn de cliente: sem dado.
- Custo por quadro da mistura de subquadros em numpy e da tipografia com glifos deformados: sem dado (B14).
- Filtro de ampliação do base.mp4: sem dado (B17). Sei só que foi o ffmpeg desta máquina (J-M3).
- Se a sessão de 26/10 continua marcada depois de o Bruno ter gravado hoje: sem dado.
- Protocolo do júri cego: não existe (B25).
- Desempenho de qualquer dos 3 formatos no Instagram: sem dado (F19, F66).
- Recurso de trial reels na conta: sem dado (B23).
- Não abri os prompts do repositório nem as páginas do CFO; uso F1, F3 e o livro de fatos.

## 8. Fontes

- /home/user/Disparo-/videos/nichos/dentista/god/contexto.md
- /home/user/Disparo-/videos/nichos/dentista/god/run/00-enquadramento.md
- /home/user/Disparo-/videos/nichos/dentista/god/run/01-fatos.md (F01 a F76, C1 a C10, B01 a B25, DR01 a DR20, P01 a P22)
- /home/user/Disparo-/videos/nichos/dentista/god/run/01-pesquisa/F1-repo-opus-prompts.md, F2-padroes-virais-talking-head.md, F3-cfo-e-fatos.md, F4-viabilidade-pipeline.md
- /home/user/Disparo-/videos/nichos/dentista/god/words-raw.json e transcricao-tempos.txt
- /home/user/Disparo-/CLAUDE.md
- /home/user/Disparo-/conteudo/sistema-instagram/00-SISTEMA.md (ficha de entrada, 3 melhores e 3 piores)
- /home/user/Disparo-/conteudo/modo-god-nichos/run/06-plano-final.md (seção 2.2, seção 4, seção 5, linhas 158 e 574 a 575)
- Medições desta cadeira: run/02-cadeiras/evidencias-J/teste_tp_aac.log e J_tp-1.0.m4a, J_tp-1.5.m4a, J_tp-2.0.m4a (J-M2); loudnorm em videos/nichos/dentista/dentista-audio-masterizado.mp4 (J-M1); ffprobe e strings em scratchpad/dent/base.mp4 (J-M3)
