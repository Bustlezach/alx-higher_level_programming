#!/usr/bin/node

// Print the values of argv except undefined.

const val = process.agrv[2];
if (typeof val === `undefined`) {
  console.log("No argument");
} else {
  console.log(`${val}`);
};
