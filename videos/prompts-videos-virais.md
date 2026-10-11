# Prompts de vídeo · O Estrategista (motion com Claude, até 40s)
Baseado no guia *Motion com Claude* e na base de conhecimento `conhecimento-o-estrategista.md`.
**Como usar:** copie o bloco inteiro de um vídeo numa conversa nova do Claude. Narração: use o texto da seção *Narração* no ElevenLabs (Multilingual v2, Stability 40–50%, Similarity 75%, Style 15–25%, Speaker boost ligado) ou grave com a sua voz. Depois confira os tempos reais e ajuste na Parte 2.
**Regras da marca respeitadas:** sem travessão na fala, sem promessa de número/prazo, sem citar fontes externas, uma palavra em ouro por frase, palavra-chave só no fim. Cada roteiro fica entre 55 e 85 palavras (cabe em 40 s).

---

## Vídeo 01 · Cem mil seguidores, catorze vendas

**Dor:** um expert com muita audiência que lançou e quase não vendeu; o problema não é o tamanho da audiência, é a ordem do lançamento. **CTA:** PARTIDA. **Palavras:** 64

### Narração (ElevenLabs)
```
Cem mil seguidores. Catorze vendas.
<break time="0.6s" />
O problema não foi o produto. Foi a ordem em que o lançamento foi jogado.
<break time="0.6s" />
Promessa antes da pesquisa. Captação sem convite. Carrinho aberto sem aquecimento.
<break time="0.6s" />
Seguidor aplaude. Comprador decide. São pessoas diferentes.
<break time="0.6s" />
Eu desenho e comando o lançamento em cinco lances, cada um com data, número e plano B.
<break time="0.6s" />
Comenta PARTIDA que eu te mostro por onde começar.
```

### Prompt para o Claude
```
Você é um motion designer sênior e desenvolvedor front-end. Crie uma animação vertical para Reels, em um único arquivo HTML, que eu vou gravar da tela para virar vídeo.

PARTE 1 · MINHA MARCA
Marca: O Estrategista (Bruno | Estrategista de Lançamento, @o_estrategista.com.br)
Sobre o que é o vídeo: um expert com muita audiência que lançou e quase não vendeu; o problema não é o tamanho da audiência, é a ordem do lançamento
Público: experts que já têm audiência e já faturam (médicos, dentistas, advogados, psicólogos, nutricionistas com 20 a 150 mil seguidores) e infoprodutores orgânicos estagnados
Tom: calmo, direto, sério, de quem já viu o filme e conta o final. Comandante, não vendedor.
Cores (hex): fundo #050505 · texto #EFE6D6 · destaque #E8B36A (ouro, usado só como luz ou em UMA palavra por frase) · apoio #9A5F2A
Fontes (Google Fonts): títulos Playfair Display 600 · textos Inter (Cinzel 500 caps só para rótulos pequenos)
Referências visuais: tabuleiro de xadrez escuro com luz dourada lateral, peças surgindo em silhueta; ritmo seco e elegante, sem exagero; transições de zoom com desfoque e um brilho dourado passando; visual premium e sóbrio, nada de amarelo chapado, azul ou ostentação
Palavra do CTA: PARTIDA

PARTE 2 · ROTEIRO E TEMPOS
Duração total: 40 segundos
Cena 1 (Gancho (dor)) · [0,0–3,0 s] · Fala: "Cem mil seguidores. Catorze vendas." · Na tela: 100.000 → 14 (contador caindo)
Cena 2 (Revelação) · [3,5–9,5 s] · Fala: "O problema não foi o produto. Foi a ordem em que o lançamento foi jogado." · Na tela: peças de xadrez fora de posição
Cena 3 (Prova) · [10,0–17,0 s] · Fala: "Promessa antes da pesquisa. Captação sem convite. Carrinho aberto sem aquecimento." · Na tela: checklist de 3 itens com X dourado
Cena 4 (Contraste) · [17,5–24,5 s] · Fala: "Seguidor aplaude. Comprador decide. São pessoas diferentes." · Na tela: duas colunas: seguidor x comprador
Cena 5 (Virada (solução com autoridade)) · [25,0–31,5 s] · Fala: "Eu desenho e comando o lançamento em cinco lances, cada um com data, número e plano B." · Na tela: 5 casas do tabuleiro acendendo
Cena 6 (CTA) · [32,0–40,0 s] · Fala: "Comenta PARTIDA que eu te mostro por onde começar." · Na tela: PARTIDA + caixa de comentário

PARTE 3 · DIREÇÃO (não precisa mudar)
Formato e técnica
- Um único arquivo HTML com CSS e JavaScript puro, sem bibliotecas. Pode usar Google Fonts.
- Palco fixo de 1080x1920 px, centralizado e escalado para caber na janela, com fundo preto em volta.
- O vídeo inteiro é controlado por um relógio único: uma função render(t) que define o estado de cada elemento a partir do tempo t, em segundos. Não use animações CSS soltas; assim o vídeo sempre toca igual.
- Ao abrir: tela preta com "Clique ou aperte ESPAÇO para começar". Ao começar: contagem 3-2-1 (1 s cada), depois o vídeo toca uma vez e congela no último quadro.
- Atalhos: ESPAÇO pausa/continua · R reinicia com a contagem · setas esquerda/direita pulam de cena · T mostra/esconde o tempo atual no canto (escondido por padrão).
- Esconda o cursor durante a reprodução. Anime principalmente transform e opacity para rodar liso.
Estilo e movimento
- Cada fala vira texto grande na tela, entrando palavra por palavra no ritmo da narração (distribua as palavras dentro do tempo de cada cena).
- Destaque 1 ou 2 palavras-chave por frase com a cor de destaque.
- Entradas rápidas que desaceleram no fim (ease-out exponencial, 400 a 700 ms), com um leve desfoque que some ao entrar. Mesmo estilo de movimento no vídeo todo.
- Uma ideia por cena. Além do texto, cada cena tem um elemento visual que mostra o que a fala diz (cards, ícones, interface, números, gráficos, checklist, peças de xadrez), feito em HTML, CSS ou SVG.
- Transição em todas as trocas de cena (zoom com desfoque, flash de luz ou deslize rápido) e uma aproximação lenta e contínua da câmera: nada fica 100% parado.
- Fundo vivo: manchas de luz nas cores da marca se movendo devagar, granulado sutil e vinheta nas bordas.
- Títulos entre 90 e 140 px (só a palavra do CTA pode ser maior); nenhum texto menor que 40 px; no máximo 2 fontes.
- Área segura do Reels: nenhum texto acima de y = 280 px nem abaixo de y = 1250 px, e pelo menos 70 px de margem nas laterais.
- Cena final: a palavra do CTA bem grande com um brilho passando, uma caixa de comentário simulada digitando essa palavra, e 3 segundos parada no fim.
Entrega
- Entregue o código completo e pronto, num único arquivo.
- Depois do código, liste em uma linha por cena o que acontece e em que segundo, para eu revisar.
```

