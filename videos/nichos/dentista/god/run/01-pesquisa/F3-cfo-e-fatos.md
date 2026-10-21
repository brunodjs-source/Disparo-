# F3 · CFO e fatos · número de dentistas e regras de publicidade para o reel do dentista

Cliente: O Estrategista (@o_estrategista.com.br). Frente F3 da pesquisa do conselho Agência Reunida, 21/10/2026.
Etiquetas: [FATO] com fonte · [ESTIMATIVA] com conta · [HIPÓTESE] a testar · [PRIOR] palpite do modelo, nunca fecha objeção sozinho.
Escopo: somente leitura (GET em páginas públicas do CFO). Nada foi clonado, instalado, enviado ou preenchido. Cópias das fontes lidas estão em `run/01-pesquisa/evidencias-F3/`.

## 0. Resposta curta

1. O número do Bruno confere. São **474.659 cirurgiões-dentistas ativos** na soma das 27 linhas da tabela oficial do CFO lida em 21/10/2026 às 16:40 UTC. "Mais de 474 mil" pode ir para a tela com a fonte "CFO, out/2026".
2. Nenhuma norma do CFO de 2025 ou 2026 mudou o capítulo de publicidade do Código de Ética além da Resolução 271/2025 (que mexeu em cartão de desconto e aliciamento por telemarketing). A Resolução 196/2019 continua sendo a regra de imagem (selfie, diagnóstico e conclusão; vedado o transcurso do procedimento).
3. O reel fala de negócio com dentistas e não mostra paciente nem procedimento. Pelas regras lidas, o risco fica em três pontos: imagem clínica no b-roll, promessa de resultado (financeiro ou clínico) e preço ou gratuidade. Todos são evitáveis na edição.

## 1. Verificação das fontes

| Fonte | Como conferi | Resultado |
|---|---|---|
| Tabela "Quantidade Geral de Profissionais e Entidades Ativas" (website.cfo.org.br/estatisticas/quantidade-geral-de-entidades-e-profissionais-ativos/) | GET com curl, duas leituras; parse das 27 linhas do array da tabela no HTML | [FATO] HTTP 200. Rodapé "Última atualização WSCFO: 21/10/2026". A página não exibe total nacional; o total abaixo é a soma das 27 linhas. Leitura às 16:40 UTC: CD 474.659 nas duas leituras desta frente |
| Tabela de especialistas (website.cfo.org.br/estatisticas/quantidade-geral-de-cirurgioes-dentistas-especialistas/) | GET e parse | [FATO] HTTP 200, colunas "Especialidade, Feminino, Masculino, Total", linha "TOTAL GERAL" |
| Tabela por ano de inscrição (website.cfo.org.br/dados-estatisticos-de-profissionais-e-entidades-ativas-por-ano/) | GET e parse | [FATO] HTTP 200; o HTML só traz o ano 2026 carregado (196 linhas) |
| Resolução CFO-SEC-196/2019 | GET em sistemas.cfo.org.br/visualizar/atos/RESOLUÇÃO/SEC/2019/196 (PDF) e pdftotext | [FATO] texto oficial lido, 6 artigos |
| Código de Ética Odontológica, Res. CFO-118/2012 | PDF oficial em website.cfo.org.br/wp-content/uploads/2018/03/codigo_etica.pdf (link da página website.cfo.org.br/codigos/) | [FATO] lido. Atenção: o PDF é a redação original de 2012 (metadado de criação 18/07/2012). Não incorpora a Res. 271/2025 |
| Resolução CFO-SEC-271/2025 | GET no sistema de atos | [FATO] lida. Altera art. 20 VIII e X, revoga art. 32 XIII, altera art. 44 XIV |
| Decisão CFO-SEC-05/2025 | GET no sistema de atos | [FATO] lida. Cria grupo para reescrever o capítulo de publicidade e prevê "minuta com o texto do novo capítulo" |
| Varredura das resoluções 2025 e 2026 | GET nas numerações 255 a 330 de 2025 e 2026 e 1 a 30, leitura do título da 1ª página de cada PDF | [FATO] existem de 268 (09/01/2025) a 308 (29/09/2026). Nenhum título trata de anúncio, propaganda ou publicidade. Busca textual por "publicidade, propaganda, anúncio, redes sociais" em todas: só ocorrências no sentido de princípio administrativo, mais a Res. 286/2026 art. 16 (curso com paciente, ver seção 3) |
| Resolução 295/2026 | 1ª tentativa | ERRO: timeout de 20 s. 2ª tentativa: HTTP 200, PDF lido (sedação; sem regra de publicidade) |
| Resolução CFO-63/2005 (Consolidação das Normas) | GET no sistema de atos | ERRO parcial: HTTP 200, mas o PDF tem 54 linhas (só cabeçalho). Texto consolidado não lido |
| Lei 5.081/1966 (planalto.gov.br/ccivil_03/leis/l5081.htm) | curl e WebFetch | ERRO: resposta vazia no curl e HTTP 503 no WebFetch. Não lida. Nada desta lei é usado como fato aqui |

