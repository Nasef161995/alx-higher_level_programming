#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const myArray = [];
  for (let i = 2; i < process.argv.length; i++) { myArray.push(Number(process.argv[i])); }
  myArray.sort((a, b) => b - a);
  console.log(myArray[1]);
}
