# Decision Brief · Reel do dentista · O Estrategista · 21/10/2026

> Conselho de instâncias do mesmo modelo é autocrítica estruturada, não verificação independente. Concordância unânime pode refletir viés comum. Este documento reduz risco e explicita premissas; não garante resultado.

**NÃO CONVERGIU: D3**
**PRE-FLIGHT COM PENDÊNCIA** (a palavra "colegas" na fala e na legenda só vale se o Bruno for dentista inscrito em CRO; depende de resposta dele, 09-preflight.md)

Etiquetas: [FATO] com fonte; [ESTIMATIVA] com a conta; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, nível 4.

---

## 1. Resumo por decisão

| Decisão | O que fazer | Confiança | Prob. | Conferir em |
|---|---|---|---|---|
| D1 Áudio | Voz única nos 3 vídeos. Padrão: voz_master remasterizado (loudnorm 2 passadas, I -14, TP -1,5 antes do AAC). A cadeia_E só entra se vencer a regra fechada | **Baixa** (regra deu Média; rebaixei, motivo na seção 11) | 0,60 | 23/10/2026 |
| D2 Modelo A | Tzur v2 enxuto: P&B até o 474, 5 a 6 letreiros em y 300 a 400, legenda palavra a palavra, CTA digitado, sem confete, aplauso, tremida, RGB split ou prova inventada | **Baixa** | 0,38 | 05/11/2026 |
| D3 Modelos B e C | B em tela dividida (Bruno em tela cheia até 3 s), primeiro no direct, depois no feed se o A passar o corte de 48 h. C tipográfico só como amostra de 300 quadros em outubro e anúncio 4:5 depois de 18/11 | **Baixa**, não convergiu | 0,30 | 05/11/2026 |
| D4 Qual versão publicar e como medir | Exploratória, sem rótulo e sem recomendação | sem rótulo | sem dado | sem data |

O que depende do Bruno: escuta cega do áudio (10 min), aprovação de 3 stills (2 min), resposta sobre o CRO ("colegas"), 20 envios no direct (cerca de 30 min). Prazo das duas primeiras: 23/10.

## 2. Livro de fatos (o que sustenta as decisões)

- [FATO evidencias-J/teste_tp_aac.log; evidencias-K/tp_aac_teste.log] O AAC sobe o pico de 0,1 a 0,2 dB. Alvo de -1,5 dBTP termina em -1,3 depois do AAC.
- [FATO plano-M M1; evidencias-G/loudness_entregaveis_existentes.log] O voz_master mede -14,2 LUFS e -0,5 dBTP; o MP4 já entregue mede -0,3 dBTP. Reprova como está.
- [FATO evidencias-K/b02_trecho.log] No trecho da tese, o reconhecimento lê "forçar" com 0,45 no voz_master. [FATO evidencias-E/cadeia_E_medida.log] A cadeia_E, refeita do raw, lê "formar" com 0,93, mede -14,3 LUFS e -1,4 dBTP no m4a.
- [FATO evidencias-E/dr02_compara.log] Pelo método DR02, a distância média fala-pausa é 16,0 a 16,5 dB; a melhor pausa fica em 33,9 dB (voz_master) e 36,8 dB (cadeia_E). O corte de 40 dB é [PRIOR] e nenhuma versão o atinge por esse método.
- [FATO evidencias-K/ocupacao_mask.log] Faixa y 300 a 400: ocupação mediana da pessoa 0%, p90 29%. Faixa y 400 a 500: mediana 26,6%. Faixa livre total só entre y 120 e 300.
- [FATO CLAUDE.md] Reels com o Bruno falando: 2,4x a 5,8x a mediana. Animação com voz sintética: 0,15x a 0,8x, com 77% a 92% de pulo.
- [FATO 00-SISTEMA.md] Mediana de alcance da conta: 53. Os 3 reels do Bruno com dado: 126, 165 e 307.
- [FATO F32, ov2.html linhas 70 a 81] O bloco final do Tzur v2 fiel traz @ fictícios, o contador "1287 comentários", chuva de "R$", RGB split e tremida.
- [FATO evidencias-F/meta-ad-library-F-2026-10-21.md] 1.432 anúncios ativos de "curso para dentistas".
- [FATO F58] Maior reel de negócio para dentista no recorte Buzzfy: 764 views.
- [FATO F49, F10] O alex-prompter-997524 exige uma cena de prova; a única seria o case Tzur, que o Bruno não citou nesta tomada (contexto.md).
- [ESTIMATIVA F26] Render de 300 quadros do A: 0,752 s x 300, cerca de 226 s, contra portão de 452 s.
- Sem arquivo de origem: o par "106 de alcance e 68% de pulo" usado como corte de desempenho (05-debates/D2.md e D3.md). Tratado aqui como premissa, não como fato.

