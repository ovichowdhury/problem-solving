# https://leetcode.com/problems/3sum-closest/description/

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
      nums.sort()
      closest_sum = float('inf')

      for i, a in enumerate(nums):
         l, r = i + 1, len(nums) - 1

         while l < r:
            three_sum = a + nums[l] + nums[r]
            if abs(three_sum - target) < abs(closest_sum - target):
               closest_sum = three_sum

            if three_sum > target:
              r -= 1
            elif three_sum < target:
              l += 1
            else:
               return three_sum

      return closest_sum
    
# Example usage:
s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1)) # Expected output: 2

print(s.threeSumClosest([0, 0, 0], 1)) # Expected output: 0