---

## Vídeo 02 · Live cheia, venda zero

**Dor:** a live lotada que não vende porque ensinou demais e não elevou o desejo. **CTA:** TABULEIRO. **Palavras:** 64

### Narração (ElevenLabs)
```
Sua live lotou. E ninguém comprou.
<break time="0.6s" />
Você ensinou demais. Quem aprende tudo de graça não sente que precisa de você.
<break time="0.6s" />
Evento bom faz três travessias: indignação, desejo de mudança e o caminho.
<break time="0.6s" />
Live que ensina, enche. Live que eleva, vende.
<break time="0.6s" />
O conteúdo do evento se desenha de trás pra frente, a partir da oferta.
<break time="0.6s" />
Comenta TABULEIRO e veja em qual casa seu lançamento trava.
```

### Prompt para o Claude
```
Você é um motion designer sênior e desenvolvedor front-end. Crie uma animação vertical para Reels, em um único arquivo HTML, que eu vou gravar da tela para virar vídeo.

PARTE 1 · MINHA MARCA
Marca: O Estrategista (Bruno | Estrategista de Lançamento, @o_estrategista.com.br)
Sobre o que é o vídeo: a live lotada que não vende porque ensinou demais e não elevou o desejo
Público: experts que já têm audiência e já faturam (médicos, dentistas, advogados, psicólogos, nutricionistas com 20 a 150 mil seguidores) e infoprodutores orgânicos estagnados
Tom: calmo, direto, sério, de quem já viu o filme e conta o final. Comandante, não vendedor.
Cores (hex): fundo #050505 · texto #EFE6D6 · destaque #E8B36A (ouro, usado só como luz ou em UMA palavra por frase) · apoio #9A5F2A
Fontes (Google Fonts): títulos Playfair Display 600 · textos Inter (Cinzel 500 caps só para rótulos pequenos)
Referências visuais: tabuleiro de xadrez escuro com luz dourada lateral, peças surgindo em silhueta; ritmo seco e elegante, sem exagero; transições de zoom com desfoque e um brilho dourado passando; visual premium e sóbrio, nada de amarelo chapado, azul ou ostentação
Palavra do CTA: TABULEIRO

PARTE 2 · ROTEIRO E TEMPOS
Duração total: 40 segundos
Cena 1 (Gancho (dor)) · [0,0–3,0 s] · Fala: "Sua live lotou. E ninguém comprou." · Na tela: contador de espectadores alto, vendas 0
Cena 2 (Revelação) · [3,5–9,5 s] · Fala: "Você ensinou demais. Quem aprende tudo de graça não sente que precisa de você." · Na tela: quadro cheio de anotações apagando
Cena 3 (Prova) · [10,0–17,0 s] · Fala: "Evento bom faz três travessias: indignação, desejo de mudança e o caminho." · Na tela: 3 setas em sequência
Cena 4 (Contraste) · [17,5–24,5 s] · Fala: "Live que ensina, enche. Live que eleva, vende." · Na tela: antes x depois: aula x oferta
Cena 5 (Virada (solução com autoridade)) · [25,0–31,5 s] · Fala: "O conteúdo do evento se desenha de trás pra frente, a partir da oferta." · Na tela: seta voltando da oferta ao início
Cena 6 (CTA) · [32,0–40,0 s] · Fala: "Comenta TABULEIRO e veja em qual casa seu lançamento trava." · Na tela: TABULEIRO + caixa de comentário

PARTE 3 · DIREÇÃO (não precisa mudar)
Formato e técnica
- Um único arquivo HTML com CSS e JavaScript puro, sem bibliotecas. Pode usar Google Fonts.
- Palco fixo de 1080x1920 px, centralizado e escalado para caber na janela, com fundo preto em volta.
- O vídeo inteiro é controlado por um relógio único: uma função render(t) que define o estado de cada elemento a partir do tempo t, em segundos. Não use animações CSS soltas; assim o vídeo sempre toca igual.
- Ao abrir: tela preta com "Clique ou aperte ESPAÇO para começar". Ao começar: contagem 3-2-1 (1 s cada), depois o vídeo toca uma vez e congela no último quadro.
- Atalhos: ESPAÇO pausa/continua · R reinicia com a contagem · setas esquerda/direita pulam de cena · T mostra/esconde o tempo atual no canto (escondido por padrão).
- Esconda o cursor durante a reprodução. Anime principalmente transform e opacity para rodar liso.
Estilo e movimento
- Cada fala vira texto grande na tela, entrando palavra por palavra no ritmo da narração (distribua as palavras dentro do tempo de cada cena).
- Destaque 1 ou 2 palavras-chave por frase com a cor de destaque.
- Entradas rápidas que desaceleram no fim (ease-out exponencial, 400 a 700 ms), com um leve desfoque que some ao entrar. Mesmo estilo de movimento no vídeo todo.
- Uma ideia por cena. Além do texto, cada cena tem um elemento visual que mostra o que a fala diz (cards, ícones, interface, números, gráficos, checklist, peças de xadrez), feito em HTML, CSS ou SVG.
- Transição em todas as trocas de cena (zoom com desfoque, flash de luz ou deslize rápido) e uma aproximação lenta e contínua da câmera: nada fica 100% parado.
- Fundo vivo: manchas de luz nas cores da marca se movendo devagar, granulado sutil e vinheta nas bordas.
- Títulos entre 90 e 140 px (só a palavra do CTA pode ser maior); nenhum texto menor que 40 px; no máximo 2 fontes.
- Área segura do Reels: nenhum texto acima de y = 280 px nem abaixo de y = 1250 px, e pelo menos 70 px de margem nas laterais.
- Cena final: a palavra do CTA bem grande com um brilho passando, uma caixa de comentário simulada digitando essa palavra, e 3 segundos parada no fim.
Entrega
- Entregue o código completo e pronto, num único arquivo.
- Depois do código, liste em uma linha por cena o que acontece e em que segundo, para eu revisar.
```

