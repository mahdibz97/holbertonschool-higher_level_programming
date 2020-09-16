#!/usr/bin/node
function factorialize (num) {
  if (num === 0 || num === 1 || (isNaN(process.argv[2]))){ 
      return 1; 
    }else{
      return num * factorialize(numb-1)
  }
}
console.log(factorialize(process.argv[2]));
