#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

const message = function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const count = films.filter((film) => film.characters.includes(apiUrl + 'people/' + characterId + '/')).length;
    console.log(count);
  }
};

request(apiUrl, message);
