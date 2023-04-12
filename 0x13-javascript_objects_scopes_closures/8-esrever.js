#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  for (let a = list.length - 1; a >= 0; a--) {
    rev.push(list[a]);
  }
  return rev;
};
