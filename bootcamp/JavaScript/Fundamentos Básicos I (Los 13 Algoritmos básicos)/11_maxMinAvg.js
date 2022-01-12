// Max/Min/Avg: Dado un array con múltiples valores, escribe una función que devuelva un nuevo array que solo contenga el valor mayor (max), menor (min) y promedio (avg) del array original (ej: [1,5,10,-2] devolverá [10,-2,3.5]).

function maxMinAvg(x){

    var max = x[0];
    var sum = 0;
    var avg = 0;
    var arr = [];

    for(var i=0; i<x.length; i++){
        
        if(x[i]>max){
            max = x[i];
        }

        else if(x[i]<max){
            min = x[i];
        }

        sum = sum + x[i];
    }
    
    avg = sum/x.length;

    arr.push(max);
    arr.push(min);
    arr.push(avg);

    return console.log(arr);
}

maxMinAvg([1,5,10,-2]);