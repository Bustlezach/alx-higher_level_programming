#!/usr/bin/node

// Check the number of values entered in argv

const len = process.argv.length;
console.log(len === 2 ? 'No argument' : len === 3 ? 'Argument found' : 'Arguments found');
