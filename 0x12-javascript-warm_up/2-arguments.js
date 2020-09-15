#!/usr/bin/node
// output according to number of args 

const argLen = process.argv.length;

const myVar = (argLen === 2) ? 'No argument'
  : (argLen === 3) ? 'Argument found'
    : 'Arguments found';

console.log(myVar);
