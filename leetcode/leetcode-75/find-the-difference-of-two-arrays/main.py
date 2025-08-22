# https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]

# Example usage
sol = Solution()
print(sol.findDifference([1, 2, 3], [2, 4, 6]))  # Output: [[1, 3], [4, 6]]