## 3. Opções e matriz

| Decisão | Opção | Votos finais (delphi) | Prob. mediana dos votantes [ESTIMATIVA, leitura de 04-votos.json] |
|---|---|---|---|
| D1 | 2 Remasterizar voz_master | 7 | 0,35 a 0,58 |
| D1 | 3 Refazer do raw (cadeia_E) | 5 | 0,12 a 0,60 |
| D1 | 5 Remaster com gate de escuta antes | 2 | 0,33 a 0,45 |
| D2 | 2 Tzur v2 enxuto | 12 | 0,30 a 0,45 |
| D2 | 4 Enxuto com camada de conversão ou marca | 2 | 0,35 a 0,40 |
| D3 | 2 B tela dividida, C tipográfico | 13 | 0,30 a 0,65 |
| D3 | 5 Variante com título de filtro no C | 1 | 0,55 |

Estatística por regra (08-confianca.json): D1 share 0,50, faixa 0,05 a 0,78, dispersão 0,48. D2 share 0,86, faixa 0,15 a 0,65, dispersão 0,15. D3 share 0,93, faixa 0,15 a 0,85, dispersão 0,35, marcada como rachada na faixa.

## 4. Dinâmica do conselho

Votos por opção nas três rodadas (14 cadeiras, 04-votos.json):

| Decisão | Primeiro | Final | Delphi |
|---|---|---|---|
| D1 | 2: 8 · 3: 4 · 5: 2 | 2: 8 · 3: 4 · 5: 2 | 2: 7 · 3: 5 · 5: 2 |
| D2 | 2: 7 · 4: 6 · 1: 1 | 2: 9 · 4: 5 | 2: 12 · 4: 2 |
| D3 | 2: 9 · 5: 5 | 2: 11 · 5: 3 | 2: 13 · 5: 1 |

Mudanças e o fato que as causou:
- B, D3, de 5 para 2: reacts imitam prova social (F32); o título que filtra põe uma segunda variável no post; a máscara limita o letreiro a y 300 a 400.
- H, D2, de 1 para 2: o Tzur fiel tem itens banidos e a ocupação em y 300 a 560 é alta.
- I, D3, de 5 para 2 (final) e de volta para 5 (delphi): primeiro aceitou o título como teste isolado; depois propôs o título só no direct, sem gastar slot do feed. Única cadeira que oscilou.
- N, D2, de 4 para 2: escurecer o fundo pela máscara levaria o risco de halo a 100% do vídeo.
- No delphi: C (D3, 5 para 2) pela ocupação medida; D (D2, 4 para 2; D3, 5 para 2) pelo título como hipótese e pela saída do alex-prompter; G (D2 e D3 para 2) porque as travas de conformidade entraram na opção 2; J (D2, 4 para 2) pela exposição ao halo; H (D1, 2 para 3) ao conhecer a cadeia_E.
- Mudanças anuladas por falta de fato novo: 0.

Leitura: em D1 o debate moveu um voto só, e para o lado da minoria (H, de 2 para 3, ao conhecer a cadeia_E). A divergência é de premissa, não de informação.

## 5. Onde concorda e em que premissa

