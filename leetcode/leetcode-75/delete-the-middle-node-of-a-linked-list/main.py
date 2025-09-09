# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to print the linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return None
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = slow.next

        return head
    
# Example usage:
head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))

print("Original linked list:")
print_linked_list(head)

solution = Solution()
new_head = solution.deleteMiddle(head)

print("Linked list after deleting middle node:")
print_linked_list(new_head)