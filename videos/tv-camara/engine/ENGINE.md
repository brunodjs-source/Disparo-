# Motor da entrevista · TV Câmara Campinas

Mesma lógica da HyperFrames: HTML com `render(t, camada)` determinístico, capturado quadro a quadro pelo Playwright e composto pelo ffmpeg/numpy.

## Fontes (fora do repo, no scratchpad da sessão; o original fica no rascunho de release `entrevista-tv-camara`)
- `src/entrevista-1080p.mp4`: plano ABERTO, 1080x1920, 30 fps, já convertido de HDR (tonemap hable).
- `src/entrevista-zoom.mp4`: plano Z2, recorte nativo 1080x1920 do 4K (x 1080, y 1000), mesmo tempo.
- `voz_trat.wav`: áudio inteiro tratado (highpass, arnndn, afftdn, compressor, EQ 3 kHz, dynaudnorm), -16 LUFS.
- `dados/transcricao.json`: segmentos com palavras `[ini, fim, texto, prob]` e falante (`B` Bruno, `M` Mirna).

## Planos (comp.py)
| Plano | Fonte | Recorte (x, y, w, h) | Uso |
|---|---|---|---|
| Z2 | zoom | 0, 0, 1080, 1920 | os dois na mesa, parede livre em cima |
| CB | zoom | 309, 250, 771, 1371 (1,4x) | Bruno em 3/4 |
| CM | zoom | 0, 250, 771, 1371 (1,4x) | Mirna (só com autorização, até 25% do tempo) |
| ABERTO | full | 0, 0, 1080, 1920 | sala inteira, timelapse |

## corte.json (um por peça)
```json
{
  "id": "pb01", "fmt": "pb", "seg": [ini_s, fim_s], "dur": 28.4, "w": 1080, "h": 1920,
  "planos": [{"t0": 0, "t1": 9.2, "plano": "Z2", "zoom": [[0,1.0],[9.2,1.06]], "foco": [760, 870]}, ...],
  "pb": [[0, 28.4]], "look": "pb|cinema|natural", "back": false, "mascara": null,
  "blur_rects": {"zoom": [[x,y,w,h]], "full": [...]},
  "words": [[t_rel, "palavra", "B"], ...], "destaques": ["palavra"],
  "textos": {...livre por formato...},
  "sfx": [["ding_si", 12.4, 0.35]], "trilha": "close-up", "trilha_vol": 0.06, "quietude": [[11.6, 12.0]],
  "fade": [0, 0.2]
}
```
Tempos dentro do corte são relativos ao início do trecho (`seg[0]`).

## Template (`templates/<fmt>.html`)
- Começa com `<script>/*__BASE__*/` (injeta `_base.js`: easing, `legendaGigante`, `connectHook`, `letreiro`, `nomeCargo`, `seloTV`, `ctaComentario`, `marca`, `progresso`, cores e fontes) e define `function render(t, camada)` que escreve em `#back` ou `#front`.
- Camada front é obrigatória em todo quadro (pode ficar vazia). Camada back só se `"back": true` (letreiro atrás das pessoas, recortado pela `mascara`).
- Regras: efeito na palavra que ele ilustra; 1 efeito novo a cada 2 s; nada encostado na borda, sobre a boca, no rodapé (y > 1650) ou na lateral direita (x > 960); sem logo de terceiros; sem travessão nem emoji.

## Rodar
```
node cap.js corte.json CAMADAS [quadros de teste]
python3 comp.py corte.json CAMADAS video.mp4 [quadros de teste]   # com quadros: gera CAMADAS/still_XXXXX.jpg
python3 mix.py corte.json audio.wav
ffmpeg -i video.mp4 -i audio.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest final.mp4
```
