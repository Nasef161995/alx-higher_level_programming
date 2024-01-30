#!/usr/bin/node

const request = require('request');
const num = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + num, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const resJSON = JSON.parse(body);
    console.log(resJSON.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
