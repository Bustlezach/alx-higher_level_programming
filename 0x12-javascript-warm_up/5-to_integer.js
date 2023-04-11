#!/usr/bin/node

// This script prints My number: <first argument converted in integer> 
//if the first argument can be converted to an integer

const val = Math.floor(Number(process.agrv[2]));
if (isNaN(val) === false){
        console.log(`My number: ${val}`);
} else{
        console.log(`Not a number`);
}
