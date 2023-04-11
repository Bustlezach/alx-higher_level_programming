#!/usr/bin/node

// This script prints My number: <first argument converted in integer> 
//if the first argument can be converted to an integer

const num = Math.floor(Number(process.agrv[2]));
console.log(isNaN(num) ? `Not a number` : `My number: ${num}`);