---

## Vídeo 03 · Psicólogo com fila de espera

**Dor:** profissional de saúde com agenda lotada que já tem um produto pronto e não percebe. **CTA:** CASA. **Palavras:** 81

### Narração (ElevenLabs)
```
Psicólogo com fila de espera tem um produto pronto. E ainda não percebeu.
<break time="0.6s" />
Sua agenda cheia é um teto. Você só vende as horas que tem.
<break time="0.6s" />
A fila prova a demanda. A audiência prova a confiança. Falta a engenharia.
<break time="0.6s" />
Hoje você atende quarenta por mês. Um lançamento atende quatrocentos sem você estar na sala.
<break time="0.6s" />
Eu desenho o lançamento com a sua ética e o seu conselho no centro. Você entra com o conhecimento.
<break time="0.6s" />
Comenta CASA que eu te explico como funciona.
```

### Prompt para o Claude
```
Você é um motion designer sênior e desenvolvedor front-end. Crie uma animação vertical para Reels, em um único arquivo HTML, que eu vou gravar da tela para virar vídeo.

PARTE 1 · MINHA MARCA
Marca: O Estrategista (Bruno | Estrategista de Lançamento, @o_estrategista.com.br)
Sobre o que é o vídeo: profissional de saúde com agenda lotada que já tem um produto pronto e não percebe
Público: experts que já têm audiência e já faturam (médicos, dentistas, advogados, psicólogos, nutricionistas com 20 a 150 mil seguidores) e infoprodutores orgânicos estagnados
Tom: calmo, direto, sério, de quem já viu o filme e conta o final. Comandante, não vendedor.
Cores (hex): fundo #050505 · texto #EFE6D6 · destaque #E8B36A (ouro, usado só como luz ou em UMA palavra por frase) · apoio #9A5F2A
Fontes (Google Fonts): títulos Playfair Display 600 · textos Inter (Cinzel 500 caps só para rótulos pequenos)
Referências visuais: tabuleiro de xadrez escuro com luz dourada lateral, peças surgindo em silhueta; ritmo seco e elegante, sem exagero; transições de zoom com desfoque e um brilho dourado passando; visual premium e sóbrio, nada de amarelo chapado, azul ou ostentação
Palavra do CTA: CASA

PARTE 2 · ROTEIRO E TEMPOS
Duração total: 40 segundos
Cena 1 (Gancho (dor)) · [0,0–3,0 s] · Fala: "Psicólogo com fila de espera tem um produto pronto. E ainda não percebeu." · Na tela: agenda lotada, células preenchidas
Cena 2 (Revelação) · [3,5–9,5 s] · Fala: "Sua agenda cheia é um teto. Você só vende as horas que tem." · Na tela: barra de horas batendo no limite
Cena 3 (Prova) · [10,0–17,0 s] · Fala: "A fila prova a demanda. A audiência prova a confiança. Falta a engenharia." · Na tela: 2 cards verdes e 1 vazio dourado
Cena 4 (Contraste) · [17,5–24,5 s] · Fala: "Hoje você atende quarenta por mês. Um lançamento atende quatrocentos sem você estar na sala." · Na tela: 40 → 400
Cena 5 (Virada (solução com autoridade)) · [25,0–31,5 s] · Fala: "Eu desenho o lançamento com a sua ética e o seu conselho no centro. Você entra com o conhecimento." · Na tela: escudo + tabuleiro
Cena 6 (CTA) · [32,0–40,0 s] · Fala: "Comenta CASA que eu te explico como funciona." · Na tela: CASA + caixa de comentário

PARTE 3 · DIREÇÃO (não precisa mudar)
Formato e técnica
- Um único arquivo HTML com CSS e JavaScript puro, sem bibliotecas. Pode usar Google Fonts.
- Palco fixo de 1080x1920 px, centralizado e escalado para caber na janela, com fundo preto em volta.
- O vídeo inteiro é controlado por um relógio único: uma função render(t) que define o estado de cada elemento a partir do tempo t, em segundos. Não use animações CSS soltas; assim o vídeo sempre toca igual.
- Ao abrir: tela preta com "Clique ou aperte ESPAÇO para começar". Ao começar: contagem 3-2-1 (1 s cada), depois o vídeo toca uma vez e congela no último quadro.
- Atalhos: ESPAÇO pausa/continua · R reinicia com a contagem · setas esquerda/direita pulam de cena · T mostra/esconde o tempo atual no canto (escondido por padrão).
- Esconda o cursor durante a reprodução. Anime principalmente transform e opacity para rodar liso.
Estilo e movimento
- Cada fala vira texto grande na tela, entrando palavra por palavra no ritmo da narração (distribua as palavras dentro do tempo de cada cena).
- Destaque 1 ou 2 palavras-chave por frase com a cor de destaque.
- Entradas rápidas que desaceleram no fim (ease-out exponencial, 400 a 700 ms), com um leve desfoque que some ao entrar. Mesmo estilo de movimento no vídeo todo.
- Uma ideia por cena. Além do texto, cada cena tem um elemento visual que mostra o que a fala diz (cards, ícones, interface, números, gráficos, checklist, peças de xadrez), feito em HTML, CSS ou SVG.
- Transição em todas as trocas de cena (zoom com desfoque, flash de luz ou deslize rápido) e uma aproximação lenta e contínua da câmera: nada fica 100% parado.
- Fundo vivo: manchas de luz nas cores da marca se movendo devagar, granulado sutil e vinheta nas bordas.
- Títulos entre 90 e 140 px (só a palavra do CTA pode ser maior); nenhum texto menor que 40 px; no máximo 2 fontes.
- Área segura do Reels: nenhum texto acima de y = 280 px nem abaixo de y = 1250 px, e pelo menos 70 px de margem nas laterais.
- Cena final: a palavra do CTA bem grande com um brilho passando, uma caixa de comentário simulada digitando essa palavra, e 3 segundos parada no fim.
Entrega
- Entregue o código completo e pronto, num único arquivo.
- Depois do código, liste em uma linha por cena o que acontece e em que segundo, para eu revisar.
```

