#!/usr/bin/node
exports.esrever = function (list) {
  const myList = [];
  let i = 0;
  for (let x = list.length - 1; x >= 0; x--) {
    myList[i] = list[x];
    i += 1;
  }
  return myList;
};
