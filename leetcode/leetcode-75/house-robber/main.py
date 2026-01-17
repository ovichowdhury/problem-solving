# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # print(dp)
        return dp[-1]
        


# Example usage:
sol = Solution()
print(sol.rob([1, 2, 3, 1]))  # Output: 4
# Another example:
print(sol.rob([2, 7, 9, 3, 1]))  # Output: 12

# Edge case:
print(sol.rob([2, 1, 1, 2]))  # Output: 4