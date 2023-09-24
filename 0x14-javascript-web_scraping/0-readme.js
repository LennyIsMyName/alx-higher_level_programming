#!/usr/bin/node

const fs = require('fs');
const arg = process.argv.slice(2);
const filepath = arg[0];

fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data);
});
