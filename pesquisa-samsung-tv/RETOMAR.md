# Retomar a pesquisa da TV Samsung (pausada em 25/10/2026 as 22:07 UTC)

Sessao: https://claude.ai/code/session_01BhQPrBiDaiJf7XpEvToiQa
Modelo da sessao no momento da pausa: claude-fable-5-1 (trocado pelo Bruno com /model).
Retomada agendada: 26/10/2026 as 15:10 de Brasilia (18:10 UTC), tarefa trig_01U8CW22SmihudH1Cvy2Gmhn.

## Estado no momento da pausa
- Workflow `samsung-tv-personalizacao`, runId `wf_4557ac37-f8a`, taskId `wztkkskkx`.
- Fase Varredura: concluida. 11 angulos, 143 achados brutos (achados-brutos.json) e 119 lacunas
  apontadas pelos pesquisadores (lacunas-dos-pesquisadores.json).
- Fase Verificar: 72 dos 143 achados tem veredito (vereditos-parciais.json: 13 confirmados,
  55 parciais, 4 sem fonte). Categorias cobertas: menu-servico, modo-hotel, modo-desenvolvedor,
  tizenbrew, api-rede, anuncios-privacidade. Dois lotes falharam sem resultado (ids de
  modo-desenvolvedor/tizenbrew e api-rede que nao aparecem em vereditos-parciais.json).
  Faltam: visual, root-firmware, brasil, decodificar-modelo, alternativas e os dois lotes falhos.
  Regra pratica: verificar todo achado cujo id nao esta em vereditos-parciais.json.
- Fases Lacunas e Plano: nao iniciadas.
- Dois agentes estavam no meio da execucao quando o workflow foi parado.
- As transcricoes completas dos agentes (32 MB) ficaram so no container e podem se perder.
  O que importa (resultados) esta nos JSON desta pasta.

## Como retomar (ordem)
1. Se o container for novo: `git fetch origin samsung-tv-pesquisa && git checkout samsung-tv-pesquisa`.
2. Clonar de novo o cleanyourtv no scratchpad, porque o CONTEXT do script aponta para
   `/tmp/claude-0/-home-user/ecc3fd7d-108c-5148-9bf5-bf7042299da0/scratchpad/r/cleanyourtv`:
   `git clone --depth 1 https://github.com/Gathin23/cleanyourtv.git` dentro de `scratchpad/r`.
   Se nao der, usar `referencia-cleanyourtv-samsung-tizen.md` desta pasta e ajustar o caminho em `args`.
3. Tentar o resume se o journal ainda existir em
   `/root/.claude/projects/-home-user/ecc3fd7d-108c-5148-9bf5-bf7042299da0/subagents/workflows/wf_4557ac37-f8a/journal.jsonl`:
   `Workflow({scriptPath: ".../workflows/scripts/samsung-tv-personalizacao-wf_4557ac37-f8a.js", resumeFromRunId: "wf_4557ac37-f8a"})`.
   Os 33 agentes concluidos voltam do cache; so os lotes restantes rodam.
4. Se o journal nao existir (container novo): NAO refazer a varredura. Escrever um script novo
   (base: workflow-script.js) que receba via `args` o conteudo de achados-brutos.json,
   vereditos-parciais.json e lacunas-dos-pesquisadores.json, verifique apenas os achados sem
   veredito, rode o critico de lacunas, a rodada extra e o plano.
5. Ao terminar: escrever `pesquisa-samsung-tv/PLANO.md`, fazer commit neste branch, resumir para o
   Bruno em portugues do Brasil (sem travessao, sem emoji, sem promessa de resultado) e pedir o
   codigo do modelo da TV (etiqueta atras ou Configuracoes > Suporte > Sobre esta TV) para
   filtrar o plano para o ano e a versao do Tizen dele.

## Pendencias combinadas com o Bruno
- Ele ainda nao informou o modelo da TV.
- Ele quer: todos os "codigos" Samsung (menu de servico, modo hotel, modo desenvolvedor,
  codigos de tecla, IDs de app, codigo de modelo) e todas as formas de personalizar, com plano.
- Script de descoberta da TV pelo Wi-Fi ja entregue (acha_tv.py nesta pasta, porta 8001).
  Precisa rodar num computador no mesmo Wi-Fi da TV; a sessao na nuvem nao alcanca a rede dele.
