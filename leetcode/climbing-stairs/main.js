// Problem: https://leetcode.com/problems/climbing-stairs/

/**
 * @param {number} n
 * @return {number}
 */
// var climbStairs = function (n) {
//   let count = 0;
//   const recurse = (num) => {
//     if (num < 0) return;
//     if (num === 0) {
//       count += 1;
//       return;
//     }
//     recurse(num - 1);
//     recurse(num - 2);
//   };
//   recurse(n);
//   return count;
// };

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n, memo = {}) {
  if (n < 0) return 0;
  if (n === 0) return 1;
  if (memo[n] !== undefined) return memo[n];
  const val = climbStairs(n - 1, memo) + climbStairs(n - 2, memo);
  memo[n] = val;
  return val;
};

console.log(climbStairs(45));
