# F3 · Benchmark de nicho: marketing digital, lançamento de infoproduto e uso de TV e imprensa (Brasil)

Frente F3 da pesquisa do conselho Agência Reunida para o @o_estrategista.com.br. Versão de sábado, 24/10/2026, 15h05 (São Paulo). Substitui a versão das 13h55, escrita antes do fato novo: a entrevista à TV Câmara Campinas vai ao ar na **segunda-feira, 02/11/2026** (Finados, feriado nacional [FATO, 00-enquadramento, Lei 10.607/2002]; horário sem dado), e o Bruno vai marcar a Mirna nas postagens pelo app. O que mudou: entrou a seção 2 (como criadores usam TV e imprensa antes, no dia e depois) e a leitura da seção 8 foi refeita em torno de 02/11. As seções 3 a 7 mantêm os números da rodada das 13h40, conferidos de novo onde a consulta ainda era possível.

Somente leitura: nada foi publicado, agendado ou alterado no Instagram, no Buzzfy ou no PostZen.

**Etiquetas:** [FATO] com a fonte ao lado; [ESTIMATIVA] com a conta ou a premissa; [HIPÓTESE] a testar; [PRIOR] palpite do modelo, evidência nível 4, que nunca fecha objeção sozinho. Métrica que falta: "sem dado".

**Reels de terceiros entram só como referência.** Toda frase de outro criador citada aqui é dado (o Buzzfy a devolve marcada como "untrusted"), serve para estudar o padrão e não para copiar. Perfis aparecem pelo @ que a consulta devolveu; nenhuma opinião é atribuída a eles além do que o resumo do Buzzfy descreve.

---

## 0. Consultas feitas

### 0.1 Rodada das 13h40 a 13h50 (mantida)

| # | Consulta (só leitura) | Parâmetros | Resultado |
|---|---|---|---|
| 1 | Buzzfy `buzzfy_niche_report` | main_niche=marketing | OK. "Marketing & content creation", report_id 6d38b430-0ccb-4217-95fd-f2c8ae4f2436, montado em 08/10/2026, próxima atualização 07/11/2026. 142 reels (72 de contas verificadas, 70 de não verificadas) |
| 2 | Buzzfy `buzzfy_niche_report` | niche="lançamento de infoproduto" | **Não gerado.** `status: upgrade`: relatório de tema específico exige o plano MAX. O Buzzfy devolveu o relatório do item 1 no lugar. Registrado como limite de plano, não como dado |
| 3 | Buzzfy `buzzfy_niche_report_reels` | report_id acima, páginas 1 a 6 | OK. 142 reels; contagens do relatório batem com a lista |
| 4 e 5 | Buzzfy `buzzfy_reel_search` | lançamento de infoproduto, pt, most_viewed e best_hook | **ERRO** de tempo nas duas ("Reel search took too long"). call_ids 0e70eb2f-5299-4069-bcb7-ad68e7cedf7e e f2394f1c-6db0-4ed1-afc2-980a9bf07b55 |
| 6 a 11 | Buzzfy `buzzfy_reel_search` (B1 a B6) | B1 lançamento de infoproduto; B2 marketing e clientes; B3 best_hook; B4 até 5.000 seguidores; B5 corte de entrevista; B6 CTA de palavra-chave. Todas em pt | OK. 22, 116, 50, 150, 115 e 56 correspondências; 19, 50, 13, 50, 25 e 25 mostradas |
| 12 | Buzzfy `buzzfy_playbook` | small_accounts, formats, length_and_pace | OK. "The Viral Reels Playbook, 2026 Edition (Buzzfy Research, September 2026)" |

### 0.2 Rodada das 14h55 a 15h05 (nova)

| # | Consulta (só leitura) | Parâmetros | Resultado |
|---|---|---|---|
| 13 | Buzzfy `buzzfy_niche_report` | report_id 6d38b430... | OK. Mesmo relatório, mesmos números (142 reels, 72/70, padrões de gancho, formato, CTA, legenda e ritmo idênticos aos da rodada das 13h40) |
| 14 | Buzzfy `buzzfy_niche_report_reels` | páginas 1, 2 e 3 | OK. 75 reels conferidos; achados os 3 com a etiqueta de gancho "authority" (seção 3.2) |
| 15 | Buzzfy `buzzfy_reel_search` (T0) | "empresário ou especialista mostrando que apareceu na TV, entrevista na televisão, reportagem ou matéria no jornal sobre o trabalho dele", pt, most_viewed | **ERRO** de tempo. call_id d59b68a6-a0b0-452a-bba4-8afc0e13ae76 |
| 16 | Buzzfy `buzzfy_reel_search` (T1) | "entrevista na TV, apareci na televisão", pt, most_viewed, 2 páginas | OK. 50 correspondências, 37 mostradas |
| 17 | Buzzfy `buzzfy_reel_search` (T2) | palavra exata "na TV", pt, most_viewed | OK. 9 correspondências, 9 mostradas |
| 18 | Buzzfy `buzzfy_reel_search` (T3) | "vai ao ar, assista minha entrevista no programa de TV, contagem regressiva para a exibição", pt, most_viewed, 2 páginas | OK. 193 correspondências, 50 mostradas (limite da busca) |
| 19 | Buzzfy `buzzfy_reel_search` (T4) | "saiu uma reportagem sobre mim no jornal, matéria na revista, apareci na imprensa", pt, most_viewed, 2 páginas | OK. 202 correspondências, 50 mostradas |
| 20 | Buzzfy `buzzfy_reel_search` (T5) | "bastidores da gravação de entrevista para programa de TV, estúdio, câmeras, maquiagem", pt | **ERRO: limite diário.** "This account has used its 10 reel searches for today. The next one frees up in about 23 hours (around 16:45 UTC)". call_id 74dbc45c-34ca-4195-a5f0-0ed444369202. Não é dado vazio: a busca não rodou |
| 21 | Buzzfy `buzzfy_playbook` | second_life, small_accounts, case_files | OK |

