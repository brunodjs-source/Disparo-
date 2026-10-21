> **Conselho de instâncias do mesmo modelo é autocrítica estruturada, não verificação independente. Concordância unânime pode refletir viés comum. Este documento reduz risco e explicita premissas; não garante resultado.**

# Plano final · Reel do dentista · 3 modelos de edição · O Estrategista

Data: 21/10/2026. Presidente do conselho Agência Reunida. Fontes: run/01-fatos.md, run/01-pesquisa/F1 a F4, run/02-cadeiras/plano-A a plano-N, run/03-julgamento, run/05-debates. Volume de ideias do conselho não prova nada.

Pesos fixos usados em todas as decisões: impacto 25, probabilidade 20, evidência 20, custo e reversibilidade 15, tempo até o primeiro sinal 10, risco 10.

Linha do tempo única para os 3 modelos: 36,43 s, 1093 quadros a 30 fps, sem cortar nenhuma pausa [FATO, words-raw.json e F4; 14 de 14 cadeiras]. Quadro = segundo x 30.

---

## 1. Resumo executivo

| Modelo | Formato | Hipótese de conversão que testa | Vai ao feed |
|---|---|---|---|
| A (o que já fazemos) | Tzur v2 enxuto: P&B que vira cor no 474, letreiro 3D atrás da cabeça em 5 momentos, legenda palavra a palavra, 1 b-roll desenhado, CTA digitado | [HIPÓTESE] Bruno em tela cheia quase o tempo todo, com o efeito pedido, mantém o padrão medido da conta (reels com o Bruno falando de 2,4x a 5,8x a mediana, CLAUDE.md; 3 de 3 reels recentes do Bruno acima de 106 com pulo abaixo de 68%, plano-D, ig_post_stats 21/10/2026) | 29/10 |
| B (novo) | Tela dividida: tela cheia de 0 a 3 s, depois painel de 1080x800 em cima com animação da fala e o Bruno em 1080x1120 embaixo, voltando à tela cheia em "Qual é?" e no CTA | [HIPÓTESE] Mostrar o mecanismo da oferta (da cadeira para a aula) e ler sem som aumenta respostas qualificadas no direct e segura o pulo mesmo com o rosto menor | Direct na semana de 29/10; feed no slot seguinte se A passar o corte de D+3 |
| C (novo) | Prédio de palavras: as palavras ditas sobem e viram estrutura atrás da cabeça na faixa y 300 a 400, quietude de 0,60 s antes de "Qual é?" | [HIPÓTESE] Tipografia arquitetônica como criativo pago 4:5 converte o dentista que já compra atenção no feed (1.432 resultados ativos da busca por palavra-chave "curso para dentistas", que inclui anúncios de outros temas, Meta Ad Library 21/10/2026, leitura única, evidencias-B/meta-ad-library-2026-10-21.md; reler antes de 18/11) | Não vai ao feed em outubro. Anúncio 4:5 só depois de 18/11, só com teto escrito pelo Bruno e depois de checar a política de anúncios da Meta sobre ganho financeiro e oportunidade de negócio (sem dado hoje) |

Por que estes três: A é o único formato com base medida na conta. B é o único que atende ao pé da letra o pedido "dividindo tela com reacts e animações". C é o formato com menor dependência de máscara fina e serve de molde para anúncio e para os outros nichos. Nenhum dado da conta compara os três formatos entre si (F66); a escolha da ordem é desenho de teste, não prova de qual formato é melhor.

Força da evidência geral: forte nas medições técnicas (áudio, máscara, tempos de render por quadro, número do CFO); fraca em tudo que é desempenho no Instagram (N = 1 por formato, mediana recente de 34 [ESTIMATIVA, plano-D] contra 53 do 00-SISTEMA).

---

## 2. Os três modelos

### Regras comuns aos 3 (consenso de 14 de 14 ou quase)
- Bruno em cena do quadro 0 ao 90 em tela cheia.
- comp.py corrigido antes de qualquer render: sai `mk[:470]=0` (a pessoa passa de y=470 em 71,6% dos quadros, F4), fica só o maior componente conexo da máscara (44 quadros com gente ao fundo), o script falha se faltar PNG, Math.random com semente fixa.
- Banidos (twoclipping-000267): shockwave, partículas, confete, RGB split, camera shake, tremida, lens flare, neon, piso de grade, fundo piscando, easing elástico. Sai inteiro o bloco final do ov2.html com prova inventada ("1.287 comentários", 8 @ fictícios, chuva de R$, glifos de coração).
- Lista branca de imagem (Res. CFO 196/2019 e CEO art. 44, lidos no texto oficial, F3): sem boca, dente realista, raio X, cadeira odontológica, instrumental, antes e depois, preço, "grátis", promessa de faturamento ou agenda, caso de terceiro. Tzur fora da tela.
- Zoom máximo 1,10x (a fonte já está ampliada 1,875x, F4). Punch-in de 1,00 a 1,08 em geral.
- SFX iniciando pelo pico medido: whoosh começa 268,5 ms antes do evento, riser 1596,6 ms antes, swipe 137,1 ms antes, pop e tick no próprio quadro [FATO F4].
- Trilha a zero e nada se move na quietude de 19,50 a 20,10 s.
- Checklist T01 a T12 e grep de strings (travessão, emoji, nomes vetados, R$, grátis) antes de cada render (plano-G).
- Render em série, nunca em paralelo (paralelo 2 a 5 vezes mais lento, F4). Render de 300 quadros cronometrado antes do cheio.

### 2.1 Modelo A · Tzur v2 enxuto

**Conceito.** O pipeline que já roda (seg.py, ov2.html, cap2.js, comp.py, add_music.sh), sem o que é banido ou inventado. O rosto do Bruno fica em tela cheia cerca de 95% do tempo [ESTIMATIVA: 1 b-roll de 1,70 s em 36,43 s].

**Referências do repositório.** sab8a-475686 (contrato mínimo de talking head punchy com legenda), techhalla-498547 (mola por letra e punch-in de 1,0 a 1,08; descarta RGB split e paleta), twoclipping-000267 (banidos, SFX por pico, loudnorm -14). Letreiro atrás da pessoa vem do nosso pipeline, não do repositório (zero prompts citam rembg, F1).

**Paleta e tipografia.** Preto #141210 e ouro #E8B36A da Série 2; letreiro em Cinzel com extrusão falsa de 14 text-shadow e rotateX 55° (cap2.js atual); legenda em sans bold branca com palavra ativa em ouro, 2 a 4 palavras por vez.

**Faixa do letreiro.** y 300 a 400, onde a máscara tem ocupação mediana de 0% e p90 de 29% [FATO evidencias-K/ocupacao_mask.log]. Reserva sem máscara: y 120 a 220, livre medido.

