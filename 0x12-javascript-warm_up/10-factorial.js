#!/usr/bin/node
function factorialize (numb) {
  if (numb === 0 || numb === 1 || (isNaN(process.argv[2]))){ 
      return 1; 
    }else{
      return numb * factorialize(numb-1)
  }
}
console.log(factorialize(process.argv[2]));
