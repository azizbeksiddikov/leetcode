# Link: https://leetcode.com/problems/reverse-linked-list
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

# values = [0, 1, 2, 3]  # [3,2,1,0]

# Build a linked list for local testing.
# dummy = ListNode()
# tail = dummy
# for value in values:
#     tail.next = ListNode(value)
#     tail = tail.next

# reversed_head = Solution().reverseList(dummy.next)

# # Collect values back to a Python list for readable output.
# result = []
# curr = reversed_head
# while curr:
#     result.append(curr.val)
#     curr = curr.next

# print(result)
#  O(n) time and O(1) space, where n is the length of the given list.
