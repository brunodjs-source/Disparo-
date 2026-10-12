# Calendário e funil · série "Etapas reais do lançamento"

Toda peça segue o mesmo caminho: comentário com a palavra → direct automático com botão → página com formulário → PDF + Grupo do Estrategista → diagnóstico O Tabuleiro.

Página de captação: https://estrategista-materiais-videon8ns-projects.vercel.app/m/<material>
Painel de leads e PDFs: https://estrategista-materiais-videon8ns-projects.vercel.app/admin

| Data | Hora | Post | Palavra | Página / PDF |
|---|---|---|---|---|
| já no ar | | Reels 01 Pesquisa | PESQUISA | /m/pesquisa · Pesquisa antes do produto |
| 12/10 | 06h | Carrossel 10 perguntas | CHECKLIST | /m/checklist · Checklist de Lançamento |
| 12/10 | 11h | Reels 02 Oferta | OFERTA | /m/oferta · Estrutura de Oferta |
| 12/10 | 18h | Reels 03 Captação | CAPTAÇÃO | /m/captacao · Checklist de Captação |
| 12/10 | 20h | Reels 04 Aquecimento | AQUECIMENTO | /m/aquecimento · Sequência de Aquecimento |
| 13/10 | 11h | Reels 05 Evento | EVENTO | /m/evento · Roteiro do Evento |
| 13/10 | 18h | Reels 06 Carrinho | CARRINHO | /m/carrinho · Cronograma do Carrinho |
| 13/10 | 20h | Reels 07 Recuperação | RECUPERAÇÃO | /m/recuperacao · Recuperação e Downsell |
| 14/10 | 11h | Reels 08 Perpétuo | PERPÉTUO | /m/perpetuo · Do lançamento ao perpétuo |

Stories (postados à mão, com figurinha de link para o Reels do dia): use `videos/stories/sNN` uns 30 a 60 minutos depois de cada Reels sair.

Os PDFs ficam em `materiais/pdfs/` (fonte em `materiais/pdfs/src`, gerar com `node build.js`). A última página de cada PDF lista as 9 palavras da série (`python3 fill_series.py`).
