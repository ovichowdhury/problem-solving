# https://leetcode.com/problems/unique-paths-iii/

from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        empty_count = 0
        start_x, start_y = 0, 0

        # Count empty squares and find the starting point
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    empty_count += 1
                elif grid[i][j] == 1:
                    start_x, start_y = i, j 


        # total steps need to be taked 
        total_steps = empty_count + 1
        paths_count = 0


        def dfs(x, y, steps_count):

            nonlocal paths_count
            
            # exit condition
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == -1:
                return
            
            # success condition
            if grid[x][y] == 2:
                if steps_count == total_steps:
                    paths_count += 1
                return

            temp = grid[x][y]
            grid[x][y] = -1

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy, steps_count + 1)
            
            grid[x][y] = temp

        dfs(start_x, start_y, 0)
        return paths_count
    


grid = [
  [1,0,0,0],
  [0,0,0,0],
  [0,0,2,-1]
]
sol = Solution()
print(sol.uniquePathsIII(grid))  # Output: 2