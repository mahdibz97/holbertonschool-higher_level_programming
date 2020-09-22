#!/usr/bin/node
const array = require('./100-data.js').list;
console.log(array);
const newarray = array.map((x, y) => x * y);
console.log(newarray);
