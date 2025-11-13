# https://leetcode.com/problems/concatenation-of-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# Example usage:
sol = Solution()
result = sol.getConcatenation([1,2,3])
print(result)  # Expected output: [1,2,3,1,2,3]