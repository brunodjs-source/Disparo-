# Plano da cadeira K · Advogado do diabo · Reel do dentista · Agência Reunida Modo GOD · 21/10/2026

Cliente: O Estrategista (@o_estrategista.com.br). Bruto: selfie do Bruno, 36,44 s.

| Campo | Conteúdo |
|---|---|
| Persona | Cadeira que procura o que vai dar errado: premissa frágil, dinheiro jogado fora, risco de política e de reputação |
| OTIMIZA PARA | Proteger o caixa do cliente e a credibilidade da Agência |
| PONTO CEGO (assumido) | Travar tudo por excesso de cautela. Compensação escrita: toda objeção abaixo vem com um conserto barato e um critério de liberar. Nenhuma objeção minha atrasa a publicação de 29/10, com duas exceções que custam zero tempo: tirar o case Tzur da tela e tirar a prova social inventada do bloco final do ov2.html |
| PERGUNTA CONTRÁRIA | Qual é o plano de menor arrependimento? Resposta na seção 1.1 |

Etiquetas: [FATO] com fonte · [ESTIMATIVA] com conta · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, nível 4, nunca fecha objeção sozinho.
Trabalhei isolado: não abri planos nem evidências de outras cadeiras. Medições novas desta cadeira estão em `run/02-cadeiras/evidencias-K/` (scripts e logs).

---

## 1. Veredito (12 linhas)

1. Fazer os 3 modelos, como o Bruno pediu, mas em portões: áudio aprovado primeiro, depois A, depois C, depois B. Publicar só 1 em 29/10.
2. Achado novo: o "forna que a gente disputa" é defeito da redução de ruído, não da fala. No raw.wav o reconhecimento lê "formar quem disputa" com probabilidade 0,99 e 0,91. No voz_master lê "forçar" (0,45) [FATO, evidencias-K/b02_trecho.log].
3. Logo, o áudio sai de novo do raw, com redução mais leve. O voz_master atual perde consoante: confiança média de reconhecimento 0,850 contra 0,878 do raw [FATO, evidencias-K/inteligibilidade_K.log].
4. O bruto chegou pelo WhatsApp: vídeo de 1,31 Mb/s e áudio AAC de 59,8 kb/s [FATO, ffprobe do upload]. Pedir ao Bruno o arquivo original do celular é a ação mais barata para melhorar rosto, máscara e voz.
5. True peak: o MP4 já entregue (dentista-audio-masterizado.mp4) mede -0,3 dBTP depois do AAC [FATO, ffmpeg]. Limitar o PCM em -1,5 dBTP deixa o AAC em -1,5 [FATO, evidencias-K/tp_aac_teste.log].
6. O critério de 40 dB de ruído nas pausas é PRIOR e nenhuma versão chega a ele (DR02). Trocar por critério de ouvido e de inteligibilidade, senão a D1 fracassa por régua, não por som.
7. Modelo A: Tzur v2 enxuto e corrigido. Tirar o corte mk[:470]=0, pôr o letreiro na faixa y 300 a 420 (a cabeça cobre no máximo 29% dela em 90% dos quadros) e cortar a prova inventada [FATO, evidencias-K/ocupacao_mask.log; F32].
8. Modelo C (tipografia cinética sobre o rosto, sem rembg) é o reserva de publicação. Ele não depende da máscara, que é a peça mais frágil do pipeline.
9. Modelo B (tela dividida com reacts) atende ao pedido literal "dividindo com reacts". É o mais exposto: reduz o rosto a 58% da tela, e a conta só tem dado de rosto em tela cheia.
10. O Tzur não entra na tela. Ele não foi dito, a autorização não está confirmada, e ao lado de dentista "6 para 20 milhões" vira leitura de promessa.
11. Formato não é o gargalo de conversão da conta. Em 30 dias foram 12 comentários, 7 cliques no link, 1 disparo de automação e 0 vendas [FATO, 00-SISTEMA.md]. O risco de caixa é gastar horas de AE e esquecer a resposta manual ao CTA.
12. Probabilidade de o reel publicado bater alcance de 106 ou mais e pulo abaixo de 68% em 7 dias: 0,35, faixa de 0,20 a 0,50 [PRIOR, base: mediana de 53 e Bruno em cena de 2,4x a 5,8x].

### 1.1 Pergunta contrária: qual é o plano de menor arrependimento?

O de menor arrependimento erra barato e cedo, e não erra caro nem em público:
1. **Hoje (custo de 1 mensagem):** pedir ao Bruno o vídeo original do celular, mandado como documento ou por Drive, para não passar de novo pela compressão do WhatsApp. Se não vier até 22/10 12h, segue o bruto atual sem esperar.
2. **Áudio uma vez para os 3:** cadeia do raw com redução mais leve, conferida por ouvido e por reconhecimento automático no trecho de 24,94 a 29,04 s, limitador em -1,5 dBTP e medida no MP4 final. Um áudio errado contamina 3 renders. Um áudio certo serve aos 3.
3. **Um arquivo de tempos para os 3:** legenda corrigida ("no Brasil", "deixa de disputar paciente e passa a formar quem disputa") num JSON só. B e C leem do mesmo arquivo.
4. **A primeiro, com QA de máscara:** zero quadro com letreiro sobre olhos ou boca e zero pessoa do fundo dentro da máscara. Se não passar até 27/10, publica o C.
5. **Publicar 1 só em 29/10.** Os outros 2 ficam no arquivo para outro nicho ou para trial reel, se a conta tiver o recurso (sem dado, B23).
6. **Nada que não se desfaça:** sem Tzur, sem @ fictício, sem número sem fonte, sem ícone de dente real, sem "coin" de dinheiro no SFX.
7. **O que mais protege o caixa:** o Bruno responder à mão cada "dentista" nos comentários em até 2 h nas primeiras 48 h [HIPÓTESE]. Isso decide conversão mais que qualquer letreiro.

Arrependimentos que esse plano evita: (a) publicar prova inventada e perder credibilidade com público profissional; (b) renderizar 3 vídeos em cima de um áudio que o Bruno manda refazer; (c) letreiro por cima da cabeça em 71,6% dos quadros (F29); (d) descobrir na timeline que a legenda diz "forna que a gente". Arrependimento que ele aceita: B e C podem nunca ser publicados. O custo é cerca de 30 a 40 min de render (F4, DR08) mais montagem.

---

## 2. Respostas às 14 perguntas

### P1. Qual modelo a cadeira defende e quais ids entram?

Defendo **produzir os 3 e publicar o A enxuto corrigido**, com o **C como reserva automática** se o A falhar no QA de máscara. O B fica como variante de arquivo.

