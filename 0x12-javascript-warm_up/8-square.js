#!/usr/bin/node
//  print a square of arg size

const size = process.argv[2];
let count = 1;
let output = 'X';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (count < size) {
    output = output + 'X';
    count += 1;
  }
  count = 0;
  while (count < size) {
    console.log(output);
    count += 1;
  }
}
