# 01 · Livro de fatos · Reel do dentista · Agência Reunida Modo GOD · 21/10/2026

Cliente: O Estrategista (@o_estrategista.com.br). Cadeira: CURADOR DE FATOS. Esta cadeira não opina sobre estratégia.

Etiquetas: [FATO] com a fonte ao lado · [ESTIMATIVA] com a conta ou a premissa · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, evidência nível 4, nunca fecha objeção sozinho.

Níveis de evidência: **1** dado primário do cliente (arquivos do Bruno, contas dele, medições feitas nesses arquivos) · **2** ferramenta oficial ou fonte primária de terceiro (CFO, data/videos.json, código-fonte, Buzzfy sobre reels de terceiros) · **3** fonte pública secundária (blogs de fornecedor, imprensa) · **4** palpite.

Insumos lidos: contexto.md, run/00-enquadramento.md, run/01-pesquisa/F1 a F4, words-raw.json, transcricao-tempos.txt, evidencias-F3/cfo-ativos-por-cro-2026-10-21.csv, conteudo/sistema-instagram/00-SISTEMA.md (linhas 15 a 40), conteudo/modo-god-nichos/run/06-plano-final.md (busca por 106, 29/10 e 18/11), CLAUDE.md.

Reconferido por esta cadeira em 21/10/2026 (não só copiado das frentes): loudness do raw.wav e do voz_master.wav (ffmpeg loudnorm), as 8 pausas do words-raw.json, a linha SOMA do CSV do CFO, a mediana da conta no 00-SISTEMA.md, a meta de 106 e o critério de pulo no 06-plano-final.md, e o ruído nas pausas das 5 versões de áudio (seção 3, DR02, medição nova).

---

## 1. Fatos dados ou verificados

### 1.1 Material bruto e áudio (pesa em D1)

| # | Fato | Fonte | Coleta | Nível |
|---|---|---|---|---|
| F01 | Bruto: selfie vertical 576x1024, 31,6 fps nominais, 36,4 s, uma tomada só, sem cortes de câmera | contexto.md; ffprobe (F4) | 21/10/2026 | 1 |
| F02 | raw.mp4 tem taxa de quadro variável: r_frame_rate 31,58, média 29,99 fps, 58 intervalos de 63 ms, desvio máximo de 31,7 ms contra 30 fps fixo. base.mp4 tem os mesmos 1093 quadros a 30 fps, 1080x1920, 36,43 s | ffprobe, F4 seção 5 R2 e 2.1 | 21/10/2026 | 1 |
| F03 | raw.wav: -32,6 LUFS integrado, true peak -10,1 dBTP, LRA 3,2 LU | ffmpeg loudnorm, reconferido por esta cadeira | 21/10/2026 | 1 |
| F04 | voz_master.wav: -14,2 LUFS integrado, true peak -0,5 dBTP, LRA 1,6 LU, 36,44 s. O true peak está 0,5 dB acima do alvo de -1,0 dBTP da D1 | ffmpeg loudnorm, reconferido por esta cadeira | 21/10/2026 | 1 |
| F05 | Existem 3 reduções de ruído já geradas a partir do raw: rn_std.wav, rn_sh.wav, rn_bd.wav (36,44 s cada), além de spec_before.png e spec_after.png | ls em scratchpad/dent | 21/10/2026 | 1 |
| F06 | words-raw.json: 79 palavras, primeira "Dentistas" em 0,00 s, última "respondo." de 35,36 a 35,92 s; soma do tempo de fala 32,94 s | words-raw.json, conta desta cadeira | 21/10/2026 | 1 |
| F07 | 8 pausas acima de 0,05 s, somando 2,98 s: 0,32 s após "Brasil," (5,16 a 5,48); 0,52 após "conclusão." (13,32 a 13,84); 0,60 após "mercado." (19,50 a 20,10); 0,48 após "colega?" (22,22 a 22,70); 0,22 após "lançamento,"; 0,18 após "disputar,"; 0,24 após "disputa."; 0,42 após "produto." (31,58 a 32,00) | words-raw.json, reconferido | 21/10/2026 | 1 |
| F08 | Trecho 24,94 a 29,04 s transcrito como "deixa disputar, paciente passa a forna que a gente disputa"; o texto do contexto.md é "deixa de disputar paciente e passa a formar quem disputa". "a" tem 0,06 s e "gente" 0,04 s no alinhamento | words-raw.json; contexto.md | 21/10/2026 | 1 |
| F09 | A fala diz "em Brasil" (4,80 a 5,16 s); o roteiro dizia "no Brasil" | words-raw.json | 21/10/2026 | 1 |
| F10 | O Bruno não cita o case Tzur nesta tomada | contexto.md | 21/10/2026 | 1 |
| F11 | O CTA já gravado é "Dentista, comenta a sua profissão aqui que eu te respondo" (32,00 a 35,92 s) | words-raw.json | 21/10/2026 | 1 |

### 1.2 Conta, metas e aprendizados (pesa em D2 e D3)

