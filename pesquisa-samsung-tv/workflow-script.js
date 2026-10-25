export const meta = {
  name: 'samsung-tv-personalizacao',
  description: 'Pesquisa exaustiva sobre como personalizar uma TV Samsung Tizen (codigos, modos, apps, rede, anuncios), com verificacao adversarial e plano final',
  phases: [
    { title: 'Varredura', detail: '11 angulos de pesquisa em paralelo' },
    { title: 'Verificar', detail: 'tentar refutar cada achado' },
    { title: 'Lacunas', detail: 'critico de completude e rodada extra' },
    { title: 'Plano', detail: 'sintetizar o plano final' },
  ],
}

const FINDING_PROPS = {
  title: { type: 'string' },
  what_it_enables: { type: 'string' },
  steps: { type: 'string' },
  applies_to: { type: 'string' },
  requirements: { type: 'string' },
  risk: { type: 'string', enum: ['baixo', 'medio', 'alto'] },
  reversible: { type: 'string' },
  sources: { type: 'array', items: { type: 'string' } },
  confidence: { type: 'string', enum: ['alta', 'media', 'baixa'] },
  fact_or_hypothesis: { type: 'string', enum: ['fato', 'hipotese'] },
}
const FINDINGS = {
  type: 'object',
  properties: {
    findings: { type: 'array', items: { type: 'object', properties: FINDING_PROPS, required: ['title', 'what_it_enables', 'steps', 'applies_to', 'requirements', 'risk', 'reversible', 'sources', 'confidence', 'fact_or_hypothesis'] } },
    gaps: { type: 'array', items: { type: 'string' } },
  },
  required: ['findings', 'gaps'],
}
const VERDICTS = {
  type: 'object',
  properties: {
    verdicts: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' },
      verdict: { type: 'string', enum: ['confirmado', 'parcial', 'refutado', 'sem_fonte'] },
      corrections: { type: 'string' },
      applies_to_corrected: { type: 'string' },
      extra_sources: { type: 'array', items: { type: 'string' } },
      notes: { type: 'string' },
    }, required: ['id', 'verdict', 'corrections', 'applies_to_corrected', 'extra_sources', 'notes'] } },
  },
  required: ['verdicts'],
}
const CRITIC = {
  type: 'object',
  properties: {
    gaps: { type: 'array', items: { type: 'object', properties: {
      topic: { type: 'string' }, why: { type: 'string' }, search_hint: { type: 'string' },
    }, required: ['topic', 'why', 'search_hint'] } },
    weak_items: { type: 'array', items: { type: 'string' } },
  },
  required: ['gaps', 'weak_items'],
}

const CONTEXT = `CONTEXTO
Dono de uma TV Samsung (sistema Tizen), modelo ainda desconhecido, comprada provavelmente no Brasil. Ele quer personalizar a TV ao maximo: tela inicial, apps, anuncios, telemetria, visual, controle por rede, e entender todos os "codigos" Samsung (codigos de menu de servico, modo hotel, modo desenvolvedor, codigos de modelo, codigos de tecla do controle, IDs de app). Data de hoje: ${args.date}.

O que ja sabemos (fonte: repositorio cleanyourtv, arquivo ${args.repoDoc}, que voce pode ler com a ferramenta Read; e ${args.showcase}):
- Firmware de varejo nao tem ADB (porta 5555 fechada) nem shell. Nao da para desativar apps da Samsung por "pm disable" como em Android TV.
- Portas abertas: 8001 (API HTTP /api/v2/ e websocket do controle), 8002 (o mesmo em TLS), 9197 (UPnP DMR), 7678 (nservice), 8080 e 9080 (nao identificadas). 26101 (sdb) so abre com Modo Desenvolvedor ligado.
- Com Modo Desenvolvedor e certificado Samsung, da para instalar um app web (.wgt) proprio que lista e abre apps e mostra HDMI, mas o botao Home continua abrindo a Samsung Home.
- "Start Screen Options" (Iniciar com Smart Hub desligado + Executar ultimo app ligado) fez a TV voltar para o app proprio ao sair do standby, em um unico teste.
- Testado em modelos 18_KANTME_UHD (2018), 21_KANTSU2E_UHD_VOICE (2021), 22_NIKEL_UHD (2022), 24_KSUE_UB_T09 (2024, Tizen 9).

REGRAS DE PESQUISA
- Use WebSearch (carregue via ToolSearch se precisar; use mode "extended" quando o resultado padrao vier raso ou o assunto for de nicho) e WebFetch para LER as paginas. Cada achado precisa de pelo menos uma URL que voce leu de verdade. Nao cite URL que nao abriu.
- Priorize: documentacao oficial Samsung (developer.samsung.com, samsung.com/support, samsung.com/br), GitHub, XDA, Reddit, Samsung Community, Home Assistant community, e conteudo em portugues do Brasil quando existir.
- Para cada achado informe: a quais anos, series ou versoes de Tizen se aplica (seja preciso, ex.: "2018 a 2021, Tizen 4 a 6"); o risco (baixo, medio, alto) e se e reversivel e como; o que exige (ferramenta, conta, certificado, cabo, PC).
- Separe fato de hipotese. Fato = voce leu em fonte confiavel ou em 2 relatos independentes. Hipotese = deducao ou relato unico sem confirmacao. Nunca invente passos ou codigos. Se nao encontrar, registre em "gaps".
- Campos curtos e densos: "steps" com no maximo 900 caracteres, os demais com no maximo 300. Entre 6 e 14 achados.
- Escreva em portugues do Brasil, sem travessao e sem emoji.
`

