# Plano completo para personalizar uma TV Samsung (Tizen)

Pesquisa feita em 25 e 26 de outubro de 2026. Base: 143 achados mais 44 achados de lacunas, cada um checado por um verificador que tentou refutar o que foi afirmado. Toda afirmacao pratica traz a fonte entre parenteses. Fato quer dizer documento oficial ou duas ou mais fontes independentes. Hipotese quer dizer deducao ou relato unico. Quando falta base, esta escrito "sem dado".

Aviso importante de leitura: a maior parte das combinacoes de tecla, codigos e caminhos de menu abaixo foi confirmada em alguns modelos e anos, nunca em todos. O modelo da sua TV ainda nao foi informado. O Passo 0 serve para voce descobrir o ano e a versao do Tizen e so entao escolher o ramo que se aplica. Nada disto foi testado na sua TV.

## 1. Resumo em dez linhas

1. TV Samsung roda Tizen, nao Android, entao os scripts de ADB e os launchers de Android TV nao servem (referencia-cleanyourtv-samsung-tizen.md).
2. Firmware de varejo nao tem shell nem root pela porta de depuracao: da para instalar app proprio assinado, nao apagar apps da Samsung pela conexao de desenvolvedor em TVs de 2021 em diante (github.com/helalaou/AeroTizen).
3. O botao Home fisico quase sempre volta para a Samsung Home; um app proprio pode reaparecer em 1 a 2 segundos, mas nao assume o Home de verdade sem rotas de risco (AeroTizen; cleanyourtv issue 441).
4. O que da de forma segura e grande: desligar anuncios, ACR e telemetria pelo menu, fazer a TV ligar na HDMI ou no ultimo app, controlar tudo por rede e instalar apps de fora (TizenBrew, Jellyfin, Moonlight).
5. YouTube sem anuncio na propria TV existe pelo TizenTube (github.com/reisxd/TizenTube).
6. Menu de servico e modo hotel existem e abrem ate pela rede em modelos recentes, mas sao a rota de maior risco de travar a TV (github.com/Maassoft/ColorControl issues 498 e 531).
7. Root existe so como pesquisa de seguranca, volatil, por modelo exato, e nao e recomendado (github.com/chris-ritsen/samsung-tv-root).
8. Nao existe firmware alternativo para Tizen nem downgrade de firmware por USB em TV de consumo (en.wikipedia.org/wiki/SamyGO; github.com/synacktiv/samsung-q60t-exploit).
9. A rota que realmente entrega uma tela inicial limpa e propria e uma caixa externa (Chromecast, Google TV, Shield, Xiaomi) com Anynet+ ligando a TV na HDMI certa (github.com/Gathin23/cleanyourtv).
10. Tudo que for seguro e reversivel; antes de mexer, fotografe cada tela e anote os valores originais, porque nao existe backup completo restauravel da TV (referencia-cleanyourtv-samsung-tizen.md).

## 2. Passo 0: identificar a TV

Tudo depende do ano e da versao do Tizen. Descubra assim:

1. Codigo do modelo: etiqueta atras da TV, na caixa, ou em Configuracoes, Suporte, Sobre esta TV (github.com/jss8649/quiet-tizen). Exemplo brasileiro: UN50AU8000GXZD.
2. Pela rede, com a TV ligada no mesmo Wi-Fi, um GET em http://IP_DA_TV:8001/api/v2/ devolve modelName (codigo de varejo), model (codinome interno, ex. 21_KANTSU2E_UHD_VOICE) e countryCode. O campo firmwareVersion vem "Unknown" em todos os anos, entao a build real so aparece na TV (github.com/carlosbarreto55/tvhomelab; referencia-cleanyourtv-samsung-tizen.md). O script acha_tv.py nesta pasta faz essa leitura. Esse JSON expoe DUID, MAC e nome da rede: nao publique esses campos.
3. A versao do Tizen nao aparece na tela; deduza pelo ano (tabela abaixo) ou leia por sdb depois de ligar o Modo Desenvolvedor.

