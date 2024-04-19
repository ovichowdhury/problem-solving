import BinaryTree, { Node } from "../../data-structures/tree/binary-tree";

const bTree = new BinaryTree();

bTree.insert(1);
bTree.insert(2);
bTree.insert(3);
bTree.insert(4);
bTree.insert(5);
bTree.insert(6);
bTree.insert(7);

function postOrderRecursive(root: Node | null) {
  if (root !== null) {
    postOrderRecursive(root.left);
    postOrderRecursive(root.right);
    console.log(root.data);
  }
}

postOrderRecursive(bTree.root);
