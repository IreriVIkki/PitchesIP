$(document).ready(function () {
    $('.box-link').click(function (e) {
        e.preventDefault();

    });

    $('.dim').click(function (e) {
        e.preventDefault();
        var dim = '.dim'
        $(dim).addClass('d-none');
        $('.dim').addClass('fadeOut');
        $('.dim').removeClass('fadeIn');
        $('.comment-block').addClass('d-none');
    });

});

function classname(id) {
    var id = '.res' + id
    $(id).removeClass('d-none');
    $(id).removeClass('fadeOut');
    $(id).addClass('fadeIn');
    $('.dim').removeClass('d-none');
}