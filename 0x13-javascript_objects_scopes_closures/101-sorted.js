#!/usr/bin/node

const dict = require('./100-data.js').dict;

const new_dict = {};

for (const [key, value] of Object.entries(dict)) {
  if (!new_dict[value]) {
    new_dict[value] = [key];
  } else {
    new_dict[value].push(key);
  }
}

console.log(new_dict);