Como ler o codigo brasileiro (fato nas letras de ano, hipotese na semantica letra a letra, porque samsung.com/br nao abriu na pesquisa): UN = LED para as Americas, QN = QLED e Neo QLED; dois digitos = polegadas; a serie carrega a letra do ano; G antes do XZD = sintonizador ISDB-T do Brasil; ZD = Brasil. Exemplos reais lidos: UN49MU6100GXZD (2017), UN82TU8000GXZD (2020), UN50AU8000GXZD (2021), UN50BU8000GXZD (2022), QN65QN90CAGXZD (2023), QN65QN85DAGXZD (2024), UN50M75HAGXZD (2026, Tizen 10) (github.com/chris-ritsen/samsung-tv-root issue 7; github.com/sandstream/Beggad-tv).

Tabela ano, letra, Tizen e o que da para fazer (letras e Tizen confirmados por varias fontes; recursos conforme os achados deste plano):

| Ano | Letra | Tizen de fabrica | Modo Dev e app proprio | TizenBrew | Remover app de loja por sdb | Observacao |
|---|---|---|---|---|---|---|
| 2016 | K | 2.4 | so protocolo antigo | nao (precisa 3.0) | relato unico | 8001 sem token |
| 2017 | M | 3.0 | sim, cert. Tizen comum | sim | sem teste | |
| 2018 | N | 4.0 | sim, cert. Tizen comum | sim | sim (ex. NU7400) | |
| 2019 | R | 5.0 | sim, cert. Tizen comum | sim | sem teste | |
| 2020 | T | 5.5 | sim, cert. Tizen comum | sim | recusado (Q60T) | |
| 2021 | A | 6.0 | sim, cert. Tizen comum | sim | nao | |
| 2022 | B | 6.5 | sim, cert. Tizen comum | sim | nao | |
| 2023 | C | 7.0 | exige conta Samsung + DUID | sim | nao | |
| 2024 | D | 8.0 (9 por update) | exige conta Samsung + DUID | parcial, instavel | nao | |
| 2025 | F | 9.0 | exige conta Samsung + DUID | sem dado | nao | E foi pulado |
| 2026 | H (provavel G no catalogo) | 10.0 | exige conta Samsung + DUID | 1 relato | nao | letra do ano sem confirmacao |

Fontes da tabela: github.com/Yskra/yskra compatibility.md; github.com/lucaskfp/tizen-sim; github.com/matomo-org/device-detector; github.com/reisxd/TizenBrew; github.com/helalaou/AeroTizen; github.com/ardazeytin/samsung-tizen-tv-debloat. A versao do Tizen segue o firmware, nao so o ano: TVs 2023 e 2024 atualizadas ja reportam Tizen 9 (referencia-cleanyourtv-samsung-tizen.md).

## 3. Os "codigos" Samsung, um por um

### 3.1 Modo Desenvolvedor (codigo 12345)

O que abre: a porta sdb 26101, que deixa instalar app proprio assinado (.wgt), TizenBrew, Jellyfin. Nao da shell nem root (capability mostra intershell_support e sdbd_rootperm desativados) (referencia-cleanyourtv-samsung-tizen.md; github.com/dragoshont/vemm).

Como ligar: abra o painel Apps do Smart Hub, digite 1 2 3 4 5 no controle (ou pelo botao 123 do Smart Remote, ou pelo teclado do app SmartThings), ligue Developer mode, ponha em Host PC IP o IP do seu PC e reinicie. Em TVs One UI de 2024 e 2025 o atalho passou para Apps, App Settings, 12345 (github.com/jellyfin/jellyfin-tizen issue 299). Em varios modelos a porta 26101 so abre depois de tirar a TV da tomada por alguns segundos, nao com reinicio pelo controle (github.com/reisxd/TizenBrew; FAQ Apps2Samsung).

Certificado: de 2017 a 2022 (Tizen 3.0 a 6.5) o certificado Tizen comum costuma bastar; de 2023 em diante (Tizen 7+) e preciso conta Samsung e um certificado com o DUID da TV, e as ferramentas pedem login (github.com/reisxd/TizenBrew docs; github.com/simbasjungles/free-my-tv).

