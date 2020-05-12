#!/usr/bin/node
/* Get number of times character 17 (Wedge Antilles) appear in Star
Wars movie, throught the use of Swapi, a star wars information api */
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonedUrl = JSON.parse(body);
    let count = 0; /* Number of times we have character # 17 */
    for (let movie = 0; movie < jsonedUrl.count - 1; movie++) {
      if (jsonedUrl.results[movie].characters[18]) {
        count += 1;
      }
    }
    console.log(count);
  }
});
