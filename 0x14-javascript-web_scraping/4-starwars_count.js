#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  else {
    let i = 0;
    const result = JSON.parse(body).results;
    for (const movie of result) {
      for (const wedge of movie.characters) {
        if (wedge.endsWith('18/')) {
          i++;
        }
      }
    }
    console.log(i);
  }
});
