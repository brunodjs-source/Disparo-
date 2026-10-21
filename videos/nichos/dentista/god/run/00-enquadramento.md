# 00 · Enquadramento · Reel do dentista · Agência Reunida Modo GOD · 21/10/2026

Cliente: O Estrategista (@o_estrategista.com.br). Cadeira: ENQUADRADOR.
Etiquetas: [FATO] com fonte · [ESTIMATIVA] com conta · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, nunca fecha objeção sozinho.

## 0. Fatos de partida (conferidos nesta rodada)

| Item | Valor | Fonte |
|---|---|---|
| Bruto | selfie vertical 576x1024, 31,6 fps, 36,4 s | [FATO] contexto.md |
| Áudio bruto | -32,6 LUFS integrado, true peak -10,1 dBTP, LRA 3,2 LU | [FATO] ffmpeg loudnorm em raw.wav, 21/10/2026 |
| Áudio já tratado | -14,2 LUFS integrado, true peak -0,5 dBTP, LRA 1,6 LU, 36,44 s | [FATO] ffmpeg loudnorm e ffprobe em voz_master.wav, 21/10/2026 |
| Última palavra | "respondo." de 35,36 a 35,92 s | [FATO] words-raw.json |
| Trecho com fala truncada | 24,94 a 29,04 s: "deixa disputar, paciente passa a forna que a gente disputa" (o roteiro previa "deixa de disputar paciente e passa a formar quem disputa"). "que a gente" tem 0,04 s por palavra no alinhamento | [FATO] words-raw.json. Se é erro de fala ou de transcrição: sem dado (precisa ouvir) |
| "em Brasil" (4,80 a 5,16 s) | fala diz "em Brasil", roteiro dizia "no Brasil" | [FATO] words-raw.json |
| 474 mil dentistas ativos | 474.640 e 474.659 em leituras de 21/10/2026 | [FATO] tabela CFO, citada em conteudo/modo-god-nichos/run/06-plano-final.md seção 1 (F4) |
| Case Tzur | o Bruno não cita o Tzur nesta tomada | [FATO] contexto.md |
| Mediana de reel da conta | 53 de alcance, 74 views, 6,2 s assistidos, 68% de pulo | [FATO] 00-SISTEMA.md linha 20 (Buzzfy, 17 reels) |
| Bruno em cena | 2,4x a 5,8x a mediana; melhor reel 307 de alcance, 18,6 s assistidos, 53% de pulo | [FATO] CLAUDE.md e 00-SISTEMA.md linha 34 |
| Meta do reel do dentista | 106 de alcance; publicação prevista qui 29/10/2026 | [FATO] 06-plano-final.md seção 1 e 2.2 |
| Verba | zero até 18/11/2026 | [FATO] 06-plano-final.md linha 236 |
| Desempenho do formato "letreiro 3D atrás + b-roll + reacts" (case Tzur v2) | sem dado: nenhuma métrica do case Tzur v2 publicada em conteudo/sistema-instagram/semanas/ | [FATO] busca nos arquivos da conta, 21/10/2026 |

## 1. Pesos da matriz (fixados antes das opções)

| Critério | Peso |
|---|---|
| Impacto | 25 |
| Probabilidade | 20 |
| Evidência | 20 |
| Custo e reversibilidade | 15 |
| Tempo até o primeiro sinal | 10 |
| Risco | 10 |
| **Total** | **100** |

Motivo de manter o padrão: é o mesmo conjunto usado no plano dos 5 nichos (06-plano-final.md), o que deixa as decisões comparáveis. Nenhum critério ganhou motivo escrito para mudar. Observação para quem pontua: em D1 a evidência é medição técnica (ffmpeg), em D2 a D4 a evidência de desempenho do formato editado é sem dado, então "evidência" vai pesar contra qualquer opção que dependa de efeito não medido.

## 2. Decisões

