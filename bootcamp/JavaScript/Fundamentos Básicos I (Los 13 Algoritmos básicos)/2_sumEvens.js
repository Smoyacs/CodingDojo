// Consigue pares hasta 1000: Escribe una función que entregue la suma de todos los números pares del 1 al 1000 - Puedes usar un operador de módulo para este ejercicio. 

function sumEven(x){
    var sum = 0;
    for(var i=0; i<x+1; i++){
        if(i%2==0){
            sum = sum + i;
            // console.log(i); verificacion de numeros al sumar.
        }
    }
    return console.log(sum);
}

sumEven(1000);
