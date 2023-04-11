#!/usr/bin/node

// Check the number of values entered in argv

const val = process.agrv;
const len = val.length;
if (len <= 2) {
  console.log("No argument");
} else {
  console.log("Argument found");
};