| # | Tempo (s) | Quadros | Rosto e fundo | Letreiro 3D atrás | Texto na tela | React ou animação | B-roll | Transição | SFX | Música |
|---|---|---|---|---|---|---|---|---|---|---|
| A01 | 0,00 a 2,08 | 0 a 62 | Bruno em P&B, punch-in 1,00 para 1,04 | nenhum | título fixo "Dentista: sua técnica pode virar um 2º produto?" no topo seguro + legenda "Dentistas, são mais de" | nenhum | não | corte seco no quadro 0 | nenhum | trilha entra a -30 LUFS |
| A02 | 2,08 a 3,80 | 62 a 114 | cor volta no "474" em 6 quadros | "+474 MIL" sobe de trás da cabeça, repousa em y 300 a 400 | rodapé "Dentistas ativos. Soma dos CROs no site do CFO, 21/10/2026" de 2,08 a 6,26 s | contador rolando de 0 a 474 | não | máscara de tipo revela o número | riser com pico em 2,08 s; tick em 3,18 | ducking 8 dB |
| A03 | 3,80 a 5,16 | 114 a 155 | tela cheia | 474 MIL permanece | legenda "colegas ativos no Brasil" (corrigido de "em Brasil") | nenhum | não | nenhum | nenhum | trilha |
| A04 | 5,48 a 8,80 | 164 a 264 | punch-in 1,00 para 1,08 em "hora" | "HORA DE CADEIRA" sobe em 7,68 s | legenda palavra a palavra | relógio SVG traço (não cadeira) desenhado no canto inferior | não | nenhum | pop em 7,68 | trilha |
| A05 | 9,36 a 10,24 | 281 a 307 | tela cheia | sai HORA DE CADEIRA | legenda | nenhum | não | swipe de saída | swipe com pico em 10,24 | trilha |
| A06 | 10,24 a 11,94 | 307 a 358 | rosto sai | nenhum | 3 cards cinza iguais "DIAGNÓSTICO / CONCLUSÃO" sem imagem clínica | cards duplicam em grade | b-roll desenhado (não foto) | corte com 0,30 s de respiro antes do retorno | whoosh com pico em 10,24 | trilha |
| A07 | 11,94 a 13,32 | 358 a 400 | rosto volta, 1,04 | nenhum | legenda "e a mesma conclusão." | cards encolhem para o canto e somem | não | corte | tick em 12,66 | trilha |
| A08 | 13,84 a 17,92 | 415 a 538 | tela cheia, 1,00 para 1,06 | "SUA TÉCNICA" sobe em 15,08 s | legenda | nenhum | não | nenhum | pop em 15,08 | trilha |
| A09 | 17,92 a 19,50 | 538 a 585 | tela cheia | troca para "UM MERCADO" em 18,90 s | legenda "existe um mercado." | nenhum | não | nenhum | tick em 19,12 | trilha |
| A10 | 19,50 a 20,10 | 585 a 603 | rosto parado, 1,06 | UM MERCADO parado | nada se move | nenhum | não | quietude | silêncio | trilha a zero |
| A11 | 20,10 a 22,22 | 603 a 667 | punch-in 1,00 para 1,08 em "ensinar" | "ENSINAR O SEU COLEGA" atravessa atrás da cabeça e repousa | legenda | nenhum | não | nenhum | whoosh com pico em 20,64 | trilha volta em 20,64 |
| A12 | 22,70 a 24,24 | 681 a 727 | tela cheia | sai letreiro | rótulo fixo "Eu desenho o seu lançamento" de 22,70 a 31,58 s + terço inferior "Bruno · Estrategista de Lançamento" de 22,70 a 25,70 | nenhum | não | nenhum | ding_si em 22,82 | trilha |
| A13 | 24,46 a 29,04 | 734 a 871 | tela cheia | "DE DISPUTAR PACIENTE" riscado em 25,42, depois "PARA FORMAR QUEM DISPUTA" em 27,24 | legenda corrigida "você deixa de disputar paciente e passa a formar quem disputa" (condicionada à escuta B02, ver seção 3) | risco animado por traço | não | nenhum | pop em 27,24 | trilha |
| A14 | 29,28 a 31,58 | 878 a 947 | punch-in até 1,08 em "segundo" | "2º PRODUTO" sobe e pousa | legenda | nenhum | não | nenhum | pop em 30,78 | trilha |
| A15 | 31,58 a 32,00 | 947 a 960 | tela cheia | 2º PRODUTO permanece | nenhum novo | nenhum | não | nenhum | nenhum | trilha |
| A16 | 32,00 a 35,92 | 960 a 1078 | tela cheia, letterbox leve de 60 px | "DENTISTA" em y 300 a 400 | CTA digitado "Qual é a sua profissão? Comenta aqui" + legenda da fala | cursor digitando | não | nenhum | typing do início do CTA, pico 302,2 ms | trilha sobe 2 dB |
| A17 | 35,92 a 36,43 | 1078 a 1092 | tela cheia | DENTISTA | "@o_estrategista.com.br" | nenhum | não | fade 6 quadros | nenhum | trilha sai |

### 2.2 Modelo B · Tela dividida

**Conceito.** O vídeo encena a tese: o painel de cima desenha o que o Bruno diz, o Bruno fica sempre visível embaixo. Tela cheia em 0 a 3,18 s, em "Qual é? Ensinar o seu colega" e no CTA. Rosto visível 100% do tempo, em tela cheia cerca de 28% [ESTIMATIVA: 0 a 3,18 + 19,50 a 22,22 + 32,00 a 36,43 = 10,33 s; 10,33 / 36,43 = 28,4%; o trecho de "Qual é?" já está na soma].

**Referências do repositório.** sab8a-475686 (talking head punchy), twoclipping-000267 (banidos, loudnorm, SFX por pico), stokebuilder-356793 (rosto entre gráficos, adaptado de PiP para divisão horizontal, proíbe inventar número), gdgtify-929495 (seek(t) determinístico e quietude). Cenas do painel vêm da Série 2 (count, cross, cta) em JPEG por pipe (0,077 a 0,080 s por quadro, F4).

**Paleta e tipografia.** Painel em #141210 com traço ouro #E8B36A; títulos em Cinzel, apoio em Playfair itálico. Bruno embaixo sem nova ampliação, recorte seguindo o centro da máscara.

**Reacts.** O debate D3 tirou os reacts desenhados livres. O presidente mantém uma forma restrita, porque o pedido do Bruno nomeia reacts: no máximo 3 stickers vetoriais da lista branca (seta, círculo de destaque, relógio), nunca emoji, nunca glifo de coração, check ou xis, nunca contador ou @. Ver divergência na D3.

| # | Tempo (s) | Quadros | Rosto e fundo | Letreiro 3D atrás | Painel de cima / texto | React ou animação | B-roll | Transição | SFX | Música |
|---|---|---|---|---|---|---|---|---|---|---|
| B01 | 0,00 a 3,18 | 0 a 95 | Bruno em tela cheia, cor | "+474 MIL" em y 300 a 400 a partir de 2,08 | legenda + rodapé "Soma dos CROs no site do CFO, 21/10/2026" | nenhum | não | nenhum | riser com pico em 2,08 | trilha -30 LUFS |
| B02 | 3,18 a 5,16 | 95 a 155 | Bruno desce para 1080x1120 | sai | painel: 474 pontos (1 ponto = 1.000 dentistas) acendem em grade 2D | pontos acendem por traço | não | divisão desliza de cima, 8 quadros | swipe com pico em 3,18 | trilha |
| B03 | 5,48 a 8,80 | 164 a 264 | janela de baixo | nenhum | painel: relógio SVG, ponteiro gira; texto "SÓ HORA DE CADEIRA" | relógio | não | corte | tick em 7,68 | trilha |
| B04 | 9,36 a 13,32 | 281 a 400 | janela de baixo | nenhum | painel: grade de cards cinza iguais "DIAGNÓSTICO" e "CONCLUSÃO" se repetindo | cards copiam um ao outro | não | nenhum | pop em 11,38 e 12,66 | trilha |
| B05 | 13,84 a 17,92 | 415 a 538 | janela de baixo | nenhum | painel: "SUA TÉCNICA" e seta para uma plateia de pontos | seta vetorial (react 1) | não | máscara de tipo | pop em 15,08 | trilha |
| B06 | 17,92 a 19,50 | 538 a 585 | janela de baixo | nenhum | painel: "UM MERCADO" | círculo de destaque (react 2) | não | nenhum | tick em 19,12 | trilha |
| B07 | 19,50 a 20,10 | 585 a 603 | Bruno volta à tela cheia | nenhum | nada se move | nenhum | não | quietude | silêncio | trilha a zero |
| B08 | 20,10 a 22,22 | 603 a 667 | tela cheia, 1,00 para 1,08 | "ENSINAR O SEU COLEGA" atrás da cabeça | legenda | nenhum | não | nenhum | whoosh com pico em 20,64 | trilha volta |
| B09 | 22,70 a 24,24 | 681 a 727 | volta à janela de baixo | nenhum | painel: planta de lançamento desenhada a traço; "EU DESENHO O SEU LANÇAMENTO" + "Bruno · Estrategista de Lançamento" | traço desenhando | não | divisão desliza | swipe com pico em 22,70 | trilha |
| B10 | 24,46 a 29,04 | 734 a 871 | janela de baixo | nenhum | painel: "DISPUTAR PACIENTE" riscado, depois "FORMAR QUEM DISPUTA" (sala de aula em pontos) | risco animado | não | nenhum | pop em 27,24 | trilha |
| B11 | 29,28 a 31,58 | 878 a 947 | janela de baixo | nenhum | painel: dois blocos "1º SERVIÇO" e "2º PRODUTO" | seta (react 3) | não | nenhum | pop em 30,78 | trilha |
| B12 | 32,00 a 36,43 | 960 a 1092 | tela cheia | "DENTISTA" em y 300 a 400 | CTA digitado "Qual é a sua profissão? Comenta aqui" + "@o_estrategista.com.br" | cursor | não | divisão sobe e some | typing | trilha sai em fade |

