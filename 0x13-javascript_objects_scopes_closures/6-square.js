#!/usr/bin/node
class Square extends require('./5-square') {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.height));
      } else {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
