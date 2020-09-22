#!/usr/bin/node
const content = process.argv[3];
const filename = process.argv[2];
const fs = require('fs');
fs.writeFile(filename, content, err => {
  if (err) console.error(err);
});