Legenda palavra a palavra corre na emenda entre painel e janela em todo o trecho dividido.

### 2.3 Modelo C · Prédio de palavras

**Conceito.** As palavras ditas sobem de trás da cabeça e viram estrutura: HORA DE CADEIRA é o térreo, SUA TÉCNICA a viga, UM MERCADO a coluna, 2º PRODUTO pousa no topo. Só palavras faladas. Rosto em tela cheia 100% do tempo, zoom até 1,08. Exportado em 9:16 e em 4:5 (texto entre y 285 e 1635).

**Referências do repositório.** gdgtify-929495 (palavras viram arquitetura, seek(t), quietude), twoclipping-000267 (banidos, motion blur de 3 subquadros só nas janelas de movimento, SFX por pico). alex-prompter-997524 fica fora: exige prova e 3 passos que a fala não tem (debate D3). twoclipping-041659 (órbita atrás da cabeça) fica como opção só em ENSINAR, se o render de 300 quadros couber no portão.

**Paleta e tipografia.** Preto e ouro; palavras em Cinzel com sombra que as assenta no plano; legenda mínima em sans branca só onde não há palavra-estrutura.

| # | Tempo (s) | Quadros | Rosto e fundo | Palavra-estrutura atrás | Texto na tela | Animação | Transição | SFX | Música |
|---|---|---|---|---|---|---|---|---|---|
| C01 | 0,00 a 3,80 | 0 a 114 | tela cheia | "+474 MIL" como fundação larga | título fixo "Dentista: sua técnica pode virar um 2º produto?" + rodapé CFO | blocos sobem com mola por letra | nenhum | riser com pico em 2,08 | trilha |
| C02 | 5,48 a 8,80 | 164 a 264 | tela cheia | "HORA DE CADEIRA" vira térreo | legenda | tijolo assenta | nenhum | pop em 7,68 | trilha |
| C03 | 9,36 a 13,32 | 281 a 400 | tela cheia | "O MESMO" repetido em andares iguais | legenda | andares clonados | nenhum | tick em 11,14 | trilha |
| C04 | 13,84 a 19,50 | 415 a 585 | tela cheia | "SUA TÉCNICA" viga; "UM MERCADO" coluna | legenda | blur de 3 subquadros só na subida | nenhum | pop em 15,08 e 18,90 | trilha |
| C05 | 19,50 a 20,10 | 585 a 603 | tela cheia | estrutura parada | nada | quietude | nenhum | silêncio | zero |
| C06 | 20,10 a 22,22 | 603 a 667 | tela cheia, até 1,08 | "ENSINAR O SEU COLEGA" atravessa atrás da cabeça | legenda | máscara de tipo de 12 quadros | match cut | whoosh com pico em 20,64 | volta |
| C07 | 22,70 a 29,04 | 681 a 871 | tela cheia | "EU DESENHO" vira planta a traço; "FORMAR QUEM DISPUTA" | terço inferior "Bruno · Estrategista de Lançamento" | traço | nenhum | ding_si em 22,82 | trilha |
| C08 | 29,28 a 31,58 | 878 a 947 | tela cheia | "2º PRODUTO" pousa no topo | legenda | pouso amortecido | nenhum | pop em 30,78 | trilha |
| C09 | 32,00 a 36,43 | 960 a 1092 | tela cheia | prédio fica | CTA digitado "Qual é a sua profissão? Comenta aqui" + @ | cursor | fade final | typing | sai |

---

## 3. Mudanças de texto na tela exigidas pelo CFO e pela checagem do 474 mil

1. Escrever "+474 mil" ou "474 MIL", nunca 474.659 nem "474 mil pessoas". A soma das 27 linhas por CRO deu 474.659 em 21/10/2026 16:40 UTC e outra leitura do mesmo dia deu 474.640 [FATO F3, evidencias-F3/cfo-ativos-por-cro-2026-10-21.csv]; a página não traz total nacional e pode contar inscrição duplicada.
2. Rodapé obrigatório junto do número, por pelo menos 4,2 s: "Dentistas ativos. Soma dos CROs no site do CFO, 21/10/2026". O CFO não publica total nacional; o número é soma nossa e variou no mesmo dia (474.659 e 474.640).
3. Legenda "em Brasil" vira "no Brasil".
4. Trecho 24,94 a 29,04 s: o ASR no raw lê "passa a formar quem disputa" com 0,91 a 0,99 em três cadeiras (E, G, K); no voz_master sai "forçar" (0,45) ou "forna". Legenda corrigida para "você deixa de disputar paciente e passa a formar quem disputa" só depois da escuta do Bruno (B02). Se o áudio final ainda soar "forçar" para o ouvinte leigo, a legenda some de 27,24 a 29,04 s e o letreiro "FORMAR QUEM DISPUTA" carrega a ideia, sem pôr na tela palavra que a boca não diz.
5. Sem imagem clínica: o trecho 9,36 a 13,32 s ("diagnóstico e conclusão") vira cards cinza sem foto (Res. CFO 196/2019; CEO art. 44 I e XII, F3).
6. Sem preço, "grátis", promessa de faturamento ou de agenda, "melhor técnica", Tzur, antes e depois, som de moeda.
7. [HIPÓTESE] Nome e número de inscrição no terço inferior só se aplicam se o Bruno for cirurgião-dentista inscrito em CRO: CEO art. 43 e Res. 196 art. 4º obrigam quem anuncia serviço odontológico, e o Bruno vende lançamento. Perguntar até 23/10 se ele é dentista. A fala diz "colegas", o que sugere que é; se não for, rever o "colegas" (regravar ou trocar a legenda por "dentistas ativos").

---

## 4. Legenda do post e CTA

CTA na tela nos três: "Qual é a sua profissão? Comenta aqui". Motivos: (1) a fala gravada diz "comenta a sua profissão aqui", e a tela acompanha a fala; (2) a regra do cliente é uma palavra-chave por mês (TABULEIRO), só em post com 150 ou mais de alcance (CLAUDE.md; 00-SISTEMA.md), e a previsão central do A é abaixo disso, então DENTISTA não entra como palavra-chave; (3) plano-G cita o Instagram dizendo, em 2024, que não recomenda post que pede comentário com palavra específica [FATO nível 3, Social Media Today, 02/06 e 05/06/2024, citado em plano-G; fonte oficial do Instagram não anexada]. A palavra DENTISTA só volta como CTA se o Bruno revogar a regra por escrito. TABULEIRO fica fora pelo mesmo corte de 150.

**Modelo A (feed)**
> Dentista, o Brasil tem mais de 474 mil dentistas ativos (soma dos CROs no site do CFO, 21/10/2026). Quanto do seu faturamento ainda é só hora de cadeira?
> Se você domina uma técnica que outros dentistas querem aprender, existe um mercado: ensinar o seu colega. Eu desenho e comando o lançamento com você.
> Qual é a sua profissão? Comenta aqui que eu te respondo.

**Modelo B (direct e feed seguinte)**
> Da cadeira para a aula. Você atende paciente; a técnica que você domina pode virar um segundo produto, vendido para quem disputa o mesmo paciente.
> Dentistas ativos, soma dos CROs no site do CFO em 21/10/2026: +474 mil.
> Qual é a sua profissão? Comenta aqui e eu te mostro como seria o seu lançamento.

**Modelo C (anúncio 4:5 depois de 18/11)**
> Para dentista que já domina uma técnica: ela pode virar um segundo produto.
> Eu desenho o seu lançamento e comando com você.
> Chama no direct.

Uma única frase "não é X, é Y" por peça: a fala já tem "deixa de disputar paciente e passa a formar quem disputa", então nenhuma legenda acrescenta outra construção desse tipo.

---

## 5. Ordem de publicação e métrica de decisão em 48 h

