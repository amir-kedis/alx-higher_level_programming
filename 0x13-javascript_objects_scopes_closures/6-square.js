#!/usr/bin/node

const SquareO = require('./5-square');

class Square extends SquareO {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    c = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