const ANGLES = [
  { key: 'menu-servico', focus: `MENU DE SERVICO (factory menu) em TVs Samsung Tizen: combinacoes de teclas por ano e por tipo de controle (ex.: Mute 1 8 2 Power; Info Menu Mute Power; como fazer com o controle Smart que nao tem teclas numericas, usando o teclado numerico na tela, o app SmartThings ou um controle universal); o que existe la dentro (Option, Control, Advanced, SVC, Debug, Hotel Option, Shop/Retail mode, mudanca de regiao ou pais, Samsung TV Plus, opcoes de painel, Local Dimming, Freesync etc.); quais ajustes as pessoas realmente fazem para personalizar ou limpar a TV; riscos reais de "brick" documentados; como fotografar e anotar valores antes de mudar e como restaurar.` },
  { key: 'modo-hotel', focus: `MODO HOTEL / HOSPITALITY em TVs Samsung de consumidor (ex.: Mute 1 1 9 Enter; ou pelo menu de servico > Hotel Option): o que oferece (Power On Source, Power On Channel, Power On Volume, Max Volume, Welcome Message, Logo de inicializacao personalizado via USB "Logo DL" ou "Logo Display", bloqueio de menus, Smart Hub on/off, Clock, Music mode, Channel Editor, Panel Button Lock); se o logo personalizado funciona em TVs de consumidor e em quais anos; como sair do modo hotel; como ele interage com o Smart Hub e com "Autorun Last App"; riscos.` },
  { key: 'modo-desenvolvedor', focus: `MODO DESENVOLVEDOR TIZEN: ativar (Apps > digitar 12345), Host PC IP, Tizen Studio e Tizen CLI (tizen, sdb), certificados Samsung (autor e distribuidor, DUID da TV), instalar um app web .wgt proprio; limites (sem shell, nao substitui a Home); APIs uteis para um "painel inicial" proprio (tizen.application getAppsInfo e launch, tizen.tvwindow para HDMI, tizen.tvinputdevice para registrar teclas do controle, tizen.systeminfo, webapis.network, webapis.productinfo); como fazer o app abrir sozinho ao ligar (Start Screen Options, Autorun Last App) e o que a documentacao oficial diz; versao de Tizen e de Chromium por ano de TV; se da para instalar sem Tizen Studio (so CLI, ou Docker).` },
  { key: 'tizenbrew', focus: `TIZENBREW e homebrew: o que e o TizenBrew (reisxd), como instalar por ano de TV (2017 a 2026, Tizen 3 a 9), o instalador (TizenBrew Installer, Docker, Tizen Studio), modulos existentes (TizenTube, Jellyfin, Moonlight, Bilibili, outros no npm com tag tizenbrew), se funciona em TVs 2024 e 2025 (Tizen 8 e 9) e problemas conhecidos (certificado expirado, app sumindo, TV apagando o app apos update), TizenTube Legacy, Jellyfin Tizen, Moonlight Tizen, outros apps homebrew conhecidos e como sao instalados.` },
  { key: 'api-rede', focus: `CONTROLE PELA REDE: API /api/v2/ (8001 e 8002), websocket do controle remoto (bibliotecas samsungtvws / samsung-tv-ws-api em Python, samsung-remote, node-samsung-remote), lista COMPLETA de key codes aceitos (KEY_HOME, KEY_MENU, KEY_SOURCE, KEY_AMBIENT, KEY_RETURN, KEY_EXIT, KEY_POWER, KEY_HDMI1, KEY_GUIDE, KEY_CHUP, KEY_VOLUP, KEY_0 a KEY_9, KEY_ENTER, KEY_UP etc.), IDs de apps (Netflix, YouTube, Prime Video, Disney+, Globoplay, Spotify, Plex, navegador) e endpoints REST para listar, abrir e fechar apps; SmartThings cloud API (capabilities switch, mediaInputSource, custom.launchapp, samsungvd.*), integracao do Home Assistant (samsungtv e SmartThings), Wake on LAN; diferencas por ano (TVs 2016 "encrypted" legado, 2018+ token), o aviso "Permitir" na TV e quanto tempo o token dura; o que da para automatizar com isso (ex.: ligar e ir direto para um app ou HDMI).` },
  { key: 'anuncios-privacidade', focus: `ANUNCIOS E TELEMETRIA: caminhos exatos nas configuracoes por versao de Tizen (Termos e Politicas / Privacidade: anuncios baseados em interesse, Servicos de informacao de visualizacao (ACR), reconhecimento de voz, personalizacao), desligar ou remover Samsung TV Plus (remover do Smart Hub, ocultar canal, trocar pais), "Smart Hub ao ligar", banners promocionais na tela inicial, ofertas na barra de apps; listas DNS (Pi-hole, AdGuard Home, NextDNS) com dominios Samsung atualizados 2024 a 2026 e os dominios que quebram login, atualizacao ou hora (time.samsungcloudsolution.net etc.); o que a Samsung diz oficialmente; o que NAO da para tirar (anuncios dentro dos apps).` },
  { key: 'visual', focus: `PERSONALIZACAO VISUAL E DO SMART HUB: Ambient Mode e Art Mode (The Frame), fotos e papeis de parede proprios via SmartThings, protecao de tela, Ambient em modelos que nao sao Frame, reorganizar, ocultar e remover apps do Smart Hub (quais pre-instalados podem ser apagados e em quais anos), remover Samsung TV Plus e "Universal Guide" da barra, mudar nome da TV, atalhos de acessibilidade, remapear botoes do controle (se existe, ex.: botoes Netflix e Prime), Multi View, Game Bar, temas e modos de cor da interface, diferencas de layout por Tizen 6, 7, 8 e 9 (barra inferior vs tela cheia), como voltar ao layout antigo se existir.` },
  { key: 'root-firmware', focus: `ROOT, JAILBREAK E FIRMWARE: historico (SamyGO e quais series cobre), pesquisas publicas de seguranca sobre Tizen (ex.: 2017 "40 vulnerabilidades", CVEs recentes), sdb root em firmwares antigos, downgrade de firmware via USB (e possivel? a Samsung bloqueia? arquivos T-XXX), firmware customizado; o que e viavel HOJE (${args.date}) para TVs 2018 a 2025 e o risco real (brick, garantia, perda de apps); deixe claro o que e so hipotese ou boato. Nao descreva nada ilegal; o alvo e a TV do proprio dono.` },
  { key: 'brasil', focus: `CONTEXTO BRASIL: como ler o codigo de modelo brasileiro (ex.: UN50AU8000GXZD, QN55Q60DAGXZD, UN43CU7700GXZD: significado de UN/QN, polegadas, serie AU/CU/Q60, numero, letra do ano, sufixo G e XZD), firmwares regionais (sufixo XZD, regiao LATAM) e se o menu de servico muda por regiao, Samsung TV Plus Brasil (canais e como tirar), apps brasileiros pre-instalados (Globoplay, etc.), tutoriais em portugues (YouTube, Clube do Hardware, Reddit, Tecnoblog, Canaltech) sobre menu de servico, modo hotel, modo desenvolvedor e TizenBrew, assistencia e garantia Samsung Brasil e o que invalida, comunidade brasileira sobre TizenBrew ou TizenTube.` },
  { key: 'decodificar-modelo', focus: `DECODIFICAR O MODELO E O ANO: tabela da letra do ano no codigo Samsung (K=2016, M=2017, N=2018, R=2019, T=2020, A=2021, B=2022, C=2023, D=2024, F ou outra=2025, e 2026), versao do Tizen por ano (2.4, 3.0, 4.0, 5.0, 5.5, 6.0, 6.5, 7.0, 8.0, 9.0 e 2026), versao do motor web (Chromium ou WebKit) por Tizen, quais recursos de personalizacao existem por ano (Modo Desenvolvedor, TizenBrew, Autorun Last App, Ambient Mode, remover apps, Multi View), como descobrir o ano pela string do /api/v2/ (ex.: 24_KSUE_UB_T09, 21_KANTSU2E_UHD_VOICE, 22_NIKEL_UHD, 18_KANTME_UHD: o que significam KANT, NIKE, KSU, MUSE, etc.) e pelo menu Suporte > Sobre esta TV; como ver a versao do Tizen e do firmware na propria TV.` },
  { key: 'alternativas', focus: `ALTERNATIVAS SEM MEXER NO SISTEMA: navegador da TV (Samsung Internet) com pagina inicial propria hospedada (limites: consegue abrir apps? existe deep link para apps Tizen?), caixa externa (Chromecast com Google TV, Android TV box, Apple TV, Fire TV Stick, Xiaomi) rodando um launcher limpo como o cleanyourtv, com a TV configurada para ligar direto nessa HDMI (Anynet+ / HDMI-CEC, Power On Source no modo hotel, Autorun Last App ou Last Source), ocultando o Smart Hub; precos aproximados no Brasil em 2026; quais caixas aceitam ADB e launcher proprio e quais nao; comparacao esforco x resultado entre as rotas (ajustes de configuracao, modo hotel, app proprio, TizenBrew, caixa externa).` },
]

