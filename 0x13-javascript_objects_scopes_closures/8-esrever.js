#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  let element;
  for (let i = list.length - 1; i >= 0; i--) {
    element = list[i];
    newlist.push(element);
  }
  return newlist;
};
