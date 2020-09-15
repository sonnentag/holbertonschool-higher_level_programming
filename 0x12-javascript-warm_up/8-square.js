#!/usr/bin/node
//  print a square of arg size

const size = process.argv[2];
let count1 = 0;
let count2 = 1;
let output = 'x';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (count1 < size) {
    while (count2 < size) {
      output = output + 'x';
      count2 += 1;
    }
    console.log(output);
    count1 += 1;
  }
}
