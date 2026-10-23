# Regras do projeto · O Estrategista (@o_estrategista.com.br)

## Sistema Instagram (obrigatório)
O Instagram é operado pelo sistema em `conteudo/sistema-instagram/00-SISTEMA.md`: 7 módulos em cadeia (Auditoria → Posicionamento → Calendário 30 dias → Hooks → Roteiro de retenção → Funil → Performance semanal). Os prompts originais estão em `conteudo/sistema-instagram/prompts-originais.md`.

- Cada módulo usa a saída do anterior. Sempre aplicado a nós (Bruno, Estrategista de Lançamento), nunca genérico.
- Antes de criar qualquer conteúdo, ler o 00-SISTEMA.md e seguir posicionamento, calendário e hooks aprovados.
- Toda semana (ou quando o Bruno pedir números): rodar o Módulo 7 com dados reais do Buzzfy (ig_account_stats, ig_follower_growth, ig_post_stats) e do PostZen (listCommentAutomationLogs). Entregar PARAR / MANTER / DOBRAR / TESTAR, duplicações e os próximos 7 dias. Registrar a rodada em `conteudo/sistema-instagram/semanas/AAAA-MM-DD.md` e atualizar a projeção.
- Se os dados contradisserem um módulo, reescrever o módulo. Não proteger decisão antiga.
- Separar fato de hipótese. Nunca estimar métrica que falta: escrever "sem dado".

## Aprendizados medidos (atualizar a cada rodada)
- 21/10/2026: reels com o Bruno falando ficaram de 2,4x a 5,8x acima da mediana. Reels de animação com voz sintética ficaram de 0,15x a 0,8x, com 77% a 92% de pulo. Regra: todo reel tem o Bruno em cena nos 3 primeiros segundos.
- 3 posts por dia não aumentaram seguidores. Ritmo: 5 reels + 2 carrosséis por semana + stories diários.
- Uma palavra-chave por mês (TABULEIRO), só em post com alcance de 150 ou mais.

## Edição de vídeo (aprendizados: PDF "42 efeitos" + reels medidos)
Referência completa: `conteudo/edicao/42-efeitos-referencia.txt`. Motor próprio: HTML com render(t) determinístico + Playwright + ffmpeg (mesma lógica da HyperFrames).
- Cada efeito entra na palavra que ele ilustra, nunca antes (tempo pela transcrição palavra a palavra do Whisper).
- No máximo 1 efeito novo a cada 2 segundos. Legenda o vídeo inteiro. O vídeo sem som precisa fazer sentido.
- Nada encosta na borda, fica em cima da boca, no rodapé ou na lateral direita (botões do Instagram).
- Movimento com mola ou curva suave, nunca linear; elementos em sequência com 2 a 4 quadros de diferença.
- Identidade: escolher 4 a 6 efeitos por tipo de vídeo e repetir. Base fixa da marca: Connect Hook (gancho palavra a palavra), Legenda Gigante, CTA de Comentário, letreiro 3D atrás da cabeça, preto e ouro (#141210 / #E8B36A, Cinzel + Playfair itálico).
- Antes do render final: folha com 4 quadros por segundo, nota de 0 a 10 por efeito, corrigir o que ficar abaixo de 8.
- Combinações: bastidor (Storyboard, Grade de vídeos, Punch-in, Flash, Comentário caindo); depoimento/entrevista (Nome e cargo, Legenda Gigante, Marca-texto, Look cinemático, Title Card); oferta (Connect Hook, Contagem, Barras, CTA de Comentário).
- Interface recriada (feed, notificação, busca) nunca usa logo ou marca de outra empresa.

## Regras de texto
Português do Brasil, sem travessão, sem emoji, sem promessa de resultado, sem citar HighClass, Júnior Prazeres ou Felipe Roser. No máximo uma frase "não é X, é Y" por peça.
