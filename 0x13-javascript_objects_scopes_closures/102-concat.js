#!/usr/bin/node
'use strict';

const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(err.message);
    return;
  }
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(err.message);
      return;
    }
    fs.writeFile(destinationFile, data1 + data2, (err) => {
      if (err) {
        console.error(err.message);
        return;
      }
      console.log(`The content of ${sourceFile1} and ${sourceFile2} has been concatenated and written to ${destinationFile}`);
    });
  });
});
