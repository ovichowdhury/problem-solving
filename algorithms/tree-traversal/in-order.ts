import BinaryTree, { Node } from "../../data-structures/tree/binary-tree";

const bTree = new BinaryTree();

bTree.insert(1);
bTree.insert(2);
bTree.insert(3);
bTree.insert(4);
bTree.insert(5);
bTree.insert(6);
bTree.insert(7);

function inOrderRecursive(root: Node | null): void {
  if (root !== null) {
    inOrderRecursive(root.left);
    console.log(root.data);
    inOrderRecursive(root.right);
  }
}

function inOrderStack(root: Node | null): void {
  const stack: Node[] = [];
  while (1) {
    while (root !== null) {
      stack.push(root);
      root = root.left;
    }
    if (stack.length === 0) break;
    const lastNode = stack.pop();
    console.log(lastNode?.data);
    if (lastNode) root = lastNode;
    root = root!.right;
  }
}

inOrderRecursive(bTree.root);
console.log("============================");
inOrderStack(bTree.root);
