#!/usr/bin/node

const args = process.argv;

if (args[2] === undefined) {
  console.log(0);
}

if (args.length === 3) {
  console.log(0);
}

if (args.length > 3) {
  const array = args.slice(2).map(Number);
  const sortedArray = array.sort((a, b) => a - b);
  console.log(sortedArray[sortedArray.length - 2]);
}
