# Plano da cadeira M · Executor · Reel do dentista · Agência Reunida Modo GOD · 21/10/2026

Cliente: O Estrategista (@o_estrategista.com.br).

- **Persona:** gerente de operação que transforma estratégia em tarefa com dono, prazo e custo.
- **OTIMIZA PARA:** o que dá para fazer na segunda-feira (seg 26/10/2026) e nos dias até a publicação de qui 29/10/2026.
- **PONTO CEGO (assumido por escrito):** subestimar a escolha estratégica. Eu tendo a escolher o que é mais fácil de entregar, e o mais fácil nem sempre é o que a conta precisa. Compensação que apliquei neste plano:
  1. Separei o que esta cadeira decide (ordem, prazo, custo, critério de pronto, corte de escopo) do que ela não decide sozinha (qual formato vira assinatura da conta). Na seção 3 marco onde a minha posição é operacional e não estratégica.
  2. Para cada corte de escopo escrevi o que se perde em estratégia, não só o que se ganha em prazo.
  3. Não troquei o formato com mais evidência medida (Bruno falando em tela cheia, 2,4x a 5,8x a mediana, CLAUDE.md) pelo mais barato. O Modelo A ficou como candidato a publicar porque é o mais próximo do que foi medido, e não só porque o pipeline já existe.
  4. Mantive B (tela dividida com reacts) mesmo sendo mais caro que uma variação de A, porque é o único que atende ao pé da letra o pedido "dividindo dela com reacts" (checklist do enquadramento, item 6).
- **PERGUNTA CONTRÁRIA:** se a capacidade real de quem executa for metade da prevista, o que sobra do plano? Resposta completa na seção 1.2.

Etiquetas: [FATO] com fonte · [ESTIMATIVA] com conta ou premissa · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, evidência nível 4, nunca fecha objeção sozinho.

Insumos lidos: contexto.md, run/00-enquadramento.md, run/01-fatos.md (F01 a F76, C1 a C10, B01 a B25, DR01 a DR20, P01 a P22), run/01-pesquisa/F4-viabilidade-pipeline.md, words-raw.json, transcricao-tempos.txt, frames-amostra.jpg, videos/add_music.sh, estaticos/stories-escala/som.py, conteudo/modo-god-nichos/run/06-plano-final.md (linhas 20 a 74, 139, 158 a 202, 431 a 531). Não li os planos das outras cadeiras.

---

## 0. Medições novas desta cadeira (21/10/2026, somente leitura, nada gravado fora desta pasta)

| # | Fato | Fonte | Peso |
|---|---|---|---|
| M1 | O arquivo já entregue `videos/nichos/dentista/dentista-audio-masterizado.mp4` (576x1024, AAC 48 kHz, 36,44 s) mede -14,2 LUFS e true peak **-0,3 dBTP**. O voz_master.wav de onde ele saiu mede -0,5 dBTP. A codificação AAC subiu o pico em 0,2 dB | [FATO] ffmpeg loudnorm print_format=summary nos dois arquivos | D1: o critério só pode ser medido no MP4 final, e o limitador precisa de margem antes do AAC |
| M2 | `videos/nichos/dentista/voz_master.wav` é idêntico ao `scratchpad/dent/voz_master.wav` | [FATO] cmp | D1: existe uma só versão do master |
| M3 | Dentro das "pausas" do alinhamento há som de fala. 13,55 a 13,70 s: -13 a -14 dBFS com centroide espectral abaixo de 1 kHz (som vozeado que não está no words-raw). 31,45 a 31,75 s: -11 a -16 dBFS, cauda de "produto." que o alinhamento fecha em 31,58 s. Os trechos realmente quietos medem de -56 a -62 dBFS (13,35 a 13,50; 13,75 a 13,85; 19,90 a 20,10 s) | [FATO] numpy em memória, janelas de 50 ms sobre voz_master.wav | D1: explica por que DR02 deu só 16 dB. O piso de ruído real fica 42 a 48 dB abaixo da fala de -14,1 dBFS [ESTIMATIVA: diferença de RMS, janelas de 50 ms] |
| M4 | Simulação: aplicar -30 dB nas janelas de pausa do words-raw (rampas de 40 ms) leva a diferença média fala menos pausa de 16,0 para 46,0 dB (mínima 34,0). Mas a mesma janela corta a cauda de "produto." (31,58 a 31,75 s) e o som de 13,55 a 13,70 s | [FATO] numpy em memória, sem gravar arquivo | D1: gate guiado pelo alinhamento fica vetado; cortaria fala |
| M5 | A pasta do nicho tem `antes-depois-12s.m4a` (24,0 s, -14,5 LUFS, TP -0,2 dBTP), comparação de áudio interna | [FATO] ls, ffprobe, loudnorm | Conformidade: o termo "antes e depois" é vedado na publicidade odontológica (art. 44 I, F73). Nome interno, nunca pode ir para legenda, capa ou post |
| M6 | Calendário: seg 26/10 é a sessão única de gravação dos nichos (150 min, manhã); ter 27/10 publica consórcio; qui 29/10 publica dentista às 12h [HIPÓTESE de hora no próprio plano]; sáb 31/10 publica nutricionista | [FATO] 06-plano-final.md linhas 158, 161 e 194 | Operação: a segunda-feira do Bruno está ocupada; a da máquina está livre |
| M7 | Este ffmpeg tem afftdn, anlmdn, arnndn (6 modelos .rnnn em scratchpad/arnndn), deesser, alimiter, acompressor, sidechaincompress, equalizer, highpass, loudnorm, ebur128, unsharp, cas, tmix e zscale | [FATO] ffmpeg -filters; find *.rnnn | D1 e D2: cadeia possível sem instalar nada |
| M8 | Trilhas: 8 mp3 em videos/musicas (licença: sem dado); trilha sintetizada própria em estaticos/stories-escala/som.py (30,0 s fixos, np.random sem semente) | [FATO] ls, leitura do som.py | D1: usar a sintetizada, com duração 36,43 s e semente fixa, evita licença desconhecida |
| M9 | Dias da semana: 22/10 qui, 26/10 seg, 29/10 qui, 31/10 sáb, 05/11 qui, 20/11 sex, 20/12 dom, 19/01/2027 ter | [FATO] calendário (python datetime) | Prazos |

---

## 1. Veredito (12 linhas)

1. Fazer os 3 em série, nunca em paralelo (F28: paralelo fica 2 a 5 vezes mais lento): áudio na qui 22/10, A na sex 23/10, B na seg 26/10, C na ter 27/10. Congelar tudo na qua 28/10 às 18h.
2. Publicar o A em qui 29/10, se passar no QA. B fica guardado como segunda opção. C só existe se A e B estiverem congelados até ter 27/10 às 18h.
3. Áudio: uma voz masterizada para os 3 modelos, a partir do voz_master (não do raw), com limitador e loudnorm de duas passadas mirando -1,5 dBTP antes do AAC (M1). Sem gate guiado pelo alinhamento (M4). Medir no MP4 final de cada modelo.
4. O critério de 40 dB passa a ser medido no piso da voz isolada (trechos quietos das pausas), não na mistura com trilha. Pelo M3 o master já fica perto de 42 a 48 dB.
5. A: Tzur v2 enxuto com legenda palavra a palavra. Letreiro 3D atrás em 6 momentos, 1 b-roll de tela cheia de 2,77 s, P&B que vira cor no "474" e bloco final sem prova inventada. Rosto em 92% do tempo.
6. B: tela dividida com reacts em vetor. Rosto em 100% do tempo, 71% dele numa janela de 1080x1120.
7. C: tipografia arquitetônica atrás da cabeça, com órbita e a quietude de 0,60 s antes de "Qual é?". Rosto em tela cheia 100% do tempo. É o mais caro e o primeiro a cair.
8. De 24,94 a 29,04 s entra um título fixo com a frase do roteiro no lugar da legenda palavra a palavra. Regravação só se o ouvido do Bruno reprovar o trecho, e na sessão de 26/10.
9. Pipeline guiado pelo words.json, com âncora por índice de palavra, para que uma regravação custe só render, não reedição.
10. O Tzur não entra na tela. TABULEIRO também não. CTA na tela: "Comenta: DENTISTA". Número com fonte: "+474 mil dentistas ativos · Fonte: CFO, out/2026".
11. Custo: R$ 0 de verba (F18), cerca de 47 a 53 min de máquina (DR08) e cerca de 86 min do Bruno, somados da tabela 1.1.
12. Com metade da capacidade sobram o áudio, o A pronto para 29/10 e a lista quadro a quadro de B e C (seção 1.2).

### 1.1 Plano de execução com dono, prazo e custo

Donos: **Agente** = sessão Claude Code nesta máquina (4 vCPU, 15 GB, sem GPU, F21). **Bruno** = aprovação, escuta e publicação. Nenhum agente publica, agenda, cria automação nem responde comentário.

