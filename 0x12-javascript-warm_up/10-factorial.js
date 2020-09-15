#!/usr/bin/node
// return factorial of arg

let num = process.argv[2];

if (isNaN(num)) {
  num = 0;
}

const factorial = function (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
};

console.log(factorial(num));