---

## Vídeo 04 · Desconto é confissão

**Dor:** dar desconto no carrinho sinaliza que a oferta não foi construída; a saída é a escada pós-carrinho. **CTA:** PARTIDA. **Palavras:** 61

### Narração (ElevenLabs)
```
Desconto no carrinho é confissão.
<break time="0.6s" />
Confessa que a oferta não tinha valor percebido suficiente.
<break time="0.6s" />
Oferta forte tem oportunidade, prova, história, objeção invertida e o preço por último.
<break time="0.6s" />
Preço errado pra cima tem conserto. Pra baixo, quase nunca.
<break time="0.6s" />
Antes de baixar o preço, eu reabro. O downsell nasce da pesquisa com quem não comprou.
<break time="0.6s" />
Comenta PARTIDA e eu te mostro a escada.
```

### Prompt para o Claude
```
Você é um motion designer sênior e desenvolvedor front-end. Crie uma animação vertical para Reels, em um único arquivo HTML, que eu vou gravar da tela para virar vídeo.

PARTE 1 · MINHA MARCA
Marca: O Estrategista (Bruno | Estrategista de Lançamento, @o_estrategista.com.br)
Sobre o que é o vídeo: dar desconto no carrinho sinaliza que a oferta não foi construída; a saída é a escada pós-carrinho
Público: experts que já têm audiência e já faturam (médicos, dentistas, advogados, psicólogos, nutricionistas com 20 a 150 mil seguidores) e infoprodutores orgânicos estagnados
Tom: calmo, direto, sério, de quem já viu o filme e conta o final. Comandante, não vendedor.
Cores (hex): fundo #050505 · texto #EFE6D6 · destaque #E8B36A (ouro, usado só como luz ou em UMA palavra por frase) · apoio #9A5F2A
Fontes (Google Fonts): títulos Playfair Display 600 · textos Inter (Cinzel 500 caps só para rótulos pequenos)
Referências visuais: tabuleiro de xadrez escuro com luz dourada lateral, peças surgindo em silhueta; ritmo seco e elegante, sem exagero; transições de zoom com desfoque e um brilho dourado passando; visual premium e sóbrio, nada de amarelo chapado, azul ou ostentação
Palavra do CTA: PARTIDA

PARTE 2 · ROTEIRO E TEMPOS
Duração total: 40 segundos
Cena 1 (Gancho (dor)) · [0,0–3,0 s] · Fala: "Desconto no carrinho é confissão." · Na tela: etiqueta de preço rasgando
Cena 2 (Revelação) · [3,5–9,5 s] · Fala: "Confessa que a oferta não tinha valor percebido suficiente." · Na tela: balança de valor x preço desequilibrada
Cena 3 (Prova) · [10,0–17,0 s] · Fala: "Oferta forte tem oportunidade, prova, história, objeção invertida e o preço por último." · Na tela: 5 pilares subindo
Cena 4 (Contraste) · [17,5–24,5 s] · Fala: "Preço errado pra cima tem conserto. Pra baixo, quase nunca." · Na tela: seta para cima ok, para baixo travada
Cena 5 (Virada (solução com autoridade)) · [25,0–31,5 s] · Fala: "Antes de baixar o preço, eu reabro. O downsell nasce da pesquisa com quem não comprou." · Na tela: escada: reabertura → downsell → ascensão
Cena 6 (CTA) · [32,0–40,0 s] · Fala: "Comenta PARTIDA e eu te mostro a escada." · Na tela: PARTIDA + caixa de comentário

PARTE 3 · DIREÇÃO (não precisa mudar)
Formato e técnica
- Um único arquivo HTML com CSS e JavaScript puro, sem bibliotecas. Pode usar Google Fonts.
- Palco fixo de 1080x1920 px, centralizado e escalado para caber na janela, com fundo preto em volta.
- O vídeo inteiro é controlado por um relógio único: uma função render(t) que define o estado de cada elemento a partir do tempo t, em segundos. Não use animações CSS soltas; assim o vídeo sempre toca igual.
- Ao abrir: tela preta com "Clique ou aperte ESPAÇO para começar". Ao começar: contagem 3-2-1 (1 s cada), depois o vídeo toca uma vez e congela no último quadro.
- Atalhos: ESPAÇO pausa/continua · R reinicia com a contagem · setas esquerda/direita pulam de cena · T mostra/esconde o tempo atual no canto (escondido por padrão).
- Esconda o cursor durante a reprodução. Anime principalmente transform e opacity para rodar liso.
Estilo e movimento
- Cada fala vira texto grande na tela, entrando palavra por palavra no ritmo da narração (distribua as palavras dentro do tempo de cada cena).
- Destaque 1 ou 2 palavras-chave por frase com a cor de destaque.
- Entradas rápidas que desaceleram no fim (ease-out exponencial, 400 a 700 ms), com um leve desfoque que some ao entrar. Mesmo estilo de movimento no vídeo todo.
- Uma ideia por cena. Além do texto, cada cena tem um elemento visual que mostra o que a fala diz (cards, ícones, interface, números, gráficos, checklist, peças de xadrez), feito em HTML, CSS ou SVG.
- Transição em todas as trocas de cena (zoom com desfoque, flash de luz ou deslize rápido) e uma aproximação lenta e contínua da câmera: nada fica 100% parado.
- Fundo vivo: manchas de luz nas cores da marca se movendo devagar, granulado sutil e vinheta nas bordas.
- Títulos entre 90 e 140 px (só a palavra do CTA pode ser maior); nenhum texto menor que 40 px; no máximo 2 fontes.
- Área segura do Reels: nenhum texto acima de y = 280 px nem abaixo de y = 1250 px, e pelo menos 70 px de margem nas laterais.
- Cena final: a palavra do CTA bem grande com um brilho passando, uma caixa de comentário simulada digitando essa palavra, e 3 segundos parada no fim.
Entrega
- Entregue o código completo e pronto, num único arquivo.
- Depois do código, liste em uma linha por cena o que acontece e em que segundo, para eu revisar.
```

