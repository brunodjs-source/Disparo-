# Reescreve o bloco "Outros materiais da série" de cada PDF com a série completa (menos o próprio).
# Uso: python3 fill_series.py [slug ...]
import re, sys, os
SERIE = [
  ('checklist', 'Checklist de Lançamento', 'CHECKLIST'),
  ('pesquisa', 'Pesquisa antes do produto', 'PESQUISA'),
  ('oferta', 'Estrutura de Oferta', 'OFERTA'),
  ('captacao', 'Checklist de Captação', 'CAPTAÇÃO'),
  ('aquecimento', 'Sequência de Aquecimento', 'AQUECIMENTO'),
  ('evento', 'Roteiro do Evento', 'EVENTO'),
  ('carrinho', 'Cronograma do Carrinho', 'CARRINHO'),
  ('recuperacao', 'Recuperação e Downsell', 'RECUPERAÇÃO'),
  ('perpetuo', 'Do lançamento ao perpétuo', 'PERPÉTUO'),
]
here = os.path.dirname(os.path.abspath(__file__))
slugs = sys.argv[1:] or [s for s, _, _ in SERIE]
for slug in slugs:
    p = os.path.join(here, slug + '.html')
    if not os.path.exists(p):
        continue
    html = open(p, encoding='utf-8').read()
    items = ''.join(f'\n    <div><b>{t}</b>Comenta <span>{k}</span></div>' for s, t, k in SERIE if s != slug)
    block = ('<h4 style="color:var(--gold);margin-top:6mm">Outros materiais da série · comente a palavra no post ou peça no direct</h4>\n'
             '  <div class="series">' + items + '\n  </div>')
    new, n = re.subn(r'<h4[^>]*>Outros materiais[^<]*</h4>\s*<div class="series">.*?</div>\s*</div>', block, html, flags=re.S)
    if n != 1:
        print(slug, 'bloco nao encontrado'); continue
    open(p, 'w', encoding='utf-8').write(new)
    print(slug, 'ok')
