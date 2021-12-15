var num = 15;
if (num >= 10) {
    console.log("el número es mayor que 10");
}

// el número es mayor que 10

var name = "Bruce";
if (name != "Bruce") {
    console.log("¿Cuál es tu nombre?");
} 
else {
    console.log("Hola, Bruce!");
}

// Hola, Bruce!

var num1 = 10;
var num2 = 15;
if (num1 <= num2) {
    num1 = num1 + 10;
}
console.log(num1);
console.log(num2);

// 20
// 15
function maxMinAvg(arr) {
    var arrnew=[];
    var max=0;
    var ln=arr.length;
    var sum=0;


    
    for(var i=0;i<ln;i++){

        if(arr[i]>max){
            max = arr[i];
        }
        
        if(arr[i]<max){
            min = arr[i];
        }
    
        sum = sum + arr[i];

    }


    
    avg = sum/ln
    
    arrnew.push(max);
    arrnew.push(min);
    arrnew.push(avg);
    
    return console.log(arrnew); 
}
var arr=[4,2,5,87,-3,0,-100];
maxMinAvg(arr);

var arr=[100,200,1,300,500,20];
function swap(arr) {
    
    var arrnew=0;
    var temp=0;
    var ln=arr.length;
    
    temp=arr[0];
    arr[0]=arr[ln-1];
    arr[ln-1]=temp;
    arrnew=arr

    return console.log(arrnew); 
}

swap(arr);