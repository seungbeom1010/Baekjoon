const fs = require('fs');
const input = require("fs").readFileSync("/dev/stdin").toString().split(" ");

// initialise the time value with Number.
let num1 = Number(input[0]); // H for hour
let num2 = Number(input[1]); // M for minute

// provide a new condition : -45, to num2.
num2 -= 45; // subtract from the default time value

// establish if statement

if (num2 < 0) { 
	num2 += 60; 
    num1 --;
    
    if (num1 === -1) {
    	num1 = 23;
	}
}

console.log(num1 + " " + num2);