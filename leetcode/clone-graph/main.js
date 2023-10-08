// Problem: https://leetcode.com/problems/clone-graph/

/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function (node) {
  const map = new Map();
  const dfs = (n) => {
    if (map.get(n)) return map.get(n);
    const newNode = new Node(n.val);
    map.set(n, newNode);
    for (let nei of n.neighbors) newNode.neighbors.push(dfs(nei));
    return newNode;
  };
  return node ? dfs(node) : null;
};
