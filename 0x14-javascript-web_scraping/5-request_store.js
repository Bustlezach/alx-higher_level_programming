#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, function(error, response, body) {
    if (error) {
        console.error(error);
    } else {
        const webContent = JSON.parse(body);
        fs.writeFile(file, JSON.stringify(webContent), 'utf8', function(error) {
            if (error) {
                console.error(error);
            }
        });
    }
});
