# F1 · Repositório awesome-opus5-5-videos · 8 prompts para o reel do dentista

Cliente: O Estrategista (@o_estrategista.com.br). Frente F1 da pesquisa do conselho Agência Reunida, 21/10/2026.
Etiquetas: [FATO] com fonte · [ESTIMATIVA] com conta · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, nunca fecha objeção sozinho.
Escopo: somente leitura. Nada foi clonado nem instalado nesta frente; a cópia local já existia em /home/user/yihui-dev/awesome-opus5-5-videos.

## 1. Verificação das fontes

| Fonte | Como conferi | Resultado |
|---|---|---|
| Cópia local do repositório | `git log -1` e `git remote -v` | [FATO] commit 92aee2f5, 13/10/2026, remoto github.com/yihui-dev/awesome-opus5-5-videos, mensagem "Remove 150 entries not made from a plain Opus 5.5 prompt (703 total)" |
| data/videos.json remoto | GET em raw.githubusercontent.com/.../main/data/videos.json e sha256 | [FATO] HTTP 200, 813.423 bytes, sha256 1c307487... idêntico ao arquivo local |
| prompts/twoclipping-041659.md remoto | GET raw e sha256 | [FATO] idêntico ao local (b4499f03...) |
| URL que o Bruno mandou (github.com/.../tree/main/prompts) | GET | ERRO: HTTP 403 pelo proxy da sessão. Não é dado vazio; o conteúdo foi conferido pelo raw.githubusercontent.com acima |
| API do GitHub (`gh api repos/.../commits/main`) | consulta somente leitura | ERRO: HTTP 403 "GitHub access to this repository is not enabled for this session". Commit remoto atual: sem dado |
| Páginas Skillry dos 6 selecionados que têm remake | GET | [FATO] HTTP 200 em sab8a-475686, stokebuilder-356793, techhalla-498547, gdgtify-929495, twoclipping-000267, alex-prompter-997524; títulos conferidos em 3 delas ("Opus 5.5 video prompt by @sab8a...", "@stokebuilder", "@techhalla") |
| Posts no X de twoclipping-041659 e twoclipping-551116 | GET | HTTP 200, mas a página volta sem título legível (casca JavaScript). Existência do post: não confirmada por esta consulta. O texto do prompt foi conferido no repositório |

Ressalva [FATO, data/videos.json]: o arquivo traz o texto do prompt, não traz visualizações, curtidas nem retenção de nenhum vídeo. Nenhum prompt desta lista tem desempenho medido; "funciona" aqui quer dizer "técnica aplicável", nunca "converte".

## 2. Números do acervo

Todos [FATO], consulta Python em data/videos.json (703 entradas) em 21/10/2026, salvo indicação.

| Recorte | Quantidade |
|---|---|
| Total de prompts | 703 (também 703 arquivos em prompts/, `ls | wc -l`) |
| Por categoria | motion 369, 3d 117, explainer 116, interactive 101 |
| Com remake no Skillry | 418 |
| Marcados como prompt parcial (`prompt_partial`) | 207 |
| Citam talking head ou "to camera" | 3 (sab8a-475686, stokebuilder-356793, twoclipping-551116) |
| Citam legenda (caption ou subtitle) | 13 |
| Citam formato 9:16 ou 1080x1920 | 13 |
| Citam tipografia cinética | 18 |
| Usam seek(t) determinístico | 30 |
| Citam Playwright | 32 |
| Citam motion blur por subquadros | 22 |
| Citam -14 LUFS | 13 |
| Citam whisper para tempo de palavra | 3 |
| Citam split screen | 0 |
| Citam emoji | 0 |
| Citam rembg ou segmentação de pessoa real | 0 |

Leitura: o acervo é forte em motion de produto e fraco em pessoa falando. Só 3 de 703 prompts tratam de talking head, e nenhum descreve letreiro atrás de uma pessoa filmada nem split screen. Essas duas peças do pedido do Bruno vêm do nosso pipeline (caso Tzur), não do repositório.

## 3. Critério de seleção

Pontuei pela utilidade direta para um reel vertical de 36,4 s com o Bruno falando [FATO, contexto.md]: (a) trata pessoa real em vídeo ou voz com transcrição, (b) técnica de texto cinético ou legenda, (c) profundidade ou camada atrás de figura, (d) divisão de tela, inserção ou react, (e) estrutura narrativa de conversão, (f) engenharia compatível com HTML + Playwright + ffmpeg. Descartei prompts de produto ou 3D sem pessoa, mesmo os mais longos.

## 4. Os 8 prompts

