#!/usr/bin/node
'use strict';

const list = require('./100-data').list;

console.log(list);
console.log(list.map((value, index) => value * index));
