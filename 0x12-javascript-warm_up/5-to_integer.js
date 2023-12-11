#!/usr/bin/node
if (Number.parseInt(process.argv[2])) {
  console.log(Number.parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
