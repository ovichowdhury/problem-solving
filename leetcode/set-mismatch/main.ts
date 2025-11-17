// https://leetcode.com/problems/set-mismatch/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii

function findErrorNums(nums: number[]): number[] {
  const hist: Record<number, number> = {};
  for (let i = 0; i < nums.length; i++) {
    if (!(nums[i] in hist)) {
      hist[nums[i]] = 1;
    } else {
      const actualSum = (nums.length * (nums.length + 1)) / 2;
      const currentSum = nums.reduce((a, b) => a + b, 0);
      const missing = actualSum + nums[i] - currentSum;
      return [nums[i], missing];
    }
  }

  return [];
}

// Example usage
console.log(findErrorNums([1, 2, 2, 4])); // Expected Output: [2,3]
console.log(findErrorNums([1, 1])); // Expected Output: [1,2]
console.log(findErrorNums([2, 2])); // Expected Output: [2,1]
