# Pre-flight de texto · 06-plano-final.md · 25/10/2026

Skill creative-pre-flight: não está na lista de skills desta sessão (nem no repositório; só há os registros de 21/10 em `modo-god-nichos/run/09-preflight.md`). Apliquei as dimensões de texto dela: coerência elemento a elemento, anti-IA e português, mais as regras do cliente (CLAUDE.md, `stories-objecoes/02-provas.md` "O que NÃO pode ser dito", `conhecimento-o-estrategista.md` 2.3 e 4.4). Só leitura em sites e ferramentas; a única escrita fora deste arquivo foi a correção no `06-plano-final.md`.

## Travessões e caracteres
- U+2014: 0. U+2013: 0. Outros traços (U+2010 a U+2015, U+2212, U+2E3A, U+2E3B, U+FE58, U+FE63, U+FF0D): 0. Hífen entre espaços: 0. Emoji: 0 [FATO, varredura em Python do arquivo inteiro, antes e depois das correções]. Nada a trocar.
- As 2 setas (U+2193) estão só na citação da linha antiga da bio, a que sai. Não vão ao ar.

## Limites contados caractere a caractere
Não há anúncio no arquivo (mídia paga R$ 0 até 18/11 e nenhum anúncio com conteúdo da TV, seção 4): limites de plataforma de anúncio não se aplicam. Limites usados: direct de automação com botão até 640 e título do botão até 20 [FATO, esquema do `createCommentAutomation`, citado no D6]; bio até 150 [PRIOR, limite do app]; legenda até 2.200 [PRIOR, limite do app]; gancho até cerca de 125 (BASE §10, `conhecimento` 2.3).

| Peça | Caracteres | Limite | Situação |
|---|---|---|---|
| Texto B, direct novo da TABULEIRO (9.2 e 12.1) | 324 | 640 | ok; o plano dizia 325, corrigido |
| Texto A, direct da ESTRATEGISTA do case (10.4 e 12.1) | 410 | 640 | ok |
| Texto A2, à mão (12.1) | 445 | 1.000 do direct comum [PRIOR] | ok; o plano dizia 444 e a regra de 10.4 tirava o ponto antes de "Se fizer sentido", corrigido |
| Botão e sticker "Fazer o teste" | 13 | 20 | ok |
| Resposta ao caso de dom 09h02 | 459 | 1.000 [PRIOR] | ok |
| Modelo dos balões, com a linha do dia | 370 a 404; SUA VEZ 307 | 1.000 [PRIOR] | ok; o plano dizia 361 a 404, refeito depois da troca do modelo |
| Resposta ao DIAGNÓSTICO · 30 MIN | 239 (sem &p=) a 255 (nutricionista) | 1.000 [PRIOR] | ok; o plano dizia 251 "sem a profissão", corrigido |
| Resposta privada a comentário | 293 | 1.000 [PRIOR] | ok; era 284 antes da troca do modelo |
| Resposta à mão do nicho 1 | 381 | 1.000 [PRIOR] | ok |
| Bio, 4 linhas, quebras contam 1 | 146 | 150 | ok |
| Nome "Bruno \| Estrategista de Lançamento" | 34 | sem dado | ok: é o nome de perfil já registrado na base [FATO, `conhecimento` 2.1]; a reserva de 26 continua |
| 12 legendas (car02 a car05, tl01, car01, pb02, tl02, po01, R1, Dentista C, nicho 1) | de 313 a 713 | 2.200 | ok; 5 hashtags em cada, sem repetição |
| 12 ganchos e frases de story | de 34 a 82 | cerca de 125 | ok |

## Peças auditadas (66)
- Stories, texto (31): frases 3 e 4; caso das 09h02; link v2 com sticker; molde da contagem e as 7 frases; estático das 09h de 02/11; story das 21h10 de 02/11; chamadas refeitas do tl01, do pb01 e do po01; SUA VEZ; S2 com 7 frases, 4 balões e viradas (O9 a O12) e 3 pilares novos; os 6 balões da S1 e as 5 viradas citados na mensagem das 20h.
- Carrosséis, lâmina a lâmina e legenda (4): car02, car03, car04, car05.
- Legendas (11): tl01, car01, pb01 (frase de crédito), pb02, tl02, po01, ci01 (frase trocada), R1, Dentista C (2 variantes), nicho 1, case (variantes de 11.2).
- Bio e perfil (1): bio, Nome, título do link, fixados.
- Directs e respostas, que fazem o papel de chatbot (9): textos B, A e A2, caso das 09h02, modelo dos balões com 7 linhas do dia, DIAGNÓSTICO · 30 MIN, resposta pública e privada a comentário, nicho 1, resposta pública da automação do case.
- E-mail (1): pedido à Assessoria de Imprensa da Câmara (10.6).
- Texto de site (1): os 2 trechos novos da política de privacidade (10.7).
- Mensagens operacionais ao Bruno, só travessão, português e coerência com o plano (8): 08h15 completa (12.1), 18h e 20h de domingo (11.1), seg 12h e 18h (10.5), sexta 18h (11.7), mensagem da porta (12.4), aviso das 18h40 (12.3).

