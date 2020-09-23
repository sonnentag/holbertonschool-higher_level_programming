#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];
request(url, function (err, request, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filename, body, err => {
      if (err) console.log(err);
    });
  }
});
