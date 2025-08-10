# https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=leetcode-75
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity: O(n), where n is the number of nodes in the tree.
    # Space Complexity: O(h), where h is the height of the tree (due to
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)
    
    # Time Complexity: O(n), where n is the number of nodes in the tree.
    # Space Complexity: O(n) in the worst case (if the tree is skewed), or O(w) where w is the maximum width of the tree (for a balanced tree).
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [root]
        depth = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
    

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
    print(solution.maxDepthBFS(root))  # Output: 3


    
