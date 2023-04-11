#!/usr/bin/node

// This script prints the factorial of n

function factorial(n){
  if (n === 0 || isNaN(n)) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
}

console.log(factorial(Number(process.argv[2])));
