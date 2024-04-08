#!/usr/bin/node

const args = process.argv;

if (args[2] === undefined) {
  console.log('Missing size');
} else {
  const size = parseInt(args[2]);
  if (isNaN(size)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < size; i++) {
      console.log('X'.repeat(size));
    }
  }
}
