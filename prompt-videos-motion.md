# Prompt para criar vídeos no padrão dos Reels e do anúncio de Campinas

Use no Claude Code (precisa rodar código: Playwright, ffmpeg, Python). Troque o bloco DADOS.

```text
Você vai criar um vídeo vertical em motion graphics no padrão que já validamos. Siga as etapas na ordem e me mostre o resultado de cada uma antes de seguir.

DADOS
- Marca/pessoa: [nome] · profissão: [ex.: nutricionista] · cidade: [ex.: Campinas]
- Público: [quem assiste] · Objetivo: [Reels orgânico | anúncio]
- CTA: [orgânico: "comenta PALAVRA" | anúncio: "toca no botão e agenda"]
- Cores: [fundo, texto, destaque] · Fontes: [título, apoio] · Logo: [arquivo]
- Voz: [gravação de referência da pessoa | voz sintética pt-BR]

1. ROTEIRO (30 a 40 s, no máximo 100 palavras, 6 a 8 frases)
Estrutura que funcionou:
1) Gancho com até 8 palavras, falando com quem assiste e com o que está em jogo (ex.: "Em Campinas, você perde cliente no mesmo lugar.")
2) Dor concreta, uma cena que a pessoa reconhece ("Ele pede o preço, diz que vai pensar e some.")
3) Quebra de crença no formato "Ninguém te conta": três palavras soltas com ponto e uma virada ("Seguidor. Curtida. Indicação. Nenhum deles diz quem vai fechar.")
4) Ponto em comum, nomeando as profissões ou o público
5) Autoridade com número real e uma frase-tese curta ("A venda não morre no preço. Morre no intervalo.")
6) Solução em etapas, numa frase com 3 ou 4 itens
7) Por que precisa de você: divisão de papéis ("Você atende, e eu desenho e comando.")
8) CTA com número concreto, repetindo uma palavra do gancho para criar loop
Regras: português do Brasil; sem travessão, sem emoji e sem promessa de resultado; no máximo uma frase "não é X, é Y"; nada de metáfora de xadrez; respeitar as regras de publicidade do conselho da profissão. Me mostre o roteiro e a nota do gancho antes de seguir.

2. VOZ
- Com gravação da pessoa: gere a fala em pt-BR (Kokoro, voz pm_alex, lang pt-br) e troque o timbre com ChatterboxVC, usando 10 a 15 s da gravação como referência. Não use TTS clonado direto, porque sai com sotaque de Portugal.
- Uma frase por arquivo. Confira cada uma com o Whisper; se alguma palavra sair errada, gere de novo em outra velocidade.
- Listas curtas ("Seguidor. Curtida. Indicação.") são geradas palavra por palavra, com 0,2 s de pausa.
- Se uma palavra ficar ambígua (ex.: "eu" soando "é o"), reescreva a frase em vez de forçar a pronúncia.
- Monte a faixa: corte o silêncio, encurte as pausas acima de 0,32 s, iguale o volume, acelere 8% a 12% sem mudar o tom (atempo) e deixe 0,3 s entre as frases e 1,5 s no final. Tire o tempo de cada palavra com o Whisper no áudio final (timeline.json).

3. ANIMAÇÃO (HTML + SVG, 1080x1920, 30 fps)
- Uma cena por frase, com um rótulo curto em caixa alta no topo (ex.: "O CLIENTE QUE SOME").
- Cada cena desenha a ideia com ícones e objetos simples (cartões, celular com conversa, linha do tempo, etiqueta de preço riscada), animados no tempo exato das palavras.
- Texto na tela desde o primeiro quadro.
- Legenda palavra por palavra, em 3D, com as palavras-chave destacadas na cor de destaque; entre a altura 935 e 1250 px.
- Partículas na troca de cena; logo discreto embaixo; seta para o botão no CTA.
- Todo o conteúdo entre as alturas 285 e 1635 px, para o corte 4:5 funcionar.
- Renderize com Playwright chamando render(t) quadro a quadro e mande para o ffmpeg. Antes, me mostre prints de 6 momentos para conferir a sincronia.

4. TRILHA E FINAL
- Trilha com grave, a −14 LUFS no total, abaixando quando a voz entra (sidechain). A entrada do grave cai na frase de autoridade.
- Gere duas versões: 9:16 (Reels e Stories) e 4:5 (Feed, corte 1080x1350 a partir de y=285).
- Confira: duração até 40 s, Whisper entende o roteiro inteiro com a trilha, e os prints das duas versões estão certos.

5. ENTREGA
Me mande os dois MP4, o roteiro final e a legenda do post (gancho, 3 linhas de valor e o CTA). Não publique nada sem o meu OK.
```