- 29/10: A no feed, às 12h (posts próprios às 12h: 4 posts, média 62 de alcance; seguidores online: 405 às 12h e 425 às 18h, pico; diferença de 5% [FATO ig_best_times 21/10/2026, plano-L linha 150]). Bruno responde à mão em até 60 min nas 3 primeiras horas.
- 29/10 a 31/10: A e B no direct, 10 envios por braço, mesmo canal, mesmo horário, mesma lista, planilha pareada. A lista é só de quem já interagiu com a conta (comentou, respondeu story ou mandou DM antes); a origem de cada contato é registrada na planilha. Nada de DM fria (risco LGPD e limite de envio do Instagram). Envio feito pelo Bruno, nunca por agente. Isso escolhe só o texto de abertura da DM (10 por braço dá sinal, não prova).
- Slot seguinte do feed: B, uma vez, se o A passar o corte de 48 h abaixo.
- C: só render de 300 quadros em outubro; anúncio depois de 18/11.

**Métrica de decisão em 48 h (ig_post_stats, conferência em 31/10/2026 12h):** linha de base é a mediana recente de 34 de alcance [ESTIMATIVA, plano-D: mediana dos 18 reels de 30/09 a 20/10] e não 53, porque a regra de parada com 53 mataria um reel na média atual (J4).
- Passa: alcance em 48 h de 68 ou mais (2x 34) e pulo abaixo de 68%. B ocupa o slot seguinte.
- Zona cinza: alcance de 34 a 67 ou pulo entre 68% e 77%. B vai ao feed só se o direct der diferença de 2 ou mais respostas qualificadas a favor do B.
- Falha: alcance abaixo de 34 ou pulo acima de 77% (teto de pulo dos reels de animação, CLAUDE.md). B não vai ao feed; próximo reel testa o CTA de pergunta aberta como variável única.
- Conflito registrado: 60% de pulo aparece como meta forte (plano-A, plano-M). Fica como linha de dobrar, não de parar.

---

## 6. Riscos técnicos e plano B

| Risco | Evidência | Plano B |
|---|---|---|
| Halo da máscara rembg (320x320 interno, mask.mp4 em 360x640) no cabelo | F4; plano-H | Stills dos quadros 95, 640 e 805 para o Bruno até 23/10. Halo em 2 de 3 stills: letreiro vai para y 120 a 220 sem máscara |
| Letreiro por cima da cabeça | 71,6% dos quadros acima de y=470 | Tirar o corte fixo; faixa y 300 a 400 medida |
| Gente ao fundo entra na máscara | 44 quadros | Só o maior componente conexo |
| comp.py pula PNG faltante em silêncio | F4 | Falhar alto; contar 1093 PNG por camada |
| Render mais lento que o previsto | nenhum render cronometrado (B13) | 300 quadros do A contra portão de 452 s [ESTIMATIVA: 226 a 261 s para 300 quadros; 0,752 s por quadro x 300 = 226 s (plano-L) e 951 s / 1093 x 300 = 261 s (F4); portão = 226 x 2]; acima disso a composição vai para o overlay do ffmpeg (0,071 s por quadro medido) |
| Colisão com o consórcio de 27/10 no mesmo pipeline | plano-C | Ordem fixa: áudio 22/10, A 23/10, B 26/10, C só amostra 27/10; congelar 28/10 18h. Dependências do Bruno com data limite e padrão se ele não responder: escuta cega do áudio até 23/10 12h (sem resposta: fica o voz_master); 3 stills até 23/10 18h (sem resposta: letreiro na faixa y 120 a 220 sem máscara); se é dentista inscrito em CRO até 23/10 (sem resposta: sem nome e inscrição na tela e legenda "dentistas ativos" no lugar de "colegas"); original do celular até 24/10 (sem resposta: usa o bruto do WhatsApp); pausa da regra CASE até 28/10 18h (sem resposta: não publica, ver linha abaixo) |
| True peak sobe no AAC | -1,0 vira -0,9; -1,5 vira -1,3 a -1,5 [FATO evidencias-J, evidencias-K] | Alvo de processo -1,5; aceite -1,0 no MP4 |
| Bruto veio pelo WhatsApp (1,31 Mb/s vídeo, 59,8 kb/s áudio) | plano-K | Pedir hoje o original do celular, sem esperar por ele |
| Regra CASE do PostZen reage a "caso" e manda DM sobre Tzur com "sete para oito dígitos" | plano-L, PostZen 21/10/2026 | Portão de publicação: o A não vai ao feed enquanto a regra CASE estiver ativa, porque a DM fala da Tzur e de "sete para oito dígitos" (promessa de resultado e caso de terceiro, vetados no CLAUDE.md). Bruno pausa a CASE ou exclui dentista, dentistas e profissão das 6 regras gerais até 28/10 18h. Agente não altera |
| Origem o=ig-dentista não é lida pela página | plano-A M5 | Anotar à mão na planilha até corrigir |
| Bruno não reconhece o A enxuto como "o que já fazemos" | aberto | Volta a abertura P&B com aplausos, sem confete nem prova inventada |

---

## 7. Decisões

### D1. Áudio masterizado dos 3 vídeos

**Recomendação.** Uma voz única para os 3. Padrão provisório: remasterizar o voz_master (highpass 80 Hz, de-esser, EQ de presença, expansor híbrido por transcrição ou energia, nunca gate só por alinhamento) com loudnorm em duas passadas I -14 e TP -1,5 antes do AAC. A cadeia_E (a partir do raw) entra se vencer a regra fechada do debate: WER contra o roteiro até 0,086; nivelamento dentro de 0,5 LU; escuta cega do Bruno em 24,94 a 29,04 s e nas pausas de 13,37 e 31,63 s; ouvinte leigo transcreve o trecho e desempata; MP4 de amostra com música em -1,0 dBTP ou menos. Empate fica o voz_master. Trilha e SFX por modelo, medidos com ebur128 em cada MP4 final.

**Onde concorda.** 12 de 14 limitam em -1,5 antes do AAC e aceitam só no MP4 final. Premissa: dois testes independentes (evidencias-J/teste_tp_aac.log, evidencias-K/tp_aac_teste.log) mostram o AAC subindo o pico 0,1 a 0,2 dB. 14 de 14 concordam que o corte de 40 dB nas pausas é PRIOR e inalcançável pelo método do DR02, porque mede cauda de palavra e respiração (pausas reais já a 39 a 49 dB abaixo, plano-A M3 e M4).

**Onde diverge.** Origem: voz_master (maioria, votos 7 na opção 2) contra raw (5 na opção 3: E, G, K). Resolve: a escuta cega mais o ouvinte leigo, abaixo de 1 hora. Também diverge o substituto dos 40 dB (25, 28, 30, 35 dB, -45 dBFS). Presidente fixa: piso no miolo das pausas (excluindo 50 ms de borda) abaixo de -45 dBFS e não pior que o voz_master atual, mais aprovação no ouvido do Bruno.

**Minoria vencedora parcial.** A minoria do raw (E, G, K) traz o argumento mais forte sobre a frase-tese: "forçar" sob legenda "formar" é erro visível justamente na frase que diferencia o Bruno (J5). Por isso a escuta é portão obrigatório e não opcional. Não vence por inteiro porque a cadeia_E não tem WER medido e o WER geral de raw e voz_master é igual (0,086).

**L e N reprovados na configuração:** TP -1,0 no loudnorm termina em -0,9 depois do AAC.

- Primeira ação: rodar WER da cadeia_E e medir os dois m4a; montar o par cego.
- Dono: agência (técnico de áudio); escuta: Bruno.
- Prazo: 2 dias (até 23/10/2026).
- Dado que mudaria: WER da cadeia_E acima de 0,086; ouvinte leigo escrevendo "forçar" no voz_master; chiado audível nas pausas da cadeia_E.
- Critério de abandono: se em 23/10/2026 nenhuma das duas versões fechar TP de -1,0 ou menos no MP4 com música, ou o Bruno reprovar ambas, refazer a partir do original do celular ou regravar a tomada inteira na sessão de 26/10.
- Teste mais barato: escuta cega de 10 min mais 5 min do ouvinte leigo, custo zero.
- Previsão: 3 de 3 MP4 finais entre -15 e -13 LUFS e TP de -1,0 ou menos, com aprovação escrita na primeira rodada. Probabilidade 0,6 [faixa 0,4 a 0,75] [PRIOR], conferência 23/10/2026.
- Força da evidência: alta para loudness e true peak (medido duas vezes); média para inteligibilidade (ASR, não ouvido humano); nula para gosto do Bruno.

