#!/usr/bin/node
const fs = require('fs');

const [,, fileA, fileB, fileC] = process.argv;

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) throw err;
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) throw err;
    fs.writeFile(fileC, dataA.trim() + '\n' + dataB.trim() + '\n', (err) => {
      if (err) throw err;
    });
  });
});
