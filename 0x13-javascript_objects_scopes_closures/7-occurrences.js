#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((c, cur) => cur === searchElement ? c + 1 : c, 0);
};
