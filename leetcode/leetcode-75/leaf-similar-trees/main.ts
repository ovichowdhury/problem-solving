// https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75

class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

// Time Complexity: O(N + M), where N and M are the number of nodes in root1 and root2 respectively.
// Space Complexity: O(H + L), where H is the maximum height of the trees and L is the number of leaves.
function leafSimilar(root1: TreeNode | null, root2: TreeNode | null): boolean {
  return (
    getLeafSequence(root1).toString() === getLeafSequence(root2).toString()
  );
}

function getLeafSequence(root: TreeNode | null): number[] {
  const leaves: number[] = [];
  const stack: (TreeNode | null)[] = [root];

  while (stack.length > 0) {
    const node = stack.pop();
    if (node) {
      if (!node.left && !node.right) {
        leaves.push(node.val);
      }
      if (node.left) stack.push(node.left);
      if (node.right) stack.push(node.right);
    }
  }

  return leaves;
}

// Example Usage
const tree1 = new TreeNode(
  3,
  new TreeNode(
    5,
    new TreeNode(6),
    new TreeNode(2, new TreeNode(7), new TreeNode(4))
  ),
  new TreeNode(1, new TreeNode(9), new TreeNode(8))
);

const tree2 = new TreeNode(
  3,
  new TreeNode(5, new TreeNode(6), new TreeNode(7)),
  new TreeNode(
    1,
    new TreeNode(4),
    new TreeNode(2, new TreeNode(9), new TreeNode(8))
  )
);

console.log(leafSimilar(tree1, tree2)); // Output: true
