#!/usr/bin/node
const request = require('request');
const movieID = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
let res;

const message = function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    res = JSON.parse(body);
    console.log(res.title);
  }
};
request(url, message);
