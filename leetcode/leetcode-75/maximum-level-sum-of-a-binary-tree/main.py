# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level = 1
        max_sum = float('-inf')

        def bfs(node: TreeNode) -> None:
            nonlocal max_level, max_sum
            if not node:
                return

            queue = deque([node])
            level = 1

            while queue:
                level_size = len(queue)
                current_level_sum = 0

                for _ in range(level_size):
                    n = queue.popleft()
                    current_level_sum += n.val

                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
                
                if current_level_sum > max_sum:
                    max_sum = current_level_sum
                    max_level = level
                level += 1

        bfs(root)
        return max_level
                

if __name__ == "__main__":
    # Build the tree:
    #       1
    #      / \
    #     7   0
    #    / \
    #   7  -8
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)

    # Example: call Solution().maxLevelSum(root)
    solution = Solution()
    result = solution.maxLevelSum(root)
    print(f"Maximum level sum is at level: {result}")

    # Another example tree: [1,1,0,7,-8,-7,9]
    #       1
    #      / \
    #     1   0
    #    / \ / \
    #   7 -8 -7 9
    root2 = TreeNode(1)
    root2.left = TreeNode(1)
    root2.right = TreeNode(0)
    root2.left.left = TreeNode(7)
    root2.left.right = TreeNode(-8)
    root2.right.left = TreeNode(-7)
    root2.right.right = TreeNode(9)

    result2 = solution.maxLevelSum(root2)
    print(f"Maximum level sum (example 2) is at level: {result2}")
    