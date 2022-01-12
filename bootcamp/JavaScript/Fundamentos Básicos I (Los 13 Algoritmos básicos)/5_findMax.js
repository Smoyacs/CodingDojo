// Encuentra el mayor (max): Dado un array con múltiples valores, escribe una función que devuelva el número mayor (ej: para [-3,3,5,7] el número mayor (max) es 7). 

function findMax(x){

    var maxElement = x[0];
    
    for(var i=0; i<x.length; i++){

        if(x[i]>maxElement){
            maxElement = x[i];
            // console.log(i);
        }
    }
    return console.log(maxElement);
}

findMax([1,10,20,-5,3]);