function sweepPrompt(a) {
  return CONTEXT + `\nSEU ANGULO (pesquise so isso, com profundidade): ${a.focus}\n\nRetorne os achados no formato estruturado. Em "gaps", liste perguntas que ficaram sem resposta confiavel.`
}

function verifyPrompt(batch) {
  return `Voce e um verificador cetico. Abaixo estao achados de pesquisa sobre personalizacao de TVs Samsung Tizen. Para CADA item, tente REFUTAR: procure pelo menos uma fonte independente da citada (documentacao oficial em developer.samsung.com ou samsung.com/support, GitHub, XDA, Reddit, Samsung Community, Home Assistant community) usando WebSearch (ToolSearch para carregar; mode "extended" quando precisar) e WebFetch. Abra as URLs citadas e confira se dizem o que o achado afirma.

Veredito:
- "confirmado": doc oficial ou 2 ou mais fontes independentes concordam, e os passos e anos de aplicacao estao corretos.
- "parcial": funciona, mas so em alguns anos ou modelos, ou os passos tem erro. Escreva a correcao em "corrections" e os anos certos em "applies_to_corrected".
- "refutado": fontes dizem que nao funciona, ou o achado inventou algo. Explique.
- "sem_fonte": nao encontrou nada que confirme nem negue.
Na duvida, prefira "parcial" com a correcao a "confirmado". Nao aceite codigos de teclas ou menus que apareçam em so um site de baixa qualidade. Responda em portugues do Brasil, sem travessao e sem emoji. Campos curtos.

Data de hoje: ${args.date}.

ITENS:
${JSON.stringify(batch, null, 1)}`
}

