# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good_count = 0

        def dfs_preorder(node: TreeNode, prev_value_stack: List[int]):
            nonlocal good_count
            prev_value_stack.append(node.val)

            if node.val >= max(prev_value_stack):
                good_count += 1
            
            if node.left:
                dfs_preorder(node.left, prev_value_stack)

            if node.right:
                dfs_preorder(node.right, prev_value_stack)

            prev_value_stack.pop()
        
        dfs_preorder(root, [])

        return good_count
            

# Example usage:
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
solution = Solution()
print(solution.goodNodes(root))  # Output: 4

# Example usage for tree: [9, None, 3, 6]
root2 = TreeNode(9)
root2.right = TreeNode(3)
root2.right.left = TreeNode(6)
print(solution.goodNodes(root2))  # Output should match the number of good nodes for this tree