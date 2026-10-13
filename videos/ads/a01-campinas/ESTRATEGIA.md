# Anúncio 01 · Campinas · "O mesmo lugar"

Vídeo de anúncio no formato dos Reels (motion branco, voz do Bruno, trilha com grave), com 38,1s. Ele chama quatro profissões de Campinas pelo nome, mostra o que elas têm em comum e leva para uma conversa no WhatsApp. A conversa termina no diagnóstico gratuito de 30 minutos.

Arquivos:
- `anuncio-campinas-9x16.mp4`: Reels e Stories.
- `anuncio-campinas-4x5.mp4`: Feed.
- `index.html`, `script.json`, `gerar_voz_br.py`, `build_clone.py`, `capture.js`, `finalizar.sh`: fonte do vídeo. Para refazer: `python gerar_voz_br.py REFERENCIA.wav` (gera a fala), `python3 build_clone.py` (monta `voz.wav` e `timeline.json`), depois `./finalizar.sh` (renderiza, põe a trilha e gera as duas versões). A gravação de referência do Bruno não fica no repositório.
- `tts.py`, `build.py`, `build.sh` e `gerar_voz_no_pc.py`: caminho antigo com a voz Antonio (Microsoft), que ficou bloqueado no servidor da sessão.

---

## 1. Quem tem mais chance de virar contrato em Campinas

Critérios, nesta ordem de peso:
1. Capacidade de pagar fixo + porcentagem.
2. Encaixe da dor com a lógica de lançamento.
3. Velocidade de decisão: o dono decide sozinho?
4. Atrito de regra do conselho.
5. Maturidade digital.

Não encontrei contagem oficial de profissionais por cidade (CRN-3, CRO-SP, OAB-SP Campinas), então a ordem abaixo é uma leitura qualitativa.

| # | Nicho | Por que tende a fechar | Lançamento que faz sentido pra ele | Cuidado |
|---|---|---|---|---|
| 1 | **Especialista em consórcio** (consultor, assessoria, financeira) | Mercado em recorde: de janeiro a julho de 2026, 3,31 milhões de cotas vendidas (+14,9%) e R$ 331,6 bilhões em créditos (+22,9%), com 13,41 milhões de participantes ativos, segundo a ABAC. A decisão do cliente é longa e de confiança (pede simulação e diz que vai pensar). A comissão por carta é alta e o dono decide sozinho. Você já tem prova no mercado financeiro de Campinas (conta da financeira no seu Gerenciador e o case Tzur, que só pode ser contado na conversa, do jeito autorizado). | Aula aberta sobre usar consórcio para construir patrimônio e uma turma de grupo com data real de fechamento. A formação do grupo e a assembleia já são um prazo verdadeiro, então o carrinho fecha sem escassez inventada. | Não prometer contemplação nem data. O anúncio não vende consórcio ao consumidor; se vender, entra na categoria especial de produtos financeiros do Meta. |
| 2 | **Advogado** | Escritório já compra marketing: a sua agência atende vários, então você chega com vocabulário e histórico do nicho. A dor é clara: a consulta vira "vou ver com a família" e quase tudo depende de indicação. O ticket é alto. | Aula aberta de conteúdo para leigos, dentro do Provimento 205/2021, ou curso e mentoria para outros advogados (o mercado de advogado que vende para advogado existe e está ativo). | A OAB proíbe captação direta e promessa de resultado. A sequência precisa ser informativa. |
| 3 | **Dentista** (implante, alinhador, lente, harmonização) | O ticket por caso é alto e o "orçamento na gaveta" é exatamente o intervalo que o lançamento encurta. Recuperar orçamentos abertos traz retorno rápido, e na clínica quem decide é o próprio dono. | Evento de avaliação com agenda limitada de verdade e recuperação dos orçamentos parados (reabertura antes de desconto). | O CFO restringe antes e depois e divulgação de preço. |
| 4 | **Nutricionista** | É o nicho com mais presença digital e audiência, e a dor de adesão é forte (o paciente some depois da segunda consulta). Programa, desafio e turma encaixam direto em lançamento. O ticket individual é menor, então o fixo precisa caber. | Turma ou programa em grupo, com evento de três aulas e carrinho curto. | CFN: sem promessa de emagrecimento e sem antes e depois. |
| 5 | Médico | Tem o maior ticket, e Campinas atrai paciente pela saúde avançada. Mas decide devagar, tem agenda presa a convênio e foge de risco de imagem. | Programa ou turma de educação do paciente. | Resolução CFM 2.336/2023. |
| 6 | Psicólogo | A fila de espera vira produto (grupo, curso), mas o ticket e a verba são menores. | Grupo terapêutico educativo ou curso. | CFP. |