function criticPrompt(items, gaps0) {
  const compact = items.map(i => `- [${i.id}] (${i.category}) ${i.title} | aplica: ${i.applies_to} | veredito: ${i.verdict}`).join('\n')
  return `Voce e o critico de completude de uma pesquisa sobre como personalizar uma TV Samsung Tizen (modelo desconhecido, Brasil). Abaixo esta a lista de achados ja verificados e as lacunas registradas pelos pesquisadores.

Pergunte-se: o que esta faltando para o dono da TV conseguir, na pratica, (1) identificar o modelo e o ano, (2) tirar anuncios e telemetria, (3) controlar a TV por script, (4) ter uma tela inicial propria ou o mais perto disso, (5) instalar apps de fora, (6) decidir se vale mexer em menu de servico, modo hotel ou root, (7) desfazer tudo. Pense tambem em: codigos ou menus que ninguem pesquisou, versoes recentes (Tizen 8 e 9, TVs 2024 a 2026), diferencas do controle Solar sem teclas numericas, Samsung Brasil, e procedimentos de backup e restauracao.

Liste de 3 a 8 lacunas concretas (topic, why, search_hint em portugues) e os ids dos itens que ficaram fracos (sem_fonte ou parcial) e merecem uma segunda checagem. Portugues do Brasil, sem travessao e sem emoji.

ACHADOS:
${compact}

LACUNAS DOS PESQUISADORES:
${gaps0.map(g => '- ' + g).join('\n')}`
}