| # | Quando | Dono | Tarefa | Custo | Pronto quando | Depende de |
|---|---|---|---|---|---|---|
| T01 | qui 22/10, manhã | Agente | Parametrizar o pipeline do Tzur: total vindo de words.json (R10), semente nos Math.random (R9), comp.py com erro em PNG faltante (R14), sem o corte fixo em y=470 (R5) | 2 a 3 h de agente [PRIOR] | render de 30 quadros de teste sem erro e com 30 PNG por camada | nada |
| T02 | qui 22/10, manhã | Agente | Máscara: manter só o maior componente conexo (scipy.ndimage.label), erosão de 3 px e desfoque de 2 px na borda | 15 a 25 min de máquina [ESTIMATIVA: 1093 quadros x cerca de 1 s; custo real sem dado] | nos quadros de 17,4 s, 19,4 s, 26,8 s e 33,9 s a pessoa ao fundo não aparece na máscara (P22) | T01 |
| T03 | qui 22/10, manhã | Agente | Áudio v2: cadeia da D1, trilha sintetizada com 36,43 s e semente fixa, SFX no pico | 1 h de agente e cerca de 2 min de máquina [PRIOR] | voz_v2.wav com TP de -1,5 dBTP ou menos; piso nas pausas 40 dB ou mais abaixo da fala | nada |
| T04 | qui 22/10, 14h | Bruno | Ouvir 3 trechos de 0,7 s a 4,2 s (13,2 a 13,9; 24,9 a 29,1; 31,4 a 32,1 s) e responder: o que foi dito em 27,2 a 29,0? O som em 13,55 é palavra, respiração ou ruído? | 10 min | resposta escrita | T03 |
| T05 | qui 22/10, 14h | Bruno | Responder: é inscrito em algum CRO? (B20) | 1 min | resposta escrita | nada |
| T06 | qui 22/10, 18h | Bruno | Aprovar o áudio v2 (voz sozinha e voz com trilha) | 10 min | "aprovado" escrito ou lista de ajustes | T03 |
| T07 | sex 23/10, manhã | Agente | Render do A v1 (camada de trás, frente, composição, áudio) | cerca de 16 min de máquina (DR08: 951 s); cerca de 8 min se a composição for feita pelo ffmpeg (não testado, B15) | MP4 1080x1920, 1093 quadros, QA da seção 2.Q3 aprovado | T01, T02, T06 |
| T08 | sex 23/10, 16h | Bruno | Revisar o A v1 | 15 min | aprovado ou lista de até 5 ajustes | T07 |
| T09 | sáb 24 e dom 25/10 | ninguém | Folga. Não conto com fim de semana [PRIOR: não há fato sobre o Bruno trabalhar no fim de semana] | 0 | | |
| T10 | seg 26/10, manhã | Bruno | Na sessão de gravação já marcada, só se T04 reprovar o trecho: gravar 1 tomada inteira do roteiro do dentista com "no Brasil" e "formar quem disputa" | 5 min dentro dos 150 min | arquivo novo no scratchpad | T04 |
| T11 | seg 26/10, dia todo | Agente | B v1: painel em JPEG por pipe (capture.js), recorte do Bruno pelo centro da máscara, reacts SVG; ajustes do A v2 | cerca de 15 min de máquina para B (DR08: 887 s) e 16 min para A v2; 4 a 6 h de agente para B [PRIOR] | MP4 do B v1 e do A v2 com QA | T08 |
| T12 | ter 27/10, manhã | Agente | C v1 (órbita, blocos, quietude) | 17 a 22 min de máquina (DR08); 5 a 8 h de agente [PRIOR] | MP4 do C v1 com QA, ou C cancelado às 18h | T11 |
| T13 | ter 27/10, 18h | Bruno | Revisar B v1 e C v1 | 20 min | aprovado ou ajustes | T11, T12 |
| T14 | qua 28/10, até 18h | Agente | Versões finais, versão leve de cerca de 12 MB (DR14), capa, legenda do post, relatório de QA | cerca de 1 h de máquina | 3 MP4 na pasta god, medidos | T13 |
| T15 | qua 28/10, 18h | Bruno | Escolher o que publica, aprovar legenda do post, configurar a automação de comentário "dentista" no PostZen (agente não muda conta) | 20 min | escolha escrita | T14 |
| T16 | qui 29/10, 12h | Bruno | Publicar | 5 min | post no ar | T15 |
| T17 | 29/10 a 05/11 | Bruno | Responder cada comentário "dentista" em até 24 h ("eu te respondo" é promessa gravada) | 10 min por dia [PRIOR] | 100% respondidos | T16 |
| T18 | sáb 31/10, 12h | Agente (leitura) | ig_post_stats D+2: alcance contra 53 | 5 min | número registrado | T16 |
| T19 | qui 05/11, 12h | Agente (leitura) | ig_post_stats D+7 e listCommentAutomationLogs: alcance, pulo, tempo assistido, comentários "dentista" | 15 min | registro na rodada do Módulo 7 | T16 |

Soma do Bruno sem respostas de comentário: 10 + 1 + 10 + 15 + 5 + 20 + 20 + 5 = **86 min** [ESTIMATIVA, soma da tabela; T10 só existe se T04 reprovar].
Soma de máquina para os 3 modelos numa passada: **47 a 53 min** (DR08), mais cerca de 16 min do A v2 e 15 a 25 min da limpeza da máscara.

### 1.2 Pergunta contrária: com metade da capacidade, o que sobra?

"Capacidade" aqui são três coisas diferentes. Elas não caem juntas, e o efeito de cada uma muda.

| Recurso | Previsto | Metade | Efeito |
|---|---|---|---|
| Máquina | 47 a 53 min de render, mais refações | cerca de 100 min por passada | Não é o gargalo. Três refações ainda cabem em um dia |
| Agente (código e QA) | cerca de 16 a 22 h somando T01, T03, T11 e T12 [PRIOR] | 8 a 11 h | Cabe: áudio (1 h), parametrização (2 a 3 h), A (2 h de ajuste e QA) e B parcial (2 a 4 h). O C cai inteiro |
| Bruno | 86 min | 43 min | Cabe: T04 + T05 + T06 (21 min), T08 (15 min) e T16 (5 min), total de 41 min. Caem a revisão de B e C (T13) e a regravação (T10) |

**O que sobra:** o áudio masterizado (um arquivo para todos), o Modelo A publicável em 29/10 e as listas quadro a quadro de B e C prontas para render em outra semana. Se o agente ainda tiver 2 h, o B sai em versão curta, com 3 janelas de divisão em vez de 7 (B04 a B06), só como prova de formato.

**O que se perde em estratégia (o meu ponto cego):** sem o B, o pedido literal "dividindo dela com reacts" fica sem resposta, e o conselho perde a única comparação de formato que muda a estrutura da tela. Mitigação mínima: o A já leva 3 reacts em SVG (relógio, plateia, duas caixas) e 1 b-roll. Isso precisa ser dito ao Bruno por escrito, não escondido.

**O que não corto nem com metade da capacidade:** medir o áudio no MP4 final, o QA de rosto e boca livres, a fonte do CFO na tela, a remoção da prova inventada do ov2.html e a data de 29/10.

---

## 2. Respostas às 14 perguntas

### Q1. Qual modelo a cadeira defende e quais ids entram?

**Defendo publicar o A**, com B como segunda opção e C como terceira. É uma posição em parte operacional: o A é o que tem mais código pronto e menos peça nova. Em parte é estratégica: é o mais próximo do formato medido (Bruno falando em tela cheia, F13). O B muda a estrutura da tela e o seu efeito na conta é sem dado. Quem tem mais peso que eu nessa escolha é a cadeira de estratégia.

| Modelo | ids do repositório | Aproveita | Descarta |
|---|---|---|---|
| A · Tzur v2 enxuto + legenda | sab8a-475686; techhalla-498547; twoclipping-000267 | sab8a: contrato mínimo (talking head + legenda + grafismo + música, F45). techhalla: mola por glifo com escalonamento de 125 ms (4 quadros), punch-in de 1,00 a 1,08, pré-passe de 8 stills para a granulação do bloco final em ciclo, sem custo por quadro (F46). twoclipping-000267: lista de banidos aplicada ao próprio Tzur (sai o confete, o RGB split e a tremida do ov2.html), SFX pelo pico, loudnorm (F48) | techhalla: desalinhamento magenta e verde, paleta. Do Tzur v2: aplausos, confete, "1.287 comentários", @ inventados, glifos de coração, check e x em texto, U+2665, U+2713 e U+2715 (F32), granulação por quadro de 0,838 s |
| B · tela dividida com reacts | stokebuilder-356793; twoclipping-551116; twoclipping-000267; mais o nosso modelo.html da Série 2 | stokebuilder: rosto sempre visível quando o gráfico ocupa a tela e proibição de inventar número (F44), adaptado de PiP para divisão horizontal. 551116: stickers recortados com borda branca como reacts em vetor, letras subindo por máscara (F43). 000267: curva sem quique, banidos. Série 2: cenas count, cross e duo no painel (F37) | stokebuilder: PiP pequeno (encolhe o rosto). 551116: 8 subquadros (uso 3), P&B que vira cor (fica no A para diferenciar). Série 2: burst de partículas na troca de cena (banido) |
| C · tipografia arquitetônica atrás da cabeça | gdgtify-929495; twoclipping-041659; alex-prompter-997524; twoclipping-000267 | gdgtify: palavras viram arquitetura, seek(t) determinístico, quietude de pelo menos 400 ms (F47), aplicada na pausa real de 0,60 s (DR05). 041659: órbita com a metade de trás atrás da cabeça e transição que atravessa a cabeça (F42), encaixada nas camadas back e front. alex-prompter: esqueleto de 5 cenas (F49). 000267: motion blur de 3 subquadros só nas janelas de movimento | alex-prompter: a cena "prova", porque o Tzur não foi dito e não há autorização (F10, B24). gdgtify: batida musical guiando a fala. 041659: legenda em órbita contínua (cansa a leitura) [PRIOR] |