| # | Fato | Fonte | Coleta | Nível |
|---|---|---|---|---|
| F12 | Mediana de reel da conta: 53 de alcance, 74 views, 6,2 s assistidos, 68% de pulo (17 reels) | 00-SISTEMA.md linha 20 (Buzzfy) | 21/10/2026 | 1 |
| F13 | Reels com o Bruno falando ficaram de 2,4x a 5,8x a mediana; animação com voz sintética de 0,15x a 0,8x, com 77% a 92% de pulo | CLAUDE.md, aprendizado de 21/10/2026 | 21/10/2026 | 1 |
| F14 | Melhor reel: "Ele nunca fez um anúncio", 307 de alcance, 18,6 s assistidos, 53% de pulo | 00-SISTEMA.md | 21/10/2026 | 1 |
| F15 | Seguidores: 1.618. Reels da conta aparecem no Buzzfy com 565 e 194 views (DeDhWnuoTLT, DeIjIM5ovUo) | 00-SISTEMA.md; F2 Q2 | 21/10/2026 | 1 |
| F16 | Meta do reel do dentista: alcance de 106 ou mais, definida como 2 x mediana de 53; publicação prevista qui 29/10/2026, 12h [a hora é HIPÓTESE no próprio plano] | 06-plano-final.md linhas 60, 161 e 179 | 21/10/2026 | 1 |
| F17 | O 06-plano-final.md usa pulo abaixo de **60%** como critério (linha 179, marcado PRIOR lá). As afirmações D2 e D3 usam pulo abaixo de **68%** (mediana). Os dois cortes coexistem nos arquivos | 06-plano-final.md linha 179; 00-enquadramento.md D2 | 21/10/2026 | 1 |
| F18 | Verba zero até 18/11/2026 | 06-plano-final.md linha 236 | 21/10/2026 | 1 |
| F19 | Nenhuma métrica do case Tzur v2 registrada em conteudo/sistema-instagram/semanas/ (único arquivo: 2026-10-21.md, sem menção a Tzur nem dentista) | busca grep desta cadeira; 00-enquadramento.md | 21/10/2026 | 1 |
| F20 | Regra da conta: todo reel tem o Bruno em cena nos 3 primeiros segundos; palavra-chave do mês (TABULEIRO) só em post com alcance de 150 ou mais | CLAUDE.md | 21/10/2026 | 1 |

### 1.3 Pipeline e máquina (pesa em D2 e no custo de D3)

| # | Fato | Fonte | Coleta | Nível |
|---|---|---|---|---|
| F21 | Máquina: 4 vCPU, 15 GB de RAM, sem GPU (onnxruntime só CPU e Azure), 18 GB livres. ffmpeg 6.1.1 com tmix, loudnorm, vidstab, alphamerge, maskedmerge. Sem OpenCV | F4, nproc, free, df, onnxruntime | 21/10/2026 | 1 |
| F22 | Pipeline Tzur v2: seg.py (rembg u2net_human_seg em 360x640, suavização 0,6/0,4, "-r 30" fixo) → ov2.html render(t, layer) → cap2.js (PNG transparente, camadas back e front) → comp.py (máscara (m-70)/110, zerada acima de y=470, P&B até 4,28 s, x264 crf 18) → add_music.sh (ducking, loudnorm de uma passada, TP -1,5) | F4 seção 1.1, leitura dos arquivos | 21/10/2026 | 1 |
| F23 | O script que montou base.mov (Tzur) e base.mp4 (dentista) não está no repositório; método de ampliação de 576x1024 para 1080x1920: sem dado | F4, grep | 21/10/2026 | 1 |
| F24 | Camada de trás do ov2.html: 12 letreiros com extrusão falsa de 14 text-shadow, rotateX 55° para 0°, entrada 0,55 s, saída 0,35 s, y entre 440 e 580 px | ov2.html (F4) | 21/10/2026 | 1 |
| F25 | Tzur v2 final: 1080x1920, 30 fps, 1627 quadros, 54,3 s, 13,99 Mb/s (95 MB); versão leve 2,55 Mb/s | ffprobe (F4) | 21/10/2026 | 1 |
| F26 | Custo por quadro medido: trás 0,099 s; frente 0,131 s; overlay v1 0,226 s; bloco com granulação 0,838 s (PNG de 2,2 MB); Série 2 JPEG por pipe 0,077 a 0,080 s; laço numpy do comp.py 0,40 a 0,51 s; x264 crf 18 0,072 s; overlay ffmpeg + x264 0,071 s (300 quadros) | stat e testes curtos (F4 seção 2) | 21/10/2026 | 1 |
| F27 | Segmentação do dentista: 1093 quadros em 589,4 s (0,539 s por quadro); máscara pronta em scratchpad/dent/mask.mp4 | scratchpad/dent/seg.log | 21/10/2026 | 1 |
| F28 | Teste concorrente (laço com a segmentação rodando junto): 0,84 a 2,55 s por quadro, 2 a 5 vezes mais lento | bench.py (F4) | 21/10/2026 | 1 |
| F29 | Máscara do dentista: topo da pessoa entre y=252 e y=555 (mediana 420). Em 783 de 1093 quadros (71,6%) a pessoa sobe acima de y=470, onde o comp.py zera a máscara | head.py em mask.mp4 (F4 R5) | 21/10/2026 | 1 |
| F30 | Em 44 de 1093 quadros a máscara tem um segundo componente (gente ao fundo), por exemplo em 17,4 s, 19,4 s, 26,5 a 27,5 s e 33,9 s; conferido no quadro de 26,8 s | head.py, chk268.jpg (F4 R6) | 21/10/2026 | 1 |
| F31 | rembg u2net_human_seg redimensiona a entrada para 320x320 | rembg/sessions/u2net_human_seg.py linha 32 | 21/10/2026 | 2 |
| F32 | O ov2.html tem prova social inventada ("1.287 comentários" e @ fictícios), glifos ♥ ✓ ✕ como texto, RGB split, tremida e confete; render(t) usa Math.random no confete e na granulação | ov2.html (F4 R8 e R9) | 21/10/2026 | 1 |
| F33 | comp.py pula PNG faltante em silêncio (try/except FileNotFoundError: pass) | comp.py (F4 R14) | 21/10/2026 | 1 |
| F34 | Constantes fixas do Tzur: 54,2 s em cap2.js e comp.py, P&B até 4,28 s, aplausos em 4280 ms, bloco final em 44,45 s | cap2.js, comp.py, ov2.html (F4 R10) | 21/10/2026 | 1 |
| F35 | Picos dos SFX (envelope RMS 5 ms): whoosh 268,5 ms, riser 1596,6 ms, swipe 137,1 ms, typing 302,2 ms (primeiro clique 27,6 ms); pop, tick, shutter, impact, sub, ding_si e coin entre 2,5 e 6,6 ms. Biblioteca sintetizada própria, 11 arquivos, 48 kHz mono | numpy em videos/nichos/dentista/sfx (F4 4.4) | 21/10/2026 | 1 |
| F36 | tr.trf (vidstabdetect) já existe em scratchpad/dent (7,9 MB) | ls (F4) | 21/10/2026 | 1 |
| F37 | Série 2 (modelo.html): biblioteca de cenas sem rosto (count, cards, cross, big, duo, funnel, vs, cta), preto e ouro #141210 e #E8B36A, Cinzel e Playfair | modelo.html (F4 1.2); contexto.md | 21/10/2026 | 1 |

