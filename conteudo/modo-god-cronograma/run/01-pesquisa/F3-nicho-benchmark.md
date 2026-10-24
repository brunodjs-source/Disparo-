# F3 · Benchmark de nicho: marketing digital e lançamento de infoproduto (Brasil)

Frente F3 da pesquisa do conselho Agência Reunida para o @o_estrategista.com.br. Consultas feitas entre 13h40 e 13h50 de sábado, 24/10/2026 (São Paulo), todas só de leitura. Nada foi publicado, agendado ou alterado no Instagram, no Buzzfy ou no PostZen.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha objeção sozinho. Métrica que falta: "sem dado".

**Reels de terceiros entram só como referência.** Toda frase de outro criador citada aqui é dado (vem marcada como "untrusted" pelo Buzzfy), serve para estudar o padrão e não para copiar.

---

## 0. Consultas feitas

| # | Consulta (só leitura) | Parâmetros | Resultado |
|---|---|---|---|
| 1 | Buzzfy `buzzfy_niche_report` | main_niche=marketing | OK. Relatório "Marketing & content creation", report_id 6d38b430-0ccb-4217-95fd-f2c8ae4f2436, montado em 08/10/2026, próxima atualização 07/11/2026. 142 reels (72 de contas verificadas, 70 de não verificadas) |
| 2 | Buzzfy `buzzfy_niche_report` | niche="lançamento de infoproduto" | **Não gerado.** Resposta `status: upgrade`: relatório de tema específico exige o plano MAX (buzzfy.co/upgrade). O Buzzfy devolveu o mesmo relatório do item 1 no lugar. Registrado como limite de plano, não como dado |
| 3 | Buzzfy `buzzfy_niche_report_reels` | report_id acima, páginas 1 a 6 | OK. 142 reels listados, 25 por página. Conferi as contagens do relatório contra a lista: batem (72/70, CTA 57/30/28/8/7/6/3/3, formato talking head 70) |
| 4 | Buzzfy `buzzfy_reel_search` | "lançamento de infoproduto, curso online, estratégia de lançamento digital, mentoria", pt, most_viewed, últimos 365 dias | **ERRO**: "Reel search took too long. Try again in a minute." call_id 0e70eb2f-5299-4069-bcb7-ad68e7cedf7e |
| 5 | Buzzfy `buzzfy_reel_search` | mesma consulta, best_hook | **ERRO**: mesmo timeout. call_id f2394f1c-6db0-4ed1-afc2-980a9bf07b55 |
| 6 | Buzzfy `buzzfy_reel_search` (B1) | "lançamento de infoproduto, curso online, estratégia de lançamento digital", pt, most_viewed | OK. 22 correspondências, 19 mostradas |
| 7 | Buzzfy `buzzfy_reel_search` (B2) | "marketing digital, como vender mais pelo Instagram, conseguir clientes, estratégia para empreendedores", pt, most_viewed, 2 páginas | OK. 116 correspondências, 50 mostradas (limite da busca) |
| 8 | Buzzfy `buzzfy_reel_search` (B3) | "marketing digital, vendas, negócios, empreendedorismo, posicionamento, Instagram para negócios", pt, best_hook | OK. 50 correspondências, 13 com 1.000 views ou mais (o filtro best_hook só mostra esses) |
| 9 | Buzzfy `buzzfy_reel_search` (B4) | "marketing, vendas, negócios, lançamento, tráfego pago, Instagram para empreendedores e profissionais", pt, most_viewed, max_followers 5.000, 2 páginas | OK. 150 correspondências, 50 mostradas |
| 10 | Buzzfy `buzzfy_reel_search` (B5) | "corte de entrevista ou podcast com empresário ou especialista falando de negócios, marketing e vendas", pt, formato interview_podcast, most_viewed | OK. 115 correspondências, 25 mostradas |
| 11 | Buzzfy `buzzfy_reel_search` (B6) | "marketing digital, vendas, lançamento, negócios, conseguir clientes", pt, CTA comment_keyword, most_viewed | OK. 56 correspondências, 25 mostradas |
| 12 | Buzzfy `buzzfy_playbook` | small_accounts, formats, length_and_pace | OK. "The Viral Reels Playbook, 2026 Edition (Buzzfy Research, September 2026)". O detalhe do playbook está na F2; aqui entra só o que toca conta pequena |

Fontes do repositório: `conteudo/modo-god-cronograma/contexto.md`, `run/00-enquadramento.md`, `run/01-pesquisa/F1-auditoria-conta.md`, `run/01-pesquisa/F2-playbook-buzzfy.md`, `conteudo/sistema-instagram/00-SISTEMA.md` (Módulo 2), `conteudo/modo-god-nichos/run/01-pesquisa/F5-formatos-virais-profissoes.md` (buscas em pt de 21/10, para não repetir).