O vídeo fala com os quatro primeiros pelo nome. Médico, psicólogo, arquiteto e corretor aparecem na tela como "todos".

---

## 2. O que todos têm em comum (a tese do anúncio)

- Todos vendem **uma decisão que o cliente adia**: a dieta, a carta de crédito, o implante, o processo.
- O cliente pede o preço, diz que vai pensar e some. **A venda não morre no preço. Morre no intervalo** entre o interesse e a decisão.
- Seguidor, curtida e indicação não dizem quem vai fechar.
- **Lançamento é a engenharia que encurta esse intervalo:** pesquisa, oferta na ordem certa, aquecimento e prazo real. É o mesmo esqueleto de funil que serve para lançamento, perpétuo e venda consultiva.
- O especialista não pode parar de atender para desenhar e comandar isso. **Por isso todo especialista precisa de um estrategista.**

---

## 3. O vídeo viral que serviu de base, e o que mudou

Método da skill **/ig-viral**: o que conta não é a view bruta, é o **múltiplo** (views do vídeo divididas pela mediana da própria conta). Usei a sua rodada de 10/10 (134 vídeos, uns 25 criadores, mais 106 reels do Instagram) e o acervo do Buzzfy.

| O que foi aproveitado | De onde veio | Como ficou no nosso anúncio |
|---|---|---|
| Fórmula **"Nobody Tells You"** (vídeo-base) | @b2med, Shorts de 31s, **11,9x a mediana** (619 views contra 52). Gancho: "Só que nenhum deles vai te dizer se essa pessoa vai marcar a consulta." Opinião concreta contra métrica de vaidade. | "Seguidor. Curtida. Indicação. Nenhum deles diz quem vai fechar." A ideia foi estendida para quatro profissões e ligada ao método. |
| **Dor do profissional nomeado** | @VitorJaci: 827x e 169x no Instagram, 17,3x no YouTube (uma conta só, então evidência fraca). | As quatro profissões são chamadas pelo nome nos primeiros 3 segundos, com Campinas na tela. |
| Pergunta que confronta o dono do negócio | Buzzfy, pt-BR: @newtonlindolfo ("Seu negócio é uma empresa ou é um hobby caro?") teve cerca de 6,8x os seguidores e mais compartilhamentos que curtidas. | "Ele pede o preço, diz que vai pensar e some." É a cena que todo profissional reconhece. |
| "Você precisa de um profissional", dito de forma concreta | Buzzfy: @votliapp, 412 compartilhamentos ("A fidelidade coloca alguém ao seu lado, mas só a competência coloca você na frente"). | "Por isso todo especialista precisa de um estrategista: você atende, e eu desenho e comando." |

Regras do Viral Reels Playbook 2026 (Buzzfy) aplicadas:
- A primeira frase é curta, específica e sem cumprimento, e não vende nada.
- O texto aparece na tela desde o primeiro quadro: reels assim romperam 1,18x mais que os sem texto.
- A legenda está queimada no vídeo: a mesma peça com legenda teve 4,6x a mediana de views.
- Uma pergunta fica aberta e só se resolve depois: "no mesmo lugar" só se explica em "morre no intervalo".

