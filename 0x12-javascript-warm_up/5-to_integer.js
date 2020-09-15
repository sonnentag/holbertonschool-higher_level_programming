#!/usr/bin/node
// output arg as integer or 'not a number'

const Arg = isNaN(process.argv[2]) ? 'Not a number' : 'My number: ' + process.argv[2];

console.log(Arg);