## 2. Números

### 2.1 Cirurgiões-dentistas ativos

| Recorte | Valor | Etiqueta |
|---|---|---|
| CD ativos, soma dos 27 CROs | **474.659** | [FATO] tabela CFO, 21/10/2026 16:40 UTC, `evidencias-F3/cfo-ativos-por-cro-2026-10-21.csv` |
| Leitura anterior no mesmo dia (outra frente) | 474.640 | [FATO] registrado em run/00-enquadramento.md; a tabela muda ao longo do dia |
| SP / MG / RJ / PR / BA | 126.491 / 59.164 / 41.109 / 28.217 / 24.047 | [FATO] mesma tabela |
| Clínicas (EPAO) | 102.088 | [FATO] mesma tabela |
| ASB / TSB / TPD / APD / laboratórios / empresas (ECIPO) | 199.155 / 53.620 / 26.358 / 7.784 / 4.167 / 1.120 | [FATO] mesma tabela |
| Total de inscritos na tabela (pessoas e entidades) | 868.951 | [FATO] soma da coluna TOTAL |
| CD com ano de inscrição no regional 2026 | 29.495 | [FATO] tabela por ano, ano 2026. Ressalva: é inscrição no regional, pode incluir transferência e inscrição secundária |
| SP sobre o total | 26,6% | [ESTIMATIVA] 126.491 / 474.659 |

Ressalva de método: a soma por CRO pode contar duas vezes o dentista com inscrição em mais de um regional. A página não diz se conta pessoa ou inscrição. Por isso a forma segura na tela é "mais de 474 mil" com fonte, e não "474.659 dentistas".

### 2.2 Especialistas (útil para "técnica que o colega quer aprender")

| Especialidade | Total (F / M) | Etiqueta |
|---|---|---|
| Linha TOTAL GERAL | 162.011 (95.604 / 66.407) | [FATO] tabela de especialistas |
| Ortodontia | 34.506 | [FATO] |
| Implantodontia | 24.042 | [FATO] |
| Endodontia | 21.054 | [FATO] |
| Prótese dentária | 15.300 | [FATO] |
| Periodontia | 11.215 | [FATO] |
| Odontopediatria | 10.670 | [FATO] |
| Harmonização orofacial | **6.845** (5.479 F / 1.366 M) | [FATO] |
| Cirurgia estética orofacial | 165 | [FATO]; especialidade reconhecida pela Res. 286/2026 |

Pendência fechada: o plano final (06-plano-final.md, item 15) registrou três valores para HOF (6.845, 5.479, 1.366). A tabela tem cabeçalho "Feminino, Masculino, Total": **6.845 é o total nacional**, os outros dois são o recorte por sexo.

[ESTIMATIVA] No máximo 34,1% dos CD ativos têm especialidade registrada (162.011 / 474.659). É teto, porque um dentista com duas especialidades pode contar duas vezes na linha TOTAL GERAL (a soma das 25 especialidades dá exatamente 162.011).

## 3. Regras do CFO aplicáveis ao reel

### 3.1 Quem a regra alcança

- [FATO, CEO art. 1º] O Código regula cirurgião-dentista, técnicos, auxiliares e pessoas jurídicas inscritas.
- [HIPÓTESE] O Bruno não é inscrito no CFO, então o código não o alcança de forma direta. Alcança o dentista que aparecer no vídeo, repostar, ou contratar o lançamento. [FATO, CEO art. 45] Respondem solidariamente pela publicidade irregular "os proprietários, responsável técnico e demais profissionais que tenham concorrido na infração". Na prática, a peça precisa ser segura para o dentista que vai comentar e virar cliente.

### 3.2 Normas em vigor e o que dizem