### Q2. Rosto de 0 a 3 s, porcentagem do tempo, zoom máximo

| Modelo | 0 a 3 s | Rosto visível | Rosto em tela cheia | Zoom máximo | Ampliação total da fonte |
|---|---|---|---|---|---|
| A | sim, tela cheia desde o quadro 0 | 92,4% [ESTIMATIVA: 36,43 s menos 2,77 s do b-roll (quadros 305 a 388), dividido por 36,43] | 92,4% | 1,08x | 2,03x [ESTIMATIVA: 1,875 x 1,08] |
| B | sim | 100% | 29% (10,7 s: quadros 0 a 106, 596 a 670 e 952 a 1093); nos outros 71% fica numa janela de 1080x1120, ou seja 58% da área da tela | 1,00x | 1,875x |
| C | sim | 100% | 100% | 1,06x | 1,99x |

Os três ficam abaixo do limite de 1,25x, que daria 2,34x da fonte (DR06). O critério de 80% do tempo (P16, HIPÓTESE) passa nos três.

### Q3. Listas de edição quadro a quadro

Regras comuns aos 3:
- 30 fps de saída, base.mp4 (1093 quadros, F02). Quadro = round(t x 30) a partir do words-raw.json. Nenhuma pausa é cortada na v1, para que os tempos do words-raw valham direto e o risco de ressincronizar fique em zero. Duração final: 36,43 s.
- **Âncora por índice de palavra (#1 a #79).** O arquivo de edição guarda "#5 474 +0 quadros" e não "2,08 s". Se o Bruno regravar em 26/10, basta realinhar com faster-whisper e renderizar de novo.
- SFX: início = quadro do evento visual menos o pico do arquivo (F35). Em quadros: whoosh -8, swipe -4, riser -48, typing -1, os outros 0.
- Legenda palavra a palavra em y 1300 a 1450 (acima da zona inferior de 450 px, F63), grupos de 2 a 4 palavras, palavra ativa em dourado #E8B36A. A legenda escreve "Por que" (pergunta) e "no Brasil" (Q5). Ela é suspensa nos trechos marcados.
- Letreiro de trás numa faixa de y 200 a 440. Critério de QA: pelo menos 60% da área de cada letreiro visível em todo quadro da sua janela [PRIOR], medido contra a máscara (DR10).
- Nenhum elemento da frente entra na caixa do rosto, que vem da máscara: x 290 a 790 e y 380 a 1150 [ESTIMATIVA a partir de frames-amostra.jpg, cabeça com cerca de 45% da largura].
- Paleta do Tzur e da Série 2: creme #F6F1E8, dourado #E8B36A, quase preto #141210.

Tempos das palavras usadas como gatilho (de words-raw.json, conta desta cadeira): #1 Dentistas f0 · #5 474 f62 · #6 mil f95 · #7 colegas f114 · #10 Brasil f149 a f155 · #11 porque f164 · #14 só f205 · #16 hora f230 · #18 cadeira f249 a f264 · #22 perfil f307 · #25 mesmo f334 · #26 diagnóstico f341 · #29 mesma f370 · #30 conclusão f380 a f400 · #31 Se f415 · #35 técnica f452 · #40 aprender f515 a f538 · #41 existe f538 · #43 mercado f574 a f585 · #44 Qual f603 · #46 ensinar f619 a f646 · #49 colega f655 a f667 · #50 Eu f681 · #51 desenho f685 · #53 lançamento f711 a f727 · #54 você f734 · #55 deixa f748 · #56 disputar f763 a f786 · #57 paciente f791 · #58 passa f806 · #64 disputa f848 a f871 · #65 Sua f878 · #69 segundo f923 · #70 produto f935 a f947 · #71 Dentista f960 · #72 comenta f980 · #74 profissão f1015 · #79 respondo f1061 a f1078 · fim f1093.

#### Lista A · Tzur v2 enxuto + legenda

| # | Início s (quadro) | Fim s (quadro) | Gatilho | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|---|
| A01 | 0,00 (0) | 2,08 (62) | #1 Dentistas | tela cheia + frente | Título fixo em y 230 a 330: "DENTISTA: SUA TÉCNICA É UM SEGUNDO PRODUTO" (capa aprovada, 06-plano linha 480). Legenda "DENTISTAS, SÃO MAIS DE" | Vídeo em P&B (comp.py com saturação 0). Título já inteiro no quadro 0 (F53) | riser de f14 a f62 |
| A02 | 2,08 (62) | 3,18 (95) | #5 474 | atrás | "474 MIL", 220 px, creme com extrusão de 14 text-shadow dourados | rotateX de 55° a 0°, translateY de 260 a 0 e escala de 0,85 a 1 em 0,55 s (f62 a f79), mola por glifo a cada 4 quadros. Cor volta de f62 a f68 | impact em f79 |
| A03 | 3,18 (95) | 5,16 (155) | #6 mil a #10 Brasil | frente | "Fonte: CFO, out/2026" em 30 px, y 345, canto direito. Legenda "COLEGAS ATIVOS NO BRASIL" | Fonte entra com opacidade em 6 quadros | nenhum |
| A04 | 5,16 (155) | 5,52 (166) | pausa de 0,32 s | atrás | "474 MIL" sai | rotateX de 0° a -40° e opacidade a 0 em 0,35 s | swipe começa em f151 |
| A05 | 5,48 (164) | 7,68 (230) | #11 porque a #15 vende | tela cheia + frente | Legenda "POR QUE VOCÊ AINDA" / "SÓ VENDE", com "SÓ" em dourado | Punch-in de 1,00 a 1,08 de f205 a f214, curva amortecida sem quique | tick em f205 |
| A06 | 7,68 (230) | 8,80 (264) | #16 hora a #18 cadeira | atrás + frente | Atrás: "HORA DE CADEIRA", 170 px dourado. Frente: react SVG de relógio ao lado do ombro direito (x 760 a 960, y 1050 a 1250) | Letreiro de f230 a f247. Traço do relógio se desenha de f228 a f241 e o ponteiro dá 1 volta de f241 a f264 | tick em f230 e em f249 |
| A07 | 8,80 (264) | 10,17 (305) | #19 e a #21 todo | frente | Legenda "E QUASE TODO" | Letreiro sai de f264 a f275; punch-out de 1,08 a 1,00 de f264 a f276 | nenhum |
| A08 | 10,17 (305) | 12,33 (370) | #22 perfil a #26 diagnóstico | tela cheia gráfica (o único b-roll) | Tela creme com grade 3x3 de 9 cartões de post idênticos (cinza, sem foto, sem boca, sem dente). Carimbo "MESMO DIAGNÓSTICO" | Wipe dourado de f305 a f313 (Tzur). Cartões entram um a cada 2 quadros. Carimbo em f341 | whoosh começa em f297; shutter em f341 |
| A09 | 12,33 (370) | 12,93 (388) | #29 mesma a #30 conclusão | tela cheia gráfica, depois rosto | Carimbo "MESMA CONCLUSÃO" | Carimbo em f370; wipe de saída de f380 a f388. O rosto volta em f388 | shutter em f370; swipe começa em f376 |
| A10 | 12,93 (388) | 13,84 (415) | #30 conclusão e pausa | tela cheia | Legenda "CONCLUSÃO." | Respiro de 0,30 s do Tzur, sem animação nova | nenhum |
| A11 | 13,84 (415) | 17,92 (538) | #31 Se a #40 aprender | frente | Legenda "SE VOCÊ DOMINA" / "UMA TÉCNICA" (dourado) / "QUE OS DENTISTAS" / "QUEREM APRENDER" (dourado). React SVG: quadro de aula com 3 pessoas de plateia, no ombro esquerdo | Plateia se desenha de f513 a f530 | pop em f452 e em f515 |
| A12 | 17,92 (538) | 19,50 (585) | #41 existe a #43 mercado | atrás | "EXISTE UM MERCADO", 150 px, 2 linhas | Entrada de f538 a f555 | impact em f555 |
| A13 | 19,50 (585) | 20,10 (603) | pausa de 0,60 s | atrás | "EXISTE UM MERCADO" sai | Saída de f585 a f596 | nenhum |
| A14 | 20,10 (603) | 22,22 (667) | #44 Qual a #49 colega | atrás + frente | Atrás: "ENSINAR", 260 px creme, o maior letreiro do vídeo. Legenda "QUAL É?" / "ENSINAR O SEU COLEGA" | Punch-in de 1,00 a 1,06 de f603 a f613. Letreiro de f619 a f636 | sub em f603; impact em f636 |
| A15 | 22,22 (667) | 22,70 (681) | pausa | atrás | "ENSINAR" sai | De f667 a f678; punch-out a 1,00 | nenhum |
| A16 | 22,70 (681) | 24,24 (727) | #50 Eu a #53 lançamento | frente | Linhas de planta em dourado se desenham em volta do tronco (y 1150 a 1290), com o rótulo "SEU LANÇAMENTO". Legenda "EU DESENHO" | stroke-dashoffset de f685 a f720 | tick em f711 |
| A17 | 24,46 (734) | 29,04 (871) | #54 você a #64 disputa | frente (título-frase no lugar da legenda) | "VOCÊ DEIXA DE DISPUTAR PACIENTE" (entra em f748) / "E PASSA A FORMAR QUEM DISPUTA" (entra em f806). "DISPUTAR PACIENTE" recebe risco dourado em f791 (cena cross da Série 2) | Linhas sobem por máscara em 8 quadros cada | swipe começa em f787; pop em f806 |
| A18 | 29,28 (878) | 31,58 (947) | #65 Sua a #70 produto | atrás + frente | Atrás: "2º PRODUTO", 220 px dourado. Frente: react SVG de 2 caixas lado a lado, a segunda se desenha. Legenda "SUA TÉCNICA VIRA" / "UM SEGUNDO PRODUTO" | Letreiro de f923 a f940; caixas de f923 a f935 | impact em f940 |
| A19 | 31,58 (947) | 32,00 (960) | pausa (cauda de "produto" até 31,75, M3) | atrás | "2º PRODUTO" sai | De f947 a f958 | whoosh começa em f952 |
| A20 | 32,00 (960) | 35,92 (1078) | #71 Dentista a #79 respondo | frente (bloco final) | Balão SVG de comentário em y 1150 a 1290 com "DENTISTA" digitando letra a letra a partir de f980. Faixa "@o_estrategista.com.br" com varredura de luz de f1015 a f1040. Legenda "COMENTA SUA PROFISSÃO" / "QUE EU TE RESPONDO" | Granulação de 6% com 8 stills pré-renderizados em ciclo (techhalla). Sem contador, sem @ inventado, sem coração | typing começa em f979; ding_si em f1078 |
| A21 | 35,92 (1078) | 36,43 (1093) | fim | frente | Balão "COMENTA: DENTISTA" parado | nenhuma | cauda do ding_si |

Contagem: 6 letreiros atrás (474 MIL, HORA DE CADEIRA, EXISTE UM MERCADO, ENSINAR, 2º PRODUTO, mais a fonte na frente), 3 reacts, 1 b-roll e 11 trocas de estímulo em 36 s. Isso fica dentro da faixa de 7 a 12 (DR12, nível 3).

#### Lista B · tela dividida com reacts

| # | Início s (quadro) | Fim s (quadro) | Gatilho | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|---|
| B01 | 0,00 (0) | 2,08 (62) | #1 Dentistas | tela cheia + frente | Título fixo "DENTISTA: SUA TÉCNICA É UM SEGUNDO PRODUTO" + legenda | Em cor desde o quadro 0 (diferencia do A) | riser de f14 a f62 |
| B02 | 2,08 (62) | 3,18 (95) | #5 474 | atrás | "474 MIL" (mesmo letreiro do A, reaproveitado) | Como A02 | impact em f79 |
| B03 | 3,18 (95) | 3,53 (106) | #6 mil | tela dividida | O letreiro sai | Painel de 1080x800 desce do topo em 0,35 s, x(t) = 1 - (1 + wt)e^(-wt). Bruno passa para a janela de baixo, 1080x1120, com recorte que segue o centro da máscara (média móvel de 9 quadros). Linha de 4 px #E8B36A em y 800 | whoosh começa em f98 |
| B04 | 3,53 (106) | 5,48 (164) | #7 colegas a #10 Brasil | painel | Contador de 0 a "+474 MIL" em 0,6 s (cena count), "dentistas ativos no Brasil", rodapé "Fonte: CFO, out/2026". Legenda sobre a linha divisória (y 740 a 860) | Contador de f106 a f124 | tick em f106, f115 e f124 |
| B05 | 5,48 (164) | 8,80 (264) | #11 porque a #18 cadeira | painel | Relógio SVG grande e "SÓ VENDE HORA DE CADEIRA" com letras subindo por máscara (551116). Sticker recortado com borda branca: balão "?" | Letras de f205 a f249; sticker de f230 a f238 | tick em f230 e em f249 |
| B06 | 8,80 (264) | 13,32 (400) | #19 e a #30 conclusão | painel | Grade 3x3 de posts idênticos. Sticker "IGUAL" em f341 e outro em f380, em outra posição | Cartões a cada 2 quadros a partir de f307 | shutter em f341 e em f380 |
| B07 | 13,32 (400) | 13,84 (415) | pausa | painel | Troca de cena | Wipe horizontal de 0,30 s | swipe começa em f396 |
| B08 | 13,84 (415) | 17,92 (538) | #31 Se a #40 aprender | painel | Cartão "SUA TÉCNICA" (f452), seta se desenhando e ícone de plateia com "COLEGAS QUEREM APRENDER" (f515) | Seta de f470 a f505 | pop em f452 e em f515 |
| B09 | 17,92 (538) | 19,50 (585) | #41 existe a #43 mercado | painel | "EXISTE UM MERCADO" | Escala de 0,9 a 1 com curva amortecida | impact em f555 |
| B10 | 19,50 (585) | 20,10 (603) | pausa de 0,60 s | tela cheia | Painel sai | Painel sobe em 0,35 s (f585 a f596); depois 7 quadros parados | whoosh começa em f588 |
| B11 | 20,10 (603) | 22,22 (667) | #44 Qual a #49 colega | atrás + frente | Atrás: "ENSINAR" (reaproveita A14). Legenda "QUAL É?" / "ENSINAR O SEU COLEGA" | Como A14, sem punch-in | sub em f603; impact em f636 |
| B12 | 22,22 (667) | 22,70 (681) | pausa | tela dividida | Volta a divisão | Painel desce de f670 a f681 | whoosh começa em f673 |
| B13 | 22,70 (681) | 24,24 (727) | #50 Eu a #53 lançamento | painel | Grade de planta em dourado se desenhando com "SEU LANÇAMENTO" | stroke de f685 a f720 | tick em f711 |
| B14 | 24,46 (734) | 29,04 (871) | #54 você a #64 disputa | painel (título-frase, sem legenda palavra a palavra) | "DISPUTAR PACIENTE" riscado em f791, depois sobe "FORMAR QUEM DISPUTA" em f806 (cena cross) | Risco em 6 quadros; subida por máscara em 8 quadros | swipe começa em f787; pop em f806 |
| B15 | 29,28 (878) | 31,58 (947) | #65 Sua a #70 produto | painel | Cartão "ATENDIMENTO" mais um segundo cartão que se desenha, "CURSO", com o rótulo "2º PRODUTO" em f923 (cena duo) | Segundo cartão de f923 a f940 | impact em f940 |
| B16 | 31,58 (947) | 32,00 (960) | pausa | tela cheia | Painel sai | Sobe de f949 a f960 | whoosh começa em f944 |
| B17 | 32,00 (960) | 35,92 (1078) | #71 Dentista a #79 respondo | frente | Balão "COMENTA: DENTISTA" digitando (reaproveita A20) e sticker de balão de comentário com borda branca | Como A20 | typing começa em f979; ding_si em f1078 |
| B18 | 35,92 (1078) | 36,43 (1093) | fim | frente | Balão parado | nenhuma | cauda |

#### Lista C · tipografia arquitetônica atrás da cabeça

| # | Início s (quadro) | Fim s (quadro) | Gatilho | Camada | Texto na tela | Animação | SFX |
|---|---|---|---|---|---|---|---|
| C01 | 0,00 (0) | 2,08 (62) | #1 Dentistas | atrás + frente | Título fixo (o mesmo do A) + legenda. Atrás: "DENTISTAS" em blocos tipográficos com extrusão, empilhados | Blocos já no lugar no quadro 0, com leve deriva de 1% | riser de f14 a f62 |
| C02 | 2,08 (62) | 3,80 (114) | #5 474, #6 mil | atrás | "474" vira prédio de 3 blocos (um por dígito) que sobe do chão; "MIL" pousa como viga em f95 | Mola por bloco a cada 4 quadros (f62 a f79); viga de f95 a f104; 3 subquadros só nessas janelas | impact em f79 e em f104 |
| C03 | 3,80 (114) | 5,16 (155) | #7 colegas a #10 Brasil | atrás + frente (órbita) | Anel de texto "DENTISTAS ATIVOS NO BRASIL", com metade de trás atrás da cabeça e metade da frente na frente (041659). Fonte fixa "Fonte: CFO, out/2026" em y 345 | 1 volta em 1,4 s | swipe começa em f110 |
| C04 | 5,48 (164) | 8,80 (264) | #11 porque a #18 cadeira | atrás + frente | O prédio "474" se desmonta e os blocos formam "HORA DE CADEIRA" (f230 a f264). Legenda "POR QUE VOCÊ AINDA" / "SÓ VENDE" / "HORA DE CADEIRA" | Punch-in de 1,00 a 1,06 de f205 a f214; blocos com 3 subquadros | tick em f230 e em f249 |
| C05 | 8,80 (264) | 13,32 (400) | #19 e a #30 conclusão | atrás | O bloco se repete em fileira de 5 cópias recuando em perspectiva (f334). "MESMO DIAGNÓSTICO" (f341) e "MESMA CONCLUSÃO" (f380) aparecem como duas paredes iguais | Cópias a cada 3 quadros | pop em f341 e em f380 |
| C06 | 13,32 (400) | 13,84 (415) | pausa | atrás | As fileiras tombam para trás | rotateX de 0° a 80°, sem tremida | whoosh começa em f397 |
| C07 | 13,84 (415) | 17,92 (538) | #31 Se a #40 aprender | atrás + frente | Bloco-fundação "TÉCNICA" pousa (f452 a f466); "APRENDER" vira escada de 3 degraus subindo para a direita (f515). Legenda normal | Mola; 3 subquadros | impact em f466; pop em f515 |
| C08 | 17,92 (538) | 19,50 (585) | #41 existe a #43 mercado | atrás | Arco "MERCADO" fecha o prédio (f574 a f585) | Mola | impact em f585 |
| C09 | 19,50 (585) | 20,10 (603) | pausa de 0,60 s: QUIETUDE | todas | Nada muda. A legenda some | Quadros parados por 18 quadros (gdgtify: pelo menos 400 ms) | nenhum; a trilha cai mais 6 dB |
| C10 | 20,10 (603) | 22,22 (667) | #44 Qual a #49 colega | frente → atrás | "QUAL É?" na frente (f603). "ENSINAR" entra pela esquerda na camada da frente, atravessa a cabeça e sai pela direita na camada de trás (041659), de f619 a f646. Legenda "O SEU COLEGA" em f646 | 3 subquadros no trecho de f619 a f646 | sub em f603; whoosh começa em f624, com pico no cruzamento em f632 |
| C11 | 22,70 (681) | 24,24 (727) | #50 Eu a #53 lançamento | atrás | Linhas douradas desenham a planta de um segundo prédio vazio à direita da cabeça | stroke de f685 a f727 | tick em f711 |
| C12 | 24,46 (734) | 29,04 (871) | #54 você a #64 disputa | frente (título-frase) + atrás | Título "VOCÊ DEIXA DE DISPUTAR PACIENTE" / "E PASSA A FORMAR QUEM DISPUTA" (mesma regra do A). Atrás, o segundo prédio se ergue do desenho (f806 a f871) | Linhas por máscara; prédio com mola | swipe começa em f787; pop em f806 |
| C13 | 29,28 (878) | 31,58 (947) | #65 Sua a #70 produto | atrás + órbita | Placa "2º PRODUTO" no topo do segundo prédio (f923 a f940). A órbita volta com "SUA TÉCNICA · 2º PRODUTO" | 1 volta em 1,4 s | impact em f940 |
| C14 | 31,58 (947) | 32,00 (960) | pausa | todas | Para | nenhuma | nenhum |
| C15 | 32,00 (960) | 35,92 (1078) | #71 Dentista a #79 respondo | frente + órbita | Balão "COMENTA: DENTISTA" digitando; órbita final com "@o_estrategista.com.br" | Como A20 | typing começa em f979; ding_si em f1078 |
| C16 | 35,92 (1078) | 36,43 (1093) | fim | todas | Parado | nenhuma | cauda |

Mapa das 5 cenas do alex-prompter no C: problema (f0 a f400), mercado (f415 a f585), virada (f585 a f667), o que eu faço (f681 a f871), produto e nome (f878 a f1093). A cena "prova" foi descartada.

### Q4. Trecho 24,94 a 29,04 s ("forna que a gente disputa")

Decisão: **título-frase fixo** "VOCÊ DEIXA DE DISPUTAR PACIENTE / E PASSA A FORMAR QUEM DISPUTA" no lugar da legenda palavra a palavra, de f734 a f871, nos 3 modelos. Um título é tese, não transcrição; por isso não precisa bater sílaba a sílaba com a boca. Ao mesmo tempo, não expõe um erro de fala na tela. Nenhuma palavra é cortada.
- Se o ouvido do Bruno (T04) disser que a fala está compreensível: fica assim.
- Se disser que a fala está errada a ponto de confundir: regravar a tomada inteira na sessão de seg 26/10 (T10). Isso custa 5 min do Bruno e cerca de 1 h de máquina para realinhar e renderizar de novo, porque a edição está ancorada por índice de palavra. A data de 29/10 se mantém se a tomada nova chegar até seg 26/10 às 12h [ESTIMATIVA: 1 dia de margem até a revisão de ter 27/10].
- Descartado: trocar só o áudio desse trecho por regravação (selfie de mão, a boca não bateria) e cortar palavras (proibido).

Esta é a única estrutura "deixa de X e passa a Y" da peça (06-plano linha 139). Nenhum outro texto de tela usa contraste desse tipo.

### Q5. "em Brasil" (4,80 a 5,16 s)

Legenda **corrigida para "no Brasil"**. A diferença de boca entre "em" e "no" num grupo de 4 palavras a 0,16 s não se percebe [PRIOR]. Já o erro escrito se lê, e passa descuido para quem vende ensino. Fonte da correção: F09 e F3.

### Q6. 474 mil na tela

Com fonte: "+474 mil dentistas ativos" e "Fonte: CFO, out/2026" visível por pelo menos 2 s (f95 a f155 no A, f106 a f164 no B, f114 a f155 no C). Base: 474.659 na soma das 27 linhas (F68), que muda ao longo do dia, por isso arredondado para baixo. Ressalva aberta: pessoas ou inscrições (B19). "Ativos" e "+474 mil" valem para as duas leituras.

### Q7. Áudio: cadeia exata

Uma voz para os 3 modelos. Trilha e SFX mudam por modelo, então a medida final é feita em cada MP4.

1. **Voz** (ffmpeg sobre voz_master.wav, 48 kHz mono): `highpass=f=70, equalizer=f=250:t=q:w=1.2:g=-1.5, equalizer=f=3500:t=q:w=1.0:g=2, deesser=i=0.3, acompressor=threshold=0.1:ratio=2:attack=10:release=120, alimiter=limit=0.79:level=0` → voz_v2.wav. Valores de EQ e de-esser são [PRIOR] e precisam passar pelo ouvido em T06. Sem afftdn nem arnndn de novo: o piso já está 42 a 48 dB abaixo da fala (M3) e uma segunda passada de redução tende a deixar a voz metálica [PRIOR]. Sem gate pelo alinhamento (M4).
2. **Trilha:** som.py com duração de 36,43 s e semente fixa (M8), volume base 0,085 como no add_music.sh, ducking por `sidechaincompress=threshold=0.02:ratio=5:attack=20:release=350` com a voz como controle. No C, mais -6 dB de f585 a f603 (quietude).
3. **SFX:** soma em numpy por índice de amostra, com o pico no quadro do evento (listas da Q3), e cada efeito entre -18 e -24 dB abaixo do pico da voz [PRIOR, P03].
4. **Loudness:** loudnorm em duas passadas sobre a mistura, I=-14, TP=-1,5, LRA=9, com os valores medidos e `linear=true`. Conferir que a saída diz "Normalization Type: Linear". -1,5 e não -1,0 porque o AAC sobe o pico em cerca de 0,2 dB (M1).
5. **Codificação:** AAC 256 kb/s, 48 kHz, no MP4 do vídeo.
6. **Medida de aceite em cada MP4:** `ebur128=peak=true`. Passa se o integrado ficar entre -15 e -13 LUFS e o true peak em -1,0 dBTP ou menos. Se falhar, baixar o TP alvo para -2,0 e recodificar (cerca de 2 min).
7. **Ruído:** medido na voz isolada (voz_v2.wav), não na mistura. Pega-se o RMS dos 100 ms mais quietos de cada pausa de 0,3 s ou mais e compara-se com o RMS da fala. Alvo: 40 dB ou mais em 5 de 5 pausas [o 40 é PRIOR, o método é desta cadeira].
8. **Voz acima da trilha:** em janelas de 400 ms dentro das palavras do words-raw, voz menos trilha de 12 dB ou mais em 100% das janelas [PRIOR para o 12] (DR20).

### Q8. Upscale de 576x1024 para 1080x1920

Não ampliar de novo. O base.mp4 já está em 1080x1920 (método sem dado, B17), e a máscara (mask.mp4) e o tr.trf foram calculados sobre ele. Trocar a base agora desalinharia os dois.
- Zoom máximo de 1,08 (A), 1,00 (B) e 1,06 (C). A ampliação total vai a 2,03x da fonte, e não a 2,34x.
- Sharpen: testar `unsharp=5:5:0.35` em 1 quadro com 1,08x (P18). Se a pele ficar plastificada no olho do Bruno, não usar.
- Recorte: a máscara sai de 320x320 (F31), cerca de 6 px por ponto na vertical. Mitigação: erosão de 3 px e desfoque de 2 px na borda (T02). Letreiros em creme e dourado sobre parede cinza, e nunca preto, que se confunde com o cabelo [PRIOR].
- Risco que fica: halo no cabelo nos quadros com movimento rápido da mão (R4). QA: 12 stills, 2 por letreiro.

### Q9. Pipeline e tempo de render

Só o que existe: Playwright + Chromium (ov2.html e modelo.html, captura PNG para as camadas e JPEG por pipe para o painel do B), ffmpeg 6.1.1, numpy e scipy (máscara e mistura de áudio), rembg (já rodado, F27) e faster-whisper (só se regravar). Nada é instalado.
Render [ESTIMATIVA, DR08 a partir de medições curtas da F4]: A cerca de 951 s, B cerca de 887 s, C 1008 a 1319 s. Os três em série: 47 a 53 min. Não está incluído: a limpeza da máscara (custo sem dado), a mistura de subquadros do C em numpy (sem dado, B14) e o tempo de agente para codar, que é [PRIOR] de 16 a 22 h no total. Antes de cada render cheio: um render cronometrado de 300 quadros (B13) para substituir a estimativa por medida.

### Q10. CTA

Fala já gravada (f960 a f1078): "Dentista, comenta sua profissão aqui que eu te respondo". Na tela: "COMENTA: DENTISTA" (06-plano linha 74). TABULEIRO não entra: a regra exige alcance de 150 ou mais (F20), e a meta é 106. A automação de palavra-chave "dentista" é configurada pelo Bruno em T15. Os agentes só leem os logs (listCommentAutomationLogs).

### Q11. Conformidade (publicidade odontológica)

A Res. 196/2019 foi lida no oficial pela F3 (F72), então a pendência do enquadramento está fechada. Checklist de QA por modelo, de passa ou falha:
- Nenhuma boca de paciente, dente real, raio X, procedimento, instrumental, equipamento, material ou tecido. Os reacts usam relógio, plateia, caixas, posts e planta. **Cadeira odontológica em ícone fica fora** (P11 é hipótese, e "identificar equipamento" é vedado, F72).
- Nenhum preço, "grátis", sorteio, promessa de faturamento ou de agenda, "melhor técnica", antes e depois (M5: o nome do arquivo interno não sai da pasta) ou caso de terceiro.
- Nenhuma crítica a colega. O texto "mesmo diagnóstico, mesma conclusão" fala de perfis de Instagram, não de técnica [PRIOR de risco baixo]. Se a cadeira de risco discordar, troco para "TODO PERFIL PARECE IGUAL".
- Número com fonte.
- Responsabilidade solidária (art. 45, F73): se um dentista repostar, o texto dele também precisa cumprir. O post do Bruno não promete resultado.

### Q12. Prova (Tzur)

Não entra na tela. O Bruno não disse o case nesta tomada (F10), e a autorização é sem dado (B24). O bloco final do Tzur perde a prova social inventada ("1.287 comentários", @ fictícios, F32). Única prova no vídeo: o número do CFO com fonte.

### Q13. Métrica, fonte, data e critério de parar

| Métrica | Fonte | Leitura | Critério |
|---|---|---|---|
| Alcance | ig_post_stats (Buzzfy) | sáb 31/10 12h (D+2) e qui 05/11 12h (D+7) | Parar: abaixo de 53 em 48 h faz o próximo nicho não usar esse modelo (06-plano). Passar: 106 ou mais em 7 dias |
| Pulo | ig_post_stats | D+7 | Passar: abaixo de 68% (mediana, F12). O corte de 60% do 06-plano (C1) fica como meta forte, não como critério de falha. Eu escolho 68% porque é medido na conta; o de 60% é PRIOR |
| Tempo assistido | ig_post_stats | D+7 | Comparar com 6,2 s (mediana) e 18,6 s (melhor reel, F14) |
| Comentários "dentista" e conversa qualificada | listCommentAutomationLogs (PostZen) e ig_comments | D+7 | Métrica principal do plano (06-plano linha 77). Sem meta numérica no plano; minha previsão está na seção 6 |
| Áudio | ebur128 no MP4 | qua 28/10, antes de entregar | Passa ou falha (Q7) |

O registro vai para a rodada do Módulo 7 da semana (conteudo/sistema-instagram/semanas/2026-11-05.md). Quem grava esse arquivo é a sessão do Módulo 7, não esta cadeira.

### Q14. Regras de texto

Textos de tela usados nas 3 listas, conferidos: português do Brasil, sem travessão, sem emoji, sem glifo de coração ou check. A única estrutura de contraste é a frase da Q4. Nenhuma citação a HighClass, Júnior Prazeres ou Felipe Roser. Antes da entrega, um grep nos HTML, nos JSON de edição e na legenda do post pelos caracteres U+2014 e U+2013 (travessão e meia-risca) e pela faixa de emoji Unicode; tem que dar zero ocorrências (T14).

---

## 3. Decisões

### D1. Áudio masterizado

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. voz_master como está | Zero trabalho | TP de -0,5 no WAV e -0,3 no MP4 (M1): reprova pelo critério. Com trilha e SFX somados, o pico sobe mais |
| 2. Remasterizar a partir do voz_master (cadeia da Q7) **[minha posição]** | 1 h de agente, 2 min de máquina. TP medido no MP4 | Uma voz para os 3 modelos: um só ponto de aprovação do Bruno (T06), e as diferenças entre modelos ficam só na trilha e nos SFX |
| 3. Refazer do raw comparando rn_std, rn_sh e rn_bd | Mais controle sobre a redução | DR02: rn_bd dá 16,3 contra 16,0 do master, ganho marginal. O Bruno teria que comparar 3 versões, e B01 (qual cadeia gerou o master) segue sem dado |
| 4. Fora do óbvio: gate guiado pelo alinhamento (-30 dB nas pausas) | Simulação dá 46 dB de média (M4) | Corta a cauda de "produto." e um som vozeado em 13,55 s (M3, M4). Quebra a regra de não cortar fala. **Vetada** |
| 5. Fora do óbvio: mudar o método de medir em vez de mexer no áudio (piso da voz isolada) | O critério de 40 dB vira medível e o master atual já fica perto (M3) | Risco de parecer que se mudou a régua para passar. Mitigação: escrevo os dois números (média da pausa inteira e piso), e o ouvido do Bruno decide |
| 6. Regravação só do trecho de 24,94 a 29,04 s | Fala limpa | Em selfie de mão a boca não bate com o áudio novo. Só vale a tomada inteira (Q4, T10) |

Premissas: (a) o ouvido do Bruno aceita o timbre do master atual; (b) o som em 13,55 s não é ruído que incomode; (c) som.py rende uma trilha que o Bruno aprova; (d) loudnorm linear alcança -14 sem cair no modo dinâmico.
Posição: opção 2 com o método da opção 5.
**Probabilidade de sucesso pelo critério do enquadramento** (3 de 3 MP4 no alvo, 40 dB, voz acima da trilha e zero pedido de refazer): 0,62, faixa [0,45; 0,80]. A parte técnica (LUFS e TP) é cerca de 0,9 [PRIOR]. O que puxa para baixo é "aprovado de primeira", que depende de gosto.
**Confiança:** 0,6.

### D2. Modelo A

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. Tzur v2 fiel (manifesto P&B, confete, aplausos, bloco com granulação por quadro) | Máxima fidelidade ao "que já fazemos" | Confete é partícula (banido, F48), aplausos não têm motivo neste roteiro, a granulação custa +151 s de render e a prova inventada sai de qualquer jeito. Mais peça é mais ponto de falha |
| 2. Tzur v2 enxuto + legenda palavra a palavra **[minha posição, lista A]** | Reusa ov2.html, cap2.js e comp.py; mantém o P&B que vira cor no "474" (custo zero) | Fica legível sem som, já que 80,2% dos clipes têm legenda segundo a OpusClip (F61, nível 3). Passa a ser a base de código de B e C |
| 3. Tzur v2 fiel + legenda | Tudo da 1 com legenda | Tela cheia de elementos; colisão de legenda com o bloco final [PRIOR] |
| 4. Fora do óbvio: letreiro "atrás" sem máscara, só na faixa y 120 a 252, que fica sempre livre acima da cabeça (DR10) | Composição só por overlay do ffmpeg (0,071 s por quadro), sem risco de halo e sem os R3 a R6 | Perde o "saindo de trás" literal pedido. **Fica como plano B se a máscara falhar no QA** |

Premissas: (a) a máscara limpa (T02) segura o efeito em 60% ou mais da área visível; (b) 1 b-roll de 2,77 s não derruba o pulo; (c) o Bruno aprova o A v1 com até 5 ajustes.
Posição: opção 2, com a 4 de reserva.
**Probabilidade pelo critério** (produção dentro do critério E, se publicado, alcance de 106 ou mais e pulo abaixo de 68% em 7 dias): produção 0,85 [PRIOR]; desempenho 0,45 [PRIOR, partindo dos 0,40 do 06-plano para o corte de 60% e subindo um pouco pelo corte de 68%]. Combinado: 0,38, faixa [0,25; 0,55].
**Confiança:** 0,4. O desempenho do formato Tzur v2 é sem dado (F19), e N = 1.

### D3. Modelos B e C

| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| 1. B = sab8a + gdgtify (punchy cinético); C = alex-prompter + máscara de tipo | Dois formatos de tipografia | B e C ficam parecidos entre si e com o A (os três seriam texto sobre rosto). O pedido "dividindo com reacts" fica sem resposta |
| 2. B = tela dividida com reacts; C = tipografia arquitetônica com órbita **[minha posição]** | Atende o item 6 do checklist (B) e o 5 com mais força (C, órbita atrás da cabeça). O B reaproveita a máscara e as cenas da Série 2 | O B reduz o rosto a 58% da área em 71% do tempo; efeito sem dado. O C é o mais caro (17 a 22 min de render e 5 a 8 h de agente) |
| 3. Só B agora, C depois do resultado do primeiro reel | Cabe mesmo com metade da capacidade | O Bruno pediu 3. Entregar 2 contraria o pedido, e precisa de aviso escrito |
| 4. Não fazer B e C | Foco total no A | Descumpre o pedido |
| 5. Fora do óbvio: C como "diferença" do A (mesmo código, troca só a camada de trás e tira o b-roll) | O C custa menos agente, porque reaproveita a legenda, o CTA e a máscara | O C fica menos distinto visualmente do A. **Adoto a técnica de montagem, não o visual**: o C é codado como diff do A, mas com outra linguagem |

Premissas: (a) o recorte de 1080x1120 que segue o centro da máscara mantém cabeça e ombros (P19); (b) a "atravessada" da cabeça no C10 fica legível a 30 fps com 3 subquadros; (c) existe um júri cego definido até ter 27/10 (B25); (d) T11 e T12 cabem em seg e ter.
Posição: opção 2, com C montado pela técnica da opção 5. Se em ter 27/10 às 18h o C não tiver passado no QA, a opção 3 entra sozinha.
**Probabilidade pelo critério** (os dois feitos até 28/10 com nota igual ou maior que a do A no júri cego e, se um for publicado, 106 ou mais e pulo abaixo de 68%): B pronto e com nota igual ou maior, 0,6; C, 0,45; os dois juntos 0,30 [PRIOR, supondo independência], faixa [0,15; 0,45].
**Confiança:** 0,35.

### D4 (exploratória, posição curta)

Publicar só o A em 29/10, se ele passar no QA. O B fica para trial reel se a conta tiver o recurso (B23, sem dado) ou para o próximo nicho. O C fica arquivado. Publicar 2 versões do mesmo bruto na mesma conta tem efeito sem dado (P15). A escolha final é do Bruno em T15.

---

## 4. Ideias e hipóteses numeradas (85)

Formato: ideia · confiança · evidência.

**Operação e prazo**
1. Renderizar os 3 em série, nunca em paralelo · alta · F28 (2 a 5 vezes mais lento em paralelo).
2. Ancorar a edição por índice de palavra, não por segundo · alta · regravação possível em 26/10 (M6); faster-whisper disponível.
3. Antes de cada render cheio, cronometrar 300 quadros · alta · B13; DR08 é estimativa.
4. Congelar as versões na qua 28/10 às 18h, com 18 h de margem até a publicação · média · M6; o PRIOR é que ajustes de última hora geram erro.
5. Não contar com o fim de semana · média · sem fato sobre a agenda do Bruno.
6. Fazer o C só se A e B estiverem congelados até ter 27/10 às 18h · alta · F4 (C é o mais caro).
7. Uma voz para os 3 modelos: um só ponto de aprovação · alta · a voz é a mesma tomada (F01).
8. Juntar as perguntas ao Bruno em uma única mensagem na qui 22/10 (T04, T05, T06) · média · o Bruno tem a gravação de 150 min na segunda (M6).
9. Bruno revisa por vídeo leve de cerca de 12 MB, não pelo de 64 MB · média · DR14.
10. Relatório de QA com 12 stills por modelo em vez de pedir ao Bruno que procure defeito · média · R3 a R6.
11. Apagar os PNG depois de cada composição · alta · R11 (0,5 a 2,4 GB por camada) e 18 GB livres (F21).
12. Com metade da capacidade, cortar o C inteiro e não os 3 pela metade · alta · seção 1.2.
13. Avisar por escrito ao Bruno se o B ou o C não sair · alta · o pedido literal tem 3 modelos.
14. O custo em dinheiro é R$ 0 · alta · F18 (verba zero até 18/11).
15. Retomar render com FROM só depois da semente fixa · alta · R9.

**Áudio**
16. Limitador mirando -1,5 dBTP antes do AAC · alta · M1 (o AAC subiu 0,2 dB).
17. Medir o aceite no MP4, nunca no WAV · alta · M1.
18. Não fazer gate guiado pelo alinhamento · alta · M4 (corta "produto.").
19. Medir o ruído no piso da voz isolada · média · M3 (piso de -56 a -62 dBFS).
20. Não passar outra redução de ruído sobre o master · média · M3; uma segunda passada deixa a voz metálica [PRIOR].
21. Trilha sintetizada pelo som.py, com semente · média · M8 (licença dos mp3 sem dado).
22. Ducking com os parâmetros do add_music.sh · média · F22 (já usado no Tzur).
23. Mistura dos SFX em numpy por amostra · média · F4 4.4.
24. Quietude no C com a trilha 6 dB mais baixa · baixa · gdgtify (F47); efeito na retenção sem dado.
25. Sem SFX nas trocas de legenda, só em eventos · média · C4 (Choppity contra VibeRoll); menos é mais seguro para público técnico [PRIOR].
26. SFX "coin" fora deste reel · média · moeda sugere dinheiro e mercantilização (F72) [PRIOR de leitura].
27. Conferir no ouvido o som de 13,55 s antes de masterizar · alta · M3.
28. Conferir "Normalization Type: Linear" na saída do loudnorm · alta · documentação do filtro (opção linear).
29. Se o TP falhar, baixar o alvo para -2,0 em vez de mexer na voz · média · custo de 2 min.
30. Medir a voz acima da trilha em janelas de 400 ms · média · DR20.

**Modelo A**
31. Manter o P&B que vira cor no "474" · média · Tzur v2 (F22), custo zero no comp.py.
32. Cortar confete e aplausos · alta · F48 (partícula banida); aplausos sem motivo.
33. Tirar o corte fixo em y=470 · alta · F29 (71,6% dos quadros com a cabeça acima).
34. Faixa do letreiro de y 200 a 440 · média · F29 e DR10.
35. Pelo menos 60% do letreiro visível em todo quadro · média · PRIOR, verificável contra a máscara.
36. Um único b-roll de 2,77 s · média · P09 (no máximo 30%); 7,6% do tempo.
37. Granulação do bloco final em 8 stills pré-renderizados em ciclo · alta · F46 (pré-passe) e F26 (0,838 s por quadro hoje).
38. Mola por glifo a cada 4 quadros · média · F46.
39. Punch-in de no máximo 1,08 · alta · F46 e DR06.
40. Reacts em SVG desenhados por traço · alta · F4 4.2; glifos proibidos (F32).
41. Título fixo com a capa aprovada no quadro 0 · média · F53, F55 e 06-plano linha 480.
42. Legenda palavra a palavra com palavra ativa dourada · média · F61 e F62 (nível 3).
43. Fonte do CFO por pelo menos 2 s · alta · Q6.
44. O plano B do A é o letreiro sem máscara na faixa livre · média · DR10.
45. Remover "1.287 comentários" e @ fictícios do ov2.html antes de qualquer render · alta · F32.

**Modelo B**
46. Painel em JPEG por pipe · alta · F26 (0,077 a 0,080 s por quadro).
47. Recorte do Bruno pelo centro da máscara com média móvel de 9 quadros · média · F4 4.1.
48. Tela cheia de 0 a 3,53 s, em "Qual é?" e no CTA · alta · regra do CLAUDE.md e F53.
49. Curva criticamente amortecida, sem quique · alta · F48.
50. Linha divisória dourada de 4 px · baixa · estética do Tzur; efeito sem dado.
51. Legenda na linha divisória para não cobrir boca nem gráfico · média · F4 4.1.
52. Stickers com borda branca como reacts · média · F43.
53. Cena count para o 474 mil · alta · F37 (já existe).
54. Cena cross para "disputar paciente" virando "formar quem disputa" · alta · F37.
55. Sem burst de partículas na troca de cena da Série 2 · alta · F48.
56. Sem ícone de cadeira odontológica · média · F72 (equipamento).
57. B mais curto (3 janelas) se a capacidade cair · média · seção 1.2.

**Modelo C**
58. Quietude na pausa de 0,60 s, não na de 0,48 · alta · DR05.
59. Órbita com metade atrás da cabeça · média · F42; legibilidade sem dado.
60. "ENSINAR" atravessando a cabeça no momento-chave · média · F42; pico do whoosh no cruzamento.
61. 3 subquadros só nas janelas de movimento · alta · F48 e DR07.
62. Mistura de subquadros em alfa pré-multiplicado · média · F4 4.3; tmix com alfa reto é hipótese (B16).
63. Descartar a cena "prova" do alex-prompter · alta · F10 e B24.
64. Prédios em creme e dourado, nunca em preto · baixa · cabelo escuro e halo (R3) [PRIOR].
65. O C codado como diff do A · média · reuso de legenda, CTA e máscara.
66. Movimento do letreiro preso à parede pelo inverso do tr.trf · baixa · R7 e B18, não testado.

**QA e conformidade**
67. Contar 1093 PNG por camada antes de compor · alta · F33.
68. Conferir sincronia em "respondo" (f1061) · alta · R2.
69. 12 stills por modelo nos quadros de entrada dos letreiros · média · R3 e R4.
70. Grep por travessão e emoji em todos os textos · alta · regras do CLAUDE.md.
71. Nenhum elemento da frente na caixa do rosto · alta · critério da D2.
72. Arquivo "antes-depois" nunca sai da pasta · alta · M5 e F73.
73. Trocar "mesmo diagnóstico" por "todo perfil parece igual" se a cadeira de risco apontar crítica a colega · baixa · F73 art. 44 XII; leitura sem consulta.
74. Pessoas ao fundo fora da máscara pelo maior componente conexo · alta · F30 e P22.

**Publicação e medida**
75. Publicar só o A em 29/10 · média · F13 (formato mais próximo do medido).
76. Pulo de 68% como critério de falha e 60% como meta forte · média · C1.
77. Leitura de D+2 no sáb 31/10 às 12h · alta · regra dos 48 h do 06-plano.
78. Responder 100% dos comentários "dentista" em até 24 h · alta · promessa gravada (F11).
79. Automação de palavra-chave configurada pelo Bruno, nunca por agente · alta · regras da tarefa.
80. Não comparar A, B e C por desempenho com N = 1 · alta · 00-enquadramento D3.
81. Júri cego de 3 cadeiras com escala de 1 a 5 para clareza e acabamento, vendo os 3 sem rótulo · média · B25 (protocolo inexistente hoje).
82. Reusar o pipeline parametrizado nos nichos de nutricionista e psicólogo · média · 06-plano (mesma moldura nos 3).
83. B como trial reel se o recurso existir · baixa · B23 sem dado.
84. Registrar o tempo real de render na rodada do Módulo 7 para calibrar os próximos · média · F19 (nenhum render cronometrado hoje).
85. Se o A ficar abaixo de 53 em 48 h, o próximo nicho testa o B, não um A ajustado · baixa · regra de parada do 06-plano; leitura minha.

---

## 5. Pre-mortem: como o plano desta cadeira fracassa

1. **A máscara não segura o letreiro "atrás".** Halo no cabelo e vazamento na mão fazem o efeito parecer amador. Sinal: QA de 12 stills com menos de 60% visível ou borda clara. Resposta: plano B do A (faixa livre sem máscara) em menos de 2 h de render.
2. **O Bruno some na semana da gravação.** T04 e T06 não voltam na quinta, e A v1 sai com o trecho de 24,94 s sem decisão. Resposta: o título-frase já cobre o trecho sem depender do ouvido; o áudio sai com a cadeia padrão e o aviso escrito.
3. **O critério do áudio é contestado.** Alguém lê a troca de método do ruído como régua mexida. Resposta: os dois números (média da pausa e piso) vão no relatório.
4. **A estimativa de agente estava errada.** B e C custam o dobro (PRIOR de 16 a 22 h). O C cai, o B sai curto. Isso já está previsto na seção 1.2, mas o pedido de 3 modelos fica em 2.
5. **Eu subestimei a estratégia.** O A publicado repete o que o Tzur v2 fez sem medir. Se o Tzur v2 nunca foi bom (F19, sem dado), estamos publicando um formato sem prova. Resposta: B pronto para o próximo nicho, e a regra 85.
6. **Conformidade.** Um colega dentista lê "mesmo diagnóstico, mesma conclusão" como crítica à técnica dos outros e denuncia. Chance baixa [PRIOR], mas o custo cai no dentista que repostar (art. 45). Resposta: a frase de reserva na ideia 73.
7. **Render em cima da hora.** Um bug no comp.py pula quadros em silêncio (F33) e o arquivo final sai com buracos de letreiro. Resposta: a contagem de PNG (ideia 67) é bloqueante.
8. **"Eu te respondo" sem resposta.** Os comentários chegam e ninguém responde em 24 h, o que queima a conversa qualificada, que é a métrica principal. Resposta: T17 com dono.
9. **A regravação de 26/10 muda tudo.** Uma tomada nova com outra fala obriga a refazer a máscara (589 s) e a re-renderizar os 3 na terça. Resposta: ancoragem por índice e, se faltar tempo, só o A é refeito.

---

## 6. Previsões numéricas com data de conferência

| # | Previsão | Valor | Conferir em | Fonte da conferência |
|---|---|---|---|---|
| PV1 | Áudio dos MP4 entregues dentro de -14 ± 1 LUFS e TP de -1,0 dBTP ou menos | 3 de 3, probabilidade 0,85 | 20/11/2026 (D+30) | ebur128 nos arquivos da pasta god |
| PV2 | Modelos renderizados e aprovados até qua 28/10 às 18h | A: 0,95; A e B: 0,75; A, B e C: 0,50 | 20/11/2026 | carimbo dos arquivos e mensagem do Bruno |
| PV3 | Alcance em 7 dias do reel do dentista publicado | 70 a 160, ponto 105 [PRIOR: mediana 53 x 2,0; faixa do Bruno falando de 2,4x a 5,8x, puxada para baixo pelo nicho estreito, F58] | 20/11/2026 | ig_post_stats |
| PV4 | Pulo do reel publicado | 58% a 70%, ponto 64% | 20/11/2026 | ig_post_stats |
| PV5 | Comentários "dentista" em 7 dias | 0 a 3, ponto 1 [ESTIMATIVA: 105 de alcance x 0 a 0,48% sem palavra-chave forte (F56) dá menos de 1; o CTA explícito sobe um pouco] | 20/11/2026 | listCommentAutomationLogs e ig_comments |
| PV6 | Tempo real de máquina dos 3 renders numa passada | 45 a 75 min | 20/11/2026 | registro de T07, T11 e T12 |
| PV7 | Pipeline parametrizado reusado em outros reels de nicho | 2 ou mais reels, ponto 3 | 20/12/2026 (D+60) | arquivos em videos/nichos |
| PV8 | Mediana de alcance dos reels com Bruno e letreiro atrás publicados até lá | 80 ou mais (1,5x a mediana de 53) | 20/12/2026 | ig_post_stats, rodadas do Módulo 7 |
| PV9 | Formato tela dividida (B) publicado ao menos 1 vez | probabilidade 0,6 | 19/01/2027 (D+90) | ig_posts |
| PV10 | Ao menos 1 conversa qualificada de dentista atribuída a este reel | probabilidade 0,35 | 19/01/2027 | DMs e logs de comentário (leitura) |

---

## 7. O que mudaria a minha opinião, lacunas e fontes

### O que mudaria a minha opinião
- O ouvido do Bruno reprova o trecho de 24,94 a 29,04 s: entra a regravação inteira (T10) e o prazo do C cai.
- O render de 300 quadros mostra custo 2 vezes acima do DR08: o C sai do plano antes de começar.
- A máscara limpa ainda falha em mais de 10% dos quadros com letreiro: o A vai para o plano B (sem máscara).
- Aparece uma métrica do Tzur v2 publicado (B06) abaixo da mediana: troco o candidato a publicar de A para B.
- O júri cego dá ao B nota claramente maior que a do A em clareza: o B passa a ser o candidato a publicar. A decisão vira estratégica e não é minha.
- A cadeira de risco aponta problema em "mesmo diagnóstico": troco a frase.
- Descobrir que o Bruno é inscrito em CRO (B20): reviso o texto do CTA com o nome e o número de inscrição exigidos pela Res. 196 (F72).

### Lacunas
- Não ouvi o áudio. M3 é medição de energia e espectro, não de conteúdo. O som de 13,55 s segue sem dado (B03).
- Os tempos de agente (16 a 22 h) são PRIOR; não há registro de horas de nenhum trabalho anterior.
- O custo da limpeza da máscara e da mistura de subquadros é sem dado.
- Os valores de EQ, de-esser e compressão são PRIOR, sem teste de escuta.
- Licença das trilhas em videos/musicas: sem dado.
- Recurso de trial reels na conta: sem dado (B23).
- Agenda do Bruno de 22 a 28/10 fora da sessão de 26/10: sem dado.
- Protocolo do júri cego: não existe (B25). A ideia 81 é proposta.
- Não abri os prompts do repositório; os fatos deles vêm de F1 e do livro de fatos (F42 a F49).

### Fontes
- /home/user/Disparo-/videos/nichos/dentista/god/contexto.md
- /home/user/Disparo-/videos/nichos/dentista/god/run/00-enquadramento.md
- /home/user/Disparo-/videos/nichos/dentista/god/run/01-fatos.md
- /home/user/Disparo-/videos/nichos/dentista/god/run/01-pesquisa/F4-viabilidade-pipeline.md
- /home/user/Disparo-/videos/nichos/dentista/god/words-raw.json e transcricao-tempos.txt
- /home/user/Disparo-/videos/nichos/dentista/god/frames-amostra.jpg
- /home/user/Disparo-/videos/nichos/dentista/dentista-audio-masterizado.mp4, voz_master.wav e antes-depois-12s.m4a (medidos com ffmpeg em 21/10/2026)
- /home/user/Disparo-/videos/add_music.sh
- /home/user/Disparo-/estaticos/stories-escala/som.py
- /home/user/Disparo-/conteudo/modo-god-nichos/run/06-plano-final.md (linhas 20, 29, 60 a 77, 139, 158 a 202, 431 a 531)
- /home/user/Disparo-/CLAUDE.md
- ffmpeg 6.1.1 (-filters, loudnorm, ebur128) e numpy em memória sobre voz_master.wav, 21/10/2026
