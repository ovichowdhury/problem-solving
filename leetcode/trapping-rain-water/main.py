# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0

        while left < right:
            if height[left] < height[right]:
                # Process Left
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                # Process Right
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1

        return water_trapped





# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    heights1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result1 = solution.trap(heights1)
    print(f"Example 1: {heights1}")
    print(f"Water trapped: {result1}\n")
    
    # Example 2
    heights2 = [4, 2, 0, 3, 2, 5]
    result2 = solution.trap(heights2)
    print(f"Example 2: {heights2}")
    print(f"Water trapped: {result2}\n")
    
    # Example 3
    heights3 = [9, 8, 9]
    result3 = solution.trap(heights3)
    print(f"Example 3: {heights3}")
    print(f"Water trapped: {result3}\n")
    
    # Example 4
    heights4 = [1, 0, 2]
    result4 = solution.trap(heights4)
    print(f"Example 4: {heights4}")
    print(f"Water trapped: {result4}\n")

