# 07 · Red team · Reel do dentista · O Estrategista · 21/10/2026

Fontes lidas: contexto.md, run/06-plano-final.md (citado como PF), run/01-fatos.md (citado por número F e C). Nada foi consultado fora desses arquivos nesta rodada; o que não está neles aparece como "sem dado".

Etiquetas: [FATO] com fonte; [ESTIMATIVA] com a conta; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, nível 4, nunca fecha objeção sozinho.

Postura deste documento: o conselho é feito de instâncias do mesmo modelo e votou 12 de 14, 13 de 14 e 14 de 14 em quase tudo (PF seção 7). Concordância desse tamanho é sinal de viés comum, não de acerto. Abaixo a hipótese contrária é testada de propósito em cada decisão.

---

## 0. As cinco objeções que mais pesam (leitura rápida)

1. **A métrica de 48 h não consegue distinguir sucesso de ruído.** A linha de base é mediana 34 de alcance [FATO PF seção 5, 18 reels]. Com números desse tamanho, um reel cai entre 20 e 70 por acaso [PRIOR, sem desvio padrão medido no plano]. O corte "passa com 68" vai premiar ou matar formato por sorte. O próprio plano admite N = 1 por formato (PF seção 1).
2. **O CTA da tela contradiz a fala.** O Bruno diz "comenta a sua profissão aqui" [FATO F11]; a tela digita "Comenta: DENTISTA" (PF A16, B12, C09). Quem escreve "dentista", "sou dentista", "ortodontista" ou "HOF" pode não disparar a automação, e a regra CASE do PostZen pode responder com Tzur e "sete para oito dígitos" [FATO PF seção 6]. Esse é o ponto exato onde a conversão acontece.
3. **Não existe braço de controle simples.** Nenhum dos três modelos é "Bruno + legenda, sem efeito". Se o A for bem, ninguém saberá se foi o letreiro 3D ou só o rosto do Bruno, que é a única variável com dado (F13). A hipótese contrária plausível: o efeito não acrescenta nada e custa 3 dias de pipeline.
4. **Demanda do comprador não está medida.** 474 mil dentistas ativos [FATO F68] é tamanho de categoria, não de mercado de quem quer lançar curso. No recorte dentista do Buzzfy o maior reel teve 764 views e o do nosso ângulo, 494 [FATO F58]. Espera de comentários do A: cerca de 1 [ESTIMATIVA PF D2: 0,49 a 0,84 por 100 de alcance x 95]. Um comentário não decide nada.
5. **A frase-tese pode estar inaudível.** "Formar quem disputa" sai como "forçar" ou "forna" no voz_master [FATO F08, PF seção 3 item 4]. É a frase que diferencia a oferta. Se o portão de escuta falhar e a legenda sumir, o reel perde a ideia central.

---

## 1. Pre-mortem (estamos em 21/04/2027; o plano fracassou)

Causas mais prováveis, da mais para a menos provável [PRIOR na ordem; os fatos citados sustentam cada causa]:

