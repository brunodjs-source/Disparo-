# Plano da cadeira L · Automação e atendimento · 21/10/2026

**Persona:** engenheiro de automação, chatbot e mensuração (CAPI, conversões offline).
**OTIMIZA PARA:** resposta rápida e dado limpo voltando para a plataforma.
**PONTO CEGO (assumido):** vejo tudo como fluxo e subestimo oferta e criativo. Compensação: toda proposta de fluxo abaixo fica condicionada a existir volume de entrada; quando o gargalo for topo de funil, digo isso e não vendo automação como solução.
**PERGUNTA CONTRÁRIA:** e se o problema não for atender bem, e sim não ter lead para atender?

**Resposta à pergunta contrária.** Os dados dizem que é isso. [FATO, contexto.md, Buzzfy 21/09 a 21/10/2026] 448 visitas ao perfil, 58 seguidores, 7 cliques no link, 1 disparo de automação e 0 vendas. Com 1 disparo em 30 dias, não há atendimento para melhorar: o funil está vazio no topo. Conclusão da minha cadeira: nesta rodada a automação tem papel pequeno e barato (capturar, etiquetar, medir) e não deve consumir horas que deveriam ir para gravar os 5 reels. O que eu defendo construir é o mínimo para que cada lead que aparecer seja contado e respondido em minutos, e para que a semana 2 decida com número, não com impressão.

## 1. Veredito (até 12 linhas)
1. O gargalo é volume de lead, não atendimento. [FATO] 1 disparo em 30 dias.
2. D1: gravar os 3 fixos na mesma semana dentro do ritmo de 5 reels, Bruno em cena no segundo 0. Probabilidade de bater mediana >= 106 e pulo < 60%: 0,45 [0,30; 0,60].
3. D2: extras psicólogo e advogado, com advogado marcado como teste de anúncio existente sem dado de mercado. Prob. 0,30 [0,15; 0,45].
4. D3: manter TABULEIRO como palavra única (regra do CLAUDE.md) com automação PostZen ligada em todos os 5 posts desde a publicação, mas sem anunciar a palavra no vídeo abaixo de 150 de alcance. Etiqueta de nicho entra na resposta da DM, não na palavra-chave. Prob. de >= 5 disparos e >= 2 diagnósticos: 0,20 [0,08; 0,35].
5. D4: só orgânico até D+7; impulsionamento só com teto aprovado pelo Bruno por escrito. Prob. ganho líquido >= 30 em 14 dias: 0,40 [0,25; 0,55].
6. Entrega da minha cadeira: planilha de leads com 9 colunas, UTM por nicho no link da bio, resposta em até 15 min no horário comercial, registro de cada diagnóstico como conversão offline (manual nesta rodada, sem CAPI até existir 10 eventos).
7. Não construir chatbot completo agora. Custo de oportunidade maior que o ganho com 1 disparo por mês.

## 2. Respostas às 9 perguntas

**P1. Qual decisão move e qual número muda?** Movo D3 diretamente: de 1 disparo/30 dias [FATO, contexto.md] para meta de >= 5 disparos em 28 dias somando os 5 vídeos, e de "diagnósticos sem dado" para um número contado. Movo D4 indiretamente por medir seguidores líquidos (hoje sem dado, só o bruto de 58 em 30 dias). D1 e D2 eu só instrumento.

**P2. Fonte de cada dado.**
- Mediana 53, pulo 68%, 307 melhor alcance, 58 seguidores, 7 cliques, 1 disparo: [FATO] contexto.md (Buzzfy 21/09 a 21/10/2026).
- Formato 30 a 40 s, pessoa falando: [FATO] F5, Buzzfy buzzfy_reel_search 21/10/2026.
- Mercado: consórcio [FATO] F2 (ABAC via em.com.br); dentistas 474.640 [FATO] F4 (CFO); nutricionistas 126.539 em 2017 [FATO] F3 (SciELO); psicólogos +151,1% de vínculos [FATO, nível 3, resumo de busca] F1.
- [ESTIMATIVA] ~27 seguidores em 14 dias = 58/30 x 14, bruto. Ganho líquido: sem dado.
- [ESTIMATIVA] Taxa clique para disparo: 1/7 = 14%. Amostra de 7, não confiável.
- Diagnósticos realizados no período: sem dado.