Riscos e desfazer: baixo. Desligar o Modo Desenvolvedor pelo mesmo dialogo 12345 fecha a porta 26101. A Samsung nao documenta efeito em garantia.

### 3.2 Codigos de tecla do controle pela rede (API local)

O que abre: controle total por script, sem tocar na TV. A TV expoe, com a TV ligada e na mesma sub-rede:
- REST em http://IP:8001/api/v2/applications/{id}: GET le o status do app, POST abre, DELETE fecha, PUT instala da loja (github.com/xchwarze/samsung-tv-ws-api rest.py).
- Websocket em wss://IP:8002/... para enviar teclas KEY_*. Em TVs que anunciam TokenAuthSupport true (na pratica 2018 em diante e muitos 2016 e 2017 atualizados), use a 8002 com token; a 8001 sem token so nas mais antigas (github.com/home-assistant/core bridge.py).

Lista util de teclas (nenhuma e oficial, variam por modelo): KEY_POWER, KEY_HOME, KEY_MENU, KEY_SOURCE, KEY_HDMI, KEY_TV, KEY_AMBIENT, KEY_RETURN, KEY_EXIT, KEY_UP/DOWN/LEFT/RIGHT, KEY_ENTER, KEY_VOLUP/VOLDOWN/MUTE, KEY_CHUP/CHDOWN, KEY_0 a KEY_9, KEY_PLAY/PAUSE (github.com/xchwarze/samsung-tv-ws-api COMMANDS.md). KEY_HDMI1 a KEY_HDMI4 aparecem em algumas bibliotecas mas sao ignoradas em varios modelos; para escolher uma HDMI especifica use SmartThings (github.com/ollo69/ha-samsungtv-smart). KEY_FACTORY abre o menu de servico e e perigoso (ver 3.4).

Pareamento: na primeira conexao a TV mostra "Permitir"; aceite e o token fica salvo. Para a TV parar de perguntar: Configuracoes, Geral, Gerenciador de Dispositivos Externos, Gerenciador de Conexao de Dispositivos, Notificacao de acesso, "Apenas a primeira vez"; a Lista de dispositivos nessa tela revoga clientes (github.com/dahuby/iobroker.samsung_tizen; doc Home Assistant samsungtv).

Ferramentas prontas: Python samsung-tv-ws-api (xchwarze, com CLI e Art Mode), Node samsung-tv-control (Toxblh), Home Assistant integracao nativa samsungtv (descoberta automatica) ou a HACS ha-samsungtv-smart (ollo69, mais completa, com cadeias de tecla e SmartThings).

Risco: baixo; nada e gravado na TV alem do cliente autorizado.

### 3.3 IDs de aplicativo

Para abrir um app por rede voce precisa do ID. IDs numericos lidos (quando ha dois, TVs 2020+ tendem ao da direita): Netflix 11101200001 ou 3201907018807; YouTube 111299001912; Prime Video 3201512006785 ou 3201910019365; Disney+ 3201901017640, 3202009021709 ou 3202204027038; Spotify 3201606009684; Plex 3201512006963; navegador org.tizen.browser, 3201907018784 ou 3202010022079. Brasil: Globoplay 3201908019022; Telecine 3201604009182; DIRECTV GO 3201907018786 (github.com/xchwarze/samsung-tv-ws-api APPLICATIONS.md; github.com/tavicu/homebridge-samsung-tizen issue 26). Os IDs do Brasil nao tem teste publicado. Confirme sempre o ID da sua TV com GET /api/v2/applications/{id} antes de automatizar. Em TVs de 2020 em diante a listagem automatica de apps pela rede parou de responder; para ver os IDs reais use sdb shell 0 applist com Modo Desenvolvedor (github.com/xchwarze/samsung-tv-ws-api issue 23).

### 3.4 Menu de servico (factory menu)

O que abre: ajustes de engenharia (painel, calibracao, regiao, opcoes de jogo). E a rota de maior risco de travar a TV.

