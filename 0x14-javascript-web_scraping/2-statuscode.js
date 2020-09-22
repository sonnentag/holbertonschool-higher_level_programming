#!/usr/bin/node
const request = require('request');
const opts = {
  method: 'GET',
  url: process.argv[2]
};
request(opts, (err, res) => {
  if (err) return console.error(err);
  console.log('code: %d', res.statusCode);
});