| Modelo | Ids misturados | O que aproveita | O que descarta, e por quê |
|---|---|---|---|
| A (o que já fazemos) | pipeline Tzur v2 (seg.py, ov2.html, cap2.js, comp.py, add_music.sh); twoclipping-041659; twoclipping-000267 | Letreiro 3D na camada de trás com extrusão de 14 text-shadow e rotateX 55° para 0° (F24). Órbita e ordem atrás e frente da cabeça (041659, F42). Lista de banidos, SFX pelo pico e loudnorm -14 (000267, F48) | mk[:470]=0 do comp.py (F29). Bloco final com "1.287 comentários" e @ fictícios, glifos ♥ ✓ ✕, RGB split, tremida e confete com Math.random (F32, banidos em F48). Constantes de 54,2 s (F34). Aplausos (não há plateia, soa falso) |
| B (tela dividida com reacts) | stokebuilder-356793; twoclipping-551116; twoclipping-000267 | Gráfico com quem fala sempre visível e texto fiel ao dito (356793, F44). Stickers recortados com borda branca e letras subindo por máscara (551116, F43). Banidos e SFX pelo pico (000267) | PiP pequeno do 356793 (encolhe o rosto demais). 8 subquadros do 551116 (custo 2,7x o de 3, DR07). Qualquer emoji ou glifo de texto como react (F41, regra do CLAUDE.md) |
| C (tipografia cinética sobre o rosto) | gdgtify-929495; techhalla-498547; twoclipping-041659; alex-prompter-997524 (só o mapa de batidas) | Fala como relógio e quietude de pelo menos 400 ms (929495, F47). Mola por glifo com 125 ms entre letras e punch-in de 1,0 a 1,08 (498547, F46). Legenda presa ao tempo de cada palavra (041659). As 5 batidas do 997524 viram rótulos de capítulo | Cenas em tela cheia sem rosto do 997524 (contra F13). A batida "prova" do 997524 (não há prova dita). Desalinhamento magenta e verde e a paleta do 498547 (RGB split é banido em F48). rembg (o C não precisa de máscara) |

Por que A e não B como principal: o A é o pedido literal mais forte ("letreiro 4D atrás", "o que já fazemos"), mantém o rosto em tela cheia (o único formato com dado na conta, F13) e reaproveita código existente. O risco dele é técnico e mensurável antes de publicar (máscara). O risco do B é de desempenho e só aparece depois de publicar.

### P2. Rosto de 0 a 3 s, porcentagem do tempo e zoom

| Modelo | Rosto em 0 a 3 s | Rosto visível no total | Tamanho do rosto | Zoom máximo |
|---|---|---|---|---|
| A | Sim, tela cheia desde o quadro 0 | 35,50 de 36,44 s = 97,4% [ESTIMATIVA: 36,44 menos 2 cartões de 0,52 e 0,42 s] | Tela cheia | 1,08 (punch-in), total de 2,03x da fonte (1,875 x 1,08) |
| B | Sim, tela cheia de 0 a 3,18 s | 100% (tela cheia em 0 a 3,18 s e 32,00 a 36,44 s; janela de 1080x1120 no resto) | 58% da altura em 28,82 s, ou 79% do vídeo [ESTIMATIVA: (31,58 menos 3,18) / 36,44 = 0,78; rosto menor nesse trecho] | 1,00 na janela (sem nova ampliação); 1,06 nas partes em tela cheia |
| C | Sim, tela cheia desde o quadro 0 | 100% | Tela cheia | 1,08 |

Limite de 1,25x: nenhum modelo passa de 1,08. Motivo: a fonte já está ampliada 1,875x (F02, F23), e 1,25x levaria a 2,34x (DR06). O ganho de 1,25x sobre 1,08x é PRIOR (Choppity, nível 3); o custo em nitidez do rosto é certo.

### P3. Lista de edição quadro a quadro

Regras para os 3: saída 1080x1920, 30 fps CFR, 1093 quadros (0 a 1092), sem cortar pausas. Cortar pausas muda todos os tempos, tem ganho só PRIOR (P10) e arrisca cortar cauda de palavra no trecho de alinhamento ruim (24,94 a 29,04 s). Quadro = round(t x 30) sobre words-raw.json. Tempos do trecho corrigido vêm da 2ª transcrição do raw (evidencias-K/b02_trecho.log): "de" 25,38 a 25,56; "formar" 27,52 a 28,02; "quem" 28,02 a 28,16; "disputa." 28,16 a 29,06. Faixa do letreiro de trás: y 300 a 420 (ocupação da pessoa: mediana 0%, p90 29%, máximo 52,4%) [FATO, evidencias-K/ocupacao_mask.log]. Legenda: y 1270 a 1400, acima dos 450 px de baixo (F63, nível 3). Rodapé de fonte: y 1420 a 1450.

#### Modelo A · Tzur v2 enxuto corrigido (o que defendo publicar)

| # | Início s [quadro] | Fim s [quadro] | Palavra que dispara | Camada | Texto na tela | Animação | SFX (início = evento menos pico, F35) |
|---|---|---|---|---|---|---|---|
| A01 | 0,00 [0] | 36,44 [1093] | (todo o vídeo) | tela cheia | (vídeo base.mp4) | Base 1080x1920. Punch-in 1,00 para 1,06 de 0,00 a 3,18 (ease out) e volta a 1,00 até 5,16 | nenhum |
| A02 | 0,00 [0] | 2,08 [62] | "Dentistas" | tela cheia | (sem texto extra) | P&B que vira cor de 2,08 a 2,40 [62 a 72] (assinatura Tzur e 551116) | nenhum |
| A03 | 0,00 [0] | 35,92 [1078] | cada palavra | frente | Legenda de 2 a 4 palavras, palavra ativa em #E8B36A, texto corrigido (P4 e P5) | Entrada por máscara de baixo para cima em 4 quadros | nenhum |
| A04 | 2,08 [62] | 4,80 [144] | "474" | atrás (y 300 a 420) | +474 MIL | Extrusão de 14 sombras, rotateX 55° para 0° em 0,55 s; contagem de 0 a 474 de 2,08 a 3,18 | riser de 0,48 [14] a 2,08 (pico 1596,6 ms) a -24 dB da voz; sub em 2,08 [62] |
| A05 | 3,80 [114] | 5,48 [164] | "colegas" | frente (y 1420 a 1450) | dentistas ativos · Fonte: CFO, out/2026 | Fade de 6 quadros | nenhum |
| A06 | 4,80 [144] | 5,15 [155] | "em" | atrás | (saída do 474 MIL) | Saída de 0,35 s (F24) | nenhum |
| A07 | 7,68 [230] | 9,36 [281] | "hora" | atrás | HORA DE CADEIRA | Mesma extrusão; palavra CADEIRA entra em 8,30 [249] | tick em 7,68 [230] |
| A08 | 10,24 [307] | 13,32 [400] | "perfil" | frente (lado direito, x 700 a 1040, y 760 a 1100) | grade 3x3 de cartões de post iguais, sem dente, sem boca, sem raio X | Cartões entram com 60 ms de diferença; em "mesma" 12,34 [370] todos ficam cinza | pop em 10,24 [307], 3 pops no máximo |
| A09 | 13,32 [400] | 13,84 [415] | pausa após "conclusão." | tela cheia (cartão) | UMA TÉCNICA | Cartão preto e ouro (Série 2), cortes secos de entrada e saída | swipe de 13,18 [395] (pico 137,1 ms) |
| A10 | 13,84 [415] | 17,92 [538] | "Se" | tela cheia | (vídeo) | Punch-in 1,00 para 1,08 em 13,84 a 14,44 | nenhum |
| A11 | 15,08 [452] | 17,92 [538] | "técnica" | atrás | SUA TÉCNICA | Extrusão, entrada 0,55 s | whoosh de 14,81 [444] (pico 268,5 ms) |
| A12 | 19,12 [574] | 19,50 [585] | "mercado." | atrás | UM MERCADO | Entrada curta de 0,30 s, segura até 19,50 | nenhum |
| A13 | 19,50 [585] | 20,10 [603] | pausa após "mercado." | todas | (legenda sai, letreiro some em 3 quadros) | Quietude de 0,60 s: trilha a -40 dB, sem SFX, imagem parada no punch-in (929495) | silêncio de propósito |
| A14 | 20,64 [619] | 22,70 [681] | "ensinar" | atrás | ENSINAR O SEU COLEGA | Extrusão; sublinhado SVG desenhado por traço em 21,82 [655] | ding_si em 20,64 [619] |
| A15 | 22,82 [685] | 24,46 [734] | "desenho" | frente (x 700 a 1040, y 760 a 1100) | (desenho SVG de um plano de lançamento em 5 casas, traço ouro) | Traço que se desenha de 22,82 a 24,24 | typing de 22,52 [676] (pico 302,2 ms), -24 dB |
| A16 | 25,42 [763] | 26,88 [806] | "disputar," | atrás | DISPUTAR PACIENTE | Extrusão; risco horizontal desenhado em 26,88 [806] | tick em 26,88 [806] |
| A17 | 27,52 [826] | 29,28 [878] | "formar" (tempo do raw) | atrás | FORMAR QUEM DISPUTA | Troca por máscara de tipo (000267) do texto riscado para o novo | impact em 27,52 [826] a -24 dB |
| A18 | 30,78 [923] | 31,58 [947] | "segundo" | atrás | 2º PRODUTO | Extrusão, entrada 0,40 s | ding_si em 30,78 [923]. Sem coin (som de dinheiro, ver ideia 41) |
| A19 | 31,58 [947] | 32,00 [960] | pausa após "produto." | tela cheia (cartão) | SUA TÉCNICA, SEU 2º PRODUTO | Cartão preto e ouro, corte seco | swipe de 31,44 [943] |
| A20 | 32,68 [980] | 36,44 [1093] | "comenta" | frente (y 1100 a 1250) | Comenta: DENTISTA | Caixa que cresce com mola; balão de comentário em SVG desenhado por traço em 33,58 [1007] | pop em 32,68 [980] |
| A21 | 35,92 [1078] | 36,44 [1093] | fim de "respondo." | tela cheia | @o_estrategista.com.br | Fade da trilha em 0,5 s | nenhum |

