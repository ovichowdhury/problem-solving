# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()

        def search(arr: List[int], target: int, spell: int) -> int:
            low = 0
            high = len(arr) - 1
            result_index = -1

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] * spell >= target:
                    result_index = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return result_index

        for s in spells:
            index = search(potions, success, s)
            if index == -1:
                pairs.append(0)
            else:
                pairs.append(len(potions) - index)

        return pairs
    

# Example usage:
solution = Solution()
spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7
result = solution.successfulPairs(spells, potions, success)
print(result)  # Expected output: [4, 0, 3]