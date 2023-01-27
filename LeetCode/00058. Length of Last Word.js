/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
  /* Split, filter to remove empty string items from splitted list then get the length of last word
  */
  return s.split(" ").filter( e => e.trim().length > 0).slice(-1)[0].length
};
