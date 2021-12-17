function a() {
    console.log('hola');
}
console.log('Dojo');

// Dojo

function b() {
    console.log('hola');
    return 15;
}
var x = b();
console.log('x es', x);

// hola
// x es 15

function a(n) {
    console.log('n es', n);
    return n+15;
}
var x = a(3);
console.log('x es', x);

// n es 3
// x es 18

var z = 15;
console.log(z);
function a(z){
   console.log(z);   
   return z;
}
var b = a(10);
console.log(b);
console.log(z);

//      variable    |   valor
//           z      |   15        
//           b      |   10

// 15
// 10
// 10
// 15 

var c = 15;
console.log(c);
function d(c){
   console.log(c);   
   return c*2;
}
var e = d(10);
console.log(e);
console.log(c);

//      variable    |   valor
//           c      |   15        
//           e      |   (imprime 10),20    

// 15,10,20,15

function a(n) {
    console.log('n es', n);
    y = n*2;
    return y;
}
var x = a(3) + a(5);
console.log('x es', x);

//      variable    |   valor
//           x      |   (n es 3),6        
//                  |   (n es 5),10

// n es 3, n es 5, x es 16


function o(num1, num2) {  
    return num1+num2;
 }
 console.log(o(2,3));
 console.log(o(3,5));


//      variable    |   valor
//  o(num1,num2)    |     5      
//                  |     8

// 5,8

function u(num1, num2) {
    console.log(num1);   
    return num1+num2;
 }
 console.log(u(2,3))
 console.log(u(3,5))

//      variable    |   valor
//  y(num1,num2)    |     2,5      
//                  |     3,8

// 2,5,3,8

function i(a,b) {
    var c = a + b;
    console.log('c es', c);
    return c;
}
var x = i(2,3) + i(3,5);
console.log('x es', x);

//      variable    |   valor
//      z(a,b)      |   (c es 5)     
//                  |   (c es 8)
//         x        |   (x es 13)  

// c es 5,c es 8,x es 13

function d(a,b) {
    var c = a + b;
    console.log('c es', c);
    return c;
}
var x = d(2,3) + d(3,d(2,1)) + d(d(2,1),d(2,3));
console.log('x es', x);

//      variable    |   valor
//      d(a,b)      |   (c es 5)     
//                  |   (c es 3),(c es 6)
//                  |   (c es 3),(c es 5),(c es 8)
//         x        |   (x es 19)

// c es 5,c es 3,c es 6,c es 3,c es 5,c es 8,x es 19


