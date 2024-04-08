#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  return a + b;
}

if (args[2] === undefined || args[3] === undefined) {
  console.log('NaN');
} else {
  console.log(add(parseInt(args[2]), parseInt(args[3])));
}
