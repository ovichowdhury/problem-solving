# https://leetcode.com/problems/rotting-oranges/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh_count = 0
        minutes = 0
        rotten = deque([])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))
        
        while rotten and fresh_count > 0:
            minutes += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # right, left, down, up
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        rotten.append((nr, nc))
        return minutes if fresh_count == 0 else -1

# Example Usage
if __name__ == "__main__":
    grid = [[2,1,1],
            [1,1,0],
            [0,1,1]]

    sol = Solution()
    result = sol.orangesRotting(grid)
    print(result)  # Expected output: 4

    # Another test case
    grid = [[2,1,1],
            [0,1,1],
            [1,0,1]]
    result = sol.orangesRotting(grid)
    print(result)  # Expected output: -1