1. **Nenhum lead qualificado de dentista em 6 meses.** O reel teve alcance perto da mediana (34 a 95), 0 a 2 comentários, nenhum deles de dentista com técnica para ensinar. A planilha de "lead qualificado" ficou vazia porque o volume nunca permitiu ler fração de comprador (PF D2 pedia fração em D+7).
2. **Decisão de formato tomada por ruído.** A passou ou falhou o corte de 68 por variação normal; B foi promovido ou enterrado com base nisso. Meses depois descobriu-se que o mesmo reel republicado teria dado outro veredito.
3. **Automação errada no momento da verdade.** Comentários com "dentista" ou "profissão" acionaram a regra CASE ou caíram em regra geral, e o dentista recebeu DM sobre Tzur com promessa de "sete para oito dígitos" [FATO PF seção 6]. Isso é exatamente o tipo de promessa de resultado que o CLAUDE.md proíbe e que o dentista lê como golpe.
4. **Cronograma engolido pelo consórcio de 27/10.** Áudio 22/10, A 23/10, B 26/10, C 27/10 no mesmo pipeline e na mesma máquina de 4 vCPU sem GPU [FATO F21]; render em paralelo é 2 a 5 vezes mais lento [FATO F28]. A data de 29/10 escorregou, o reel saiu sem o B, o C nunca saiu.
5. **O Bruno não aprovou a tempo.** Stills até 23/10, escuta cega até 23/10, inscrição em CRO até 23/10, pausa da regra CASE antes de 29/10: quatro aprovações na mão de uma pessoa, todas com prazo de 2 a 8 dias. Uma delas travou e o plano ficou parado.
6. **Formato pesado contra a evidência da própria conta.** O que performou foi o Bruno falando [FATO F13]; a animação falhou com 77% a 92% de pulo. O B põe o rosto em 1080x1120 e cobre a tela de cima com animação em cerca de 67% do tempo [ESTIMATIVA PF 2.2]. Se o B for ao feed e repetir o padrão de animação, gasta um slot dos 5 reels da semana.
7. **Nicho errado para a oferta.** Dentista que ensina colega é segmento pequeno; quem já vende curso tem agência ou produtor. 1.432 anúncios ativos de "curso para dentistas" [FATO PF seção 1, Meta Ad Library 21/10/2026] indicam mercado disputado por quem tem verba, enquanto nós temos verba zero até 18/11 [FATO F18].
8. **Atrito regulatório com o cliente final.** Um dentista que contratar a oferta vai divulgar curso; o Código de Ética veda propaganda enganosa de curso e gratuidade para atrair aluno (art. 35 V e VII) e há responsabilidade solidária (art. 45) [FATO F73]. Sem dado de que o Bruno tenha processo para isso.
9. **Reel bom, oferta sem esteira.** O DM pergunta "qual técnica e se já ensina" (PF D2), mas não há página, preço ou próximo passo descrito para dentista. O lead morre na conversa.

---

## 2. Piores casos por decisão

**D1 · Áudio**
- Pior caso 1: escuta cega aprova o voz_master, ouvinte leigo do grupo não é leigo de verdade (alguém da agência que já sabe a frase) e o público ouve "forçar quem disputa". Comentário de deboche vira o único comentário do post.
- Pior caso 2: nenhuma versão fecha -1,0 dBTP com música e o critério de abandono manda regravar em 26/10, colidindo com o consórcio de 27/10 (PF D1, seção 6). A regravação muda os tempos e invalida todas as tabelas de quadros dos três modelos, que estão presas a 1093 quadros e aos tempos do words-raw.json.

**D2 · Modelo A**
- Pior caso 1: letreiro 3D com halo no cabelo passa nos 3 stills (quadros 95, 640 e 805) mas aparece em outro quadro, por exemplo nos 44 quadros com segundo componente [FATO F30]. Visual amador no exato formato vendido como "profissional estilo After Effects".
- Pior caso 2: A fica abaixo de 34 em 48 h por causa do horário, do dia ou do algoritmo, a regra de abandono de 05/11 tira o formato do nicho e a conta perde o único formato com base medida por um resultado de N = 1.

**D3 · Modelos B e C**
- Pior caso 1 (B): B vai ao feed sem esperar o direct (PF D3: "vence o opositor"), repete o padrão de animação com 77% ou mais de pulo e derruba a média da semana. O direct pareado de 10 por braço nunca chega a ser lido.
- Pior caso 2 (C): anúncio 4:5 depois de 18/11 em categoria com 1.432 anúncios ativos, com verba pequena e criativo tipográfico sem prova; Meta reprova ou entrega caro; teto do Bruno queima sem nenhum lead. Sem dado de CPM ou CPL no nicho.

---

## 3. Atores irracionais (ou simplesmente imprevistos)