## Corrigido no arquivo
1. **car02, lâmina 4, e pilar QUEM SOU de dom 01/11 (9.3 e 9.8). Regra do cliente.** "13 anos de marketing digital" está na lista do `02-provas.md` ("número de anos fica fora da tela até o Bruno confirmar"; a entrevista só sustenta "em 2015 já estava no digital"). Lâmina 4 ficou "No BNI, eu ocupo a cadeira de estrategista de lançamentos."; o pilar ficou com a frase-definição da base 2.1, "Eu desenho e comando o lançamento de experts que já têm audiência." Nenhum render do car02 existe ainda [FATO, busca por car02 a car05 no disco], então não há imagem a refazer.
2. **car02, lâmina 7. Português.** "cliente ... do cliente" na mesma linha. Ficou "Um caso do mercado financeiro: de 6 para 20 milhões por mês, contado pelo marketing do cliente." A regra do case (não chamar de lançamento, não dizer que o Bruno causou sozinho) segue cumprida.
3. **car03, legenda. Anti-IA.** Duas tríades seguidas ("grava, aparece e aprova" e "desenho, comando e leio"). A primeira passou a "você grava as aulas e aprova a oferta".
4. **car05, lâminas 3 e 7 e legenda. Coerência.** "Fechando comigo ou não." vinha solto depois de "Preço só entra depois que eu entendo a sua partida.", o que não faz sentido. No story de origem (3010-1731) ele completa "Vou te mostrar onde você está perdendo". Voltou para lá, e na legenda foi para a frase do Lance: "Eu olho com você o Lance em que o seu lançamento trava, fechando comigo ou não."
5. **car01, legenda. Coerência.** A nota "(Três, sem a lâmina 2)" estava dentro do texto entre aspas, que a agência cola como está. Saiu das aspas e virou instrução ("Sem a lâmina 2, 'Quatro frases' vira 'Três frases'.").
6. **pb02, legenda. Português e regra de caso.** "Colocamos ele" (pronome reto como objeto) e uma causa atribuída antes de o registro dizer qual foi o papel do Bruno. Ficou "Com o marketing digital, passou a vender 250 mil."
7. **tl01 e tl02, legendas. Coerência.** O índice traz minutos que são da gravação do celular, não da edição exibida [fato 81]; o car01 já avisava, o tl01 e o tl02 não. Entrou "Os minutos são da minha gravação no estúdio." antes do pedido.
8. **E-mail à Assessoria. Coerência e anti-IA.** "trechos curtos" contradizia o item 3 do próprio pedido (um trecho mais longo depois da exibição): ficou "trechos desse registro". Os 4 "não vou" seguidos viraram uma frase só, com o mesmo conteúdo.
9. **Modelo dos balões e resposta privada a comentário (12.2). Coerência.** "Se quiser ver em qual casa o seu lançamento trava, O Tabuleiro tem 12 casas" não fecha a condição. Ficou "faz O Tabuleiro, o teste de 12 casas, em cerca de 4 minutos".
10. **Linha do dia O2. Anti-IA.** "Num lançamento comigo ... fica comigo" repetia a palavra. Saiu o primeiro "comigo".
11. **Linha do dia O3. Coerência.** "Por isso" retomava o balão do story, que no direct não aparece antes. Saiu o "Por isso".
12. **Contagens.** Texto B 324 (9.2 e 12.1); A2 445, com o ponto que a regra de 10.4 tirava (10.4 e 12.1); balões 370 a 404 e SUA VEZ 307; DIAGNÓSTICO · 30 MIN de 239 a 255; resposta privada de comentário 293. Todas abaixo dos limites.

