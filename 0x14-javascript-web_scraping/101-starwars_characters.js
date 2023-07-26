#!/usr/bin/node
const request = require('request');
const id = parseInt(process.argv[2]);
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const printCharacters = function (characters, index) {
  if (index >= characters.length) return;

  request(characters[index], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
      printCharacters(characters, index + 1);
    } else {
      printCharacters(characters, index + 1);
    }
  });
};

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