Sem bloco final cinematográfico depois da fala: o do Tzur durava 9,75 s (44,45 a 54,2 s, F34) sem rosto e com prova inventada.

#### Modelo B · tela dividida com reacts (eventos principais)

| # | Início s [quadro] | Fim s [quadro] | Palavra | Camada | Texto ou react | Animação | SFX |
|---|---|---|---|---|---|---|---|
| B01 | 0,00 [0] | 3,18 [95] | "Dentistas" | tela cheia | legenda | Punch-in 1,00 para 1,06 | riser até 2,08 |
| B02 | 3,18 [95] | 31,58 [947] | "mil" | tela dividida: painel opaco 1080x800 em cima, Bruno 1080x1120 embaixo, recortado do base seguindo o centro da máscara, sem nova ampliação (F4) | legenda no pé do painel (y 660 a 780) | Divisão abre com cortina de 8 quadros | swipe em 3,04 [91] |
| B03 | 3,18 [95] | 5,48 [164] | "mil" | painel | 474.659 contando de 474.000, "dentistas ativos", rodapé CFO, out/2026 | Contador (count da Série 2) | tick por mil, 3 no máximo |
| B04 | 7,68 [230] | 9,36 [281] | "hora" | painel | ampulheta SVG + HORA DE CADEIRA | Areia cai por traço | tick |
| B05 | 10,24 [307] | 13,32 [400] | "perfil" | painel | grade 3x3 de posts iguais | P&B que vira cinza, sticker "IGUAL" com borda branca (551116) | pop |
| B06 | 14,44 [433] | 19,50 [585] | "domina" | painel | 1 nó (SUA TÉCNICA) ligado a 12 nós (colegas) | Linhas desenhadas por traço | whoosh |
| B07 | 19,50 [585] | 20,10 [603] | pausa | painel preto | (vazio) | Quietude de 0,60 s | silêncio |
| B08 | 20,64 [619] | 22,70 [681] | "ensinar" | painel | ENSINAR O SEU COLEGA | Letras sobem por máscara (551116) | ding_si |
| B09 | 22,82 [685] | 24,46 [734] | "desenho" | painel | plano em 5 casas | Traço | typing a -24 dB |
| B10 | 25,42 [763] | 29,28 [878] | "disputar," / "formar" | painel em 2 colunas | DISPUTAR PACIENTE (riscado) / FORMAR QUEM DISPUTA | Coluna da direita acende em 27,52 [826] | tick, impact |
| B11 | 30,78 [923] | 31,58 [947] | "segundo" | painel | 2 caixas empilhadas: SUA AGENDA / SEU CURSO | Mola | ding_si |
| B12 | 31,58 [947] | 36,44 [1093] | pausa e CTA | tela cheia | Comenta: DENTISTA | Divisão fecha em 8 quadros; caixa do CTA em 32,68 [980] | swipe, pop |

#### Modelo C · tipografia cinética sobre o rosto (eventos principais)

| # | Início s [quadro] | Fim s [quadro] | Palavra | Camada | Texto | Animação | SFX |
|---|---|---|---|---|---|---|---|
| C01 | 0,00 [0] | 8,80 [264] | "Dentistas" | frente, título fixo (y 240 a 330) | Por que você ainda só vende hora de cadeira? | Presente desde o quadro 0 (F53, F55) | nenhum |
| C02 | 0,00 [0] | 35,92 [1078] | cada palavra | frente (y 1270 a 1400) | legenda palavra a palavra (041659) | Mola por glifo com 125 ms (498547) | nenhum |
| C03 | 2,08 [62] | 4,80 [144] | "474" | frente, palavra-arquitetura (y 900 a 1200, laterais do rosto) | 474 MIL | Letras se erguem como colunas (929495), motion blur de 3 subquadros só na entrada | sub em 2,08 |
| C04 | 3,80 [114] | 5,48 [164] | "colegas" | rodapé | Fonte: CFO, out/2026 | Fade | nenhum |
| C05 | 7,68 [230] | 9,36 [281] | "hora" | frente | HORA / CADEIRA | Palavras empilhadas como tijolos | tick |
| C06 | 9,36 [281] | 13,32 [400] | "quase" | rótulo de capítulo (y 240 a 330) | 1 · O PROBLEMA | Troca do título fixo | nenhum |
| C07 | 13,84 [415] | 19,50 [585] | "Se" | rótulo | 2 · O MERCADO | Punch-in 1,00 para 1,08 | whoosh |
| C08 | 19,50 [585] | 20,10 [603] | pausa | todas | (só o rosto) | Quietude de 0,60 s, nada se move | silêncio |
| C09 | 20,64 [619] | 22,70 [681] | "ensinar" | frente | ENSINAR | Palavra cresce de 1,0 a 1,08 e fica | ding_si |
| C10 | 22,70 [681] | 29,28 [878] | "Eu" | rótulo | 3 · O QUE EU FAÇO | Troca | swipe |
| C11 | 25,42 [763] | 29,28 [878] | "disputar," / "formar" | frente | DISPUTAR PACIENTE (riscado), depois FORMAR QUEM DISPUTA | Máscara de tipo (000267) | tick, impact |
| C12 | 29,28 [878] | 31,58 [947] | "Sua" | rótulo e frente | 4 · SEGUNDO PRODUTO | Mola | ding_si |
| C13 | 32,00 [960] | 36,44 [1093] | "Dentista" | rótulo e frente | 5 · Comenta: DENTISTA | Caixa com mola em 32,68 | pop |

