#!/usr/bin/node

const fs = require('fs');
const pathfile = process.argv[2];
const content = process.argv[3];

fs.writeFile(pathfile, content, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