Contas feitas por script a partir das saídas acima (tabelas salvas no rascunho da sessão, fora do repositório). Toda mediana desta frente é de views públicas (plays) informadas pelo Buzzfy.

---

## 1. Respostas curtas

1. **O relatório de nicho do Buzzfy não é um retrato do Brasil.** Dos 142 reels, 97 estão em inglês, 35 em hindi e 2 em português, e os 2 em português são de advocacia e de clínica de estética [FATO, `buzzfy_niche_report_reels`]. 17 dos 20 maiores ensinam a crescer no Instagram, e 17 dos 142 falam de maternidade ou de criadora mãe [FATO, campo topics e summary]. O relatório de "lançamento de infoproduto" não saiu (exige MAX) [FATO, consulta 2].
2. **No relatório global, curto estoura mais no corte entre contas.** Reels abaixo de 20 s: 51 reels, mediana de 354.535 plays; 20 s ou mais: 91 reels, mediana de 65.255 [FATO, conta sobre a lista]. Entre os 31 talking heads de contas não verificadas, os 9 abaixo de 30 s têm mediana de 1.738.928 e os 22 de 30 s ou mais, 15.392,5 [FATO]. Ressalva: o playbook do mesmo Buzzfy, comparando cada criador consigo mesmo, diz que a duração quase não muda nada (de 6 s a 2 min, tudo a cerca de 5% do normal) [FATO, `buzzfy_playbook` length_and_pace].
3. **Formato global que mais estoura entre contas não verificadas:** tutorial/demonstração, mediana de 505.320 plays (12 reels), contra 20.748 do talking head (31 reels) [FATO, relatório]. No recorte em português, tutorial aparece só 5 vezes, mediana de 401 [FATO, buscas B1 a B6].
4. **CTA de palavra-chave não puxa alcance em conta pequena.** Global, contas não verificadas: sem CTA 234.541 de mediana (33 reels), palavra-chave 90.253 (12) [FATO, relatório]. Português, no tema: palavra-chave 401 views e 0,043x os seguidores (25 reels), demais CTAs 430 e 0,081x (101) [FATO, B1 a B6]. Nenhum dos 9 reels de contas de até 6 mil seguidores que passaram de 1.000 views usou palavra-chave [FATO]. Contra: entre verificadas no global, palavra-chave tem mediana maior que sem CTA (245.556 contra 111.128) [FATO, relatório].
5. **No Brasil, o recorte (126 reels no tema, 73 criadores, postados de 01/09 a 23/10/2026)** tem mediana de 428,5 views, 55,5 s de duração e 7.986 seguidores. Só 36 passaram de 1.000 views, 6 de 10.000, e 6 tiveram mais views que seguidores [FATO, B1 a B6].
6. **Pares do Bruno** (no tema, 1.000 a 3.500 seguidores, 29 reels): mediana de 322 views, 0,12x os seguidores, 53 s; 5 de 29 passaram de 1.000; 23 de 29 são talking head [FATO, B1 a B6].
7. **Onde a conta está.** A biblioteca do Buzzfy tem 5 reels do @o_estrategista.com.br. Contra os 29 pares: o reel falado de 04/10 de madrugada (565 views) fica em 10º de 30; o "90% dos lançamentos que floparam" (234) em 18º; os slideshows de texto (70, 70 e 47) em 29º e 30º [FATO, B1 a B6]. O Dentista A (267, contexto.md) ficaria em 17º [ESTIMATIVA: mesma régua, número do contexto.md].
8. **Cortes de entrevista em português:** 28 no tema, 16 com 1.000 views ou mais, mediana de 1.136 views, mas de contas grandes (mediana de 44.403 seguidores; 0,045x os seguidores) [FATO, B5 e outras]. Nenhum dos 28 abre com "Pois é" ou "Bom" [FATO, primeira fala de cada um]. Isso conversa com o achado da F2 sobre pb01, pb02 e pf01.
9. **O que contas pequenas brasileiras fazem:** 40 de 55 reels (até 6 mil seguidores) são o dono falando para a câmera; mediana de 282 views e 52 s; 28 de 55 sem CTA nenhum [FATO, B1 a B6]. Os 3 estouros de quem tem o nosso tamanho vieram de 2 criadores: um com texto na tela e 8 a 26 s (14.304 e 15.122 views), outro com fala de 69 s começando por pergunta (2.401) [FATO].

---

## 2. O que o relatório global mede, e o que não mede

