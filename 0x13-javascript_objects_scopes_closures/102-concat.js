#!/usr/bin/node
const { dict } = require('./101-data');

const sortedDict = {};

for (const key in dict) {
  const value = dict[key];
  if (!(value in sortedDict)) {
    sortedDict[value] = [];
  }
  sortedDict[value].push(key);
}

console.log(sortedDict);
