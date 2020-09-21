#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('X');
        }
        process.stdout.write('\n');
      }
    }
    rotate () {
        const h = this.height;
        const w = this.width;
    
        this.height = w;
        this.width = h;
      }
    
      double () {
        this.height = this.height * 2;
        this.width = this.width * 2;
      }
  }
  module.exports = Rectangle;