#!/usr/bin/node
const id = process.argv[2];
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request(url, function (err, resp, body) {
  if (err) { console.log(err); } else {
    const allCharacters = JSON.parse(body).characters;
    myPrint(allCharacters, 0);
  }
});
function myPrint (allCharacters, count) {
  request(allCharacters[count], function (err, resp, body) {
    const length = allCharacters.length;
    if (err) { console.log(err); } else {
      console.log(JSON.parse(body).name);
      if (count + 1 < length) {
        myPrint(allCharacters, count + 1);
      }
    }
  });
}
