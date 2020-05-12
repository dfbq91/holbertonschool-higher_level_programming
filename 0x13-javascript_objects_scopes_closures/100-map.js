#!/usr/bin/node
const myList = require('./100-data').list;
const product = myList.map(function (element, index) {
  return element * index;
});
console.log(myList);
console.log(product);
