# Subset Sum Problem: Determine if there's a subset of a given set with a sum equal to a given target.
# Example: Given a set [3, 34, 4, 12, 5, 2] and a target sum of 9, the subset [4, 5] sums to 9.

from typing import List


def subset_sum(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i - num]
    
    return dp[target]

# Example Usage
nums = [2, 3, 5]
target = 7
result = subset_sum(nums, target)
print(result)