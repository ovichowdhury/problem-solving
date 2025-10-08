
# https://leetcode.com/problems/search-in-a-binary-search-tree/submissions/1795528910/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# Example usage:
# Constructing a simple BST:
#       4
#      / \
#     2   7
#    / \
#   1   3
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
solution = Solution()
result = solution.searchBST(root, 2)

print(result.val)  # Output: 2