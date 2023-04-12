#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

const incr = function () {
  this.value += 1;
};
