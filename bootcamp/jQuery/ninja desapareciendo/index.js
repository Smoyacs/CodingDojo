$(document).ready(function(){

    $('.content img').click(function(){
        $(this).hide();
    });

    $('.button').click(function(){
        $('.content img').show();
    });
    
});

