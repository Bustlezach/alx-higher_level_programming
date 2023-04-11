#!/usr/bin/node

// This script searches the second biggest integer in the list of arguments

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const vals = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(vals[vals.length - 2]);
}
