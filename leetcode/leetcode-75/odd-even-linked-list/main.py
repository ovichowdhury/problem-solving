# https://leetcode.com/problems/odd-even-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = head
        even_head = head.next if head else None

        odd = odd_head
        even = even_head

        while odd and even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        if odd:
            odd.next = even_head

        return odd_head
    
# Example usage:
# Constructing the linked list 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
solution = Solution()
new_head = solution.oddEvenList(head)
# Printing the modified linked list
current = new_head
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next 