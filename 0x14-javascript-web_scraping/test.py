#!/usr/bin/node



const request = require('request');



request.get('https://example.com', (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(response.statusCode);
  }
});
