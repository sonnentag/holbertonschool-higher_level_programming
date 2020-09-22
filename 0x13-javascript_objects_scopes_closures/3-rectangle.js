#!/usr/bin/node
/* empty class */

class Rectangle {
  constructor (w, h) {
    if ((w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    } else {
    }
  }

  print () {
    let out = '';
    for (let x = 0; x < this.width; x++) {
      out = out + 'X';
    }
    for (let x = 0; x < this.height; x++) {
      console.log(out);
    }
  }
}
module.exports = Rectangle;