- D1: 12 de 14 limitam em -1,5 dBTP antes do AAC e aceitam só no MP4 final. As 14 tratam o corte de 40 dB como [PRIOR] inalcançável pelo método DR02. Premissa: os dois testes independentes de AAC (J e K) e o fato de o DR02 medir cauda de palavra como ruído.
- D2: 12 de 14 no enxuto. Premissa: o Bruno em cena é o único formato com base medida na conta, e o fiel tem itens banidos ou inventados.
- D3: 13 de 14 na opção 2, um modelo por vez no feed. Premissa: os 3 modelos repetem a mesma fala de 36 s e só a tela dividida atende ao pedido literal do Bruno ("dividindo com reacts").

## 6. Onde diverge e o que resolveria

- D1: origem da voz (voz_master, 7 votos, contra raw/cadeia_E, 5). Resolve: WER da cadeia_E, escuta cega de 10 min do Bruno e transcrição de um ouvinte leigo de 24,94 a 29,04 s.
- D2: camada de conversão ou marca na tela (opção 4) e a faixa do letreiro. Resolve: fração de comprador na DM em D+7 (abaixo de 20%, o título que filtra vira teste isolado); a ocupação medida já fechou a faixa em y 300 a 400.
- D3: qual formato vai primeiro ao feed, se há reacts e se o B depende do direct. Resolve: corte de 48 h do A (alcance 68 ou mais e pulo abaixo de 68%) e o direct pareado com 10 envios por braço.

## 7. Minoria vencedora

O presidente marcou as três recomendações como minoria vencedora: o texto final incorpora condições que vieram de cadeiras derrotadas.
- D1: a regra A/B com a cadeia_E como desafiante e o ouvinte leigo vêm das cadeiras E, F, G e K (opção 3) e da I (gate de escuta). Sem elas, a recomendação seria só o remaster.
- D2: as perguntas fixas na DM e a coluna de lead qualificado vêm de D e I (opção 4).
- D3: a lista branca fechada, a proibição de @, contador e balão e o grep T01 a T12 vêm de G (opção 5).

## 8. Red team (07-redteam.md)

Pre-mortem, os que mais pesam:
- Nenhum lead qualificado: alcance de 34 a 95 e cerca de 1 comentário esperado [ESTIMATIVA PF D2], então a fração de comprador nunca pode ser lida.
- Decisão de formato por ruído: corte de 48 h com N = 1 por formato premia ou mata por sorte.
- Automação errada: a tela pede DENTISTA e a fala pede "a sua profissão" (F11); a regra CASE do PostZen manda DM sobre Tzur.
- Cronograma engolido pelo consórcio de 27/10 na mesma máquina de 4 vCPU sem GPU (F21, F28).
- Bruno aprovador único de stills, áudio, CRO e regra CASE.
- "formar quem disputa" ouvido como "forçar" (F08).

Piores casos: ouvinte "leigo" da agência aprova o voz_master e o público ouve "forçar"; nenhuma versão fecha -1,0 dBTP e a regravação de 26/10 colide com o consórcio; halo passa nos 3 stills e aparece nos 44 quadros com segundo componente (F30); A fica abaixo de 34 por acaso e sai do nicho com N = 1; B vai ao feed sem esperar o direct e repete o pulo de animação; anúncio 4:5 do C é reprovado ou entrega caro.

Premissas de alto impacto FRÁGEIS: letreiro 3D melhora retenção (nível 4); comentário vira DM e DM vira lead (nível 4); CTA escrito e falado diferentes não confundem (nível 1); tela dividida não repete o fracasso da animação (nível 1); existe demanda paga de dentista que quer lançar curso conosco (nível 4).

Cisnes negros: nova resolução do CFO sobre publicidade (F75), mudança de algoritmo, perda de acesso à conta ou à automação, reel viraliza entre pacientes e a automação manda oferta para paciente.

## 9. Sensibilidade

| Premissa | Valor atual | Vira quando | Vira na faixa plausível? |
|---|---|---|---|
| Leads qualificados esperados por reel | cerca de 1 comentário [ESTIMATIVA]; fração qualificada sem dado | abaixo de 1 lead esperado o plano não gera dado de conversão: troca para reel simples já e DMs ativas | sim |
| Corte de 48 h separa formato de ruído | 68 ou mais, base 34 | se p10 a p90 dos 18 reels cobrir 34 a 68, o corte não discrimina: 3 a 4 reels por formato ou retenção no segundo 5 | sim |
| Ganho do Bruno em cena vale com rosto reduzido no B | B com tela cheia em cerca de 28% a 33% [ESTIMATIVA] | pulo do B de 77% ou mais: B não vai ao feed | sim |

