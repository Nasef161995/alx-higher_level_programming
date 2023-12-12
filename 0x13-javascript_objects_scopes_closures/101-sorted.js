#!/usr/bin/node
const dic = require('./101-data').dict;
const newdict = {};
for (const key in dic) {
  if (newdict[dic[key]] === undefined) {
    newdict[dic[key]] = [key];
  } else {
    newdict[dic[key]].push(key);
  }
}
console.log(newdict);