- [FATO, relatório] "smaller" no Buzzfy quer dizer conta **não verificada**, não conta pequena. O relatório não traz número de seguidores. Há contas "smaller" com 21 milhões de plays.
- [FATO, datas da lista] Os plays somam com o tempo: 19 dos 20 maiores foram postados antes de 2026 (de 2022 a 2025). Mediana dos 53 reels postados antes de 24/10/2025: 425.482; dos 89 dos últimos 12 meses: 45.222.
- [FATO, relatório, campo how_to_use] "Plays são contagens públicas; nada aqui mede alcance, salvamentos ou tempo assistido."
- [FATO] Idiomas: inglês 97, hindi 35, português 2, malaiala 2, e 1 cada de italiano, urdu, árabe, espanhol, tâmil e marati.
- [FATO, topics] 17 dos 20 maiores são sobre como crescer no Instagram (configurações, alcance, visualizações, SEO, agendamento). O nicho global de "marketing" no Buzzfy é, na prática, "marketing de Instagram para criador". Lançamento de infoproduto não aparece como tema em nenhum dos 142.

Uso correto: o global serve para formato, duração, ritmo e CTA em conta não verificada; o recorte em português serve para tema e tamanho de conta.

---

## 3. Relatório global (142 reels, "Marketing & content creation")

### 3.1 Formato (mediana de plays)

| Formato | Todos (n) | Todos (mediana) | Não verificadas (n) | Não verificadas (mediana) |
|---|---|---|---|---|
| talking head | 70 | 56.235 | 31 | 20.748 |
| tutorial/demonstração | 26 | 376.219 | 12 | 505.320 |
| montagem estética | 13 | 244.807 | 11 | 79.416 |
| slideshow de texto | 7 | 1.006.121 | 3 | 1.006.121 |
| voz sobre imagens | 5 | 320.798 | 2 | 50.755 |
| vitrine de produto | 5 | 57.349 | 4 | 257.390 |
| vlog/POV | 8 | 20.474,5 | 3 | 7.723 |

[FATO, relatório e lista]. Linhas com menos de 5 reels são evidência fraca (o próprio Buzzfy avisa).

[FATO, lista] Pessoa falando para a câmera: 83 reels, mediana de 89.114; sem pessoa falando para a câmera: 59, mediana de 128.304. Entre não verificadas: 28.444 (33) contra 101.090 (37). Esse corte entre contas vai na direção oposta à medição da própria conta (Bruno falando ficou 2,4x a 5,8x acima da mediana, CLAUDE.md; F1: 5,2x no alcance). A medição dentro da conta pesa mais que o corte entre contas em inglês e hindi.

### 3.2 Gancho (tipo de abertura, mediana de plays)

| Tipo | Todos (n / mediana) | Não verificadas (n / mediana) |
|---|---|---|
| resultado primeiro | 5 / 3.118.071 | 4 / 5.207.242 |
| antes e depois | 5 / 2.908.834 | 3 / 2.908.834 |
| opinião contrária (hot take) | 7 / 634.730 | 4 / 404.425 |
| curiosidade/segredo | 4 / 524.003 | 3 / 1.006.121 |
| afirmação forte | 28 / 318.630 | 10 / 335.884 |
| lista numerada | 15 / 294.333 | 8 / 228.331 |
| como fazer | 14 / 162.542 | 8 / 252.107 |
| chamada de público ("se você é...") | sem linha em "todos" | 8 / 43.654 |
| pergunta | sem linha em "todos" | sem linha (verificadas: 8 / 44.590) |

[FATO, relatório]. Tipo mais usado: afirmação forte (19,7% de todos). Nos 20 maiores: lista numerada 3, resultado primeiro 3, antes e depois 3, dor 2, como fazer 2, afirmação forte 2, opinião contrária 2, curiosidade 1, pergunta 1, truque 1 [FATO, lista].

### 3.3 Duração

| Faixa | Todos (n / mediana) | Não verificadas (n / mediana) |
|---|---|---|
| até 6 s | 9 / 320.798 | 6 / 611.762 |
| 6 a 15 s | 38 / 449.188,5 | 27 / 375.911 |
| 15 a 20 s | 4 / 45.669,5 | 0 / sem dado |
| 20 a 30 s | 15 / 234.541 | 8 / 793.787 |
| 30 a 45 s | 35 / 28.444 | 16 / 27.300 |
| 45 a 60 s | 22 / 59.949,5 | 6 / 18.541,5 |
| 60 a 90 s | 12 / 57.561,5 | 6 / 9.691 |
| 90 s ou mais | 7 / 84.457 | 1 / 1.370.356 |

[FATO, conta sobre a lista]. Duração mediana: 32,5 s (todos), 23,6 s (não verificadas), 37,8 s (verificadas); melhor faixa nas três divisões: abaixo de 20 s [FATO, relatório]. Só nos últimos 12 meses: abaixo de 20 s, 31 reels e mediana de 79.416; 20 s ou mais, 58 e 39.976 [FATO].

### 3.4 CTA

