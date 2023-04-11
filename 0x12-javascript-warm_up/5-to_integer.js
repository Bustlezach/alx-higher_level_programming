#!/usr/bin/node

const num = Math.floor(Number(process.agrv[2]));
console.log(isNaN(num) ? `Not a number` : `My number: ${num}`);
