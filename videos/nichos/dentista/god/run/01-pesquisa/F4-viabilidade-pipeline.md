# F4 · Viabilidade do pipeline · Reel do dentista · 21/10/2026

Conselho Agência Reunida para O Estrategista (@o_estrategista.com.br). Frente F4: o que já existe, o que dá para reaproveitar, quanto custa em tempo de render e quais riscos técnicos a fonte 576x1024 traz.

Etiquetas: [FATO] com a fonte ao lado · [ESTIMATIVA] com a conta · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, nunca fecha objeção sozinho.

Máquina desta sessão [FATO, nproc, free -g, onnxruntime.get_available_providers(), df -h, 21/10/2026]: 4 vCPU, 15 GB de RAM, sem GPU (só CPUExecutionProvider e AzureExecutionProvider), 18 GB livres em disco. Ferramentas conferidas: ffmpeg 6.1.1, Node 22, Playwright com Chromium em /opt/pw-browsers/chromium, Python cbenv com rembg 2.0.85, onnxruntime 1.31.0, numpy 2.3.5, scipy 1.18.1, pyloudnorm, librosa, DeepFilterLib. Sem OpenCV (import cv2 falha).

As medições de tempo vêm de duas origens: carimbo de data dos arquivos gerados nas rodadas anteriores (stat) e testes curtos rodados nesta rodada no scratchpad (seg.log, bench.py, ffmpeg em 300 quadros). Quando o carimbo só dá teto, está escrito "no máximo". Nada foi instalado; nenhum arquivo fora da pasta god foi alterado (os testes gravaram só no scratchpad).

---

## 1. O pipeline existente, passo a passo

### 1.1 Case Tzur v2 (videos/cases/tzur)

| Etapa | Arquivo | O que faz exatamente | Fonte |
|---|---|---|---|
| 0. Montagem do bruto | sem script no repositório | base.mov 1080x1920, 30 fps, 1627 quadros, 54,23 s, áudio PCM, montado a partir de bruno.mov e pablo.mov seguindo edit.json "cuts" (6 cortes). O script que gerou base.mov e aplausos.wav não está versionado | [FATO] ffprobe em scratchpad/cases/base.mov; grep por "base.mov" no repositório só acha comp.py, cap.js e cap2.js |
| 1. Texto e tempos | edit.json | "cuts" (origem, entrada, saída, início na timeline), "words" (148 pares [segundo, palavra]) e "total": 54.2 | [FATO] edit.json |
| 2. Segmentação | seg.py | lê o vídeo reduzido a 360x640, roda rembg com u2net_human_seg em cada quadro (only_mask), suaviza no tempo com 0,6 x atual + 0,4 x anterior, grava máscara cinza em H.264 crf 12 com "-r 30" fixo | [FATO] seg.py linhas 4 a 15 |
| 3. Overlays | ov2.html + cap2.js | ov2.html expõe render(t, layer). cap2.js injeta edit.json no lugar de __EDIT__, abre Chromium 1080x1920, renderiza primeiro a camada "back" e depois a "front", um PNG transparente por quadro (omitBackground), de 0 a ceil(54,2 x 30). Variável FROM permite retomar a camada da frente a partir de um quadro | [FATO] cap2.js |
| 3a. Camada de trás | ov2.html, array LT | 12 letreiros [início, fim, texto, cor, tamanho, y]. Efeito "3D": 14 text-shadow empilhados (extrusão falsa) + rotateX de 55° para 0° + translateY 260 px para 0 + escala 0,85 para 1, em 0,55 s, saída em 0,35 s. Tamanhos 150 a 260 px, y entre 440 e 580 px | [FATO] ov2.html, constante LT e ramo layer=="back" |
| 3b. Camada da frente | ov2.html | legenda palavra a palavra em grupos de até 4 palavras (quebra em pontuação ou pausa acima de 0,9 s), lista HL de palavras douradas; b-roll em tela creme de c-0,7 s a c+0,9 s em volta de cada corte; wipe dourado; tarja de nome; CTA que digita a palavra-chave; confete em canvas (160 partículas) aos 4,28 s; bloco cinematográfico a partir de 44,45 s (alerta com RGB split e tremida, números flutuando com blur, comentários subindo com contador, corações, revelação da marca com varredura de luz, granulação por canvas a cada quadro) | [FATO] ov2.html |
| 4. Composição | comp.py | lê base.mov em rgb24 e mask.mp4 ampliada para 1080x1920; até 4,28 s converte para P&B, depois satura 1,15; máscara vira alfa com (m-70)/110 e zera tudo acima de y=470; aplica back x (1 - máscara) e depois front por cima; mistura aplausos.wav com atraso de 4280 ms a 0,5; x264 crf 18 preset medium, AAC 192 kb/s | [FATO] comp.py |
| 5. Trilha | videos/add_music.sh | trilha a 0,085, bass +3 dB em 90 Hz, fade, sidechaincompress pela voz (threshold 0,02, ratio 5), amix e loudnorm de uma passada I=-14, TP=-1,5, LRA=9 | [FATO] videos/add_music.sh |
| Saída | case-tzur-v2-9x16.mp4 | 1080x1920, 30 fps, 1627 quadros, 54,3 s, 13,99 Mb/s (95 MB). Versão leve 2,55 Mb/s (17 MB) | [FATO] ffprobe nos dois arquivos |

