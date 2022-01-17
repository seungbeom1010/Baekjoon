const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const A = parseInt(input[0]);
const B = parseInt(input[1]);
const B1 = parseInt(input[1][2]);
const B2 = parseInt(input[1][1]);
const B3 = parseInt(input[1][0]);

console.log(A * B1);
console.log(A * B2);
console.log(A * B3);
console.log(A * B);