[FATO, consulta 20] O plano do Buzzfy desta conta dá 10 buscas por dia; acabaram hoje. Próxima busca livre por volta de 13h45 de dom 25/10 (São Paulo) [ESTIMATIVA: 16h45 UTC menos 3 h]. Páginas seguintes de uma busca já feita não gastam busca (usei isso em T1, T3 e T4).

Fontes do repositório: `conteudo/modo-god-cronograma/contexto.md` (versão das 14h40), `run/00-enquadramento.md`, `run/01-pesquisa/F1-auditoria-conta.md`, `F2-playbook-buzzfy.md`, `F4-entrevista-tv.md`, `conteudo/sistema-instagram/00-SISTEMA.md` (Módulo 2). Contas feitas em Python sobre as saídas acima (script no rascunho da sessão, fora do repositório). Toda mediana de views desta frente é de views públicas informadas pelo Buzzfy.

---

## 1. Respostas curtas

**TV e imprensa (novo)**

1. **O mercado anuncia antes e mostra conteúdo depois.** Nos 3 reels de "antes" de criadores que foram à TV ou à imprensa, nenhum traz trecho do que foi dito: são convite e bastidor [FATO, T1 a T4]. Se algum criador publicou trecho da entrevista antes de ir ao ar: sem dado. É evidência fraca (n de 3) para a pergunta aberta sobre pb01, car01, ci01, po01 e pb02.
2. **O corte bruto do programa é o que menos rende.** 3 cortes de programa de TV postados por quem apareceu neles: de 0,004x a 0,025x os seguidores, mediana de 0,0055x [FATO, T1 e T3]. O reel típico do playbook fica em 0,17x os seguidores [FATO, `buzzfy_playbook` small_accounts].
3. **O que rendeu no "depois" foi a notícia em texto e a história contada pelo próprio criador.** Manchete de imprensa na tela, 5 s, sem fala: 30.915 views, 2,53x os seguidores, 1.043 compartilhamentos [FATO, T4]. Criador contando como foi a entrevista na TV, 339 s: 4.227 views, 0,90x [FATO, T1].
4. **Quatro peças no mesmo dia diluem.** Uma criadora postou 4 reels em 04/09 sobre a revista e a live dela: de 0,030x a 0,058x os seguidores cada [FATO, T3 e T4]. O segundo post sobre a mesma aparição, 9 dias depois, teve 30% das views do primeiro [ESTIMATIVA: 598 / 2.026, n de 1].
5. **No dia, todos os exemplos dizem "hoje" e 2 de 3 dizem a hora.** "E HOJE ás 19:30...", "É HOJE • EM POUCOS MINUTOS", "Hoje, saiu mais uma conversa..." [FATO, T3]. Para o Bruno, o horário de 02/11 é sem dado.
6. **O caso do tamanho do Bruno não prova orgânico.** @newtonlindolfo (1.616 seguidores; o Bruno tem 1.618) anunciou uma entrevista ao vivo com 2 reels só de texto (10 s e 26 s): 11.056 e 15.122 views, 6,8x e 9,4x os seguidores, 0 comentário, curtidas de 1,3% e 2,2% das views [FATO, T3]. [HIPÓTESE] Compatível com impulsionamento pago ou envio em massa pelos convidados; sem dado para separar.
7. **"Autoridade" no nicho global é credencial na primeira frase, não logo de emissora.** Os 3 reels com gancho "authority" (mediana de 705.913 plays) abrem dizendo quem fala e o que já fez; nenhum usa TV ou imprensa [FATO, `buzzfy_niche_report_reels`].
8. **Marcar a repórter: sem dado de mercado.** O Buzzfy não traz marcação nem colaboração dos reels de terceiros. Efeito da marcação da Mirna no alcance: sem dado.

**Nicho (mantido da rodada das 13h40)**

9. O relatório de nicho do Buzzfy não é retrato do Brasil: dos 142 reels, 97 em inglês, 35 em hindi, 2 em português (advocacia e clínica de estética) [FATO]. Relatório de "lançamento de infoproduto" exige MAX [FATO, consulta 2].
10. Global, contas não verificadas: tutorial tem mediana de 505.320 plays (12 reels), talking head 20.748 (31); curto (abaixo de 20 s) ganha no corte entre contas [FATO]. Dentro do criador, o playbook diz que a duração quase não muda nada [FATO].
11. CTA de palavra-chave não puxa alcance em conta pequena: no recorte em português, 401 views e 0,043x os seguidores (25 reels) contra 430 e 0,081x dos outros CTAs; 0 dos 9 estouros de contas até 6 mil seguidores usou palavra-chave [FATO, B1 a B6].
12. Pares diretos do Bruno (mesmo tema, 1.000 a 3.500 seguidores, 29 reels): mediana de 322 views, 0,12x os seguidores; 5 de 29 passaram de 1.000 [FATO, B1 a B6].
13. Os reels da conta na biblioteca: falados ficam em 10º e 18º de 30 entre os pares; slideshows em 29º e 30º [FATO, B1 a B6].

---

## 2. TV e imprensa: como criadores usam a aparição (antes, no dia e depois)

### 2.1 O que a biblioteca tem e o que não tem

