// Obtén del 1 al 255: Escribe una función que devuelve un array con todos los números del 1 al 255.

function printUpTo(x) {
    
    var num = [];
    for(var i=1; i<x+1; i++){
        
        num.push(i);
    }
    return console.log(num);
}
printUpTo(255); 