---

## Vídeo 05 · Eu recuso lançamento

**Dor:** autoridade por recusa: por que o estrategista não aceita todo projeto. **CTA:** TABULEIRO. **Palavras:** 57

### Narração (ElevenLabs)
```
Eu recuso lançamento.
<break time="0.6s" />
De expert que nunca perguntou pra audiência o que ela compraria.
<break time="0.6s" />
A pesquisa vem antes da promessa. Sempre. Ela diz o quê, o como e o quanto.
<break time="0.6s" />
Sem pesquisa você aposta. Com pesquisa você joga.
<break time="0.6s" />
Por isso todo projeto começa pelo diagnóstico, não pela data no calendário.
<break time="0.6s" />
Comenta TABULEIRO e faça o seu diagnóstico.
```

### Prompt para o Claude
```
Você é um motion designer sênior e desenvolvedor front-end. Crie uma animação vertical para Reels, em um único arquivo HTML, que eu vou gravar da tela para virar vídeo.

PARTE 1 · MINHA MARCA
Marca: O Estrategista (Bruno | Estrategista de Lançamento, @o_estrategista.com.br)
Sobre o que é o vídeo: autoridade por recusa: por que o estrategista não aceita todo projeto
Público: experts que já têm audiência e já faturam (médicos, dentistas, advogados, psicólogos, nutricionistas com 20 a 150 mil seguidores) e infoprodutores orgânicos estagnados
Tom: calmo, direto, sério, de quem já viu o filme e conta o final. Comandante, não vendedor.
Cores (hex): fundo #050505 · texto #EFE6D6 · destaque #E8B36A (ouro, usado só como luz ou em UMA palavra por frase) · apoio #9A5F2A
Fontes (Google Fonts): títulos Playfair Display 600 · textos Inter (Cinzel 500 caps só para rótulos pequenos)
Referências visuais: tabuleiro de xadrez escuro com luz dourada lateral, peças surgindo em silhueta; ritmo seco e elegante, sem exagero; transições de zoom com desfoque e um brilho dourado passando; visual premium e sóbrio, nada de amarelo chapado, azul ou ostentação
Palavra do CTA: TABULEIRO

PARTE 2 · ROTEIRO E TEMPOS
Duração total: 40 segundos
Cena 1 (Gancho (dor)) · [0,0–3,0 s] · Fala: "Eu recuso lançamento." · Na tela: carimbo RECUSADO
Cena 2 (Revelação) · [3,5–9,5 s] · Fala: "De expert que nunca perguntou pra audiência o que ela compraria." · Na tela: balão de pergunta vazio
Cena 3 (Prova) · [10,0–17,0 s] · Fala: "A pesquisa vem antes da promessa. Sempre. Ela diz o quê, o como e o quanto." · Na tela: 3 cards: o quê / o como / o quanto
Cena 4 (Contraste) · [17,5–24,5 s] · Fala: "Sem pesquisa você aposta. Com pesquisa você joga." · Na tela: dado x peça de xadrez
Cena 5 (Virada (solução com autoridade)) · [25,0–31,5 s] · Fala: "Por isso todo projeto começa pelo diagnóstico, não pela data no calendário." · Na tela: calendário sendo trocado por lupa
Cena 6 (CTA) · [32,0–40,0 s] · Fala: "Comenta TABULEIRO e faça o seu diagnóstico." · Na tela: TABULEIRO + caixa de comentário

PARTE 3 · DIREÇÃO (não precisa mudar)
Formato e técnica
- Um único arquivo HTML com CSS e JavaScript puro, sem bibliotecas. Pode usar Google Fonts.
- Palco fixo de 1080x1920 px, centralizado e escalado para caber na janela, com fundo preto em volta.
- O vídeo inteiro é controlado por um relógio único: uma função render(t) que define o estado de cada elemento a partir do tempo t, em segundos. Não use animações CSS soltas; assim o vídeo sempre toca igual.
- Ao abrir: tela preta com "Clique ou aperte ESPAÇO para começar". Ao começar: contagem 3-2-1 (1 s cada), depois o vídeo toca uma vez e congela no último quadro.
- Atalhos: ESPAÇO pausa/continua · R reinicia com a contagem · setas esquerda/direita pulam de cena · T mostra/esconde o tempo atual no canto (escondido por padrão).
- Esconda o cursor durante a reprodução. Anime principalmente transform e opacity para rodar liso.
Estilo e movimento
- Cada fala vira texto grande na tela, entrando palavra por palavra no ritmo da narração (distribua as palavras dentro do tempo de cada cena).
- Destaque 1 ou 2 palavras-chave por frase com a cor de destaque.
- Entradas rápidas que desaceleram no fim (ease-out exponencial, 400 a 700 ms), com um leve desfoque que some ao entrar. Mesmo estilo de movimento no vídeo todo.
- Uma ideia por cena. Além do texto, cada cena tem um elemento visual que mostra o que a fala diz (cards, ícones, interface, números, gráficos, checklist, peças de xadrez), feito em HTML, CSS ou SVG.
- Transição em todas as trocas de cena (zoom com desfoque, flash de luz ou deslize rápido) e uma aproximação lenta e contínua da câmera: nada fica 100% parado.
- Fundo vivo: manchas de luz nas cores da marca se movendo devagar, granulado sutil e vinheta nas bordas.
- Títulos entre 90 e 140 px (só a palavra do CTA pode ser maior); nenhum texto menor que 40 px; no máximo 2 fontes.
- Área segura do Reels: nenhum texto acima de y = 280 px nem abaixo de y = 1250 px, e pelo menos 70 px de margem nas laterais.
- Cena final: a palavra do CTA bem grande com um brilho passando, uma caixa de comentário simulada digitando essa palavra, e 3 segundos parada no fim.
Entrega
- Entregue o código completo e pronto, num único arquivo.
- Depois do código, liste em uma linha por cena o que acontece e em que segundo, para eu revisar.
```

