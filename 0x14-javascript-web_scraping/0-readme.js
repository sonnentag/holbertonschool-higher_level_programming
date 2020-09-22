#!/usr/bin/node
const filename = process.argv[2];
const fs = require('fs');

fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
