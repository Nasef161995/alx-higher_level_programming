#!/usr/bin/node
const mylist = require('./100-data').list;
let i = 0;
const newlist = mylist.map((x) => x * i++);
console.log(mylist);
console.log(newlist);
