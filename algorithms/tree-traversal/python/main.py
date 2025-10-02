
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder(node: TreeNode):
    if node is None:
        return
    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)

def inorder(node: TreeNode):
    if node is None:
        return
    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)

def postorder(node: TreeNode):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=" ")

# Example Usage
root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')

preorder(root)
print()
inorder(root)
print()
postorder(root)