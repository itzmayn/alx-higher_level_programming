#!/usr/bin/node
const request = require('request');

// Define the SWAPI URL with the film ID provided as a command-line argument
const filmId = process.argv[2];
const swapiUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

// Make an HTTP GET request to the SWAPI
request(swapiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
  } else {
    // Parse the response body and print the movie title
    const movieData = JSON.parse(body);
    console.log('Movie Title:', movieData.title);
  }
});
