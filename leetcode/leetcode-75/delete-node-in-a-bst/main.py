# https://leetcode.com/problems/delete-node-in-a-bst/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Search the node to delete
        if key < root.val:
            # key is smaller go left (BST)
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # key is greater go right (BST)
            root.right = self.deleteNode(root.right, key)
        
        # match found in the current node
        else:
            # node with single child node or no child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # node with two child
            successor = self.findMin(root.right)

            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)

        return root
    
    def findMin(self, node: TreeNode):
        while node.left:
            node = node.left
        return node
        

        


# Example Usage
# Example tree:
#       5
#      / \
#     3   6
#    / \   \
#   2   4   7

root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2), TreeNode(4))
root.right = TreeNode(6, None, TreeNode(7))

sol = Solution()
# Delete node with key 3
new_root = sol.deleteNode(root, 3)

def print_tree(node, prefix="", is_left=True):
    if node is not None:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

# After deleting node
print_tree(new_root)