| CTA | Todos (n / mediana) | Não verificadas (n / mediana) | Últimos 12 meses (n / mediana) |
|---|---|---|---|
| nenhum | 57 / 120.957 | 33 / 234.541 | 30 / 26.471 |
| seguir | 30 / 79.721,5 | 12 / 38.451 | 23 / 65.255 |
| comentar palavra-chave | 28 / 149.069,5 | 12 / 90.253 | 19 / 59.161 |
| salvar ou compartilhar | 8 / 424.600,5 | 4 / 1.787.044 | 3 / 234.402 |
| pergunta para comentar | 7 / 16.335 | 4 / 13.975 | 6 / 13.975 |
| direct | 6 / 21.243,5 | 2 / 13.231 | 5 / 20.024 |
| link na bio | 3 / 214.279 | 2 / 761.342,5 | 2 / 761.342,5 |

[FATO, relatório e lista]. O sinal do CTA de palavra-chave muda conforme o recorte: perde para "nenhum" entre não verificadas e no total antigo, ganha nos últimos 12 meses. Não dá para tirar regra disso.

### 3.5 Legenda e ritmo

- [FATO, relatório] Legenda: mediana de 454 caracteres (não verificadas 521); 35,9% têm pergunta; 21,8% pedem palavra-chave na legenda.
- [FATO, relatório] Ritmo: 0,137 corte por segundo (1 corte a cada 7,3 s) [ESTIMATIVA: 1 / 0,137]; primeiro corte aos 3,87 s (verificadas 3,19 s, não verificadas 4,11 s).

---

## 4. Brasil: biblioteca do Buzzfy em português (6 buscas válidas)

### 4.1 Base

- [FATO, B1 a B6] 143 reels únicos. Separei: 126 no tema (marketing, vendas, negócios, lançamento, tráfego), 10 fora do tema (2 de livro de terceiros, tênis, teaser de produto de beleza, espelho, serviço de moto, banho espiritual, pregão de bolsa, "pacto de riqueza", anúncio imobiliário), 2 de celebridade com 1,9 milhão de seguidores e 5 da própria conta. A separação é minha, pelo resumo do Buzzfy.
- [FATO] Todos postados de 01/09/2026 a 23/10/2026. A biblioteca em português do Buzzfy cobre só criadores que usam o Buzzfy; não é o Instagram inteiro.
- [FATO] 126 reels no tema, 73 criadores. Mediana: 7.986 seguidores, 428,5 views, 55,5 s, 0,079x os seguidores. 36 com 1.000 views ou mais; 6 com 10.000 ou mais; 6 com mais views que seguidores (4,8%).
- [FATO, B1] A busca específica por lançamento de infoproduto teve só 22 correspondências em português, e 2 delas são da própria conta. Tema raro na biblioteca.

### 4.2 Por formato (no tema)

| Formato | n | Mediana de views | Views ÷ seguidores (mediana) |
|---|---|---|---|
| talking head | 81 | 378 | 0,079 |
| entrevista/podcast | 28 | 1.136 | 0,045 |
| tutorial/demonstração | 5 | 401 | 0,060 |
| vitrine de produto | 4 | 678 | 0,104 |
| slideshow de texto | 4 | 196,5 | 0,142 |
| montagem estética | 2 | 1.221,5 | 0,332 |

[FATO]. Viés de seleção: a busca B5 foi só de entrevista, o que infla essa linha. Mediana de seguidores: entrevista 44.403; talking head 7.456 [FATO].

### 4.3 Por duração (no tema)

| Faixa | n | Mediana de views | Views ÷ seguidores |
|---|---|---|---|
| até 20 s | 14 | 845,5 | 0,159 |
| 20 a 40 s | 28 | 359 | 0,081 |
| 40 a 60 s | 30 | 404,5 | 0,057 |
| 60 a 90 s | 32 | 407,5 | 0,045 |
| 90 s ou mais | 22 | 435 | 0,084 |

[FATO]. Talking head abaixo de 40 s: 22 reels, mediana 271; 40 s ou mais: 59, mediana 381 [FATO]. O padrão global "talking head curto estoura" não se repete no recorte brasileiro. Os curtos que puxam a mediana de "até 20 s" são texto na tela ou anúncio de live, não fala.

### 4.4 Por CTA (no tema)

| CTA | n | Mediana de views | Views ÷ seguidores |
|---|---|---|---|
| nenhum | 45 | 322 | 0,100 |
| comentar palavra-chave | 25 | 401 | 0,043 |
| seguir | 18 | 427,5 | 0,070 |
| pergunta para comentar | 15 | 738 | 0,087 |
| link na bio | 9 | 776 | 0,013 |
| salvar ou compartilhar | 8 | 327 | 0,322 |
| direct | 4 | 811,5 | 0,028 |

