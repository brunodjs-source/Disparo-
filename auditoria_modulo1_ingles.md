# Auditoria — Módulo 1 (Básico 1) da plataforma World Teaching School

**Data:** 14/10/2026
**Módulo auditado:** `Basico 1 - Introducao ao Ingles` (Level A1) — https://app.worldteachingschool.com.br/modules/f2207734-be2a-4988-9d1c-2797992edb61
**Base da auditoria:** os 5 documentos enviados pela cliente (Alphabet & Sounds, Greetings, Personal Pronouns & Verb To Be, Days/Months & Time, Family/Countries & Professions + Object Pronouns) comparados, exercício por exercício, com os 280 exercícios cadastrados na plataforma (conteúdo, opções, resposta correta, transcrição de áudio e explicação foram extraídos pela API da própria plataforma).

---

## 1. Resumo executivo

| Tópico na plataforma | Exercícios pedidos no doc | Exercícios na plataforma | Pedidos encontrados | Situação |
|---|---|---|---|---|
| 1 — Alphabet & Sounds | 15 | 30 | 15 / 15 | ✅ Completo (+15 extras, incl. 4 speaking) |
| 2 — Greetings | 30 (20 + 10 speaking) | 41 | 30 / 30 | ✅ Completo (+11 extras) |
| 3 — Personal Pronouns & Verb To Be | 25 | 36 | 25 / 25 | ✅ Completo (+11 extras) |
| 4 — Numbers, Colors & Basic Adjectives | **sem documento enviado** | 51 | — | ⚠️ Não auditável |
| 5 — Days, Months & Time | 20 + 7 writing + 7 speaking extras | 50 | 34 / 34 | ✅ Completo (+16 extras) |
| 6 — Family, Countries & Professions | 20 | 35 | 18 / 20 | ⚠️ 2 exercícios parciais |
| 7 — Object Pronouns | 20 | 37 | 20 / 20 | ✅ Completo (+17 extras) |

**Total: 144 exercícios solicitados → 142 implementados integralmente, 2 implementados parcialmente, 0 ausentes.**

Regras gerais dos documentos também foram verificadas:

