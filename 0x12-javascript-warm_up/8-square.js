#!/usr/bin/node

const num = process.argv[2];
const inte = parseInt(num);
if (!num || isNaN(inte)) {
  console.log('Missing size');
} else if (inte > 0) {
  for (let i = 0; i < inte; i++) {
    let row = '';
    for (let j = 0; j < inte; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
