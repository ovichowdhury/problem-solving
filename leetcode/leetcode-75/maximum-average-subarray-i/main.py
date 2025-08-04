# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k
        max_sum = sum(nums[:k])
        while j <= len(nums):
            current_sum = sum(nums[i:j])
            if current_sum > max_sum:
                max_sum = current_sum
            i += 1
            j += 1
        return max_sum / k
    
class SolutionOptimized:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k

sol = SolutionOptimized()
# Example usage:
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))  # Output: 12.75
print(sol.findMaxAverage([5], 1))  # Output: 5.0
print(sol.findMaxAverage([1,2,3,4,5], 1))  # Output: 5.0