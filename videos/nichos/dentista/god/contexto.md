# Contexto · Reel do dentista · O Estrategista · 21/10/2026

Leia também: /home/user/Disparo-/CLAUDE.md (regras e aprendizados medidos), /home/user/Disparo-/conteudo/sistema-instagram/00-SISTEMA.md (sistema de 7 módulos), /home/user/Disparo-/conteudo/modo-god-nichos/run/06-plano-final.md (plano dos 5 nichos; seção 2.2 é o dentista).

## O material bruto [FATO]
- Arquivo: /tmp/claude-0/-home-user-Disparo-/54eeb75b-22b3-521e-a4d4-71920aed6701/scratchpad/dent/raw.mp4 (selfie vertical gravada no celular, 576x1024, 31,6 fps, 36,4 s). Áudio já tratado: voz_master.wav na mesma pasta (ruído removido, -14 LUFS).
- Cena: Bruno em selfie de mão, plano fechado do rosto e ombros, jaqueta azul jeans, camiseta preta "PIXEL", escritório/coworking ao fundo com quadros coloridos (amarelo, roxo, branco), cadeiras, plantas e pessoas passando. Cabeça ocupa o centro; há parede livre acima e dos lados da cabeça (bom para letreiro atrás da pessoa). Veja frames-amostra.jpg.
- Transcrição com tempos (s): transcricao-tempos.txt. Texto: "Dentistas, são mais de 474 mil colegas ativos em Brasil. Por que você ainda só vende hora de cadeira? E quase todo perfil posta o mesmo diagnóstico e a mesma conclusão. Se você domina uma técnica que os dentistas querem aprender, existe um mercado. Qual é? Ensinar o seu colega. Eu desenho seu lançamento. Você deixa de disputar paciente e passa a formar quem disputa. Sua técnica vira um segundo produto. Dentista, comenta a sua profissão aqui que eu te respondo."
- Observação: o Bruno não citou o case Tzur nesta tomada.

## O que já fazemos (pipeline real no repositório) [FATO]
- videos/cases/tzur/: ov2.html + cap2.js + comp.py + seg.py. Abertura manifesto (P&B que vira colorido no número, confete, aplausos), letreiro 3D atrás da pessoa por segmentação rembg (u2net_human_seg) com camada de trás e camada da frente, b-roll nos cortes com 0,30 s de respiro, bloco final cinematográfico estilo After Effects com reacts.
- videos/serie2/: modelo.html genérico de motion (Playwright render(t) + ffmpeg), estética preto e ouro (#141210, #E8B36A, Cinzel + Playfair itálico), FX sonoro em Si e trilha lounge sintetizada em numpy (estaticos/stories-escala/som.py).
- Ferramentas: Playwright + Chromium, ffmpeg, numpy, rembg (cbenv), faster-whisper. Sem After Effects; tudo em HTML/Canvas/SVG/Three.js renderizado quadro a quadro.

## Referências de modelos (repositório awesome-opus5-5-videos, clonado em /home/user/yihui-dev/awesome-opus5-5-videos/prompts, 703 prompts, data/videos.json)
Candidatos já lidos: sab8a-475686 (cortar talking head em edição punchy com legenda, grafismo e música), gdgtify-929495 (tipografia cinética em que as palavras viram arquitetura; seek(t) determinístico; um momento de quietude de 400 ms), twoclipping-000267 (máscara de tipo, match cut, motion blur real por subframes com tmix, SFX alinhado pelo pico, loudnorm -14, lista de banidos: shockwave, partículas, RGB split, camera shake, lens flare, neon), alex-prompter-997524 (explainer de 5 cenas: problema, o que eu faço, 3 passos, prova, nome).

## Pedido literal do Bruno
"esse video é do dentista eu preciso que melhore o audio tire ruido e fundo do audio deixe ele totalmente masterizado e faça o video no modo que todo que vai atrair conversão baseado em saindo letreiro 4d atras e tambem dividindo dela com reacts e animações que representa precisa ser algo profissional estilo adobe effects. toma a decisão correta de quais os formatos fazer e ative a agencia modo god para tomar as decisões e pode misturar modelos de videos que estão no repositorio. faça um modelo no que ja fazemos e faça outros 2 no que voces pensam"

## Restrições
- 3 vídeos finais do MESMO bruto, 1080x1920, cerca de 36 s (pode cortar respiros, nunca cortar fala). Modelo A = o que já fazemos (estilo Tzur v2). Modelos B e C = propostas novas, podendo misturar prompts do repositório.
- Dados medidos: reels com o Bruno em cena performam 2,4x a 5,8x a mediana; animação sem rosto falha. O rosto do Bruno precisa estar visível nos 3 primeiros segundos e na maior parte do vídeo.
- CFO (publicidade odontológica): o vídeo fala com o dentista sobre negócio; sem antes e depois, sem promessa de resultado, sem preço. "474 mil colegas ativos" precisa de fonte (CFO) ou vira texto genérico na tela.
- Regras de texto: português do Brasil, sem travessão, sem emoji, sem citar HighClass, Júnior Prazeres ou Felipe Roser.
- Fonte de vídeo é 576x1024: upscale necessário; evitar zoom acima de 1,25x no rosto.
- Somente leitura: nenhum agente publica, agenda ou altera conta. Agentes podem escrever arquivos só dentro de /home/user/Disparo-/videos/nichos/dentista/god.
