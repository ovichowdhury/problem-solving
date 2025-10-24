# https://leetcode.com/problems/evaluate-division/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List, Set, Dict
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        output = [-1.0] * len(queries)
        adj = defaultdict(list)

        for i, (u, v) in enumerate(equations):
            adj[u].append((v, values[i]))
            adj[v].append((u, 1/values[i]))

        def dfs_find_cost(node: str, target: str, total_cost: float, visited: Set, adj_list: Dict):
            # if the node does not exist in the graph, no path is possible
            if node not in adj_list:
                return -1.0
            visited.add(node)
            if node == target:
                return total_cost

            for neighbor, cost in adj_list[node]:
                if neighbor not in visited:
                    # do not mutate total_cost so other branches aren't affected
                    res = dfs_find_cost(neighbor, target, total_cost * cost, visited, adj_list)
                    if res != -1.0:
                        return res
            return -1.0


        for j, (c, d) in enumerate(queries):
            visited = set()
            output[j] = dfs_find_cost(c, d, 1, visited, adj)
        

        return output
        
        

# Example Usage
if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    sol = Solution()
    result = sol.calcEquation(equations, values, queries)
    print(result)  # Expected: [6.0, 0.5, -1.0, 1.0, -1.0]