### 4.1 twoclipping-041659 · voz transcrita, cabeça com órbita passando atrás
Ficha [FATO, videos.json]: interactive, sem tech_tags, sem remake, prompt completo (5.616 caracteres), adicionado 12/10/2026. Arquivo: prompts/twoclipping-041659.md.
- Técnica central: cada cena pendurada no tempo das palavras medido com faster-whisper; legenda digitada junto com a voz atrás de um cursor de bloco; silhueta de cabeça como máscara; "a thin white orbit draws itself around the head, its far half passing behind it"; transição em que a cabeça escalada vira janela para a cena seguinte ("fall through the head"); cada passagem começa no último quadro exato da cena anterior.
- O que copiar: (1) a órbita com metade de trás escondida pela cabeça, que é o efeito "4D atrás" pedido pelo Bruno em versão elegante; (2) a palavra-chave sublinhada em cor no instante em que é falada; (3) a regra de passagem sem corte seco; (4) o gotcha da máscara: estender a máscara além da borda do quadro para membro cortado não virar linha reta.
- O que evitar: a estética de mapa de calor na silhueta e os objetos em pixel art (não conversam com o nicho nem com a identidade preto e ouro); o formato 4:3.
- Adaptação ao nosso pipeline: já temos words-raw.json com tempo por palavra [FATO], então a etapa de whisper está feita. A órbita sai em duas metades: a metade de trás vai para a camada `back` do ov2.html (composta sob a máscara rembg em comp.py) e a metade da frente vai para a camada `front`. É exatamente a divisão back/front que cap2.js já renderiza [FATO, cap2.js]. Para o "fall through", usar a máscara de seg.py escalada como matte em numpy. Ponto de atenção [FATO, comp.py]: a linha `mk[:470]=0` zera a máscara nos 470 px de cima; no Tzur isso funcionava, no dentista a cabeça ocupa o centro e o topo [FATO, contexto.md], então essa linha precisa ser revista ou o letreiro vai passar por cima do cabelo.
- Uso sugerido [HIPÓTESE]: palavra "colegas" (3,80 a 4,40 s) ou "mercado" (19,12 a 19,50 s) com órbita atrás da cabeça.

### 4.2 twoclipping-551116 · clipes falando para a câmera dentro do design, stickers recortados
Ficha [FATO]: motion, sem remake, prompt completo (4.770 caracteres), 12/10/2026. Um dos 3 prompts com "talking-to-camera".
- Técnica central: os clipes reais tocam dentro do layout; stickers com borda branca recortada (dilatação do alfa) e sombra suave, entram com ease e mantêm um balanço lento; letras sobem através de uma linha de máscara uma a uma; câmera nunca para (push lento de 1,03 a 1,07 por cena); trocas em carrossel de 0,55 s; mudança de cor em 0,35 s; clipe em preto e branco que vira colorido no "CAST"; contador 1/4 a 4/4; SFX posicionado pelo pico medido; -14 LUFS; 8 subquadros de motion blur.
- O que copiar: os stickers recortados como formato dos "reacts" (ícones vetoriais nossos, nunca emoji, por regra do CLAUDE.md); a regra "nada aparece com pop seco"; o P&B que vira cor num momento de virada (já fazemos no Tzur, aqui ganha um gatilho de fala: "Ensinar o seu colega", 20,64 a 22,70 s); a lista de banidos (flash branco, crossfade entre cenas, rotação travada no beat).
- O que evitar: o quadrado 1440x1440; as 4 pessoas e os 12 retratos (só temos o Bruno); números de "views contando" e "MATCH %", que seriam métricas inventadas na tela.
- Adaptação: stickers como SVG desenhados no ov2.html, borda recortada gerada uma vez em PIL (dilatar o alfa) e reaproveitada; pico do SFX medido em numpy antes de posicionar; o balanço do sticker é função de t, então sobrevive ao render quadro a quadro do Playwright.
- Custo [ESTIMATIVA]: 8 subquadros multiplicam por 8 as capturas da camada animada. Conta: 36,4 s x 30 fps = 1.092 quadros por camada; 2 camadas = 2.184 capturas hoje; com 8 subquadros, 17.472. Aplicar subquadros só nos trechos de movimento rápido.

