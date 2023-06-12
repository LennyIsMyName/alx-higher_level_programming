#!/usr/bin/node

const pars = process.argv[2];

if (isNaN(pars)) {
  console.log('Not a number');
} else {
  const ans = Math.trunc(pars);
  console.log(`My number: ${ans}`);
}
