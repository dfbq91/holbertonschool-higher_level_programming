#!/usr/bin/node
/* Get number of tasks completed by each user id */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dict = {};
    const jsonedUrl = JSON.parse(body);
    let id = 1;
    for (const task of jsonedUrl) {
      if (task.userId === id && task.completed === true) {
        dict[task.userId] += 1;
      } else if (task.completed === true) {
        id += 1;
        dict[id] += 1;
      }
    }
    console.log(dict);
  }
});