O que ficou de fora, porque afundou nas três rodadas da sua pesquisa:
- Ensino tático.
- Tese abstrata.
- Abertura de aquecimento.
- Palavra-chave no gancho.

**Confiança:** média para a forma, baixa para o número exato. A amostra em português é de contas pequenas, e nelas um compartilhamento muda o ranking. Por isso o plano prevê teste de ganchos (seção 7).

---

## 4. Roteiro final (aprovado nas ferramentas da skill)

O gancho foi testado no **hookscore** do /ig-reel. A primeira versão ("Nutricionista, especialista em consórcio, dentista, advogado.") tirou **28,6 (fraco)**: não falava com quem assiste nem dizia o que estava em jogo. A versão final, **"Em Campinas, você perde cliente no mesmo lugar."**, tirou **87,0 (forte)**, com 8 palavras e cerca de 2,9s. As profissões continuam chamadas pelo nome, mas na tela (desde o primeiro quadro) e no trecho do "ponto em comum".

O **beats.py** deu 34,2s para o alvo de 35s (no vídeo final, a fala termina em 36,6s e a tela final fica mais 1,5s). O fim repete "cliente" do gancho, o que cria o loop de segunda visualização. A pedido da ferramenta, o fim ganhou um número concreto ("30 minutos").

| Bloco | Fala | Na tela |
|---|---|---|
| Gancho | Em Campinas, você perde cliente no mesmo lugar. | Os quatro ícones (nutrição, consórcio, odontologia, direito) com clientes caindo no mesmo buraco. Texto "ONDE O CLIENTE SOME" desde o primeiro quadro. |
| Dor | Ele pede o preço, diz que vai pensar e some. | Conversa no celular. O cliente some e fica "visto por último há 9 dias". |
| Dor (vídeo-base) | Seguidor. Curtida. Indicação. Nenhum deles diz quem vai fechar. | Widgets de métrica que apagam e um contrato com "?" |
| Ponto em comum | Nutricionista, consórcio, dentista, advogado: vocês vendem uma decisão que o cliente adia. | Quatro cartões (a dieta, a carta de crédito, o implante, o processo) com o carimbo DEPOIS |
| Autoridade | Treze anos de marketing me mostraram: a venda não morre no preço. Morre no intervalo. | "13 ANOS" em 3D, etiqueta de preço riscada, linha INTERESSE ··· INTERVALO ··· DECISÃO |
| Solução | Lançamento encurta esse intervalo: pesquisa, oferta na ordem certa, aquecimento e prazo real. | Os quatro nós entram na linha e a decisão chega mais perto |
| Por que um estrategista | Por isso todo especialista precisa de um estrategista: você atende, e eu desenho e comando. | ESPECIALISTA + ESTRATEGISTA viram os dois cartões de papel |
| CTA | Me manda sua profissão. Em 30 minutos eu te mostro onde o seu cliente escapa. | Campo digitando profissões, botão ENVIAR MENSAGEM, "30 MINUTOS · SEM CUSTO", seta para o botão do anúncio |

### Voz

A narração usa o timbre do Bruno, com pronúncia do Brasil:

1. O **Kokoro** (licença Apache 2.0) lê o roteiro com a voz brasileira `pm_alex`.
2. O **ChatterboxVC** (licença MIT) troca o timbre pelo do Bruno. A referência são 11,5s da gravação `voz-03-fica-aqui`.
3. O **Whisper** confere cada trecho e refaz o que sair com palavra errada.

A semelhança com a voz do Bruno ficou em 0,88, numa escala em que duas gravações dele dão de 0,92 a 0,95 e a voz Antonio dá 0,67. A primeira tentativa, com o Chatterbox gerando a fala direto, saiu com sotaque de Portugal e foi descartada.