### D2. Modelo A no pipeline do case Tzur v2

**Recomendação.** Tzur v2 enxuto (opção 2), conforme a tabela 2.1: P&B só até o 474, 5 a 6 letreiros 3D atrás na faixa y 300 a 400, legenda palavra a palavra, 1 b-roll desenhado, relógio SVG, sem manifesto com confete, aplausos, tremida, RGB split e prova inventada. Portões: comp.py corrigido, 300 quadros contra 452 s, 3 stills aprovados, depois render cheio. Duas perguntas fixas na DM (qual técnica e se já ensina) e coluna de lead qualificado na planilha. Título que filtra comprador não entra em 29/10.

**Onde concorda.** 12 de 14 votos na opção 2 (share 0,86). Premissa: o Tzur v2 fiel traz itens banidos ou inventados e o critério "letreiro nunca cobre olhos e boca" favorece o enxuto; e o formato Bruno em tela cheia é o único com base na conta (3 de 3 acima de 106). Atenção: o Tzur v2 nunca foi publicado (plano-E, plano-L), então "o que já fazemos" tem zero dado de desempenho próprio; a base é o Bruno em cena, não o efeito.

**Onde diverge.** 2 votos na opção 4 (com camada de conversão ou sistema de marca). Resolve: a fração de comprador nas DMs em D+7; abaixo de 20%, o título que filtra entra como teste isolado. Faixa do letreiro: A propunha y 330 a 600, onde a pessoa cobre 49,2% em y 500 a 600; vence K, a única cadeira que mediu ocupação.

**Minoria vencedora.** K na faixa do letreiro (medição contra palpite). I e B no filtro de comprador como métrica de DM, não de tela, porque duas variáveis no mesmo post não deixam ler a causa.

- Primeira ação: corrigir o comp.py e renderizar 300 quadros cronometrados.
- Dono: agência (editor de pipeline); aprovação de stills: Bruno.
- Prazo: render cheio até 23/10/2026; publicação 29/10/2026.
- Dado que mudaria: halo em 2 de 3 stills (letreiro vai para y 120 a 220 sem máscara); render de 300 quadros acima de 452 s (composição no ffmpeg); Bruno não reconhecer o modelo.
- Critério de abandono: se em 05/11/2026 o alcance for abaixo de 34 e o pulo acima de 77%, o formato A enxuto sai do nicho dentista e o próximo reel testa outra variável.
- Teste mais barato: 300 quadros (226 a 261 s de máquina [ESTIMATIVA, plano-L e F4]) mais 2 min do Bruno nos stills, até 23/10.
- Previsão: alcance em 7 dias de 106 ou mais com pulo abaixo de 68%. A meta de 106 não é 2x 53: é o corte que só 4 de 18 reels da janela atingiram (307, 168, 165, 126) e que 3 de 3 reels do Bruno falando passaram com pulo abaixo de 68% [FATO, plano-D seção 0, ig_post_stats 21/10/2026]; contra a mediana de 34 equivale a cerca de 3x [ESTIMATIVA: 106 / 34]. Valor central 95 de alcance [faixa 40 a 250] [PRIOR]. Probabilidade de bater 106 e pulo abaixo de 68%: 0,40 [faixa 0,20 a 0,60] [ESTIMATIVA, plano-D: 3 de 3 reels do Bruno e 3 de 18 de todos, com desconto de nicho não medido]. Conferência 05/11/2026 por ig_post_stats. Comentários esperados: entre 0,5 e 0,8, menos de 1 [ESTIMATIVA: 95 x 0,49/100 = 0,47 e 95 x 0,84/100 = 0,80; 0,49 = 6 comentários / 1.230 de alcance nos 18 reels, plano-D; 0,84 = 5 / 598 nos reels com o Bruno, plano-L].
- Força da evidência: alta para a execução técnica (máscara, ocupação, tempos por quadro medidos); fraca para desempenho (N = 1, mediana recente de 34 abaixo da usada na meta).

### D3. Formatos novos para B e C

**Recomendação.** Opção 2 com o conteúdo do debate: B = tela dividida (sab8a-475686, twoclipping-000267, stokebuilder-356793 adaptado, seek(t) da gdgtify-929495), tela cheia de 0 a 3,18 s, em "Qual é?" e no CTA. C = prédio de palavras (gdgtify-929495 com twoclipping-000267) na faixa y 300 a 400, sem alex-prompter-997524. B vai ao direct na semana de 29/10 e ao feed no slot seguinte pela regra da seção 5. C só como amostra de 300 quadros em outubro e anúncio 4:5 depois de 18/11 com teto escrito.

**Onde concorda.** 13 de 14 na opção 2 (share 0,93). Premissa: só um modelo por vez no feed, porque os três repetem a mesma fala de 36 s; e B é o único que atende o pedido literal de tela dividida.

**Onde diverge.** Qual vai ao feed primeiro: A (7 cadeiras), tela dividida (C, F, I) ou tipografia (B, E, G, N). Resolve: o corte de 48 h do A e o direct pareado. Reacts: o debate retirou os reacts desenhados; o presidente mantém 3 stickers vetoriais de lista branca no B porque o pedido do Bruno nomeia reacts e o risco de imitar prova social vem de contador e @, que ficam proibidos. Regra única para o B ir ao feed (a da seção 5): se o A passar o corte de 48 h, o B vai sem esperar o direct; na zona cinza, só com diferença de 2 ou mais respostas qualificadas a favor do B no direct; na falha, não vai.

**Minoria vencedora.** H e J em descartar alex-prompter-997524: pede prova e 3 passos que a fala não tem, e a cena de prova puxaria o case Tzur sem autorização. Argumento melhor porque toca regra do cliente, não gosto.

- Primeira ação: consultar ig_post_stats dos 3 reels do Bruno (pulo e retenção no segundo 5) e montar a planilha pareada.
- Dono: agência (montagem e planilha); envios no direct: Bruno (agente nenhum manda mensagem).
- Prazo: render do B até 26/10/2026; amostra do C até 27/10/2026.
- Dado que mudaria: render do C projetado acima de 60 min (sai de outubro); pulo do B no feed acima de 77% (B volta só para direct); Res. CFO ou Ad Library contrárias (C não roda como anúncio).
- Critério de abandono: se em 05/11/2026 o B no feed tiver alcance abaixo de 34 ou pulo acima de 77%, a tela dividida sai do feed do nicho e fica só como peça de direct.
- Teste mais barato: consulta Buzzfy de 5 min, planilha de 10 min, 20 envios em cerca de 30 min do Bruno, 300 quadros do C em 277 a 362 s de máquina, mais a mistura dos subquadros em numpy (sem dado) [ESTIMATIVA: 1008 a 1319 s / 1093 x 300, F4].
- Previsão: júri cego de 3 cadeiras dá ao B e ao C nota de acabamento igual ou maior que a do A com probabilidade 0,35 [faixa 0,15 a 0,55] [PRIOR], conferência 28/10/2026. Se o B for ao feed: alcance em 7 dias valor central 70 [faixa 25 a 200] [PRIOR], probabilidade de 106 ou mais e pulo abaixo de 68% de 0,3 [PRIOR], conferência 07/11/2026 (se publicado em 31/10) ou 7 dias após a publicação.
- Força da evidência: fraca. Zero dado da conta para tela dividida ou tipografia; o acervo tem só 3 prompts de talking head e nenhum de split screen ou react (F1); fontes de edição são fornecedores de ferramenta (F2).

---

## 8. O que continua aberto
- Escuta do trecho 24,94 a 29,04 s e das pausas de 13,37 e 31,63 s (B02, B03).
- Qual cadeia gerou o voz_master.
- Se a tabela do CFO conta pessoas ou inscrições; se o Bruno é inscrito em CRO.
- Primeiro render cronometrado de cada modelo.
- Métricas do Tzur v2: não existem, ele nunca foi publicado.

