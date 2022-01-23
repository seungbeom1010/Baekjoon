var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ').map(value => +value);

for (i = 1; i < 10; i++) {
    console.log(input + ' * ' + i + ' = ' + input * i)
}