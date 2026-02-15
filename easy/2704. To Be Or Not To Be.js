// Link: https://leetcode.com/problems/to-be-or-not-to-be/description/

/**
 * @param {string} val
 * @return {Object}
 */
var expect = function (val) {
  return {
    toBe(val_2) {
      if (val === val_2) return true;
      else throw new Error('Not Equal');
    },
    notToBe(val_2) {
      if (val !== val_2) return true;
      else throw new Error('Equal');
    },
  };
};
