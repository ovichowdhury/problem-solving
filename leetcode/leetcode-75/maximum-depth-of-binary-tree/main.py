# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)
    

# Example usage:
if __name__ == "__main__":
    # Create a sample binary tree:
    #       1
    #      / \
    #     2   3
    #    /     \  
    #   4       5
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4))
    root.right = TreeNode(3, TreeNode(5))

    solution = Solution()
    print(solution.maxDepth(root))  # Output: 3

    # [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print(solution.maxDepth(root))  # Output: 3

    # [1,null,2]
    root = TreeNode(1, None, TreeNode(2))
    print(solution.maxDepth(root))  # Output: 2

    # []
    root = None
    print(solution.maxDepth(root))  # Output: 0

    # [0]
    root = TreeNode(0)
    print(solution.maxDepth(root))  # Output: 1

    # [1,2,3,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)
    print(solution.maxDepth(root))  # Output: 3


    