| Norma | Ponto que importa para este vídeo | Etiqueta |
|---|---|---|
| Res. 196/2019 art. 1º | Selfie de dentista liberada, com ou sem paciente, com TCLE do paciente. § 1º: proibidas imagens que permitam identificar equipamentos, instrumentais, materiais e tecidos biológicos | [FATO] |
| Res. 196/2019 art. 2º | Imagem de diagnóstico e de conclusão liberada só para o dentista que fez o caso, com TCLE. § 1º: continua proibido o que caracterize "sensacionalismo, a autopromoção, a concorrência desleal, a mercantilização da Odontologia ou a promessa de resultado" | [FATO] |
| Res. 196/2019 art. 3º | Proibida a divulgação de vídeo ou imagem do transcurso ou da realização do procedimento, "exceto em publicações científicas" | [FATO] |
| Res. 196/2019 art. 4º | Em toda publicação de imagem ou vídeo: nome do profissional e número de inscrição; vedado divulgar caso clínico de terceiro | [FATO] |
| CEO art. 9º XIII | Dever de não praticar atos que impliquem mercantilização da Odontologia | [FATO] |
| CEO art. 35 V e VII (Do Magistério) | Infração: permitir propaganda abusiva ou enganosa de cursos de especialização, aperfeiçoamento e atualização; aliciar alunos com vantagens, benefícios ou gratuidades para esses cursos | [FATO]. É a regra mais próxima de "lançar curso para dentista" |
| CEO art. 43 | Na divulgação é obrigatório nome e número de inscrição do profissional | [FATO] |
| CEO art. 44 I | Infração: publicidade enganosa ou abusiva, "inclusive com expressões ou imagens de antes e depois, com preços, serviços gratuitos, modalidades de pagamento" | [FATO] texto de 2012. A Res. 196/2019 abriu imagem de diagnóstico e conclusão; preço, gratuidade e forma de pagamento seguem no texto |
| CEO art. 44 III | Infração: anunciar técnica ou terapia sem comprovação científica | [FATO] |
| CEO art. 44 IV | Infração: criticar técnicas de outros profissionais como inadequadas ou ultrapassadas | [FATO] |
| CEO art. 44 V | Infração: divulgar resultados clínicos em veículo de massa | [FATO] (abrandado para imagem pela Res. 196/2019) |
| CEO art. 44 XII | Infração: expor ao público leigo imagens ou expressões de antes, durante e depois | [FATO]. O reel fala com dentista, mas o Instagram é público leigo também |
| Res. 271/2025 art. 4º | Nova redação do art. 44 XIV: veda aliciamento de pacientes por telemarketing ativo, caixa de som, plaqueteiro e meios semelhantes. Saíram do texto cartão de desconto, mala direta via internet e sites promocionais | [FATO] |
| Res. 286/2026 art. 16 §§ 2º a 4º | Para cursos de cirurgia estética orofacial: curso com participação de paciente só com autorização prévia do CRO; vedada a divulgação desses cursos sem a autorização; descumprimento é infração "manifestamente grave" | [FATO]. Vale para CEOF. Para as outras áreas não achei regra igual nas resoluções lidas |
| Decisão 05/2025 | Grupo especial vai reescrever o capítulo de publicidade | [FATO]. Até 308/2026 nenhuma resolução publicou o novo capítulo [FATO, varredura]. Pode mudar a qualquer momento |

## 4. O que pode e o que não pode aparecer na tela

### 4.1 Pode

| Elemento | Por quê | Etiqueta |
|---|---|---|
| "Mais de 474 mil dentistas ativos no Brasil" com rodapé "Fonte: CFO, out/2026" | Número público do próprio CFO, arredondado para baixo | [FATO] seção 2.1 |
| O Bruno em selfie no escritório, sem paciente, sem consultório | Não é imagem clínica; não há equipamento, instrumental, material ou tecido em cena (frames-amostra.jpg: escritório com quadros, cadeiras e plantas) | [FATO] contexto.md + Res. 196 art. 1º § 1º |
| Letreiro com as frases da fala: "hora de cadeira", "ensinar o seu colega", "segundo produto", "eu desenho seu lançamento" | Falam de modelo de negócio e de ensino entre colegas, não de tratamento | [HIPÓTESE] risco baixo; nenhuma norma lida veda falar de curso para dentista |
| Ícones e animações genéricas: lousa, sala de aula, plateia, calendário, gráfico sem número, tabuleiro | Sem boca, sem dente real, sem instrumental | [HIPÓTESE] |
| Dente estilizado em ícone plano ou 3D abstrato | Não é tecido biológico nem caso clínico | [PRIOR] interpretação; a Res. 196 fala em imagem que identifique tecido, um ícone não identifica |
| Reacts de plateia (aplauso, rosto surpreso) de banco de imagem | Não envolvem paciente | [HIPÓTESE] |
| CTA "Dentista, comenta a sua profissão aqui" | Pede comentário, não oferece serviço odontológico nem vantagem | [HIPÓTESE] |
| Prova "case Tzur" dita como outro mercado | Não é resultado clínico. O Bruno não citou o case nesta tomada (contexto.md) | [FATO] contexto.md; uso: [HIPÓTESE] |

### 4.2 Não pode (ou não deve)

