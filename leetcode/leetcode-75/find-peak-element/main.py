# https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        if left == right:
            return left
        else:
            return -1

# Example usage:
solution = Solution()
nums = [1, 2, 1, 3, 5, 6, 4]
result = solution.findPeakElement(nums)
print(result)  # Expected output: Index of a peak element, e.g., 1

# Example usage:
solution = Solution()
nums = [1, 2, 3, 1]
result = solution.findPeakElement(nums)
print(result)  # Expected output: Index of a peak element, e.g., 2

# Example usage: edge case with single element
solution = Solution()
nums = [1]
result = solution.findPeakElement(nums)
print(result)  # Expected output: 0