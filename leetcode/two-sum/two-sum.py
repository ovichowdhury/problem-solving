# Problem: https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, n in enumerate(nums):
            diff = target - n
            try:
                j = memo[diff]
                return [j, i]
            except:
                memo[n] = i


s = Solution()

print(s.twoSum([2, 7, 11, 15], 9))
