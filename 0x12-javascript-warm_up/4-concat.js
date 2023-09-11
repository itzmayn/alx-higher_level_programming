#!/usr/bin/node
// Prints two arguments passed to it in the following format: " is "

if (process.argv.length < 4) {
    console.log("Please provide at least two arguments.");
  } else {
    console.log(process.argv[2] + ' is ' + process.argv[3]);
  }
  