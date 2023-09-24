#!/usr/bin/node

const https = require('https');
const arg = process.argv.slice(2);
const url = arg[0];
https.get(url, (response) => {
  console.log(`code: ${response.statusCode}`);
});