### 1.2 Série 2 (videos/serie2/modelo.html)

| Etapa | Arquivo | O que faz | Fonte |
|---|---|---|---|
| Voz e tempos | voz.py | gera voz sintética Kokoro, confere com faster-whisper e escreve timeline.json com "segs" (início, fim, texto, rótulo, visual, destaques, tempos de palavra) | [FATO] voz.py |
| Cenas | modelo.html | render(t) puro sobre fundo creme #F6F1E8; tipos de cena prontos: count (contador animado), cards (lista com ícone), cross (palavra riscada que vira outra), big (Cinzel + Playfair), duo (dois cartões), funnel, vs, cta (balão com a palavra digitando); burst de partículas na troca de cena | [FATO] modelo.html, função scene() |
| Captura | capture.js | screenshot JPEG qualidade 92 por quadro, enviado por pipe direto para o ffmpeg (sem PNG em disco), muxado com voz.wav | [FATO] capture.js |
| Lote | render_todos.sh | renderiza os 5 reels e aplica add_music.sh com uma trilha diferente para cada | [FATO] render_todos.sh |

Diferença central: a Série 2 não tem pessoa em cena (é a "animação sem rosto" que o CLAUDE.md registra como fracasso medido). Serve como biblioteca de cenas e como técnica de captura rápida, não como formato.

---

## 2. Tempo de render medido

| Passo medido | Quadros | Tempo | Custo por quadro | Fonte |
|---|---|---|---|---|
| Overlay v1 (ov, 1 camada PNG) | 1626 | 366,7 s | 0,226 s | [FATO] stat de ov/00000.png e ov/01625.png, 14/10 |
| Camada de trás v2 (ov2_back, PNG) | 1626 | 161,6 s | 0,099 s | [FATO] stat de ov2_back, 18/10 |
| Camada da frente v2 sem bloco final pesado (ov2_front.old) | 1626 | 212,4 s | 0,131 s | [FATO] stat de ov2_front.old |
| Bloco cinematográfico com granulação (ov2_front, quadros 1333 a 1625) | 292 | 244,6 s | 0,838 s, PNG de 2,2 MB cada | [FATO] stat e tamanho dos PNGs |
| Segmentação Tzur (seg.py, 360x640) | 1627 | no máximo 850 s | no máximo 0,52 s | [FATO] teto: seg.py salvo 02:44:27, mask.mp4 fechado 02:58:58 |
| Segmentação do dentista (seg.py em dent/base.mp4, rodada de hoje) | 1093 | 589,4 s | 0,539 s | [FATO] scratchpad/dent/seg.log ("1093 quadros 589.4 s"), 16:26 a 16:36 |
| Composição Tzur (comp.py + x264) | 1627 | 598 s entre o último PNG da frente (03:34:10) e o MP4 (03:44:08); o início real não foi registrado e pode ter sido antes, porque comp.py pula em silêncio o PNG que ainda não existe | sem dado exato | [FATO] stat; comp.py, blocos try/except FileNotFoundError |
| Laço numpy de comp.py (sem ler vídeo e sem x264), PNGs reais do Tzur, CPU livre | 5 quadros, 2 rodadas | | 0,40 a 0,51 s (primeira leitura fria 1,82 s) | [FATO] scratchpad/f4bench/bench.py, 16:38 |
| x264 crf 18 preset medium em 1080x1920 | 300 | 21,6 s | 0,072 s | [FATO] ffmpeg em dent/base.mp4, 16:39 |
| Overlay de PNG pelo próprio ffmpeg + x264 | 300 | 21,4 s | 0,071 s | [FATO] ffmpeg overlay de ov2_front sobre base.mov, 16:39 |
| Série 2, captura JPEG por pipe + x264 | 750 a 834 por reel | 53 a 67 s por reel | 0,077 a 0,080 s | [FATO] stat de _r1-caixa.html e sem-trilha.mp4 de r1 a r5, 17/10 |
| Trilha (add_music.sh) | 1 vídeo | cerca de 4 s | | [FATO] diferença entre sem-trilha.mp4 e r*-9x16.mp4 |
| Disco | | ov2_front 800 MB, ov2_back 114 MB, ov 334 MB | | [FATO] du -sh |