- [FATO, T1 a T4] 37, 9, 50 e 50 resultados mostrados, com repetições entre buscas (contagem de únicos não feita). A maior parte não é o criador aparecendo na mídia: comentário político, celebridade, trecho de TV de outra pessoa, anúncio de evento.
- Classifiquei pelo resumo do Buzzfy (classificação minha): **13 reels de aparição própria** em TV, revista ou matéria, fora política; **7 anúncios de transmissão** (live, podcast, canal), usados como análogo do "dia"; **6 anúncios de convite ou credencial**; **1 react** a entrevista de TV de terceiro.
- [FATO] Do nosso tema (marketing, vendas, negócios) entre os 13: 3 (pesquisa de mercado, restaurante, Black Friday e IA). De lançamento de infoproduto: 0.
- [FATO] Postados de 04/09 a 19/10/2026. Pelo menos 1 perfil escreve em português de Portugal ("Já vos disse").

### 2.2 Os 13 de aparição própria

| Fase | Perfil (seguidores) | O que é (resumo do Buzzfy) | Formato, duração | CTA | Views | ÷ seguidores | Compart. por 100 curtidas | Link |
|---|---|---|---|---|---|---|---|---|
| antes: anúncio | @perolamansur.maternalize (16.210) | anuncia convite para falar num programa de saúde na TV; abre com "Gente, eu tenho uma novidade muito especial para compartilhar com vocês." | talking head, 42 s | pergunta | 3.263 | 0,201 | 4 | instagram.com/reel/Dec1u6fpq0J |
| antes: bastidor | @dr.brunobarros (3.215) | bastidor de entrevista na TV, texto na tela "Bastidores REDETV", sem fala de abertura | bastidor, 22 s | nenhum | 156 | 0,049 | 9 | instagram.com/reel/DecbBfRhL1J |
| antes: bastidor | @rafaperich (13.675) | gravação com "o pessoal de jornalismo da UP", texto na tela (se é veículo de imprensa ou projeto acadêmico: sem dado) | montagem, 5 s | nenhum | 1.754 | 0,128 | 18 | instagram.com/reel/Dc4auEhPpue |
| dia | @ritasalgueiro_ (9.036) | chegou a revista em que ela é capa: "Hoje, cheguei à Obm e encontrei a nova edição..." | voz sobre imagens, 21 s | nenhum | 2.026 | 0,224 | 14 | instagram.com/reel/DduSVEkBQhn |
| dia | @katiaferreira.usa (17.551) | colunista numa revista digital, texto "Honrada em participar deste projeto de amor" | slideshow, 15 s | nenhum | 526 | 0,030 | 0 | instagram.com/reel/Dc2YEtTMHzs |
| dia | @katiaferreira.usa (17.551) | mesma revista, "E a mensagem chega à Europa" | slideshow, 15 s | seguir | 785 | 0,045 | 0 | instagram.com/reel/Dc3KmgMx6Pw |
| depois: história | @camisacomhistoria_oficial (4.698) | conta como foi ser entrevistado na TV pela coleção dele; abre com "Hoje não tem roteiro, hoje não tem camisa específica para falar." | talking head, 339 s | seguir | 4.227 | 0,900 | 21 | instagram.com/reel/DeaJhwKhUJV |
| depois: 2º post | @ritasalgueiro_ (9.036) | 9 dias depois do anterior: "Já vos disse que fui capa da revista de projeto?" | slideshow, 10 s | nenhum | 598 | 0,066 | 3 | instagram.com/reel/DeFdgzvhOnA |
| depois: manchete | @mirabilerestaurante (12.243) | manchete de imprensa na tela: prato do restaurante eleito o melhor do mundo num ranking | slideshow, 5 s | nenhum | 30.915 | 2,525 | 94 | instagram.com/reel/DesEejOqciB |
| depois: matéria | @leandroscalise (1.187) | matéria de revista sobre Black Friday e IA, texto na tela (que ele seja o autor ou o citado: provável, não confirmado) | slideshow, 5 s | nenhum | 535 | 0,451 | 3 | instagram.com/reel/DdRWjI4OIAX |
| depois: corte de TV | @renato.meirelles (40.656) | trecho de programa de TV; abre com a pergunta do apresentador "O que move a classe C, a maior fatia da população brasileira?" | entrevista, 25 s | nenhum | 1.019 | 0,025 | 4 | instagram.com/reel/DebtyGZRIbo |
| depois: corte de TV | @psic_quantica (31.709) | trecho de entrevista na TV; abre com "Antes de mais nada, deixa eu te apresentar quem são os doutores que estão aqui com a gente..." | entrevista, 94 s | salvar | 175 | 0,006 | 29 (7 curtidas) | instagram.com/reel/DekuokkSLXP |
| depois: corte de TV | @mario_paiva_advogado (92.342) | trecho de telejornal sobre direito do trabalhador no dia da eleição; abre com "Tem autorização para ir votar?" | entrevista, 256 s | nenhum | 336 | 0,004 | 0 | instagram.com/reel/Dd7GVGvpzSX |

[FATO, T1, T3 e T4; links como a consulta devolveu, não abertos no Instagram]. Referências do playbook para ler as duas últimas colunas: reel típico com views de 0,17x os seguidores e cerca de 2 compartilhamentos por 100 curtidas; os 8 estouros dos "case files" tiveram de 12 a 220 [FATO, `buzzfy_playbook` small_accounts e case_files].

### 2.3 Medianas por fase (os 13)

| Fase | n | Mediana de views | Mediana ÷ seguidores |
|---|---|---|---|
| antes (anúncio e bastidor) | 3 | 1.754 | 0,128 |
| dia | 3 | 785 | 0,045 |
| depois (todos) | 7 | 598 | 0,066 |
| só cortes de programa de TV | 3 | 336 | 0,0055 |
| todos | 13 | 785 | 0,066 |

[FATO, conta sobre a tabela 2.2]. 5 dos 13 ficaram em 0,17x ou mais (anúncio com pergunta, revista no dia, história contada, manchete, matéria); os 3 cortes de TV ficaram todos abaixo de 0,03x [FATO]. n pequeno em toda linha: evidência fraca.

