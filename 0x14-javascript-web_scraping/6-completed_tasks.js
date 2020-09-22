#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  else if (response.statusCode === 200) {
    const done = {};
    for (const i in JSON.parse(body)) {
      const tasks = JSON.parse(body)[i];
      if (tasks.completed === true) {
        if (done[tasks.userId] === undefined) {
          done[tasks.userId] = 1;
        } else done[tasks.userId]++;
      }
    }
    console.log(done);
  }
});