Leitura: a composição em numpy custa cerca de 0,52 s por quadro (0,45 do laço + 0,072 do x264) [ESTIMATIVA pela soma das duas medições]. É a etapa mais cara depois da segmentação. Fazer a mesma conta com filtros do ffmpeg (alphaextract, negate, blend multiply, alphamerge, overlay) ficaria perto de 0,07 a 0,10 s por quadro [HIPÓTESE: só o overlay simples foi medido, a cadeia com máscara não]. Um teste do laço feito com a segmentação rodando ao mesmo tempo deu 0,84 a 2,55 s por quadro: rodar duas etapas pesadas juntas nesta máquina triplica o custo.

### 2.1 Custo estimado por modelo (bruto do dentista: dent/base.mp4, 1080x1920, 30 fps, 1093 quadros, 36,43 s [FATO] ffprobe)

Premissa comum: saída em 30 fps (os dois pipelines e a fonte efetiva são 30 fps), uma passada limpa, sem contar prints de conferência nem refações.

| Modelo | Conta | Total estimado |
|---|---|---|
| A · o que já fazemos (Tzur v2: letreiro atrás + b-roll + reacts + bloco final) | máscara já pronta (589 s, rodada hoje) + trás 1093 x 0,099 = 108 s + frente 913 x 0,131 = 120 s + bloco final de 6 s com granulação 180 x 0,838 = 151 s + composição 1093 x 0,52 = 568 s + trilha 4 s = 951 s | [ESTIMATIVA] cerca de 16 min após a máscara; cerca de 14 min sem granulação por quadro no bloco final; cerca de 8 min se a composição for para filtros do ffmpeg |
| B · tela dividida com reacts vetoriais e motion blur só nas transições | máscara reaproveitada de A (0 s) + painel opaco em JPEG por pipe 1093 x 0,08 = 87 s + legenda PNG 1093 x 0,131 = 143 s + subquadros em 10 janelas de 0,5 s (150 quadros x 4 subquadros extras x 0,131 = 79 s) + composição 1093 x 0,52 = 568 s + áudio 10 s = 887 s | [ESTIMATIVA] cerca de 15 min |
| C · tipografia cinética com máscara de tipo e motion blur em todo o vídeo | máscara reaproveitada (0 s) + overlay com 3 subquadros por quadro: 1093 x 3 x 0,131 a 0,226 = 430 a 741 s + composição 568 s + áudio 10 s = 1008 a 1319 s | [ESTIMATIVA] 17 a 22 min, sem contar a mistura dos subquadros em numpy (custo sem dado). Custo por quadro de glifo SVG deformado: sem dado, a faixa usa os dois overlays medidos |
| Qualquer modelo em 60 fps (como pede o twoclipping-000267) | dobra quadros de overlay e de composição; a fonte só tem cerca de 30 quadros reais por segundo | [ESTIMATIVA] cerca de 2x o tempo acima; não recomendado |

