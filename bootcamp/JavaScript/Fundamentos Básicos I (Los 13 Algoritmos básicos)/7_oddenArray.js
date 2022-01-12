// Array de impares: Escribe una función que devuelva un array de todos los números impares entre 1 y 50 (ej: [1,3,5, …, 47,49]). Pista: Usa el método ‘push’.

function oddenArray(x){
    var oddenArr = [];

    for(var i=1; i<x+1; i++){
        if(i%2 != 0){
            oddenArr.push(i);
        }
    }
    return console.log(oddenArr);
}

oddenArray(50);