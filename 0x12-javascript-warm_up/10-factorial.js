#!/usr/bin/node

const num = parseInt(process.argv[2]) || 1;

const factorial = (n) => {
  if (n === 0) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
};

console.log(factorial(num).toString());
