#!/usr/bin/node
const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.height; j++) {
        process.stdout.write(c);
      }
      process.stdout.write('\n');
    }
  }
}
module.exports = Square;