---

## Registro de verificação (corretor, 21/10/2026)

**Corrigido**
1. D2, comentários esperados: com alcance central de 95 a conta dá 0,47 a 0,80; agora "entre 0,5 e 0,8, menos de 1" [ESTIMATIVA], com as somas (6/1.230 do plano-D; 5/598 do plano-L).
2. Meta de 106 contra linha de base 34: 106 justificado como o corte que 4 de 18 reels atingiram (plano-D seção 0), não como 2x 53.
3. Mediana de 34 etiquetada [ESTIMATIVA, plano-D] nas seções 1 e 5.
4. 2.2, tela cheia do B: 10,33 / 36,43 = 28,4%; agora "cerca de 28%" (o trecho de "Qual é?" já estava na soma). Item repetido na lista, aplicado uma vez.
5. D3, 300 quadros do C: "cerca de 15 min" não tinha conta; agora 277 a 362 s mais a mistura em numpy (sem dado), por F4 (1008 a 1319 s / 1093 x 300).
6. Seção 6 e D2, 300 quadros do A: faixa 226 a 261 s (plano-L 0,752 s por quadro; F4 951 s / 1093 x 300).
7. D2, probabilidade 0,38 sem conta: trocada pela do plano-D (0,40, faixa 0,20 a 0,60, linha 295); valor central 95 marcado [PRIOR], pois não aparece no plano-D.
8. D3, alcance central 70, probabilidade 0,3 e júri 0,35: marcados [PRIOR].
9. D1, probabilidade 0,6: marcada [PRIOR].
10. Cabeçalho, "1137 ideias": o número só aparece em 07-redteam.md e 07-verificacao/V1.md, que o citam a partir do plano; sem contagem de origem. Número removido.
11 e 14. 1.432 da Meta Ad Library: reescrito como resultados da busca por palavra-chave, que inclui outros temas (o próprio arquivo de evidência diz que é teto), com data, leitura única e releitura antes de 18/11.
12. Item 7 da seção 3 (inscrição no CRO): marcado [HIPÓTESE]; as normas citadas obrigam quem anuncia serviço odontológico. Pergunta ao Bruno se é dentista até 23/10 e revisão do "colegas" se não for. Não abri os arquivos do CEO e da Res. 196 nesta rodada; a correção só rebaixa a afirmação, não depende deles.
13. Rodapé do 474 mil: "Soma dos CROs no site do CFO, 21/10/2026" em todas as telas e legendas; seção 3 explica que o total é soma nossa e variou no mesmo dia (474.659 e 474.640, já registrado no item 1 da seção 3).
15. Instagram 2024: fonte apontada (Social Media Today, 02/06 e 05/06/2024, nível 3, citada no plano-G linhas 24 e 132), com aviso de que a fonte oficial não está anexada.
16. Horário: números do ig_best_times postos (4 posts às 12h com média 62 de alcance; 405 seguidores online às 12h e 425 às 18h; plano-L linha 150).
17. Conta dos comentários por 100 de alcance mostrada (ver item 1).
18 e 19. CTA "Comenta: DENTISTA": trocado nos três modelos e nas legendas por "Qual é a sua profissão? Comenta aqui". Alinha a tela à fala gravada e cumpre a regra de uma palavra-chave por mês só com alcance de 150 ou mais. DENTISTA volta só se o Bruno revogar a regra por escrito. O letreiro "DENTISTA" atrás da cabeça fica, porque é rótulo e não palavra-chave de automação.
20. Contradição seção 5 e D3: fica a regra da seção 5 (zona cinza exige 2 respostas a mais no direct); D3 reescrita para apontar para ela.
21. D3: 31/10 + 7 dias = 07/11/2026; corrigido.
22. Lista do direct: só contatos que já interagiram, origem registrada, sem DM fria, envio pelo Bruno.
23. "E a maioria ainda vende só hora de cadeira": sem fonte; trocada por pergunta.
24. Regra CASE do PostZen: virou portão de publicação do A (DM cita Tzur e "sete para oito dígitos").
25. Dependências do Bruno: data limite e padrão para cada uma (escuta, stills, CRO, original do celular, regra CASE) na linha de colisão da seção 6.
27. C: "estrutura, não só agenda" cortado; a peça fica só com a construção da fala ("deixa de... e passa a...").
28. Política de anúncios da Meta sobre ganho financeiro: checagem antes de 18/11 incluída no resumo executivo como condição do anúncio 4:5.

**Rejeitado**
- 26, "Sua técnica vira um segundo produto" nos textos fixos: os textos fixos do plano já usam "pode virar" (título dos modelos A e C, legenda do B, legenda do C corrigida). "Vira" só existe na fala gravada, que a legenda palavra a palavra transcreve; trocar a legenda poria na tela palavra que a boca não diz (mesmo critério do item 4 da seção 3). Se o Bruno quiser tirar o "vira", é regravação. Sem mudança de texto.

---

## 9. Execução de amanhã (acrescentado pelo crítico de lacunas, passada 1, 21/10/2026)

### 9.1 Áudio: comandos (itens 1, 2 e 3 do pedido)
Pasta de trabalho: SCR=/tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/dent [FATO, contexto.md e listagem da pasta em 21/10/2026]. Ponto de partida: voz_master.wav, que mede -14,2 LUFS e true peak -0,5 dBTP [FATO F04]; o true peak precisa cair ao menos 0,5 dB [ESTIMATIVA DR01].

Passo 1, remaster da voz (cadeia da D1; valores de EQ e de-esser são [HIPÓTESE] a validar na escuta, nenhum foi medido):
```
ffmpeg -y -i $SCR/voz_master.wav -af "highpass=f=80,deesser=i=0.4,equalizer=f=3500:t=q:w=1.2:g=2,loudnorm=I=-14:TP=-1.5:LRA=7:print_format=json" -f null - 2> $SCR/ln1.log
# ler measured_I, measured_TP, measured_LRA, measured_thresh, target_offset do ln1.log e rodar a 2a passada:
ffmpeg -y -i $SCR/voz_master.wav -af "highpass=f=80,deesser=i=0.4,equalizer=f=3500:t=q:w=1.2:g=2,loudnorm=I=-14:TP=-1.5:LRA=7:measured_I=..:measured_TP=..:measured_LRA=..:measured_thresh=..:offset=..:linear=true" -ar 48000 $SCR/voz_v2.wav
```
O expansor por transcrição da D1 fica fora desta primeira versão: não há comando testado para ele (sem dado). Se a escuta apontar ruído nas pausas, aplicar só nas pausas do words-raw.json, com volume=-12dB entre as palavras e 50 ms de borda.

Passo 2, aceite: `ffmpeg -i $SCR/voz_v2.wav -af ebur128=peak=true -f null -` deve dar entre -15 e -13 LUFS e TP de -1,5 ou menos (critério D1). Escuta do Bruno nos trechos 24,94 a 29,04 s, 13,37 s e 31,63 s (B02, B03). Empate ou reprovação: fica o voz_master.

Passo 3, trilha: usar /home/user/Disparo-/videos/add_music.sh (ducking por sidechain, loudnorm I -14 TP -1,5, AAC 192k) [FATO, leitura do arquivo]. Ele faz loudnorm de uma passada [FATO F22]; por isso o aceite final é o ebur128 do MP4 (TP -1,0 ou menos, D1).

### 9.2 Trilha escolhida
O plano dizia só "trilha". Arquivos disponíveis em /home/user/Disparo-/videos/musicas: close-up (95 s), complicated (109 s), deep-urban (289 s), hazy-after-hours (127 s), hip-hop-02 (115 s), like-a-loop-machine (129 s), trap-electro-vibes (116 s), uplifting-bass (96 s) [FATO, ffprobe 21/10/2026]. Já usada em peça nossa: hazy-after-hours (videos/ads/a01-campinas/finalizar.sh) [FATO]. Decisão: hazy-after-hours nos 3 modelos, mesma trilha para que a trilha não seja variável do teste [HIPÓTESE: nenhum dado compara trilhas]. Início em 0 s. A quietude de 19,50 a 20,10 s exige volume=0 nesse trecho: acrescentar `volume=enable='between(t,19.5,20.1)':volume=0` na cadeia [mus] do add_music.sh numa cópia local, sem alterar o original.

