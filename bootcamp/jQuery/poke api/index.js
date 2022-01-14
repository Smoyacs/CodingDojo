$(document).ready(function(){
    for (var i=1; i < 152; i++){
        $('div.pokemones').append("<img src=http://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+i+".png>");
    }
})