### P4. Trecho de 24,94 a 29,04 s

Legenda: **"você deixa de disputar paciente e passa a formar quem disputa"**. Sem regravação e sem corte.
- [FATO] 2ª transcrição do raw.wav (faster-whisper small, beam 5 e 10, só esse trecho): "Você deixa de escutar paciente e passa a formar quem disputa", com "formar" a 0,99 e "quem" a 0,91. Fonte: evidencias-K/b02_trecho.log.
- [FATO] No voz_master o mesmo trecho dá "deixa de disputar, paciente passa a forçar quem disputa", com "forçar" a 0,45. As 3 reduções de ruído dão "forna a quem", "forma que a gente" e "forma a quem" (evidencias-K/inteligibilidade_K.log).
- [HIPÓTESE forte] O Bruno disse "formar quem". O "forna que a gente" do words-raw.json saiu do áudio já processado. "disputar" no voz_master e "escutar" no raw discordam, mas o texto do roteiro (06-plano-final.md linha 139) é "deixa de disputar paciente". Fecha no ouvido (B02) em 2 minutos.
- Consequência: a legenda corrigida bate com a boca. O risco que o enquadramento via ("corrigir e não bater com a boca") cai.

### P5. "em Brasil"

Corrigir para **"no Brasil"** na legenda. "em" e "no" são sílabas curtas de 0,16 s, quase sem diferença visível na boca. "em Brasil" na tela parece erro de digitação para um público profissional, e isso custa credibilidade [HIPÓTESE]. O F3 recomenda o mesmo.

### P6. 474 mil

Na tela: **"+474 MIL"** no letreiro e o rodapé **"dentistas ativos · Fonte: CFO, out/2026"**. "Mais de 474 mil" é verdade nas duas leituras do dia (474.640 e 474.659, C2) [FATO, F68]. Não escrever 474.659 no letreiro: o número muda ao longo do dia e pode contar inscrição dupla (B19). O B mostra 474.659 só no contador, com rodapé.

### P7. Áudio

Cadeia, do raw.wav ou do original do celular se chegar:
1. Fonte: raw.wav. Não partir do voz_master, que perde consoante (P4).
2. Passa-alta 80 Hz.
3. Redução de ruído mais leve que a atual: escolher entre rn_std, rn_sh e rn_bd, ou misturar 70% processado com 30% seco. A versão escolhida é a que acerta "formar quem disputa" e "técnica" no reconhecimento e passa no ouvido em 13,32 a 13,84 s e 31,58 a 32,00 s (B03). Critério de desempate: menor perda de confiança média contra o raw (0,878).
4. EQ de presença +2 dB entre 3 e 4 kHz, de-esser leve e compressão de 3:1.
5. Loudnorm em duas passadas: I = -14, LRA 7, TP = -1,5, modo linear.
6. Trilha própria sintetizada (som.py da Série 2, sem direito autoral de terceiro) com ducking por sidechain de 6 a 9 dB sob a fala. Na fala a trilha fica de 18 a 22 dB abaixo da voz [PRIOR, P03]. Na quietude de 19,50 a 20,10 s, a -40 dB.
7. SFX alinhados pelo pico (F35), de 18 a 24 dB abaixo do pico da voz [PRIOR, P03].
8. alimiter com 4x de sobreamostragem e teto em -1,5 dBFS, antes do AAC.
9. Medida no MP4 final de cada modelo (ebur128 e loudnorm summary): de -15 a -13 LUFS e true peak até -1,0 dBTP. [FATO] Com teto de -1,5 o AAC de 192 kb/s ficou em -1,5 dBTP e -14,5 LUFS. Com teto de -1,0 o AAC subiu para -0,9 (evidencias-K/tp_aac_teste.log). O C7 resolve-se a favor do -1,5 no PCM.

Critério de ruído: trocar "40 dB abaixo" (PRIOR que nenhuma versão cumpre, DR02) por (a) nenhum ruído audível nas 5 pausas no ouvido do Bruno e (b) diferença fala menos pausa igual ou maior que a do voz_master (16,0 dB) pelo método da DR02.

### P8. Ampliação de 576x1024 para 1080x1920

- Melhor opção: o arquivo original do celular. O upload é "WhatsApp_Video_2026-10-21_at_13.08.15.mp4", com vídeo de 1,31 Mb/s [FATO, ffprobe]. O WhatsApp reduz resolução e taxa. Se o original vier em 1080p ou mais, some a ampliação e a máscara melhora.
- Sem o original: usar o base.mp4 como está (1080x1920, 30 fps CFR, F02). O método de ampliação é sem dado (F23). Aplicar unsharp leve só no rosto (P18), testando 1 quadro antes.
- Risco no recorte: a máscara tem 360x640 [FATO, ffprobe de mask.mp4], vinda de 320x320 interno (F31), e é ampliada 3x na composição. Halo de até cerca de 6 px na vertical (F31). Mitigar com erosão de 1 a 2 px e borda suavizada de 3 px, e mantendo o letreiro na faixa y 300 a 420, onde a borda da cabeça é curta.
- Gente ao fundo: manter só o maior componente conexo da máscara (P22). Conferir 17,4 s, 19,4 s, 26,8 s e 33,9 s (F30).

### P9. Pipeline e tempo de render

- Ferramentas existentes: Playwright em /opt/node-tools/node_modules/playwright, ffmpeg 6.1.1, numpy 2.5.3, rembg só no venv scratchpad/cbenv, faster-whisper só em scratchpad/fw com o modelo small em scratchpad/fwmodels [FATO, find nesta rodada].
- Risco: base.mp4, mask.mp4, raw.mp4 e os rn_*.wav estão só no scratchpad, que é da sessão. Só o voz_master.wav tem cópia no repositório (cmp idêntico). O original do upload continua em /root/.claude/uploads. Se a sessão cair, a segmentação de 589,4 s (F27) se repete.
- Tempo: A cerca de 951 s, B cerca de 887 s, C de 1008 a 1319 s, em série 47 a 53 min (DR08, F4). Minha correção: [ESTIMATIVA] de 70 a 110 min com QA e um re-render parcial (47 a 53 x 1,5 a 2,0). O fator é PRIOR, porque nenhum render foi cronometrado do início ao fim (B13). O C sem rembg pode cair abaixo da estimativa da F4 se a composição for só overlay do ffmpeg (0,071 s por quadro, F26). Isso é hipótese até o teste de 300 quadros.
- Não rodar em paralelo (F28).

