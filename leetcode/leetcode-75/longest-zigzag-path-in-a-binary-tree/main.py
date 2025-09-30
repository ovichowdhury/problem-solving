# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def dfs(node: TreeNode | None, direction: int, length: int):
            if not node:
                return

            self.max = max(self.max, length)

            if direction == 0:
                dfs(node.right, 1, length + 1)
                dfs(node.left, 0, 1)
            else:
                dfs(node.left, 0, length + 1)
                dfs(node.right, 1, 1)

        dfs(root.left, 0, 1)
        dfs(root.right, 1, 1)

        return self.max



# Example Usage
# Example binary tree:
#         1
#        / \
#       2   3
#        \   \
#         4   5
#        /     \
#       6       7

root = TreeNode(1)
root.left = TreeNode(2, None, TreeNode(4, TreeNode(6)))
root.right = TreeNode(3, None, TreeNode(5, None, TreeNode(7)))

sol = Solution()
print(sol.longestZigZag(root))  # Output: (expected value based on your implementation)


# ...existing code...

root2 = TreeNode(1)
root2.right = TreeNode(1)
root2.right.left = TreeNode(1)
root2.right.right = TreeNode(1)
root2.right.left.right = TreeNode(1)
root2.right.left.right.left = TreeNode(1)
root2.right.left.right.left.right = TreeNode(1)

# Example usage:
sol = Solution()
print(sol.longestZigZag(root2))  # Output: (expected value based on your implementation)