As três viram dentro da faixa plausível. Por isso nenhuma decisão de desempenho passa de Baixa.

## 10. Lacunas

14 lacunas tratadas (08-lacunas.md). Continuam abertas:
- WER da cadeia_E: sem dado.
- Escuta humana do trecho 24,94 a 29,04 s: sem dado.
- TP no MP4 com música e SFX: sem dado.
- Halo da máscara nos stills: sem dado.
- Tempo de render do C: sem dado (nunca cronometrado). Render do B: 887 s, só [ESTIMATIVA].
- Origem do corte "106 / 68%": sem arquivo.
- Origem do lead na página de destino (o=ig-dentista não é lido, M5): sem dado.
- Desempenho do formato Tzur v2 na conta: sem dado (nunca publicado, F19).
- Inscrição do Bruno em CRO: pendência do pre-flight.
- 3 números sem fonte restantes em D1 (motivo da regra de confiança).

## 11. Recomendação, primeira ação, abandono e conferência

### D1 Áudio · confiança Baixa (regra: Média)
Rebaixei de Média para Baixa: o voto está rachado 7 contra 5, a faixa vai de 0,05 a 0,78, e a premissa que separa as duas opções (ouvinte leigo distingue "formar" de "forçar" como o público) tem evidência nível 4.
- Recomendação: uma voz para os 3 vídeos. Padrão provisório: voz_master com highpass 80 Hz, de-esser, EQ de presença, expansor híbrido, loudnorm em duas passadas (I -14, TP -1,5) antes do AAC. A cadeia_E substitui só se fizer WER até 0,086, vencer a escuta cega do Bruno (ouvinte leigo desempata) e fechar TP de -1,0 ou menos no MP4 com música. Aceite medido em cada MP4 final.
- Primeira ação: rodar o WER da cadeia_E, medir os dois m4a e montar o par cego. Dono: agência (áudio); escuta do Bruno. Prazo: 2 dias. Custo: zero [ESTIMATIVA].
- Teste mais barato: escuta cega de 10 min mais transcrição de 5 min do ouvinte leigo. O ouvinte tem de ser de fora da agência (red team).
- Dado que muda: WER da cadeia_E acima de 0,086; ouvinte leigo escreve "forçar" no voz_master; chiado audível nas pausas da cadeia_E.
- Abandono: se em 23/10/2026 nenhuma versão fechar TP de -1,0 dBTP ou menos no MP4 com música, ou se o Bruno reprovar as duas, usar o original do celular ou regravar a tomada inteira em 26/10.
- Previsão: 3 de 3 MP4 entre -15 e -13 LUFS e TP de -1,0 ou menos, aprovados de primeira (faixa 2 a 3 de 3), probabilidade 0,60. Conferir em 23/10/2026.

### D2 Modelo A · confiança Baixa
- Recomendação: Tzur v2 enxuto. P&B só até o 474, 5 a 6 letreiros 3D em y 300 a 400, legenda palavra a palavra, 1 b-roll desenhado, CTA digitado. Sem confete, aplausos, tremida, RGB split e prova inventada. Portões antes do render cheio: comp.py corrigido, 300 quadros contra 452 s, 3 stills aprovados. Perguntas fixas na DM e coluna de lead qualificado na planilha.
- Primeira ação: corrigir o comp.py e renderizar 300 quadros cronometrados. Dono: agência; stills aprovados pelo Bruno. Prazo: 2 dias (até 23/10).
- Dado que muda: halo em 2 de 3 stills (letreiro vai para y 120 a 220, sem máscara) ou 300 quadros acima de 452 s (composição passa para o ffmpeg).
- Antes de publicar, pelo red team: alinhar CTA da tela e da fala (DENTISTA contra "a sua profissão") e conferir a regra CASE do PostZen.
- Abandono: se em 05/11/2026 o alcance ficar abaixo de 34 e o pulo acima de 77%, o formato sai do nicho.
- Previsão: alcance em 7 dias (ig_post_stats) de 95, faixa 40 a 250, probabilidade 0,38. Conferir em 05/11/2026.