### P10. CTA

Usa o gravado (32,00 a 35,92 s). Na tela: "Comenta: DENTISTA". Sem TABULEIRO: só entra com 150 ou mais de alcance em 48 h, e no comentário fixado, não no vídeo (06-plano-final.md linhas 56 e 181). "Eu te respondo" é promessa do Bruno: resposta à mão em até 2 h nas primeiras 48 h [HIPÓTESE de prazo].

### P11. Conformidade com a publicidade odontológica

A Res. 196/2019 foi lida no texto oficial pela F3 (F72). O que entra e o que não entra na tela nos 3 modelos:
- Sem boca, dente real, raio X, instrumental, cadeira odontológica desenhada com detalhe, procedimento, antes e depois, preço, "grátis", sorteio, faturamento ou agenda prometida (F72, F73).
- A fala "o mesmo diagnóstico e a mesma conclusão" (11,38 a 13,32 s) não ganha ilustração clínica. Ela vira uma grade de posts genéricos. Diagnóstico e conclusão são palavras da própria Res. 196/2019, e imagem clínica ali chama exatamente o que ela regula.
- Nenhum ícone de dente. P11 (ícone estilizado é seguro) é palpite, e trocar por ampulheta e grade custa zero.
- Sem coin no SFX (som de dinheiro ao lado de "segundo produto" pode ser lido como mercantilização, F72) [HIPÓTESE].
- O art. 45 do Código de Ética (F73) alcança o dentista que repostar ou aparecer. Nenhum dentista aparece. Vale para as respostas: não prometer curso pronto nem número de alunos.

### P12. Prova e Tzur

**Não entra na tela em nenhum modelo.** Motivos: o Bruno não disse (F10); a autorização em vídeo é bloqueante e não confirmada (06-plano-final.md linha 272); "6 para 20 milhões por mês" ao lado de "sua técnica vira um segundo produto" vira leitura de promessa de resultado (CLAUDE.md; F73 art. 35 V). Também sai do ov2.html a prova social inventada ("1.287 comentários" e 8 @ fictícios, linha 77 do ov2.html) [FATO, grep nesta rodada].

### P13. Métrica, fonte, data e critério de parar

| Métrica | Fonte | Leitura | Critério |
|---|---|---|---|
| Conversa qualificada de dentista (métrica principal, 06-plano-final.md linha 77) | comentários e DMs, ig_comments e ig_inbox (Buzzfy, leitura) e planilha de leads | 31/10 (48 h) e 05/11 (7 dias) | 0 conversa com alcance de 106 ou mais: TESTAR o CTA, não o formato |
| Alcance, views, tempo assistido, pulo | ig_post_stats (Buzzfy) | 31/10 e 05/11 | Alcance menor que 53 em 48 h: o modelo publicado não se repete no próximo nicho. Alcance de 106 ou mais e pulo abaixo de 68%: sucesso pela D2 e D3. Pulo abaixo de 60%: sucesso também pelo 06-plano-final.md |
| Disparo de automação | listCommentAutomationLogs (PostZen) | D+1 (30/10) | Só se o TABULEIRO for ligado com 150 ou mais |
| Áudio | ffmpeg ebur128 no MP4 final | antes de entregar, até 23/10 | Fora de -15 a -13 LUFS ou TP acima de -1,0: não entrega |
| Máscara do A | QA quadro a quadro: letreiro sobre olhos ou boca e 2º componente | antes de 27/10 | Qualquer falha não consertada: publica o C |

Corte de pulo (C1): esta cadeira usa 68% como critério formal deste reel, porque é a mediana medida (F12). O 60% é marcado como meta esticada. Assim um 64% conta como sucesso aqui e como parcial no plano dos nichos, e os dois ficam registrados.

### P14. Regras de texto

Todos os textos de tela das tabelas acima estão em PT-BR, sem travessão e sem emoji. A única estrutura de contraste é a falada: "deixa de disputar paciente e passa a formar quem disputa". Nenhum letreiro cria outra. Sem HighClass, Júnior Prazeres ou Felipe Roser.

---

## 3. Decisões

### D1 · Áudio

| Opção | 1ª ordem | 2ª ordem | Premissas |
|---|---|---|---|
| 1. voz_master como está | Zero trabalho | TP -0,3 no AAC (medido), "forna" na legenda automática, consoante perdida nos 3 vídeos | Que ninguém note. Falsa para TP |
| 2. Remasterizar do voz_master (limitador, EQ, trilha) | Corrige o TP | Herda a perda de "formar" e de "técnica"; EQ de presença não devolve consoante removida | Que o voz_master seja a melhor base. O reconhecimento diz que não (0,850 contra 0,878) |
| 3. Refazer do raw com redução mais leve, escolhida por ouvido e reconhecimento, TP -1,5 antes do AAC (minha posição) | Voz mais inteligível, TP dentro | Os 3 vídeos herdam o mesmo áudio bom; os tempos da legenda mudam no trecho de 24,94 a 29,04 s | Que a redução mais leve ainda tire o fundo do coworking o bastante para o ouvido do Bruno |
| 4. Fora do óbvio: pedir ao Bruno o arquivo original do celular (sem WhatsApp) e masterizar dele | Áudio de taxa maior que 59,8 kb/s, menos artefato antes de tratar | Também resolve a ampliação do vídeo e a máscara (P8). Custa 1 mensagem e pode atrasar 1 dia | Que o original exista no celular. Sem dado |
| 5. Regravar só o trecho de 24,94 a 29,04 s | Resolve a dúvida da fala | Dublagem fora de sincronia com a boca; a P4 mostra que a fala estava certa | Que a fala esteja errada. A medição diz que não |

**Posição: 3, com a 4 tentada em paralelo e sem esperar por ela.**
Probabilidade de sucesso pelo critério do enquadramento: com o critério de 40 dB literal, 0,10, faixa de 0,05 a 0,20 (nenhuma versão passa de 16,3 dB pela DR02). Com o critério trocado como proponho na P7, 0,65, faixa de 0,45 a 0,80.
Confiança: 0,6.

### D2 · Modelo A

| Opção | 1ª ordem | 2ª ordem | Premissas |
|---|---|---|---|
| 1. Tzur v2 fiel (manifesto P&B, letreiro, b-roll, reacts, bloco final) | Mais "AE", mais horas | Bloco final de cerca de 10 s sem rosto e com prova inventada; vídeo passa de 36 s; confete e aplauso soam falsos para dentista | Que mais efeito retenha mais. Sem dado (F19, F60) |
| 2. Tzur v2 enxuto corrigido (minha posição: tabela A01 a A21) | Letreiro em 8 momentos, rosto em 97,4% | Exige corrigir comp.py (faixa y 300 a 420, sem corte em 470, maior componente) | Que a máscara de 360x640 aguente a faixa y 300 a 420 sem halo visível |
| 3. Tzur v2 fiel com legenda palavra a palavra | Mais leitura | Tela carregada: letreiro, legenda, cartões e reacts ao mesmo tempo | Que mais texto ajude. F53 só diz "texto no quadro 0" |
| 4. Fora do óbvio: A sem rembg, letreiro só acima da cabeça (y 120 a 300), sem oclusão | Zero risco de máscara | Perde o "4D atrás", que é o pedido literal do Bruno | Que o efeito de profundidade não importe para o Bruno. Falsa pelo pedido |
| 5. Fora do óbvio: A com máscara só nas 8 janelas do letreiro (cerca de 15 s) | Menos quadro para QA | Mesmo custo de segmentação, já pago (mask.mp4 pronto) | Que o QA de 15 s seja mais fácil. Verdade, e entra na opção 2 |

