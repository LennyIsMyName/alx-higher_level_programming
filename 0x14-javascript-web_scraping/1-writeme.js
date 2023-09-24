#!/usr/bin/node

const fs = require('fs');

const args = process.argv.slice(2);
const file = args[0];
const text = args[1];

fs.writeFile(file, text, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
