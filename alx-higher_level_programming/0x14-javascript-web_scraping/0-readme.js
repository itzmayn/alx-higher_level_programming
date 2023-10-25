#!/usr/bin/node
const fs = require('fs');

// Read the content of the file specified in the command-line argument (process.argv[2])
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Log either the content of the file if there's no error, or the error message
  console.log(error || content);
});
