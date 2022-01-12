// Intercambia Valores: Escribe una función que intercambie el primer y el último valor de cualquier array. La extensión mínima predeterminada del array es 2 (ej: [1,5,10,-2] será [-2,5,10,1]). 

function swapValues(x){

    var ln = x.length-1; // se le resta 1 debido a que necesitamos tomar el indice
    var first_num = x[0];
    var last_num = x[ln];

    // console.log(first_num);  verificacion de numeros
    // console.log(last_num);

    if(x.length<2){
        console.log("La extension minima del array es 2");
    }

    x[ln] = first_num;
    x[0] = last_num;

    return console.log(x);

}

swapValues([1,5,10,-2]);