Comparação dentro da mesma conta, só com o que as buscas trouxeram [FATO, T1 e T3]: @mario_paiva_advogado tem outros reels com 408, 379, 336 e 216 views, e o corte de telejornal (336) fica nessa faixa; @psic_quantica tem outros com 284 e 342, e o corte de TV (175) fica abaixo. [ESTIMATIVA, n de 2 a 4 por conta] Nessas duas contas o corte de TV não ficou acima do normal delas.

### 2.4 Os 7 anúncios de transmissão (análogo do "antes" e do "dia")

| Momento | Perfil (seguidores) | O que é | Formato, duração | CTA | Views | ÷ seguidores | Curtidas ÷ views | Comentários | Link |
|---|---|---|---|---|---|---|---|---|---|
| véspera | @newtonlindolfo (1.616) | texto "DE 2 PRA 7": anúncio de entrevista ao vivo sobre crescer de 2 para 7 lojas | slideshow, 10 s | nenhum | 11.056 | 6,84 | 1,3% | 0 | instagram.com/reel/DedYl26xvHn |
| dia | @newtonlindolfo (1.616) | texto "E HOJE ás 19:30 uma LIVE que você não pode perder" | vitrine, 26 s | nenhum | 15.122 | 9,36 | 2,2% | 0 | instagram.com/reel/Def-H0IRWgK |
| dia | @katiaferreira.usa (17.551) | texto "É HOJE • EM POUCOS MINUTOS", pede "EU QUERO" nos comentários para o link | slideshow, 4 s | palavra-chave | 799 | 0,046 | 0,9% | 4 | instagram.com/reel/Dc4fYaTJ0to |
| dia | @ritasalgueiro_ (9.036) | "Hoje, saiu mais uma conversa de curadoria no meu canal de YouTube." | talking head, 20 s | link na bio | 1.309 | 0,145 | 4,0% | 1 | instagram.com/reel/DdhepjsIrh1 |
| antes | @fabio_szescsik (6.720) | teaser de episódio de podcast ao vivo, "Vem novidades por aí!!" | entrevista, 25 s | nenhum | 772 | 0,115 | 3,9% | 6 | instagram.com/reel/DdceJ7HPpx5 |
| antes | @flavio2207 (526) | anúncio de live com data e hora na tela ("11/set Sexta-feira 19h30") | talking head, 39 s | nenhum | 247 | 0,470 | 9,3% | 4 | instagram.com/reel/DdEsMPnx-mQ |
| antes | @johnathanybera (261.680) | contagem: "Tá chegando, tá chegando, tá chegando." | talking head, 59 s | seguir | 17.770 | 0,068 | 2,5% | 97 | instagram.com/reel/DdrJMTkhnqT |

[FATO, T3]. Mediana dos 7: 1.309 views e 0,145x os seguidores [FATO, conta]. Os dois do @newtonlindolfo têm 119 e 44 compartilhamentos por 100 curtidas e nenhum comentário; a rodada das 13h40 já tinha achado um terceiro reel dele com 14.304 views e 0 comentário (B1 a B6). [HIPÓTESE] Três reels de 11 a 15 mil views sem nenhum comentário numa conta de 1.616 seguidores combinam com anúncio pago ou com distribuição pelos convidados; sem dado para separar. Não usar como prova de alcance orgânico.

### 2.5 Convite, credencial e react

- [FATO, T3 e T4] 6 anúncios de convite ou credencial (convite de ministério, convite para coordenar livro, convite para seminário, "de autor a palestrante", convite para palestra, lançamento de livro de celebridade): mediana de 0,108x os seguidores. O mais alto por seguidor é de uma conta de 526 seguidores, "Olá, eu sou Flávio Vicente, educador, gestor escolar e escritor.", 977 views (1,86x), 42 comentários com CTA de pergunta (instagram.com/reel/Ddt5PS4Juag).
- [FATO, T1] React: um médico comenta, pela especialidade dele, a entrevista de TV de uma figura pública sobre um diagnóstico. 15.183 views, 0,63x os seguidores de 24.036, 124 s, abre com "E aí, gente boa." (instagram.com/reel/DdR2OfvOrMW). Exemplo de criador reagindo à **própria** entrevista na TV: sem dado nas buscas.
- [FATO, T2] Um especialista em negócios abre com "Ouvi na TV que o Split Payment quebra o capital de giro das empresas." 491 views, 0,15x os seguidores de 3.217 (instagram.com/reel/DeUgWZax2Ip). A TV como gancho de assunto, não como prova de autoridade.

### 2.6 Padrões que os números sustentam (e o que não sustentam)

