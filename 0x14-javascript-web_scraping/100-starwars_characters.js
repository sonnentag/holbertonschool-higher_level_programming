#!/usr/bin/node
const id = process.argv[2];
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request(url, function (err, resp, body) {
  if (err) { console.log(err); } else {
    const allCharacters = JSON.parse(body).characters;
    allCharacters.map(arg => request(arg, function (err, resp, body) {
      if (err) { console.log(err); } else {
        console.log(JSON.parse(body).name);
      }
    }));
  }
});