**Posição: 2, com o QA da opção 5 (só as janelas do letreiro).**
Probabilidade de produção (1080x1920, nenhuma palavra cortada, rosto de 0 a 3 s, letreiro nunca sobre olhos e boca, lista quadro a quadro): 0,75, faixa de 0,55 a 0,90.
Probabilidade de desempenho (alcance de 106 ou mais e pulo abaixo de 68% em 7 dias): 0,35, faixa de 0,20 a 0,50 [PRIOR].
Confiança: 0,5.

### D3 · Modelos B e C

| Opção | 1ª ordem | 2ª ordem | Premissas |
|---|---|---|---|
| 1. B = sab8a com gdgtify; C = alex-prompter em 5 cenas com 000267 | C explica bem | Cenas do alex-prompter em tela cheia tiram o rosto (F13: animação sem rosto rende de 0,15x a 0,8x); a cena "prova" fica vazia | Que explicar ganhe de rosto. A conta diz o contrário |
| 2. B = tela dividida com reacts; C = tipografia cinética sobre o rosto (minha posição, tabelas B e C) | Cobre o pedido literal "dividindo com reacts" e dá um C sem dependência de máscara | B encolhe o rosto em 79% do vídeo; C é o reserva de publicação | Que rosto a 58% da altura ainda conte como "Bruno em cena". Sem dado |
| 3. Só B agora, C depois do primeiro resultado | Economiza cerca de 17 a 22 min de render (DR08) | Descumpre "faça outros 2"; o Bruno pediu 3 | Que o Bruno aceite 2. Contra o pedido |
| 4. Não fazer B e C | Economiza mais | Descumpre o pedido, e a Agência perde a cara de "modo god" | Nenhuma defensável |
| 5. Fora do óbvio: C = controle cru (rosto, título fixo da tese, legenda, zero efeito) | Mede se o acabamento AE importa | Contra o pedido "tudo profissional estilo AE"; o Bruno pode ler como preguiça | Que aprender valha mais que agradar. Fica como ideia, não como posição |

**Posição: 2, com B renderizado por último.**
Probabilidade de cumprir o critério de produção (ids citados, rosto de 0 a 3 s, sem banidos, 1080x1920, nenhuma palavra cortada, lista): 0,75, faixa de 0,55 a 0,85.
Probabilidade de o júri cego dar nota igual ou maior que a do A: C 0,50 (de 0,30 a 0,65); B 0,45 (de 0,25 a 0,60).
Probabilidade de desempenho, se um deles for publicado: C 0,35; B 0,25, faixa de 0,10 a 0,45 [PRIOR].
Confiança: 0,45.

---

## 4. Ideias e hipóteses numeradas