---

## Vídeo 06 · Quem não compra vale mais

**Dor:** o lead que não comprou é o ativo mais valioso do lançamento. **CTA:** CASA. **Palavras:** 75

### Narração (ElevenLabs)
```
Quem não comprou no seu lançamento vale mais do que quem comprou.
<break time="0.6s" />
Porque é ali que está a maior parte da sua receita escondida.
<break time="0.6s" />
Reabertura, recuperação por temperatura do lead e downsell somam de vinte a quarenta por cento a mais.
<break time="0.6s" />
A maioria fecha o carrinho e some. O lançamento acaba no auge.
<break time="0.6s" />
Eu desenho o pós-lançamento antes de abrir o carrinho. O final é decidido no começo.
<break time="0.6s" />
Comenta CASA que eu te mostro como.
```

### Prompt para o Claude
```
Você é um motion designer sênior e desenvolvedor front-end. Crie uma animação vertical para Reels, em um único arquivo HTML, que eu vou gravar da tela para virar vídeo.

PARTE 1 · MINHA MARCA
Marca: O Estrategista (Bruno | Estrategista de Lançamento, @o_estrategista.com.br)
Sobre o que é o vídeo: o lead que não comprou é o ativo mais valioso do lançamento
Público: experts que já têm audiência e já faturam (médicos, dentistas, advogados, psicólogos, nutricionistas com 20 a 150 mil seguidores) e infoprodutores orgânicos estagnados
Tom: calmo, direto, sério, de quem já viu o filme e conta o final. Comandante, não vendedor.
Cores (hex): fundo #050505 · texto #EFE6D6 · destaque #E8B36A (ouro, usado só como luz ou em UMA palavra por frase) · apoio #9A5F2A
Fontes (Google Fonts): títulos Playfair Display 600 · textos Inter (Cinzel 500 caps só para rótulos pequenos)
Referências visuais: tabuleiro de xadrez escuro com luz dourada lateral, peças surgindo em silhueta; ritmo seco e elegante, sem exagero; transições de zoom com desfoque e um brilho dourado passando; visual premium e sóbrio, nada de amarelo chapado, azul ou ostentação
Palavra do CTA: CASA

PARTE 2 · ROTEIRO E TEMPOS
Duração total: 40 segundos
Cena 1 (Gancho (dor)) · [0,0–3,0 s] · Fala: "Quem não comprou no seu lançamento vale mais do que quem comprou." · Na tela: lista de leads, a maioria em cinza
Cena 2 (Revelação) · [3,5–9,5 s] · Fala: "Porque é ali que está a maior parte da sua receita escondida." · Na tela: iceberg: parte submersa dourada
Cena 3 (Prova) · [10,0–17,0 s] · Fala: "Reabertura, recuperação por temperatura do lead e downsell somam de vinte a quarenta por cento a mais." · Na tela: gráfico de barras +20 a 40%
Cena 4 (Contraste) · [17,5–24,5 s] · Fala: "A maioria fecha o carrinho e some. O lançamento acaba no auge." · Na tela: linha caindo para zero
Cena 5 (Virada (solução com autoridade)) · [25,0–31,5 s] · Fala: "Eu desenho o pós-lançamento antes de abrir o carrinho. O final é decidido no começo." · Na tela: peão virando dama
Cena 6 (CTA) · [32,0–40,0 s] · Fala: "Comenta CASA que eu te mostro como." · Na tela: CASA + caixa de comentário

PARTE 3 · DIREÇÃO (não precisa mudar)
Formato e técnica
- Um único arquivo HTML com CSS e JavaScript puro, sem bibliotecas. Pode usar Google Fonts.
- Palco fixo de 1080x1920 px, centralizado e escalado para caber na janela, com fundo preto em volta.
- O vídeo inteiro é controlado por um relógio único: uma função render(t) que define o estado de cada elemento a partir do tempo t, em segundos. Não use animações CSS soltas; assim o vídeo sempre toca igual.
- Ao abrir: tela preta com "Clique ou aperte ESPAÇO para começar". Ao começar: contagem 3-2-1 (1 s cada), depois o vídeo toca uma vez e congela no último quadro.
- Atalhos: ESPAÇO pausa/continua · R reinicia com a contagem · setas esquerda/direita pulam de cena · T mostra/esconde o tempo atual no canto (escondido por padrão).
- Esconda o cursor durante a reprodução. Anime principalmente transform e opacity para rodar liso.
Estilo e movimento
- Cada fala vira texto grande na tela, entrando palavra por palavra no ritmo da narração (distribua as palavras dentro do tempo de cada cena).
- Destaque 1 ou 2 palavras-chave por frase com a cor de destaque.
- Entradas rápidas que desaceleram no fim (ease-out exponencial, 400 a 700 ms), com um leve desfoque que some ao entrar. Mesmo estilo de movimento no vídeo todo.
- Uma ideia por cena. Além do texto, cada cena tem um elemento visual que mostra o que a fala diz (cards, ícones, interface, números, gráficos, checklist, peças de xadrez), feito em HTML, CSS ou SVG.
- Transição em todas as trocas de cena (zoom com desfoque, flash de luz ou deslize rápido) e uma aproximação lenta e contínua da câmera: nada fica 100% parado.
- Fundo vivo: manchas de luz nas cores da marca se movendo devagar, granulado sutil e vinheta nas bordas.
- Títulos entre 90 e 140 px (só a palavra do CTA pode ser maior); nenhum texto menor que 40 px; no máximo 2 fontes.
- Área segura do Reels: nenhum texto acima de y = 280 px nem abaixo de y = 1250 px, e pelo menos 70 px de margem nas laterais.
- Cena final: a palavra do CTA bem grande com um brilho passando, uma caixa de comentário simulada digitando essa palavra, e 3 segundos parada no fim.
Entrega
- Entregue o código completo e pronto, num único arquivo.
- Depois do código, liste em uma linha por cena o que acontece e em que segundo, para eu revisar.
```

