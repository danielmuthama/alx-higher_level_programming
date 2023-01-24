#!/usr/bin/node
<<<<<<< HEAD

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
	};
=======
exports.converter = function (base) {
  function convert (number) {
    return number.toString(base);
  }
  return convert;
>>>>>>> 195949af5f2fd8f529bca1448ae08731cc6e2a99
};
