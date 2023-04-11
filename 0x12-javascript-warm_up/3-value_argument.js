#!/usr/bin/node

// Print the values of argv except undefined.


console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
