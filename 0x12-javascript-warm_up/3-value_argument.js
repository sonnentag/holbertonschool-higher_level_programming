#!/usr/bin/node
// output according to number of args 

const firstArg = process.argv[2];

const myVar = (firstArg) ? firstArg : 'No argument';

console.log(myVar);
