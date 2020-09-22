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

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const width = this.width;
    this.width = this.height;
    this.height = width;
  }
}
module.exports = Rectangle;
