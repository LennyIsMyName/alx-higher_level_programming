#!/usr/bin/js

const len = process.argv.length;
const args = process.argv;

function bubbleSort (Args) {
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (Args[j] > Args[j + 1]) {
        const tmp = Args[j];
        Args[j] = Args[j + 1];
        Args[j + 1] = tmp;
      }
    }
  }
}

bubbleSort(args);
if (len <= 3) {
  console.log(0);
} else {
  console.log(args[len - 2]);
}
