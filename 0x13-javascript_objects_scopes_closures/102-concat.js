#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <source1> <source2> <destination>');
  process.exit(1);
}

const [, , source1, source2, destination] = process.argv;

const data1 = fs.readFileSync(source1, 'utf8');
const data2 = fs.readFileSync(source2, 'utf8');

fs.writeFileSync(destination, data1 + data2);

console.log('Files concatenated successfully!');
