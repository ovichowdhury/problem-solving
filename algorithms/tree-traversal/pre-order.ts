import BinaryTree, { Node } from "../../data-structures/tree/binary-tree";

const bTree = new BinaryTree();

bTree.insert(1);
bTree.insert(2);
bTree.insert(3);
bTree.insert(4);
bTree.insert(5);
bTree.insert(6);
bTree.insert(7);
bTree.insert(8);

function preOrderRecursive(root: Node | null): void {
  if (root !== null) {
    console.log(root.data);
    preOrderRecursive(root.left);
    preOrderRecursive(root.right);
  }
}

function preOrderStack(root: Node | null): void {
  const stack: Node[] = [];
  while (1) {
    while (root !== null) {
      console.log(root.data);
      stack.push(root);
      root = root.left;
    }
    if (stack.length === 0) break;
    const lastNode = stack.pop();
    if (lastNode) root = lastNode;
    root = root!.right;
  }
}

preOrderRecursive(bTree.root);
console.log("============================");
preOrderStack(bTree.root);
