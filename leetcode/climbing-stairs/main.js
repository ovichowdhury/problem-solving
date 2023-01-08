// Problem: https://leetcode.com/problems/climbing-stairs/

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  let count = 0;
  const recurse = (num) => {
    if (num < 0) return;
    if (num === 0) {
      count += 1;
      return;
    }
    recurse(num - 1);
    recurse(num - 2);
  };
  recurse(n);
  return count;
};

console.log(climbStairs(10));
