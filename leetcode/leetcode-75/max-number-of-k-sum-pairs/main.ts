// https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

// Brute force approach Time Complexity: O(n^2)
// Space Complexity: O(1) for the brute force approach
function maxOperationsBruteForce(nums: number[], k: number): number {
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    for (let j = nums.length - 1; j > i; j--) {
      if (nums[i] + nums[j] === k && nums[i] !== -1 && nums[j] !== -1) {
        nums[i] = -1; // Mark as used
        nums[j] = -1; // Mark as used
        count++;
        break; // Move to the next i
      }
    }
  }
  return count;
}

// Two-pointer approach Time Complexity: O(n log n) for sorting, O(n) for the two-pointer traversal
// Space Complexity: O(1) for the two-pointer approach
function maxOperationsTwoPointer(nums: number[], k: number): number {
  nums.sort((a, b) => a - b);
  let count = 0;
  let left = 0;
  let right = nums.length - 1;
  while (left < right) {
    const sum = nums[left] + nums[right];
    if (sum === k) {
      count++;
      left++;
      right--;
    } else if (sum < k) {
      left++;
    } else {
      right--;
    }
  }
  return count;
}

// Hash map approach Time Complexity: O(n)
// Space Complexity: O(n) for the hash map
function maxOperations(nums: number[], k: number): number {
  const countMap: { [key: number]: number } = {};
  let count = 0;
  for (const num of nums) {
    const complement = k - num;
    if (countMap[complement] > 0) {
      count++;
      countMap[complement]--;
    } else countMap[num] = (countMap[num] || 0) + 1;
  }
  return count;
}

// Example usage:
// const nums = [1, 2, 3, 4];
// const k = 5;
// console.log(maxOperationsBruteForce(nums, k)); // Output: 2

// const nums2 = [3, 1, 3, 4, 3];
// const k2 = 6;
// console.log(maxOperationsBruteForce(nums2, k2)); // Output: 1

const nums = [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4];
const k = 2;
console.log(maxOperations(nums, k));