### D3 Modelos B e C · confiança Baixa · NÃO CONVERGIU
- Recomendação: B em tela dividida (sab8a-475686, twoclipping-000267, stokebuilder-356793 adaptado, seek(t) do gdgtify-929495), com até 3 reacts vetoriais da lista branca, sem @, contador ou balão. Vai ao direct na semana de 29/10 e ao feed no slot seguinte só se o A passar o corte de 48 h. C é o prédio de palavras (gdgtify-929495 com twoclipping-000267), sem alex-prompter-997524: em outubro só a amostra de 300 quadros; anúncio 4:5 depois de 18/11, após conferir a Res. CFO 196/2019.
- Primeira ação: consultar ig_post_stats dos 3 reels do Bruno e montar a planilha pareada. Dono: agência (render e planilha); envios pelo Bruno. Prazo: 6 dias.
- Teste mais barato: consulta Buzzfy de 5 min, planilha de 10 min, 20 envios no direct (cerca de 30 min do Bruno) e 300 quadros do C (cerca de 15 min de máquina, [ESTIMATIVA]).
- Dado que muda: render do C projetado acima de 60 min; pulo do B no feed acima de 77%; Res. CFO e Ad Library contrárias ao anúncio.
- Abandono: se em 05/11/2026 o B no feed tiver alcance abaixo de 34 ou pulo acima de 77%, a tela dividida fica só no direct.
- Previsão: alcance em 7 dias do B no feed de 70, faixa 25 a 200, probabilidade 0,30. Conferir em 05/11/2026.
- Por que não convergiu: o share é alto (0,93), mas as probabilidades vão de 0,15 a 0,85. Parte das cadeiras pontuou só produção, parte somou desempenho. O número de 0,30 do presidente mede desempenho no feed, não produção.

### D4 Qual versão publicar e como medir · exploratória
Sem recomendação e sem rótulo. Fica registrada a regra que já sai de D2 e D3: um modelo por vez no feed, direct pareado só para escolher texto de abertura, nunca formato (premissa de 10 envios por braço é FRÁGIL).

## 12. Log de convergência e chamadas

- Rodadas: primeiro voto, voto final depois do debate, delphi.
- D1: convergiu pela regra; placar 8, 4, 2 nas duas primeiras rodadas e 7, 5, 2 no delphi.
- D2: convergiu, de 7 para 12 votos na opção 2.
- D3: não convergiu; share subiu de 9 para 13, faixa de probabilidade continuou larga (0,15 a 0,85).
- Mudanças registradas: 4 na rodada final, mais as do delphi; anuladas sem fato novo: 0.
- Chamadas de modelo até aqui: 104. Falhas: 0 (nenhuma).

## 13. Fontes

- /home/user/Disparo-/CLAUDE.md
- /home/user/Disparo-/conteudo/sistema-instagram/00-SISTEMA.md
- /home/user/Disparo-/videos/nichos/dentista/god/contexto.md
- run/00-enquadramento.md, run/01-fatos.md, run/02-cadeiras/ (planos A a N e evidencias-C, E, F, G, H, J, K), run/03-julgamento/ (J1, J3, J4), run/05-debates/D1.md, D2.md, D3.md, run/06-plano-final.md, run/07-redteam.md, run/08-lacunas.md, run/09-preflight.md
- run/04-votos.json, run/08-confianca.json
- Logs citados: evidencias-J/teste_tp_aac.log, evidencias-K/tp_aac_teste.log, evidencias-K/b02_trecho.log, evidencias-K/ocupacao_mask.log, evidencias-E/cadeia_E_medida.log, evidencias-E/dr02_compara.log, evidencias-G/loudness_entregaveis_existentes.log, evidencias-H/medicoes-H.txt, evidencias-F/meta-ad-library-F-2026-10-21.md
- Buzzfy ig_post_stats, consulta de 21/10/2026 (citada nos planos D e E)
- videos/cases/tzur/ov2.html, linhas 70 a 81
