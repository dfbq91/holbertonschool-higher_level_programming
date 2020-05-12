#!/usr/bin/node
/* Get number of times character 17 (Wedge Antilles) appear in Star
Wars movie, throught the use of Swapi, a star wars information api */
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, 'utf-8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
