# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75

from collections import defaultdict
from typing import Dict, List, Set


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        adj_list = defaultdict(list)

        for u, v in connections:
            adj_list[u].append((v, 1))
            adj_list[v].append((u, 0))
        
        def dfs(node: int, visited_node: Set, adj: Dict) -> int:
            visited_node.add(node)
            reverse_needed = 0
            for neighbor, cost in adj[node]:
                if neighbor not in visited_node:
                    reverse_needed += cost
                    reverse_needed += dfs(neighbor, visited_node, adj)
            return reverse_needed

        return dfs(0, visited, adj_list)

# Example Usage
sol = Solution()
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
result = sol.minReorder(n, connections)
print(result) # Expected output: 3