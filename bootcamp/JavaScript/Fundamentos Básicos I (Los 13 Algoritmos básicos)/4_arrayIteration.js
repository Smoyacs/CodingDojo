// Itera un array: Escribe una función que devuelva la suma de todos los valores dentro de un array (ej:  [1,2,5] retorna 8. [-5,2,5,12] retorna 14). 


function sumArray(x){

    let sum = 0;

    for(var i=0; i<x.length; i++){
        sum = sum + x[i];
        
    }
    return console.log(sum);
}

sumArray([1,2,6]);