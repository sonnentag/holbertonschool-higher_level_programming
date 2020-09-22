#!/usr/bin/node
const filename = process.argv[2];
const fs = require('fs');
fs.readFile(filename, 'utf8', (err, data) => {
  if (err) return console.error(err);
  console.log(data);
});