- **Concorrente que corta preço:** produtoras de curso odontológico oferecem "lançamento por porcentagem" sem fixo. O dentista compara e some. Sem dado de preço nosso nem deles.
- **Plataforma que reprova ou esconde:** Instagram pode reduzir distribuição de post que pede palavra específica no comentário (plano-G cita fonte nível 3, PF seção 4). Meta pode reprovar anúncio do C por "promessa de renda" se a legenda for lida como oportunidade de negócio.
- **Plataforma que muda a métrica:** "pulo" e "alcance" do ig_post_stats mudam de definição ou o Buzzfy fica sem cota no dia da conferência de 31/10, como já ficou em 21/10 [FATO F60]. A decisão de 48 h sai sem dado.
- **CRO ou colega denunciante:** dentista concorrente denuncia o perfil do cliente final por mercantilização (Res. 196/2019, F72). Não atinge o Bruno direto, atinge o cliente e a reputação do Bruno no nicho.
- **Cliente que some:** dentista comenta, recebe DM, responde as 2 perguntas e para. Padrão comum em nicho de alta renda e agenda cheia [PRIOR].
- **Sócio ou aprovador que trava:** o Bruno é o único aprovador de stills, áudio, CRO, regra CASE e DMs (PF D1 a D3). Se ele viajar ou estiver no consórcio, tudo trava junto.
- **O próprio Bruno muda de ideia:** ele pediu "letreiro 4d atrás" e "dividindo com reacts" (contexto.md). Se olhar o A enxuto e achar fraco, volta confete e aplausos, que o plano baniu (PF seção 6, última linha). O plano já prevê isso como risco aberto.
- **Comentarista hostil:** dentista comenta "mais um vendendo curso de como vender curso". Sem moderação definida no plano.

---

## 4. Cisnes negros

- Resolução nova do CFO sobre publicidade (grupo criado pela Decisão 05/2025, texto ainda não publicado [FATO F75]) sai entre outubro e abril e restringe divulgação de cursos ou uso de número de colegas.
- Mudança de algoritmo do Instagram que derruba reels de conta pequena (1.618 seguidores [FATO F15]) ou que muda o peso de comentário com palavra-chave.
- Perda de acesso à conta, ao Buzzfy ou ao PostZen (ban de automação de DM por excesso de respostas).
- Caso público de dentista processado por curso, que contamina a categoria "dentista que ensina" por meses.
- Falha da máquina ou do repositório (18 GB livres [FATO F21]; renders de 95 MB cada [FATO F25]) às vésperas do consórcio.
- Reel viraliza fora do público: alcance de 10 mil em paciente e não em dentista; comentários de pacientes poluem o funil e a automação responde paciente com oferta de lançamento.

---

## 5. Teste de premissas

Escala: nível de evidência 1 = medido na conta ou no arquivo; 2 = fonte oficial ou dado de terceiro verificado; 3 = afirmação de fornecedor ou blog; 4 = palpite.

