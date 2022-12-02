// problem: https://leetcode.com/problems/add-two-numbers/

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

function printList(l) {
  while (l !== null) {
    process.stdout.write(l.val.toString());
    l = l.next;
  }
}

function toLinkedList(arr) {
  let head = new ListNode(arr[0]);
  for (let i = 1; i < arr.length; i++) {
    let current = head;
    while (current.next !== null) {
      current = current.next;
    }
    current.next = new ListNode(arr[i]);
  }
  return head;
}

function toArr(l) {
  const arr = [];
  while (l !== null) {
    arr.push(l.val);
    l = l.next;
  }
  return arr;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  const a1 = toArr(l1);
  const a2 = toArr(l2);
  let num1 = BigInt(a1.reverse().join(""));
  let num2 = BigInt(a2.reverse().join(""));
  let sum = num1 + num2;
  sum = sum
    .toString()
    .split("")
    .reverse()
    .map((n) => parseInt(n));

  return toLinkedList(sum);
};

printList(
  addTwoNumbers(
    toLinkedList([
      1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 1,
    ]),
    toLinkedList([5, 6, 4])
  )
);
