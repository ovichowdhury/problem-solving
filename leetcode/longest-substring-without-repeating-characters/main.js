/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let max = 0;
  for (w = 0; w < s.length; w++) {
    const charMap = {};
    for (let i = w; i < s.length; i++) {
      if (charMap[s[i]] === undefined) charMap[s[i]] = 1;
      else break;
    }
    const numOfKeys = Object.keys(charMap).length;
    if (numOfKeys > max) max = numOfKeys;
  }

  return max;
};

console.log(lengthOfLongestSubstring(" "));
