// https://leetcode.com/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=leetcode-75
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function reverseList(head: ListNode | null): ListNode | null {
  return reverseIterative(head, null);
}

function reverse(
  current: ListNode | null,
  prev: ListNode | null
): ListNode | null {
  if (current === null) {
    return prev;
  }
  const next = current.next;
  current.next = prev;
  return reverse(next, current);
}

function reverseIterative(
  current: ListNode | null,
  prev: ListNode | null
): ListNode | null {
  while (current) {
    const next = current.next;
    current.next = prev;

    prev = current;
    current = next;
  }

  return prev;
}

// Example usage:
const list = new ListNode(
  1,
  new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))
);
const reversedList = reverseList(list);
let node: ListNode | null = reversedList;
const result: number[] = [];
while (node !== null) {
  result.push(node.val);
  node = node.next;
}
console.log(result); // Output: [5, 4, 3, 2, 1]
