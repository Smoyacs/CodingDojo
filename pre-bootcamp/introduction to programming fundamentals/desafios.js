function imprimeHasta(x) {
    // escribe tu código aquí

    if(x>=1){
        for(var i=1;i<x+1;i++){
            console.log(i);
        }
    }
    else if(x<1){
        return false
        
    }   
}
imprimeHasta(1000000); // debe imprimir todos los enteros desde el 1 hasta el 1000000
y = imprimeHasta(-10); 
console.log(y); // debe imprimir false


function printSum(x) {
    var sum = 0;
    // escribe tu código aquí
    for(var i=0;i<x+1;i++){
        console.log(i);
        sum = sum + i;
    }
    return sum
}
y = printSum(255) // debe imprimir todos los enteros desde el 0 hasta el 255, y la suma parcial en cada punto
console.log(y) // debe imprimir 32640



function printSumArray(x) {
    var sum = 0;
    for (var i = 0; i < x.length; i++) {
        // escribe tu código aquí
        sum = x[i] + sum;
    }
    return sum;
}
console.log( printSumArray([1,2,3]) ); // debe imprimir 6



function mayorElem(x) {
    var mayorHastaAhora = x[0];
    // escribe tu código aquí
    for(var i=0;i<x.length;i++){
        if(x[i]>mayorHastaAhora){
            mayorHastaAhora = x[i];
        }
    }
    return mayorHastaAhora;
}
console.log( mayorElem([8,3,11,2,-8]) ); // debe imprimir 11