Três ajustes de áudio:
- "Seguidor. Curtida. Indicação." é gerado palavra por palavra, com pausa entre elas. Lido de uma vez, saía emendado.
- "Você atende. Eu desenho e comando." virou "você atende, e eu desenho e comando". Sozinho, o "Eu" soava "é o desenho". Mexer só na pronúncia acertou no máximo 2 de 6 testes do Whisper; com o "e eu", acertou 5 de 6 e, no áudio final, todas as vezes.
- A fala está 12% mais rápida, sem mudar o tom, para caber em 38,1s.

A entrada do grave da trilha cai no começo do trecho da autoridade ("Treze anos…"). Para isso, a introdução da música ganha um compasso.

---

## 5. Copy do anúncio

Os três textos passaram no **detect** do /ig-human (detector de texto com cara de IA, em português): A com 71,5, B com 74,4 e C com 75,8, todos PASS. Nenhum tem termo-clichê nem travessão.

**Texto principal A (geral):**
> Nutricionista, especialista em consórcio, dentista, advogado: em Campinas, Valinhos ou Paulínia, todo mundo perde cliente no mesmo lugar.
>
> O cliente pede o preço. Diz que vai pensar. Some.
>
> Não falta técnica pra vocês. Falta alguém cuidando do intervalo entre o interesse e a decisão, que é onde a venda morre.
>
> Em 13 anos de marketing eu vi isso em consultório, escritório e financeira. O conserto tem nome: pesquisa, oferta na ordem certa, aquecimento e prazo real. Eu desenho e comando. Você continua atendendo.
>
> Me manda sua profissão no WhatsApp. Em 30 minutos, sem custo, eu te mostro onde o seu cliente escapa.

**Texto principal B (consórcio e crédito):**
> Especialista em consórcio em Campinas: quantas simulações deste mês viraram "vou pensar"?
>
> O mercado tá em alta. De janeiro a julho foram R$ 331,6 bilhões em créditos, 22,9% a mais que em 2025, segundo a ABAC. Mesmo assim, carta de crédito é decisão grande. E decisão grande fica pra depois. Às vezes, pra nunca.
>
> A venda não morre na taxa. Morre no intervalo.
>
> Grupo com data de formação já é um prazo real. Falta a sequência antes dele: pesquisa, convite, aula e fechamento. Isso eu desenho e comando.
>
> Me chama no WhatsApp e me conta como você vende hoje. São 30 minutos de diagnóstico, sem custo.

**Texto principal C (saúde e advocacia):**
> Orçamento enviado. Paciente que sumiu depois da segunda consulta. Cliente que disse "vou ver com a família".
>
> Dentista, nutricionista e advogado de Campinas, Valinhos e Vinhedo vendem a mesma coisa: uma decisão que o cliente deixa pra depois. A dieta, o implante, o processo.
>
> Em 13 anos de marketing eu vi essa cena em consultório e escritório. Lançamento é a engenharia que encurta esse caminho, dentro das regras do CFO, do CFN e da OAB. Você atende. Eu desenho e comando.
>
> Me manda sua profissão no WhatsApp. Em 30 minutos eu te mostro onde o seu cliente escapa. Sem custo.

**Títulos (até 40 caracteres):**
- Diagnóstico gratuito em Campinas
- Onde o seu cliente escapa?
- Especialista precisa de estrategista
- A venda morre no intervalo
- Me diga sua profissão

**Descrição:** Estrategista de lançamento · 30 minutos, sem custo

**Botão:** Enviar mensagem (WhatsApp)

**Mensagem pré-preenchida no WhatsApp:**
> Oi, Bruno! Vi o anúncio de Campinas. Minha profissão é:

**Perguntas frequentes (até 4):**
- Sou nutricionista
- Trabalho com consórcio
- Sou dentista
- Sou advogado(a)

**Roteiro de qualificação (três perguntas, uma por vez):**
1. Você atende sozinho ou tem equipe?
2. Hoje o cliente mais some antes do orçamento, depois do orçamento ou depois da primeira consulta?
3. Você já tem público no Instagram ou uma lista de clientes antigos?

