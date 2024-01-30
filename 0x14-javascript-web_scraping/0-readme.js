#!/usr/bin/node
const fs = require('fs');

const pathfile = process.argv[2];
fs.readFile(pathfile, 'utf8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});