| Decisão | Premissa | Nota | Nível | Impacto | Como testar barato |
|---|---|---|---|---|---|
| D1 | O AAC sobe o pico 0,1 a 0,2 dB, então processar em -1,5 | SOLIDA | 1 | baixa | Já medido duas vezes (evidencias-J e K) |
| D1 | O ouvinte "leigo" separa "formar" de "forçar" igual ao público | ABALAVEL | 4 | alta | 3 pessoas fora da agência, sem ver texto, transcrevem 24,94 a 29,04 s pelo celular com o alto-falante; 5 min |
| D1 | Remasterizar o voz_master não piora a inteligibilidade | ABALAVEL | 3 | media | WER das duas versões contra o roteiro antes da escuta (PF D1 já prevê) |
| D2 | O ganho de 2,4x a 5,8x vem do Bruno em cena e se transfere ao reel do dentista | ABALAVEL | 1 para o passado, 4 para a transferência | alta | Comparar nos 3 reels recentes do Bruno se o tema era nicho específico ou amplo; se todos eram amplos, a transferência é palpite |
| D2 | Letreiro 3D atrás da cabeça melhora retenção ou conversão | FRAGIL | 4 | alta | Publicar uma versão sem letreiro (só legenda) no direct pareado; zero dado hoje (F66) |
| D2 | Mediana de 34 é a linha de base certa | ABALAVEL | 1 | alta | Calcular desvio padrão e faixa dos 18 reels no ig_post_stats; se o p75 já passa de 68, o corte "passa" não diz nada |
| D2 | 48 h bastam para ler alcance de reel em conta pequena | ABALAVEL | 4 | media | Nos 18 reels, comparar alcance em 48 h com alcance em 7 dias; se a ordem muda, o corte de 48 h é ruído |
| D2 | 3 stills bastam para aprovar a máscara | FRAGIL | 1 contra (F30: 44 quadros com segundo componente) | media | Exportar contato de 1 quadro a cada 15 (73 quadros) e olhar em 2 min |
| D2 | Comentário vira DM e DM vira lead qualificado | FRAGIL | 4 | alta | Simular a automação com conta de teste comentando "dentista", "sou dentista", "ortodontista" e "profissão" antes de 29/10, só leitura dos logs (listCommentAutomationLogs) |
| D2 | A palavra da tela (DENTISTA) e a fala ("a sua profissão") não confundem | FRAGIL | 1 (contradição está nos arquivos, F11 e PF A16) | alta | Ler os comentários de reels antigos com CTA falado diferente do escrito; ou alinhar: tela "Comenta a sua profissão" e automação por lista de profissões |
| D3 | Só um modelo por vez no feed, porque a fala é a mesma | SOLIDA | 4, mas lógica direta | media | Não precisa |
| D3 | Tela dividida atende o pedido e não repete o fracasso da animação | FRAGIL | 1 contra (F13: animação 0,15x a 0,8x); 0 a favor (F41, F66) | alta | Mandar B só no direct; medir quem assiste até o fim pelo "visto" da DM; não ir ao feed sem isso |
| D3 | 10 envios por braço no direct dão sinal | FRAGIL | 4 | baixa | Aceitar que é só preferência de texto; não usar para decidir formato |
| D3 | Tipografia 4:5 converte dentista que já compra atenção no feed | FRAGIL | 2 para existência do mercado (1.432 anúncios), 4 para conversão | media | Ler na Ad Library quantos dos anúncios ativos usam tipografia sem rosto e há quanto tempo rodam (anúncio que roda há mais de 60 dias provavelmente paga) |
| Todas | 474 mil dentistas é um número útil e seguro na tela | ABALAVEL | 2 (soma de CROs, pode contar inscrição duplicada, F68) | media | Perguntar ao CFO ou trocar por "mais de 470 mil" com a mesma fonte; ou usar o número de especialistas (162.011, F70), mais próximo de quem tem técnica para ensinar |
| Todas | Existe demanda de dentista que quer lançar curso e paga por isso | FRAGIL | 2 para o mercado de cursos existir; 4 para nós vendermos | alta | 5 DMs manuais do Bruno a dentistas que já ensinam (lista do Instagram) perguntando como lançam hoje; 30 min, só pesquisa, sem pitch |
| Todas | O Bruno aprova tudo até 23/10 | ABALAVEL | 4 | alta | Mandar hoje uma lista de 4 aprovações com prazo e perguntar se cabe na agenda |

---

## 6. Sensibilidade das 3 premissas de maior impacto

