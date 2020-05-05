#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
}
process.argv.sort(function(a, b) {
  return a - b;
})
console.log(process.argv[process.argv.length - 2])
