# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            max_area = max(max_area, current_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        

sol = Solution()
# Example usage:
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(sol.maxArea([1,1]))  # Output: 1
print(sol.maxArea([4,3,2,1,4]))  # Output: 16
print(sol.maxArea([1,2,1]))  # Output: 2