### 4.3 stokebuilder-356793 · animação em tela cheia sobre talking head com o rosto em PiP
Ficha [FATO]: explainer, canvas e svg, remake no Skillry (HTTP 200), prompt PARCIAL (`prompt_partial: true`, 2.242 caracteres). Um dos 3 prompts com talking head.
- Técnica central: encontrar cada trecho de fala que comporta uma animação; quando o gráfico ocupa a tela, quem fala fica em picture-in-picture no canto inferior direito; sem punch-in nas câmeras; texto fiel ao que foi dito ("Never invent facts, numbers or quotes"); sincronizar as batidas da animação com as palavras; cada gráfico dentro de um trecho de áudio sem corte; deixar alguns segundos de rosto entre gráficos; um juiz separado avalia cada animação uma vez.
- O que copiar: é a base do "dividindo dela com reacts e animações". Regra de rosto: o Bruno sempre visível, em PiP quando o gráfico entra, e rosto cheio entre gráficos (casa com o aprendizado medido de 2,4x a 5,8x a mediana com o Bruno em cena [FATO, CLAUDE.md]). Copiar também a regra de texto fiel: a fala real tem "em Brasil" e o trecho truncado de 24,94 a 29,04 s [FATO, 00-enquadramento.md], então a legenda não pode "consertar" a frase como se fosse fala.
- O que evitar: a meta de 35 a 50 momentos (é para episódio longo; em 36 s isso vira poluição); a proibição total de zoom (no nosso caso um punch-in até 1,08x cabe no limite de 1,25x do contexto.md).
- Adaptação: variante vertical do PiP. Proposta [HIPÓTESE]: em vez do canto, divisão horizontal (gráfico em cima, Bruno embaixo em 1080x960 com recorte rembg e fundo trocado), porque o rosto num PiP pequeno a partir de 576x1024 perde nitidez. Cada bloco de gráfico só dentro de uma frase inteira de words-raw.json. Nos 3 primeiros segundos, nenhum gráfico em tela cheia (regra do CLAUDE.md).

### 4.4 sab8a-475686 · talking head bruto vira edição rápida com legenda, grafismo e música
Ficha [FATO]: motion, canvas e ai-image, remake no Skillry (HTTP 200), prompt completo mas de uma linha (86 caracteres): "Cut a raw talking-head clip into a punchy, fun edit with subtitles, graphics and music".
- Técnica central: o próprio enunciado. É o único prompt do acervo cujo insumo é igual ao nosso (um talking head bruto).
- O que copiar: o escopo mínimo como contrato do Modelo A: corte de respiros, legenda, grafismo, música. Serve de régua: se o vídeo não cumpre estas 4 coisas, não está pronto.
- O que evitar: o prompt não dá direção, paleta, ritmo nem regra de texto; usar só ele gera resultado genérico. A tag ai-image indica imagem gerada no remake [FATO, videos.json]; para nós, nada de imagem gerada no lugar de prova.
- Adaptação: cortar só pausas acima de um limite medido em words-raw.json, nunca palavra. Pausas medidas acima de 0,05 s [FATO, words-raw.json]: 8, somando 2,98 s (0,32 s após "Brasil,"; 0,52 após "conclusão."; 0,60 após "mercado."; 0,48 após "colega?"; 0,22 após "lançamento,"; 0,18 após "disputar,"; 0,24 após "disputa."; 0,42 após "produto."). Cortar todas levaria o vídeo de 36,4 s para cerca de 33,4 s [ESTIMATIVA: 36,44 menos 2,98, sem contar respiros de 0,30 s que o Tzur preserva nos cortes]. Recomendação: manter a de 0,60 s (ver 4.6). Música em numpy (som.py da serie2) por baixo da voz_master.wav.

