$(document).ready(function(){

    // obtencion de imagen
    for(var i=1; i<152; i++){
        
        var url = "https://pokeapi.co/api/v2/pokemon/" +i+ "/";
        $.get(url, function(res) {
            console.log("res",res);
            console.log("id", res.id);
            $('.pokemones').append("<img src='" + res.sprites.front_default + "' id= '" + res.id + "'>");
        }, "json");                      
    }

    // muestra de info
    $(".pokemones").on('click','img', function() {
        var id = $(this).attr('id');
        console.log(id)
        var url = "https://pokeapi.co/api/v2/pokemon/" + id + "/";
        var html = "";
        

        $.get(url, function(res) {
            
            html = "<h2>#"+ res.id +" "+ res.name + "</h2>";
            html += "<img src='" + res.sprites.front_default + "'>";
            html += "<h4>Tipos</h4>";
            html += "<ul>";
            for(var i in res.types){
                html += "<li>" + res.types[i].type.name + "</li>";
            }
            html += "</ul>";
            html += "<p> Peso: " + res.weight + "</p>";
            html += "<p> Altura: " + res.height + "</p>";

            $('.pokedex').html(html);
        }, "json");
    });


});
    