Como entrar:
- Por controle IR com numeros, a partir do standby: desligue a TV, espere o LED ficar fixo, e digite em ate 3 segundos Info, Menu, Mute, Power, ou Mute, 1, 8, 2, Power. Confirmado em TVs antigas (2010 a 2015); em Tizen de varejo 2016 a 2024 nao ha relato de sucesso, so um teste negativo em um modelo de hotel (github.com/Apps2Samsung tizen-community-packages issue 34). O Smart Remote sem numeros nao serve para isso.
- Pela rede, com a TV ligada: enviar KEY_INFO e depois KEY_FACTORY. Confirmado em OLED e monitores de 2022 a 2025 (github.com/oBusk/samsung-service-menu; github.com/Maassoft/ColorControl). O app ColorControl (Windows) faz isso com um clique.
- A secao Advanced pede um codigo com o item realcado: 0098 em TVs, 0038 em monitores (confirmado em S90C, S95C, S95D, S89C de 2023 e 2024; github.com/Maassoft/ColorControl issue 540). Depois de atualizacao, a posicao do item Advanced muda, mas o codigo 0098 continua.

Risco alto e documentado: sair pelo botao "Exit" do ColorControl (que manda KEY_FACTORY duas vezes) jogou S90C, S95B e S95F num ciclo de telas coloridas (modo aging), recuperado so com varios ciclos de energia ou reabrindo o menu pela rede na janela de segundos entre os ciclos (github.com/Maassoft/ColorControl issues 498 e 531). Regra: saia sempre pelo Power do controle, nunca mandando KEY_FACTORY de novo. Nunca mexa em Local Set (regiao), Type, Front Color, calibracao ou painel: grava em memoria protegida e pode nao ter volta (github.com/Tianyulife/samsung-m8-cn-to-us). Fotografe cada tela antes e deixe um PC ja pareado pronto para reabrir o menu se travar.

### 3.5 Modo hotel (Hotel Option)

O que abre: Hospitality Mode, fonte, canal e volume ao ligar, volume maximo, mensagem de boas-vindas, logo de abertura por USB, bloqueio de menus, clonagem de ajustes.

Como entrar: com a TV ligada, em qualquer fonte, Mute, 1, 1, 9, Enter em 2 a 3 segundos; ou pela rede enviando KEY_MUTE, KEY_1, KEY_1, KEY_9, KEY_ENTER. Confirmado por documento oficial Samsung de hospitalidade (manual HG470/570, 2012) e por teste real numa UE55RU7020 de 2019 pela rede (github.com/Apps2Samsung issue 635; github.com/capital-lan/LN32D467). Em TVs de hotel (prefixo HG) a sequencia e Mute, cima, baixo, Enter. Nao ha relato verificado de sucesso em TV de consumo Tizen de 2022 a 2025.

Para que serve na pratica: ligar a TV direto numa HDMI ou canal (Power On Source), fixar volume, por um logo proprio de abertura por USB (arquivo samsung.bmp ou samsung.avi; confirmado so em chassis antigos). O logo proprio nunca foi confirmado em TV de consumo Tizen recente (github.com/capital-lan/LN32D467).

Risco medio a alto: ligar Hospitality Mode em Interactive, ou Menu Display OFF, pode esconder o Smart Hub e trancar voce fora do proprio menu hotel; Security com Factory Lock pode exigir senha que voce talvez nao tenha anotado (github.com/Apps2Samsung issue 639; tizen-community-packages issue 34). Reverter: Hospitality Mode Off e desligar e ligar a TV. Anote tudo antes.

### 3.6 Codigo de modelo

Nao e um menu, e a etiqueta. Serve para tudo no Passo 0: identifica ano, serie, sintonizador e regiao, e e o que voce usa para achar firmware, tutoriais e compatibilidade de apps (github.com/chris-ritsen/samsung-tv-root issue 7).

## 4. Niveis de personalizacao, do mais seguro ao mais arriscado

### Nivel A: so configuracoes (risco baixo, reversivel, 2016 a 2026)
Anuncios, ACR, voz, ligar na HDMI ou no ultimo app, limpar a barra de apps, Ambient ou Art Mode com fotos proprias. Nao precisa de PC nem conta de desenvolvedor. Detalhes nas secoes 5 e 6.

