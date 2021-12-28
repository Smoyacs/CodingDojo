function sum_even(a){
    var sum = 0;

    for(var i=0; i<a+1; i++){
        if(i%2===0){
            sum = sum + i;

        }
    }
    return console.log(sum)
}

sum_even(1000);

