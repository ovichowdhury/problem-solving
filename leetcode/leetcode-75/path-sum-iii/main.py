# https://leetcode.com/problems/path-sum-iii/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        from collections import defaultdict
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        path_count = 0

        def dfs(node: TreeNode | None, curr_sum: int):
            nonlocal path_count
            nonlocal prefix_count
            if not node:
                return
            
            curr_sum += node.val
            if prefix_count[curr_sum - target_sum] > 0:
                path_count = path_count + prefix_count[curr_sum - target_sum]
            
            prefix_count[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            prefix_count[curr_sum] -= 1
        dfs(root, 0)
        return path_count



# Example usage:
# Construct the binary tree [10,5,-3,3,2,None,11,3,-2,None,1]
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1) 
solution = Solution()
print(solution.pathSum(root, 8))  # Output 3