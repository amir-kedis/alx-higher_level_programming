#!/usr/bin/node

const args = process.argv;

if (args[2] === undefined) {
  console.log('Not a number');
} else {
  const num = parseInt(args[2]);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${num}`);
  }
}