1. **Antes: aviso e bastidor, sem conteúdo.** [FATO, 2.2] Os 3 de "antes" são convite e bastidor. Bastidor como reel: 0,049x e 0,128x. Aviso falado com pergunta: 0,201x e 1,41% de comentários (46 em 3.263 views), a terceira maior taxa de comentário dos 13 (as duas maiores: 1,68% e 1,58%) [FATO, conta].
2. **Dia: uma peça com "hoje" e a hora.** [FATO, 2.4] Os 3 avisos de dia trazem "hoje" e 2 trazem a hora. Os 4 reels da mesma criadora no mesmo dia ficaram de 0,030x a 0,058x [FATO, 2.2 e 2.4; o normal dela é sem dado, então diluição é leitura minha: HIPÓTESE].
3. **Depois: a notícia e a história rendem; o corte bruto não.** [FATO, 2.3] Manchete 2,53x, história contada 0,90x, matéria 0,45x; cortes de programa de 0,004x a 0,025x. Os 2 cortes com abertura conhecida abrem com a fala do apresentador (pergunta ou apresentação dos convidados), o mesmo defeito que a rodada das 13h40 achou nos cortes de entrevista abaixo de 1.000 views (seção 4.7).
4. **Repetir o anúncio cansa.** [ESTIMATIVA, n de 1] Segundo post sobre a mesma capa de revista: 30% do primeiro.
5. **Abertura com saudação ou "novidade".** [FATO] "Gente, eu tenho uma novidade...", "Eu tenho uma novidade fantástica...", "Quero compartilhar com vocês um convite que recebi com muita honra." ficaram em 0,201x, 0,058x e 0,004x. Os 8 estouros do playbook não abrem com saudação e todos têm palavra na tela [FATO, `buzzfy_playbook` case_files]. [HIPÓTESE] A abertura de "novidade" funciona como aviso para quem já segue, não para estranhos.
6. **O que os dados não respondem:** se publicar trecho antes da exibição tira audiência da TV ou alcance do "depois" (sem dado); se marcar a repórter ou a emissora aumenta alcance (sem dado); quantos espectadores da TV viram perfil depois (sem dado); a data de exibição dos 3 cortes de TV em relação à data do post (sem dado).

---

## 3. Relatório global (142 reels, "Marketing & content creation")

Reaberto às 14h55 com o mesmo report_id: números idênticos aos da rodada das 13h40 [FATO, consulta 13].

### 3.1 O que o relatório mede, e o que não mede

- [FATO] "smaller" no Buzzfy é conta **não verificada**, não conta pequena; o relatório não traz seguidores.
- [FATO] Plays somam com o tempo: 19 dos 20 maiores foram postados antes de 2026. Mediana dos 53 reels de antes de 24/10/2025: 425.482; dos 89 dos últimos 12 meses: 45.222.
- [FATO, campo how_to_use] "Plays are public play counts; nothing here measures reach, saves or watch time."
- [FATO] 17 dos 20 maiores ensinam a crescer no Instagram. Lançamento de infoproduto não aparece como tema em nenhum dos 142.

### 3.2 Formato, gancho, duração, CTA

| Formato | Todos (n / mediana) | Não verificadas (n / mediana) |
|---|---|---|
| talking head | 70 / 56.235 | 31 / 20.748 |
| tutorial/demonstração | 26 / 376.219 | 12 / 505.320 |
| montagem estética | 13 / 244.807 | 11 / 79.416 |
| slideshow de texto | 7 / 1.006.121 | 3 / 1.006.121 |
| vitrine de produto | 5 / 57.349 | 4 / 257.390 |

| Gancho | Todos (n / mediana) | Não verificadas (n / mediana) |
|---|---|---|
| resultado primeiro | 5 / 3.118.071 | 4 / 5.207.242 |
| antes e depois | 5 / 2.908.834 | 3 / 2.908.834 |
| opinião contrária | 7 / 634.730 | 4 / 404.425 |
| curiosidade/segredo | 4 / 524.003 | 3 / 1.006.121 |
| afirmação forte | 28 / 318.630 | 10 / 335.884 |
| lista numerada | 15 / 294.333 | 8 / 228.331 |
| como fazer | 14 / 162.542 | 8 / 252.107 |
| chamada de público | sem linha | 8 / 43.654 |

[FATO, relatório]. Linhas com menos de 5 reels são evidência fraca (aviso do próprio Buzzfy).

**Etiqueta "authority" (autoridade)** [FATO, relatório e páginas 2 e 3 da lista]: 3 reels, mediana de 705.913 plays. São eles:
- #29 @digitalglowsolutions (não verificada), 1.137.752 plays, montagem de 3,3 s, texto "HOW I DEVELOP SOCIAL MEDIA STRATEGIES as a social media agency owner".
- #34 @devinjatho (verificada), 705.913, talking head de 89,5 s, "Going viral is not luck; it's calculated. Don't believe me? The last 24 videos that...".
- #40 @dev.gotmoney (verificada), 475.995, talking head de 50,8 s, "My name is Dave, and I am a social media manager. And my clients pay...".

Os 3 dizem na primeira frase quem fala ou o que já fez. Nenhum usa TV, imprensa ou logo de terceiro.

| Duração | Todos (n / mediana) | Não verificadas (n / mediana) |
|---|---|---|
| até 6 s | 9 / 320.798 | 6 / 611.762 |
| 6 a 15 s | 38 / 449.188,5 | 27 / 375.911 |
| 20 a 30 s | 15 / 234.541 | 8 / 793.787 |
| 30 a 45 s | 35 / 28.444 | 16 / 27.300 |
| 45 a 60 s | 22 / 59.949,5 | 6 / 18.541,5 |
| 60 a 90 s | 12 / 57.561,5 | 6 / 9.691 |

[FATO, conta sobre a lista]. Duração mediana: 32,5 s (todos), 23,6 s (não verificadas). Melhor faixa nas três divisões: abaixo de 20 s [FATO, relatório]. Ressalva: dentro do criador, o playbook diz que de 6 s a 2 min tudo fica a cerca de 5% do normal; o que muda é quanto do vídeo é assistido [FATO, `buzzfy_playbook` length_and_pace].

| CTA | Todos (n / mediana) | Não verificadas (n / mediana) |
|---|---|---|
| nenhum | 57 / 120.957 | 33 / 234.541 |
| seguir | 30 / 79.721 | 12 / 38.451 |
| comentar palavra-chave | 28 / 149.069 | 12 / 90.253 |
| salvar ou compartilhar | 8 / 424.600 | 4 / 1.787.044 |
| pergunta para comentar | 7 / 16.335 | 4 / 13.975 |
| direct | 6 / 21.243 | 2 / 13.231 (conta sobre a lista) |