function gapPrompt(g) {
  return CONTEXT + `\nSEU ANGULO (lacuna apontada pelo critico): ${g.topic}\nPor que importa: ${g.why}\nDica de busca: ${g.search_hint}\n\nRetorne de 2 a 8 achados no formato estruturado.`
}

function planPrompt(items) {
  return `Voce vai escrever o PLANO FINAL para um dono de TV Samsung Tizen (modelo ainda desconhecido, comprado no Brasil) que quer personalizar a TV ao maximo e pediu uma pesquisa minuciosa sobre todos os codigos Samsung e todas as formas de personalizacao. Use SOMENTE os achados verificados abaixo (JSON). Itens "refutado" entram apenas na secao "O que nao funciona". Itens "sem_fonte" ou "hipotese" so entram marcados como hipotese.

Formato: Markdown, portugues do Brasil, sem travessao (use virgula, ponto ou dois pontos), sem emoji, sem promessa de resultado. Nao use a palavra "garantido". Separe fato de hipotese em cada secao. Toda afirmacao pratica cita a fonte entre parenteses com a URL.

Estrutura obrigatoria:
1. Resumo em 10 linhas: o que da e o que nao da para fazer numa Samsung Tizen.
2. Passo 0: identificar a TV (codigo de modelo brasileiro decodificado, letra do ano, como achar Tizen e firmware na propria TV e pelo /api/v2/, o que a string do modelo diz). Inclua a tabela ano x letra x Tizen x recursos disponiveis.
3. Os "codigos" Samsung, um por um: menu de servico (combinacoes por tipo de controle), modo hotel, modo desenvolvedor (12345), codigos de tecla do controle por rede, IDs de app, codigo de modelo. Para cada um: o que abre, o que da para mudar, riscos, como desfazer.
4. Niveis de personalizacao, do mais seguro ao mais arriscado: A) so configuracoes; B) controle por rede e automacao; C) modo hotel; D) menu de servico; E) app proprio via modo desenvolvedor; F) TizenBrew e homebrew; G) root ou firmware; H) caixa externa com launcher limpo. Para cada nivel: pre-requisitos, passos resumidos, o que se ganha, o que se perde, reversibilidade, anos em que funciona.
5. Roteiro recomendado em ordem (o que fazer primeiro, com backup e anotacao de valores originais), com os comandos e caminhos de menu exatos.
6. Anuncios e telemetria: caminhos de menu e lista DNS, com os dominios que nao se deve bloquear.
7. O que nao funciona ou e boato.
8. Perguntas que ficaram em aberto e como o dono pode responder com a TV dele (o que medir, o que fotografar).
9. Fontes (lista de URLs unicas).

Seja completo e concreto: quem le deve conseguir executar sem outra pesquisa. Tamanho esperado: entre 1500 e 3000 palavras. Retorne APENAS o Markdown.

Data de hoje: ${args.date}.

ACHADOS VERIFICADOS:
${JSON.stringify(items, null, 1)}`
}

