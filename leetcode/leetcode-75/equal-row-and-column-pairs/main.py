# https://leetcode.com/problems/equal-row-and-column-pairs/?envType=study-plan-v2&envId=leetcode-75

from collections import Counter
from typing import List

# Time Complexity: O(n^3) Space Complexity: O(n)
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(n):
                if grid[i] == [grid[k][j] for k in range(n)]:
                    count += 1
        return count

# Time Complexity: O(n^2) Space Complexity: O(n^2)
class Solution2:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        hash_map = {}
        for i in range(n):
            row = tuple(grid[i])
            hash_map[row] = hash_map.get(row, 0) + 1

        count = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += hash_map.get(col, 0)

        return count

class Solution3:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hm = Counter(map(tuple, grid))
        return sum(hm[col] for col in zip(*grid))

# Example usage
if __name__ == "__main__":
    sol = Solution3()
    grid1 = [
        [3,2,1],
        [1,7,6],
        [2,7,7]
    ]
    print(sol.equalPairs(grid1))  # Expected output: 1

    grid2 = [
        [3,1,2,2],
        [1,4,4,5],
        [2,4,2,2],
        [2,4,2,2]
    ]
    print(sol.equalPairs(grid2))  # Expected output: 3
