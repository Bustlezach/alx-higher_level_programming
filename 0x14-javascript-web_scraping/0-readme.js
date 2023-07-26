#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];

const message = function (error, data) {
  if (error) {
    console.log(error);
  } else {
    process.stdout.write(data);
  }
};
fs.readFile(file, 'utf8', message);
