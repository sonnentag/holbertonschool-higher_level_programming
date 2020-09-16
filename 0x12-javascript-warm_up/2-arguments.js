#!/usr/bin/node
// output according to number of args

console.log((process.argv.length === 2) ? 'No argument'
  : (process.argv.length === 3) ? 'Argument found'
    : 'Arguments found');
