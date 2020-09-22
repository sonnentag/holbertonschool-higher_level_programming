#!/usr/bin/node
/* empty class */

module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }

  charprint (c) {
    let out = '';
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let x = 0; x < this.width; x++) {
      out = out + c;
    }
    for (let x = 0; x < this.height; x++) {
      console.log(out);
    }
  }
};
