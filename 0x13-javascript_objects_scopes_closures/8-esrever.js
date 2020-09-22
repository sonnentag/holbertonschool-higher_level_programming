#!/usr/bin/node
exports.esrever = function (list) {
  const r = [];
  let x = list.length - 1;
  for (let i = 0; i < list.length; i++, x--) {
    r[i] = list[x];
  }
  return r;
};
