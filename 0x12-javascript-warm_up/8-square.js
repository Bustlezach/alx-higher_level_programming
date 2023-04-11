#!/usr/bin/node 

// This script prints square 

const x = Math.floor(Number(process.argv[2]));
if(isNaN(x) || process.argv[2] === 'undefined'){
        console.log('Missing size');
} else {
        for(let i = 0; i < x; i++){
                console.log('x'.repeat(x));
        }
}
