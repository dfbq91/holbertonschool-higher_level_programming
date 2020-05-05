#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
if (isNaN(myNum)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < process.argv[2]; j++) {
    console.log('X'.repeat(myNum));
  }
}
