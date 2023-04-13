#!/usr/bin/node

const list = require ('./100-data.js').list;

const new_arr = list.map ((cur, i) => cur * i);
console.log (list);
console.log (new_arr);
