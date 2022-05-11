var fs = require('fs');
var inputData = fs.readFileSync('/dev/stdin').toString().split(' ').map(value => +value);
var [a, b, c] = inputData;
console.log((a + b) % c);
console.log(((a % c) + (b % c)) % c);
console.log((a * b) % c);
console.log(((a % c) * (b % c)) % c);