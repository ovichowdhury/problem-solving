# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        e_row, e_col = entrance
        visited = set((e_row, e_col))
        queue = deque([(e_row, e_col, 0)])  # (row, col, distance)

        def is_visit_possible(r, c):
            if r >= 0 and r < rows and c >= 0 and c < cols and maze[r][c] == '.':
                return True
            return False
        
        def is_exit_node(r, c):
            if r == e_row and c == e_col:
                return False
            if r == 0 or c == 0 or r + 1 == rows or c + 1 == cols:
                return True
            return False
            

        while queue:
            node_row, node_col, distance = queue.popleft()
            

            if is_exit_node(node_row, node_col):
                return distance

            right = (node_row, node_col + 1, distance + 1)
            left = (node_row, node_col - 1, distance + 1)
            up = (node_row - 1, node_col, distance + 1)
            down = (node_row + 1, node_col, distance + 1)

            for neighbor in [right, left, up, down]:
                r, c, d = neighbor
                if (r, c) not in visited and is_visit_possible(r, c):
                    visited.add((r, c))
                    queue.append(neighbor)
        
        return -1
       
    
# Example Usage
if __name__ == "__main__":
    maze = [["+", "+", ".", "+"],
            [".", ".", ".", "+"],
            ["+", "+", "+", "."]]
    entrance = [1, 2]

    sol = Solution()
    result = sol.nearestExit(maze, entrance)
    print(result)  # Expected: 1

    # Another test case
    maze = [["+", "+", "+"],
            [".", ".", "."],
            ["+", "+", "+"]]
    entrance = [1, 0]

    sol = Solution()
    result = sol.nearestExit(maze, entrance)
    print(result)  # Expected: 2

    # Another test case
    maze = [[".", "+"]]
    entrance = [0, 0]
    sol = Solution()
    result = sol.nearestExit(maze, entrance)
    print(result)  # Expected: -1
