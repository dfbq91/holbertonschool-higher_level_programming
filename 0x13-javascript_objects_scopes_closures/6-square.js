#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let x = 0; x < this.size; x++) {
      console.log(c.repeat(this.size));
    }
  }
};
