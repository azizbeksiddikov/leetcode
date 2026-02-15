// Link: https://leetcode.com/problems/counter/

/**
 * @param {number} n
 * @return {Function} counter
 */
const createCounter = function (n) {
  return function () {
    return n++;
  };
};
