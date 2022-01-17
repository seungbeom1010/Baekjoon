var fs = require('fs');
var inputData = fs.readFileSync('/dev/stdin').toString().split(' ').map(value => +value);
var [a, b] = inputData;
console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(Math.floor(a / b));
console.log(a % b);