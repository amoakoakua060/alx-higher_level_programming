#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  if (response.statusCode !== 200) {
    console.log('Code: ' + response.statusCode);
    return;
  }

  const res = {};
  const todos = JSON.parse(body);
  for (const i in todos) {
    const todo = todos[i];
    if (todo.completed) {
      if (todo.userId in res) {
        res[todo.userId]++;
      } else {
        res[todo.userId] = 1;
      }
    }
  }
  console.log(res);
});
