# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

  def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = fast.next

        prev = None
        current = slow.next

        while current:
            next = current.next
            current.next = prev

            prev = current
            current = next
        
        max_sum = 0

        while fast and head:

            sum = head.val + fast.val

            if sum > max_sum:
                max_sum = sum

            head = head.next
            fast = fast.next

        return max_sum
    
# Example usage:
# Creating a linked list: 5 -> 4 -> 2 -> 1
head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
solution = Solution()
print(solution.pairSum(head))  # Output: 6