### 1.4 Repositório awesome-opus5-5-videos (pesa em D3)

| # | Fato | Fonte | Coleta | Nível |
|---|---|---|---|---|
| F38 | 703 prompts: motion 369, 3d 117, explainer 116, interactive 101; 418 com remake no Skillry; 207 marcados como parciais | data/videos.json (F1) | 21/10/2026 | 2 |
| F39 | data/videos.json local idêntico ao remoto (sha256 1c307487... confere com raw.githubusercontent.com); commit local 92aee2f5 de 13/10/2026 | sha256 e git log (F1) | 21/10/2026 | 2 |
| F40 | Só 3 de 703 prompts tratam de talking head: sab8a-475686, stokebuilder-356793, twoclipping-551116 | consulta em videos.json (F1) | 21/10/2026 | 2 |
| F41 | Zero prompts citam split screen, emoji, react, rembg ou segmentação de pessoa. 13 citam legenda, 13 citam 9:16, 18 tipografia cinética, 30 seek(t), 32 Playwright, 22 motion blur por subquadros, 13 -14 LUFS | consulta em videos.json (F1) | 21/10/2026 | 2 |
| F42 | twoclipping-041659 descreve órbita cuja metade de trás passa atrás da cabeça, legenda presa ao tempo de cada palavra e transição que atravessa a cabeça | prompts/twoclipping-041659.md | 21/10/2026 | 2 |
| F43 | twoclipping-551116: clipes de quem fala para a câmera dentro do layout, stickers recortados com borda branca, letras subindo por máscara, P&B que vira cor, 8 subquadros de motion blur, -14 LUFS | prompts/twoclipping-551116.md (F1) | 21/10/2026 | 2 |
| F44 | stokebuilder-356793 manda deixar quem fala em PiP quando um gráfico ocupa a tela e proíbe inventar fatos, números ou citações. Prompt marcado como parcial | prompts/stokebuilder-356793.md; videos.json | 21/10/2026 | 2 |
| F45 | sab8a-475686 tem 86 caracteres: "Cut a raw talking-head clip into a punchy, fun edit with subtitles, graphics and music". Tag ai-image | videos.json (F1) | 21/10/2026 | 2 |
| F46 | techhalla-498547: mola por glifo com escalonamento de 125 ms, punch-in de 1,0 a 1,08, 4 subquadros, pré-passe de 8 stills, desalinhamento magenta e verde | prompts/techhalla-498547.md (F1) | 21/10/2026 | 2 |
| F47 | gdgtify-929495 manda não forçar a fala numa batida musical e pede pelo menos 400 ms de quietude; seek(t) determinístico | prompts/gdgtify-929495.md | 21/10/2026 | 2 |
| F48 | twoclipping-000267 bane shockwave, partículas, RGB split, camera shake, lens flare, neon, piso de grade, fundo piscando e easing elástico; usa tmix de 3 subquadros (t menos, t, t mais 1/240 s) a 60 fps, SFX pelo pico medido e loudnorm -14; avisa para não pôr opacidade ou filtro em elemento preserve-3d | prompts/twoclipping-000267.md linhas 18, 35 e 36 | 21/10/2026 | 2 |
| F49 | alex-prompter-997524: 5 cenas em 30 s (problema, o que eu faço, 3 passos, prova, nome), 348 caracteres | prompts/alex-prompter-997524.md (F1) | 21/10/2026 | 2 |
| F50 | O videos.json não tem views, retenção nem conversão de nenhum vídeo | data/videos.json (F1) | 21/10/2026 | 2 |
| F51 | Páginas Skillry dos 6 prompts com remake responderam HTTP 200 | GET (F1) | 21/10/2026 | 2 |

