#!/usr/bin/node

const request = require('request');
const arg = process.argv.slice(2);
const url = arg[0];
request.get(url, (response) => {
  console.log(`code: ${response.statusCode}`);
});