async function verifyAll(items, phaseName) {
  const batches = []
  for (let i = 0; i < items.length; i += 4) batches.push(items.slice(i, i + 4))
  const results = await pipeline(batches, (b, _orig, idx) =>
    agent(verifyPrompt(b), { label: `verificar:${b[0].category}:${idx}`, phase: phaseName, schema: VERDICTS, effort: 'high' }))
  const byId = new Map()
  results.filter(Boolean).forEach(r => r.verdicts.forEach(v => byId.set(v.id, v)))
  return items.map(it => {
    const v = byId.get(it.id)
    return Object.assign({}, it, {
      verdict: v ? v.verdict : 'sem_verificacao',
      corrections: v ? v.corrections : '',
      applies_to_corrected: v ? v.applies_to_corrected : '',
      extra_sources: v ? v.extra_sources : [],
      verifier_notes: v ? v.notes : '',
    })
  })
}

phase('Varredura')
const sweeps = await parallel(ANGLES.map(a => () =>
  agent(sweepPrompt(a), { label: `varredura:${a.key}`, phase: 'Varredura', schema: FINDINGS })
    .then(r => (r ? { key: a.key, r } : null))))
const raw = []
const gaps0 = []
sweeps.filter(Boolean).forEach(s => {
  s.r.findings.forEach((f, i) => raw.push(Object.assign({ id: `${s.key}-${i + 1}`, category: s.key }, f)))
  gaps0.push(...(s.r.gaps || []))
})
const failed = ANGLES.length - sweeps.filter(Boolean).length
if (failed) log(`${failed} angulo(s) de varredura falharam e ficaram de fora`)
log(`${raw.length} achados brutos em ${sweeps.filter(Boolean).length} angulos`)

phase('Verificar')
const verified = await verifyAll(raw, 'Verificar')
const tally = {}
verified.forEach(v => { tally[v.verdict] = (tally[v.verdict] || 0) + 1 })
log(`vereditos: ${JSON.stringify(tally)}`)

phase('Lacunas')
const critic = await agent(criticPrompt(verified, gaps0), { label: 'critico', phase: 'Lacunas', schema: CRITIC, effort: 'high' })
const gapTopics = critic ? critic.gaps.slice(0, 6) : []
if (critic && critic.gaps.length > 6) log(`critico apontou ${critic.gaps.length} lacunas; pesquisando as 6 primeiras`)
const extraRaw = []
const extraSweeps = await pipeline(gapTopics, (g, _o, i) =>
  agent(gapPrompt(g), { label: `lacuna:${g.topic.slice(0, 40)}`, phase: 'Lacunas', schema: FINDINGS })
    .then(r => (r ? { i, r } : null)))
extraSweeps.filter(Boolean).forEach(s => {
  s.r.findings.forEach((f, j) => extraRaw.push(Object.assign({ id: `lacuna${s.i + 1}-${j + 1}`, category: 'lacuna' }, f)))
})
log(`${extraRaw.length} achados extras das lacunas`)
const verifiedExtra = extraRaw.length ? await verifyAll(extraRaw, 'Lacunas') : []

// segunda checagem dos itens fracos apontados pelo critico
const weakIds = new Set(critic ? critic.weak_items : [])
const weak = verified.filter(v => weakIds.has(v.id) && (v.verdict === 'sem_fonte' || v.verdict === 'parcial'))
log(`${weak.length} itens fracos recebem segunda checagem`)
const rechecked = weak.length ? await verifyAll(weak, 'Lacunas') : []
const recheckMap = new Map(rechecked.map(r => [r.id, r]))
const finalMain = verified.map(v => {
  const r = recheckMap.get(v.id)
  if (!r) return v
  // mantem o melhor veredito entre as duas checagens
  const rank = { confirmado: 3, parcial: 2, sem_fonte: 1, refutado: 0, sem_verificacao: -1 }
  return rank[r.verdict] > rank[v.verdict] ? Object.assign({}, r, { second_check: true }) : Object.assign({}, v, { second_check_verdict: r.verdict, second_check_notes: r.verifier_notes })
})

phase('Plano')
const all = finalMain.concat(verifiedExtra)
const plan = await agent(planPrompt(all), { label: 'plano-final', phase: 'Plano', effort: 'xhigh' })

const stats = {}
all.forEach(v => { stats[v.verdict] = (stats[v.verdict] || 0) + 1 })
return { plan, stats, total: all.length, gaps: critic ? critic.gaps : [], items: all }