### Nivel B: controle por rede e automacao (risco baixo, 2016+)
Home Assistant, samsung-tv-ws-api ou um painel no celular ligam a TV (Wake on LAN por cabo, ou SmartThings no Wi-Fi), trocam para HDMI e abrem apps por ID. Faz o papel de tela inicial sem instalar nada na TV. Limite: nao muda o botao Home. Aviso: a API de nuvem do SmartThings passou a cobrar cerca de 4,99 dolares por mes no plano pessoal a partir de outubro de 2026 (doc Home Assistant smartthings); o controle local pela 8002 continua gratis.

### Nivel C: modo hotel (risco medio a alto, ganho pequeno em TV de consumo)
Power On Source e logo de abertura. Em TV de consumo recente o suporte e incerto. So vale depois de esgotar A e B. Ver 3.5.

### Nivel D: menu de servico (risco alto, so se precisar de ajuste de painel ou jogo)
Ver 3.4. Para a maioria das personalizacoes nao e necessario e nao compensa o risco.

### Nivel E: app proprio via Modo Desenvolvedor (risco baixo, 2017+)
Instalar um .wgt proprio que lista e abre apps, mostra HDMI dentro de si (tizen.tvwindow) e volta do standby com Autorun Last App. Nao assume o Home. Projetos: AeroTizen (sem root, troca a tela inicial e volta em 1 a 2 s ao apertar Home, testado de 2022 a 2024), custom-tv, arn0-tv (github.com/helalaou/AeroTizen; github.com/NelsonEU/arn0-tv). Exige PC, conta Samsung (2023+) e certificado por DUID.

### Nivel F: TizenBrew e homebrew (risco medio, 2017+)
Carregador de apps e mods. Instala pelo TizenBrew Installer Desktop (PC) ou pelo Apps2Samsung, que resolve o certificado por DUID. Com ele voce poe TizenTube (YouTube sem anuncio com SponsorBlock), Jellyfin, Moonlight (jogos do PC por streaming), players IPTV e outros (github.com/reisxd/TizenBrew; github.com/Apps2Samsung/Apps2Samsung). Em TVs 2024 e 2025 (Tizen 8 e 9) e parcial e instavel: ha relatos de erro de certificado e de servico que nao sobe, contornados reassinando com certificado proprio ou usando o Apps2Samsung (github.com/reisxd/TizenBrew issues 131, 234, 245). Reverter: desinstalar o app e desligar o Modo Desenvolvedor.

Jellyfin tem app oficial na loja Samsung desde fevereiro de 2026 para modelos 2021+ (Tizen 6+), com cobertura regional parcial; procure na loja antes de fazer sideload (jellyfin.org; github.com/Georift/install-jellyfin-tizen).

### Nivel G: root ou firmware (nao recomendado, so pesquisa de seguranca)
Nao existe firmware alternativo para Tizen, nem downgrade de firmware por USB em TV de consumo (en.wikipedia.org/wiki/SamyGO; github.com/synacktiv/samsung-q60t-exploit). Root existe apenas como pesquisa de seguranca publicada, especifico por build exata, volatil (some ao reiniciar), e depende de falhas que a Samsung corrige em atualizacoes; pesquisadores profissionais ja o fizeram (Synacktiv, GreHack 2021), o que mostra que e real e nao boato (github.com/chris-ritsen/samsung-tv-root). Nao traz passo a passo aqui porque o risco (instabilidade, boot loop relatado, possivel perda de garantia, sem backup restauravel) nao compensa para personalizar a TV, e tudo que o root faria de util (tirar app de sistema, trocar o Home) tem alternativa mais segura nos niveis A a F ou no nivel H. Se um dia quiser seguir essa linha, pesquise pelo codigo exato do seu modelo e aceite que pode perder a TV.

### Nivel H: caixa externa com launcher limpo (risco baixo, independe do ano da TV)
Esta e a unica rota que entrega, de verdade, uma tela inicial propria e limpa. Uma caixa Google TV ou Android TV (Chromecast com Google TV, Google TV Streamer, Xiaomi Mi Box S, NVIDIA Shield) roda o launcher limpo do cleanyourtv por ADB, e com Anynet+ (HDMI-CEC) ligado ela acende a TV e puxa a entrada para si ao ligar (github.com/Gathin23/cleanyourtv). A TV vira um monitor. Detalhes e ressalvas na secao 5, passo 6.

