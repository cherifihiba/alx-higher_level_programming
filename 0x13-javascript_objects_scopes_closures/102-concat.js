#!/usr/bin/node

const fs = require('fs');
const { promisify } = require('util');

const readFile = promisify(fs.readFile);
const appendFile = promisify(fs.appendFile);

async function concatFiles(source1, source2, destination) {
  try {
    const data1 = await readFile(source1, 'utf8');
    const data2 = await readFile(source2, 'utf8');
    await appendFile(destination, data1 + data2);
    console.log('Files concatenated successfully!');
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

if (process.argv.length !== 5) {
  console.error('Usage: ./concat_files.js <source1> <source2> <destination>');
  process.exit(1);
}

const [, , source1, source2, destination] = process.argv;
concatFiles(source1, source2, destination);