### D1 · Áudio masterizado
- **Afirmação falsificável:** entregar a voz final de cada um dos 3 vídeos em -14 LUFS integrado (tolerância de 1 LU), true peak até -1,0 dBTP, sem ruído de fundo audível nas pausas e com trilha e SFX abaixo da voz produz um áudio aprovado pelo Bruno de primeira, medido por ffmpeg loudnorm no arquivo final de cada modelo e pela aprovação escrita do Bruno, até 23/10/2026.
- **Critério de sucesso:** 3 de 3 arquivos finais medem entre -15 e -13 LUFS e true peak até -1,0 dBTP; ruído nas pausas (por exemplo 13,84 a 14,08 s e 20,10 a 20,44 s) pelo menos 40 dB abaixo da voz [PRIOR: corte sem origem medida]; voz acima da trilha em todo trecho falado; zero pedido de refazer áudio.
- **Opções iniciais:**
  1. Usar voz_master.wav como está (-14,2 LUFS, mas true peak -0,5 dBTP, acima do alvo de -1,0 [PRIOR: alvo comum de plataformas, o Instagram não publica especificação]).
  2. Remasterizar a partir de voz_master.wav: limitador em -1,0 dBTP, de-esser leve, EQ de presença, e mixar trilha com ducking e SFX por cima, medindo de novo no arquivo final.
  3. Refazer a cadeia a partir de raw.wav comparando as 3 reduções de ruído já geradas (rn_std, rn_sh, rn_bd) antes de masterizar.
  4. Pedir ao Bruno uma regravação do trecho 24,94 a 29,04 s (fala truncada), só para áudio.
- **Decidível:** sim.
- **Custo de reverter:** baixo. raw.wav e voz_master.wav ficam intactos; refazer é rodar a cadeia de novo [ESTIMATIVA: minutos de processamento, sem conta de tempo medida].

### D2 · Modelo A (o que já fazemos, estilo case Tzur v2)
- **Afirmação falsificável:** editar o bruto no pipeline do case Tzur v2 (videos/cases/tzur: letreiro 3D atrás da pessoa por segmentação rembg com camada de trás e da frente, b-roll nos cortes com 0,30 s de respiro, reacts e bloco final cinematográfico) produz um reel 1080x1920 com o rosto do Bruno visível de 0 a 3 s, que, se publicado em 29/10/2026, passa da mediana da conta: alcance de 106 ou mais e pulo abaixo de 68%, medido por ig_post_stats (Buzzfy) até 05/11/2026.
- **Critério de sucesso:** produção: render 1080x1920 sem quebrar fala; rosto visível em 0 a 3 s e na maior parte do vídeo [HIPÓTESE de corte: 80% do tempo, a fixar no plano]; zoom no rosto até 1,25x; letreiro nunca cobre olhos e boca; lista de edição quadro a quadro alinhada a words-raw.json. Desempenho (se publicado): alcance de 106 ou mais e pulo abaixo de 68% em 7 dias.
- **Opções iniciais:**
  1. Tzur v2 fiel (abertura manifesto P&B que vira colorido no número 474 mil, letreiro 3D atrás, b-roll, reacts, bloco final), com o Bruno em cena desde o frame 0.
  2. Tzur v2 enxuto: sem abertura manifesto, letreiro 3D só nos 4 momentos fortes (474 mil, hora de cadeira, ensinar o seu colega, segundo produto), b-roll só nos cortes.
  3. Tzur v2 fiel mais legenda palavra a palavra embaixo (cap2.js).
- **Decidível:** sim para a produção. O desempenho só é decidível se o Modelo A for o publicado (ver D4).
- **Custo de reverter:** baixo antes de publicar (é só render). Depois de publicado: arquivar o reel é possível, mas a distribuição e o dado de pulo já gastos não voltam [HIPÓTESE sobre efeito na conta: sem dado].