## 5. Roteiro recomendado, em ordem

Antes de tudo: fotografe a tela inicial, as Opcoes da Tela Inicial e o menu de privacidade; anote o modelo, a string do /api/v2/, o Host PC IP se for usar, e os logins dos apps. Nao existe backup restauravel da TV (ext: tabela acao x reversao).

1. Identifique a TV (Passo 0) e anote ano e Tizen.
2. Desligue anuncios, ACR e voz (secao 6). Reversivel, sem risco.
3. Faca a TV ligar na HDMI ou no ultimo app: Opcoes da Tela Inicial, "Iniciar com Smart Hub" desligado; "Executar ultimo app" ligado para reabrir o app, ou desligado para cair na ultima entrada. Caminho por ano: 2018 a 2021 em Geral, Recursos Smart; 2022 a 2024 em Geral e Privacidade, Opcoes de Tela Inicial; Tizen 9 e 2025 em Recursos Avancados, Opcoes da Tela Inicial (referencia-cleanyourtv-samsung-tizen.md; samsung.com/br, nao aberto na pesquisa; github.com/helalaou/AeroTizen). Em um teste no DU7000 isso fez a TV voltar ao app ao sair do standby, mas o reinicio longo voltou ao HDMI e o botao Home seguiu abrindo a Samsung Home.
4. Limpe a barra: remova apps da tela inicial, exclua apps que voce instalou, desative o Samsung TV Plus (realce o icone, seta para baixo, Desativar) (github.com/helalaou/AeroTizen; e-manual 2025). Apps de sistema nao saem.
5. Decida se quer mais:
   - So YouTube sem anuncio: Nivel F so com TizenTube.
   - Painel proprio dentro da TV: Nivel E (AeroTizen).
   - Controle por celular ou automacao: Nivel B.
   - Tela inicial limpa de verdade: Nivel H (caixa externa).
6. Se for de caixa externa (Nivel H): ligue a caixa numa HDMI, ligue Anynet+ (HDMI-CEC) na TV em Geral, Gerenciador de Dispositivos Externos; ligue o CEC na caixa, incluindo acender a TV; some o passo 3 para quando a TV for ligada pelo controle Samsung. No Chromecast e no Google TV Streamer, trocar o Home por completo desliga o assistente de configuracao e isso derruba as credenciais do Cast: use a lista debloat-keep-cast.txt (so no Chromecast 4K) ou o Cast Fix, ou aceite que Shield e Xiaomi Mi Box S sao mais simples para isso (github.com/Gathin23/cleanyourtv). Os botoes de atalho (Netflix, YouTube) do controle da caixa param e pedem remapeamento.
7. Antes de levar a TV para assistencia, ou se quiser voltar atras: desligue o Modo Desenvolvedor pelo dialogo 12345, desinstale apps proprios, e volte as Opcoes da Tela Inicial aos valores fotografados. Reset de fabrica (Configuracoes, Geral e Privacidade, Redefinir, PIN 0000) apaga contas, apps, canais e ajustes, mas mantem firmware e rede, e nao desfaz modo hotel nem troca o DUID de forma previsivel (ext: reset de fabrica; ext: Redefinir Smart Hub).

## 6. Anuncios e telemetria

