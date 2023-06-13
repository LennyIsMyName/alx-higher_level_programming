#!/usr/bin/node

const occu = process.argv[2];

if (!occu) {
  console.log('Missing number of occurrenses');
} else if (!isNaN(occu) || occu >= 1) {
  const inte = parseInt(occu);
  for (let i = 0; i < inte; i++) {
    console.log('C is fun');
  }
}
