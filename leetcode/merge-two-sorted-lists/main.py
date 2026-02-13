# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        
        current.next = list1 if list1 else list2

        return dummy.next


# Example Usage
if __name__ == "__main__":
    sol = Solution()
    # Create list1: 1 -> 2 -> 4
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    
    # Create list2: 1 -> 3 -> 4
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    
    merged_list = sol.mergeTwoLists(list1, list2)
    
    # Print merged list
    current = merged_list
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # Expected output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

    # Example 2: list1 = [], list2 = []
    merged_list = sol.mergeTwoLists(None, None)
    print("\nExample 2 Output:", end=" ")
    current = merged_list
    if not current:
        print([])
    else:
        vals = []
        while current:
            vals.append(current.val)
            current = current.next
        print(vals)

    # Example 3: list1 = [], list2 = [0]
    merged_list = sol.mergeTwoLists(None, ListNode(0))
    print("Example 3 Output:", end=" ")
    current = merged_list
    if not current:
        print([])
    else:
        vals = []
        while current:
            vals.append(current.val)
            current = current.next
        print(vals)

    