Fechamento:
> Pelo que você me contou, o seu intervalo está em ___. Em 30 minutos eu te mostro onde ele está e o que eu faria primeiro, sem custo e sem pitch escondido. Fica melhor ___ ou ___?

---

## 6. Configuração no Gerenciador de Anúncios (Meta)

- **Conta:** não encontrei no seu Gerenciador uma conta de anúncios do Estrategista; as que aparecem são de clientes. Use uma conta própria (ou crie uma) para não misturar cobrança, pixel e dados.
- **Objetivo:** Engajamento, com local de conversão Mensagens (WhatsApp), otimizando para conversas. A Página precisa estar ligada ao WhatsApp Business.
- **Localização:** Campinas com raio de 25 km ("pessoas que moram neste local"). Idade de 25 a 60 anos.
- **Público:** comece aberto (Advantage+), com sugestões de interesse em Nutrição, Odontologia, Direito, Consórcio, Empreendedorismo e Pequenas empresas. Quem filtra de verdade é o gancho, que chama as profissões pelo nome.
- **Posicionamentos:** Reels e Stories (vídeo 9:16) e Feed (vídeo 4:5).
- **Teste de 7 dias:**
  - Estrutura: 1 campanha com 2 conjuntos, (A) aberto e (B) com interesses empilhados.
  - Anúncios: o mesmo vídeo com os 3 textos.
- **Verba sugerida:** de R$ 40 a R$ 60 por dia, por 7 dias (R$ 280 a R$ 420), para ter leitura. Isso não é promessa de resultado.
- **Régua de leitura**, nesta ordem:
  1. Taxa de gancho: views de 3s ÷ impressões, acima de 30%.
  2. Conversas iniciadas.
  3. % de conversas com profissional do perfil certo.
  4. Diagnósticos agendados.
  5. Propostas.
  6. Contratos.

  O custo por conversa sozinho não decide; quem decide é o custo por contrato.
- **Rastreamento:** a mensagem pré-preenchida identifica o anúncio. Use uma etiqueta "anúncio Campinas" no WhatsApp Business e anote, para cada conversa, a profissão, onde o cliente some e o estágio.

---

## 7. Próximos testes

1. **Gancho por nicho.** Mudam só os primeiros 3 segundos e o resto do vídeo é o mesmo. Notas no hookscore:
   - "Consórcio em Campinas: você perde a venda no mesmo lugar." (84,4)
   - "Advogado em Campinas, você perde o cliente depois da primeira consulta." (80,0)
   - "Dentista em Campinas, você perde o paciente depois do orçamento." (76,4)
   - "Nutricionista em Campinas, você perde o paciente na segunda consulta." (76,4)
2. **Remarketing** para quem viu 50% do vídeo, com o convite direto para o diagnóstico.
3. **Comparar a taxa de gancho de cada versão em 48h.** A versão vencedora vira série, com outros temas na mesma forma.

---

## 8. Cuidados de política e de conselho

- **Meta:**
  - O anúncio não afirma nenhum atributo pessoal de quem assiste. Profissão pode; saúde e finanças pessoais, não.
  - O anúncio não oferece consórcio ao consumidor.
  - Se o Meta classificar o anúncio como financeiro mesmo assim, tire "carta de crédito" da copy e reenvie.
- Sem promessa de resultado, prazo ou número.
- Na hora de executar o lançamento de cada cliente, mandam as regras do conselho dele:
  - CFN, CFO, CFM e CFP.
  - OAB (Provimento 205/2021).

Fontes de mercado: ABAC via [Legismap (julho/2026)](https://legismap.com.br/conteudos/artigos-e-noticias/sistema-de-consorcios-em-julho-2026-dados-economicos) e [DGABC](https://www.dgabc.com.br/Noticia/4337927/consorcios-crescem-no-semestre-e-batem-recordes-no-pais); Campinas: [Caravela](https://www.caravela.info/regional/campinas---sp) e [Alesp](https://www.al.sp.gov.br/noticia/?id=496543).
