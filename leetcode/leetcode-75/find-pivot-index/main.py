# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = []
        right_sum = []
        for i in range(len(nums)):
            if i == 0:
                left_sum.append(nums[i])
            else:
                left_sum.append(left_sum[i - 1] + nums[i])

        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                right_sum.append(nums[j])
            else:
                right_sum.insert(0, nums[j] + right_sum[0])

        for k in range(len(nums)):
            if left_sum[k] == right_sum[k]:
                return k
        return -1

# Example usage
sol = Solution()
print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))  # Output: 3
print(sol.pivotIndex([1, 2, 3]))  # Output: -1
print(sol.pivotIndex([2, 1, -1]))  # Output: 0
print(sol.pivotIndex([0, 0, 0, 0, 0]))  # Output: 0
print(sol.pivotIndex([-1, -1, -1, -1, -1]))  # Output: 2