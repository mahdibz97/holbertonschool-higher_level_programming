#!/usr/bin/node
function factorialize (num) {
  if (num === 0 || num === 1 || (isNaN(process.argv[2])))
    return 1;
  for (let i = num - 1; i >= 1; i--) {
    num *= i;
  }
  return num;
}
console.log(factorialize(process.argv[2]));
