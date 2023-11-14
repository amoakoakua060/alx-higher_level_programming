#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    w = parseInt(w);
    h = parseInt(h);

    if ((!isNaN(w) && w > 0) && (!isNaN(h) && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let a;
    for (let i = 0; i < this.height; i++) {
      a = '';
      for (let j = 0; j < this.width; j++) {
        a = a + 'X';
      }
      console.log(a);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