**P3. CFN, CFO e consórcio.** Na camada de automação: a resposta automática da DM não usa "resultado", "garantido", "contemplação", "antes e depois", nem número de faturamento do cliente final. Mensagem padrão fala só do negócio do profissional (lançamento, agenda de turmas, posicionamento). Para nutricionista, considero a Resolução CFN 856 como vigente por precaução, já que a vigência em out/2026 não foi confirmada [F3, lacuna]. Para consórcio, nenhum texto pode sugerir contemplação garantida [FATO, F2, Res. BCB 285/2023 via trecho de busca].

**P4. Bruno em cena nos 3 primeiros segundos e 75 a 100 palavras.** Não é minha cadeira escrever o roteiro; minha checagem é de dado: medir no Buzzfy a retenção nos 3 s e a duração média assistida de cada post. Critério: se duração média assistida < 6,2 s (mediana atual [FATO]) o hook falhou, independente do nicho.

**P5. Estrutura HOOK a CTA.** Aceito a estrutura. Exijo que o CTA seja um só e idêntico ao que a automação espera (ver D3), para não perder disparo por palavra digitada errada.

**P6. Prova.** Só Tzur Capital (de 6 para 20 milhões/mês, case autorizado, contexto.md) ou dado próprio do perfil. A automação não cita número do case na DM para não parecer promessa ao lead.

**P7. Métrica e data.** Ver seção 6 e tabela de regras: D+7 de cada post (alcance e pulo, Buzzfy ig_post_stats); 11/11/2026 decide D1; 18/11/2026 decide D2, D3 e D4 (PostZen listCommentAutomationLogs, ig_follower_growth e planilha de diagnósticos).

**P8. Terceiros e verba.** Dependem de terceiro: PostZen (automação de comentário, já em uso), Buzzfy (leitura), agenda do Bruno (diagnóstico). Verba de impulsionamento: aprovação do Bruno, teto sem dado. Nenhuma ação minha publica ou altera conta; a configuração da automação é feita pelo Bruno ou com aprovação explícita dele.

**P9. Regras de texto.** Este plano e as mensagens propostas: sem travessão, sem emoji, sem promessa, sem nomes proibidos. A única construção "não é X, é Y" que uso está na mensagem 2 da DM (ideia 21).

## 3. Decisões

### D1. Formato e ordem dos 3 fixos
| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| A. Um por dia útil, seg a qua | Leitura rápida, 3 pontos em 3 dias | Pouco tempo para cada post acumular alcance antes do próximo |
| B. Os 3 na mesma semana dentro dos 5 reels (seg, qua, sex) | Respeita o ritmo do CLAUDE.md | Deixa 2 vagas para os extras na semana 2 ou para repetir o vencedor |
| C. Testar 1 nicho e esperar sinal | Menos gravação | Uma amostra de 1 não separa nicho de dia ou horário; atrasa D2 em 1 semana |
| D. Fora do óbvio: gravar os 3 numa sessão com 2 hooks cada e publicar o hook B como trial reel (se disponível na conta) | Dobra a amostra sem dobrar gravação | Risco de canibalizar; trial reel na conta: sem dado |

Premissas: Bruno grava em uma sessão; o histórico de 2,4x a 5,8x se mantém com tema de nicho [ESTIMATIVA, 127 a 307 de alcance].
**Posição:** B, com D como hipótese se o trial reel existir. Prob. 0,45 [0,30; 0,60]. Confiança 0,5. Motivo do teto: os reels de negócio para saúde e dentista tiveram 78 a 494 views em perfis de terceiros [FATO, F5], e pulo < 60% só foi visto uma vez (53%, melhor reel).

