#!/usr/bin/node
// executes x times a function, function is exported.

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
