#!/usr/bin/node

// Print the values of argv except undefined.

const vals = process.agrv;
if (vals[2] === undefined) {
  console.log("No argument");
} else {
  vals.forEach((val) => {
    console.log(val);
  });
};