| Elemento | Norma | Etiqueta |
|---|---|---|
| Foto ou vídeo de boca, dente real, sorriso de paciente, raio X | Res. 196 arts. 1º § 1º, 2º e 4º; CEO art. 44 VI | [FATO] |
| B-roll de procedimento em andamento (cadeira com paciente, broca, moldagem, injeção) | Res. 196 art. 3º | [FATO] |
| Equipamento, instrumental ou material odontológico identificável (cadeira odontológica, fotopolimerizador, seringa, kit) | Res. 196 art. 1º § 1º (regra escrita para selfie; uso no b-roll por analogia) | [FATO] na selfie; [HIPÓTESE] no b-roll |
| Antes e depois, qualquer formato | CEO art. 44 I e XII; Res. 196 art. 2º só libera para o autor do caso, com TCLE | [FATO] |
| Preço do curso, "vagas gratuitas", "aula grátis", parcelamento, desconto, sorteio | CEO art. 44 I; art. 35 VII (gratuidade para atrair aluno de curso); art. 20 VIII nova redação (brinde, premiação, sorteio) | [FATO] |
| Promessa de resultado: "fature R$ X", "agenda cheia", "seu curso vai lotar", número de alunos garantido | Res. 196 art. 2º § 1º (promessa de resultado); CEO art. 35 V (propaganda enganosa de curso); regra do próprio cliente no CLAUDE.md | [FATO] |
| "Melhor técnica", "a única que funciona", "os outros fazem errado" | CEO art. 44 IV (criticar técnica de outro) e art. 44 III | [FATO] |
| Logo, nome ou caso clínico de dentista real sem autorização | Res. 196 art. 4º (caso de terceiro) | [FATO] |
| Anúncio de curso com paciente (hands-on) de cirurgia estética orofacial sem autorização do CRO | Res. 286/2026 art. 16 § 3º | [FATO] |
| Número sem fonte ("mais de 500 mil", "70% dos dentistas") | Regra do cliente; CEO art. 49 VI veda falsear dado estatístico (seção de publicação científica) | [FATO] |

### 4.3 Ajustes de texto recomendados para a tela e a legenda

1. Letreiro do número: "+474 mil dentistas ativos" e, no rodapé, "Fonte: CFO, out/2026". [FATO] seção 2.1.
2. A fala diz "em Brasil" (transcricao-tempos.txt, 4,96 s). Na legenda queimada, escrever "no Brasil". [FATO] transcrição; correção é decisão editorial.
3. A transcrição automática registrou "passa a forna que a gente disputa" (27,24 a 29,28 s). O texto do contexto.md é "passa a formar quem disputa". A legenda deve usar o texto do contexto, conferido de ouvido antes do render. [FATO] os dois arquivos divergem.
4. "Você deixa de disputar paciente e passa a formar quem disputa": manter como fala, sem letreiro com cifrão ou gráfico de faturamento. [HIPÓTESE] reduz a leitura de "mercantilização" (CEO art. 9º XIII).
5. Na legenda do post, não citar valor de curso, faturamento de cliente nem número de alunos. [FATO] seção 4.2.

## 5. Lacunas

- Se a tabela do CFO conta pessoas ou inscrições (dentista com inscrição secundária em outro CRO pode contar duas vezes). Sem dado.
- Total nacional publicado pelo próprio CFO (a página só traz as 27 linhas). Sem dado; o total é soma feita aqui.
- Série histórica de CD ativos (crescimento ano a ano): a página por ano só trouxe 2026 no HTML. Sem dado.
- Texto consolidado do Código de Ética com a Res. 271/2025 incorporada: o PDF do site é de 2012. A leitura combinada foi feita à mão nesta frente.
- Resultado do grupo da Decisão 05/2025 (novo capítulo de publicidade): nada publicado até a Res. 308/2026. Pode sair a qualquer momento.
- Regra geral do CFO sobre divulgação de curso com paciente fora da cirurgia estética orofacial: não achei nas resoluções 268 a 308. A Consolidação das Normas (Res. 63/2005) não abriu (PDF só com cabeçalho).
- Lei 5.081/1966: não lida (Planalto fora do ar, HTTP 503). Fontes secundárias citam vedação de "exposição de trabalho odontológico"; [PRIOR] até ler o texto.
- Normas fora do CFO que também valem para anúncio de curso (Código de Defesa do Consumidor, CONAR): não verificadas nesta frente. [PRIOR] proíbem propaganda enganosa em termos parecidos.
- Se o Bruno é ou não inscrito em algum CRO: sem dado. A seção 3.1 parte da hipótese de que não é.
- Interpretação do CRO local para ícone de dente e para "curso para dentista" em reel público: sem consulta ao CRO. Tudo marcado como [HIPÓTESE] na seção 4.1 é interpretação, não parecer.