No menu (fato, com caminho por ano):
- Anuncios por interesse e ACR: desmarque "Servicos de Informacoes de Visualizacao" (ACR) e "Publicidade com base em interesses". 2016 a 2019 em Suporte, Termos e Politica; 2022 a 2024 em Geral e Privacidade, Termos e Privacidade, Escolhas de Privacidade; 2025 pelo app Privacy Choices ou pela busca do menu (policy.samsungrs.com; github.com/helalaou/AeroTizen; consumerreports.org). A propria Samsung avisa que o opt-out so deixa o anuncio generico, nao o remove (samsung.com/br/info/privacy/smarttv; developer.samsung.com TIFA).
- Redefinir PSID na mesma tela de Termos zera o perfil de anuncio; a Samsung diz que redefinir o PSID sozinho nao para os anuncios por interesse, faca os dois (policy.samsungrs.com).
- Voz e Bixby: desmarque "Servicos de Reconhecimento de Voz" e desligue a ativacao por voz em Geral e Privacidade, Voz (em 2025, Recursos Avancados, Voz) (consumerreports.org; samsung.com/au/info/ads-privacy).
- Banner da tela inicial: nao ha chave oficial para o bloco promocional; desligar anuncios so o deixa generico (cybershack.com.au; github.com/helalaou/AeroTizen).

Por DNS (Pi-hole, AdGuard Home, NextDNS), corta na rede o que o menu nao tira (ACR, telemetria, servidores de anuncio):
- Use uma lista mantida: HaGeZi native.samsung (github.com/hagezi/dns-blocklists) ou Okazakee tv-dns-blocklist (github.com/Okazakee/tv-dns-blocklist). Dominios de anuncio e ACR tipicos: samsungads.com, samsungadhub.com, samsungtvads.com, samsungacr.com, acr0.samsungcloudsolution.com, acr-br-prd.samsungcloud.tv (este e o endpoint brasileiro de ACR).
- Nunca bloqueie, para nao quebrar a TV: time.samsungcloudsolution.com e .net (relogio; sem eles os apps se acham offline), cdn.samsungcloudsolution.com (derruba Wi-Fi e YouTube), auth.samsungosp.com (login), os servidores de atualizacao (otnprd8 a 11.samsungcloudsolution.net, samsungotn.net), a loja (osb-apps-v2.samsungqbe.com) e o Smart Hub (as zonas inteiras samsungqbe.com e samsungcloudsolution). Em resumo: bloqueie os hosts de anuncio e ACR nomeados, nunca as zonas inteiras (github.com/Perflyst/PiHoleBlocklist issues 142, 150 e 60).
- A TV aceita um unico servidor DNS (Conexao, Rede, Status da Rede, Config. IP, DNS manual); se o filtro cair, fica sem internet. Alguns modelos ignoram o DNS do DHCP do roteador, entao fixe o DNS na propria TV; se mesmo assim escapar, so um redirecionamento da porta 53 no roteador resolve (hipotese, github.com/Okazakee/tv-dns-blocklist).

O que nao sai de jeito nenhum: anuncios dentro dos apps (YouTube, Tubi, Plex) e comerciais do Samsung TV Plus chegam pelo mesmo caminho do video; bloquear quebra a reproducao. A unica saida ali e assinatura sem anuncio ou outro aparelho (github.com/hagezi/dns-blocklists issue 11088; news.samsung.com/br).

## 7. O que nao funciona ou e boato

- Scripts de ADB e launchers de Android TV na Samsung: nao, Tizen nao e Android (referencia-cleanyourtv-samsung-tizen.md).
- Apagar apps da Samsung pela conexao de desenvolvedor em TVs 2021 em diante: nao; o sdb recusa apps de sistema e de loja no Tizen 6+ (github.com/helalaou/AeroTizen; github.com/ardazeytin/samsung-tizen-tv-debloat). Em TVs 2018 e anteriores (Tizen 4 e menos) alguns apps de loja saem por sdb.
- Trocar o botao Home fisico de forma oficial e estavel: nao; so por rotas de risco especificas por modelo (cleanyourtv issue 441; AeroTizen).
- Firmware customizado para Tizen e downgrade por USB em TV de consumo: nao existem de forma publica e estavel (en.wikipedia.org/wiki/SamyGO; github.com/synacktiv/samsung-q60t-exploit).
- SamyGO: so cobre TVs Samsung pre-Tizen (ate cerca de 2014), nao as Tizen (en.wikipedia.org/wiki/SamyGO).
- Remapear os botoes Netflix e Prime do controle: nao ha opcao oficial (us.community.samsung.com).
- PINs "universais" de menu hotel com taxa de sucesso: aparecem so em sites de baixa qualidade; nao confie (github.com/Apps2Samsung SamsungSystemApps.cs).