### D2. Nichos extras
| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| A. Advogado | Anúncio já existe, coerência com tráfego pago | Sem dado de mercado; OAB tem regra de publicidade própria não verificada |
| B. Psicólogo | Crescimento medido (+151,1%, nível 3) | CFP tem regra de publicidade não verificada; tema saúde mental exige cuidado |
| C. Educador financeiro ou IA aplicada | Infoproduto com dado (IA R$ 142,8 mi Hotmart, F1) | Público pode ser concorrente do próprio Bruno; foge de "profissional liberal" |
| D. Fora do óbvio: escolher o 2º extra pelos comentários e DMs dos 3 fixos (nicho que mais aparecer em perfis de quem comenta) | Decisão por dado próprio | Atrasa 1 semana; amostra pequena |
| E. Só os 3 fixos agora | Foco | Ignora pedido do Bruno de 5 |

**Posição:** B (psicólogo) fixo e A (advogado) como 2º, mas com a regra D como desempate: se até 31/10 houver >= 3 comentários de um mesmo outro nicho, ele substitui advogado. Prob. 0,30 [0,15; 0,45]. Confiança 0,35. Premissa: "ao menos 1 comentário de profissional do nicho" é o critério mais difícil com 1.618 seguidores.

### D3. CTA e caminho até o diagnóstico (minha decisão principal)
| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| A. TABULEIRO só em post com alcance >= 150 | Cumpre regra do CLAUDE.md | O corte só se conhece depois; o CTA já está gravado. Exige 2 versões de CTA ou legenda editável |
| B. Seguir + link na bio abaixo de 150 | Simples | 7 cliques em 30 dias [FATO]: caminho fraco e sem atribuição por nicho |
| C. Palavra por nicho | Atribuição limpa | Fere a regra de 1 palavra/mês; dilui aprendizado |
| D. Fora do óbvio: CTA gravado neutro ("comenta a sua profissão") + automação PostZen que responde qualquer comentário com a DM do TABULEIRO; palavra TABULEIRO só entra na legenda fixada quando o post passar 150 | Gera comentário (sinal de alcance) e lead com etiqueta de nicho automática | Comentário de "profissão" pode atrair curioso; precisa filtro manual |

**Posição:** A + D combinadas. Gravar o CTA final como "comenta a sua profissão que eu te mando o diagnóstico" (cumpre a regra, pois não cria palavra nova) e manter TABULEIRO como gatilho oficial na legenda quando o post passar 150. Automação responde em minutos. Prob. de >= 5 disparos e >= 2 diagnósticos até 18/11: 0,20 [0,08; 0,35]. Confiança 0,4. Premissa crítica: o PostZen permite automação disparada por qualquer comentário (sem dado; confirmar no listCommentAutomations, somente leitura). Se não permitir, volta para A pura.

### D4. Meta de seguidores
| Opção | 1ª ordem | 2ª ordem |
|---|---|---|
| A. Só orgânico | Custo zero | Meta de 30 líquidos é ~11% acima do ritmo bruto estimado |
| B. Orgânico + impulsionar o melhor | Mais alcance | Seguidor pago pode não virar lead; verba irreversível; teto sem dado |
| C. Não impulsionar e reduzir seguindo (3.523) | Melhora razão e percepção | Não mexe em seguidor ganho |
| D. Fora do óbvio: impulsionar não o reel, e sim o anúncio já existente do nicho vencedor apontando para DM, medindo custo por conversa | Testa lead direto, que é o gargalo | Precisa verba e aprovação; mistura objetivo |

**Posição:** A até D+7; D só com teto aprovado pelo Bruno. Prob. 0,40 [0,25; 0,55]. Confiança 0,35. Premissa: deixar de seguir não altera o ganho líquido medido.

