#!/usr/bin/node
const myArray = process.argv;
if (myArray.length === 2) { console.log('No argument'); } else if (myArray.length === 3) { console.log('Argument found'); } else { console.log('Arguments found'); }
