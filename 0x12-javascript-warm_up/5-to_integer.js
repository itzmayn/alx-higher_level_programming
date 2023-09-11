#!/usr/bin/node
// Prints a number argument in the following format: "My number is "

if (process.argv.length < 3) {
  console.log('Please provide a number as an argument.');
} else if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number is ' + parseInt(process.argv[2]));
}
