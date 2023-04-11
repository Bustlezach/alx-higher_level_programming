#!/usr/bin/node

// This script prints x times “C is fun”

let x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log("Missing number of occurrences");
} else {
  while (x != 0) {
    console.log("C is fun");
    x -= 1;
  }
}