Os três juntos: [ESTIMATIVA] 951 + 887 + 1008 a 1319 s = cerca de 47 a 53 min de máquina numa passada, em série, com a máscara já pronta. Em paralelo não ajuda: 4 vCPU, a segmentação sozinha usou cerca de 350% de CPU [FATO, ps às 16:31] e o teste concorrente ficou 2 a 5 vezes mais lento [FATO, bench.py]. Cada rodada de prints de conferência e cada refação somam por cima.

---

## 3. O que é reaproveitável para o reel do dentista

| Peça | Reaproveita? | Ajuste necessário | Fonte |
|---|---|---|---|
| seg.py | sim, já rodou em dent/base.mp4 (dent/mask.mp4, 1093 quadros, 360x640) | trocar "-r 30" fixo por parâmetro; manter só o maior componente conexo (scipy.ndimage.label) para tirar quem passa ao fundo | [FATO] seg.log e ffprobe de dent/mask.mp4; seg.py linha 7 |
| cap2.js | sim | trocar a duração fixa 54.2 por E.total; trocar Math.random do confete por gerador com semente (senão retomar com FROM muda o confete no meio) | [FATO] cap2.js e ov2.html, array P |
| comp.py | sim, é o coração do Modelo A e serve de base para B e C | parametrizar N, o trecho P&B (4,28 s), o corte da máscara em y=470 (ver risco R5) e o atraso dos aplausos; trocar a mistura de áudio pela cadeia da seção 4.4 | [FATO] comp.py |
| ov2.html, camada de trás (LT) | sim | novos letreiros ("474 MIL", "HORA DE CADEIRA", "ENSINAR", "2º PRODUTO") numa faixa de y=120 a 450 px: a parte de cima fica sempre livre (o topo da pessoa nunca sobe acima de y=252) e a de baixo passa atrás da cabeça | [FATO] medição da máscara do dentista, R5; legibilidade da parte escondida: [HIPÓTESE] |
| ov2.html, legenda palavra a palavra e lista HL | sim | alimentar com words-raw.json do dentista | [FATO] words-raw.json existe na pasta god |
| ov2.html, b-roll nos cortes | parcial | o bruto do dentista é uma tomada só, sem cortes de câmera; os "cortes" viram marcações de frase escolhidas na lista de edição | [FATO] contexto.md |
| ov2.html, bloco final | parcial | remover "1.287 comentários" e os @ inventados (@dra.julia, @dr.pedro etc.): é prova social fabricada e fere a regra de não inventar dado; trocar ♥ e ✓ (glifos de texto) por SVG | [FATO] ov2.html, ramo t<50.6 |
| modelo.html (Série 2) | sim, como biblioteca de cenas para o painel da tela dividida | count para 474 mil, cross para "hora de cadeira" virando "segundo produto", cta com "DENTISTA" digitando; trocar ✓ e ✕ de texto por SVG | [FATO] modelo.html |
| capture.js (JPEG por pipe) | sim, para painéis opacos | 0,08 s por quadro contra 0,10 a 0,23 s do PNG em disco | [FATO] seção 2 |
| add_music.sh | parcial | serve para a trilha, mas usa loudnorm de uma passada e TP -1,5; ver 4.4 | [FATO] add_music.sh |
| SFX | sim | biblioteca sintetizada sem licença de terceiros em videos/nichos/dentista/sfx (11 arquivos, 48 kHz mono) | [FATO] sfx/sfx.py |
| Áudio da voz | sim | voz_master.wav (-14,2 LUFS, TP -0,5 dBTP) precisa de limitador antes da mixagem final | [FATO] 00-enquadramento.md seção 0 |
| tr.trf (vidstab) | sim | arquivo de transformações já gerado em dent/ às 16:22 (7,9 MB); serve para fazer o letreiro acompanhar a parede (R7) | [FATO] ls dent/; uso: [HIPÓTESE] |

---

## 4. Propostas técnicas

### 4.1 Tela dividida (split screen)

Geometria [FATO de medida, contas próprias]: base.mp4 já é 1080x1920 ampliado 1,875x a partir de 576x1024. Uma janela de 1080x1120 recortada do base, sem nova ampliação, mostra cabeça e ombros (nos frames-amostra a cabeça ocupa cerca de 45% da largura e o tronco vai até a borda de baixo).

