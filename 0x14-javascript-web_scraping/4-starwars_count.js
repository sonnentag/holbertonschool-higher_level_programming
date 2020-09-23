#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let c = 0;
request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    for (const result of JSON.parse(body).results) {
      for (const character of result.characters) {
        if (character.includes('18')) c++;
      }
    }
    console.log(c);
  }
});