## 8. Perguntas em aberto e como voce responde na sua TV

- Qual o modelo e o ano: leia a etiqueta ou Sobre esta TV e rode o acha_tv.py desta pasta. Isso destrava qual ramo de cada secao se aplica.
- Qual a versao do Tizen de hoje (a de fabrica pode ter subido por update): ligue o Modo Desenvolvedor e rode sdb capability, ou veja o comportamento do menu (One UI com Recursos Avancados indica Tizen 9).
- Seu controle e Solar sem numeros: o Solar emite IR nas teclas que tem (setas, OK, Home, 123, volume, canal), mas nao tem Info, Menu, digitos nem o Power classico, entao nao serve para as sequencias de standby do menu de servico; use o botao 123 ou o SmartThings para o 12345, e um controle antigo com numeros, um Flipper Zero ou um celular com emissor IR para as sequencias de servico (github.com/Lucaslhm/Flipper-IRDB).
- A sua TV ignora o DNS da rede: depois de reiniciar, veja se o IP dela aparece no log do Pi-hole ou AdGuard; se nao aparecer, fixe o DNS na TV e, se preciso, redirecione a porta 53 no roteador.
- O Autorun Last App funciona no seu modelo: teste com um app aberto, desligue e ligue; a Samsung avisa que nem todo app aceita.
- Fotografe, antes de qualquer mudanca de risco: as Opcoes da Tela Inicial, o menu de privacidade e, se for abrir menu de servico ou hotel, cada tela dele. Essas fotos sao o seu unico "desfazer".

## 9. Fontes

Oficiais Samsung: policy.samsungrs.com; samsung.com/br/info/privacy/smarttv; developer.samsung.com (TIFA, certificados); samsung.com/us/support/answer/ANS10010616 (ACR); news.samsung.com/br (Samsung Ads); manual de hospitalidade HG470/570 (via github.com/capital-lan/LN32D467).

Projetos e bibliotecas: github.com/Gathin23/cleanyourtv (e docs/devices/samsung-tizen.md, copia local nesta pasta); github.com/reisxd/TizenBrew e TizenTube; github.com/Apps2Samsung/Apps2Samsung e tizen-community-packages; github.com/helalaou/AeroTizen; github.com/NelsonEU/arn0-tv; github.com/xchwarze/samsung-tv-ws-api; github.com/ollo69/ha-samsungtv-smart; github.com/home-assistant/core (samsungtv); github.com/Toxblh/samsung-tv-control; github.com/Maassoft/ColorControl; github.com/oBusk/samsung-service-menu; github.com/Georift/install-jellyfin-tizen; github.com/jeppevinkel/jellyfin-tizen-builds; github.com/brightcraft/moonlight-tizen; github.com/SushyDev/tizen-homebrew; github.com/andrearicci93/vetro; github.com/chris-ritsen/samsung-tv-root; github.com/synacktiv/samsung-q60t-exploit; github.com/Tianyulife/samsung-m8-cn-to-us.

DNS: github.com/hagezi/dns-blocklists; github.com/Okazakee/tv-dns-blocklist; github.com/Perflyst/PiHoleBlocklist.

Decodificacao e compatibilidade: github.com/Yskra/yskra; github.com/lucaskfp/tizen-sim; github.com/matomo-org/device-detector; github.com/bbc/melanite; github.com/jss8649/quiet-tizen; github.com/carlosbarreto55/tvhomelab.

IR: github.com/Lucaslhm/Flipper-IRDB; github.com/probonopd/irdb.

Seguranca e imprensa: bishopfox.com (Tizen); synacktiv.com (GreHack 2021); ucl.ac.uk (ACR, 2024); texasattorneygeneral.gov (acordo ACR, 2026); jellyfin.org; sammobile.com; flatpanelshd.com.

Os arquivos de dados desta pesquisa (achados-finais.json, achados-extras-lacunas.json, vereditos-parciais.json, critico-lacunas.json) estao nesta mesma pasta e trazem, por achado, o veredito, a correcao do verificador e a lista completa de URLs.
