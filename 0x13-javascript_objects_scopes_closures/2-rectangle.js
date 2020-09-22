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
}
module.exports = Rectangle;