---

## Vídeo 07 · Lead barato é lead errado

**Dor:** CPL baixo engana; o que manda é o custo por cliente. **CTA:** TABULEIRO. **Palavras:** 58

### Narração (ElevenLabs)
```
Lead barato é lead errado.
<break time="0.6s" />
Você comemora o custo por lead e chora no carrinho.
<break time="0.6s" />
O custo por lead só indica. Quem manda é o custo por cliente.
<break time="0.6s" />
Mil leads curiosos vendem menos que duzentos que pediram pra entrar.
<break time="0.6s" />
Eu troco captação por convite. Quem entra já chega querendo.
<break time="0.6s" />
Comenta TABULEIRO e veja onde o seu funil vaza.
```

### Prompt para o Claude
```
Você é um motion designer sênior e desenvolvedor front-end. Crie uma animação vertical para Reels, em um único arquivo HTML, que eu vou gravar da tela para virar vídeo.

PARTE 1 · MINHA MARCA
Marca: O Estrategista (Bruno | Estrategista de Lançamento, @o_estrategista.com.br)
Sobre o que é o vídeo: CPL baixo engana; o que manda é o custo por cliente
Público: experts que já têm audiência e já faturam (médicos, dentistas, advogados, psicólogos, nutricionistas com 20 a 150 mil seguidores) e infoprodutores orgânicos estagnados
Tom: calmo, direto, sério, de quem já viu o filme e conta o final. Comandante, não vendedor.
Cores (hex): fundo #050505 · texto #EFE6D6 · destaque #E8B36A (ouro, usado só como luz ou em UMA palavra por frase) · apoio #9A5F2A
Fontes (Google Fonts): títulos Playfair Display 600 · textos Inter (Cinzel 500 caps só para rótulos pequenos)
Referências visuais: tabuleiro de xadrez escuro com luz dourada lateral, peças surgindo em silhueta; ritmo seco e elegante, sem exagero; transições de zoom com desfoque e um brilho dourado passando; visual premium e sóbrio, nada de amarelo chapado, azul ou ostentação
Palavra do CTA: TABULEIRO

PARTE 2 · ROTEIRO E TEMPOS
Duração total: 40 segundos
Cena 1 (Gancho (dor)) · [0,0–3,0 s] · Fala: "Lead barato é lead errado." · Na tela: etiqueta R$ 0,90 piscando em vermelho
Cena 2 (Revelação) · [3,5–9,5 s] · Fala: "Você comemora o custo por lead e chora no carrinho." · Na tela: gráfico CPL bom, vendas ruins
Cena 3 (Prova) · [10,0–17,0 s] · Fala: "O custo por lead só indica. Quem manda é o custo por cliente." · Na tela: CPL pequeno, CAC grande em destaque
Cena 4 (Contraste) · [17,5–24,5 s] · Fala: "Mil leads curiosos vendem menos que duzentos que pediram pra entrar." · Na tela: 1000 vs 200 com mais vendas
Cena 5 (Virada (solução com autoridade)) · [25,0–31,5 s] · Fala: "Eu troco captação por convite. Quem entra já chega querendo." · Na tela: envelope de convite dourado
Cena 6 (CTA) · [32,0–40,0 s] · Fala: "Comenta TABULEIRO e veja onde o seu funil vaza." · Na tela: TABULEIRO + caixa de comentário

PARTE 3 · DIREÇÃO (não precisa mudar)
Formato e técnica
- Um único arquivo HTML com CSS e JavaScript puro, sem bibliotecas. Pode usar Google Fonts.
- Palco fixo de 1080x1920 px, centralizado e escalado para caber na janela, com fundo preto em volta.
- O vídeo inteiro é controlado por um relógio único: uma função render(t) que define o estado de cada elemento a partir do tempo t, em segundos. Não use animações CSS soltas; assim o vídeo sempre toca igual.
- Ao abrir: tela preta com "Clique ou aperte ESPAÇO para começar". Ao começar: contagem 3-2-1 (1 s cada), depois o vídeo toca uma vez e congela no último quadro.
- Atalhos: ESPAÇO pausa/continua · R reinicia com a contagem · setas esquerda/direita pulam de cena · T mostra/esconde o tempo atual no canto (escondido por padrão).
- Esconda o cursor durante a reprodução. Anime principalmente transform e opacity para rodar liso.
Estilo e movimento
- Cada fala vira texto grande na tela, entrando palavra por palavra no ritmo da narração (distribua as palavras dentro do tempo de cada cena).
- Destaque 1 ou 2 palavras-chave por frase com a cor de destaque.
- Entradas rápidas que desaceleram no fim (ease-out exponencial, 400 a 700 ms), com um leve desfoque que some ao entrar. Mesmo estilo de movimento no vídeo todo.
- Uma ideia por cena. Além do texto, cada cena tem um elemento visual que mostra o que a fala diz (cards, ícones, interface, números, gráficos, checklist, peças de xadrez), feito em HTML, CSS ou SVG.
- Transição em todas as trocas de cena (zoom com desfoque, flash de luz ou deslize rápido) e uma aproximação lenta e contínua da câmera: nada fica 100% parado.
- Fundo vivo: manchas de luz nas cores da marca se movendo devagar, granulado sutil e vinheta nas bordas.
- Títulos entre 90 e 140 px (só a palavra do CTA pode ser maior); nenhum texto menor que 40 px; no máximo 2 fontes.
- Área segura do Reels: nenhum texto acima de y = 280 px nem abaixo de y = 1250 px, e pelo menos 70 px de margem nas laterais.
- Cena final: a palavra do CTA bem grande com um brilho passando, uma caixa de comentário simulada digitando essa palavra, e 3 segundos parada no fim.
Entrega
- Entregue o código completo e pronto, num único arquivo.
- Depois do código, liste em uma linha por cena o que acontece e em que segundo, para eu revisar.
```