Layout proposto [HIPÓTESE]:
1. 0 a 3 s: tela cheia, rosto do Bruno, letreiro atrás em "474 mil" (regra do CLAUDE.md: Bruno em cena nos 3 primeiros segundos).
2. Divisão entra em uma frase escolhida da lista de edição: painel gráfico de 1080x800 desce no topo e o Bruno passa para a janela de baixo, 1080x1120. A transição é um deslocamento de 0,35 s com curva criticamente amortecida, x(t) = 1 - (1 + wt) e^(-wt), sem quique (o twoclipping-000267 bane "bouncy easing").
3. Volta para tela cheia nos momentos de fala mais forte e no CTA final, para o rosto ficar na maior parte do vídeo.

Como montar:
- Painel: Playwright em 1080x800 opaco, JPEG por pipe (técnica do capture.js), cenas do modelo.html.
- Recorte do Bruno: em comp.py, o y do recorte por quadro sai do centro de massa da máscara (mask.mp4), suavizado com média móvel de 9 quadros e preso aos limites do quadro. Assim a cabeça fica enquadrada mesmo com a câmera na mão, sem zoom extra.
- Linha divisória: 4 px dourada (#E8B36A) desenhada no próprio comp.py.
- Legenda: camada PNG da frente, posicionada sobre a linha divisória para não cobrir boca nem gráfico.

### 4.2 Reacts sem emoji

Regra: nenhum caractere de emoji nem glifo de texto como ♥, ✓, ✕ (hoje ov2.html e modelo.html usam esses glifos). Tudo vira SVG desenhado no próprio HTML, sem dependência externa.

- Biblioteca proposta [HIPÓTESE]: dente, cadeira odontológica, relógio (hora de cadeira), quadro de aula (ensinar o colega), diploma, duas caixas de produto, gráfico subindo, balão de comentário, check e X desenhados em traço.
- Animação: traço que se desenha (stroke-dasharray e stroke-dashoffset, já usado nos gráficos do ov2.html) mais escala com a curva amortecida da 4.1. Duração de 0,25 a 0,45 s, entrada 2 quadros antes da palavra.
- Ancoragem: o react nasce perto do ombro do Bruno ou dentro do painel da tela dividida, nunca sobre olhos e boca. A posição do rosto vem da máscara.
- Ícones de pacote pronto (Lucide e similares): sem dado sobre ícone de dente e cadeira odontológica; não consultado e nada instalado. Desenhar à mão evita licença e dependência.

### 4.3 Motion blur por subquadros

Base: o twoclipping-000267 manda renderizar 3 subquadros por quadro em t - 1/240, t e t + 1/240 e misturar com tmix, a 60 fps [FATO] prompts/twoclipping-000267.md linha 35.

Adaptação para 30 fps [PRIOR para os valores de obturador]:
- Obturador de 180° em 30 fps cobre 1/60 s. Subquadros em t - 1/120, t e t + 1/120 (3 amostras) nos movimentos comuns, e 5 amostras nas transições rápidas (whip, entrada do painel).
- Só nas janelas de movimento listadas na lista de edição; quadro parado renderiza 1 vez. Isso mantém o custo da seção 2.1.
- render(t) precisa ser puro. Hoje não é em dois pontos do ov2.html: confete com Math.random na carga e granulação com Math.random a cada chamada. A granulação deve usar semente pelo índice do quadro, senão os subquadros fazem a média do ruído e a granulação some justo no blur.
- Mistura: fazer em numpy, em alfa pré-multiplicado (média de rgb x a e média de a, depois "over"). [FATO] tmix existe neste ffmpeg com frames, weights e scale; [HIPÓTESE] tmix em RGBA tira a média do alfa reto e cria borda escura nos semitransparentes. Se usar tmix, ele é janela deslizante: com 3 subquadros por quadro, pegar só os quadros alinhados com select='eq(mod(n\,3)\,2)', e não framestep=3, que pega janelas desalinhadas.
- O vídeo do Bruno não recebe blur sintético; a câmera do celular já tem o borrão real dela.

### 4.4 SFX alinhado ao pico

Base: "coloque cada efeito de modo que o pico medido, não o início do arquivo, caia no evento; loudnorm a -14 LUFS" [FATO] twoclipping-000267.md linha 36.

Picos medidos nesta rodada (envelope RMS de 5 ms) [FATO, numpy em videos/nichos/dentista/sfx]:

| Efeito | Duração | Pico |
|---|---|---|
| pop | 0,120 s | 2,6 ms |
| tick | 0,040 s | 2,6 ms |
| shutter | 0,180 s | 2,5 ms |
| impact | 1,200 s | 4,2 ms |
| sub | 0,900 s | 3,7 ms |
| ding_si | 1,800 s | 6,6 ms |
| coin | 0,600 s | 2,5 ms (pico de amostra em 62,5 ms) |
| swipe | 0,250 s | 137,1 ms |
| whoosh | 0,550 s | 268,5 ms |
| typing | 0,600 s | 302,2 ms (cliques espalhados; alinhar o primeiro clique, em 27,6 ms) |
| riser | 1,600 s | 1596,6 ms |

Regra de posição: início do efeito = tempo do evento visual - pico. O evento visual é o quadro em que a animação chega ao ponto máximo (por exemplo, o fim da extrusão do letreiro, 0,55 s depois do início dele no ov2.html), arredondado para o quadro de 33,3 ms, e não o início da palavra. Exemplo: whoosh numa transição que fecha em 20,10 s começa em 19,83 s; riser que culmina em 3,18 s ("mil") começa em 1,58 s.

Cadeia de áudio proposta:
1. Mixar voz, SFX e trilha em numpy por índice de amostra (48 kHz), em vez de uma cadeia de adelay com dezenas de entradas.
2. SFX entre -18 e -24 dB abaixo do pico da voz [PRIOR]; trilha com ducking pela voz (sidechaincompress do add_music.sh).
3. Loudnorm em duas passadas: medir, depois aplicar com measured_I, measured_TP, measured_LRA e linear=true [FATO: as opções existem em ffmpeg -h filter=loudnorm], alvo -14 LUFS e TP -1,0 dBTP (meta do 00-enquadramento, D1). Conferir com ebur128 no arquivo final.

---

## 5. Riscos técnicos com fonte 576x1024

| # | Risco | Fato medido | Efeito | Mitigação |
|---|---|---|---|---|
| R1 | Ampliação | fonte 576x1024 a 1,31 Mb/s; base.mp4 já ampliado 1,875x; método de ampliação usado no base.mp4: sem dado [FATO] ffprobe | zoom de 1,25x no rosto vira 2,34x da fonte; blocos de compressão e pele lavada aparecem | punch-in no máximo 1,25x e só em cortes curtos; preferir mudança de layout (tela dividida) a zoom; [HIPÓTESE] unsharp leve depois da ampliação |
| R2 | Taxa de quadro variável | r_frame_rate 31,58 (600/19), média 29,99 fps; 58 intervalos de 63 ms, um a cada 0,63 s; base.mp4 tem os mesmos 1093 quadros em 30 fps fixo; desvio máximo 31,7 ms [FATO] ffprobe nos pacotes de raw.mp4 | até 1 quadro de diferença entre boca e legenda | usar sempre base.mp4 e os tempos de words-raw.json; conferir sincronia em 35,9 s ("respondo") |
| R3 | Máscara de baixa resolução | rembg u2net_human_seg redimensiona a entrada para 320x320 [FATO] rembg/sessions/u2net_human_seg.py linha 32; seg.py ainda reduz para 360x640 | em 1080x1920 cada ponto da máscara cobre cerca de 6 px na vertical e 3,4 px na horizontal: halo no cabelo e nos ombros | desfocar e encolher 2 a 4 px a borda; letreiro com cor que não brigue com o cabelo |
| R4 | Atraso da máscara | suavização 0,6 atual + 0,4 anterior [FATO] seg.py linha 13 | em movimento rápido da mão, a máscara fica cerca de 1 quadro atrás e o letreiro "vaza" na borda | reduzir o peso do anterior nos trechos de movimento ou suavizar com média centrada (passado e futuro) |
| R5 | Corte fixo em y=470 | comp.py zera a máscara acima de y=470 [FATO]. Na máscara do dentista (maior componente), o topo da pessoa vai de y=252 a 555 em 1080x1920, mediana 420; em 783 de 1093 quadros (71,6%) a pessoa sobe acima de y=470 [FATO, scratchpad/f4bench/head.py em dent/mask.mp4, 16:37] | onde a cabeça sobe acima de 470 px, o letreiro passa por cima da cabeça em vez de atrás | tirar o corte fixo; usar a máscara inteira com maior componente conexo |
| R6 | Gente passando ao fundo | em 44 de 1093 quadros a máscara tem um segundo componente acima de 200 px (em 360x640), por exemplo em 17,4 s, 19,4 s, 26,5 a 27,5 s e 33,9 s; conferido no quadro de 26,8 s: pessoa sentada na borda esquerda [FATO, head.py e chk268.jpg no scratchpad] | o letreiro é recortado por quem passa | manter só o maior componente conexo da máscara (scipy disponível) |
| R7 | Câmera na mão | selfie de mão com parede se movendo [FATO] contexto.md; tr.trf do vidstabdetect já existe | letreiro parado na tela enquanto a parede mexe: a ilusão de "atrás" fica fraca | mover o letreiro com o inverso da transformação do tr.trf, ou estabilizar (vidstabtransform), que corta borda e come parte do limite de 1,25x |
| R8 | Elementos que ferem regras | ov2.html tem "1.287 comentários" e @ inventados; ♥, ✓ e ✕ como texto; RGB split, tremida e confete [FATO] ov2.html | prova social inventada; glifos parecidos com emoji; itens da lista de banidos do twoclipping-000267 | Modelo A: remover contador e @; trocar glifos por SVG. B e C: sem RGB split, tremida e partículas sem motivo escrito |
| R9 | render(t) não determinístico | Math.random no confete (na carga) e na granulação (a cada quadro) [FATO] ov2.html | retomar com FROM muda o confete; subquadros apagam a granulação | gerador com semente pelo índice do quadro |
| R10 | Constantes fixas do Tzur | 54.2 em cap2.js e comp.py, 4,28 s de P&B, aplausos em 4280 ms, legenda em y 1330 e 1590, bloco final em 44,45 s [FATO] | render corta ou passa do fim; efeitos em tempo errado | ler total e marcas da lista de edição do dentista (36,43 s) |
| R11 | Disco e peso | PNG da frente com granulação: 2,2 MB por quadro; Tzur v2 final 13,99 Mb/s [FATO] | cerca de 0,5 a 2,4 GB de PNG por modelo [ESTIMATIVA: 1093 quadros x 0,5 a 2,2 MB]; arquivo final de cerca de 64 MB [ESTIMATIVA: 36,43 s x 13,99 Mb/s / 8] | apagar PNG depois da composição; gerar também versão leve |
| R12 | True peak da voz | voz_master.wav com TP -0,5 dBTP [FATO] 00-enquadramento.md | somar SFX e trilha estoura o limite de -1,0 | limitador e loudnorm em duas passadas no final (4.4) |
| R13 | Fala truncada | 24,94 a 29,04 s: "deixa disputar, paciente passa a forna que a gente disputa" [FATO] words-raw.json | legenda fiel ao áudio expõe o erro; legenda "corrigida" desalinha da boca | decisão de conteúdo fora da F4; tecnicamente, a legenda pode seguir o roteiro com tempos do alinhamento |
| R14 | Composição pula quadro em silêncio | comp.py usa try/except FileNotFoundError: pass nas duas camadas [FATO] | se a composição começar antes do fim do overlay, sai vídeo sem letreiro naqueles quadros e sem erro | conferir a contagem de PNG (1093 por camada) antes de compor; trocar o pass por erro |

---

## 6. Lacunas

- Script que montou base.mov do Tzur e base.mp4 do dentista: não versionado; método de ampliação de 576x1024 para 1080x1920: sem dado.
- Custo por quadro de tipografia com glifos SVG deformados (Modelo C): sem dado; a estimativa usa a faixa dos overlays medidos.
- Tempo real da composição do Tzur: o início não foi registrado; a estimativa usa o laço medido hoje (5 quadros) mais o x264 medido (300 quadros).
- Cadeia de composição só com filtros do ffmpeg (com máscara): não testada.
- Efeito de tmix em RGBA com alfa: hipótese, não testada.
- Desempenho no Instagram de qualquer um dos três formatos: sem dado (nenhuma métrica do case Tzur v2 registrada em conteudo/sistema-instagram/semanas/, conforme 00-enquadramento.md).
