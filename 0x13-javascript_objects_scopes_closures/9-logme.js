#!/usr/bin/node

// Initialize a count variable.
let count = 0;

// Export a function that logs each item with an incremented count.
exports.logMe = function (item) {
  // Log the item along with the current count, and then increment the count.
  console.log(`${count++}: ${item}`);
};
