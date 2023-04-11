#!/usr/bin/node

// Print the values of argv except undefined.

const vals = process.agrv;
if (typeof vals[2] === undefined) {
  console.log("No argument");
} else {
  console.log(`${vals[2]}`);
};
