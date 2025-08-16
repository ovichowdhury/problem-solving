// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75

function longestSubarray(nums: number[]): number {
  let left = 0;
  let right = 0;
  let zeroCount = 0;
  let maxLength = 0;

  while (right < nums.length) {
    if (nums[right] === 0) {
      zeroCount++;
    }
    while (zeroCount > 1) {
      if (nums[left] === 0) {
        zeroCount--;
      }
      left++;
    }
    right++;

    maxLength = Math.max(maxLength, right - left - 1);
  }

  return maxLength;
}

// Example usage:
const nums = [1, 1, 0, 1];
console.log(longestSubarray(nums)); // Output: 3
const nums2 = [0, 1, 1, 1, 0, 1, 1, 0, 1];
console.log(longestSubarray(nums2)); // Output: 5
const nums3 = [1, 1, 1];
console.log(longestSubarray(nums3)); // Output: 2
const nums4 = [0, 0, 0];
console.log(longestSubarray(nums4)); // Output: 0
