//  1 to x
function printUpTo(x) {
   // your code here
   for(var i=1; i<x+1; i++){
      console.log(i);
   }
   if(x<0){
      return false;
   }
}
 printUpTo(1000); // debería imprimir todos los enteros de 1 to 1000
 y = printUpTo(-10); // debería imprimir false
 console.log(y); // debería imprimir false


//  print sum
function printSum(x) {
   var sum = 0;
   //your code here
   for(var i=0; i<x+1; i++){
      console.log('n° entero: ',i); // imprime los enteros 
      sum = sum + i; 
      console.log('suma parcial:',sum,'\n'); // imprime suma parcial
      
   }
   return sum
}
 y = printSum(255) // debería imprimir todos los enteros de 0 a 255 y que cada entero imprima la suma parcial.
 console.log(y,'\n') // // debería imprimir 32640


// printsum array
function printSumArray(x) {
   var sum = 0;
   for(var i=0; i<x.length; i++) {
     //your code here
      sum = sum + x[i];
   }
   return sum;
}
console.log( printSumArray([1,2,3]),'\n' ); // debería imprimir 6


function largestElement(x){
   var largest = x[0];
   for(var i=0; i<x.length; i++){
      if(x[i]>largest){
         largest = x[i];
      }
   }
   return console.log(largest);
}
largestElement([1,30,5,7]);