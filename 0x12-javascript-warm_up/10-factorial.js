#!/usr/bin/node
function factorial (a) {
  if (a <= 1 || isNaN(a)) {
    return 1;
  }
  return a * factorial(a - 1)
}
const myNum = parseInt(process.argv[2]);
const result = factorial(myNum);
console.log(result);
