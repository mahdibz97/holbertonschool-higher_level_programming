#!/usr/bin/node
function secondbiggest (array) {
  let big = 0; let secbig = 0;

  for (const value of array) {
    const nr = Number(value);

    if (nr > big) {
      [secbig, big] = [big, nr];
    } else if (nr < big && nr > secbig) {
      secbig = nr;
    }
  }

  return secbig;
}

const array = process.argv.slice(2);
console.log(secondbiggest(array));
