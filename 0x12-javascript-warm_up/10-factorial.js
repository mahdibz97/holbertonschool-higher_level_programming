#!/usr/bin/node
function factorialize (numb) {
  if (numb === 0 || numb === 1 || (isNaN(process.argv[2])))
    return 1;
  for (let i = numb - 1; i >= 1; i--) {
    numb *= i;
  }
  return numb;
}
console.log(factorialize(process.argv[2]));
