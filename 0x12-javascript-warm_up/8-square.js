#!/usr/bin/node
if (Number.parseInt(process.argv[2])) {
  const x = Number.parseInt(process.argv[2]);
  for (let i = 0; i < x; i++) {
    let square = '';
    for (let j = 0; j < x; j++) { square += 'X'; }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
