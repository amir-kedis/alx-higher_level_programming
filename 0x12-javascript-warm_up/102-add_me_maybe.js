#!/usr/bin/node

function addMeMaybe (n, theFunction) {
  theFunction(n + 1);
}

module.exports = {
  addMeMaybe
};
