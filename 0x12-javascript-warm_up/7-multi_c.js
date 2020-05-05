#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
