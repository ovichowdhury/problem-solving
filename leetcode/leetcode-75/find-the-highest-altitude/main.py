# https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = gain[0]
        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]
            if gain[i] > max:
                max = gain[i]
        return max if max > 0 else 0
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestAltitude([-5, 1, 5, 0, -7]))  # Output: 1
    print(solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))  # Output: 0
    print(solution.largestAltitude([-5, 1, 5, 0, -7, 3, 2]))  # Output: 1
    print(solution.largestAltitude([1, 2, 3, 4, 5]))  # Output: 15
    print(solution.largestAltitude([-1, -2, -3, -4, -5]))  # Output: 0
    print(solution.largestAltitude([0, 0, 0, 0, 0]))  # Output: 0
    print(solution.largestAltitude([52,-91,72]))  # Output: 52