[FATO]. A busca B6 só trouxe reels com palavra-chave, o que aumenta o n dessa linha. Palavras pedidas pelos criadores no recorte: tráfego, estratégia, BASE, CANAL, VENDAS, LUCRO, ESTRUTURA, SCRIPT, MENTORIA, entre outras, sempre uma por reel [FATO, B6].

### 4.5 Por tamanho de conta (no tema)

| Seguidores | n | Mediana de views | Views ÷ seguidores |
|---|---|---|---|
| menos de 1.000 | 22 | 155 | 0,390 |
| 1.000 a 5.000 | 30 | 314,5 | 0,115 |
| 5.001 a 20.000 | 35 | 639 | 0,055 |
| 20.001 a 100.000 | 32 | 663 | 0,017 |
| mais de 100.000 | 7 | 1.514 | 0,010 |

[FATO]. Views sobem pouco com o tamanho da conta: de menos de 1.000 para 20 a 100 mil seguidores, a mediana passa de 155 para 663 views (4,3x) [ESTIMATIVA: 663 / 155].

### 4.6 Os 10 maiores no tema (português)

| # | Abertura (dado de terceiro) | Perfil (seguidores) | Views | Compart. | Formato, duração | Gancho Buzzfy | CTA | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | "Primeiro, princípios e valores." | @alessandro_pizzolatto (96.518) | 19.530 | 2 | entrevista, 31 s | sem nota | pergunta | instagram.com/reel/Dc1aVrwhAc9 |
| 2 | Texto: "E HOJE às 19:30 uma LIVE que você não pode perder" | @newtonlindolfo (1.616) | 15.122 | 146 | vitrine, 26 s | good | nenhum | instagram.com/reel/Def-H0IRWgK |
| 3 | Texto: "Não precisa ser um cyborg para aprender a gerir seu próprio negócio" | @newtonlindolfo (1.616) | 14.304 | 140 | talking head, 8 s | good | nenhum | instagram.com/reel/DcyK4aAR2th |
| 4 | "Uma influenciadora que tá aí no mercado, você não imagina o tanto de menina que tem audiência..." | @johnathanybera (261.680) | 13.659 | 74 | entrevista, 56 s | bad | nenhum | instagram.com/reel/DeMqnTVBrsP |
| 5 | "A gente está passando por um momento de recuperar a confiança no setor." | @matheusfreitasth (286.987) | 12.288 | 1 | entrevista, 65 s | bad | pergunta | instagram.com/reel/DdCblE3OX8W |
| 6 | "Quer vender mais?" | @rafaaraujo.oficial (74.502) | 11.965 | 8 | entrevista, 88 s | good | palavra-chave | instagram.com/reel/Ddd2nP3BY27 |
| 7 | "Teve esperante que agora vendeu 6 mil por dia agora no inverno." | @rafaelmariano (315.235) | 7.780 | 17 | entrevista, 47 s | bad | nenhum | instagram.com/reel/Dd386pbRmfv |
| 8 | "E aí eu decidi montar um minicurso de uma hora e meia sobre essa ferramenta." | @robsondelfiol (5.994) | 5.911 | 301 | entrevista, 37 s | good | nenhum | instagram.com/reel/DehSjA4x1ld |
| 9 | Texto: "Empresários: posicionem-se sem medo." | @ianafurst (13.458) | 5.578 | 24 | talking head, 119 s | good | nenhum | instagram.com/reel/DeKgG8dpFk9 |
| 10 | "Endividamento da população, enquanto que isso afeta o teu negócio." | @minerandoosol (7.469) | 4.100 | 120 | entrevista, 180 s | bad | seguir | instagram.com/reel/Dc35t6zPq0B |

[FATO, B1 a B6; links como a consulta devolveu, não abertos no Instagram]. Nos 15 maiores no tema: 9 sem CTA, 1 com palavra-chave; 8 entrevistas, 5 talking heads [FATO]. Maior taxa de compartilhamento do recorte (com 500 views ou mais): #8, 301 em 5.911 views (5,1%) [ESTIMATIVA: conta direta]. A nota "good/bad" é do Buzzfy e não tem número por trás.

### 4.7 Cortes de entrevista em português (o formato da série da TV Câmara)