### D3 · Modelos B e C (quais formatos novos, misturando o repositório)
- **Afirmação falsificável:** escolher para B e C dois formatos que mudam a forma da edição e preservam o rosto do Bruno (candidatos já lidos: sab8a-475686, gdgtify-929495, twoclipping-000267, alex-prompter-997524) produz duas peças em que um júri cego de 3 cadeiras do conselho dá nota de clareza da mensagem e acabamento "profissional estilo After Effects" igual ou maior que a do Modelo A, e que, se uma for publicada, passa de 106 de alcance e de 68% de pulo, medido por ig_post_stats até 05/11/2026.
- **Critério de sucesso:** cada modelo cita os ids dos prompts misturados e o que foi aproveitado e descartado; rosto visível de 0 a 3 s; nenhum item da lista de banidos do twoclipping-000267 (shockwave, partículas, RGB split, camera shake, lens flare, neon) sem motivo escrito; 1080x1920, cerca de 36 s, nenhuma palavra cortada; lista de edição quadro a quadro. Nota do júri: [HIPÓTESE] o júri cego mede acabamento, não conversão.
- **Opções iniciais:**
  1. B = talking head punchy com tipografia cinética arquitetônica (sab8a-475686 mais gdgtify-929495, com o momento de quietude de 400 ms em "Qual é?", 20,10 a 20,64 s). C = explainer em 5 cenas sobre o rosto (alex-prompter-997524: problema, o que eu faço, passos, prova, nome) com máscara de tipo e match cut de twoclipping-000267.
  2. B = tela dividida: Bruno numa metade e reacts ou animação representando a fala na outra (atende "dividindo com reacts"). C = tipografia cinética arquitetônica (gdgtify-929495).
  3. Um só modelo novo agora (B) e C só depois de ler o resultado do primeiro reel publicado.
  4. Não fazer B e C agora.
- **Decidível:** sim para a produção e a nota do júri. A comparação de desempenho entre A, B e C é exploratória (decidivel parcial): com uma postagem por nicho, N = 1 por modelo, não separa efeito do formato do efeito do dia [HIPÓTESE].
- **Custo de reverter:** baixo antes de publicar. Custo de tempo de produção: sem dado (nenhum render deste pipeline foi cronometrado nos arquivos).

### D4 · Qual versão publicar e como medir (exploratória)
- **Afirmação falsificável:** publicar um único modelo como reel principal em qui 29/10/2026 e guardar os outros dois como variante produz uma leitura de desempenho limpa (alcance, views assistidas, pulo e comentários "dentista" em 7 dias), medida por ig_post_stats e listCommentAutomationLogs até 05/11/2026; publicar os 3 do mesmo bruto na mesma conta reduz o alcance de cada um [HIPÓTESE, sem precedente na conta].
- **Critério de sucesso:** reel principal com alcance de 106 ou mais, pulo abaixo de 68% e ao menos 1 conversa qualificada de dentista em 7 dias [meta de conversa: PRIOR, o plano não fixa número]. Se ficar abaixo de 53 de alcance em 48 h, o próximo nicho não usa esse modelo.
- **Opções iniciais:**
  1. Publicar só o modelo que o conselho pontuar mais alto; os outros ficam no arquivo para outro nicho.
  2. Publicar o principal como reel e testar um segundo modelo como trial reel (só não seguidores), se a conta tiver o recurso [sem dado: não consultado].
  3. Publicar os 3 em dias diferentes.
  4. Não publicar agora: entregar os 3 e o Bruno escolhe.
- **Decidível:** não (exploratória). Agentes não publicam nem agendam; a decisão final é do Bruno. N = 1 e muitos fatores mudando juntos.
- **Custo de reverter:** desconhecido. Reel publicado pode ser arquivado, mas o efeito de 2 ou 3 versões do mesmo bruto na distribuição da conta não tem dado.

## 3. Perguntas que todo plano de cadeira precisa responder

