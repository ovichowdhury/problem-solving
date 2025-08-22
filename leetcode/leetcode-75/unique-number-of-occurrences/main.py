# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hist = Counter(arr)
        has_duplicates = len(hist.values()) != len(set(hist.values())) 
        return not has_duplicates

# Example usage
sol = Solution()
print(sol.uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # Output: True