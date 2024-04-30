#!/usr/bin/node
'use strict';

const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

try {
  const data1 = fs.readFileSync(sourceFile1, 'utf8');
  const data2 = fs.readFileSync(sourceFile2, 'utf8');
  
  fs.writeFileSync(destinationFile, data1 + data2);
  
  console.log(`The content of ${sourceFile1} and ${sourceFile2} has been concatenated and written to ${destinationFile}`);
} catch (error) {
  console.error(error.message);
}
