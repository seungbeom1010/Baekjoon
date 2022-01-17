const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ').map(val => +val);
const A = input;

if (A % 4 == 0 && A % 100 != 0) {
    console.log(1)
} else if (A % 400 == 0) {
    console.log(1)
} else {
    console.log(0)
};