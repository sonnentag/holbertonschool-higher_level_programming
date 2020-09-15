#!/usr/bin/node
// output according to number of args

const fstArg = (process.argv[2]) ? process.argv[2] : undefined;
const sndArg = (process.argv[3]) ? process.argv[3] : undefined;

console.log(fstArg + ' is ' + sndArg);
