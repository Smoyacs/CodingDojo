// Suma impares hasta 5000: Escribe una función que devuelva la suma de todos los números impares entre 1 y 5000 (ej: 1+3+5+...+4997+4999).

function sumOdden(x){
    var sum = 0;

    for(var i=1; i<x+1; i++){
        if(i%2 != 0){
            sum = sum + i;
            // console.log(i); Verficacion de numeros al sumar
        }
    }
    return console.log(sum);
}

sumOdden(5000);