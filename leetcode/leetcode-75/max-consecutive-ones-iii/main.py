# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_length = 0

        for right, num in enumerate(nums):
            if num == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
    
# Example usage:
solution = Solution()
print(solution.longestOnes([1,1,0,0,1,1,1,0,1], 2))  # Output: 7
print(solution.longestOnes([0,0,1,1,0,1,1,1, 0, 1], 3))  # Output: 9
print(solution.longestOnes([1,0,1,0,1,0,1], 1))  # Output: 3
print(solution.longestOnes([0,0,0,0,0], 2))  # Output: 2
print(solution.longestOnes([1,1,1,1,1], 0))  # Output: 5