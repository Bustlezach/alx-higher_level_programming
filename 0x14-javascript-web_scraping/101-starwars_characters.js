#!/usr/bin/node
const request = require('request');
const id = parseInt(process.argv[2]);
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

const message = function (error, response, body){
        if(error){
                console.error(error);
        } else {
                const characters = JSON.parse(body).characters;
                characters.forEach((character) => {
                        request(character, function(error, reponse, body){
                                if (!error){
                                        console.log(JSON.parse(body).name);
                                }
                        });
                        });
                }
};
request(url, message);
