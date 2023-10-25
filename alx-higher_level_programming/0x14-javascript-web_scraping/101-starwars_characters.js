#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;
request(movieUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  } else {
    console.error('Error:', error || `Request failed with status code ${response.statusCode}`);
  }
});

function printCharacters(characters, index) {
  if (index < characters.length) {
    request(characters[index], function (error, response, body) {
      if (!error && response.statusCode === 200) {
        console.log(JSON.parse(body).name);
        printCharacters(characters, index + 1);
      } else {
        console.error('Error:', error || `Request failed with status code ${response.statusCode}`);
      }
    });
  }
}
