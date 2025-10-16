# https://leetcode.com/problems/keys-and-rooms/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited: List[bool] = [False] * len(rooms)
        queue = deque([0])

        while queue:
            node = queue.popleft()
            if not visited[node]:
                next_nodes = rooms[node]
                for n in next_nodes:
                    queue.append(n)
                visited[node] = True
        return all(visited)

        


# Example usage:
sol = Solution()
print(sol.canVisitAllRooms([[1],[2],[3],[]]))  # Output: True
print(sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))  # Output: False