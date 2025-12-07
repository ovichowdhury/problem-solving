# https://leetcode.com/problems/koko-eating-bananas/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def canFinish(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k
            if hours <= h:
                return True
            else:
                return False
        
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid # speed is ok but can be further optimized
            else:
                left = mid + 1 # speed is not enough need to increase the speed
        return left

# Example usage:
sol = Solution()
print(sol.minEatingSpeed([3,6,7,11], 8))  # Output: 4

# Example usage:
sol = Solution()
print(sol.minEatingSpeed([30,11,23,4,20], 5))  # Output: 30