- [FATO, B5 e outras] 28 cortes no tema. 16 com 1.000 views ou mais. Mediana de 1.136 views, 56,5 s, 44.403 seguidores, 0,045x os seguidores.
- [FATO] Nenhum dos 28 abre com "Pois é" ou "Bom". Um abre com "Então, em resumo" (427 views).
- [FATO] Aberturas dos que passaram de 1.000: pergunta direta ("Quer vender mais?"; "Quantas vezes você precisou mudar o seu negócio para manter ele vivo?"), número ou valor ("economizou tipo 18 mil reais"; "vendeu 6 mil por dia"), conflito ("vamos demitir os clientes"; "desculpa, você não vai vender") ou história já andando ("E aí eu decidi montar um minicurso...").
- [FATO] Cortes abaixo de 1.000 que começam conversando com o entrevistador antes do ponto: "Queria saber de você, qual conselho você dá..." (305), "Então, em resumo..." (427), "Eu tava pensando aqui, pastor, e eu queria ouvir a opinião do Vitor também." (509), "Sérgio, você falou uma coisa que me lembrei..." (610), "Olha quanto isso é interessante, porque a gente é prestador de serviço, né Rodrigo?" (772).
- [HIPÓTESE] A leitura causal (abrir no ponto aumenta views) é minha. Os cortes que abrem no ponto também são, na maioria, de contas maiores.
- Conta pequena com corte de entrevista que passou de 1.000: só @robsondelfiol (5.994 seguidores), 2 vezes (5.911 e 1.018) [FATO].

### 4.8 Palavra-chave nos comentários (português)