- "Evitar a expressão *Hey* em toda a aplicação" → **cumprido** (0 ocorrências nos 280 exercícios; o exercício "Greeting Puzzle" foi adaptado de "Hey, Ben!" para "Hello, Ben!").
- Todo exercício tem feedback/explicação em português → **cumprido** (280/280).
- Todo exercício de Listening e Speaking tem áudio gerado → **cumprido**.
- "Evitar *What comes after B?* / sequências de calendário / respostas por imagem" → **cumprido** (nenhum exercício desse tipo foi encontrado).
- Pedido extra do doc de Days: "Ela está em casa na segunda-feira (todos os dias) no Writing e no Speaking para ouvir e repetir" → **cumprido** (7 writing #44–50 e 7 speaking #32–38).

---

## 2. Dez exemplos do que FOI FEITO (conforme solicitado)

| # | Doc da cliente | Na plataforma | Evidência |
|---|---|---|---|
| 1 | **Alphabet — Reading 1 "Wrong Name Tag"** (Ben / B-E-N / crachá VEN) | Tópico 1, ex. #21 (reading_comprehension) | Passagem, 3 alternativas e resposta "A) The first letter is wrong" idênticas ao doc. |
| 2 | **Alphabet — Listening 14 "New Gamer"** (montar J-A-X com as letras G-A-J-E-X-S) | Tópico 1, ex. #14 (word_order, modo letras) | Mesmas 6 letras disponíveis, áudio "My username is Jax. J-A-X.", resposta j-a-x. |
| 3 | **Greetings — Grammar 5 "Repair the chat"** (You'm good → I'm) | Tópico 2, ex. #5 (tap_wrong_word) | Texto "Anna: You'm good, thanks!", correção you'm → i'm, opções I'm / You're / Am. |
| 4 | **Greetings — Listening 19 "The audio stops"** (áudio corta em "How are—") | Tópico 2, ex. #14 | Transcrição "Anna: Hello, Leo! How are" (cortada), resposta "you". |
| 5 | **Greetings — Speaking 9 "Follow the Conversation"** (ouvir, depois ser o Ben em 2 falas) | Tópico 2, ex. #35 (speaking com 2 turnos) | Diálogo Sarah/Ben completo + 2 turnos: "Good morning, Sarah." e "I'm fine, thanks. How are you?" |
| 6 | **Pronouns — Speaking 25 "The Pronoun Switch — Final Challenge"** (She / He / They em 3 perguntas) | Tópico 3, ex. #31 (speaking com 3 turnos) | Turnos "Tell me about Anna / Leo / Anna and Leo" com alvos She is a student / He is a student / They are students. |
| 7 | **Pronouns — Reading 20 "The profile puzzle"** (Daniel 19, Sofia 22, We are students) | Tópico 3, ex. #25 (multi_blank) | Texto idêntico, 3 lacunas I / She / They. |
| 8 | **Days — Speaking 20 "Weekly Memory Challenge"** (ouvir 1x, 5 detalhes = Perfect schedule) | Tópico 5, ex. #31 | Áudio da Sofia idêntico, 5 grupos de palavras-chave de pontuação (she/her, busy+Monday, class+Wednesday, seven, free+Friday). |
| 9 | **Days — pedido extra "Ela está em casa na segunda-feira… todos os dias"** | Tópico 5, ex. #44–#50 (writing) e #32–#38 (speaking "Listen and repeat") | 7 frases alternando She/He com os 7 dias, nas duas habilidades, com áudio no speaking. |
| 10 | **Family — Speaking 15 "Family Profile Challenge"** (6 detalhes = Family Expert) | Tópico 6, ex. #30 | Áudio da Anna idêntico, 6 grupos de pontuação (mother/Emma, teacher/England, Monday/eight, father/Leo, doctor/Brazil, Tuesday/seven). |

Outros exemplos conferidos e idênticos: Object Pronouns Reading 1–5, Listening 6–10, Writing 11–15 e Speaking 16–20 (Tópico 7 #11–#15, #21–#27, #28–#37), Family Listening 6–10 (Tópico 6 #11–#15), Greetings Writing 11–15 (Tópico 2 #37–#41), Pronouns Writing 11–15 (Tópico 3 #32–#36).

---

## 3. Dez pontos que NÃO foram feitos ou ficaram parciais / divergentes

Como praticamente todos os exercícios foram implementados, a lista abaixo mistura (a) partes de exercícios faltando, (b) pedidos que não puderam ser verificados e (c) divergências de padrão em relação ao que o doc estabelece.

| # | O que o doc pede | O que está na plataforma | Gravidade |
|---|---|---|---|
| 1 | **Family — Reading 4 "The Wrong Family Report"**: o aluno deve **reescrever** a frase errada ("Julia is a teacher from Italy") **e depois completar** "Ben is her ___. He is from ___" (uncle / Canada). | Tópico 6 #24 virou um *tap_wrong_word* (toca em "doctor" → "teacher"). A segunda parte (uncle / Canada) **não existe**. | ⚠️ Parcial |
| 2 | **Family — Writing 20 "Build a Family Schedule"**: o aluno escreve **dois perfis** — primeiro Sofia (aunt/chef/Mexico/Sunday/six), depois Daniel. | Tópico 6 #35 entrega o perfil da Sofia **pronto como exemplo** e só pede o de Daniel. Metade da produção escrita foi removida. | ⚠️ Parcial |
| 3 | **Tópico 4 — Numbers, Colors & Basic Adjectives**: nenhum documento foi enviado pela cliente. | 51 exercícios cadastrados sem especificação para comparar. Não é possível atestar aderência. | ⚠️ Não auditável |
| 4 | **Padrão de idioma dos enunciados**: todos os docs trazem enunciados em inglês. | Tópico 5, writing #39–#50 estão com enunciado **em português** ("Mia diz…", "Escreva em inglês…"), enquanto os outros 268 exercícios estão em inglês. Inconsistência visível ao aluno. | ⚠️ Divergência |
| 5 | **Greetings — Speaking 2**: após a resposta do aluno, "Mia replies: *That's great!*". **Speaking 10**: após a resposta, "Leo answers: *Great! Have a good class!*". | Tópico 2 #28 e #36 não têm a fala de fechamento da personagem; a cena termina na fala do aluno. | 🔹 Menor |
| 6 | **Perguntas do interlocutor devem ser ouvidas**: ex. Pronouns Speaking 21 "Lucas asks: *Who is Mia?*", Speaking 22 "Anna asks: *What about Ben and Leo?*", Days Speaking 18 "Anna asks: *What about us?*". | Em Tópico 3 #27, #28, #29 e Tópico 5 #29 a pergunta aparece **só no texto da cena**, não no áudio (o áudio tem apenas a fala original). Em outros exercícios (ex. Tópico 7 #28) o narrador **está** no áudio — padrão inconsistente. | 🔹 Menor |
| 7 | **Greetings — Speaking 6 "The Wrong Recording"**: "Then compare: Ben's recording × Student recording". | Tópico 2 #32 pede a gravação correta, mas não há etapa de comparação lado a lado com a gravação errada do Ben. | 🔹 Menor / não verificável |
| 8 | **Greetings — Speaking 4 "Anna Stops Talking"**: "Then the complete audio plays" após a resposta. **Listening 18**: "Replay: I'm fine, thanks!". | Tópico 2 #30 e #13: não há indicação de reprodução do áudio completo após a resposta. | 🔹 Menor / não verificável |
| 9 | **Object Pronouns — Reading 2**: além da lacuna, o doc pede o quadro "Compare: father → him / mother → her". | Tópico 7 #23 tem só a lacuna; a comparação explícita não aparece ao aluno (apenas na explicação pós-resposta). | 🔹 Menor |
| 10 | **Lógica pedagógica dos docs**: "evitar perguntas resolvidas apenas por tradução" e "evitar repetição isolada (*Say Hello*)". | Os 7 writing #44–#50 são tradução direta PT→EN e os 7 speaking #32–#38 são "Listen and repeat" puro. **Foi um pedido explícito da cliente no doc de Days**, mas contradiz a diretriz geral dela — vale alinhar. | 🔹 Observação |

---

## 4. Extras entregues além do solicitado (para conhecimento)

- Tópico 1: +5 grammar, +5 listening, +1 reading, +4 speaking (o doc não previa speaking para Alphabet).
- Tópico 2: +5 grammar, +5 listening, +1 reading.
- Tópico 3: +5 grammar, +5 listening, +1 reading.
- Tópico 5: +10 grammar, +5 listening, +1 reading (o doc não previa Grammar para Days).
- Tópico 6: +10 grammar, +5 listening (o doc não previa Grammar para Family).
- Tópico 7: +10 grammar, +5 listening, +2 reading (o doc especificava Reading, Listening, Writing e Speaking; todos os 20 foram encontrados).

Todos os extras seguem o mesmo padrão pedagógico dos docs (personagens Mia/Leo/Ben/Anna, mudança de perspectiva, correção de transcrição), sem exercícios de lista ou de lógica pura.

---

## 5. Recomendações

1. Completar a segunda parte do Tópico 6 #24 (uncle / Canada) e adicionar o perfil da Sofia como produção no Tópico 6 #35.
2. Traduzir os enunciados do Tópico 5 #39–#50 para inglês (ou definir com a cliente se enunciados em PT são desejados).
3. Solicitar à cliente o documento de **Numbers, Colors & Basic Adjectives** para auditar o Tópico 4.
4. Padronizar: pergunta do narrador/interlocutor sempre no áudio dos exercícios de speaking.
5. Adicionar falas de fechamento (Tópico 2 #28 e #36) se o fluxo da cena for importante para a cliente.