1. Qual modelo (A, B ou C) a cadeira defende e quais ids de prompt do repositório entram, com o que é aproveitado e o que é descartado?
2. O rosto do Bruno aparece de 0 a 3 s? Em que porcentagem do tempo total? Zoom máximo no rosto (limite 1,25x)?
3. Lista de edição quadro a quadro: para cada evento, início e fim em segundos e em frame (a 30 fps de saída), palavra de words-raw.json que dispara, camada (atrás da pessoa, frente, tela cheia, tela dividida), texto na tela, animação, SFX.
4. Como trata o trecho 24,94 a 29,04 s ("forna que a gente disputa"): legenda fiel ao que foi dito, legenda corrigida (risco de não bater com a boca), corte de palavra (proibido: nunca cortar fala) ou regravação?
5. "em Brasil" (4,80 a 5,16 s): a legenda escreve o que foi dito ou corrige para "no Brasil"?
6. Número 474 mil na tela: com fonte "CFO, out/2026" em rodapé ou texto genérico?
7. Áudio: cadeia exata, alvo -14 LUFS e true peak até -1,0 dBTP, nível da trilha, ducking, SFX e medida no arquivo final.
8. Upscale de 576x1024 para 1080x1920: método, risco de artefato no rosto e no recorte rembg.
9. Pipeline: só ferramentas que já existem (Playwright + Chromium, ffmpeg, numpy, rembg, faster-whisper, HTML/Canvas/SVG/Three.js). Nada novo instalado. Tempo de render: estimativa com conta ou sem dado.
10. CTA: "Dentista, comenta a sua profissão aqui que eu te respondo" (já gravado). Texto na tela "Comenta: dentista"? A regra TABULEIRO só entra com alcance de 150 ou mais.
11. Conselho de classe (publicidade odontológica): sem boca, procedimento, antes e depois, promessa de resultado ou preço. Resolução CFO 196/2019 com texto oficial não aberto (06-plano-final.md seção 2.2).
12. Prova: o Tzur não foi dito. A cadeira põe o case na tela ou não? Se sim, com qual autorização (06-plano-final.md seção 7, item 5)?
13. Qual métrica, de onde vem, em que data é lida e qual o critério de parar?
14. Regras de texto: português do Brasil, sem travessão, sem emoji, no máximo uma frase "não é X, é Y", sem citar HighClass, Júnior Prazeres ou Felipe Roser.

## 4. Checklist literal do pedido do Bruno (o crítico de lacunas cobra cada item)

1. "melhore o audio"
2. "tire ruido e fundo do audio"
3. "deixe ele totalmente masterizado"
4. "faça o video no modo que [...] vai atrair conversão"
5. "saindo letreiro 4d atras" (leitura do conselho: letreiro com profundidade saindo de trás da pessoa)
6. "dividindo dela com reacts" (leitura do conselho: dividir a tela ou o vídeo com reacts; ambíguo, cada plano diz qual leitura usou)
7. "animações que representa" (animação que representa o que está sendo dito)
8. "precisa ser algo profissional estilo adobe effects" (After Effects)
9. "toma a decisão correta de quais os formatos fazer"
10. "ative a agencia modo god para tomar as decisões"
11. "pode misturar modelos de videos que estão no repositorio" (github.com/yihui-dev/awesome-opus5-5-videos/tree/main/prompts)
12. "faça um modelo no que ja fazemos"
13. "faça outros 2 no que voces pensam"

Itens acrescentados pelo enquadramento (não ditos pelo Bruno, vêm da tarefa computada): lista de edição quadro a quadro para cada modelo, alinhada aos tempos da transcrição; 3 vídeos de cerca de 36 s em 1080x1920 do mesmo bruto.

## 5. Gatilhos de escalada

| Gatilho | Presente? | Onde |
|---|---|---|
| Custo de reverter desconhecido | Sim | D4 (efeito de várias versões do mesmo bruto na distribuição) |
| Compromisso com terceiros | Parcial | Não há preço, contrato ou anúncio pago. Há exposição regulatória (publicidade odontológica, CFO 196/2019 não lida no oficial) e a promessa "eu te respondo" no CTA, que exige resposta manual |
| Vários fatores mudando ao mesmo tempo | Sim | Nicho novo, 3 estilos de edição, letreiro 3D, tela dividida e CTA na mesma rodada |
| Sem precedente na conta ou no mercado | Sim | Formato Tzur v2 sem métrica publicada na conta; primeiro reel do nicho dentista |
| Verba acima do teto do Bruno | Não | Verba zero até 18/11/2026 |

**Modo sugerido: god.** Três gatilhos presentes, e o Bruno pediu o modo god de forma explícita.
