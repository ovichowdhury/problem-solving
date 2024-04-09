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

function traverseLevelOrder(root: TreeNode) {
  const arr: number[] = [];
  const queue: TreeNode[] = [root];
  while (queue.length > 0) {
    const currentNode = queue.shift();
    if (currentNode) arr.push(currentNode?.val);
    if (currentNode?.left) queue.push(currentNode.left);
    if (currentNode?.right) queue.push(currentNode.right);
  }
  console.log(arr);
}

function invertTree(root: TreeNode | null): TreeNode | null {
  function invert(node: TreeNode | null) {
    if (!node) return;
    const tmp: TreeNode | null = node.left;
    node.left = node.right;
    node.right = tmp;
    invert(node.left);
    invert(node.right);
  }
  if (root) invert(root);
  return root;
}

let _root: TreeNode | null = new TreeNode(
  4,
  new TreeNode(2, new TreeNode(1), new TreeNode(3)),
  new TreeNode(7, new TreeNode(6), new TreeNode(9))
);

traverseLevelOrder(_root);

_root = invertTree(_root);

traverseLevelOrder(_root!);
