// Encuentra el promedio (avg): Dado un array con múltiples valores, escribe una función que devuelva el promedio de los valores (ej: para [1,3,5,7,20] el promedio es 7.2).

function findAvg(x){

    var sum = 0;
    var avg = 0;

    for(var i=0; i<x.length; i++){
        sum = sum + x[i];
    }

    avg = sum/x.length;

    return console.log(avg);
}

findAvg([1,3,5,7,20]);