| # | Ideia ou hipótese | Confiança | Evidência |
|---|---|---|---|
| 1 | "forna que a gente" é artefato da redução de ruído; o Bruno disse "formar quem" | alta | b02_trecho.log: raw dá "formar" 0,99 e "quem" 0,91 |
| 2 | O voz_master perde inteligibilidade contra o raw | média | Confiança média de reconhecimento de 0,850 contra 0,878; reconhecimento é proxy, não ouvido |
| 3 | Masterizar a partir do raw, não do voz_master | alta | Ideias 1 e 2 |
| 4 | Misturar 70% processado com 30% seco pode devolver consoante | baixa | PRIOR; testar pelo reconhecimento do trecho |
| 5 | Pedir o arquivo original do celular | alta | Upload WhatsApp, 1,31 Mb/s de vídeo e 59,8 kb/s de áudio (ffprobe) |
| 6 | O original resolve ampliação e máscara ao mesmo tempo | média | F23, F31; depende de existir |
| 7 | Limitar em -1,5 dBFS antes do AAC | alta | tp_aac_teste.log: -1,5 fica -1,5; -1,0 vira -0,9 |
| 8 | Medir loudness no MP4 final, nunca no WAV | alta | dentista-audio-masterizado.mp4 mede -0,3 dBTP contra -0,5 do WAV |
| 9 | O critério de 40 dB derruba a D1 por régua | alta | DR02: máximo de 16,3 dB entre as versões |
| 10 | Trocar o critério de ruído por ouvido mais não piorar os 16,0 dB do voz_master | média | DR02; P01 |
| 11 | "técnica" (29,56 a 29,76 s) sai "tênka" nas 5 versões | alta | inteligibilidade_K.log; palavra de 0,20 s |
| 12 | A legenda escreve "técnica" mesmo assim | alta | Sentido da frase; o roteiro tem "técnica" |
| 13 | Conferir "Qual é esse?" (20,10 a 20,64 s) no ouvido | média | 3 de 5 versões leem "esse" (inteligibilidade_K.log) |
| 14 | Se houver "esse", a legenda inclui; nunca apagar palavra dita | alta | Regra de não cortar fala |
| 15 | Os tempos do trecho de 24,94 a 29,04 s vêm do alinhamento do raw | média | b02_trecho.log; words-raw.json tem palavras de 0,04 s ali (F08) |
| 16 | Tirar mk[:470]=0 do comp.py | alta | F29: a pessoa passa de y=470 em 71,6% dos quadros |
| 17 | Letreiro de trás na faixa y 300 a 420 | alta | ocupacao_mask.log: p90 de 29%, máximo de 52,4% |
| 18 | Letreiro na faixa do Tzur (y 440 a 580) teria a cabeça cobrindo de 27% a 49% em mediana | alta | ocupacao_mask.log, faixas 400 a 500 e 500 a 600 |
| 19 | Letreiro largo, de borda a borda, para a parte coberta pela cabeça não esconder o número | média | Ideia 18; leitura do 4D depende de oclusão parcial |
| 20 | "474" fica fora do centro, de modo que a cabeça cubra "MIL" e não os dígitos | média | Rosto no centro (frames-amostra.jpg) |
| 21 | Manter só o maior componente conexo da máscara | média | F30, P22 |
| 22 | Erosão de 1 a 2 px e borda de 3 px na máscara | média | Máscara de 360x640 ampliada 3x (ffprobe) |
| 23 | QA só nas janelas do letreiro (cerca de 15 s) | alta | Tabela A; reduz o QA a cerca de 40% do vídeo [ESTIMATIVA] |
| 24 | Se o QA do A falhar até 27/10, publicar o C | alta | C não usa máscara |
| 25 | Cortar o bloco final cinematográfico do Tzur | alta | F32, F34: prova inventada e 9,75 s sem rosto |
| 26 | Cortar confete, aplausos, RGB split e tremida | alta | F32, F48 |
| 27 | Trocar ♥ ✓ ✕ por SVG desenhado por traço | alta | F32; regra sem emoji |
| 28 | Não pôr o Tzur na tela | alta | F10; 06-plano-final.md linha 272 |
| 29 | Sem @ fictício em react de comentário | alta | ov2.html linha 77 (grep) |
| 30 | Não cortar pausas | média | P10 é PRIOR; cortar desalinha o trecho incerto |
| 31 | Usar a pausa de 0,60 s (19,50 a 20,10) como quietude | alta | DR05; gdgtify (F47) |
| 32 | Trilha a -40 dB na quietude | média | F47 pede quietude real |
| 33 | Punch-in máximo de 1,08 | média | DR06; F46 |
| 34 | Não chegar a 1,25x | média | Ganho só PRIOR (F62), perda de nitidez certa (DR06) |
| 35 | Corrigir "em Brasil" para "no Brasil" | alta | F09; diferença de boca mínima |
| 36 | Escrever "+474 MIL" e não 474.659 no letreiro | alta | C2; B19 |
| 37 | Rodapé "Fonte: CFO, out/2026" | alta | F68 |
| 38 | Contador em 474.659 só no B, com rodapé | média | F68 |
| 39 | Nenhum ícone de dente | alta | P11 é palpite; trocar custa zero |
| 40 | "diagnóstico" e "conclusão" ilustrados com grade de posts, não com imagem clínica | alta | F72 |
| 41 | Sem coin no SFX | média | F72 (mercantilização); HIPÓTESE de leitura |
| 42 | Sem SFX nas transições do cartão além de 1 swipe | baixa | C4: fontes divergem |
| 43 | SFX de 18 a 24 dB abaixo da voz | média | P03 |
| 44 | Trilha própria (som.py) | alta | Zero risco de direito autoral |
| 45 | Não rodar os 3 renders em paralelo | alta | F28 |
| 46 | Ordem de render: A, C, B | média | Valor de publicação e risco |
| 47 | Render de teste de 300 quadros antes do cheio | alta | B13 |
| 48 | Tempo real de 70 a 110 min para os 3 | baixa | DR08 x 1,5 a 2,0 [PRIOR] |
| 49 | Copiar base.mp4 e mask.mp4 para fora do scratchpad assim que houver pasta autorizada | média | Só o voz_master tem cópia no repositório (cmp) |
| 50 | Seed fixa no lugar de Math.random | alta | F32: render não determinístico |
| 51 | comp.py tem de falhar em PNG faltante | alta | F33 |
| 52 | Constantes de duração lidas do áudio, não fixas em 54,2 s | alta | F34 |
| 53 | Publicar só 1 modelo em 29/10 | alta | P15; D4 sem dado |
| 54 | B e C ficam para outro nicho ou trial reel | média | B23 sem dado |
| 55 | Resposta manual ao CTA em até 2 h nas primeiras 48 h | média | 12 comentários em 30 dias (00-SISTEMA.md) |
| 56 | Planilha de leads desde o primeiro comentário | alta | 06-plano-final.md linha 222 |
| 57 | Não ligar TABULEIRO abaixo de 150 | alta | CLAUDE.md |
| 58 | O gargalo da conta é conversa, não acabamento | média | 7 cliques e 0 vendas em 30 dias (00-SISTEMA.md) |
| 59 | O B encolhe o rosto e pode render menos que o A | baixa | F13 só mede tela cheia; sem dado de tela dividida |
| 60 | Título fixo da tese no quadro 0 ajuda o C | baixa | F55 (N = 10, rating qualitativo) |
| 61 | Rótulos de capítulo 1 a 5 no C dão sensação de progresso | baixa | alex-prompter (F49); PRIOR |
| 62 | Retirar a batida "prova" do alex-prompter | alta | Não há prova dita (F10) |
| 63 | Motion blur de 3 subquadros só nas entradas | média | F48; DR07 |
| 64 | Alfa pré-multiplicado se houver tmix em RGBA | média | B16 não testado |
| 65 | Comparar A, B e C por júri cego mede acabamento, não conversão | alta | P17 |
| 66 | N = 1 não separa formato de dia | alta | 00-enquadramento D3 |
| 67 | Usar 68% como corte formal de pulo e 60% como meta esticada | média | C1; F12 |
| 68 | Alcance menor que 53 em 48 h: não repetir o modelo | média | 06-plano-final.md linha 255 |
| 69 | A frase "sua técnica vira um segundo produto" fica só na fala, sem número ao lado | média | CLAUDE.md, sem promessa de resultado |
| 70 | Nenhum letreiro com "curso" ou "faturamento" | média | F73 art. 35 V; F76 |
| 71 | Gente passando ao fundo pode ser identificável; não pôr letreiro preso a ela | baixa | F30; frames-amostra.jpg |
| 72 | Duração de 36 s é aceitável, embora a mediana dos top seja 82,5 s | média | C6; o nosso bruto não tem mais fala |
| 73 | Não esticar o vídeo com bloco final sem fala | média | Ideia 72 mais F13 |
| 74 | O Bruno pode mandar refazer o áudio por gosto, não por medida | média | B04; nenhum histórico de aprovação |
| 75 | Entregar ao Bruno um trecho de 10 s de áudio antes dos renders | alta | Barato e evita 3 re-renders |
| 76 | A versão leve (2,55 Mb/s) não é a publicada; subir a de taxa alta | média | F25; o Instagram recomprime |
| 77 | Camiseta "PIXEL" e o "R" da parede não precisam de tratamento | baixa | Marca de roupa e decoração; HIPÓTESE de risco baixo |
| 78 | Verba zero: nenhum impulsionamento para salvar o reel | alta | F18 |
| 79 | Se o original do celular vier, refazer a segmentação (cerca de 10 min) | média | F27: 589,4 s para 1093 quadros |
| 80 | Não pôr legenda e letreiro com o mesmo texto ao mesmo tempo no A | baixa | Tela carregada; PRIOR |

---

## 5. Pre-mortem: como o meu plano fracassa

1. **O portão de áudio vira gargalo.** Eu exijo ouvido e reconhecimento antes dos renders; o Bruno demora a ouvir e os 3 vídeos atrasam para depois de 29/10. Antídoto: o áudio sai até 22/10 com prazo de 24 h. Sem resposta, segue a versão com melhor reconhecimento.
2. **A redução mais leve deixa o coworking audível.** O Bruno pediu "tire ruído e fundo". Uma voz mais limpa de consoante e com mais fundo pode ser reprovada. Antídoto: entregar 2 versões de 10 s (leve e forte) e deixar o Bruno escolher.
3. **O original do celular não existe ou chega tarde.** Antídoto: nada espera por ele.
4. **A faixa y 300 a 420 fica alta demais e o letreiro parece "em cima" e não "atrás".** O 4D pedido some. Antídoto: o letreiro desce até y 460 só nas palavras curtas, com QA de oclusão.
5. **O C vira reserva e nunca é publicado, e o B nunca sai do arquivo.** O Bruno sente que pagou por 3 e usou 1. Antídoto: avisar desde já que B e C são para os próximos nichos ou trial reel.
6. **Minha cautela com CFO tira força visual.** Sem dente, sem cadeira, sem número grande de faturamento, o vídeo pode parecer genérico. Antídoto: a força vem do 474 MIL, do contraste falado e do rosto, que são os elementos com dado.
7. **O reconhecimento automático me enganou.** "formar" a 0,99 pode ser viés do modelo para uma frase plausível. Antídoto: 2 minutos de ouvido (B02) antes de travar a legenda.
8. **O formato não importa e o reel fica abaixo de 53.** O nicho estreito repete os 78 a 494 views de terceiros (06-plano-final.md linha 29). Nenhum dos 3 modelos salva. Antídoto: o critério de parar está escrito e o próximo passo é hook, não efeito.
9. **O Bruno não responde aos comentários a tempo.** A métrica principal (conversa qualificada) fica em 0 com alcance bom. Antídoto: lembrete e planilha, decisão do Bruno.
10. **Erro de tempo na lista quadro a quadro**, porque words-raw.json veio do voz_master e eu troquei a base de áudio. Antídoto: realinhar as 79 palavras no áudio novo antes do render e regerar os quadros.

