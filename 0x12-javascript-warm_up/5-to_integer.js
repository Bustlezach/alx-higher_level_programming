#!/usr/bin/node

// This script prints My number: <first argument converted in integer> 
//if the first argument can be converted to an integer

let vals = process.agrv;
vals = Math.floor(Number(vals[2]));
if (isNaN(vals) === false){
        console.log(`My number: ${vals[2]}`);
} else{
        console.log(`Not a number`);
}
