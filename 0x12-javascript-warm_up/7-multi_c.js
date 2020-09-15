#!/usr/bin/node
// output x times 'c is fun' or 'missing number..' 

let myArg = process.argv[2];

if (isNaN(myArg)) {
  console.log('Missing number of occurences');
} else {
  while ((myArg > 0)) {
    console.log('C is fun');
    myArg -= 1;
  }
}
