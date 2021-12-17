// usar diagrama T

var h = [2,4,6,8,10];
for (var i = 0; i < h.length; i++) {
    console.log(i);
    console.log(h[i]);
}

//      variable    |   valor
//           i      |   0,1,2,3,4        
//           h      |   2,4,6,8,10

var j = [2,4,6,8,10];
for (var k = j.length - 1; k > 0; k--) {
    console.log(k);
    console.log(j[k]);
}

//      variable    |   valor
//           k      |   4,3,2,1        
//           j      |   10,8,6,4

var m = [2,4,6,8,10];
for (var n = 0; n < m.length; n += 2) {
    console.log(n);
    console.log(m[n]);
}

//      variable    |   valor
//           n      |   0,2,4        
//           m      |   2,6,10

var p = [-1,0,5,-3,2];
for (var q = 0; q < p.length; q++) {
    if (p[q] < 0) {
        p[q] = "Dojo";
    }
}
console.log(p);

//      variable    |   valor
//           q      |   0,1,2,3,4        
//           p      |   [Dojo,0,5,Dojo,2]

var r = [-1,0,5,-3,2];
for (var s = 0; s < r.length; s++) {
    if (r[s] > 0) {
        r[s] = r[s] * r[s];
    }
}
console.log(r);

//      variable    |   valor
//           s      |   0,1,2,3,4        
//           r      |  [-1,0,25,-3,4]

var t = [];
for (var u = 0; u < 4; u++) {
    t.push(u);
}
console.log(t);

//      variable    |   valor
//           u      |   0,1,2,3        
//           t      |  [0,1,2,3]

var v = [1,2,3,4,5];
for (var w = 0; w < v.length; w++) {
    v.pop();
}
console.log(v);

//      variable    |   valor
//           w      |   0,1,2,3,4        
//           v      |  [1,2]