### 9.3 Trechos sem linha nas tabelas
As tabelas 2.1, 2.2 e 2.3 pulam intervalos (por exemplo A: 5,16 a 5,48, 8,80 a 9,36, 13,32 a 13,84, 22,22 a 22,70, 29,04 a 29,28; B: 5,16 a 5,48, 8,80 a 9,36, 13,32 a 13,84, 22,22 a 22,70, 29,04 a 29,28, 31,58 a 32,00; C: 3,80 a 5,48, 8,80 a 9,36, 13,32 a 13,84, 22,22 a 22,70, 29,04 a 29,28, 31,58 a 32,00) [FATO, leitura das tabelas]. São as pausas do words-raw.json. Regra: no intervalo sem linha o quadro mantém o estado da linha anterior (rosto, letreiro, painel e zoom parados no último valor), sem SFX novo e sem legenda (a legenda some na pausa). Exceção: o swipe ou a divisão do B que começa na linha seguinte pode iniciar dentro do intervalo, pelo pico de F35.

### 9.4 Arquivos de saída e ordem
Pasta de saída: /home/user/Disparo-/videos/nichos/dentista/render/ (criar). Nomes: dentista-A-9x16.mp4, dentista-B-9x16.mp4, dentista-C-9x16.mp4, dentista-C-4x5.mp4, todos 1080x1920 a 30 fps, 1093 quadros, H.264 crf 18 (padrão do comp.py, F22), AAC 192k.
Ordem: (1) voz_v2.wav e escuta; (2) comp.py corrigido; (3) 300 quadros do A cronometrados contra 452 s; (4) A cheio; (5) add_music.sh; (6) ebur128 e ffprobe de cada MP4 (1093 quadros, 36,43 s); (7) B; (8) amostra C.
C em 4:5: `ffmpeg -i dentista-C-9x16.mp4 -vf "crop=1080:1350:0:285" -c:a copy dentista-C-4x5.mp4` (faixa y 285 a 1635 da seção 2.3). Verificar no still que a legenda e o @ caem dentro do recorte; se não, subir esses textos para y abaixo de 1600 só na versão 4:5.

## 10. Execução de amanhã, passada 2 (crítico de lacunas, 21/10/2026)

### 10.1 Arquivos de SFX e atraso de cada um (Modelo A)
O plano citava whoosh, riser, swipe, pop, tick, typing e ding_si sem dizer onde estão. Estão em /home/user/Disparo-/videos/nichos/dentista/sfx/ [FATO, listagem 21/10/2026], com durações por ffprobe: whoosh 0,55 s, riser 1,60 s, swipe 0,25 s, pop 0,12 s, tick 0,04 s, typing 0,60 s, ding_si 1,80 s. coin.wav está na pasta e fica proibido (som de moeda, seção 3 item 6). impact, sub e shutter não entram.
Atraso (adelay, ms) = tempo do evento menos a antecipação do pico [FATO F4 para whoosh 268,5, riser 1596,6 e swipe 137,1 ms; conta feita aqui]:

| Evento A | Arquivo | adelay (ms) |
|---|---|---|
| A02 riser, pico 2,08 | riser.wav | 483 |
| A02 tick 3,18 | tick.wav | 3180 |
| A04 pop 7,68 | pop.wav | 7680 |
| A05 swipe, pico 10,24 | swipe.wav | 10103 |
| A06 whoosh, pico 10,24 | whoosh.wav | 9972 |
| A07 tick 12,66 | tick.wav | 12660 |
| A08 pop 15,08 | pop.wav | 15080 |
| A09 tick 19,12 | tick.wav | 19120 |
| A11 whoosh, pico 20,64 | whoosh.wav | 20372 |
| A12 ding_si 22,82 | ding_si.wav | 22820 [HIPÓTESE: pico do ding_si não medido; tratado como no quadro] |
| A13 pop 27,24 | pop.wav | 27240 |
| A14 pop 30,78 | pop.wav | 30780 |
| A16 typing, pico 302,2 ms | typing.wav | 31698 [HIPÓTESE: leitura de que o pico deve cair em 32,00 s] |

B e C usam a mesma conta com os tempos das tabelas 2.2 e 2.3 (por exemplo swipe do B02 com pico 3,18 entra em 3043; whoosh do C06 em 20372). Mixagem: cada SFX com volume=0.5 (o mesmo do aplausos em comp.py [FATO, comp.py linha 8]; nível do SFX em si é [HIPÓTESE] a validar na escuta) e amix normalize=0 sobre voz_v2.wav, antes do add_music.sh. Nenhum SFX cai entre 19,50 e 20,10 s (conferido na lista).

### 10.2 comp.py: o que trocar além da correção da máscara
comp.py está preso ao Tzur [FATO, leitura de cases/tzur/comp.py linhas 4 a 9]: N=int(54.2*30)+1, entrada base.mov, mix de aplausos.wav com adelay 4280 e saída case_v2_sem_trilha.mp4. Para o dentista: copiar para /home/user/Disparo-/videos/nichos/dentista/a/comp.py e trocar N=1093, base.mov pelo upscale do raw.mp4 em 1080x1920, aplausos.wav pela mixagem de 10.1 e a saída por dentista-A-sem-trilha.mp4. Aplausos fora (o A enxuto tira o manifesto, D2). Depois roda o add_music.sh e o resultado vira dentista-A-9x16.mp4 da seção 9.4.

### 10.3 Fontes
Cinzel e Playfair itálico não estão instaladas no sistema (fc-list vazio para as duas [FATO, 21/10/2026]); ov2.html e serie2/modelo.html carregam por @font-face de /home/user/Disparo-/videos/ads/a01-campinas/fonts/ (cinzel-latin.woff2, playfair-italic-latin.woff2) [FATO]. Usar o mesmo caminho nos HTML de B e C. A legenda em "sans bold" não tem arquivo na pasta: usar a sans do Chromium do Playwright e conferir acentos (ã, ç, º) no still [HIPÓTESE: nenhum teste de acento feito].

### 10.4 Montagem da tela dividida do B
O plano dava os tamanhos (painel 1080x800 em cima, Bruno 1080x1120 embaixo) mas não o comando. Com o vídeo base já em 1080x1920 (base_A.mp4, mesmo upscale do A) e o painel renderizado em 1080x800 (painel_B.mp4, cenas count, cross e cta do serie2/modelo.html):
```
ffmpeg -i base_A.mp4 -i painel_B.mp4 -filter_complex "[0:v]crop=1080:1120:0:Y[b];[1:v][b]vstack=inputs=2[s]" -map "[s]" -an split.mp4
```
Y = linha de topo da janela do Bruno. Sem dado de onde fica o queixo no quadro de 1920; ponto de partida Y=400 [HIPÓTESE], conferido em still nos quadros 95, 640 e 805 (os mesmos da seção 6): olhos e boca inteiros dentro da janela. A troca entre split.mp4 e tela cheia (0 a 3,18; 19,50 a 22,22 com divisão já fora; 32,00 em diante) e a divisão deslizando em 8 quadros são feitas no compositor em numpy, quadro a quadro pela tabela 2.2, não por concat (concat cortaria a animação de 8 quadros).

### 10.5 Arquivo do Modelo C
Nenhum arquivo do C existe [FATO, listagem de videos/]. Criar /home/user/Disparo-/videos/nichos/dentista/c/predio.html a partir de serie2/modelo.html (render(t) e captura por Playwright), com seek(t) determinístico da gdgtify-929495 e a camada de trás mascarada pelo mesmo mask.mp4 do A. Saída em PNG com alfa, composta pelo comp.py de 10.2 com N=1093. Amostra de 300 quadros primeiro (D3).

## 11. Execução de amanhã, passada 3 (crítico de lacunas, 21/10/2026)

