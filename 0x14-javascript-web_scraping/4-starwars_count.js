#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('Error code: ' + response.statusCode);
    return;
  }

  console.log(JSON.parse(body).results.reduce((count, res) => {
    return count + (res.characters.find(c => c.endsWith('/18/')) ? 1 : 0);
  }, 0));
});