| # | Premissa | Valor atual | Limiar em que a recomendação vira | Cai na faixa plausível? |
|---|---|---|---|---|
| S1 | Taxa comentário para lead qualificado no funil do A | Sem dado. Comentários esperados cerca de 1 [ESTIMATIVA PF D2]; fração de comprador sem dado | Se a esperança de leads qualificados por reel for abaixo de 1 (comentários x fração qualificada < 1), o plano de 3 modelos não gera dado de conversão nenhum e a recomendação vira: um reel simples (Bruno + legenda), publicado já, e o esforço vai para DMs ativas e conteúdo de nicho mais amplo. Com 1 comentário esperado, basta fração qualificada abaixo de 100% para virar | Sim. Qualquer fração realista (por exemplo 10% a 50% [PRIOR]) já está abaixo do limiar. Esta é a premissa mais frágil do plano |
| S2 | Corte de 48 h separa formato bom de ruim | Passa com alcance de 68 ou mais, linha de base 34 (PF seção 5) | Se a faixa natural dos 18 reels (por exemplo p10 a p90) cobrir 34 a 68, o corte não discrimina e a regra de abandono de 05/11 vira loteria. A recomendação deveria virar: acumular 3 a 4 reels por formato antes de decidir, ou usar retenção no segundo 5 em vez de alcance | Sim, provável. O melhor reel teve 307 e a mediana 53 do 00-SISTEMA virou 34 na amostra recente [FATO F12, F14, PF seção 5]: a variação entre reels já é maior que 2x. Sem desvio medido; conferir antes de 29/10 |
| S3 | Ganho do formato "Bruno em cena" se mantém com efeito pesado (A) e com rosto reduzido (B) | 2,4x a 5,8x a mediana com Bruno falando; 0,15x a 0,8x com animação sem rosto [FATO F13]. Rosto em tela cheia: A cerca de 95%, B cerca de 28% a 33% [ESTIMATIVA PF] | Se o B se comportar como animação (pulo de 77% ou mais), a recomendação de levar B ao feed sem esperar o direct vira. Para o A, se o letreiro 3D for lido como "edição de template", o limiar é pulo acima de 68% (mediana), quando o efeito passa a custar mais que ajuda | Sim para o B: com o rosto em tela cheia só um terço do tempo, cair na faixa da animação é plausível. Para o A, sem dado; o rosto está quase sempre cheio, então a virada é menos provável |

---

## 7. Hipótese contrária, dita sem rodeio

- **Contra o A:** o que performa é o Bruno, não o pipeline Tzur. Um corte simples com legenda pode render igual em 1 dia em vez de 3, e libera o pipeline para o consórcio de 27/10. O plano não testa isso.
- **Contra o B:** o pedido do Bruno ("dividindo com reacts") não é evidência de conversão. Atender o pedido ao pé da letra no feed contraria o único aprendizado medido da conta. B cabe como peça de direct ou de apresentação, não de feed.
- **Contra o C:** anúncio pago em categoria saturada, com verba ainda indefinida e criativo sem rosto, é a aposta com pior relação custo por informação.
- **Contra o nicho:** o tamanho do sinal esperado (cerca de 1 comentário) não paga 1137 ideias, 14 cadeiras e 3 renders. Pode ser melhor usar a mesma fala como reel amplo ("profissional liberal que vende hora") e deixar o dentista como exemplo, testando se o recorte de nicho reduz alcance.
- **Contra o próprio conselho:** 14 de 14 em várias decisões, previsões com probabilidade 0,38 e 0,3 de bater meta e, mesmo assim, recomendação de seguir com os três. O plano assume que fazer algo é melhor que fazer menos.

---

## 8. O que eu mudaria antes de 29/10 (barato, sem mexer em conta)

1. Alinhar o CTA: ou a tela diz o que a fala diz, ou a automação aceita a lista de profissões. Testar os gatilhos lendo os logs do PostZen; quem altera regra é o Bruno.
2. Medir a dispersão dos 18 reels antes de usar 34 e 68 como cortes.
3. Gerar uma versão controle (Bruno + legenda + rodapé CFO, sem letreiro) junto com o A; custa menos que o B.
4. Segurar o B no direct até haver retenção dele em alguma amostra.
5. Fazer as 5 conversas de descoberta com dentistas que já ensinam antes de investir no C.

Arquivo: /home/user/Disparo-/videos/nichos/dentista/god/run/07-redteam.md
