# Evidências da cadeira L · leituras de 21/10/2026 (somente leitura, nada alterado)

## PostZen · listCommentAutomations (21/10/2026)
Perfil m572737azhq1p7yg8yv50cxvbd8g5s85. Duas contas no mesmo perfil:
- conta j974hjgcbkx3efd1fzdexszzm98gh4ed: 5 regras de outro negócio (TESTE, ESTOQUE, PROMO, FRETE, LUCRO), 0 disparos. Fora do escopo.
- conta j97772ycndetk3f1wcdbh14p898g4b8w (O Estrategista): 16 regras, todas isActive=true, todas linkTracking=false.

Regras da conta toda (sem postId), valem para qualquer post novo, inclusive o reel do dentista:
| Regra | Palavras | matchMode | typoTolerance | Gatilho | Link |
|---|---|---|---|---|---|
| CASE · série 2 | case, caso | word | false | comment | estrategistadelancamento.com.br/?o=ig-case |
| ESTRATEGISTA · série 2 | estrategista | word | true | comment | estrategistadelancamento.com.br/?o=ig-estrategista |
| ETAPAS · série 2 | etapas, etapa | word | true | comment | .../m/checklist?o=ig-etapas |
| FUNIL · série 2 | funil | word | true | comment | .../m/checklist?o=ig-funil |
| CAIXA · série 2 | caixa | word | true | comment | .../m/recuperacao?o=ig-caixa |
| ETAPAS · resposta de Story | etapas, etapa | word | true | story_reply | .../m/checklist?o=ig-story-etapas |

Regras presas a um post: ETAPAS (Escala 7x7), RECUPERAÇÃO, PERPÉTUO, CARRINHO, EVENTO, PESQUISA, AQUECIMENTO, CAPTAÇÃO, OFERTA, CHECKLIST.
Não existe regra TABULEIRO nem regra DENTISTA.
Soma de stats.totalTriggered nas 16 regras: 1 (CHECKLIST, totalSent 1).
A DM da regra CASE cita a Tzur Capital ("em seis meses o faturamento mensal foi de sete para oito dígitos").
Descrição da ferramenta PostZen: "A comment permits one private reply ever, within 7 days"; logs: "Misses are not logged".

## PostZen · listCommentAutomationLogs
- CHECKLIST (qs7de23c7nzxzw2k4yjshgm5gd8g5dmx): 1 log, 12/10/2026 10:45 UTC, comentário "Checklist", autor bruno26111982, status sent. Que o autor seja o próprio Bruno testando: HIPÓTESE pelo nome.
- CASE (qs79dctypcnz18m9wbeb7cg4en8gh8fm): 0 logs.

## Buzzfy · ig_automations_list
Erro: recurso do plano MAX, conta sem o plano (call_id 955cc31d-c97f-4c8d-bb53-ea43def92608). Teste a seco de comentário: sem dado.

## Buzzfy · ig_posts (reels, 20 mais recentes)
Reel mais recente: 20/10/2026 21:30 UTC ("Você não enriquece o marqueteiro"). Nenhum reel do case Tzur v2 na lista. Reel "Médico com agenda lotada" (30/09/2026, id 17995270031834903) tem CTA "Comenta AGENDA" e não existe regra AGENDA no PostZen.

## Buzzfy · ig_post_stats (21/10/2026)
| Reel | Alcance | Views | Comentários | Assistido | Pulo |
|---|---|---|---|---|---|
| Ele nunca fez um anúncio (04/10) | 307 | 577 | 3 | 18,6 s | 53,4% |
| 90% dos lançamentos (04/10) | 165 | 251 | 2 | 12,6 s | 46,0% |
| Problema de equipe (06/10) | 126 | 204 | 0 | 17,4 s | 50,4% |
| Médico com agenda lotada (30/09) | 63 | 101 | 1 | 9,4 s | 56,3% |
| Você gravou o curso inteiro (11/10) | 168 | 213 | 0 | 4,9 s | 87,4% |
| Você não enriquece o marqueteiro (20/10, provisório) | 8 | 14 | 0 | 5,3 s | 87,5% |
Base Buzzfy: mediana de 17 reels = 53 de alcance, 74 views, 6,2 s, pulo 68,4%.

## Buzzfy · ig_best_times (America/Sao_Paulo, 25 posts)
Seguidores online: pico 18h (425), 19h (420), 12h (405). Posts próprios: melhor hora 12h (4 posts, média 62 de alcance), 18h (6 posts, 48). Melhores dias: domingo (5 posts, 72), quarta (2 posts, 71). Quinta não aparece entre os melhores. Mediana de alcance dos 25: 33.
