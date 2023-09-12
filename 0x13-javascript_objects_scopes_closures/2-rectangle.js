#!/usr/bin/node
// This JavaScript script defines a class and initializes values if they are positive integers.
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