### 1.5 Mercado: reels de terceiros (pesa em D2 e D3, só como contexto)

| # | Fato | Fonte | Coleta | Nível |
|---|---|---|---|---|
| F52 | 4 buscas Buzzfy (pt, 365 dias) devolveram 109 reels; 10 talking heads de 2026 escolhidos, views de 494 a 287.470, mediana 37.691 | buzzfy_reel_search Q1 a Q4 (F2) | 21/10/2026 | 2 |
| F53 | 10 de 10 mostram o rosto do criador e têm texto na tela no frame 0 | Buzzfy, campo on_screen_text (F2) | 21/10/2026 | 2 |
| F54 | 5 de 10 abrem com título fixo diferente da fala (#3, #4, #5, #9, #10); 5 de 10 abrem com texto igual ao início da fala (#1, #2, #6, #7, #8). Que esse texto seja legenda sincronizada é inferência | Buzzfy (F2) | 21/10/2026 | 2 |
| F55 | Os 4 reels de negócio ou saúde com gancho "good" no Buzzfy usam título fixo (#3, #4, #5, #9). O rating é qualitativo; N = 10 | Buzzfy (F2) | 21/10/2026 | 2 |
| F56 | @clinicavolpe (DdNAJMnSOQb): 162.820 views, 7.837 comentários (4,8%) com o CTA "EU QUERO"; o segundo maior em comentários tem 0,48% | Buzzfy (F2) | 21/10/2026 | 2 |
| F57 | @rosangelahaydem (Dc9PthWJYXP): 287.470 views, 29.068 compartilhamentos (10,1%); "Se eu fosse" de @flaviotavaresoficial: 4,2% e 5,1% | Buzzfy (F2) | 21/10/2026 | 2 |
| F58 | Recorte dentista ou consultório (Q1): o maior teve 764 views; o reel com o nosso ângulo (fisio, hora contra empresa, @fisiomarcoaraujo) teve 494 | Buzzfy (F2) | 21/10/2026 | 2 |
| F59 | Duração dos 10: só 2 abaixo de 50 s (#2 com 47 s, #4 com 44 s) | Buzzfy (F2) | 21/10/2026 | 2 |
| F60 | Edição dos 10 (cortes por segundo, zoom, b-roll, split, react, texto 3D, SFX): sem dado. Buzzfy sem plano pago (pacing nulo) e cota diária esgotada (call_ids 0aba82df-556d-439f-862d-9cb74f574896 e afd6af79-bc75-400b-8fe8-37b484ec933c) | erro registrado (F2 Q5 e Q6) | 21/10/2026 | 1 (registro do erro) |
| F61 | OpusClip afirma: em 13,5 milhões de clipes, 80,2% têm legenda, 78,6% legenda animada, 6,0% b-roll, música abaixo de 2%. Método não descrito, amostra da própria ferramenta | opus.pro/blog/video-editing-tips, 03/06/2026 | 21/10/2026 | 3 |
| F62 | Choppity afirma, a partir de 6 Shorts do Hormozi: corte a cada 1 a 3 s, punch-in de 10% a 20%, 2 a 4 palavras por vez, palavra ativa amarela, sem SFX nas transições | choppity.com (F2) | 21/10/2026 | 3 |
| F63 | VibeRoll afirma: cortar silêncio acima de cerca de 0,5 s, b-roll em 30% a 50%, zona segura livre nos ~220 px de cima e ~450 px de baixo, whoosh e hit nos cortes | viberoll.questera.ai, 30/07/2026 | 21/10/2026 | 3 |
| F64 | OpusClip afirma (500 vídeos, TikTok, método não descrito): troca de estímulo a cada 4 s dá 58% de retenção contra 41% do talking head estático | opus.pro/blog/tiktok-length-format-retention-data, 11/11/2025 | 21/10/2026 | 3 |
| F65 | Statusphere afirma (2.000 vídeos, maio a julho de 2024): Reels de 60 a 80 s têm 71% mais views que os abaixo de 60 s. Kapwing (08/07/2026) diz 21 a 34 s sem ligar número a fonte | brands.joinstatus.com; kapwing.com | 21/10/2026 | 3 |
| F66 | O texto atrás da pessoa existe como técnica documentada (FlexClip, template CapCut); nenhuma fonte traz dado de desempenho dele, de split screen ou de react em talking head de negócio | flexclip.com (F2) | 21/10/2026 | 3 |
| F67 | A afaqs.com cita Mosseri: "imperfection becomes a signal". Post original não aberto | afaqs.com, 05/01/2026 | 21/10/2026 | 3 |

### 1.6 CFO e regras (pesa no conteúdo de tela dos 3 modelos)

| # | Fato | Fonte | Coleta | Nível |
|---|---|---|---|---|
| F68 | 474.659 cirurgiões-dentistas ativos na soma das 27 linhas por CRO (linha SOMA do CSV confere). Outra leitura do mesmo dia: 474.640. A página não exibe total nacional nem diz se conta pessoa ou inscrição | website.cfo.org.br/estatisticas/quantidade-geral-de-entidades-e-profissionais-ativos/, rodapé "Última atualização WSCFO: 21/10/2026"; evidencias-F3/cfo-ativos-por-cro-2026-10-21.csv, reconferido | 21/10/2026 16:40 UTC | 2 |
| F69 | Mesma tabela: SP 126.491, MG 59.164, RJ 41.109, PR 28.217, BA 24.047; EPAO 102.088; ASB 199.155; TSB 53.620; TPD 26.358; total 868.951 | CSV (F3), reconferido | 21/10/2026 | 2 |
| F70 | Especialistas: TOTAL GERAL 162.011; ortodontia 34.506; implantodontia 24.042; endodontia 21.054; HOF 6.845 total nacional (5.479 F, 1.366 M) | website.cfo.org.br, tabela de especialistas (F3) | 21/10/2026 | 2 |
| F71 | CD com ano de inscrição no regional em 2026: 29.495 | tabela por ano do CFO (F3) | 21/10/2026 | 2 |
| F72 | Res. CFO 196/2019: selfie liberada (com TCLE se houver paciente); proibido identificar equipamento, instrumental, material e tecido; proibido vídeo do procedimento em andamento; vedada promessa de resultado, sensacionalismo, autopromoção, mercantilização; exige nome e número de inscrição; vedado caso de terceiro | texto oficial, evidencias-F3/res-cfo-196-2019.txt | 21/10/2026 | 2 |
| F73 | Código de Ética (Res. 118/2012, PDF de 2012): art. 35 V e VII (propaganda enganosa de curso, gratuidade para atrair aluno); art. 44 I, III, IV, XII (antes e depois, preço, gratuidade, pagamento, técnica sem comprovação, crítica à técnica de colega); art. 45 (responsabilidade solidária) | evidencias-F3/codigo-etica-odontologica-118-2012.txt | 21/10/2026 | 2 |
| F74 | Res. 271/2025 só alterou art. 20 VIII e X, revogou art. 32 XIII e mudou art. 44 XIV (aliciamento) | evidencias-F3/res-cfo-271-2025.txt | 21/10/2026 | 2 |
| F75 | Decisão CFO 05/2025 criou grupo para reescrever o capítulo de publicidade; nenhuma resolução de 268 a 308/2026 (29/09/2026) publicou o texto novo | evidencias-F3/decisao-cfo-05-2025.txt; varredura (F3) | 21/10/2026 | 2 |
| F76 | Res. 286/2026 art. 16 §3º: vedada a divulgação de curso de cirurgia estética orofacial com paciente sem autorização prévia do CRO | evidencias-F3/res-cfo-286-2026.txt | 21/10/2026 | 2 |

### 1.7 Conflitos entre fontes (registrados, não resolvidos aqui)

| # | Conflito | Lado A | Lado B |
|---|---|---|---|
| C1 | Corte de pulo do reel do dentista | 68% (D2, D3, mediana F12) | 60% (06-plano-final.md linha 179, PRIOR) |
| C2 | Número de dentistas ativos | 474.640 (00-enquadramento) | 474.659 (F3, 16:40 UTC). A tabela muda ao longo do dia |
| C3 | Trecho 27,24 a 29,28 s | "passa a forna que a gente disputa" (transcrição automática) | "passa a formar quem disputa" (contexto.md). Só o ouvido decide |
| C4 | SFX nas transições | Choppity: Hormozi não usa | VibeRoll: whoosh e hit nos cortes |
| C5 | B-roll | OpusClip: 6,0% dos clipes usam | VibeRoll: cobrir 30% a 50% |
| C6 | Duração | Statusphere: 60 a 80 s têm 71% mais views | Kapwing: 21 a 34 s |
| C7 | True peak de saída | add_music.sh do Tzur: TP -1,5 dBTP | alvo da D1: -1,0 dBTP |
| C8 | Subquadros de motion blur | twoclipping-000267: 3 | twoclipping-551116: 8; techhalla-498547: 4 |
| C9 | Janela do Bruno na tela dividida | F1: 1080x960 com fundo trocado | F4: 1080x1120 recortada do base, sem nova ampliação |
| C10 | Comentários de @marinamangaravite | Buzzfy: 116 | página web: 148 (leituras em momentos diferentes) |

---

## 2. Fatos a buscar

| # | O que falta | Decisão | Onde buscar | Custo de buscar |
|---|---|---|---|---|
| B01 | Qual redução de ruído (rn_std, rn_sh, rn_bd ou outra) e qual cadeia geraram o voz_master.wav | D1 | histórico de comandos da sessão anterior no scratchpad/dent; se não houver, refazer e comparar | baixo |
| B02 | O que foi dito de fato em 24,94 a 29,04 s ("forna que a gente" ou "formar quem") | D1, D2, D3 | ouvir voz_master.wav e raw.wav no trecho; alinhar de novo com faster-whisper só nesse trecho | baixo |
| B03 | O que há de fato nas pausas de 13,37 a 13,79 s e 31,63 a 31,95 s do voz_master (ver DR02: só 4 a 6 dB abaixo da fala) | D1 | ouvir e ver espectrograma desses trechos; conferir se é cauda de palavra, respiração ou ruído | baixo |
| B04 | Aprovação escrita do Bruno do áudio e de cada modelo | D1, D2, D3 | mensagem do Bruno | depende do Bruno |
| B05 | Especificação de loudness do Instagram para Reels | D1 | documentação oficial da Meta; não há publicação conhecida até aqui (00-enquadramento marca -1,0 dBTP como PRIOR) | baixo |
| B06 | Desempenho do case Tzur v2 (se foi publicado) | D2 | ig_post_stats (Buzzfy) da conta, leitura apenas | baixo |
| B07 | Alcance, views, tempo assistido e pulo do reel do dentista publicado | D2, D3 | ig_post_stats (Buzzfy) até 05/11/2026; comentários "dentista" em listCommentAutomationLogs (PostZen) | depende da publicação |
| B08 | Edição medida dos 10 reels de referência (cortes por segundo, zoom, b-roll, split, react, texto 3D, SFX) | D2, D3 | buzzfy_reel_detail no plano pago (campo pacing) ou o Bruno abrir os links e anotar | médio (plano pago) ou manual |
| B09 | Retenção de reels de terceiros | D2, D3 | não acessível por fonte pública conhecida | provavelmente inacessível |
| B10 | Qualidade visual real das técnicas dos 8 prompts | D3 | assistir aos remakes nas páginas Skillry (HTTP 200) e aos originais | baixo |
| B11 | Existência dos posts no X de twoclipping-041659 e twoclipping-551116 | D3 | abrir com navegador logado ou outra fonte; não muda a técnica, só a atribuição | baixo |
| B12 | Commit remoto atual do repositório | D3 | gh ou API quando o acesso da sessão permitir (hoje 403) | baixo |
| B13 | Tempo real de render de cada modelo (nenhum render deste pipeline foi cronometrado do início ao fim) | D2, D3 | cronometrar um render curto de 300 quadros por modelo antes do render cheio | baixo |
| B14 | Custo por quadro da tipografia com glifos SVG deformados e da mistura de subquadros em numpy | D3 | teste curto em 30 a 60 quadros | baixo |
| B15 | Se a composição só com filtros do ffmpeg (alphaextract, negate, blend, alphamerge) reproduz o comp.py | D2 | teste de 300 quadros comparando com o comp.py | baixo |
| B16 | Se tmix em RGBA com alfa reto escurece borda | D2, D3 | teste de 30 quadros com um letreiro semitransparente | baixo |
| B17 | Método de ampliação de 576x1024 para 1080x1920 usado no base.mp4 | D2, D3 | metadado do base.mp4 (encoder, filtros) ou histórico de comandos | baixo |
| B18 | Se o vidstab (tr.trf) segura o letreiro preso à parede | D2, D3 | teste curto | baixo |
| B19 | Se a tabela do CFO conta pessoas ou inscrições | todas (texto de tela) | página de método do CFO ou pedido via ouvidoria (não enviar nada: só leitura de página pública) | médio |
| B20 | Se o Bruno é inscrito em algum CRO | todas (texto de tela) | pergunta ao Bruno | baixo |
| B21 | Interpretação do CRO sobre ícone de dente e reel público sobre curso para dentista | todas | consulta formal ao CRO (decisão do Bruno; agente não envia) | alto |
| B22 | Lei 5.081/1966, CDC e CONAR para anúncio de curso | todas | planalto.gov.br (hoje 503), conar.org.br | baixo |
| B23 | Se a conta tem o recurso de trial reels | D4 (fora deste livro, afeta D2 e D3) | Buzzfy, leitura apenas | baixo |
| B24 | Autorização para citar o case Tzur na tela | D2 | Bruno e o cliente Tzur (06-plano-final.md seção 7, item 5) | depende de terceiros |
| B25 | Protocolo do júri cego de 3 cadeiras (quem, escala, o que vê) | D3 | definir no plano; hoje não existe | baixo |

---

## 3. Fatos a derivar

Valores já calculados aqui vêm marcados [ESTIMATIVA] com a conta. Os que dependem de decisão ficam só com o método.

| # | O que derivar | Como | Resultado (se já dá) |
|---|---|---|---|
| DR01 | Quanto o true peak precisa cair | -0,5 - (-1,0) | [ESTIMATIVA] pelo menos 0,5 dB de redução de pico (limitador true peak antes de somar trilha e SFX; medir de novo depois da mistura) |
| DR02 | Distância entre fala e pausa em cada versão de áudio (critério de 40 dB da D1) | RMS da fala (janelas das 79 palavras) contra RMS de 5 pausas de 0,3 s ou mais, cortando 50 ms de cada borda; numpy em 48 kHz mono, rodado por esta cadeira em 21/10/2026 | [ESTIMATIVA] diferença média fala menos pausa: raw 8,3 dB; rn_std 14,3; rn_sh 15,6; rn_bd 16,3; voz_master 16,0. No voz_master as pausas medem -35,8, -19,9, -28,5, -48,0 e -18,1 dBFS contra fala de -14,1 dBFS; a melhor pausa (22,27 a 22,65 s) fica 33,9 dB abaixo. Nenhuma versão chega a 40 dB por este método. Ressalva: as janelas vêm do alinhamento automático e podem conter cauda de palavra ou respiração (ver B03) |
| DR03 | Duração se cortar pausas | 36,44 menos as pausas cortadas | [ESTIMATIVA] todas cortadas: cerca de 33,46 s; todas menos a de 0,60 s: cerca de 34,06 s; só as acima de 0,5 s (0,52 e 0,60): cerca de 35,32 s. Sem contar respiros de 0,30 s que o Tzur preserva |
| DR04 | Quadro de cada palavra-chave a 30 fps | round(t x 30) a partir de words-raw.json | [ESTIMATIVA] "474" quadros 62 a 95; "mil" 95 a 114; "colegas" 114 a 132; "hora" 230 a 244; "cadeira" 249 a 264; "mercado." 574 a 585; pausa 585 a 603; "Qual" 603 a 613; "ensinar" 619 a 646; "colega?" 655 a 667; "desenho" 685 a 706; "lançamento," 711 a 727; "segundo" 923 a 935; "produto." 935 a 947; "Dentista" 960 a 980; "comenta" 980 a 1007; "respondo." 1061 a 1078 (sem cortar pausas; refazer se cortar) |
| DR05 | Se a quietude de 400 ms cabe em pausa real | comparar 0,40 s com as pausas de F07 | [ESTIMATIVA] cabe em 2 pausas: 0,60 s (19,50 a 20,10) e 0,52 s (13,32 a 13,84). Não cabe em 0,48 nem 0,42 se exigir 400 ms mais margem de 50 ms em cada borda |
| DR06 | Ampliação total da fonte com zoom de 1,25x | 1,875 x 1,25 | [ESTIMATIVA] 2,34x da fonte 576x1024 |
| DR07 | Capturas de render por modelo | 1093 quadros x camadas x subquadros | [ESTIMATIVA] 2 camadas sem subquadro: 2.186 (F1 usou 1.092 e chegou a 2.184); com 3 subquadros: 6.558; com 8: 17.488. Aplicar subquadro só nas janelas de movimento reduz em proporção ao tempo dessas janelas |
| DR08 | Tempo de render de A, B e C | soma dos custos por quadro de F26 | [ESTIMATIVA, F4] A cerca de 951 s; B cerca de 887 s; C 1008 a 1319 s; os três em série 47 a 53 min com a máscara pronta; em paralelo piora (F28) |
| DR09 | Área útil fora da zona segura em 1080x1920 | 1920 - 220 - 450 | [ESTIMATIVA] 1.250 px de altura útil (y 220 a 1470), se a zona da VibeRoll (nível 3) for adotada |
| DR10 | Faixa do letreiro de trás versus topo da cabeça | cruzar a faixa escolhida com F29 por quadro | método: para cada quadro, medir quanto do letreiro fica sob a máscara; F4 propõe y=120 a 450 px. Com topo mínimo em y=252, a faixa de 120 a 252 fica livre em 100% dos quadros [ESTIMATIVA a partir de F29] |
| DR11 | Percentual do tempo com o rosto visível em cada modelo | somar os intervalos sem tela cheia de gráfico na lista quadro a quadro | depende da lista; fecha o critério de 80% (HIPÓTESE da D2) |
| DR12 | Número de trocas de estímulo em cerca de 36 s | 36/5 e 36/3 | [ESTIMATIVA] 7 a 12 trocas, se a regra de 3 a 5 s (nível 3 e PRIOR) for adotada |
| DR13 | Início de cada SFX | tempo do evento visual menos o pico de F35 | exemplos [ESTIMATIVA, F4]: whoosh que fecha em 20,10 s começa em 19,83 s; riser que culmina em 3,18 s começa em 1,58 s |
| DR14 | Tamanho do arquivo final | duração x taxa | [ESTIMATIVA] 36,43 s x 13,99 Mb/s / 8 = cerca de 64 MB; versão leve a 2,55 Mb/s: cerca de 12 MB |
| DR15 | Disco de PNG por modelo | 1093 x 0,5 a 2,2 MB | [ESTIMATIVA, F4] cerca de 0,5 a 2,4 GB por camada pesada |
| DR16 | Participação de SP e teto de especialistas | 126.491/474.659; 162.011/474.659 | [ESTIMATIVA] 26,6%; no máximo 34,1% (teto, pode contar duas vezes quem tem duas especialidades) |
| DR17 | Meta de alcance em múltiplos da mediana | 106/53; 307/53 | [ESTIMATIVA] 106 = 2,0x; melhor reel = 5,8x |
| DR18 | Taxas dos reels de terceiros | comentários/views, compartilhamentos/views | [ESTIMATIVA, F2] 4,8% (@clinicavolpe); 10,1% (@rosangelahaydem); mediana de compartilhamento dos 10: 1,75%; mediana de duração: 82,5 s |
| DR19 | Loudness integrado, true peak e LRA de cada arquivo final | ffmpeg loudnorm print_format=summary ou ebur128 no MP4 final de cada modelo | só depois do render (critério de sucesso da D1) |
| DR20 | Voz acima da trilha em todo trecho falado | RMS por janela de 400 ms da voz contra a trilha, só nas janelas de fala do words-raw.json | só depois da mistura |

---

## 4. Palpites (nível 4, separados; nenhum fecha objeção sozinho)

| # | Palpite | De onde vem | Como virar fato |
|---|---|---|---|
| P01 | Ruído nas pausas pelo menos 40 dB abaixo da voz como critério de "sem ruído audível" | 00-enquadramento, D1, corte sem origem medida. DR02 mostra que nenhuma versão atual chega lá pelo método usado | definir o método (janela, cauda) e testar no ouvido do Bruno |
| P02 | -1,0 dBTP como alvo de true peak de plataforma | 00-enquadramento; o Instagram não publica especificação conhecida | B05 |
| P03 | SFX entre -18 e -24 dB abaixo do pico da voz | F4 4.4 | ouvir e medir DR20 |
| P04 | Obturador de 180° a 30 fps: subquadros em t ± 1/120 s, 3 amostras nos movimentos comuns e 5 nas transições | F4 4.3 | teste visual curto (B16) |
| P05 | B tende a parecer mais "After Effects" e C tende a explicar melhor | F1 seção 6 | júri cego (B25) |
| P06 | Título fixo com a tese somado à legenda palavra a palavra segura melhor a abertura | F2, a partir de F55 (N = 10, rating qualitativo) | ig_post_stats do reel publicado; N = 1 não separa formato de dia |
| P07 | Algo deve mudar na tela a cada 3 a 5 s; punch-in de 10% a 20%; 2 a 4 palavras por vez na legenda | F62 a F64 (nível 3) usados como regra | sem teste previsto na conta |
| P08 | Estilo brainrot (corte a cada 0,6 a 0,8 s) não serve para público de dentista | F2 seção 4 | nenhum |
| P09 | B-roll ou react em no máximo 30% do tempo | F2, entre F61 e F63 | DR11 e retenção do reel publicado |
| P10 | Cortar pausas acima de 0,5 s melhora retenção | F63 (fornecedor) | nenhum teste na conta |
| P11 | Ícone de dente estilizado não fere a Res. 196/2019 | F3, interpretação | B21 |
| P12 | Letreiros de negócio e ensino, reacts de plateia e o CTA "comenta a sua profissão" têm risco baixo perante o CFO | F3, marcados HIPÓTESE lá | B21 |
| P13 | O Bruno não é inscrito no CFO, então o código o alcança só por via do dentista que aparece, reposta ou contrata | F3 seção 3.1, HIPÓTESE | B20 |
| P14 | Lei 5.081/1966, CDC e CONAR vedam propaganda enganosa em termos parecidos | F3, por fonte secundária | B22 |
| P15 | Publicar os 3 modelos do mesmo bruto na mesma conta reduz o alcance de cada um | 00-enquadramento D4 | sem precedente na conta |
| P16 | Rosto visível em 80% do tempo como limite de "maior parte do vídeo" | 00-enquadramento D2, HIPÓTESE de corte | DR11 mais resultado publicado |
| P17 | O júri cego mede acabamento, não conversão | 00-enquadramento D3 | nenhum; é limite do método |
| P18 | Unsharp leve depois da ampliação reduz o aspecto lavado do rosto | F4 R1 | teste visual de 1 quadro |
| P19 | A janela de 1080x1120 recortada do base mostra cabeça e ombros sem nova ampliação | F4 4.1, a partir dos frames-amostra | render de 1 quadro por layout |
| P20 | A frase de Mosseri ("imperfection becomes a signal") favorece edição menos polida | F67 (nível 3) mais leitura do modelo | nenhum |
| P21 | Probabilidade de 0,40 de o reel bater alcance de 106 ou mais e pulo abaixo de 60%; mediana prevista de 95 de alcance para os 3 nichos | 06-plano-final.md linha 204, PRIOR sem conta | B07 em 05/11/2026 |
| P22 | Tirar quem passa ao fundo mantendo só o maior componente conexo da máscara resolve os 44 quadros de F30 | F4 R6 | teste em 17,4 s, 19,4 s, 26,8 s e 33,9 s |

---

## Lacunas desta cadeira

- Não ouvi o áudio. DR02 é medição por janela de alinhamento automático; B02 e B03 só fecham no ouvido.
- Não reabri os prompts do repositório nem as páginas do CFO; os fatos de nível 2 dessas fontes vêm de F1 e F3 (com arquivos de evidência). O CSV do CFO foi reconferido.
- Os custos de render (F26, DR08) vêm de testes curtos de F4, não de um render completo.
