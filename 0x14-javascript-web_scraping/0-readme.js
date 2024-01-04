#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (error, body) {
  if (error) {
    console.log(error);
    return;
  }
  console.log(body);
);
