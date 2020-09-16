#!/usr/bin/node
// return second biggest number in arg list

const arr = [];
let idx = 2;
let max = -Infinity;
let res = -Infinity;
let cur;

while (process.argv[idx]) {
  if (isNaN(process.argv[idx]) || process.argv.length <= 3) {
    res = 0;
  }
  arr.push(process.argv[idx]);
  idx += 1;
}

if (res !== 0) {
  for (const val of arr) {
    cur = Number(val);
    if (cur > max) {
      [res, max] = [max, cur];
    } else if (cur < max && cur > res) {
      res = cur;
    }
  }
}

console.log(res);
