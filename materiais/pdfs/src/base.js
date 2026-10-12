// Adiciona cabecalho e rodape com numero de pagina em todas as paginas, exceto a capa.
(function () {
  var title = document.body.getAttribute('data-short') || '';
  var pages = document.querySelectorAll('.page');
  var total = pages.length;
  pages.forEach(function (pg, i) {
    if (pg.classList.contains('cover')) return;
    var n = String(i + 1).padStart(2, '0');
    var t = String(total).padStart(2, '0');
    var hd = document.createElement('div');
    hd.className = 'hd';
    hd.innerHTML = '<span>O Estrategista</span><span class="t">' + title + '</span>';
    var ft = document.createElement('div');
    ft.className = 'ft';
    ft.innerHTML = '<span>@o_estrategista.com.br · estrategistadelancamento.com.br</span><span class="n"><i>' + n + '</i> / ' + t + '</span>';
    pg.appendChild(hd);
    pg.appendChild(ft);
  });
})();
