#!/usr/bin/node

const square = require('./5-square');

module.exports = class Square extends square {
  constructor (size, c) {
    super(size);
    this.c = c;
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
};