- [FATO, B6] 56 correspondências com CTA de palavra-chave no tema. Maior no tema: 11.965 views (#6 da tabela 4.6, conta de 74.502 seguidores). O resto fica abaixo de 2.000.
- [FATO, B1 a B6] Palavra-chave: mediana 401 views e 0,043x os seguidores; os outros CTAs: 430 e 0,081x.
- [FATO, F1] Na própria conta: 17 automações ativas, 1 disparo somado; as 19 peças com palavra-chave somaram 3 comentários.

---

## 5. O que contas pequenas fazem

### 5.1 Brasil, no tema, até 6 mil seguidores

Usei 6 mil e não 5 mil porque a busca B4 (filtro de até 5.000) devolveu @robsondelfiol com 5.994; o número de seguidores do Buzzfy varia entre consultas [FATO, B4].

- [FATO] 55 reels, 32 criadores. Mediana: 282 views, 52 s, 0,25x os seguidores.
- [FATO] Formato: 40 talking heads (mediana 283,5), 4 entrevistas (995), 3 slideshows (59), 3 vitrines (129), 3 tutoriais (344).
- [FATO] CTA: nenhum 28 (mediana 242), seguir 8 (333), salvar ou compartilhar 6 (264), pergunta 5 (534), palavra-chave 5 (151).
- [FATO] Duração: até 20 s, 7 reels, mediana 719; 20 a 40 s, 15, 175; 40 a 60 s, 14, 242; 60 a 90 s, 11, 285; 90 s ou mais, 8, 325,5.

Os 9 que passaram de 1.000 views:

| Perfil (seguidores) | Views | Compart. | Formato, duração | Gancho | CTA | Abertura (dado de terceiro) | Link |
|---|---|---|---|---|---|---|---|
| @newtonlindolfo (1.616) | 15.122 | 146 | vitrine, 26 s | good | nenhum | texto de anúncio de live | instagram.com/reel/Def-H0IRWgK |
| @newtonlindolfo (1.616) | 14.304 | 140 | talking head, 8 s | good | nenhum | texto: "Não precisa ser um cyborg..." | instagram.com/reel/DcyK4aAR2th |
| @robsondelfiol (5.994) | 5.911 | 301 | entrevista, 37 s | good | nenhum | "E aí eu decidi montar um minicurso..." | instagram.com/reel/DehSjA4x1ld |
| @rafaelvmoraes_ (1.680) | 2.401 | 3 | talking head, 69 s | bad | nenhum | "Você sabia que tem uma coisa que algumas das maiores marcas do mundo entenderam antes de muita gente?" | instagram.com/reel/DdZY6AVR0Yk |
| @vinicruzgg (852) | 2.326 | 3 | talking head, 51 s | bad | seguir | notícia política do dia ligada a vendas | instagram.com/reel/Deu0dz9Se9Y |
| @robsondelfiol (5.994) | 2.281 | 1 | talking head, 45 s | bad | nenhum | história de um post que viralizou | instagram.com/reel/DdpuxGdNwtt |
| @rafaelvmoraes_ (1.680) | 1.524 | 9 | talking head, 163 s | bad | pergunta | "Eu tava aqui pensando, tem muita gente boa ficando invisível porque tem medo de se expor." | instagram.com/reel/DdoxqYesgkZ |
| @robsondelfiol (5.994) | 1.018 | 1 | entrevista, 18 s | bad | nenhum | definição de um termo | instagram.com/reel/DeAnxxVNqz4 |
| @sabino.prof (1.266) | 1.002 | 1 | talking head, 26 s | bad | salvar | "Irmão, a tendência de hoje aqui na Terra é o Founder Led Marketing." | instagram.com/reel/Dduc--Rg321 |

[FATO, B1 a B6]. Nenhum dos 9 com palavra-chave; 6 dos 9 sem CTA. Os 9 vêm de 5 criadores.

- [FATO] @newtonlindolfo: 333 curtidas em 15.122 views (2,2%) e 49 curtidas em 14.304 (0,34%), 0 comentário nos dois. Se houve impulsionamento pago: sem dado. [HIPÓTESE] A taxa de curtida muito baixa do segundo é compatível com anúncio; não usar esses dois como prova de formato orgânico.

### 5.2 Pares diretos do Bruno (1.000 a 3.500 seguidores, no tema)

- [FATO] 29 reels de 19 criadores. Mediana: 322 views, 0,12x os seguidores, 53 s. 23 de 29 são talking head. Quartis de views: 179,5 (quarto de baixo), 322 (mediana), 766 (quarto de cima) [FATO, conta sobre a amostra].
- [FATO] 5 de 29 passaram de 1.000 views (17%) [ESTIMATIVA: 5 / 29]; 3 de 29 tiveram mais views que seguidores.

### 5.3 Playbook do Buzzfy sobre conta pequena (medido dentro de cada criador)

- [FATO, `buzzfy_playbook` small_accounts] Abaixo de 1.000 seguidores, o reel típico teve 243 views e o melhor cerca de 2.000. Um reel típico tem views de 0,17x os seguidores; um estouro, 1,85x. 74% dos criadores de 1 a 5 mil seguidores tiveram ao menos um estouro em 22 meses.
- [FATO, idem] Contas pequenas foram melhor com estranhos: seus Trial Reels passaram o alcance usual 21% das vezes, contra 13% nas contas acima de 100 mil.
- [FATO, `buzzfy_playbook` formats] De 1 a 5 mil seguidores: história 1,28x o normal do criador, montagem 0,69x; tutorial 1,02x abaixo de 5 mil.
- [FATO, `buzzfy_playbook` length_and_pace] Duração quase não muda nada dentro do criador; o que muda é quanto do vídeo é assistido (assistido acima de 1,5x a duração: 33% de estouro; abaixo de 20%: 5%).

---

## 6. Onde o @o_estrategista.com.br fica no benchmark

| Reel da conta na biblioteca | Postado (UTC) | Views na biblioteca | Formato, duração | CTA (Buzzfy) | Posição entre os 29 pares (de 30) |
|---|---|---|---|---|---|
| "Deixa eu te contar uma coisa." | 04/10 02h06 | 565 | talking head, 75 s | salvar ou compartilhar | 10º |
| "Ei, vem cá, escuta essa: 90% dos lançamentos que floparam..." | 04/10 14h11 | 234 | talking head, 70 s | pergunta | 18º |
| "100 mil seguidores, 14 vendas, e a culpa foi pro preço." | 01/10 18h05 | 70 | slideshow, 33 s | palavra-chave | 29º |
| "O que você recusa vende mais do que o que você oferece." | 05/10 01h30 | 70 | slideshow, 66 s | "1, 2 ou 3" | 29º |
| "Você criou o produto, gravou as aulas, e ninguém comprou." | 11/10 21h29 | 47 | slideshow, 38 s | PESQUISA | 30º |

[FATO, B1, B2, B4 e B6]. O Dentista A (267 views, contexto.md) ficaria em 17º [ESTIMATIVA].

- [ESTIMATIVA] O reel de 565 views deve ser o "Ele nunca fez um anúncio" do contexto.md (04/10, 10,14x): 10,14 x 57 = 578, perto de 565; o resumo do Buzzfy fala de Jesus e lançamento. O de 234 deve ser o "reel de 04/10 14h" (4,42x): 4,42 x 57 = 252. A ligação por nome é hipótese; a contagem de views é da biblioteca.
- [FATO] Os reels com o Bruno falando ficam na metade de cima ou no meio dos pares; os slideshows ficam no fundo. O benchmark externo concorda com a medição interna (CLAUDE.md, F1).
- [ESTIMATIVA] Views ÷ seguidores: 565 / 1.619 = 0,35x; 234 / 1.619 = 0,14x; normal da conta 57 / 1.618 = 0,035x (F2). Mediana dos pares: 0,12x.

---

## 7. Leitura para o cronograma (hipóteses, não regras)

Nenhum item abaixo muda regra do CLAUDE.md sozinho. Cada um é TESTAR com uma mudança por vez, medido no Módulo 7.

1. **Régua externa para o portão de segunda** [HIPÓTESE, régua tirada do FATO 5.2]. Pares brasileiros do mesmo tema e tamanho: mediana de 322 views; 1.000 ou mais é o quinto de cima (17%). Proposta para o Módulo 7: reel com 322 ou mais em 48 h está "na mediana dos pares"; 1.000 ou mais é "estouro entre pares". Hoje o normal da conta (57) fica abaixo do quarto de baixo dos pares (179,5), e o Dentista A (267) abaixo da mediana. Ressalva: views da biblioteca são vida inteira até 24/10, não 48 h.
2. **Cortes da TV abrindo no ponto** [HIPÓTESE, apoia a F2]. Os 28 cortes de entrevista em português não abrem com "Pois é" nem "Bom"; os que passaram de 1.000 abrem com pergunta, número, conflito ou história andando (4.7). Teste já proposto pela F2: pb02 (sex 30/10, 21h) com o ápice no quadro 0, contra o pb01 como está.
3. **CTA de alcance sem palavra-chave** [HIPÓTESE]. Evidência a favor: 4.4, 4.8, 5.1 (0 de 9 estouros de conta pequena com palavra-chave), global de não verificadas (3.4) e a própria conta (1 disparo em 17 automações). Evidência contra: verificadas e últimos 12 meses no global. Leitura: a palavra-chave é ferramenta de conversão, não de distribuição. Isso já é a regra do CLAUDE.md (TABULEIRO uma vez por mês, só em post com 150 de alcance ou mais); nos outros reels, pergunta para comentar (mediana 738 no recorte, 534 entre pequenas) ou nenhum CTA.
4. **Duração** [HIPÓTESE fraca]. Corte entre contas favorece até 20 s (global 354.535 contra 65.255; Brasil 845,5 contra cerca de 400), mas no Brasil isso vem de texto na tela e anúncio, e o talking head curto não ganhou (271 contra 381). Dentro do criador, o playbook diz que duração quase não importa. Se testar, um corte de 15 a 20 s de um trecho da TV contra a mediana da própria série, mesmo assunto.
5. **Tutorial com o rosto do Bruno** [HIPÓTESE]. Tutorial é o formato que mais estoura entre não verificadas no global (505.320); no playbook rende 1,02x o normal do criador abaixo de 5 mil seguidores (1,10x a 1,14x de 5 mil a 100 mil). Os "tutoriais" da conta foram slideshows sem rosto e ficaram no fundo dos pares (6). Teste quando houver gravação: Bruno em cena nos 3 primeiros segundos mostrando a tela de um diagnóstico de lançamento, com resultado primeiro, passos e resultado de novo (estrutura do playbook).
6. **História com resultado, no formato entrevista** [HIPÓTESE]. O único corte de entrevista de conta pequena que estourou (@robsondelfiol, 5.911 views, 5,1% de compartilhamento) começa no meio da ação e conta um resultado concreto de produto digital. Para a série da TV, isso aponta para trechos em que o Bruno conta um caso (ex.: o Método Xeque-Mate aplicado a alguém) antes de trechos de opinião. Os números do caso só entram com fonte; sem promessa de resultado (CLAUDE.md).
7. **O que não copiar** [PRIOR]. Do global: tutoriais de "configuração do Instagram" (17 dos 20 maiores) e pedidos de "comenta seu @" de criadoras mães, fora do posicionamento do Módulo 2. Do Brasil: notícia política do dia (estourou em conta de 852 seguidores), risco de marca para quem fala com médico, dentista e advogado.

---

## 8. Lacunas

- Relatório específico de "lançamento de infoproduto": sem dado. Exige plano MAX do Buzzfy (consulta 2).
- 2 buscas com timeout (call_ids 0e70eb2f-5299-4069-bcb7-ad68e7cedf7e e f2394f1c-6db0-4ed1-afc2-980a9bf07b55). A mesma ideia foi refeita com outra frase (B1) e respondeu.
- Biblioteca em português: só criadores que usam o Buzzfy, só de 01/09 a 23/10/2026. Os grandes nomes de lançamento do Brasil não aparecem: sem dado sobre eles.
- Amostra não aleatória: busca por sentido mais ordenação por views, máximo de 50 por busca; B5 (só entrevista) e B6 (só palavra-chave) inflam essas duas linhas. As medianas comparam grupos escolhidos assim.
- Views de terceiros são públicas e de vida inteira: sem alcance, retenção, pulo, salvamento ou tempo assistido (sem dado). Curtidas, comentários e compartilhamentos só nas buscas, não no relatório global.
- Impulsionamento pago nos reels de terceiros: sem dado.
- Número de seguidores varia entre consultas (@robsondelfiol com 5.994 num filtro de até 5.000).
- A classificação "no tema / fora do tema / celebridade" é minha, pelo resumo do Buzzfy.
- Os links vieram das consultas ao Buzzfy (a consulta confirma que o reel está na biblioteca); não abri as páginas no Instagram.
- Nota de gancho "good/bad/unknown" é qualitativa; "unknown" aparece quase só em reel com poucas views, então a comparação entre notas mistura nota e alcance.
- O relatório global não traz seguidores; "smaller" é conta não verificada.
- Ligação nominal entre os reels da conta na biblioteca e os nomes usados no contexto.md: estimativa por views (seção 6).