## 4. Ideias e hipóteses numeradas (77)
Formato: ideia · confiança · evidência.
1. O gargalo é topo de funil, não atendimento · alta · 1 disparo e 7 cliques em 30 dias (contexto.md).
2. Planilha única de leads com colunas data, origem (post), nicho, canal, tempo de resposta, status, diagnóstico agendado, realizado, próximo passo · alta · sem registro hoje de diagnósticos (01-fatos, lacuna D3).
3. Medir tempo até primeira resposta humana; meta 15 min em horário comercial · média · [PRIOR] lead esfria; sem dado próprio.
4. Etiquetar o nicho no momento do primeiro contato · alta · D2 e D3 exigem atribuição por nicho.
5. UTM no link da bio por semana (utm_content=nicho do reel da semana) · média · 7 cliques sem origem (contexto.md).
6. Não construir chatbot multietapas nesta rodada · alta · volume de 1 disparo não justifica.
7. Registrar diagnóstico realizado como conversão offline manual na planilha; CAPI só após 10 eventos · média · [PRIOR] otimização exige volume.
8. Conferir no PostZen (leitura) se a automação TABULEIRO está ativa e em quais posts · alta · 1 disparo pode ser falha de configuração, não de interesse.
9. Hipótese: parte dos 7 cliques não achou caminho para agendar · baixa · sem dado de página.
10. CTA gravado único e igual ao gatilho da automação · alta · palavra digitada errada não dispara.
11. Aceitar variações (tabuleiro, Tabuleiro, TABULEIRO, com espaço) no gatilho · média · prática comum; confirmar no PostZen.
12. "Comenta a sua profissão" como CTA de alcance · média · comentário é sinal; F5 mostra 8 de 15 hooks nomeando profissão.
13. Resposta pública ao comentário em até 1 h para aumentar sinal do post · baixa · [PRIOR].
14. DM 1: agradece, pergunta o momento do negócio em 1 linha · média · [PRIOR] pergunta aumenta resposta.
15. DM 2 só após resposta: oferece diagnóstico de 30 min com link de agenda · média · porta de entrada existe (contexto.md).
16. DM sem número do case Tzur, para não soar promessa · alta · regra de texto.
17. DM específica por nicho em 1 frase (consórcio: venda um a um; nutri: prova sem antes e depois; dentista: curso) · média · F2, F3, F4.
18. Nutricionista: DM nunca pede ou comenta resultado de paciente · alta · Res. CFN 856 (F3).
19. Consórcio: DM nunca usa "contemplação" · alta · F2.
20. Dentista: DM não comenta procedimento clínico · alta · F4, CFO 196/2019 (secundária).
21. Mensagem 2 usa a única "não é X, é Y" do kit: "não é sobre ter mais pacientes, é sobre ter uma turma" · baixa · estilo; limite de 1 por peça.
22. Follow-up único em 24 h se o lead não responder; depois parar · média · [PRIOR] evita spam.
23. Lista de perguntas de qualificação: tem audiência? já vendeu curso? quantos seguidores? · média · ticket R$ 25 mil exige filtro (contexto.md).
24. Desqualificar com gentileza quem não tem audiência e oferecer conteúdo · média · ticket alto.
25. Medir taxa comentário para disparo por post · alta · base para D3.
26. Medir taxa disparo para resposta · alta · idem.
27. Medir taxa resposta para agendamento · alta · idem.
28. Medir agendado para realizado (no-show) · alta · idem.
29. Lembrete do diagnóstico 24 h e 1 h antes por DM manual · média · [PRIOR] reduz no-show.
30. Hipótese: alcance de 150 é atingido por 1 a 3 dos 5 reels · média · histórico de 127 a 307 com Bruno [ESTIMATIVA].
31. Se nenhum passar 150, TABULEIRO não aparece no mês; o caminho é a DM do "comenta profissão" · média · regra do CLAUDE.md.
32. Medir seguidores líquidos diários via ig_follower_growth desde D0 · alta · líquido sem dado hoje.
33. Registrar baseline de 7 dias antes do primeiro post · alta · sem baseline não há comparação.
34. Separar seguidor vindo de reel de nicho do vindo de outros posts: impossível com precisão; marcar como sem dado · alta · limitação da plataforma.
35. Usar visitas ao perfil por post como proxy de interesse · média · 448 visitas no período (contexto.md).
36. Hipótese: bio mencionar os 5 nichos aumenta clique · baixa · [PRIOR].
37. Destaque de stories "Diagnóstico" com o passo a passo · baixa · [PRIOR].
38. Stories diários com caixinha "qual sua profissão" alimentam a planilha · média · ritmo de stories diários (CLAUDE.md).
39. Fixar comentário do Bruno com a instrução do CTA · média · [PRIOR].
40. Não responder DM com áudio automático de voz sintética · alta · voz sintética teve 77% a 92% de pulo; [HIPÓTESE] rejeição se estende.
41. Responder com vídeo curto do Bruno gravado uma vez por nicho · média · Bruno em cena performa 2,4x a 5,8x.
42. Psicólogo como extra exige checar regra do CFP antes de publicar · alta · F1 sem regra verificada.
43. Advogado exige checar provimento da OAB sobre publicidade · alta · sem dado no livro de fatos.
44. Usar comentários de profissionais para escolher o 2º extra · média · D2 opção D.
45. Hipótese: consórcio gera mais lead qualificado porque o especialista vende produto financeiro e já pensa em funil · baixa · F2 (venda um a um é HIPÓTESE).
46. Hipótese: dentista gera mais comentário que lead · baixa · F5 alcance 78 a 494.
47. Hipótese: nutricionista tem dor nova e urgente com a CFN 856 · média · F3.
48. Se a CFN 856 não estiver vigente, mudar a frase do roteiro de "proibido" para "em discussão" · alta · vigência não confirmada.
49. Ordem dos fixos: nutricionista primeiro por urgência regulatória · baixa · F3; sem dado de alcance.
50. Alternativa: consórcio primeiro por mercado em alta medido · baixa · F2.
51. Publicar no melhor horário do ig_best_times · média · ferramenta disponível; dado não consultado.
52. Não publicar dois fixos no mesmo dia · alta · 3 posts/dia não aumentaram seguidores (CLAUDE.md).
53. Checar se anúncios existentes estão rodando e com qual verba (leitura) · média · anúncios criados (contexto.md); estado sem dado.
54. Se anúncio estiver rodando, conferir se o botão "Agendar diagnóstico" registra evento no pixel · média · mensuração.
55. Não ligar CAPI agora · média · volume baixo.
56. Criar público personalizado de quem engajou com os 5 reels para remarketing futuro, só com aprovação · baixa · verba sem dado.
57. Contar leads por nicho na semana 1 e semana 2 · alta · D2.
58. Regra PARAR: post com alcance < 53 e pulo > 75% em D+7 · média · abaixo da mediana atual.
59. Regra MANTER: alcance 53 a 105 · média · faixa entre mediana e meta.
60. Regra DOBRAR: alcance >= 150 ou >= 2 disparos no post · média · corte da TABULEIRO.
61. Regra TESTAR: alcance alto e 0 disparo, testar CTA novo · média · separa criativo de fluxo.
62. Se alcance for alto e disparo zero, o problema é CTA ou automação, minha cadeira assume · alta · diagnóstico de fluxo.
63. Se alcance for baixo e pulo alto, o problema é hook, não é da minha cadeira · alta · compensa ponto cego.
64. Teste de automação antes de publicar: comentário de conta de teste aciona DM? · alta · evita perder o primeiro dia; feito pelo Bruno.
65. Log semanal em semanas/AAAA-MM-DD.md com números do PostZen e Buzzfy · alta · CLAUDE.md.
66. Hipótese: 1 de cada 3 comentários vem de não profissional · baixa · [PRIOR].
67. Responder "sem dado" para métrica que falta no log · alta · CLAUDE.md.
68. Segunda rodada de reel com o vencedor de D1 em ângulo novo · média · Módulo 7.
69. "Se eu fosse [nicho]" como hook de teste para o vencedor · média · F5 aparece 3 vezes.
70. Duração 30 a 40 s · média · F5 reels good de perfil pequeno 21 a 37 s.
71. Legenda com 1 pergunta para gerar comentário · baixa · [PRIOR].
72. Não usar link encurtado sem UTM · média · perde atribuição.
73. Agenda do diagnóstico com campo obrigatório "profissão" · alta · atribuição.
74. Campo "como chegou" com opção do reel · média · conversão offline manual.
75. Reunião de 15 min no D+7 para ler números e decidir · média · Módulo 7.
76. Se em 18/11 houver 0 diagnóstico, rever oferta (diagnóstico gratuito pode ser pouco claro) e não o fluxo · média · compensa ponto cego.
77. Teto de tempo da minha cadeira: 2 h de configuração no total · alta · gargalo não é atendimento.

