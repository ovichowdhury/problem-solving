// Problem: https://leetcode.com/problems/target-sum/

var findTargetSumWays = function (nums, target) {
  const cache = {};
  const backtract = (index, total) => {
    if (index === nums.length) return total === target ? 1 : 0;
    if (cache[`${index}:${total}`] !== undefined) {
      return cache[`${index}:${total}`];
    }

    cache[`${index}:${total}`] =
      backtract(index + 1, total + nums[index]) +
      backtract(index + 1, total - nums[index]);
    console.log(`${index}:${total}`);
    return cache[`${index}:${total}`];
  };
  return backtract(0, 0);
};

console.log(
  findTargetSumWays(
    [
      2, 107, 109, 113, 127, 131, 137, 3, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
      47, 53,
    ],
    899
  )
);
