// Cuadrados: Dado un array con múltiples valores, escribe una función que reemplace cada valor por el cuadrado del mismo valor (ej: [1,5,10,-2] será [1,25,100,4]).

function replaceToSquare(x){
    for(var i=0; i<x.length; i++){
        x[i] = x[i]**2;
    }
    return console.log(x);
}

replaceToSquare([1,5,10,-2,-3]);