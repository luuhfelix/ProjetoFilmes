/**
 * Created by Luciana on 24/10/2014.
 */

$(document).ready(function () {
    var $movieForm = $('#movie-form');
    $movieForm.hide();
    $('#mostrar-form-btn').click(function () {
        $movieForm.slideToggle();
    });


    var $tituloInput = $('#tituloInput');
    var $lancamentoInput = $('#lancamentoInput');
    var $deInput = $('#deInput');
    var $generoInput = $('#generoInput');
    var $comInput = $('#comInput');
    var $ajaxGif = $('#ajax-gif');

    var $tituloDiv = $('#tituloDiv');
    var $lancamentoDiv = $('#lancamentoDiv');

    $ajaxGif.hide();
    var $salvarBtn = $('#salvar-btn');
    var $helpTituloSpan = $('#help-titulo');
    var $helpLancamentoSpan = $('#help-lancamento');
    var $corpoTabela = $('#corpo-tabela');

    var adicionarLinha=function adicionarLinha(movie) {
        var linha = '<tr id="tr' + movie.id + '"> <td>' + movie.titulo + '</td>' +
            '<td>' + movie.lancamento + '</td>' +
            '<td>' + movie.de + '</td>' +
            '<td>' + movie.genero + '</td>' +
            '<td>' + movie.com + '</td>' +
            '<td><button id="bt' + movie.id + '" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button>' +
            '</td> </tr>';

        $corpoTabela.prepend(linha);

        var $linhaHtml = $('#tr' + movie.id);

        $linhaHtml.hide();
        $linhaHtml.fadeIn();
        $('#bt' + movie.id).click(function () {
            $linhaHtml.fadeOut();
            $.post('/movies/rest/delete',{'movie_id':movie.id}).success(function(){
                $linhaHtml.remove();
            }).error(function(){
                alert('Remoção não funcionou');
                $linhaHtml.fadeIn();
            });
        });
    }

    $.get('/movies/rest').success(function (listaDeMovies) {
        for (var i = 0; i < listaDeMovies.length; i += 1) {
            adicionarLinha(listaDeMovies[i]);
        }

    });

    $salvarBtn.click(function () {
        var movie = {titulo: $tituloInput.val(),
            lancamento: $lancamentoInput.val(),
            de: $deInput.val(),
            genero: $generoInput.val(),
            com: $comInput.val()};

        $ajaxGif.slideDown();
        $salvarBtn.hide();
        var promessa = $.post('/movies/rest/save', movie);
        promessa.success(function (movie_do_servidor) {
           adicionarLinha(movie_do_servidor);
        });


        promessa.error(function (erros) {
            if (erros.responseJSON != null && erros.responseJSON.titulo != null) {
                $tituloDiv.addClass('has-error');
                $helpTituloSpan.text(erros.responseJSON.titulo);
            }
            if (erros.responseJSON != null && erros.responseJSON.lancamento != null) {
                $lancamentoDiv.addClass('has-error');
                $helpLancamentoSpan.text(erros.responseJSON.lancamento);
            }
        });

        promessa.always(function () {
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        })
    });

});

