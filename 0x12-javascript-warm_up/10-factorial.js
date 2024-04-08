#!/usr/bin/node

const args = process.argv;

function factorial(n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

if (args[2] === undefined) {
  console.log("1");
} else {
  console.log(factorial(parseInt(args[2])));
}