[FATO, relatório]. Entre verificadas, palavra-chave tem mediana maior que "nenhum" (245.556 contra 111.128). O sinal muda com o recorte.

- [FATO, relatório] Legenda: mediana de 454 caracteres; 35,9% com pergunta; 21,8% pedem palavra-chave. Ritmo: 0,137 corte por segundo; primeiro corte aos 3,87 s (não verificadas 4,11 s).
- [FATO, lista] Pessoa falando para a câmera: 83 reels, mediana de 89.114; sem: 59, mediana de 128.304. Vai contra a medição da própria conta (Bruno falando de 2,4x a 5,8x acima da mediana, CLAUDE.md). A medição dentro da conta pesa mais que o corte entre contas em inglês e hindi.

---

## 4. Brasil: biblioteca do Buzzfy em português (B1 a B6, rodada das 13h40)

Não refeito às 15h: o limite diário de buscas acabou (consulta 20). Números da consulta das 13h40.

### 4.1 Base

- [FATO, B1 a B6] 143 reels únicos; 126 no tema (marketing, vendas, negócios, lançamento, tráfego), 73 criadores, postados de 01/09 a 23/10/2026. Mediana: 7.986 seguidores, 428,5 views, 55,5 s, 0,079x os seguidores. 36 com 1.000 views ou mais; 6 com 10.000 ou mais; 6 com mais views que seguidores.
- [FATO, B1] A busca específica por lançamento de infoproduto teve 22 correspondências em português, 2 delas da própria conta.

### 4.2 Por formato, duração, CTA e tamanho (no tema)

| Formato | n | Mediana de views | ÷ seguidores |
|---|---|---|---|
| talking head | 81 | 378 | 0,079 |
| entrevista/podcast | 28 | 1.136 | 0,045 |
| tutorial/demonstração | 5 | 401 | 0,060 |
| slideshow de texto | 4 | 196,5 | 0,142 |

| Duração | n | Mediana de views | ÷ seguidores |
|---|---|---|---|
| até 20 s | 14 | 845,5 | 0,159 |
| 20 a 40 s | 28 | 359 | 0,081 |
| 40 a 60 s | 30 | 404,5 | 0,057 |
| 60 a 90 s | 32 | 407,5 | 0,045 |
| 90 s ou mais | 22 | 435 | 0,084 |

| CTA | n | Mediana de views | ÷ seguidores |
|---|---|---|---|
| nenhum | 45 | 322 | 0,100 |
| comentar palavra-chave | 25 | 401 | 0,043 |
| seguir | 18 | 427,5 | 0,070 |
| pergunta para comentar | 15 | 738 | 0,087 |
| link na bio | 9 | 776 | 0,013 |
| salvar ou compartilhar | 8 | 327 | 0,322 |

| Seguidores | n | Mediana de views | ÷ seguidores |
|---|---|---|---|
| menos de 1.000 | 22 | 155 | 0,390 |
| 1.000 a 5.000 | 30 | 314,5 | 0,115 |
| 5.001 a 20.000 | 35 | 639 | 0,055 |
| 20.001 a 100.000 | 32 | 663 | 0,017 |
| mais de 100.000 | 7 | 1.514 | 0,010 |

[FATO, B1 a B6]. Vieses: B5 (só entrevista) e B6 (só palavra-chave) inflam essas linhas. Talking head abaixo de 40 s: mediana de 271; 40 s ou mais: 381. Os curtos que puxam "até 20 s" são texto na tela ou anúncio de live, não fala.

### 4.3 Os maiores no tema (português)

| Abertura (dado de terceiro) | Perfil (seguidores) | Views | Formato, duração | CTA | Link |
|---|---|---|---|---|---|
| "Primeiro, princípios e valores." | @alessandro_pizzolatto (96.518) | 19.530 | entrevista, 31 s | pergunta | instagram.com/reel/Dc1aVrwhAc9 |
| Texto: "E HOJE ás 19:30 uma LIVE..." | @newtonlindolfo (1.616) | 15.122 | vitrine, 26 s | nenhum | instagram.com/reel/Def-H0IRWgK |
| Texto: "Não precisa ser um cyborg para aprender a gerir seu próprio negócio" | @newtonlindolfo (1.616) | 14.304 | talking head, 8 s | nenhum | instagram.com/reel/DcyK4aAR2th |
| "Quer vender mais?" | @rafaaraujo.oficial (74.502) | 11.965 | entrevista, 88 s | palavra-chave | instagram.com/reel/Ddd2nP3BY27 |
| "E aí eu decidi montar um minicurso de uma hora e meia sobre essa ferramenta." | @robsondelfiol (5.994) | 5.911 (301 compart.) | entrevista, 37 s | nenhum | instagram.com/reel/DehSjA4x1ld |

[FATO, B1 a B6]. Nos 15 maiores no tema: 9 sem CTA, 1 com palavra-chave; 8 entrevistas, 5 talking heads.

### 4.4 Cortes de entrevista em português (o formato da série da TV Câmara)

- [FATO, B5 e outras] 28 cortes no tema; 16 com 1.000 views ou mais; mediana de 1.136 views, 56,5 s, 44.403 seguidores (0,045x).
- [FATO] Nenhum dos 28 abre com "Pois é" ou "Bom". Os que passaram de 1.000 abrem com pergunta direta, número ou valor, conflito, ou história já andando ("E aí eu decidi montar um minicurso...").
- [FATO] Os que ficaram abaixo de 1.000 e abrem conversando com o entrevistador antes do ponto: "Queria saber de você, qual conselho você dá..." (305), "Então, em resumo..." (427), "Sérgio, você falou uma coisa que me lembrei..." (610).
- [HIPÓTESE] Abrir no ponto aumenta views. Leitura minha; os cortes que abrem no ponto também são, na maioria, de contas maiores. A seção 2.3 repete o padrão nos cortes de TV.

