#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const myNum = parseInt(process.argv[2]);
const myNum2 = parseInt(process.argv[3]);
const result = add(myNum, myNum2);
console.log(result);
