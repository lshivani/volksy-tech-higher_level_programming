#!/usr/bin/node
if(isNaN(parseInt(process.argv[2], 10))) {
  console.log('Not a number');
} else {
  console.log(parseInt(process.argv[2], 10));
}
