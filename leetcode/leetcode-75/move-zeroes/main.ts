// https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75

/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
  let lastNonZeroFoundAt = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      let temp = nums[lastNonZeroFoundAt];
      nums[lastNonZeroFoundAt++] = nums[i];
      nums[i] = temp;
    }
  }
}
let nums = [0, 1, 0, 3, 12];
moveZeroes(nums);
console.log(nums); // Output: [1, 3, 12, 0, 0]