---

## 5. O que contas pequenas fazem

### 5.1 Brasil, no tema, até 6 mil seguidores (B1 a B6)

- [FATO] 55 reels, 32 criadores. Mediana: 282 views, 52 s, 0,25x os seguidores. 40 talking heads (283,5), 4 entrevistas (995), 3 slideshows (59). CTA: nenhum 28 (242), seguir 8 (333), pergunta 5 (534), palavra-chave 5 (151).
- [FATO] 9 passaram de 1.000 views, de 5 criadores; nenhum com palavra-chave, 6 sem CTA. Os 2 maiores são do @newtonlindolfo (texto na tela, 8 e 26 s; ver a hipótese de pago em 2.4). Depois: @robsondelfiol, corte de entrevista contando uma ação com resultado, 5.911 views e 301 compartilhamentos (5,1%); @rafaelvmoraes_, 69 s abrindo com pergunta, 2.401.

### 5.2 Pares diretos do Bruno (1.000 a 3.500 seguidores, no tema)

- [FATO] 29 reels de 19 criadores. Mediana de 322 views, 0,12x os seguidores, 53 s; 23 de 29 são talking head. Quartis: 179,5, 322 e 766. 5 de 29 passaram de 1.000 (17%) [ESTIMATIVA: 5 / 29].

### 5.3 Playbook do Buzzfy (cada criador comparado consigo mesmo)

- [FATO, small_accounts, reconferido às 15h] Um reel típico tem views de 0,17x os seguidores; um estouro, 1,85x. 64% dos estouros passaram o número de seguidores. 74% dos criadores de 1 a 5 mil seguidores tiveram ao menos um estouro em 22 meses. Trial Reels de contas pequenas passaram o alcance usual 21% das vezes, contra 13% acima de 100 mil.
- [FATO, case_files] Os 8 estouros: todos com palavra na tela, nenhum abre com saudação, pulo de 20% a 32% (típico 57%), de 12 a 220 compartilhamentos por 100 curtidas (típico cerca de 2), de 8 a 77 s.
- [FATO, second_life] Remake de reel que já estourou: original de 5x ou mais volta a ganhar 35% das vezes; de 2x a 5x, 15%; de 1x a 2x, 7%. Mudar ao menos duas coisas (abertura, legenda, corte 20% a 40% mais curto, resposta a comentário) e testar como Trial Reel.
- [FATO, formats, rodada das 13h40] De 1 a 5 mil seguidores: história 1,28x o normal do criador, montagem 0,69x; tutorial 1,02x abaixo de 5 mil.

---

## 6. Onde o @o_estrategista.com.br fica no benchmark

| Reel da conta na biblioteca | Postado (UTC) | Views na biblioteca | Formato, duração | Posição entre os 29 pares (de 30) |
|---|---|---|---|---|
| "Deixa eu te contar uma coisa." | 04/10 02h06 | 565 | talking head, 75 s | 10º |
| "Ei, vem cá, escuta essa: 90% dos lançamentos que floparam..." | 04/10 14h11 | 234 | talking head, 70 s | 18º |
| "100 mil seguidores, 14 vendas, e a culpa foi pro preço." | 01/10 18h05 | 70 | slideshow, 33 s | 29º |
| "O que você recusa vende mais do que o que você oferece." | 05/10 01h30 | 70 | slideshow, 66 s | 29º |
| "Você criou o produto, gravou as aulas, e ninguém comprou." | 11/10 21h29 | 47 | slideshow, 38 s | 30º |

[FATO, B1, B2, B4 e B6]. O Dentista A (267 views, contexto.md) ficaria em 17º [ESTIMATIVA: mesma régua]. Normal da conta: 57 views, 0,035x os seguidores [ESTIMATIVA: 57 / 1.618, número do contexto.md], abaixo do quarto de baixo dos pares (179,5) e abaixo dos 0,066x da mediana de aparição na mídia da seção 2.3.

---

## 7. Corte de entrevista e tamanho de conta

- [FATO, 4.4 e 2.2] Corte de entrevista em português rende mais views absolutas (mediana 1.136) mas vem de contas grandes (mediana 44.403 seguidores) e fica em 0,045x os seguidores. Em conta pequena, só um criador do recorte passou de 1.000 com corte de entrevista (@robsondelfiol, 5.994 seguidores, 2 vezes).
- [ESTIMATIVA] Para a conta do Bruno (1.618 seguidores), 0,045x daria cerca de 73 views por corte; 0,0055x (cortes de TV da seção 2.3) daria cerca de 9. São réguas de outras contas, não previsão.

---

## 8. Leitura para o cronograma em torno de 02/11 (hipóteses, não regras)

Nenhum item muda regra do CLAUDE.md sozinho. Cada um é TESTAR com uma mudança por vez, medido no Módulo 7. Todo reel continua com o Bruno em cena nos 3 primeiros segundos.

**Antes (24/10 a dom 01/11)**

1. **Aviso e bastidor ficam nos stories; o feed não precisa de reel de bastidor** [HIPÓTESE, apoio em 2.6 item 1]. Bastidor como reel rendeu 0,049x e 0,128x no mercado. Isso confirma o que já está agendado (st01 e estáticos de bastidor, rótulo "NA TV · SEGUNDA, 02/11").
2. **Os 5 cortes de 26 a 30/10** [HIPÓTESE fraca, n de 3, apoio em 2.6 item 1 e 2.6 item 6]. O mercado observado anuncia antes e mostra conteúdo depois. É um argumento a favor da opção de mover cortes para depois de 02/11, mas não fecha a decisão: o efeito de publicar antes na audiência da TV e no alcance do "depois" é sem dado. Se ficarem antes, a legenda segue falando da gravação e nunca diz "foi ao ar" (F4).
3. **Se houver um reel de aviso, texto curto com a data sobre a imagem do Bruno** [HIPÓTESE, apoio em 2.4]. 10 a 26 s, sem CTA, com o Bruno no quadro 0. O exemplo que estourou (@newtonlindolfo) é suspeito de pago: entra como TESTAR, nunca como DOBRAR.