### 4.5 techhalla-498547 · tipografia cinética por glifo, máscara a partir da palavra que sai
Ficha [FATO]: motion, canvas, remake no Skillry (HTTP 200), prompt completo (3.878 caracteres).
- Técnica central: mola por glifo (y, opacidade, desfoque) com escalonamento de 125 ms; mola em forma fechada para ser determinística; revelação da palavra nova com máscara derivada do contorno da palavra que sai; câmera só com punch-in de 1,0 a 1,08 e pan seco no tempo; 4 subquadros de motion blur; pré-passe de 8 stills antes do render completo; mensagem travada em ordem fixa.
- O que copiar: a mola por glifo para o letreiro atrás do Bruno (cada letra sobe de trás da cabeça); o punch-in de 1,0 a 1,08 (abaixo do teto de 1,25x); a mensagem travada em ordem (usar as palavras exatas da fala); o pré-passe de stills.
- O que evitar: o desalinhamento de cor magenta e verde (é um RGB split, e twoclipping-000267 bane RGB split); a paleta magenta e verde ácido (nossa é preto e ouro, #141210 e #E8B36A [FATO, contexto.md]); o "STOP SCROLLING" literal e a energia de pôster de rua, que destoam do tom de consultor.
- Adaptação: a mola fechada vira uma função `spring(t)` no ov2.html; o escalonamento por glifo usa os spans `.L span` que o ov2.html já tem [FATO, ov2.html]. O punch-in é aplicado no vídeo base em ffmpeg (scale e crop por quadro) ou em numpy no comp.py, sincronizado com a camada de máscara para o letreiro não descolar da cabeça.

### 4.6 gdgtify-929495 · palavras viram arquitetura, com um momento de quietude
Ficha [FATO]: motion, canvas, remake no Skillry (HTTP 200), prompt completo (4.373 caracteres).
- Técnica central: cada palavra ganha um papel estrutural (viga, carga, apoio, abertura, piso); a frase final se apoia no que as anteriores construíram; cue sheet por frase e pausa, não por batida musical ("Do not force the speech onto a dance beat"); pelo menos 400 ms de quietude absoluta; seek(t) determinístico sem estado acumulado; ciclo em que o último quadro volta ao primeiro.
- O que copiar: o relógio pela fala, não pela música (nosso vídeo é fala do começo ao fim); a quietude de 400 ms antes da virada; a ideia de que o letreiro final se apoia em peças anteriores, aplicada a "Sua técnica vira um segundo produto" (29,28 a 32,00 s), em que "técnica" e "produto" podem ser as peças que viraram estrutura antes.
- O que evitar: palco 100% tipográfico sem pessoa (a animação sem rosto ficou de 0,15x a 0,8x a mediana [FATO, CLAUDE.md]); o formato 1080x1080.
- Adaptação: a arquitetura de palavras fica na camada `back`, atrás do Bruno, ocupando a parede livre acima e dos lados da cabeça [FATO, contexto.md]. A quietude de 400 ms cabe em pausas reais da fala [FATO, words-raw.json, intervalo entre o fim de uma palavra e o início da seguinte]: 0,60 s entre "mercado." (fim 19,50 s) e "Qual" (20,10 s), que antecede a virada "Ensinar o seu colega"; 0,52 s entre "conclusão." (13,32 s) e "Se" (13,84 s); 0,48 s entre "colega?" (22,22 s) e "Eu" (22,70 s); 0,42 s entre "produto." (31,58 s) e "Dentista" (32,00 s), antes da chamada. A de 19,50 a 20,10 s é a candidata natural para a quietude antes da virada. Atenção: a regra do 4.4 manda cortar respiros; esta pausa deve ser mantida.

### 4.7 twoclipping-000267 · minimalismo caro, máscara de tipo, match cut e áudio pelo pico
Ficha [FATO]: 3d, svg e css, remake no Skillry (HTTP 200), prompt completo (2.515 caracteres).
- Técnica central: uma ideia por plano, muito espaço vazio, uma cor de destaque, uma sans; revelações por máscara de tipo e match cut; motion blur real com 3 subquadros (t menos, t, t mais 1/240 s) combinados com `tmix` no ffmpeg; SFX posicionado pelo pico medido, não pelo início do arquivo; -14 LUFS; sondar 20 quadros antes do render; lista de banidos: shockwave, partículas, RGB split, camera shake, lens flare, neon, piso de grade, fundo piscando, easing elástico.
- O que copiar: a lista de banidos inteira como guarda-corpo do "estilo After Effects profissional" (o pedido do Bruno puxa para efeito; esta lista evita o efeito barato); o `tmix` de 3 subquadros, mais barato que os 8 do 4.2; o gotcha de nunca pôr opacidade ou filtro num elemento preserve-3d (achata e mostra as duas faces), relevante para o letreiro 3D.
- O que evitar: a grade de 120 BPM com corte em todo tempo forte (conflita com o relógio de fala do 4.6); o 1920x1080.
- Adaptação: render das camadas com 3 subquadros e `tmix=frames=3` antes do comp.py. Custo [ESTIMATIVA]: 2.184 capturas viram 6.552. SFX: medir o pico de cada whoosh em numpy e alinhar o pico ao quadro do evento. A voz já está em -14,2 LUFS [FATO, 00-enquadramento.md]; após somar trilha e SFX, rodar loudnorm de novo na mistura.

### 4.8 alex-prompter-997524 · explainer de 5 cenas para negócio
Ficha [FATO]: explainer, svg e gsap, remake no Skillry (HTTP 200), prompt completo (348 caracteres).
- Técnica central: 5 cenas em 30 s: problema do cliente, o que eu faço, como funciona em 3 passos, uma prova, o nome no fim.
- O que copiar: o esqueleto de conversão. Mapeado na fala real [FATO, words-raw.json]: problema 0,00 a 13,84 s ("474 mil colegas... hora de cadeira... mesmo diagnóstico"); o que eu faço 22,70 a 24,46 s ("Eu desenho seu lançamento"); como funciona 13,84 a 22,70 s ("técnica que os dentistas querem aprender, existe um mercado, ensinar o seu colega"); resultado de posição 24,46 a 32,00 s; chamada 32,00 a 35,92 s ("comenta a sua profissão aqui").
- O que evitar: a cena de "prova" sem fonte. Nesta tomada o Bruno não cita o case Tzur [FATO, contexto.md], então a única prova disponível é o número do CFO (474 mil, leituras de 474.640 e 474.659 em 21/10/2026 [FATO, 00-enquadramento.md, via 06-plano-final.md]). Nada de "3 passos" inventados que a fala não diz; a fala não tem 3 passos explícitos.
- Adaptação: as 5 cenas viram 5 estados do letreiro de trás e dos cartões, sem tirar o Bruno da tela, o que diferencia do explainer puro do prompt. Texto na tela só com palavras ditas ou com o número com fonte.

## 5. Suplentes (lidos, fora dos 8)

- everestchris6-399895 [FATO: 3d, sem remake, 7.882 caracteres]: "facts file" como única fonte de número na tela; régua medida: no máximo cerca de 1 s de tela congelada por 30 s, nenhum trecho parado acima de 0,5 s, contraste mínimo 4,5:1, entender sem som; crítico separado que nunca vê o raciocínio do construtor. Bom como checklist de QA para os 3 modelos.
- notdwd-998633 [FATO: motion, sem remake, 4.205 caracteres]: legenda de no máximo 7 palavras, uma camada de texto por vez, cinza para branco em 0,2 s no tempo da palavra; voz 10 a 15 dB acima da música, ducking de -18 dB enquanto fala; -14 LUFS. Útil para a mistura.
- l3d1c-632524 [FATO: motion, svg, remake, prompt PARCIAL]: legenda medida na fonte real e encolhida para caber na zona segura 9:16; folha de contato com cerca de 20 stills antes do render; cortes de 30, 15 e 6 s como listas de cenas. Útil para a zona segura do Reels.

## 6. Como os 8 se distribuem nos 3 modelos [HIPÓTESE, para o conselho decidir]

| Modelo | Base | Prompts que alimentam |
|---|---|---|
| A, o que já fazemos (Tzur v2) | ov2.html + seg.py + comp.py | 4.4 sab8a como contrato mínimo, 4.5 techhalla na mola do letreiro, 4.7 twoclipping-000267 na lista de banidos, no tmix e no SFX pelo pico |
| B, proposta 1 | letreiro em profundidade e órbita atrás da cabeça, relógio pela fala | 4.1 twoclipping-041659, 4.6 gdgtify, 4.8 alex-prompter como esqueleto |
| C, proposta 2 | tela dividida com reacts e gráficos, Bruno sempre visível | 4.3 stokebuilder (PiP adaptado para divisão horizontal), 4.2 twoclipping-551116 (stickers recortados como reacts) |

[PRIOR] B tende a parecer mais "After Effects" e C tende a explicar melhor; nenhum dos dois tem medição de desempenho na conta. Desempenho do formato Tzur v2 também é sem dado [FATO, 00-enquadramento.md].

## 7. Lacunas

1. Nenhum prompt do acervo descreve letreiro atrás de pessoa filmada com segmentação, nem split screen, nem emoji ou react (contagens 0, seção 2). Essas técnicas vêm do nosso pipeline, sem referência externa no repositório.
2. Nenhuma métrica de desempenho dos vídeos do acervo (o JSON não tem views nem retenção). Escolha por técnica, não por resultado.
3. github.com e API do GitHub responderam 403; commit remoto atual sem dado. Conteúdo conferido por raw.githubusercontent.com (hash idêntico).
4. Posts do X dos dois prompts sem remake (twoclipping-041659, twoclipping-551116) não confirmados por leitura: a página volta sem conteúdo legível.
5. stokebuilder-356793 e l3d1c-632524 são prompts parciais segundo o próprio JSON; pode faltar instrução que o autor usou.
6. Não vi os vídeos originais nem os remakes, só os textos. Qualidade visual real de cada técnica: sem dado.
7. Os tempos de palavra vêm de alinhamento automático (words-raw.json); no trecho de 24,94 a 29,04 s há palavras com 0,04 s, então as pausas desse trecho podem estar imprecisas. Conferir no ouvido antes de cortar.
8. A linha `mk[:470]=0` do comp.py precisa ser testada no enquadramento do dentista antes do render (seção 4.1).
