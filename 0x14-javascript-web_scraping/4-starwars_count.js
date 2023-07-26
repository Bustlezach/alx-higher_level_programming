#!/usr/bin/node

const request = require('request');
const url = "https://swapi-api.alx-tools.com/api/films/";

const message = function (error, response, body) {
    if (error) {
        console.error(error);
    } else {
        const res = JSON.parse(body).results;
        console.log(
            res.reduce((count, movie) => {
                return movie.characters.some((character) => character.endsWith('/18/')) ? count + 1 : count;
            }, 0)
        );
    }
};

request(url, message);