**No dia (seg 02/11, Finados)**

4. **Uma peça no feed, com "hoje" e a hora** [HIPÓTESE, apoio em 2.6 item 2]. Os avisos de dia trazem o quando; 4 reels no mesmo dia ficaram de 0,030x a 0,058x. Sem o horário confirmado (sem dado hoje), a peça do dia fica sem a informação que todos os exemplos têm: a chamada para assistir vai para os stories quando a grade sair (F4, seção 8).

**Depois (ter 03/11 em diante)**

5. **A peça principal do "depois" é o Bruno contando, não o corte cru** [HIPÓTESE, apoio em 2.6 item 3]. História contada pelo próprio criador: 0,90x; cortes de programa: de 0,004x a 0,025x. Para o Bruno isso pede gravação (o REACT ou um relato curto de selfie, F5). Sem gravação, os cortes prontos entram com o ápice no quadro 0 (F2; seção 4.4), nunca com a pergunta da repórter na abertura.
6. **"Manchete" com frase literal do Bruno, 5 a 8 s** [HIPÓTESE, apoio em 2.2: manchete 2,53x, matéria 0,45x]. Frase dele sobre a imagem dele do quadro da TV, preto e ouro, sem logo, cores ou letreiro da emissora, rotulada como frase do Bruno. Nunca imitar manchete de veículo nem dizer que a imprensa escreveu algo que não escreveu (lista de vetos do 02-provas; CLAUDE.md sobre interface recriada).
7. **Um anúncio de "fui à TV", não vários** [ESTIMATIVA, n de 1: segundo post sobre a mesma aparição teve 30% do primeiro]. O "depois" varia o assunto de cada corte e não repete a notícia da aparição.
8. **Credencial na primeira frase, quando o Bruno gravar** [HIPÓTESE, apoio em 3.2, etiqueta authority]. No nicho global, autoridade é dizer quem fala e o que fez na primeira frase. "Na TV Câmara eu disse..." pode abrir uma fala nova gravada; nas peças prontas, a TV fica na legenda, como já está.

**Sem relação direta com a TV (mantidos)**

9. **Régua externa para o Módulo 7** [HIPÓTESE, régua tirada de 5.2]. Pares brasileiros do mesmo tema e tamanho: mediana de 322 views; 1.000 ou mais é o quinto de cima. Reel com 322 ou mais em 48 h está "na mediana dos pares"; 1.000 ou mais é "estouro entre pares". Ressalva: views da biblioteca são vida inteira, não 48 h.
10. **CTA de alcance sem palavra-chave** [HIPÓTESE, apoio em 4.2, 5.1 e 3.2]. Já é a regra do CLAUDE.md (TABULEIRO uma vez por mês, só com 150 de alcance ou mais). Nos outros reels, pergunta para comentar (mediana 738 no recorte, 534 entre pequenas) ou nenhum CTA. Na série da TV, a pergunta do anúncio com 1,41% de comentários (2.2) é o modelo mais próximo.
11. **O que não copiar** [PRIOR]. Tutoriais de configuração do Instagram do global; comentário político do dia; react a celebridade; o "comenta seu @" de troca de seguidores. Fora do posicionamento do Módulo 2.

---

## 9. Lacunas

- Relatório de nicho de "lançamento de infoproduto": sem dado. Exige plano MAX (consulta 2).
- Buscas que não rodaram: 3 por tempo (call_ids 0e70eb2f-5299-4069-bcb7-ad68e7cedf7e, f2394f1c-6db0-4ed1-afc2-980a9bf07b55, d59b68a6-a0b0-452a-bba4-8afc0e13ae76) e 1 por limite diário (74dbc45c-34ca-4195-a5f0-0ed444369202, a de bastidores de TV). Por causa do limite, não houve busca em inglês sobre TV e imprensa nem refação de B1 a B6. Próxima busca livre por volta de 13h45 de dom 25/10 [ESTIMATIVA].
- TV e imprensa: n de 3 a 7 por grupo; classificação por fase e tipo é minha, pelo resumo do Buzzfy; normal de cada criador: sem dado (só o múltiplo sobre seguidores, que mistura tamanho de conta).
- Se publicar trecho da entrevista antes da exibição muda audiência da TV ou alcance do "depois": sem dado no mercado e na conta.
- Efeito de marcar repórter, emissora ou colaborador: sem dado (o Buzzfy não traz marcação de reels de terceiros).
- Data de exibição dos programas de onde saíram os 3 cortes de TV: sem dado.
- Impulsionamento pago nos reels de terceiros: sem dado; @newtonlindolfo tratado como suspeito, não como fato.
- Biblioteca em português: só criadores que usam o Buzzfy, de 01/09 a 23/10/2026; inclui ao menos 1 perfil de Portugal. Grandes nomes de lançamento do Brasil não aparecem.
- Views de terceiros são públicas e de vida inteira: alcance, retenção, pulo, salvamento e tempo assistido são sem dado.
- Número de seguidores varia entre consultas (@robsondelfiol com 5.994 num filtro de até 5.000).
- Links vieram das consultas ao Buzzfy; não abri as páginas no Instagram.
- Ligação nominal entre os reels da conta na biblioteca e os nomes do contexto.md: estimativa por views (rodada das 13h40).