## Conferido sem problema
- Regras do CLAUDE.md nas peças: sem emoji; sem HighClass, Júnior Prazeres ou Felipe Roser; sem o nome do cliente do case nem de quem conta (0 ocorrência no arquivo); "Estrategista Digital" só em nota, nunca em peça; nenhuma palavra banida da BASE §10 (imagine, no fim das contas, afinal, vale lembrar, mindset, jornada, desbloquear, revolucionário, renda extra, liberdade financeira, "e é aí que entra", "seja... seja", "não apenas... mas também", "No mundo de hoje").
- "Não é X, é Y": no máximo uma por peça (car05 lâmina 3; R1 "Não teve... Teve"; nicho 1 "para de convencer e passa a conduzir"); as outras peças não têm nenhuma.
- Promessa de resultado: nenhuma. Os números de caso aparecem só como fato do caso, com "O número de um caso não se repete igual em outro negócio." (car02, caso das 09h02, Texto A, tl01 e pb02 com registro). "Em cerca de 4 minutos você vê qual Lance é o seu gargalo" descreve o teste, não o negócio.
- Preço: nenhum valor em peça; "sem custo" no car05 bate com "gratuito" da base 3.2; "Preço só entra depois" coerente com o story 3010-1201.
- Conselhos: Dentista C é anúncio do Bruno para dentistas, sem imagem clínica nem promessa ao paciente, com o 474 mil e a fonte da legenda publicada do Dentista A (Res. CFO 196/2019 e 118/2012 seguem como condição do G1); nicho 1 sem a linha da ABAC e sem "contemplação" ou prazo; ganchos de advogado, psicólogo, nutricionista e médico falam do negócio do profissional, sem resultado de paciente, e o do médico leva "Exemplo ilustrativo.", como a voz da base pede.
- Frases vetadas da TV ("ao vivo", "rede nacional", "a TV Câmara recomenda", "fui convidado pela TV", "entrevista exclusiva", "A TV me chamou de história de sucesso"): 0 em peça. "Vai ao ar na segunda, 02/11" é a data dada pelo Bruno [FATO 1]; "foi ao ar" só aparece como condição.
- Nomes do D6: "O Tabuleiro" é o teste e "diagnóstico" só a conversa de 30 min em todas as peças novas; botão, sticker e título do link da bio dizem o mesmo "Fazer o teste"; origens o= e datas AAMMDD batem com o dia de cada post (261024, 261025, 261028, 261030).
- Um pedido por peça em todas as legendas.
- Registro: a BASE §10 aprova o português falado ("pra", "tá", "dá pra"). Ficaram como estão o imperativo de fala ("Toca", "Responde este story", "Me conta"), a próclise no começo ("Te mandei") e "chega no meu WhatsApp", por serem desse registro e por já estarem em PNG agendado; não são erro de digitação nem de concordância.

## Não conferido
- O resto da legenda do pb01 e a do ci01: o plano só traz a frase trocada; o texto inteiro está no PostZen.
- Link com ponto final logo depois (A2, caso das 09h02, balões, nicho 1): se o app incluir o ponto no link, a origem chega como "ig-case." [HIPÓTESE; conferir tocando no link no primeiro envio à mão].
- Peças visuais (lâminas de car02 a car05, PNGs dos balões com "Responde este story", caso das 09h02, link v2, contagem, stories refeitos com foto de marca, R1, nicho 1, Dentista C): ficam para o CRAFT e a folha de quadros do CLAUDE.md. Texto aprovado não aprova imagem.

## Reprovadas (sem correção)
Todas são do reel do case de 6 para 20, agendado pelo Bruno para dom 25/10 21h. Nenhum agente mexe no PostZen, e a correção depende da resposta dele ao item 4 da mensagem das 08h15 (12.1).
1. **Regra do cliente, palavra-chave.** A legenda agendada e o CTA falado pedem "comenta ESTRATEGISTA", uma segunda palavra-chave no mês da TABULEIRO (CLAUDE.md: uma por mês); a variante de 11.2 ("Se o seu negócio travou, comenta ESTRATEGISTA.") mantém a palavra. Tirar só da legenda quebraria a coerência com a fala do vídeo. Fecha com a exceção escrita do Bruno (item 4d) ou com reedição.
2. **Regras do cliente, fala e tela.** Duas "não é X, é Y" faladas (máximo de uma), "6 MESES" na tela (o `02-provas.md` veta "em 6 meses" como fato; a fala do cliente diz "acredito que seis meses"), nome e logo da empresa no cartão e no cenário (proibidos nesta série pelo `02-provas.md`) e o nome do responsável na legenda sem ok escrito. Fecha com a autorização escrita (item 4b e 4c) ou com reedição.
3. **Coerência e veracidade, tela final de 50 s.** A interface recriada mostra "1.282 comentários" (a conta teve 2 em 7 dias [FATO, `ig_account_stats` 19h42]) e @ com cara de perfil real, alguns com título de profissão regulada. Fecha com a versão sem a tela final (item 4a), pronta às 11h segundo o plano.
