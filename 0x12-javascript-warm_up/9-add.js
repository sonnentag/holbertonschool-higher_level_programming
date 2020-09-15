#!/usr/bin/node
// add 2 args

const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}
