// Mayor que Y: Dado un valor Y, escribe una función que toma un array y devuelve los valores mayores que Y. Por ejemplo, si arr = [1,3,5,7] y Y = 3, tu función devolverá 2 (hay 2 números en el array mayores que 3, esto son 5 y 7). 

function biggerThanY(arr,y){

    var biggerThan = [];

    for(var i=0; i<arr.length; i++){
        if(arr[i]>y){
            biggerThan.push(arr[i]);
        }
    }
    return console.log(biggerThan);
}

biggerThanY([1,3,5,7], 2);