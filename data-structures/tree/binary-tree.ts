export class Node {
  public data: number;
  public left: Node | null;
  public right: Node | null;

  constructor(value: number) {
    this.data = value;
    this.left = null;
    this.right = null;
  }
}

export default class BinaryTree {
  public root: Node | null;
  constructor(root: Node | null = null) {
    this.root = root;
  }

  public insert(value: number) {
    const node = new Node(value);
    if (this.root === null) this.root = node;
    else this.insertHelper(node);
  }

  private insertHelper(newNode: Node) {
    const queue = [this.root];
    while (queue.length > 0) {
      const currentNode = queue.shift();
      if (currentNode?.left === null) {
        currentNode.left = newNode;
        break;
      }
      if (currentNode?.right === null) {
        currentNode.right = newNode;
        break;
      }
      if (currentNode?.left) queue.push(currentNode.left);
      if (currentNode?.right) queue.push(currentNode.right);
    }
  }
}