### 11.1 Base e máscara já existem: não refazer
Na pasta SCR já estão base.mp4 (1080x1920, 30 fps, 1093 quadros, só vídeo, sem faixa de áudio) e mask.mp4 (360x640, 30 fps, 1093 quadros) [FATO, ffprobe 21/10/2026]; o seg.log registra "1093 quadros 589.4 s" [FATO, SCR/seg.log]. O raw.mp4 já tem 1093 quadros [FATO, ffprobe]. Portanto o upscale da seção 10.2 e o seg.py não precisam rodar de novo: base_A.mp4 da seção 10.4 é SCR/base.mp4. Antes de usar, conferir o still do quadro 95 contra o raw (alinhamento de tempo) [HIPÓTESE: não se verificou que base.mp4 saiu do raw.mp4 atual].

### 11.2 comp.py: três linhas que a passada 2 não listou
Lendo cases/tzur/comp.py [FATO, linhas 5, 7 e 14]:
1. Linha 14: P&B até 4,28 s. Trocar para P&B até 2,08 s e cor voltando em 6 quadros (tabela 2.1, A02): `k=min(max((f/30-2.08)/0.2,0),1); g=img.mean(2,keepdims=True); img=g+(img-g)*(k*1.15)`. O 1,15 de saturação é o valor atual do Tzur [FATO, linha 15], não medido para este bruto.
2. Linha 7: o áudio vem de `-i base.mov` ([1:a]). base.mp4 não tem áudio [FATO, ffprobe], então a entrada 1 vira SCR/voz_v2.wav (ou a mixagem com SFX da 10.1), mapeada com `-map 1:a`.
3. Linha 5 e 7: base.mov vira SCR/base.mp4.

### 11.3 Letreiros e legenda do A: arquivo de dados pronto
cap2.js injeta edit.json no ov2.html e fixa a duração em 54,2 s [FATO, cap2.js linha 7]. ov2.html tem os letreiros do Tzur escritos no código (PABLO, 6 MESES, ESTRATÉGIA, FUNIL, PERSONA, O QUE MUDOU, A LIÇÃO) [FATO, ov2.html linhas 42 a 83].
- Criado /home/user/Disparo-/videos/nichos/dentista/god/a/edit.json: 1 corte (0 a 36,43 s, src bruno) e as 79 palavras com tempo de início do words-raw.json (voz_master.wav), com "em" de 4,80 s trocado por "no" (seção 3 item 3) [FATO, gerado nesta passada]. A palavra de 27,24 s sai como o ASR leu; trocar à mão para "formar" só depois da escuta B02 (seção 3 item 4).
- Copiar ov2.html e cap2.js para videos/nichos/dentista/a/. Em cap2.js trocar `Math.ceil(54.2*30)` por `1093`. Em ov2.html apagar os blocos de letreiro das linhas 42 a 83 e escrever os 7 letreiros da tabela 2.1 com os tempos dela: +474 MIL (2,08 a 5,16), HORA DE CADEIRA (7,68 a 10,24), SUA TÉCNICA (15,08 a 18,90), UM MERCADO (18,90 a 20,10, parado na quietude), ENSINAR O SEU COLEGA (20,64 a 22,22), DE DISPUTAR PACIENTE riscado (25,42) e PARA FORMAR QUEM DISPUTA (27,24 a 29,04), 2º PRODUTO (30,78 a 32,00), DENTISTA (32,00 a 36,43). O grafismo de gráfico com caminhos SVG do Tzur (linhas 50, 74 e 83) sai inteiro: não há número de resultado nesta fala.
- Ordem: `node cap2.js` com SHOTS dos quadros 95, 640 e 805 primeiro (o cap2.js já aceita lista de quadros e salva sh2_back e sh2_front [FATO, linha 6]); depois o render cheio de 1093 quadros por camada.

## 12. Execução de amanhã, passada 4 (crítico de lacunas, 21/10/2026)

### 12.1 Painel do B: o serie2/modelo.html não serve como está
A 10.4 manda renderizar painel_B.mp4 em 1080x800 com as cenas do serie2/modelo.html. Lido o arquivo [FATO, serie2/modelo.html linhas 4 a 12 e 37 a 60; serie2/capture.js]:
- A página é fixa em 1080x1920 com fundo claro #F6F1E8, e não #141210 como pede a 2.2; o palco fica no meio da página, a legenda (#cap) em y 960, o rótulo (#lab) em y 330 e a marca (#brand) em y 1440.
- O capture.js abre a página em 1080x1920, exige voz.wav na pasta e grava sem-trilha.mp4 com áudio.
- Tipos de cena que existem: count, cards, cross, big, duo, funnel, vs, cta. Não existem grade de 474 pontos, relógio SVG, planta a traço nem seta. O cards usa os glifos ✓ e ✕ nos tons ok e bad, vetados na 2.2; só o tom gold (→) pode ser usado.
- O cta digita TL.kw (palavra-chave); o B12 é tela cheia e não usa o painel.

O que fazer:
1. Criado /home/user/Disparo-/videos/nichos/dentista/god/b/timeline.json [FATO, gerado nesta passada]: 8 segmentos do painel (B02 a B06 e B09 a B11), tempos de início das palavras tirados do words-raw.json, só com tipos que existem: B02 count de 0 a +474 mil; B03 big "SÓ HORA / de cadeira"; B04 cards gold "Diagnóstico, Conclusão, Diagnóstico"; B05 big "SUA TÉCNICA"; B06 big "UM MERCADO"; B09 big "EU DESENHO SEU LANÇAMENTO / Bruno · Estrategista de Lançamento"; B10 cross "DISPUTAR PACIENTE" riscado e "FORMAR QUEM DISPUTA"; B11 duo "1º SERVIÇO / 2º PRODUTO". Campo text vazio de propósito: a legenda do B corre na emenda pelo compositor, não pelo painel, e o ASR erra o trecho 24,94 a 29,04 s (seção 3 item 4).
2. Copiar modelo.html para videos/nichos/dentista/b/painel.html e, nessa cópia: body e #bg em #141210 sem os gradientes; cor do texto em #F3EDE2 e destaques em #E8B36A; #cap, #brand e o canvas #pc (burst de confete) com display:none; #stage centrado numa área de 1080x800 (top 0, height 800). Corrigir os caminhos das fontes para ../../../ads/a01-campinas/fonts/ (a cópia fica três níveis abaixo de videos/).
3. Copiar capture.js para b/capture.js: viewport {width:1080,height:800}; tirar a entrada '-i voz.wav', '-c:a aac', '-b:a 192k' e '-shortest'; acrescentar '-an'; quadros = 1093 (Math.floor(36.43*30) daria 1092 [ESTIMATIVA, conta]); saída painel_B.mp4. Fora dos segmentos o render(t) mostra o segmento mais próximo; isso não importa porque o compositor só usa o painel nas janelas divididas da tabela 2.2.
4. Grade de pontos (B02), relógio (B03) e planta a traço (B09) ficam como [HIPÓTESE] de segunda versão: a primeira versão sai com count, big e duo. Motivo: nenhum dos três existe em código no repositório [FATO, grep em serie2/modelo.html] e desenhá-los agora entra no prazo de 26/10 sem render medido. Os 3 reacts da lista branca entram no compositor do B como SVG estático sobre o painel (seta em B05 e B11, círculo em B06), sem animação na primeira versão.
5. Aceite: `node capture.js` com SHOTS 4, 7, 11, 16, 19, 23, 27, 30 (um segundo por segmento) antes do render cheio; nenhum ✓, ✕ ou coração na imagem; fundo escuro em toda a área.

### 12.2 Texto de resposta ao comentário e da DM
O A e o B pedem "comenta a sua profissão aqui que eu te respondo" e a D2 manda duas perguntas fixas na DM (qual técnica e se já ensina), mas o texto não estava escrito. Texto [HIPÓTESE, sem teste de resposta]:
- Resposta pública ao comentário de dentista: "Obrigado por comentar. Te mandei uma pergunta no direct."
- Resposta pública a outra profissão: "Obrigado por comentar. Me conta no direct qual técnica você domina."
- DM, enviada pelo Bruno à mão (seção 5, nunca por agente): "Oi, aqui é o Bruno. Duas perguntas rápidas: qual técnica você domina que outros dentistas querem aprender? Você já ensina essa técnica hoje, em curso, mentoria ou aula?"
- Registrar na planilha: profissão, técnica, se já ensina (sim/não), origem do contato. Sem preço, sem promessa e sem citar caso de terceiro (CLAUDE.md).