---

## Vídeo 08 · Não é mais conteúdo

**Dor:** o expert que posta todo dia e não vende; falta estratégia, não conteúdo. **CTA:** PARTIDA. **Palavras:** 65

### Narração (ElevenLabs)
```
Você posta todo dia e não vende. Mais conteúdo não vai resolver.
<break time="0.6s" />
Conteúdo cria audiência. Quem transforma audiência em venda é o desenho do lançamento.
<break time="0.6s" />
Pesquisa, convite, evento, carrinho e pós. Cinco lances, nessa ordem.
<break time="0.6s" />
Sem ordem, cada post é uma jogada solta. Com ordem, vira partida.
<break time="0.6s" />
Você entra com as peças que já construiu. Do resto, cuido eu.
<break time="0.6s" />
Comenta PARTIDA que eu te chamo.
```

### Prompt para o Claude
```
Você é um motion designer sênior e desenvolvedor front-end. Crie uma animação vertical para Reels, em um único arquivo HTML, que eu vou gravar da tela para virar vídeo.

PARTE 1 · MINHA MARCA
Marca: O Estrategista (Bruno | Estrategista de Lançamento, @o_estrategista.com.br)
Sobre o que é o vídeo: o expert que posta todo dia e não vende; falta estratégia, não conteúdo
Público: experts que já têm audiência e já faturam (médicos, dentistas, advogados, psicólogos, nutricionistas com 20 a 150 mil seguidores) e infoprodutores orgânicos estagnados
Tom: calmo, direto, sério, de quem já viu o filme e conta o final. Comandante, não vendedor.
Cores (hex): fundo #050505 · texto #EFE6D6 · destaque #E8B36A (ouro, usado só como luz ou em UMA palavra por frase) · apoio #9A5F2A
Fontes (Google Fonts): títulos Playfair Display 600 · textos Inter (Cinzel 500 caps só para rótulos pequenos)
Referências visuais: tabuleiro de xadrez escuro com luz dourada lateral, peças surgindo em silhueta; ritmo seco e elegante, sem exagero; transições de zoom com desfoque e um brilho dourado passando; visual premium e sóbrio, nada de amarelo chapado, azul ou ostentação
Palavra do CTA: PARTIDA

PARTE 2 · ROTEIRO E TEMPOS
Duração total: 40 segundos
Cena 1 (Gancho (dor)) · [0,0–3,0 s] · Fala: "Você posta todo dia e não vende. Mais conteúdo não vai resolver." · Na tela: calendário cheio de posts
Cena 2 (Revelação) · [3,5–9,5 s] · Fala: "Conteúdo cria audiência. Quem transforma audiência em venda é o desenho do lançamento." · Na tela: seta audiência → venda bloqueada
Cena 3 (Prova) · [10,0–17,0 s] · Fala: "Pesquisa, convite, evento, carrinho e pós. Cinco lances, nessa ordem." · Na tela: 5 casas em sequência
Cena 4 (Contraste) · [17,5–24,5 s] · Fala: "Sem ordem, cada post é uma jogada solta. Com ordem, vira partida." · Na tela: peças soltas → formação
Cena 5 (Virada (solução com autoridade)) · [25,0–31,5 s] · Fala: "Você entra com as peças que já construiu. Do resto, cuido eu." · Na tela: mão movendo a torre
Cena 6 (CTA) · [32,0–40,0 s] · Fala: "Comenta PARTIDA que eu te chamo." · Na tela: PARTIDA + caixa de comentário

PARTE 3 · DIREÇÃO (não precisa mudar)
Formato e técnica
- Um único arquivo HTML com CSS e JavaScript puro, sem bibliotecas. Pode usar Google Fonts.
- Palco fixo de 1080x1920 px, centralizado e escalado para caber na janela, com fundo preto em volta.
- O vídeo inteiro é controlado por um relógio único: uma função render(t) que define o estado de cada elemento a partir do tempo t, em segundos. Não use animações CSS soltas; assim o vídeo sempre toca igual.
- Ao abrir: tela preta com "Clique ou aperte ESPAÇO para começar". Ao começar: contagem 3-2-1 (1 s cada), depois o vídeo toca uma vez e congela no último quadro.
- Atalhos: ESPAÇO pausa/continua · R reinicia com a contagem · setas esquerda/direita pulam de cena · T mostra/esconde o tempo atual no canto (escondido por padrão).
- Esconda o cursor durante a reprodução. Anime principalmente transform e opacity para rodar liso.
Estilo e movimento
- Cada fala vira texto grande na tela, entrando palavra por palavra no ritmo da narração (distribua as palavras dentro do tempo de cada cena).
- Destaque 1 ou 2 palavras-chave por frase com a cor de destaque.
- Entradas rápidas que desaceleram no fim (ease-out exponencial, 400 a 700 ms), com um leve desfoque que some ao entrar. Mesmo estilo de movimento no vídeo todo.
- Uma ideia por cena. Além do texto, cada cena tem um elemento visual que mostra o que a fala diz (cards, ícones, interface, números, gráficos, checklist, peças de xadrez), feito em HTML, CSS ou SVG.
- Transição em todas as trocas de cena (zoom com desfoque, flash de luz ou deslize rápido) e uma aproximação lenta e contínua da câmera: nada fica 100% parado.
- Fundo vivo: manchas de luz nas cores da marca se movendo devagar, granulado sutil e vinheta nas bordas.
- Títulos entre 90 e 140 px (só a palavra do CTA pode ser maior); nenhum texto menor que 40 px; no máximo 2 fontes.
- Área segura do Reels: nenhum texto acima de y = 280 px nem abaixo de y = 1250 px, e pelo menos 70 px de margem nas laterais.
- Cena final: a palavra do CTA bem grande com um brilho passando, uma caixa de comentário simulada digitando essa palavra, e 3 segundos parada no fim.
Entrega
- Entregue o código completo e pronto, num único arquivo.
- Depois do código, liste em uma linha por cena o que acontece e em que segundo, para eu revisar.
```
