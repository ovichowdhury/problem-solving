# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node: TreeNode | None):
            if node is None:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            
            if left:
                return left
            else:
                return right
                

        return dfs(root)

# Example Usage
# Example binary tree:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4
#         / \
#        9  10  
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.left.right.right.left = TreeNode(9)
root.left.right.right.right = TreeNode(10)

sol = Solution()
p = root.left  # Node with value 5
q = root.right  # Node with value 1
lca = sol.lowestCommonAncestor(root, p, q)
print(lca.val)  # Output: 3