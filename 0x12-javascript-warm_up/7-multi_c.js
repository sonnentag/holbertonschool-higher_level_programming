#!/usr/bin/node
// output x times 'c is fun' or 'missing number..'

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  while (process.argv[2] > 0) {
    console.log('C is fun');
    process.argv[2] -= 1;
  }
}