## 5. Pre-mortem (como meu plano fracassa)
- Os 5 reels ficam na faixa de 78 a 494 dos reels de saúde de terceiros [F5], perto do piso: não há comentário, a automação fica perfeita e ociosa. É o cenário da pergunta contrária.
- O CTA "comenta a sua profissão" gera comentário de curioso e a planilha enche de lead sem audiência, consumindo o Bruno.
- O PostZen não aceita gatilho genérico e a automação não dispara: perdemos a janela dos primeiros dias.
- O Bruno não responde em 15 min e o dado de tempo de resposta fica vazio.
- A planilha não é preenchida e voltamos a "diagnósticos sem dado" em 18/11.
- Excesso de regra de fluxo atrasa a gravação; o ponto cego vence.

## 6. Previsões numéricas
| Métrica | Valor previsto | Conferência |
|---|---|---|
| Disparos de automação somando os 5 reels | 3 [faixa 1 a 8] | D+30, 20/11/2026 |
| Diagnósticos agendados vindos dos 5 reels | 1 [0 a 3] | D+30, 20/11/2026 |
| Mediana de alcance dos 3 fixos em D+7 | 110 [60 a 200] | 11/11/2026 |
| Reels dos 5 com alcance >= 150 | 1 [0 a 3] | D+30 |
| Ganho líquido de seguidores em 14 dias | 28 [15 a 45] | 18/11/2026 |
| Tempo mediano até primeira resposta | <= 60 min | D+30 |
| Disparos acumulados no mês seguinte | 5 [2 a 12] | D+60, 20/12/2026 |
| Diagnósticos realizados acumulados | 3 [0 a 6] | D+90, 19/01/2027 |
| Vendas | 0 [0 a 1] | D+90, 19/01/2027 |
Todas são [ESTIMATIVA] a partir de base de 1 disparo/30 dias e histórico de 127 a 307 de alcance com o Bruno.

## 7. O que mudaria minha opinião
- Se o PostZen mostrar comentários com TABULEIRO que não dispararam: o problema era fluxo e minha cadeira sobe de prioridade.
- Se algum reel passar 300 de alcance com 0 disparo: CTA ou automação falha, não topo.
- Se houver >= 10 leads em 14 dias: vale chatbot de qualificação e CAPI.
- Se a CFN 856 for suspensa: muda a mensagem do nicho nutricionista.

**Lacunas:** diagnósticos realizados no período; ganho líquido de seguidores; teto de verba; configuração atual da automação PostZen (gatilho genérico possível?); estado e verba dos anúncios existentes; regra de publicidade de CFP e OAB; vigência da CFN 856; existência de trial reels na conta; tempo de resposta atual.

**Fontes:** /home/user/Disparo-/conteudo/modo-god-nichos/contexto.md; /home/user/Disparo-/CLAUDE.md; /home/user/Disparo-/conteudo/modo-god-nichos/run/01-fatos.md; run/01-pesquisa/F1 a F5 (resumos repassados no enquadramento). Nenhuma consulta nova a site ou conta foi feita por esta cadeira.