---

## 6. Previsões numéricas com data de conferência

Referência: publicação de 1 modelo em qui 29/10/2026. D+30 = 20/11/2026; D+60 = 20/12/2026; D+90 = 19/01/2027. Todas [PRIOR] salvo indicação.

| # | Métrica | Valor previsto | Conferência |
|---|---|---|---|
| 1 | Os 3 MP4 finais com TP até -1,0 dBTP e entre -15 e -13 LUFS (ebur128) | 3 de 3, probabilidade 0,9 [ESTIMATIVA a partir de tp_aac_teste.log] | 23/10/2026 |
| 2 | Bruno pede para refazer o áudio pelo menos 1 vez | probabilidade 0,35 | 23/10/2026 |
| 3 | O QA do A acha pelo menos 1 quadro com letreiro sobre olho ou boca antes do conserto | probabilidade 0,5 | 27/10/2026 |
| 4 | Tempo real de render dos 3, somado | 70 a 110 min, ponto de 85 min | no render |
| 5 | Alcance do reel em 7 dias (ig_post_stats) | ponto de 85, faixa de 40 a 200 | 05/11/2026, reconferido em D+30 (20/11) |
| 6 | Pulo do reel em 7 dias | ponto de 68%, faixa de 58% a 76% | 05/11/2026 |
| 7 | Alcance de 106 ou mais e pulo abaixo de 68% | probabilidade 0,35 | 05/11/2026 |
| 8 | Comentários "dentista" no reel | ponto de 2, faixa de 0 a 6 | D+30, 20/11/2026 |
| 9 | Conversas qualificadas de dentista | ponto de 0, faixa de 0 a 2; probabilidade de pelo menos 1 = 0,35 | D+30, 20/11/2026 |
| 10 | Pelo menos 1 diagnóstico de 30 min agendado com dentista | probabilidade 0,15 | D+60, 20/12/2026 |
| 11 | Pelo menos 1 venda vinda do nicho dentista | probabilidade 0,03 | D+90, 19/01/2027 |
| 12 | Mais de 1 dos 3 modelos publicado | probabilidade 0,5 | D+30, 20/11/2026 |
| 13 | O modelo publicado em 29/10 é o A | probabilidade 0,6 (C: 0,3; B: 0,1) | 29/10/2026 |
| 14 | O modelo do reel do dentista é reusado em pelo menos 1 outro nicho | probabilidade 0,5 | D+60, 20/12/2026 |
| 15 | Alguma notificação ou denúncia de conselho ligada ao reel | probabilidade 0,01 | D+90, 19/01/2027 |

---

## 7. O que mudaria minha opinião

- **Ouvido do Bruno ou de outra cadeira diz "forna que a gente"** no raw: a legenda volta a ser fiel e a regravação do trecho entra como opção.
- **O original do celular chega em 1080p ou mais:** refazer base e máscara. O teto de zoom pode subir para 1,15.
- **O QA do A passa limpo de primeira:** cai o peso do C como reserva, e o A fica com 0,8 de chance de ser o publicado.
- **Métricas do case Tzur v2 (B06) com pulo abaixo de 55%:** subo a probabilidade de desempenho do A para 0,45.
- **A conta tem trial reels (B23):** o B sai do arquivo e vira teste em não seguidores na mesma semana.
- **Uma redução leve que mantém "formar" e tira o fundo no ouvido:** a D1 sobe para 0,8.
- **Dado de terceiros mostrando que tela dividida em talking head de negócio retém igual à tela cheia:** o B sobe para principal empatado.

### Lacunas

- Não ouvi o áudio. As afirmações sobre "formar", "técnica" e "esse" vêm de reconhecimento automático (faster-whisper small, int8, uma rodada por configuração), que é proxy do ouvido.
- A ocupação da máscara foi medida em 1 a cada 3 quadros (365 de 1093) e numa máscara de 360x640 ampliada. Ainda é preciso medir a borda real em 1080x1920.
- O teste de TP usou só alimiter e AAC de 192 kb/s. A recompressão do próprio Instagram é sem dado.
- Nenhum render foi cronometrado do início ao fim (B13).
- Desempenho de qualquer dos 3 formatos na conta: sem dado (F19).
- Se a conta tem trial reels: sem dado (B23).
- Se a tabela do CFO conta pessoas ou inscrições: sem dado (B19).
- Se o Bruno é inscrito em CRO: sem dado (B20).
- Se o arquivo original do celular ainda existe: sem dado.

### Fontes

- Arquivos do cliente: /home/user/Disparo-/CLAUDE.md; conteudo/sistema-instagram/00-SISTEMA.md (linhas 15 a 40); conteudo/modo-god-nichos/run/06-plano-final.md (linhas 29, 31, 56, 77, 139, 155, 161, 179 a 184, 222, 255, 272); videos/cases/tzur/comp.py (linhas 4, 14 e 17), cap2.js (linha 7), ov2.html (linha 77).
- Conselho: videos/nichos/dentista/god/contexto.md, run/00-enquadramento.md, run/01-fatos.md (F01 a F76, C1 a C10, B01 a B25, DR01 a DR20, P01 a P22), run/01-pesquisa/F1 a F4 (via resumo da tarefa e do livro de fatos).
- Medições desta cadeira, 21/10/2026, em run/02-cadeiras/evidencias-K/: b02_trecho.py e b02_trecho.log (2ª transcrição do trecho); inteligibilidade_K.py e inteligibilidade_K.log (5 versões contra o roteiro); tp_aac_teste.log (limitador e AAC); ocupacao_mask.py e ocupacao_mask.log (ocupação da pessoa por faixa de altura).
- ffprobe e ffmpeg nesta rodada: upload original (/root/.claude/uploads/.../79e29878-WhatsApp_Video_2026-10-21_at_13.08.15.mp4: h264 576x1024 a 1,31 Mb/s, AAC 44,1 kHz a 59,8 kb/s); videos/nichos/dentista/dentista-audio-masterizado.mp4 (-14,2 LUFS, -0,3 dBTP); videos/nichos/dentista/voz_master.wav (-14,2 LUFS, -0,5 dBTP, idêntico ao do scratchpad por cmp); scratchpad/dent/mask.mp4 (360x640, 1093 quadros, 30 fps).
- Ferramentas localizadas por find: /opt/node-tools/node_modules/playwright; scratchpad/cbenv (rembg); scratchpad/fw e scratchpad/fwmodels (faster-whisper small).
