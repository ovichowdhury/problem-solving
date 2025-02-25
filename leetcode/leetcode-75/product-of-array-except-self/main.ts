// Problem: https://leetcode.com/problems/product-of-array-except-self/

function productExceptSelf(nums: number[]): number[] {
  const prefix: number[] = [];
  const postfix: number[] = [];
  const result: number[] = [];
  for (let i = 0; i < nums.length; i++) {
    if (i === 0) prefix[i] = nums[i];
    else prefix[i] = nums[i] * prefix[i - 1];
  }

  for (let i = nums.length - 1; i >= 0; i--) {
    if (i === nums.length - 1) postfix[i] = nums[i];
    else postfix[i] = nums[i] * postfix[i + 1];
  }

  for (let i = 0; i < nums.length; i++) {
    const pre = prefix[i - 1] ?? 1;
    const post = postfix[i + 1] ?? 1;
    result[i] = pre * post;
  }
  return result;
}

console.log(productExceptSelf([-1, 1, 0, -3, 3]));
