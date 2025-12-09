# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0
        i, j = 0, 1
        water = 0

        while j < len(height):
            # i is zero height
            if height[i] == 0:
                i += 1
                j = i + 1
                continue

            # detect rectangle
            if height[j] >= height[i] and j - i > 1:
                w, h = (j - i) - 1, height[i]
                area = w * h
                trapped_water = area - sum(height[i+1:j])
                water += trapped_water
                i = j
                j = i + 1
                continue
            j += 1

        return water





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
    
    # # Example 3
    # heights3 = [9, 8, 9]
    # result3 = solution.trap(heights3)
    # print(f"Example 3: {heights3}")
    # print(f"Water trapped: {result3}\n")
    
    # # Example 4
    # heights4 = [1, 0, 2]
    # result4 = solution.trap(heights4)
    # print(f"Example 4: {heights4}")
    # print(f"Water trapped: {result4}\n")

