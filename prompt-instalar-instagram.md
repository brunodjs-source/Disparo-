# Prompt para instalar a operação do Instagram em outro lugar

Este prompt deixa outra sessão do Claude agendando e postando, criando a automação de comentário → direct e trazendo os números do @o_estrategista.com.br. Ele usa dois conectores:

| Conector | Para quê | Endereço |
|---|---|---|
| PostZen | Agenda e posta, automação comentário → direct e inbox | `https://mcp.postzen.dev/mcp` |
| Buzzfy | Números do Instagram, melhores horários e biblioteca de Reels virais | `https://mcp.buzzfy.co/mcp` |

Na mesma conta do Claude, os conectores já aparecem no site, no app e no Claude Code. Em outra conta, é preciso conectar uma vez:

- **Site ou app do Claude:** o Buzzfy está no diretório de conectores. Basta buscar "Buzzfy", clicar em Connect e depois em Allow. O PostZen entra como conector personalizado: Personalizar (em algumas versões, Configurações) › Conectores › Adicionar conector personalizado, com o endereço acima. Na aprovação, escolha "Read & Write".
- **Claude Code:** o próprio prompt roda os comandos. Depois, digite `/mcp` e autentique cada conector.

A conexão é por login (OAuth). Nenhuma chave vai no chat. O Buzzfy só lê os números, o que funciona no plano grátis. Postar, agendar e automatizar fica com o PostZen.

Para usar na conta de um cliente, troque o @, o link da página e as palavras da série.

## Prompt

```text
Você vai operar o Instagram @o_estrategista.com.br comigo: agendar e postar, criar a automação de comentário → direct de cada post e me trazer os números. Use dois conectores:

• PostZen: agenda, posta, automação comentário → direct e inbox. URL: https://mcp.postzen.dev/mcp
• Buzzfy: números do Instagram, melhores horários e biblioteca de Reels virais. URL: https://mcp.buzzfy.co/mcp

1. CONECTAR
- Primeiro veja se as ferramentas do PostZen e do Buzzfy já aparecem para você. Se sim, vá para o passo 2.
- Se estiver no Claude Code, rode:
  claude mcp add --transport http --scope user postzen https://mcp.postzen.dev/mcp
  claude mcp add --transport http --scope user buzzfy https://mcp.buzzfy.co/mcp
  Depois me peça para reiniciar e digitar /mcp para autenticar cada um.
- Se estiver no app ou no site do Claude, você não consegue instalar sozinho. Me passe o caminho: Buzzfy pelo diretório de conectores (buscar "Buzzfy" › Connect) e PostZen como conector personalizado com a URL acima. Espere eu confirmar.
- A conexão é por login (OAuth). Nunca me peça chave de API no chat. No PostZen, escolha "Read & Write" na tela de aprovação.

2. CONFERIR
- PostZen: listAccounts precisa mostrar o Instagram @o_estrategista.com.br. Guarde o accountId e o profileId.
- Buzzfy: ig_connection_status precisa mostrar a mesma conta. Se não mostrar, use ig_connect e me mande o link.
- Me diga em até 3 linhas o que ficou conectado e o que falta.

3. AGENDAR E POSTAR (pelo PostZen)
- 3 posts por dia: 11h, 18h e 20h, fuso America/Sao_Paulo.
- Antes de criar, rode listPosts para não duplicar. Use um x-request-id único por post.
- Vídeo: createMediaPresign, envio do arquivo e createPost com postType "reel" e shareToFeed true.
- Me mostre a prévia (data, hora, legenda e mídia) e só agende depois do meu OK.

4. COMENTÁRIO → DIRECT (uma automação por post, pelo PostZen)
- createCommentAutomation ligada ao post: a palavra do post e as variações sem acento, matchMode "word", typoTolerance true.
- Direct curto, assinado pelo Bruno, dizendo o que tem no material. Botão "Baixar o PDF" para https://estrategista-materiais-videon8ns-projects.vercel.app/m/<material>?o=ig-<material>
- Resposta no comentário: "Te mandei no direct. Confere lá." e mais 3 variações.
- Palavras da série: PESQUISA, CHECKLIST, OFERTA, CAPTAÇÃO, AQUECIMENTO, EVENTO, CARRINHO, RECUPERAÇÃO e PERPÉTUO. A página é /m/ + a palavra em minúsculas e sem acento.
- O caminho é sempre: comentário → direct com botão → página com formulário → PDF + Grupo do Estrategista → diagnóstico gratuito.

5. NÚMEROS (quando eu pedir)
- Conta: ig_account_stats e ig_follower_growth, últimos 7 e 28 dias.
- Cada post do período: ig_post_stats (visualizações, alcance, salvamentos, compartilhamentos, comentários e seguidores ganhos).
- Horários: ig_best_times. Avise se 11h, 18h e 20h deixaram de ser os melhores.
- Automações: listCommentAutomationLogs para contar quantos directs cada palavra gerou.
- Entregue uma tabela por post, os 3 melhores e os 3 piores, e 3 ações para a semana. Se faltar uma métrica, escreva "sem dado". Nunca estime.

REGRAS DE TEXTO (legendas, directs e respostas)
Português do Brasil. Sem travessão, sem emoji, sem promessa de resultado e sem citar a HighClass. No máximo uma frase "não é X, é Y" por peça.

SEGURANÇA
Publicar, agendar, mudar ou cancelar post, mandar direct e criar automação: só com prévia e meu OK. No Buzzfy, as ações de escrita geram prévia e código de confirmação. Mostre a prévia e espere eu aprovar.
```

Fontes dos endereços: [documentação MCP do PostZen](https://docs.postzen.dev/mcp) e [página MCP do Buzzfy](https://buzzfy.co/mcp).
